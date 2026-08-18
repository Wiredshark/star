# A2 Dialogue Vertical Slice Handoff — 2026-08-18

## Verdict

**PARTIAL / SPECIALIST CANDIDATE — NOT YET A3-READY**

The branch contains a real production-content vertical slice and a focused structural validator, but this backup run did not have a clone/build/runtime environment for `Wiredshark/star`; therefore parser/build/save-load/actual-game runtime acceptance is not claimed.

## Repository authority recovered

- Repository: `Wiredshark/star`
- Authoritative staging branch observed through the active B2 handoff: `agent/global-loop-diversity-20260815`
- Authoritative base SHA used: `c6cb81fe47d00c25df9a3947db83eb930f872f35`
- Base commit subject: `docs: carry dialogue priority into stage prompts`
- A2 branch: `agent/a2-dialogue-vertical-20260818-1406`
- Current A2 head before this handoff file: `e217cdf87bf4003fc4a9fe67f912ff39ce6fa3ba`

## Concurrency check

GitHub branch search showed no active branch matching `a2`. An open B2 draft PR exists (`agent/b2-broken-compact-20260818-1326`) and explicitly assigns engine primitives to A2/A1, so this A2 slice intentionally avoids editing B2's character packet and instead uses a separate named NPC/content proof.

## Implemented slice

Files:

- `data/human/a2 dialogue vertical slice.txt`
- `tools/validate_a2_dialogue_slice.py`

Named NPC: **Imani Rook**, port mediator on New Boston.

The first mission presents four meaningful routes:

1. balanced evidence-first mediation;
2. `[Combat experience: convoy command]`, gated by authoritative `combat rating >= 5`;
3. `[Prior service: Deep convoy]`, gated by persistent `Deep: Syndicate Convoy: done`;
4. refusal, which remains valid content rather than a reload/dead-end path.

The special-response labels are deliberately presentation text only. Their authority remains the existing `to display` condition mechanism; no dialogue-only shadow state is introduced.

Route choice writes ordinary persistent condition state. Completion writes route-specific outcome state. Separate later-reader missions consume those outcomes, including a refusal reader, so the first conversation is not an isolated one-shot.

## Persistence / compatibility invariants

- Uses stock conversation, mission, condition, and GameAction syntax only.
- Adds no save schema.
- Old saves default all new `A2 Dialogue:*` conditions to absent/zero.
- No duplicate relationship/world-state database is introduced.
- Existing conversations are untouched.
- Requirement labels do not replace or duplicate the authoritative condition check.

## Structural validator

`tools/validate_a2_dialogue_slice.py` checks the intended acceptance structure:

- production mediation mission exists;
- named later readers exist;
- both special labels exist;
- each label has the corresponding authoritative persistent gate;
- four routes exist;
- route-specific durable outputs exist;
- later readers consume those outputs;
- forbidden shadow-state markers are absent.

## Validation performed in this backup run

Verified through GitHub connector evidence:

- base SHA and dialogue-priority document;
- stock `Conversation` supports per-choice `to display` and `to activate` conditions;
- stock `ConversationPanel` hides choices through `ShouldDisplayNode()` and tests activation separately;
- stock `GameAction` falls through to condition assignments for unrecognized action keywords;
- stock mission data uses inline conversations and persistent condition mechanisms;
- `New Boston` is an existing production location;
- branch writes succeeded and exact commit SHAs were returned by GitHub.

Not performed / not claimed:

- C++ build;
- Endless Sky parser/load gate on the new file;
- save/load roundtrip;
- actual-game runtime interaction;
- screenshot/UI proof (no engine UI change was made);
- execution of the new Python validator against a checked-out branch.

The private Fallout Mesh Host repository workspace was inspected first but is wired to `Wiredshark/fallout-test`, not `Wiredshark/star`, so it was not used to fake or contaminate validation for this repository.

## A3 integration instructions

Do **not** integrate yet. First obtain a real `Wiredshark/star` checkout at this branch and run, at minimum:

1. `python3 tools/validate_a2_dialogue_slice.py`
2. repository data/parser validation or equivalent load gate;
3. normal build/unit suite relevant to mission/conversation parsing;
4. actual-game proof that each eligible route appears/hides correctly;
5. actual-game proof that route state survives save/load;
6. actual-game proof that `Rook Remembers` / refusal reader consumes the prior choice;
7. stock conversation regression / integration gates.

If those pass without content-syntax corrections, upgrade the verdict to READY/SPECIALIST_READY. Until then:

`DIALOGUE_SYSTEM_STATUS: NOT_STARTED` remains too pessimistic because a production candidate now exists, but `INTEGRATED_FOUNDATION` and `INTEGRATED_PRODUCTION_SLICE` are not justified. Recommended specialist status: `SPECIALIST_CANDIDATE_UNVALIDATED`.

`DIALOGUE_SYSTEM_NEXT_GAP: obtain authoritative star build/runtime environment; parse/load/save/runtime-validate the Imani Rook production slice and correct any data-syntax issues before A3 integration.`

## Diversity / domain labels

- `LOOP_ID: A2`
- `DOMAIN: modern dialogue / persistent RPG consequence`
- `SUBSYSTEM: conversation conditions + mission/global-condition persistence`
- `WORK_TYPE: production vertical-slice content + acceptance validator`
- `DIVERSITY_CHECK: explicit user-priority repeat; justified by open A_LOOP_DIALOGUE_SYSTEM.md acceptance target`
