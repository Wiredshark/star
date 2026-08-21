# B2 Broken Compact dialogue-lifecycle repair handoff

## Verdict

PARTIAL pending repository-native validation on the exact branch head. Do not integrate until simulation/story/style and production build/save-load workflows are terminal green.

## Exact state

- authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- branch: `agent/b2-broken-compact-lifecycle-20260821-1325`
- production lifecycle repair: `947ef852c4df26d4b5e18ab2ecb5d168d51e0102`
- validator hardening: `3d7b0bb2ec9cb32504233f633bb44b4fd4127990`

## Defect

`B2 Broken Compact` is a five-mission dialogue/state-only character arc. Its positive terminal conversation paths wrote persistent `ES-STORY-0002:*` state and then used `accept` despite creating no gameplay objective. In Endless Sky that can move an objective-less offered mission into the accepted mission list after its conversation ends.

The slice has more terminal paths than the newer three-mission B2 compacts: Notice has four outcomes, Senn Evidence has three, Dorne Evidence has three, Settlement has four, and Kelm Aftermath has one, for fifteen state-only terminals total.

## Repair

- add the repository-standard Endless Sky copyright/GPL header to the touched legacy data file;
- change every state-only terminal to `decline` after writing exactly the same persistent state as before;
- preserve all Nadia Kelm, Elias Dorne, and Mara Senn dialogue and characterization;
- preserve the evidence-broker / early-estate / early-partnership / refusal states;
- preserve Senn and Dorne evidence acquisition semantics;
- preserve all four settlement outcomes: operating partnership, estate sale, arbitration, and player acquisition;
- preserve Kelm's one-shot aftermath reader;
- preserve the existing player-visible evidence-gated arbitration route;
- do not add cargo, destination, NPC, waypoint, timer, or other mission objectives.

## Focused validator hardening

`tools/story/validate_b2_broken_compact_production.py` now additionally enforces:

- zero terminal `accept` commands;
- exactly fifteen `decline` terminals;
- no objective-bearing mission directives that would invalidate the dialogue/state-only lifecycle assumption;
- all pre-existing mission/character/evidence/settlement/later-reader/shadow-state checks remain.

## Ownership / continuity

No state ownership changes are introduced. Existing `ES-STORY-0002:*` condition names and values remain unchanged. The repair does not invent a parallel relationship database or save schema and does not reinterpret the Morrow Line ownership dispute.

The important narrative distinction remains: evidence of an obligation does not automatically establish a specific ownership percentage or title. The four settlement outcomes and character trust/resentment consequences remain exactly as previously authored.

## Validation required before READY

Run the repository-native fork validation workflows on the exact final head:

1. Fork simulation and story validation, including focused validator discovery, A1/state-ownership regressions, and changed-content style.
2. Fork save-load integration smoke, including production configure/build and stock save-load smoke.

A3 retains integration authority. This branch must remain unmerged until exact-head validation is terminal green and the handoff is promoted to READY.
