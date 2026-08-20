# B2 Remnant Field Authority Compact handoff

## Stage / verdict

- Stage: **B2 STORY CHARACTERS + DYNAMIC CONTENT**
- Current verdict: **PARTIAL** pending exact-head repository-native simulation/story/style and production save-load validation.
- Do not self-integrate. A3 retains integration authority.

## Repository authority

- Authoritative `main` observed at slice selection: `fdaf94f18aaa02abd4e7269196375572cd0fdf9b`
- Required B1 parent: `ce1fb181aff53bfcba72f7137c68961e6f828df4`
- B1 branch: `agent/b1-remnant-qualification-institutions-20260820-0517`
- B1 exact-head repository-native validation is now green:
  - Fork simulation and story validation #202 / `32353249969`: SUCCESS
  - Fork save-load integration smoke #191 / `32353250072`: SUCCESS
- B2 branch: `agent/b2-remnant-field-authority-20260820-0727`
- Production commit: `0f22f9f13bb30d556a8b591f299a75eaeb9ffc15`
- Focused-validator commit: `359e3d7c263b90cd6c68c87519436787be309be8`

## Scope

Adds a three-mission persistent character arc using existing canonical characters **Plume** and **Prefect Chilia** after the player has already encountered Chilia in the Cognizance chain.

The arc consumes B1's Remnant qualification/authority history and deepens the established Cognizance authority model: a qualified specialist can identify a danger or bind decisions inside that specialist field, but the designation does not automatically decide tactics, routing, resource allocation, engineering, quarantine scale, or other cross-discipline responses.

### Offer — `A Threat Is Not an Order`

A biological hazard in a mixed research/patrol/courier corridor has been formally designated a threat by Plume. A copied summary is being treated as though the designation itself ordered a closure. Plume and Chilia disagree over how to preserve the warning's force without allowing domain-specific expertise to become universal authority.

The player may choose:

1. **authority map** — every designation carries its qualified field, binding scope, excluded decisions, and next required authority;
2. **prefect adjudication** — specialist recommendations stay separate and the cross-discipline priority decision is recorded as a distinct adjudication;
3. **paired record** — bounded specialist finding plus a separate response record naming routing/force/logistics/engineering/review owners;
4. **refusal** — preserve the disagreement without creating a standing compact.

The three substantive routes schedule Review after 7–11 days. Refusal does not schedule Review.

### Review — `When the Warning Becomes the Order`

Downstream summaries begin collapsing evidence, qualified authority, and response decisions into one inherited claim. The player resolves this into exactly one of two persistent settlements:

- **portable authority packet** — every copied conclusion carries evidence owner, qualified domain, binding scope, excluded decisions, response owner, review point, and unresolved objections;
- **layered ledger** — specialist findings remain immutable evidence records while cross-discipline response decisions remain separately revisable and cite, rather than absorb, those findings.

### Aftermath — `Plume Remembers`

A one-shot later reader demonstrates that a prefect or response owner can change what the Remnant do without retroactively changing what a qualified specialist observed or concluded inside that field.

## Dependencies / continuity

- Requires `Remnant: Cognizance 4: done`, avoiding any pre-emption of Chilia's established introduction.
- Requires B1 `Remnant Qualification Ledger Archive: offered`.
- Uses canonical Plume/Chilia authority semantics already explained in `Remnant: Cognizance 2`.
- Preserves the merged Remnant hierarchy rather than inventing a separate military/civilian bureaucracy.
- Preserves field-specific competence: authority in one specialty does not automatically transfer into another.
- Preserves prefect adjudication as cross-discipline priority judgment, not omniscience or permission to rewrite specialist evidence.
- Does not establish a new Remnant constitution, office, universal form, or command structure.

## State ownership / persistence

All writes are namespaced under `B2 Remnant Field Authority Compact:*`.

The slice does **not** write:

- B1 Remnant qualification-history state;
- Cognizance campaign state;
- any `world:*` simulation state;
- credits or reputation;
- cargo/outfit/ship/fleet/combat state.

Persistent route/trust/review/settlement/aftermath conditions are ordinary mission conditions intended to survive save/load using the engine's normal persistence model.

## Files

- `data/remnant/b2 remnant field authority compact.txt`
- `tools/story/validate_b2_remnant_field_authority_compact.py`
- `story/B2_REMNANT_FIELD_AUTHORITY_COMPACT_HANDOFF_20260820.md`

## Focused validator

`tools/story/validate_b2_remnant_field_authority_compact.py` checks:

- exact three-mission graph;
- canonical Plume + Prefect Chilia presence;
- post-Cognizance and B1 gating;
- three substantive routes plus refusal;
- 7–11 day Review scheduling only on substantive routes;
- exactly two terminal settlements;
- one-shot aftermath state;
- local goto/label integrity;
- B2-only write ownership;
- no material/reputation/world-state mutation;
- specialist-evidence / bounded-authority / cross-discipline-response continuity invariants.

## Validation state

Before integration, require repository-native validation on the exact final B2 head:

1. `Fork simulation and story validation` — must be terminal SUCCESS.
2. `Fork save-load integration smoke` — must be terminal SUCCESS.
3. If CI exposes a validator/content-style defect, repair the candidate and re-run on the repaired exact head rather than integrating around the failure.

Actual-game A3/B3 acceptance should also confirm when practical:

- Offer does not appear before `Remnant: Cognizance 4: done` and the B1 qualification archive gate;
- all three positive routes persist through save/reload;
- refusal does not schedule Review;
- Review waits for its delayed event;
- both terminal settlements persist and remain mutually exclusive;
- aftermath is one-shot;
- nearby Remnant mission offer precedence remains sane.

## A3 / B3 integration notes

Integration order: accept/integrate the validated B1 Remnant qualification-history parent first if it is not already authoritative, then re-read current `main` and integrate this B2 branch only if ancestry and continuity remain clean.

B3 should preserve these distinctions:

- identifying a threat != choosing tactics or force;
- specialist evidence != cross-discipline response decision;
- prefect adjudication != rewriting specialist evidence;
- strong expertise != universal authority;
- copied summaries must not manufacture authority by dropping scope metadata.

## Current exact SHAs

- authoritative main observed: `fdaf94f18aaa02abd4e7269196375572cd0fdf9b`
- required B1 parent: `ce1fb181aff53bfcba72f7137c68961e6f828df4`
- production: `0f22f9f13bb30d556a8b591f299a75eaeb9ffc15`
- focused validator: `359e3d7c263b90cd6c68c87519436787be309be8`

Current verdict remains **PARTIAL** until both exact-head B2 repository-native workflows are terminal green.
