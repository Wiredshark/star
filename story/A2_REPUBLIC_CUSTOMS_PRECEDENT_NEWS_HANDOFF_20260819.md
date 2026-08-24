# A2 Republic Customs Precedent News Handoff — 2026-08-19

Verdict: **PARTIAL / specialist candidate pending repository-native CI and actual-game acceptance**

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative integration branch: `main`
- Exact base SHA: `d485dea4c511964c1209d86dae15f5bcbf17a03b`
- A2 branch: `agent/a2-republic-customs-precedent-news-20260819-0205`
- Production data commit: `457c8866a84acefa38d4d4f42a461a16fd37616f`
- Validator commit: `e039490bcbec13e8c41aea99d88317a4ec57f982`
- Final branch head: this handoff commit

## A2 slice

This slice extends the already-integrated `A2 Republic Customs Review` arc into ambient Republic world reaction without creating another customs authority or another dialogue decision.

The existing later reader lets the player decide whether Sera Noll may reuse the procedure as a bounded precedent or must keep the case private. This consumer respects that choice mechanically:

- public News requires `A2 Republic Customs Review: later reader seen`;
- public News also requires `A2 Republic Customs Review: precedent use bounded`;
- `precedent kept private` never authorizes any public News;
- four public variants correspond to the resolved customs outcome: bounded document audit, written uncertainty, contextualized routing, or preserved formal-process refusal.

The refusal-derived public variant is deliberately anonymized and describes only the procedural rule. It does not identify or celebrate the player character.

## Ownership and persistence invariants

- No `action` block exists in the new News file.
- A2 does not write `world: republic customs scrutiny`.
- A2 does not write `world: republic border pressure`.
- A2 does not rewrite the underlying customs-review outcome or precedent-consent conditions.
- Persistence is inherited from ordinary existing mission/global conditions written by the integrated Republic customs-review arc.
- Save compatibility is unchanged because no new engine-side serialization schema is introduced.

## Files

- `data/human/a2 republic customs precedent news.txt`
- `tools/story/validate_a2_republic_customs_precedent_news.py`
- `story/A2_REPUBLIC_CUSTOMS_PRECEDENT_NEWS_HANDOFF_20260819.md`

## Focused validator contract

The validator requires exactly four News groups, exact outcome-memory gates, `later reader seen` on all groups, `precedent use bounded` on all groups, absence of private-precedent authorization, and absence of writes to the A1 world-state authorities or consent state.

## Validation state at handoff creation

Repository-native CI is now available on `main`, including blocking changed-file content style, cross-file story ownership/graph checks, focused story validators, A1 simulation tests, and stock save/load smoke coverage for relevant changes. This branch should be judged using those checks once the PR is opened.

No manual actual-game News rotation/visibility pass is claimed here.

## A3 acceptance gates

Before integration, require:

1. repository-native story/style CI PASS on the exact PR head;
2. cross-file ownership/graph contract PASS;
3. stock save/load smoke PASS when triggered for the candidate surface;
4. in-game Republic News visibility after `later reader seen` + `precedent use bounded` for each of the four outcomes;
5. negative proof that no customs-precedent News appears before the later reader resolves;
6. negative proof that `precedent kept private` produces no public News;
7. News rotation/regression check alongside stock Republic ambient news.

## A3 integration note

This is a downstream read-only consequence of the integrated Republic customs-review arc. It should be reviewed as an ambient consequence layer, not as a replacement for the original dialogue or A1 customs-scrutiny simulation.

`DIALOGUE_SYSTEM_STATUS`: integrated source arc consumed read-only

`DIALOGUE_SYSTEM_NEXT_GAP`: actual-game consent-bounded News visibility and negative privacy proof