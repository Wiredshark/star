# B2 Hicemus Access Compact handoff — 2026-08-19

## Stage / verdict

- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Verdict: PARTIAL — simulation/story/style validation is green on the exact repaired production/validator head; save-load integration smoke is still in progress
- Required dependency: B1 Hicemus contact institutions at `3295dbf520b011510ac9fd0ce7db4261efde8629`
- Isolated branch: `agent/b2-hicemus-access-compact-20260819-1627`
- Production commit: `211cf8e15e9a50b2663191d2c7159b5466b7db4f`
- Focused-validator commit: `e4a9ae3a61bbf148fdb06f6bc8e8a9bb493da3cd`
- Privacy-continuity repair commit: `9bd89b7a9c9ebccc14a474357443fd60bb7fab35`
- Exact production/data/validator head validated by simulation/story workflow: `9bd89b7a9c9ebccc14a474357443fd60bb7fab35`

## Scope

Adds a three-mission persistent Hicemus character arc consuming B1's `Hicemus History: Station Access Archive` after formal human contact.

The player privately calls two recurring Incipias the **Dispatcher** and **Maintainer**. These are explicitly player-facing shorthands, not canonical names, titles, offices, or evidence about the political meaning of the Hicemus/Conlatio division.

The initial dispute concerns a damaged transfer lock that forces freight, residential movement/privacy, maintenance, and emergency access to compete for station corridors. The player may choose:

1. emergency-route priority;
2. capacity-limited freight with hard emergency preemption;
3. a temporary access compact with cargo windows, emergency override, and explicit review/expiry;
4. refusal.

A later Review remembers the route and exposes second-order interactions among multiple individually reasonable temporary exceptions. It resolves into exactly two persistent institutional outcomes:

- **portable access record** — every copied exception carries purpose, capacity, emergency priority, expiry, and closure/review responsibility;
- **shared conflict table** — departments retain local discretion, but temporary exceptions are checked against shared emergency paths, junction capacities, and simultaneous-load limits.

`Maintainer Remembers` is the one-shot later reader.

## State ownership / persistence

All new writable conditions are namespaced under `B2 Hicemus Access Compact:*`.

B2 reads but does not write:

- `Incipias: Help The Stranded 2: done`;
- `Hicemus History: Station Access Archive: offered`.

The slice does not mutate A1 `world:*` state, credits, reputation, cargo, outfits, ships, fleets, combat rating, B1 state, or unrelated campaign conditions.

## Canon / continuity assumptions

The slice is grounded in B1's station-access history: orbital routing must balance cargo, visitors, maintenance, emergency access, safety, and privacy, and old routing maps preserve prior compromises.

Preserve these boundaries:

- Dispatcher/Maintainer are private player shorthand only.
- The slice does not define why Hicemus and Conlatio are divided.
- It does not assert a new Hicemus constitution, centralized station bureaucracy, or faction-wide legal code.
- Temporary access records and conflict tables are practical station-operation mechanisms, not evidence of political unification or universal Incipias standards.

## Files changed

- `data/incipias/b2 hicemus access compact.txt`
- `tools/story/validate_b2_hicemus_access_compact.py`
- this handoff file

## Validation evidence

Focused validator command implemented:

```text
python3 tools/story/validate_b2_hicemus_access_compact.py "data/incipias/b2 hicemus access compact.txt"
```

The first exact-head `Fork simulation and story validation` attempt on `4fb2012d53cc4f7c41b0faa6b1707171a8121ed0` failed only because the focused validator required the B1 station-access continuity concept `privacy` while the production scene expressed the residential constraint without that literal term. The production text was repaired to explicitly preserve residential privacy in commit `9bd89b7a9c9ebccc14a474357443fd60bb7fab35`.

On exact repaired head `9bd89b7a9c9ebccc14a474357443fd60bb7fab35`:

- `Fork simulation and story validation` run `32298999592` / run #124: **SUCCESS**.
- `Changed fork content style`: **SUCCESS**.
- `Focused simulation and story contracts`: **SUCCESS**.
- all focused story validators, including `validate_b2_hicemus_access_compact.py`: **SUCCESS**.
- A1 simulation/state-ownership contract tests: **SUCCESS**.

Exact repaired-head `Fork save-load integration smoke` run `32298999544` / run #113 is still **in progress**. No production build/save-load PASS is claimed until that run reaches terminal green.

The focused validator checks:

- exact three-mission graph;
- recurring Dispatcher/Maintainer private-shorthand continuity;
- Hicemus source scoping and required B1/contact gates;
- three substantive routes plus refusal;
- exactly two terminal settlement writes;
- one-shot later reader;
- B2-only persistent writes;
- no material/world/reputation state mutation;
- local `goto` / `label` integrity;
- station-access continuity including cargo, emergency access, capacity, temporary routing, and privacy;
- exception-accountability invariants;
- explicit preservation of uncertainty around the Hicemus/Conlatio political division.

## Remaining validation before READY

1. exact repaired-head `Fork save-load integration smoke` must reach terminal SUCCESS, including production configure/build and stock persistence smoke;
2. the B1 dependency must itself reach an acceptable terminal validation state before integration;
3. actual-game acceptance should exercise all three substantive routes, refusal, Review routing, both terminal settlements, one-shot aftermath behavior, and save/reload between stages.

No PASS should be claimed for any gate that has not actually completed.

## A3 integration order

Integrate/accept the B1 Hicemus contact-institutions dependency first. Then review this B2 branch against the then-current `main`. Do not self-integrate from B2.

## A2 / B3 consumption notes

Later A2/B3 work may consume these states for visitor logistics, emergency-access consequences, station privacy/cargo tradeoffs, or character reactions to whether temporary exceptions remain accountable. Preserve B2 state ownership and the distinction between practical routing institutions and political authority.
