---
name: "skill-refiner"
description: "Refines existing skills by removing bad design features and adding good ones. Invoke when a skill needs improvement, triggers incorrectly, is too long/short, is too rigid, or has received feedback indicating it underperforms. DO NOT invoke for creating new skills from scratch — use skill-creator for that."
---
# Skill Refiner

This skill refines and improves existing agent skills through a dual approach: **remove bad design features** while **adding good ones**. Refinement is iterative — incorporating feedback, evaluation results, and testing outcomes across multiple rounds.

## Trigger Conditions

### When to Invoke This Skill

- A skill triggers too eagerly, too narrowly, or in wrong contexts — its trigger boundaries need tightening.
- A skill's `SKILL.md` exceeds ~2000 words or falls below ~500 words and feels incomplete or bloated.
- A skill contains rigid pseudocode or hardcoded commands instead of conveying intention and principles.
- A skill lacks or misuses the hierarchical file structure (`scripts/`, `references/`, `assets/`).
- A skill needs to be made more reusable across different tools, languages, or project contexts.
- A user reports that a skill "doesn't work well" or "feels off" but the problem isn't a specific bug.
- Any external signal indicates a refinement need: user feedback on output quality, a scorecard audit revealing gaps, or test failures from structural or behavioral validation.

### When NOT to Invoke

- Creating a brand-new skill from scratch — defer to `skill-creator`.
- Fixing a single concrete bug in a skill script — that's a regular code fix, not refinement.
- The skill works well and the request is purely cosmetic (e.g., only fixing a typo).
- The user is asking about skill mechanics conceptually without wanting changes applied.
- The target is a regular project file, not a skill file under the agent's skills directory.

## Core Principle: Remove Bad, Add Good

Every refinement action is one of two things:

1. **Remove a bad design feature.** Consult `references/skill-anti-patterns.md` — taxonomy spans trigger, content, structure, generalization, and trust/feedback.
2. **Add a good design feature.** Consult the benchmark below — sharp triggers, intention-driven instructions, self-validation, feedback loops.

Tag every change as "remove" or "add." Removing without adding leaves a hollow skill; adding without removing leaves it broken. Both are required.

## Core Principle: Use Scripts, Don't Rebuild

When mechanical steps are needed (word counting, structure validation), leverage existing tools before creating anything new.

- **Check first**: Verify an existing script already handles the task. Invoke it — don't recreate what exists.
- **If it fails**: Don't debug it. Create a temporary script based on the intention in this document. Principles define what needs to happen; the script carries it out.
- **New permanent scripts**: Only add when the task is mechanical, frequent, and reusable. One-off needs don't justify permanent additions.

## Refinement Workflow

This workflow is intention-driven and iterative. It describes what to achieve at each stage, not which specific commands to run. Adapt the approach to the situation and to the type of input driving the refinement (initial diagnosis, user feedback, evaluation results, or test failures).

### Stage 1: Diagnosis — Understand What's Wrong and What's Missing

Before making any changes, read the skill's `SKILL.md` and any supporting files in `scripts/`, `references/`, and `assets/`. Form a judgment across two parallel tracks. Do not modify anything yet.

**Track A: Identify Bad Features Present**

Using `references/skill-anti-patterns.md` as a reference, scan across all five categories. For each bad feature found, record:
- Which bad feature it is and how it manifests concretely in this skill.
- Severity: High (blocks operation), Medium (degrades quality), Low (annoyance).

**Track B: Identify Good Features Missing**

Using the benchmark below as a checklist, identify which good features are absent or underdeveloped. For each gap, record which feature is missing and why the skill needs it.

**Track C: Incorporate External Signals**

If this round is driven by external input, map each signal to its root cause:
- **User feedback**: Map complaints to the bad feature causing them and the good feature that would resolve them (e.g., "the skill runs when it shouldn't" → Over-broad triggers → needs Razor-sharp trigger boundaries).
- **Evaluation results**: Compare against the previous round's scorecard. Which bad features persisted? Which good features still haven't landed?
- **Testing results**: Trace each test failure to the bad feature or missing good feature that caused it.

**Track D: Identify Extraction and Enhancement Opportunities**

Scan `SKILL.md` for content that would serve better in supporting files:

- **Extraction candidates**: Lengthy blocks of domain knowledge, examples, verification scenarios, templates, or reference tables. If moving them to `references/` or `assets/` would improve clarity or conciseness — flag them.
- **Enhancement candidates**: Content already in `references/` or `assets/` that is thin and could be expanded with more detail during refinement.
- Record what to move or enhance, the target file, and the improvement.

Fill out a new `assets/skill-scorecard.md` entry for this round, including the "Bad Features Identified", "Good Features Missing", and if applicable, the "Iteration History" linking back to the previous round.

### Stage 2: Propose — Draft a Dual-Direction Plan

Present a structured refinement plan to the user, grouped into sections. For each change, state the current problem, the concrete edit that resolves it, and why it matters.

**Section 1: Bad Features to Remove** — List each bad feature from diagnosis with its removal edit and the failure mode it prevents.

**Section 2: Good Features to Add** — List each missing good feature from diagnosis with its addition and the quality dimension it elevates.

**Section 3: Extract and Enhance** — List extraction candidates from Track D: what to move out of `SKILL.md` into `references/` or `assets/`, and what existing supporting file content should be enriched with more detail. For each, state the target file and the improvement it brings.

Ask the user to approve the plan before making edits. If the user provides additional feedback at this stage, fold it back into the diagnosis and update the plan.

### Stage 3: Apply — Execute Both Directions

Once approved, apply changes. **Remove first, then add** — clearing bad features creates space for good ones to land cleanly.

When removing bad features, work through the categories in `references/skill-anti-patterns.md`: eliminate command-driven instructions, cut redundancy, tighten triggers, remove hardcoded external knowledge, and clean up structural issues.

When adding good features, work through the benchmark below: add exclusion clauses, introduce branching logic where workflows are linear, build in self-validation, establish feedback loops, and define testing instructions.

**The refinement scope includes all files under the skill directory** — not just `SKILL.md`:

- **Edit `SKILL.md`**: Update instructions, triggers, and workflow descriptions. Keep the YAML frontmatter, update `description`.
- **Edit `references/`**: Extract hardcoded domain knowledge (color specs, APIs, style guides) from the body. General rule: if content in `SKILL.md` is lengthy and moving it to `references/` would improve the skill — do it. Create new references when domain knowledge would help.
- **Edit `assets/`**: Update templates and examples. Same rule: if lengthy template content in `SKILL.md` would serve better as a standalone asset, extract it. Add templates the skill lacks.
- **Edit `scripts/`**: Only for genuinely mechanical, frequent tasks not already covered. Prefer intention-based guidelines.

Every supporting file change must be referenced from `SKILL.md`.

### Stage 4: Validate — Run Checks and Record Results

After applying changes, read the refined skill end-to-end and verify:

- [ ] All bad features identified in diagnosis have been removed or mitigated.
- [ ] All planned good features have been added and are functional.
- [ ] The `description` field clearly states both trigger and non-trigger conditions.
- [ ] The body is between 500 and 2000 words (excluding frontmatter).
- [ ] Instructions express intention, not commands or pseudocode.
- [ ] The hierarchical structure is clean: `SKILL.md` governs, optional directories serve clear purposes.
- [ ] The skill is general enough to apply across multiple tools, languages, or project types.
- [ ] No external input (user feedback, evaluation, test failures) was ignored — every signal was addressed.

Run the structural validation script found in `scripts/` to mechanically confirm layout integrity, frontmatter validity, and word count range. If the script is unavailable or fails, manually reproduce its checks by reading the skill files and verifying each criterion from this checklist yourself.

Record validation results and any test scenario outcomes in the scorecard's "Test Results Log."

If any check fails, return to Stage 2 and iterate.

### Stage 5: Iterate — Continuous Improvement Loop

Refinement is not one-and-done. A skill may go through multiple rounds as it encounters real-world use. After each round:

1. **Close the round**: Update the scorecard's "Iteration History" with pre/post scores, bad features removed, good features added, and the feedback source that drove this round.

2. **Open the next round if needed**: If the skill has been used and new issues surface (user feedback, test failures, edge cases discovered), begin a new round at Stage 1. The scorecard from the previous round provides baseline metrics.

3. **Know when to stop**: A skill is "done enough" when:
   - The average good-feature score is ≥ 4 across all dimensions.
   - Zero high-severity bad features remain.
   - The skill has survived at least one round of real-world testing without new issues being found.
   - Further changes would be cosmetic or would trade one benefit for another without net improvement.

4. **Regression guard**: Before starting a new round, re-run the structural validator and re-check the existing scorecard. Ensure the new round's fixes don't reintroduce bad features that were previously removed.

## What Makes a Great Skill: The Benchmark

Use these heuristics for evaluation and as targets when adding good features.

1. **Trigger boundaries are razor-sharp.** Description alone lets an agent decide in seconds; includes both affirmative triggers and explicit exclusions.
2. **Self-contained scope.** Doesn't leak into other skills' territory. Overlapping triggers signal disambiguation or merging is needed.
3. **Intentions travel further than instructions.** Write for the principle, not the tool. Principles survive framework migrations; CLI commands don't.
4. **Length is proportional to complexity.** Simple skills near 500 words; complex ones approach 2000. Never pad; never cut essentials.
5. **The hierarchy serves a purpose.** Every file in optional directories exists for a reason, and `SKILL.md` references it explicitly.
6. **Negative space is intentional.** Include guardrails: what *not* to do and when to *stop*, not just what to do.
7. **Ages well.** No hardcoded versions, APIs, or platform assumptions in the body. Isolate external references in `references/`.
8. **Self-validation is built in.** Workflow includes a step where output is checked before presenting to the user.
9. **A feedback loop exists.** Mechanism to adjust based on intermediate results or user correction — no one-shot assumptions.
10. **Testing is defined.** Verification scenarios exist so changes can be validated, with results tracked across rounds.

## Verification Scenarios

Three behavioral walkthroughs in `assets/verification-scenarios.md` test the refiner end-to-end: over-broad trigger diagnosis, filler removal from bloated skills, and feedback-driven refinement. Use them to validate changes to this skill, or as a model for other skills' test scenarios.

## References Directory

`references/` contains domain knowledge, style guides, and patterns that the agent consults during refinement:

- `skill-anti-patterns.md`: A taxonomy of bad design features across five categories (trigger, content, structure, generalization, trust/feedback). Use during diagnosis to identify what to remove.
- Additional references (e.g., well-refined skill examples, structure benchmarks) may be added as needed.

## Scripts Directory

`scripts/` contains automation for mechanical parts of refinement — things that don't require judgment:

- `validate-skill-structure.py`: Checks SKILL.md existence, frontmatter validity, word count range (500-2000), and optional directory integrity. Run during Stage 4 validation and before each new refinement round as a regression guard.

Scripts include usage documentation in their headers.

## Assets Directory

`assets/` contains templates and reference outputs:

- `skill-scorecard.md`: A structured evaluation template for recording bad features found, good features missing, scores across dimensions, iteration history, and test results. Fill out a fresh entry for each refinement round to track the skill's evolution over time.
- `verification-scenarios.md`: Three behavioral walkthroughs that test the refiner end-to-end. Consult during Stage 4 validation.
