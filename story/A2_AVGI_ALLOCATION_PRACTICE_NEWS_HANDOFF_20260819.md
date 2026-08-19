# A2 Avgi Allocation Practice News Handoff — 2026-08-19

## Verdict

PARTIAL / specialist production candidate. Repository-native validation must pass on the exact candidate head before A3 integration, and actual-game News visibility/rotation remains a separate acceptance boundary.

## Authority and isolation

- Authoritative integration base: `main` @ `709fb2bde2c63fdcaf1fe8d761427d6096220e28`
- Isolated branch: `agent/a2-avgi-allocation-practice-news-20260819-0603`
- Production commit: `bcf46b1f0113810599a855b9a5d0250a0dc0c62e`
- Validator commit: `0a4914ac349fb4243bbaf389711b110835712de7`

This run inspected current open A2 pull requests before authoring. Existing A2 candidates cover Republic review practice, Syndicate maintenance policy, Free Worlds joint-corridor doctrine, and Republic customs-precedent News. No open A2 Avgi slice was found.

## Implemented loop

This candidate is a read-only player-facing consequence layer over the integrated B2 Avgi Allocation Compact.

The upstream B2 arc allows the player to help Verdigris and Ochre establish either:

1. a `settlement public emergency ledger`; or
2. a `settlement dual threshold`.

After B2's `aftermath seen` reader resolves, this A2 layer exposes four Consonance-port News groups:

- public-ledger civilian/allocation perspective;
- public-ledger Twilight Guard perspective;
- dual-threshold civilian/review perspective;
- dual-threshold Twilight Guard perspective.

The public consequences therefore require both a resolved B2 aftermath and the exact durable settlement that produced them.

## Invariants

- B2 remains sole owner/writer of `B2 Avgi Allocation Compact:*` state.
- This candidate has no `action` blocks and writes no persistent state.
- It introduces no A1 `world:*` state and does not write any simulation authority.
- The B2 declined path remains private: no News group consumes or publicizes it.
- All News remains gated by `language: Avgi`, scoped to `Avgi (Consonance)` ports, and excluded from `aberrant siege` locations to match surrounding stock Avgi News conventions.
- No player name or explicit public attribution is emitted.

## Files changed

- `data/avgi/a2 avgi allocation practice news.txt`
- `tools/story/validate_a2_avgi_allocation_practice_news.py`
- `story/A2_AVGI_ALLOCATION_PRACTICE_NEWS_HANDOFF_20260819.md`

## Focused validation contract

Run:

```bash
python3 tools/story/validate_a2_avgi_allocation_practice_news.py
```

The validator requires exactly four News groups, exact B2 aftermath/settlement gates, Avgi-language and Consonance location gates, no action blocks, no B2-state writes, no `world:*` authority tokens, and no declined/refusal publicization.

## Remaining A3 gates

1. Confirm the exact candidate head passes repository-native story/simulation/style validation.
2. Confirm the exact candidate head passes the stock save-load/build smoke workflow if triggered.
3. Observe each of the four News groups in the actual game under its exact B2 settlement state.
4. Negative proof that none appear before `B2 Avgi Allocation Compact: aftermath seen`.
5. Negative proof that the B2 declined path produces no allocation-practice News.
6. Save/reload proof that B2 settlement/aftermath gates continue to expose the same News after reload.
7. Avgi News rotation/regression review alongside existing merchant/politician/military/safety-advisory groups.

Do not self-integrate. A3 should preserve the read-only ownership boundary and only integrate an exact candidate head with passing required validation.
