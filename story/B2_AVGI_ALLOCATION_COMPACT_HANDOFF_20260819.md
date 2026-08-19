# B2 Avgi Allocation Compact — A3 handoff

## Verdict

READY for A3 review/integration after the B1 Avgi institutional-history parent.

## Exact repository state

- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Authoritative `main` observed at stage start: `d485dea4c511964c1209d86dae15f5bcbf17a03b`
- Required B1 parent/base: `406002899849146ad8884d33616f599b9e141284`
- Isolated branch: `agent/b2-avgi-allocation-compact-20260819-0326`
- Production content commit: `fe535ed99b5d7a8c25be5f2845fa42046b421e1c`
- Focused validator commit: `9c78aac5481a1ec37cc205eed13d208c890f80b0`
- Header/style repair and exact validated production/data/validator head: `79f20bc4f3a45f1b5f35391b899d7e757a7a7d5f`
- Draft PR: #66

## Character / dynamic-content slice

This slice consumes the B1 Avgi Allocation Ledger and Twilight Guard Muster institutional history. It turns the historical split between civilian allocation bureaucracy and civil-defense emergency authority into a present-day named-character dispute over emergency dee / energy reserves.

Named characters:

- **Verdigris** — Consonance allocation clerk; prioritizes auditable civilian-service floors and a reserve picture that exposes displaced loads.
- **Ochre** — Twilight Guard reserve officer; prioritizes immediate emergency authority during alerts while accepting durable review records.

Production file: `data/avgi/b2 avgi allocation compact.txt`

Missions:

1. `B2 Avgi Allocation Compact: Offer`
   - Verdigris route: protected civilian-service floor.
   - Ochre route: immediate Guard draw authority with post-alert review.
   - Paired route: shared reserve ledger and pre-authorized emergency classes.
   - Refusal route.
2. `B2 Avgi Allocation Compact: Review`
   - Remembers the initial policy position.
   - Paired route is the intentional conversation fallthrough; Verdigris/Ochre routes have specialized review text.
   - Resolves to one of two terminal settlements:
     - `settlement public emergency ledger`
     - `settlement dual threshold`
3. `B2 Avgi Allocation Compact: Verdigris Remembers`
   - One-shot later reader for either terminal settlement.

## Authority / continuity invariants

- Every writable condition is namespaced `B2 Avgi Allocation Compact:*`.
- B2 does not write `avgi:*`, `world:*`, credits, reputation, cargo, outfits, ships, or fleets.
- All three missions require `language: Avgi (Written)`.
- All three preserve `not "avgi: lost in twilight"`.
- The compact coordinates emergency reserve records and authorization rules; it does **not** imply political merger, military subordination, or institutional unification of the Consonance and Twilight Guard.
- B1 institutional-history content remains observational authority; B2 consumes it rather than rewriting its historical claims.

## Validation evidence

### Focused / repository contracts

Executed in a fresh isolated clone at exact head `79f20bc4f3a45f1b5f35391b899d7e757a7a7d5f`:

- `python3 tools/story/validate_b2_avgi_allocation_compact.py` — PASS.
- `python3 tools/story/run_focused_validators.py` — PASS, 27/27 checks.
  - Includes all focused A2/B2 story validators.
  - Includes `validate_fork_content_contracts.py` uniqueness, goto/label, and state-ownership checks.
- `python3 tools/story/validate_story_repo.py` — PASS.
- `python3 tools/story/test_b2_character_packets.py` — PASS.

The private host's system Python does not include `pytest`, so the direct host `python3 -m pytest -q tests/a1` command could not start. Repository-native CI installs pytest and covers that gate below.

### Changed-content style

The first CI pass correctly rejected the production file for a missing standard copyright/GPL header. The header was added in commit `79f20bc4f3a45f1b5f35391b899d7e757a7a7d5f`.

Then, using an isolated Python venv with `regex` installed:

`python tools/story/check_changed_content_style.py --base 406002899849146ad8884d33616f599b9e141284 --head 79f20bc4f3a45f1b5f35391b899d7e757a7a7d5f`

Result: PASS, `No issues found.`

### Repository-native CI

On exact production/data/validator head `79f20bc4f3a45f1b5f35391b899d7e757a7a7d5f`:

- GitHub Actions `Fork simulation and story validation` run `32229202515` — SUCCESS.
  - Focused simulation/story contracts are green.
  - Changed fork content style is green.
  - A1 pytest contracts are therefore covered by repository-native CI.
- GitHub Actions `Fork save-load integration smoke` run `32229202513` was still in progress when this handoff was written. A3 should honor a later failure if that run does not finish green.

### Production build / stock persistence smoke

A private-host production executable was configured and built successfully with:

- `cmake -S . -B build/b2-avgi-local -G Ninja -DES_USE_VCPKG=OFF -DBUILD_TESTING=OFF -DCMAKE_BUILD_TYPE=Release`
- `cmake --build build/b2-avgi-local --config Release --target EndlessSky --parallel 2`

The built `endless-sky` executable then successfully ran the stock integration tests against the exact final Avgi resource tree:

- `Saving during conversation` — exit 0.
- `Loading and Reloading` — exit 0.
- `Loading and Saving` — exit 0.

The executable emits pre-existing `Incomplete assignment` warnings from already-present A1/A2 fork data and existing libpng profile warnings. These warnings are not introduced by this B2 slice; all three stock integration cases still exited successfully.

## A3 integration instructions

1. Integrate B1 Avgi institutional-history parent `406002899849146ad8884d33616f599b9e141284` first.
2. Review/integrate this B2 branch after that parent.
3. Preserve the authority boundary: B2 owns only `B2 Avgi Allocation Compact:*`; do not convert the settlement into writes against upstream Avgi campaign state or A1 `world:*` state.
4. Preserve separate Consonance / Twilight Guard institutional authority in later continuity work.
5. Check final status of save-load workflow run `32229202513`; if it later fails, investigate before integration despite the local production build and three successful stock smoke cases.

## Deferred / follow-up opportunities

A2 may later read the two terminal settlement conditions to alter news, emergency-response dialogue, or policy reactions. B3 may reconcile this compact with future Avgi civil-defense content, but should not infer a new central Avgi government or treaty from the shared emergency ledger.
