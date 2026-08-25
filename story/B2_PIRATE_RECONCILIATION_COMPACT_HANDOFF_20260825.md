# B2 Pirate Reconciliation Compact — handoff

Verdict: PARTIAL pending exact-head repository-native validation.

## Authority
- repository: `Wiredshark/star`
- authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- branch: `agent/b2-pirate-reconciliation-compact-20260825`
- production commit: `ea36933d98360f4e1f8c42b5034de17d3451021f`
- focused validator commit: `5b67387b28ece445b56f97ed3a890efac1635557`

## Character / dynamic-content behavior
Adds former pirate crewmates Ressa Vale and Kade Orin in a three-mission relationship arc. A failed boarding left Ressa stranded after Kade obeyed a retreat order. Kade has apologized; Ressa may forgive him without restoring the old operational relationship.

Offer routes:
1. apology stands without entitlement to forgiveness, friendship, or renewed access;
2. changed behavior may matter as evidence without purchasing forgiveness;
3. personal forgiveness and operational trust are explicitly separate;
4. refusal, which does not arm Review.

The three substantive routes schedule a 7–11 day Review. A later joint-job assumption tests whether visible reconciliation becomes automatic crew trust. Review resolves into either fresh job-specific trust or gradual bounded trust. `Ressa Remembers` is a one-shot aftermath reader.

## RPG / history dependencies
- reads existing vanilla `pirate jobs` history only (`> 2`) to ensure the player has meaningful Pirate-facing experience;
- `pirate jobs` remains read-only;
- no `world:*`, B1, A1, A2, material, reputation, cargo, equipment, ship, fleet, combat, or government-attitude writes.

## Persistence / lifecycle
All new writes are namespaced under `B2 Pirate Reconciliation Compact:*`.

The focused validator proves:
- exactly three missions;
- exactly three substantive Offer routes plus refusal;
- route-local `introduced`, route-state, delayed Review scheduling, and terminal behavior;
- refusal cannot introduce or schedule Review;
- exactly two Review settlements with settlement-local writes and one Review closure each;
- one-shot aftermath consuming either settlement;
- all seven dialogue/state-only terminal paths use `decline`;
- no gameplay-objective or material-reward directives;
- `pirate jobs` remains read-only;
- no centralized Pirate law/office/code is introduced.

## Canon / continuity assumptions
This is one personal relationship, not a Pirate institution. Apology, forgiveness, friendship, operational trust, changed behavior, job-specific consent, and future crew authority are distinct facts. Changed behavior can matter without buying forgiveness. Forgiveness can be genuine without restoring operational trust. A repaired friendship does not automatically recreate a prior crew partnership.

## Process / integration boundary
The separate global B2 dialogue-lifecycle audit was observed and left untouched. Four pre-existing service-owned host processes were observed and preserved. No destructive Git operation or self-integration is authorized from B2.

## Validation required for READY
- Fork simulation and story validation on the exact production/validator/handoff candidate;
- focused story validator discovery/execution;
- A1 simulation/state-ownership contracts;
- changed-content style;
- Fork save-load integration smoke on the same exact candidate, including production configure/build and stock save-load smoke;
- final base/head isolation and mergeability recheck.

A3 retains integration authority.
