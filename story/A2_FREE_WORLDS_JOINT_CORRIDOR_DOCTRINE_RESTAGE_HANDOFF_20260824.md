# A2 Free Worlds Joint Corridor Doctrine — current-main restage handoff

**Verdict: PARTIAL pending exact-head repository-native validation.**

## Authority

- Authoritative integration base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-free-worlds-joint-corridor-doctrine-restage-20260824-1606`
- Production restage: `e189d902f2cdf6fb8c533551976f005254baad4a`
- Strengthened validator: `b807e9a59eb0eee287b965d93cb6807ee94846c9`
- Historical PARTIAL PR #63 remains untouched.

## Scope

Restages the cross-system Free Worlds joint-corridor sequel on current authoritative main. Both predecessor A2 arcs are already integrated on current main:

- `A2 Free Worlds Patrol Doctrine:*` (Anika Ro)
- `A2 Southern Rim Traffic Coordination:*` (Rhea Solano)

The Review waits until both predecessor arcs have resolved and neither predecessor route was refused. It recognizes aligned earlier policy pairs and asks the player to persist one standing joint corridor protocol:

- protected capacity;
- synchronized patrol/traffic windows;
- delegated local coordination authority;
- refusal to convert bounded emergency advice into standing doctrine.

The Stress Test waits for a later authoritative `world: southern rim transit congestion >= 4` recurrence. Each positive protocol resolves differently depending on whether `world: free worlds patrol surge` is simultaneously active, yielding six live-state-sensitive outcomes. Refusal is explicitly remembered and respected during recurrence rather than being silently converted into standing authority.

## Ownership and persistence invariants

- A1 remains sole writer of `world: southern rim transit congestion`, `world: free worlds patrol surge`, and `world: free worlds defense strain`.
- The integrated patrol-doctrine and traffic-coordination A2 conditions are read-only inputs.
- Every new persistent write is namespaced under `A2 Free Worlds Joint Corridor Doctrine:*`.
- Both missions use `offer precedence 9`.
- All five objective-less terminal paths use `decline`; there are zero state-only `accept` terminals.
- No gameplay objective, credits, reputation, cargo, equipment, fleet, ship, or combat mutation is introduced.
- Refusal remains refusal; recurrence proves that the earlier refusal is respected rather than manufacturing permanent policy.

## Validation

A strengthened focused validator is included at `tools/story/validate_a2_free_worlds_joint_corridor_doctrine.py`. It checks:

- exact two-mission structure and both precedence declarations;
- predecessor A2 gating and refusal suppression before Review;
- all three positive protocols plus refusal;
- six patrol-surge-active/quiet stress outcomes plus refusal-respected handling;
- five state-only decline terminals and zero state-only accepts;
- A1 and predecessor-A2 read-only ownership;
- A2 namespace isolation;
- absence of gameplay/material mutation directives.

Repository-native simulation/story/style and production build/save-load workflows have not yet completed on this restage. Do not claim READY until both are terminal green on an exact candidate SHA.

## A3 integration boundary

A3 must re-read current `main`, confirm branch ancestry and mergeability, and avoid integrating historical PR #63 together with this restage. Preserve predecessor A2 and A1 ownership exactly. Do not self-integrate from A2.
