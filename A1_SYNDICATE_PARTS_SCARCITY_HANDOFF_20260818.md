# A1 handoff: Syndicate parts scarcity

- stage: A1
- authoritative base/integration SHA used: b448e0f977ee37535c49243d616045b3efef9772 (`origin/main` at run start)
- isolated branch: `agent/a1-syndicate-parts-scarcity-20260818-2008`
- isolated host worktree: `/opt/agent-workspace/renderer-admin-scratch/a1-syndicate-parts-scarcity-20260818-2008`
- exact A1 implementation commit: `581e1aa801c8fd4d8fa051bbc93e77a72eeed1a9`
- verdict: READY

## Implemented feedback loop

Deepens the existing Syndicate industrial-maintenance loop. When a maintenance mobilization consumes backlog, it now creates persistent `world: syndicate parts scarcity` (+2, capped at 6). Two scheduled recovery events remove one scarcity unit after 4 and 8 days, while an independent Syndicate assisting flow can relieve scarcity one unit at a time. Emergency maintenance therefore carries a remembered second-order resource cost instead of erasing strain without consequence.

## Key files

- `data/human/a1 syndicate maintenance backlog.txt`
- `tests/a1/test_syndicate_maintenance_backlog.py`

## Invariants and compatibility

- Existing maintenance backlog remains bounded 0..6.
- New parts scarcity remains bounded 0..6 and clamps at zero on recovery/relief.
- Existing surge lockout and six-day surge lifetime are unchanged.
- The new state uses the existing persistent numeric-condition mechanism. Old saves have no stored value for this condition and therefore begin from the normal zero/default state; no migration is required.
- No A2, A3, B, C/remaster, or D behavior was changed.

## Test and validation evidence

PASS:

- `python3 tests/a1/test_border_pressure_model.py`
- `python3 tests/a1/test_free_worlds_defense_strain.py`
- `python3 tests/a1/test_relief_demand_model.py`
- `python3 tests/a1/test_syndicate_maintenance_backlog.py`
- `python3 tests/a1/test_transit_congestion_model.py`
- `git diff --check`

The focused model exercises repeated backlog accumulation, surge gating, successive mobilizations, scarcity cap behavior, independent relief, and long-horizon recovery back to zero. The host did not provide a `pytest` executable on PATH, so the repository's A1 Python contracts were executed directly.

A full Release build was also attempted with:

- `cmake -S . -B .a1-build -G Ninja -DCMAKE_BUILD_TYPE=Release`
- `cmake --build .a1-build -j2`

Compilation progressed through executable/test linking, but GCC 13 LTO terminated with an internal compiler error (`lto-wrapper` / linker failure). This is recorded as an environment/compiler failure, not a passing build and not a simulation-test failure. Generated build artifacts were removed and run-owned build processes were cleaned up.

## Persistence implications

`world: syndicate parts scarcity` is persistent world state, bounded 0..6. It decays through scheduled four-day/eight-day recovery events and can also be reduced by qualifying Syndicate assistance. Existing saves need no explicit migration.

## Known risks / deferred work

- A2 may consume `world: syndicate parts scarcity` for dialogue, news, mission weighting, or other RPG consequences; that narrative work is intentionally outside A1.
- A3 should repeat the repository's normal full build/CI on its integration environment because this run's Release build was interrupted by a GCC 13 LTO compiler ICE.

## A3 integration instructions

Cherry-pick exact implementation commit `581e1aa801c8fd4d8fa051bbc93e77a72eeed1a9`. It is based directly on `b448e0f977ee37535c49243d616045b3efef9772`, which already contains the original Syndicate maintenance-backlog/surge slice. Preserve that ordering. The handoff documentation commit itself is not required for gameplay integration.
