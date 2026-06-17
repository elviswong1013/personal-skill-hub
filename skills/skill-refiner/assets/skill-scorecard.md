# Skill Scorecard

Use this template during the diagnosis stage to evaluate a skill consistently. Fill in one row per dimension, then summarize. For subsequent refinement rounds, use a fresh scorecard (or update this one) to track progress between iterations.

---

**Skill Being Evaluated:** `skill-refiner`
**Date:** `2026-06-17`
**Evaluator:** `agent`
**Refinement Round:** `1`

## Good Feature Dimensions

Rate how well the skill embodies each good feature (1 = absent, 5 = exemplary).

| Good Feature | Rating (1-5) | Evidence / Notes |
|---|---|---|
| Razor-sharp trigger boundaries | 4 | 10 trigger conditions + 5 concrete exclusions. "DO NOT invoke" is specific. Minor overlap risk with code-reviewer on "review" keyword — mitigated by skills-directory path gate. |
| Self-contained scope (no overlaps) | 4 | Explicitly defers to skill-creator for creation. Boundaries clean. |
| Intention-driven instructions | 4 | Overwhelmingly intention-driven. One command prescription found in Stage 4 (fixed this round). |
| Length proportional to complexity | 4 | 1,921 words fits 5-stage dual-track workflow. No filler detected. |
| Hierarchy serves a clear purpose | 5 | All 3 optional directories have justified content, all files referenced from SKILL.md. |
| Intentional negative space (guardrails) | 4 | "When NOT to Invoke" section present. "Know when to stop" in Stage 5. |
| Ages well (no hardcoded externals) | 4 | No version numbers, APIs, or framework mentions. PyYAML in validator is unavoidable. |
| Self-validation built in | 4 | Stage 4 with 8-item checklist plus mechanical validator. |
| Feedback loop for iteration | 5 | Stage 5 defines full round lifecycle with stop criteria and regression guard. |
| Testing strategy defined | 2 → **4** | Previously: structural validation only. This round: added 3 behavioral verification scenarios (A/B/C) with setup, expected behavior, and pass criteria. |

**Pre-Refinement Average:** 4.0
**Post-Refinement Average:** 4.2

## Bad Features Identified

| # | Bad Feature | Category | Manifestation in This Skill | Severity |
|---|---|---|---|---|
| 1 | 2.1 Command-driven instruction | Content Quality | Stage 4 contained a code block prescribing `Run scripts/validate-skill-structure.py against the skill directory` — a tool-specific command instead of stating the intent. | Low |
| 2 | 5.3 No testing strategy | Trust & Feedback | Only mechanical validation existed. No behavioral walkthroughs to verify the refiner's logic under real scenarios (trigger tightening, filler removal, feedback-driven refinement). | Medium |

## Good Features Missing

| # | Missing Good Feature | Why It's Needed |
|---|---|---|
| 1 | Testing strategy (verification scenarios) | The refiner judges other skills for lacking this. Without its own test scenarios, behavioral correctness can't be verified after changes. |

## Refinement Plan Summary

**Remove these bad features:**
1. Command-driven instruction (fixed: replaced with intention language + fallback guidance)
2. No testing strategy (fixed: added 3 verification scenarios)

**Add these good features:**
1. Testing strategy (3 behavioral scenarios: over-broad trigger diagnosis, filler removal, feedback-driven refinement)
2. Script-usage principle (check existing scripts first, fall back to intention if they fail)

**Top priorities for this round:**
1. Add verification scenarios to close the testing gap
2. Remove command prescription, replace with intention + fallback
3. Add "Use Scripts, Don't Rebuild" core principle

## Iteration History

| Round | Date | Pre-Refinement Avg Score | Post-Refinement Avg Score | Bad Features Removed | Good Features Added | Feedback Source | Key Changes |
|---|---|---|---|---|---|---|---|
| 1 | 2026-06-17 | 4.0 | 4.2 | 2 | 2 | Self-review (initial diagnosis) | Fixed command prescription; added 3 verification scenarios + script-usage principle |

## Test Results Log

| Round | Test Type | Scenario | Expected | Actual | Pass/Fail | Notes |
|---|---|---|---|---|---|---|
| 1 | Structural | validate-skill-structure.py | All checks pass, word count 500-2000 | Passed, 1,921 words (pre-fix) | Pass | — |

## Overall Assessment

**Pass**

**Summary of findings:**
The skill-refiner scores 4.2/5.0 post-refinement. Two bad features were found and removed: a minor command prescription in Stage 4 (replaced with intention language + manual fallback guidance) and a medium-severity testing gap (filled with 3 behavioral verification scenarios). A new core principle ("Use Scripts, Don't Rebuild") was added to prevent token waste on recreating existing tooling. The skill now models the testing it demands of others and explicitly prefers intention over command even in its validation stage.
