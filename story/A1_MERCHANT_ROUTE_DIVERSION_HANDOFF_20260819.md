# A1 Merchant Route Diversion handoff — 2026-08-19

## Stage and authority

- `stage`: A1
- `verdict`: READY
- `authoritative_base_used`: `fda6705d533559f31ea98a5f5e42e5b1d4e161af`
- `authoritative_main_after_concurrent_integration`: `709fb2bde2c63fdcaf1fe8d761427d6096220e28`
- `isolated_branch`: `agent/a1-merchant-route-diversion-20260819-0506-v2`
- `exact_a1_implementation_commit`: `12bc56d056d090d64545d8e5809238eb2b442abf`
- `draft_validation_pr`: `#72` (open, draft, mergeable, not merged)
- `superseded_failed_style_pr`: `#71` (closed, never merged; preserved evidence of the missing-header repair)

## Implemented world-simulation feedback slice

Adds persistent `world: merchant route diversion pressure` as a cross-system A1 signal that consumes, but never mutates, two existing authoritative A1 states:

- `world: merchant rescue load`
- `world: southern rim transit congestion`

One elevated upstream signal contributes `+1`; simultaneous elevated rescue load and congestion contribute `+2`. Accepted contributions schedule equal six-day decay, so every escalation has an exact recovery obligation. The diversion signal is bounded to `0..6`.

When both upstream pressures have receded to `<= 1` and diversion pressure remains `>= 4`, a four-day recovery latch allows dispatchers to remove two backlog units. This gives the slice explicit recovery hysteresis and prevents recovery capacity from erasing an active rescue/congestion crisis.

Feedback shape:

`rescue load / transit congestion -> route diversion pressure -> exact scheduled decay -> low-pressure dispatcher recovery`

A rate-limited notice exposes elevated diversion pressure without moving presentation or A2 narrative ownership into A1.

## Files changed in the implementation commit

- `data/human/a1 merchant route diversion.txt`
- `tests/a1/test_merchant_route_diversion.py`

Implementation blobs:

- data blob: `173d2de9028d3ba39e306c2e2d049cfbf990596d`
- test blob: `186470c76b584314cbbfce9499311416ae9aba6a`

The implementation commit contains only those two files relative to authoritative base `fda6705d533559f31ea98a5f5e42e5b1d4e161af`.

## Invariants and compatibility

- `world: merchant route diversion pressure` is bounded to `0..6`.
- Severe simultaneous pressure contributes exactly two units only when two units fit; it does not saturate by two and later over-decay.
- Moderate pressure contributes exactly one unit when only one upstream authority is elevated.
- Every accepted `+1` contribution schedules one six-day `-1` decay; every accepted `+2` schedules one six-day `-2` decay.
- Dispatcher recovery requires both upstream authorities to be `<= 1`, diversion pressure `>= 4`, and no recovery latch already active.
- Recovery subtracts two and clamps at zero.
- Existing Merchant rescue load and Southern Rim transit congestion are read-only inputs in this slice.
- No A2, A3, B, C/remaster, or D state is written.
- No C++ save schema is changed. New ordinary Endless Sky conditions default to unset/zero on old saves, so no migration is required.
- Standard Endless Sky GPL content header is present and passed the blocking changed-content style gate.

## Validation evidence

### Isolated local contract execution

Executed against byte-identical staged implementation contents before publication:

- `python3 tests/a1/test_merchant_route_diversion.py`
  - PASS: `A1 Merchant route-diversion contract: PASS`

The model includes deterministic accelerated horizons of 30, 180, and 720 simulated days. Each horizon is run twice and traces must match exactly. Assertions enforce `0 <= diversion pressure <= 6`; 180- and 720-day crisis/recovery runs converge to zero after upstream pressure clears.

### Repository-native GitHub Actions on draft PR #72

Commit under test: `12bc56d056d090d64545d8e5809238eb2b442abf`.

`Fork simulation and story validation`, run `32236393627`, conclusion: SUCCESS.

Successful steps include:

- `python -m compileall -q tools/story tests/a1`
- `python tools/story/run_focused_validators.py`
- `python -m pytest -q tests/a1`
- `python tools/story/check_changed_content_style.py --base "$BASE_SHA" --head "$HEAD_SHA"`

Both jobs passed:

- `Focused simulation and story contracts` — SUCCESS
- `Changed fork content style` — SUCCESS

`Fork save-load integration smoke`, run `32236393768`, conclusion: SUCCESS.

Successful steps include:

- dependency installation
- production executable configuration
- production executable build
- stock save-load smoke cases

The PR merge ref was generated against concurrently advanced main `709fb2bde2c63fdcaf1fe8d761427d6096220e28`; PR #72 reports `mergeable: true`. This is forward-compatibility evidence only and is not an integration action.

### Repair history

Initial implementation commit `139f8aec17b5c1f1d0fbb45a7d3f9097cf4bd73a` on the non-v2 branch passed focused simulation/story/A1 tests but failed the blocking style gate solely because the new data file lacked the repository-standard GPL header. That branch was not rewritten. Draft PR #71 was closed unmerged. A fresh v2 branch was created from the same authoritative base with only the required header correction, producing final implementation SHA `12bc56d056d090d64545d8e5809238eb2b442abf`, which passed all native CI listed above.

## Persistence implications

The new numeric state and notice/recovery latches are ordinary condition values. Existing saves lacking them begin at the engine's normal zero/unset semantics. Scheduled decay events exist only after new qualifying arrivals. Repository-native stock save/load smoke passed on the validated PR merge ref.

## Known risks / intentionally deferred work

- Diversion pressure is an A1 observability/state signal; it does not directly alter commodity prices, fleet spawning, credits, mission payouts, or reputation in this slice.
- Earth is used as the existing synchronization destination pattern for this A1 family rather than generalizing the trigger to every Merchant or Free Worlds port.
- No A2 dialogue/news consumer is added here. Later narrative work may consume `world: merchant route diversion pressure` read-only.
- Concurrent main advancement after the run began is intentionally not rebased or merged into this branch. A3 should integrate the exact implementation SHA onto the then-current authoritative main and rerun gates.

## A3 integration instructions

Integrate only exact implementation commit `12bc56d056d090d64545d8e5809238eb2b442abf` onto the then-current authoritative integration branch. Do not integrate superseded commit `139f8aec17b5c1f1d0fbb45a7d3f9097cf4bd73a` and do not treat this handoff record as gameplay content.

After integration, rerun at minimum:

- `python tools/story/run_focused_validators.py`
- `python -m pytest -q tests/a1`
- `python tools/story/check_changed_content_style.py --base <integration-parent> --head <integration-head>`
- production build / stock save-load integration smoke

No ordering dependency exists beyond the already-present authoritative inputs `world: merchant rescue load` and `world: southern rim transit congestion`.

## Verdict

READY. The final implementation is isolated, bounded, deterministic under accelerated horizons, persistence-compatible, mergeable against the newer concurrent main seen during validation, and green under repository-native focused validation, A1 pytest, blocking content-style, production build, and stock save/load smoke.