# B2 Republic Border Testimony Compact handoff — 2026-08-20

## Stage / verdict
- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Verdict: READY for A3 review/integration
- No self-integration. A3 retains integration authority.

## Repository authority
- Repository: `Wiredshark/star`
- Authoritative integration branch: `main`
- Authoritative base SHA recovered at run start and rechecked before candidate validation: `e7606069107ebfb082555898e10caecb23e1159d`
- Isolated branch: `agent/b2-republic-border-testimony-20260820-1525`
- Production commit: `2e9df5f482401ccf4b71732a1a6cc7a2fa680af0`
- Initial focused-validator commit: `764821b20aa23f55dab86fece8b9be607ba9d3f7`
- Repaired validator / exact repository-native validated candidate: `9105753f179ffaa18cfed5bb4a2ab316051b2314`
- This READY update is handoff-only; production content and validator behavior are unchanged from the validated candidate.

## Scope
Adds a three-mission Republic border-records character arc that consumes A1 `world: republic border pressure` read-only.

The slice is intentionally distinct from existing Republic customs-review and manifest-appeal arcs. Those focus customs declarations, review triggers, corrections, and challenge/disposition policy. This slice focuses border-security testimony provenance: direct patrol observation, civilian witness reports, clerk summaries, repeated copies, independent corroboration, and how resolved warnings should stop circulating as active evidence.

Recurring characters:
- Talia Rook — Republic border-records officer who wants a durable evidence trail.
- Jace Verran — independent courier who has crossed the pirate frontier often enough that copied summaries of one observation have begun to look like multiple independent reports.

## Dynamic behavior
### Offer
Appears while `world: republic border pressure >= 4`.

Three substantive routes plus refusal:
1. **Lineage-first** — preserve every report while marking direct observation, witness statement, summary, copy, correction, and source lineage.
2. **Independent-evidence-first** — operational decisions count independently verified observations while retaining copied claims as provenance rather than deleting them.
3. **Paired evidence/history** — maintain a complete evidence-history view plus a separate current-evidence view that tracks independence, age, verification, challenge, and contradiction.
4. **Refusal** — records no general procedure and does not enter the Review path.

### Review
Appears only after A1 naturally reduces border pressure to `<= 2`.

Second-order problem: downstream copies can preserve a suspicious conclusion while losing source lineage, corrections, contradictions, or the disposition that closed the warning.

Two terminal settlements:
- **Portable provenance packet** — source type, direct/derived status, observation date, independence, corrections, contradictions, current disposition, and open/closed status travel together.
- **Expiry and renewal** — resolved reports remain historical/searchable but stop circulating as active warnings; only genuinely new observation can reopen them.

### Aftermath
`Rook Remembers` consumes either settlement exactly once and demonstrates that history can remain durable without duplication manufacturing corroboration.

## Ownership / persistence invariants
- A1 is sole owner/writer of `world: republic border pressure`.
- B2 reads that signal only for Offer/Review gating.
- Every direct persistent write in the new slice is under `B2 Republic Border Testimony Compact:*`.
- No credits, reputation, cargo, outfits, ships, fleets, combat rating, or unrelated campaign state are modified.
- Historical source presence is not guilt, motive, or fresh evidence.
- Repeated summaries/copies of one observation do not become independent corroboration.
- A resolved historical warning may remain searchable without remaining an active accusation forever.

## Files
- `data/human/b2 republic border testimony compact.txt`
- `tools/story/validate_b2_republic_border_testimony_compact.py`
- `story/B2_REPUBLIC_BORDER_TESTIMONY_COMPACT_HANDOFF_20260820.md`

## Focused validation
```bash
python3 tools/story/validate_b2_republic_border_testimony_compact.py "data/human/b2 republic border testimony compact.txt"
```

The first simulation/story workflow exposed one validator-only wording mismatch: the validator required the phrase `resolved warnings stop propagating as active warnings`, while the production content correctly expressed the semantic invariant as resolved reports that `stop circulating as active warnings`. Production content and the intended behavior were unchanged; the validator was repaired in `9105753f179ffaa18cfed5bb4a2ab316051b2314`.

## Exact repository-native validation evidence
On exact candidate `9105753f179ffaa18cfed5bb4a2ab316051b2314`:
- `Fork simulation and story validation` run #262 / `32408984516`: **SUCCESS**.
- Focused story/simulation validator discovery and execution: **SUCCESS**.
- `validate_b2_republic_border_testimony_compact.py`: **PASS** as part of the focused suite.
- Changed-content style: **SUCCESS**.
- A1 world-state ownership/regression contracts: **SUCCESS**.
- `Fork save-load integration smoke` run #247 / `32408984517`: **SUCCESS**.
- Production Endless Sky configure/build and stock save-load smoke: **SUCCESS**.

Actual-game acceptance can still exercise all four Offer choices, save/reload persistence, Review gating after A1 pressure recovery, both mutually exclusive settlements, and one-shot aftermath behavior, but repository-native acceptance gates required for READY are green.

## Process safety
The private execution service process inventory was checked. It reported four pre-existing service-owned orphan processes; none were killed or modified. No unrelated host workspace or process was disturbed.

## A3 / B3 guidance
A3 should re-read current `main` before integration, verify ancestry/conflicts, and integrate only if this branch remains semantically clean against newer authoritative work. B3 should preserve the distinction among direct observation, witness report, copied summary, inference, correction, contradiction, and disposition. A copied report must never silently become an independent witness merely because it appears in multiple downstream files.
