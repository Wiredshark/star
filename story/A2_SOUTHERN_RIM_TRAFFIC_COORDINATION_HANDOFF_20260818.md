# A2 Southern Rim Traffic Coordination Handoff — 2026-08-18

Verdict: **PARTIAL / specialist production candidate — not yet A3-ready**

## Authority and isolation
- Repository: `Wiredshark/star`
- Authoritative integration branch: `main`
- Exact base SHA: `8d24d7e626bc3f3bb0df9db7c1644e2f9b855c43`
- A2 branch: `agent/a2-southern-rim-traffic-coordination-20260818-2203`
- Exact A2 commit: see branch head / PR handoff

## Selection / diversity
Open A2 work already covers persistent mediation, reactive news, Deep Security, science/mystery, origin-aware career identity, Syndicate maintenance triage, and Free Worlds humanitarian relief. This slice deliberately targets a different integrated A1 surface: Southern Rim transit congestion, cross-read with Merchant rescue load.

## A1 authority consumed
A1 remains sole writer/owner of:
- `world: southern rim transit congestion`
- `world: merchant rescue load`

A2 reads both and writes only `A2 Southern Rim Traffic Coordination:*` memory.

## Production behavior
Named NPC: **Rhea Solano**, Free Worlds traffic coordinator.

Briefing:
- offered at congestion `>= 4`;
- special framing at congestion `>= 6`;
- special framing at rescue load `>= 3`;
- combined framing when both are elevated;
- player chooses emergency corridors, staggered clearances, distributed routing, or refusal.

After-action:
- appears after congestion recovers below 4;
- each positive policy combines with current rescue load `< 3` versus `>= 3`;
- six simulation-sensitive positive outcomes plus refusal;
- only A2-owned follow-up state is cleared/marked seen.

## Files
- `data/human/a2 southern rim traffic coordination.txt`
- `tools/story/validate_a2_southern_rim_traffic_coordination.py`
- `story/A2_SOUTHERN_RIM_TRAFFIC_COORDINATION_HANDOFF_20260818.md`

## Invariants
1. A1 remains sole authority for both `world:` signals.
2. A2 never mutates those signals.
3. Player choice persists through ordinary condition state.
4. Later dialogue reflects current simulation state, not only the earlier choice.
5. Refusal is valid and remembered without becoming endorsement.
6. No new parser syntax, C++ save authority, or dialogue-owned world-state copy is introduced.

## Focused validation
Run:
`python3 tools/story/validate_a2_southern_rim_traffic_coordination.py "data/human/a2 southern rim traffic coordination.txt"`

The validator checks both missions, named NPC, A1 thresholds, four initial routes, six positive after-action variants plus refusal, persistent A2 memory, and absence of writes to either A1 signal.

## Validation not claimed
Until run in an authoritative checkout/runtime, do not claim:
- standard content-style checker;
- normal Endless Sky content parser/build suite;
- actual-game branch exercise;
- save/load roundtrip;
- player-visible dialogue/layout review.

## A3 integration gates
1. Run the focused validator on the exact commit.
2. Run content-style/parser/build validation.
3. Exercise baseline, gridlock-only, rescue-only, and combined briefing framing.
4. Exercise all four player routes.
5. Lower congestion below 4 and verify all six rescue-high/low positive after-action variants plus refusal.
6. Save/reload after each first-stage choice and before the later reader.
7. Confirm A1 values are unchanged by A2 conversations.
8. Review actual in-game dialogue presentation.

Do not integrate solely on structural validation.

- `LOOP_ID`: A2
- `WORK_DOMAIN`: dynamic traffic policy / emergency-response narrative
- `WORLD_STATE_INPUTS`: Southern Rim transit congestion + Merchant rescue load
- `A1_WRITE_AUTHORITY`: none
- `VERDICT`: PARTIAL
