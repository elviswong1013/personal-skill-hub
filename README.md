# Personal Skill Hub

A personal collection of high-quality agent skills designed for portability across coding agents — Claude Code, Cursor, Codex CLI, Trae IDE, and more. Each skill is self-contained under `skills/` with a standardized hierarchical structure.

## Repository Structure

```
personal-skill-hub/
├── skills/
│   └── skill-refiner/                   # Meta-skill for auditing and improving skills
│       ├── SKILL.md
│       ├── scripts/
│       ├── references/
│       └── assets/
├── .gitignore
└── README.md
```

Each skill follows the same hierarchical convention:

```text
skills/{skill-name}/
├── SKILL.md              # Required: YAML frontmatter + step-by-step instructions
├── scripts/              # Optional: executable helper scripts
├── references/           # Optional: domain knowledge, style guides, API patterns
└── assets/               # Optional: templates, diagrams, output examples
```

## Available Skills

### skill-refiner

A meta-skill for auditing, refining, and improving agent skills. It diagnoses bad design features, identifies missing good ones, and applies a dual-direction refinement — **remove the bad, add the good** — across iterative rounds driven by feedback, evaluation, and testing.

**What it does:**
- Diagnoses skills across 5 categories of bad design (trigger, content, structure, generalization, trust/feedback)
- Scores skills on 10 quality dimensions
- Proposes concrete refinements tagged as "remove bad feature" or "add good feature"
- Validates mechanically (word count, frontmatter, directory integrity) and behaviorally (test scenarios)
- Iterates across rounds, tracking scores and changes in a scorecard

## Installation

This hub is framework-agnostic. To use a skill, copy its directory into your agent's skills folder.

### Trae IDE

```bash
mkdir -p .trae/skills/
cp -r skills/skill-refiner .trae/skills/skill-refiner
```

### Claude Code

```bash
# Project-level
mkdir -p .claude/skills/
cp -r skills/skill-refiner .claude/skills/skill-refiner

# Global
mkdir -p ~/.claude/skills/
cp -r skills/skill-refiner ~/.claude/skills/skill-refiner
```

### Cursor

```bash
mkdir -p .cursor/rules/
cp -r skills/skill-refiner .cursor/rules/skill-refiner
```

### OpenAI Codex CLI

```bash
mkdir -p .codex/skills/
cp -r skills/skill-refiner .codex/skills/skill-refiner
```

### Other Agents

Copy into your agent's skill/rule directory. All files are plain Markdown and Python — no framework-specific APIs.

### Verify (skill-refiner)

Requires Python 3.7+ and `pyyaml`:

```bash
pip install pyyaml
python skills/skill-refiner/scripts/validate-skill-structure.py skills/skill-refiner
```

Expected output: word count within 500–2000 range, all checks passed.

## Usage

Each skill triggers automatically when its conditions are met. You can also invoke explicitly:

- "Refine the code-reviewer skill"
- "Score my skills using the scorecard"
- "This skill triggers too often — tighten it"

## Adding New Skills

1. Create a new directory under `skills/`:

   ```bash
   mkdir -p skills/my-new-skill/{scripts,references,assets}
   ```

2. Create `skills/my-new-skill/SKILL.md` with YAML frontmatter:

   ```markdown
   ---
   name: "my-new-skill"
   description: "What it does. Invoke when X. Do NOT invoke when Y."
   ---
   # My New Skill
   ```

3. Add supporting files in `scripts/`, `references/`, and `assets/` as needed.

4. Use `skill-refiner` to audit and improve it before committing.

## Requirements

- Python 3.7+ with `pyyaml` — only needed for the structural validator in `skill-refiner`
- All skills work with any agent that supports a file-based skill directory
