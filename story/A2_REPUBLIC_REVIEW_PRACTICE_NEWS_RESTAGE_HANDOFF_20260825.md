# A2 Republic Review Practice News — current-main restage handoff

Verdict: READY for A3 review/integration. Keep this branch isolated and unmerged; A3 retains integration authority.

## Authority / isolation
- Authoritative repository: `Wiredshark/star`
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-republic-review-practice-news-restage-20260825-1805`
- Production commit: `003073c23fe7a5c9a4d5ae6f04e1cd0e1998f8be`
- Strengthened validator commit: `881dcfcc435c0142ee8270a807e83b60dda61c2b`
- Exact validated production/validator/handoff candidate: `a28a6c93821ae9369e1a6e617daf169af1f99196`
- Historical branch `agent/a2-republic-review-practice-news-20260819-0505` remains untouched and must not be integrated alongside this restage.
- No self-integration was performed.

## Player-facing dynamic narrative loop
This is a read-only ambient consequence layer that connects three already-integrated systems:

`A2 bounded customs-precedent consent -> B2 Republic Review Mentorship settlement -> live A1 customs scrutiny -> Republic News consequence`

Four News groups are emitted:
1. safeguards-record settlement with routine customs scrutiny `< 3`;
2. safeguards-record settlement with elevated customs scrutiny `>= 3`;
3. supervised-review-circle settlement with routine customs scrutiny `< 3`;
4. supervised-review-circle settlement with elevated customs scrutiny `>= 3`.

Every group also requires `B2 Republic Review Mentorship: aftermath seen`, requires `A2 Republic Customs Review: precedent use bounded`, and explicitly excludes `A2 Republic Customs Review: precedent kept private`.

## Ownership / persistence invariants
- This A2 slice writes no persistent state.
- `world: republic customs scrutiny` is read-only; A1 remains sole writer.
- `B2 Republic Review Mentorship:*` is read-only; B2 remains sole writer.
- `A2 Republic Customs Review:*` is read-only; the upstream A2 consent/privacy boundary remains authoritative.
- Private precedent is never positively used to authorize public News.
- No mission, conversation, action, objective, destination, waypoint, cargo, outfit, credits, reputation, fleet, ship, combat, event, or government-attitude mutation is introduced.
- Scope remains Republic ambient News only.

## Files
- `data/human/a2 republic review practice news.txt`
- `tools/story/validate_a2_republic_review_practice_news.py`
- `story/A2_REPUBLIC_REVIEW_PRACTICE_NEWS_RESTAGE_HANDOFF_20260825.md`

## Validation contract
The focused validator checks:
- canonical GPL header and trailing newline;
- exactly four expected News groups;
- exact one-to-one B2 settlement x A1 scrutiny mapping;
- B2 aftermath, bounded-consent, and private-precedent exclusion in every group;
- Republic government scope and News payloads;
- no cross-settlement or conflicting scrutiny gates;
- no upstream/world assignments;
- no gameplay/material/objective mutation directives.

## Exact validation evidence
Exact candidate `a28a6c93821ae9369e1a6e617daf169af1f99196`:
- `Fork simulation and story validation` #630 / run `32904579883`: SUCCESS
  - focused Python validation compile: SUCCESS
  - all focused story validators: SUCCESS
  - A1 simulation/state-ownership contracts: SUCCESS
  - changed fork content style: SUCCESS
- `Fork save-load integration smoke` #615 / run `32904579990`: SUCCESS
  - checkout: SUCCESS
  - build/runtime dependencies: SUCCESS
  - production configure: SUCCESS
  - production build: SUCCESS
  - stock save-load smoke: SUCCESS

## A3 integration instructions
A3 may review this branch as the current-main replacement for the historical Republic Review Practice News candidate. Preserve the exact four outcome mappings, bounded-consent/private-precedent boundary, Republic-only scope, and A1/B2/upstream-A2 read-only ownership. Do not integrate the historical branch alongside this restage.
