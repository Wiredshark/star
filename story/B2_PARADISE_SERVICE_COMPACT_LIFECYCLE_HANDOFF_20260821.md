# B2 Paradise Service Compact lifecycle handoff — 2026-08-21

## Verdict

READY for A3 review/integration.

## Scope

Focused lifecycle repair only. No new Paradise story route, settlement, character, reward, world-state write, or integration authority is added.

The existing `B2 Paradise Service Compact` consists of dialogue/state-only missions. Its positive Offer routes, both Review settlements, and `Mercer Remembers` aftermath persisted state and then used `accept` despite having no destination, cargo, NPC, timer, waypoint, passenger, or other mission objective. That can leave an objective-less mission active after the conversation ends.

This branch changes those six positive terminal commands from `accept` to `decline`. Together with the existing refusal route, all seven terminal dialogue paths now persist exactly the same state and terminate cleanly with `decline`.

Because the production file is modified, it also receives the standard Endless Sky copyright/GPL header required by changed-content style checks.

## Authority / base

- repository: `Wiredshark/star`
- authoritative base observed before work: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- branch: `agent/b2-paradise-service-lifecycle-20260821-0428`
- production lifecycle commit: `95e3e640d8eb7e4dddd73127e3adfe532c059ca0`
- validator-hardening commit: `9770fb56b0406775d0d8104c02fdcb7d9555ec10`
- exact fully validated production/validator/handoff candidate: `80a3ee191843bb60b9b9ce5967be49177f95dea0`

## Files changed

- `data/human/b2 paradise service compact.txt`
  - add standard GPL header;
  - change 3 positive Offer terminals, 2 Review settlement terminals, and 1 aftermath terminal from `accept` to `decline`;
  - add a comment documenting the dialogue/state-only lifecycle invariant.
- `tools/story/validate_b2_paradise_service_compact.py`
  - require zero terminal `accept` commands;
  - require exactly seven terminal `decline` commands;
  - reject objective-bearing directives that would invalidate the state-only lifecycle assumption;
  - preserve all existing route, scope, settlement, goto/label, persistence, and material-mutation checks.
- this handoff document.

## Invariants preserved

- Iona Mercer and Celia Voss remain the same named characters.
- Offer routes remain Mercer / Voss / compact / refusal.
- Review still consumes Mercer and Voss explicitly, with compact as intentional fallthrough.
- Terminal settlements remain exactly:
  - `B2 Paradise Service Compact: settlement municipal corridor`
  - `B2 Paradise Service Compact: settlement shared service compact`
- `Mercer Remembers` still consumes either settlement and writes only `aftermath seen`.
- All existing `B2 Paradise Service Compact:*` condition names and values are unchanged.
- Republic + `paradise` + non-station scoping is unchanged.
- No credits, reputation, cargo, outfits, combat, ships, fleets, or A1 `world:*` state are written.
- B2 does not self-integrate.

## Exact validation evidence

Exact candidate `80a3ee191843bb60b9b9ce5967be49177f95dea0` is terminal green on both repository-native acceptance workflows:

- `Fork simulation and story validation` run `32463528675` / #316: SUCCESS
  - compile focused Python validation code: SUCCESS
  - run all focused story validators: SUCCESS
  - run A1 simulation contract tests: SUCCESS
  - changed fork content style: SUCCESS
- `Fork save-load integration smoke` run `32463528654` / #301: SUCCESS
  - production dependency setup: SUCCESS
  - production configure: SUCCESS
  - production build: SUCCESS
  - stock save/load smoke cases: SUCCESS

The private execution-service process inventory was also checked. Four pre-existing service-owned processes were observed and preserved; no unrelated process was killed or modified.

## A3 / B3 integration notes

This is intentionally a minimal lifecycle repair. A3 should re-read current `main`, confirm ancestry remains compatible, and integrate this branch only through normal integration authority.

B3 should preserve the rule that dialogue-only B2 missions that merely write persistent state terminate with `decline`; `accept` should be reserved for missions that actually enter an objective-bearing lifecycle.
