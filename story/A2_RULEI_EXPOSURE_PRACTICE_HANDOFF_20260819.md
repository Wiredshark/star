# A2 Rulei Exposure Practice Handoff — 2026-08-19

## Verdict

PARTIAL pending exact-head repository-native validation and actual-game acceptance.

## Authority and base

- Repository: `Wiredshark/star`
- Authoritative base: `main@a4ba72896870d0b764272ef95d012b661b677c06`
- Base integrates B2 Rulei Exposure Accountability after its A3 acceptance.
- Isolated branch: `agent/a2-rulei-exposure-practice-20260819-1602`
- No `a2-rulei` branch existed at selection time.

## Implemented A2 loop

The slice consumes the resolved B2 Rulei exposure-accountability aftermath and asks what procedural lesson, if any, the player carries forward. Four persistent routes are available: bounded-warning practice, consent-and-purpose practice, local-only treatment, and explicit refusal. A later one-shot reflection demonstrates a distinct consequence for each route.

The feedback loop is deliberately downstream of the B2 settlement: resolved exposure-accountability state -> player-selected A2 practice -> later history-aware administrative consequence.

## Invariants

- B2 Rulei state is read-only.
- No `world:*` state is introduced or written.
- All writes are namespaced `A2 Rulei Exposure Practice:*`.
- Observed symptoms, testimony, interpretation, current fitness, causation, and motive remain distinct.
- The slice does not establish that Rulei contact caused lasting injury or that the Rulei intended harm.
- The player gains no medical office, Rulei authority, credential, endorsement, or representative status.
- Refusal persists as refusal and is not converted into an implicit policy.

## Files

- `data/rulei/a2 rulei exposure practice.txt`
- `tools/story/validate_a2_rulei_exposure_practice.py`
- `story/A2_RULEI_EXPOSURE_PRACTICE_HANDOFF_20260819.md`

## Validation required

Run the focused validator, repository-wide focused story validators, A1 ownership/simulation contracts, changed-content style gate, production build/save-load smoke, and actual-game offer/reflection paths. Verify save/reload between the two missions and duplicate-offer suppression.

## A3 integration instructions

Integrate only after exact-head repository-native workflows are terminal green. Preserve B2/world read-only ownership and the observation-versus-causation boundary. Do not resolve conflicts by broadening the player's authority or turning the Rulei case into universal medical doctrine.
