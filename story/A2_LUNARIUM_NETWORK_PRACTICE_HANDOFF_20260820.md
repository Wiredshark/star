# A2 Lunarium Network Practice handoff

Verdict: PARTIAL pending exact-head repository validation and actual-game acceptance.

Authoritative base: `fdaf94f18aaa02abd4e7269196375572cd0fdf9b`
Branch: `agent/a2-lunarium-network-practice-20260820-0910`
Production commit: `0f8c6758adcab47b51b3968da40e6fe89b241519`
Validator commit: `d1f8f090e2c98c51896f10e7915b57a1ca2f6a71`

## Loop
After the player has joined the Lunarium, Chiree asks the player to choose a private operating practice: preserve civilian-aid obligations independently of covert convenience, use compartmented need-to-know handoffs, preserve provenance/corrections around allegations, or refuse a standing rule. A later one-shot reflection demonstrates a consequence of each positive route.

## Invariants
- `joined the lunarium` / `joined the heliarchs` are read-only gates.
- No `world:*` state is written.
- All persistent writes are namespaced `A2 Lunarium Network Practice:*`.
- Genuine charity remains a genuine obligation even when routes also provide covert cover.
- Compartmentation limits disclosure; it is not omniscient security.
- Repeated allegations do not manufacture independent corroboration.
- Refusal does not arm the later reflection.
- The player receives no Lunarium office or authority to speak for civilian beneficiaries.

## Files
- `data/coalition/a2 lunarium network practice.txt`
- `tools/story/validate_a2_lunarium_network_practice.py`
- this handoff

## Validation still required
Run the focused validator and repository story/simulation/style workflow on the exact final head; run production build/save-load smoke; exercise all four briefing routes, three reflections, refusal suppression, save/reload between stages, one-shot behavior, and Lunarium offer precedence in-game.

## A3
Do not integrate until exact-head repository-native gates are terminal green and current-main ancestry/conflict review remains clean. A3 owns integration.
