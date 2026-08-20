# A2 Syndicate Labor Practice — handoff

## Verdict

PARTIAL — specialist A2 candidate. The slice is isolated and ownership-safe, but requires repository-native CI plus actual-game acceptance before A3 integration.

## Authority and base

- Repository: `Wiredshark/star`
- Authoritative integration branch: `main`
- Authoritative base SHA: `37bf17aa303d7a9f284a5b2b433d560ddd0404c2`
- A2 branch: `agent/a2-syndicate-labor-practice-20260820-0208`
- Production commit: `8dbb18c51abeb5357a7825b10862109970ea9cba`
- Validator commit: `6c211202baf2099f65d2adeb8a3f0d784031ba72`

## Implemented loop

This slice consumes the newly integrated Syndicate dockyard-labor surface without changing its simulation ownership.

1. During `world: syndicate labor rotation active`, with labor strain at least 2, staffing coordinator Nera Voss asks the player for a workforce-practice recommendation.
2. The player may choose qualification-first matching, protected rest intervals, bounded cross-yard reassignment, or explicit refusal.
3. Positive and refusal choices persist only under `A2 Syndicate Labor Practice:*` conditions.
4. After A1 ends the crew rotation, a one-shot review evaluates each positive policy against current `world: syndicate labor strain` being either still elevated (`>= 2`) or stabilized (`< 2`).
5. This yields six live-world-state-sensitive positive outcomes plus refusal-respected handling.

The narrative deliberately applies the newly integrated B1 history themes—qualification ledgers, rest intervals, temporary reassignment scope—without pretending those historical observations create universal Syndicate labor law.

## Files

- `data/human/a2 syndicate labor practice.txt`
- `tools/story/validate_a2_syndicate_labor_practice.py`
- `story/A2_SYNDICATE_LABOR_PRACTICE_HANDOFF_20260820.md`

## Invariants

- A1 remains sole writer of `world: syndicate labor strain` and `world: syndicate labor rotation active`.
- This slice does not write Syndicate maintenance backlog, parts scarcity, or existing Tessa Marr maintenance-triage state.
- Refusal remains refusal and is not converted into authorization or public attribution.
- No universal Syndicate-wide labor statute, office, or player authority is invented.
- New persistence is deterministic and serializable through ordinary condition state.

## Validation

Focused validator command once executable checkout/CI is available:

`python3 tools/story/validate_a2_syndicate_labor_practice.py`

Required broader gates:

- repository story/simulation/style workflow on exact candidate HEAD;
- production build and stock save-load smoke;
- actual-game offer during active labor rotation;
- all four initial routes;
- all six elevated/stabilized review outcomes plus refusal handling;
- save/reload between briefing and review;
- one-shot suppression and Syndicate offer-precedence regression.

No unexecuted test is claimed as passed.

## A3 integration notes

Integrate only after exact-head repository validation and runtime acceptance. Preserve the A1 ownership boundary and do not combine this branch with Tessa Marr maintenance triage by rewriting either system's existing conditions. The intended connection is thematic and world-state-driven, not shared mutable state.
