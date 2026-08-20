# A2 dialogue lifecycle cleanup handoff - 2026-08-20

## Verdict

**PARTIAL pending exact-head repository validation.**

## Authority

- Repository: `Wiredshark/star`
- Base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-dialogue-lifecycle-cleanup-20260820`

## Defect

Endless Sky's conversation `accept` endpoint is mission lifecycle, not a generic successful close. `PlayerInfo::MissionCallback(Endpoint::ACCEPT)` moves an offered mission into the player's accepted mission list.

Three integrated A2 dialogue-only slices wrote their intended persistent state and then used `accept` despite having no cargo, destination, waypoint, completion objective, or other gameplay mission lifecycle. The result can be inert accepted-mission entries that never had an objective to complete.

## Repair

Changed only standalone conversation endpoints from `accept` to `decline` after their existing state actions in:

- `data/human/a2 deep field review.txt`
- `data/human/a2 deep security debrief.txt`
- `data/human/a2 free worlds patrol doctrine.txt`

No dialogue text, branching, conditions, state names, state values, A1 ownership, or later-reader semantics were changed.

Added `tools/story/validate_a2_dialogue_lifecycle.py`. The guard scans A2 mission blocks and rejects `accept` only when the mission has no real gameplay objective. Legitimate future A2 missions with cargo/passengers/destination/waypoint/stopover/NPC/timer/deadline/completion/enter/land/boarding/assisting lifecycle remain allowed to accept normally.

## Regression evidence required

Before integration:

1. `Fork simulation and story validation` must be terminal SUCCESS on the exact final head, including the new lifecycle guard.
2. `Fork save-load integration smoke` must be terminal SUCCESS on the exact final head.
3. Re-read `main` and recheck mergeability because concurrent A2 runtime-acceptance work is active.

## Invariants

- This is lifecycle cleanup only; no A1/B1/B2 authority moves.
- Existing A2 persistent condition names and values are unchanged.
- Refusal behavior remains refusal.
- Positive dialogue choices continue to write the same A2 state before closing.
- Later readers continue to consume the same pending/route state.
