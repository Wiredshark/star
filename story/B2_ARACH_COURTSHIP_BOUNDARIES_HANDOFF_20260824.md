# B2 Arach Courtship Boundaries handoff — READY

## Authority
- Repository: `Wiredshark/star`
- Authoritative base observed: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/b2-arach-courtship-boundaries-20260824`
- Production syntax-fixed commit: `61f2eb7cbf9c3f76fc7828e00c3b1bc7085d8e33`
- Initial focused validator: `cd2c4ed4a4dd5ec5298da758caa99d516e096544`
- Final validator hardening / exact fully validated candidate: `71f526acfd9052ad3906f4526d038e8e1c35553a`
- Final READY handoff-only head: this commit

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
- Review requires introduced + review-ready + not-reviewed state;
- exactly two terminal settlements each close Review once;
- `Selka Remembers` requires either settlement and is one-shot;
- all seven state-only terminal paths use `decline`;
- refusal does not schedule Review;
- all writes are `B2 Arach Courtship Boundaries:*`;
- no `world:*`, B1/A1/A2, material, reputation, cargo, equipment, ship, fleet, or combat mutation.

## Files
- `data/coalition/b2 arach courtship boundaries.txt`
- `tools/story/validate_b2_arach_courtship_boundaries.py`
- `story/B2_ARACH_COURTSHIP_BOUNDARIES_HANDOFF_20260824.md`

## Validation evidence
Exact fully validated candidate: `71f526acfd9052ad3906f4526d038e8e1c35553a`.

- `Fork simulation and story validation` #528 / run `32712074527`: **SUCCESS**.
  - changed fork content style: **SUCCESS**;
  - focused Python validation compilation: **SUCCESS**;
  - all focused story validators, including Arach Courtship Boundaries: **SUCCESS**;
  - A1 simulation/state-ownership contracts: **SUCCESS**.
- `Fork save-load integration smoke` #513 / run `32712074525`: **SUCCESS**.
  - production configure: **SUCCESS**;
  - production build: **SUCCESS**;
  - stock save-load integration smoke: **SUCCESS**.

The first two simulation/story attempts failed only in the newly added focused validator because its local-scope wording assertions depended on physical line formatting. Changed-content style passed on both attempts and production behavior did not need semantic repair. Commit `71f526ac...` makes those scope checks formatting-independent while preserving the same canon boundary.

## Concurrency / process boundary
Current open B2 PRs and the active global dialogue-lifecycle audit were inspected before selecting scope. This slice does not modify existing B2 production files and does not race the lifecycle audit. Unrelated processes/workspaces were preserved. No destructive Git operation or self-integration was performed.

## A3 / B3 notes
**Verdict: READY for A3 review/integration.** A3 retains integration authority. Re-read current `main`, active B2 work, branch ancestry, and Arach canon immediately before integration.

Preserve the distinction among private relationship status, public acknowledgement, event attendance, patronage, gifts, publication consent, revision, withdrawal, and current status. A copied social notice does not become fresh consent or independent evidence. Do not generalize this couple's compromise into centralized Arach or Coalition relationship law.
