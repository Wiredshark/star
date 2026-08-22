# B2 Merchant Recovery Margin Compact — dialogue lifecycle repair handoff

## Verdict

PARTIAL pending repository-native validation.

## Authority and isolation

- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-merchant-margin-lifecycle-20260822`
- Production lifecycle repair: `8971501779d85fe0321d6af39d536852bec16f3d`
- Focused validator hardening: `15d16a35626a557bf21477d07984659b9d923dfc`
- A3 retains integration authority; this branch must not self-integrate.

## Repair

`B2 Merchant Recovery Margin Compact` is a three-mission dialogue/state-only slice. Its three positive Offer routes, two Review settlements, and `Vale Remembers` aftermath previously wrote their existing persistent state and then terminated with `accept`, despite creating no destination, cargo, NPC, waypoint, timer, or other gameplay objective. That can leave objective-less missions in the active mission list.

The production repair changes exactly those six positive terminals from `accept` to `decline`. The refusal route already used `decline`, so all seven state-only terminal paths now persist the same state and close cleanly.

No dialogue, route condition, trust state, settlement, A1/B1 gate, Merchant scope, or persistent condition name/value was changed.

## Validator hardening

`tools/story/validate_b2_merchant_recovery_margin_compact.py` now additionally requires:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no destination, stopover, waypoint, NPC, cargo, passenger, deadline, or timer directives that would invalidate the state-only lifecycle assumption.

The pre-existing checks remain for the three missions, Imani Vale and Corin Beck, the three routes plus refusal, both settlements, one-shot aftermath consumption, A1 read-only ownership, B2-only writes, material/reputation mutation guards, local `goto`/`label` integrity, and distributed Merchant continuity.

## Ownership and continuity invariants

- A1 remains sole owner/writer of `world: merchant repair backlog`.
- B2 writes only `B2 Merchant Recovery Margin Compact:*` conditions.
- Clearing the current repair backlog is distinct from restoring future rescue/recovery margin.
- Declared reserve is distinct from physically usable berth, crew, tug, and repair capacity.
- Participating Merchant ports retain local control; this does not create a centralized Merchant government.
- Dialogue/state-only B2 missions terminate with `decline`; `accept` is reserved for mission paths that create actual gameplay objectives.

## Validation

Pending repository-native branch validation:

- `Fork simulation and story validation`
- `Fork save-load integration smoke`

Promote to READY only if both required workflows are terminal green on an exact production/validator candidate. Do not claim build/save-load success before that evidence exists.

## A3 / B3 integration notes

Review the exact candidate SHA and branch ancestry against current `main` before integration. Preserve every existing state name/value and the A1 read-only boundary. The expected production diff is lifecycle-only (`accept` -> `decline` on six positive state-only terminals); validator/handoff changes are acceptance infrastructure.
