# B2 Republic Tracing Compact Lifecycle Repair Handoff — 2026-08-21

## Verdict

**READY for A3 review/integration.**

This branch repairs the dialogue lifecycle of the integrated `B2 Republic Tracing Compact` slice without changing its character, routing, settlement, ownership, or persistence semantics.

## Repository authority and branch

- Repository: `Wiredshark/star`
- Authoritative base/main recovered at start: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-republic-tracing-lifecycle-20260821-1023`
- Production lifecycle repair: `de83fe1f95c017c02ac7bd14554283d7e4f8e37f`
- Focused validator hardening: `d2b758f3a602c8d3ff42bd6788bf4e5c2f361ce5`
- Exact fully validated production/validator/handoff candidate: `018b92db22035af955f2f3982470e23feef72a3a`

## Defect repaired

`B2 Republic Tracing Compact` contains three dialogue/state-only missions. The three positive Offer routes, two Review settlements, and `Saye Remembers` aftermath path all wrote persistent state and then used `accept` despite creating no destination, cargo, NPC, waypoint, passenger, timer, or other gameplay objective. In the current mission lifecycle, that can leave objective-less missions in the accepted mission list.

The refusal route already used `decline`.

## Production changes

File: `data/human/b2 republic tracing compact.txt`

- added the repository-standard Endless Sky GPL header because this legacy file is now touched by changed-content style validation;
- changed all six positive state-only terminal `accept` commands to `decline`;
- preserved the existing refusal `decline`, yielding exactly seven state-only dialogue terminals that all close cleanly;
- preserved all Anika Saye / Corin Vell dialogue, Republic source scope, three initial routes, refusal state, both terminal settlements, trust state, and one-shot aftermath state;
- preserved A1 ownership: `world: republic displacement pressure` and `world: republic resettlement surge` remain read-only inputs;
- preserved all writes under `B2 Republic Tracing Compact:*`.

## Validator hardening

File: `tools/story/validate_b2_republic_tracing_compact.py`

The focused validator now additionally requires:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no objective-bearing mission directives that would invalidate the state-only lifecycle assumption.

All existing checks remain: exact mission set, named characters, authoritative A1 reads, B2-only write ownership, three routes plus refusal, exactly two settlements, one-shot aftermath, material/reputation guards, and local `goto`/`label` integrity.

## Exact validation evidence

On exact candidate `018b92db22035af955f2f3982470e23feef72a3a`:

- `Fork simulation and story validation` run `32492243674` / #333: **SUCCESS**
  - focused story validators, including Republic Tracing lifecycle assertions: SUCCESS
  - A1 simulation/state-ownership contracts: SUCCESS
  - changed-content style: SUCCESS
- `Fork save-load integration smoke` run `32492243686` / #318: **SUCCESS**
  - production configure/build: SUCCESS
  - stock save-load smoke: SUCCESS

The branch comparison from authoritative base to the validated candidate is exactly 3 commits ahead / 0 behind with 3 changed files. Four pre-existing service-owned host processes were observed and preserved; none were killed or modified.

## Persistence / canon invariants

- A1 remains sole owner/writer of Republic displacement pressure and resettlement surge.
- B2 continues to distinguish family-tracing status from residence, return, and local-settlement decisions.
- Administrative transfer is not family reunification.
- Contact-sharing consent, current address, tracing status, and records-custodian responsibility remain separate fields/decisions.
- No credits, reputation, cargo, outfits, ships, fleets, combat state, or new save schema are introduced.
- No narrative, route, settlement, or condition-name/value changes were made.

## A3 / B3 integration notes

A3 retains integration authority. Re-read current `main`, verify ancestry/mergeability, and integrate only if the validated lifecycle repair remains semantically clean. Preserve the state-only `decline` lifecycle invariant and every existing B2/A1 ownership boundary.

B3 should preserve the story distinction among family tracing, residence, return, contact consent, and explicit closure; lifecycle repair does not authorize semantic consolidation of those states.
