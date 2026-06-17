---
name: "llm-wiki-constructor"
description: "Builds or extends llm-wiki style knowledge repositories. Invoke when the user asks to organize topic materials into raw/source/entity/concept/wiki/history with wikilinks and governance. Do NOT invoke for simple note-taking, single-file documentation, API reference docs, meeting notes, or non-wikilink knowledge bases."
---

# LLM Wiki Constructor

This skill constructs or extends an `llm-wiki` style knowledge repository for a target topic.

## Invoke This Skill When

Use this skill when the user wants to build a new topic knowledge base with a 6-layer structure, reorganize scattered materials into `raw`/`source`/`entity`/`concept`/`wiki`/`history`, prepare for wikilink-based graph navigation, preserve source traceability, or establish merge rules, change logs, and stale-knowledge review rules.

## When NOT to Invoke

Do NOT use for: quick unstructured notes or single documents, API references or linear how-to guides, knowledge bases without wikilinks/graph navigation, meeting notes or personal logs, projects with a non-llm-wiki structure the user is happy with.

## Goals

The skill should produce a repository that preserves traceable source intake in `raw`, synthesizes knowledge into `source`, extracts durable entities into `entity`, extracts stable ideas into `concept`, builds navigable route pages in `wiki`, and records governance and changes in `history`.

### Layer Transformation Logic

Each layer **refines** the previous, never copies it:

- **raw → source**: Distill signal from noise. Combine raw items on the same subtopic into synthesis pages. Drop redundancy, flag contradictions, note what is well-supported vs. weakly-supported.
- **source → entity**: Extract durable, named things. An entity earns its own page by appearing across multiple source pages — not promoted from a single mention.
- **source → concept**: Extract stable, reusable ideas. A concept earns its page by bridging multiple entities or source pages — it has explanatory power beyond one context.
- **entity/concept → wiki**: Build navigation. Wiki pages organize, compare, and route readers through existing pages — they do not add new facts.

## Required Structure

```text
/raw
/source
/entity
/concept
/wiki
/history
index.md
```

### index.md Specification

The root `index.md` serves as the entry point. It should contain: topic name and scope statement, links to key entry pages per directory, repository purpose (survey/handbook/learning-map), and last-updated date. Start from `assets/templates/index.md`.

### history/ File Purposes

- **project-constitution.md**: Records topic scope, repository purpose, language policy, and governing rules. Start from `assets/templates/project-constitution.md`.
- **operations-playbook.md**: Records naming conventions, directory usage, and procedures for common operations (adding raw materials, promoting content, resolving conflicts). Start from `assets/templates/operations-playbook.md`.

## Operating Rules

### Rule 1: Raw First — New material enters `raw` first with metadata and first-pass judgment.

### Rule 2: Compare Before Merge — Compare new material against existing content in all layers before promotion.

### Rule 3: Confirm Before Upward Merge — Summarize new/repeated/conflicting/pending, obtain user confirmation before merging upward.

### Rule 4: Preserve Traceability — `raw` keeps source traceability. Higher layers must be explainable in terms of supporting materials.

### Rule 5: Record History — Every significant restructuring, merge, or removal logged in `history`.

### Rule 6: Use Wikilinks — `[[wikilinks]]` for concepts, entities, and route pages wherever they improve navigation.

## Execution Workflow

### Step 1: Inspect Current State

Inspect whether the repository already exists, whether files are scattered or partially structured, and what language and formatting conventions are already in use.

### Step 2: Define Topic Boundary

Identify the main topic, adjacent subtopics, and whether the repository is a survey, handbook, or learning map.

### Step 3: Initialize Or Normalize Structure

**If the repository does not exist:** create all core directories, `history/project-constitution.md` (from `assets/templates/project-constitution.md`), `history/operations-playbook.md` (from `assets/templates/operations-playbook.md`), and the root `index.md` (from `assets/templates/index.md`).

**If the repository already exists:** normalize only what is missing or inconsistent. Do not recreate files that are already well-formed. Update `index.md` only if its section index is stale.

### Step 4: Collect Raw Materials

Gather materials into `raw` with source metadata and first-pass judgment, grouped by subtopic when useful. Use `assets/templates/raw-note.md` as the starting template.

**If materials are already placed in `/raw` by the user:** skip to comparison. Do not re-ingest content that has already been processed.

### Step 5: Produce Comparison Summary

Classify each finding using the criteria in `references/comparison-classification.md` (new, repeated, conflicting, pending review). Present the comparison to the user before promotion.

**If there is no prior content in higher layers:** comparison is simpler — only flag internal conflicts within the new batch itself.

### Step 6: Promote Knowledge

Promotion moves content upward through the layers. Work in order: source first, then entity and concept in parallel, then wiki last. Consult `references/promotion-criteria.md` for what qualifies for each layer, and `references/note-patterns.md` for page structure.

#### 6a: Create Source Synthesis Pages

Combine related `raw` items into `source` pages. Each should: synthesize raw sources on the same subtopic, identify well-supported vs. weakly-supported claims, flag contradictions, and link to the raw items it draws from. Start from `assets/templates/source-note.md`.

#### 6b: Propose Entity and Concept Keywords

Before creating entity or concept pages, extract candidate keywords from the source pages. Score each keyword by importance — this is a **filtering** step to decide which keywords deserve pages, separate from the sorting step that determines their order.

Score each keyword on these dimensions:

- **Cross-source count**: Appears in how many different source pages? 1 = weak, 2 = moderate, 3+ = strong.
- **Position prominence**: Appears in headings or first paragraphs? Boosts score.
- **Role fit**: Does it clearly match the entity or concept category? Off-category terms score lower.
- **Specificity**: Multi-word, precise terms score higher than generic single words.

Assign each a confidence level: **High** (definitely include), **Medium** (include, flag for review), **Low** (exclude unless user overrides).

Present scored keyword lists to the user:

- **Proposed entities**: People, organizations, tools, roles, frameworks, books, platforms
- **Proposed concepts**: Ideas, principles, patterns, bridge terms, distinctions

Before sorting, ask the user which ordering method to use:

- **Specificity** (default, `--mode specificity`): Multi-word terms rank above single-word, longer above shorter.
- **Frequency** (`--mode frequency`): Rank by occurrence count across source pages. Pass `keyword<TAB>count` pairs.
- **Composite** (`--mode composite`): Weighted blend of specificity + frequency.

Also run with `--check-overlaps` to detect substring containment.

**Ask the user to confirm, revise, or approve the keyword lists.** Do not create pages until confirmed. **Skip this confirmation only if the user explicitly agreed to skip it** (e.g., "just go ahead," "auto-approve all").

#### Keyword Safety Rules

When processing confirmed keywords into pages and wikilinks, follow the rules in `references/keyword-safety.md` — priority ordering, filename sanitization, case-insensitive deduplication, and entity/concept disambiguation.

#### 6c: Create Entity Pages

For each confirmed entity, create a page starting from `assets/templates/entity-note.md`. Link back to supporting source pages and add `[[wikilinks]]` to related entities and concepts.

#### 6d: Create Concept Pages

For each confirmed concept, create a page starting from `assets/templates/concept-note.md`. Link back to source pages and related entities.

#### 6e: Create Wiki Route Pages

Build maps, playbooks, comparison pages, and artifact-flow pages starting from `assets/templates/wiki-note.md`. Wiki pages organize and navigate existing content.

### Step 7: Densify The Graph

Add comparison pages for easily confused concepts and route descriptions. Prioritize wikilinks for higher-priority terms (ranked first by `scripts/sort-keywords.py`). Avoid overlinking.

### Step 8: Maintain History

Update a dated change log recording why changes were made, what judgments were used, and whether later user confirmation is still needed.

### Step 9: Validate Output

Before handing off, verify:

- [ ] All required directories exist and are non-empty
- [ ] `index.md` links to the correct sections and is up to date
- [ ] Key `[[wikilinks]]` resolve to existing pages (no dead links to major entities or concepts)
- [ ] No nested or broken wikilinks from overlapping keywords (e.g., no `[[[[Claude]] Code]]`)
- [ ] `history/` contains a dated entry for this session's changes
- [ ] The "pending user confirmation" items are clearly flagged

### Iteration

After validation, summarize what was created or changed. If the user requests adjustments, return to the relevant step (comparison at Step 5, promotion at Step 6, or densification at Step 7) rather than restarting from scratch.

## Supporting Files

### references/ — consulted during execution

- `references/promotion-criteria.md` — What qualifies for entity, concept, and wiki promotion (Step 6).
- `references/note-patterns.md` — Page structure for raw, source, entity, concept, and wiki notes (Steps 4, 6a, 6c, 6d, 6e).
- `references/comparison-classification.md` — Classification rubric for new/repeated/conflicting/pending review (Step 5).
- `references/keyword-safety.md` — Rules for processing confirmed keywords: priority ordering, filename sanitization, deduplication, disambiguation (Step 6b).

### assets/templates/ — copied to bootstrap pages

- `raw-note.md`, `source-note.md`, `entity-note.md`, `concept-note.md`, `wiki-note.md` — Page templates for each layer.
- `index.md`, `project-constitution.md`, `operations-playbook.md` — Root and governance templates (Step 3).

### assets/ — consulted during execution and testing

- `assets/knowledge-flow-example.md` — Illustrated walkthrough of materials flowing through all 6 layers.
- `assets/verification-scenarios.md` — Four behavioral test scenarios for validating skill behavior.

### scripts/ — executed for mechanical tasks

- `scripts/sort-keywords.py` — Keyword priority sorting with three scoring modes and overlap detection (Step 6b, Step 7).

## Maintenance Rules

- Periodically review stale terms; mark as historical or pending-review instead of deleting.
- Compare new terminology against old before replacing.
- Preserve change traces in `history`.

## Output Quality Standard

- Clean English or Chinese per repository policy. No garbled text or placeholder characters.
- Plain Markdown, wikilink-system compatible. Higher layers more synthetic than lower.

## Recommended Extra Pages

Add when they improve the repository: comparison matrix, confusing pairs page, artifact-flow page, adoption playbook, wikilink-system usage note.

## Knowledge Flow Example

See `assets/knowledge-flow-example.md` for an illustrated walkthrough of materials flowing through all 6 layers.

## Verification Scenarios

Four behavioral walkthroughs in `assets/verification-scenarios.md` validate the skill's behavior: fresh repository creation, existing repository extension, keyword confirmation skip, and substring containment handling.
