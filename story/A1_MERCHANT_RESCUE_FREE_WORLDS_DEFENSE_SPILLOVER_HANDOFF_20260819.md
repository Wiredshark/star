# A1 Merchant Rescue -> Free Worlds Defense Spillover Handoff

- stage: A1
- authoritative base/integration SHA: `a4ba72896870d0b764272ef95d012b661b677c06`
- isolated branch: `agent/a1-merchant-rescue-fw-defense-spillover-20260819-1604`
- A1 implementation+test commit SHA: `38a90c52247ddb31025284269b9790edaed83b1f`
- verdict: **READY**, with host-runtime limitation recorded below.

## Implemented feedback loop

Sustained Merchant rescue load (`world: merchant rescue load >= 3`) now produces one bounded unit of existing Free Worlds defense strain on the next qualifying Free Worlds system entry. A six-day latch prevents repeated jumps from amplifying one rescue episode. The bridge never mutates Merchant rescue load; the existing Merchant recovery remains authoritative upstream, and the existing Free Worlds defense-strain recovery remains authoritative downstream.

## Key files

- `data/human/a1 merchant rescue free worlds defense spillover.txt`
- `tests/a1/test_merchant_rescue_free_worlds_defense_spillover.py`

Existing state owners consumed read/write-consistently:

- `data/human/a1 merchant rescue load.txt` — read-only upstream signal.
- `data/human/a1 free worlds defense strain.txt` — bounded downstream state and existing six-day recovery event.

## Invariants / compatibility

- Merchant rescue load remains bounded by its existing owner and is never changed by the bridge.
- Free Worlds defense strain remains bounded to `[0, 5]`.
- The bridge contributes at most one strain unit per six-day latch window.
- Existing `ES A1: Free Worlds Defense Strain Recovery` owns downstream decay; no duplicate decay system is introduced.
- No new save schema or engine state is introduced; only standard persisted mission condition keys/events are used.
- Presentation is limited to existing simulation-state mechanics; no A2 narrative or A3 integration behavior is added.

## Validation evidence

Exact host-side `Wiredshark/star` checkout execution was unavailable in this run: the exposed Fallout Mesh Host repository workspace resolved to `Wiredshark/fallout-test`, so no repository test/build command is claimed against `star`.

Strongest available substitute executed against exact retrieved upstream file contents plus the proposed bridge logic:

- static ownership assertions: PASS;
- threshold behavior at rescue load 2/3 and defense strain 4/5: PASS;
- latch suppression: PASS;
- deterministic accelerated horizon: 1,095 simulated days with 42-day acute rescue periods every 120 days, qualifying entry every 2 days, six-day recovery/latch cadence: PASS;
- boundedness invariant `0 <= defense strain <= 5` across the full horizon: PASS;
- quiet-tail convergence to zero: PASS.

Repository test added for later exact-checkout execution:

`python tests/a1/test_merchant_rescue_free_worlds_defense_spillover.py`

Recommended broader validation at integration time:

`python tests/a1/test_merchant_rescue_free_worlds_defense_spillover.py`

plus the repository's current simulation/story validation and save/load workflow used by A3 for other A1 handoffs.

## Persistence

The new latch condition is standard persisted world condition state. Existing source/downstream counters and scheduled events retain their current persistence behavior. No migration is required; absent latch state defaults naturally to inactive.

## Known risks / deferred work

- Exact Endless Sky parser/runtime validation must be rerun from an authoritative `Wiredshark/star` checkout before A3 integration because the available execution host was bound to another repository.
- This slice intentionally does not alter fleet spawning, economy pricing, dialogue, news, or narrative consequences; later lanes may consume the resulting state without taking ownership of it.

## A3 integration instructions

1. Re-read current `main` and confirm no later integrated bridge already couples Merchant rescue load directly into Free Worlds defense strain.
2. Confirm commit `38a90c52247ddb31025284269b9790edaed83b1f` descends from authoritative base `a4ba72896870d0b764272ef95d012b661b677c06` or review/rebase/cherry-pick conflicts without rewriting this A1 branch.
3. Run the focused test on an exact checkout, then the current simulation/story and save/load workflows.
4. Preserve upstream read-only ownership of `world: merchant rescue load`, downstream cap 5, and six-day latch/recovery cadence.
5. Integrate through A3 only; A1 must not self-merge.
