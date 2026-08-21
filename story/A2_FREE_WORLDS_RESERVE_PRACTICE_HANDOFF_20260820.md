# A2 Free Worlds Reserve Practice Handoff — 2026-08-20

## Verdict

**PARTIAL pending refreshed exact-head repository-native validation after lifecycle repair.**

This A2 slice is isolated, committed, and intentionally unmerged for A3 authority.

## Repository / branch

- Repository: `Wiredshark/star`
- Authoritative integration branch recovered before repair: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Original authoritative base: `66766690c3c46c5f0c8b8d1c9bfb7781615c3e2c`
- A2 branch: `agent/a2-free-worlds-reserve-practice-20260820-1506`
- Original production commit: `81785ac0d65eb05ae3619926ce99c53d1b4e84e8`
- Original focused-validator commit: `c04819d528d6c90e44bf24d088e40717bc164d7c`
- Original style-repair candidate: `14b093e2d68eb491a2381269e7d070bfb376583b`
- Dialogue lifecycle repair: `d9f4f16ce375b013da63e47d0930b4d6f7e90a06`
- Focused lifecycle-validator repair: `d849b2470aebd18b40ba42d705d924ee69f27c49`

## Concurrency / selection

This backup run recovered current `main`, open A2 work, and recent B2 work before modifying anything. Current `main` has not advanced beyond the validated Bunrodea Review Queue integration, and the obvious newly authored B2 slices remain unintegrated. Rather than opening another speculative A2 feature, the run inspected existing isolated A2 candidates for executable repair work.

The Free Worlds Reserve Practice branch was already non-overlapping and had previously completed both repository-native workflows successfully on `14b093e...`, but that candidate predates the newly identified A2 dialogue lifecycle invariant. Inspection of the exact production diff found state-only terminal `accept` endpoints in both missions. That would place objective-less dialogue missions into the accepted mission list.

The repair changes only lifecycle termination semantics: every positive Briefing route and the Recurrence terminal now records the same persistent A2 state and exits with `decline`. Narrative text, route names, world-state thresholds, B2 settlement consumption, and ownership semantics are unchanged.

The focused validator now rejects any `accept` endpoint in this state-only slice and requires all four Briefing terminals plus the Recurrence terminal to use `decline`.

## Player-facing loop

After B2 aftermath and only while authoritative A1 `world: free worlds relief reserve strain <= 1`, returning characters Rina Sol and Cal Brenner ask what practice should survive into the next emergency.

Persistent routes:

1. **Closure evidence** — a restoration claim should retain the evidence that closed each stock, staffing, transport, maintenance, and borrowed-capacity obligation.
2. **Current capacity** — historical recovery records remain provenance, but present staffing, transport, maintenance, and stock decide what is available now.
3. **Local only** — the compact remains contextual precedent rather than automatic authority over another Free World's procedure.
4. **Refusal** — no standing practice is established and the recurrence reader is not armed.

A later authoritative A1 reserve-strain recurrence at `>= 3` triggers a one-shot history-aware review. Each positive A2 route is crossed with the integrated B2 settlement type, producing six distinct recurrence outcomes.

## Feedback chain

`A1 reserve strain episode -> B2 recovery settlement -> A2 player practice during recovery -> later A1 reserve strain recurrence -> history-aware A2 consequence`

## Ownership / invariants

- A1 remains sole writer of `world: free worlds relief reserve strain`.
- All `B2 Free Worlds Reserve Recovery Compact:*` conditions are read-only.
- All new persistent writes are confined to `A2 Free Worlds Reserve Practice:*`.
- No credits, reputation, cargo, outfit, ship, fleet, combat, or material mutation.
- State-only dialogue missions do not remain in the accepted mission list.
- A prior closure is evidence about a prior condition, not proof that the reserve can never deteriorate again.
- Historical records remain provenance; current capacity must remain inspectable.
- Shared practice does not create centralized Free Worlds reserve authority.
- Refusal remains refusal and does not schedule the recurrence reader.

## Files

- `data/human/a2 free worlds reserve practice.txt`
- `tools/story/validate_a2_free_worlds_reserve_practice.py`
- `story/A2_FREE_WORLDS_RESERVE_PRACTICE_HANDOFF_20260820.md`

## Validation evidence

Previous exact-head `14b093e2d68eb491a2381269e7d070bfb376583b` evidence remains useful as regression history but is superseded for acceptance because the branch now contains lifecycle changes:

- Fork simulation and story validation #259 / run `32407158443`: SUCCESS on the pre-lifecycle-repair head.
- Fork save-load integration smoke #244 / run `32407158322`: SUCCESS on the pre-lifecycle-repair head.

Required now:

1. Refreshed `Fork simulation and story validation` succeeds on the exact post-lifecycle-repair head, including the strengthened focused validator and changed-content style.
2. Refreshed `Fork save-load integration smoke` succeeds on the exact post-lifecycle-repair head.
3. Optional actual-game acceptance verifies B2-aftermath + calm-state Briefing gating, all four initial routes, later A1 recurrence gating, all six positive settlement-sensitive outcomes, refusal suppression, save/reload between stages, one-shot suppression, and absence of lingering accepted dialogue missions.

Do not promote to READY until both refreshed repository-native workflows are terminal green on the same exact head.

## Host/process boundary

No authoritative `Wiredshark/star` execution host was exposed through the available process connector in this run. Repository-native GitHub validation is therefore the executable acceptance gate; no host runtime evidence is fabricated.

## A3 integration instructions

Re-read current authoritative `main` before integration. Verify ancestry and conflicts. Preserve A1 ownership of relief-reserve strain and B2 ownership of the Reserve Recovery Compact. Integrate only the exact post-lifecycle-repair head after both repository-native workflows are green. Do not self-integrate from A2.
