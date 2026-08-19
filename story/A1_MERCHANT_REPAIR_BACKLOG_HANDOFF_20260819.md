# A1 Merchant Repair Backlog Handoff — 2026-08-19

- stage: A1
- authoritative base/integration SHA: `d485dea4c511964c1209d86dae15f5bcbf17a03b`
- isolated branch: `agent/a1-merchant-repair-backlog-20260819-0208`
- exact A1 commit SHA: `38daba4517d8c22dfc2f20438155b673f5820113`
- verdict: READY

## Increment

Adds a persistent Merchant repair/salvage-demand feedback loop that consumes the existing A1 `world: merchant rescue load` authority. Rescue load at 3+ creates bounded `world: merchant repair backlog` in +2 contributions with a three-day pressure window and six-day natural recovery. Once rescue load has fallen to 1 or less, a temporary yard surge can remove two backlog points, giving the loop explicit recovery hysteresis rather than allowing repair capacity to erase an active rescue crisis.

## Files / systems

- `data/human/a1 merchant repair backlog.txt`
- `tests/a1/test_merchant_repair_backlog.py`
- this durable handoff record

## Invariants and compatibility

- Existing `world: merchant rescue load` remains the sole upstream rescue-pressure authority and is read-only here.
- New persistent numeric state is bounded to `0..6`.
- Repair surge is blocked until rescue load is `<= 1`.
- Recovery clamps at zero; escalation clamps at six.
- No source/C++ save-format change. Conditions/events use the existing data-driven persistent-condition mechanism, so old saves with no new conditions retain the engine's normal unset/zero behavior.
- No A2/A3/B/C/D content is changed.

## Validation evidence

Executed in an isolated clean clone derived from the exact base SHA.

- `python3 tests/a1/test_merchant_repair_backlog.py` — PASS (`A1 Merchant repair-backlog hysteresis contract: PASS`).
- Direct execution of every `tests/a1/test_*.py` script — PASS for all nine A1 model/contract scripts present after this increment.
- `python3 tools/story/validate_fork_content_contracts.py` — PASS; 45 fork files, 10 A1 files, 132 missions, 17 events, 26 A1 world-condition writers; mission/event uniqueness, local goto labels, and A1 world-state ownership all passed.
- `python3 tools/story/validate_story_repo.py` — PASS.
- `python3 tools/story/check_changed_content_style.py --base d485dea4c511964c1209d86dae15f5bcbf17a03b --head HEAD` with the checker dependency isolated in scratch `PYTHONPATH` — PASS (`No issues found.`).
- `pytest -q tests/a1` could not be invoked because the host has no `pytest` executable; all A1 test scripts were therefore executed directly and passed.

Deterministic horizon evidence: the new model test runs 365 simulated days, with 180 days of sustained rescue crisis followed by durable low rescue load. It asserts backlog remains within `0..6`, no recovery surge occurs during acute rescue load, and backlog converges to zero during the recovery horizon.

## Save / persistence implications

Only new data-driven persistent conditions are introduced (`world: merchant repair backlog`, pressure/surge flags, notice flags). No binary save schema or C++ serializer is modified. Unset conditions on pre-existing saves naturally behave as zero/false under the same mechanism used by the existing A1 world-state files.

## Risks / deferred work

- No A2 narrative consumer is added here; later stages may read the repair-backlog signal without owning or mutating it.
- No A3 integration is performed here.
- A live interactive game-runtime mission-offer run was not available as a documented repository-native A1 gate in this execution path; data contracts, deterministic model behavior, cross-file ownership validation, and incremental style validation all passed.

## A3 integration instructions

Cherry-pick exact A1 commit `38daba4517d8c22dfc2f20438155b673f5820113` onto the then-current integration branch. Re-run the focused A1 tests, `validate_fork_content_contracts.py`, `validate_story_repo.py`, and the incremental changed-content style gate against the integration base. The only ordering dependency is the already-integrated Merchant rescue-load authority present in base `d485dea4c511964c1209d86dae15f5bcbf17a03b`.
