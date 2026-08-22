# A2 Ka'het Evidence Practice current-main restage handoff

Verdict: PARTIAL pending exact-head repository validation.

Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`

Branch: `agent/a2-kahet-evidence-practice-restage-20260822-1004`

Production restage: `b8d838ff021140feda1ed3300abaec2480734023`

Strengthened validator: `3a33a1fde9f6ce1fcd8570d9996ac072e56fd176`

This restages historical PARTIAL PR #114 from current authoritative `main` without modifying or rebasing the historical branch.

## RPG / narrative loop

After integrated `B2 Ka'het Signal Interpretation: aftermath seen`, the Interpreter and Scout ask what evidence-handling practice should travel beyond the original dispute. The player may choose bounded-hypothesis discipline, contradiction-preserving discipline, local-only reuse, or explicit refusal. Each positive route schedules a later one-shot reflection; refusal does not.

The reflection explicitly gates all three positive routes. It demonstrates how the chosen practice affects a later Remnant evidence packet while keeping ancient translated traffic distinct from present field evidence.

## Invariants

- B2 Ka'het Signal Interpretation state is read-only.
- No `world:*` state is written.
- All persistent writes are `A2 Ka'het Evidence Practice:*`.
- Both state-only missions use `offer precedence 9`.
- All five objective-less terminal paths use `decline`; there is no state-only `accept`.
- The Reflection rechecks B2 aftermath and explicitly gates bounded-hypothesis, contradiction-preserved, and local-only routes.
- Refusal does not schedule or arm the later Reflection.
- Interpreter and Scout remain player-private shorthand, not Remnant offices or Ka'het titles.
- No Ka'het or Remnant representative authority is created.
- Historical condition names and route meanings are preserved for save compatibility.

## Files

- `data/kahet/a2 kahet evidence practice.txt`
- `tools/story/validate_a2_kahet_evidence_practice.py`
- `story/A2_KAHET_EVIDENCE_PRACTICE_RESTAGE_HANDOFF_20260822.md`

## Validation status

Exact-head repository workflows have not yet been observed on the completed candidate. Do not claim simulation/story/style, production build, save-load, or runtime success until the exact-head runs are terminal green.

## A3 boundary

Re-read current `main`, verify ancestry and mergeability, and preserve B2/world read-only ownership, explicit route gating, refusal suppression, offer precedence 9, and state-only dialogue `decline` lifecycle. Do not reinterpret evidence practice as permission to speak for the Ka'het or the Remnant.
