# B2 Deep Family Trade Choice Compact handoff

Verdict: PARTIAL pending exact-head repository-native validation.

- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-deep-family-trade-choice-20260825`
- Production: `data/human/b2 deep family trade choice compact.txt`
- Focused validator: `tools/story/validate_b2_deep_family_trade_choice_compact.py`
- Production commit: `7e243fb2631a924f5a940bf4c0513cbfcfed2458`
- Validator commit: `a5da75f95362f81075c5eb08b41c853b11c3625b`

## Character / dynamic-content behavior

Adds Deep shipyard electrician Sela Rook and her adult son Tomas Rook after the player has completed the A2 Career Review later-reader. Tomas was trained in the family workshop but has chosen an independent survey career. The conflict separates inherited skill and family history from present career consent and actual named obligations.

Routes:
- training as family gift unless an explicit adult succession/repayment promise exists;
- explicit closure of real shared obligations without assigning a profession;
- paired training-history and current-career/current-agreement records;
- refusal.

The three substantive routes schedule a 7–11 day Review. Review addresses a copied recommendation that converts truthful training history into a false succession plan. It resolves into either a portable training-and-choice packet or fresh succession consent. `Tomas Remembers` is one-shot aftermath.

## Dependencies / ownership

- Reads `A2 Career Review: later reader seen` only.
- A2 remains read-only.
- Writes only `B2 Deep Family Trade Choice Compact:*`.
- No `world:*`, B1/A1/A2, credits, reputation, cargo, equipment, ship, fleet, combat, or government-attitude mutation.
- All seven state-only terminals use `decline`; zero `accept`.
- Refusal cannot introduce the arc or schedule Review.

## Focused validation contract

The focused validator checks the exact three-mission graph, Deep scope, A2 read-only dependency, route-local writes and one 7–11 day Review schedule per substantive route, refusal suppression, settlement-local closure, one-shot aftermath, B2-only persistence, no objective/material directives, seven declines / zero accepts, and the family-training/current-career/succession-consent continuity boundary.

## Persistence / canon assumptions

Training history, family expectation, demonstrated skill, actual ownership/debt/contract obligations, present career choice, succession consent, and current authority remain separate facts. Teaching a child does not itself create a debt or career assignment; leaving the workshop does not erase genuine training history. This is one household conflict, not Deep labor or inheritance law.

## Validation

Repository-native workflows must be terminal green on an exact production/validator candidate before READY may be claimed.

## A3/B3 integration notes

A3 retains integration authority. Re-read current `main`, ancestry, mergeability, active B1/A2/B2 work, and exact workflow state before integration. Preserve the A2 Career Review dependency as read-only and do not reinterpret this local family resolution as a general Deep institution.
