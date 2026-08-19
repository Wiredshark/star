# B2 Paradise Service Compact Handoff — 2026-08-18

## Verdict

**PARTIAL / specialist production candidate — not yet A3-ready.**

The focused structural validator executed successfully in a fresh isolated clone of this exact branch. Normal Endless Sky content-style/parser/build/runtime/save-load validation is still required before integration.

## Repository authority and ancestry

- Repository: `Wiredshark/star`
- Authoritative `main` observed at run start: `d611ce688997d3847ac303c229f64b80663db26c`
- Parent B1 Paradise institutional-history branch: `agent/b1-paradise-institutions-20260818-1720`
- Parent B1 commit: `d4e1daeeb1570e73e443e1404da6a6fe88922300`
- B2 branch: `agent/b2-paradise-service-compact-20260818-1728`
- B2 production commit: `4b666e5a8b0c71f47276714bc70e41e5b1f2f420`
- B2 validator commit: `2070d55d741797871580d4fd268f16bc9fb4a1ce`

## Non-overlap / concurrency decision

Existing open B2 work already covers:

- Broken Compact / Republic ownership and legal-state relationships;
- Far North Yard Legacy / apprenticeship and repair-capacity relationships;
- Syndicate Charter Obligations / corporate public-service obligations.

A new B1 Paradise institutional-history handoff was available and was not yet consumed by B2. This slice therefore targets a separate Paradise service-district / public-private transit problem rather than racing or duplicating existing B2 candidates.

## Character and dynamic-content behavior

The production file `data/human/b2 paradise service compact.txt` introduces:

- **Iona Mercer** — municipal transit coordinator;
- **Celia Voss** — estate management consortium liaison.

The initial dispute consumes the B1 `Paradise Service District Museum` theme: workers depend on service infrastructure that may still be privately owned or operated even after the surrounding district functions as a municipality.

Persistent initial routes:

1. Mercer / protect public worker access;
2. Voss / preserve private control and explicit operating responsibility;
3. compact / separate guaranteed access from funding and operating ownership;
4. refusal / player declines to participate.

Later review resolves to one of two terminal persistent settlements:

- `B2 Paradise Service Compact: settlement municipal corridor`
  - the municipality owns the late transit schedule and compensates the estate for defined access/security costs;
- `B2 Paradise Service Compact: settlement shared service compact`
  - the estate keeps operating the gate while the municipality funds a defined public-service window under a reviewable compact.

`B2 Paradise Service Compact: Mercer Remembers` is a later named-character reader for both terminal states and records one-shot aftermath completion.

## State / persistence model

This slice intentionally uses only stock mission/global conditions already established by Endless Sky content patterns. It introduces no new serialization authority and no C++ state owner.

Important conditions include:

- `B2 Paradise Service Compact: introduced`
- `B2 Paradise Service Compact: declined`
- `B2 Paradise Service Compact: route mercer`
- `B2 Paradise Service Compact: route voss`
- `B2 Paradise Service Compact: route compact`
- `B2 Paradise Service Compact: mercer trusts player`
- `B2 Paradise Service Compact: voss trusts player`
- `B2 Paradise Service Compact: reviewed`
- `B2 Paradise Service Compact: settlement municipal corridor`
- `B2 Paradise Service Compact: settlement shared service compact`
- `B2 Paradise Service Compact: aftermath seen`

The two terminal settlement conditions are intended to be mutually exclusive because only one review choice can be accepted.

## Validation actually executed

A fresh isolated clone of `agent/b2-paradise-service-compact-20260818-1728` at exact head `2070d55d741797871580d4fd268f16bc9fb4a1ce` was created on the private execution host and the focused validator was run:

```text
python3 tools/story/validate_b2_paradise_service_compact.py
```

Observed result:

```text
PASS: B2 Paradise Service Compact structure validated
PASS: missions=3
PASS: named_characters=2
PASS: initial_routes=3 + refusal
PASS: terminal_settlements=2
PASS: later_reader=Mercer Remembers
PASS: persistence_model=stock mission/global conditions
```

The validation clone was temporary and removed after the run. No unrelated repository worktree or process was touched.

## Validation not yet proven

An additional attempt to run the repository-wide content style checker on a fresh clone timed out before a terminal result was returned. Therefore **no style-check pass is claimed**.

The following remain required before A3 promotion/integration:

1. normal repository content-style validation;
2. Endless Sky data/content parser or equivalent build-time content-load validation;
3. configured build/regression gate appropriate to human mission content;
4. runtime smoke-load on a Republic Paradise world;
5. route exercise for Mercer / Voss / compact / refusal;
6. review exercise proving exactly one terminal settlement is written;
7. save/load after initial route and after terminal settlement;
8. later-reader exercise proving both terminal states reach `Mercer Remembers` and the one-shot aftermath gate works.

## Canon / content assumptions

- Parent B1 history is deliberately institutional/general and establishes the service-district public/private infrastructure tension without hard dates or named historical figures.
- B2 introduces modern named characters without rewriting B1 history.
- No credits, reputation, cargo, combat, outfit, or campaign progression mutation is intended.
- Source scoping remains Republic + `paradise` + not station.

## A3 integration notes

Do not integrate this B2 branch before the remaining parser/style/runtime/save-load gates pass.

If promoted later, preserve ancestry after the Paradise B1 history commit `d4e1daeeb1570e73e443e1404da6a6fe88922300`, because this B2 slice explicitly consumes that institutional framing.

## B3 continuity notes

B3 should verify future Paradise class/service-labor content does not simultaneously claim that service roads are wholly public or wholly private by default. This slice deliberately treats ownership, operating responsibility, public dependence, and funding as separate dimensions.
