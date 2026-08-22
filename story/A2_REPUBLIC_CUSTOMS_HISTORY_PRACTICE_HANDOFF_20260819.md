# A2 Republic Customs History Practice handoff

Verdict: PARTIAL pending exact-head repository-native validation and actual-game acceptance.

Authoritative base: `main` @ `8785f25572b65d66c6181a39d1ef2b28ca6dda83`.
Branch: `agent/a2-republic-customs-history-practice-20260819-2102`.
Production commit: `16c2a53df5f1034d95c8a78370d9133fb726bf48`.
Validator commit: `0de2fbef6c1d2ee8d88f51cf5c99289f90135201`.

## Loop

Consumes the already-integrated A2 Republic Customs Review only after its later reader has been seen, then turns newly integrated B1 Republic customs institutional history into a player-owned evidence-handling practice. The player chooses provenance/amendment visibility, trigger-fact-inference separation, current-reason-before-repeat-review, or local-only handling. A later one-shot reflection demonstrates the institutional distinction without claiming that procedure guarantees correctness.

## Invariants

- B1 history is observational and remains write-free.
- Existing `A2 Republic Customs Review:*` state is read-only.
- No A1 `world:*` state is consumed or written by this slice.
- New persistence is confined to `A2 Republic Customs History Practice:*`.
- The choice grants no Republic credential, office, customs authority, endorsement, or representative status.
- Procedure remains revisable; review trigger, confirmed evidence, inference, and unresolved questions remain distinct.

## Files

- `data/human/a2 republic customs history practice.txt`
- `tools/story/validate_a2_republic_customs_history_practice.py`
- this handoff

## Required A3 gates

Run the focused validator and repository story/simulation/style workflow on the exact final head; run stock build/save-load smoke; then verify actual-game gating after the customs-review later reader, all four choices, save/reload between stages, one-shot reflection suppression, and Republic offer-precedence regression. Do not self-integrate from A2.
