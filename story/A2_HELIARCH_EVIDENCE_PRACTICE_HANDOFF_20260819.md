# A2 Heliarch Evidence Practice handoff

Verdict: PARTIAL pending exact-head CI and actual-game acceptance.

Authoritative base: `main@813b78f74737649ea2303ade3441a2d63ef3cdb9`.
Branch: `agent/a2-heliarch-evidence-practice-20260819-1407`.

## RPG loop

This A2 slice consumes the integrated B2 Heliarch Evidence Handoff only after `aftermath seen`. The player privately chooses whether to carry forward a provenance-oriented method, a falsification/re-examination challenge, or keep the lesson local. A later one-shot reflection demonstrates a distinct consequence of each persisted choice without granting Heliarch authority.

## Invariants

- B2 Heliarch state is read-only.
- No A1 `world:*` state is written or introduced.
- All new persistence is under `A2 Heliarch Evidence Practice:*`.
- Clerk and Investigator remain player-private shorthand inherited from B2, not titles.
- The player gains no Heliarch office, endorsement, credential, investigative role, or representative authority.
- Existing B2 provenance-packet versus independent-reexamination settlement remains intact.

## Files

- `data/coalition/a2 heliarch evidence practice.txt`
- `tools/story/validate_a2_heliarch_evidence_practice.py`
- `story/A2_HELIARCH_EVIDENCE_PRACTICE_HANDOFF_20260819.md`

## Validation required

Run repository-native story/simulation/style CI and save-load smoke on the exact final head. In-game acceptance should prove: no offer before B2 aftermath; all three routes persist; each later reflection is route-correct; save/reload preserves the route; no duplicate offer after `reflection seen`; Coalition offer precedence remains healthy.

## A3 integration

Integrate only after exact-head CI passes and runtime acceptance is satisfactory. Preserve B2 as sole writer of `B2 Heliarch Evidence Handoff:*`; do not reinterpret this A2 private practice as Heliarch policy.
