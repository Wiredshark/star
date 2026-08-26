# B2 Rook Confidential Teaching Compact — Handoff

Verdict: **PARTIAL pending exact-head repository-native validation.**

## Authority / isolation

- Repository authority: `Wiredshark/star`
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-rook-confidential-teaching-compact-20260826`
- Production commit: `5595504ca4de7a158c700783789296b33edf0fa3`
- Focused validator commit: `cdabaf4e0f52ab90e0f0262cf630fd1c3a6fb5c1`
- A3 retains integration authority. Do not self-integrate.

## Character / dynamic-content slice

Sequel to `A2 Rook Mediation: later reader seen`.

Returns port mediator **Imani Rook** and introduces junior mediator **Nora Bell**. The resolved convoy-loss case is useful as training material, but some of its reasoning depended on confidential settlement context. The conflict is whether a closed case can teach future mediators without turning private settlement material into reusable evidence.

Initial approaches:

1. anonymized abstraction: teach the reasoning path while confidential settlement facts remain sealed;
2. purpose-bound consent: identifiable excerpts require explicit audience/purpose permission;
3. paired records: complete sealed case plus separately authored teaching material that cites only what may travel;
4. refusal: leave the closed case out of training entirely.

The three substantive routes schedule a delayed Review after 7–11 days. Review stress-tests the chosen rule against contextual re-identification and downstream audience drift. It resolves into either:

- **re-identification review** before teaching material becomes portable; or
- **consent-bound excerpts** carrying audience, purpose, expiry, and withdrawal state.

`Bell Remembers` is the one-shot aftermath reader.

## Dependencies / ownership

- Reads `A2 Rook Mediation: later reader seen` and route outcome state read-only.
- Writes only `B2 Rook Confidential Teaching Compact:*`.
- No A2 or `world:*` writes.
- No credits, reputation, cargo, equipment, ship, fleet, combat, or government-attitude mutation.
- All seven dialogue/state-only terminal paths use `decline`; zero `accept`.
- Refusal cannot introduce the arc or schedule Review.

## Focused validation contract

`tools/story/validate_b2_rook_confidential_teaching_compact.py` checks:

- exact three-mission / one-event graph;
- Imani Rook and Nora Bell continuity;
- A2 inputs are read-only;
- route-local writes and exactly one 7–11 day Review schedule per substantive route;
- refusal suppression of introduced/route/schedule state;
- exact Review gates and route branches, with abstract as deliberate fallthrough;
- settlement-local writes and one Review closure per settlement;
- exact two-settlement aftermath eligibility and one-shot aftermath;
- seven `decline` / zero `accept` state-only terminals;
- no gameplay-objective directives or material/reputation mutations;
- local `goto`/`label` integrity;
- confidentiality, re-identification, audience/purpose/expiry/withdrawal continuity boundaries.

## Canon / continuity assumptions

A closed settlement can remain historically true while its confidential material remains non-portable. Redaction alone is not guaranteed anonymity when route, equipment, timing, or quotations can re-identify a participant. Consent to settle is not automatically consent to become training material; permission to use an excerpt is audience/purpose/time bounded. This is one Republic mediation-training practice, not universal Republic law.

## Remaining acceptance gates

Before READY:

- repository-native `Fork simulation and story validation` must be terminal green on the exact candidate;
- changed-content style and all focused story validators must pass;
- A1 state-ownership/simulation contracts must pass;
- repository-native production configure/build and stock save-load integration smoke must be terminal green;
- final diff/ancestry/mergeability must be checked against current authoritative main.
