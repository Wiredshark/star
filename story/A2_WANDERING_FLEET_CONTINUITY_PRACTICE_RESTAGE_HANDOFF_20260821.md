# A2 Wandering Fleet Continuity Practice current-main restage

Verdict: PARTIAL pending exact-head repository-native validation.

- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`.
- Branch: `agent/a2-avgi-wandering-fleet-practice-restage-20260821-1405`.
- Production restage: `5b0a8167a7d59d22908e42e9efcb1510639f11d1`.
- Strengthened validator: `7d0f8d0f204a8eb4baebd39bc90ab38db3b91038`.

## Scope

Restages the historical Wandering Fleet continuity practice onto current authoritative main. After integrated B2 aftermath, the player chooses repair-success/system-restoration separation, dependency provenance, local-only handling, or refusal. A later one-shot reflection demonstrates a distinct consequence for each positive route.

## Repairs and invariants

- B2 and world state remain read-only; all writes are `A2 Wandering Fleet Continuity Practice:*`.
- All five objective-less dialogue terminals persist state and use `decline`, never `accept`.
- Both missions use `offer precedence 9`.
- Refusal does not arm reflection.
- Successful recipient repair does not imply restored fleet resilience.
- Compatibility does not imply equivalence; emergency borrowing does not erase donor obligations.
- Loadkeeper/Fitter remain player-private shorthand; no Avgi office or representative authority is created.
- Language, refit, and not-lost gates are retained.

## Concurrency

Historical PR #177 remains untouched. This clean restage is derived directly from current main because #177 had a story/simulation failure and later became stale against advancing integration state. Other current A2 restages cover separate faction/system surfaces.

## Validation boundary

Run exact-head Fork simulation/story/style and Fork save-load integration smoke. Promote to READY only if both are terminal green. A3 retains integration authority; do not self-merge.
