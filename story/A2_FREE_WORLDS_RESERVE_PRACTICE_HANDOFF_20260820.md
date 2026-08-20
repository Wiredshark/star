# A2 Free Worlds Reserve Practice Handoff — 2026-08-20

## Verdict

**PARTIAL pending exact-head repository-native validation and actual-game acceptance.**

This A2 slice is isolated, committed, and intentionally unmerged for A3 authority.

## Repository / branch

- Repository: `Wiredshark/star`
- Authoritative integration branch: `main`
- Authoritative base SHA recovered at run start: `66766690c3c46c5f0c8b8d1c9bfb7781615c3e2c`
- Base integration: B2 Free Worlds Reserve Recovery Compact
- A2 branch: `agent/a2-free-worlds-reserve-practice-20260820-1506`
- Production commit: `81785ac0d65eb05ae3619926ce99c53d1b4e84e8`
- Focused-validator commit: `c04819d528d6c90e44bf24d088e40717bc164d7c`

## Concurrency / selection

Live `main`, open PRs, and matching A2 branches were inspected before authoring. No open or existing `a2-free-worlds-reserve*` branch was found. Existing Free Worlds A2 work targets relief coordination, patrol/traffic doctrine, storm navigation, repair priority, and related surfaces, not the newly integrated B2 reserve-recovery aftermath.

The newly authoritative B2 compact already distinguishes visible stock replenishment from genuinely restored emergency capacity, persists either a portable reserve-status packet or a reconciliation-cycle settlement, and writes `B2 Free Worlds Reserve Recovery Compact: aftermath seen`. This A2 slice consumes those states read-only.

## Player-facing loop

### Briefing

After B2 aftermath and only while authoritative A1 `world: free worlds relief reserve strain <= 1`, returning characters Rina Sol and Cal Brenner ask what practice should survive into the next emergency.

Persistent routes:

1. **Closure evidence** — a restoration claim should retain the evidence that closed each stock, staffing, transport, maintenance, and borrowed-capacity obligation.
2. **Current capacity** — historical recovery records remain provenance, but present staffing, transport, maintenance, and stock decide what is available now.
3. **Local only** — the compact remains contextual precedent rather than automatic authority over another Free World's procedure.
4. **Refusal** — no standing practice is established and the recurrence reader is not armed.

### Recurrence

A later authoritative A1 reserve-strain recurrence at `>= 3` triggers a one-shot history-aware review. Each positive A2 route is crossed with the integrated B2 settlement type:

- closure evidence + portable packet;
- closure evidence + reconciliation cycle;
- current capacity + portable packet;
- current capacity + reconciliation cycle;
- local-only + portable packet;
- local-only + reconciliation cycle.

This produces six distinct recurrence outcomes without rewriting the A1 strain or B2 settlement state.

## Feedback chain

`A1 reserve strain episode -> B2 recovery settlement -> A2 player practice during recovery -> later A1 reserve strain recurrence -> history-aware A2 consequence`

## Ownership / invariants

- A1 remains sole writer of `world: free worlds relief reserve strain`.
- All `B2 Free Worlds Reserve Recovery Compact:*` conditions are read-only.
- All new persistent writes are confined to `A2 Free Worlds Reserve Practice:*`.
- No credits, reputation, cargo, outfit, ship, fleet, combat, or material mutation.
- A prior closure is evidence about a prior condition, not proof that the reserve can never deteriorate again.
- Historical records remain provenance; current capacity must remain inspectable.
- Shared practice does not create centralized Free Worlds reserve authority.
- Refusal remains refusal and does not schedule the recurrence reader.

## Files

- `data/human/a2 free worlds reserve practice.txt`
- `tools/story/validate_a2_free_worlds_reserve_practice.py`
- `story/A2_FREE_WORLDS_RESERVE_PRACTICE_HANDOFF_20260820.md`

## Validation attempted / required

The focused validator is committed and is expected to be auto-discovered by the repository's story-validation workflow.

Required exact-head gates before A3 integration:

1. `Fork simulation and story validation` succeeds on the exact candidate head, including the focused validator, changed-content style, A1 regressions, and cross-file state-ownership checks.
2. `Fork save-load integration smoke` succeeds on the exact candidate head, including production configure/build and stock save-load smoke.
3. Actual-game acceptance verifies B2-aftermath + calm-state Briefing gating, all four initial routes, later A1 recurrence gating, all six positive settlement-sensitive outcomes, refusal suppression, save/reload between stages, one-shot suppression, and Free Worlds offer-precedence regression.

Do not claim any gate above until its actual result is observed.

## Host/process boundary

The exposed private execution host was inspected. It reports unrelated service process state and its repository remote is `Wiredshark/fallout-test`, not `Wiredshark/star`. It was left untouched and is not used as Endless Sky runtime evidence.

## A3 integration instructions

Re-read current authoritative `main` before integration. Verify ancestry and conflicts. Preserve A1 ownership of relief-reserve strain and B2 ownership of the Reserve Recovery Compact. Integrate only if exact-head repository-native validation is green and the content remains non-overlapping with newer A2 work.
