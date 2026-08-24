# B2 Quarg Cross-Generation Promise — handoff

**Stage:** B2 STORY CHARACTERS + DYNAMIC CONTENT  
**Verdict:** PARTIAL pending exact-head repository-native validation  
**Authoritative base:** `a17a89fb4779200a0634a6dade1811c4dc9cc2be`  
**Branch:** `agent/b2-quarg-cross-generation-promise-20260824`  
**Production commit:** `7fa95c1c2c2aa00d018bacf5b5be76f9ba2cb2b2`  
**Focused validator commit / current candidate:** `afaa43370ffe824698a2cd7e301150020616003c`

## Scope
Adds a local Quarg/human intergenerational friendship arc grounded in established Quarg longevity canon. Jules Sorel is the adult grandson of Mira Sorel; the recurring Quarg is called `Old Friend` only in the player's private notes. Mira's remembered request that the Quarg look after her family after she is gone becomes a dispute over whether a personal promise can become hereditary obligation.

Player routes:
- historical promise + explicit living-party renewal;
- bounded family continuity through specific present requests;
- paired historical-promise and current-agreement records;
- refusal.

The three substantive routes schedule a Review after 7–11 days. Review resolves into either a portable promise history or renewal by living parties. `Jules Remembers` is the one-shot aftermath reader.

## Ownership / lifecycle
- reads only established `First Contact: Quarg: offered`;
- all writes are `B2 Quarg Cross-Generation Promise:*`;
- no `world:*`, B1/A1/A2, credits, reputation, cargo, equipment, ship, fleet, or combat mutation;
- all seven dialogue/state-only terminal paths use `decline`;
- refusal does not arm Review;
- `Old Friend` is player-private shorthand, not a Quarg title or office.

## Canon / continuity
Quarg first-contact canon explicitly establishes that Quarg live for many human lifetimes and make friends among younger species. This slice does not define Quarg inheritance law, family law, contract law, or a new Quarg bureaucracy. It keeps family memory, historical promise, current consent, present obligation, later fulfillment, and explicit closure separate. Repetition cannot fill in unknown intent or manufacture current authority.

## Concurrency / process boundary
Current main, recent B2 PRs, Quarg B2 branches, and the active global B2 dialogue-lifecycle audit were inspected before authoring. Existing Quarg B2 work concerns stewardship boundaries; no Quarg intergenerational-friendship/promise slice was active. Four pre-existing service-owned host processes were observed and preserved; no cleanup or unrelated process action was performed.

## Files
- `data/quarg/b2 quarg cross generation promise.txt`
- `tools/story/validate_b2_quarg_cross_generation_promise.py`
- `story/B2_QUARG_CROSS_GENERATION_PROMISE_HANDOFF_20260824.md`

## Validation contract
The focused validator checks the exact three-mission graph, Quarg first-contact/source gates, three substantive routes plus refusal, 7–11 day Review scheduling, refusal suppression, both settlements, one-shot aftermath, B2-only writes, seven `decline` terminals, absence of gameplay-objective/material directives, local `goto`/`label` integrity, and the historical-promise versus present-authority boundary.

Repository-native `Fork simulation and story validation` and `Fork save-load integration smoke` must both be terminal green on the exact candidate before this handoff is promoted to READY.

## A3 / B3 integration notes
A3 retains integration authority; B2 must not self-integrate. Re-read current `main`, active B2/A2/B1 work, ancestry, mergeability, and exact workflow state immediately before integration. Preserve `Old Friend` as private shorthand and keep remembered relationship, attributed words, current consent, current obligation, fulfillment, and closure distinct.
