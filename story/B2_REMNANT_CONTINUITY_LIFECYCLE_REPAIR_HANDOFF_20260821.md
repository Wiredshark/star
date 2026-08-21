# B2 Remnant Continuity Compact lifecycle repair handoff

## Status

**PARTIAL — production and validator repair are isolated; repository-native CI is still required before A3 integration.**

## Authority and branch

- Stage: B2
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-remnant-continuity-lifecycle-20260821-1228`
- Production lifecycle repair: `8f8c3ac5f9c6a98d8581a3a65073d776616ef4e8`
- Validator hardening: `85ea4dcb7893914467d321fb09e123848d6e717d`

## Defect repaired

`B2 Remnant Continuity Compact` is a three-mission dialogue/state-only slice. Its three positive Offer routes, two Review settlements, and `Taal Remembers` aftermath path wrote persistent state and then used `accept` even though none of the missions creates cargo, a destination, NPC objective, waypoint, timer, or another playable objective. That can leave objective-less missions active after their conversations finish.

The repair changes those six positive terminals to `decline`; the existing refusal path already used `decline`, giving seven clean state-only terminal paths. It also adds the repository-standard Endless Sky GPL header because the legacy production file is now touched by changed-content style validation.

## Preserved behavior

The repair does **not** change:

- Nera Venn or Corin Taal dialogue/characterization;
- continuity/provenance/compact/refusal route conditions;
- Venn/Taal trust conditions;
- custody-reconciliation or two-key-reserve settlement state;
- Remnant source scoping;
- one-shot `Taal Remembers` persistence;
- B2 condition names or values;
- A1/B1/world-state ownership;
- rewards, reputation, cargo, credits, combat state, outfits, ships, or fleets.

## Validator hardening

`tools/story/validate_b2_remnant_continuity_compact.py` now additionally requires:

- zero terminal `accept` commands;
- exactly seven `decline` terminal commands;
- no objective-bearing directives that would invalidate the dialogue/state-only lifecycle assumption.

All pre-existing mission, character, route, settlement, later-reader, mutation-surface, and local goto/label checks remain.

## Validation required before READY

Run repository-native acceptance on the exact candidate head:

- focused story validator discovery including `validate_b2_remnant_continuity_compact.py`;
- changed-content style;
- A1 simulation/state-ownership regressions;
- production configure/build;
- stock save-load smoke.

Do not promote to READY unless both the fork simulation/story workflow and production save-load workflow reach terminal green on an exact head containing the production and validator repairs.

## A3/B3 integration note

This is a lifecycle-only repair. A3 should review/integrate it without changing the established Remnant continuity/provenance semantics. The durable lifecycle invariant is:

> Dialogue-only B2 missions that merely persist state terminate with `decline`; `accept` is reserved for mission lifecycles that actually create gameplay objectives.
