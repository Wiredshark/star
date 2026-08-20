# A2 Free Worlds Repair Priority — handoff

- Authoritative base: `main@8c61fb377068f6f8cc0d43876fbc15b99f95d6c0`
- Branch: `agent/a2-free-worlds-repair-priority-20260819-2302`
- Production commit: `de3ac834dfbd231ed18bf04f28d2fce6eaaa387e`
- Validator commit: `90fcad466a0d36e832d6e769ec8f585a59c4396b`
- Stage: A2 CORE RPG + DYNAMIC NARRATIVE
- Verdict: PARTIAL pending exact-head repository-native validation and actual-game acceptance.

## Implemented loop

Consumes A1 `world: free worlds repair backlog` and `world: free worlds patrol surge` read-only. At repair backlog >=3, yard coordinator Mara Venn asks the player to choose safety-first, patrol-readiness, predictable-civilian-turnaround, or refusal. When backlog later recovers to <=1, a one-shot review combines each positive priority with whether the A1 patrol surge is still active, yielding six simulation-sensitive outcomes plus refusal-respected handling.

## Invariants

A1 remains sole writer of repair backlog and patrol surge. This slice writes only `A2 Free Worlds Repair Priority:*`. It does not alter the earlier Anika Ro patrol-doctrine state. Refusal is not converted into endorsement. No save-schema or C++ change is introduced; persistence uses ordinary condition state.

## Files

- `data/human/a2 free worlds repair priority.txt`
- `tools/story/validate_a2_free_worlds_repair_priority.py`
- this handoff

## Required validation

Run the focused validator and repository-native story/simulation/style workflow on the exact final head. Run production build/save-load smoke. In the actual game verify initial backlog gating, all four choices, backlog-recovery gating, all six patrol-surge/quiet outcomes, refusal handling, save/reload between stages, one-shot suppression, and Free Worlds offer-precedence regression.

## A3 integration

Do not self-integrate. Re-read current `main`, verify ancestry/conflicts, require terminal-green repository workflows, and preserve A1 ownership of both consumed world states.
