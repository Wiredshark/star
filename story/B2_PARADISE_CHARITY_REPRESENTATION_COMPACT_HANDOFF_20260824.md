# B2 Paradise Charity Representation Compact — Handoff

Verdict: PARTIAL pending exact-head save-load completion.

Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`

Branch: `agent/b2-paradise-charity-representation-20260824`

Production commit: `084ccdfd215586a2e77bdbfe646d3f6d46261992`

Initial focused-validator commit: `23726bad8fcdf39aece4806aa9c963b48318002f`

Validator hardening / exact current production+validator candidate: `fcecc102e3950d0245cc3399f344b4cf27a61972`

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

## Validation evidence

Initial handoff head `7f07d3f8aba3cbdef5c8536465e5d38a225a4132`:

- Fork save-load integration smoke #551 / run `32796266491`: SUCCESS.
- Fork simulation and story validation #566 / run `32796266302`: FAILED in the focused story-validator step while changed-content style passed.

The failure was validator-only: a continuity assertion required a phrase to survive source-comment line wrapping. Production semantics were unchanged. Commit `fcecc102e3950d0245cc3399f344b4cf27a61972` hardens that check to a semantic fragment while retaining all route-local, settlement-local, lifecycle, ownership, and continuity assertions.

Exact current candidate `fcecc102e3950d0245cc3399f344b4cf27a61972`:

- Fork simulation and story validation #567 / run `32798115269`: SUCCESS.
- Fork save-load integration smoke #552 / run `32798115261`: IN PROGRESS at handoff update time.

Do not promote to READY until exact candidate `fcecc102e3950d0245cc3399f344b4cf27a61972` has terminal-green save-load integration evidence. Do not self-integrate. A3 retains integration authority and must re-read current `main`, ancestry, mergeability, and concurrent B1/A2/B2 work before integration.
