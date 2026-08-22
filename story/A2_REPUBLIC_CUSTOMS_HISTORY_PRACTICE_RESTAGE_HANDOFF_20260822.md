# A2 Republic Customs History Practice — current-main restage handoff

Verdict: PARTIAL pending exact-head repository workflows.

## Authority and isolation

- Authoritative integration base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`.
- Branch: `agent/a2-republic-customs-history-practice-restage-20260822-0705`.
- Historical source candidate: PR #128 / `agent/a2-republic-customs-history-practice-20260819-2102`; left untouched.
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

## Files

- `data/human/a2 republic customs history practice.txt`
- `tools/story/validate_a2_republic_customs_history_practice.py`
- `story/A2_REPUBLIC_CUSTOMS_HISTORY_PRACTICE_RESTAGE_HANDOFF_20260822.md`

## Validation

Exact-head repository-native story/simulation/style and production build/save-load workflows must be terminal green before A3 integration. Do not claim runtime acceptance until those workflows complete successfully.

## A3 integration instructions

Integrate only after both exact-head gates are green. Preserve the current-main base ancestry, read-only upstream ownership, route-specific persistence, `offer precedence 8`, and state-only `decline` lifecycle. Do not self-integrate from A2.
