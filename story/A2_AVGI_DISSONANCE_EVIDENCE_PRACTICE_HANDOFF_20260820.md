# A2 Avgi Dissonance Evidence Practice handoff — 2026-08-20

## Authority and base

- Repository: `Wiredshark/star`
- Authoritative integration branch at selection: `main`
- Authoritative base SHA: `a44dc035658d928e4becf0398ab9ce41e0c39e0a`
- Candidate branch: `agent/a2-avgi-dissonance-evidence-practice-20260820-0504`
- Production commit: `f0ae7841378dea35d5220f5626f3c37b8d1e4d25`
- Validator commit: `018216073900090ae4fdfd49438855224c567d2a`

## RPG / narrative loop

Consumes the newly integrated B1 Avgi Dissonance institutional-history material as context. The player chooses a private evidence-handling practice: preserve the full record including adverse evidence; separate documented burden from later claims about blame/motive/reform; keep the lesson local; or refuse a standing practice. A later one-shot reflection demonstrates the consequence of each route.

## Invariants

- No A1 `world:*` state is read or written.
- B1 institutional-history content remains observational and read-only.
- All persistent writes are confined to `A2 Avgi Dissonance Evidence Practice:*`.
- Dissonance political plurality is preserved; no archive is treated as speaking for all Dissonance communities.
- Evidence is kept distinct from inference, motive, blame, and proposed reform.
- The player receives no Avgi or Dissonance office, endorsement, credential, or representative authority.
- Refusal remains a real boundary and is not converted into consent.

## Files

- `data/avgi/a2 avgi dissonance evidence practice.txt`
- `tools/story/validate_a2_avgi_dissonance_evidence_practice.py`
- `story/A2_AVGI_DISSONANCE_EVIDENCE_PRACTICE_HANDOFF_20260820.md`

## Validation

Focused validator is committed but execution is not claimed until repository-native CI or a correct `Wiredshark/star` execution host reports it. Required remaining gates: focused validator; changed-content style; story/simulation suite; production build/save-load smoke; actual-game offer gating and all four reflection routes; save/reload between decision and reflection; one-shot suppression; Avgi offer-precedence regression.

## A3 integration

Do not integrate until the exact candidate head passes repository-native validation and player-visible acceptance. If accepted, integrate the candidate as a read-only downstream practice layer; do not transfer A1/B1 authority into A2.

## Verdict

PARTIAL — isolated production candidate with validator and durable handoff; exact-head CI/runtime acceptance still required.
