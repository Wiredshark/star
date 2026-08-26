# B2 Deep Unequal Means Friendship Compact handoff

Verdict: PARTIAL pending exact-head repository-native validation.

- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-deep-unequal-means-friendship-20260825`
- Production: `data/human/b2 deep unequal means friendship compact.txt`
- Focused validator: `tools/story/validate_b2_deep_unequal_means_friendship_compact.py`
- Production commit: `23eb81999a0aa78356260b1e880b5e3a9bdc522f`
- Validator commit: `d9865888ac81e3f23fb07e6b7ef4b138352ec568`

## Character / dynamic content

Adds longtime Deep friends Ilya Sorn and Mera Pell. A growing income gap has started making outsiders interpret ordinary gifts, favors, and time spent helping as patronage or repayment. The player can preserve gifts without debt, require explicit obligations to be named in advance, separate friendship history from actual material obligations, or refuse to referee the relationship.

Three substantive routes schedule a Review after 7-11 days. Review reacts to player wealth at `credits >= 1000000` and changes the conflict from money to time/effort. It resolves into broad reciprocity or explicit promises, followed by one-shot `Mera Remembers`.

## State / ownership

- Reads built-in player `credits` only.
- Writes only `B2 Deep Unequal Means Friendship Compact:*`.
- No `world:*`, B1/A1/A2, reputation, cargo, equipment, ship, fleet, combat, or government-attitude mutations.
- All seven dialogue/state-only terminal paths use `decline`; zero `accept`.
- Refusal cannot introduce the arc or schedule Review.

## Canon boundary

Material generosity, emotional gratitude, actual loans, explicit promises, time spent helping, refusal, and continuing friendship remain separate facts. Unequal means do not automatically create hierarchy or authority. This is one Deep friendship, not Deep law.

## Validation required before READY

Run the repository-native simulation/story workflow, including all focused story validators, A1 state-ownership contracts, and changed-content style. Run the production build/save-load integration workflow. Record exact terminal evidence on the exact candidate SHA before promoting READY.

A3 retains integration authority. No self-integration.
