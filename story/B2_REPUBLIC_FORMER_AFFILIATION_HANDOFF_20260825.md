# B2 Republic Former Affiliation Compact Handoff — 2026-08-25

Verdict: READY for A3 review/integration.

- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-republic-former-affiliation-20260825`
- Production commit: `5a5dd70d8c8815218555fc926f4f76286cb905ce`
- Focused validator commit: `4d40bf5bd387d0e46fdd16f694c238dd31c5954d`
- Original production/validator candidate: `f9cb481aa910dcc6d772c31cb4189c83d30aecfe`
- Exact fully validated recovery head: `ec324eb0b9c053c9b967845c90693e3972a036a7`

## Behavior
Adds Mira Sol and Devon Pryce in a persistent three-mission Republic character arc about old crew membership being copied as present affiliation. Routes separate dated historical membership, bounded former-crew references, and paired historical/current affiliation records; refusal does not schedule Review. Review resolves into either a portable affiliation packet or expiry plus fresh acknowledgement. `Devon Remembers` is one-shot aftermath.

## Ownership and lifecycle
All writes are `B2 Republic Former Affiliation Compact:*`. No `world:*`, A1/A2/B1, material, reputation, cargo, equipment, ship, fleet, or combat mutation. All seven state-only terminal paths use `decline`; refusal cannot arm Review.

## Continuity
Historical crew membership, observed work, former-crew reference, current affiliation, present sponsorship, responsibility, loyalty, and closure remain separate facts. An accurate old roster does not become current affiliation simply because it is repeatedly copied. This is a local employment-record practice, not universal Republic law.

## Exact validation evidence
The original production/validator candidate `f9cb481aa910dcc6d772c31cb4189c83d30aecfe` passed `Fork simulation and story validation` #576 / run `32809256512`, while its first save-load run #561 / `32809256500` was cancelled during production build and is not treated as acceptance evidence.

A handoff-only recovery commit produced exact head `ec324eb0b9c053c9b967845c90693e3972a036a7` without changing production or validator behavior. That exact head passed both repository-native acceptance workflows:
- `Fork simulation and story validation` #578 / run `32813412627`: **SUCCESS**;
- `Fork save-load integration smoke` #563 / run `32813412582`: **SUCCESS**;
- dependency installation: **SUCCESS**;
- production configure/build: **SUCCESS**;
- stock save-load smoke: **SUCCESS**.

## A3 boundary
Do not self-integrate. Re-read current main, open B2/A2/B1 work, ancestry, mergeability, and exact workflow state before integration. This final READY update is handoff-only; production and validator behavior are the already validated behavior above.
