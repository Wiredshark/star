# B2 Near Earth Traffic Appeal Compact handoff

## Stage
B2 STORY CHARACTERS + DYNAMIC CONTENT

## Verdict
READY for A3 review/integration.

## Repository authority
- authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- isolated branch: `agent/b2-near-earth-traffic-appeal-20260820-2325`
- production commit: `1a82d59c44330fc0a5febfb1038cd1904035025f`
- focused-validator commit: `1bc8bce7d353e6601acb0c1683ea6c892044d58c`
- exact fully validated production/validator/handoff candidate: `87554a5025baa3c9c9927e14f3960b77e48b2235`

## Scope
Adds a three-mission Near Earth traffic-record character arc grounded in the integrated B1 `Near Earth Traffic Archive`.

Characters:
- **Sera Venn**, traffic clerk;
- **Oren Mall**, independent tug captain.

The initial conflict starts when an emergency medical-transport berth reassignment is copied downstream without its reason, causing the displaced freighter to look late rather than legitimately bumped. The player can choose:
1. change-provenance records that carry reason/source/affected ship/review status;
2. a clean current schedule with a durable link to the underlying change record;
3. paired operating-schedule and immutable-change-ledger records;
4. refusal.

Every substantive route schedules a Review after 7-11 days.

The Review addresses the second-order failure mode where an old emergency exception survives copying after the emergency and review have ended. It resolves to one of two persistent models:
- **portable slot-change packet**: original slot, new slot, source, reason, affected ship, fee/priority effect, review point, and explicit closure travel together;
- **expiry and renewal**: resolved temporary exceptions remain searchable history but stop propagating as active restrictions unless fresh evidence explicitly renews them.

`Sera Remembers` is the one-shot aftermath reader.

## B1 / canon dependency
Consumes read-only condition:
- `Near Earth Traffic Archive: offered`

The B1 archive establishes that Near Earth traffic procedure grew from practical compromises among captains, dockworkers, local governments, and insurers around congestion, missed connections, damaged cargo, and accidents. This B2 slice turns that history into a present-day character dispute without creating a centralized Near Earth traffic government.

## State ownership
All new writes are namespaced under:
- `B2 Near Earth Traffic Appeal Compact:*`

No `world:*`, credits, reputation, cargo, outfits, ships, fleets, combat rating, B1 state, or unrelated campaign state are written.

The dialogue-only missions terminate with `decline` after persisting state so they do not remain as accepted objective-less missions.

## Continuity invariants
- A historical berth exception is not automatically a current restriction.
- A copied current schedule may be concise without becoming context-free.
- Emergency priority may be legitimate while still requiring review and closure evidence.
- Repetition of one copied schedule does not create independent evidence for why a slot changed.
- Resolved exceptions remain auditable history but should not silently continue as active penalties.
- Practical inter-port traffic record conventions do not imply centralized Near Earth political authority or a universal traffic code.

## Files
- `data/human/b2 near earth traffic appeal compact.txt`
- `tools/story/validate_b2_near_earth_traffic_appeal_compact.py`
- `story/B2_NEAR_EARTH_TRAFFIC_APPEAL_COMPACT_HANDOFF_20260820.md`

## Focused validation contract
`python3 tools/story/validate_b2_near_earth_traffic_appeal_compact.py "data/human/b2 near earth traffic appeal compact.txt"`

The focused validator checks:
- exact three-mission graph;
- Sera Venn + Oren Mall;
- B1 Traffic Archive dependency;
- three persistent routes plus refusal;
- 7-11 day delayed Review;
- exactly two terminal settlements;
- one-shot aftermath reader;
- dialogue-only `decline` lifecycle;
- B2-only persistent writes;
- no material/reputation/world-state mutations;
- local goto/label integrity;
- history-vs-current-exception continuity;
- no invented centralized Near Earth traffic authority.

## Exact validation evidence
On exact candidate `87554a5025baa3c9c9927e14f3960b77e48b2235`:

- `Fork simulation and story validation` #296 / run `32443463608`: **SUCCESS**.
- `Changed fork content style`: **SUCCESS**.
- `Focused simulation and story contracts`: **SUCCESS**.
- focused validator discovery/execution: **SUCCESS**.
- A1 simulation/state-ownership contracts: **SUCCESS**.
- `Fork save-load integration smoke` #281 / run `32443463523`: **SUCCESS**.
- production configure: **SUCCESS**.
- production build: **SUCCESS**.
- stock save/load smoke: **SUCCESS**.

The candidate is therefore suitable for A3 review. The final commit after this candidate changes only this durable handoff wording; production content and validator behavior are unchanged.

## A3 / B3 guidance
A3 should re-read current `main`, compare ancestry, and integrate only if this validated candidate remains conflict-free.

B3 should preserve the distinction among:
- original berth assignment;
- emergency reassignment;
- reason/source for the change;
- downstream copied schedule;
- fee/priority consequence;
- review/closure state;
- genuinely current operational restriction.

The core rule is: **traffic history can explain today's board, but old exceptions must not become today's unexplained punishment.**
