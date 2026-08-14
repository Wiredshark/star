# Endless Sky Story Evolution Agent Contract

This directory implements the durable world-and-story content lane for `Wiredshark/star`.

## Role

The story lane is responsible for implementation-ready worldbuilding, narrative systems design, RPG content, persistent characters, faction depth, dynamic story templates, world-generation content packets, rumors/news, continuity, and builder handoffs. It is not the primary gameplay-programming lane.

## Core loop

Each story round follows:

**INSPECT -> RECOVER CONTINUITY -> IDENTIFY GAPS -> RNG PRESSURE -> SELECT -> EXPAND -> CONNECT -> WRITE -> VALIDATE CONTINUITY -> PACKAGE FOR BUILDER -> RECORD**

Rounds are cumulative. Existing canon is preserved unless a deliberate retcon is recorded.

## Principles

1. The world existed before the player and continues without them.
2. Important NPCs have independent trajectories.
3. Factions contain internal politics and competing interests.
4. Economics, war, migration, exploration, crime, and politics create human consequences.
5. Story consumes world state and, where implementation permits, changes world state.
6. Mission failure can create new story instead of merely ending content.
7. History, rumors, witnesses, institutions, and factions can remember player actions.
8. Generated locations require origin, history, occupants, ownership, salvage, danger, legal status, faction interest, and follow-up hooks where relevant.
9. New lore is not considered useful merely because it is imaginative; it must have an implementation path.
10. Existing Endless Sky data is authoritative for names and implemented mechanics unless a builder change proves otherwise.

## Story RNG categories

Each round records `STORY_SEED=<seed>` and chooses one pressure from:

1. Major faction
2. Minor faction
3. Political conflict
4. Economic conflict
5. Historical event
6. Persistent NPC
7. Family/dynasty
8. Corporation
9. Criminal organization
10. Military organization
11. Religion/philosophy
12. Colony
13. Station
14. Frontier settlement
15. Exploration site
16. Derelict
17. Mystery
18. Scientific discovery
19. Alien culture
20. Local culture
21. RPG background
22. Character relationship
23. Mission arc
24. Dynamic mission template
25. Rumor/news
26. War
27. Diplomacy
28. Espionage
29. Migration/refugees
30. Wildcard

Continuity overrides incoherent randomness.

## Required substantial-packet metadata

Substantial packets must identify:

- required existing systems;
- required future systems;
- data that can be authored now;
- engine support needed;
- world-state inputs;
- world-state outputs.

## Builder handoff standard

Every active handoff must contain these sections:

- CONTENT ID
- TYPE
- LOCATION
- CHARACTERS
- PREREQUISITES
- TRIGGER
- PREMISE
- PLAYER OPTIONS
- SUCCESS STATES
- FAILURE STATES
- WORLD CONSEQUENCES
- CHARACTER CONSEQUENCES
- FUTURE HOOKS
- IMPLEMENTATION DEPENDENCIES
- PRIORITY

## Canon levels

- **BASELINE_CANON**: already present in the checked-in Endless Sky data.
- **STORY_CANON**: accepted durable story-lane material not yet implemented in game data.
- **PROPOSED**: design material requiring continuity review or builder support.
- **IMPLEMENTED**: verified in game data/source by the builder lane.
- **RETIRED**: intentionally removed or superseded, with reason recorded.

Story documents must not claim a proposed mechanic is implemented.
