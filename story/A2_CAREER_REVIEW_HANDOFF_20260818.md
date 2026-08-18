# A2 Career Review Handoff — 2026-08-18

Verdict: **PARTIAL / specialist production candidate — not yet A3-ready**

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative integration branch observed: `main`
- Exact base SHA: `d611ce688997d3847ac303c229f64b80663db26c`
- Isolated A2 branch: `agent/a2-career-review-20260818-1906`
- Exact A2 implementation commit: `435ce5a1d44cac9c01fd98eda397587ba7b5cdde`

## Non-overlap / concurrency review

Before selection, the open A2 portfolio was inspected. Existing A2 candidates already cover Imani Rook mediation, Deep reactive news, Broken Compact relationship/legal content, Mara Venn security dialogue, and Selene Arcos science/mystery dialogue. Current B branches also cover Paradise, Far North, Syndicate, and southern-institution character/story work.

This slice deliberately uses a separate RPG axis: **player career identity and origin-aware self-definition**.

## Production behavior

`data/human/a2 career review.txt` adds two minor Republic-spaceport conversations centered on Pilot Guild assessor **Nia Calder**.

First meeting:
- offers only at `combat rating >= 25`;
- reads stock `start: deep`, `start: paradise`, and `start: syndicate` origin state to personalize framing;
- offers three substantive command-principle routes plus refusal;
- keeps the veteran-combat route visible but disabled until `combat rating >= 80`;
- stores only A2-owned derived memory: margin, force, options, or refusal;
- schedules a one-shot later reader.

Later reader:
- consumes the selected principle/refusal;
- reflects it back through Calder;
- records route-specific memory;
- clears its pending condition.

No C++ save schema, parser syntax, origin state, combat-rating state, or parallel dialogue-state authority is introduced or modified.

## Files

- `data/human/a2 career review.txt`
- `tools/story/validate_a2_career_review.py`
- `story/A2_CAREER_REVIEW_HANDOFF_20260818.md`

## Validation actually performed

A fresh private-host clone of the exact branch was created successfully. The clone resolved to branch head `078cc34cd549cbc65d4fb00b657c30f9ac573a98` at validation time and `git status --short` was clean.

Focused validator executed in that clone:

`python3 tools/story/validate_a2_career_review.py "data/human/a2 career review.txt"`

Observed result:

- PASS
- missions=2
- named_character=Nia Calder
- authoritative_inputs=start:* origin + combat rating
- career_principles=margin, force, options
- refusal_route=present
- later_reader=present
- authoritative_input_writes=none

The validator checks that the slice reads but does not overwrite stock origin/combat state.

The repository content-style checker was also attempted against the exact branch:

`python3 utils/check_content_style.py "data/human/a2 career review.txt"`

It could not start because the host Python environment lacks package `regex`:

`ModuleNotFoundError: No module named 'regex'`

This is recorded as an environment dependency limitation, not as a style pass or content failure.

## Validation not claimed

This run does **not** claim:
- successful repository content-style validation;
- full content parser/build regression pass;
- actual in-game offer/branch behavior;
- visible-disabled response presentation;
- save/load roundtrip;
- later-reader behavior after reload.

## A3 acceptance gates

Before integration:
1. rerun the focused validator from the final branch head;
2. provide the `regex` dependency and run normal Endless Sky content-style validation;
3. run the normal content parser/build test set;
4. exercise all four first-meeting routes in game;
5. verify no offer below combat rating 25;
6. verify veteran response disabled below 80 and selectable at/above 80;
7. exercise default, Deep, Paradise, and Syndicate origin framing;
8. save/reload after every route and verify the later reader;
9. verify stock conversation compatibility and no unrelated mission-state collision.

## Integration summary

This candidate is based directly on `main` and uses a private `A2 Career Review:*` condition namespace. It has no intended ordering dependency on other A2 specialist branches.

- Stage: A2
- Verdict: PARTIAL
- Base: `d611ce688997d3847ac303c229f64b80663db26c`
- Implementation commit: `435ce5a1d44cac9c01fd98eda397587ba7b5cdde`
