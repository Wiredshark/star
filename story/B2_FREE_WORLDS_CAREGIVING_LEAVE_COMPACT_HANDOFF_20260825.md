# B2 Free Worlds Caregiving Leave Compact handoff

## Status

READY for A3 review/integration. Remains draft and unmerged; B2 does not self-integrate.

## Authority

- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-free-worlds-caregiving-leave-compact-20260825`
- Production commit: `f64d716aa9fa0a9dba33ca86ca97809aa21e617a`
- Initial focused validator commit: `0df30aae9a076b152d9f8e46c29e4399afdf58e3`
- Validator line-wrap hardening / exact fully validated candidate: `208b4f46c22385e0b10a5199d96dc402b5efac51`

## Character / dynamic-content behavior

Adds independent Free Worlds transport captain Mira Senn and engineer Jalen Ro. During authoritative A1 Free Worlds defense strain, a temporary caregiving-leave note for Jalen is repeatedly copied into emergency staffing records until a time-bounded family obligation begins masquerading as permanent unavailability or unreliability.

Player routes:

- bounded current availability without routine copying of private family reasons;
- voluntary standby with explicit windows and retained right to refuse later requests;
- paired employment/current-availability and private leave records;
- refusal, which does not arm the later Review.

The three substantive routes schedule `B2 Free Worlds Caregiving Leave Compact: Review Ready` after 7-11 days. Review requires A1 `world: free worlds defense strain <= 1` and resolves into either:

- `settlement portable availability packet`; or
- `settlement expiry plus fresh request`.

`Jalen Remembers` is a one-shot aftermath reader.

## Dependencies / ownership

- Reads authoritative A1 `world: free worlds defense strain` only.
- A1 remains sole writer of defense strain.
- All B2 writes are namespaced under `B2 Free Worlds Caregiving Leave Compact:*`.
- No A1/A2/B1/world-state, credits, reputation, cargo, equipment, ship, fleet, combat, or government-attitude mutation.
- All seven dialogue/state-only terminal paths use `decline`.
- Refusal cannot write `introduced`, cannot write a substantive route, and cannot schedule Review.

## Canon / persistence assumptions

Current availability, historical leave, private family details, emergency standby commitments, reliability judgments, and current duty authority are separate facts. A true old leave record does not remain current authority after its dates expire. Agreeing to one emergency window does not create unlimited future call-up authority. Family-care details are not required in routine staffing records. This is local voluntary Free Worlds practice rather than centralized employment law.

## Validation

Focused validator: `tools/story/validate_b2_free_worlds_caregiving_leave_compact.py`.

The first exact-head simulation/story run exposed one validator-only line-wrap-sensitive canon assertion; changed-content style passed and production semantics were already correct. Commit `208b4f46c22385e0b10a5199d96dc402b5efac51` replaced that brittle literal with formatting-independent semantic fragments.

Exact candidate `208b4f46c22385e0b10a5199d96dc402b5efac51` is fully green:

- Fork simulation and story validation #590 / run `32821958099`: SUCCESS.
  - changed-content style: SUCCESS;
  - focused Python compilation: SUCCESS;
  - all focused story validators, including this compact: SUCCESS;
  - A1 simulation/state-ownership contracts: SUCCESS.
- Fork save-load integration smoke #575 / run `32821958104`: SUCCESS.
  - build/runtime dependencies: SUCCESS;
  - production configure: SUCCESS;
  - production build: SUCCESS;
  - stock save-load smoke: SUCCESS.

The validator proves exact mission/event structure, route-local writes, refusal suppression, exact 7-11 day scheduling, A1 read-only ownership, recovered-strain Review gating, settlement-local writes, one-shot aftermath, B2-only persistence, zero objective-less `accept` terminals, exactly seven `decline` terminals, no gameplay-objective directives, and core continuity assertions.

## Concurrency / process safety

Current B2 PR/branch activity was inspected before selecting scope; no active caregiving-leave slice was found. The active global dialogue-lifecycle audit was left untouched. Four pre-existing service-owned host processes were observed and preserved; no unrelated process or workspace was reset, killed, or modified.

## A3 / B3 integration notes

Re-read current `main`, active B2/A2/B1 work, ancestry, mergeability, and exact workflow state before integration. Preserve A1 ownership of Free Worlds defense strain and the distinction among caregiving history, private family information, current availability, voluntary emergency commitments, reliability, and current duty authority. Do not generalize this local voluntary arrangement into centralized Free Worlds employment law.
