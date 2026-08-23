# B2 Remnant Continuity Compact lifecycle repair handoff

## Status

**READY for A3 review/integration.**

The production and validator repair are isolated, exact-head repository-native simulation/story/style validation passed, and exact-head production build/save-load smoke passed.

## Authority and branch

- Stage: B2
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-remnant-continuity-lifecycle-20260821-1228`
- Production lifecycle repair: `8f8c3ac5f9c6a98d8581a3a65073d776616ef4e8`
- Validator hardening: `85ea4dcb7893914467d321fb09e123848d6e717d`
- Exact fully validated production/validator/handoff candidate: `b6a9193ed65ebfd232530d46509c3ec49285c04b`

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

## Exact validation evidence

On exact candidate `b6a9193ed65ebfd232530d46509c3ec49285c04b`:

- `Fork simulation and story validation` run `32503327019` / #338: **SUCCESS**;
- focused story validator discovery including `validate_b2_remnant_continuity_compact.py`: **SUCCESS**;
- changed-content style: **SUCCESS**;
- A1 simulation/state-ownership regressions: **SUCCESS**;
- `Fork save-load integration smoke` run `32503327116` / #323: **SUCCESS**;
- production configure/build: **SUCCESS**;
- stock save-load smoke: **SUCCESS**.

Exact base-to-candidate comparison is 3 commits ahead / 0 behind, with exactly three changed files: the production slice, its focused validator, and this durable handoff.

## Persistence and canon assumptions

No persistent condition names or values changed, so no save-state migration is required. This repair is lifecycle-only.

Preserve the existing Remnant continuity boundary: emergency transfers, provenance uncertainty, custody responsibility, and later reconciliation are separate facts. Neither urgency nor provenance caution should silently erase the other.

## A3/B3 integration note

A3 should re-read current `main`, verify ancestry/mergeability, and integrate this exact lifecycle repair without changing the established Remnant continuity/provenance semantics. B2 does not self-integrate.

The durable lifecycle invariant is:

> Dialogue-only B2 missions that merely persist state terminate with `decline`; `accept` is reserved for mission lifecycles that actually create gameplay objectives.
