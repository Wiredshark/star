# A2 Free Worlds Storm Navigation Doctrine — handoff

## Stage
A2 CORE RPG + DYNAMIC NARRATIVE

## Verdict
PARTIAL pending exact-head repository-native validation and actual-game acceptance.

## Authoritative base
`main` @ `8c61fb377068f6f8cc0d43876fbc15b99f95d6c0`

## Isolated branch
`agent/a2-free-worlds-storm-navigation-doctrine-20260819-2202`

## Scope
Consumes the newly integrated A1 Free Worlds geomagnetic-storm simulation as read-only narrative input.

The player meets traffic coordinator Rhea Solano while:
- `world: free worlds geomagnetic storm active` is set; and
- `world: free worlds geomagnetic navigation strain >= 3`.

The player chooses one of four policies:
1. verified-corridor doctrine;
2. independent cross-check doctrine;
3. local-autonomy doctrine;
4. explicit refusal.

Positive routes set only `A2 Free Worlds Storm Navigation Doctrine:*` conditions and mark a recovery boundary pending.

An invisible A2 boundary waits until the original disturbance has genuinely recovered:
- storm inactive; and
- navigation strain `<= 1`.

Only then is a future recurrence armed. A later storm with strain `>= 3` triggers one recurrence review. Each positive doctrine has a moderate-strain and severe-strain (`>= 5`) consequence, for six deterministic world-state-sensitive outcomes. Refusal remains respected and does not arm the recurrence loop.

## Dynamic feedback loop
`A1 storm + strain -> player doctrine -> full A1 recovery -> future A1 storm recurrence -> route-specific A2 consequence`

This deliberately prevents the recurrence reader from firing during the same initial disturbance.

## Ownership invariants
A1 remains sole writer of:
- `world: free worlds geomagnetic storm active`;
- `world: free worlds geomagnetic storm cooldown`;
- `world: free worlds geomagnetic storm advisory seen`;
- `world: free worlds geomagnetic strain advisory seen`;
- `world: free worlds geomagnetic navigation strain`.

This A2 slice reads only `storm active` and `navigation strain` and writes no `world:*` state.

All new persistence is confined to `A2 Free Worlds Storm Navigation Doctrine:*`.

The slice does not alter Rhea Solano's earlier Southern Rim traffic-coordination state.

## Files
- `data/human/a2 free worlds storm navigation doctrine.txt`
- `tools/story/validate_a2_free_worlds_storm_navigation_doctrine.py`
- `story/A2_FREE_WORLDS_STORM_NAVIGATION_DOCTRINE_HANDOFF_20260819.md`

## Focused validator contract
The focused validator checks:
- all three missions;
- Rhea Solano identity;
- active-storm and strain thresholds;
- three positive doctrines plus refusal;
- recovery boundary ordering;
- full-recovery arming condition;
- six recurrence outcomes plus refusal handling;
- refusal does not arm recurrence evaluation;
- zero writes to A1-owned storm/navigation state.

## Required validation before A3 integration
1. Run exact-head `Fork simulation and story validation` and require SUCCESS.
2. Run exact-head `Fork save-load integration smoke` and require SUCCESS.
3. In the actual game, prove the briefing appears only during active storm with strain >=3.
4. Exercise all three positive doctrine routes plus refusal.
5. Prove the recurrence review cannot occur during the same initial storm.
6. Prove the recurrence arm occurs only after storm inactive + strain <=1.
7. Exercise each positive doctrine under moderate recurrence strain and severe recurrence strain >=5.
8. Prove refusal does not schedule or imply a doctrine.
9. Save/reload between briefing, recovery boundary, and recurrence review.
10. Check offer precedence/regression with existing Free Worlds traffic and relief conversations.

## A3 integration instructions
Do not self-integrate. Re-read current `main`, verify ancestry/conflicts and exact-head workflow results, then integrate only if the candidate remains isolated and all required repository-native gates are green. Preserve A1 ownership exactly.
