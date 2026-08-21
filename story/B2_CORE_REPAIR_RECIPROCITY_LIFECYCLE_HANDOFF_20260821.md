# B2 Core Repair Reciprocity — dialogue lifecycle repair handoff

## Verdict

PARTIAL — production lifecycle repair and focused validator hardening are complete on an isolated branch. Promotion to READY requires repository-native simulation/story/style and production build/save-load workflows to reach terminal green on the candidate head.

## Authority and isolation

- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Authoritative base/main at slice selection: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-core-repair-lifecycle-20260821-0327`
- Production lifecycle repair: `4427b19afc0cd8e70f81d33c0fd9eb2fdf995e77`
- Focused validator hardening / candidate head before this handoff: `464428cc95df2f1c869d48bdc2dfe9e9bf85da2e`
- No self-integration performed.

## Problem repaired

`B2 Core Repair Reciprocity` consists entirely of dialogue/state-recording missions. Its positive Offer routes, both Review settlements, and `Renn Remembers` aftermath path wrote persistent state and then used `accept`, despite having no destination, cargo, passenger, NPC, deadline, waypoint, or other gameplay objective. Accepting those terminal paths can leave objective-less missions in the active mission list after the conversation is over.

The production repair changes only those six state-only positive terminal commands from `accept` to `decline`. The existing refusal path already used `decline`, so all seven terminal conversation paths now close cleanly after writing the same persistent state.

## Semantic invariants preserved

- No dialogue text changed.
- No mission names or source scoping changed.
- No route conditions changed.
- No B2 persistent condition name or value changed.
- No settlement semantics changed.
- No trust-state semantics changed.
- The provisional Offer route remains the intentional Review fallthrough; Renn and Cross remain explicit Review branches.
- No material/reputation reward or world-state mutation was added.
- This is a lifecycle repair, not a redesign of credential policy.

## Focused validator hardening

`tools/story/validate_b2_core_repair_reciprocity.py` now additionally enforces:

- zero terminal `accept` commands in this state-only slice;
- exactly seven `decline` terminals;
- no objective-bearing directives that would invalidate the state-only lifecycle assumption;
- all pre-existing structure, state ownership, settlement, routing, scope, and no-material-reward checks remain intact.

## Validation required before READY

Run on the exact candidate/final head:

- focused B2 Core Repair Reciprocity validator;
- repository-wide focused story validators/state-ownership checks;
- changed-content style;
- A1/fork simulation regression contracts;
- production Endless Sky configure/build;
- stock save-load integration smoke.

Do not claim any of these as passed until the repository-native workflows report terminal success.

## A3 / B3 integration note

A3 should integrate only a terminal-green validated head. Preserve the lifecycle invariant that dialogue-only B2 missions which merely persist state terminate with `decline`, so they do not remain objective-less accepted missions. Do not rewrite the existing route/settlement state during integration.
