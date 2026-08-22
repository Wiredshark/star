# B2 Drak Memorial Custody Compact lifecycle repair handoff

Verdict: **PARTIAL pending exact-head repository-native validation.**

## Authority and isolation

- Authoritative integration base observed: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-drak-memorial-lifecycle-20260821-2127`
- Production lifecycle repair: `a7dd70ca265e6ff4052f5dc963a4b4764f0a2f1f`
- Focused validator hardening: `6ec25fe666198e4f656e928ec39d32f984ec916b`
- No self-integration performed.

## Defect

`B2 Drak Memorial Custody Compact` is a three-mission dialogue/state-only slice. Its three positive Offer routes, two Review settlements, and `Custodian Remembers` aftermath wrote persistent B2 state and then used terminal `accept` despite creating no gameplay objective. In Endless Sky this can leave objective-less missions in the accepted mission list after the conversation closes.

## Repair

- Convert the six positive state-only terminal `accept` commands to `decline`.
- Preserve the existing refusal `decline`, giving seven clean state-only terminal paths.
- Preserve all dialogue, route conditions, settlement conditions, trust/question state, Drak-system scope, one-shot aftermath state, and existing persistence names/values.
- Preserve `Custodian` as the player's private shorthand, not a canonical Drak title or office.
- Preserve the B1 continuity boundary between extinction prevention, memorial custody, intervention restraint, provenance, and historical memory.

## Validator hardening

`tools/story/validate_b2_drak_memorial_custody_compact.py` now additionally requires:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no destination, stopover, waypoint, NPC, cargo, passenger, deadline, or timer directive that would invalidate the state-only lifecycle assumption.

All prior mission-graph, route, settlement, one-shot reader, state-ownership, material-mutation, goto/label, provenance, and restraint/autonomy checks remain.

## Persistence / compatibility

No persistent condition name or value changed. No save migration is required. The repair changes only how state-only conversations terminate after writing the same existing state.

## Process safety

The private execution service reported four pre-existing service-owned processes before work. They were preserved. No unrelated process was killed or modified.

## Required acceptance before A3 integration

Run the repository-native validation gates on the exact candidate head:

1. `Fork simulation and story validation`
2. `Fork save-load integration smoke`

READY requires both to reach terminal green, including changed-content style, focused story validators, A1 simulation/state-ownership contracts, production configure/build, and stock save-load smoke.

## A3 / B3 integration notes

A3 should re-read current `main`, verify ancestry/mergeability, and integrate only after exact-head validation is green. Preserve the lifecycle invariant: dialogue-only B2 missions that merely persist state terminate with `decline`; reserve `accept` for mission lifecycles that actually create gameplay objectives.
