# A2 Avgi Dissonance Evidence Practice current-main restage handoff — 2026-08-22

## Authority

- Repository: `Wiredshark/star`
- Authoritative integration branch: `main`
- Authoritative base SHA: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-avgi-dissonance-evidence-practice-restage-20260822-1805`
- Production restage: `bd831bd299bfde403a9558cf5819070184b193c2`
- Strengthened validator: `dffac95da76c4b12ae19216502f0630ac524640c`

Historical PARTIAL PR #159 remains untouched.

## RPG / narrative loop

The player revisits Dissonance archival practice and chooses one of four persistent responses: preserve the complete record including adverse corrections; separate documented burden from later arguments about blame, motive, or reform; keep the lesson local/context-bound; or refuse a standing practice. The three positive routes arm a later one-shot reflection with an explicit route gate. Refusal remains persistent but does not arm Reflection.

## Current architecture / invariants

- No A1 `world:*` state is read or written.
- Dissonance archival/B1 context is observational and read-only.
- All persistent writes are confined to `A2 Avgi Dissonance Evidence Practice:*`.
- Political plurality is preserved; no archive is treated as speaking for every Dissonance community.
- Documented burden remains distinct from inference about motive, blame, or the correct reform.
- Both state-only missions use `offer precedence 9`.
- All five objective-less terminal paths use `decline`; no state-only `accept` remains.
- Reflection explicitly gates all three positive routes; refusal is excluded from Reflection.
- No Avgi/Dissonance office, endorsement, credential, or representative authority is created.
- Existing route names from historical PR #159 are preserved for save-compatible absent-condition defaults and continuity.

## Files

- `data/avgi/a2 avgi dissonance evidence practice.txt`
- `tools/story/validate_a2_avgi_dissonance_evidence_practice.py`
- `story/A2_AVGI_DISSONANCE_EVIDENCE_PRACTICE_RESTAGE_HANDOFF_20260822.md`

## Validation status

Repository-native exact-head workflows must be terminal green before A3 integration. The focused validator is committed and is discoverable by the repository story-validation workflow. No manual actual-game acceptance is claimed unless separately recorded.

## A3 boundary

Re-read current `main`, verify ancestry/mergeability, preserve no-world-state ownership, explicit route gating, refusal suppression, offer precedence 9, state-only `decline` lifecycle, and the no-representative-authority boundary. A2 must not self-integrate.

## Verdict

PARTIAL pending exact-head repository-native simulation/story/style and production build/save-load validation.
