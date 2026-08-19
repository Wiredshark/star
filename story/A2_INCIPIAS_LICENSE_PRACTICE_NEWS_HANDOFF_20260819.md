# A2 Incipias License Practice News handoff — 2026-08-19

## Stage
A2 CORE RPG + DYNAMIC NARRATIVE

## Verdict
PARTIAL pending exact-head repository-native validation and actual-game acceptance.

## Repository state
- Authoritative repository: `Wiredshark/star`
- Authoritative base: `main` @ `67203cc6d170f4961fd7cfe2374881453296fa04`
- Branch: `agent/a2-incipias-license-practice-news-20260819-1006`
- Production commit: `ea60df016d60b6bdc75b601e800e62cece345019`
- Validator commit: `4b090a47542a9ebe6830e6ac2f94e8844ade5219`
- Exact candidate head: the commit containing this handoff; PR metadata records its full SHA.

## Scope
Consumes the integrated B2 Incipias License Compact only after `B2 Incipias License Compact: aftermath seen`.

Adds four Conlatio-port ambient News groups:
1. portable endorsement — working pilot/crew perspective;
2. portable endorsement — licensing-record perspective;
3. tiered renewal — working pilot/crew perspective;
4. tiered renewal — licensing-review perspective.

The public consequences show how the two terminal settlements change everyday licensing practice after the original Registrar/Pilot arc has resolved. The declined route never reaches the B2 Review chain and is intentionally not publicized here.

## Ownership and canon invariants
- B2 state is read-only.
- No `action` blocks and no persistent writes.
- No A1 `world:*` state is read or written.
- All News remains scoped to existing `Conlatio` ports.
- No Incipias personal names, formal offices, central bureaucracy, treaty, or galaxy-wide licensing authority is invented.
- Portable endorsement means evidence/ship-class/supervision/limits travel with the credential; it does not erase ship-class distinctions.
- Tiered renewal keeps local discretion distinct from portable/shared categories through independent review.

## Files
- `data/incipias/a2 incipias license practice news.txt`
- `tools/story/validate_a2_incipias_license_practice_news.py`
- `story/A2_INCIPIAS_LICENSE_PRACTICE_NEWS_HANDOFF_20260819.md`

## Focused validator contract
Checks exactly four News groups, exact B2 aftermath gating, two portable groups, two tiered groups, Conlatio scoping, absence of action/state writes, absence of `world:*` state, and absence of declined/refusal publicization.

## A3 integration gates
Before integration:
1. Require exact-head `Fork simulation and story validation` success.
2. Require exact-head `Fork save-load integration smoke` success.
3. In the actual game, observe both perspectives for both terminal settlements.
4. Prove no license-practice News appears before `aftermath seen`.
5. Prove the declined B2 route produces no license-practice News.
6. Verify persistent gates after a real save/reload and review Incipias News rotation/offer regression.

Do not self-integrate; A3 owns integration.
