# Verification Scenarios

These behavioral walkthroughs test the refiner end-to-end. Use them to validate changes to this skill, or as a model for other skills' test scenarios.

## Scenario A: Skill With Over-Broad Triggers

**Setup:** Identify a skill whose description says "Invoke for any task involving code" with no exclusion section.

**Expected:** Diagnosis spots "Over-broad triggers" and "Missing exclusion clauses." The proposal adds concrete counterexamples. After refinement, reading only the description, an agent can name 3 scenarios where the skill should not activate.

**Pass:** Both bad features removed; exclusions are concrete, not vague.

## Scenario B: Skill Bloated Above 2,000 Words

**Setup:** Identify a skill whose body exceeds 2,200 words with visible filler paragraphs that restate section headings.

**Expected:** Diagnosis identifies "Redundancy and filler" with specific line citations. The proposal targets filler for removal without touching substantive instructions. After refinement, word count is 500–2,000 and all original workflow steps remain intact.

**Pass:** Word count in range, zero filler sentences, no substantive content lost.

## Scenario C: Refinement Driven by User Feedback

**Setup:** User reports "The skill runs when I ask about file permissions, but it's for database migrations only."

**Expected:** Feedback maps to "Over-broad triggers" in Track C. The proposal tightens the description. After refinement, the "When NOT to Invoke" section explicitly excludes file permission tasks.

**Pass:** The user's reported false-trigger scenario appears in the exclusion list.
