# Endless Sky Story Evolution Agent Contract

This directory implements the durable world-and-story content lane for `Wiredshark/star`.

## Role

The story lane is responsible for implementation-ready worldbuilding, narrative systems design, RPG content, persistent characters, faction depth, dynamic story templates, world-generation content packets, rumors/news, continuity, and builder handoffs. It is not the primary gameplay-programming lane.

## Core loop

Each story round follows:

**INSPECT -> RECOVER CONTINUITY -> AUDIT DOMAIN MIX -> IDENTIFY GAPS -> RNG PRESSURE -> SELECT -> EXPAND -> CONNECT -> WRITE -> DIVERSITY CHECK -> VALIDATE CONTINUITY -> PACKAGE FOR BUILDER -> RECORD**

Rounds are cumulative. Existing canon is preserved unless a deliberate retcon is recorded.

## Principles

1. The world existed before the player and continues without them.
2. Important NPCs have independent trajectories.
3. Factions contain internal politics and competing interests.
4. Economics, war, migration, exploration, crime, politics, relationships, law, culture, environment, ownership, and discovery can all create human consequences.
5. Story consumes world state and, where implementation permits, changes world state.
6. Mission failure can create new story instead of merely ending content.
7. History, rumors, witnesses, institutions, and factions can remember player actions.
8. Generated locations require origin, history, occupants, ownership, salvage, danger, legal status, faction interest, and follow-up hooks where relevant.
9. New lore is not considered useful merely because it is imaginative; it must have an implementation path.
10. Existing Endless Sky data is authoritative for names and implemented mechanics unless a builder change proves otherwise.
11. Freight/logistics is one narrative domain, not the default dynamic-story template.
12. New content must demonstrate domain diversity according to `NARRATIVE_DIVERSITY_POLICY.md`.

## Mandatory narrative-diversity gate

`NARRATIVE_DIVERSITY_POLICY.md` is part of this contract.

Before selecting a new substantial story packet, inspect at least the two most recently authored or implemented packets and identify their primary narrative domains.

A new packet must not use freight, cargo loss, shortages, convoy escort, trade-route security, or market disruption as its primary conflict if either of the two most recent packets already used one of those as a primary conflict.

Across the active implementation-ready backlog, no single narrative domain should exceed one third of packets unless a regional arc deliberately requires concentration and the handoff records the reason.

Each substantial packet must use at least two meaningful world-state inputs. Unless the packet is explicitly economic, at least one input must come from outside the economy/freight domain.

Valid non-economic inputs include faction control, diplomacy, war state, crime pressure, law/enforcement posture, population movement, NPC relationships, player reputation, discoveries, ownership, governance, environmental conditions, character survival/location, ideology, prior testimony/evidence, and previous player choices.

Consequences must also diversify. Do not reduce every outcome to credits, commodity supply, freight capacity, or security-fleet intensity. Persistent relationships, faction control, legal status, access, NPC roles, location state, discoveries, governance, war/diplomacy, migration, future dialogue, and mission availability are equally valid outputs.

Every substantial packet and every builder handoff must contain a `DIVERSITY_CHECK` that states:

- primary narrative domain;
- two recent packet domains considered;
- non-economic world-state inputs used;
- how the premise differs structurally from recent freight/logistics stories;
- persistent consequence types created.

If the check exposes a reskinned freight crisis, revise the packet before handoff.

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

Continuity overrides incoherent randomness. Diversity overrides repeatedly selecting the same convenient subsystem: if recent rounds cluster around economy/freight, reroll or deliberately select a different category.

## Required substantial-packet metadata

Substantial packets must identify:

- required existing systems;
- required future systems;
- data that can be authored now;
- engine support needed;
- world-state inputs;
- world-state outputs;
- primary narrative domain;
- `DIVERSITY_CHECK`.

## Builder handoff standard

Every active handoff must contain these sections:

- CONTENT ID
- TYPE
- NARRATIVE DOMAIN
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
- DIVERSITY_CHECK
- PRIORITY

## Canon levels

- **BASELINE_CANON**: already present in the checked-in Endless Sky data.
- **STORY_CANON**: accepted durable story-lane material not yet implemented in game data.
- **PROPOSED**: design material requiring continuity review or builder support.
- **IMPLEMENTED**: verified in game data/source by the builder lane.
- **RETIRED**: intentionally removed or superseded, with reason recorded.

Story documents must not claim a proposed mechanic is implemented.
