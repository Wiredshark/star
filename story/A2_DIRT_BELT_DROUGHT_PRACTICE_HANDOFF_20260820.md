# A2 Dirt Belt Drought Practice handoff - 2026-08-21

Verdict: PARTIAL pending refreshed exact-head repository-native validation.

Current authoritative main recovered before repair: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
Original branch base: `main@f6c6d272fcf869092795f1ac534732339cdb1829`
Branch: `agent/a2-dirt-belt-drought-practice-20260820-1406`
Original candidate head: `af3b925a4dddad3c6201131f30f3bb524ad00482`
Lifecycle production repair: `8fe6b3d7232a7f490aa3da1ba302f7ddba2f6698`
Lifecycle validator repair: `b7022f3230cc1bb93cdfac47cd3ca2bcf6407b2f`

## RPG / narrative loop
Consumes authoritative A1 Dirt Belt drought pressure and irrigation-reserve strain read-only. At drought pressure >=3 and irrigation strain >=2, Mara Dene asks the player to choose a reserve floor, restoration-obligation tracking, current-condition review, or refusal. Positive choices persist. Once both A1 pressures recover to <=1, a one-shot review demonstrates a route-specific consequence.

## Lifecycle repair
The original candidate used `accept` after the three positive Briefing choices and after the Recovery Review. These missions contain only dialogue and persistent-state writes; they have no gameplay objective. Current engine lifecycle semantics would therefore leave objective-less accepted missions behind.

The repaired production file preserves all existing narrative text, thresholds, route names, A1 ownership, and persistent A2 state, but every terminal dialogue path now ends with `decline` after recording its state. Refusal already used `decline`.

The focused validator now rejects any state-only `accept` endpoint and requires all five terminal paths (three positive briefing routes, refusal, and recovery review) to terminate with `decline`.

The repair also restores the repository-standard full GPL content header and a final newline, addressing the prior exact-head story/style failure surface without changing gameplay semantics.

## Invariants
- A1 remains sole writer of `world: dirt belt drought pressure` and `world: dirt belt irrigation reserve strain`.
- The stock `Drought Relief` job is not mutated.
- All new persistent writes are under `A2 Dirt Belt Drought Practice:*`.
- Relief delivery and restored irrigation capacity are distinct outcomes.
- Historical drought evidence does not become permanent priority.
- Borrowed water, pump time, and maintenance remain obligations until capacity is actually restored.
- Refusal is not consent and does not arm the recovery review.
- State-only conversations must not remain in the accepted mission list.
- No Republic or Dirt Belt representative authority is granted.

## Prior validation evidence
On original head `af3b925a4dddad3c6201131f30f3bb524ad00482`:
- Fork save-load integration smoke run `32401531131`: SUCCESS.
- Fork simulation and story validation run `32401531406`: FAILURE.

The original red story/style result is superseded for acceptance by the repaired head and must not be presented as a passing gate.

## Required refreshed gate
Require both repository-native workflows to finish successfully on the exact repaired handoff head before promoting this candidate to READY:
1. Fork simulation and story validation = SUCCESS.
2. Fork save-load integration smoke = SUCCESS.

Actual-game exploratory acceptance may additionally exercise high-pressure offer gating, all four choices, dual-state recovery gating, save/reload between stages, one-shot suppression, and Dirt Belt offer precedence. No self-integration from A2.
