# Endless Sky Story Repository

This directory is the durable narrative/worldbuilding lane for the evolving `Wiredshark/star` fork.

## Current files

- `AGENT_CONTRACT.md` — operating contract, canon levels, loop, and handoff standard.
- `WORLD_BIBLE.md` — confirmed baseline anchors and accepted story-canon world material.
- `RPG_CONTENT.md` — RPG backgrounds, traits, and their narrative/gameplay consequences.
- `DYNAMIC_STORY_LIBRARY.md` — reusable stories driven by world/simulation state.
- `BUILDER_HANDOFF.md` — implementation-ready queue for the gameplay-builder lane.
- `STORY_EVOLUTION_LOG.md` — persistent round history, seeds, continuity, and next pressures.

## Editing rule

Before adding new content, inspect the current game data and this directory. Prefer deepening or connecting existing material over introducing another faction, region, or character with a duplicate role.

Every substantial packet must state what can be authored with existing Endless Sky data support and what requires future builder/engine work.

## Validation

Run:

`python3 tools/story/validate_story_repo.py`

The validator checks that the durable repository exists, builder handoffs contain the mandatory contract sections, story rounds record a seed and required report headings, and substantial content distinguishes current and future implementation dependencies.
