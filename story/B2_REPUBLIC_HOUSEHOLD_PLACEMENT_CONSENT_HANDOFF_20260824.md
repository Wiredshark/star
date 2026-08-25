# B2 Republic Household Placement Consent — Handoff

Verdict: READY for A3 review/integration.

Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`

Branch: `agent/b2-republic-household-placement-consent-20260824`

Production commit: `b0f75083405bd6f4a4c6b7d87ce4d06d1edb19f2`

Focused validator commit: `746e64ddcf21ec98d34ad12cfffc54c6c6e005ff`

Exact fully validated production/validator/handoff candidate: `9d02459f9c93288c361e20353bfeb7d7b67af7a9`

## Character / dynamic-content behavior

This slice returns Lena Orr after integrated `A2 Republic Resettlement Council: followup seen` and introduces adult siblings Nadia Kess and Owen Kess. An emergency household-contact record has been copied downstream as though Nadia retained authority over Owen's durable residence and placement choices.

The opening dialogue reacts to the saved A2 policy route: family unity, work continuity, or distributed placement each explains a different way the emergency system could have elevated one household contact. B2 never writes those A2 states.

Player approaches:

- separate individual adult consent from emergency household coordination;
- retain a household representative only for explicit tasks, scope, duration, and revocation;
- keep paired emergency-placement and durable-consent records;
- refusal, which records refusal but does not arm Review.

Three substantive routes schedule a 7–11 day Review. Review resolves into either a portable consent packet or expiry-and-renewal. `Owen Remembers` is a one-shot aftermath reader.

## Ownership / persistence

- Reads integrated `A2 Republic Resettlement Council: followup seen` and the three A2 policy-route memories.
- Writes only `B2 Republic Household Placement Consent:*`.
- Does not write A1/A2/B1 or `world:*` state.
- No credits, reputation, cargo, equipment, ship, fleet, combat, or government-attitude mutations.
- All seven dialogue/state-only terminal branches use `decline`.
- Refusal cannot write `introduced`, a substantive route, or schedule Review.

## Canon / continuity assumptions

Emergency coordination, household contact, durable adult consent, present representative authority, task scope, expiry, revocation, and historical placement evidence remain separate facts. A person may have legitimately helped another adult during displacement without acquiring permanent authority over that adult's residence or contracts. This local correction does not establish universal Republic household law.

## Exact validation evidence

On exact candidate `9d02459f9c93288c361e20353bfeb7d7b67af7a9`:

- `Fork simulation and story validation` run `32805306041` / #574: SUCCESS.
- Focused simulation/story contracts: SUCCESS.
- All focused story validators: SUCCESS.
- A1 simulation contract tests: SUCCESS.
- Changed fork content style: SUCCESS.
- `Fork save-load integration smoke` run `32805306105` / #559: SUCCESS.
- Production configuration: SUCCESS.
- Production build: SUCCESS.
- Stock save-load smoke: SUCCESS.

Exact base-to-candidate comparison: 3 commits ahead / 0 behind, exactly three added files, 370 additions, zero deletions.

## Files

- `data/human/b2 republic household placement consent.txt`
- `tools/story/validate_b2_republic_household_placement_consent.py`
- `story/B2_REPUBLIC_HOUSEHOLD_PLACEMENT_CONSENT_HANDOFF_20260824.md`

## A3 / B3 integration notes

A3 must re-read current `main` and mergeability before integration. Do not self-integrate. Preserve A2 ownership of the Resettlement Council policy memories and the distinction between historical emergency coordination and current adult consent/authority.
