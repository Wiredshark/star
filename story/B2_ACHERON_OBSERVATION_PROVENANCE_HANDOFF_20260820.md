# B2 Acheron Observation Provenance — Handoff

## Verdict

READY for A3 review/integration.

The original B2 slice is now additionally repaired for dialogue lifecycle: all state-only terminal branches close with `decline`, preventing objective-less accepted missions from lingering. The focused validator enforces that invariant.

## Authority, dependency, and branch

- Current authoritative `main` observed during this recovery run: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Required B1 parent branch: `agent/b1-acheron-lifeform-history-20260820-0221`
- Required B1 parent SHA: `e8078b8f4f514ab64fbbe5b4359cd5118200c53e`
- B2 branch: `agent/b2-acheron-observation-provenance-20260820-0328`
- Original READY handoff head: `1bc6213e6832d43ca505654f427c340cc0a4ed75`
- Dialogue-lifecycle production repair: `04e2667a715989e69aa08b0735c60ce4a03a82ac`
- Lifecycle validator hardening / exact fully validated candidate: `3810419152773fa0c1420c12c69d47b0c3aed5be`

The lifecycle candidate is historically diverged from current `main`: compare against current authority reported 8 commits ahead / 61 behind with merge base `95fdb069b0a56d990f75a59b0c44fe9d6401038d`. GitHub still reports PR #155 mergeable, but A3 must re-read current-main ancestry and reconcile the required B1 dependency before integration.

## Implemented slice

B2 converts the Acheron/Vyrmeid natural-history evidence discipline into a persistent player-facing character arc between field observer Nira Sol and survey pilot Tomas Pell.

The first encounter distinguishes passive baseline observation from controlled ship-induced stimulus. Three substantive player routes persist: baseline-first, stimulus-first with exact human-action context, or paired baseline/stimulus evidence. Refusal does not enter the later review chain.

The Review addresses downstream evidence degradation: copied biological summaries can preserve observed response while losing the human maneuver, environment, source lineage, or uncertainty that made the observation interpretable. It resolves into either a portable provenance packet or an evidence ladder separating passive observation, controlled response, relayed report, inference, and contradiction. `Sol Remembers` is the one-shot later reader.

## Dialogue-lifecycle repair

These three missions only persist story state and do not create gameplay objectives. The production repair changes the three positive Offer terminals, two Review settlements, and `Sol Remembers` aftermath terminal from `accept` to `decline`. Refusal already used `decline`, so all 7 terminal paths now close cleanly.

No dialogue, route, settlement, trust state, condition name/value, source gate, canon boundary, or material-state behavior changed.

The focused validator now requires:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no destination, stopover, waypoint, NPC, cargo, passenger, deadline, or timer directive that would invalidate the state-only lifecycle assumption;
- all prior route, settlement, ownership, mutation-surface, provenance, uncertainty, and `goto`/`label` checks.

## Continuity and ownership invariants

- Direct observation is not identical to human-elicited response.
- Biological hazard is not hostile motive.
- Responsiveness is not proof of communication or intention.
- Repeated copies of one source are not independent observations.
- Every persistent write is namespaced under `B2 Acheron Observation Provenance:*`.
- B2 does not write `world:*`, credits, reputation, cargo, outfits, ships, fleets, combat state, or B1 history state.
- The slice requires existing `Rulei: Umbral Reach: offered` access and thematically depends on the B1 Acheron natural-history archives.
- Dialogue/state-only B2 missions terminate with `decline`; `accept` is reserved for mission paths that actually create gameplay objectives.

## Files

- `data/vyrmeid/b2 acheron observation provenance.txt`
- `tools/story/validate_b2_acheron_observation_provenance.py`
- `story/B2_ACHERON_OBSERVATION_PROVENANCE_HANDOFF_20260820.md`

## Validation evidence

Exact lifecycle-repair candidate: `3810419152773fa0c1420c12c69d47b0c3aed5be`

- `Fork simulation and story validation` #457 / run `32620426186`: SUCCESS.
- Focused story validators, including the hardened Acheron lifecycle validator: SUCCESS.
- A1 simulation/state-ownership contracts: SUCCESS.
- Changed-content style: SUCCESS.
- `Fork save-load integration smoke` #442 / run `32620426050`: SUCCESS.
- Production configure/build: SUCCESS within the green save-load workflow.
- Stock save/load integration smoke: SUCCESS within the green save-load workflow.

## A3 / B3 integration notes

Integrate or otherwise accept the B1 Acheron natural-history parent first. Re-read current authoritative `main` because this historical branch is substantially behind current integration state even though GitHub reports it mergeable. Preserve the evidence hierarchy rather than simplifying copied records into generalized Vyrmeid motive claims. If later B3 continuity work sees another Acheron/Iije/Rulei observation arc, keep scopes distinct: this slice is specifically about Acheron/Vyrmeid field-observation provenance and copied biological summaries.
