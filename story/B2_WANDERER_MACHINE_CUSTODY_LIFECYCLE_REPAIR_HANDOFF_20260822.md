# B2 Wanderer Machine Custody Compact lifecycle repair handoff

Verdict: PARTIAL pending repository-native CI.

## Scope

This B2 slice repairs the mission lifecycle of the existing `B2 Wanderer Machine Custody Compact` without changing its narrative, state model, canon boundary, or settlement semantics.

The three missions are dialogue/state-only. They do not create a destination, stopover, waypoint, NPC objective, cargo/passenger obligation, deadline, or timer. Previously, six positive terminal paths used `accept`, which could leave objective-less accepted missions in the player's active mission list. Refusal already used `decline`.

The production repair changes those six positive terminal commands from `accept` to `decline`, yielding seven clean terminal `decline` paths total.

## Repository state

- authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- branch: `agent/b2-wanderer-machine-custody-lifecycle-20260822-0526`
- production repair: `f9e51e3e51fe2e6168e30314297896501c6a2bf3`
- validator hardening: `1d5cbe357b166fb13ce1a2c94ceec9c06d82e44b`

## Files changed

- `data/wanderer/b2 wanderer machine custody compact.txt`
- `tools/story/validate_b2_wanderer_machine_custody_compact.py`
- this handoff

## Preserved behavior and canon

No persistent condition names or values changed. No save-state migration is required.

Preserved exactly:

- Curator / Engineer as player-private shorthand rather than canonical Wanderer titles or offices;
- three initial routes: custody, sandbox, paired;
- refusal persistence;
- delayed Review scheduling on the three substantive routes;
- `transferable custody packet` and `two-key derivative review` settlements;
- one-shot `Engineer Remembers` aftermath state;
- Wanderer source scope;
- B1 dependency on Factory Deactivation Provenance Ledger and Autonomous Weapon Custody Record;
- B2-only persistent writes;
- the epistemic boundary between sealed original evidence, derived research copies, transformations, uncertainty, interpretation, and later conclusions.

## Validator hardening

The focused validator now additionally requires:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- absence of objective-bearing directives (`destination`, `stopover`, `waypoint`, `npc`, `cargo`, `passenger`, `deadline`, `timer`) that would invalidate the state-only lifecycle assumption.

All pre-existing route, settlement, state-ownership, mutation-surface, provenance, canon, one-shot, and local `goto`/`label` checks remain.

## Host / concurrency safety

Before work, the service-owned process inventory reported four pre-existing processes. They were preserved. The normal private host repository workspace is unrelated to authoritative `Wiredshark/star`, so no host workspace or process was modified for this slice.

## Required acceptance before READY

Repository-native CI must be terminal green for the exact candidate head:

1. Fork simulation and story validation, including changed-content style, focused story validators, and A1/state-ownership contracts.
2. Fork save-load integration smoke, including production configure/build and stock save/load smoke.

Do not promote to READY or integrate until those gates are green.

## A3 / B3 integration notes

This is a focused lifecycle repair. A3 should integrate only after verifying current-main ancestry and green exact-head CI. No ordering dependency beyond the already-integrated Wanderer Machine Custody content is introduced.

Durable lifecycle invariant: dialogue/state-only B2 missions that merely persist state terminate with `decline`; `accept` is reserved for mission paths that actually create gameplay objectives.
