# B2 Drak Memorial Custody Compact lifecycle repair handoff

Verdict: **READY for A3 review/integration.**

## Authority and isolation

- Authoritative integration base observed and rechecked: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-drak-memorial-lifecycle-20260821-2127`
- Production lifecycle repair: `a7dd70ca265e6ff4052f5dc963a4b4764f0a2f1f`
- Focused validator hardening: `6ec25fe666198e4f656e928ec39d32f984ec916b`
- Exact fully validated candidate: `0c9a6032b3f1d74985e2d6e57bbb965ef43aa624`
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

## Exact validation evidence

Exact candidate `0c9a6032b3f1d74985e2d6e57bbb965ef43aa624` is terminal green on both repository-native gates:

- `Fork simulation and story validation` #368 / run `32543832083`: **SUCCESS**
  - focused story validators: SUCCESS
  - hardened Drak lifecycle validator: SUCCESS
  - A1 simulation/state-ownership contracts: SUCCESS
  - changed-content style: SUCCESS
- `Fork save-load integration smoke` #353 / run `32543832076`: **SUCCESS**
  - dependency installation: SUCCESS
  - production configure/build: SUCCESS
  - stock save-load smoke: SUCCESS

## Process safety

The private execution service reported four pre-existing service-owned processes before work. They were preserved. No unrelated process was killed or modified.

## A3 / B3 integration notes

A3 should re-read current `main`, verify ancestry/mergeability, and integrate the exact validated candidate plus this handoff-only READY promotion if the branch remains clean. Preserve the lifecycle invariant: dialogue-only B2 missions that merely persist state terminate with `decline`; reserve `accept` for mission lifecycles that actually create gameplay objectives.

Preserve the Drak continuity invariant that `Custodian` is the player's private shorthand rather than a canonical title or office, and preserve the distinction between historical source, later intervention, safe reconstruction, provenance, and memorial custody.
