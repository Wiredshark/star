# B2 Iije Field Observation Compact handoff — lifecycle recovery 2026-08-23

## Verdict
READY for A3 review/integration after the validated B1 dependency is accepted or reconciled.

## Authority and isolation
- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Repository: `Wiredshark/star`
- Current authoritative `main` rechecked before recovery: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Required historical B1 dependency branch: `agent/b1-iije-natural-history-20260820-0016`
- Required B1 dependency exact head: `f118ed2e50c31ab03b5658af89907f81783e8b7d`
- B1 dependency validation: simulation/story #172 SUCCESS; save-load #161 SUCCESS
- B2 isolated branch: `agent/b2-iije-field-observation-20260820-0027`
- Original production commit: `2f29e159ce6315e4b3a6d0ff0426bde85b46edda`
- Original validated candidate before lifecycle recovery: `fe1069471bfb90d04a93ae0e50a8023b175fd393`
- Lifecycle production repair: `c08a8479e4c1e060e86d84e2f5a1c98b87eb088d`
- Lifecycle validator hardening / exact fully validated candidate: `1ef5e1323b364d54a8b9369b8563f3dac23ca45e`

B2 must not self-integrate. A3 owns integration.

## Character / dynamic-content behavior
The slice remains the same persistent Iije field-science character arc. Two recurring human specialists are identified only through the player's private shorthand:
- **Observer** — a field biologist who prioritizes baseline conditions and unprovoked behavior.
- **Pilot** — an expedition pilot who wants controlled tests that answer practical navigation questions.

These remain player-private shorthand, not canonical names, formal titles, offices, credentials, or representative authority.

Initial routes remain:
1. **passive** — natural/baseline observation first; interventions create an explicit boundary in the record;
2. **stimulus** — controlled light trials are allowed, but every response remains labeled stimulus-elicited;
3. **paired** — baseline observation and measured stimulus trial remain linked but separately identifiable;
4. **refusal** — the player declines to define a protocol and no Review is scheduled.

Each substantive route still schedules a delayed Review after 7–11 days. The Review still resolves to exactly one of:
- **stimulus provenance packet** — ambient conditions, human intervention, instrument limits, timing, and unresolved uncertainty travel with observations;
- **reversible field model** — predictions remain replaceable interpretations over separately preserved baseline observations and stimulus trials.

`Pilot Remembers` remains the one-shot aftermath reader.

## Lifecycle recovery
The original three missions are dialogue/state-only. They create no destination, cargo, NPC, waypoint, timer, passenger, deadline, or other gameplay objective, but six positive terminal paths used `accept`:
- three Offer routes;
- two Review settlements;
- the `Pilot Remembers` aftermath.

That could leave objective-less accepted missions active after conversation completion.

Commit `c08a8479e4c1e060e86d84e2f5a1c98b87eb088d` changes only those six positive terminal commands from `accept` to `decline`. The refusal path already used `decline`, so all **7/7 state-only terminal paths** now persist the same existing story state and close cleanly.

No dialogue, route, settlement, trust condition, delayed-event timing, persistence name/value, source location, B1 gate, or canon assumption changed.

## Validator hardening
Commit `1ef5e1323b364d54a8b9369b8563f3dac23ca45e` extends `tools/story/validate_b2_iije_field_observation_compact.py` to require:
- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no gameplay-objective directives in this state-only slice.

All previous checks remain, including:
- exact three-mission graph;
- three substantive routes plus refusal;
- exactly three 7–11 day Review schedules and none on refusal;
- exactly two terminal settlements;
- one-shot aftermath;
- B2-only writes;
- no `world:*` or material/reputation/combat mutation;
- local `goto` / `label` integrity;
- Midgard/Mirrorlake and B1 gating;
- Observer/Pilot private-shorthand continuity;
- baseline/stimulus/provenance/uncertainty concepts;
- guards against unsupported Iije motive claims.

## Ownership / canon invariants
- Requires `Rulei: Umbral Reach: offered`.
- Requires B1 `Iije History: Stellar Feeding Survey: offered`.
- All persistent writes remain `B2 Iije Field Observation Compact:*`.
- No `world:*`, credits, reputation, cargo, outfit, ship, fleet, combat, Rulei campaign, or B1-state writes.
- Bright work lights may alter Jje movement without proving hostility, curiosity, communication, intent, or any other motive.
- The slice does not invent Iije language, society, politics, motive, or a directly observed Jje-to-Ayym transformation.
- Baseline/spontaneous behavior remains distinct from behavior elicited by human intervention.
- A copied conclusion does not become stronger evidence merely because stimulus parameters or evidence limitations were dropped.

## Files
- `data/rulei/b2 iije field observation compact.txt`
- `tools/story/validate_b2_iije_field_observation_compact.py`
- `story/B2_IIJE_FIELD_OBSERVATION_COMPACT_HANDOFF_20260820.md`

## Exact lifecycle-recovery validation
On exact candidate `1ef5e1323b364d54a8b9369b8563f3dac23ca45e`:
- `Fork simulation and story validation` run `32645633825` / #486: **SUCCESS**.
- focused story validators, including the hardened Iije lifecycle validator: **SUCCESS**.
- A1 simulation/state-ownership contracts: **SUCCESS**.
- changed-content style: **SUCCESS**.
- `Fork save-load integration smoke` run `32645633834` / #471: **SUCCESS**.
- production configure/build: **SUCCESS**.
- stock save-load smoke: **SUCCESS**.

No manual actual-game acceptance is claimed beyond repository-native production build/save-load and structural/state-ownership validation.

## Process / concurrency safety
Before recovery, live `main`, recent/open B2 work, and the existing Iije branch were inspected. No competing Iije lifecycle repair was active. The existing Iije branch was advanced rather than duplicating its scope.

The private service process inventory reported four pre-existing service-owned processes. None were killed or modified.

## A3 / B3 integration notes
This is a historical B2 branch whose original dependency chain predates current authoritative `main`. A3 must re-read current `main`, verify ancestry/mergeability, and reconcile/accept B1 Iije natural-history institutions before or with this B2 slice as appropriate. Do not infer readiness solely from GitHub's mergeable flag.

Preserve the distinction among:
- baseline/spontaneous behavior;
- human-elicited response;
- environmental and instrument context;
- downstream interpretation/prediction;
- uncertainty and contradiction.

Preserve the lifecycle invariant that dialogue/state-only B2 missions close with `decline`; reserve `accept` for paths that create actual gameplay objectives.
