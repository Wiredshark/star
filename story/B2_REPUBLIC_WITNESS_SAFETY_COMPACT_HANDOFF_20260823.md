# B2 Republic Witness Safety Compact handoff — 2026-08-23

Verdict: READY for A3 review/integration.

## Authority
- repository: `Wiredshark/star`
- authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- branch: `agent/b2-republic-witness-safety-compact-20260823`
- production commit: `af476f73dbe0ebf7d9a1ac11ce8c472cdf117dde`
- focused-validator commit: `3791edcd81da848e8d57df50652e8ab6cc13a993`
- exact fully validated production/validator/handoff candidate: `c8e328b750d61b6f8d7175fe87c4302e0169704a`

## Character / dynamic-content scope
This is a sequel to the integrated `B2 Republic Border Testimony Compact` rather than another evidence-provenance duplicate.

Returning characters:
- Talia Rook, Republic border-records officer;
- Jace Verran, independent courier and recurring civilian witness.

The prior arc solved how source lineage and copied testimony should count. This slice addresses what happens when evidentiary provenance correctly preserves a witness reference but downstream copies also expose current berth, route, family/emergency contact, or other personal data.

Initial substantive routes:
1. identity escrow with a stable witness reference;
2. purpose-bounded access with recorded audience and expiry;
3. paired testimony-provenance and current-safety/contact records;
4. refusal, which records refusal and does not arm the Review.

Every substantive route schedules `B2 Republic Witness Safety Compact: Review Ready` after 7–11 days. Review waits for authoritative A1 border pressure to ease and resolves into either:
- portable access packet; or
- expiry plus fresh cause.

`Verran Remembers` is the later one-shot consequence reader.

## Dependencies / state ownership
Read-only inputs:
- `B2 Republic Border Testimony Compact: aftermath seen`;
- A1-owned `world: republic border pressure`.

All direct writes are namespaced under `B2 Republic Witness Safety Compact:*`.

No `world:*`, prior-B2, A1/A2/B1, credits, reputation, cargo, outfit, ship, fleet, or combat mutation is introduced.

## Lifecycle
All seven dialogue/state-only terminal paths use `decline`. The slice creates no gameplay objective and therefore does not introduce an objective-less accepted mission.

## Continuity / canon assumptions
- Provenance and privacy are separate requirements: a statement may need an auditable source without publishing the witness's current location or personal contacts to every reader.
- A stable witness reference can support authorship review without granting routine readers access to direct identity/contact fields.
- A protection restriction is a safety control, not evidence of guilt or unreliability.
- Historical protection status is not fresh danger, fresh suspicion, or fresh evidence.
- Exceptional access must retain purpose, audience, expiry/review, custodian, and closure state.
- This is bounded Republic records practice, not a universal witness-protection law or new centralized authority.

## Files
- `data/human/b2 republic witness safety compact.txt`
- `tools/story/validate_b2_republic_witness_safety_compact.py`
- `story/B2_REPUBLIC_WITNESS_SAFETY_COMPACT_HANDOFF_20260823.md`

## Exact validation evidence
On exact candidate `c8e328b750d61b6f8d7175fe87c4302e0169704a`:
- `Fork simulation and story validation` #507 / run `32679841782`: SUCCESS;
- focused story validators, including `validate_b2_republic_witness_safety_compact.py`: SUCCESS;
- A1 simulation/state-ownership contracts: SUCCESS;
- changed-content style: SUCCESS;
- `Fork save-load integration smoke` #492 / run `32679841776`: SUCCESS;
- production configure/build: SUCCESS;
- stock save-load integration smoke: SUCCESS.

Exact base-to-candidate comparison: 3 commits ahead / 0 behind, exactly three added files, 405 additions, 0 deletions. PR #274 is mergeable and remains draft/unmerged for A3 authority.

## Risks / deferred work
No manual in-game narrative QA beyond repository-native build/save-load coverage is claimed. A3 should still re-read current `main`, recheck ancestry/mergeability, and assess overlap with any newly integrated Republic privacy or witness content immediately before integration.

## A3 / B3 notes
A3 retains integration authority. Re-read current `main` immediately before integration and preserve the read-only ownership of Republic border pressure and prior Border Testimony state.

B3 should preserve the distinction among source identity, stable witness reference, contact data, safety restriction, permitted audience, evidentiary weight, current risk, and explicit closure. A copied protection label must not become permanent active suspicion.
