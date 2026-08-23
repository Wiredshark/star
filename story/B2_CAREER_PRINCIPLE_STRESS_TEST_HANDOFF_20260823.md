# B2 Career Principle Stress Test Handoff — 2026-08-23

Verdict: **READY for A3 review/integration**

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative integration branch observed/rechecked: `main`
- Exact authoritative base SHA: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated B2 branch: `agent/b2-career-principle-stress-test-20260823`
- Production commit: `5ff24eda401d7ac22cb419f0814e4dc63b597b45`
- Focused-validator commit: `def7406d276b350a03a9435b62ff2bc4a29847cd`
- Exact fully validated production/validator/handoff candidate: `ec93d63496cbf3162e8d63ee8a5596b921d5b4f0`

## Non-overlap / concurrency

This slice deliberately avoided the active global B2 dialogue-lifecycle audit and does not modify an existing B2 arc. It is new additive character/dynamic content built directly on authoritative `main`.

Existing B2 coverage already handles Republic border testimony, displacement, tracing, customs mentorship, manifest appeal, and civic case continuity. This slice uses a separate player-character axis: **whether an earlier self-described command principle should acquire authority when a newer captain copies it under different conditions**.

The private execution-service process inventory reported four pre-existing service-owned processes; none were killed or modified.

## Character and dynamic-content behavior

The slice deepens canonical fork character **Nia Calder** from `A2 Career Review` and introduces younger independent captain **Rafi Sorn**.

Offer conditions:

- consumes `A2 Career Review: later reader seen`;
- requires one of the A2 principles (`margin`, `force`, or `options`), excluding the earlier refusal route;
- reacts to A1-owned `world: republic border pressure >= 4`;
- writes only `B2 Career Principle Stress Test:*` persistence.

Initial player approaches:

1. keep the original principle as a default unless current evidence disproves it;
2. keep the principle but record explicit exceptions and review triggers;
3. treat the principle as a hypothesis that must continue earning authority from evidence;
4. refuse to turn one captain's old self-description into another captain's template.

Each substantive route schedules a delayed Review after 7–11 days.

Review conditions:

- requires A1 border pressure to recover to `<= 2`;
- compares the remembered A2 principle against Sorn's actual high-pressure decisions;
- exposes source/context loss in downstream copies.

Terminal settlements:

- **portable command-rationale packet** — principle, source, present conditions, exception/revision, observed outcome, uncertainty, and review point travel together;
- **revalidation cycle** — old principles remain historical evidence, while each serious new pressure phase requires a fresh current decision record.

`Sorn Remembers` is a later one-shot reader showing the chosen model operating in practice.

## Ownership and persistence invariants

- A1 remains sole writer of `world: republic border pressure`.
- A2 remains sole writer of every `A2 Career Review:*` condition.
- B2 writes only `B2 Career Principle Stress Test:*` conditions.
- No credits, reputation, cargo, outfits, ships, fleets, combat rating, or other material state are mutated.
- All seven dialogue/state-only terminal paths use `decline`; this slice introduces no objective-less accepted mission lifecycle.
- No save schema change or migration is required.

## Continuity / canon boundary

A remembered player command principle is **evidence about one captain's prior self-description**, not standing authority, Pilot Guild doctrine, or Republic law. Current conditions, exceptions/revisions, observed outcomes, uncertainty, source lineage, and review state remain distinct. Repetition of one copied teaching note does not become independent corroboration.

## Files

- `data/human/b2 career principle stress test.txt`
- `tools/story/validate_b2_career_principle_stress_test.py`
- `story/B2_CAREER_PRINCIPLE_STRESS_TEST_HANDOFF_20260823.md`

## Validation evidence

Exact candidate `ec93d63496cbf3162e8d63ee8a5596b921d5b4f0` passed both repository-native acceptance workflows:

- `Fork simulation and story validation` #490 / run `32651868253`: **SUCCESS**
  - focused story validators: passed;
  - `validate_b2_career_principle_stress_test.py`: passed as part of focused validator discovery;
  - A1 simulation/state-ownership contracts: passed;
  - changed-content style: passed.
- `Fork save-load integration smoke` #475 / run `32651868245`: **SUCCESS**
  - production configuration: passed;
  - production build: passed;
  - stock save-load integration smoke: passed.

Isolation against the selected base was also verified:

- status: ahead;
- ahead by: 3;
- behind by: 0;
- changed files: exactly 3;
- additions: 440;
- deletions: 0.

## A3/B3 integration notes

- Re-read current `main` before integration in case it advances after this handoff.
- Preserve A1/A2 ownership boundaries exactly.
- Do not collapse the prior command principle into a binding rule.
- Preserve the distinction among source principle, present conditions, exception/revision, outcome, uncertainty, and current authority.
- This candidate is suitable for A3 review/integration under the documented process; B2 did not self-integrate.
