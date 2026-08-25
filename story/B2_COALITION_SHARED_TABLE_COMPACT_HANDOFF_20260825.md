# B2 Coalition Shared Table Compact — handoff

Status: READY for A3 review/integration.

## Authority

- Repository: `Wiredshark/star`
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-coalition-shared-table-compact-20260825`
- Production commit: `387f21be7455c31fc69cb9494b5d471dd134d476`
- Focused validator commit: `6d334b429a7b911e185982730b3177196634532c`
- Exact fully validated production/validator candidate: `5b4510562f0894eedf0adc84515d2db74caf2459`

## Character / dynamic-content behavior

Adds Saryd baker Leri Vann and Kimek neighbor Mato Kesh in a persistent three-mission local Coalition friendship/culture arc. A neighborhood dish improvised from both families' cooking is being copied as an ancient, universal Coalition tradition.

Routes: attributable lineage; living version with named adapters; paired family-source/current-recipe records; refusal. Positive routes schedule a 7–11 day Review. Review resolves into portable recipe-lineage packet or versioned coexistence. `Mato Remembers` is the one-shot aftermath.

## Dependencies and ownership

- Reads `known to the heliarchs` only.
- Writes only `B2 Coalition Shared Table Compact:*`.
- No `world:*`, B1/A1/A2, material, reputation, cargo, equipment, ship, fleet, combat, or government-attitude mutation.
- Saryd-local source scope; this friendship does not establish centralized Coalition food law.
- All 7 dialogue/state-only terminal paths use `decline`.
- Refusal cannot introduce the arc or arm Review.

## Validation contract

Focused validator: `tools/story/validate_b2_coalition_shared_table_compact.py`.

It enforces the exact three-mission graph, recurring characters, Saryd scope, Coalition access gate, route-local writes and scheduling, refusal suppression, Review gates, settlement-local closure, one-shot aftermath, B2-only persistence, seven `decline` terminals, no objective-bearing directives, and the family-source/shared-adaptation/current-version canon boundary.

## Exact validation evidence

On exact candidate `5b4510562f0894eedf0adc84515d2db74caf2459`:

- `Fork simulation and story validation` #623 / run `32884111234`: SUCCESS after rerunning the previously cancelled changed-content-style job.
  - focused Python compilation: SUCCESS
  - all focused story validators: SUCCESS
  - A1 simulation/state-ownership contracts: SUCCESS
  - changed-content style: SUCCESS
- `Fork save-load integration smoke` #608 / run `32884111331`: SUCCESS after rerunning the previously cancelled stock save-load job.
  - checkout: SUCCESS
  - dependency installation: SUCCESS
  - production configure: SUCCESS
  - production build: SUCCESS
  - stock save-load smoke: SUCCESS

The earlier cancellations were non-failing interruptions and are not counted as acceptance evidence; the rerun jobs above are terminal green on the exact production/validator candidate.

## Continuity / canon assumptions

Family recipe source, inherited technique, local adaptation, co-authorship, later revision, attribution, disputed authenticity, and current version are separate facts. Repetition of one menu does not manufacture antiquity or universal authenticity. Archival/source recognition does not prohibit later adaptation, and adaptation does not rewrite source lineage.

## A3 / B3 notes

A3 retains integration authority. Re-read current main, ancestry, mergeability, active B1/A2/B2 work, and exact workflow state before integration. No self-integration.
