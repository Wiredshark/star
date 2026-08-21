# B2 Bunrodea Review Queue Dialogue Lifecycle Repair — Handoff

## Verdict

PARTIAL pending exact-head repository-native validation.

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-bunrodea-review-lifecycle-20260821-0227`
- Production lifecycle repair: `f5511e65b47950aa741358504c921264ee3f920d`
- Focused validator hardening: `16dce33349b855dce4a8094b63e2205da521802d`
- Final handoff head: this commit

This branch is isolated and must remain unmerged until A3 review.

## Why this repair exists

`B2 Bunrodea Review Queue Compact` is state-recording dialogue content: the Offer, Review, and `Iral Remembers` missions have no cargo, passenger, destination, waypoint, NPC, timer, or other gameplay objective. Their conversation endpoints previously used `accept` on positive/settlement/aftermath paths.

In current Endless Sky mission lifecycle semantics, an `accept` endpoint accepts the offered mission and can leave a state-only, objective-less mission in the player's active mission list. The B2 persistent state is already written before each terminal endpoint, so the correct lifecycle is to record state and terminate with `decline`.

## Exact behavioral change

The repair changes only dialogue terminal lifecycle in:

- `data/bunrodea/b2 bunrodea review queue compact.txt`

All seven terminal routes now use `decline` after writing the same state that existed before:

- Offer: age-first
- Offer: risk-first
- Offer: paired lanes
- Offer: refusal
- Review: portable delay history
- Review: reconciliation cycle
- Iral Remembers: aftermath completion

No dialogue text, route condition, A1 backlog threshold, B2 state name/value, settlement semantics, named character, source government, or ownership boundary was changed.

## Validator hardening

`tools/story/validate_b2_bunrodea_review_queue_compact.py` now additionally proves:

- no `accept` terminal remains in the state-only slice;
- exactly seven terminal `decline` endpoints are present;
- no gameplay-objective token has been added that would invalidate the state-only lifecycle assumption;
- all prior structural, state-ownership, route, settlement, goto/label, and continuity checks still apply.

## Ownership / continuity invariants

- A1 remains sole owner of `world: bunrodea freight review backlog`.
- Prior `B2 Bunrodea Freight Petition Compact` settlement state remains read-only.
- All writes remain `B2 Bunrodea Review Queue Compact:*`.
- Queue recovery remains distinct from individual petition recovery.
- The repair does not introduce centralized Bunrodea authority.
- Refusal remains refusal.
- Positive choices and settlements write exactly the same B2 conditions as before.

## Validation required before READY

Run the exact branch through repository-native gates:

1. `Fork simulation and story validation`
2. changed-content style
3. focused `validate_b2_bunrodea_review_queue_compact.py`
4. A1/state-ownership regressions
5. `Fork save-load integration smoke`
6. production configure/build and stock save-load smoke

If those gates are green on the exact final head, promote this handoff to READY without changing production behavior.

## A3 / B3 integration note

This is a lifecycle repair, not a narrative rewrite. A3 should review it as a two-file behavioral correction plus handoff. B3 should preserve the existing Bunrodea queue continuity semantics unchanged.
