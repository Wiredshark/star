# A2 Wandering Fleet Continuity Practice — handoff

Verdict: PARTIAL pending exact-head repository-native validation and actual-game acceptance.

- Authoritative integration base observed at run start: `fdaf94f18aaa02abd4e7269196375572cd0fdf9b`.
- Branch: `agent/a2-avgi-wandering-fleet-practice-20260820-1003`.
- Production commit: `224c16bc14275c58a0cedb9246cc3a732ea0f9b0`.
- Validator commit: `65d6d2039fee0a185da2e6b9d0b19c59b91d95db`.

## Scope

Consumes the validated B2 Avgi Wandering Fleet Transfer Compact after `aftermath seen`. The player privately chooses to preserve the repair-success/system-restoration boundary, preserve dependency provenance, keep the lesson local, or refuse a standing practice. A later one-shot reflection demonstrates a distinct consequence for each positive route.

## Invariants

- B2 state is read-only.
- No `world:*` state is written.
- All new persistent writes are `A2 Wandering Fleet Continuity Practice:*`.
- Loadkeeper/Fitter remain player-private shorthand, not Avgi offices.
- A successful recipient repair does not prove restored fleet resilience.
- Compatibility does not prove equivalence.
- Emergency borrowing does not erase donor reserve/dependency obligations.
- Local-only practice does not grant borrowed Avgi authority elsewhere.
- Refusal does not arm the later reflection.

## Concurrency

Live authoritative main and open PR inventory were inspected. Existing open A2 Avgi candidates cover allocation and Dissonance evidence practice. No A2 candidate targets Wandering Fleet repair/dependency continuity. B1 PR #172 and B2 PR #173 are separate upstream candidates and were not modified.

## Validation required

Run the focused validator and repository-native story/simulation/style workflow on the exact final head, plus stock production build/save-load smoke. Actual-game acceptance should exercise all four choices, all three positive reflections, refusal suppression, save/reload between stages, one-shot suppression, and Avgi offer precedence. A3 must also ensure B1 #172 and B2 #173 are integrated or otherwise available before this downstream candidate.

Do not self-integrate.
