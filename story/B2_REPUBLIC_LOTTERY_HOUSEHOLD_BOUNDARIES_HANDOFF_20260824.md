# B2 Republic Lottery Household Boundaries — Handoff

## Verdict

PARTIAL — production and focused validator are isolated on a current-main B2 branch. Repository-native simulation/story/style and production build/save-load workflows must be terminal green on the exact candidate before A3 integration.

## Authority

- Repository authority: `Wiredshark/star`
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-republic-lottery-household-20260824`
- Production commit: `db763dd31ae2549833fa76417afdebc8d7f893a7`
- Focused validator commit: `87d6113f51406fadb43d46de4d25aebe1f608732`

## Scope

Adds Near Earth siblings Mara and Elias Penn. Existing Republic culture already depicts ordinary lottery play and small winners immediately buying more tickets; this slice turns that background into a persistent household relationship conflict without diagnosing Elias or asserting a universal Republic gambling policy.

Player routes:

- household floor first: agreed rent, food, medicine, and explicit shared debts precede either sibling's claim over the other's personal spending;
- voluntary limit: Elias chooses a temporary limit/cooling-off period with review and expiry, without turning Mara into a financial guardian;
- paired records: shared obligations and explicit loans remain auditable while personal legal spending stays private once agreed obligations are met;
- refusal: no general rule is imposed and Review is not armed.

Positive routes schedule a 7–11 day Review. Review reacts read-only to A1 `world: republic civic strain` and then resolves to one of two settlements:

- portable household boundary record;
- expiry plus fresh cause.

`Elias Remembers` is the one-shot aftermath reader.

## Ownership and persistence

- Reads A1 `world: republic civic strain` only; A1 remains sole writer.
- All writes are `B2 Republic Lottery Household Boundaries:*`.
- No A1/A2/B1, credits, reputation, cargo, outfit, ship, fleet, or combat mutation.
- All 7 dialogue/state-only terminal paths use `decline`; no objective-less `accept` path is introduced.
- Refusal does not schedule Review.

## Canon / interpretation boundaries

- The existing lottery scene establishes that ordinary legal lottery play exists in Republic space; it does not establish a diagnosis, a universal policy, or a causal link between civic strain and lottery behavior.
- Household obligation, personal spending, explicit loans, voluntary limits, guardianship authority, historical worry, and current closure status remain separate facts.
- A repaid loan remains history rather than current debt.
- An expired voluntary limit remains history rather than a current judgment of competence.
- A new missed obligation can justify a new conversation; an old record alone does not manufacture fresh authority.
- One family's compromise is local household practice, not Republic law.

## Files

- `data/human/b2 republic lottery household boundaries.txt`
- `tools/story/validate_b2_republic_lottery_household_boundaries.py`
- `story/B2_REPUBLIC_LOTTERY_HOUSEHOLD_BOUNDARIES_HANDOFF_20260824.md`

## Validation

Pending repository-native exact-candidate validation:

- Fork simulation and story validation
- focused validator discovery/execution
- A1 simulation/state-ownership contracts
- changed-content style
- Fork save-load integration smoke
- production configure/build
- stock save-load smoke

## A3 / B3 integration notes

A3 retains integration authority. Do not self-integrate. Re-read current `main`, open B2 work, ancestry, and exact workflow state immediately before integration. Preserve A1 ownership of Republic civic strain and keep shared obligations, personal legal spending, voluntary limits, explicit loans, historical records, and current authority distinct.
