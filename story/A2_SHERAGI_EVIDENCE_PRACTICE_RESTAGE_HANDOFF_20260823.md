# A2 Sheragi Evidence Practice Restage Handoff — 2026-08-23

Verdict: PARTIAL pending exact-head repository-native validation and actual-game acceptance.

Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`

Branch: `agent/a2-sheragi-evidence-practice-restage-20260823-0105`

Production: `d88e34a47972d31f991a7267197ed77d73d68375`

Validator: `75a6896fa50d46850e9d1d91f5fad5f05c7a1e4c`

## Implemented RPG / narrative loop

This is a current-main restage of the historical Sheragi evidence-practice candidate, not a new archaeological conclusion. After `Sheragi Archaeology: Epilogue: done`, the player privately chooses provenance-first, context-first, revision-first, local-only, or explicit refusal handling of the modern human/Hai evidence practices that grew around the investigation. Each positive route persists under `A2 Sheragi Evidence Practice:*` and drives an explicitly gated one-shot later reflection. Refusal is persistent and does not arm the later reader.

## Invariants

- `Sheragi Archaeology: Epilogue: done` is read-only.
- No `world:*` state is read or written by this slice.
- All new persistent writes are under `A2 Sheragi Evidence Practice:*`.
- Ancient Sheragi evidence remains distinct from modern human/Hai evidence-handling practice.
- No archaeological office, curatorial authority, Hai authority, Sheragi title, endorsement, or representative authority is granted.
- Both dialogue-only missions use `offer precedence 9`.
- All six state-only terminal paths use `decline`; no objective-less `accept` remains.
- Provenance, context, revision, and local routes all have explicit later-reader gates.
- Refusal does not arm the later reflection.

## Files

- `data/sheragi/a2 sheragi evidence practice.txt`
- `tools/story/validate_a2_sheragi_evidence_practice.py`
- `story/A2_SHERAGI_EVIDENCE_PRACTICE_RESTAGE_HANDOFF_20260823.md`

## Validation required before READY

Run the repository-native `Fork simulation and story validation` and `Fork save-load integration smoke` workflows on the exact production/validator head. Do not claim success until both are terminal green. Actual-game follow-up should verify post-epilogue offer gating, all positive routes, refusal suppression, explicit later reflections, save/reload between stages, one-shot suppression, and Republic/Sheragi offer precedence behavior.

## A3 integration instructions

Do not self-integrate. A3 should integrate only after exact-head repository gates are green and should preserve the read-only epilogue boundary, namespace isolation, explicit route gating, refusal semantics, precedence 9, and state-only decline lifecycle.
