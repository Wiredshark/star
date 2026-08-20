# B2 Lunarium Cover Continuity Compact handoff

**Stage:** B2 STORY CHARACTERS + DYNAMIC CONTENT

**Verdict:** PARTIAL — required B1 dependency is fully green; B2 production and focused validator are complete, including one validator-only CI repair, and the final B2 exact-head repository-native workflows remain to be observed.

**Authoritative `main` observed at selection:** `fdaf94f18aaa02abd4e7269196375572cd0fdf9b`

**Required B1 parent:** `edbab3c06a24faaff34858bb43a5746164645b9b`

**B1 exact-head validation:** simulation/story run `32368544592` SUCCESS; save-load run `32368544765` SUCCESS.

**Branch:** `agent/b2-lunarium-cover-continuity-20260820-0828`

**Production commit:** `1c579bd3d4331372124e7efd44462da69ee60969`

**Initial focused validator:** `a700fedf4d7202db32f54e7a7d4781be7b9a771b`

**Validator repair / exact production+validator candidate:** `cac59ac09812271498cce8c01ffb4261f3e7e056`

## Scope

Adds a three-mission Lunarium character arc consuming B1's `Lunarium Cover Network Archive`.

Characters:
- **Chiree**, existing Lunarium leader and operator of the real Kimek charity network used as cover for some covert transfers.
- **Niree**, a new Kimek charity-route quartermaster concerned with preserving actual civilian obligations when covert traffic borrows capacity.

Initial routes:
1. **Aid first** — covert cargo may use spare capacity but not capacity already promised to civilian beneficiaries.
2. **Continuity first** — urgent covert use may displace aid only if the displaced civilian obligation remains explicit, assigned, and reviewable.
3. **Paired records** — ordinary charity obligations and compartmented covert-capacity records remain separate, linked only by a narrow displacement record.
4. **Refusal** — no general compact is established.

The Review exposes the second-order problem that a copied displacement marker can survive without proving whether the civilian obligation was later restored.

Terminal settlements:
- **portable obligation receipt** — carries only legitimate aid-administration facts: civilian commitment, capacity displaced, replacement route/carrier, current responsible coordinator, review point, and closure status; no covert cargo details;
- **two-ledger reconciliation** — charity and clandestine records remain separate, while a narrow trusted check verifies restoration/reassignment without copying mission details, identities, or destinations into public records.

`Niree Remembers` is the one-shot aftermath reader.

## Canon / continuity

The slice is grounded in current `data/coalition/lunarium intro.txt`, where Chiree explicitly describes the Kimek charity as genuine aid work as well as cover for Lunarium transfers. The B1 Cover Network Archive further establishes that the charity's legitimate beneficiaries and civic obligations must remain real rather than becoming disposable camouflage.

Core invariant:

> Covert use may borrow logistics capacity, but it must not silently erase civilian obligations; conversely, civilian manifests must not become a disguised map of clandestine operations.

The content does not create a centralized Lunarium logistics ministry, reveal clandestine identities/routes in public charity records, or claim that every charity shipment is a covert operation.

## State ownership

All writes are namespaced under `B2 Lunarium Cover Continuity Compact:*`.

Read-only dependencies include:
- `joined the lunarium`
- `joined the heliarchs`
- `Lunarium Cover Network Archive: offered`

No `world:*`, credits, reputation, cargo, outfit, ship, fleet, combat, B1, or campaign-state mutation is introduced.

## Isolation / concurrency

Before branching, live `main`, recent commits, open B2 PRs, and the current B1 candidate inventory were inspected. No existing Lunarium-specific B2 slice was found. Current/recent B2 work targets Remnant authority, Deep escort capacity, Dirt Belt receiving capacity, Avgi tax appeals, Acheron observation, Iije field science, Free Worlds storm routing, and other unrelated domains.

This B2 branch is based directly on the B1 Lunarium candidate so A3 must integrate/accept B1 first if it is still outstanding.

## Focused validator / CI repair

`tools/story/validate_b2_lunarium_cover_continuity_compact.py` checks the exact mission graph, characters, gates, routes, settlements, one-shot aftermath, write ownership, no material/reputation mutation, goto/label integrity, and genuine-aid/compartmentation continuity rules.

The first B2 simulation/story workflow discovered the validator correctly but failed one brittle prose assertion because the required phrase crossed a source line break. Production content was not the failing behavior. Commit `cac59ac09812271498cce8c01ffb4261f3e7e056` repairs that validator assertion to tolerate whitespace while preserving the same continuity requirement.

## Required validation gate

Before promotion to READY or A3 integration:
1. final exact-head `Fork simulation and story validation` must be terminal green;
2. final exact-head `Fork save-load integration smoke` must be terminal green;
3. A3 must re-read current authoritative `main`, verify ancestry/conflicts, and preserve the continuity/state-ownership boundaries above.

Do not self-integrate. A3 retains integration authority.
