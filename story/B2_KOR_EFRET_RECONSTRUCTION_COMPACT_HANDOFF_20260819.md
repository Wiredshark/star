# B2 Kor Efret Reconstruction Compact — Handoff — 2026-08-19

## Status

PARTIAL pending repository-native validation.

## Branch and ancestry

- Repository: `Wiredshark/star`
- Authoritative `main` observed at run start: `af9efc35faa7ccccc48dcd3e9b2a2811c083e94a`
- B1 parent branch: `agent/b1-kor-efret-reconstruction-institutions-20260819-0716`
- B1 parent SHA: `680b873a83e4d23baa94b7a2488c147c247fadf6`
- B2 branch: `agent/b2-kor-efret-reconstruction-compact-20260819-0723`
- Production commit: `6b9a8455e2b29342fc07ab7a740a5376d36c32ed`
- Focused validator commit: `7defe38c71bfa97d5ae7f0ea1b20add92f494634`

## Implemented slice

Adds a persistent Kor Efret reconstruction dispute between two recurring workers whom the player privately thinks of as the **Recorder** and the **Repairer**. Those are player-facing shorthands only; the content explicitly does not establish Korath names, titles, or offices.

The initial encounter turns B1's reconstruction institutions into a character conflict over a functioning air recycler removed from a sealed district. The player can prioritize complete provenance, immediate repair, a paired transfer record, or refuse to judge.

The later Review remembers the initial route and asks how repeated salvage transfers should avoid turning reconstruction into invisible abandonment. It resolves into one of two persistent policies:

1. **Transferable provenance bond** — component provenance follows the part while the donor district retains an explicit replacement/closure obligation.
2. **Restoration-priority ledger** — transfers depend on documented habitability, ecological recovery, remaining systems, and realistic replacement prospects.

`Recorder Remembers` is a later one-shot reader of either settlement.

## B1 dependencies and continuity

Consumes the B1 parent branch's four reconstruction-history concepts:

- salvage provenance ledger;
- sealed habitat register;
- restoration obligation ledger;
- ecological recovery archive.

The B2 slice does not write B1 state and does not invent a new Kor Efret bureaucracy. Its central continuity invariant is that scarce salvage can move to urgent repairs **without erasing either component provenance or the unfinished obligation of the donor site**.

## Files

- `data/korath/b2 kor efret reconstruction compact.txt`
- `tools/story/validate_b2_kor_efret_reconstruction_compact.py`
- `story/B2_KOR_EFRET_RECONSTRUCTION_COMPACT_HANDOFF_20260819.md`

## State ownership

All persistent writes are namespaced under:

`B2 Kor Efret Reconstruction Compact:*`

No direct writes to `world:*`, credits, reputation, cargo, outfits, ships, fleets, or combat state are allowed by the focused validator.

## Required validation

Focused validator:

```bash
python3 tools/story/validate_b2_kor_efret_reconstruction_compact.py "data/korath/b2 kor efret reconstruction compact.txt"
```

Repository story validation and changed-content style should also pass, followed by the normal Endless Sky production build/save-load smoke used by recent READY B2 slices.

At the time this handoff was first written, those repository-native gates had not yet returned a terminal result, so the verdict remains PARTIAL until exact-head evidence is available.

## A3 / B3 integration notes

- Integrate the B1 Kor Efret reconstruction-history parent first.
- Then review/integrate this B2 branch.
- Preserve the explicit non-title status of `Recorder` and `Repairer`.
- Preserve B2-only state ownership.
- The two terminal settlements should remain mutually exclusive.
- Do not collapse component provenance into site-restoration status; they are intentionally separate records linked by the compact.

## Verdict

**PARTIAL** pending focused validator, repository story/style validation, production build, and save/load smoke evidence.
