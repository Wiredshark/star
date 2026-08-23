# B2 Coalition Rescue Handoff Compact handoff

Verdict: PARTIAL pending repository-native validation.

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative base observed: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-coalition-rescue-handoff-compact-20260823`
- Production commit: `266fb6466409a223a783b0a1f86575ef0dc008fd`
- Focused validator commit: `cb4a139ee1cc002f8444ff3f500c7e147aba325e`
- Integration authority remains A3. Do not self-integrate.

## Character / dynamic-content behavior

This slice consumes the institutional premise of the B1 `Coalition Rescue Compact Archive`: cross-jurisdiction rescue depends on shared distress categories, medical summaries, towing conventions, and survivor transfer procedure without implying a centralized Coalition rescue authority.

It introduces recurring rescue coordinator **Lira Senn** and civilian tug captain **Oren Vale**. Their conflict is whether emergency handoffs preserve a survivor's continuing consent, treatment context, family-contact limits, and unresolved care without making the emergency record too large to use under pressure.

The Offer has three substantive routes plus refusal:

1. continuity-first handoff;
2. operational-first summary with durable source link and limits;
3. paired emergency and survivor-continuity records;
4. refusal to generalize one case into Coalition-wide authority.

Each substantive route schedules a delayed Review after 7-11 days. The Review resolves into one of two persistent models:

- portable survivor-status packet;
- expiry-and-reconciliation.

`Oren Remembers` is the one-shot aftermath reader.

## State ownership and lifecycle

- All writes are `B2 Coalition Rescue Handoff Compact:*`.
- No `world:*`, credits, reputation, cargo, equipment, ship, fleet, combat, B1, or campaign state is mutated.
- All seven dialogue/state-only terminal paths use `decline`; no objective-less accepted missions are introduced.
- No save-state migration is required because this is additive namespaced state.

## Continuity invariants

- Physical transfer is not equivalent to completed care.
- Emergency medical facts, consent scope, family-contact permission, unresolved follow-up, and current responsibility are separate facts.
- A short emergency summary may be operationally necessary without becoming the entire survivor record.
- Copied emergency information can expire; consent or unresolved-care state does not silently expire with it.
- Shared rescue procedure remains distributed Coalition interoperability, not a centralized rescue government.

## Validation required before READY

Run repository-native validation on the exact branch head:

- `python3 tools/story/validate_b2_coalition_rescue_handoff_compact.py`
- fork simulation/story validation workflow, including changed-content style and A1/state-ownership regressions;
- production Endless Sky configure/build;
- stock save-load integration smoke.

Promote to READY only after both repository-native workflows are terminal green on an exact production/validator candidate.

## A3 / B3 notes

A3 should re-read current `main` immediately before integration and verify no conflicting Coalition rescue/consent slice has landed. B3 should preserve the distinction between emergency handoff, survivor consent, private contact information, continuing care responsibility, and political authority.
