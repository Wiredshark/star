# A2 Merchant Diversion Evidence Practice handoff — 2026-08-20

## Verdict

PARTIAL pending exact-head repository-native validation and actual-game acceptance. Do not self-integrate; A3 owns integration.

## Exact repository state

- Repository: `Wiredshark/star`
- Authoritative integration branch: `main`
- Authoritative base SHA: `7c8009bd1a26b09d464ab9a2dae11fb69c7f95e2`
- Isolated branch: `agent/a2-merchant-diversion-evidence-practice-20260820-0405`
- Production commit: `f20e9e6231480d54a2b9d4fca0319249033f0373`
- Focused validator commit: `4f149bb7704f068b1f759ca67a2996b615e56158`
- This handoff commit is the branch head after publication.

## Selection and concurrency

Current `main`, recent open A2 work, Merchant A2 branches, and the newly integrated B2 Merchant Diversion Compact were inspected before authoring.

Existing Merchant A2 candidates cover repair backlog and recovery-margin capacity. No A2 Merchant branch consumes the newly integrated B2 route-diversion docket/evidence-ladder settlements. This slice therefore occupies a separate route-evidence/expiry domain.

The exposed private execution host was also checked. Its service process inventory reports five pre-existing service-owned orphan processes, which were left untouched. Its repository workspace remote is `Wiredshark/fallout-test`, not `Wiredshark/star`, and the workspace is already dirty. It is therefore not valid Endless Sky runtime evidence and was not modified.

## RPG / dynamic narrative loop

The upstream B2 compact is already resolved before this A2 slice begins. `A2 Merchant Diversion Evidence Practice: Briefing` requires `B2 Merchant Diversion Compact: aftermath seen`.

Nessa Ward asks what should travel from the previous compact into future route warnings. The player can persist one of three private operating practices or decline:

1. **expiry** — every copied detour keeps the condition that ends or renews it;
2. **lineage** — repeated copies preserve source ancestry and never manufacture independent confirmation;
3. **contradiction** — later disconfirming evidence travels as visibly as the warning it weakens;
4. **decline** — no standing player-backed practice is established.

Because B2's review/aftermath occurs only after A1 route-diversion pressure has recovered, the second mission naturally waits for a later recurrence. `A2 Merchant Diversion Evidence Practice: Recurrence` requires authoritative `world: merchant route diversion pressure >= 3`.

Each positive practice has a normal recurrence outcome and a severe-pressure (`>= 5`) outcome, yielding six deterministic world-state-sensitive consequences. Refusal does not arm the recurrence mission.

## Acceptance invariants

- A1 remains sole writer of `world: merchant route diversion pressure` and all upstream rescue/congestion/recovery state.
- B2 remains sole writer of `B2 Merchant Diversion Compact:*`.
- A2 writes only `A2 Merchant Diversion Evidence Practice:*`.
- Repeated copies of one warning do not become independent observations.
- Expired advice remains historical evidence rather than current routing truth.
- Contradictory evidence lowers confidence without retroactively erasing the original observation.
- No centralized Merchant route authority is created; participation remains compatible with independent carrier judgment.
- No credits, reputation, cargo, outfit, ship, fleet, or combat semantics are changed.

## Files

- `data/human/a2 merchant diversion evidence practice.txt`
- `tools/story/validate_a2_merchant_diversion_evidence_practice.py`
- `story/A2_MERCHANT_DIVERSION_EVIDENCE_PRACTICE_HANDOFF_20260820.md`

## Validation

Completed before handoff:

- exact `main` SHA recovered immediately before branch creation;
- current open A2 PRs and Merchant A2 branch inventory inspected for overlap;
- integrated B2 Merchant Diversion Compact and A1 Merchant route-diversion implementation inspected for exact state names, thresholds, recovery semantics, and ownership;
- focused validator added to the repository's normal `tools/story/validate_*.py` discovery surface;
- private host process/workspace boundary checked; unrelated Fallout workspace left untouched.

Not yet claimed:

- focused validator execution;
- exact-head `Fork simulation and story validation` success;
- exact-head `Fork save-load integration smoke` success;
- actual-game offer/branch/persistence behavior.

## Remaining gates

1. Exact-head story/simulation/style workflow succeeds.
2. Exact-head production build/save-load smoke succeeds.
3. Actual-game B2-aftermath gating.
4. All three positive practices plus refusal.
5. Future A1 diversion recurrence at pressure 3-4 and severe pressure >=5.
6. All six positive recurrence outcomes.
7. Negative proof that refusal does not arm recurrence.
8. Save/reload between briefing and recurrence.
9. One-shot suppression and Merchant offer-precedence regression.

## A3 integration instructions

Re-read current `main` immediately before integration because concurrent A/B work is expected. Verify base ancestry/conflicts, preserve A1/B2 ownership, and integrate only after exact-head repository-native validation is terminal green. Do not merge this branch from A2.
