# Resume Optimizer v2

A resume audit & optimization skill for AI coding assistants (Trae, Codex, Claude Code, etc.).

It does one thing well: turns ordinary, job-description-style resumes into high-impact, results-driven career documents.

## What's new in v2 (v1.1.0)

- **Multi-language support** — auto-detects resume language; outputs in English or Chinese accordingly
- **ATS compatibility checklist** — `references/ats-checklist.md` covers keyword density, section naming, format traps, and self-verification steps
- **Iterative feedback loop** — Step 6.5 asks for user review after each draft rewrite
- **Structured 30-second diagnostic** — first impression / fatal flaw / hidden gem template
- **Soft-skill evidence framework** — transforms vague "good communication" into concrete behavioral evidence
- **One-page reverse guidance** — when NOT to compress (15+ yr senior roles, academic CVs, etc.)
- **Expanded red flags** — AI-generated content detection, education inflation, over-optimization risks
- **Chinese agent interface** — `agents/openai.yaml` localized
- **Sample resumes** — `examples/` with before/after pairs in both English and Chinese
- **Version tracking** — `SKILL.md` frontmatter includes `version: "1.1.0"`

## What it solves

- Finds the most damaging issues in your resume, not vague suggestions
- Rewrites "responsible for" into "delivered X, resulting in Y"
- Digs out quantified results, business value, and actual deliverables
- Adjusts keywords and project emphasis based on target job descriptions
- Generates a polished rewrite draft you can continue editing
- Compresses multi-page resumes into one page (when appropriate)
- Identifies outsourcing stints, toy projects, missing metrics, AI-generated phrasing, and other red flags

## Project structure

```
resume-optimizer-v2/
├── README.md
├── LICENSE
├── SKILL.md
├── agents/
│   └── openai.yaml
├── examples/
│   ├── sample-before-cn.md
│   ├── sample-after-cn.md
│   ├── sample-before-en.md
│   └── sample-after-en.md
└── references/
    ├── audit-checklist.md
    ├── narrative-tools.md
    ├── one-page-resume.md
    ├── red-flags.md
    └── ats-checklist.md
```

## Installation

### Trae

```bash
mkdir -p .trae/skills
git clone https://github.com/elviswong1013/resume-optimizer-v2.git .trae/skills/resume-optimizer
```

### Codex

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/elviswong1013/resume-optimizer-v2.git ~/.codex/skills/resume-optimizer
```

### Claude Code

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/elviswong1013/resume-optimizer-v2.git ~/.claude/skills/resume-optimizer
```

### Manual

Copy the entire directory into your skills folder. At minimum, keep:

- `SKILL.md`
- `references/`
- `agents/openai.yaml`

## Usage

Explicit invocation:

```text
Use $resume-optimizer to audit my resume for a senior backend role.
```

Natural language triggers:

```text
请帮我审计这份简历，并按高级后端工程师 JD 优化重点。
```

```text
Turn this project experience from duty-based into achievement-based. Don't fabricate data.
```

```text
Compress this 2-page resume into one page, keeping only my strongest results.
```

## Output style

This skill produces:

1. 30-second verdict
2. Key issues list
3. Value extraction & quantification gaps
4. Rewrite strategy
5. Revised resume snippets or full draft
6. One-page version confirmation prompt
7. Action checklist

## Suitable scenarios

- Tech role resumes (mid to senior level)
- Campus hire project description refinement
- Pre-application JD-tailored customization
- Compressing 2+ page resumes to one page
- Pre-interview resume audit
- Outsourcing, career switch, or gap-period narrative repair

## Credits

Originally created by [wyh0626](https://github.com/wyh0626/resume-optimizer).  
v2 enhancements by [elviswong1013](https://github.com/elviswong1013).
