# A2 Wandering Fleet Continuity Practice — handoff

Verdict: PARTIAL pending exact-head repository-native validation and actual-game acceptance.

- Authoritative integration base: `2f497a46d4787d6081bd4a59c6d7800a3d06c8f2`.
- Branch: `agent/a2-avgi-wandering-fleet-practice-live-20260820-1104`.
- Production commit: `058dc9569450d6c5fab12ee8fe6682b883148706`.
- Validator commit: `4db74c9ab9577e5c0813898c7ba308bcb63a610b`.

## Scope

Consumes the now-integrated B2 Avgi Wandering Fleet Transfer Compact after `aftermath seen`. The player privately chooses to preserve the repair-success/system-restoration boundary, preserve dependency provenance, keep the lesson local, or refuse a standing practice. A later one-shot reflection demonstrates a distinct consequence for each positive route.

## Invariants

- B2 state is read-only; no `world:*` state is written.
- All persistent writes are `A2 Wandering Fleet Continuity Practice:*`.
- Loadkeeper/Fitter remain player-private shorthand, not Avgi offices.
- A successful recipient repair does not prove restored fleet resilience.
- Compatibility does not prove equivalence.
- Emergency borrowing does not erase donor reserve/dependency obligations.
- Local-only practice does not grant borrowed Avgi authority elsewhere.
- Refusal does not arm the later reflection.
- Both briefing and reflection retain the upstream language/refit/not-lost gating.

## Concurrency and recovery

The prior A2 PR #174 targeted this same exact slice but was based on a pre-integration main and explicitly depended on then-unintegrated B1/B2 candidates. It was not modified or raced. This branch restages the slice from the live authoritative main after B2 integration, with the upstream dependency now present in the base itself. Other open A2 Avgi candidates cover allocation and Dissonance evidence, not Wandering Fleet repair/dependency continuity.

The exposed private process service reported four pre-existing service-owned orphan processes. None were touched; that service is not used as Endless Sky repository evidence.

## Validation required

Run the focused validator and repository-native story/simulation/style workflow on the exact final head, plus stock production build/save-load smoke. Actual-game acceptance should exercise all four choices, all three positive reflections, refusal suppression, save/reload between stages, one-shot suppression, and Avgi offer precedence. A3 owns integration.
