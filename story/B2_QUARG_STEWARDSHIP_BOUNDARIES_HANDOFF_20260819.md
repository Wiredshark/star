# B2 Quarg Stewardship Boundaries handoff — 2026-08-19

## Verdict

**PARTIAL pending stock save-load workflow completion.** The exact production/data/validator head is simulation/story/style green. Do not integrate if the associated save-load workflow later fails.

## Repository and branch

- Repository authority: `Wiredshark/star`
- Authoritative `main` observed at B2 start: `fda6705d533559f31ea98a5f5e42e5b1d4e161af`
- B1 Quarg parent/final head: `58083c55af8242ca8001f3ad5b84b7f524712503`
- Isolated B2 branch: `agent/b2-quarg-stewardship-boundaries-20260819-0428`
- Production commit: `6e4a2add580e54331daf68a9f7d5dad17b46ba12`
- Exact production/data/validator head: `0587544d7b06c1e8c6613600873325c31367d79a`
- Draft PR: `#69`

## Slice

`data/quarg/b2 quarg stewardship boundaries.txt` turns B1's **Protected Community Ledger** into a persistent present-day character problem: a recurring Quarg refuge steward must decide how protection can remain a duty without silently becoming permanent jurisdiction over a protected community.

The Offer appears only after Quarg first contact and after the B1 Protected Community Ledger has been offered. The player can choose:

1. **Local autonomy first** — transfer ordinary decisions while reserving Quarg intervention for explicit survival emergencies.
2. **Accountable protection** — keep temporary joint review, but every intervention receives a written reason and expiration point.
3. **Dual ledger** — separate local decisions from Quarg protection obligations so neither can silently rewrite the other.
4. **Refusal** — the Quarg explicitly treats refusal as non-consent rather than silently recording approval.

A delayed Review exposes failure modes in the initial approach and resolves into one of two persistent terminal arrangements:

- **Narrow stewardship covenant** — local authority is the default; intervention requires a named survival trigger, explicit scope, and automatic review.
- **Paired-duty register** — local decisions and Quarg aid obligations remain separate; intervention requires either a local request or an immediate survival threat.

`Steward Remembers` is a one-shot later reader of either settlement and preserves the recurring steward as a character who remembers the player's reasoning.

## Authority and canon invariants

- Every writable condition is prefixed `B2 Quarg Stewardship Boundaries:`.
- B2 does not write Quarg/Korath/Drak campaign state or `world:*` simulation state.
- B2 does not mutate credits, reputation, cargo, outfits, ships, fleets, or combat rating.
- The slice does not claim that Quarg protection equals sovereignty, annexation, or permanent political subordination.
- The protected community is intentionally left unnamed so B2 does not overwrite the established Korath Efreti relationship or invent a new canonical protectorate identity.
- The slice consumes B1's institutional-history concept without expanding the intentionally underspecified Drak/pathway technology.

## Files

- `data/quarg/b2 quarg stewardship boundaries.txt`
- `tools/story/validate_b2_quarg_stewardship_boundaries.py`
- `story/B2_QUARG_STEWARDSHIP_BOUNDARIES_HANDOFF_20260819.md`

## Validation evidence

Exact production/data/validator head: `0587544d7b06c1e8c6613600873325c31367d79a`.

GitHub Actions `Fork simulation and story validation` run `32233029125`: **SUCCESS**.

Observed job evidence:

- `Changed fork content style`: **SUCCESS**.
- `Focused simulation and story contracts`: validator compilation **SUCCESS**.
- `tools/story/run_focused_validators.py`: **SUCCESS**, including the new Quarg validator.
- A1 simulation contract tests: **SUCCESS**.

The focused Quarg validator checks:

- exactly three missions plus the delayed event;
- B1 Protected Community Ledger offered-state dependency;
- recurring steward continuity across Offer/Review/aftermath;
- three persistent routes plus refusal;
- exactly two terminal settlements;
- Quarg government scoping;
- local `goto`/`label` integrity;
- B2-only condition mutation;
- absence of material/reputation reward mutation;
- later-reader consumption of both terminal states.

Exact base-to-validator-head compare: **2 commits ahead, 0 behind**, two added files, 277 additions, zero deletions, and no unrelated file changes.

GitHub Actions `Fork save-load integration smoke` run `32233029192` was still **IN PROGRESS** when this handoff was written. No save-load PASS is claimed yet.

The private execution host was inspected before using it: its repository workspace points to `Wiredshark/fallout-test`, not `Wiredshark/star`, and it was already dirty. It was left untouched and is not claimed as Endless Sky runtime evidence.

## A3 integration notes

Integration order is strict:

1. B1 Quarg stewardship institutional history at `58083c55af8242ca8001f3ad5b84b7f524712503`.
2. This B2 Quarg Stewardship Boundaries branch.

Before integration, A3 should confirm:

- exact production/data/validator head `0587544d7b06c1e8c6613600873325c31367d79a` remains simulation/story/style green;
- save-load run `32233029192` completed successfully;
- the B1 `Quarg History: Protected Community Ledger: offered` condition is present after B1 integration;
- no later Quarg branch has claimed conflicting stewardship/protectorate semantics.

If the save-load workflow fails, keep this candidate PARTIAL and repair on the isolated B2 branch before integration.
