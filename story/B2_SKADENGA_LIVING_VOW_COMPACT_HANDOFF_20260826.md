# B2 Skadenga Living Vow Compact — Handoff

Verdict: **PARTIAL** pending repository-native validation.

## Authority and isolation
- Repository: `Wiredshark/star`
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-skadenga-living-guidance-compact-20260826`
- Production commit: `5251a2d42701295d29f970e62f889db7a2ea6bd9`
- Focused-validator commit: `e9c9d64ac8dbf64f74800632de4f6906fa652dbb`
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

## Canon/persistence assumptions
- Hjlod remains the canonical Skadenga character from the migration arc.
- Runa is a new individual Skadenga, not a formal office or universal representative.
- The slice does not decide Skadenga theology. It treats one person's vow, remembered interpretations, and current practical duty as distinct facts.
- Refusing a present work assignment must not be treated as evidence that Runa rejected her faith.
- Preserving the original vow must not make it a permanent labor assignment.
- No save migration is expected because this is additive, namespaced state.

## Files
- `data/human/b2 skadenga living vow compact.txt`
- `tools/story/validate_b2_skadenga_living_vow_compact.py`
- `story/B2_SKADENGA_LIVING_VOW_COMPACT_HANDOFF_20260826.md`

## Required acceptance before READY
- repository-native Fork simulation/story validation, including focused validators and changed-content style;
- A1 state-ownership/simulation contracts;
- production Endless Sky configure/build;
- stock save-load integration smoke;
- exact final diff/status/ancestry recheck.

## A3/B3 integration notes
Preserve the distinction among exact historical words, attributed interpretation, spiritual meaning, current consent, current duty, renewal, and closure. A living vow may remain meaningful without becoming a permanent staffing order or universal Skadenga law.
