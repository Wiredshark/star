# Agent Build-Loop Diversity Policy

This policy applies to every project agent lane and every recurring build/evolution loop in `Wiredshark/star`.

## Purpose

Agent loops naturally converge on the first subsystem that produces measurable progress. That is useful for debugging, but harmful as a long-term development strategy: repeated local optimization can make the whole project appear active while large parts of the game remain untouched.

The project therefore requires **portfolio diversity** across simulation, RPG/story, worldbuilding, visuals, architecture, QA, and tooling. Depth is still allowed; accidental funneling is not.

Correctness, regressions, save compatibility, blockers, broken builds, and acceptance failures always take priority over diversity. Required repair work must be labeled as such rather than disguised as a new feature round.

## Explicit A-loop user priority: modern dialogue

The project has an explicit user-priority requirement to evolve Endless Sky's existing branching conversations into a deeper persistent RPG dialogue system. The authoritative implementation target is `A_LOOP_DIALOGUE_SYSTEM.md`.

Until A3 records `DIALOGUE_SYSTEM_STATUS: INTEGRATED_PRODUCTION_SLICE`, A2/A3 must treat this as an open explicit-user-priority item when selecting discretionary work. A blocker, regression, incompatible current-head evidence, or a more urgent integration dependency may delay it, but agents must carry the priority forward rather than silently dropping it.

The first accepted slice must extend/reuse the existing conversation system, connect to real persistent game state, ship with a production conversation, survive save/load, and prove a later consequence/reader. A parser-only framework or a prettier dialogue box without systemic consequences does not satisfy the priority.

After the first coherent production slice is integrated, dialogue returns to normal portfolio rotation rather than monopolizing successive A rounds.

## Mandatory run labels

Every A/B/C/D stage prompt, run report, and implementation handoff should carry these fields:

```text
LOOP_ID: <A1/A2/A3/B1/B2/B3/C1/C2/C3/C4/D1/D2/D3/D4/etc.>
RUN_TYPE: FEATURE | CONTENT | ART | INTEGRATION | QA | TOOLING | REPAIR
PRIMARY_DOMAIN: <main subsystem or content domain advanced>
SECONDARY_DOMAINS: <other systems materially touched>
RECENT_DOMAIN_WINDOW: <primary domains from the most recent comparable runs>
DIVERSITY_STATUS: PASS | JUSTIFIED_REPEAT | BLOCKED
CONCENTRATION_JUSTIFICATION: <required when repeating a recent primary domain; otherwise N/A>
NEGLECTED_AREA_ADVANCED: <underrepresented area improved by this run, or N/A for mandatory repair>
CROSS_SYSTEM_CONNECTION: <existing system this work is newly connected to, or N/A with reason>
```

These labels describe the *actual work*, not the title of the agent. For example, A1 does not use `world simulation` as its primary domain every round; it should report a narrower domain such as `population/migration`, `crime/law`, `war/diplomacy`, or `environment/hazards`.

## Anti-funneling gate

Before choosing discretionary work, an agent must inspect recent completed work and classify its primary domains.

1. Inspect at least the **three most recent comparable runs in the same lane** when available.
2. Inspect at least the **two most recent integrated handoffs from adjacent lanes** when they materially overlap the agent's scope.
3. A discretionary run should not select the same primary domain for a third consecutive run.
4. If one domain appears in two of the previous three comparable runs, prefer an underrepresented domain for the next discretionary run.
5. Across a rolling six-run discretionary window, target no primary domain above one third of runs. Exceeding that target requires a recorded reason and creates **concentration debt** that later discretionary rounds should pay down.
6. A new feature should normally connect to at least one existing subsystem instead of creating another isolated vertical silo.
7. Renaming the location, faction, asset, test fixture, character, or data source does not make repeated structure diverse.

## Mandatory-repeat exception

The anti-funneling gate must never suppress necessary repair work.

The following may repeat a domain and use `DIVERSITY_STATUS: JUSTIFIED_REPEAT`:

- build or runtime blockers;
- regressions;
- save/load or deterministic-state failures;
- performance failures above an accepted budget;
- security/correctness issues;
- integration conflicts;
- failed visual acceptance/proof gates;
- QA closure items that remain reproducible;
- explicit user-priority work.

A justified repeat does **not** erase concentration debt. After the blocker is closed, the next discretionary round should preferentially advance an underrepresented area.

## Lane domain maps

These are examples, not closed taxonomies. Agents should use the narrowest accurate label.

### A1 — world simulation

Rotate among areas such as:

- economy/trade/industry;
- population/migration/demography;
- crime/law/enforcement;
- faction control/politics/governance;
- war/diplomacy/military state;
- environment/hazards/disasters;
- exploration/discovery/world events;
- NPC/social/relationship state;
- ownership/institutions/property;
- travel/traffic/infrastructure;
- resource/ecological state.

A1 should not treat economy/freight as the universal source of simulated change.

For the dialogue priority, A1's role is limited to exposing or reusing authoritative world-state inputs needed by dialogue. It must not create a second narrative copy of simulation truth merely to make a conversation branch possible.

### A2 — RPG and dynamic narrative

Rotate among:

- relationships and personal history;
- politics/governance;
- crime/investigation/law;
- exploration/science/mystery;
- war/diplomacy;
- culture/ideology/religion;
- ownership/inheritance/claims;
- disaster/migration/community pressure;
- careers/backgrounds/skills;
- dialogue/conversation systems and player-facing social choice;
- economy/logistics when genuinely appropriate.

A2 additionally inherits `story/NARRATIVE_DIVERSITY_POLICY.md`.

While the modern-dialogue user priority is open, A2 is the primary specialist responsible for implementing the reusable dialogue capability and at least one production conversation described in `A_LOOP_DIALOGUE_SYSTEM.md`. A2 must not close the priority with only design prose, a parser-only abstraction, or a conversation that has no persistent later consequence.

### A3 — integration/evolution

A3 is responsible for portfolio balance as well as merge correctness.

A3 should:

- record the primary domains of integrated specialist handoffs;
- identify repeated discretionary concentration;
- reject or defer duplicated feature work when it adds little new systemic coverage;
- integrate mandatory fixes regardless of concentration;
- favor cross-system connections between previously separate domains;
- leave a `PORTFOLIO_BALANCE` note in the integration handoff.

For the modern-dialogue priority, A3 must inspect `A_LOOP_DIALOGUE_SYSTEM.md`, verify the exact A2 implementation against current authority, and record `DIALOGUE_SYSTEM_STATUS`. The priority is not satisfied before a tested, save-safe production conversation demonstrates state-dependent branching and a later persistent consequence/reader.

### B1 — world history and regional identity

Rotate among regions, institutions, historical periods, factions, cultures, political structures, conflicts, migrations, discoveries, religions/ideologies, industries, and local civic identity. Do not make every regional history an explanation for current trade disruption.

### B2 — characters and dynamic content

Rotate character roles and pressures: family, authority, crime, science, military service, religion/ideology, labor, exploration, medicine, law, ownership, personal relationships, political ambition, survival, and commerce. Persistent characters should not all be merchants, captains, dispatchers, or logistics intermediaries.

When useful, B2 should author conflicts with at least three credible dialogue approaches and persistent character consequences so the A2 dialogue system receives real production consumers rather than synthetic fixtures.

### B3 — continuity and handoff

B3 should audit the **content portfolio**, not only contradictions. Flag domain concentration, duplicate character roles, repeated plot structures, and regions receiving disproportionate attention. Continuity review should preserve deliberate arcs while resisting accidental monoculture.

For dialogue content, B3 should also flag branches that contradict established character authority, expose knowledge the player/NPC should not have, duplicate persistent state, or reduce multiple supposedly distinct responses to the same consequence.

### C lanes — visual/remaster work

Rotate, when acceptance blockers permit, among:

- ships/vehicles;
- weapons/effects/VFX;
- environments/space backgrounds;
- stations/planets/large structures;
- props/scenery;
- UI/presentation;
- lighting/composition;
- animation/state variants;
- characters/portraits where the pipeline supports them.

Visual proof and actual-game screenshot requirements remain mandatory. A failed proof/acceptance item may remain the focus as `JUSTIFIED_REPEAT`, but after closure the queue should move to underrepresented visual categories instead of endlessly polishing the same asset family.

### D1 — architecture/coherence

Rotate architecture review across simulation boundaries, persistence, data ownership, event flow, UI/game-state boundaries, story/simulation coupling, rendering boundaries, performance architecture, duplication, and dead/disconnected systems. Record **concentration debt** when the project keeps expanding one subsystem while adjacent systems remain disconnected.

D1 should review the dialogue feature for state ownership and ensure the conversation layer reads authoritative mission, relationship, legal, survey, reputation, and simulation facts instead of creating a second truth store.

### D2 — QA/long-run

QA breadth must not mirror feature concentration. Maintain coverage across:

- regression;
- save/load and historical saves;
- deterministic state;
- long-run simulation;
- combat;
- economy;
- missions/story state;
- NPC/faction/world state;
- performance;
- rendering/presentation where testable;
- cross-system interactions.

New-system tests are additive; they do not replace broad regression coverage.

For dialogue-system work, include graph/branch reachability, condition correctness, later-reader persistence, old-save compatibility, stock conversation compatibility, and UI proof when presentation changes.

### D3 — tooling

Do not repeatedly build tools for the same subsystem merely because its fixtures already exist. Prefer reusable infrastructure and rotate among build/test automation, save inspection, simulation diagnostics, story validation, asset proof, profiling, data validation, integration/handoff verification, and observability according to project friction.

Dialogue graph validation/inspection is appropriate when real authoring friction demonstrates a need, especially for unreachable nodes, contradictory gates, orphaned effects, or missing later readers.

### D4 — closure/verification

D4 must distinguish:

- unresolved correctness blockers;
- closed blockers;
- justified repeated repair work;
- unresolved concentration debt.

Concentration debt is normally a planning/coherence issue, not a reason to pretend a correct build failed. It must still be carried into the next Agent A planning/integration handoff.

While the dialogue priority remains open, D4 should carry `DIALOGUE_SYSTEM_STATUS` and any unmet acceptance-gate items into the next A cycle.

## Cross-lane diversity check

Every discretionary handoff should answer:

```text
DIVERSITY_CHECK
- Primary domain:
- Recent same-lane domains considered:
- Adjacent-lane work considered:
- Why this is not another iteration of the same subsystem:
- Underrepresented area advanced:
- New cross-system connection:
- Persistent/player-visible capability added:
- Concentration exception, if any:
```

## Selection order

Use this order when selecting work:

1. **Reproducible blocker or regression?** Fix it and label the repeat.
2. **Explicit user priority?** Do it and record why it overrides normal rotation. The open modern-dialogue requirement in `A_LOOP_DIALOGUE_SYSTEM.md` is such a priority until A3 integrates the first production slice.
3. **Integration dependency preventing other work?** Resolve it.
4. Otherwise audit recent domains and choose an underrepresented high-value area.
5. Prefer work that connects two existing systems over work that deepens one already-dominant silo.
6. Validate, record the actual domain, and hand off with the diversity fields.

## What does not count as diversity

The following are still the same domain unless their mechanics meaningfully differ:

- another freight crisis on a different planet;
- another economy variable feeding the same security response;
- another character whose main role is assigning cargo jobs;
- another visual variant of the same asset family while unrelated categories remain untouched;
- another QA harness testing only the subsystem already receiving most feature work;
- another tool specialized to the same data path when a reusable cross-project tool would solve the broader need.

Diversity means advancing different **player experiences, world behaviors, architecture surfaces, content structures, visual categories, and failure modes**, not merely producing different filenames.

## Integration handoff requirement

A3's authoritative integration/evolution report should include a compact `PORTFOLIO_BALANCE` section containing:

- domains integrated this round;
- recent domain distribution;
- concentration debt still open;
- underrepresented domains recommended for the next A/B/C/D rounds;
- justified repeats that should stop once their blocker closes.

While the dialogue priority is open, the A3 report must also include:

```text
DIALOGUE_SYSTEM_STATUS: NOT_STARTED | SPECIALIST_READY | INTEGRATED_FOUNDATION | INTEGRATED_PRODUCTION_SLICE | BLOCKED_WITH_EVIDENCE
DIALOGUE_SYSTEM_NEXT_GAP: <highest-value unmet acceptance item or N/A>
```

This makes anti-funneling and the explicit dialogue priority part of the build path itself rather than relying on agents to remember informal preferences.
