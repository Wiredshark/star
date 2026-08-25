# B2 Deep Keepsake Friendship — Handoff

Verdict: PARTIAL pending exact-head repository-native validation.

- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-deep-souvenir-friendship-20260825`
- Production commit: `7f6d6df1bb916ad703afa6fa33919c526851e091`
- Focused validator commit: `70fb27524cfaf6b0dc5bd858e74ec11f182e6d39`
- Exact current handoff head: this commit.

## Character / dynamic-content behavior

Returns to the two young Deep locals first seen in `Gift Store Interaction`. Niko Rell and Sana Vey have an old friendship ritual built around laughing at overpriced spaceport souvenirs. Niko's improved income and Sana's departure for a training post turn one expensive farewell present into a conflict over pride, generosity, reciprocity, and whether help creates debt.

Routes:
- keep the old ritual intentionally cheap and equal-access;
- allow generous gifts while explicitly rejecting matching debt;
- separate gifts from actual loans/promises;
- refusal, which leaves the friendship unresolved without arming Review.

Each substantive route schedules a 7–11 day Review. The Review stress-tests the chosen idea against a large favor measured in time rather than money, then resolves into broad reciprocity or explicit-promise boundaries. `Sana Remembers` is the one-shot aftermath.

## Ownership / persistence

- Reads `Gift Store Interaction: declined` only as an existing-culture/encounter hook.
- Writes only `B2 Deep Keepsake Friendship:*`.
- No `world:*`, B1/A1/A2, credits, reputation, cargo, equipment, ship, fleet, combat, or government-attitude mutation.
- All seven dialogue/state-only terminal paths use `decline`.
- Refusal cannot write `introduced`, cannot write substantive route state, and cannot schedule Review.
- Both settlements close Review once and feed one-shot aftermath.

## Canon / continuity

This is deliberately a personal friendship arc rather than a new Deep institution. Material generosity, emotional gratitude, actual loans, explicit promises, time spent helping, refusal, and continuing friendship remain separate facts. A generous act cannot be retroactively converted into a debt merely because one friend later has more money or time to give.

## Validation required before READY

- `python3 tools/story/validate_b2_deep_keepsake_friendship.py`
- repository focused story-validator suite;
- A1 simulation/state-ownership contracts;
- changed-content style;
- production configure/build;
- stock save-load integration smoke;
- exact base/head comparison and final clean diff review.

A3 retains integration authority. Do not self-integrate.
