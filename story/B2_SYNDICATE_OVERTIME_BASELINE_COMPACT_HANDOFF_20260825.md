# B2 Syndicate Overtime Baseline Compact — handoff

Verdict: PARTIAL pending exact-head repository-native validation.

## Authority
- Repository: `Wiredshark/star`
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-syndicate-overtime-baseline-compact-20260825`
- Production commit: `39496ea9f198fdd6989516d4a30b4403817eb510`
- Focused validator commit: `c0a25cfe08cf2a1feed04f6624d2aa53224d3e9c`

## Scope
Adds Syndicate dockyard supervisor Kellan Voss and pressure-hull welder Rhea Noll. During authoritative A1 labor strain and active crew rotation, Rhea's voluntary emergency overtime is copied into a later performance summary as her ordinary productivity baseline.

Routes:
- keep ordinary baseline separate from exceptional surge output;
- make emergency overtime a current explicit commitment with window, rest, and compensation;
- keep paired ordinary-workload and emergency-contribution/recovery records;
- refusal.

Positive routes schedule a 7–11 day Review. Once A1 labor strain recovers and rotation ends, Review resolves into either a portable workload packet or expiry/reset model. `Rhea Remembers` is one-shot aftermath.

## Dependencies and ownership
- Reads `world: syndicate labor strain` and `world: syndicate labor rotation active` only; A1 remains sole writer.
- Grounded in the existing Syndicate Shift Rotation Archive distinction between temporary surge management, rest, qualification, and durable skilled capacity.
- All writes are `B2 Syndicate Overtime Baseline Compact:*`.
- No `world:*`, A1/A2/B1, credits, reputation, cargo, equipment, ship, fleet, combat, or government-attitude mutation.
- All seven dialogue/state-only terminal paths use `decline`; refusal cannot arm Review.

## Canon and persistence assumptions
Emergency contribution, ordinary workload baseline, explicit current overtime commitment, compensation, rest/recovery obligation, historical credit, and current duty authority are separate facts. Exceptional help can remain credited without becoming a permanent expectation. A later emergency requires a fresh request and fresh consent. This is a local dockyard practice, not centralized Syndicate labor law.

## Validation
Focused validator added at `tools/story/validate_b2_syndicate_overtime_baseline_compact.py`. It proves the three-mission graph, A1 read-only gates, route-local state and 7–11 day scheduling, refusal suppression, settlement-local closure, one-shot aftermath, B2-only writes, seven `decline` terminals, absence of gameplay-objective directives, and core continuity invariants.

Repository-native simulation/story/style and production build/save-load gates must be terminal green on the exact branch head before promotion to READY.

## A3 / B3 integration notes
A3 retains integration authority. Re-read current `main`, active B2 work, ancestry, mergeability, and exact workflow state before integration. Preserve A1 ownership of labor strain/rotation and do not collapse emergency overtime into ordinary performance or permanent availability.
