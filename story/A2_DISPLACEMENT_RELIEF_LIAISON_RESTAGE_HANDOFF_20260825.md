# A2 Displacement Relief Liaison current-main restage handoff

**Verdict:** PARTIAL pending exact-head repository-native validation.

**Authoritative base:** `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`

**Branch:** `agent/a2-displacement-relief-liaison-restage-20260825-0909`

**Production restage:** `04208f0fd207067deeea9160cb3ccf08d27c7804`

**Strengthened validator:** `7e142c4d24b0b77c938bfda7274ede58abbb2a08`

Historical PARTIAL PR #93 remains untouched.

## Scope
Restages the Republic-displacement -> Free Worlds relief liaison on current authoritative main. During authoritative A1 `world: republic displacement relief spillover active` with Republic displacement pressure `>= 4`, Imani Vale asks the player to choose bounded anonymous provenance, aggregate-only capacity tracking, consent-led linkage, or refusal. When the A1 spillover latch later ends, the Review combines each positive choice with current Republic displacement pressure `>= 4` versus `< 4`, yielding six history-aware outcomes; refusal is explicitly remembered and respected.

## Current architecture / invariants
- A1 remains sole writer of `world: republic displacement relief spillover active`, `world: republic displacement pressure`, and `world: free worlds relief demand`.
- All new writes remain `A2 Displacement Relief Liaison:*`.
- Existing route/state names are preserved from the historical candidate for save compatibility.
- Both state-only missions use `offer precedence 9`.
- Exactly five state-only terminal commands use `decline`; no objective-less `accept` remains.
- All seven Review routes are explicitly branched and explicitly converge through `label finish`; refusal no longer depends on conversation fallthrough.
- Individual displacement history remains distinct from aggregate network load.
- Anonymous provenance does not expose passenger identity; aggregate tracking does not attach political origin to individual cases; consent-led linkage travels only when the arrival asks for it.
- Refusal is recorded as refusal and is not converted into later authorization.
- No credits, reputation, cargo, equipment, ship, fleet, combat, destination, waypoint, or other gameplay-objective mutation is introduced.

## Validation contract
`tools/story/validate_a2_displacement_relief_liaison_restage.py` enforces:
- exact two-mission structure and both precedence declarations;
- four explicit briefing routes;
- six positive pressure-sensitive Review outcomes plus explicit refusal handling;
- seven explicit Review branches/labels and seven `goto finish` convergence paths;
- five decline terminals and zero state-only accepts;
- absence of gameplay objective/material directives;
- A1 world-state read-only ownership;
- A2 namespace-only assignments;
- key consent/privacy continuity language;
- trailing newline.

## A3 integration boundary
Do not self-integrate. A3 should re-read current authoritative main, verify ancestry/mergeability and exact workflow results, and preserve A1 ownership, route/state-name compatibility, explicit refusal handling, offer precedence 9, and the state-only decline lifecycle. Do not integrate historical PR #93 together with this restage.
