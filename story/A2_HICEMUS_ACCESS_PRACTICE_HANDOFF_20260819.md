# A2 Hicemus Access Practice handoff

- Authoritative base: `main@5928089939e8dc7806deb2775a9030a3ba5bf9bb`
- Branch: `agent/a2-hicemus-access-practice-20260819-1906`
- Production commit: `c4bad57e1be57bb85441f8f42083c90656c4921f`
- Validator commit: `32faf8866642b6f26a5cf38d48d4d6be965f3c3d`
- Verdict: PARTIAL until exact-head repository CI and actual-game acceptance complete.

## Loop

Consumes `B2 Hicemus Access Compact: aftermath seen` and its terminal settlement read-only. The player chooses a bounded-record, interaction-first, local-only, or refusal practice. A later one-shot reflection demonstrates a distinct consequence for each persisted route.

## Invariants

B2 remains sole writer of B2 access-compact state. A2 writes only `A2 Hicemus Access Practice:*`; no `world:*` writes. Dispatcher/Maintainer remain player-private shorthand. The player gains no Hicemus office, credential, endorsement, linguistic authority, or representative authority.

## Validation

Focused validator is committed at `tools/story/validate_a2_hicemus_access_practice.py`. No execution result is claimed in this handoff until a workflow or suitable checkout actually runs it.

## A3 integration gates

Require exact-head story/simulation/style validation, build/save-load smoke, actual-game B2-aftermath gating, all four initial routes and later reflections, save/reload between stages, one-shot suppression, and Incipias/Hicemus offer-precedence regression. Do not integrate on PARTIAL.
