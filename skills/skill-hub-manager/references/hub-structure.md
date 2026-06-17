# Skill Hub Structure

Each skill hub follows this layout. The hub itself is a git repository — skills are subdirectories under `skills/`.

```text
{hub-name}/
├── skills/
│   ├── skill-one/
│   │   ├── SKILL.md              # Required: governance file with YAML frontmatter
│   │   ├── scripts/              # Optional: executable helpers
│   │   ├── references/           # Optional: domain knowledge, guides
│   │   └── assets/               # Optional: templates, output examples
│   └── skill-two/
│       └── ...
├── .gitignore
└── README.md                     # Hub index listing all skills
```

## Skill Directory Contract

Every skill under `skills/` must follow this minimum contract:

- `SKILL.md` exists at the root of the skill directory
- `SKILL.md` has valid YAML frontmatter with `name` and `description`
- Optional directories (`scripts/`, `references/`, `assets/`) are not empty (no dead directories)

## Hub Discovery

The hub is self-documenting: scanning `skills/` produces the complete skill inventory. No separate registry file is required — the filesystem is the registry.

## Supported Agent Targets

When pulling skills FROM the hub INTO a project, copy to the appropriate agent directory:

| Agent | Target Directory |
|---|---|
| Trae IDE | `.trae/skills/` |
| Claude Code | `.claude/skills/` |
| Cursor | `.cursor/rules/` |
| Codex CLI | `.codex/skills/` |
| Generic | `{AGENT}/skills/` |
