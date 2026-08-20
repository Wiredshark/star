# B2 Avgi Wandering Fleet Transfer Compact — Handoff

## Stage / verdict
- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Current verdict: PARTIAL pending exact-head repository-native validation
- Do not self-integrate; A3 retains integration authority.

## Authority / ancestry
- Authoritative `main` observed at selection: `fdaf94f18aaa02abd4e7269196375572cd0fdf9b`
- Required B1 parent: `411cf259b4b09eccbef9d7502119e995aa736f92`
- B1 branch: `agent/b1-avgi-wandering-fleet-institutions-20260820-0916`
- B1 exact-head validation recorded on PR #172: simulation/story SUCCESS and save-load SUCCESS.
- B2 branch: `agent/b2-avgi-wandering-fleet-transfer-compact-20260820-0928`

## Exact B2 commits
- Production: `cdaa576bfd0e4584a71c0fb5925657b478fea9d8`
- Focused validator: `48a0bd5f083d47e6aa0f747ab9e5f7abc5ab892b`
- Current handoff head: this commit.

## Scope
Adds one three-mission recurring-character arc consuming B1 Wandering Fleet load/reserve, refit-provenance, and repair-dependency history.

The recurring specialists are identified by the player's private shorthand as the **Loadkeeper** and the **Fitter**. These are not canonical Avgi titles/offices and do not imply a new centralized Wandering Fleet authority.

### Offer — `The Part That Leaves a Hole`
An urgent compatible-component transfer can restore one ship while reducing the donor ship's planned repair reserve. The player chooses:
1. reserve-first: do not cross a donor reserve floor without an explicit restoration owner;
2. repair-first: allow urgent documented transfers when compatibility/provenance are known, while keeping donor risk visible;
3. paired: maintain a linked transfer-debt record covering both recipient repair and donor deficit;
4. refusal.

### Review — `The Fleet Still Owes Itself`
The receiving ship can be legitimately repaired while downstream summaries omit the donor deficit. The player resolves the practice into exactly one of:
- **portable transfer-debt packet** — provenance, compatibility assumptions, recipient result, donor reserve lost, downstream dependency, restoration owner, and closure evidence travel together;
- **dependency reconciliation cycle** — ship-local repair records remain lightweight while fleet-wide reconciliation compares open reserve deficits, borrowed components, adapters, deferred inspections, and replacement promises against physical reality.

### Later reader — `Loadkeeper Remembers`
One-shot aftermath demonstrates the selected distinction between a completed ship repair and restored fleet resilience.

## Ownership / continuity invariants
- Requires Avgi written language, `avgi: wandering fleet refit 1`, and not being `avgi: lost in twilight`.
- Initial Offer additionally consumes B1 `Avgi Wandering Fleet Load and Reserve Ledger: offered` read-only.
- Every new persistent write is `B2 Avgi Wandering Fleet Transfer Compact:*`.
- No `avgi:*`, B1, or `world:*` mutation.
- No credits, reputation, cargo, outfit, ship, fleet, or combat mutation.
- Physical compatibility does not prove engineering equivalence; provenance and limits remain attached to a transfer.
- A repaired recipient does not prove the fleet's reserve/dependency state has been restored.
- Emergency borrowing can be justified without allowing the resulting deficit to disappear from later records.
- Practical fleet-wide repair accounting does not create a new Avgi government or universal repair law.

## Non-overlap / concurrency review
Before authoring, live `main`, recent commits, and the open B2 inventory were inspected. Existing Avgi B2 work covers Consonance/Twilight emergency power allocation and Dissonance tax appeals; no B2 slice covered Wandering Fleet component transfers, distributed reserves, or repair-dependency debt. The active A2 inventory was also reviewed; no current candidate owns this exact surface.

## Isolation evidence
Exact B1-parent to validator-head comparison (`411cf259...` -> `48a0bd5...`):
- 2 commits ahead / 0 behind
- 2 added files
- production: 154 additions
- validator: 130 additions
- 0 deletions

## Validation status
Required before READY:
1. focused validator `tools/story/validate_b2_avgi_wandering_fleet_transfer_compact.py` passes on exact candidate;
2. repository-native `Fork simulation and story validation` passes, including changed-content style and state-ownership contracts;
3. repository-native `Fork save-load integration smoke` passes, including production configure/build and stock save/load smoke;
4. exact branch remains isolated/mergeable against the required B1 dependency and then-current A3 integration state.

No CI/build/save-load success is claimed until those exact-head workflows actually complete.

## A3 / B3 guidance
A3 should integrate/accept the B1 Wandering Fleet institutional-history dependency first if it remains outstanding, re-read current `main`, then integrate this B2 slice only if ancestry and continuity are still clean.

B3 should preserve these distinctions:
- total stores vs. distributed reserve availability;
- successful local repair vs. restored fleet resilience;
- compatibility vs. understood equivalence/limits;
- emergency transfer justification vs. closure of the donor's resulting obligation;
- practical shared logistics vs. centralized political authority.
