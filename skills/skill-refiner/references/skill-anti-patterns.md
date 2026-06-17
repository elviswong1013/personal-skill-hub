# Bad Design Features: A Taxonomy

This reference catalogues features that make a skill poorly designed. Use it during diagnosis alongside the scorecard — each bad feature you spot should be addressed in the refinement plan. The inverse of each bad feature points toward a corresponding good feature (see `SKILL.md`'s "What Makes a Great Skill" section).

---

## Category 1: Trigger Design Failures

A skill with poor trigger design is either invisible to the agent or impossible to ignore — both are failures.

### 1.1 Over-broad Triggers

**Symptom:** The description says "Invoke for any task involving X" or uses sweeping language like "whenever you work with files." The skill hijacks tasks it shouldn't.

**Why it matters:** The agent loses discernment. A skill for writing tests shouldn't fire when the user asks for a code review that mentions the word "test." Each false activation erodes trust in the skill system.

**Detection:** Ask: "If I read only the description, can I list 3 concrete scenarios where this skill should NOT activate?" If not, the trigger is too broad.

### 1.2 Missing Exclusion Clauses

**Symptom:** The skill has affirmative triggers but no "When NOT to Invoke" section. The description tells the agent when to jump in but never when to stay out.

**Why it matters:** Without negative examples, the agent has no guardrails. It applies the skill in borderline cases where it's inappropriate, then the user has to undo the damage.

**Detection:** Look for the absence of a "Do NOT invoke" or "When NOT to" section. If present, check whether the exclusions are concrete scenarios or just vague hand-waving like "don't use this when it doesn't apply."

### 1.3 Trigger Overlap With Other Skills

**Symptom:** Two or more skills claim the same triggering condition. For example, both a "code-reviewer" and a "bug-finder" skill fire when the user says "check this code."

**Why it matters:** The agent faces a coin toss. It may invoke the wrong skill, or invoke both, or freeze. Ambiguity in trigger territory is ambiguity in execution.

**Detection:** Scan the description of sibling skills. If any trigger condition appears in more than one skill without a disambiguating clause, there's overlap.

### 1.4 Trigger Based on Tool Names, Not Intent

**Symptom:** "Invoke when the user mentions `git` or `npm`." The trigger is keyed to specific tooling rather than the user's underlying goal.

**Why it matters:** Tool names change, fall out of fashion, or differ by platform. A skill triggered by tool mention will either go stale or fail to activate when the user uses alternative tooling.

**Detection:** Count how many trigger conditions name a specific CLI command, library, or brand. More than zero is a warning; more than two is a problem.

---

## Category 2: Content Quality Failures

A skill's instruction body can be too rigid, too vague, too bloated, or too sparse. All four are failures.

### 2.1 Command-Driven Instructions

**Symptom:** The skill reads like a shell script. Instructions say "Run `git status`", "Execute `npm run build`", "Create a file with `Write` tool." Every step is a prescribed action tied to a specific tool.

**Why it matters:** The skill becomes environment-locked. An agent on Windows can't use bash syntax. An agent with different tool names can't follow the recipe. The skill ages poorly as tools evolve.

**Detection:** Grep for backtick-wrapped commands (`), shell syntax, or tool-specific function names. If more than 30% of instruction lines contain tool references, the skill is command-driven.

### 2.2 Linear, No-Branch Workflows

**Symptom:** "First do A, then B, then C" with no decision points, no "if X, then..." logic, no handling of edge cases. The skill assumes one happy path.

**Why it matters:** Reality is messy. A skill for debugging that says "step 1: reproduce the bug" without addressing what to do when the bug can't be reproduced is a skill that fails in the real world.

**Detection:** Look for branching language: "if... then... otherwise..." or "when X happens, do Y." If the entire workflow is a single numbered list with no conditional splits, it's linear.

### 2.3 Hardcoded External Knowledge

**Symptom:** The skill body contains version numbers (`v2.3.1`), library-specific API signatures, URLs to documentation pages, or code snippets that will deprecate.

**Why it matters:** External knowledge rots. When the library releases v3.0 or the documentation URL changes, the skill becomes partially or entirely wrong. Agents following stale instructions produce broken output.

**Detection:** Scan for version strings, `.com` URLs (except internal project references), or import statements with specific package names.

### 2.4 Redundancy and Filler

**Symptom:** A section heading says "Step 1: Read the file," and the next paragraph says "The first step is to read the file by opening it with a text reading tool to understand its contents." The body restates what the heading already conveys.

**Why it matters:** This is word-count bloat masquerading as thoroughness. It pushes the skill over the 2000-word ceiling without adding information density. Agents waste time parsing fluff.

**Detection:** Read each section and ask: "Does this paragraph say anything not already captured by its heading and the surrounding context?" If a sentence can be deleted without changing what the agent understands, it's filler.

### 2.5 Framework-Specific Tunnel Vision

**Symptom:** "For example, in React..." — but the skill purports to be about frontend testing. The examples, principles, and workflow all orbit one ecosystem.

**Why it matters:** The skill becomes useless outside that ecosystem. An agent helping with a Vue project will either misapply React patterns or ignore the skill entirely.

**Detection:** Count framework/library mentions. If one framework dominates >50% of examples, the skill has tunnel vision.

### 2.6 Vague or Missing Rationale

**Symptom:** Instructions say "do X" but never explain why X matters. The agent follows orders without understanding the goal, so it can't adapt when X doesn't fit the situation.

**Why it matters:** Intention-driven agents need to understand *why* they're doing something to make good judgment calls. Without rationale, they follow instructions blindly — and blindly is how mistakes happen.

**Detection:** For each major instruction, ask: "Is it clear what outcome this step achieves and why that outcome matters?" If the answer is "no" for more than one major step, rationale is lacking.

---

## Category 3: Structural Design Failures

A skill's file structure is its skeleton. A misaligned skeleton causes the skill to collapse under real use.

### 3.1 SKILL.md Abdicates Governance

**Symptom:** The `SKILL.md` is a stub — perhaps just a few paragraphs — while the real logic lives in `scripts/`. The agent must execute scripts to understand what to do.

**Why it matters:** The hierarchical model puts `SKILL.md` at the top for a reason: it's the first file an agent reads. If it doesn't govern the workflow, the agent misses the big picture and may skip or misuse the scripts.

**Detection:** Compare the word count and instructional density of `SKILL.md` against the total content in `scripts/`. If `SKILL.md` is the minority, governance is inverted.

### 3.2 Orphaned Supporting Files

**Symptom:** `references/api-guide.md` exists and is comprehensive, but `SKILL.md` never mentions it. The agent never discovers the resource.

**Why it matters:** Supporting files that aren't referenced don't get used. They become dead weight — maintained by nobody, trusted by nobody, and eventually out of sync.

**Detection:** List every file in `scripts/`, `references/`, and `assets/`. Search for mentions of each filename in `SKILL.md`. Any file with zero mentions is orphaned.

### 3.3 Empty or Placeholder Directories

**Symptom:** `scripts/` exists but contains only `.gitkeep`. `references/` is an empty directory created "for future use."

**Why it matters:** Empty directories mislead. An agent sees the directory and assumes content exists. When it doesn't find any, it wastes time searching or makes assumptions about missing content. The structure should reflect actual content, not aspirational structure.

**Detection:** Check each optional directory. If it exists and contains only `.gitkeep` or is empty, it's dead structure.

### 3.4 Bloated Assets Directory

**Symptom:** `assets/` contains screenshots, large generated files, binaries, or cached data alongside legitimate templates.

**Why it matters:** Bloated assets slow down version control, create merge conflicts, and make it hard to find the actual templates that agents need.

**Detection:** Check file sizes and types in `assets/`. Any binary file or file over 100KB that isn't a reference template is suspect.

---

## Category 4: Generalization Failures

A non-generalizable skill is a skill that works for one person in one project and nobody else.

### 4.1 Platform Assumptions

**Symptom:** The skill assumes Linux ("use `/tmp/`"), macOS ("use `pbcopy`"), or Windows ("use `C:\Users\`") — without acknowledging other platforms exist.

**Why it matters:** The skill silently fails for users on other operating systems. They either get errors they don't understand or spend time translating instructions themselves.

**Detection:** Search for OS-specific paths, commands, or conventions. If present without alternatives or abstraction, the skill is platform-locked.

### 4.2 IDE or Editor Lock-In

**Symptom:** "Click the green play button in the top-right corner of VSCode." The instructions assume a specific editor UI.

**Why it matters:** Not every agent runs in VSCode. A skill that references editor-specific UI is unusable in any other environment.

**Detection:** Search for editor brand names, UI element descriptions ("click the...", "open the sidebar..."), or keyboard shortcuts that are editor-specific.

### 4.3 Project Structure Assumptions

**Symptom:** "Open `src/components/Button.tsx`" — the skill assumes a specific directory layout that only one project follows.

**Why it matters:** No two projects have identical directory structures. A skill that hardcodes paths is non-transferable.

**Detection:** Count hardcoded file paths. If more than two appear without qualifiers like "look for a file matching the pattern...", the skill has structure lock-in.

### 4.4 Single-Purpose Design

**Symptom:** The skill does exactly one thing, in exactly one way, for exactly one context — and was never intended to handle variations. There's no "adapt this approach when..." or "the principle applies even when..."

**Why it matters:** Single-purpose skills multiply. Instead of one general skill, you end up with five narrow variants that are hard to discover and harder to maintain.

**Detection:** Ask: "Could I use this skill for a related but slightly different task without modifying it?" If the answer is no, the skill is too narrow.

---

## Category 5: Trust and Feedback Failures

Skills that don't seek feedback or validate their own effectiveness degrade silently over time.

### 5.1 No Self-Validation Step

**Symptom:** The skill's workflow ends at "deliver the output." There's no step where the agent checks whether the output is correct or useful before presenting it.

**Why it matters:** Without self-validation, errors propagate to the user. The user becomes the QA layer, which is exactly what skills are meant to prevent.

**Detection:** Look for a "validate" or "verify" stage in the workflow. If absent, the skill lacks self-validation.

### 5.2 No Feedback Loop for Iteration

**Symptom:** The skill assumes one-shot perfection. There's no mechanism for the agent to say "this didn't work, let me adjust" or for the user to provide correction that feeds into the next attempt.

**Why it matters:** Skills operate in complex environments. First attempts often miss the mark. Without a feedback loop, the skill either fails silently or forces the user to start over from scratch.

**Detection:** Look for language about retrying, adjusting, or incorporating user feedback. If the workflow is strictly linear with no loops, the skill has no feedback mechanism.

### 5.3 No Testing Strategy

**Symptom:** The skill was written, checked once manually, and called done. There's no guidance on how to verify the skill works correctly after changes, and no record of past test results.

**Why it matters:** Without testing, refinement is blind. You can't know if you improved the skill or broke it. Changes accumulate, and quality drifts.

**Detection:** Look for test scenarios, validation criteria, or testing instructions. A section titled "How to test this skill" or "Verification scenarios" is a strong positive signal; its absence is a gap.
