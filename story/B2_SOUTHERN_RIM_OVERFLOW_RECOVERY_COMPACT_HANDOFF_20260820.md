# B2 Southern Rim Overflow Recovery Compact handoff

**Stage:** B2 STORY CHARACTERS + DYNAMIC CONTENT  
**Verdict:** READY for A3 review/integration  
**Authoritative `main` observed at selection:** `afde12845a8426df9e39edea0b6f58d10ef2c9e7`  
**Authoritative `main` rechecked after validation:** `56d6ee50f27b6555d4a3013dba150c55e5450d48`  
**Required B1 parent:** `39a189069031cd8673362ea7d04b664ebac7db14`  
**Branch:** `agent/b2-southern-rim-overflow-recovery-20260820-1324`  
**Production commit:** `4a9f5536c708f894d44c9aba4b0ba0012d3cdcbb`  
**Focused validator commit:** `08a512bcc752faec53e4cfd977963a4676094e9b`  
**Exact fully validated production/validator/handoff candidate:** `d6e75ca279f09e7840d61b93855aafc75759d505`

## Scope

Adds a three-mission Southern Rim character/dynamic-content arc that consumes:

- B1 `Southern Rim Overflow Berth Compact Archive` history;
- the completed A2 Rhea Solano traffic-coordination aftermath;
- authoritative A1 `world: southern rim transit congestion` as read-only live state.

The arc uses returning traffic coordinator **Rhea Solano** and introduces overflow-port yardmaster **Jo Kessler**. Their conflict is the capacity debt created when major Southern Rim queues are relieved by shifting work onto secondary ports.

Initial routes:

1. make berth/tug/repair/fuel/crew/maintenance displacement a visible capacity obligation;
2. keep overflow routing flexible but assign restoration owner and deadline;
3. pair diversion results with receiving-port capacity use and closure evidence;
4. refuse to create a regional practice.

When A1 naturally recovers congestion to `<= 1`, the Review resolves into exactly one of:

- a **portable borrowed-capacity packet** carrying origin, receiving capacity used, deferred obligation, restoration owner, review point, and closure evidence;
- a **reconciliation cycle** that preserves local capacity ledgers while preventing the network from calling borrowed capacity restored before participating ports actually close the remaining deficits.

`Kessler Remembers` is the one-shot later reader.

## Continuity / ownership invariants

- A1 remains sole writer of `world: southern rim transit congestion`.
- B1 history and A2 traffic-coordination state are read-only.
- Every new write is `B2 Southern Rim Overflow Recovery Compact:*`.
- No credits, reputation, cargo, outfit, ship, fleet, or combat mutation.
- Clearing the major traffic queue is not the same condition as restoring secondary-port berth, tug, repair, fuel, crew, and maintenance capacity.
- A diversion result and its downstream capacity cost may both be true and must remain separately visible.
- A restoration deadline is not closure evidence by itself.
- Resolved obligations should close rather than becoming permanent warnings.
- Shared overflow/reconciliation records do not create a centralized Southern Rim traffic authority; local port authority remains explicit.

## Non-overlap / concurrency

Open/recent B2 inventory was checked before branching. Existing B2 work covers Free Worlds reserve recovery, Gegno baselines, Kor Efret passage, Lunarium cover, Remnant field authority, Dirt Belt receiving, Deep escort capacity, Merchant diversion/recovery, Acheron observation, Avgi Dissonance, Iije observation, and other separate domains. No current B2 slice targeted Southern Rim overflow receiving-capacity recovery.

The existing A2 Southern Rim Traffic Coordination arc focuses on temporary routing policy during congestion and its immediate after-action consequence. This B2 slice instead targets a later recurrence and the secondary-port capacity debt that persists after the primary queue clears.

## Files

- `data/human/b2 southern rim overflow recovery compact.txt`
- `tools/story/validate_b2_southern_rim_overflow_recovery_compact.py`
- `story/B2_SOUTHERN_RIM_OVERFLOW_RECOVERY_COMPACT_HANDOFF_20260820.md`

## Exact validation evidence

Required B1 parent `39a189069031cd8673362ea7d04b664ebac7db14` is terminal green on both repository-native workflows:

- `Fork simulation and story validation` run `32343574572` / #191: **SUCCESS**
- `Fork save-load integration smoke` run `32343574569` / #180: **SUCCESS**

On exact B2 candidate `d6e75ca279f09e7840d61b93855aafc75759d505`:

- `Fork simulation and story validation` run `32397670179` / #240: **SUCCESS**
- focused simulation/story contracts: **SUCCESS**
- all focused story validators, including `validate_b2_southern_rim_overflow_recovery_compact.py`: **SUCCESS**
- A1 simulation/state-ownership contracts: **SUCCESS**
- changed fork content style: **SUCCESS**
- `Fork save-load integration smoke` run `32397670197` / #229: **SUCCESS**
- production configure: **SUCCESS**
- production build: **SUCCESS**
- stock save-load smoke cases: **SUCCESS**

The repository-native workflows therefore establish parser/style/state-ownership/build/persistence evidence for the exact candidate. Actual-game route-by-route manual acceptance remains a useful optional follow-up, not a blocker for A3 review under the current repository validation protocol.

## A3 / B3 integration guidance

A3 should accept/integrate B1 Southern Rim transit institutional history first if it remains outstanding, then re-read current `main` and integrate this B2 slice only if ancestry, ownership, and continuity remain clean.

B3 should preserve the distinction among:

- primary queue clearance;
- diverted traffic success;
- receiving-port physical capacity used;
- deferred maintenance / crew / tug / fuel obligations;
- promised restoration;
- actual closure evidence.

Practical interoperability among independent ports must not become a single centralized Southern Rim traffic government.
