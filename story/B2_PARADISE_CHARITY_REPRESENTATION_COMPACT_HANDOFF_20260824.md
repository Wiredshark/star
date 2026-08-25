# B2 Paradise Charity Representation Compact — Handoff

Verdict: PARTIAL pending exact-head repository-native validation.

Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`

Branch: `agent/b2-paradise-charity-representation-20260824`

Production commit: `084ccdfd215586a2e77bdbfe646d3f6d46261992`

Focused-validator commit / exact production+validator candidate before this handoff: `23726bad8fcdf39aece4806aa9c963b48318002f`

## Behavior

Adds a three-mission Paradise character arc around charity publicity and recipient representation.

- Nara Dey: Paradise charity campaign coordinator.
- Ivo Sen: teacher and former student portrayed in a successful historical storm-relief appeal.
- Offer routes: purpose-bound consent; correction rights; paired aid-evidence/publicity records; refusal.
- Positive routes schedule a Review after 7–11 days.
- Review settlements: portable representation packet; fresh-context renewal.
- `Ivo Remembers` is the one-shot aftermath reader.

## Canon / state ownership

The slice consumes the integrated Paradise Charity Circuit Archive as historical/cultural background. It preserves that charity campaigns can perform real aid while also becoming part of elite social life and recipient portrayal.

All persistent writes are under `B2 Paradise Charity Representation Compact:*`. There are no `world:*`, B1/A1/A2, credits, reputation, cargo, equipment, ship, fleet, or combat mutations.

All seven dialogue/state-only terminal paths use `decline`. Refusal does not write `introduced`, does not write a substantive route, and does not schedule Review.

The core continuity boundary is that verified aid facts, fundraising narrative, publicity consent, approved images/claims, purpose, expiry, correction, withdrawal, and present need are separate facts. Historical preservation does not create standing publicity authority, while withdrawal of current permission does not rewrite the fact that an older campaign occurred.

This is one local Paradise charity dispute and does not establish centralized Paradise charity law.

## Files

- `data/human/b2 paradise charity representation compact.txt`
- `tools/story/validate_b2_paradise_charity_representation_compact.py`
- `story/B2_PARADISE_CHARITY_REPRESENTATION_COMPACT_HANDOFF_20260824.md`

## Validation required before READY

On the exact PR head, require terminal green:

- Fork simulation and story validation, including changed-content style, focused story validators, and A1 simulation/state-ownership contracts.
- Fork save-load integration smoke, including production configuration/build and stock save-load smoke.

Do not self-integrate. A3 retains integration authority and must re-read current `main`, ancestry, mergeability, and concurrent B1/A2/B2 work before integration.
