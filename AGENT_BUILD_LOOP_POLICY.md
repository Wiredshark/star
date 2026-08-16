# Agent Build-Loop Diversity Policy

This policy applies to every project agent lane and every recurring build/evolution loop in `Wiredshark/star`.

## Purpose

Agent loops naturally converge on the first subsystem that produces measurable progress. That is useful for debugging, but harmful as a long-term development strategy: repeated local optimization can make the whole project appear active while large parts of the game remain untouched.

The project therefore requires **portfolio diversity** across simulation, RPG/story, worldbuilding, visuals, architecture, QA, and tooling. Depth is still allowed; accidental funneling is not.

Correctness, regressions, save compatibility, blockers, broken builds, and acceptance failures always take priority over diversity. Required repair work must be labeled as such rather than disguised as a new feature round.

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
- economy/logistics when genuinely appropriate.

A2 additionally inherits `story/NARRATIVE_DIVERSITY_POLICY.md`.

### A3 — integration/evolution

A3 is responsible for portfolio balance as well as merge correctness.

A3 should:

- record the primary domains of integrated specialist handoffs;
- identify repeated discretionary concentration;
- reject or defer duplicated feature work when it adds little new systemic coverage;
- integrate mandatory fixes regardless of concentration;
- favor cross-system connections between previously separate domains;
- leave a `PORTFOLIO_BALANCE` note in the integration handoff.

### B1 — world history and regional identity

Rotate among regions, institutions, historical periods, factions, cultures, political structures, conflicts, migrations, discoveries, religions/ideologies, industries, and local civic identity. Do not make every regional history an explanation for current trade disruption.

### B2 — characters and dynamic content

Rotate character roles and pressures: family, authority, crime, science, military service, religion/ideology, labor, exploration, medicine, law, ownership, personal relationships, political ambition, survival, and commerce. Persistent characters should not all be merchants, captains, dispatchers, or logistics intermediaries.

### B3 — continuity and handoff

B3 should audit the **content portfolio**, not only contradictions. Flag domain concentration, duplicate character roles, repeated plot structures, and regions receiving disproportionate attention. Continuity review should preserve deliberate arcs while resisting accidental monoculture.

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

### D3 — tooling

Do not repeatedly build tools for the same subsystem merely because its fixtures already exist. Prefer reusable infrastructure and rotate among build/test automation, save inspection, simulation diagnostics, story validation, asset proof, profiling, data validation, integration/handoff verification, and observability according to project friction.

### D4 — closure/verification

D4 must distinguish:

- unresolved correctness blockers;
- closed blockers;
- justified repeated repair work;
- unresolved concentration debt.

Concentration debt is normally a planning/coherence issue, not a reason to pretend a correct build failed. It must still be carried into the next Agent A planning/integration handoff.

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
2. **Explicit user priority?** Do it and record why it overrides normal rotation.
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

This makes anti-funneling part of the build path itself rather than relying on agents to remember an informal preference.
