# B2 Kor Efret Passage Continuity Compact Handoff

## Stage

B2 STORY CHARACTERS + DYNAMIC CONTENT

## Current verdict

PARTIAL pending exact-head repository-native simulation/story/style and production save-load/build validation.

## Repository authority

- Authoritative `main` observed at slice selection: `2f497a46d4787d6081bd4a59c6d7800a3d06c8f2`.
- Required B1 parent: `0bba94eea1dfe9daa7588e23ece87ec527aa575e` (`B1: Kor Efret resettlement institutional history`).
- Isolated branch: `agent/b2-kor-efret-resettlement-compact-20260820-1027`.
- Production commit: `0b91871af14a5065c9408d22f3e9ae7ad6afd377`.
- Focused-validator commit: `62c5a14570ab393b69c1376e0c737275fd14590b`.

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

This slice consumes the new B1 Kor Efret resettlement institutions:

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

## Validation implemented

Focused validator checks:

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

## Remaining acceptance gates

Before promotion to READY or A3 integration, require exact-head:

1. `Fork simulation and story validation` SUCCESS, including changed-content style, focused validator discovery/execution, and state-ownership contracts.
2. `Fork save-load integration smoke` SUCCESS, including production configure/build and stock save/load smoke.
3. Recheck current `main` and B1 dependency ancestry/conflict state immediately before integration.

## A2 / B3 / A3 consumption notes

- **A2** may consume the difference between safety, contact, destination preference, reunion, and voluntary resettlement for later player practice/consequence content.
- **B3** should reject continuity that treats arrival as automatic settlement, family tracing as compulsory return, or old destination preference as permanent consent.
- **A3** should integrate/accept the B1 Kor Efret resettlement-history dependency first, then this B2 slice only if exact-head validation is green and current-main reconciliation remains clean.

## Host/process boundary

The exposed private Fallout execution connector returned a transient HTTP 502 when its service process inventory was queried. No process was killed, cancelled, or modified. No host-side Endless Sky runtime result is claimed from that unrelated service.
