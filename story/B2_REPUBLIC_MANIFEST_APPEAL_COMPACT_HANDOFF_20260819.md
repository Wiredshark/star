# B2 Republic Manifest Appeal Compact — handoff

- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Historical branch base: `8785f25572b65d66c6181a39d1ef2b28ca6dda83`
- Authoritative `main` recovered during lifecycle completion: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-republic-manifest-appeal-20260819-2027`
- Original production commit: `438752c6eb98703ddd90478a6c0ccb7172799daf`
- Original validator commit: `8f72380b62612641f1420ece6b7ae421de05e5b4`
- Original candidate head: `bf95d5e9191e4e21450cb7fff1d81987f143b600`
- Dialogue-lifecycle production repair: `3b6a114613d1b0d1a0bd13e06344b151a6401910`
- Lifecycle validator hardening: `fd17f239613878cfe785da3a266fdd5c20a4485b`
- Current verdict: PARTIAL pending terminal exact-head repository-native validation.

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

## Lifecycle completion

The three missions are dialogue/state-only. They create no destination, cargo, NPC, waypoint, passenger, deadline, timer, or other gameplay objective. Historically, the three positive Offer routes, two Review settlements, and `Varo Remembers` aftermath all wrote persistent state and then used terminal `accept`, risking objective-less accepted missions remaining active.

Commit `3b6a114613d1b0d1a0bd13e06344b151a6401910` converts exactly those six positive terminal commands to `decline`. Refusal already used `decline`, so all 7/7 state-only terminal paths now persist the same existing state and close cleanly.

Commit `fd17f239613878cfe785da3a266fdd5c20a4485b` hardens the focused validator to require:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no gameplay-objective directives in this state-only slice.

No dialogue, route, settlement, character, trust state, condition name/value, source scope, delayed Review timing, or evidence/canon semantic was changed by the lifecycle repair. No save-state migration is required.

## Dependencies and ownership

- Historical dependency is the integrated B1 Republic customs institutional history.
- Reads no A1/A2 state directly.
- Writes only `B2 Republic Manifest Appeal Compact:*` conditions.
- Does not write `world:*`, A1/A2 conditions, credits, reputation, cargo, outfits, ships, fleets, or combat state.
- Preserves the invariant that review/challenge history is not itself fresh evidence.
- Preserves the distinction among observed facts, declarations, corrections, unresolved challenges, and final dispositions.

## Files

- `data/human/b2 republic manifest appeal compact.txt`
- `tools/story/validate_b2_republic_manifest_appeal_compact.py`
- `story/B2_REPUBLIC_MANIFEST_APPEAL_COMPACT_HANDOFF_20260819.md`

## Exact validation state

Repository-native workflows were triggered automatically on exact production/validator head `fd17f239613878cfe785da3a266fdd5c20a4485b`:

- `Fork simulation and story validation` run `32608008477` / #439: in progress at handoff update time.
- `Fork save-load integration smoke` run `32608008487` / #424: queued at handoff update time.

Do not promote this handoff to READY until both exact-head workflows are terminal green. If either fails, repair the exact failure without weakening the lifecycle, state-ownership, or evidence boundaries.

## A3 / B3 notes

No self-integration has been performed. The historical branch is old relative to current `main`, so A3 must re-read current authoritative `main`, verify ancestry/mergeability, and integrate conservatively rather than assuming the original base remains current authority.

B3 should preserve the continuity boundary that an inherited challenge or prior decision to investigate cannot silently become new evidence merely because it was copied through multiple ports.

Lifecycle invariant: dialogue/state-only B2 missions that merely persist state terminate with `decline`; reserve `accept` for mission paths that actually create gameplay objectives.
