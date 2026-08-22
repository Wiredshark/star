# B2 Merchant Diversion Compact lifecycle repair — 2026-08-22

## Verdict

PARTIAL pending repository-native validation.

## Authoritative base

- repository: `Wiredshark/star`
- authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- branch: `agent/b2-merchant-diversion-lifecycle-20260822-0027`

## Scope

Focused lifecycle repair for the already-integrated `B2 Merchant Diversion Compact` slice.

The three missions are dialogue/state-only. The Offer previously used terminal `accept` on its three positive routes, the Review used terminal `accept` on both settlements, and `Ward Remembers` used terminal `accept`, even though none of those paths create a gameplay objective. Refusal already used `decline`.

The production repair converts all six objective-less positive `accept` terminals to `decline`. All seven terminal paths now persist the same existing state and close cleanly.

## Exact commits

- production lifecycle repair: `fdc2b6b4acf8ba979aa4b9eec6efd12ff69ebe49`
- validator hardening: `0add002577ffe99bd4a83fbd1f906c02483e7ef9`

## Files changed

- `data/human/b2 merchant diversion compact.txt`
- `tools/story/validate_b2_merchant_diversion_compact.py`
- `story/B2_MERCHANT_DIVERSION_COMPACT_LIFECYCLE_REPAIR_HANDOFF_20260822.md`

## Behavior preserved

- Nessa Ward / Cal Harker characterization remains unchanged.
- expiry-first, field-first, paired, and refusal routes remain unchanged.
- portable-expiry-docket and evidence-ladder settlements remain unchanged.
- `Ward Remembers` remains the one-shot aftermath reader.
- Merchant source scope remains unchanged.
- A1 remains sole owner/writer of `world: merchant route diversion pressure`; B2 reads it only.
- all persistent writes remain under `B2 Merchant Diversion Compact:*`.
- no material, reputation, cargo, ship, fleet, or combat ownership changes.
- temporary routing advice remains distinct from permanent route truth.
- repeated reports remain distinguishable from independent observations and later contradictions.

## Validator hardening

The focused validator now additionally requires:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no destination/stopover/waypoint/NPC/cargo/passenger/deadline/timer directive that would invalidate the state-only lifecycle assumption.

All existing mission graph, route, settlement, A1 ownership, B2 write ownership, mutation-surface, continuity, and local `goto`/`label` checks remain.

## Validation state

Repository-native validation is pending on the exact branch head. Do not promote to READY or integrate until both simulation/story/style and production build/save-load workflows are terminal green.

## A3 / B3 integration notes

A3 retains integration authority. Do not self-merge this branch. Re-read current `main`, verify ancestry/mergeability, and integrate only if the lifecycle-only diff remains clean.

Preserve the lifecycle invariant that dialogue/state-only B2 missions terminate with `decline`; reserve `accept` for mission paths that actually create gameplay objectives.

Preserve the Merchant diversion invariant that a temporary route recommendation is not permanent route truth, and that direct observation, relayed report, inference, contradiction, review state, and closure remain distinguishable.
