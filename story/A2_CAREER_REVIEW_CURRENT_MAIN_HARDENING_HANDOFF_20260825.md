# A2 Career Review current-main hardening handoff - 2026-08-25

## Verdict

PARTIAL pending exact-head repository validation.

## Authority

- Repository: `Wiredshark/star`
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-career-review-hardening-20260825-2104`
- Production hardening: `c36ac34113d5f662ed4ff1d26ef0e921da27d966`
- Strengthened validator: `6905c987be7e32664c90af233a4b90f2de88a3ed`

## Scope

Hardens the already-integrated A2 Career Review rather than duplicating its RPG content. Nia Calder continues to ask the player which command principle their career has actually produced: protect the margin, use force only to prevent worse loss, keep options open, or refuse the assessment. The later reader preserves route-specific memory and explicitly respects refusal.

## Hardening

- Adds the canonical 2026 Endless Sky GPL content header to the integrated production file.
- Preserves every existing A2 Career Review condition name and value for save compatibility.
- Preserves `offer precedence 8` and the existing state-only `decline` lifecycle.
- Strengthens the focused validator to prove both missions, all three positive routes, explicit later-reader route gates, refusal persistence/respect, read-only built-in origin/combat inputs, A2-only write namespace, zero objective-less `accept`, no gameplay/material directives, and trailing newline.

## Ownership / invariants

- `start:*` origin state is read-only.
- Built-in `combat rating` is read-only.
- All writes remain `A2 Career Review:*`.
- A remembered command principle remains player history/evidence, not Pilot Guild doctrine or Republic law.
- Refusal remains refusal and is not converted into a hidden category.
- No credits, reputation, cargo, equipment, fleet, combat, destination, waypoint, passenger, or objective mutation is introduced.

## Persistence implications

No migration is required. Existing condition names and route meanings are unchanged.

## Validation required

Run both repository-native exact-head gates after this handoff commit:

- `Fork simulation and story validation`
- `Fork save-load integration smoke`

Do not promote to READY unless both are terminal green on the exact candidate head.

## A3 boundary

A3 retains integration authority. Re-read current `main`, active A2/B2 work, ancestry, mergeability, and exact workflow state before integration. Preserve save-compatible state names, read-only built-in inputs, refusal semantics, `offer precedence 8`, and the state-only decline lifecycle. No self-integration.
