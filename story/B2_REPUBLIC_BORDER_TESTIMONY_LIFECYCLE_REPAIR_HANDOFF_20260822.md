# B2 Republic Border Testimony Compact lifecycle repair handoff

- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Verdict: READY for A3 review/integration
- Authoritative base/main: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-republic-border-testimony-lifecycle-20260822-0725`
- Production lifecycle repair: `5c235a636c81549eabaf75dd9c2912a17fb36c94`
- Focused validator hardening: `e3f98fc13fa91a5b0dde2f0f61454ee1f11b82ed`
- Exact fully validated candidate: `e189971a4c98147a2bf4a89404dbef7b8becd058`

## Defect repaired

`B2 Republic Border Testimony Compact` is a dialogue/state-only three-mission slice. Its three positive Offer routes, two Review settlements, and `Rook Remembers` aftermath path wrote persistent state and then used terminal `accept` despite creating no destination, cargo, NPC, waypoint, timer, passenger, or other gameplay objective. The refusal path already used `decline`.

That lifecycle can leave objective-less accepted missions active after the conversation closes.

## Production repair

The six positive state-only terminal `accept` commands were changed to `decline`. All seven terminal paths now persist their pre-existing state and close cleanly.

No dialogue, character behavior, route, settlement, trust state, condition name/value, Republic scope, or world-state threshold changed. No save migration is required.

Files changed:

- `data/human/b2 republic border testimony compact.txt`
- `tools/story/validate_b2_republic_border_testimony_compact.py`
- `story/B2_REPUBLIC_BORDER_TESTIMONY_LIFECYCLE_REPAIR_HANDOFF_20260822.md`

## Ownership and continuity

A1 remains the sole writer/owner of `world: republic border pressure`. B2 reads it only for the existing Offer (`>= 4`) and Review (`<= 2`) gates.

All story writes remain under `B2 Republic Border Testimony Compact:*`.

The evidence/canon boundary is unchanged: direct observation, civilian testimony, clerk summary, copied report, inference, correction, contradiction, and final disposition remain separate facts. Repeated copies of one source do not become independent corroboration.

## Validator hardening

The focused validator now additionally enforces:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no destination, stopover, waypoint, NPC, cargo, passenger, deadline, or timer directives that would invalidate the dialogue/state-only lifecycle assumption.

All existing route, settlement, A1 ownership, B2 namespace, mutation-surface, evidence-boundary, and `goto`/`label` checks remain.

## Validation evidence

Exact candidate `e189971a4c98147a2bf4a89404dbef7b8becd058` passed both required repository-native workflows:

- `Fork simulation and story validation` run #398 / `32570340763`: SUCCESS
- `Fork save-load integration smoke` run #383 / `32570340748`: SUCCESS

This covers the focused Republic Border Testimony validator, full focused story/simulation contracts, A1/state-ownership regressions, changed-content style, production configure/build, and stock save-load integration smoke.

## A3 / B3 integration note

Do not self-integrate. A3 should re-read current `main`, confirm ancestry and that no equivalent lifecycle fix has already landed, then integrate the candidate if validation remains applicable.

Lifecycle invariant: dialogue/state-only B2 missions that merely persist state terminate with `decline`; `accept` is reserved for mission lifecycles that actually create gameplay objectives.
