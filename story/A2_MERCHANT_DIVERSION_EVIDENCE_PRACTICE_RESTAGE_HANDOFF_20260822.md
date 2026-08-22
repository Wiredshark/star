# A2 Merchant Diversion Evidence Practice current-main restage handoff — 2026-08-22

## Verdict

READY for A3 review/integration. Do not self-integrate; A3 retains integration authority.

## Exact repository state

- Repository: `Wiredshark/star`
- Authoritative integration branch: `main`
- Authoritative base SHA: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/a2-merchant-diversion-evidence-practice-restage-20260822-0502`
- Production restage commit: `1bf97436d2eab237c05b3cacf8bde4f3bd5dd089`
- Strengthened validator commit: `9b0aeb1fff1c1f1d0945a16b75f24e8e29a10af1`
- Validator wording repair / exact fully validated production+validator head: `eeae8b035de970277dba1e381cb8cba52f4e89c6`
- Historical PR #156 remains untouched.

## Selection and concurrency

Live `main` and open A2 work were recovered before branching. Current-main A2 coverage is extensive, but historical Merchant Diversion Evidence Practice PR #156 remains a distinct PARTIAL slice and no current-main restage of that route-evidence domain existed. The restage avoids the active Republic Border Testimony runtime repair and does not duplicate the READY Merchant Repair Priority slice.

The exposed private execution host was checked. It reports four pre-existing service-owned processes; no unrelated process was modified. Its workspace is not used as Endless Sky runtime evidence.

## RPG / dynamic narrative loop

The integrated B2 Merchant Diversion Compact is already resolved before this A2 slice begins. The Briefing requires `B2 Merchant Diversion Compact: aftermath seen` and distinguishes the B2 settlement where relevant.

Nessa Ward asks what should travel from the previous compact into future route warnings. The player may persist one of three practices or explicitly refuse:

1. **expiry** — every copied detour preserves the condition that ends or renews it;
2. **lineage** — repeated copies preserve source ancestry and do not become independent observations merely through repetition;
3. **contradiction** — later disconfirming evidence travels as visibly as the warning it weakens;
4. **refusal** — no standing player-backed Merchant evidence practice is established.

Because the upstream aftermath occurs after the original diversion wave has recovered, the second mission naturally waits for a later authoritative A1 recurrence. At `world: merchant route diversion pressure >= 3`, each positive practice receives a normal consequence and a severe-pressure (`>= 5`) consequence, yielding six deterministic history-aware outcomes. Refusal does not arm recurrence.

## Current architecture / lifecycle repairs

This restage preserves the original narrative/state semantics while applying the current A2 dialogue lifecycle contract:

- both state-only missions use `offer precedence 9`;
- all four Briefing terminals and the Recurrence terminal end with `decline` after recording state;
- objective-less `accept` is forbidden;
- no cargo/passenger/destination/waypoint/NPC/deadline gameplay objective is introduced.

## Ownership and invariants

- A1 remains sole writer of `world: merchant route diversion pressure` and upstream rescue/congestion/recovery state.
- B2 remains sole writer of `B2 Merchant Diversion Compact:*`.
- A2 writes only `A2 Merchant Diversion Evidence Practice:*`.
- Repeated copies of one warning do not become independent corroboration.
- Expired advice remains historical evidence rather than current routing truth.
- Contradictory evidence can lower confidence without erasing the original observation.
- No centralized Merchant routing authority is created.
- Refusal remains refusal and does not arm recurrence.
- No credits, reputation, cargo, outfit, ship, fleet, or combat semantics are changed.

## Files

- `data/human/a2 merchant diversion evidence practice.txt`
- `tools/story/validate_a2_merchant_diversion_evidence_practice.py`
- `story/A2_MERCHANT_DIVERSION_EVIDENCE_PRACTICE_RESTAGE_HANDOFF_20260822.md`

## Validator coverage

The strengthened focused validator checks:

- exact two-mission structure;
- integrated B2 aftermath/settlement inputs;
- A1 moderate/severe recurrence thresholds;
- all three positive practices plus refusal;
- six positive recurrence outcomes;
- A1/B2 read-only ownership;
- A2 namespace isolation;
- zero state-only `accept` endpoints;
- exactly five `decline` terminals;
- `offer precedence 9` on both missions;
- no gameplay-objective directives;
- refusal not arming recurrence.

## Validation history and exact evidence

Initial exact head `98cf7007bdb86cc94adf26392d8444668570aa1f` produced:

- `Fork save-load integration smoke` run `32563966229` / #373: **SUCCESS**;
- `Fork simulation and story validation` run `32563966327` / #388: **FAILURE**.

The failed job `97009722440` showed a single focused-validator defect: the validator required the typo phrase `centralized Merchant route authority`, while the production invariant correctly says `centralized Merchant routing authority`. Changed-content style and repository-wide content contracts were already green.

Commit `eeae8b035de970277dba1e381cb8cba52f4e89c6` fixes only that validator wording. Production RPG/state behavior is unchanged.

On exact fully validated production+validator head `eeae8b035de970277dba1e381cb8cba52f4e89c6`:

- `Fork simulation and story validation` run `32566820411` / #391: **SUCCESS**;
  - focused story validators: SUCCESS;
  - A1 simulation/state-ownership contracts: SUCCESS;
  - changed-content style: SUCCESS;
- `Fork save-load integration smoke` run `32566820386` / #376: **SUCCESS**;
  - production configure/build: SUCCESS;
  - stock save-load smoke: SUCCESS.

No manual actual-game acceptance is claimed beyond those repository-native gates.

## A3 integration instructions

Re-read current `main`, verify ancestry and mergeability, then review the validated current-main restage. Preserve A1/B2 ownership, the route-evidence epistemic boundaries, refusal semantics, `offer precedence 9`, and the state-only `decline` lifecycle. The current branch tip may include only this READY handoff promotion after validated head `eeae8b035de970277dba1e381cb8cba52f4e89c6`; production and validator behavior must remain identical to that green SHA. Do not self-merge from A2.
