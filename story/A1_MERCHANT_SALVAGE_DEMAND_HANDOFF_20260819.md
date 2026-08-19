# A1 Merchant salvage-demand handoff

**Stage:** A1 CORE WORLD SIMULATION  
**Verdict:** PARTIAL pending exact-head repository-native validation  
**Authoritative base:** `45841e29941fb0b720031a4c0cbc70e8bc32c890`  
**Isolated branch:** `agent/a1-merchant-salvage-demand-20260819-1210`  
**A1 production/test commit:** `8696742e62eb13839e25cb6b0e01661cbff4be1b`

## Implemented simulation loop

Sustained Merchant rescue-network overload now propagates into a separate persistent `world: merchant salvage demand` signal. A qualifying Earth arrival requires `world: merchant rescue load >= 3`, salvage demand below its cap, and no active latch. Activation increments salvage demand by one, caps it at four, schedules deterministic recovery eight days later, and rate-limits further activation for five days.

This gives downstream A2/A3 systems a bounded repair/salvage scarcity signal without changing the accepted rescue-load producer or recovery semantics.

## Files

- `data/human/a1 merchant salvage demand.txt`
- `tests/a1/test_merchant_salvage_demand.py`
- `story/A1_MERCHANT_SALVAGE_DEMAND_HANDOFF_20260819.md`

## Invariants and compatibility

- `world: merchant rescue load` is read-only in this slice.
- `world: merchant salvage demand` is bounded to `[0, 4]`.
- One activation is permitted per five-day latch window.
- Every activation schedules exactly one eight-day decrement, clamped at zero.
- Quiet rescue state cannot manufacture new salvage demand after latch release.
- No A2, A3, B, C/remaster, or D state is written.
- State uses normal Endless Sky conditions/events, so persistence follows existing condition/event save behavior; no save-format migration is introduced.

## Validation contract

Focused test coverage asserts source ownership, threshold/cap/latch behavior, quiet recovery, and a deterministic three-year stress horizon with repeated overload/quiet seasons. The test requires salvage demand to remain bounded throughout and drain to zero on a quiet tail.

The currently exposed private execution host was inspected but its repository workspace is an unrelated Fallout checkout, not `Wiredshark/star`. No Endless Sky host-side runtime/build result is claimed from that environment.

## A3 integration instructions

Integrate only the exact production/test commit `8696742e62eb13839e25cb6b0e01661cbff4be1b` plus this handoff after repository-native validation is green. Preserve the rescue-load read-only boundary and the five-day latch/eight-day recovery relationship. No ordering dependency exists beyond requiring the already-integrated `data/human/a1 merchant rescue load.txt` state producer present on the authoritative base.

## Deferred / risk

Actual-game observation of the Earth-entry trigger and save/reload across an outstanding recovery event remains an integration acceptance check if repository-native save-load CI does not exercise scheduled A1 events directly.
