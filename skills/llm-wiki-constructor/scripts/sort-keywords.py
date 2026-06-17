"""
Keyword Priority Sorter for llm-wiki-constructor

Sorts entity and concept keywords by priority so that more significant
terms get wikilinks and pages first. Supports three scoring modes.

Modes:
  specificity  (default)  Multi-word terms first, then longer terms, then alphabetical.
                          Best for: repositories where compound terms are inherently
                          more important (e.g., technical or academic topics).
  frequency               Most frequent keywords first (requires occurrence count).
                          Best for: topic surveys where prevalence signals importance.
  composite               Weighted blend of specificity + frequency.
                          Best for: balanced importance assessment.

Input format:
  - One keyword per line for 'specificity' mode.
  - "keyword<TAB>count" per line for 'frequency' or 'composite' modes.
    Lines without a tab get a default count of 1.

Usage:
    python sort-keywords.py --mode specificity keywords.txt
    python sort-keywords.py --mode frequency --check-overlaps keywords.txt
    echo -e "claude\t15\nclaude code\t8\nanthropic\t3" | python sort-keywords.py --mode composite

Options:
    --mode MODE          specificity (default), frequency, or composite
    --check-overlaps     Print warnings for substring containment pairs (stderr)
"""

import sys


def priority_key_specificity(keyword: str) -> tuple:
    """(-word_count, -char_length, lowercase_term)."""
    words = keyword.strip().split()
    return (-len(words), -len(keyword.strip()), keyword.strip().lower())


def priority_key_frequency(keyword: str, count: int) -> tuple:
    """(-count, -char_length, lowercase_term)."""
    return (-count, -len(keyword.strip()), keyword.strip().lower())


def priority_key_composite(keyword: str, count: int) -> tuple:
    """Composite: word_count * 0.4 + normalized_freq * 0.4 + char_length_normalized * 0.2.
    
    This balances specificity (multi-word terms) with real-world prevalence (frequency)
    and term richness (length). All three are negated for descending sort.
    """
    word_count = len(keyword.strip().split())
    char_len = len(keyword.strip())
    # Use count directly as the frequency weight; caller normalizes if desired
    freq_weight = count
    # Composite: word_count * 10 (boost multi-word), + freq, + char_len * 0.3
    score = word_count * 10 + freq_weight + char_len * 0.3
    return (-score, keyword.strip().lower())


def sort_keywords(keywords: list[str], mode: str = "specificity",
                  counts: dict[str, int] | None = None) -> list[str]:
    """Sort keywords by the given mode."""
    if mode == "frequency":
        def key(kw):
            c = counts.get(kw.strip().lower(), 1) if counts else 1
            return priority_key_frequency(kw, c)
    elif mode == "composite":
        def key(kw):
            c = counts.get(kw.strip().lower(), 1) if counts else 1
            return priority_key_composite(kw, c)
    else:
        key = priority_key_specificity

    return sorted(keywords, key=key)


def detect_overlaps(keywords: list[str]) -> list[tuple[str, str]]:
    """Find pairs where one keyword is a case-insensitive substring of another.
    
    Returns list of (container, contained) tuples sorted by container length desc.
    Only checks unique keywords (case-insensitive dedup applied first).
    """
    seen = {}
    unique = []
    for kw in keywords:
        lower = kw.strip().lower()
        if lower not in seen:
            seen[lower] = kw.strip()
            unique.append(kw.strip())

    overlaps = []
    for i, outer in enumerate(unique):
        outer_lower = outer.lower()
        for j, inner in enumerate(unique):
            if i == j:
                continue
            inner_lower = inner.lower()
            if inner_lower != outer_lower and inner_lower in outer_lower:
                overlaps.append((outer, inner))

    overlaps.sort(key=lambda p: (-len(p[0]), -len(p[1])))
    return overlaps


def parse_args(argv: list[str]) -> tuple[list[str], bool, str]:
    """Parse command-line arguments. Returns (positional_args, check_overlaps, mode)."""
    check_overlaps = False
    mode = "specificity"
    positional = []
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == '--check-overlaps':
            check_overlaps = True
        elif arg == '--mode':
            i += 1
            if i < len(argv) and argv[i] in ('specificity', 'frequency', 'composite'):
                mode = argv[i]
            else:
                print(f"Invalid mode: {argv[i] if i < len(argv) else '(missing)'}. "
                      f"Use: specificity, frequency, composite.", file=sys.stderr)
                sys.exit(1)
        else:
            positional.append(arg)
        i += 1
    return positional, check_overlaps, mode


def parse_keywords(lines: list[str]) -> tuple[list[str], dict[str, int]]:
    """Parse keyword lines. Lines may be 'keyword' or 'keyword<TAB>count'.
    Returns (keywords in input order, lowercase->count dict)."""
    keywords = []
    counts = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if '\t' in line:
            parts = line.split('\t', 1)
            kw = parts[0].strip()
            try:
                cnt = int(parts[1].strip())
            except ValueError:
                cnt = 1
        else:
            kw = line
            cnt = 1

        keywords.append(kw)
        lower = kw.lower()
        counts[lower] = max(counts.get(lower, 0), cnt)

    return keywords, counts


def main():
    args, check_overlaps, mode = parse_args(sys.argv[1:])

    if args:
        with open(args[0], 'r', encoding='utf-8') as f:
            raw_lines = [line.rstrip('\n') for line in f if line.strip()]
    else:
        raw_lines = [line.rstrip('\n') for line in sys.stdin if line.strip()]

    if not raw_lines:
        print("No keywords provided.", file=sys.stderr)
        sys.exit(1)

    keywords, counts = parse_keywords(raw_lines)
    sorted_keywords = sort_keywords(keywords, mode=mode, counts=counts)

    if check_overlaps:
        overlaps = detect_overlaps(keywords)
        if overlaps:
            print("[WARN] Overlapping keyword pairs detected:", file=sys.stderr)
            for container, contained in overlaps:
                print(f"  \"{container}\" contains \"{contained}\" — "
                      f"process \"{container}\" first to avoid substring interference.",
                      file=sys.stderr)
            print("", file=sys.stderr)
        else:
            print("[OK] No overlapping keyword pairs found.", file=sys.stderr)

    if mode in ('frequency', 'composite') and counts:
        print(f"[INFO] Mode: {mode}. Counts loaded for {len(counts)} unique keywords.",
              file=sys.stderr)

    for kw in sorted_keywords:
        print(kw)


if __name__ == '__main__':
    main()
