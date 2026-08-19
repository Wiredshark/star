# A2 Bunrodea Freight Practice News Handoff — 2026-08-19

Verdict: **PARTIAL / specialist candidate — actual-game acceptance remains required**

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative integration branch: `main`
- Recovered authoritative base SHA: `6f4e270c71ceffe7403252bcc404f0ec91651cc8`
- A2 branch: `agent/a2-bunrodea-freight-practice-news-20260819-0706`
- Production commit: `fc4a8c7f839828e92fbfe12b6bdb8b2928091e62`
- Validator commit: `387f86e820f70dcf0718e5b7b9165eaf7c090396`
- Integration authority: A3 only. Do not self-merge.

## Selection / concurrency boundary

The run recovered current `main` and inspected open A2 PRs before authoring. Active A2 candidates covered Avgi allocation practice, Republic review practice, Syndicate maintenance policy, Free Worlds joint-corridor doctrine, and Republic customs precedent. No active Bunrodea A2 slice was found.

The newest integrated main change is the B2 Bunrodea Freight Petition Compact. This A2 increment therefore consumes that newly integrated terminal state instead of racing an existing A2 specialist branch.

## Implemented RPG / narrative feedback

The integrated B2 compact resolves the Sedi Var / Iral Kes dispute into one of two persistent settlements and later records `aftermath seen`:

- `settlement portable docket`
- `settlement dual ledger`

This A2 slice propagates those resolved outcomes into ambient Bunrodea port News, providing a downstream player-facing consequence after the direct NPC arc has ended.

Four read-only News groups cover both settlement forms from two institutional perspectives:

1. portable docket — Megasa freight perspective;
2. portable docket — Erabu/general petition perspective;
3. dual ledger — Megasa freight perspective;
4. dual ledger — Erabu/general petition perspective.

Every group requires `B2 Bunrodea Freight Petition Compact: aftermath seen` plus the exact matching settlement.

The B2 declined route is deliberately not publicized because no review chain or terminal settlement was entered.

## Invariants

1. B2 remains sole writer of `B2 Bunrodea Freight Petition Compact:*` state.
2. This A2 consumer contains no `action` blocks and writes no persistent state.
3. No A1 `world:*` state is introduced, read, or mutated.
4. Megasa operational evidence does not become an estate-liability ruling.
5. Erabu petition authority does not erase certified freight facts.
6. The player is not named or converted into Bunrodea legal authority.
7. Declining the original dispute produces no public policy consequence.

## Files

- `data/bunrodea/a2 bunrodea freight practice news.txt`
- `tools/story/validate_a2_bunrodea_freight_practice_news.py`
- `story/A2_BUNRODEA_FREIGHT_PRACTICE_NEWS_HANDOFF_20260819.md`

## Validation contract

The focused validator checks:

- exactly four News groups;
- both settlement gates appear exactly twice;
- every group requires `aftermath seen`;
- two Megasa-scoped and two Bunrodea/Erabu-scoped variants;
- no B2 state writes;
- no `world:*` state use;
- no `action` blocks;
- no declined-route publicization.

Repository-native CI should additionally run the automatically discovered validator, changed-content style gate, focused story contracts, A1 simulation tests, and stock save-load/build smoke.

## Remaining acceptance gates

Before A3 integration:

1. confirm exact-head repository-native story/simulation/style validation succeeds;
2. confirm exact-head stock build/save-load smoke succeeds;
3. observe all four News variants in the actual game;
4. prove no News appears before B2 `aftermath seen`;
5. prove the declined route produces no freight-practice News;
6. verify settlement gating survives an actual-game save/reload;
7. review Bunrodea News rotation and offer/regression behavior.

## A3 integration instruction

Integrate only after the exact candidate head is green and the runtime boundary above is accepted. Preserve the distinction between certified operational freight facts and estate ownership/liability authority exactly as written.
