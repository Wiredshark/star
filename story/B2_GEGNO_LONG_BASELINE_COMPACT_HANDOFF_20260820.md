# B2 Gegno Long-Baseline Compact handoff

## Stage / verdict

- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Verdict: PARTIAL pending exact-head repository-native workflows
- Integration authority: A3 only; this branch must remain isolated/unmerged

## Repository authority

- Authoritative `main` observed at slice selection: `afde12845a8426df9e39edea0b6f58d10ef2c9e7`
- Required B1 parent: `2a9dfc0a8d2aa9cf1aed57d05fbb905da7128695`
- Isolated branch: `agent/b2-gegno-long-baseline-compact-20260820-1125`
- Production commit: `4edace914f301251aa318cb2e3cde7742feeaf0c`
- Focused-validator commit: `4d5da1d3942a8f5a9acbe929c6b1656b8698f4b5`

## B1 dependency

B1 `Gegno Environmental Observation` is the direct content dependency. It establishes:

- Ghneoe long-baseline seasonal ecology records;
- Cyife crystal survey provenance and preservation of failed/negative observations;
- sand-beast field records that separate observed behavior from inferred territory/intelligence/ritual meaning;
- long-lived instruments whose measurements can outlast uncertain ownership.

Exact B1 head `2a9dfc0a8d2aa9cf1aed57d05fbb905da7128695` has terminal-green repository-native validation:

- Fork simulation and story validation run `32363546416`: SUCCESS
- Fork save-load integration smoke run `32363546411`: SUCCESS

## B2 character/dynamic-content slice

Adds `data/gegno/b2 gegno long baseline compact.txt`.

Two recurring Gegno specialists are presented through player-private shorthand, **Archive Keeper** and **Pathfinder**, explicitly not as formal Gegno offices. Their disagreement is how short field expeditions should update long environmental records without turning either old patterns or fresh observations into unquestioned truth.

Initial persistent routes:

1. **baseline first** — preserve the long series as reference; add fresh observations as visible exceptions until repeated evidence supports a lasting change;
2. **current layer** — update operational warnings quickly, but carry observation date, method, and confidence;
3. **paired layers** — keep a long-baseline series and a current operational layer linked by explicit contradictions;
4. refusal — no later settlement chain.

The delayed Review identifies the downstream copy problem: conclusions can survive while observation date, survey method, historical baseline, source lineage, uncertainty, or contradiction is lost.

Terminal settlements:

- **observation packet** — every operational warning carries observation date, method, source lineage, modified baseline, uncertainty, and review trigger;
- **expiry register** — temporary operational conclusions expire unless renewed, while unresolved contradictions remain durable evidence until reconciled.

`Keeper Remembers` is the one-shot aftermath reader.

## Ownership / canon invariants

- All writes are under `B2 Gegno Long-Baseline Compact:*`.
- B1 state, A1 `world:*`, credits, reputation, cargo, outfits, ships, fleets, and combat state are untouched.
- Archive Keeper / Pathfinder are player-private shorthand, not canonical titles or evidence of a centralized Gegno scientific bureaucracy.
- A short field observation may be real and operationally important without proving a permanent environmental change.
- A long baseline may be statistically useful without being allowed to erase a contradictory current hazard.
- Dangerous sand-beast behavior is not converted into claims of intelligence, territory, or ritual meaning.
- Old-instrument measurements remain evidence even when ownership is uncertain.
- Practical cross-faction evidence records do not imply Vi/Scin political unification.

## Validation surface

Focused validator added:

`python3 tools/story/validate_b2_gegno_long_baseline_compact.py`

It checks:

- exact 3-mission graph + delayed Review event;
- B1 environmental continuity concepts;
- 3 substantive routes + refusal;
- exactly 2 terminal settlements;
- one-shot aftermath reader;
- Tschyss source scope;
- local `goto` / `label` integrity;
- B2-only condition writes;
- absence of material/reputation mutations;
- preservation of observation/context/inference boundaries.

Required before READY:

- exact-head Fork simulation and story validation: SUCCESS;
- exact-head changed-content style: SUCCESS;
- focused validator discovery/execution: SUCCESS;
- exact-head Fork save-load integration smoke: SUCCESS;
- production configure/build + stock save/load smoke: SUCCESS.

## A3 / B3 integration notes

A3 should integrate/accept B1 `2a9dfc0a...` first if it is not already present, then re-read current `main` before considering this B2 branch. Preserve normal A3 integration authority.

B3 should preserve the central distinction among long-baseline pattern, current field observation, temporary operational warning, copied conclusion, uncertainty, and unresolved contradiction. Repeated copies of a short observation must not become independent evidence or permanent environmental truth.
