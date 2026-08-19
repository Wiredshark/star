# A1 Republic civic administration strain handoff — 2026-08-19

## Stage

- Stage: A1
- Verdict: READY pending A3 integration review
- Authoritative base/integration SHA: `af9efc35faa7ccccc48dcd3e9b2a2811c083e94a`
- Isolated branch: `agent/a1-republic-civic-strain-20260819-0709`
- Isolated worktree: `renderer-admin-scratch/star-a1-backup-20260819-070929-run1`
- Exact A1 implementation commit: `1ff829565da4f92c7b2d63e8e9d8100ba60cccde`

## Increment

This A1 slice adds a bounded Republic civic-administration strain feedback loop. It consumes two existing A1-owned authorities, `world: republic displacement pressure` and `world: republic customs scrutiny`, without mutating either one. When both are simultaneously elevated, qualifying Republic arrivals add `+2` to `world: republic civic strain`, capped at 6, with a four-day assessment latch and a scheduled one-unit recovery ten days later.

The recovery path is intentionally hysteretic. Accelerated stabilization is unavailable while either source pressure remains elevated; once displacement is `<= 2` and customs scrutiny is `<= 1`, strain of at least 2 can fall by two units with a six-day stabilization latch. This prevents the derived governance signal from declaring recovery while either source crisis is still active, while also ensuring residual strain does not become permanently stranded after the source pressures recede.

A rate-limited notice exposes the state as administrative/public-service capacity rather than guilt, reputation, or a law-enforcement penalty. A2/A3 can later consume `world: republic civic strain` for governance, public-service, institutional-capacity, or dialogue consequences.

## Files and ownership

Implementation commit changes only:
- `data/human/a1 republic civic strain.txt`
- `tests/a1/test_republic_civic_strain.py`

This handoff is a documentation-only follow-up and is not part of the A1 implementation SHA above.

A1 reads but never writes:
- `world: republic displacement pressure`
- `world: republic customs scrutiny`

A1 owns:
- `world: republic civic strain`
- `world: republic civic assessment active`
- `world: republic civic stabilization`
- `world: republic civic strain notice seen`

No credits, reputation, cargo, combat rating, mission-completion history, A2 state, B-lane state, or unrelated world conditions are mutated.

## Invariants and compatibility

- `world: republic civic strain` remains within `0..6`.
- Escalation requires both displacement `>= 4` and scrutiny `>= 3`.
- Escalation is rate-limited by a four-day assessment latch.
- Each escalation schedules a one-unit ten-day recovery and clamps at 6.
- Fast stabilization requires both source pressures to have receded to low thresholds and clamps at zero.
- The derived signal never writes either source authority.
- Existing saves require no migration: absent numeric/global conditions use the engine's normal zero/false default until a qualifying transition occurs.
- The implementation uses stock mission/event/global-condition persistence; no save schema or C++ serialization changes are introduced.

## Diversity check

LOOP_ID: A1
RUN_TYPE: FEATURE
PRIMARY_DOMAIN: faction control / politics / governance
SECONDARY_DOMAINS: population/migration; crime/law/enforcement; institutional capacity
RECENT_DOMAIN_WINDOW: relief reserve strain; merchant route diversion; relief routing backlog
DIVERSITY_STATUS: PASS
CONCENTRATION_JUSTIFICATION: N/A
NEGLECTED_AREA_ADVANCED: governance/institutional-capacity feedback after a logistics/resource-heavy A1 window
CROSS_SYSTEM_CONNECTION: existing Republic displacement pressure + existing Republic customs scrutiny

DIVERSITY_CHECK
- Primary domain: politics/governance.
- Recent same-lane domains considered: relief reserve/resource strain, merchant route diversion, relief routing backlog, syndicate labor strain.
- Adjacent-lane work considered: Republic resettlement/customs consumers already read A1 state; this slice exposes a new derived governance signal without rewriting their narrative state.
- Why this is not another iteration of the same subsystem: it does not model cargo, freight, routing, market prices, supply, or convoy capacity.
- Underrepresented area advanced: institutional/public-service capacity.
- New cross-system connection: population displacement plus customs/enforcement scrutiny jointly drive civic strain.
- Persistent/player-visible capability added: a bounded, recoverable governance-pressure state and rate-limited public-service notice.
- Concentration exception: none.

## Validation evidence

Focused model:
- `python3 tests/a1/test_republic_civic_strain.py` -> PASS after repairing an initially detected convergence defect.
- Initial deterministic-year run correctly failed because the original stabilization threshold could strand residual strain below 4. The threshold was changed so low-source stabilization can clear strain from 2 to 0; the repaired 365-day deterministic horizon then passed.

A1 regression set:
- `bash -lc 'set -e; for f in tests/a1/test_*.py; do python3 "$f"; done'` -> PASS for all 9 A1 scripts on this checkout.

Repository-native cross-file validation:
- `python3 tools/story/run_focused_validators.py` -> PASS, 31/31 checks.
- `tools/story/validate_fork_content_contracts.py` within that run reported 54 fork files, 10 A1 files, 162 missions, 19 events, 25 A1 world conditions with writers; mission/event names unique; mission goto targets valid; B1/A2/B2 do not mutate A1 `world:*` authority; all discovered `world:*` writers are A1-owned.

Diff hygiene:
- `git diff --cached --check` -> PASS before implementation commit.

Environment limitations, not claimed as passes:
- `pytest -q tests/a1` could not run because the host has no `pytest` executable; all A1 test modules were therefore executed directly with `python3` and passed.
- `python3 utils/check_content_style.py 'data/human/a1 republic civic strain.txt'` could not run because Python module `regex` is absent on the host. Repository-native focused/fork validators did run and pass.
- No compiled Endless Sky runtime/build or stock save-load smoke was executed in this host run; A3 should perform those integration checks on the then-current authoritative head.

## Deterministic horizon evidence

The focused model simulates 365 deterministic days: 150 days with displacement=5 and scrutiny=4 followed by 215 days with displacement=1 and scrutiny=1. It asserts every daily state remains within `0..6`, stabilization never triggers during the acute joint crisis, scheduled recovery cannot underflow, and the post-crisis system converges exactly to zero.

No RNG is used by this slice, so no random seed is required for reproducibility.

## A3 integration instructions

1. Recover the then-current authoritative integration head; do not assume the base above remains current.
2. Cherry-pick exact implementation commit `1ff829565da4f92c7b2d63e8e9d8100ba60cccde` only after checking whether its two input authorities still exist with the documented ownership semantics.
3. Confirm no concurrent A1 handoff has introduced the same `world: republic civic strain` keys or mission/event names.
4. Re-run all A1 scripts and `python3 tools/story/run_focused_validators.py`.
5. Run repository content-style validation in an environment with the `regex` dependency, then the normal Endless Sky parser/build and stock save/load smoke.
6. Treat this signal as A1 authority. A2 may read it but should not clear/reduce it to manufacture narrative resolution.

No ordering dependency exists on the currently unintegrated Free Worlds reserve, merchant-route, relief-routing, or Syndicate labor A1 branches; this slice is based solely on authoritative `main` at the exact base SHA above.

## Deferred / risks

- Balance thresholds are intentionally conservative and should be observed after integration; no economy or fleet-spawn changes are bundled here.
- The public notice is minimal observability only. Rich narrative reactions belong to A2.
- Compiled parser/runtime and save-load verification remain A3 integration requirements because this host run did not execute them.

ES4_NEXT_STAGE_CONTEXT_BEGIN
A3 must integrate exact A1 implementation SHA `1ff829565da4f92c7b2d63e8e9d8100ba60cccde` from base `af9efc35faa7ccccc48dcd3e9b2a2811c083e94a`. Preserve A1 ownership of `world: republic civic strain`; `world: republic displacement pressure` and `world: republic customs scrutiny` are read-only inputs. Re-run content style with the missing `regex` dependency available plus normal parser/build/save-load checks before final integration acceptance.
ES4_NEXT_STAGE_CONTEXT_END
