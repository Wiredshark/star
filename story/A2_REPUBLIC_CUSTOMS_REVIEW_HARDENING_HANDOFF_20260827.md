# A2 Republic Customs Review current-main hardening handoff

Verdict: PARTIAL pending exact-head repository-native validation.

## Authority and isolation

- Authoritative integration base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`.
- Branch: `agent/a2-republic-customs-review-hardening-20260827-1607`.
- Production hardening: `6d4eeda7548cf7726121121812e7e6f824962997`.
- Strengthened focused validator: `8fc6bc85e5d2295f1894beee41b8055a8224f45e`.
- No self-integration. A3 retains integration authority.

## Player-facing loop

The existing staged RPG loop is preserved without renaming persistent conditions:

`A1 Republic customs scrutiny >= 3 -> player chooses bounded audit / written basis / underworld context / formal process -> A1 scrutiny recovers below 3 -> route-specific disposition -> later consent choice for bounded precedent use versus keeping the case private`.

The initial review still reads current Republic border pressure for framing and repeated pirate-job history for the optional underworld-context response.

## Production hardening

- Added the canonical 2026 Endless Sky GPL content header.
- Preserved every existing `A2 Republic Customs Review:*` save-state name and value.
- Made the formal-process disposition route explicit with its own branch and label instead of relying on fallthrough.
- Made the refusal-preserved later-reader route explicit with its own branch and label instead of relying on fallthrough.
- Added explicit convergence for the contextualized-routing disposition and later-reader context/private routes.
- No narrative outcome, threshold, or authority ownership moved.

## Ownership and persistence invariants

- A1 remains sole writer of `world: republic customs scrutiny` and `world: republic border pressure`.
- `pirate jobs` remains read-only.
- All persistent writes remain under `A2 Republic Customs Review:*`.
- Existing downstream conditions such as `later reader seen`, `precedent use bounded`, and `precedent kept private` remain save-compatible.
- Both bounded-precedent consent and private-precedent refusal semantics are preserved.
- No credits, reputation, cargo, outfits, ships, fleet, combat, destination, waypoint, NPC, timer, or objective mutations are introduced.
- All three dialogue-only missions retain `offer precedence 9`.
- State-only terminals remain `decline`; no objective-less `accept` is introduced.

## Validator hardening

The focused validator now proves:

- exact three-mission order and Republic scope;
- exact four initial routes and four route-specific disposition outcomes;
- explicit formal-process/refusal routing rather than accidental fallthrough;
- exact later-reader routing for all four outcomes;
- both precedent choices and explicit convergence;
- six state-only `decline` terminals and zero `accept` terminals;
- A1 and pirate-history inputs are read-only;
- all assignments are confined to the A2 customs-review namespace;
- no gameplay/material/objective directives;
- canonical GPL header and trailing newline;
- local goto targets resolve.

## Validation boundary

Repository-native pull-request workflows have not yet been observed on the final branch tip. Do not claim simulation/story/style, production build, or save-load success until exact-head runs are terminal green.

## A3 instructions

Before integration, re-read current `main`, verify branch ancestry and mergeability, and require both repository-native acceptance workflows to be terminal green on the exact candidate head. Preserve all existing condition names because multiple downstream A2/B2 consumers use this customs-review state.
