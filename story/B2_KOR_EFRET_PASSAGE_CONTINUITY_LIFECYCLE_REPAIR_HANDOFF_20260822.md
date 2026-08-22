# B2 Kor Efret Passage Continuity Compact lifecycle repair handoff

Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT

Verdict: PARTIAL pending exact-head repository-native validation.

Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`

Branch: `agent/b2-kor-efret-passage-lifecycle-20260822-1326`

Production lifecycle repair: `7300c337af170a52ddf3f55b6842b417fa4d2bcc`

Validator hardening / current candidate: `59e30295f57e6e60335a5c37a33544839587cf09`

## Scope

The integrated `B2 Kor Efret Passage Continuity Compact` is a dialogue/state-only three-mission arc. Its three positive Offer routes, two Review settlements, and `Tracker Remembers` aftermath previously terminated with `accept` despite creating no gameplay objective. That can leave objective-less missions active after their conversations end.

This repair changes only those six positive terminal commands from `accept` to `decline`. Refusal already used `decline`, so all seven state-only terminal paths now persist the same existing story state and close cleanly.

## Preserved behavior and canon

- Tracker and Passage Keeper remain player-private shorthand rather than Korath names, titles, or centralized offices.
- Existing reunion-first, passage-first, paired, and refusal routes are unchanged.
- Existing family-packet and two-stage settlements are unchanged.
- All existing `B2 Kor Efret Passage Continuity Compact:*` condition names and values are unchanged; no save migration is required.
- The B1 Family Reunification Register and Passage Contribution Ledger remain read-only dependencies.
- Physical safety, family contact, current destination preference, onward passage, consent, and voluntary settlement remain separate facts.
- The repair does not create or imply mandatory repatriation or a centralized Kor Efret refugee authority.

## Validator hardening

`tools/story/validate_b2_kor_efret_passage_continuity_compact.py` now additionally requires:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no destination, stopover, waypoint, NPC, cargo, passenger, deadline, or timer directives that would invalidate the dialogue/state-only lifecycle assumption.

All previous mission graph, recurring-character, route, settlement, B1 dependency, state-ownership, mutation-surface, local goto/label, consent, and voluntary-resettlement checks remain.

## Required validation before READY

- `Fork simulation and story validation` must be terminal green on the exact candidate/head.
- `Fork save-load integration smoke` must be terminal green on the exact candidate/head.
- Changed-content style must pass.
- Focused Kor Efret Passage validator must pass.
- A1/state-ownership contracts must pass.
- Production configure/build and stock save-load smoke must pass.

## A3 / B3 integration notes

A3 should integrate only after exact-head validation is terminal green and current-main ancestry is rechecked. The lifecycle invariant is: dialogue/state-only B2 missions that merely persist state terminate with `decline`; `accept` is reserved for mission paths that actually create gameplay objectives.

Preserve the distinction among physical safety, family contact, current destination preference, onward passage, consent, and voluntary resettlement. A safe arrival must not silently become a completed family or settlement obligation.
