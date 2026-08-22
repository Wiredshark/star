# A2 Rulei Exposure Practice — current-main restage handoff

Verdict: PARTIAL pending exact-head repository-native validation.

## Authority and isolation

- Authoritative integration base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`.
- Branch: `agent/a2-rulei-exposure-practice-restage-20260822-1306`.
- Historical PARTIAL PR #110 remains untouched.
- Production restage commit: `44a49743b4f994a2ef044ff93fa05e8a3bd37fb7`.
- Strengthened validator commit: `bb315b377e091b6b90b656b4c23c5040528cbd68`.
- No self-integration.

## Player-facing loop

After `B2 Rulei Exposure Accountability: aftermath seen`, Dr. Sena Orlov and Eli Verran ask what evidence-handling practice should survive the original contact dispute. The player may persist:

- bounded-warning discipline, keeping evidence, current status, and review/removal conditions attached;
- consent-and-purpose discipline, requiring audience, fields, purpose, and expiry for secondary use;
- local-only reuse, refusing to universalize an unusually uncertain Rulei-contact case;
- explicit refusal to establish a standing practice.

The three positive routes produce explicitly gated one-shot later reflections. Refusal is persistent but does not arm the Reflection.

## Invariants

- `B2 Rulei Exposure Accountability:*` is read-only.
- No `world:*` simulation state is written.
- All new writes are `A2 Rulei Exposure Practice:*`.
- Observation, current fitness, testimony, interpretation, causation, motive, and permission remain distinct.
- No affirmative claim that Rulei contact caused lasting injury or that the Rulei intended harm.
- No Rulei office, credential, endorsement, medical authority, or representative authority is created.
- Both missions use `offer precedence 9`.
- All five objective-less terminal paths persist state and terminate with `decline`; state-only `accept` is forbidden.
- Reflection rechecks B2 aftermath and explicitly gates each positive route.

## Persistence / compatibility

Existing A2 condition names from historical PR #110 are preserved. Absent conditions remain safe defaults. The only semantic tightening is that an explicit refusal no longer schedules a later reflection, preserving refusal as a true boundary.

## Validation required before READY

Run the repository-native `Fork simulation and story validation` workflow and `Fork save-load integration smoke` workflow on the exact branch head. Do not promote to READY or integrate until both are terminal green. Actual-game manual acceptance remains a separate downstream A3 concern.

## A3 integration boundary

Re-read current `main`, verify ancestry/mergeability, and preserve B2/world read-only ownership, explicit positive-route reflection gating, refusal suppression, offer precedence 9, and the state-only `decline` lifecycle. A3 retains integration authority.
