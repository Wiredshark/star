# B2 Rulei Recovery Role Choice — handoff

Status: READY for A3 review/integration.

## Authority

- Repository: `Wiredshark/star`
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-rulei-recovery-role-choice-20260825`
- Production commit: `552cf3455d7d27cb5f1a48ceabedadbaba784d45`
- Initial focused validator: `d5cbd917d455f01be76dbfae3c6e19bf685e1df3`
- Event-declaration validator hardening / exact fully validated production+validator candidate: `5c26653636da6537c4d10c1d812c4b1e7032d2b8`

## Character / dynamic-content behavior

Adds a three-mission sequel to integrated `B2 Rulei Exposure Accountability: aftermath seen`.

Returning character: Dr. Sena Orlov.
New recurring character: Kaia Renn, a human survey pilot whose old Rulei-contact recovery history is accurate but whose temporary support history is being copied as though it were a permanent work limitation.

Offer routes:

1. current-function first;
2. worker-directed, task-bounded support;
3. paired exposure/recovery history plus current role/support record;
4. refusal, which does not introduce the arc or arm Review.

The three substantive routes schedule Review after 7–11 days. Review resolves into either:

- portable current-role packet; or
- fresh-need renewal.

`Renn Remembers` is the one-shot aftermath reader.

## Ownership / persistence

- Reads `B2 Rulei Exposure Accountability: aftermath seen` only.
- Writes only `B2 Rulei Recovery Role Choice:*`.
- No `world:*`, A1/A2/B1, prior-B2, material, reputation, cargo, equipment, ship, fleet, combat, or government-attitude mutation.
- All seven dialogue/state-only terminal paths use `decline`.
- Refusal cannot schedule Review.

## Continuity / canon assumptions

Past symptoms, recovery history, current demonstrated capability, current restrictions if any, worker-requested support, role preference, assignment authority, expiry/review, and closure are separate facts.

A support that genuinely helped in the past remains historical evidence; it does not automatically remain a current restriction. Asking for support on one job does not create a permanent identity or universal limitation. Current clearance is not the same thing as a forced assignment. The slice does not diagnose a lasting Rulei effect and does not create universal employment law.

## Validation

The first exact-head simulation/story run (#619 / `32878234374`) failed only in the new focused validator. Changed-content style passed and the repository-wide story contracts were otherwise green. The defect was a validator count that treated the Review Ready event declaration and the three delayed schedules as the same form.

Commit `5c26653636da6537c4d10c1d812c4b1e7032d2b8` made the declaration check line-exact without changing production content.

On exact candidate `5c26653636da6537c4d10c1d812c4b1e7032d2b8`:

- Fork simulation and story validation #620 / run `32878352582`: **SUCCESS**
  - focused Python compilation: SUCCESS
  - all focused story validators: SUCCESS
  - A1 simulation/state-ownership contracts: SUCCESS
  - changed-content style: SUCCESS
- Fork save-load integration smoke #605 / run `32878352414`: **SUCCESS**
  - dependency installation: SUCCESS
  - production configuration/build: SUCCESS
  - stock save-load smoke: SUCCESS

## Files

- `data/rulei/b2 rulei recovery role choice.txt`
- `tools/story/validate_b2_rulei_recovery_role_choice.py`
- `story/B2_RULEI_RECOVERY_ROLE_CHOICE_HANDOFF_20260825.md`

## Process / workspace boundary

This run performed repository work through the GitHub connector and did not attach to, reset, kill, or modify any unrelated local worktree or process. No destructive Git operation or self-integration was performed.

## A3 / B3 notes

A3 should re-read current `main`, active B1/A2/B2 work, ancestry, mergeability, and exact workflow state immediately before integration. Preserve the prior Rulei Exposure Accountability aftermath as read-only. Do not reinterpret the local Orlov/Renn compromise as Republic-wide employment law, medical doctrine, or proof of a lasting Rulei-caused impairment.
