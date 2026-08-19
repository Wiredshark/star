# A2 Free Worlds Joint Corridor Doctrine Handoff — 2026-08-19

Verdict: **PARTIAL / specialist candidate — pending repository CI and actual-game acceptance**

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative integration branch: `main`
- Exact base SHA: `d485dea4c511964c1209d86dae15f5bcbf17a03b`
- Isolated branch: `agent/a2-free-worlds-joint-corridor-doctrine-20260819-0305`
- Production data commit: `b73092f8ca43e8da5d61dd95a6e6ebc6b5a8edff`
- Focused validator commit: `c1ae0ec5ba497eff7c7a0f5b4dab690ca54e9ae8`

## Why this slice

The existing A2 portfolio already contains separate player-facing consumers for Free Worlds patrol doctrine and Southern Rim traffic coordination. A1 also contains a cross-system relationship where patrol mobilization can contribute to Southern Rim congestion. The missing player-facing seam was a durable doctrine that reconciles the two earlier A2 decisions and is later tested by a recurrence of the underlying A1 pressure.

This slice therefore deepens/integrates existing systems instead of adding another disconnected faction conversation.

## Implemented RPG / dynamic-narrative loop

### Joint review

After both earlier A2 arcs have resolved, and only when neither earlier arc was refused, Anika Ro and Rhea Solano jointly review the player's prior advice.

The conversation recognizes three especially aligned prior-policy pairs:

- civilian patrol protection + emergency traffic corridors;
- mobile patrol distribution + distributed traffic routing;
- interdiction patrol doctrine + staggered traffic clearances.

The player then chooses one standing joint corridor protocol:

1. protected emergency/civilian/rescue capacity;
2. synchronized patrol and traffic movement windows;
3. delegated local patrol/controller authority;
4. refusal to convert emergency advice into permanent doctrine.

Only `A2 Free Worlds Joint Corridor Doctrine:*` conditions are written.

### Future stress test

The later reader waits for a future recurrence of authoritative Southern Rim congestion (`world: southern rim transit congestion >= 4`). It then combines the remembered joint protocol with whether `world: free worlds patrol surge` is simultaneously active.

That yields six positive simulation-sensitive outcomes:

- protected capacity under combined patrol+traffic pressure;
- protected capacity under traffic-only pressure;
- synchronized windows under combined pressure;
- synchronized windows under traffic-only pressure;
- delegated authority under combined pressure;
- delegated authority under traffic-only pressure;

plus an explicit refusal-respected outcome.

The result is a multi-stage feedback loop:

`earlier A2 patrol/traffic decisions -> joint RPG doctrine -> future A1 recurrence -> player-visible consequence`.

## Files

- `data/human/a2 free worlds joint corridor doctrine.txt`
- `tools/story/validate_a2_free_worlds_joint_corridor_doctrine.py`
- `story/A2_FREE_WORLDS_JOINT_CORRIDOR_DOCTRINE_HANDOFF_20260819.md`

## Ownership and persistence invariants

- A1 remains sole writer of `world: southern rim transit congestion`.
- A1 remains sole writer of `world: free worlds patrol surge` and `world: free worlds defense strain`.
- This slice reads prior A2 patrol/traffic choices but never rewrites them.
- This slice introduces no new C++ save authority or parallel state database.
- New state uses ordinary persistent mission/global conditions and therefore follows the existing save path.
- Refusal remains bounded: declining codification is later reported as a respected refusal rather than silently converted into policy.

## Validation

A focused validator is committed at:

`tools/story/validate_a2_free_worlds_joint_corridor_doctrine.py`

It checks:

- both missions and both returning named characters;
- prior A2 completion gates;
- three doctrine routes plus refusal;
- future congestion and patrol-surge inputs;
- six positive stress variants plus refusal;
- no writes to prior A2 policy state;
- no writes to authoritative A1 world state.

At handoff-file creation time, repository CI for the final branch head had not yet been observed, so no CI/build/runtime result is claimed here until GitHub reports it.

## Remaining acceptance gates

Before A3 integration, require:

1. repository-native focused story validation PASS;
2. changed-file content-style gate PASS;
3. cross-file ownership/graph contract PASS;
4. stock configure/build and save-load smoke PASS when triggered;
5. actual-game proof that the joint review does not appear before both predecessor arcs resolve;
6. actual-game proof that either predecessor refusal suppresses the joint review;
7. actual-game exercise of all three protocol choices and refusal;
8. actual-game proof of each protocol under both congestion-only and congestion+patrol-surge stress states;
9. save/reload proof across the joint review and later stress reader;
10. regression inspection for offer precedence/rotation alongside existing Free Worlds conversations.

## A3 integration guidance

Do not merge solely because the focused source validator passes. Review exact branch ancestry and CI first. Preserve A1 state ownership and the earlier A2 policy flags as read-only inputs. If the branch is rebased or otherwise changes after validation, rerun exact-head CI before integration.

