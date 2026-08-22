# A2 Merchant Recovery Margin Practice handoff

Verdict: PARTIAL pending exact-head CI and actual-game acceptance.

- Authoritative base: `85ecbd74ba8fdff055d5151707c3550b24e915e2`
- Branch: `agent/a2-merchant-recovery-margin-practice-20260820-0103`
- Production commit: `8fe08fb950b5d546943ff728af458eb0f15a4c40`
- Validator commit: `2118f6313ff57f93536f86883cd8ff37155d7b3f`

## Loop
Consumes the integrated B2 Merchant Recovery Margin Compact only after `aftermath seen`. The player chooses continuity, current-capacity challenge, local-only reuse, or refusal. A later Merchant repair backlog recurrence (`>= 3`) combines each positive practice with A1 `world: merchant repair surge` active vs inactive, producing six distinct pressure-test outcomes.

## Invariants
- A1 remains sole writer of Merchant repair backlog/surge state.
- B2 remains sole writer of Recovery Margin Compact state.
- A2 writes only `A2 Merchant Recovery Margin Practice:*`.
- The compact remains voluntary coordination among participating Merchant ports, not centralized Merchant government.
- Refusal creates no later pressure-test state.
- Current physical capacity is not inferred solely from historical paperwork.

## Files
- `data/human/a2 merchant recovery margin practice.txt`
- `tools/story/validate_a2_merchant_recovery_margin_practice.py`
- this handoff

## Validation boundary
Focused validator is committed for repository-native discovery. No local Wiredshark/star execution host was established in this run, so local parser/build/runtime/save-load success is not claimed. Exact-head repository CI must pass before promotion.

## A3 integration
Re-read current `main`; confirm ancestry and no overlapping Merchant recovery-margin consumer. Require exact-head story/simulation/style and save-load workflows green, then exercise both missions in-game, all three positive practices under surge active/inactive, refusal suppression, persistence across save/reload, and Merchant offer precedence. Do not self-integrate.
