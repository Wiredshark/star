# B2 Bunrodea Freight Petition Compact lifecycle repair handoff — 2026-08-22

## Verdict
PARTIAL pending repository-native exact-head validation.

## Authoritative base
`a17a89fb4779200a0634a6dade1811c4dc9cc2be`

## Scope
Focused B2 lifecycle repair for the integrated `B2 Bunrodea Freight Petition Compact`. The three missions are dialogue/state-only, but six positive terminal paths used `accept` despite creating no gameplay objective. This repair changes those six terminals to `decline`; the refusal path already declined, so all seven state-only terminal paths now persist the same state and close cleanly.

## Preserved story/state semantics
- Sedi Var / Iral Kes characterization and dialogue are unchanged.
- Sedi-first, Iral-first, paired-docket, and refusal routes are unchanged.
- Portable petition docket / dual-ledger settlements are unchanged.
- One-shot `Sedi Remembers` aftermath is unchanged.
- All persistent condition names and values remain `B2 Bunrodea Freight Petition Compact:*`.
- Common freight facts remain distinct from ownership/liability petition authority.
- No `world:*`, material, reputation, ship, fleet, or combat ownership is introduced.

## Validator hardening
`tools/story/validate_b2_bunrodea_freight_petition_compact.py` now requires zero terminal `accept`, exactly seven terminal `decline`, and rejects objective-bearing mission directives that would invalidate the dialogue/state-only lifecycle assumption. Existing graph, character, route, settlement, state-ownership, mutation-surface, continuity, and local `goto`/`label` checks remain.

## Lifecycle invariant
Dialogue/state-only B2 missions that merely persist conditions terminate with `decline`; `accept` is reserved for mission paths that actually create gameplay objectives.

## Validation required before READY
- focused Bunrodea Freight Petition validator
- repository story/state-ownership validators
- changed-content style
- production configure/build
- stock save-load smoke

## A3/B3 integration notes
A3 retains integration authority. Re-read current `main`, verify ancestry/mergeability, and preserve all existing condition names/values. B3 should preserve the distinction between verified freight facts and separately appealable ownership/liability authority.
