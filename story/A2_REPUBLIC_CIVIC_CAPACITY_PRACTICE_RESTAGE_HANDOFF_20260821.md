# A2 Republic Civic Capacity Practice current-main restage — handoff

Verdict: PARTIAL pending exact-head repository-native validation.

- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-republic-civic-capacity-practice-restage-20260821-1805`
- Production restage: `0614e5ded1910826f54c1d530f516d055994d7ed`
- Strengthened validator: `33051eef1e6ca7f126297870592fddd78bf1a54c`

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

## Validation contract
The focused validator checks both missions, high-strain/recovery thresholds, four initial routes, namespaced persistence, A1 read-only ownership, exact state-only lifecycle terminal count, absence of objective-bearing directives, and offer precedence 8 on both missions.

## Required exact-head gates
Before promotion to READY, require terminal-green repository-native `Fork simulation and story validation` and `Fork save-load integration smoke` on the exact candidate head. Do not claim manual actual-game acceptance unless separately executed.

## A3 boundary
A3 retains integration authority. Re-read current `main`, verify ancestry/mergeability, preserve A1 ownership and the state-only `decline` lifecycle invariant, and integrate only the exact validated restage. Do not self-integrate from A2.
