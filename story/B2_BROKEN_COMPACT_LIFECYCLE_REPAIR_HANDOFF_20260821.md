# B2 Broken Compact dialogue-lifecycle repair handoff

## Verdict

READY for A3 review/integration. Production behavior and focused lifecycle validation are terminal green on exact candidate `d1f41366628ac58b89682d26fe2db35856e180aa`. This branch remains draft and unmerged; A3 retains integration authority.

## Exact state

- authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- branch: `agent/b2-broken-compact-lifecycle-20260821-1325`
- production lifecycle repair: `947ef852c4df26d4b5e18ab2ecb5d168d51e0102`
- validator hardening: `3d7b0bb2ec9cb32504233f633bb44b4fd4127990`
- exact fully validated production/validator/handoff candidate: `d1f41366628ac58b89682d26fe2db35856e180aa`

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

## Exact validation

On exact candidate `d1f41366628ac58b89682d26fe2db35856e180aa`:

- `Fork simulation and story validation` run `32508272812` / #339: **SUCCESS**
  - changed-content style: **SUCCESS**
  - focused story validators, including the hardened Broken Compact validator: **SUCCESS**
  - A1 simulation/state-ownership contracts: **SUCCESS**
- `Fork save-load integration smoke` run `32508272818` / #324: **SUCCESS**
  - production configure/build: **SUCCESS**
  - stock save-load smoke: **SUCCESS**

The exact base-to-candidate comparison is 3 commits ahead / 0 behind and changes only:

- `data/human/b2 broken compact.txt`
- `tools/story/validate_b2_broken_compact_production.py`
- `story/B2_BROKEN_COMPACT_LIFECYCLE_REPAIR_HANDOFF_20260821.md`

A3 should re-read current `main`, verify ancestry and mergeability, and preserve the state-only dialogue lifecycle invariant while integrating. No self-integration was performed.
