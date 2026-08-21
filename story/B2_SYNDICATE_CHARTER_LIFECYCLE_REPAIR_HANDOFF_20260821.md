# B2 Syndicate Charter Obligations lifecycle repair handoff

## Verdict

PARTIAL pending repository-native validation on the exact candidate head.

## Exact state

- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-syndicate-charter-lifecycle-20260821-0724`
- Production lifecycle repair: `5a33ec5ed16f4d2c3e1c1beb8dbfc8ad897ab9f2`
- Focused validator hardening: `993ff520b68473efa434ab4421fcf30dd2da7c09`

## Defect

`B2 Syndicate Charter Obligations` is a three-mission dialogue/state-only slice. The three positive Offer routes, two Review settlements, and `Solis Remembers` aftermath path persisted state and then used `accept` despite creating no gameplay objective. That can leave objective-less missions in the player's active mission list after the conversation closes.

## Repair

- Converted all six positive terminal `accept` commands to `decline`; the refusal path already declined.
- Preserved every existing route, character/trust condition, settlement condition, Syndicate scope, dialogue, and one-shot aftermath state.
- Added the repository-standard Endless Sky copyright/GPL header because the touched legacy data file must pass changed-content style.
- Hardened `tools/story/validate_b2_syndicate_charter_obligations.py` to require zero `accept` terminals, exactly seven `decline` terminals, and no objective-bearing directives that would invalidate the state-only lifecycle assumption.

## Ownership and continuity

- No A1/A2/B1/world-state ownership moves.
- All persistent writes remain `B2 Syndicate Charter Obligations:*`.
- Rhea Solis / Ilan Merrow characterization is unchanged.
- Solis, compromise, Merrow, and refusal routes are unchanged.
- Public-service covenant and consortium-reserve settlements are unchanged.
- `Solis Remembers` remains a one-shot aftermath reader.
- No credits, reputation, cargo, combat, ship, fleet, or equipment mutation was added.

## Validation required before READY

Run the repository-native `Fork simulation and story validation` and `Fork save-load integration smoke` workflows on the exact candidate. READY requires terminal green focused story validation, changed-content style, A1/state-ownership regressions, production configure/build, and stock save-load smoke.

## A3/B3 integration note

This is lifecycle-only. Preserve all existing Syndicate Charter route/settlement semantics and the invariant that dialogue-only missions which merely persist state terminate with `decline`; `accept` is reserved for objective-bearing mission lifecycles.
