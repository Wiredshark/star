# A2 Saryd Seed Practice Echo Restage Handoff

Verdict: READY for A3 review/integration

Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`

Branch: `agent/a2-saryd-seed-practice-echo-restage-20260822-2004`

Production commit: `fa4115202995dc09f7fdb245823e4c5b224a1f40`

Validator commit: `2303bda4eef6067189b64893504f50ff1b027c20`

Exact validated production/validator/handoff candidate: `91be43ca59e91436fa56694251bfa3e30f7f14ef`

## Implemented RPG / narrative loop

This current-main restage consumes the integrated B2 Saryd Seed Stewardship aftermath read-only. The player can choose one of four durable responses to how an earlier seed-stewardship settlement should travel:

- keep the precedent local;
- carry forward only the reasoning method and evidence discipline;
- allow the settlement to travel only as a bounded example with its crop, climate, urgency, and record-quality limitations attached;
- refuse to decide how other Saryd exchanges should reuse the precedent.

The three positive routes persist separately and each has an explicit later Reflection gate. Refusal remains persistent but does not arm Reflection.

## Files / systems changed

- `data/coalition/a2 saryd seed practice echo.txt`
- `tools/story/validate_a2_saryd_seed_practice_echo.py`
- this handoff

## Invariants

- `B2 Saryd Seed Stewardship:*` is read-only.
- No `world:*` state is written.
- All new writes are namespaced under `A2 Saryd Seed Practice Echo:*`.
- Keeper and Grower remain player-private shorthand, not Saryd names, offices, endorsements, or representative authority.
- A portable precedent does not silently erase crop, climate, urgency, access, provenance, uncertainty, or record-quality differences.
- Refusal does not become permission and does not arm the Reflection.
- Both dialogue-only missions use `offer precedence 9`.
- All five objective-less terminal paths use `decline`; no state-only `accept` remains.
- Reflection rechecks B2 aftermath and explicitly gates local, method, and bounded-example routes.

## Persistence implications

Existing saves remain compatible because all A2 conditions default absent/zero until the player encounters the new missions. No migration is required. Positive choices set `introduced` plus one route bit. Refusal sets only `declined`. Reflection sets `reflection seen` once.

## Exact validation evidence

On exact candidate `91be43ca59e91436fa56694251bfa3e30f7f14ef`:

- `Fork simulation and story validation` run `32606972138` / #437: **SUCCESS**.
- `Fork save-load integration smoke` run `32606972147` / #422: **SUCCESS**.

These are repository-native exact-head gates. No additional manual actual-game acceptance is claimed beyond those workflows.

## A3 integration instructions

Re-read current `main`, verify ancestry/mergeability, then review/integrate the exact validated candidate plus any handoff-only READY descendant. Preserve B2/world read-only ownership, explicit route gating, refusal suppression, offer precedence 9, the state-only dialogue `decline` lifecycle, and the private-shorthand/no-Saryd-authority boundary. Do not self-integrate from A2.
