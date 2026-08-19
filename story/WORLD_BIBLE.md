# World Bible

## Canon policy

This file records only baseline facts confirmed in the checked-in game data plus story-lane additions explicitly marked by status.

## Baseline state at story bootstrap

Status: **BASELINE_CANON**

Repository baseline: Endless Sky 0.11.2 import at commit `d611ce688997d3847ac303c229f64b80663db26c`.

The checked-in data already contains many distinct governments and regional cultures, including the Republic, Free Worlds, Syndicate, Deep, Pirates, Hai, Coalition, Remnant, Wanderers, Korath groups, Successors, Avgi groups, Gegno groups, and others. The story lane should deepen these before inventing duplicate high-level factions.

The human map includes established regional identities such as Earth, the Deep, Dirt Belt, Rim, South, Paradise Worlds, North, and Core. These are useful anchors for systemic story content because the existing map, government, fleet, trade, mission, and planet data already encode differences between regions.

## Dirt Belt anchor

Status: **BASELINE_CANON**

The Dirt Belt is selected as the first systemic-story anchor because its existing data already exposes useful narrative inputs: Republic government, merchant traffic, militia, pirate pressure, mining, variable commodity prices, working-class worlds, and stations.

Confirmed examples include:

- **Algorel** — Republic system with the `dirt belt` attribute. Existing traffic includes Southern Merchants, Militia, Republic fleets, and Southern Pirates. Existing trade includes food, metals, industrial goods, medical goods, electronics, equipment, clothing, plastics, and luxury goods.
- **New Wales** — inhabited object in Algorel.
- **Hydra Station** — station object in Algorel.
- **Alioth** — Republic Dirt Belt system with Southern Merchants, Militia, and pirate traffic.
- **New Tibet** — inhabited object in Alioth.
- **Alnasl** — Republic Dirt Belt system with merchant, militia, pirate, and derelict traffic.

These facts are sufficient to support authored economic and social stories without inventing a new region.

## Story-canon addition: Belt Mutuals

Status: **STORY_CANON**

`Belt Mutuals` is a generic local term for small freight cooperatives, family shipping partnerships, repair pools, cargo insurers, and informal credit associations that operate across the Dirt Belt. It is not a new government and should not be implemented as one unless future design requires it.

The term exists to make economic simulation legible through people. A commodity disruption can therefore affect named captains, warehouse owners, mechanics, debt holders, station unions, and cooperative insurers rather than only changing a market number.

### Internal tensions

- Older owner-captains prefer handshake contracts and local reputation.
- Younger operators push for pooled insurance, standardized maintenance, and shared dispatch data.
- Independent crews resent Republic paperwork but rely on Republic patrols when piracy rises.
- Larger merchants can survive temporary losses that would bankrupt a one-ship family.
- Some mutuals quietly buy contraband cargo when legal contracts fail.

### Simulation hooks

Future world simulation can expose:

- freight demand by commodity;
- local shortage severity;
- piracy pressure;
- convoy losses;
- insurance cost;
- repair scarcity;
- debt stress;
- station warehouse capacity;
- local employment pressure.

These values can drive news, rumors, mission generation, NPC trajectory changes, and persistent local political consequences.

## Continuity rule

Do not turn the Belt Mutuals into a galaxy-wide super-organization. They are deliberately fragmented institutions that differ by system, station, family, and trade route.
