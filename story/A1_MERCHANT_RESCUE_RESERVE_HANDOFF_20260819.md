# A1 Merchant Rescue Reserve Strain handoff — 2026-08-19

- stage: A1
- authoritative base/integration SHA: `67203cc6d170f4961fd7cfe2374881453296fa04`
- isolated branch: `agent/a1-merchant-rescue-reserve-strain-20260819-1006`
- verdict: READY, subject to A3 exact-head repository-native validation noted below

## Increment

Adds a bounded Merchant rescue-reserve strain feedback loop. Existing `world: merchant rescue load` remains authoritative and read-only. Entering Merchant space while rescue load is elevated contributes temporary reserve strain; critical rescue load contributes twice as much. Every contribution schedules an equal ten-day recovery, so sustained demand is remembered while recovery converges exactly after demand subsides.

Owned state: `world: merchant rescue reserve strain`, bounded `0..4`, plus its notice latch.

- rescue load `<3`: no reserve-strain contribution;
- rescue load `3..4`: `+1` while strain `<4`, exact `-1` after 10 days;
- rescue load `>=5`: `+2` only while strain `<3`, exact `-2` after 10 days;
- the critical `<3` gate prevents a saturated `3 -> 4` write from scheduling a later two-point over-decay;
- recovery clamps at zero;
- notice threshold is strain `>=3` and does not alter economics, reputation, cargo, missions, or upstream rescue load.

## Files

- `data/human/a1 merchant rescue reserve.txt`
- `tests/a1/test_merchant_rescue_reserve_model.py`
- `story/A1_MERCHANT_RESCUE_RESERVE_HANDOFF_20260819.md`

## Invariants / compatibility

The slice never writes `world: merchant rescue load`. It owns only its new reserve-strain signal and notice latch. No stock save schema changes are required because Endless Sky conditions/events persist through the existing condition store. Missing historical state defaults to zero under the existing condition semantics.

## Validation

The focused Python model checks production contract text, upstream write isolation, low-load inactivity, bounded elevated/critical accumulation, exact scheduled recovery, mixed-load saturation behavior, underflow protection, and a representative 24-arrival sustained-pressure horizon that converges back to zero after scheduled recoveries.

Execution limitation: the only exposed private execution host is wired to `Wiredshark/fallout-test`, not authoritative `Wiredshark/star`, so host-side repository tests/build/runtime/save-load were deliberately not run against the wrong repository. A3 must run the repository-native focused test and normal simulation/story/save-load gates from the exact A1 commit before integration.

## A3 integration

Cherry-pick the exact A1 commit from `agent/a1-merchant-rescue-reserve-strain-20260819-1006` onto the then-current authoritative integration head. Before accepting, run `python3 tests/a1/test_merchant_rescue_reserve_model.py` plus the repository's A1/story validation, normal build/parser validation, and stock save-load smoke. Reject if another integrated slice has taken ownership of `world: merchant rescue reserve strain` or introduced an equivalent rescue-reserve feedback loop.

No A2/A3/B/C/D files or authorities are modified.
