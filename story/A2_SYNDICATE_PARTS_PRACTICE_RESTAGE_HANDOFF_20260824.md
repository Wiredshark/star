# A2 Syndicate Parts Practice current-main restage handoff

Verdict: **PARTIAL** pending exact-head repository-native validation.

## Authority
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-syndicate-parts-practice-restage-20260824-0002`
- Production restage: `c404d447069d250e1e1a9bbf35c754120b773ff1`
- Strengthened validator: `753a19a5b951446e74dc0037b6c285596d34ab3f`
- Historical PARTIAL PR #149 remains untouched.

## Player-facing loop
During authoritative A1 `world: syndicate parts scarcity >= 3`, procurement auditor Elara Dane asks the player to choose provenance-first traceability, reserving the best-documented components for systems without certified substitutes, reversible temporary substitution with expiry/reinspection, or refusal.

Once authoritative scarcity later recovers to `<= 1`, the Recovery Review combines each positive policy with current A1 `world: syndicate maintenance backlog >= 3` versus `< 3`, yielding six history-aware outcomes plus refusal-respected handling.

Feedback chain:
`A1 parts scarcity -> persistent A2 procurement policy -> A1 scarcity recovery + live maintenance backlog -> history-aware A2 consequence`.

## Ownership and persistence invariants
- A1 remains sole writer of `world: syndicate parts scarcity`.
- A1 remains sole writer of `world: syndicate maintenance backlog`.
- This slice writes only `A2 Syndicate Parts Practice:*` conditions.
- It does not mutate labor strain/rotation, Tessa Marr maintenance-triage state, or B2 Qualification Compact state.
- Save compatibility is additive: absent A2 conditions remain the default for existing saves.
- Refusal remains explicit and is not converted into a positive policy.

## Lifecycle and content invariants
- Both dialogue/state-only missions use `offer precedence 9`.
- Exactly five state-only terminal actions use `decline`.
- No objective-less `accept` endpoint is allowed.
- No cargo/passenger/destination/waypoint/NPC or other gameplay objective is introduced.
- Component compatibility does not erase supplier, repair, substitution, test, expiry, or uncertainty history.
- The player receives no centralized Syndicate procurement office or representative authority.

## Files
- `data/human/a2 syndicate parts practice.txt`
- `tools/story/validate_a2_syndicate_parts_practice.py`
- `story/A2_SYNDICATE_PARTS_PRACTICE_RESTAGE_HANDOFF_20260824.md`

## Validation status
Exact-head repository-native `Fork simulation and story validation` and `Fork save-load integration smoke` must both be terminal green before promotion to READY. No manual runtime result is claimed from the unrelated private Fallout host.

## Host/process boundary
The exposed private process service reported four pre-existing service-owned orphan processes. They were left untouched. The host is not treated as authoritative Endless Sky execution evidence.

## A3 integration instructions
Do not self-integrate. A3 should re-read current `main`, verify ancestry and mergeability, review the exact validated candidate, and preserve A1 ownership, A2 namespace isolation, refusal semantics, `offer precedence 9`, all six backlog-high/backlog-low recovery outcomes, and the state-only `decline` lifecycle.
