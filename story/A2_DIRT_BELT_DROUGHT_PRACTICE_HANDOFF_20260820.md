# A2 Dirt Belt Drought Practice handoff — 2026-08-20

Verdict: PARTIAL pending exact-head repository-native validation and actual-game acceptance.

Authoritative base: `main@f6c6d272fcf869092795f1ac534732339cdb1829`
Branch: `agent/a2-dirt-belt-drought-practice-20260820-1406`
Production commits: `eb45492f439e4692dc7a07d63fa6f70ba2391723`, header correction `5dc0dbaf772d80291bfb354af5da0555d8947a86`
Focused validator commit: `003978abea8cf0951d7bad170c647d89a32e3117`

## RPG / narrative loop
Consumes authoritative A1 Dirt Belt drought pressure and irrigation-reserve strain read-only. At drought pressure >=3 and irrigation strain >=2, Mara Dene asks the player to choose a reserve floor, restoration-obligation tracking, current-condition review, or refusal. Positive choices persist. Once both A1 pressures recover to <=1, a one-shot review demonstrates a route-specific consequence.

## Invariants
- A1 remains sole writer of `world: dirt belt drought pressure` and `world: dirt belt irrigation reserve strain`.
- The stock `Drought Relief` job is not mutated.
- All new persistent writes are under `A2 Dirt Belt Drought Practice:*`.
- Relief delivery and restored irrigation capacity are distinct outcomes.
- Historical drought evidence does not become permanent priority.
- Borrowed water, pump time, and maintenance remain obligations until capacity is actually restored.
- Refusal is not consent and does not arm the recovery review.
- No Republic or Dirt Belt representative authority is granted.

## Files
- `data/human/a2 dirt belt drought practice.txt`
- `tools/story/validate_a2_dirt_belt_drought_practice.py`
- this handoff

## Validation / A3 gate
The focused validator is committed but no repository-native exact-head result is claimed in this handoff commit. A3 should require exact-head focused story/simulation/style validation, production build/save-load smoke, actual-game initial gating, all four choices, recovery gating, persistence across save/reload, one-shot suppression, and Dirt Belt offer-precedence regression. Do not self-integrate from A2.