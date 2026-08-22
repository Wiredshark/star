# B2 Pug Uncertainty Protocol handoff — 2026-08-22 lifecycle recovery

## Verdict
PARTIAL pending terminal-green exact-head repository-native simulation/story/style and save-load/build validation for this recovered candidate, plus terminal-green save-load validation of the required B1 Pug contact-memory dependency.

## Authority and isolation
- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Repository: `Wiredshark/star`
- Current authoritative `main` recovered on 2026-08-22: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- B1 dependency branch: `agent/b1-pug-contact-memory-20260819-1218`
- B1 dependency exact head: `4a3a61d36a3401946e8401963691866b47680de4`
- B2 isolated branch: `agent/b2-pug-uncertainty-protocol-20260819-1226`
- Original production commit: `859101d7c8dfffde83b3587e58e21c0e0c7518f8`
- Original focused validator commit: `19bff050dd6091551b97451e5b44a0eb43730f24`
- Original candidate/handoff head: `62e92811dc07ea4a20a850a9f6e13fc6f300f25e`
- Dialogue-lifecycle production repair: `57a4d3d83ba98e24f15f87b3b92b13e3fb5e2d4b`
- Lifecycle validator hardening: `707fe8604ad7d558627acfed52d50765406064bf`

B2 must not self-integrate. A3 owns integration.

## Recovery rationale
The original draft PR #100 had been idle since 2026-08-19. Its exact-head simulation/story workflow had succeeded, while its old save-load workflow was later observed as cancelled rather than green. No competing open Pug lifecycle-repair PR existed when this recovery pass began.

Inspection found a concrete gameplay-lifecycle defect in the production slice: the three positive Offer routes, two Review settlements, and `Archivist Remembers` aftermath path all persisted state and then used terminal `accept`, even though these missions create no gameplay objective. Refusal already used `decline`.

The recovery repair changes exactly those six objective-less positive terminal commands from `accept` to `decline`. All seven state-only terminal paths now persist the same story state and close cleanly. No dialogue, route, settlement, trust, source scope, condition name/value, B1 dependency, or Pug epistemic/canon semantics changed.

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
- Repeated or copied interpretations do not become independent evidence merely by repetition.

## Dialogue lifecycle invariant
These three missions are dialogue/state-only. They do not create a destination, stopover, waypoint, NPC objective, cargo/passenger objective, deadline, or timer.

Therefore:
- terminal `accept` count must be **0**;
- terminal `decline` count must be **7**;
- all state-only paths must write persistence and close cleanly with `decline`;
- `accept` is reserved for mission lifecycles that actually create gameplay objectives.

The focused validator now enforces this lifecycle invariant in addition to the original structural, continuity, and ownership checks.

## Files
- `data/pug/b2 pug uncertainty protocol.txt`
- `tools/story/validate_b2_pug_uncertainty_protocol.py`
- `story/B2_PUG_UNCERTAINTY_PROTOCOL_HANDOFF_20260819.md`

## Validation requirements
Focused validator:
`python3 tools/story/validate_b2_pug_uncertainty_protocol.py "data/pug/b2 pug uncertainty protocol.txt"`

Repository-wide simulation/story/style and save-load/build workflows must both pass on the exact recovered candidate before READY promotion.

The focused validator checks:
- exact three-mission structure;
- delayed Review event and no Review scheduling on refusal;
- private Archivist/Interpreter shorthand;
- Neutral Deneb + post-main-plot + B1 archive gating;
- three persistent routes plus refusal;
- exactly two terminal settlements;
- one-shot aftermath reader;
- 0 terminal `accept`, exactly 7 terminal `decline`, and no gameplay-objective directives;
- B2-only persistent mutation surface;
- local goto/label integrity;
- contact-uncertainty continuity concepts;
- guard against unsupported Pug-motive assertions.

Runtime acceptance should confirm offer gating, all three substantive routes, refusal negative path, delayed Review timing, both terminal settlements, aftermath one-shot behavior, and persistence across save/reload.

## Historical and current workflow evidence
Original B2 candidate `62e92811dc07ea4a20a850a9f6e13fc6f300f25e`:
- `Fork simulation and story validation` run `32276193898` / #101: SUCCESS.
- `Fork save-load integration smoke` run `32276193893` / #90: CANCELLED, not a PASS.

Required B1 dependency `4a3a61d36a3401946e8401963691866b47680de4`:
- simulation/story run `32275607631` / #100: SUCCESS.
- historical save-load run `32275607634` / #89: CANCELLED; a fresh rerun was requested during this recovery pass and must reach terminal green before integration.

Do not mark READY based only on the old simulation/story success. The lifecycle-repaired exact head must receive fresh repository-native validation.

## Host/process boundary
The previously exposed private execution host was inspected in the original work and is not an authoritative `Wiredshark/star` workspace. No unrelated host process/worktree is modified or used as Endless Sky validation evidence in this recovery pass.

## A3 / B3 integration notes
Integration order: B1 Pug contact-memory history first, then B2 Pug Uncertainty Protocol.

A3 must re-read current `main`, verify ancestry/mergeability, confirm required B1 validation, and integrate only if the exact lifecycle-repaired B2 candidate is terminal green.

B3 should preserve the distinction between:
- what was observed;
- what was translated or inferred;
- how confident that inference was;
- what source lineage produced it;
- what later revisions changed.

Copies of one interpretation remain one evidence lineage; repeated copying must not manufacture corroboration.
