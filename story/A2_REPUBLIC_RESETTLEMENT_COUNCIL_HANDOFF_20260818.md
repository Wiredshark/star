# A2 Republic Resettlement Council Handoff — 2026-08-18

Verdict: **PARTIAL / specialist production candidate — not yet A3-ready**

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative integration branch: `main`
- Exact base SHA: `953629bd94aa7ef2e525f2f4bb4c08bc9cb62053`
- A2 branch: `agent/a2-republic-resettlement-council-20260818-2303`
- Production implementation commit: `19dc92b4c81c3e791365bf6f32d7bbec980f0794`
- Validator commit: `8ddccb0e37d80f741ec0f774405d1afb785b07d5`

## Why this slice

The authoritative base just integrated A1 Republic civilian displacement pressure. This A2 slice is a direct player-facing consumer of that new simulation instead of another disconnected dialogue branch.

It deliberately avoids the currently open A2 portfolio covering Imani Rook mediation, reactive Deep news, Deep Security, Deep science/mystery, Pilot Guild career identity, Syndicate maintenance triage, Free Worlds relief coordination, and Southern Rim traffic coordination.

## Production behavior

Named NPC: **Lena Orr**, Republic civil resettlement coordinator.

Emergency Session:
- offers on Earth when authoritative `world: republic displacement pressure >= 2`;
- distinguishes an active `world: republic resettlement surge` from ordinary elevated pressure;
- separately recognizes severe displacement at `>= 4`;
- player selects family unity, work continuity, distributed placement, or refusal;
- writes only `A2 Republic Resettlement Council:*` persistent memory.

After Action:
- offers when authoritative displacement pressure falls below 2;
- combines each positive remembered policy with the *current* authoritative `world: republic border pressure` being `< 4` versus `>= 4`;
- yields six world-sensitive positive outcomes plus a separately respected refusal;
- clears only the A2-owned follow-up-pending state.

## Authority invariants

A1 remains sole writer/owner of:

- `world: republic displacement pressure`
- `world: republic border pressure`
- `world: republic resettlement surge`

A2 reads those values only. It does not set, clear, increment, decrement, clamp, or otherwise mutate them.

No new C++ save schema or parallel narrative-world-state database is introduced. The slice uses the existing persistent mission/global-condition mechanism.

## Files

- `data/human/a2 republic resettlement council.txt`
- `tools/story/validate_a2_republic_resettlement_council.py`
- `story/A2_REPUBLIC_RESETTLEMENT_COUNCIL_HANDOFF_20260818.md`

## Validation actually executed

The focused structural validator was executed locally against the exact candidate text before handoff publication:

`python3 validator.py candidate.txt`

Observed result:

- PASS
- missions=2
- named_character=Lena Orr
- authoritative inputs = Republic displacement pressure, Republic border pressure, Republic resettlement surge
- initial routes = family unity / work continuity / distributed placement / refusal
- after-action variants = 6 + refusal
- authoritative A1 writes = none
- persistent A2 memory = yes

The committed validator implements the same checks at the repository path:

`python3 tools/story/validate_a2_republic_resettlement_council.py "data/human/a2 republic resettlement council.txt"`

## Validation NOT claimed

No executable `Wiredshark/star` checkout/process host is exposed in this run, so none of the following are claimed as passed:

1. normal Endless Sky content-style checker;
2. normal content/data parser;
3. configured project build/regression suite;
4. actual-game Earth offer ordering while the A1 invisible resettlement surge is firing;
5. all four first-stage dialogue routes;
6. all six border-high/border-low after-action outcomes plus refusal;
7. save/load roundtrip between Emergency Session and After Action;
8. regression against stock Republic missions and conversations.

These are required before A3 integration.

## A3 integration instructions

1. Review the exact branch diff against base `953629bd94aa7ef2e525f2f4bb4c08bc9cb62053`.
2. Run the focused validator from an authoritative checkout.
3. Run normal style/parser/build regressions.
4. Exercise the A1 displacement loop and confirm Lena Orr's offer ordering works at pressure 2, severe pressure 4+, and during `world: republic resettlement surge`.
5. Verify A2 never mutates the three A1-owned inputs.
6. Save after each initial policy route, reload, allow A1 pressure to decay below 2, and verify the correct border-pressure-dependent reader appears.
7. Integrate only if those gates pass.

## Verdict rationale

**PARTIAL** because the production slice, persistent-state feedback design, isolated branch, and focused structural validation exist, but authoritative parser/build/runtime/save-load evidence is still missing.
