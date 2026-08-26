# B2 Skadenga Living Vow Compact — Handoff

Verdict: **READY for A3 review/integration**.

## Authority and isolation
- Repository: `Wiredshark/star`
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-skadenga-living-guidance-compact-20260826`
- Production commit: `5251a2d42701295d29f970e62f889db7a2ea6bd9`
- Focused-validator commit: `e9c9d64ac8dbf64f74800632de4f6906fa652dbb`
- Exact fully validated production/validator/handoff candidate: `42f8328d3c29680c97250cf674f74a560a6e7548`
- No self-integration.

## Character/content behavior
Three-mission state-only character arc following the canonical Skadenga migration arrangements:
1. `The Vow After the Journey` — Hjlod and Runa disagree over whether Runa's migration-era spiritual vow can be treated as a permanent pathfinder assignment.
2. `When the Copy Becomes the Calling` — a copied roster preserves the old words but silently turns them into current work authority.
3. `Runa Remembers` — one-shot aftermath showing the chosen settlement in practice.

Player approaches:
- preserve the vow as attributed spiritual history while requiring present consent for current assignment;
- allow a living speaker to renew or reinterpret the vow without rewriting the older wording;
- maintain paired sacred-memory/current-duty records;
- refusal, which does not introduce the arc or schedule Review.

Review is scheduled once after 7–11 days on each substantive route and resolves to either:
- `settlement vow context`; or
- `settlement living recommitment`.

## Dependencies and ownership
Read-only dependency:
- `Home for Skadenga 4: done`.

Writes only `B2 Skadenga Living Vow Compact:*` conditions.
No writes to vanilla Skadenga state, `world:*`, A1/A2/B1 state, credits, reputation, cargo, equipment, ships, fleets, combat, or government attitudes.

All seven dialogue/state-only terminal paths use `decline`; zero `accept` terminals. No objective-bearing mission directives are present.

## Exact acceptance evidence
On exact candidate `42f8328d3c29680c97250cf674f74a560a6e7548`:
- Fork simulation and story validation #655 / run `32938543784`: **SUCCESS**
  - focused Python compilation: SUCCESS
  - all focused story validators: SUCCESS
  - A1 simulation/state-ownership contracts: SUCCESS
  - changed-content style: SUCCESS
- Fork save-load integration smoke #640 / run `32938543706`: **SUCCESS**
  - dependency installation: SUCCESS
  - production configuration: SUCCESS
  - production build: SUCCESS
  - stock save-load smoke: SUCCESS

## Canon/persistence assumptions
- Hjlod remains the canonical Skadenga character from the migration arc.
- Runa is a new individual Skadenga, not a formal office or universal representative.
- The slice does not decide Skadenga theology. It treats one person's vow, remembered interpretations, and current practical duty as distinct facts.
- Refusing a present work assignment must not be treated as evidence that Runa rejected her faith.
- Preserving the original vow must not make it a permanent labor assignment.
- No save migration is required because this is additive, namespaced state.

## Files
- `data/human/b2 skadenga living vow compact.txt`
- `tools/story/validate_b2_skadenga_living_vow_compact.py`
- `story/B2_SKADENGA_LIVING_VOW_COMPACT_HANDOFF_20260826.md`

## A3/B3 integration notes
Re-read current main and open B1/A2/B2 work immediately before integration. Preserve the distinction among exact historical words, attributed interpretation, spiritual meaning, current consent, current duty, renewal, and closure. A living vow may remain meaningful without becoming a permanent staffing order or universal Skadenga law.
