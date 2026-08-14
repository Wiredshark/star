# Builder Handoff Queue

## CONTENT ID

`ES-STORY-0001`

## TYPE

RPG background + scripted economic story proof + future dynamic template.

## LOCATION

Primary proof location: **Algorel** system, using existing **New Wales** and **Hydra Station** anchors.

Regional scope: Dirt Belt.

## CHARACTERS

### Imani Velez

Status: **STORY_CANON**

- Life stage: mid-career human.
- Origin: New Wales.
- Current location: Hydra Station / Algorel route network.
- Factional position: Republic citizen; independent merchant-cooperative dispatcher, not a government official.
- Occupation: freight dispatcher and contract broker for several small owner-captains.
- Economic position: solvent but thinly capitalized; personally guarantees portions of several cooperative repair debts.
- Personality: patient, numerate, dry, reluctant to dramatize bad news.
- Strengths: route planning, credibility with small carriers, remembers who actually fulfills promises.
- Flaws: protects failing cooperative members too long; withholds alarming information until she has verified it.
- Ideology: markets function only when institutions keep small participants from being destroyed by one unlucky week.
- Fear: a cascading default that sells local routes to outside operators.
- Goal: keep enough independent freight capacity alive that Algorel is not dependent on one large carrier.
- Secret: one member captain has already missed two repair-debt payments and Velez has covered them from the mutual reserve without telling the others.
- Independent trajectory: if the player never engages, Velez attempts to pool contracts and obtain a temporary Republic-backed guarantee. Success depends on crisis severity; failure pushes her toward selling the mutual's contracts to a larger carrier.

### Tomas Rhyne

Status: **STORY_CANON**

- Life stage: older human.
- Origin: itinerant Dirt Belt freight family.
- Current location: Algorel routes.
- Occupation: owner-captain of one aging freighter.
- Economic position: asset-rich on paper, cash-poor, one major drive failure from insolvency.
- Personality: proud, funny when relaxed, defensive around administrators.
- Strengths: experienced pilot, reliable under pressure, knows old local contacts.
- Flaws: delays maintenance, resents pooled decision-making, conceals financial weakness.
- Ideology: a captain who cannot choose their own cargo and route does not truly own a ship.
- Fear: losing the vessel that represents his family's livelihood.
- Goal: survive the current freight shock without surrendering ownership.
- Secret: he accepted an unofficial high-risk delivery to cover a repair bill, exposing the mutual to reputational damage.
- Independent trajectory: without player involvement, Rhyne attempts the risky contract. Depending on later builder-selected state, he succeeds and becomes more independent, suffers a disabling breakdown, loses cargo to pirates, or sells the ship.

## PREREQUISITES

For the static proof:

- player can access Algorel;
- ordinary mission conditions/effects are available;
- no conflicting active `ES-STORY-0001` state;
- builder chooses a campaign-safe availability window.

For the future dynamic version:

- a freight/commodity disruption in Algorel or another eligible Dirt Belt system;
- persistent event and NPC state exposed to story conditions.

## TRIGGER

Static proof: a spaceport or job-board contact at New Wales or Hydra Station reports that several routine freight contracts have stopped clearing even though listed commodity supply does not explain the disruption.

Dynamic version: `DST-DIRT-001 Freight Shock` is instantiated when an eligible logistics/economic state crosses a builder-defined threshold.

## PREMISE

Small Algorel carriers are dropping out of service because repair delays and cash-flow stress are compounding normal pirate risk. The visible symptom resembles a commodity shortage, but the immediate cause is insufficient reliable freight capacity. Imani Velez wants to pool contracts so surviving ships can keep critical deliveries moving. Tomas Rhyne refuses to reveal how close he is to insolvency and is considering a risky unofficial contract.

The story tests whether simulation-derived economic pressure can produce persistent people, competing interests, multiple viable interventions, and consequences that survive mission completion.

## PLAYER OPTIONS

1. **Haul critical freight personally.** Immediate relief, but does not automatically solve the carrier-capacity problem.
2. **Support Velez's pooled-contract plan.** Requires persuading or compensating reluctant captains.
3. **Back Rhyne's independent run.** Potentially fast and profitable, but concentrates risk in one vulnerable ship.
4. **Seek Republic support.** Request temporary escort, guarantee, or administrative relief; may improve stability while increasing official leverage.
5. **Use unofficial/smuggler capacity.** Restores movement quickly at the cost of strengthening black-market relationships.
6. **Exploit the disruption.** Buy distressed contracts/assets or work with a larger operator to displace weak carriers.
7. **Decline involvement.** NPC trajectories continue and the crisis resolves according to scripted or simulated state.

A future `Contract Spacer` background adds information and negotiation variants to options 2, 3, 4, and 5 but does not create a mandatory best answer.

## SUCCESS STATES

### `ES-STORY-0001: mutual stabilized`

Velez's pool survives; Rhyne remains independent or accepts limited cooperative rules; local small-carrier capacity improves.

### `ES-STORY-0001: republic stabilized`

Official intervention prevents collapse; local freight recovers, but Republic influence over contracts/inspection increases.

### `ES-STORY-0001: outside carrier stabilized`

A larger operator restores service efficiently while acquiring distressed routes or debt.

### `ES-STORY-0001: black market stabilized`

Unofficial capacity restores deliveries; criminal/smuggling contacts gain durable leverage.

## FAILURE STATES

### `ES-STORY-0001: rhyne lost`

Rhyne's ship is destroyed, disabled, captured, or sold. Velez's mutual loses capacity and may blame the player depending on advice given.

### `ES-STORY-0001: mutual default`

Repair debt and missed contracts cascade. Small carriers leave the route or sell assets.

### `ES-STORY-0001: false diagnosis`

The player solves the wrong problem, such as delivering one cargo while the capacity bottleneck remains. Payment may still occur, but the broader event worsens or returns.

### `ES-STORY-0001: abandoned`

The player leaves the situation unresolved. A deterministic builder-selected fallback trajectory resolves it later without waiting for the player.

## WORLD CONSEQUENCES

Static proof can record condition flags and produce follow-up missions/news.

Future simulation outputs should include some combination of:

- Algorel freight-capacity modifier;
- shortage duration/severity modifier;
- pirate opportunity modifier;
- local small-carrier concentration;
- Republic intervention level;
- black-market logistics presence;
- future freight-job weighting;
- local historical event record.

## CHARACTER CONSEQUENCES

Velez may become:

- trusted mutual organizer;
- debtor to the player;
- hostile critic;
- employee/contractor of a larger carrier;
- failed organizer who leaves Algorel.

Rhyne may become:

- loyal independent contact;
- cooperative convert;
- rival who resents player interference;
- bankrupt former captain;
- smuggler;
- casualty whose relatives/partners remember the outcome.

Neither character should disappear simply because the first mission resolves.

## FUTURE HOOKS

- a later insurance dispute over losses from the crisis;
- a pirate broker reveals who purchased stolen cargo;
- Velez tries to expand pooled maintenance across nearby Dirt Belt systems;
- Rhyne's debt is purchased by an outside company;
- Republic auditors investigate the emergency guarantee;
- a later genuine commodity shortage reuses established contacts and remembers this outcome;
- rumors/newspapers describe the event differently according to institution and result.

## IMPLEMENTATION DEPENDENCIES

### Existing support usable now

- standard Endless Sky mission/conversation condition system;
- system, planet, government, fleet, trade, news, and reputation data;
- Algorel/New Wales/Hydra Station map anchors.

### Builder work for static proof

- author a contained mission chain using normal data syntax;
- add conversations for Velez and Rhyne;
- add local news/reaction variants;
- reserve stable condition names beginning with `ES-STORY-0001:`;
- verify the chain does not conflict with stock campaign state.

### Future builder support for systemic form

- RPG background state (`background: contract spacer` or equivalent);
- dynamic world/economy state exposed to mission conditions;
- persistent named NPC records and trajectories;
- story-template scheduler/selector;
- durable event-history queries;
- relationship/contact memory richer than global government reputation.

## PRIORITY

**HIGH** — implement the static Algorel proof before generalizing a dynamic-story engine. It exercises the desired coupling among RPG identity, economy, persistent NPCs, news, failure states, and world memory while remaining implementable with current mission data.
