# B2 Wanderer Evacuation Recovery Compact lifecycle repair handoff

## Verdict

PARTIAL — isolated production/validator lifecycle repair; promote to READY only after exact-head repository-native simulation/story/style and production build/save-load workflows are terminal green.

## Authority and isolation

- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Repository authority: `Wiredshark/star`
- Authoritative base at branch creation: `main` (live integration head recovered before branching)
- Isolated branch: `agent/b2-wanderer-evacuation-lifecycle-20260822-1123`
- Production lifecycle repair: `a041a9801fb0a217d7c2a54433d99422328511c3`
- Validator hardening / current candidate: `8bbbdb19ef1d431d7a5d7ee5c010f4619f06af55`
- No self-integration performed; A3 retains integration authority.

## Defect repaired

`B2 Wanderer Evacuation Recovery Compact` consists of dialogue/state-only missions. Its three positive Offer routes, two Review settlements, and `Keeper Remembers` aftermath path persisted state and then used terminal `accept`, despite creating no destination, cargo, NPC, waypoint, deadline, timer, passenger, or other gameplay objective. This could leave objective-less missions active after their conversations ended.

The production repair changes exactly those six positive terminal commands from `accept` to `decline`. The existing refusal already used `decline`, so all seven terminal paths now persist their existing state and close cleanly.

## Preserved story/content behavior

The repair deliberately preserves:

- Harbor Keeper / Route Tender recurring characterization and their status as player-private shorthand rather than formal Wanderer offices;
- Offer gating on the existing Wanderer invasion and authoritative A1 `world: wanderer evacuation logistics strain >= 3`;
- Review gating on A1 recovery to `world: wanderer evacuation logistics strain <= 1`;
- obligation-first, current-risk-first, paired-record, and refusal routes;
- all existing trust conditions;
- portable-recovery-packet and reconciliation-cycle settlements;
- one-shot `Keeper Remembers` aftermath state;
- every existing `B2 Wanderer Evacuation Recovery Compact:*` persistent condition name/value;
- A1 sole write ownership of `world: wanderer evacuation logistics strain`;
- the continuity distinction that safe arrival is an event while restored evacuation capacity is a condition.

No save-state migration is required because no persistent key or value changed.

## Validator hardening

`tools/story/validate_b2_wanderer_evacuation_recovery_compact.py` now additionally enforces the lifecycle contract:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- absence of destination/stopover/waypoint/NPC/cargo/passenger/deadline/timer directives that would invalidate the state-only lifecycle assumption.

All pre-existing mission graph, recurring-character, A1 read-only ownership, route, settlement, B2-only write ownership, mutation-surface, continuity, one-shot aftermath, and local `goto`/`label` checks remain.

## Concurrency / process safety

Before branching, live `main`, current open lifecycle PRs, and Wanderer-specific open work were inspected. No competing B2 Wanderer Evacuation Recovery lifecycle repair was found. An open A2 Wanderer evacuation recovery-practice restage exists, but it owns A2 follow-up/practice state and is deliberately not modified or duplicated here.

The private execution service reported four pre-existing service-owned processes. They were preserved; none were killed, cancelled, or modified.

## Validation required before READY

Run/confirm both repository-native workflows on the exact candidate head:

1. `Fork simulation and story validation`
   - focused story validator discovery/execution;
   - hardened Wanderer evacuation lifecycle validator;
   - A1 simulation/state-ownership contracts;
   - changed-content style.
2. `Fork save-load integration smoke`
   - production configure/build;
   - stock save-load smoke.

Do not promote to READY if either exact-head gate fails.

## A3 / B3 integration notes

- Re-read current authoritative `main` immediately before integration because concurrent A/B integrations are expected.
- Preserve A1 sole ownership of `world: wanderer evacuation logistics strain`.
- Preserve Harbor Keeper / Route Tender as player-private shorthand, not canonical offices.
- Preserve the distinction among safe arrival, current operational effect, borrowed capacity, restoration responsibility, closure evidence, and historical emergency records.
- Preserve the lifecycle invariant: dialogue/state-only B2 missions that merely persist state terminate with `decline`; `accept` is reserved for mission paths that actually create gameplay objectives.

## Current verdict

PARTIAL pending exact-head repository-native workflows.
