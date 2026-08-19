# B2 Syndicate Charter Obligations handoff — 2026-08-18

## Verdict

**PARTIAL — specialist production candidate. Do not integrate until the normal Endless Sky content/parser/runtime/save-load gates run successfully.**

## Ancestry

- Repository: `Wiredshark/star`
- B1 parent branch: `agent/b1-world-history-20260818-1421`
- B1 parent/base SHA: `012e395a83148b5c30897a46fa394329ddf62cee`
- B2 branch: `agent/b2-syndicate-charter-obligations-20260818-1626`
- B2 production-data commit: `23b7af65c001dd516a07009b32b1a3708e87754f`
- B2 implementation + focused-validator head before this handoff: `8f33fcddf17444adf7970f353e111cff3e8907de`

## Scope

This B2 slice consumes B1's `Syndicate Charter Gallery` institutional-history conversation and turns the underlying question — whether old corporate charters still carry public obligations — into named-character persistent content.

Named characters:

- **Rhea Solis** — curator of historic Syndicate charters, focused on institutional memory and continuity of public obligations.
- **Ilan Merrow** — freight/berth coordinator for a shipping consortium, focused on current operational capacity and explicit assignment of costs.

Production content in `data/human/b2 syndicate charter obligations.txt` contains three stock mission/conversation slices:

1. `B2 Syndicate Charter Obligations: Offer`
   - Solis / compromise / Merrow / refusal routes.
   - Persists introduction, route, and character-trust/doubt state.
2. `B2 Syndicate Charter Obligations: Review`
   - Reads the initial route.
   - Resolves into one of two terminal institutional outcomes:
     - `settlement public covenant`
     - `settlement consortium reserve`
3. `B2 Syndicate Charter Obligations: Solis Remembers`
   - Reads either terminal outcome later.
   - Persists one-shot aftermath state.

No credits, reputation, cargo reward, or combat state is intentionally changed. Persistence uses stock mission/global conditions only.

## B1 / A2 dependencies and boundaries

- Direct B1 dependency: `Syndicate Charter Gallery` from `data/human/history conversations.txt` on the parent B1 branch.
- No dependency on the active Broken Compact B2 branches.
- No dependency on Far North Yard Legacy B2 content.
- No dependency on the active A2 dialogue/news branches.
- The slice is designed to provide later A2/B3 readers with stable institutional outcomes without requiring a new engine subsystem.

## Validation work

Added focused validator:

`python3 tools/story/validate_b2_syndicate_charter_obligations.py`

The validator checks:

- exactly 3 expected missions;
- both named characters;
- 3 persistent initial routes;
- 2 terminal settlement states;
- reviewed/aftermath one-shot persistence gates;
- both settlement outcomes consumed by the later reader;
- all missions remain Syndicate-scoped;
- no accidental credits/reputation/combat/cargo reward mutation;
- every local `goto` target has a matching `label`.

### Executable-validation limitation

An attempt was made to clone the exact branch into the available private execution host and run the focused validator there. The private command timed out during the repository-clone/validation attempt, and no validated test result was returned. Therefore this handoff **does not claim that the validator, content parser, build, runtime smoke-load, or save/load checks passed**.

GitHub currently exposes no commit status checks for `8f33fcddf17444adf7970f353e111cff3e8907de`.

## Required acceptance before A3 integration

Run in a real `Wiredshark/star` checkout at the exact candidate head:

1. `python3 tools/story/validate_b2_syndicate_charter_obligations.py`
2. repository-normal content/style validation (including `utils/check_content_style.py` when its Python dependencies are available)
3. normal Endless Sky parser/build gate
4. runtime smoke-load on a Syndicate non-station source
5. exercise all Offer routes and both Review settlement outcomes
6. save/load after introduction and after settlement; verify route/outcome persistence
7. confirm only one terminal settlement is authoritative per playthrough
8. verify `Solis Remembers` appears only after a terminal settlement and only once

## A3 / B3 integration notes

- Review/integrate only after the B1 parent `012e395a83148b5c30897a46fa394329ddf62cee` ancestry is present or the B1 file is integrated independently.
- B3 should check terminology against other Syndicate corporate/public-institution content and ensure the named characters do not collide with later authored canon.
- A2 may consume the terminal settlement conditions for later reactive port news/dialogue, but should not rewrite these conditions' ownership.
- This branch should remain PARTIAL until executable content/runtime/save-load validation is actually observed.
