# A2 Republic Border Alert Practice handoff

Verdict: PARTIAL pending exact-head repository-native validation and actual-game acceptance.

- Authoritative base: `fdaf94f18aaa02abd4e7269196375572cd0fdf9b`
- Branch: `agent/a2-republic-border-alert-practice-20260820-0810`
- Production commit: `ad6e4b9a80ed7732905d2df02203decb5373c051`
- Validator commit: `400451f127b342f5c6ab0d29b64c0df862a6c47c`

## RPG loop
At authoritative A1 Republic border pressure >=4, Mara Vey asks the player to choose current-factual-basis discipline, protected civilian/medical/relief continuity, explicit alert review points, or refusal. After A1 border pressure recovers to <=2, a one-shot review demonstrates a route-specific consequence.

## Invariants
- A1 remains sole writer of `world: republic border pressure`.
- Arrival from Pirate space is a trigger for general security attention, not evidence of individual guilt.
- A2 does not claim the player's policy caused A1 pressure recovery.
- Refusal is persisted and is not converted into consent.
- All new writes are confined to `A2 Republic Border Alert Practice:*`.
- No Republic office, credential, enforcement power, or representative authority is granted.

## Concurrency boundary
Open A2 inventory was inspected before branching. Existing Republic A2 candidates cover customs-review/history, displacement-relief, resettlement, and civic capacity. No open A2 candidate targets the A1 border-pressure alert itself. Open B1 Republic border-security history is observational and remains untouched.

## Validation required before A3
Run exact-head focused/story/simulation/style validation and stock build/save-load smoke. Then exercise actual-game initial pressure >=4 gating, all four choices, recovery <=2 gating, save/reload between stages, one-shot suppression, and Republic offer-precedence regression. Do not self-integrate.
