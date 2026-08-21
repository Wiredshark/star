# B2 Core Repair Reciprocity — dialogue lifecycle repair handoff

## Verdict

READY for A3 review/integration.

## Authority and isolation

- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Authoritative base/main at slice selection: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-core-repair-lifecycle-20260821-0327`
- Production lifecycle repair: `4427b19afc0cd8e70f81d33c0fd9eb2fdf995e77`
- Focused validator hardening: `464428cc95df2f1c869d48bdc2dfe9e9bf85da2e`
- Required standard copyright/GPL header repair / exact fully validated candidate: `7d87185d3d905b64aec6656580beab092438930e`
- No self-integration performed.

## Problem repaired

`B2 Core Repair Reciprocity` consists entirely of dialogue/state-recording missions. Its positive Offer routes, both Review settlements, and `Renn Remembers` aftermath path wrote persistent state and then used `accept`, despite having no destination, cargo, passenger, NPC, deadline, waypoint, or other gameplay objective. Accepting those terminal paths can leave objective-less missions in the active mission list after the conversation is over.

The production repair changes only those six state-only positive terminal commands from `accept` to `decline`. The existing refusal path already used `decline`, so all seven terminal conversation paths now close cleanly after writing the same persistent state.

The first changed-content style run also exposed a pre-existing omission in this older integrated B2 data file: it lacked the standard Endless Sky copyright/GPL header. The exact candidate adds that standard repository header and makes no narrative or gameplay-semantic change beyond the lifecycle repair.

## Semantic invariants preserved

- No dialogue text changed.
- No mission names or source scoping changed.
- No route conditions changed.
- No B2 persistent condition name or value changed.
- No settlement semantics changed.
- No trust-state semantics changed.
- The provisional Offer route remains the intentional Review fallthrough; Renn and Cross remain explicit Review branches.
- No material/reputation reward or world-state mutation was added.
- This is a lifecycle/style repair, not a redesign of credential policy.

## Focused validator hardening

`tools/story/validate_b2_core_repair_reciprocity.py` now additionally enforces:

- zero terminal `accept` commands in this state-only slice;
- exactly seven `decline` terminals;
- no objective-bearing directives that would invalidate the state-only lifecycle assumption;
- all pre-existing structure, state ownership, settlement, routing, scope, and no-material-reward checks remain intact.

## Exact validation evidence

Exact validated candidate: `7d87185d3d905b64aec6656580beab092438930e`.

- Fork simulation and story validation #311 / run `32459232537`: SUCCESS.
  - focused story validators: SUCCESS;
  - Core Repair lifecycle validator: SUCCESS;
  - A1 simulation/state-ownership regression contracts: SUCCESS;
  - changed-content style: SUCCESS.
- Fork save-load integration smoke #296 / run `32459232541`: SUCCESS.
  - production configure: SUCCESS;
  - production build: SUCCESS;
  - stock save-load smoke cases: SUCCESS.

The preceding failed style run is superseded: its focused simulation/story job was already green, and its only failure was the missing standard copyright header, repaired in the exact validated candidate above.

## A3 / B3 integration note

A3 should review/integrate the exact validated candidate plus this handoff-only READY update. Preserve the lifecycle invariant that dialogue-only B2 missions which merely persist state terminate with `decline`, so they do not remain objective-less accepted missions. Do not rewrite the existing route/settlement state during integration.
