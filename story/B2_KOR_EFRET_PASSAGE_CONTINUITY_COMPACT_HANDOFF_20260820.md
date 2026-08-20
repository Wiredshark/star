# B2 Kor Efret Passage Continuity Compact Handoff

## Stage

B2 STORY CHARACTERS + DYNAMIC CONTENT

## Verdict

READY for A3 review/integration.

## Repository authority

- Authoritative `main` observed at slice selection and final pre-handoff recheck: `2f497a46d4787d6081bd4a59c6d7800a3d06c8f2`.
- Required B1 parent: `0bba94eea1dfe9daa7588e23ece87ec527aa575e` (`B1: Kor Efret resettlement institutional history`).
- B1 dependency repository-native validation: simulation/story #225 / `32379693666` SUCCESS; save-load #214 / `32379693797` SUCCESS.
- Isolated branch: `agent/b2-kor-efret-resettlement-compact-20260820-1027`.
- Production commit: `0b91871af14a5065c9408d22f3e9ae7ad6afd377`.
- Initial focused-validator commit: `62c5a14570ab393b69c1376e0c737275fd14590b`.
- Validator case-sensitivity repair: `a4622393a01c1f51354b8814561d39304ef5b26f`.
- Exact fully validated production/validator candidate: `5f9db581605db8f12e5f51d1c98238d8e1d32c32`.

## Scope

Adds one focused three-mission Kor Efret character/dynamic-content arc:

- `data/korath/b2 kor efret passage continuity compact.txt`
- `tools/story/validate_b2_kor_efret_passage_continuity_compact.py`

Two recurring Kor Efreti are identified only through player-private shorthand:

- the **Tracker**, who follows family continuity and contact;
- the **Passage Keeper**, who matches people to actual available transport and shared contributions.

Those are not presented as Korath names, titles, formal offices, or evidence of centralized refugee administration.

### Initial dispute

A displaced person can leave a damaged settlement immediately, but the available passage does not reach the relative or destination they originally sought. The player can choose:

1. **reunion-first** — preserve the family/contact obligation even if a safe berth exists elsewhere;
2. **passage-first with continuity** — use the available safe passage, but preserve unresolved family contact/onward travel explicitly;
3. **paired state** — track safe location, family contact, and current destination preference separately;
4. refusal — do not convert one family's circumstances into a standing rule.

### Review

The later Review addresses copied-record degradation: downstream records can preserve where someone arrived while dropping whether arrival was temporary, whether family contact was restored, whether onward passage remains needed, whether location may be shared, or whether the traveler changed their preferred outcome.

The Review resolves into exactly one of two persistent settlements:

- **portable family-contact packet** — current safe location, consent to share it, relatives/households sought, contact status, current destination preference, and unfinished passage need travel together;
- **two-stage settlement ledger** — physical safety and voluntary reunion/resettlement remain distinct closure conditions and neither silently closes the other.

`Tracker Remembers` is the later one-shot reader.

## B1 dependency and non-overlap

This slice consumes the B1 Kor Efret resettlement institutions:

- Family Reunification Register;
- Passage Contribution Ledger;
- Translation Mediation Archive;
- Return and Resettlement Ledger.

The production Offer explicitly requires both the B1 Family Reunification Register and Passage Contribution Ledger to have been offered.

This is deliberately distinct from the already integrated `B2 Kor Efret Reconstruction Compact`, which covers salvage provenance, donor-site restoration obligations, sealed habitats, and ecological recovery. This new slice concerns people/households, voluntary destination preference, family contact, shared passage, and the distinction between physical safety and social recovery.

## State ownership / canon invariants

- All new persistent writes are namespaced `B2 Kor Efret Passage Continuity Compact:*`.
- No `world:*`, credits, reputation, cargo, outfit, ship, fleet, combat, B1-history, or campaign-state mutation.
- Physical safety, family contact, onward passage, and voluntary settlement are related but non-equivalent states.
- A person's earlier destination or reunion goal is not a permanent command; current consent/preference may change.
- Family continuity records are not a mandatory repatriation system.
- Low-fare/shared passage does not imply a centralized subsidy or a universal Kor Efret transport authority.
- The slice introduces no mandatory return policy, named founder, hard chronology, or universal translation claim.

## Validation and repair history

The focused validator checks:

- exact three-mission graph;
- Tracker/Passage Keeper private-shorthand continuity;
- B1 family-reunification and passage-history gates;
- three substantive routes plus refusal;
- exactly two terminal settlements;
- one-shot aftermath reader;
- B2-only write ownership;
- no direct material/reputation/world-state mutation;
- local `goto`/`label` integrity;
- preservation of safety/contact/preference/resettlement distinctions;
- explicit voluntary-resettlement safeguards.

The first two simulation/story attempts exposed validator-only wording brittleness, not production-content/style failures. The final validator was aligned to the actual production semantic invariant rather than requiring the stronger literal phrase `physically safe`.

On exact candidate `5f9db581605db8f12e5f51d1c98238d8e1d32c32`:

- `Fork simulation and story validation` #228 / `32380890906`: **SUCCESS**.
- Changed-content style: **SUCCESS**.
- Focused story validators, including `validate_b2_kor_efret_passage_continuity_compact.py`: **SUCCESS**.
- Fork story/state-ownership contracts: **SUCCESS**.
- A1 simulation contract tests: **SUCCESS**.
- `Fork save-load integration smoke` #217 / `32380890866`: **SUCCESS**.
- Production configure/build: **SUCCESS**.
- Stock save-load smoke: **SUCCESS**.

## Isolation evidence

Exact B1-parent-to-validated-candidate comparison:

- 5 commits ahead / 0 behind;
- exactly 3 changed files;
- `data/korath/b2 kor efret passage continuity compact.txt`: added;
- `tools/story/validate_b2_kor_efret_passage_continuity_compact.py`: added;
- `story/B2_KOR_EFRET_PASSAGE_CONTINUITY_COMPACT_HANDOFF_20260820.md`: added.

The extra commits beyond the three files are validator/handoff repair commits; production scope did not expand.

## A2 / B3 / A3 consumption notes

- **A2** may consume the difference between safety, contact, destination preference, reunion, and voluntary resettlement for later player practice/consequence content.
- **B3** should reject continuity that treats arrival as automatic settlement, family tracing as compulsory return, or old destination preference as permanent consent.
- **A3** should integrate/accept the B1 Kor Efret resettlement-history dependency first, then this B2 slice after re-reading current `main` and confirming ancestry/continuity remain clean.

## Host/process boundary

The exposed private Fallout execution connector returned a transient HTTP 502 when its service process inventory was queried. No process was killed, cancelled, or modified. No host-side Endless Sky runtime result is claimed from that unrelated service.
