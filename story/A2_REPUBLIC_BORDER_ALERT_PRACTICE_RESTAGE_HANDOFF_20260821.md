# A2 Republic Border Alert Practice Restage Handoff

## Verdict

PARTIAL pending exact-head repository-native validation.

## Authority

- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-republic-border-alert-practice-restage-20260821-1204`
- Production restage: `8dd4143724eb223780107b1644b1f1874ffb03ca`
- Strengthened validator: `c9639e58d0077740055b8541b7d49b17ee0b9d36`

This is a clean current-main restage of the older `agent/a2-republic-border-alert-practice-20260820-0810` candidate. The historical branch remains untouched.

## RPG / narrative loop

At authoritative A1 `world: republic border pressure >= 4`, Republic transit coordinator Mara Vey asks the player to choose one of four operating policies:

- ship-specific factual basis must remain distinct from the general alert;
- documented civilian, medical, relief, and passenger continuity must retain visible capacity;
- temporary restrictions must carry explicit review points;
- refusal to establish a standing doctrine from one alert cycle.

Once A1 border pressure later recovers to `<= 2`, a one-shot recovery review produces a route-specific consequence. The review explicitly does not claim that the player's policy caused the simulation to recover.

## Invariants

- A1 remains sole writer of `world: republic border pressure`.
- All A2 writes remain `A2 Republic Border Alert Practice:*`.
- Arrival from Pirate-controlled space may justify a general alert but is not evidence of individual wrongdoing.
- Refusal remains refusal and is not converted into consent.
- The slice creates no Republic office, enforcement authority, or representative role for the player.
- Both missions are state-only dialogue. All five terminal paths persist state and use `decline`; none may use objective-less `accept`.
- Both missions use `offer precedence 8`.

## Files

- `data/human/a2 republic border alert practice.txt`
- `tools/story/validate_a2_republic_border_alert_practice.py`
- `story/A2_REPUBLIC_BORDER_ALERT_PRACTICE_RESTAGE_HANDOFF_20260821.md`

## Validation required

Before promotion to READY:

1. exact-head `Fork simulation and story validation` must be terminal green;
2. exact-head `Fork save-load integration smoke` must be terminal green;
3. A3 should re-read current `main` and verify ancestry/mergeability before integration.

Optional exploratory actual-game acceptance can further exercise all four briefing routes, recovery gating, save/reload between stages, one-shot suppression, and Republic offer precedence.

No self-integration is authorized from A2.
