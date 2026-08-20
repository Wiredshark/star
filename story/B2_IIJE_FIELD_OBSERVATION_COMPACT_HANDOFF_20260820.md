# B2 Iije Field Observation Compact handoff — 2026-08-20

## Verdict
READY for A3 review/integration after the validated B1 dependency is accepted.

## Authority and isolation
- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Repository: `Wiredshark/star`
- Authoritative `main` observed at run start and rechecked before final handoff: `85ecbd74ba8fdff055d5151707c3550b24e915e2`
- Required B1 dependency branch: `agent/b1-iije-natural-history-20260820-0016`
- Required B1 dependency exact head: `f118ed2e50c31ab03b5658af89907f81783e8b7d`
- B1 dependency validation: repository-native simulation/story workflow #172 SUCCESS; save-load workflow #161 SUCCESS
- B2 isolated branch: `agent/b2-iije-field-observation-20260820-0027`
- Production commit: `2f29e159ce6315e4b3a6d0ff0426bde85b46edda`
- Initial focused validator commit: `f0be82db3bd34863d6cb6a4777e1d133cd65b9bf`
- Validator repair / exact fully validated production+validator candidate: `fe1069471bfb90d04a93ae0e50a8023b175fd393`

B2 must not self-integrate. A3 owns integration.

## Character / dynamic-content behavior
This slice consumes B1's Iije natural-history records and turns the B1 Stellar Feeding Survey's navigation/science tension into a persistent character dispute.

Two recurring human specialists are identified only through the player's private shorthand:
- **Observer** — a field biologist who prioritizes baseline conditions and unprovoked behavior.
- **Pilot** — an expedition pilot who wants controlled tests that answer practical navigation questions.

These are not canonical names, formal titles, new offices, or new institutional authority.

Initial routes:
1. **passive** — natural/baseline observation first; interventions create an explicit boundary in the record;
2. **stimulus** — controlled light trials are allowed, but every response must remain labeled stimulus-elicited;
3. **paired** — baseline observation and measured stimulus trial remain linked but separately identifiable;
4. **refusal** — the player declines to define a protocol; B2 records refusal and schedules no Review.

Each substantive route schedules a delayed Review after 7–11 days.

The Review exposes the second-order problem that copied navigation/science summaries can preserve the observed reaction while dropping the conditions that caused or constrained it. The player chooses one of two terminal settlements:
- **stimulus provenance packet** — every behavioral observation carries ambient conditions, human intervention, instrument limits, timing, and unresolved uncertainty;
- **reversible field model** — predictions/interpretations remain replaceable layers over separately preserved baseline observations and stimulus trials.

`Pilot Remembers` is the one-shot later reader of either terminal settlement.

## Dependencies / canon invariants
- Requires `Rulei: Umbral Reach: offered`.
- Requires B1 `Iije History: Stellar Feeding Survey: offered`.
- Offer and Review are on Midgard; aftermath is on Mirrorlake, both locations already used by B1 Iije natural-history content.
- Preserves B1's distinction between observed Iije behavior and inferred purpose.
- Preserves the fact that bright work lights can alter Jje movement without turning attraction to light into evidence of hostility, curiosity, communication, or intent.
- Does not invent Iije language, society, motives, political structure, or a directly witnessed Jje-to-Ayym transformation.
- Observer/Pilot remain player-private shorthand.
- All persistent writes are namespaced `B2 Iije Field Observation Compact:*`.
- No `world:*`, credits, reputation, cargo, outfit, ship, fleet, combat, Rulei campaign, or B1-state writes.

## Files
- `data/rulei/b2 iije field observation compact.txt`
- `tools/story/validate_b2_iije_field_observation_compact.py`
- `story/B2_IIJE_FIELD_OBSERVATION_COMPACT_HANDOFF_20260820.md`

## Exact validation evidence
The first repository-native simulation/story run on head `28ad9e832b2674af0d336c2ee6ef9922ea76eda1` correctly failed because the focused validator compared one recurring-character continuity phrase case-sensitively. Production content was not at fault. The validator was repaired in `fe1069471bfb90d04a93ae0e50a8023b175fd393` to evaluate those phrases case-insensitively; no production behavior changed in that repair.

On exact candidate `fe1069471bfb90d04a93ae0e50a8023b175fd393`:
- `Fork simulation and story validation` run #174 / `32332184100`: SUCCESS.
- changed fork content style: SUCCESS.
- focused simulation and story contracts: SUCCESS.
- all discovered focused story validators, including `validate_b2_iije_field_observation_compact.py`: SUCCESS.
- A1 simulation/state-ownership contract tests: SUCCESS.
- `Fork save-load integration smoke` run #163 / `32332184098`: SUCCESS.
- production configure/build: SUCCESS.
- stock save-load smoke cases: SUCCESS.

The focused validator covers:
- exact three-mission graph;
- delayed Review and no Review scheduling on refusal;
- Observer/Pilot private-shorthand continuity;
- Midgard/Mirrorlake and B1 gating;
- three persistent routes plus refusal;
- exactly two terminal settlements;
- one-shot aftermath reader;
- B2-only persistent mutation surface;
- local goto/label integrity;
- baseline/stimulus/provenance/uncertainty concepts;
- guards against unsupported Iije motive claims.

Actual-game acceptance can still exercise offer precedence and presentation, but the repository-native production build/save-load and focused structural/state-ownership gates are green on the exact candidate.

## Concurrency / non-overlap
Live `main`, recent PRs, and the full discovered `agent/b2-*` inventory were inspected before selection. No existing Iije-specific B2 branch was present. Existing Rulei/Pug/Ka'het and other xenobiology/evidence B2 slices focus on contact testimony, translation, machine provenance, or route evidence; this candidate is specifically about experimental intervention in living-Iije observation and the operational consequences of losing stimulus context.

The latest B1 Iije candidate was checked before B2 authoring. Both exact B1 repository-native workflows are green, so this B2 slice is based on a validated dependency even though A3 has not yet integrated that B1 branch into `main`.

## A3 / B3 integration notes
Integration order: B1 Iije natural-history institutions first, then B2 Iije Field Observation Compact.

A3 must re-read current `main` because concurrent work is expected. Integrate/reconcile the exact validated candidate `fe1069471bfb90d04a93ae0e50a8023b175fd393` plus this final handoff-only commit, or equivalently preserve the production and validator commits in order and rerun integrated-head validation if ancestry changes.

B3 should preserve the distinction among:
- baseline/spontaneous behavior;
- behavior elicited by human light or other intervention;
- instrument limitations and environmental context;
- downstream interpretation/prediction;
- unresolved uncertainty.

A copied behavioral conclusion must not become more certain merely because the stimulus parameters or evidence limitations were dropped.
