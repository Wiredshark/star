# A2 Republic Resettlement Council current-main hardening handoff

Verdict: PARTIAL pending exact-head repository-native validation.

## Authority
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-republic-resettlement-council-restage-20260824-0219`
- Production hardening: `4c8b40feacc4733324fe7710ed1944fde51df648`
- Strengthened validator: `d69fb4dffd7f3cf163a7bb195490685842799194`

## Why this slice
The Republic Resettlement Council production content and focused validator are already integrated on authoritative `main`, but the integrated production file predates the current repository content-style header convention and its refusal follow-up relied on implicit branch fallthrough. This isolated A2 hardening repairs those two weaknesses without changing A1 ownership, player policy choices, thresholds, or positive outcome semantics.

## RPG / dynamic narrative loop
At authoritative A1 `world: republic displacement pressure >= 2`, Lena Orr asks the player to prioritize family unity, employment continuity, distributed placement, or refusal. A2 persists only that player policy memory. After A1 displacement pressure later recovers below 2, each positive policy is combined with current A1 `world: republic border pressure >= 4` versus `< 4`, yielding six history-aware outcomes. Refusal is remembered and explicitly respected.

## Hardening changes
- Adds the repository-standard GPL content header.
- Makes the refusal follow-up an explicit `branch refused` + `has "A2 Republic Resettlement Council: refused"` + `label refused` path instead of relying on fallthrough after all positive branches.
- Strengthens the focused validator to require both missions, both `offer precedence 9` declarations, all four initial routes, six positive after-action outcomes, explicit refusal gating, five `decline` terminals, zero state-only `accept` endpoints, no gameplay-objective directives, and no writes to A1-owned world state.

## Ownership / persistence invariants
- A1 remains sole writer of `world: republic displacement pressure`.
- A1 remains sole writer of `world: republic border pressure`.
- A1 remains sole writer of `world: republic resettlement surge`.
- All A2 writes remain under `A2 Republic Resettlement Council:*`.
- Existing condition names and positive-route meanings are preserved for save compatibility.
- Refusal remains refusal; it is not silently converted into policy endorsement.
- State-only dialogue terminals use `decline` and do not create objective-less accepted missions.
- No Republic office, enforcement authority, or representative mandate is granted to the player.

## Process / workspace boundary
The exposed private process service reported four pre-existing service-owned processes. Its `repository-workspace` remote is `Wiredshark/fallout-test`, not `Wiredshark/star`, and the workspace was already dirty. It was left untouched and is not used as Endless Sky runtime evidence.

## Validation boundary
No exact-head GitHub workflow result is claimed yet. A3 must not integrate until `Fork simulation and story validation` and `Fork save-load integration smoke` are terminal green on the exact candidate head. If either fails, repair this isolated branch rather than weakening the gate.

## A3 integration guidance
Re-read authoritative `main`, verify ancestry/mergeability, preserve A1 ownership and A2 namespace/lifecycle semantics, and integrate only after exact-head validation is green. Do not self-integrate from A2.
