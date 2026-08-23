# A2 Heliarch Evidence Practice — current-main restage handoff

Verdict: PARTIAL pending exact-head repository-native validation.

Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`

Branch: `agent/a2-heliarch-evidence-practice-restage-20260822-2204`

Production restage: `3f7e599e4f4b8f446c8a817165713c36c27162d8`

Strengthened validator: `541f02536d03f6c4431d8825627ef070f669bc4c`

Historical PR #104 remains untouched.

## Scope
After integrated `B2 Heliarch Evidence Handoff: aftermath seen`, the player privately adopts provenance-first practice, independent-challenge practice, local-only reuse, or explicit refusal. The three positive routes persist and drive explicitly gated one-shot later reflections. Refusal persists but does not arm the later reflection.

## Invariants
- `B2 Heliarch Evidence Handoff:*` remains read-only.
- No `world:*` writes.
- All writes are `A2 Heliarch Evidence Practice:*`.
- Derived analysis remains distinct from source evidence; provenance and independent falsification remain separate tools.
- Both state-only missions use `offer precedence 9`.
- All five objective-less terminal paths use `decline`; no state-only `accept` remains.
- Later Reflection rechecks B2 aftermath and explicitly gates method, challenge, and local routes.
- Refusal does not arm Reflection.
- No Heliarch representative, investigator, clerk, credential, office, endorsement, or procedural authority is created.

## Validation required
Run exact-head `Fork simulation and story validation` and `Fork save-load integration smoke`. Promote to READY only when both are terminal green. Do not claim manual actual-game acceptance unless separately executed.

## A3 boundary
Re-read current `main`, verify ancestry/mergeability, preserve B2/world read-only ownership, explicit route gating, refusal suppression, offer precedence 9, and state-only `decline` lifecycle. A2 does not self-integrate.
