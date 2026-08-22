# B2 Kor Efret Passage Continuity Compact lifecycle repair handoff

Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT

Verdict: READY for A3 review/integration.

Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`

Branch: `agent/b2-kor-efret-passage-lifecycle-20260822-1326`

Production lifecycle repair: `7300c337af170a52ddf3f55b6842b417fa4d2bcc`

Validator hardening: `59e30295f57e6e60335a5c37a33544839587cf09`

Exact fully validated production/validator/handoff candidate: `4e2fc2ed4824ad48e7cd3b71511a866757bec66b`

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

## Exact validation evidence

On exact candidate `4e2fc2ed4824ad48e7cd3b71511a866757bec66b`:

- `Fork simulation and story validation` run `32588460104` / #413: SUCCESS.
- `Fork save-load integration smoke` run `32588460174` / #398: SUCCESS.
- Production configure: SUCCESS.
- Production build: SUCCESS.
- Stock save-load smoke cases: SUCCESS.
- Focused story validation, A1/state-ownership contracts, and changed-content style are covered by the successful simulation/story workflow.

The candidate is exactly three commits ahead / zero behind the authoritative base and changes only:

- `data/korath/b2 kor efret passage continuity compact.txt` — six `accept` to `decline` lifecycle fixes;
- `tools/story/validate_b2_kor_efret_passage_continuity_compact.py` — lifecycle assertions;
- this durable handoff.

## A3 / B3 integration notes

A3 should recheck current-main ancestry before integration and must retain integration authority. The lifecycle invariant is: dialogue/state-only B2 missions that merely persist state terminate with `decline`; `accept` is reserved for mission paths that actually create gameplay objectives.

Preserve the distinction among physical safety, family contact, current destination preference, onward passage, consent, and voluntary resettlement. A safe arrival must not silently become a completed family or settlement obligation.
