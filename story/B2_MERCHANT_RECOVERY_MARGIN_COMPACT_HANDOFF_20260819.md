# B2 Merchant Recovery Margin Compact — Handoff

## Verdict

PARTIAL pending repository-native exact-head validation and completion of the required B1 save-load gate.

## Authority / ancestry

- Repository: `Wiredshark/star`
- Authoritative main observed at run start: `cfa1b0e4744b31540f59543185024de0ddcb8db9`
- Required B1 parent: `549691aa16ad4ac4f83736a40f1c752e7b829003`
- Branch: `agent/b2-merchant-recovery-margin-20260819-2324`
- Production commit: `738a3b736e27bfbac19882826476c8d87d962908`
- Focused-validator commit: `a89ef93741c7dda9269803524a519b65f7003ab9`

## Scope

Adds a three-mission persistent Merchant character arc built from the B1 Merchant Recovery Margin Ledger and A1's authoritative `world: merchant repair backlog` simulation.

Recurring characters:
- **Imani Vale** — Merchant rescue/dispatch coordinator concerned with preserving real emergency recovery margin after a rescue surge.
- **Corin Beck** — yard foreman concerned with clearing already-saved ships rather than leaving nominal reserve capacity idle while repair backlog remains.

Initial routes:
1. protect a minimum emergency repair reserve;
2. clear the current queue first and rebuild reserves afterward;
3. paired approach where every borrowed reserve commitment records the displaced obligation and restoration path;
4. refusal.

The Review becomes available only after A1's repair backlog has recovered to `<= 1`. It exposes the distinction between declared reserve and physically usable capacity, and resolves into exactly two persistent outcomes:
- **portable recovery-margin packet** — actual capacity, promised reserve, displacement reason, restoration path, and open/closed status travel together;
- **reconciliation cycle** — participating yards retain local scheduling control but periodically reconcile usable capacity against unresolved reserve obligations before closing old emergency entries.

`Vale Remembers` is the one-shot aftermath reader.

## Dependencies / ownership

B2 reads but never writes:
- `Merchant Recovery Margin Ledger: offered` from B1;
- `world: merchant repair backlog` from A1.

All persistent writes are namespaced under `B2 Merchant Recovery Margin Compact:*`.

B2 does not write or clear `world:*`, credits, reputation, cargo, outfits, ships, fleets, or combat state.

## Canon / continuity invariants

- The compact is a voluntary operating practice among participating Merchant ports/associations, not a centralized Merchant government or universal regulation.
- Recovery margin is distinct from current backlog: clearing today's queue does not prove tomorrow's reserve has been restored.
- Declared reserve is distinct from physically usable berth/crew/tug capacity.
- Borrowed reserve capacity leaves an obligation that remains open until equivalent capability is actually restored.
- Imani Vale and Corin Beck are ordinary named participants in a Merchant network dispute; they do not define one Merchant-wide political authority.

## Files

- `data/human/b2 merchant recovery margin compact.txt`
- `tools/story/validate_b2_merchant_recovery_margin_compact.py`
- `story/B2_MERCHANT_RECOVERY_MARGIN_COMPACT_HANDOFF_20260819.md`

## Validation completed so far

- Current authoritative main/recent commits/open B2 PRs were inspected before selecting scope.
- No existing Merchant-network B2 slice was found; the existing South Convoy B2 is southern-frontier convoy rescue policy rather than cross-network Merchant repair/recovery-margin accounting.
- B1 Merchant exact head was inspected and its exact state names/continuity claims were consumed rather than re-invented.
- Current A1 Merchant repair-backlog implementation was inspected. B2 treats `world: merchant repair backlog` as strictly read-only and uses `>= 3` for the initial dispute and `<= 1` for recovery Review.
- A focused validator was added for mission graph, named characters, routes/refusal, terminal outcomes, label integrity, B2-only writes, A1 read-only ownership, and no material/reputation mutation.
- B1 exact-head `Fork simulation and story validation` run #166: SUCCESS.
- B1 exact-head `Fork save-load integration smoke` run #155: still IN PROGRESS at latest check.

## Required remaining gates

Before READY / A3 integration:
1. B1 exact-head save-load workflow must be terminal green.
2. Run/confirm exact B2-head `Fork simulation and story validation` and ensure the focused Merchant validator and changed-content style pass.
3. Run/confirm exact B2-head `Fork save-load integration smoke` and production build/save-load cases pass.
4. When practical, actual-game acceptance should exercise all three substantive Offer routes, refusal, save/reload before Review, Review gating after A1 backlog recovery, both settlements, one-shot aftermath behavior, and Merchant offer-precedence interactions.

## A3 / B3 notes

- Integrate or reconcile the B1 Merchant institutional-history dependency first if it is not already authoritative.
- Re-read current main before integration because A1 is actively changing Merchant repair/rescue pressure systems.
- Preserve A1 sole ownership of `world: merchant repair backlog`.
- Preserve the distinction between an emergency being cleared and recovery margin actually being rebuilt.
- Do not turn voluntary cross-port operating records into a centralized Merchant political institution.
