# B2 Republic Manifest Appeal Compact — handoff

- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Authoritative base: `8785f25572b65d66c6181a39d1ef2b28ca6dda83`
- Branch: `agent/b2-republic-manifest-appeal-20260819-2027`
- Production commit: `438752c6eb98703ddd90478a6c0ccb7172799daf`
- Validator commit: `8f72380b62612641f1420ece6b7ae421de05e5b4`
- Current verdict: PARTIAL pending repository-native exact-head CI/build/save-load evidence.

## Character / dynamic-content behavior

Adds customs adjudicator Lena Varo and freight clerk Orren Pike as recurring Republic characters. Their conflict consumes the integrated B1 Republic customs-history principles around manifest provenance, review basis, challenge records, and repeat-review limits.

The Offer provides three persistent substantive routes plus refusal:

1. visible correction chain;
2. current operational record with review link;
3. linked facts/corrections/unresolved challenges.

A delayed Review exposes a second-order failure: a corrected declaration can stop propagating while an old challenge continues to circulate without its disposition. The player resolves this into either:

- a portable disposition packet carrying trigger, verified facts, correction basis, disposition, and open/closed status; or
- an expiry-and-renewal rule where resolved challenges stop reproducing as active warnings unless fresh evidence creates a new review basis.

`Varo Remembers` is the one-shot later reader.

## Dependencies and ownership

- Depends on integrated B1 Republic customs institutional history in authoritative base `8785f25572b65d66c6181a39d1ef2b28ca6dda83`.
- Reads no A1/A2 state directly.
- Writes only `B2 Republic Manifest Appeal Compact:*` conditions.
- Does not write `world:*`, A1/A2 conditions, credits, reputation, cargo, outfits, ships, fleets, or combat state.
- Preserves the invariant that review/challenge history is not itself fresh evidence.
- Preserves the distinction among observed facts, declarations, corrections, unresolved challenges, and final dispositions.

## Files

- `data/human/b2 republic manifest appeal compact.txt`
- `tools/story/validate_b2_republic_manifest_appeal_compact.py`
- `story/B2_REPUBLIC_MANIFEST_APPEAL_COMPACT_HANDOFF_20260819.md`

## Validation required before READY

Run on the exact candidate head:

```text
python3 tools/story/validate_b2_republic_manifest_appeal_compact.py "data/human/b2 republic manifest appeal compact.txt"
python3 tools/story/validate_story_repo.py
python3 utils/check_content_style.py
```

Also require the repository-native simulation/story workflow and production configure/build/save-load smoke to complete successfully. Exercise all three routes plus refusal, delayed Review availability, mutual exclusivity of the two settlements, one-shot aftermath, and save/load persistence.

## A3 / B3 notes

A3 may integrate only after exact-head validation is terminal green. No self-integration has been performed. B3 should preserve the continuity boundary that an inherited challenge or prior decision to investigate cannot silently become new evidence merely because it was copied through multiple ports.
