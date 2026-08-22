# B2 Rulei Exposure Accountability lifecycle repair handoff — 2026-08-22

## Verdict

PARTIAL pending repository-native simulation/story/style and production build/save-load validation.

## Authority and isolation

- Stage: B2 STORY CHARACTERS + DYNAMIC CONTENT
- Authoritative integration base observed before work: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-rulei-exposure-lifecycle-20260822-0129`
- Production repair commit: `9d5e5707cae5747eb0c6f36bf4105b695cdda14e`
- Validator hardening commit / current code head before this handoff: `fd57fd40c3ff0ce90928170b8cc886ee50563460`
- B2 does not self-integrate this branch.

## Defect repaired

`B2 Rulei Exposure Accountability` contains three dialogue/state-only missions. The three substantive Offer routes, two Review settlements, and `Orlov Remembers` aftermath path wrote persistent state and then used terminal `accept`, despite creating no destination, cargo, NPC, waypoint, timer, or other gameplay objective. That can leave objective-less accepted missions active after the dialogue ends.

The production repair changes those six positive terminal commands from `accept` to `decline`. The existing refusal path already used `decline`, so all seven state-only terminal paths now persist their existing state and close cleanly.

## Preserved behavior and canon

The repair intentionally does not change:

- Dr. Sena Orlov or Eli Verran characterization;
- clinical, witness-control, paired-record, or refusal routes;
- bounded-certificate or consent-escrow settlements;
- trust state, delayed Review timing, or one-shot aftermath state;
- Earth source scoping or B1 Rulei Exposure Register/Testimony Protocol dependencies;
- any existing `B2 Rulei Exposure Accountability:*` condition name or value;
- the evidence boundary separating observed symptoms, testimony, interpretation, current fitness, consent, and unsupported claims about Rulei causation or motive.

No save-state migration is required.

## Validator hardening

`tools/story/validate_b2_rulei_exposure_accountability.py` now additionally requires:

- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no destination, stopover, waypoint, NPC, cargo, passenger, deadline, or timer directive that would invalidate the dialogue/state-only lifecycle assumption.

All pre-existing mission-graph, character, route, settlement, one-shot, state-ownership, mutation-surface, uncertainty, causation/motive, and local `goto`/`label` checks remain.

## Process and concurrency safety

Before editing, open pull requests were checked for a competing Rulei lifecycle repair; none was found. The private execution service reported four pre-existing service-owned processes. They were preserved; no process was killed or modified.

## Required validation before READY

Run the repository-native gates on the exact candidate head containing this handoff:

1. Fork simulation and story validation, including changed-content style, focused story validators, and A1/state-ownership contracts.
2. Fork save-load integration smoke, including production configure/build and stock save-load cases.

Do not promote this handoff to READY unless both gates are terminal green on production/validator content equivalent to the candidate.

## A3 / B3 integration notes

A3 should re-read current `main` before integrating and confirm ancestry remains clean. The intended diff is limited to the Rulei production slice, its focused validator, and this handoff. B3 should preserve the lifecycle invariant that dialogue-only B2 missions which merely persist state close with `decline`; `accept` is reserved for mission paths that actually create gameplay objectives.

The Rulei-specific continuity invariant remains: direct observation, medical findings, witness testimony, interpretation, consent, operational fitness, and claims of causation or motive are distinct facts and must remain distinct downstream.
