# B2 Syndicate Parts Provenance Compact — Handoff

Verdict: **READY for A3 review/integration**.

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative integration base observed for this slice: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-syndicate-parts-provenance-20260821-0124`
- Production commit: `ffa50167331b0a224f44b11c770bd65b091cdf86`
- Focused-validator commit: `1438a495ed6e79ce91ac1e46f78f3665c71f247a`
- Exact fully validated production/validator/handoff candidate: `49d5954ec40e0d98b1c8006478d5bfc7bf84a986`
- B2 does not self-integrate.

## Slice

Adds **B2 Syndicate Parts Provenance Compact**, a character/dynamic-content sequel to the Syndicate replacement-stock provenance history and a read-only consumer of A1's `world: syndicate parts scarcity` signal.

Characters:

- **Tessa Marr** — reuses the existing A2 Syndicate maintenance coordinator and gives her a second, distinct operational concern: whether a scarce substitute can safely be used without flattening its uncertainty into a broad compatibility label.
- **Ren Vale** — procurement controller focused on supplier history, repairs, substitutions, test basis, and downstream provenance.

The Offer appears while A1 parts scarcity is high (`>= 3`) and supports three substantive routes plus refusal:

1. provenance-first use;
2. bounded emergency operational qualification;
3. paired immutable provenance + installation-specific qualification;
4. refusal.

The Review appears only after A1 naturally recovers parts scarcity to `<= 1`. It resolves to exactly one of two terminal models:

- **portable qualification packet** — supplier/repair provenance, substitutions, test method/conditions, installation context, duty limits, and unresolved uncertainty travel together;
- **expiry and revalidation** — prior evidence remains useful, but a material repair, different equipment family, changed duty cycle, or changed operating assumption reopens qualification.

`Vale Remembers` is the one-shot later reader.

## Ownership and continuity invariants

- A1 is the sole writer of `world: syndicate parts scarcity`; B2 only reads it.
- Every new persistent write is namespaced `B2 Syndicate Parts Provenance Compact:*`.
- No direct credits, reputation, cargo, outfit, ship, fleet, or combat mutation.
- This does **not** duplicate A2 maintenance triage: A2 decides which work should be prioritized during a surge; this B2 slice concerns evidence attached to replacement components.
- This does **not** duplicate B2 Syndicate Qualification Compact: that slice concerns transferable worker qualifications; this one concerns component provenance and installation-specific qualification.
- A compatibility label is not proof of universal equivalence.
- A successful emergency installation is evidence about that installation, not automatic proof that the same component is equivalent under every later system, duty cycle, temperature, control package, or repair state.
- Supplier provenance, repair/substitution history, test evidence, installation-specific qualification, uncertainty, and later revalidation are distinct facts.
- Practical record sharing among participating yards does not establish a centralized Syndicate procurement authority or universal law.
- Dialogue-only terminal paths use `decline` after writing persistent state, avoiding objective-less accepted missions.

## Files

- `data/human/b2 syndicate parts provenance compact.txt`
- `tools/story/validate_b2_syndicate_parts_provenance_compact.py`
- `story/B2_SYNDICATE_PARTS_PROVENANCE_COMPACT_HANDOFF_20260821.md`

## Validation

Focused validator covers:

- exactly three missions;
- both named characters;
- high/low A1 scarcity gates;
- A1 read-only ownership;
- three substantive routes plus refusal;
- exactly two terminal settlements;
- B2-only persistent writes;
- no direct material/reputation mutation;
- local `goto` / `label` integrity;
- B1 provenance/substitution/compatibility continuity concepts;
- bounded rather than universal equivalence;
- dialogue-only lifecycle uses `decline`, not `accept`.

On exact candidate `49d5954ec40e0d98b1c8006478d5bfc7bf84a986`, repository-native validation is terminal green:

- `Fork simulation and story validation` run #303 / `32450668197`: **SUCCESS**.
- `Fork save-load integration smoke` run #288 / `32450668198`: **SUCCESS**.

Those workflows provide the repository-native story/simulation/style gate and the production build/save-load integration smoke gate required for READY. This final commit changes only the durable handoff wording; production content and validator behavior are unchanged from the exact fully validated candidate.

## A3 / B3 integration notes

A3 should re-read current `main` before integration because the integration branch may advance while this specialist branch is under validation. If ancestry remains clean, integrate the focused B2 slice through the normal A3 authority path. Do not infer that the draft PR authorizes B2 to self-integrate.

B3 should preserve the core distinction:

> A part that physically fits and worked once is not automatically equivalent everywhere. Provenance, substitutions, test conditions, operating assumptions, uncertainty, and installation-specific qualification must not collapse into one copied `compatible` label.
