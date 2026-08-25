# B2 Republic Former Affiliation Compact Handoff — 2026-08-25

Verdict: READY for A3 review/integration.

- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-republic-former-affiliation-20260825`
- Production commit: `5a5dd70d8c8815218555fc926f4f76286cb905ce`
- Original focused validator commit: `4d40bf5bd387d0e46fdd16f694c238dd31c5954d`
- Lifecycle/cardinality validator hardening: `44bca8b0db7993ef69819ea6a1129d06568384c0`
- Aftermath-validation repair / exact fully validated candidate: `6686f59eecaadddcf3628d94a1007a03808f9969`

## Behavior
Adds Mira Sol and Devon Pryce in a persistent three-mission Republic character arc about old crew membership being copied as present affiliation. Routes separate dated historical membership, bounded former-crew references, and paired historical/current affiliation records; refusal does not schedule Review. Review resolves into either a portable affiliation packet or expiry plus fresh acknowledgement. `Devon Remembers` is one-shot aftermath.

## Ownership and lifecycle
All writes are `B2 Republic Former Affiliation Compact:*`. No `world:*`, A1/A2/B1, material, reputation, cargo, equipment, ship, fleet, or combat mutation. All seven state-only terminal paths use `decline`; refusal cannot arm Review.

## Validator hardening
The focused validator now proves:
- exactly three substantive routes write `introduced`, exactly one refusal write, exactly two Review closures, and exactly one aftermath write;
- each Offer choice reaches exactly one route label;
- each substantive route writes only its own route state, schedules Review exactly once for 7–11 days, and terminates exactly once;
- refusal writes no substantive route and cannot schedule Review;
- each Review choice reaches exactly one settlement label, writes only its own settlement, and closes Review exactly once;
- aftermath requires either settlement, is one-shot, and uses the renewal settlement a second time only to select renewal-specific dialogue.

The first hardening commit `44bca8b0db7993ef69819ea6a1129d06568384c0` exposed a validator-only counting defect: the renewal settlement is intentionally referenced twice in aftermath (eligibility plus route-specific dialogue). Production content and changed-content style were already valid. The validator was corrected in `6686f59eecaadddcf3628d94a1007a03808f9969`.

## Continuity
Historical crew membership, observed work, former-crew reference, current affiliation, present sponsorship, responsibility, loyalty, and closure remain separate facts. An accurate old roster does not become current affiliation simply because it is repeatedly copied. This is a local employment-record practice, not universal Republic law.

## Exact validation evidence
On exact fully validated candidate `6686f59eecaadddcf3628d94a1007a03808f9969`:
- `Fork simulation and story validation` #581 / run `32813874200`: **SUCCESS**;
- focused story validators, including the hardened Republic Former Affiliation validator: **SUCCESS**;
- A1 simulation/state-ownership contracts: **SUCCESS**;
- changed-content style: **SUCCESS**;
- `Fork save-load integration smoke` #566 / run `32813874209`: **SUCCESS**;
- dependency installation: **SUCCESS**;
- production configure/build: **SUCCESS**;
- stock save-load smoke: **SUCCESS**.

Earlier recovery head `ec324eb0b9c053c9b967845c90693e3972a036a7` also independently passed both repository-native workflows. The original production candidate's first save-load run was cancelled during build and was not used as acceptance evidence.

## A3 boundary
Do not self-integrate. Re-read current main, open B2/A2/B1 work, ancestry, mergeability, and exact workflow state before integration. The final READY update is handoff-only; production behavior is unchanged from the fully validated candidate above.
