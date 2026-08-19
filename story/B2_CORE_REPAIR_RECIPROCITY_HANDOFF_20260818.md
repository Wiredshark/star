# B2 Core Repair Reciprocity handoff — 2026-08-18

## Verdict

**PARTIAL — do not integrate yet.** The isolated B2 production slice and focused structural validator are committed, but the normal Endless Sky parser/build/runtime/save-load acceptance gates have not been executed in a real `Wiredshark/star` checkout during this run.

## Repository state

- Repository: `Wiredshark/star`
- Authoritative `main` observed at start: `d611ce688997d3847ac303c229f64b80663db26c`
- B1 parent branch: `agent/b1-core-institutions-20260818-1916`
- Exact B1 parent SHA: `4118780bb3fbc5b64bff202ebc01587a3b8ae203`
- B2 branch: `agent/b2-core-repair-reciprocity-20260818-1926`
- Production commit: `aab7780026bbdeb4b3cbd2d0c619b353d07d2bf2`
- Focused-validator commit: `b397d644b70aa00de6b897774674735f9133e89a`
- Draft PR: #19, targeting the B1 parent branch

## What this slice adds

This B2 slice consumes the B1 **Core Ship Standard Hall** and **Core Civil Service Ledger** history. It turns the Core's long evolution toward compatible technical standards and mutually recognized administrative records into a present-day character dispute about whether repair credentials should travel between Republic ports.

Named characters:

- **Asha Renn** — Republic port inspector. She supports portable credentials only when participating offices share auditable standards and accountability.
- **Jalen Cross** — independent repair foreman. He argues that experienced mechanics should not repeatedly prove identical competence at every jurisdiction boundary.

Production content lives in `data/human/b2 core repair reciprocity.txt` and contains three missions:

1. `B2 Core Repair Reciprocity: Offer`
2. `B2 Core Repair Reciprocity: Review`
3. `B2 Core Repair Reciprocity: Renn Remembers`

Initial persistent routes:

- `route renn` — common Republic baseline before credentials travel;
- `route cross` — local endorsement of demonstrated experience;
- `route provisional` — portable baseline plus supervised local sign-off;
- refusal records `declined` and does not enter the review chain.

The Review resolves to exactly one of two intended terminal models:

- `settlement reciprocal credential` — common repair classes, reciprocal recognition, common audits, shared disciplinary records;
- `settlement portable endorsement` — local authority remains final, but supervised work-history evidence travels between ports.

`Renn Remembers` is a one-shot later reader of either terminal settlement and records `aftermath seen`.

## Persistence and state assumptions

The slice deliberately uses stock mission/global-condition mechanisms only. It introduces no custom C++ state or serializer changes. Persistence therefore depends on the existing condition serialization already used throughout Endless Sky mission content.

The three initial routes are mutually exclusive by conversation flow. The two terminal settlements are mutually exclusive by Review conversation flow. The focused validator also checks that exactly two terminal settlement writes exist and that the aftermath reader consumes either settlement.

## Focused validator

`tools/story/validate_b2_core_repair_reciprocity.py`

It checks:

- exact three-mission identity/order;
- both named characters;
- exactly one write for each of the three initial routes;
- exactly one refusal write;
- exactly one write for each of the two terminal settlements;
- exactly two `reviewed` writes, one per terminal outcome;
- exactly one aftermath-completion write;
- Republic `core factory` source scope on all three missions;
- local `goto` targets all resolve to labels;
- Review uses explicit Renn/Cross branches with the provisional route as intentional fallthrough;
- no direct credits/payment/reputation/cargo/outfit/ship/fleet mutation.

## Validation actually obtained in this run

- GitHub accepted the production and validator commits on the isolated branch.
- GitHub commit status query for validator head `b397d644b70aa00de6b897774674735f9133e89a` returned no status contexts.
- GitHub workflow-run query for that head returned no workflow runs.
- The currently exposed private execution host was inspected and its `repository-workspace` remote is `Wiredshark/fallout-test`, not `Wiredshark/star`; it was therefore not used to claim Endless Sky validation.
- No parser/build/runtime/save-load result is claimed.

## Required acceptance before READY

Run these from a real checkout of this B2 branch (or a clean detached checkout of its exact final head):

```bash
python3 tools/story/validate_b2_core_repair_reciprocity.py
python3 utils/check_content_style.py
```

Then run the repository's normal Endless Sky content parser/build gate and a runtime smoke pass that exercises:

1. Offer route Renn -> Review -> reciprocal credential -> save/load -> Renn Remembers;
2. Offer route Cross -> Review -> portable endorsement -> save/load -> Renn Remembers;
3. Offer route provisional -> Review fallthrough -> each terminal choice in separate saves;
4. refusal path does not offer Review;
5. only one terminal settlement is authoritative in each save;
6. the content loads only at Republic `core factory` sources as intended.

If any stock mission grammar differs from the structural assumptions in the focused validator, repair the production data and validator together before promotion.

## A3 / B3 integration notes

- Integrate only after the acceptance gates above pass.
- This branch is based directly on the B1 Core institutions SHA and should be ordered after that history slice.
- It is intentionally non-overlapping with the existing Broken Compact, Far North Yard Legacy, Syndicate Charter Obligations, Paradise Service Compact, and South Convoy Compact B2 slices.
- B3 should check the terminology `reciprocal credential`, `portable endorsement`, and `work-history record` against any later Core licensing/inspection story content to avoid parallel contradictory institutions.
- A3 should verify that no later integrated branch already claims a mutually exclusive Republic-wide repair-licensing model before accepting either settlement as world-state precedent.

## Promotion rule

Promote this handoff from **PARTIAL** to **READY** only after the focused validator and normal Endless Sky parser/build/runtime/save-load gates execute successfully on the exact candidate head.
