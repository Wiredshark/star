# B2 Deep Bereavement Debrief Compact Handoff — 2026-08-25

Verdict: PARTIAL pending exact-candidate repository-native validation.

- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-deep-bereavement-debrief-compact-20260825`
- Production commit: `977986912ae0ac90b97f69d810a26eb647618c9f`
- Focused validator / current candidate: `543ff13c4745c84f5613ecff1dd6672b2455d277`

## Behavior
Adds a persistent Deep character sequel for Mara Venn plus Lio Vos, sister of escort pilot Iren Vos. The conflict separates legitimate operational learning after a fatal escort incident from a family's private last message and from unsupported claims about motive.

Routes: operational facts only; purpose-bound consent for any family-approved excerpt; paired technical incident and family/private records; refusal. Three substantive routes schedule Review after 7–11 days. Review resolves into either a portable debrief-boundary packet or dual-purpose archives. `Lio Remembers` is one-shot aftermath.

## Dependencies / ownership
The Offer requires one completed A2 Deep Debrief later-reader outcome: field contact, security contact, review contact, or respected refusal. Those A2 conditions are read-only. Every new write is `B2 Deep Bereavement Debrief Compact:*`. There are no `world:*`, A1/A2/B1, credits, reputation, cargo, equipment, ship, fleet, combat, or government-attitude mutations.

All seven dialogue/state-only terminal paths use `decline`; refusal cannot schedule Review.

## Focused validation
`tools/story/validate_b2_deep_bereavement_debrief.py` proves:
- exact three-mission graph and Deep source scope;
- all four A2 completion gates are read-only and each appears exactly once;
- exactly three substantive routes, one refusal, two Review settlements, and one aftermath write;
- each substantive route writes only its own route state, schedules Review exactly once for 7–11 days, and terminates once;
- refusal writes no route state and cannot arm Review;
- each settlement closes Review exactly once and writes only its own settlement;
- aftermath consumes either settlement, is one-shot, and uses the dual settlement a second time only for settlement-specific dialogue;
- all writes remain B2-owned and no gameplay objective directives are introduced;
- private message, technical finding, consent scope, interpretation of motive, expiry/correction, and local-vs-universal authority remain distinct.

## Continuity / canon
A private family message is not automatically training evidence or proof of motive. Operational telemetry and observed actions may support a complete safety finding without claiming a complete biography. Family approval, when given, is purpose/audience/time bounded rather than permanent. This is a local Deep review practice, not universal Deep Security law.

## A3 / B3 integration notes
A3 should integrate only after both repository-native workflows pass on an exact production/validator candidate. Preserve A2 Deep Debrief state as read-only and preserve all `B2 Deep Bereavement Debrief Compact:*` persistence names. No self-integration was performed.
