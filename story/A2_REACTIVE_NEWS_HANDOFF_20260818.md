# A2 Reactive News Handoff — 2026-08-18

## Verdict

**PARTIAL / SPECIALIST CANDIDATE — NOT YET A3-READY**

This isolated A2 backup slice adds a distinct dynamic-narrative consumer rather than duplicating the open Imani Rook dialogue PR. It uses Endless Sky's stock `News` condition machinery to make ambient port dialogue react to authoritative persistent player history. No new save schema or news-only shadow state is introduced.

## Repository authority recovered

- Repository: `Wiredshark/star`
- Staging branch used for A-loop dialogue work: `agent/global-loop-diversity-20260815`
- Authoritative base SHA used: `c6cb81fe47d00c25df9a3947db83eb930f872f35`
- Base subject: `docs: carry dialogue priority into stage prompts`
- A2 branch: `agent/a2-reactive-news-20260818-1502`
- Production-data commit: `70f852c5e384d8055feffaa27b71784d169e5ff1`
- Validator commit: `0c878a71ebef3504996d1be8553d4f7012b1f578`

## Concurrency / non-duplication check

An existing open A2 draft PR (`#2`, `agent/a2-dialogue-vertical-20260818-1406`) already owns the Imani Rook production dialogue vertical slice. This run did not edit that branch, those files, or that character thread.

The current slice instead advances a separate A2 dynamic-narrative pressure from `A_LOOP_DIALOGUE_SYSTEM.md`: persistent history should have player-visible consequences outside the originating conversation. The new content is ambient `news`, not another mission/conversation tree.

## Implemented dynamic-narrative loop

File: `data/human/a2 reactive news.txt`

Three production news groups use existing authoritative state directly:

1. `A2 Deep convoy veteran`
   - Republic / Deep ambient chatter.
   - Visible only when `Deep: Syndicate Convoy: done` is true.
   - Turns a prior persistent mission outcome into later world acknowledgement.

2. `A2 Deep convoy command veteran`
   - Republic / Deep ambient chatter.
   - Requires both `Deep: Syndicate Convoy: done` and `combat rating >= 5`.
   - Demonstrates composition of persistent history plus an established player capability without copying either value into A2-owned state.

3. `A2 experienced Republic captain`
   - Republic non-station ambient chatter.
   - Requires `combat rating >= 5`.
   - Makes combat experience legible as social/world context without granting a universal dialogue advantage.

The messages deliberately acknowledge history and professional perception rather than asserting hidden NPC knowledge or creating a universal 'veteran = correct' rule.

## Persistence / compatibility invariants

- Uses existing `News::Load()` / `News::Matches()` `to show` condition support.
- Reads existing `ConditionsStore` state only.
- Writes no conditions or mission state.
- Adds no save schema.
- Old saves with absent conditions simply do not show the gated news.
- No duplicate relationship, dialogue, news-memory, or world-state authority is introduced.
- Existing stock news remains untouched.

## Focused validator

File: `tools/story/validate_a2_reactive_news.py`

The validator checks:

- all three production news groups exist;
- `Deep: Syndicate Convoy: done` is consumed;
- `combat rating >= 5` is consumed;
- the combined news group requires both inputs;
- each intended group has a `to show` gate;
- the file contains no A2-owned `seen` state, action block, shadow database marker, or other write-side state.

## Evidence recovered during this run

Live GitHub/source inspection confirmed:

- `A_LOOP_DIALOGUE_SYSTEM.md` remains an explicit open A-loop priority until A3 reaches `INTEGRATED_PRODUCTION_SLICE`.
- `source/News.h` already owns a `ConditionSet toShow` member.
- `source/News.cpp` loads `to show` with the player's `ConditionsStore` and `News::Matches()` evaluates `toShow.Test()`.
- existing human news uses the same `location`, `name`, `phrase`, `message`, and `word` data structures used by this slice.
- the separate Imani Rook A2 draft PR remains open and unmerged, so this branch intentionally avoids modifying it.

The private Fallout Mesh Host was also inspected first, but its repository workspace is `Wiredshark/fallout-test`, not `Wiredshark/star`; it was not used to fake build/runtime validation.

## Validation performed / not claimed

Performed:

- live repository/branch/PR concurrency inspection through the GitHub connector;
- direct inspection of stock `News` parser/runtime source and A-loop dialogue requirements;
- successful branch/file writes with exact returned commit SHAs;
- committed-content fetch/inspection should be used as the immediate source-level structural check.

Not performed / not claimed:

- execution of `python3 tools/story/validate_a2_reactive_news.py` in a checked-out `Wiredshark/star` tree;
- Endless Sky data parser/load gate;
- C++ build/unit suite;
- actual-game spaceport runtime proof;
- save/load runtime proof;
- UI screenshot proof (no UI code changed).

## A3 integration instructions

Do **not** integrate this branch as READY until an authoritative `Wiredshark/star` checkout can run:

1. `python3 tools/story/validate_a2_reactive_news.py`
2. repository content/data parser validation;
3. normal relevant build/unit regression suite;
4. actual-game Deep/Republic spaceport proof before and after `Deep: Syndicate Convoy: done`;
5. actual-game proof that the combined veteran item requires both convoy history and `combat rating >= 5`;
6. save/load proof that stock persistent conditions continue to drive visibility without A2-owned shadow state.

If those pass, this slice is a good secondary A2 integration candidate after or alongside the primary Imani Rook production dialogue foundation.

## Required A-loop labels

- `LOOP_ID: A2`
- `DOMAIN: dynamic narrative / ambient world acknowledgement`
- `SUBSYSTEM: News to-show conditions + persistent player-history readers`
- `WORK_TYPE: production content + focused structural validator`
- `DIVERSITY_CHECK: deliberately non-overlapping with active Imani Rook dialogue branch; adds a later world echo rather than another dialogue tree`
- `DIALOGUE_SYSTEM_STATUS: SPECIALIST_CANDIDATE_UNVALIDATED`
- `DIALOGUE_SYSTEM_NEXT_GAP: obtain authoritative star checkout/runtime; validate both the primary production dialogue and this persistent-history news reader through parser/build/save/runtime gates before A3 integration`

## A3-ready verdict

`PARTIAL` until the executable parser/build/runtime/save checks above are real and passing.
