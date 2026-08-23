# A2 Hicemus Contact Practice — current-main restage handoff

Verdict: **PARTIAL** pending exact-head repository-native validation.

- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-hicemus-contact-practice-restage-20260823-0506`
- Production restage: `fc41615ce1b4453b007892384d9dfccaf97e2d4b`
- Initial strengthened validator: `9a940162db3009a20805f0af600e7ca3db0b24c3`
- Validator terminal-count correction: `d2dacde659e19aefcec9e98b72787886e30a4ac7`

## Scope

This is a clean current-main restage of historical PARTIAL PR #117. After `Incipias: Help The Stranded 2: done`, an Incipias attendant asks what evidence-handling practice the player should carry forward from the Hicemus contact testimony register.

Persistent choices:

- observation-first: preserve witnessed facts before assigning meaning;
- revision-first: keep interpretation explicitly revisable as better evidence arrives;
- local-only: keep the lesson tied to the Hicemus contact context instead of universalizing it;
- refusal: do not adopt a standing practice.

The three positive routes drive explicit one-shot later Reflection branches. Refusal remains a true boundary and does not arm Reflection.

## Ownership and authority invariants

- `Incipias: Help The Stranded 2: done` is read-only.
- No `world:*` state is read or written.
- All persistent writes remain `A2 Hicemus Contact Practice:*`.
- Modern contact practice is not presented as a complete Hicemus language translation.
- Observation, interpretation, correction, inferred intent, and motive remain distinct.
- The player receives no Hicemus office, linguistic credential, endorsement, or representative authority.

## Current lifecycle architecture

- Both dialogue/state-only missions use `offer precedence 9`.
- Review has one converged `decline` terminal after persisting the selected route plus `decided`.
- Reflection has one `decline` terminal after persisting `reflection seen`.
- No state-only `accept` endpoint remains.
- Reflection explicitly gates observation-first, revision-first, and local-only routes.
- Refusal is excluded from Reflection with `not "A2 Hicemus Contact Practice: refused"`.

## Validation

The focused validator enforces mission count, upstream/world read-only ownership, A2 namespace isolation, precedence, state-only lifecycle, explicit positive-route Reflection gates, refusal suppression, absence of gameplay objectives, and the no-complete-language/no-authority boundaries.

Exact-head repository-native `Fork simulation and story validation` and `Fork save-load integration smoke` must both be terminal green before promotion to READY. No manual actual-game runtime result is claimed.

## A3 boundary

Do not self-integrate. A3 should re-read current `main`, verify ancestry/mergeability, and preserve all ownership, evidence-discipline, refusal, precedence, and state-only lifecycle invariants if this candidate becomes READY.
