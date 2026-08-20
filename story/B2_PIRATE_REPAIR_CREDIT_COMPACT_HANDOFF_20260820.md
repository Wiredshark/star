# B2 Pirate Repair Credit Compact Handoff

## Verdict
PARTIAL pending exact-head repository-native simulation/story/style and production build/save-load validation.

## Repository authority
- authoritative base: `27b5ddc9cbb084c4751ef52d185f13f62e825c27`
- branch: `agent/b2-pirate-repair-credit-compact-20260820-1628`
- production commit: `65ab321360841d788183ba38bb82d9618bb9bfaf`
- focused validator commit: `0c6a7c5ac17037c92cc90ed6d5f19876130fbc3a`

## Scope
Adds a three-mission Pirate character/dynamic-content arc consuming the already-integrated B1 `Pirate Repair Debt Archive` institutional history.

Recurring characters:
- Mara Quell, a dock mechanic;
- Venn Daro, a courier who moves between yards and crews.

The initial dispute concerns whether a repair-debt marker may be transferred after the original captain dies without silently changing the original bargain. Player routes are:
- provenance-first transfer;
- current-value transfer with explicit change record;
- paired immutable original obligation + current settlement record;
- refusal.

The Review exposes copied-record divergence after a marker circulates through multiple yards/fences. It resolves into exactly one of:
- portable obligation packet;
- reconciliation between the original obligation and current settlement record.

`Quell Remembers` is the one-shot later reader.

## Continuity / ownership
- B1 Pirate history remains read-only.
- Every new persistent write is `B2 Pirate Repair Credit Compact:*`.
- No `world:*`, credits, reputation, cargo, outfit, ship, fleet, or combat mutations.
- Original repair promise, substitutions, partial repayment, current holder, transfer value, and closure evidence remain distinct concepts.
- Market/transfer value does not retroactively redefine the original repair obligation.
- A copied or traded marker does not become fresh independent evidence merely by changing hands.
- The compact remains local/reputation-based Pirate practice; it does not create a pirate bank, universal legal code, or centralized pirate authority.

## Non-overlap / concurrency
Before branching, live `main`, recent commits, open B2 PRs, and B1 branch/PR inventory were inspected. Current/recent B2 work heavily covers Republic, Free Worlds, Wanderer, Southern Rim, Gegno, Lunarium, Remnant, and other faction-specific slices. No active Pirate repair-credit B2 branch/PR was found. This slice is distinct from South convoy/rescue and Merchant repair/recovery arcs because it focuses on transferable personal repair debt and obligation provenance in Pirate ports.

## Validation required
Run on the exact candidate head:
- `python3 tools/story/validate_b2_pirate_repair_credit_compact.py`
- repository-focused validator discovery / story-state ownership suite;
- changed-content style gate;
- production Endless Sky configure/build;
- stock save-load smoke.

A3 should not integrate unless the exact candidate is terminal green. If a validator catches a real content defect, repair it on this branch and re-run both repository-native workflows.

## A3 / B3 guidance
A3 retains integration authority; do not self-integrate. B3 should preserve the distinction between original obligation, later transfer terms, current market value, substitutions, partial repayment, and explicit closure evidence. Do not reinterpret local Pirate repair-credit conventions as centralized law or banking.
