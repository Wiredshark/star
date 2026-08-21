# A2 Lunarium Network Practice current-main restage handoff

Verdict: PARTIAL pending exact-head repository-native validation.

Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`

Branch: `agent/a2-lunarium-network-practice-restage-20260821-1606`

Production restage: `4b894511a187d260f2b54d22ec1fb58cb38ab2de`

Strengthened validator: `7afceb629e8bd4b3c198c3b1528d897951a369e9`

This restages historical PR #171 without rebasing, resetting, force-updating, or modifying the historical branch.

## Loop
After the player has joined the Lunarium and has not joined the Heliarchs, Chiree asks the player to choose a private operating practice: preserve civilian-aid obligations independently of covert convenience, use compartmented need-to-know handoffs, preserve provenance and corrections before acting on allegations, or refuse a standing rule. A later one-shot Reflection demonstrates a distinct consequence of each positive route.

## Current architecture repairs
- Production content uses the repository-standard complete GPL header.
- Both state-only missions declare `offer precedence 9`.
- All five state-only terminal paths persist their intended state and terminate with `decline`; objective-less `accept` is forbidden.
- The Reflection rechecks Lunarium membership and exclusion from Heliarch membership in addition to the A2 decision state.
- The focused validator enforces lifecycle, precedence, refusal suppression, one-shot reflection, faction-state read-only ownership, and A2-namespaced persistence.

## Invariants
- `joined the lunarium` and `joined the heliarchs` are read-only gates.
- No `world:*` state is written.
- All persistent writes are namespaced `A2 Lunarium Network Practice:*`.
- Genuine charity remains a genuine obligation even when routes also provide covert cover.
- Compartmentation limits disclosure; it is not omniscient security.
- Repeated allegations do not manufacture independent corroboration.
- Refusal does not arm the later Reflection.
- The player receives no Lunarium office or authority to speak for civilian beneficiaries.

## Files
- `data/coalition/a2 lunarium network practice.txt`
- `tools/story/validate_a2_lunarium_network_practice.py`
- this handoff

## Validation required
Run exact-head `Fork simulation and story validation` and `Fork save-load integration smoke`. Do not promote to READY or integrate if either exact-head repository-native gate fails. Optional exploratory acceptance after repository validation may exercise all four Briefing routes, three Reflection routes, refusal suppression, save/reload between stages, one-shot behavior, and Coalition/Lunarium offer precedence.

## A3 integration boundary
A3 retains integration authority. Re-read current `main`, verify ancestry/mergeability, preserve faction-state read-only ownership and the state-only dialogue `decline` lifecycle invariant, and integrate only the exact validated restage head if both repository-native gates are terminal green.
