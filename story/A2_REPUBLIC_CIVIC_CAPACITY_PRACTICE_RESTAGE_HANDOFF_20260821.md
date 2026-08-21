# A2 Republic Civic Capacity Practice current-main restage — handoff

Verdict: READY for A3 review/integration.

- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-republic-civic-capacity-practice-restage-20260821-1805`
- Production restage: `0614e5ded1910826f54c1d530f516d055994d7ed`
- Strengthened validator: `33051eef1e6ca7f126297870592fddd78bf1a54c`
- Exact validated production/validator head: `169e9e7d3682a19ee4cc97e70cd551f67c046439`
- `Fork simulation and story validation` run `32531593154` / #356: SUCCESS.
- `Fork save-load integration smoke` run `32531593048` / #341: SUCCESS.

## Scope
This is a clean current-main restage of historical PR #165. At authoritative A1 `world: republic civic strain >= 2`, Administrator Jo Ren asks the player to preserve case continuity, transparent real capacity/queue age, reviewable urgent exceptions, or refusal. Once A1 civic strain later recovers to `<= 1`, a one-shot recovery conversation demonstrates a route-specific consequence.

## Current architecture / invariants
- A1 remains sole writer of `world: republic civic strain` and its upstream displacement/customs sources.
- All new writes remain `A2 Republic Civic Capacity Practice:*`.
- Both state-only missions use `offer precedence 8`.
- All five state-only terminal paths persist state and terminate with `decline`; objective-less `accept` is forbidden.
- Refusal remains refusal and does not manufacture policy consent.
- Administrative coordination is not represented as creating missing housing, transport, reviewers, or other physical capacity.
- No Republic office, credential, enforcement authority, or representative role is created.

## Validation evidence
The exact production/validator head `169e9e7d3682a19ee4cc97e70cd551f67c046439` is terminal green in both repository-native gates: simulation/story/style run `32531593154` and production build/save-load run `32531593048`. The focused validator checks both missions, high-strain/recovery thresholds, four initial routes, namespaced persistence, A1 read-only ownership, exact state-only lifecycle terminal count, absence of objective-bearing directives, and offer precedence 8 on both missions.

Manual actual-game acceptance is not claimed; A3 should preserve that distinction during integration review.

## A3 boundary
A3 retains integration authority. Re-read current `main`, verify ancestry/mergeability, preserve A1 ownership and the state-only `decline` lifecycle invariant, and integrate only the validated production/validator content. Do not self-integrate from A2.
