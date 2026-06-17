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

Every refinement action falls into one of two categories:

1. **Remove a bad design feature.** Consult `references/skill-anti-patterns.md` for the full taxonomy. Bad features span trigger design, content quality, structural design, generalization, and trust/feedback failures. Each bad feature removed reduces the skill's brittleness, ambiguity, or narrowness.

2. **Add a good design feature.** Consult the "What Makes a Great Skill" benchmark below for the target state. Good features include sharp trigger boundaries, intention-driven instructions, self-validation, and feedback loops. Each good feature added increases the skill's robustness, clarity, and reusability.

Every change in the refinement plan should be explicitly tagged as "remove" or "add." A skill that only removes bad features without adding good ones becomes hollow. A skill that only adds features without removing bad ones stays broken. Both directions are required.

## Core Principle: Use Scripts, Don't Rebuild

When mechanical steps are needed (word counting, structure validation), leverage existing tools before creating anything new.

- **Check first**: Verify an existing script in `scripts/` already handles the task. Invoke it — don't waste tokens recreating what exists.
- **If it fails**: Don't debug or patch the broken script. Instead, create a temporary script based on the intention described in this document to complete the task. The principles define what needs to happen; the temporary script simply carries it out mechanically.
- **New permanent scripts**: Only add a script to `scripts/` when the task is genuinely mechanical, frequent, and reusable across refinement rounds. One-off needs don't justify permanent additions.

## Refinement Workflow

This workflow is intention-driven and iterative. It describes what to achieve at each stage, not which specific commands to run. Adapt the approach to the situation and to the type of input driving the refinement (initial diagnosis, user feedback, evaluation results, or test failures).

### Stage 1: Diagnosis — Understand What's Wrong and What's Missing

Before making any changes, read the skill's `SKILL.md` and any supporting files. Form a judgment across two parallel tracks. Do not modify anything yet.

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

Fill out a new `assets/skill-scorecard.md` entry for this round, including the "Bad Features Identified", "Good Features Missing", and if applicable, the "Iteration History" linking back to the previous round.

### Stage 2: Propose — Draft a Dual-Direction Plan

Present a structured refinement plan to the user, grouped into two sections. For each change, state the current problem, the concrete edit that resolves it, and why it matters.

**Section 1: Bad Features to Remove** — List each bad feature from diagnosis with its removal edit and the failure mode it prevents.

**Section 2: Good Features to Add** — List each missing good feature from diagnosis with its addition and the quality dimension it elevates.

Ask the user to approve the plan before making edits. If the user provides additional feedback at this stage, fold it back into the diagnosis and update the plan.

### Stage 3: Apply — Execute Both Directions

Once approved, apply changes. **Remove first, then add** — clearing bad features creates space for good ones to land cleanly.

When removing bad features, work through the categories in `references/skill-anti-patterns.md`: eliminate command-driven instructions, cut redundancy, tighten triggers, remove hardcoded external knowledge, and clean up structural issues.

When adding good features, work through the benchmark below: add exclusion clauses, introduce branching logic where workflows are linear, build in self-validation, establish feedback loops, and define testing instructions.

Keep the YAML frontmatter and update the `description` field to reflect refined trigger boundaries.

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

These behavioral walkthroughs test the refiner end-to-end. Use them to validate changes to this skill, or as a model for other skills' test scenarios.

### Scenario A: Skill With Over-Broad Triggers

**Setup:** Identify a skill whose description says "Invoke for any task involving code" with no exclusion section.

**Expected:** Diagnosis spots "Over-broad triggers" and "Missing exclusion clauses." The proposal adds concrete counterexamples. After refinement, reading only the description, an agent can name 3 scenarios where the skill should not activate.

**Pass:** Both bad features removed; exclusions are concrete, not vague.

### Scenario B: Skill Bloated Above 2,000 Words

**Setup:** Identify a skill whose body exceeds 2,200 words with visible filler paragraphs that restate section headings.

**Expected:** Diagnosis identifies "Redundancy and filler" with specific line citations. The proposal targets filler for removal without touching substantive instructions. After refinement, word count is 500–2,000 and all original workflow steps remain intact.

**Pass:** Word count in range, zero filler sentences, no substantive content lost.

### Scenario C: Refinement Driven by User Feedback

**Setup:** User reports "The skill runs when I ask about file permissions, but it's for database migrations only."

**Expected:** Feedback maps to "Over-broad triggers" in Track C. The proposal tightens the description. After refinement, the "When NOT to Invoke" section explicitly excludes file permission tasks.

**Pass:** The user's reported false-trigger scenario appears in the exclusion list.

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
