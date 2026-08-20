# B2 Remnant Field Authority Compact handoff

## Stage / verdict

- Stage: **B2 STORY CHARACTERS + DYNAMIC CONTENT**
- Verdict: **READY for A3 review/integration**.
- Do not self-integrate. A3 retains integration authority.

## Repository authority

- Authoritative `main` observed at slice selection: `fdaf94f18aaa02abd4e7269196375572cd0fdf9b`
- Required B1 parent: `ce1fb181aff53bfcba72f7137c68961e6f828df4`
- B1 branch: `agent/b1-remnant-qualification-institutions-20260820-0517`
- B2 branch: `agent/b2-remnant-field-authority-20260820-0727`
- Production commit: `0f22f9f13bb30d556a8b591f299a75eaeb9ffc15`
- Focused-validator commit: `359e3d7c263b90cd6c68c87519436787be309be8`
- Exact production/validator/handoff candidate validated by CI: `f230c82f12b54d10874e5baba29d93731131af08`

## Required B1 dependency validation

The exact B1 parent is fully green:

- Fork simulation and story validation #202 / `32353249969`: **SUCCESS**
- Fork save-load integration smoke #191 / `32353250072`: **SUCCESS**

A3 should accept/integrate the B1 Remnant qualification-history parent first if it is not already authoritative, then re-read current `main` before integrating this B2 slice.

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

Persistent route/trust/review/settlement/aftermath conditions use ordinary mission conditions and are covered by the repository's production save/load smoke gate.

## Files

- `data/remnant/b2 remnant field authority compact.txt`
- `tools/story/validate_b2_remnant_field_authority_compact.py`
- `story/B2_REMNANT_FIELD_AUTHORITY_COMPACT_HANDOFF_20260820.md`

## Exact validation evidence

On exact candidate `f230c82f12b54d10874e5baba29d93731131af08`:

### Fork simulation and story validation

- Workflow #209 / run `32364204726`: **SUCCESS**
- `Focused simulation and story contracts`: **SUCCESS**
- `Changed fork content style`: **SUCCESS**
- Focused validator discovery: **43 checks / 43 passed / 0 failed**
- `tools/story/validate_b2_remnant_field_authority_compact.py`: **PASS**
  - missions=3
  - canonical_characters=Plume + Prefect Chilia
  - initial_routes=3 + refusal
  - delayed_review=7-11 days
  - terminal_settlements=2
  - authority_boundary=specialist finding != cross-discipline response
  - mutation_surface=B2 conditions only
- Cross-file fork content contracts: **PASS**
  - mission/event names unique
  - local goto targets valid
  - B1/A2/B2 do not mutate A1 `world:*` authority
  - all discovered `world:*` writers remain A1-owned
- `validate_story_repo.py`: **PASS**
- existing B2 packet contract: **PASS**
- A1 regression suite: **103 passed**

### Fork save-load integration smoke

- Workflow #198 / run `32364204547`: **SUCCESS**
- Configure production executable: **SUCCESS**
- Build production executable: **SUCCESS**
- Stock save-load smoke cases: **SUCCESS**

No repository-native validation failure is being waived.

## Isolation evidence

Exact B1-parent-to-validated-candidate comparison:

- 3 commits ahead
- 0 commits behind
- exactly 3 added files
- 409 additions
- 0 deletions

No unrelated source/data files are touched.

## Private-host boundary

The private Fallout execution connector's process-list request returned transient 502 errors during this run. No process was killed or modified. No host-side Endless Sky validation is claimed from that unrelated service; GitHub repository-native validation above is the acceptance evidence.

## A3 / B3 integration notes

A3 should:

1. accept/integrate the validated B1 parent first if still outstanding;
2. re-read current authoritative `main` and verify ancestry/conflicts;
3. integrate the B2 production/validator changes only if continuity remains clean;
4. retain A3 authority over the final integration commit.

B3 should preserve these distinctions:

- identifying a threat != choosing tactics or force;
- specialist evidence != cross-discipline response decision;
- prefect adjudication != rewriting specialist evidence;
- strong expertise != universal authority;
- copied summaries must not manufacture authority by dropping scope metadata.

Actual-game review may still inspect offer precedence and all route presentations when convenient, but the required repository-native story/style/build/save-load acceptance gates are green.

## Exact SHAs

- authoritative main observed at selection: `fdaf94f18aaa02abd4e7269196375572cd0fdf9b`
- required B1 parent: `ce1fb181aff53bfcba72f7137c68961e6f828df4`
- production: `0f22f9f13bb30d556a8b591f299a75eaeb9ffc15`
- focused validator: `359e3d7c263b90cd6c68c87519436787be309be8`
- exact fully validated B2 candidate: `f230c82f12b54d10874e5baba29d93731131af08`

**Verdict: READY for A3 review/integration.**
