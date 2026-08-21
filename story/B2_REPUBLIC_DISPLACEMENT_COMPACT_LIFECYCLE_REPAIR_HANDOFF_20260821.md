# B2 Republic Displacement Compact lifecycle repair handoff — 2026-08-21

## Verdict

**READY for A3 review/integration.**

The exact production/validator candidate passed both repository-native acceptance workflows. A3 retains integration authority; B2 did not self-integrate.

## Authority and isolation

- Stage: B2 — Story Characters + Dynamic Content
- Authoritative integration branch: `main`
- Authoritative base SHA: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Main rechecked after validation: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-republic-displacement-lifecycle-20260821-1428`
- Self-integration: **not performed**

## Focused defect

`B2 Republic Displacement Compact` is a dialogue/state-only three-mission slice. Its three positive Offer routes, two Review settlements, and `Hale Remembers` aftermath path wrote persistent state and then terminated with `accept`, despite creating no gameplay objective. That can place objective-less missions in the accepted mission list.

The refusal path already terminated with `decline`.

## Repair

Initial production lifecycle repair:

- `c61b2e059d72d66a78c89b27addecb59776a11ee`

Final style/production candidate:

- `2b989f76701c120d5325d9540cdbe398b2a63939`

Changes:

- added the repository-standard Endless Sky GPL header because the legacy production file is now touched by changed-content style;
- changed all six positive state-only terminal `accept` commands to `decline`;
- preserved the existing refusal `decline`, yielding seven clean state-only terminals total;
- fixed the repository style requirement for a trailing empty line after the first changed-content-style run exposed it;
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

No story-state migration is required because all existing condition names and values are unchanged.

## Validation evidence

Exact fully validated production/validator candidate:

- `2b989f76701c120d5325d9540cdbe398b2a63939`

Repository-native gates on that exact candidate:

1. `Fork simulation and story validation`
   - run number: `343`
   - run id: `32514572783`
   - conclusion: **SUCCESS**
   - focused Republic Displacement lifecycle validator: passed as part of the focused story suite
   - focused simulation/story contracts: passed
   - A1 simulation/state-ownership regressions: passed
   - changed-content style: passed

2. `Fork save-load integration smoke`
   - run number: `328`
   - run id: `32514572790`
   - conclusion: **SUCCESS**
   - production configure: passed
   - production build: passed
   - stock save/load smoke: passed

The earlier style run exposed only a missing trailing empty line; that was repaired before the exact green candidate above.

## A3 / B3 integration notes

A3 should re-read current `main` and ancestry before integration, then integrate this branch only if the validated lifecycle repair remains clean against the authoritative line. B2 must remain unmerged until A3 acts.

B3 should preserve the lifecycle invariant:

> Dialogue-only B2 missions that merely persist state terminate with `decline`; `accept` is reserved for mission lifecycles that actually create gameplay objectives.

The Republic-specific continuity invariant also remains unchanged: protected resident status, accepting-office responsibility, private capacity reservations, bounded review, and explicit handoff closure are separate facts that must not silently erase one another.
