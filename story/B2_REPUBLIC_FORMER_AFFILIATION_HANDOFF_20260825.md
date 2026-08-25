# B2 Republic Former Affiliation Compact Handoff — 2026-08-25

Verdict: PARTIAL pending replacement exact-head production build/save-load completion.

- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-republic-former-affiliation-20260825`
- Production commit: `5a5dd70d8c8815218555fc926f4f76286cb905ce`
- Focused validator commit: `4d40bf5bd387d0e46fdd16f694c238dd31c5954d`
- Exact production/validator candidate: `f9cb481aa910dcc6d772c31cb4189c83d30aecfe`

## Behavior
Adds Mira Sol and Devon Pryce in a persistent three-mission Republic character arc about old crew membership being copied as present affiliation. Routes separate dated historical membership, bounded former-crew references, and paired historical/current affiliation records; refusal does not schedule Review. Review resolves into either a portable affiliation packet or expiry plus fresh acknowledgement. `Devon Remembers` is one-shot aftermath.

## Ownership and lifecycle
All writes are `B2 Republic Former Affiliation Compact:*`. No `world:*`, A1/A2/B1, material, reputation, cargo, equipment, ship, fleet, or combat mutation. All seven state-only terminal paths use `decline`; refusal cannot arm Review.

## Continuity
Historical crew membership, observed work, former-crew reference, current affiliation, present sponsorship, responsibility, loyalty, and closure remain separate facts. An accurate old roster does not become current affiliation simply because it is repeatedly copied. This is a local employment-record practice, not universal Republic law.

## Exact validation state
On exact production/validator candidate `f9cb481aa910dcc6d772c31cb4189c83d30aecfe`:
- `Fork simulation and story validation` #576 / run `32809256512`: **SUCCESS**;
- focused story validators: **SUCCESS**;
- A1 simulation/state-ownership contracts: **SUCCESS**;
- changed-content style: **SUCCESS**;
- `Fork save-load integration smoke` #561 / run `32809256500`: **CANCELLED** during production build; this is not acceptance evidence.

This handoff-only recovery commit intentionally leaves production and validator behavior unchanged and triggers replacement exact-head repository workflows. Do not promote to READY until the replacement save-load gate is terminal green.

## A3 boundary
Do not self-integrate. Re-read current main, open B2/A2/B1 work, ancestry, mergeability, and exact workflow state before integration.
