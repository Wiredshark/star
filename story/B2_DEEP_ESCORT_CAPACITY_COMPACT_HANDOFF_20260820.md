# B2 Deep Escort Capacity Compact handoff — 2026-08-20

## Verdict

PARTIAL pending exact-head repository-native simulation/story/style and production build/save-load validation for the lifecycle-repaired candidate.

## Authority and isolation

- Repository: `Wiredshark/star`
- Current authoritative `main` rechecked during lifecycle recovery: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Historical stage-selection main: `fdaf94f18aaa02abd4e7269196375572cd0fdf9b`
- Required B1 parent: `1d4a10429d3e3bfffe7ae78acb58902be8e60b80` (`B1: Deep research logistics institutional history`)
- Isolated branch: `agent/b2-deep-escort-capacity-20260820-0624`
- Original production commit: `62d1b48e9e222f12d9c5b3ea935c83bfcb4f224c`
- Original focused-validator commit: `78ec119836643ff2e2c61bd571e9163fa7ec3926`
- Lifecycle production repair: `be4beb30a4000d6d68cb3561720a52a7a67aa660`
- Lifecycle validator hardening: `523edcd88229c018b19890a2906cde161631d5f7`

B2 does not self-integrate. A3 retains integration authority.

## Character / dynamic-content loop

`B2 Deep Escort Capacity Compact` consumes B1's `Deep Research Convoy Reserve Ledger` and turns its historical capacity-accounting lesson into a persistent dispute between:

- **Mara Kest** — Deep Security liaison focused on the patrol, rescue, inspection, and maintenance obligations displaced when escorts are reassigned;
- **Elias Trent** — civilian convoy coordinator focused on successful time-sensitive research deliveries and making replacement plans operational rather than punitive.

Initial routes:

1. obligation-first — preserve every displaced duty until verified restoration;
2. outcome-first — preserve the immediate convoy outcome while naming replacement owner/deadline for borrowed capacity;
3. paired — keep convoy result, borrowed source, displaced duty, replacement plan, and restoration status together;
4. refusal — leave allocation case-by-case without entering the later settlement chain.

Review outcomes:

- **portable capacity packet** — copied escort records carry outcome, borrowed source, displaced duty, replacement owner, deadline, and verified restoration status;
- **reconciliation cycle** — dispatch outcomes and reserve deficits remain separate records that are periodically compared before an obligation may be closed.

`Kest Remembers` is the one-shot aftermath reader.

## Lifecycle repair

The three missions are dialogue/state-only. They create no destination, cargo, NPC, waypoint, timer, passenger, or other gameplay objective.

The original production used terminal `accept` on six positive paths: the three Offer routes, both Review settlements, and `Kest Remembers`. That can leave objective-less accepted missions in the player's active mission list.

Lifecycle repair commit `be4beb30a4000d6d68cb3561720a52a7a67aa660` changes exactly those six positive terminals from `accept` to `decline`. Refusal already used `decline`, so all seven state-only terminal paths now persist their existing state and close cleanly.

Validator hardening commit `523edcd88229c018b19890a2906cde161631d5f7` now enforces:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- absence of destination/stopover/waypoint/NPC/cargo/passenger/deadline/timer directives that would invalidate the state-only lifecycle assumption.

No route, settlement, character, trust condition, persistent condition name/value, Deep scope, or story semantics changed.

## B1 dependency / continuity

The required B1 parent records that Deep research convoys can consume scarce Deep Security or civilian escort capacity and that successful delivery does not erase the patrol, rescue, inspection, or maintenance work deferred to make the escort possible.

B2 preserves these distinctions:

- a successful convoy is not evidence that escort capacity was free;
- a replacement promise is not verified restoration;
- repeated reassignment can hide a persistent reserve deficit;
- operational success and reserve recovery are separate facts;
- this is practical Deep coordination, not unlimited reserve capacity or a new centralized authority.

A3 should accept/integrate the B1 Deep research-logistics parent first if it is not already authoritative.

## State ownership

All persistent writes are under `B2 Deep Escort Capacity Compact:*`.

The slice does not write `world:*`, B1 history state, credits, reputation, cargo, outfits, ships, fleets, or combat state. The B1 `Deep Research Convoy Reserve Ledger: offered` state is read-only.

## Files changed

- `data/human/b2 deep escort capacity compact.txt`
- `tools/story/validate_b2_deep_escort_capacity_compact.py`
- `story/B2_DEEP_ESCORT_CAPACITY_COMPACT_HANDOFF_20260820.md`

## Validation

Focused validator command:

`python3 tools/story/validate_b2_deep_escort_capacity_compact.py "data/human/b2 deep escort capacity compact.txt"`

Required repository-native acceptance before READY:

- `Fork simulation and story validation` succeeds on the exact lifecycle-repaired final candidate head;
- changed-content style succeeds;
- the hardened focused validator is discovered/executed successfully by the story suite;
- A1/state-ownership contracts remain green;
- `Fork save-load integration smoke` succeeds, including production configure/build and stock persistence smoke.

No PASS is claimed for the repaired head until those exact-head workflows are terminal green.

## A3 / B3 notes

A3 should re-read current `main`, verify B1 dependency ancestry, review the exact diff, and integrate only if both B1 and B2 validation are green.

B3 should preserve the core continuity invariant: **a convoy arriving safely is an event; a restored reserve is a condition.** A successful research shipment must not silently erase deferred patrol, rescue, inspection, or maintenance obligations.

Dialogue/state-only B2 missions that merely persist state should terminate with `decline`; `accept` is reserved for mission paths that actually create gameplay objectives.
