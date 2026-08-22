# A2 Republic Customs History Practice — current-main restage handoff

Verdict: READY for A3 review/integration.

## Authority and isolation

- Authoritative integration base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`.
- Branch: `agent/a2-republic-customs-history-practice-restage-20260822-0705`.
- Historical source candidate: PR #128 / `agent/a2-republic-customs-history-practice-20260819-2102`; left untouched.
- Production restage: `5269466940915f624450e5341c4e66b07272ef3b`.
- Strengthened validator: `246a22bdc361ad0834bd384fe7a01ba204f83ea2`.
- Explicit local-route reflection repair / exact validated production+validator head: `bc027978427aeb909006ec4b650ecfbaac807d28`.
- Scope is A2 only. No A1, B1, B2, or A3 state is written.

## Implemented RPG / narrative loop

The practice briefing is available only after `A2 Republic Customs Review: later reader seen`. The player persists one of four private working practices:

1. Preserve provenance and amendment history.
2. Separate review triggers, confirmed facts, inference, and unresolved questions.
3. Require a current reason before repeating an old review.
4. Keep the customs-history lesson local rather than turning it into a portable rule.

A later one-shot reflection reads that exact persistent route and demonstrates a distinct institutional consequence. The reflection does not claim that procedure guarantees correctness and does not grant the player a Republic credential, customs office, endorsement, or representative authority.

## Lifecycle and persistence invariants

- Both missions are dialogue-only state machines with `offer precedence 8`.
- All five objective-less terminal paths use `decline`; none uses `accept`.
- All new writes are under `A2 Republic Customs History Practice:*`.
- `A2 Republic Customs Review:*` is read-only.
- No `world:*` state is read or written by this slice, avoiding overlap with active customs-pressure consumers.
- The reflection is one-shot via `reflection pending` / `reflection seen`.
- Every persisted route has an explicit reflection gate; no route depends on accidental fallthrough.

## Validation and repair history

Initial head `774d8a162f79392b33106d440eb27a3c012bb4b2` passed changed-content style but failed the focused validator because `local only` used reflection fallthrough instead of an explicit state gate. The validator was kept strict and production was repaired in `bc027978427aeb909006ec4b650ecfbaac807d28` by adding an explicit `local only` branch.

On exact production/validator head `bc027978427aeb909006ec4b650ecfbaac807d28`:

- `Fork simulation and story validation` run `32569471263` / #396: SUCCESS.
- Focused story validators: SUCCESS.
- A1 simulation/state-ownership contracts: SUCCESS.
- Changed fork content style: SUCCESS.
- `Fork save-load integration smoke` run `32569471259` / #381: SUCCESS.
- Production configure/build: SUCCESS.
- Stock save/load smoke cases: SUCCESS.

No separate manual actual-game acceptance is claimed.

## Files

- `data/human/a2 republic customs history practice.txt`
- `tools/story/validate_a2_republic_customs_history_practice.py`
- `story/A2_REPUBLIC_CUSTOMS_HISTORY_PRACTICE_RESTAGE_HANDOFF_20260822.md`

## A3 integration instructions

Review/integrate the exact validated production/validator head or this handoff-only descendant after verifying current `main` ancestry. Preserve read-only upstream ownership, route-specific persistence, explicit route gating, `offer precedence 8`, and state-only `decline` lifecycle. Do not self-integrate from A2.
