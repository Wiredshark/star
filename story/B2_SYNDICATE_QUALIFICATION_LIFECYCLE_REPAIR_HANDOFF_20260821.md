# B2 Syndicate Qualification Compact lifecycle repair handoff

- Stage: B2
- Verdict: PARTIAL pending repository-native CI
- Authoritative base/main: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-syndicate-qualification-lifecycle-20260821-1928`
- Production lifecycle repair: `142ec1f205af346b52c395ed3aaa4e528fa205ce`
- Focused validator hardening: `a946e3f32910200a276b9747b3a8c64b02b422ef`

## Repair

`B2 Syndicate Qualification Compact` is a three-mission dialogue/state-only arc. Its three positive Offer routes, two Review settlements, and `Venn Remembers` aftermath previously persisted state and then used terminal `accept`, despite creating no destination, cargo, NPC, waypoint, timer, or other gameplay objective. The refusal route already used `decline`.

The production repair changes those six positive terminals to `decline`, yielding seven clean state-only terminal paths. Mara Venn / Ilias Rook characterization, local/portable/paired routes, refusal, trust conditions, packet/renewal settlements, Syndicate scope, A1 labor-strain/rotation gates, B2 persistence names, and continuity semantics are unchanged.

## Validator hardening

`tools/story/validate_b2_syndicate_qualification_compact.py` now additionally requires:

- zero terminal `accept` commands;
- exactly seven `decline` terminals;
- no destination, stopover, waypoint, NPC, cargo, passenger, deadline, or timer directive that would invalidate the dialogue/state-only lifecycle assumption.

All existing mission graph, named-character, route, settlement, A1 read-only ownership, B2-only write, mutation-surface, goto/label, and continuity checks remain.

## Ownership / persistence invariants

- A1 remains sole owner/writer of `world: syndicate labor strain` and `world: syndicate labor rotation active`.
- B2 writes only `B2 Syndicate Qualification Compact:*` conditions.
- No condition migration is required; names and values are unchanged.
- No material/reputation/cargo/outfit/ship/fleet mutation was introduced.
- The compact remains a practical agreement among participating yards, not universal Syndicate labor law or centralized personnel authority.

## Validation

Repository-native workflows must pass on the exact candidate before promotion to READY:

- Fork simulation and story validation
- changed-content style
- focused story validators including the hardened Syndicate Qualification validator
- A1 simulation/state-ownership contracts
- Fork save-load integration smoke
- production configure/build and stock save-load smoke

## A3/B3 integration notes

Integrate only after the exact candidate reaches terminal green. Preserve the existing route/settlement semantics and the lifecycle invariant that dialogue-only B2 missions which merely persist state terminate with `decline`; reserve `accept` for mission lifecycles that actually create gameplay objectives.
