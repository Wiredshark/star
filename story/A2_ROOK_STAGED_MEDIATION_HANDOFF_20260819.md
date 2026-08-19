# A2 Rook Staged Mediation handoff — 2026-08-19

## Purpose

This integration slice replaces the older `A2 Dialogue: Rook Mediation` candidate's ambiguous accepted-mission / `on complete` lifecycle with a purely staged stock-content flow.

## Production structure

File: `data/human/a2 rook staged mediation.txt`

Named character: **Imani Rook**, New Boston port mediator.

The slice contains four one-shot offered missions:

1. `A2 Rook Mediation: First Meeting`
   - balanced evidence-first route;
   - visible-disabled `[Combat experience: convoy command]` route backed by authoritative `combat rating >= 5`;
   - hidden `[Prior service: Deep convoy]` route backed by authoritative `Deep: Syndicate Convoy: done`;
   - persistent refusal route.
2. `A2 Rook Mediation: Case Review`
   - appears only after a positive first-stage route;
   - reads the chosen route and writes a route-specific outcome;
   - clears its pending latch and schedules the later reader.
3. `A2 Rook Mediation: Later Reader`
   - remembers the route-specific outcome;
   - lets the player welcome or decline future contact;
   - clears its pending latch.
4. `A2 Rook Mediation: Refusal Reader`
   - appears only after the initial refusal;
   - proves the refusal was not converted into endorsement;
   - allows a durable no-future-mediation boundary.

No mission uses `on complete`. No positive route leaves an accepted mission waiting on an implicit completion event.

## State authority

A2 reads but does not write:
- `combat rating`;
- `Deep: Syndicate Convoy: done`.

All new writable state is namespaced `A2 Rook Mediation:*` and uses ordinary condition persistence.

## Focused validator

`tools/story/validate_a2_rook_staged_mediation.py` checks:
- exact four-mission order;
- New Boston scoping;
- Imani Rook identity;
- hidden and visible-disabled special-response modes;
- three positive routes plus refusal;
- staged review/later/refusal pending-state transitions;
- absence of `on complete`;
- read-only authoritative inputs;
- local `goto` / `label` resolution.

## Validation state

Repository and committed-content inspection through the GitHub connector succeeded. An isolated local clone was attempted for executable validation, but the execution environment could not resolve `github.com` and failed before checkout:

`fatal: unable to access 'https://github.com/Wiredshark/star.git/': Could not resolve host: github.com`

Therefore this handoff does **not** claim execution of the focused validator, `utils/check_content_style.py`, the normal Endless Sky parser/build, actual-game runtime, or save/load roundtrip.

## Integration rationale

The staged replacement is safer than the older PR #2 candidate because it removes the unclear accepted-mission completion dependency entirely. Each stage becomes eligible from explicit persisted state and marks itself consumed before returning to normal gameplay. The old PR should be closed as superseded rather than merged alongside this file.
