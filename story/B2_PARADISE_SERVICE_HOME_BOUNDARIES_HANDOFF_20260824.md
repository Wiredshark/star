# B2 Paradise Service Home Boundaries — handoff

## Verdict
PARTIAL pending exact-head repository-native simulation/story and production build/save-load workflows.

## Authority
- repository: `Wiredshark/star`
- authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- branch: `agent/b2-paradise-service-home-boundaries-20260824`
- production commit: `292d8edea6d6b514b70299172d3c8d5cbcc2be0a`
- focused validator commit: `f75d1e1a3f61a0ace3bdd7ec34fbbe4168cf22ef`

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

## Validation plan
Required before READY:
- focused validator discovery/execution;
- focused Python compilation;
- repository story/state-ownership contracts;
- A1 regression suite;
- changed-content style;
- production configure/build;
- stock save-load integration smoke;
- exact SHA workflow evidence.

## A3 / B3 integration notes
A3 retains integration authority. Re-read current `main`, active B2/A2 work, ancestry, mergeability, and exact workflow state immediately before integration. Preserve the B1 history hook read-only and do not reinterpret this local case as universal housing law.
