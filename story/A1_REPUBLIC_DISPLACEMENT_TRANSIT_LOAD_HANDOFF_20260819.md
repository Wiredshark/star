# A1 Republic Displacement Transit Load Handoff — 2026-08-19

- stage: A1
- verdict: PARTIAL
- authoritative base/integration SHA: `bdeb9c4ba6c9d0203ff75532e38cd7f4334dbdd8`
- isolated branch: `agent/a1-republic-displacement-transit-load-20260819-1718`
- exact A1 integration candidate commit SHA: `b80ec738bfdbcb9df8c8344a864c3486752820a1`

## Implemented feedback loop

Acute Republic civilian displacement (`world: republic displacement pressure >= 4`) now feeds into the existing Southern Rim traffic simulation. A qualifying Republic-to-Free-Worlds crossing contributes one bounded unit of `world: southern rim transit congestion`, then latches for four days so repeated player crossings cannot rapidly amplify the same crisis. The contribution schedules the existing three-day Southern Rim decay event rather than creating a second congestion state, preserving one authoritative routing-pressure variable.

## Files

- `data/human/a1 republic displacement transit load.txt`
- `tests/a1/test_displacement_transit_load_model.py`
- `story/A1_REPUBLIC_DISPLACEMENT_TRANSIT_LOAD_HANDOFF_20260819.md`

## Invariants and compatibility

- No new source-of-truth displacement or congestion variable is introduced.
- Congestion remains clamped to `[0, 6]` by the existing Southern Rim contract.
- The new latch is boolean/ephemeral and self-clears after four days.
- Existing save games safely default the new latch to unset; existing persistent numeric variables retain their prior meanings.
- The slice is simulation-only and does not own A2 narrative or A3 integration state.

## Validation required before READY

The GitHub-only execution path used for this backup run could not execute the repository because the live private host checkout is an unrelated Fallout repository. Therefore this handoff is deliberately PARTIAL rather than claiming unrun tests.

A3 (or a later A1 validation pass) should run from exact commit `b80ec738bfdbcb9df8c8344a864c3486752820a1`:

```text
python3 tests/a1/test_displacement_transit_load_model.py
python3 tests/a1/test_border_pressure_model.py
```

Also run the repository's standard Endless Sky data/parser or simulation validation command used by current A3 integrations, plus the normal save/load workflow. Confirm the new mission parses, a displacement value below 4 does not add congestion, values 4-6 add at most one unit per latch window, congestion never exceeds 6, and scheduled decays return congestion to zero without underflow.

## Deterministic model evidence encoded by the focused test

- displacement 3, congestion 2 -> no contribution;
- displacement 4, congestion 2 -> congestion 3 and latch set;
- twenty repeated crossings during the latch -> congestion remains 3;
- repeated post-latch crisis crossings -> trace `[4, 5, 6, 6, 6, 6, 6, 6]`;
- matching plus stale decay applications -> congestion bottoms at 0.

## Risks / deferred work

- Runtime parser and save/load evidence are not available in this run and must be obtained before integration.
- This slice intentionally does not add player-facing news or policy responses; those belong to later stages.
- Do not merge this branch directly. A3 should validate and integrate exact commit `b80ec738bfdbcb9df8c8344a864c3486752820a1` under the normal integration protocol.
