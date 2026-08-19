# A2 Syndicate Maintenance Policy News Handoff — 2026-08-19

Verdict: **PARTIAL / specialist production candidate — actual-game acceptance still required**

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative integration branch: `main`
- Exact base SHA: `d485dea4c511964c1209d86dae15f5bcbf17a03b`
- A2 branch: `agent/a2-syndicate-maintenance-policy-news-20260819-0406`
- Production commit: `ca34fe829f6ef2327424224514b536be3898fd75`
- Validator commit: `620e2362737eb6101c80a0c119f267849b185431`

## Slice

This A2 increment deepens the already-integrated Tessa Marr maintenance-triage arc instead of adding another standalone conversation.

The existing after-action reader records six resolved player-visible outcomes:

- safety under pressure;
- safety stabilized;
- contracts under pressure;
- contracts stabilized;
- resilience under pressure;
- resilience stabilized.

This candidate adds six stock ambient News groups that consume those resolved memories after `A2 Syndicate Maintenance Triage: followup seen`.

The News layer makes the policy outcome visible beyond the originating conversation, so the player's earlier RPG choice becomes part of the later institutional environment.

## Privacy / refusal invariant

The refusal route is deliberately not publicized. Tessa Marr explicitly records that declining the allocation question remains a refusal and is not authorization. This downstream consumer therefore has no News group keyed to `refusal respected`.

## Ownership invariants

A1 remains sole writer of:

- `world: syndicate maintenance backlog`
- `world: syndicate maintenance surge`

The News consumer contains no `action` block and writes no A1 or A2 state. It reads only resolved A2 memory created by the integrated Tessa Marr after-action mission.

## Files

- `data/human/a2 syndicate maintenance policy news.txt`
- `tools/story/validate_a2_syndicate_maintenance_policy_news.py`
- `story/A2_SYNDICATE_MAINTENANCE_POLICY_NEWS_HANDOFF_20260819.md`

## Focused validator contract

`python3 tools/story/validate_a2_syndicate_maintenance_policy_news.py "data/human/a2 syndicate maintenance policy news.txt"`

The validator checks:

- exactly six News groups;
- all six resolved Tessa Marr memory gates;
- `followup seen` on every News group;
- no refusal publicization;
- no A1 maintenance backlog/surge writes;
- no rewrite of the original A2 policy-choice state;
- no `action` blocks.

## Validation status

Repository-native CI should run automatically when the draft PR is opened because the branch changes `data/**`. Do not claim CI success until exact-head workflow results are observed.

## Remaining A3 gates

Before integration:

1. focused validator PASS on the exact candidate head;
2. changed-content style gate PASS;
3. full repository story/ownership contract PASS;
4. A1 simulation regression PASS;
5. stock build/save-load smoke PASS when triggered;
6. actual-game observation of all six News states after the corresponding Tessa Marr after-action outcome;
7. negative proof that none of the six News groups appears before `followup seen`;
8. negative proof that refusal produces no public News;
9. save/reload proof that the resolved memory gates persist correctly;
10. News rotation/regression review alongside existing Syndicate ambient News.

## A3 integration instruction

Preserve this as a read-only consequence layer. Do not move maintenance-backlog ownership into A2 and do not add a public refusal acknowledgement unless the upstream consent semantics are intentionally redesigned and reviewed.

