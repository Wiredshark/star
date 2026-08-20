# B2 Acheron Observation Provenance — Handoff

## Verdict

PARTIAL pending repository-native simulation/story/style and production build/save-load validation on the exact B2 head.

## Dependency and branch

- Required B1 parent branch: `agent/b1-acheron-lifeform-history-20260820-0221`
- Required B1 parent SHA: `e8078b8f4f514ab64fbbe5b4359cd5118200c53e`
- B2 branch: `agent/b2-acheron-observation-provenance-20260820-0328`
- Production commit: `aa8175c53b2b0764b0729c73c4c7162e6e2d8792`
- Focused-validator commit: `e24a4d1541aff40814cc8925fa8b5554fade3b0c`

## Implemented slice

B2 converts the Acheron/Vyrmeid natural-history evidence discipline into a persistent player-facing character arc between field observer Nira Sol and survey pilot Tomas Pell.

The first encounter distinguishes passive baseline observation from controlled ship-induced stimulus. Three substantive player routes persist: baseline-first, stimulus-first with exact human-action context, or paired baseline/stimulus evidence. Refusal does not enter the later review chain.

The Review addresses downstream evidence degradation: copied biological summaries can preserve observed response while losing the human maneuver, environment, source lineage, or uncertainty that made the observation interpretable. It resolves into one of two terminal models:

1. a portable provenance packet carrying baseline, stimulus, environment, timing, source lineage, and uncertainty;
2. an evidence ladder separating passive observation, controlled response, relayed report, inference, and contradiction.

`Sol Remembers` is the one-shot later reader.

## Continuity and ownership invariants

- Direct observation is not identical to human-elicited response.
- Biological hazard is not hostile motive.
- Responsiveness is not proof of communication or intention.
- Repeated copies of one source are not independent observations.
- Every persistent write is namespaced under `B2 Acheron Observation Provenance:*`.
- B2 does not write `world:*`, credits, reputation, cargo, outfits, ships, fleets, combat state, or B1 history state.
- The slice requires existing `Rulei: Umbral Reach: offered` access and thematically depends on the B1 Acheron natural-history archives.

## Files

- `data/vyrmeid/b2 acheron observation provenance.txt`
- `tools/story/validate_b2_acheron_observation_provenance.py`
- `story/B2_ACHERON_OBSERVATION_PROVENANCE_HANDOFF_20260820.md`

## Required acceptance before READY

Run on the exact final B2 head:

- `python3 tools/story/validate_b2_acheron_observation_provenance.py "data/vyrmeid/b2 acheron observation provenance.txt"`
- repository-wide focused story validator discovery / story repository validation
- A1 state-ownership/simulation contracts
- changed-content style validation
- normal Endless Sky production configure/build
- stock save/load integration smoke, including conversation save/load cases

Do not claim any gate passed until its exact-head result is terminal green.

## A3 / B3 integration notes

Integrate or otherwise accept the B1 Acheron natural-history parent first. Preserve the evidence hierarchy rather than simplifying the final records into generalized Vyrmeid motive claims. If later B3 continuity work sees another Acheron/Iije/Rulei observation arc, keep their scopes distinct: this slice is specifically about Acheron/Vyrmeid field-observation provenance and copied biological summaries.
