"""
Skill Structure Validator

Validates that a skill directory under .trae/skills/ follows the expected
hierarchical structure. Run this script to mechanically verify layout before
beginning manual refinement.

Usage:
    python validate-skill-structure.py <path-to-skill-directory>

Outputs:
    - A pass/fail report for structural checks.
    - Word count of the SKILL.md body (excluding YAML frontmatter).

Checks performed:
    1. SKILL.md exists and is non-empty.
    2. SKILL.md has valid YAML frontmatter with 'name' and 'description' fields.
    3. SKILL.md body word count is within 500-2000 (warning only; not a hard fail).
    4. Optional directories (scripts/, references/, assets/) are properly referenced
       in SKILL.md if they contain files.
    5. No empty directories in the optional folders.
"""

import os
import sys
import re
import yaml


def extract_frontmatter_and_body(content):
    """Extract YAML frontmatter and markdown body from SKILL.md content."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not match:
        return None, content
    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        frontmatter = None
    return frontmatter, match.group(2).strip()


def count_words(text):
    """Count approximate words in text."""
    return len(text.split())


def check_directory_empty(path):
    """Return True if directory exists and is empty (or only contains .gitkeep)."""
    if not os.path.isdir(path):
        return False
    contents = [f for f in os.listdir(path) if f != '.gitkeep']
    return len(contents) == 0


def validate_skill(skill_path):
    """Run all structural checks on a skill directory and print results."""
    errors = []
    warnings = []

    print(f"Validating skill at: {skill_path}\n")

    # 1. SKILL.md exists
    skill_md_path = os.path.join(skill_path, 'SKILL.md')
    if not os.path.isfile(skill_md_path):
        errors.append("SKILL.md not found.")
        return errors, warnings

    # 2. Read and parse
    with open(skill_md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.strip():
        errors.append("SKILL.md is empty.")
        return errors, warnings

    frontmatter, body = extract_frontmatter_and_body(content)

    # 3. Check frontmatter
    if frontmatter is None:
        errors.append("SKILL.md is missing valid YAML frontmatter.")
    else:
        if 'name' not in frontmatter:
            errors.append("Frontmatter missing required field: 'name'.")
        if 'description' not in frontmatter:
            errors.append("Frontmatter missing required field: 'description'.")

    # 4. Word count check (warning only)
    word_count = count_words(body)
    print(f"SKILL.md body word count: {word_count}")
    if word_count < 500:
        warnings.append(f"Body is under 500 words ({word_count}). Consider expanding if content feels sparse.")
    elif word_count > 2000:
        warnings.append(f"Body exceeds 2000 words ({word_count}). Consider trimming redundant sections.")
    else:
        print("Word count is within the recommended 500-2000 range.")

    # 5. Check optional directories
    optional_dirs = ['scripts', 'references', 'assets']
    for dir_name in optional_dirs:
        dir_path = os.path.join(skill_path, dir_name)
        if os.path.isdir(dir_path):
            if check_directory_empty(dir_path):
                warnings.append(f"Directory '{dir_name}/' exists but is empty. Remove it or add content.")
            elif dir_name not in body:
                warnings.append(f"Directory '{dir_name}/' contains files but is not referenced in SKILL.md.")

    # Summary
    print("\n--- Results ---")
    if not errors and not warnings:
        print("All checks passed.")
    for err in errors:
        print(f"[ERROR] {err}")
    for warn in warnings:
        print(f"[WARN]  {warn}")

    return errors, warnings


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python validate-skill-structure.py <path-to-skill-directory>")
        sys.exit(1)

    skill_dir = sys.argv[1]
    if not os.path.isdir(skill_dir):
        print(f"Error: '{skill_dir}' is not a valid directory.")
        sys.exit(1)

    errors, warnings = validate_skill(skill_dir)
    if errors:
        sys.exit(1)
