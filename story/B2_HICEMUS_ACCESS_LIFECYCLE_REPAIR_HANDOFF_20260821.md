# B2 Hicemus Access Compact lifecycle repair — handoff

Verdict: PARTIAL pending repository-native CI on this exact candidate.

## Authority and isolation
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-hicemus-access-lifecycle-20260821-1527`
- B2 only; no self-integration.

## Defect repaired
`B2 Hicemus Access Compact` is a three-mission dialogue/state-only slice. Its three positive Offer routes, two Review settlements, and `Maintainer Remembers` aftermath previously used `accept` despite creating no gameplay objective. That can leave objective-less missions active after the conversation ends.

## Production change
- Convert those six positive state-only terminals from `accept` to `decline`.
- Preserve the existing refusal `decline`, producing 7/7 clean dialogue terminals.
- Preserve all Dispatcher/Maintainer characterization, three initial routes, trust state, both settlements, Hicemus scope, first-contact/B1 gates, privacy/emergency/freight continuity, and every existing `B2 Hicemus Access Compact:*` condition name/value.
- No state migration required.

## Validator hardening
`tools/story/validate_b2_hicemus_access_compact.py` now additionally requires:
- zero terminal `accept` commands;
- exactly seven `decline` terminals;
- no objective-bearing directives such as destination, stopover, waypoint, NPC, cargo, passengers, deadline, or timer.

Existing mission graph, route, settlement, character, state-ownership, mutation, continuity, and goto/label checks remain.

## A3/B3 invariant
Dialogue-only B2 missions that merely persist state terminate with `decline`; `accept` is reserved for mission lifecycles that actually create gameplay objectives.

The Hicemus continuity boundary is unchanged: temporary routing rules are practical station coordination and do not define the political meaning of the Hicemus/Conlatio division. Dispatcher/Maintainer remain player-private shorthand.

## Validation required before READY
- `python3 tools/story/validate_b2_hicemus_access_compact.py`
- repository focused story validator suite
- A1 simulation/state-ownership contracts
- changed-content style
- production Endless Sky configure/build
- stock save-load smoke

A3 must not integrate while this handoff remains PARTIAL.
