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

1. **Copy the skill directory** into your project's `.trae/skills/` folder:

   ```bash
   # From within your project directory
   mkdir -p .trae/skills/
   cp -r path/to/skill-refiner .trae/skills/skill-refiner
   ```

2. **Install the Python dependency** for the structural validator (optional — the skill works without it):

   ```bash
   pip install pyyaml
   ```

3. **Verify the installation** by running the validator against itself:

   ```bash
   python .trae/skills/skill-refiner/scripts/validate-skill-structure.py .trae/skills/skill-refiner
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
- The skill itself (SKILL.md + supporting files) works with any agent that follows `.trae/skills/` conventions
