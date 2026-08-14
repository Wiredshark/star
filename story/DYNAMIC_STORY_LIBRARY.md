# Dynamic Story Library

## DST-DIRT-001 — Freight Shock

Status: **STORY_CANON / FUTURE_SIMULATION_DEPENDENCY**

### Purpose

Turn a changing commodity or logistics condition into a multi-actor local story with memory. The template is intended for Dirt Belt systems first, but can later be generalized to other regions with different institutions and cultural responses.

### World-state inputs

Minimum future inputs:

- affected system;
- affected commodity;
- shortage or surplus severity;
- duration/trend;
- local government;
- piracy pressure;
- recent merchant losses;
- freight capacity or traffic health;
- player reputation;
- relevant prior story flags.

Optional richer inputs:

- warehouse capacity;
- local repair capacity;
- migration pressure;
- unemployment;
- nearby-system supply;
- faction war state;
- recent station or infrastructure damage;
- named NPC availability.

### Actor roles

The template selects or creates persistent actors rather than anonymous quest dispensers:

1. **Mutual dispatcher** — trying to keep several small carriers solvent.
2. **Owner-captain** — has one ship and cannot absorb repeated losses.
3. **Warehouse operator** — may be overwhelmed, hoarding, or falsely accused of hoarding.
4. **Republic or local official** — wants stability, political credit, and legal compliance.
5. **Opportunist** — pirate broker, smuggler, speculator, or large merchant seeking advantage.
6. **Affected civilian representative** — clinic, farm, factory, dock union, or neighborhood group whose needs depend on the commodity.

Not every instance needs all six.

### Trigger families

#### A. Genuine shortage

Examples: food, medical goods, industrial inputs, equipment, or metals become scarce because freight is not arriving.

#### B. Logistics bottleneck

Nominal supply exists, but warehouses, repair queues, docking congestion, escort shortage, or route disruption prevents delivery.

#### C. Manufactured shortage

A merchant, warehouse operator, cartel, corrupt official, or pirate intermediary deliberately restricts supply.

#### D. Panic shortage

Rumor causes hoarding even though the underlying supply situation is recoverable.

### Story phases

#### Phase 1 — Signals

The player encounters news, bar conversation, price movement, delayed jobs, or a named contact reporting inconsistent information.

The event should be observable before the player is asked to solve it.

#### Phase 2 — Competing explanations

Actors disagree about cause and solution. At least one explanation should be incomplete rather than simply evil or stupid.

Possible claims:

- pirates are causing losses;
- inspectors are delaying cargo;
- a warehouse is hoarding stock;
- captains are refusing an unprofitable route;
- repair shops cannot return ships to service;
- a nearby system is buying up supply;
- the shortage is mostly panic.

#### Phase 3 — Player intervention

Potential options:

- haul emergency cargo;
- escort or assemble a convoy;
- investigate missing freight;
- expose or assist hoarding;
- broker a pooled contract among small carriers;
- support official requisitioning;
- smuggle controlled goods;
- protect a warehouse;
- sabotage a competitor's logistics;
- refuse involvement.

A Contract Spacer background can reveal special information or negotiation routes but is never required.

#### Phase 4 — Resolution

The outcome changes more than payment/reputation. It should produce persistent local consequences.

### Success states

Examples:

- `STABILIZED_LEGAL` — supply restored through legal freight and coordination.
- `STABILIZED_MUTUAL` — local small carriers cooperate successfully and gain resilience.
- `STABILIZED_CORPORATE` — a large operator solves the crisis but gains local leverage.
- `STABILIZED_BLACK_MARKET` — shortages ease while criminal infrastructure grows.
- `EXPOSED_MANIPULATION` — deliberate restriction is proven and an actor loses power.

### Failure states

Failure is content:

- `CONVOY_LOST` — shortage worsens and surviving captains become more risk-averse.
- `FALSE_ACCUSATION` — an innocent warehouse or captain is ruined; the real cause persists.
- `MUTUAL_COLLAPSE` — small carriers default and larger operators absorb routes/assets.
- `RIOT_OR_UNREST` — public trust falls and security presence increases.
- `PIRATE_CAPTURE` — aid cargo is diverted, improving pirate logistics.
- `PLAYER_ABANDONED` — event resolves without the player according to NPC/world trajectories.

### NPC memory

Named actors record compact consequence states such as:

- trusts player;
- blames player;
- indebted to player;
- financially ruined;
- promoted;
- under investigation;
- joined criminal market;
- left system;
- ship destroyed;
- cooperative organizer;
- corporate client.

### News and rumor outputs

The same resolution can generate different reports:

- Republic bulletin emphasizes restored order.
- Merchant circular emphasizes freight losses or contract reliability.
- Dockside rumor attributes events to corruption, incompetence, or heroism.
- Pirate channel advertises vulnerabilities or mocks official explanations.

Reports may disagree even when they describe the same world event.

### World-state outputs

Future simulation may modify:

- shortage severity and duration;
- local freight capacity;
- pirate opportunity;
- merchant concentration;
- local political stability;
- migration pressure;
- reputation by actor/faction;
- persistent NPC states;
- future mission weights;
- historical event log entries.

### Required existing systems

- commodities and system trade values;
- missions and conditional effects;
- fleets and governments;
- conversations/news;
- reputation.

### Required future systems

For the fully dynamic form:

- runtime economy/world-state event exposure;
- persistent named NPCs;
- weighted story-template instantiation;
- regional relationship/contact memory;
- event history available to subsequent content.

### Data that can be authored now

A static proof-of-concept chain can be authored immediately using ordinary mission conditions, conversations, jobs, and news. The builder should first implement a contained Algorel proof before generalizing the template.

### Engine support needed

No new engine support is required for a scripted proof. Generalized dynamic instantiation requires builder support for querying and mutating simulation variables.
