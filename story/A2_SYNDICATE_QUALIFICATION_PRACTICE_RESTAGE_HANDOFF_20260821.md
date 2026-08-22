# A2 Syndicate Qualification Practice Restage Handoff — 2026-08-21

Verdict: **PARTIAL** pending refreshed exact-head repository-native validation.

## Authority and isolation

- Authoritative repository: `Wiredshark/star`
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-syndicate-qualification-practice-restage-20260821-2002`
- Historical source branch left untouched: `agent/a2-syndicate-qualification-practice-20260820-0307`
- Production restage: `06901b6b5abe9800243ae08cec17da1720f2bb3c`
- Initial strengthened validator: `0fd986f870c43c74ee60b4632ba260945377e424`
- Validator comparison-parsing repair: `537fa17e2abafa1ebbb6f9449c6583be615fd068`

## Implemented RPG / narrative loop

After `B2 Syndicate Qualification Compact: aftermath seen`, Mara Venn asks what practice should survive the resolved qualification compact. The player may:

1. start from carried evidence and review only the job-specific gap;
2. require scope, exclusions, supervision assumptions, and expiry context to travel with transferred qualification evidence;
3. keep the compact local rather than convert one yard network's settlement into borrowed jurisdiction; or
4. refuse to establish a standing personal doctrine.

A later authoritative A1 labor rotation pressure-tests each positive practice when `world: syndicate labor strain >= 2` and `world: syndicate labor rotation active`. The later reader is one-shot and history-aware.

## Invariants

- A1 remains sole writer of Syndicate labor strain / rotation state.
- B2 remains sole writer of `B2 Syndicate Qualification Compact:*` state.
- Every new assignment is namespaced under `A2 Syndicate Qualification Practice:*`.
- Transferable qualification evidence never becomes blanket local job authority.
- Refusal does not arm the later pressure test.
- Both state-only missions use `offer precedence 9`.
- All objective-less state-only terminal paths end with `decline`, not `accept`.

## Validation history

Initial exact-head story/simulation validation run `32539121102` failed because the new focused validator incorrectly treated the read-only comparison `world: syndicate labor strain >= 2` as an assignment by rejecting every `=` character. Commit `537fa17e2abafa1ebbb6f9449c6583be615fd068` narrows the ownership check to assignment syntax (` = `), preserving rejection of actual A1/B2 writes while allowing comparisons. The first exact-head save-load run was still in progress when the validator repair was made and is superseded for acceptance by refreshed validation on the repaired head.

## Files

- `data/human/a2 syndicate qualification practice.txt`
- `tools/story/validate_a2_syndicate_qualification_practice.py`
- `story/A2_SYNDICATE_QUALIFICATION_PRACTICE_RESTAGE_HANDOFF_20260821.md`

## Validation required before A3

Require refreshed exact-head Fork simulation/story/style validation and Fork save-load integration smoke after the validator repair. Actual-game acceptance should verify B2-aftermath gating, all four briefing choices, refusal suppression, persistence across save/reload, later A1 labor-rotation pressure testing for all three positive routes, one-shot suppression, and Syndicate offer-precedence behavior.

Do not self-integrate. A3 owns integration review.
