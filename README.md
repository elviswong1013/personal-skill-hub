# Personal Skill Hub

A personal collection of high-quality agent skills designed for portability across coding agents — Claude Code, Cursor, Codex CLI, Trae IDE, and more. Each skill is self-contained under `skills/` with a standardized hierarchical structure.

## Repository Structure

```
personal-skill-hub/
├── skills/
│   ├── skill-refiner/                   # Meta-skill for auditing and improving skills
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   ├── references/
│   │   └── assets/
│   ├── resume-optimizer/                # Resume ATS + narrative optimization
│   │   ├── SKILL.md
│   │   ├── agents/
│   │   ├── examples/
│   │   └── references/
│   ├── travel-wiki-builder/             # Travel wiki + PPT/MD/HTML plans
│   │   ├── SKILL.md
│   │   └── references/
│   └── skill-hub-manager/               # Bidirectional GitHub sync for skills
│       ├── SKILL.md
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

Refines existing skills by removing bad design features and adding good ones. Invoke when a skill needs improvement, triggers incorrectly, is too long/short, is too rigid, or has received feedback indicating it underperforms.

**What it does:**
- Diagnoses skills across 5 categories of bad design (18 anti-patterns)
- Scores skills on 10 quality dimensions
- Proposes dual-direction refinements (remove bad + add good)
- Iterates across rounds driven by feedback, evaluation, and testing
- Includes structural validator + behavioral verification scenarios

### resume-optimizer

Optimizes resumes with ATS compliance, narrative improvement, and professional formatting.

**What it does:**
- Audits resumes against ATS and red-flag checklists
- Applies narrative tools to strengthen impact
- Produces reformatted output with before/after comparisons
- Supports Chinese and English resumes

### travel-wiki-builder

Builds llm-wiki 6-layer knowledge bases for any travel destination and outputs PPT/MD/HTML travel plans.

**What it does:**
- Searches and collects travel data across 6 topics
- Builds raw → source → entity → concept → wiki → history layers
- Outputs 19-section Markdown, dark-theme HTML, and 16:9 PPTX plans
- Adapts to destination type (ring-road / single-city / multi-city)
- Includes verification scenarios and safety content requirements

### skill-hub-manager

Manages a personal skill hub on GitHub — import, push, pull, and organize skills under a standardized skills/ directory with bidirectional sync.

**What it does:**
- 5 operations: init hub, import skill, push, pull/install, list inventory
- Bidirectional sync between projects and GitHub
- Auto-maintains README with current skill inventory
- Optional `--validate` flag for pre-push quality checks
- Ask Before Change guardrail for all destructive operations
- Multi-repo and multi-agent support

## Installation

This hub is framework-agnostic. Clone the repo and copy desired skills into your agent's skills folder.

```bash
git clone https://github.com/elviswong1013/personal-skill-hub.git
```

### Trae IDE

```bash
cp -r personal-skill-hub/skills/skill-refiner .trae/skills/skill-refiner
```

### Claude Code

```bash
# Project-level
cp -r personal-skill-hub/skills/skill-refiner .claude/skills/skill-refiner

# Global
cp -r personal-skill-hub/skills/skill-refiner ~/.claude/skills/skill-refiner
```

### Cursor

```bash
cp -r personal-skill-hub/skills/skill-refiner .cursor/rules/skill-refiner
```

### OpenAI Codex CLI

```bash
cp -r personal-skill-hub/skills/skill-refiner .codex/skills/skill-refiner
```

## Usage

Each skill triggers automatically when its conditions are met. You can also invoke explicitly:

- "Refine the code-reviewer skill"
- "Score my skills using the scorecard"
- "Push this skill to my hub"
- "Build a travel wiki for Tokyo"

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

5. Use `skill-hub-manager` to push it to GitHub — the README updates automatically.

## Requirements

- Python 3.7+ with `pyyaml` — only needed for the structural validator in `skill-refiner`
- All skills work with any agent that supports a file-based skill directory
