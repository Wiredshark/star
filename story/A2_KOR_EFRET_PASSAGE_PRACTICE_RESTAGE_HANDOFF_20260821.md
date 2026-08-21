# A2 Kor Efret Passage Practice current-main restage handoff — 2026-08-21

Verdict: READY for A3 review/integration.

Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
Branch: `agent/a2-kor-efret-passage-practice-restage-20260821-1007`
Production restage: `bb3c1e37204651573aff093ea5710a48b7603986`
Strengthened validator: `8f7aacb9408417811ba4e9d55f7fd075959f07f3`
Canonical content-header repair: `3e8b9d82824cc3a5fc952b6894aefbcf92fcf043`

## Why this restage exists
The historical PR #179 candidate was based on an older integration head and used `accept` at state-only dialogue terminals. Current A2 lifecycle policy requires objective-less state-only conversations to record state and terminate with `decline`. This branch restages the same player-facing Kor Efret passage-practice loop directly from current authoritative main and leaves the historical branch untouched.

## RPG / narrative loop
Consumes integrated `B2 Kor Efret Passage Continuity Compact: aftermath seen` read-only. The player chooses consent/current-preference discipline, separate closure for safety/contact/settlement, local-only reuse, or refusal. A later one-shot reflection demonstrates a distinct consequence of each positive practice.

## Repairs / invariants
- B2 state is read-only; no B2 writes.
- No `world:*` reads or writes.
- All persistence is under `A2 Kor Efret Passage Practice:*`.
- Physical safety, family contact, onward passage, current consent, and voluntary settlement remain distinct.
- Historical destination/reunion goals do not become permanent commands.
- Refusal is not consent and does not arm reflection.
- Tracker/Passage Keeper remain player-private shorthand; no Kor Efreti title, office, endorsement, or representative authority is granted.
- Both state-only missions use `offer precedence 9`.
- All four Briefing terminals and the Reflection terminal end with `decline`; no objective-less mission is accepted.
- Production and validator files use the repository-standard GPL header convention.

## Files
- `data/korath/a2 kor efret passage practice.txt`
- `tools/story/validate_a2_kor_efret_passage_practice.py`
- this handoff

## Exact-head validation
On candidate `3e8b9d82824cc3a5fc952b6894aefbcf92fcf043`:
- `Fork simulation and story validation` run `32490982794` / #331: SUCCESS.
- Focused simulation/story contracts: SUCCESS, including the strengthened Kor Efret validator.
- Changed fork content style: SUCCESS after correcting the exact canonical GPL-header boundary required by `utils/contentStyle.json`.
- A1 simulation contract tests: SUCCESS.
- `Fork save-load integration smoke` run `32490982807` / #316: SUCCESS.
- Production configure: SUCCESS.
- Production build: SUCCESS.
- Stock save-load smoke cases: SUCCESS.

The two earlier style-red heads (`0ea406878b2c961d1866e14fb0c39380669a2980` and `c4d58b6609c0ea89a30812f80d07dafe42ed74d2`) must not be used for integration. Their precise failures were diagnosed from Actions job logs; the final repair required a literal empty line after the GPL notice rather than an extra comment separator.

## A3 integration instructions
Re-read current `main`, verify ancestry/mergeability, and review only the exact final restage head after this handoff commit and its refreshed exact-head workflows are green. Preserve B2 read-only ownership, the state-only dialogue `decline` lifecycle invariant, explicit offer precedence, refusal semantics, and the distinctions among safety, family contact, onward passage, consent, and voluntary settlement. No self-integration is authorized from A2.

Optional exploratory actual-game acceptance may still exercise all four briefing routes, all three positive reflections, refusal suppression, save/reload between stages, one-shot behavior, and Kor Efret offer precedence, but no repository-native gate remains red on the validated production/validator candidate.
