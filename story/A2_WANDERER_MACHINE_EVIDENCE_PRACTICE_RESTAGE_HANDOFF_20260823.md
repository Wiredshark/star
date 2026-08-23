# A2 Wanderer Machine Evidence Practice — current-main restage handoff

**Stage:** A2 CORE RPG + DYNAMIC NARRATIVE

**Verdict:** PARTIAL pending exact-head repository-native validation.

**Authoritative base:** `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`

**Branch:** `agent/a2-wanderer-machine-evidence-practice-restage-20260823-0302`

**Production restage:** `f60f894d236359e519cc0511dce7b24e200862c4`

**Strengthened validator:** `cf7292ece01169a9bf5cf1c61fe1e32d36c2b3cd`

Historical PARTIAL PR #125 remains untouched.

## Implemented loop

Consumes integrated `B2 Wanderer Machine Custody Compact: aftermath seen` read-only. The player persistently chooses provenance-with-derivatives, independent challenge tied to source evidence, local-only interpretation, or explicit refusal. Each positive route drives an explicitly gated one-shot later Reflection; refusal does not arm Reflection.

The loop preserves the distinction between source evidence and derivatives: copied or reconstructed results remain useful, but their transformations, missing regions, uncertainty, and disagreement must not silently disappear. Independent agreement on a safe operating limit does not automatically validate an inferred cause.

## Current architecture / invariants

- B2 custody state is read-only.
- No `world:*` state is written.
- All persistent writes are `A2 Wanderer Machine Evidence Practice:*`.
- Both state-only missions use `offer precedence 9`.
- All five objective-less terminal paths use `decline`; no state-only `accept` remains.
- Reflection rechecks B2 aftermath and explicitly gates provenance, challenge, and local-only routes.
- Refusal is persistent but does not arm Reflection.
- Curator and Engineer remain player-private shorthand, not Wanderer offices or titles.
- No definitive Mereti/Sestor directive, Builder intent, universal machine motive, Wanderer mandate, or representative authority is asserted.
- Existing condition names and route meanings are preserved for save compatibility; absent A2 conditions remain the default for older saves.

## Files

- `data/wanderer/a2 wanderer machine evidence practice.txt`
- `tools/story/validate_a2_wanderer_machine_evidence_practice.py`
- `story/A2_WANDERER_MACHINE_EVIDENCE_PRACTICE_RESTAGE_HANDOFF_20260823.md`

## Validation status

Repository-native exact-head story/simulation/style and production build/save-load workflows must be terminal green before promotion to READY. No manual actual-game acceptance is claimed in this restage.

## A3 integration boundary

Do not self-integrate. A3 should re-read current `main`, verify ancestry and mergeability, and preserve B2/world read-only ownership, explicit route gating, refusal suppression, offer precedence 9, the state-only `decline` lifecycle, and the no-Wanderer-authority boundary.
