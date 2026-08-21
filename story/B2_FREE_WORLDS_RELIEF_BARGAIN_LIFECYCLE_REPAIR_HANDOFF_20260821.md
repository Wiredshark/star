# B2 Free Worlds Relief Bargain lifecycle repair handoff

Verdict: PARTIAL pending repository-native validation.

## Stage
B2 — Story Characters + Dynamic Content

## Authority and isolation
- Authoritative integration base observed at start: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`.
- Isolated branch: `agent/b2-free-worlds-relief-lifecycle-20260821-0828`.
- No self-integration performed.
- A1 remains sole owner/writer of `world: free worlds relief demand`; this B2 slice only reads that signal.

## Problem repaired
`B2 Free Worlds Relief Bargain` is a dialogue/state-only three-mission slice. Its positive Offer routes, two Review settlements, and one-shot `Vale Remembers` aftermath wrote persistent state and then used `accept`, despite creating no destination, cargo, NPC, timer, waypoint, or other mission objective. That lifecycle can leave objective-less accepted missions active after the conversation ends.

## Production repair
Production commit: `3315f471fec7c12911493ed1922933a12af76e11`

Changed `data/human/b2 free worlds relief bargain.txt`:
- added the standard Endless Sky GPL header because the legacy file is now touched by changed-content style;
- converted the six positive state-only terminal `accept` commands to `decline`;
- preserved the existing refusal `decline`, for seven clean terminal declines total;
- preserved Lysa Kern / Oren Vale dialogue, three initial routes, trust state, two settlement outcomes, one-shot aftermath, Free Worlds scope, and all existing condition names and values;
- preserved read-only consumption of `world: free worlds relief demand`.

## Focused validation repair
Validator commit: `cdb689c430eb20ddf80e8cfa24b2a85786e2d4f0`

Hardened `tools/story/validate_b2_free_worlds_relief_bargain.py` to require:
- exactly the existing three missions and named characters;
- all three initial routes plus refusal;
- both terminal settlement writes and later-reader consumption;
- A1 relief-demand ownership remains read-only;
- no direct material/reputation/combat mutation;
- valid local `goto` / `label` targets;
- zero terminal `accept` commands;
- exactly seven terminal `decline` commands;
- no objective-bearing directives that would invalidate the state-only lifecycle assumption.

## Validation required before READY
Run on the exact branch head after this handoff commit:
1. focused validator:
   `python3 tools/story/validate_b2_free_worlds_relief_bargain.py "data/human/b2 free worlds relief bargain.txt"`
2. repository focused story/simulation validation workflow, including A1 state-ownership regressions;
3. changed-content style;
4. production build and stock save/load integration smoke.

Do not promote to READY or integrate until those gates are terminal green. Do not treat this PARTIAL handoff as authorization to merge.

## A3 / B3 integration notes
- This is a lifecycle-only repair. Do not reinterpret the narrative policy choices or settlement semantics.
- Preserve A1 sole ownership of `world: free worlds relief demand`.
- Preserve every existing `B2 Free Worlds Relief Bargain:*` condition name/value.
- Durable lifecycle invariant: dialogue-only B2 missions that merely persist state terminate with `decline`; reserve `accept` for mission paths that actually create gameplay objectives.
- If current `main` advances before integration, re-read ancestry and revalidate the isolated diff rather than rebasing destructively.
