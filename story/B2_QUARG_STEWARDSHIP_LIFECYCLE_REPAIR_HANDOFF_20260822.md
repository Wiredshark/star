# B2 Quarg Stewardship Boundaries lifecycle repair handoff

## Verdict

READY for A3 review/integration.

## Authority and ancestry

- authoritative integration `main` observed at run start: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- required B1 parent: `58083c55af8242ca8001f3ad5b84b7f524712503`
- original B2 READY head: `e573d35cdb0d612b5988b1e6415cffa83969ffa1`
- lifecycle branch: `agent/b2-quarg-stewardship-lifecycle-20260822-1227`
- production lifecycle repair: `b8a9e3bc9889227859a19a451513a9bdfb57db9d`
- validator hardening: `d2a2a688ce77a641ece0e5ca0c30b52dadd64076`
- exact fully validated production/validator/handoff candidate: `79a74c9172dbe8fff77630485f6ce17201406872`

## Repair

The three Quarg Stewardship Boundaries missions are dialogue/state-only. Six positive terminal paths previously persisted story state and then used `accept`, despite creating no destination, cargo, NPC, waypoint, deadline, timer, or other gameplay objective. Refusal already used `decline`.

The repair converts those six positive terminals to `decline`. All seven terminal paths now persist their existing state and close cleanly rather than leaving objective-less accepted missions active.

No dialogue, route, settlement, character, source scope, trust state, condition name/value, B1 dependency, Quarg campaign state, or material/reputation behavior changed.

## Validator hardening

`tools/story/validate_b2_quarg_stewardship_boundaries.py` now also requires:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no objective-bearing `destination`, `stopover`, `waypoint`, `npc`, `cargo`, `passengers`, `deadline`, or `timer` directives.

All prior mission graph, route, settlement, B1 dependency, Quarg scope, B2-only write ownership, material/reputation mutation, local goto/label, and aftermath-reader checks remain.

## Validation evidence

Exact candidate `79a74c9172dbe8fff77630485f6ce17201406872` passed both repository-native acceptance workflows:

- `Fork simulation and story validation` run `32584877052` / #410: **SUCCESS**
  - focused Python validation compilation: PASS
  - all focused story validators, including the Quarg lifecycle validator: PASS
  - A1 simulation contract tests: PASS
  - changed fork content style: PASS
- `Fork save-load integration smoke` run `32584877049` / #395: **SUCCESS**
  - production configure/build: PASS
  - stock save-load smoke cases: PASS

## Persistence and canon

No save-state migration is required. Existing `B2 Quarg Stewardship Boundaries:*` conditions and values are unchanged.

Preserve these continuity invariants:

- protection obligations do not imply Quarg sovereignty over protected communities;
- local authority remains the default outside explicitly bounded survival intervention;
- promised aid and political jurisdiction remain separate facts;
- the recurring `steward` is character continuity, not evidence of a universal Quarg bureaucracy.

## A3/B3 integration notes

A3 should accept/integrate the B1 Quarg stewardship-history dependency first if it is still outstanding, then re-check current-main ancestry before integrating this B2 lifecycle repair. Do not self-integrate this branch.

The lifecycle invariant is reusable across state-only B2 content: dialogue-only missions that merely persist state should terminate with `decline`; `accept` is reserved for mission paths that actually create gameplay objectives.
