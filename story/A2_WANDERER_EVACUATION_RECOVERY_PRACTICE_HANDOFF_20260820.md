# A2 Wanderer Evacuation Recovery Practice handoff

## Stage / verdict
- Stage: A2 CORE RPG + DYNAMIC NARRATIVE
- Verdict: PARTIAL pending exact-head repository-native workflow completion.
- No self-integration. A3 retains integration authority.

## Repository authority
- Authoritative base: `main@e7606069107ebfb082555898e10caecb23e1159d`
- Branch: `agent/a2-wanderer-evacuation-practice-20260820-1606`
- Production commit: `cd28ac54eb9132a74398ee1e1aed560f29aa50be`
- Focused validator commit: `f949179fd3efc902da06c17d6079b1c457b5a8cc`

## RPG / narrative loop
After `B2 Wanderer Evacuation Recovery Compact: aftermath seen`, and only while authoritative A1 evacuation logistics strain is recovered to `<= 1`, the player may adopt closure-evidence discipline, current-capacity review, local/context-only reuse, or explicit refusal. Positive choices persist. A later authoritative A1 evacuation recurrence at strain `>= 3` produces a one-shot history-aware consequence for the chosen practice.

Feedback chain: `A1 evacuation strain -> B2 recovery settlement/aftermath -> A2 player practice during recovery -> later A1 evacuation recurrence -> A2 consequence`.

## Invariants
- `world: wanderer evacuation logistics strain` is read-only; A1 remains sole writer.
- All new persistence is under `A2 Wanderer Evacuation Recovery Practice:*`.
- B2 state is read-only.
- Safe arrival remains distinct from restored transport/shelter/berth/staffing/maintenance capacity.
- Historical deficits do not become permanent active warnings without current evidence.
- Local reuse does not create Wanderer office, credential, endorsement, or representative authority.
- Refusal does not arm recurrence.

## Files
- `data/wanderer/a2 wanderer evacuation recovery practice.txt`
- `tools/story/validate_a2_wanderer_evacuation_recovery_practice.py`
- `story/A2_WANDERER_EVACUATION_RECOVERY_PRACTICE_HANDOFF_20260820.md`

## Validation requested
Focused validator:
`python3 tools/story/validate_a2_wanderer_evacuation_recovery_practice.py "data/wanderer/a2 wanderer evacuation recovery practice.txt"`

Repository-native gates before READY: focused story validator discovery/execution, changed-content style, A1 state-ownership/regression contracts, production configure/build, and stock save-load smoke. Actual-game acceptance should exercise all four briefing choices, refusal suppression, save/reload between briefing and recurrence, later strain `>= 3` recurrence, all three positive outcomes, one-shot suppression, and Wanderer offer precedence.

## A3 integration
Re-read current `main`, verify ancestry/conflicts, require exact-head terminal-green repository workflows, then integrate without changing A1/B2 ownership semantics.
