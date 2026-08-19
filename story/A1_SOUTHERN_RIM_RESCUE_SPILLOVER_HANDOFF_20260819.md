# A1 Southern Rim Congestion -> Merchant Rescue Spillover Handoff

- Stage: A1
- Verdict: READY
- Authoritative base/integration SHA: `6dc761ac941794c8b1125978d7bcd6eb811e3951`
- Isolated branch: `agent/a1-congestion-rescue-spillover-20260819-1104`
- A1 implementation commit SHA: `7b07a9af1db36c9145f045da3f4c1618f69e2d93`
- Validation PR: `#94` (draft; do not self-merge)

## Increment

Adds a bounded one-way feedback loop from accepted Southern Rim transit congestion into accepted Merchant rescue load. When congestion is severe (`>= 4`), a qualifying Merchant-system arrival can add one rescue-load point, capped at the existing rescue maximum of 5. A six-day latch prevents rapid re-amplification. The bridge schedules the existing five-day Merchant rescue recovery event, so downstream decay remains owned by the accepted rescue system. Southern Rim congestion is read-only in the bridge.

## Files

- `data/human/a1 southern rim rescue spillover.txt`
- `tests/a1/test_southern_rim_rescue_spillover.py`

## Invariants and compatibility

- Does not mutate `world: southern rim transit congestion`.
- Reuses `world: merchant rescue load` and its existing cap/recovery event instead of creating parallel rescue truth.
- Adds only one new latch condition: `world: southern rim rescue spillover active`.
- No source-code or save-schema changes; conditions follow existing data-driven persistent world-state behavior and default absent/zero semantics.
- No A2/A3/B/C/D content is changed.

## Validation evidence

GitHub Actions on implementation SHA `7b07a9af1db36c9145f045da3f4c1618f69e2d93`:

1. `Fork simulation and story validation` run `32268237409`: SUCCESS.
   - `python -m compileall -q tools/story tests/a1`: success.
   - `python tools/story/run_focused_validators.py`: success.
   - `python -m pytest -q tests/a1`: success, including threshold/cap/latch, read-only upstream contract, quiet recovery, and deterministic three-year horizon coverage for this bridge.
   - `python tools/story/check_changed_content_style.py --base "$BASE_SHA" --head "$HEAD_SHA"`: success.
2. `Fork save-load integration smoke` run `32268237275`: SUCCESS.
   - Production configure: `cmake -S . -B build/fork-save-load -G Ninja -DES_USE_VCPKG=OFF -DBUILD_TESTING=OFF -DCMAKE_BUILD_TYPE=Release`.
   - Production build: `cmake --build build/fork-save-load --config Release --target EndlessSky --parallel 2`.
   - Stock headless save/load cases all succeeded: `Saving during conversation`, `Loading and Reloading`, `Loading and Saving`.

Deterministic horizon: test models 3 years (`365 * 3` days) with recurring congestion stress windows, representative qualifying arrivals, six-day latch behavior, five-day rescue recovery cadence, hard rescue-load bound `0..5`, and a quiet tail that drains to zero.

## Risks / deferred

- The bridge intentionally models systemic spillover, not per-vessel casualty accounting.
- Trigger geography is Merchant government space while reading the global Southern Rim congestion signal; later A3 should preserve this as the abstraction boundary unless repository geography contracts are deliberately tightened.
- No reciprocal Merchant-rescue -> congestion feedback is added in this slice to avoid a positive feedback cycle.

## A3 integration instructions

Integrate/cherry-pick implementation commit `7b07a9af1db36c9145f045da3f4c1618f69e2d93` onto the then-current authoritative integration head. Re-run the focused simulation/story validation and save-load smoke on the resulting exact head. Before integration, verify no newer A1 bridge already connects `world: southern rim transit congestion` to `world: merchant rescue load`; if one exists, reject this commit as superseded rather than duplicating the loop.

ES4_NEXT_STAGE_CONTEXT_BEGIN
A1 implementation SHA `7b07a9af1db36c9145f045da3f4c1618f69e2d93` is READY from base `6dc761ac941794c8b1125978d7bcd6eb811e3951`. It adds only a one-way severe Southern Rim congestion -> Merchant rescue-load contribution, capped at 5 and rate-limited by a six-day latch; congestion remains read-only. GitHub Actions runs `32268237409` and `32268237275` both succeeded. A3 must re-check for superseding overlap and re-run both gates on its exact integration head.
ES4_NEXT_STAGE_CONTEXT_END
