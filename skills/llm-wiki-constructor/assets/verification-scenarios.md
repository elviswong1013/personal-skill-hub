# Verification Scenarios

Use these walkthroughs to validate the skill's behavior after changes.

## Scenario A: Fresh Empty Repository

**Setup:** User says "build an llm-wiki for topic X" and no repository exists.

**Expected:** Agent creates all 6 directories, `index.md`, and `history/` files from templates. Step 6b presents scored keyword lists and **waits for user confirmation** before creating entity/concept pages. Step 9 confirms directories are populated.

**Pass:** All directories created, index.md links correctly, history contains dated entry, keyword lists confirmed before page creation.

## Scenario B: Existing Repository With New Raw Materials

**Setup:** Repository already exists with populated `/raw`, `/source`, and `/wiki`. User provides a new batch of materials.

**Expected:** Agent skips Step 3 (normalizes only if gaps). Skips Step 4 (materials already placed). Runs comparison, presents scored keyword proposals for new content only, promotes after confirmation.

**Pass:** No duplicate directories. Existing content undisturbed. Keyword confirmation gate respected.

## Scenario C: User Skips Keyword Confirmation

**Setup:** User says "build an llm-wiki for topic X, auto-approve all keywords, no need to confirm."

**Expected:** Agent proceeds through Step 6b but skips the confirmation prompt, noting in `history/` that keyword confirmation was waived by user request.

**Pass:** Entity and concept pages created without blocking on confirmation. History records the waiver.

## Scenario D: Overlapping Keywords (Substring Containment)

**Setup:** Source pages reference both "Claude" and "Claude Code". User confirms both as entities.

**Expected:** `sort-keywords.py --check-overlaps` warns that "Claude Code" contains "Claude". Agent creates `entity/claude-code.md` first (longer term), then `entity/claude.md`. When inserting wikilinks, "Claude Code" is linked first in all pages. When inserting `[[Claude]]` links later, the agent skips occurrences already inside `[[Claude Code]]` brackets.

**Pass:** Both pages exist. No nested or broken wikilinks (e.g., no `[[claude]] code` or `[[[[Claude Code]]]]`). All bare-text occurrences link correctly.
