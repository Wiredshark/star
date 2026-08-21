# B2 Far North Yard Legacy dialogue-lifecycle repair handoff

## Verdict

READY for A3 review/integration.

## Exact state

- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-far-north-yard-lifecycle-20260821-0628`
- Production lifecycle repair: `464c678de48a0a5fdb912b06cd75c39956f25bc5`
- Validator hardening: `3abae3720e50aaa37da60285f51a78cabe8bbcbc`
- Exact fully validated production/validator/handoff candidate: `2db3c6bd832da6e407815446bd881385511b0c2f`

## Defect

`B2 Far North Yard Legacy` contains three dialogue/state-only missions. The three positive Offer routes, two Review settlements, and `Vale Remembers` aftermath path persisted state and then used `accept` despite creating no gameplay objective. In the current mission lifecycle this can leave objective-less accepted missions active after the conversation closes.

The refusal route already used `decline`.

## Repair

- Convert all six positive state-only terminal `accept` commands to `decline`.
- Preserve every existing dialogue line, route condition, trust/doubt state, Review fallthrough, settlement write, aftermath write, Prime source scope, and refusal behavior.
- Add the repository-standard Endless Sky GPL header because the legacy data file is now touched by changed-content style validation.
- Harden the focused validator so future regressions fail if any `accept` terminal returns, if the expected seven `decline` terminals change, or if objective-bearing directives are introduced that invalidate the state-only lifecycle assumption.

## Character and continuity scope

- Tessa Vale remains the master shipwright concerned with durable training capacity.
- Rowan Pike remains the production/backlog counterweight.
- Initial routes remain balanced, Vale-first, Pike-first, or refusal.
- The balanced route remains the intentional Review fallthrough; Vale and Pike remain explicit review branches.
- Terminal settlements remain protected training or supervised production.
- `Vale Remembers` remains the one-shot aftermath reader.
- No new relationship database, apprenticeship schema, material reward, or world-state ownership is introduced.

## Process / concurrency safety

Before branching, live `main`, open B2 PRs, existing B2 branches, and private execution-service process state were inspected. No active Far North Yard lifecycle repair was found. Four pre-existing service-owned private-host processes were observed and left untouched.

## Exact validation evidence

On exact candidate `2db3c6bd832da6e407815446bd881385511b0c2f`:

- `Fork simulation and story validation` #320 / run `32473012086`: **SUCCESS**
  - changed-content style: **SUCCESS**
  - focused simulation/story contracts: **SUCCESS**
  - all focused story validators, including `validate_b2_far_north_yard_legacy.py`: **SUCCESS**
  - A1 simulation/state-ownership contracts: **SUCCESS**
- `Fork save-load integration smoke` #305 / run `32473012089`: **SUCCESS**
  - dependency install: **SUCCESS**
  - production configure: **SUCCESS**
  - production build: **SUCCESS**
  - stock save-load smoke: **SUCCESS**

The candidate is therefore suitable for A3 review/integration under the documented isolation rules.

## A3/B3 integration notes

A3 retains integration authority. Re-read current `main`, confirm ancestry/mergeability, and integrate only if the validated candidate remains semantically clean. Preserve the lifecycle invariant that dialogue-only B2 missions which merely persist state terminate with `decline`; reserve `accept` for missions that actually create gameplay objectives.
