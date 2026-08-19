# B2 South Convoy Compact handoff — 2026-08-18

## Verdict

**PARTIAL / specialist production candidate — not yet A3-ready.**

The focused structural validator is committed, the exact branch files were fetched back from GitHub, and the base-to-head diff is isolated. However, this automation run does not have an executable `Wiredshark/star` Endless Sky checkout. The exposed private execution host is bound to `Wiredshark/fallout-test`, and a separate container clone attempt could not resolve `github.com`. Therefore no executable validator, content-style, parser/build, runtime, or save/load pass is claimed.

## Repository state

- Authoritative `main` observed at run start: `d611ce688997d3847ac303c229f64b80663db26c`
- Parent B1 branch: `agent/b1-south-institutions-20260818-1821`
- Parent B1 head / exact B2 base: `633b625514ae3aace38ce9f6d511e48274ccb39c`
- B2 branch: `agent/b2-south-convoy-compact-20260818-1824`
- Production-data commit: `92c5b340ae722f3d0b7d2ce71ab5e59b2f00c100`
- Focused-validator commit: `44c843bcb4be649d195edede0b1b1452575e8b4a`

At validator head, GitHub compare reports this branch exactly 2 commits ahead of the B1 parent with no behind commits and only these additions:

- `data/human/b2 south convoy compact.txt` — 136 additions
- `tools/story/validate_b2_south_convoy_compact.py` — 76 additions

## B1 dependency consumed

This slice consumes **South Convoy Memorial** from `data/human/south history conversations.txt`. B1 establishes that southern merchant convoys evolved from improvised mutual-aid agreements into scheduled departures, shared route information, emergency repair funds, and rescue obligations.

B2 turns that institutional history into a present-day named-character dispute rather than creating another disconnected regional vignette.

## Character / dynamic-content behavior

### Named characters

- **Mira Dane** — southern convoy dispatcher who argues that coordinated departures only work if captains accept explicit rescue obligations.
- **Tomas Reeve** — independent merchant captain who accepts mutual aid but objects to discovering an obligation only after an emergency begins.

### Initial routes

`B2 South Convoy Compact: Offer` provides three substantive routes plus refusal:

1. back Dane and binding rescue obligations for scheduled convoy participants;
2. back Reeve and voluntary rescue for independents;
3. propose a tiered/public pledge system before departure;
4. decline involvement.

The three substantive routes write persistent stock global conditions, including route-specific trust state.

### Review / consequences

`B2 South Convoy Compact: Review` consumes the Dane and Reeve routes explicitly; the pledge route intentionally uses the neutral fallthrough. The player then chooses one of two terminal institutional outcomes:

- `settlement standing rescue compact`
  - coordinated departures carry a clearly published rescue obligation;
  - truly independent departures remain outside the compact;
- `settlement public rescue registry`
  - rescue remains voluntary;
  - every captain publishes rescue status before departure so dispatchers and other crews can plan around explicit commitments.

Both outcomes set `reviewed` and persistent outcome state using stock mission/global conditions only.

### Later reader

`B2 South Convoy Compact: Reeve Remembers` consumes either terminal settlement and records one-shot aftermath state. Its text changes depending on whether the compact or public registry became authoritative.

## Persistence / ownership assumptions

- Uses only stock mission/global conditions; no new engine-side state authority.
- No direct credits, payment, cargo, outfit, combat, or reputation mutation.
- No hard chronology or named historic founder is added.
- B1 owns the general historical observation; B2 owns the named present-day character dispute and its local persistent outcome conditions.
- The two terminal settlement conditions are intended to be mutually exclusive because only one Review outcome path can execute before `reviewed` is set.
- Refusal prevents the Offer mission from immediately reappearing via `declined`.

## Validation evidence

### Performed

- Recovered live repository metadata and open B1/B2/A2 work from GitHub before selecting scope.
- Confirmed this is non-overlapping with active/previous B2 slices: Broken Compact, Far North Yard Legacy, Syndicate Charter Obligations, and Paradise Service Compact.
- Fetched the exact committed production file and focused validator back from the B2 branch.
- GitHub compare at `44c843bcb4be649d195edede0b1b1452575e8b4a` confirms exactly 2 commits ahead of B1 base and only the two intended files changed.
- Inspected exposed private execution host: its repository remote is `Wiredshark/fallout-test`, not `Wiredshark/star`; unrelated service processes were left untouched.
- Attempted a separate public clone for executable validation; DNS resolution for `github.com` failed in that environment.

### Committed focused validator

`python3 tools/story/validate_b2_south_convoy_compact.py`

The validator checks:

- exactly 3 B2 missions;
- both named characters;
- 3 persistent initial routes plus refusal;
- south/non-station source scoping;
- no direct material/reputation/combat reward mutation;
- all explicit conversation `goto` targets have local labels;
- Dane/Reeve review routing plus intentional pledge fallthrough;
- exactly 2 terminal settlement writes;
- later reader consumes both outcomes;
- settlement variables are not written during the Offer mission.

**Execution status: not executed in an authoritative Endless Sky checkout during this run. Do not treat the presence of the validator as a pass.**

## Required acceptance before A3 integration

Run from a real checkout of the exact final B2 head:

1. `python3 tools/story/validate_b2_south_convoy_compact.py`
2. the repository's normal content-style validator with dependencies installed;
3. the normal Endless Sky data/content parser or build gate;
4. smoke-load a qualifying southern non-station world and exercise all 4 Offer responses;
5. exercise Dane, Reeve, and pledge Review routing;
6. verify exactly one terminal settlement is set after Review;
7. verify `Reeve Remembers` renders the correct outcome-specific text once;
8. save after Offer, reload, and verify route state persists;
9. save after Review, reload, and verify terminal settlement plus aftermath gating persists;
10. verify no unrelated conditions, mission progression, credits, cargo, reputation, or combat state changes.

## A3 integration notes

- Review/integrate only after the parent B1 South institutional-history commit or equivalent content is present so the thematic dependency is preserved.
- The B2 data file does not technically reference the B1 mission condition, so Git ancestry is the current dependency mechanism.
- No known ordering dependency on other B2 regional slices.
- If A3 combines several B2 candidates, watch global-condition naming for accidental duplicate concepts; this slice namespaces all state under `B2 South Convoy Compact:`.

## B3 continuity notes

- Reconcile future hard southern chronology against the intentionally general B1 convoy history.
- Preserve the distinction between **coordinated convoy participants** and **independent departures**; the compact outcome is not intended to conscript every southern ship.
- Preserve the public-registry outcome as transparency/coordination rather than a legal enforcement regime unless later story work deliberately expands it.
