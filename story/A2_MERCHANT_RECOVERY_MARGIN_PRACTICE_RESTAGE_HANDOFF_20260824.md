# A2 Merchant Recovery Margin Practice — Current-Main Restage Handoff

Verdict: PARTIAL

## Authority and isolation
- Authoritative integration base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`.
- Isolated branch: `agent/a2-merchant-recovery-margin-practice-restage-20260824-0503`.
- Historical branch `agent/a2-merchant-recovery-margin-practice-20260820-0103` is intentionally left untouched.
- No self-integration is permitted from this A2 branch.

## RPG / dynamic narrative loop
The integrated `B2 Merchant Recovery Margin Compact: aftermath seen` state opens a private policy briefing with Imani Vale. The player may preserve unresolved reserve obligations as a continuity rule, require fresh physical-capacity checks as a challenge rule, keep the compact local to participating yards, or refuse a standing interpretation.

Positive choices persist under `A2 Merchant Recovery Margin Practice:*`. A later authoritative `world: merchant repair backlog >= 3` recurrence pressure-tests the remembered practice. Each positive route has separate `world: merchant repair surge` active versus inactive outcomes, yielding six deterministic history-aware consequences. Refusal does not arm the recurrence.

## Invariants
- A1 remains sole writer of `world: merchant repair backlog` and `world: merchant repair surge`.
- B2 remains sole writer of `B2 Merchant Recovery Margin Compact:*` state.
- All new persistent writes are namespaced under `A2 Merchant Recovery Margin Practice:*`.
- A cleared queue is not treated as proof of restored future recovery margin.
- Current physical capacity can invalidate stale operational assumptions without erasing historical evidence.
- Portable records do not create centralized Merchant routing, yard, or reserve authority.
- Both missions use `offer precedence 9`.
- All state-only terminal paths use `decline`; no objective-less mission is left accepted.

## Files
- `data/human/a2 merchant recovery margin practice.txt`
- `tools/story/validate_a2_merchant_recovery_margin_practice.py`
- `story/A2_MERCHANT_RECOVERY_MARGIN_PRACTICE_RESTAGE_HANDOFF_20260824.md`

## Persistence / compatibility
The restage preserves the historical condition namespace and route names (`introduced`, `continuity`, `challenge`, `local`, `declined`, `pressure test seen`) so existing saves using the old isolated candidate retain meaningful state. New route-specific pressure-test outcome flags are additive and deterministic.

## Validation status
Repository-native exact-head workflows have not yet been observed for this restage. Do not claim story/simulation/style, production build, save-load, or runtime success until exact-head evidence exists.

## A3 integration instructions
Integrate only after both repository-native exact-head gates are terminal green. Preserve A1/B2 read-only ownership, the six surge-active/surge-quiet pressure-test outcomes, refusal suppression, current dialogue lifecycle, and Merchant decentralization boundary.
