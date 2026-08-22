# A2 Ka'het Evidence Practice Handoff — 2026-08-19

Verdict: PARTIAL pending exact-head repository-native validation and actual-game acceptance.

## Repository authority

- Authoritative integration branch at selection: `main`
- Authoritative base SHA: `8a2fd1576ec905d7a73803ba7e3ad3618dcec862`
- Isolated A2 branch: `agent/a2-kahet-evidence-practice-20260819-1706`
- Production commit: `bf1aa001b13ef4b1e6d383a5eb621d10e305d52c`
- Focused validator commit: `b97148031e1b50801b2dc8fe224947b5dd5a902e`

## Implemented RPG / narrative loop

The slice consumes the integrated B2 Ka'het Signal Interpretation aftermath read-only. After the Interpreter/Scout review has resolved, the player can decide what evidence-handling practice should travel beyond that particular dispute:

1. bounded hypothesis — translated historical traffic may guide investigation, but operational use retains source age, translation confidence, and expiry/recheck conditions;
2. contradiction preserved — unresolved conflict between translated traffic and present field observation follows every downstream summary until new evidence closes it;
3. local only — the Ka'het case remains an example rather than a standing rule;
4. refusal — the player declines to author Remnant research practice.

Each positive route schedules a later one-shot reflection. The reflection demonstrates a route-specific downstream consequence without asserting new Ka'het history, current Ka'het intent, or Builder causation.

## Invariants

- `B2 Ka'het Signal Interpretation:*` is read-only.
- No A1 `world:*` state is introduced or written.
- All new persistence is confined to `A2 Ka'het Evidence Practice:*`.
- Interpreter and Scout remain player-private shorthand rather than formal offices.
- The player receives no Ka'het title, Remnant office, credential, endorsement, or representative authority.
- Historical translated traffic remains distinct from current field evidence.
- No unrelated gameplay semantics, economy, reputation, combat, or simulation state is changed.

## Persistence

This is data-only condition/event persistence using existing Endless Sky mechanisms; no save schema change or migration is introduced. Existing saves that lack these A2 conditions remain at their default unset state.

## Validation contract

Focused validator: `tools/story/validate_a2_kahet_evidence_practice.py`.

It checks:

- exactly two A2 missions;
- resolved B2 aftermath gating;
- recognition of the B2 contradiction-register settlement;
- all three positive routes plus refusal;
- scheduled later reflection and reflection persistence;
- zero B2/world-state writes;
- explicit private-shorthand / non-authority boundary.

At handoff-authoring time, repository-native CI and stock save-load/build validation had not yet been observed on the exact final candidate head. Do not claim those gates until their exact-head workflow results are terminal green.

## Remaining acceptance work

Before A3 integration, confirm exact-head `Fork simulation and story validation` and `Fork save-load integration smoke` are successful. Then exercise in the actual game: B2-aftermath gating, all four initial choices, all three positive later reflections, refusal suppression, save/reload between offer and reflection, one-shot suppression, and Remnant/Ka'het offer-precedence regression.

## A3 integration instructions

Do not self-integrate. Re-read the then-current authoritative `main`, verify no overlapping Ka'het A2 slice has landed, and integrate only this exact branch head after required gates are green. Preserve B2 ownership and the translated-history versus present-field-evidence distinction.
