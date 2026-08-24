# B2 Avgi Inherited Concession Boundaries — Handoff

## Authority
- Repository: `Wiredshark/star`
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-avgi-inherited-concession-boundaries-20260824`
- Production syntax-fix commit: `428c6e129cd1ca7213bc60aaf4dc6738dc6a1e28`
- Focused validator commit / current candidate: `4d210350cc864f0bbdc8824b230b3d5eae59009d`
- Verdict: PARTIAL pending repository-native validation

## Character / dynamic-content behavior
Adds a recurring Avgi parent/adult-child dispute around an inherited mineral concession. The player privately thinks of the two characters as the Holder and the Heir; those labels are not Avgi offices.

The initial Offer supports three persistent approaches plus refusal:
1. succession requires fresh consent to administrative office;
2. benefits may be retained only if continuing concession obligations are explicitly assigned to a consenting party;
3. paired records keep inherited economic interest separate from present administrative authority;
4. refusal establishes no general rule and does not schedule Review.

Each substantive route schedules a Review after 7–11 days. Review resolves into exactly two persistent settlements:
- portable succession charter;
- renunciation and reassignment.

`Heir Remembers` is the one-shot aftermath reader.

## Dependencies / canon
- Requires `language: Avgi (Written)`.
- Excludes `avgi: lost in twilight`.
- Consumes the established Avgi Mineral Tenure Archive canon: inherited concessions can include extraction rights, tax privileges, maintenance obligations, and administrative offices.
- The slice does not claim that one family's settlement is universal Consonance inheritance law.
- Holder / Heir are player-private shorthand rather than canonical offices.

## Ownership / persistence
- All persistent writes are `B2 Avgi Inherited Concession Boundaries:*`.
- `avgi:*`, `world:*`, B1, A1, and A2 state are read-only.
- No credits, reputation, cargo, equipment, ship, fleet, or combat mutations.
- All 7 state-only terminal paths use `decline`; no objective-less mission is accepted.

## Files
- `data/avgi/b2 avgi inherited concession boundaries.txt`
- `tools/story/validate_b2_avgi_inherited_concession_boundaries.py`
- `story/B2_AVGI_INHERITED_CONCESSION_BOUNDARIES_HANDOFF_20260824.md`

## Validation required before READY
- focused validator discovery and pass;
- focused Python compilation;
- repository simulation/story/state-ownership contracts;
- changed-content style;
- production configure/build;
- stock save-load integration smoke;
- final exact-SHA diff/status review.

## Integration notes
A3 must re-read current `main` and active B2 work before integration and must not self-integrate from this branch. Preserve the distinction among family lineage, inherited economic interest, retained benefits, continuing obligations, personal consent, current administrative authority, delegated duties, and explicit closure.
