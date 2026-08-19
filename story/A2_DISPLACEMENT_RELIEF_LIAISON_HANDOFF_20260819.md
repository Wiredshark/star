# A2 Displacement Relief Liaison — Handoff

Verdict: **PARTIAL pending exact-head repository-native validation and actual-game acceptance.**

- Authoritative base: `main` @ `6dc761ac941794c8b1125978d7bcd6eb811e3951`
- Branch: `agent/a2-displacement-relief-liaison-20260819-1102`
- Production commit: `e9a84edfd90c0f8c319b28754a1387993ca44a99`
- Validator commit: `aad5c072ef55070e02b49bda12d790af99abb696`

## RPG / simulation feedback loop

This slice consumes the newly integrated A1 Republic-displacement -> Free Worlds relief spillover. During the A1 five-day spillover latch, Imani Vale makes the cross-border cause player-visible and asks how relief records should preserve it. The player chooses anonymous bounded provenance, aggregate-only capacity tracking, consent-led case linkage, or refusal.

After the A1 latch ends, a second one-shot review combines each positive policy with the *current* Republic displacement pressure (`>= 4` severe vs `< 4` eased), yielding six deterministic outcomes plus refusal-respected handling. The result is a connected loop: A1 cross-system pressure -> player-facing A2 policy -> later live A1 state -> history-aware A2 consequence.

## Ownership / persistence invariants

A1 remains sole writer of `world: republic displacement relief spillover active`, `world: republic displacement pressure`, and `world: free worlds relief demand`. This slice reads the first two and writes only `A2 Displacement Relief Liaison:*` conditions. No existing Free Worlds relief-coordination state is rewritten. Refusal is recorded as refusal, not authorization.

The new A2 state uses ordinary mission conditions, so it follows the surrounding engine's existing save serialization behavior without a new save schema or migration.

## Validation required

Run `python3 tools/story/validate_a2_displacement_relief_liaison.py`, the repository-wide focused story/simulation validators, changed-content style gate, and stock build/save-load smoke against the exact final branch head. In the actual game, verify offer only during the spillover latch, all four choices, both severe/eased follow-up branches for each positive policy, refusal handling, save/reload across the latch boundary, and offer-precedence interaction with Imani Vale's existing relief-coordination missions.

## A3 integration

Do not self-integrate. Re-read current `main`, require exact-head green validation, and preserve A1 ownership of all `world:*` inputs. This slice is additive and should remain separate from the existing Free Worlds relief-coordination policy unless A3 deliberately resolves offer-ordering conflicts.
