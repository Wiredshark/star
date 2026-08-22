# B2 Sheragi Context Compact Lifecycle Restage Handoff — 2026-08-22

## Verdict

READY for A3 review/integration.

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative `main` base recovered at run start: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Restage branch: `agent/b2-sheragi-context-lifecycle-20260822-1626`
- Original stalled B2 PR: #124 / head `c494b53bca6ec89ed6f3f8e230cfb2fe55df1b48`
- Exact fully validated current-main production/validator/handoff candidate: `d6deccc02dfa88e6420e54557adb52b9aec79962`
- Original PR #124 is closed as superseded.
- This branch is a clean current-main restage rather than a destructive rewrite of the old branch.
- B2 does not self-integrate; A3 retains integration authority.

## Character / dynamic-content behavior

`B2 Sheragi Context Compact` preserves the original three-mission Nadia Rell / Ivo March arc:

1. `The Wall and the Weather` — emergency preservation versus excavation/site-context loss.
2. `A Reconstruction Without a Site` — copied reconstructions losing the boundary between measurement, context, inference, and later interpretation.
3. `Nadia Remembers` — one-shot aftermath demonstrating the selected settlement.

Persistent initial approaches remain emergency shelter/removal, context-first survey, paired preservation/context records, or refusal. Review outcomes remain portable context packet or reversible reconstruction.

## Lifecycle repair

The original candidate used terminal `accept` on six positive dialogue/state-only paths even though these missions create no destination, cargo, NPC, timer, waypoint, passenger, or other gameplay objective. This restage changes those six terminals to `decline`; refusal already declined. All seven terminal paths now write the same persistent state as before and close cleanly.

The focused validator enforces:

- zero terminal `accept` commands;
- exactly seven `decline` terminals;
- no objective-bearing mission directives;
- the existing mission graph, routes, settlements, B2-only state writes, one-shot aftermath, local goto/label integrity, mutation guards, and Sheragi evidence/interpretation continuity boundaries.

## Canon / persistence assumptions

- Nadia Rell and Ivo March remain contemporary human researchers, not claims about ancient Sheragi social structure.
- The arc remains gated behind the existing Sheragi archaeology epilogue plus B1 Evidence Provenance and Site Context institutional-history offers.
- All writes remain under `B2 Sheragi Context Compact:*`.
- No `world:*`, B1, credits, reputation, cargo, ship, fleet, combat, or other material state is mutated.
- No persistent condition names or values changed from the original B2 candidate; no save-state migration is required.
- Object, excavation context, later conservation change, reconstruction, interpretation, and unresolved uncertainty remain distinct facts.

## Validation

Original stalled head `c494b53bca6ec89ed6f3f8e230cfb2fe55df1b48` eventually passed both historical workflows, confirming the original content semantics:

- Fork simulation and story validation #143 / `32313220657`: SUCCESS
- Fork save-load integration smoke #132 / `32313220731`: SUCCESS

On exact current-main restage candidate `d6deccc02dfa88e6420e54557adb52b9aec79962`:

- Fork simulation and story validation #425 / `32596789536`: SUCCESS
- Fork save-load integration smoke #410 / `32596789549`: SUCCESS

The restage is exactly 3 commits ahead / 0 behind its selected authoritative base before this READY-handoff-only update and changes only three files: production content, focused validator, and this durable handoff.

## A3 / B3 guidance

A3 should integrate this current-main restage rather than old PR #124. Do not integrate both. Re-read current `main` immediately before integration and confirm ancestry remains clean.

B3 should preserve the core evidence boundary: a conserved physical artifact is not the same thing as its excavation context; a reconstruction is not direct evidence; downstream copies must not erase uncertainty or silently convert interpretation into original Sheragi fact.
