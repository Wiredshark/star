# B2 Dirt Belt Irrigation Reserve Compact handoff

## Verdict

PARTIAL pending exact-head repository-native validation. This branch is intentionally isolated and unmerged for A3 authority.

## Authority and exact branch state

- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Authoritative integration base recovered before branching: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-dirt-belt-irrigation-compact-20260823`
- Production commit: `3c22345aaf66c25acbc9572779a1dd056ac538f5`
- Focused validator commit: `25fb9a2c17388a00a6241c63fa009627d5fc6fcf`
- This handoff commit: use the branch head containing this file.

## Concurrency and non-overlap

Current B2 branch/PR inventory was inspected before work. A live `agent/b2-global-dialogue-lifecycle-audit-20260823` branch exists, so this run deliberately avoided global lifecycle cleanup and did not modify any existing B2 production file. No existing B2 irrigation-reserve / drought-water character compact was found.

The slice is additive and isolated to a new production file, a new focused validator, and this handoff.

## Dependencies consumed

### B1

Consumes the integrated `Dirt Belt Water Share Archive` from the Dirt Belt resilience history. That archive establishes the distinction among ordinary water claims, emergency minimums, temporary transfers, and maintenance obligations without creating centralized Dirt Belt water authority.

### A1

Reads these authoritative simulation signals only:

- `world: dirt belt drought pressure`
- `world: dirt belt irrigation reserve strain`

A1 remains the sole writer of both signals. The Offer requires drought pressure >= 3 and irrigation reserve strain >= 3. Review waits for both to recover to <= 1 and for a route-specific 7-11 day delay to have elapsed.

## Character and dynamic-content behavior

Adds recurring Dirt Belt characters:

- **Mae Calder** — inter-settlement water-share coordinator focused on claims, emergency minimums, transfers, and unresolved obligations.
- **Tobin Shaw** — pump mechanic focused on actual flow, damaged lines, borrowed equipment, operating limits, and physical restoration.

The initial dispute is explicitly about the difference between a valid water claim and water that infrastructure can physically deliver during severe irrigation-reserve strain.

Persistent initial routes:

1. **Emergency floor** — preserve minimum household/crop-survival allocations before discretionary transfers.
2. **Capacity repair** — prioritize high-leverage pump/canal repairs while preserving every displaced claim and its delay history.
3. **Paired records** — keep entitlement/transfer records and physical-capacity/maintenance records separate but permanently cross-linked.
4. **Refusal** — no standing compact is derived from the surge.

After A1 recovery and the delayed Review gate, the player resolves the second-order problem that normal regional gauges do not prove every transfer, delivery, borrowed-equipment, or maintenance obligation has closed.

Terminal settlements:

- **Portable water share** — claim, emergency minimum, transfers, actual delivered capacity, maintenance debt, responsible party, and closure evidence travel together.
- **Dual closure** — entitlement and physical-capacity ledgers remain separate authoritative views; explicit reconciliation is required before an obligation closes.

`Calder Remembers` is the one-shot aftermath reader.

## State ownership and persistence

All direct persistent writes are namespaced under `B2 Dirt Belt Irrigation Reserve Compact:*`.

The slice does not mutate:

- A1 `world:*` state;
- B1 history state;
- credits or reputation;
- cargo, outfits, ships, fleets, or combat state.

No persistent condition name is shared with another B2 slice. Refusal does not arm Review. Positive routes schedule the Review-ready event 7-11 days out. Dialogue-only terminal branches use `decline`, not objective-less `accept`.

## Canon and continuity assumptions

Preserve these distinctions during A3/B3 integration and downstream work:

- a valid water claim is not the same fact as physically deliverable flow;
- a promised emergency minimum is not the same fact as the amount actually delivered;
- aggregate recovery of A1 drought/irrigation strain does not automatically close temporary-transfer or maintenance obligations;
- an emergency repair priority does not erase the displaced claim;
- mutual-aid records and cross-settlement practice do not imply a centralized Dirt Belt water government;
- the compact does not claim drought is permanently solved or make current A1 thresholds into constitutional rules.

## Focused validation contract

`tools/story/validate_b2_dirt_belt_irrigation_reserve_compact.py` checks:

- exact three-mission graph plus Review-ready event;
- Mae Calder / Tobin Shaw presence;
- Republic / Dirt Belt / farming scope;
- B1 Water Share Archive dependency;
- A1 drought and irrigation signals read-only;
- three routes plus refusal;
- 7-11 day delayed Review scheduling on all positive routes;
- exactly two terminal settlements;
- one-shot aftermath;
- B2-only persistent writes;
- zero terminal `accept` / exactly seven terminal `decline` commands;
- absence of gameplay-objective directives;
- no material/reputation/world-state mutation;
- local `goto` / `label` integrity;
- claim-vs-capacity / transfer-vs-restoration continuity concepts.

## Validation still required before READY

Run and require terminal green on the exact candidate head:

1. `python3 tools/story/validate_b2_dirt_belt_irrigation_reserve_compact.py`
2. repository focused story validator suite / Python compile
3. A1 simulation and state-ownership contracts
4. changed-content style
5. production configure/build
6. stock save-load integration smoke

A3 should also inspect current `main` again immediately before integration because concurrent A/B work is expected.

## A3/B3 integration guidance

Do not self-integrate from B2. A3 should verify exact ancestry, current-main conflicts, validator results, and A1 ownership before accepting the candidate. B3 should preserve the central distinction between entitlement and physical capacity and reject later continuity that treats recovered aggregate strain as proof every individual water/maintenance obligation was fulfilled.
