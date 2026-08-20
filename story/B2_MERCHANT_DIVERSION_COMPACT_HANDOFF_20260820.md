# B2 Merchant Diversion Compact handoff — 2026-08-20

## Verdict

PARTIAL pending exact-head repository-native simulation/story/style and production save-load validation. Do not self-integrate; A3 owns integration.

## Exact repository state

- Repository: `Wiredshark/star`
- Authoritative `main` observed at branch creation: `95fdb069b0a56d990f75a59b0c44fe9d6401038d`
- Isolated branch: `agent/b2-merchant-diversion-compact-20260820-0223`
- Production commit: `70243a3338926f2e1685765584951b0de4afbccf`
- Focused validator commit: `08288cfa03812f3b5c2b7a560d7d4fc2e06aabdf`
- This handoff commit is the current candidate head.

## Selection / concurrency

Current main, recent open B2 work, and active A2 work were inspected before selection. The newly active A2 Syndicate parts-practice branch occupies the replacement-parts/provenance domain, so B2 deliberately did not create another Syndicate parts slice. Existing Merchant B2 work covers recovery-margin capacity, while this slice covers the separate A1 route-diversion state and B1 diversion-dispatch archive.

The exposed private execution host was also inspected. Its repository workspace points to `Wiredshark/fallout-test`, not `Wiredshark/star`, so it was not used as Endless Sky runtime evidence and no unrelated work/process was disturbed.

## Dynamic-content slice

Adds three Merchant missions and two recurring named characters:

- Nessa Ward — dispatch coordinator concerned with expiry, review, source lineage, and keeping temporary routing advice temporary.
- Cal Harker — independent carrier captain concerned with letting current field evidence move quickly enough to remain useful.

### Initial phase

`B2 Merchant Diversion Compact: Offer` requires authoritative A1 `world: merchant route diversion pressure >= 3`.

The player chooses:

1. expiry-first routing records;
2. field-first reports with explicit observation/source context;
3. a paired portable diversion record preserving evidence, cost, and expiry;
4. refusal.

### Recovery/review phase

`B2 Merchant Diversion Compact: Review` requires A1 route-diversion pressure to recover to `<= 1`. B2 does not write that world state.

The Review exposes second-order information loss when copied diversion notices preserve the route recommendation but drop fuel/repair margins, source independence, review conditions, or the evidence needed to retire the detour.

Terminal settlements:

- `settlement docket`: portable expiry docket carrying trigger, sources, observation dates, operating cost/margin, review point, and closure status;
- `settlement ladder`: evidence ladder distinguishing direct observation, independent confirmation, relayed report, inference, and contradiction.

`Ward Remembers` is the one-shot aftermath reader.

## Canon / ownership invariants

- A1 remains sole writer of `world: merchant route diversion pressure` and its upstream rescue/congestion state.
- Every B2 write is namespaced `B2 Merchant Diversion Compact:*`.
- No credits, reputation, cargo, outfits, ships, fleets, or combat mutation.
- Diversions remain temporary operating decisions, not proof that a primary route is permanently unsafe.
- Repeated copies of the same warning must not manufacture independent confirmation.
- Expired operational advice remains historical evidence rather than being silently erased.
- The compact is voluntary coordination among participating Merchant carriers, not a centralized Merchant route authority.

## Files

- `data/human/b2 merchant diversion compact.txt`
- `tools/story/validate_b2_merchant_diversion_compact.py`
- `story/B2_MERCHANT_DIVERSION_COMPACT_HANDOFF_20260820.md`

## Required exact-head validation

Before READY / A3 integration:

1. `Fork simulation and story validation` must be terminal green on the exact candidate head, including changed-content style and the focused B2 validator.
2. `Fork save-load integration smoke` must be terminal green on the exact candidate head, including production build and stock save/load smoke.
3. Actual-game acceptance should verify high-pressure Offer gating, all three substantive routes, refusal, low-pressure Review gating, both settlements, save/reload between stages, and one-shot aftermath behavior.

## A3 / B3 integration notes

This slice can integrate directly after current main because the required B1 Merchant Diversion Dispatch Archive is already authoritative. Re-read current main before integration in case a concurrent A2/B2 route-policy slice lands first. Preserve the distinction among observed route conditions, copied reports, inference, route recommendation, expiry/review status, and historical evidence.
