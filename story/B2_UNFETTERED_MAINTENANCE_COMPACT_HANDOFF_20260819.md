# B2 Unfettered Maintenance Compact handoff — 2026-08-19

## Verdict

PARTIAL pending exact-head repository-native save-load/build and changed-content style completion. Focused simulation/story validators have already executed successfully on the production+validator head.

## Repository state

- Repository authority: `Wiredshark/star`
- Authoritative integration base observed at slice start: `2f12f0e3026c0c502fb4c686677167d385cfb106`
- Base commit message: `Integrate B1 Unfettered institutional history`
- Isolated branch: `agent/b2-unfettered-maintenance-compact-20260819-2128`
- Production commit: `6717f14fdf55d079ceac442771842dfaf64ebac8`
- Focused-validator / production-data head: `f14e81e547fae1504dc8d7b1d753b55e0a864872`
- Draft PR: #130 (`B2 Unfettered Maintenance Compact`), targeting `main`
- No self-integration performed.

## B1 dependency consumed

The authoritative base integrates B1's `Unfettered Frontier Maintenance Ledger`. B1 establishes that aging frontier worlds use durable maintenance records to preserve:

- failing infrastructure and current repair priorities;
- scarce replacement parts and technician availability;
- emergency substitutions/diversions;
- unfinished obligations that should survive changes in crews and local leaders.

B2 does not change that history. It turns the institutional tension into a recurring character problem.

## Character/dynamic-content slice

Production file: `data/hai/b2 unfettered maintenance compact.txt`

Recurring characters are deliberately player-facing shorthand rather than new canonical Unfettered offices:

- **Keeper** — repeatedly returns to the maintenance ledger and argues that emergency diversions must not erase the settlement whose repair was displaced.
- **Mechanic** — argues that present failure risk has to be able to reprioritize parts and crews or the ledger becomes a memorial rather than an operational tool.

### Offer — `The Part That Keeps Moving`

A scarce pressure regulator has already been diverted repeatedly. The player may support:

1. **obligation-first** — diversions are allowed, but the displaced obligation remains open until actually fulfilled;
2. **risk-first** — current failure severity determines priority, with explicit recording of what prior promise was displaced;
3. **paired ledger** — operational priority and unfinished obligations remain separate linked records;
4. **refusal** — the player declines to impose a foreign decision.

All substantive routes persist under `B2 Unfettered Maintenance Compact:*`.

### Review — `The Repair That Came Back`

The next emergency exposes second-order failures: copied records can retain either the current priority or the old obligation while losing the history connecting them; repeated individually justified diversions can also create accumulated deferral that is never dramatic enough to become the top emergency.

The player resolves the practice into exactly one of two terminal settlements:

- **portable maintenance packet** — every reassignment carries current priority, diversion reason, displaced repair, replacement/equivalent plan, and open/closed obligation status;
- **reconciliation** — local boards retain emergency flexibility, but each maintenance cycle must reconcile present failure risk against accumulated deferral before old obligations may be closed.

### Later reader — `Keeper Remembers`

A one-shot aftermath reader demonstrates the chosen model operating in practice.

## State ownership / invariants

- Every B2 write is namespaced under `B2 Unfettered Maintenance Compact:*`.
- B2 reads `First Contact: Unfettered: offered` and the pre-invasion campaign boundary but does not write them.
- No `world:*` simulation state is written.
- No credits, reputation, cargo, outfit, ship, fleet, or combat state is mutated.
- `Keeper` and `Mechanic` are private player shorthand, not canonical titles, offices, or evidence of centralized Unfettered bureaucracy.
- Current operational priority, the reason for a diversion, and the unfinished obligation displaced by that diversion remain distinct concepts.
- A justified emergency diversion does not by itself erase the prior repair obligation.
- Preserving an old obligation does not create a veto over a genuinely more urgent failure.

## Focused validator

Validator: `tools/story/validate_b2_unfettered_maintenance_compact.py`

It checks:

- exact three-mission graph;
- Keeper/Mechanic recurring-character shorthand;
- three persistent routes plus refusal;
- exactly two terminal settlements;
- Unfettered + first-contact + pre-invasion source scope;
- B2-only write ownership;
- absence of material/reputation/world-state mutation;
- local `goto`/`label` integrity;
- explicit priority/diversion/obligation/replacement continuity concepts;
- one-shot aftermath consumption.

## Validation evidence

On production+validator head `f14e81e547fae1504dc8d7b1d753b55e0a864872`:

- GitHub Actions `Fork simulation and story validation` run #151 started successfully.
- The `Focused simulation and story contracts` job completed these steps successfully before handoff creation:
  - compile focused Python validation code;
  - run all focused story validators;
  - run A1 simulation contract tests.
- Changed-content style was still running at handoff creation.
- GitHub Actions `Fork save-load integration smoke` run #140 was still running at handoff creation.

The final handoff commit triggers exact-head workflows again. A3 must use terminal exact-head workflow results rather than treating an in-progress job as a pass.

The available private Fallout execution host was inspected but not used for Endless Sky validation: its repository workspace remote is `Wiredshark/fallout-test`, not `Wiredshark/star`, and that workspace was already dirty. Existing host processes were preserved.

## Remaining acceptance gates

Before promotion to READY or integration, require terminal green results for the branch's exact candidate head:

1. `Fork simulation and story validation`, including changed-content style and the focused Unfettered validator;
2. `Fork save-load integration smoke`, including production configure/build and stock persistence smoke cases.

If CI reports a content/validator defect, repair on this isolated branch and rerun exact-head validation. Do not weaken the continuity invariants merely to satisfy a validator.

## A3 / B3 integration notes

- A3 should integrate only after exact-head required workflows are green.
- The B1 Unfettered institutional history is already in the authoritative base used by this branch, so no separate dependency cherry-pick is required if A3 integrates from a descendant of base `2f12f0e...`.
- B3 continuity review should preserve the distinction among present failure priority, emergency diversion rationale, and accumulated unfinished repair obligation.
- Do not convert Keeper/Mechanic shorthand into formal Unfettered institutions without separate canon evidence.
