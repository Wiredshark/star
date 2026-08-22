# A2 Syndicate Parts Practice — handoff

## Verdict

PARTIAL — isolated A2 candidate pending exact-head repository-native validation and actual-game acceptance.

## Authority

- Repository: `Wiredshark/star`
- Authoritative integration branch: `main`
- Authoritative base SHA: `37bf17aa303d7a9f284a5b2b433d560ddd0404c2`
- Branch: `agent/a2-syndicate-parts-practice-20260820-0212`
- Production commit: `6ec3e0c5feb4459ddb2e3bb0692319ce5b6b1722`
- Validator commit: `e8791e97d4763b95414f24774ac06962ae80e5b2`

## Concurrency boundary

An earlier same-run labor-practice candidate was closed as REJECTED after open B2 PR #146 was found to occupy the crew-qualification/rotation domain. This replacement slice deliberately uses the separate A1 replacement-parts scarcity/provenance surface and does not modify B2 qualification state.

## Implemented RPG loop

1. At `world: syndicate parts scarcity >= 3`, procurement auditor Elara Dane asks how scarce substitute components should be governed.
2. The player chooses provenance-first traceability, critical-system reserve, reversible substitution with expiry/reinspection, or explicit refusal.
3. New persistence is confined to `A2 Syndicate Parts Practice:*`.
4. The review waits for authoritative parts scarcity to recover to `<= 1`.
5. Each positive route is then evaluated against current `world: syndicate maintenance backlog` being `>= 3` or `< 3`, producing six state-sensitive outcomes plus refusal-respected handling.

This turns the newly integrated B1 replacement-stock provenance history into a connected A2 feedback loop without making the historical exhibit itself authoritative policy.

## Files

- `data/human/a2 syndicate parts practice.txt`
- `tools/story/validate_a2_syndicate_parts_practice.py`
- `story/A2_SYNDICATE_PARTS_PRACTICE_HANDOFF_20260820.md`

## Invariants

- A1 remains sole writer of `world: syndicate parts scarcity` and `world: syndicate maintenance backlog`.
- No writes to labor strain, labor rotation, Tessa Marr maintenance-triage state, or B2 Syndicate Qualification Compact state.
- Refusal remains refusal and is not converted into consent or attribution.
- Scarcity policy does not imply universal Syndicate procurement law or player corporate authority.
- Emergency substitutes remain distinguishable from permanent certification.

## Validation plan

Focused validator:

`python3 tools/story/validate_a2_syndicate_parts_practice.py`

Required broader gates:

- exact-head fork simulation/story/style workflow;
- production build and stock save-load smoke;
- actual-game initial scarcity gating at >=3;
- all four initial choices;
- recovery gating at scarcity <=1;
- all six backlog-high/backlog-low positive outcomes plus refusal handling;
- save/reload between stages;
- one-shot suppression and Syndicate offer-precedence regression.

No test is claimed unless its execution is separately recorded.

## A3 integration instructions

Integrate only after exact-head CI and runtime acceptance. Preserve A1 ownership exactly. This slice is intentionally orthogonal to B2 PR #146's crew qualification compact and to Tessa Marr's existing maintenance-allocation policy.
