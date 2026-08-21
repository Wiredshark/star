# A2 Wanderer Evacuation Recovery Practice restage handoff

## Stage / verdict
- Stage: A2 CORE RPG + DYNAMIC NARRATIVE
- Verdict: PARTIAL pending exact-head repository-native workflow completion.
- No self-integration. A3 retains integration authority.

## Repository authority
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-wanderer-evacuation-practice-restage-20260821-0812`
- Production restage: `56b267074d2c0cb54a69d3fcbc886d01b1d527aa`
- Focused validator: `e2e92d93dab1b47db062f8e838be4f5b652ba91b`

This clean current-main restage supersedes the stale lifecycle form of PR #192 without modifying, rebasing, or force-updating that historical branch.

## RPG / narrative loop
After `B2 Wanderer Evacuation Recovery Compact: aftermath seen`, and only while authoritative A1 evacuation logistics strain is recovered to `<= 1`, the player may adopt closure-evidence discipline, current-capacity review, local/context-only reuse, or explicit refusal. Positive choices persist. A later authoritative A1 evacuation recurrence at strain `>= 3` produces a one-shot history-aware consequence for the chosen practice.

Feedback chain: `A1 evacuation strain -> B2 recovery settlement/aftermath -> A2 player practice during recovery -> later A1 evacuation recurrence -> A2 consequence`.

## Restage repairs
- Rebased by clean restage from current authoritative main rather than rewriting the old PR branch.
- Added the repository-standard GPL header to changed production and validator files.
- Repaired all objective-less state-only dialogue endings: three positive Briefing outcomes and the Recurrence outcome now record the same persistent state and terminate with `decline`; refusal already uses `decline`.
- Added `offer precedence 9` to both state-only missions to make their offer ordering explicit and deterministic relative to other Wanderer narrative content.
- Strengthened the focused validator to reject A1/B2 writes, reject state-only `accept`, require exactly five `decline` terminals, require both offer-precedence declarations, and retain the original recurrence/refusal contracts.

## Invariants
- `world: wanderer evacuation logistics strain` is read-only; A1 remains sole writer.
- All `B2 Wanderer Evacuation Recovery Compact:*` conditions are read-only.
- All new persistence is under `A2 Wanderer Evacuation Recovery Practice:*`.
- Safe arrival remains distinct from restored transport/shelter/berth/staffing/maintenance capacity.
- Historical deficits do not become permanent active warnings without current evidence.
- Local reuse does not create Wanderer office, credential, endorsement, or representative authority.
- Refusal does not arm recurrence.
- State-only dialogue missions must not remain in the accepted-mission list.

## Files
- `data/wanderer/a2 wanderer evacuation recovery practice.txt`
- `tools/story/validate_a2_wanderer_evacuation_recovery_practice.py`
- `story/A2_WANDERER_EVACUATION_RECOVERY_PRACTICE_RESTAGE_HANDOFF_20260821.md`

## Validation requested
Focused validator:
`python3 tools/story/validate_a2_wanderer_evacuation_recovery_practice.py "data/wanderer/a2 wanderer evacuation recovery practice.txt"`

Repository-native gates before READY: focused story validator discovery/execution, changed-content style, A1 state-ownership/regression contracts, production configure/build, and stock save-load smoke. Optional actual-game acceptance may still exercise all four briefing choices, refusal suppression, save/reload between briefing and recurrence, later strain `>= 3` recurrence, all three positive outcomes, one-shot suppression, and Wanderer offer precedence.

## A3 integration
Re-read current `main`, verify ancestry/conflicts, require exact-head terminal-green repository workflows, then review/integrate only this current-main restage while preserving A1/B2 ownership and the state-only dialogue lifecycle invariant.
