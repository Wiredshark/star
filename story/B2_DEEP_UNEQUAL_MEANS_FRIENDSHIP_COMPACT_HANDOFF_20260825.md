# B2 Deep Unequal Means Friendship Compact handoff

Verdict: PARTIAL pending terminal exact-head repository-native validation.

- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-deep-unequal-means-friendship-20260825`
- Production: `data/human/b2 deep unequal means friendship compact.txt`
- Focused validator: `tools/story/validate_b2_deep_unequal_means_friendship_compact.py`
- Production commit: `23eb81999a0aa78356260b1e880b5e3a9bdc522f`
- Validator commit: `d9865888ac81e3f23fb07e6b7ef4b138352ec568`
- Initial production/validator/handoff candidate: `7c0dcc806c98591519e1ae96c870b8ba94fb6f23`

## Character / dynamic content

Adds longtime Deep friends Ilya Sorn and Mera Pell. A growing income gap has started making outsiders interpret ordinary gifts, favors, and time spent helping as patronage or repayment. The player can preserve gifts without debt, require explicit obligations to be named in advance, separate friendship history from actual material obligations, or refuse to referee the relationship.

Three substantive routes schedule a Review after 7-11 days. Review reacts to player wealth at `credits >= 1000000` and changes the conflict from money to time/effort. It resolves into broad reciprocity or explicit promises, followed by one-shot `Mera Remembers`.

## State / ownership

- Reads built-in player `credits` only.
- Writes only `B2 Deep Unequal Means Friendship Compact:*`.
- No `world:*`, B1/A1/A2, reputation, cargo, equipment, ship, fleet, combat, or government-attitude mutations.
- All seven dialogue/state-only terminal paths use `decline`; zero `accept`.
- Refusal cannot introduce the arc or schedule Review.

## Validation state

On exact initial candidate `7c0dcc806c98591519e1ae96c870b8ba94fb6f23`:

- `Fork simulation and story validation` run `32915132472` / #638: **IN PROGRESS**.
  - changed-content style job: running.
  - focused simulation/story contracts job: running.
- `Fork save-load integration smoke` run `32915132450` / #623: **IN PROGRESS**.

No nonterminal job is counted as acceptance evidence. READY requires terminal success for focused validators, A1 contracts, changed-content style, production configure/build, and stock save-load smoke on one exact candidate.

## Canon boundary

Material generosity, emotional gratitude, actual loans, explicit promises, time spent helping, refusal, and continuing friendship remain separate facts. Unequal means do not automatically create hierarchy or authority. This is one Deep friendship, not Deep law.

## A3 / B3 boundary

A3 retains integration authority. Re-read current main, open B1/A2/B2 work, ancestry, mergeability, and exact workflow state before integration. Preserve player-credit state as read-only, B2-only persistence, refusal suppression of Review, all seven state-only `decline` terminals, and the gift/favor/explicit-obligation/friendship boundary.

No self-integration.
