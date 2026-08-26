# B2 Republic Former Smuggler Cooperation Compact — Handoff

LOOP_ID: B2
RUN_TYPE: CONTENT
PRIMARY_DOMAIN: crime / investigation / law
SECONDARY_DOMAINS: personal history, redemption, current consent, evidence provenance
RECENT_DOMAIN_WINDOW: confidential teaching/privacy; career/family; stewardship/authority
DIVERSITY_STATUS: PASS
CONCENTRATION_JUSTIFICATION: N/A
NEGLECTED_AREA_ADVANCED: crime/investigation character content
CROSS_SYSTEM_CONNECTION: A1 Republic customs scrutiny + Republic border pressure + built-in pirate-job RPG history

## Authority and isolation

- Repository authority: `Wiredshark/star`
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-republic-former-smuggler-cooperation-20260826`
- Production commit: `5f704e6f6013153e3aff6136a7404544f7c047cb`
- Initial focused validator commit: `a51cb7510aa5b7416842e35c480d43d7a6488aaa`
- Validator wording hardening / exact fully validated production+validator candidate: `34358a1ee9c4f0836164169619d34b1832b3a4de`
- Verdict: **READY for A3 review/integration**.
- No integration performed; A3 retains integration authority.

## Character/content behavior

Introduces Republic customs investigator **Rhea Markel** and former smuggler **Davin Sorn** on Earth.

Davin's history contains two distinct true facts: he once smuggled contraband and he once cooperated with a specific investigation that later closed. Under elevated Republic border/customs pressure, downstream copies repeatedly turn that closed history into current "active source" status or standing suspicion.

Offer approaches:

1. **Completed history** — preserve old offense/cooperation as history without treating either as present informant duty or present suspicion.
2. **Fresh agreement** — permit new case-specific cooperation only through a current request with scope, terms, and closure.
3. **Paired status** — keep historical offense/cooperation distinct from current evidence and current cooperation status.
4. **Refusal** — decline to turn one former smuggler's file into a wider office rule; does not arm Review.

All three substantive routes persist distinct state and schedule `Review Ready` after 7–11 days.

Review resolves into exactly two persistent settlements:

- **fresh cause** — active suspicion or active-source status needs a current case-specific basis rather than repetition of old labels;
- **bounded cooperation** — a current cooperation relationship carries case, requested scope, actual promises, responsible investigator, review point, and explicit closure.

`Davin Remembers` consumes either settlement once.

## Inputs and ownership

Read-only inputs:

- built-in `pirate jobs >= 3` RPG history;
- A1-owned `world: republic customs scrutiny >= 3`;
- A1-owned `world: republic border pressure >= 3`.

Writes only `B2 Republic Former Smuggler Cooperation Compact:*`.

No `world:*`, A1/A2/B1, pirate-job, credit, reputation, cargo, equipment, ship, fleet, combat, or government-attitude writes.

All seven dialogue/state-only terminal paths use `decline`; zero `accept`; no mission objective directives are present.

## Files

- `data/human/b2 republic former smuggler cooperation compact.txt`
- `tools/story/validate_b2_republic_former_smuggler_cooperation_compact.py`
- `story/B2_REPUBLIC_FORMER_SMUGGLER_COOPERATION_COMPACT_HANDOFF_20260826.md`

## Validation contract

Focused validator proves:

- exactly three missions and one Review event;
- exact two named characters and Earth scope;
- the three external inputs are read-only;
- exactly three substantive routes, each writing only its own route, introducing once, scheduling exactly one 7–11 day Review, and declining once;
- refusal cannot introduce the arc or schedule Review;
- Review requires introduced + review-ready + not-reviewed;
- fresh/paired routes are explicit Review branches; completed-history is deliberate fallthrough;
- exactly two settlements, each writing only itself and closing Review once;
- aftermath accepts either settlement, has bounded-specific dialogue, and is one-shot;
- seven `decline`, zero `accept`, and no destination/NPC/cargo/timer objective directives;
- B2-only assignment ownership and no material/reputation mutations;
- all local gotos resolve;
- continuity distinction among historical offense, closed cooperation, current evidence, current request/consent, active suspicion, active source status, and explicit closure.

## Exact validation evidence

The first simulation/story run on initial candidate `a5217545a925ffa197d172b77447c6b8fecb5ff1` failed only in the new focused validator. Changed-content style and repository-wide contracts were already green. The validator incorrectly banned the phrase `general Republic practice` even where production discussed avoiding or localizing such a practice. Production behavior was not changed.

Validator wording was hardened in `34358a1ee9c4f0836164169619d34b1832b3a4de` so the local-scope check rejects an actual positive `universal Republic law` claim instead of rejecting negative/local discussion.

On exact candidate `34358a1ee9c4f0836164169619d34b1832b3a4de`:

- `Fork simulation and story validation` #653 / run `32934639133`: **SUCCESS**
  - focused Python compilation: SUCCESS
  - all focused story validators: SUCCESS
  - A1 simulation/state-ownership contracts: SUCCESS
  - changed-content style: SUCCESS
- `Fork save-load integration smoke` #638 / run `32934639155`: **SUCCESS**
  - dependency installation: SUCCESS
  - production configuration: SUCCESS
  - production build: SUCCESS
  - stock save-load smoke: SUCCESS

These are the acceptance runs for production/validator behavior.

## Persistence/canon assumptions

- `pirate jobs` is vanilla accumulated RPG history and remains read-only.
- A1 remains sole owner of Republic border pressure and customs scrutiny.
- Davin's former smuggling/cooperation is local character history, not a new universal Republic amnesty/informant system.
- Historical wrongdoing is not erased; historical cooperation does not become permanent duty.
- Current investigation authority requires current case-specific basis rather than copied labels alone.
- No save migration is required because this slice only adds new namespaced conditions and the post-production repair changed validator wording only.

## A3/B3 integration notes

Before integration, re-read current `main`, exact ancestry, active B1/A2/B2 work, PR mergeability, and exact workflow state. Reject or defer if another integrated/current slice has since created overlapping Republic former-informant authority semantics.

B3 should preserve the following invariant:

> Historical offense, historical cooperation, current evidence, current cooperation, suspicion, source status, and closure are separate facts. A true old record must not silently manufacture present-tense investigative authority.

## DIVERSITY_CHECK

- Primary domain: crime / investigation / law.
- Previous comparable domains considered: confidential mediation teaching/privacy; career/family succession; stewardship/authority handoff.
- Non-economic systemic inputs: A1 Republic border pressure, A1 Republic customs scrutiny, built-in pirate-job RPG history.
- Why this is not a freight/logistics reskin: the core conflict is a former smuggler's closed cooperation history being misused as current investigative status, not movement of goods or capacity.
- Persistent consequence types: trust state, investigation/cooperation status model, later dialogue, one-shot aftermath.
