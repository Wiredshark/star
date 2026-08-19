# A1 Republic Customs Scrutiny handoff — 2026-08-19

## Domain

- `LOOP_ID`: A1
- `RUN_TYPE`: FEATURE
- `PRIMARY_DOMAIN`: crime / law / enforcement
- `SECONDARY_DOMAINS`: border security, persistent player history, dynamic narrative inputs
- `DIVERSITY_STATUS`: PASS
- `NEGLECTED_AREA_ADVANCED`: crime/law/enforcement after a logistics-heavy integration window
- `CROSS_SYSTEM_CONNECTION`: stock `pirate jobs` history + existing A1 Republic border pressure

## Production state

File: `data/human/a1 republic customs scrutiny.txt`

Authoritative A1-owned signal:

`world: republic customs scrutiny`

Bounds: `0..6`.

A qualifying direct Pirate -> Republic crossing requires at least three completed `pirate jobs`.

- When `world: republic border pressure < 4`, the crossing contributes `+1` scrutiny and schedules an exact `-1` decay seven days later.
- When border pressure is `>= 4`, the crossing contributes `+2` only while scrutiny is `< 5`, then schedules an exact `-2` decay seven days later.
- The `< 5` elevated gate prevents a saturated `5 -> 6` write from scheduling a later `-2` contribution that would over-decay the preexisting state.
- Both decays clamp at zero.
- A rate-limited notice is exposed at scrutiny `>= 3` and explicitly describes scrutiny as review posture rather than guilt.

## Authority boundaries

A1 reads but never writes:
- `pirate jobs`;
- `world: republic border pressure`.

The new file does not alter reputation, credits, cargo, combat rating, mission completion history, or law-enforcement penalties. It only owns `world: republic customs scrutiny` and its notice latch.

## Test

`tests/a1/test_republic_customs_scrutiny_model.py`

The test checks:
- exact production mission/event contract;
- absence of writes to both input authorities;
- no scrutiny before the pirate-history threshold;
- six routine contributions saturate at 6 and recover exactly to 0;
- three elevated contributions follow `0 -> 2 -> 4 -> 6` and recover `6 -> 4 -> 2 -> 0`;
- mixed routine/elevated pressure crosses the notice threshold without violating bounds;
- elevated contributions are suppressed at 5 while a routine `+1` can still fill the final unit;
- recovery cannot underflow.

The transition-model assertions were independently exercised during integration and passed. An exact repository checkout could not be obtained in the execution environment because `github.com` DNS resolution failed, so repository-side Python execution, content-style validation, normal Endless Sky parser/build, runtime, and save/load are not claimed.

## Next consumer

A2 may read `world: republic customs scrutiny` for investigation, due-process, legal-aid, or reputation-context dialogue. A2 must not clear or reduce scrutiny to manufacture a narrative resolution; only A1 decay owns recovery.
