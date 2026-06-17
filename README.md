# Skill Refiner

A meta-skill for auditing, refining, and improving agent skills. It diagnoses bad design features, identifies missing good ones, and applies a dual-direction refinement — **remove the bad, add the good** — across iterative rounds driven by feedback, evaluation, and testing.

## What It Does

- **Diagnoses** skills across 5 categories of bad design (trigger, content, structure, generalization, trust/feedback) using a comprehensive anti-patterns taxonomy
- **Scores** skills on 10 quality dimensions (trigger precision, intention-driven instructions, self-validation, feedback loops, etc.)
- **Proposes** concrete refinements tagged as "remove bad feature" or "add good feature"
- **Validates** mechanically via a structural checker (word count, frontmatter, directory integrity) and behaviorally via test scenarios
- **Iterates** across rounds, tracking scores, test results, and changes in a scorecard

## Structure

```
skill-refiner/
├── SKILL.md                              # Main governance file (~1,970 words)
├── scripts/
│   └── validate-skill-structure.py       # Mechanical structure + word count validator
├── references/
│   └── skill-anti-patterns.md            # Taxonomy: 18 bad design features across 5 categories
├── assets/
│   └── skill-scorecard.md                # Evaluation template with iteration history tracking
└── README.md
```

## Installation

This skill is framework-agnostic — it works with any coding agent that supports file-based skill/rule systems. The installation path depends on your agent.

### Trae IDE

Copy into `.trae/skills/`:

```bash
mkdir -p .trae/skills/
cp -r path/to/skill-refiner .trae/skills/skill-refiner
```

### Claude Code

Copy into Claude Code's skills directory (project or global):

```bash
# Project-level
mkdir -p .claude/skills/
cp -r path/to/skill-refiner .claude/skills/skill-refiner

# Global (available across all projects)
mkdir -p ~/.claude/skills/
cp -r path/to/skill-refiner ~/.claude/skills/skill-refiner
```

### Cursor

Copy into Cursor's rules directory:

```bash
mkdir -p .cursor/rules/
cp -r path/to/skill-refiner .cursor/rules/skill-refiner
```

### OpenAI Codex CLI

Copy into Codex's project instructions directory:

```bash
mkdir -p .codex/skills/
cp -r path/to/skill-refiner .codex/skills/skill-refiner
```

### Other Agents

Copy into your agent's skill/rule directory. The skill follows the convention `{AGENT_DIR}/skills/skill-refiner/` — adapt the path to match your agent's structure. The SKILL.md and supporting files are plain Markdown and Python; no agent-specific dependencies.

### Python Dependency

Install the optional Python dependency for the structural validator:

```bash
pip install pyyaml
```

### Verify Installation

Run the validator against itself from your project root (adjust the path to match your agent):

```bash
python {SKILLS_DIR}/skill-refiner/scripts/validate-skill-structure.py {SKILLS_DIR}/skill-refiner
```

Expected output: word count within 500–2000 range, all checks passed.

## Usage

The skill triggers automatically when an agent detects a skill needs improvement. You can also invoke it explicitly:

- "Review the code-reviewer skill"
- "This skill triggers too often — refine it"
- "The skill is over 2,500 words, trim it down"

Or drive refinement from specific signals:

- **Feedback-driven**: "The debugger skill runs when I ask about logging — tighten its triggers"
- **Evaluation-driven**: "Score the pdf-generator skill using the scorecard"
- **Testing-driven**: "The validator script reports the skill exceeds 2,000 words"

## Requirements

- **Python 3.7+** with `pyyaml` — only needed for the structural validator script
- The skill itself (SKILL.md + supporting files) works with any agent that supports a file-based skill directory — no framework-specific APIs
