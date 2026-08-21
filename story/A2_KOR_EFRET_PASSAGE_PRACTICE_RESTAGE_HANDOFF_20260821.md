# A2 Kor Efret Passage Practice current-main restage handoff — 2026-08-21

Verdict: PARTIAL pending exact-head repository-native validation.

Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
Branch: `agent/a2-kor-efret-passage-practice-restage-20260821-1007`
Production restage: `bb3c1e37204651573aff093ea5710a48b7603986`
Strengthened validator: `8f7aacb9408417811ba4e9d55f7fd075959f07f3`

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
- Production and validator files use the repository-standard GPL header.

## Files
- `data/korath/a2 kor efret passage practice.txt`
- `tools/story/validate_a2_kor_efret_passage_practice.py`
- this handoff

## Validation required
Run the exact-head `Fork simulation and story validation` workflow and the exact-head `Fork save-load integration smoke` workflow. Promote to READY only if both are terminal green. Optional exploratory actual-game acceptance may additionally exercise all four briefing routes, all three positive reflections, refusal suppression, save/reload between stages, one-shot behavior, and Kor Efret offer precedence.

A3 owns integration. Do not self-integrate from A2.
