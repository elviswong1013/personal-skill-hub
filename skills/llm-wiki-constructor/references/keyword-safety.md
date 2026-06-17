# Keyword Safety Rules

Rules for processing confirmed keywords into pages and wikilinks.

## Rule 1: Process by Priority Order

Process in descending priority order. The sort output puts longer terms first — creating `[[Claude Code]]` before `[[Claude]]` prevents substring interference. When inserting wikilinks for a shorter overlapping term, match only bare text occurrences. Never match text already inside `[[...]]` brackets — doing so would break `[[Claude Code]]` into `[[[[Claude]] Code]]`.

## Rule 2: Sanitize Filenames

Replace invalid filename characters (`/`, `\`, `:`, `*`, `?`, `<`, `>`, `|`, `"`) with `-`. Collapse multiple dashes. E.g., `C#` → `c-sharp`.

## Rule 3: Deduplicate Case-Insensitively

If "Claude" and "CLAUDE" both appear, keep one. Confirm the casing with the user if ambiguous.

## Rule 4: Resolve Entity/Concept Ambiguity

If the same term appears on both lists, ask the user which layer it belongs to. Do not create it in both.
