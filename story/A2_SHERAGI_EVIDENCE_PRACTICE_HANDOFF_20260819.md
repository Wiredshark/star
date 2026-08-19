# A2 Sheragi Evidence Practice handoff

Verdict: PARTIAL pending exact-head repository-native validation and actual-game acceptance.

Authoritative base: `main` @ `60ce97cc68a1b2643649896335f5b9ae6418f28e`

Branch: `agent/a2-sheragi-evidence-practice-20260819-1504`

Production commit: `6a5069756a0254ee2331d78a282fd52df6ee86cc`

Validator commit: `2c8ec592ba36a5e1fbd8edf9b38f4d9f70800030`

## Implemented loop

Consumes the integrated B1 Sheragi archaeological-memory boundary read-only through `Sheragi Archaeology: Epilogue: done`. The player privately chooses one of four ways to handle the modern evidence practices that grew around the investigation: provenance-first, context-first, revision-first, or keep the Sheragi case local. A later one-shot reflection produces a distinct consequence for each route.

The production text explicitly distinguishes ancient Sheragi evidence from the modern human/Hai archival and archaeological practices developed while studying it. It does not turn those practices into Sheragi doctrine.

## Ownership and persistence

All new writes are confined to `A2 Sheragi Evidence Practice:*`. The B1 epilogue condition is read-only. No A1 `world:*` state is referenced or written. The player receives no archaeological office, curatorial role, Hai authority, Sheragi authority, endorsement, credential, or representative status.

Save compatibility is additive: absent A2 conditions mean the reflection remains eligible after the existing Sheragi epilogue; existing saves require no migration.

## Files

- `data/sheragi/a2 sheragi evidence practice.txt`
- `tools/story/validate_a2_sheragi_evidence_practice.py`
- `story/A2_SHERAGI_EVIDENCE_PRACTICE_HANDOFF_20260819.md`

## Acceptance invariants

1. Exactly two A2 missions: initial reflection and later reflection.
2. Initial mission requires `Sheragi Archaeology: Epilogue: done` and resolves exactly one of provenance/context/revision/local practice.
3. Later mission requires resolved A2 state and produces route-specific text once.
4. B1 state remains read-only; no `world:*` authority is introduced.
5. Text preserves the distinction between Sheragi archaeological evidence and modern human/Hai evidence-handling institutions.
6. No formal authority, office, endorsement, or credential is granted to the player.

## Validation evidence

A focused validator is committed but has not yet been observed running on the exact final candidate head. Repository-native story/simulation/style CI, stock build/save-load smoke, and actual-game runtime behavior must not be claimed until observed.

## A3 integration instructions

Before integration, require exact-head story/simulation/style success and stock save-load success. In the actual game, verify: post-epilogue gating; all four initial routes; all four later reflections; one-shot suppression after resolution; save/reload persistence between stages; and offer-precedence/regression alongside existing Sheragi post-epilogue observational missions.

Do not self-integrate from A2.
