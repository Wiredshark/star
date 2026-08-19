# A-Loop Modern Dialogue System

Status: **EXPLICIT USER PRIORITY / A-LOOP IMPLEMENTATION TARGET**

This document defines the required direction for upgrading Endless Sky's existing branching `conversation` support into a deeper, player-visible RPG dialogue system. It is a build target, not a request to replace the existing conversation data model without evidence.

A2 owns the primary RPG/dialogue implementation slice. A3 owns authoritative integration and must verify that the result is useful in the actual game. A1 should expose world-state inputs when the dialogue system needs real simulation facts rather than inventing duplicate narrative state.

This priority remains open until A3 has integrated at least one production dialogue vertical slice that satisfies the acceptance gate below.

## Goal

Preserve Endless Sky's existing conversation/content compatibility while making dialogue behave more like a modern systemic RPG:

- real branching trees with materially different routes;
- responses conditioned on persistent player/world/character history;
- visible skills, backgrounds, professions, reputation, legal status, relationships, prior decisions, and physical world outcomes where appropriate;
- consequences that can modify missions, relationships, access, reputation, world state, later dialogue, and future content;
- failure/decline/hostile/uncertain responses that create future state rather than forcing a single correct branch;
- clear player-facing indication of why special responses are available or unavailable, without revealing hidden information that the character could not know;
- compatibility with old saves and existing stock conversations.

The target is not merely a prettier conversation box. The important change is that dialogue becomes a first-class interface to the persistent RPG and living-world systems already being built.

## Design constraints

1. **Extend before replacing.** Inspect the existing `Conversation`, condition, mission, PlayerInfo, reputation, event, and save paths first. Prefer additive data syntax and reusable condition/effect primitives over a parallel dialogue database.
2. **Old content keeps working.** Stock Endless Sky conversations must parse and behave as before when they do not use new fields.
3. **No dialogue-only shadow truth.** If a response depends on freight loss, a survey, a crew casualty, a legal case, a mission outcome, a relationship, or another real system, read the authoritative state for that fact.
4. **Persistent consequences.** Important choices must survive save/load using established persistence paths or a deliberately versioned extension with safe defaults.
5. **No universal stat-check spam.** Special responses should appear when the character/background/skill/history actually changes the situation.
6. **Multiple valid approaches.** Avoid trees where one highlighted special response is always objectively best.
7. **Player legibility.** The player should understand whether a response is special because of a skill, relationship, background, reputation, evidence, prior action, or world condition when that knowledge is appropriate.
8. **Content-author friendly.** The syntax should be practical for large numbers of hand-authored conversations and later dynamic-story consumers.

## Required capabilities

The system should evolve toward the following capabilities. A single A2 round does not need to implement all of them, but each implementation slice must be reusable and move the project toward this contract.

### 1. Conditional response availability

A response may be gated by one or more existing or new reusable predicates, including:

- player background;
- profession/career/rank;
- player skill or competency tier;
- faction/government reputation;
- named-character relationship or professional memory;
- prior dialogue/mission choice;
- known evidence or discovery;
- survey/exploration state;
- legal/criminal state;
- cargo/outfit/ship state when narratively relevant;
- current system/planet/government;
- simulation/world state;
- persistent event/history flags.

Conditions should compose using the project's normal condition mechanisms where feasible.

### 2. Response presentation metadata

Special responses should be able to carry optional player-visible metadata such as:

- `[Background: Contract Spacer]`
- `[Engineering]`
- `[Republic Bonded Witness]`
- `[Dawn trusts your field judgment]`
- `[Evidence: Burthen Bow Echo]`
- `[Intimidate]`
- `[Lie]`
- `[Ask about prior promise]`

Presentation metadata must not itself become the authority for the check. It explains a condition that was evaluated elsewhere.

Support for disabled-but-visible options may be added when useful, but the content author must be able to choose between:

- hidden until known/eligible;
- visible but unavailable with a requirement hint;
- visible and selectable.

Do not expose spoilers or hidden NPC/world facts merely to explain an unavailable choice.

### 3. Checks and outcomes

Where probabilistic or threshold checks are appropriate, the system should support deterministic/save-safe resolution based on explicit game state rather than ad-hoc UI randomness.

Checks may produce more than pass/fail. Prefer outcomes such as:

- strong success;
- ordinary success;
- partial/compromised success;
- refusal;
- detected deception;
- relationship gain/loss;
- information gained without agreement;
- agreement at a cost;
- future obligation/debt;
- legal or faction consequence.

A deterministic threshold response is often preferable to randomness when the relevant capability is already known.

### 4. Persistent named-character memory

Dialogue should be able to read compact persistent states for named characters, using existing mission/condition persistence where sufficient and generalized character-memory primitives only when duplication is avoided.

Examples already relevant to the fork include:

- Dawn professional/practicum history;
- Nia Solberg legal/professional memory;
- Rill promise/commitment outcomes;
- Nadia Kelm / Elias Dorne New Washington history;
- Micah Rhee recovery/aftermath history.

The system must make it easier for later conversations to reference these histories without duplicating bespoke parsing logic for every character.

### 5. Consequence outputs

A dialogue choice should be able to trigger ordinary supported effects such as:

- mission branch/state changes;
- relationship/history updates;
- reputation changes;
- access/credential changes;
- credits/cargo/outfit effects where appropriate;
- legal/criminal consequences;
- settlement/service changes;
- news/log/history entries;
- future conversation availability;
- simulation-facing requests/effects only when there is a real authoritative write path.

Do not introduce a generic `dialogue world state` blob that competes with existing authorities.

### 6. Dialogue UI modernization

After the reusable state/branching slice works, improve the conversation UI incrementally so the new information is readable without abandoning Endless Sky's visual identity.

Desired presentation direction:

- clearer separation between NPC speech and player choices;
- readable multi-option response list;
- optional response tags/check labels;
- disabled/locked response treatment where intentionally exposed;
- keyboard/gamepad selection that remains usable;
- scrolling for larger trees;
- support for longer conversations without text collisions;
- optional speaker/relationship/context treatment only when it can be integrated cleanly;
- no requirement for portraits before the core dialogue system works.

A visual/UI change requires actual-game screenshot proof under the project's normal visual acceptance rules.

## A2 implementation requirement

When this user priority is selected, A2 should implement **one reusable engine/data capability plus one production conversation that exercises it**. Do not finish with a framework that has no real consumer.

A strong first vertical slice would:

1. reuse the current conversation parser/runtime;
2. add a small general mechanism for response requirement labels and/or richer conditional choices;
3. connect it to at least two existing persistent state sources;
4. author one multi-branch production conversation around an already integrated character or story;
5. make at least three meaningfully different player approaches available;
6. make at least one later conversation or mission state remember the choice;
7. survive save/load;
8. include focused automated tests plus the existing broad regression/parse/save gates.

Recommended early consumers are Dawn, Nia, Rill, New Washington, Micah, or another currently integrated persistent-character thread. Prefer whichever has the cleanest current authority and least overlap with active work.

## A3 integration requirement

A3 must not accept this feature merely because the parser compiles. Verify:

- exact specialist commit/base;
- stock conversation compatibility;
- production conversation actually reaches distinct branches;
- requirements shown to the player correspond to real evaluated state;
- locked/hidden behavior is correct;
- effects are durable;
- save/load roundtrip is exact or intentionally migrated;
- no duplicate character/world-state authority was introduced;
- the feature has a real later reader or consequence;
- broad actual-game and parser/story regression gates pass;
- UI is visually inspected if presentation changed.

A3 should record `DIALOGUE_SYSTEM_STATUS` as one of:

- `NOT_STARTED`
- `SPECIALIST_READY`
- `INTEGRATED_FOUNDATION`
- `INTEGRATED_PRODUCTION_SLICE`
- `BLOCKED_WITH_EVIDENCE`

The user-priority item is not considered satisfied before `INTEGRATED_PRODUCTION_SLICE`.

## Initial production-slice acceptance gate

The first accepted slice should satisfy all of the following:

- at least one real named NPC conversation in production content;
- at least 3 player response routes with materially different intent;
- at least 2 routes whose availability/text/result depends on persistent player/character/world state;
- at least 1 player-visible special-response requirement label;
- at least 1 choice creates a persistent consequence read later;
- a refusal/failure/non-optimal route remains valid content rather than a dead end requiring reload;
- old save compatibility verified;
- stock conversation parsing/regression verified;
- actual-game runtime exercised;
- actual-game screenshot required if UI rendering changed;
- no duplicate dialogue-only copy of authoritative simulation/relationship state.

## Follow-on pressures after the first slice

Once the production foundation is integrated, rotate later A2 rounds among:

- generalized skill/profession checks;
- backgrounds and origin-specific responses;
- relationship tiers and named-character memory;
- evidence/investigation dialogue;
- deception/intimidation/persuasion with consequences;
- faction/legal/political dialogue;
- world-state-aware dialogue and dynamic-story entry points;
- improved conversation UI/UX;
- authoring/validation tooling for large dialogue graphs;
- dialogue graph QA: unreachable nodes, contradictory gates, orphaned effects, missing later readers, and save migration.

Do not spend many consecutive A rounds on dialogue once a coherent foundation exists; return to normal portfolio rotation while continuing to use the system in new content.

## Cross-lane support

- **A1:** expose or reuse authoritative world/simulation state required by dialogue; do not create narrative shadow state.
- **A2:** primary dialogue/RPG implementation and production consumer.
- **A3:** authoritative integration, regression, persistence and player-visible acceptance.
- **B1/B2:** author characters, histories and dialogue-ready conflicts that exercise the system.
- **B3:** continuity audit and duplicate-state/character-role review.
- **D1:** architecture/data-ownership review.
- **D2:** dialogue graph, save/load, regression and cross-system QA.
- **D3:** reusable dialogue validation/graph inspection tooling when justified by actual authoring friction.
- **D4:** verify the user-priority acceptance gate and carry unresolved dialogue debt forward.

## Completion meaning

"Dialogue system implemented" must not mean only that Endless Sky already had branching conversations. Completion means the fork has a reusable, tested extension that exposes its new persistent RPG/world state through consequential player dialogue, with at least one integrated production conversation demonstrating the full loop.
