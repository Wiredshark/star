# B2 Dirt Belt Receiving Compact handoff — 2026-08-20

## Verdict

PARTIAL pending repository-native simulation/story/style and production build/save-load validation on the exact candidate head.

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative base: `fdaf94f18aaa02abd4e7269196375572cd0fdf9b`
- Isolated branch: `agent/b2-dirt-belt-receiving-compact-20260820-0527`
- Production commit: `d47f6d2de4c351e27c0d4bdd703afbf73558432f`
- Focused-validator commit / candidate before handoff: `2fe61838d4995777bd3cec8b4a3ac0c98d5a1fb9`

B2 does not self-integrate. A3 retains integration authority.

## Implemented character/dynamic-content loop

`B2 Dirt Belt Receiving Compact` consumes B1's `Dirt Belt Drought Relief Routing Ledger` and turns its historical receiving-capacity lesson into a persistent present-day dispute.

Named characters:

- **Dara Ives** — relief coordinator focused on preserving the original need claim and the unmet remainder after partial or diverted delivery.
- **Micah Thorne** — warehouse foreman focused on practical receiving capacity: unloading labor, storage, road access, local transport, and usable delivery quantity.

Offer routes:

1. claim-first: preserve the original need and make temporary capacity limits/unmet remainder explicit;
2. capacity-first: route aid where it can actually be unloaded and used, while reopening the displaced request;
3. paired: keep original need, receiving capacity, substitute destination, usable quantity, and remaining obligation together;
4. refusal: preserve local judgment without entering the later settlement chain.

Review outcomes:

- **portable receiving packet** — original need, receiving constraints, destination changes, usable delivered quantity, and unmet remainder travel together;
- **reconciliation ledger** — need and logistics remain separate records, and a relief request closes only when both agree on what was actually satisfied.

`Ives Remembers` is the later one-shot reader.

## Continuity and ownership invariants

- B1's central distinction is preserved: a shipment can be delivered without the relief need being fully satisfied.
- Receiving capacity is not treated as one scalar; storage, road access, labor, unloading, and inland transport can fail independently.
- A practical diversion must not erase the original need claim.
- A completed freight leg is not automatically a completed relief obligation.
- Mutual aid does not imply abundance.
- The compact remains voluntary coordination among Dirt Belt settlements, not a centralized Republic/Dirt Belt relief authority.
- Every persistent write is namespaced under `B2 Dirt Belt Receiving Compact:*`.
- No `world:*`, credits, reputation, cargo, outfit, ship, fleet, or combat state is mutated.

## Files

- `data/human/b2 dirt belt receiving compact.txt`
- `tools/story/validate_b2_dirt_belt_receiving_compact.py`
- `story/B2_DIRT_BELT_RECEIVING_COMPACT_HANDOFF_20260820.md`

## Required validation before READY

Run on the exact candidate/handoff head:

- `python3 tools/story/validate_b2_dirt_belt_receiving_compact.py "data/human/b2 dirt belt receiving compact.txt"`
- repository focused story/simulation validator suite
- changed-content style validation
- production Endless Sky configure/build
- stock persistence/save-load smoke (`Saving during conversation`, `Loading and Reloading`, `Loading and Saving`)

Do not claim READY if any required workflow remains non-terminal or fails.

## A3/B3 integration notes

The B1 Dirt Belt resilience history is already integrated in the authoritative base used here. This B2 slice should be reviewed as a direct child of that integration.

Preserve this core semantic boundary during later edits:

> A completed shipment is an event; a satisfied need is a condition. Receiving capacity can change how aid moves without silently changing how much aid is still needed.
