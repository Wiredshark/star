# B2 Pug Uncertainty Protocol handoff — 2026-08-19

## Verdict
PARTIAL pending exact-head repository-native simulation/story/style and save-load/build validation.

## Authority and isolation
- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Repository: `Wiredshark/star`
- Authoritative `main` observed at run start: `ebb1398d1b911fa38806e03aa9eb91cad755a935`
- B1 dependency branch: `agent/b1-pug-contact-memory-20260819-1218`
- B1 dependency exact head: `4a3a61d36a3401946e8401963691866b47680de4`
- B2 isolated branch: `agent/b2-pug-uncertainty-protocol-20260819-1226`
- Production commit: `859101d7c8dfffde83b3587e58e21c0e0c7518f8`
- Focused validator commit: `19bff050dd6091551b97451e5b44a0eb43730f24`

B2 must not self-integrate. A3 owns integration.

## Character / dynamic-content behavior
This slice consumes B1's Pug Contact Testimony Archive and turns its central epistemic problem into a persistent character dispute on Deneb.

Two recurring human specialists are referred to only by the player's private shorthand:
- **Archivist** — prioritizes witness provenance, sensor evidence, and the distinction between observation and interpretation.
- **Interpreter** — prioritizes usable contact guidance, translation context, confidence, and competing hypotheses.

These are not canonical names, formal titles, or new offices.

Initial routes:
1. observation-first — operational records stop where verification stops;
2. interpretation-first — best interpretation is allowed but must carry confidence and alternatives;
3. paired record — immutable observations remain separate from revisable interpretation;
4. refusal — B2 records refusal and does not schedule the delayed Review.

A delayed Review exposes the second-order problem: uncertainty fields are often lost when reports are copied between crews and agencies. The player then chooses one of two terminal settlements:
- **provenance ladder** — every claim carries a portable chain back through observation, interpretation, confidence, and revision;
- **uncertainty envelope** — any exported conclusion about Pug intent must carry confidence, alternatives, and an explicit warning when motive cannot be established.

`Archivist Remembers` is a one-shot later reader of either terminal settlement.

## Dependencies / canon invariants
- Requires `main plot completed`.
- Requires `Pug Contact Testimony Archive: offered` from the B1 dependency.
- Remains scoped to Neutral Deneb.
- Does not assert why the Pug invaded, withdrew, waited, helped, or acted in any specific way.
- Preserves B1's distinction between observed Pug behavior and guessed human motive.
- Does not invent internal Pug government, history, names, titles, or institutions.
- All persistent writes are namespaced `B2 Pug Uncertainty Protocol:*`.
- No `world:*`, credits, reputation, cargo, outfit, ship, fleet, combat, main-plot, or B1-state writes.

## Files
- `data/pug/b2 pug uncertainty protocol.txt`
- `tools/story/validate_b2_pug_uncertainty_protocol.py`
- `story/B2_PUG_UNCERTAINTY_PROTOCOL_HANDOFF_20260819.md`

## Validation intended
Focused validator:
`python3 tools/story/validate_b2_pug_uncertainty_protocol.py "data/pug/b2 pug uncertainty protocol.txt"`

Repository-wide story/simulation/style workflow must also pass on the exact final head. The focused validator checks:
- exact three-mission structure;
- delayed Review event and no Review scheduling on refusal;
- private Archivist/Interpreter shorthand;
- Neutral Deneb + post-main-plot + B1 archive gating;
- three persistent routes plus refusal;
- exactly two terminal settlements;
- one-shot aftermath reader;
- B2-only persistent mutation surface;
- local goto/label integrity;
- contact-uncertainty continuity concepts;
- guard against unsupported Pug-motive assertions.

Save-load/build workflow must also complete successfully before READY promotion. Runtime acceptance should confirm offer gating, all three routes, refusal negative path, delayed Review, both terminal settlements, aftermath one-shot behavior, and persistence across save/reload.

## Host/process boundary
The exposed private execution host was inspected at the start of this run. Its repository workspace is `Wiredshark/fallout-test`, not `Wiredshark/star`, and it was already dirty. It was left untouched and is not used as Endless Sky validation evidence.

## A3 / B3 integration notes
Integration order: B1 Pug contact-memory history first, then B2 Pug Uncertainty Protocol.

A3 must re-read current `main` because concurrent work is expected. Do not integrate if the exact-head repository-native validation fails, if B1's dependency is not accepted, or if continuity review finds that the slice accidentally turns an interpretation of Pug intent into established fact.

B3 should preserve the distinction between:
- what was observed;
- what was translated or inferred;
- how confident that inference was;
- what later revisions changed.
