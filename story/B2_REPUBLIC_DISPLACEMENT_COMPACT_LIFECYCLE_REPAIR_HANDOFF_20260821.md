# B2 Republic Displacement Compact lifecycle repair handoff — 2026-08-21

## Verdict

**PARTIAL — implementation complete; repository-native CI pending.**

A3 must not integrate this branch until both repository-native validation workflows reach terminal green on the exact candidate head recorded below.

## Authority and isolation

- Stage: B2 — Story Characters + Dynamic Content
- Authoritative integration branch: `main`
- Authoritative base SHA: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-republic-displacement-lifecycle-20260821-1428`
- Self-integration: **not performed**

## Focused defect

`B2 Republic Displacement Compact` is a dialogue/state-only three-mission slice. Its three positive Offer routes, two Review settlements, and `Hale Remembers` aftermath path wrote persistent state and then terminated with `accept`, despite creating no gameplay objective. That can place objective-less missions in the accepted mission list.

The refusal path already terminated with `decline`.

## Repair

Production lifecycle repair commit:

- `c61b2e059d72d66a78c89b27addecb59776a11ee`

Changes:

- added the repository-standard Endless Sky GPL header because the legacy production file is now touched by changed-content style;
- changed all six positive state-only terminal `accept` commands to `decline`;
- preserved the existing refusal `decline`, yielding seven clean state-only terminals total;
- preserved Lena Ortiz / Devin Hale dialogue and characterization;
- preserved all three initial routes (`continuity`, `ledger`, `compact`) and refusal;
- preserved both terminal settlements (`continuity compact`, `bounded review`);
- preserved all trust, reviewed, aftermath, and other `B2 Republic Displacement Compact:*` condition names and values;
- preserved Republic source scoping and all A1 read thresholds.

No new rewards, cargo, equipment, combat, destination, NPC, timer, or other gameplay objective was added.

## Validator hardening

Focused-validator commit:

- `dc2b3f188aa5992e3f027a2475a00231defad98e`

`tools/story/validate_b2_republic_displacement_compact.py` now additionally requires:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no objective-bearing directives that would invalidate the dialogue/state-only lifecycle assumption.

Existing checks remain for mission graph, named characters, three routes plus refusal, exactly two settlements, later-reader persistence, local `goto`/`label` integrity, material/reputation mutation guards, and A1 world-state read-only ownership.

## Ownership and continuity invariants

A1 remains the sole writer of:

- `world: republic displacement pressure`

B2 continues to read that signal only for Offer/Review gating. All B2 persistence remains namespaced under:

- `B2 Republic Displacement Compact:*`

Narrative semantics are unchanged: protected housing/passage continuity, explicit accepting-office handoff, bounded review, private carrier capacity, and public responsibility remain distinct but linked concerns.

## Candidate under validation

Exact production + validator candidate before this handoff commit:

- `dc2b3f188aa5992e3f027a2475a00231defad98e`

Required repository-native gates:

1. `Fork simulation and story validation`
   - focused Republic Displacement validator
   - focused story suite / repository content contracts
   - A1 simulation and state-ownership regressions
   - changed-content style
2. `Fork save-load integration smoke`
   - production configure/build
   - stock save/load smoke cases

At handoff creation these workflows have not yet been observed terminal green, so the verdict remains PARTIAL.

## A3 / B3 integration notes

A3 should integrate only after the exact validated candidate reaches terminal green and should re-read current `main` first for ancestry/concurrency changes.

B3 should preserve the lifecycle invariant:

> Dialogue-only B2 missions that merely persist state terminate with `decline`; `accept` is reserved for mission lifecycles that actually create gameplay objectives.

No story-state migration is required because condition names and values are unchanged.
