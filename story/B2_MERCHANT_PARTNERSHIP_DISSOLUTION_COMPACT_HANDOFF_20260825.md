# B2 Merchant Partnership Dissolution Compact handoff — 2026-08-25

## Authority
- Repository: `Wiredshark/star`
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-merchant-partnership-dissolution-20260825`
- Production commit: `2eb95894209e13ab68a56b1cf708ba96a1b11012`
- Focused validator commit: `41b9a2778d5ae62b8fee0c99d723cc987499990b`
- Current handoff head: this commit
- Verdict: PARTIAL until repository-native simulation/story and save-load workflows are terminal green on the exact production/validator candidate.

## Scope
Adds Merchant repair-brokerage partners Sera Holt and Damin Vey after integrated `B2 Merchant Recovery Margin Compact: aftermath seen`.

Their long-running partnership is ending amicably, but copied vendor records collapse historical partnership, observed work, current ownership, present authority, sponsorship, guarantee, and liability into one status.

Initial routes:
1. fresh authority after a dated separation;
2. bounded former-partner references for work actually observed;
3. paired historical-partnership and current-authority/liability records;
4. refusal.

Positive routes schedule a 7–11 day Review. Review resolves into either:
- portable partnership-status packet; or
- expiry plus fresh acknowledgement.

`Damin Remembers` is the one-shot aftermath reader.

## Ownership / lifecycle
- Reads integrated `B2 Merchant Recovery Margin Compact: aftermath seen` only.
- Writes only `B2 Merchant Partnership Dissolution Compact:*`.
- No `world:*`, A1/A2/B1, credits, reputation, cargo, equipment, ship, fleet, or combat mutation.
- All seven dialogue/state-only terminal paths use `decline`.
- Refusal does not write `introduced`, does not write a substantive route, and does not arm Review.
- Each positive route writes only its route state and schedules exactly one 7–11 day Review.
- Each Review settlement closes Review once and writes only its own settlement.
- Aftermath is one-shot and consumes either settlement.

## Character / canon boundary
Historical partnership, completed shared work, former-partner reference, current ownership, present authority, sponsorship, guarantee, unresolved liability, separation date, and closure are separate facts.

A former partner may truthfully describe work personally observed without becoming a present sponsor or guarantor. Ending the partnership does not erase genuine shared history. Repetition of an old vendor profile does not make historical authority current again.

This is a local Merchant business practice, not centralized Merchant contract law or a universal partnership code.

## Files
- `data/human/b2 merchant partnership dissolution compact.txt`
- `tools/story/validate_b2_merchant_partnership_dissolution_compact.py`
- `story/B2_MERCHANT_PARTNERSHIP_DISSOLUTION_COMPACT_HANDOFF_20260825.md`

## Process safety
The exposed private service reported four pre-existing service-owned orphan processes. They were observed and preserved; none were killed or modified. No unrelated workspace is treated as authoritative Endless Sky runtime evidence.

## Validation still required
Trigger and inspect exact-candidate repository-native gates:
- Fork simulation and story validation;
- Fork save-load integration smoke.

READY only after both are terminal green on the exact production/validator candidate (or a later candidate whose production/validator changes are explicitly revalidated).

## A3 / B3 notes
A3 retains integration authority. Do not self-integrate. Re-read current `main`, open B1/A2/B2 work, ancestry, mergeability, and exact workflow state immediately before integration.

B3 should preserve the distinction among historical partnership, current authority, reference, sponsorship, guarantee, liability, and explicit closure.
