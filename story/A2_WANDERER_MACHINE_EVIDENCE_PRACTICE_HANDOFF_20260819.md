# A2 Wanderer Machine Evidence Practice — handoff

**Stage:** A2 CORE RPG + DYNAMIC NARRATIVE  
**Verdict:** PARTIAL pending exact-head repository-native validation and runtime acceptance  
**Authoritative base:** `main@46d1afcf2e22e211b02f1615e863dae903f0778f`  
**Branch:** `agent/a2-wanderer-machine-evidence-practice-20260819-2003`  
**Production commit:** `4286ceafd2222184e48469a60896d20d30fb139f`  
**Validator commit:** `cc786ed3358a31279bc7460fa9bbf77a9c303f61`

## Implemented loop

Consumes the integrated B2 Wanderer Machine Custody Compact only after its one-shot aftermath. The player chooses what private evidence-handling practice to carry forward: provenance with derivatives, independent challenge tied to source evidence, local-only interpretation, or refusal. A later one-shot reflection demonstrates a distinct consequence for each positive route.

## Invariants

- B2 custody state is read-only.
- No `world:*` state is introduced or written.
- All new persistence is under `A2 Wanderer Machine Evidence Practice:*`.
- Curator and Engineer remain player-private shorthand, not Wanderer offices or titles.
- No definitive Mereti/Sestor directive, Builder intent, universal machine motive, or Wanderer representative authority is asserted.
- Refusal does not schedule the reflection and is not converted into consent.

## Files

- `data/wanderer/a2 wanderer machine evidence practice.txt`
- `tools/story/validate_a2_wanderer_machine_evidence_practice.py`
- `story/A2_WANDERER_MACHINE_EVIDENCE_PRACTICE_HANDOFF_20260819.md`

## Validation required

Run repository-native story/simulation/style validation and production save-load smoke on the exact final head. Runtime acceptance should verify B2-aftermath gating, all four initial routes, all three positive reflections, refusal suppression, save/reload between stages, one-shot behavior, and Wanderer offer-precedence regression.

## A3 integration

Do not integrate until exact-head required CI is green and runtime acceptance is either completed or explicitly accepted as deferred under the current integration policy. Merge/cherry-pick only the isolated A2 candidate; preserve B2 ownership.
