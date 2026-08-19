# A2 Republic Review Practice News Handoff — 2026-08-19

Verdict: **PARTIAL / specialist production candidate — actual-game acceptance still required**

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative integration branch: `main`
- Exact base SHA: `fda6705d533559f31ea98a5f5e42e5b1d4e161af`
- A2 branch: `agent/a2-republic-review-practice-news-20260819-0505`
- Production commit: `28cda6cfd804ebf5547d6f198cace9e1237f5568`
- Validator commit: `a3092f6774d2f2d089b8c8f942ddcf573b8778ea`

## Why this slice

The latest integrated B2 Republic Review Mentorship resolves the player's earlier customs-review precedent into one of two durable institutional training practices: an abstract safeguards record or supervised review circles. Before this slice, those outcomes had no player-visible feedback from the live A1 Republic customs-scrutiny simulation.

This A2 consumer closes that loop without taking ownership of B2 or A1 state:

`A2 customs consent -> B2 training settlement -> current A1 customs scrutiny -> ambient Republic consequence`

## Production behavior

Four Republic News groups are added:

1. safeguards record while customs scrutiny is below 3;
2. safeguards record while customs scrutiny is at least 3;
3. supervised review circles while customs scrutiny is below 3;
4. supervised review circles while customs scrutiny is at least 3.

Every public group requires:

- `B2 Republic Review Mentorship: aftermath seen`;
- the matching B2 settlement;
- `A2 Republic Customs Review: precedent use bounded`;
- explicit absence of `A2 Republic Customs Review: precedent kept private`.

The player is never named or attributed. Private precedent therefore remains private, and the News reports only institutional practice.

## Ownership invariants

A2 is read-only with respect to:

- `world: republic customs scrutiny`;
- both B2 mentorship settlement states;
- the upstream A2 Republic Customs Review consent states.

The production file contains no `action` block and writes no conditions.

## Files

- `data/human/a2 republic review practice news.txt`
- `tools/story/validate_a2_republic_review_practice_news.py`
- `story/A2_REPUBLIC_REVIEW_PRACTICE_NEWS_HANDOFF_20260819.md`

## Validation contract

The focused validator requires exactly four News groups, verifies the two B2 settlement branches and two A1 scrutiny bands, requires bounded-consent/private-exclusion gates on every group, and rejects writes to A1/B2/upstream-A2 authority.

Repository-native CI should additionally run the focused story validators, A1 simulation tests, cross-file ownership/graph checks, changed-content style validation, and stock save-load integration smoke.

## Remaining actual-game gates

Before A3 integration:

1. observe both safeguards-record News variants below and above the scrutiny threshold;
2. observe both review-circle News variants below and above the scrutiny threshold;
3. prove no News appears before the B2 mentorship aftermath resolves;
4. prove no News appears when `precedent kept private` is selected;
5. verify persistence after an actual save/reload;
6. review rotation/regression alongside existing Republic ambient News.

Do not integrate solely on source validation. Preserve the consent boundary and A1/B2 ownership invariants exactly as documented.
