# B2 Quarg Cross-Generation Promise — handoff

**Stage:** B2 STORY CHARACTERS + DYNAMIC CONTENT  
**Verdict:** READY for A3 review/integration  
**Authoritative base:** `a17a89fb4779200a0634a6dade1811c4dc9cc2be`  
**Branch:** `agent/b2-quarg-cross-generation-promise-20260824`  
**Production commit:** `7fa95c1c2c2aa00d018bacf5b5be76f9ba2cb2b2`  
**Focused validator commit:** `afaa43370ffe824698a2cd7e301150020616003c`  
**Exact fully validated production/validator/handoff candidate:** `b03246bdc79455ac39055b251ca5e8b9fe5541d6`

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
Current main, recent commits, recent/open B2 PRs, Quarg B2 branches, handoff files, and the active global B2 dialogue-lifecycle audit were inspected before authoring. Existing Quarg B2 work concerns stewardship boundaries; no Quarg intergenerational-friendship/promise slice was active. Four pre-existing service-owned host processes were observed and preserved; no cleanup or unrelated process action was performed. The exposed private host is not used as Endless Sky runtime evidence.

## Files
- `data/quarg/b2 quarg cross generation promise.txt`
- `tools/story/validate_b2_quarg_cross_generation_promise.py`
- `story/B2_QUARG_CROSS_GENERATION_PROMISE_HANDOFF_20260824.md`

## Validation
The focused validator checks the exact three-mission graph, Quarg first-contact/source gates, three substantive routes plus refusal, 7–11 day Review scheduling, refusal suppression, both settlements, one-shot aftermath, B2-only writes, seven `decline` terminals, absence of gameplay-objective/material directives, local `goto`/`label` integrity, and the historical-promise versus present-authority boundary.

On exact candidate `b03246bdc79455ac39055b251ca5e8b9fe5541d6`:
- `Fork simulation and story validation` run `32762967269` / #554: **SUCCESS**;
- focused story validators including the new Quarg validator: **SUCCESS**;
- A1 simulation/state-ownership contracts: **SUCCESS**;
- changed-content style: **SUCCESS**;
- `Fork save-load integration smoke` run `32762967226` / #539: **SUCCESS**;
- production configure/build: **SUCCESS**;
- stock save-load integration smoke: **SUCCESS**.

Exact base-to-candidate comparison is 3 commits ahead / 0 behind, exactly three added files, 368 additions, and 0 deletions. This READY promotion changes only this durable handoff; production and validator behavior remain identical to the fully green candidate.

## Risks / deferred work
No save-state migration is required because the slice is additive and namespaced. The principal integration risk is semantic overgeneralization: A3/B3 must not turn one personal Quarg-human promise into hereditary Quarg obligation, contract law, or a Quarg office.

## A3 / B3 integration notes
A3 retains integration authority; B2 must not self-integrate. Re-read current `main`, active B2/A2/B1 work, ancestry, mergeability, and exact workflow state immediately before integration. Preserve `Old Friend` as private shorthand and keep remembered relationship, attributed words, current consent, current obligation, fulfillment, and closure distinct.
