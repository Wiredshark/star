# B2 Paradise Service Home Boundaries — handoff

## Verdict
READY for A3 review/integration. The exact production/validator candidate passed both repository-native acceptance workflows.

## Authority
- repository: `Wiredshark/star`
- authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- branch: `agent/b2-paradise-service-home-boundaries-20260824`
- production commit: `292d8edea6d6b514b70299172d3c8d5cbcc2be0a`
- initial focused validator commit: `f75d1e1a3f61a0ace3bdd7ec34fbbe4168cf22ef`
- validator wording hardening / exact fully validated candidate: `c840b086349d12596dad97326601643d2c07a57c`

## Character / dynamic-content behavior
Adds Paradise service worker Rina Vale and municipal housing clerk Tomas Keene. After the integrated `Paradise Service District Museum: offered` history hook, Rina's job change exposes an old database assumption that employment, occupancy, subsidy, and access rights are one status.

Player routes:
- tenancy-first separation of home from job;
- explicit transition for genuinely job-dependent housing/access;
- paired employment / occupancy / subsidy / access records;
- refusal.

The three substantive routes schedule a 7–11 day Review. Review resolves into either:
- `settlement portable occupancy packet`; or
- `settlement employment housing firewall`.

`Rina Remembers` is the one-shot aftermath reader.

## Ownership / persistence
- all writes are `B2 Paradise Service Home Boundaries:*`;
- `Paradise Service District Museum: offered` is read-only;
- no `world:*`, B1/A1/A2, credits, reputation, cargo, equipment, ship, fleet, or combat mutation;
- all 7 dialogue/state-only terminal paths use `decline`;
- refusal does not arm Review.

## Canon / continuity assumptions
This is one local Paradise service-district case, not Republic tenancy law or a universal Paradise rule. Employment, tenancy/occupancy, employer subsidy, work access, residential access, transition dates, and current responsible authority remain separate facts. Historical employment may remain true without becoming current authority over a home.

## Files
- `data/human/b2 paradise service home boundaries.txt`
- `tools/story/validate_b2_paradise_service_home_boundaries.py`
- `story/B2_PARADISE_SERVICE_HOME_BOUNDARIES_HANDOFF_20260824.md`

## Exact validation evidence
The first exact-head simulation/story run #547 / `32751425541` failed only in the new focused validator because one assertion expected `does not establish republic tenancy law` as a physically contiguous source string while the production comment wrapped across lines. Changed-content style was already green and production semantics were unchanged.

Validator-only hardening commit `c840b086349d12596dad97326601643d2c07a57c` replaced that line-wrap-sensitive assertion with semantic fragments.

On exact candidate `c840b086349d12596dad97326601643d2c07a57c`:
- Fork simulation and story validation #548 / `32751603606`: **SUCCESS**;
- focused Python compilation: **SUCCESS**;
- all focused story validators including Paradise Service Home Boundaries: **SUCCESS**;
- A1 simulation/state-ownership contracts: **SUCCESS**;
- changed-content style: **SUCCESS**;
- Fork save-load integration smoke #533 / `32751603593`: **SUCCESS**;
- production configure/build: **SUCCESS**;
- stock save-load integration smoke: **SUCCESS**.

Exact base-to-candidate isolation is 4 commits ahead / 0 behind, exactly three added files, 373 additions, 0 deletions.

## Risks / deferred work
No save-state migration is required because this is additive B2-only persistence. A3 should still re-read current `main`, active B2/A2 work, ancestry, mergeability, and workflow state immediately before integration.

## A3 / B3 integration notes
A3 retains integration authority. Preserve the B1 history hook read-only and do not reinterpret this local case as universal housing law. B3 may reuse the explicit separation among employment, occupancy, subsidy, and access authority rather than copying one ambiguous status field downstream.
