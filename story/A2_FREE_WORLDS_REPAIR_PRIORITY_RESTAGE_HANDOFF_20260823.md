# A2 Free Worlds Repair Priority current-main restage — handoff

- Stage: A2 CORE RPG + DYNAMIC NARRATIVE
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-free-worlds-repair-priority-restage-20260823-2205`
- Production restage: `d451eece597633ec9af9403658f4c2583e788022`
- Strengthened validator: `15a28aeda9c01afbad06c18e6d8fdcb00bab9c17`
- Historical PARTIAL PR #138 remains untouched.
- Verdict: PARTIAL pending exact-head repository-native validation.

## Implemented RPG loop

Consumes authoritative A1 `world: free worlds repair backlog` and `world: free worlds patrol surge` read-only. At repair backlog >= 3, yard coordinator Mara Venn asks the player to choose flight-critical safety, patrol readiness, predictable civilian turnaround, or refusal. Once authoritative repair backlog later recovers to <= 1, a one-shot review combines each positive priority with whether the A1 patrol surge is still active, yielding six simulation-sensitive outcomes plus refusal-respected handling.

This keeps the dynamic feedback loop connected to live simulation state rather than treating the original choice as isolated text:

`A1 repair pressure -> persistent A2 yard priority -> A1 recovery/current patrol mobilization -> history-aware A2 consequence`

## Ownership and persistence invariants

- A1 remains sole writer of Free Worlds repair backlog and patrol-surge state.
- All new writes are `A2 Free Worlds Repair Priority:*`.
- The slice does not alter earlier `A2 Free Worlds Patrol Doctrine:*` state.
- Refusal is persistent and is not converted into endorsement.
- No save-schema or C++ change is introduced; absent A2 conditions remain compatible defaults for older saves.
- The player's priority is a recorded yard practice, not centralized Free Worlds authority.

## Dialogue lifecycle

Both missions are dialogue/state-only and use `offer precedence 9`. Four Yard Briefing terminals and the Recovery Review terminal persist their state and use `decline`; there is no objective-less `accept` path.

## Files

- `data/human/a2 free worlds repair priority.txt`
- `tools/story/validate_a2_free_worlds_repair_priority.py`
- `story/A2_FREE_WORLDS_REPAIR_PRIORITY_RESTAGE_HANDOFF_20260823.md`

## Validator coverage

The focused validator checks the two-mission structure, both A1 thresholds, patrol-surge reads, all four initial routes, six surge/quiet positive outcomes, refusal-respected handling, A1 read-only ownership, A2 namespace isolation, offer precedence, state-only decline lifecycle, labels/gotos, absence of gameplay-objective directives, and one-shot recovery state.

## Required validation / A3 boundary

Run exact-head `Fork simulation and story validation` and `Fork save-load integration smoke`. Do not promote to READY or integrate unless both are terminal green. Optional exploratory actual-game acceptance may still exercise all initial routes, save/reload between stages, surge-active versus surge-quiet recovery, refusal, one-shot suppression, and Free Worlds offer precedence.

A2 must not self-integrate. A3 should re-read current authoritative `main`, verify ancestry/mergeability, and preserve A1 ownership plus the state-only dialogue lifecycle invariant.
