# B2 Free Worlds Storm Routing Compact — A3/B3 Handoff

## Stage and verdict

- Stage: **B2 STORY CHARACTERS + DYNAMIC CONTENT**
- Verdict: **READY for A3 review/integration**
- Do not self-integrate. A3 retains integration authority.

## Authority and ancestry

- Authoritative `main` recovered at slice selection: `8c61fb377068f6f8cc0d43876fbc15b99f95d6c0`
- Required B1 storm-navigation parent: `8e5e070e821de03508a76f83092fa66bc1c89838`
- Isolated branch: `agent/b2-free-worlds-storm-routing-compact-20260819-2225`
- Production commit: `022e7e1aa2b2ad0525548beeed429eceed7676d5`
- Production + focused-validator commit: `62b232af00c75ae6e5d8656b448b74083f786bc1`
- Exact fully validated production/validator/handoff head: `c4f760cdfc7e4d4b7643d15c546d0b404da81444`

The B1 parent was rechecked before B2 authoring. Its exact-head repository-native workflows are both terminal green:

- `Fork simulation and story validation` #161 / `32324387566`: **SUCCESS**
- `Fork save-load integration smoke` #150 / `32324387618`: **SUCCESS**

The exact B2 candidate head `c4f760cdfc7e4d4b7643d15c546d0b404da81444` is also terminal green:

- `Fork simulation and story validation` #162 / `32324784559`: **SUCCESS**
- `Fork save-load integration smoke` #151 / `32324784412`: **SUCCESS**

A3 should integrate B1 first if it is not already authoritative, then re-read current `main` before considering this B2 branch.

## Character / dynamic-content behavior

Adds a persistent three-mission Free Worlds character arc built around the newly integrated A1 geomagnetic-storm/navigation-strain simulation and B1 storm-navigation institutional history.

Recurring characters:

- **Mara Edden** — beacon engineer focused on calibration provenance and preventing uncertainty from disappearing when advisories are copied.
- **Colm Rusk** — independent pilot focused on rapid usable routing and field corrections under live storm pressure.

### Offer: `Static on the Board`

Available only while:

- `world: free worlds geomagnetic storm active` is true; and
- `world: free worlds geomagnetic navigation strain >= 3`.

Persistent routes:

1. **verification-first** — require fresh verification thresholds even at the cost of longer holds;
2. **field-first** — publish best current routing quickly and use pilot reports as corrections;
3. **paired** — operational route plus source/calibration age/contradictions/expiry;
4. **refusal** — player declines to turn an outsider preference into Free Worlds policy.

### Review: `After the Static`

Available after the storm has ended and A1 navigation strain has recovered to `<= 1`.

The Review exposes the second-order information-loss problem: copied route advice can retain the recommendation while losing the evidence, uncertainty, expiry, or contradictory observations that justified it.

Exactly two terminal settlements:

- **portable confidence packet** — every copied advisory retains source, calibration/verification age, contradictory reports, confidence, and expiry;
- **distributed challenge board** — materially contradictory field observations remain attached until independently resolved.

### Later reader

`Edden Remembers` consumes either terminal settlement once and records `aftermath seen`.

## Ownership and continuity invariants

- A1 remains sole owner/writer of:
  - `world: free worlds geomagnetic storm active`
  - `world: free worlds geomagnetic navigation strain`
- B2 only reads those signals.
- Every B2 persistent write is namespaced `B2 Free Worlds Storm Routing Compact:*`.
- No credits, reputation, cargo, outfits, ships, fleets, combat rating, A1 state, B1 state, or unrelated campaign state are mutated.
- The compact is a practical distributed Free Worlds procedure, **not** a centralized navigation office or new federal command authority.
- Each port may retain its own traffic response. The compact governs provenance/uncertainty of copied advice rather than political control.
- A field challenge is evidence of disagreement, not automatic replacement authority.
- A copied route recommendation must not become more certain than the observations/calibration that created it.

## Files

- `data/human/b2 free worlds storm routing compact.txt`
- `tools/story/validate_b2_free_worlds_storm_routing_compact.py`
- `story/B2_FREE_WORLDS_STORM_ROUTING_COMPACT_HANDOFF_20260819.md`

## Focused validation contract

The focused validator checks:

- exact 3-mission graph;
- both recurring named characters;
- three substantive routes + refusal;
- two terminal settlements;
- Free Worlds scoping;
- live A1 storm/strain gating and recovered-state Review gating;
- A1 world-state read-only ownership;
- B2-only persistent writes;
- no direct material/reputation/combat mutations;
- local `goto`/`label` integrity;
- distributed-authority continuity;
- one-shot aftermath consumption.

Repository-native exact-head validation confirms the focused validator, changed-content style gate, wider story/simulation contracts, production build, and stock save-load smoke all passed on `c4f760cdfc7e4d4b7643d15c546d0b404da81444`.

## Execution-host boundary

The exposed private execution host was inspected before repository work. Its `repository-workspace` remote is `Wiredshark/fallout-test`, not `Wiredshark/star`, and the workspace was already dirty. Five pre-existing service-owned processes were reported and left untouched. No Endless Sky runtime result is claimed from that unrelated host.

## Required A3 acceptance

Before integration:

1. verify branch ancestry against current authoritative `main` and integrate/reconcile B1 dependency first;
2. confirm the exact validated candidate `c4f760cdfc7e4d4b7643d15c546d0b404da81444` remains semantically unchanged except for this READY handoff update;
3. when practical, actual-game proof of:
   - Offer only during active storm with strain >= 3;
   - all three substantive routes and refusal;
   - Review only after storm ends and strain <= 1;
   - both terminal settlements;
   - save/reload between Offer and Review;
   - one-shot `Edden Remembers` aftermath;
   - normal Free Worlds offer-precedence/regression behavior.

## B3 continuity notes

Preserve the distinction among:

- sensor/beacon observation;
- calibration/verification age;
- operational recommendation;
- field contradiction;
- confidence/uncertainty;
- expiry/review obligation;
- local traffic authority.

Do not flatten distributed Free Worlds cooperation into a centralized bureaucracy, and do not let old copied advisories silently become present-tense truth after their evidentiary context has expired.
