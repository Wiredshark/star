# B2 Arach Courtship Boundaries handoff — PARTIAL

## Authority
- Repository: `Wiredshark/star`
- Authoritative base observed: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-arach-courtship-boundaries-20260824`
- Production syntax-fixed commit: `61f2eb7cbf9c3f76fc7828e00c3b1bc7085d8e33`
- Focused validator commit: `cd2c4ed4a4dd5ec5298da758caa99d516e096544`
- Exact candidate/handoff head: this commit

## Scope
Adds Selka Meren, an Arach patron from a wealthy theater-going family, and Neri Vass, an Arach stage worker. Their private relationship is being converted into public claims by guest lists, gifts, patronage entries, and copied social notices.

Player routes:
1. mutual acknowledgement only when both people approve the public claim;
2. privacy by default despite visible public appearances;
3. event-by-event separation of sponsorship, gifts, attendance, work, and relationship disclosure;
4. refusal to establish a general rule.

Positive routes schedule a 7–11 day Review. The Review resolves into either a shared public boundary with dated/revisable/withdrawable statements or a privacy firewall requiring fresh direct consent before event/patronage records can become relationship claims. `Selka Remembers` is the one-shot aftermath reader.

## Canon / architecture
- Uses established Arach theater/patron culture from `data/coalition/coalition culture conversations.txt` as background only.
- Requires existing `known to the heliarchs` access state.
- All missions source from Coalition Arach locations through source attributes rather than inventing a universal Arach institution.
- This is a local relationship practice, not Arach law, Coalition law, or a universal description of Arach courtship.
- Public relationship status, event attendance, patronage, gifts, creative work, private biography, consent, revision, and withdrawal remain separate facts.
- Silence or refusal to publish is not evidence that the relationship failed.
- Old mutually approved statements remain historical statements rather than permanent authority over current status.

## Ownership / lifecycle
- exactly three missions plus one delayed Review-ready event;
- three substantive routes plus refusal;
- positive routes schedule Review at 7–11 days;
- two terminal settlements;
- one-shot aftermath reader;
- all seven state-only terminal paths use `decline`;
- refusal does not schedule Review;
- all writes are `B2 Arach Courtship Boundaries:*`;
- no `world:*`, B1/A1/A2, material, reputation, cargo, equipment, ship, fleet, or combat mutation.

## Files
- `data/coalition/b2 arach courtship boundaries.txt`
- `tools/story/validate_b2_arach_courtship_boundaries.py`
- `story/B2_ARACH_COURTSHIP_BOUNDARIES_HANDOFF_20260824.md`

## Validation state
PARTIAL pending repository-native exact-head validation after PR creation:
- focused validator execution;
- all focused story validators;
- A1 simulation/state-ownership contracts;
- changed-content style;
- production configure/build;
- stock save-load integration smoke.

## Concurrency / process boundary
Current open B2 PRs and the active global dialogue-lifecycle audit were inspected before selecting scope. This slice does not modify existing B2 production files and does not race the lifecycle audit. Unrelated processes/workspaces are preserved. No destructive Git operation or self-integration is authorized.

## A3 / B3 notes
A3 should re-read current `main`, active B2 work, and Arach canon before integration. Preserve the distinction among private relationship status, public acknowledgement, event attendance, patronage, gifts, publication consent, and current revision/withdrawal. Do not generalize this couple's compromise into centralized Arach or Coalition relationship law.
