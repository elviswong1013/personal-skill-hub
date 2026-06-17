---
name: "skill-hub-manager"
description: "Manages a personal skill hub on GitHub — import, push, pull, and organize skills under a standardized skills/ directory with bidirectional sync. Invoke when the user wants to save a skill to their hub, push/pull skills, or set up a new hub. DO NOT invoke for creating or refining individual skills — use skill-creator or skill-refiner for that."
---

# Skill Hub Manager

Manages a personal collection of agent skills stored on GitHub under a standardized `skills/{name}/` hierarchy. Supports bidirectional sync — push skills from projects to the hub, pull skills from the hub into projects — across multiple GitHub repositories.

## When to Invoke

- User wants to save a skill from a project to their personal skill hub
- User wants to push hub changes to GitHub
- User wants to pull or install skills from their hub into a new project
- User wants to set up a new skill hub repository
- User mentions "push to my skill hub", "add this skill to my collection", "sync my skills"
- User wants to list or browse skills in their hub

## When NOT to Invoke

- Creating a brand-new skill from scratch — use `skill-creator`
- Refining or auditing an existing skill — use `skill-refiner`
- Regular git operations on a non-skill-hub repository
- User only wants to browse skills conceptually without making changes
- User is working with agent-specific skill directories directly (`.trae/skills/` etc.) without wanting hub management

## Core Principle: Ask Before Change

**Every operation that modifies the hub or a project must be confirmed by the user before execution.** This includes:

- Importing a skill (which file goes where)
- Pushing to GitHub (which commits, which remote)
- Pulling into a project (which target directory, which agent)
- Initializing a new hub (directory path, repo name)
- Deleting or overwriting an existing skill

Present a clear summary of what will happen, then ask. Do not proceed without explicit approval.

## Core Principle: Auto-Maintain README

**The hub's README.md must always reflect the current skill inventory.** After any operation that adds, removes, or renames a skill, regenerate the README:

1. **Scan `skills/`** — list all subdirectories. For each, read `SKILL.md` and extract the `description` from YAML frontmatter.
2. **Rebuild the Available Skills section** — for each skill, include its name, extracted description, and a brief summary of what it does (from the SKILL.md intro paragraph).
3. **Update the Repository Structure tree** — reflect the current set of skills.
4. **Preserve hand-written sections** — Installation, Usage, Adding New Skills, and Requirements sections are template content; keep them intact. Only regenerate the "Available Skills" section and the structure diagram.
5. **Stage README.md alongside the skill changes** — commit it in the same commit as the import/removal, or as a follow-up commit with a message like "Update README with skill inventory".

This ensures the hub is self-documenting: cloning the repo and reading the README gives a complete picture of what's inside.

## Workflow

### Operation 1: Initialize a Hub

When the user wants to create a new skill hub:

1. **Confirm the path** — where on disk the hub should live, and whether it's a new directory or an existing one to convert.
2. **Create the structure** — set up `skills/` directory, copy the `.gitignore` template from `assets/.gitignore-template`, create a minimal README.
3. **Initialize git** — if not already a git repository.
4. **Ask for remote details** — GitHub username, repo name, token if available. If the user provides a token, attempt to create the remote repo. If not, instruct the user to create it manually.
5. **Confirm**: "Initialize hub at `{path}` with remote `{user}/{repo}`. Proceed?"

### Operation 2: Import a Skill Into the Hub

When the user wants to add a skill from a project to their hub:

1. **Locate the source skill** — read its `SKILL.md` to confirm it's a valid skill. The source may be under any agent directory (`.trae/skills/`, `.claude/skills/`, `.cursor/rules/`, etc.).
2. **Detect conflicts** — check if a skill with the same name already exists in `skills/`. If so, ask whether to overwrite, skip, or import under a different name.
3. **Present the import plan**: "Import `{skill-name}` from `{source-path}` → `skills/{skill-name}/`. Contains `{n}` files. Proceed?"
4. **Copy the skill** — recursively copy the entire skill directory into `skills/{skill-name}/`, preserving all subdirectories.
5. **Regenerate README** — scan `skills/`, rebuild the "Available Skills" section and structure diagram. Stage README.md.
6. **Stage the change** — git add the new skill directory and README.md.

### Operation 3: Push to GitHub

When the user wants to push hub changes:

1. **Review uncommitted changes** — check git status. If nothing to push, report and stop.
2. **Show what will be pushed**: "Pushing to `{remote}`. Commits: `{list}`. Files changed: `{count}`. Proceed?"
3. **Optional validation** — if the user requested `--validate`, run skill-refiner's structure validator on newly added or modified skills. Report issues and ask whether to push anyway if validation fails.
4. **Commit if needed** — if there are unstaged changes, ask for a commit message or generate one summarizing the skills being added.
5. **Push** — authenticate using the available credential method (git credential manager, embedded token, or prompt for credentials).

### Operation 4: Pull / Install Skills Into a Project

When the user wants to bring skills from the hub into a project:

1. **Determine the target agent** — ask which agent the project uses (Trae, Claude Code, Cursor, Codex, or custom). Map to the correct target directory (see `references/hub-structure.md`).
2. **Select skills** — if the user specified specific skills, use those. Otherwise, show the hub inventory and ask which skills to install.
3. **Detect conflicts** — check if skills with the same names already exist in the target project. If so, ask whether to overwrite or skip each one.
4. **Present the pull plan**: "Install `{skill-list}` from hub → `{target-dir}/`. Proceed?"
5. **Copy skills** — copy each selected skill directory into the target agent's skills directory.
6. **Confirm completion** — list what was installed and where.

### Operation 5: List Hub Inventory

When the user wants to see what's available:

1. **Scan `skills/`** — list all subdirectories.
2. **Read each SKILL.md** — extract the `name` and `description` from YAML frontmatter.
3. **Present a summary table**: skill name, description, agent targets supported.

### Validation (Optional --validate Flag)

When the user appends `--validate` to a push or import operation:

- Run the structure validator against the target skill(s)
- Report word count range, frontmatter validity, optional directory integrity
- If validation produces errors: show them and ask whether to proceed anyway
- If validation produces warnings only: show them and proceed with confirmation
- Do NOT block the operation silently — always present findings and let the user decide

## Managing Multiple Hubs

The skill supports multiple hub repositories. When the user has more than one:

- **Track the active hub** — the hub in the current working directory is the default target for push/pull operations.
- **Switch hubs** — if the user mentions a different hub, locate it on disk or clone it if missing.
- **Cross-hub import** — a skill can be imported from one hub to another by specifying both paths.

## References Directory

- `hub-structure.md`: Standard hub directory layout, skill directory contract, and agent-to-directory mapping table. Consult when initializing a hub or pulling skills into a project.

## Assets Directory

- `.gitignore-template`: Template `.gitignore` for new skill hubs. Copy into the hub root during initialization.

## Verification Scenarios

### Scenario A: Import and Push

**Setup**: A skill exists at `.trae/skills/my-skill/SKILL.md`. Hub is initialized at `~/personal-skill-hub`.

**Expected**: Import copies the skill to `skills/my-skill/`. User confirms. Push attempts git push to the configured remote. If remote is unreachable, the error is reported clearly.

### Scenario B: Pull Into a Project

**Setup**: Hub has 3 skills. User is in a Trae IDE project.

**Expected**: User selects skills to install. Skills are copied to `.trae/skills/`. Pre-existing skills with name conflicts trigger an overwrite/skip prompt.

### Scenario C: Conflict Detection

**Setup**: User imports `skill-refiner` but `skills/skill-refiner/` already exists.

**Expected**: User is prompted: overwrite, skip, or rename. Operation does not proceed without an explicit choice.
