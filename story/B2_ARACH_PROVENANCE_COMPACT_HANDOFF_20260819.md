# B2 Arach Provenance Compact handoff — 2026-08-19

## Status

PARTIAL pending repository-native validation.

## Base and branch

- Repository: `Wiredshark/star`
- B1 dependency branch: `agent/b1-arach-civic-institutions-20260819-1124`
- Exact B1 parent SHA: `46f723bf88acb6fdb210e15e79131148abc84bf6`
- B2 branch: `agent/b2-arach-obligation-ledger-20260819-1328`
- Production commit: `6d7ecedf0786b8746e807b824b62210a4ab308e5`
- Focused-validator commit: `80d7bfadd202b067a11884c379e3ef5a59211819`

## Slice

B2 converts the B1 Arach Mining Provenance Register, Freight Contract Ledger, and Courier Relay Register into a persistent player-facing dispute about what evidence should survive repeated cargo handoffs.

Two recurring Arach are deliberately identified only by player-private shorthand:

- `Assayer` — emphasizes mine maps, samples, assays, and historical provenance.
- `Carrier` — emphasizes transfer seals, observed condition, custody windows, and bounded responsibility.

These are not canonical Arach names, titles, offices, or political institutions.

The initial encounter offers three persistent routes plus refusal:

1. portable provenance;
2. bounded freight custody;
3. paired provenance/custody histories;
4. refusal.

The delayed Review exposes information-loss during downstream copying and resolves into one of two persistent settlements:

- `settlement provenance packet` — source, direct observation, uncertainty, transformation/condensation, and full-record link travel with copied summaries;
- `settlement portable dispute ledger` — provenance and custody remain separate, while unresolved contradictions must travel downstream until formally closed.

`Assayer Remembers` is the one-shot later reader.

## Ownership and invariants

- Every persistent write is under `B2 Arach Provenance Compact:*`.
- B2 does not mutate B1 state, A1 `world:*` state, A2 state, credits, reputation, cargo, outfits, ships, fleets, or combat rating.
- Mine provenance is evidence of origin/history, not automatic proof of where loss or misconduct occurred.
- Freight custody records describe bounded observations/responsibility during each leg; they do not erase upstream provenance.
- A shortened/copy-derived record must not silently harden an inference into a direct observation.
- Practical shared record conventions do not imply centralized Arach political authority.

## Files

- `data/coalition/b2 arach provenance compact.txt`
- `tools/story/validate_b2_arach_provenance_compact.py`
- `story/B2_ARACH_PROVENANCE_COMPACT_HANDOFF_20260819.md`

## Required validation

Run before promotion to READY:

```bash
python3 tools/story/validate_b2_arach_provenance_compact.py
python3 tools/story/validate_story_repo.py
python3 utils/check_content_style.py
```

Also require the repository's normal fork simulation/story workflow and production build/save-load smoke on the exact final B2 head.

Runtime acceptance should exercise all three initial routes, refusal, delayed Review availability, both mutually exclusive settlements, persistence across save/load, and one-shot aftermath behavior.

## A3 integration guidance

Integrate the B1 Arach civic-institutions dependency first, then this B2 slice. Do not integrate while this handoff remains PARTIAL. If CI/content/runtime validation exposes only validator defects, repair the validator without weakening the production invariants. If production syntax/state ownership fails, repair production content and rerun exact-head validation.
