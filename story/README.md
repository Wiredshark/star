# Endless Sky Story Repository

This directory is the durable narrative/worldbuilding lane for the evolving `Wiredshark/star` fork.

All recurring story/build agents inherit the repository-wide `../AGENT_BUILD_LOOP_POLICY.md`. That policy prevents A/B/C/D loops from repeatedly optimizing one subsystem and defines the mandatory run-domain labels, concentration exceptions, and A3 portfolio-balance handoff. The story-specific rules below are an additional specialization of that global policy.

## Current files

- `../AGENT_BUILD_LOOP_POLICY.md` — repository-wide anti-funneling policy for all A/B/C/D build loops.
- `AGENT_CONTRACT.md` — operating contract, canon levels, loop, diversity gates, and handoff standard.
- `NARRATIVE_DIVERSITY_POLICY.md` — mandatory anti-repetition policy for story premises, systemic inputs, and consequences.
- `WORLD_BIBLE.md` — confirmed baseline anchors and accepted story-canon world material.
- `RPG_CONTENT.md` — RPG backgrounds, traits, and their narrative/gameplay consequences.
- `DYNAMIC_STORY_LIBRARY.md` — reusable stories driven by world/simulation state across multiple narrative domains.
- `BUILDER_HANDOFF.md` — implementation-ready queue for the gameplay-builder lane.
- `STORY_EVOLUTION_LOG.md` — persistent round history, seeds, continuity, and next pressures.

## Editing rule

Before adding new content, inspect the current game data and this directory. Prefer deepening or connecting existing material over introducing another faction, region, or character with a duplicate role.

`NARRATIVE_DIVERSITY_POLICY.md` is mandatory, not advisory. New story work must deliberately diversify away from freight/logistics when recent packets already use that domain. Freight, cargo loss, shortages, convoy security, and market disruption are valid inputs, but they must not become the default structure for dynamic narrative.

Every substantial packet must state what can be authored with existing Endless Sky data support and what requires future builder/engine work. It must also include a `DIVERSITY_CHECK` identifying its primary narrative domain, the recent domains it avoids repeating, at least one non-economic world-state input where applicable, and the persistent consequence types it creates.

Receiving implementation/integration agents must preserve both layers of metadata: the story-specific `DIVERSITY_CHECK` and the repository-wide `PRIMARY_DOMAIN`, `RECENT_DOMAIN_WINDOW`, `DIVERSITY_STATUS`, `NEGLECTED_AREA_ADVANCED`, and `CROSS_SYSTEM_CONNECTION` run labels.

## Validation

Run:

`python3 tools/story/validate_story_repo.py`

The validator checks that the durable repository exists, builder handoffs contain the mandatory contract sections, story rounds record a seed and required report headings, and substantial content distinguishes current and future implementation dependencies.

A validator pass does not override either diversity policy. B1/B2/B3/A2/A3 handoffs should reject story packets that are technically valid but repeat the same freight/economic crisis structure without a documented regional reason, and A3 should carry any broader subsystem concentration debt into its `PORTFOLIO_BALANCE` report.
