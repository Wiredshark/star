# B2 Coalition Interspecies Hosting Compact handoff — 2026-08-24

Verdict: READY for A3 review/integration.

Authority/base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
Branch: `agent/b2-coalition-hosting-compact-20260824`
Exact fully validated production/validator/handoff candidate: `32eb15eeab388fc87ad3c0c541840fbea8f2b36b`

Scope: persistent household-scale sequel to the existing Coalition Interspecies Exchange Program. Adds a recurring Saryd Host and Kimek Settler (player-private shorthand, not offices) in a three-mission arc about household expectations, privacy, guests, shared money/work, adaptation, explicit consent, revision, and the right to leave a placement.

Routes: consent floor; named adaptation; paired informal/formal boundaries; refusal. Positive routes schedule a 7–11 day Review. Settlements: portable household charter or periodic consent renewal. `Settler Remembers` is one-shot aftermath.

Ownership: reads only existing `known to the heliarchs` access state and Coalition world/source context. Writes only `B2 Coalition Interspecies Hosting Compact:*`. No material/reputation/world/A1/A2/B1 mutation. All seven state-only terminal paths use `decline`.

Continuity: disclosure is not permanent consent; cultural adaptation is not surrender of privacy or exit rights; one household compromise is not centralized Coalition domestic law; everyday friendship remains intentionally outside formal records.

Exact validation on candidate `32eb15eeab388fc87ad3c0c541840fbea8f2b36b`:
- Fork simulation and story validation #521 / run `32703862778`: SUCCESS.
- Fork save-load integration smoke #506 / run `32703862855`: SUCCESS.
- Production configure/build and stock save-load smoke: SUCCESS.
- Local-equivalent focused story validators: 49/49 PASS.
- Local-equivalent A1 regression suite: 128 PASS.
- Changed-content style and `git diff --check`: PASS.

A3: do not self-integrate. Re-read current `main`, ancestry, and active B2/A2 work before integration. The final commit after the validated candidate is handoff-only and must not be treated as a production behavior change.
