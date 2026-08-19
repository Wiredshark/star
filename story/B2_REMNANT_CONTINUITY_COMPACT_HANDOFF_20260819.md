# B2 Remnant Continuity Compact handoff

## Verdict
PARTIAL — focused/story validators pass in an isolated fresh clone, but the repository content-style gate cannot start on the available host because Python package `regex` is missing. Normal Endless Sky parser/build/runtime/save-load validation is still required before A3 integration.

## Repository state
- Repository: `Wiredshark/star`
- Authoritative `main` observed at run start: `b21d71ce67fa3473bda1e075714d9c486fef734d`
- B1 parent branch: `agent/b1-remnant-survival-institutions-20260819-0016`
- Exact B1 parent SHA: `ed15e743cae8b3d6e260978c921402ae76c7db00`
- B2 branch: `agent/b2-remnant-survival-compact-20260819-0024`
- Production commit: `441d1041b6b067382c6be18b44c7bc739d1b231b`
- Validator implementation commit: `e819c7bc6fcb95c8b02f1b7b62a29df0bc74ebf2`
- Validator hardening commit: `ddb9cc36b7cb55168433374f1066dbb6691182a9`

## Implemented slice
B1 established four linked Remnant survival institutions: continuity archives, shared watch rotations, salvage provenance, and inter-settlement reserve ledgers. B2 turns the reserve/provenance tension into named-character persistent content.

Characters:
- **Nera Venn** — Remnant reserve coordinator. Prioritizes keeping emergency transfers inside patrol and route windows while preserving explicit custody.
- **Corin Taal** — Remnant salvage engineer. Prioritizes repeatable maintenance knowledge, interface history, and named technical responsibility.

Missions:
1. `B2 Remnant Continuity Compact: Offer`
   - three persistent substantive routes: continuity, provenance, or compact;
   - explicit refusal path;
   - trust state for Venn/Taal.
2. `B2 Remnant Continuity Compact: Review`
   - remembers the initial route;
   - resolves to exactly one of two persistent institutional outcomes:
     - `settlement custody reconciliation`;
     - `settlement two key reserve`.
3. `B2 Remnant Continuity Compact: Taal Remembers`
   - later one-shot reader consuming either terminal settlement.

## Files
- `data/remnant/b2 remnant continuity compact.txt`
- `tools/story/validate_b2_remnant_continuity_compact.py`
- `story/B2_REMNANT_CONTINUITY_COMPACT_HANDOFF_20260819.md`

## Ownership and compatibility invariants
- B2 writes only `B2 Remnant Continuity Compact:*` persistent conditions.
- No `world:*` state is written.
- No credits/payment, reputation, cargo, outfits, or combat rating are modified.
- Stock mission/conversation/global-condition mechanisms only.
- The slice is additive under `data/remnant/`; it does not alter existing Remnant campaign files.
- Both terminal outcomes preserve the B1 institutional principle that emergency continuity and durable technical memory must coexist rather than silently overriding each other.

## Executed validation
A fresh clone of the exact B2 branch was created in isolated administrator scratch space on the private host.

Passed:

```text
python3 tools/story/validate_b2_remnant_continuity_compact.py "data/remnant/b2 remnant continuity compact.txt"
PASS: B2 Remnant Continuity Compact structure validated
PASS: missions=3
PASS: named_characters=2
PASS: initial_routes=3 + refusal
PASS: terminal_settlements=2
PASS: later_reader=Taal Remembers
PASS: mutation_surface=B2 conditions only
```

```text
python3 tools/story/validate_story_repo.py
PASS: story repository contract validated
PASS: 8 required durable files present
PASS: builder handoff fields=17
PASS: round report fields=13
PASS: handoff ids=ES-STORY-0001
```

```text
python3 tools/story/test_b2_character_packets.py
PASS: B2 Broken Compact packet contract validated
PASS: player approaches=8
PASS: persistent terminal outcomes=4
PASS: named characters=3
PASS: special-response label targets=2
```

Attempted but environment-blocked:

```text
python3 utils/check_content_style.py
ModuleNotFoundError: No module named 'regex'
```

No content-style PASS is claimed. No normal Endless Sky parser/build/game-runtime/save-load PASS is claimed.

## A3 acceptance requirements
Before integration:
1. Install/provide the repository content-style dependency and run `python3 utils/check_content_style.py`.
2. Run the normal Endless Sky content parser/build validation.
3. Smoke-load Remnant space and verify each mission can offer under intended conditions.
4. Exercise all three Offer routes plus refusal.
5. Save/load after Offer and after Review; verify route/trust/settlement state survives.
6. Verify the Review produces exactly one terminal settlement and `Taal Remembers` consumes either outcome once.
7. Confirm no material, reputation, combat, or `world:*` state changes occur.

## Integration guidance
Integrate only after the above gates pass. This branch is based directly on B1 Remnant survival institutions and should therefore be ordered after `ed15e743cae8b3d6e260978c921402ae76c7db00` or an integration descendant containing that B1 slice. Do not integrate this B2 slice if the parent B1 content is omitted, because the character conflict intentionally depends on the reserve-ledger and salvage-provenance history established there.
