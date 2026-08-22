# B2 Arach Provenance Compact handoff — 2026-08-22

## Status

READY for A3 review/integration.

## Base and branch

- Repository: `Wiredshark/star`
- Authoritative `main` observed during this completion pass: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Required B1 dependency branch: `agent/b1-arach-civic-institutions-20260819-1124`
- Exact B1 parent SHA: `46f723bf88acb6fdb210e15e79131148abc84bf6`
- B2 branch: `agent/b2-arach-obligation-ledger-20260819-1328`
- Original production commit: `6d7ecedf0786b8746e807b824b62210a4ab308e5`
- Original focused-validator commit: `80d7bfadd202b067a11884c379e3ef5a59211819`
- Dialogue-lifecycle repair commit: `539a7fdef14c825d2493ebf05e690bfcc28ddee5`
- Lifecycle-validator hardening / exact fully validated candidate: `65f2351401fd4ce5388cb0a83b508075fb27d131`

## Slice

B2 converts the B1 Arach Mining Provenance Register, Freight Contract Ledger, and Courier Relay Register into a persistent player-facing dispute about what evidence should survive repeated cargo handoffs.

Two recurring Arach are deliberately identified only by player-private shorthand:

- `Assayer` — emphasizes mine maps, samples, assays, and historical provenance.
- `Carrier` — emphasizes transfer seals, observed condition, custody windows, and bounded responsibility.

These are not canonical Arach names, titles, offices, or political institutions.

The initial encounter offers three persistent routes plus refusal:

1. portable provenance;
2. bounded freight custody;
3. paired provenance/custody histories;
4. refusal.

The delayed Review exposes information-loss during downstream copying and resolves into one of two persistent settlements:

- `settlement provenance packet` — source, direct observation, uncertainty, transformation/condensation, and full-record link travel with copied summaries;
- `settlement portable dispute ledger` — provenance and custody remain separate, while unresolved contradictions must travel downstream until formally closed.

`Assayer Remembers` is the one-shot later reader.

## Dialogue lifecycle repair

The three Arach missions are dialogue/state-only and create no gameplay objective. The original slice used `accept` on six positive terminal paths, which could leave objective-less accepted missions active.

The completion pass changes only those six terminal commands to `decline`; refusal already declined. All 7 terminal paths now persist the same state and close immediately.

The focused validator now enforces:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no destination, stopover, waypoint, NPC, cargo, passenger, deadline, or timer directives that would invalidate the state-only lifecycle assumption.

## Ownership and invariants

- Every persistent write is under `B2 Arach Provenance Compact:*`.
- B2 does not mutate B1 state, A1 `world:*` state, A2 state, credits, reputation, cargo, outfits, ships, fleets, or combat rating.
- Mine provenance is evidence of origin/history, not automatic proof of where loss or misconduct occurred.
- Freight custody records describe bounded observations/responsibility during each leg; they do not erase upstream provenance.
- A shortened/copy-derived record must not silently harden an inference into a direct observation.
- Practical shared record conventions do not imply centralized Arach political authority.
- Dialogue/state-only B2 missions terminate with `decline`; `accept` is reserved for mission paths that actually create gameplay objectives.

## Files

- `data/coalition/b2 arach provenance compact.txt`
- `tools/story/validate_b2_arach_provenance_compact.py`
- `story/B2_ARACH_PROVENANCE_COMPACT_HANDOFF_20260819.md`

## Validation evidence

Exact candidate `65f2351401fd4ce5388cb0a83b508075fb27d131` passed both required repository-native pull-request workflows:

- `Fork simulation and story validation` run #402 / `32573074231`: SUCCESS.
- `Fork save-load integration smoke` run #387 / `32573074182`: SUCCESS.

The simulation/story workflow covers focused story validation, state-ownership/simulation contracts, and changed-content style. The save-load workflow covers production configuration/build and stock persistence smoke.

## Process and concurrency safety

Before editing, the execution-service inventory showed four pre-existing service-owned processes. They were preserved. No unrelated process, branch, worktree, or dirty workspace was modified.

PR #103 had not been updated since 2026-08-19, so this pass completed that existing isolated B2 slice rather than creating a competing duplicate.

## A3 integration guidance

Integrate/accept the B1 Arach civic-institutions dependency first, then this B2 branch. Re-read current authoritative `main` immediately before integration and verify ancestry remains appropriate. Preserve the player-private Assayer/Carrier naming boundary, B2-only write ownership, provenance/custody distinction, and state-only `decline` lifecycle invariant.
