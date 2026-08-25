# B2 Deep Veteran Shadow Compact Handoff — 2026-08-25

Verdict: READY for A3 review/integration. Keep draft/unmerged; A3 retains integration authority.

## Authority
- Repository: `Wiredshark/star`
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-deep-veteran-shadow-compact-20260825`
- Production commit: `36b64bc59ef2a9102f1c9dfe9addee69f1202b6c`
- Focused validator commit: `fa082ec96163e1bd4022eafacca47e95e306ac37`
- Exact fully validated production/validator/handoff candidate: `9ac0032921615042ff4b3e0e479a0ec198569cf1`

## Character / dynamic-content behavior
Adds Eva Pell, an older Deep mechanic, and Lio Marr, a younger escort pilot reacting to the player's real combat progression. Offer requires `combat rating >= 80`; Review contains a dynamic `combat rating >= 160` branch so the relationship reacts if the player's reputation grows.

Routes: decision reasoning rather than signature-move imitation; independent judgment with explicit disagreement; paired observed-example/current-assessment notes; refusal. Three substantive routes schedule Review after 7–11 days. Review resolves into independent-practice records or explicit mentor attribution. `Lio Remembers` is one-shot aftermath.

## Ownership / lifecycle
- Reads built-in RPG `combat rating` only.
- Writes only `B2 Deep Veteran Shadow Compact:*`.
- No `world:*`, B1/A1/A2, material, reputation, cargo, equipment, ship, fleet, combat, or government-attitude mutation.
- All seven state-only terminals use `decline`; zero `accept`.
- Refusal cannot introduce the arc or schedule Review.

## Focused validation
The focused validator proves route-local writes and 7–11 day scheduling, refusal suppression, Review lifecycle gates, route-aware Review branches, settlement-local writes and closure, the two-settlement one-shot aftermath gate, B2-only assignments, no objective-bearing mission directives, seven declines/zero accepts, and the observed-example/current-judgment boundary.

## Exact validation evidence
Exact candidate `9ac0032921615042ff4b3e0e479a0ec198569cf1`:
- `Fork simulation and story validation` #636 / run `32910762157`: SUCCESS.
  - focused Python compilation: SUCCESS.
  - all focused story validators: SUCCESS.
  - A1 simulation/state-ownership contracts: SUCCESS.
  - changed-content style: SUCCESS.
- `Fork save-load integration smoke` #621 / run `32910762156`: SUCCESS.
  - dependency installation: SUCCESS.
  - production configure/build: SUCCESS.
  - stock save-load smoke: SUCCESS.

## Canon / continuity
Observed veteran actions, reputation, present objective, learner interpretation, current judgment, mentor advice actually given, disagreement, and current responsibility remain separate facts. A growing combat reputation does not turn simplified stories into doctrine, and one mentoring relationship does not establish Deep command doctrine or Pilot Guild law.

## A3 / B3 integration notes
Keep branch isolated and unmerged. Re-read current main, active B1/A2/B2 work, ancestry, mergeability, and exact workflow state before integration. No save migration is required because production persistence names/values were stable through validation.
