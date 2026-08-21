# B2 Republic Civic Case Continuity — A3/B3 handoff

## Status

READY for A3 review/integration.

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative base observed at slice selection: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-republic-civic-case-continuity-20260820-2127`
- Production commit: `5529c3ad05ed8c59008411716aaba422ed9464ad`
- Focused-validator commit: `7ac7e5c74db8610278ff75c28ca7109ea207f409`
- Exact fully validated production/validator/handoff candidate: `4af568da40f9b6aef304c659ec3228f9e63a48c3`
- B2 does not self-integrate.

## What this adds

A three-mission Republic civic-administration character arc driven by A1's authoritative `world: republic civic strain`.

Characters:

- **Mara Ellison** — Republic casework supervisor managing staff transfers between overloaded districts.
- **Jun Park** — neighborhood advocate focused on preventing residents from becoming the government's backup copy of their own case history.

Flow:

1. **The Desk That Moved** appears while civic strain is high (`>= 4`). The player chooses named-owner continuity, accountable pooled handoff, paired consent/context/assignment records, or refusal.
2. **The Case After the Queue** appears only after A1 naturally recovers civic strain to `<= 1`. It resolves into either a portable case packet or a reconciliation cycle.
3. **Park Remembers** is a one-shot later reader of the terminal settlement.

## Distinct scope

This does not duplicate existing Republic arcs:

- Republic Tracing Compact concerns family tracing vs residence/return decisions.
- Republic Review Mentorship concerns customs-review doctrine and training.
- Republic Border Testimony concerns direct observation vs copied border-security evidence.
- Republic Manifest Appeal concerns freight declarations, corrections, and challenge disposition.

This slice instead concerns **public-service case continuity when staff and desks move under administrative overload**: resident consent, verified case context, unresolved obligation, current responsible office/person, next action, and explicit closure evidence.

## Ownership and persistence

A1 remains sole owner/writer of `world: republic civic strain`. B2 reads it only for offer/review gating.

Every new persistent write is under `B2 Republic Civic Case Continuity:*`.

No direct credits, reputation, cargo, outfits, ships, fleets, combat rating, or unrelated campaign/world-state mutation is introduced.

## Core continuity invariant

Administrative motion is not the same thing as public-service completion.

A closed appointment, transferred file, reassigned clerk, or reduced aggregate queue must not silently erase:

- the resident's current consent;
- the last verified case context;
- the unresolved public obligation;
- the current responsible owner/office;
- the next required action;
- explicit evidence that the obligation was fulfilled, transferred, or legitimately closed.

## Validation evidence

Focused validator:

```text
python3 tools/story/validate_b2_republic_civic_case_continuity.py
```

Repository-native validation on exact candidate `4af568da40f9b6aef304c659ec3228f9e63a48c3`:

- `Fork simulation and story validation` run #291 / `32436520552`: **SUCCESS**
- `Fork save-load integration smoke` run #276 / `32436520542`: **SUCCESS**

Those workflows cover the repository's focused story-validator discovery/contracts, changed-content style, A1 simulation/state-ownership regressions, production configure/build, and stock save-load smoke used by current B2 acceptance.

The final READY commit changes only this durable handoff; production content and validator behavior are unchanged from the fully validated candidate above.

## A3/B3 integration notes

- Re-read current `main` before integration; the base SHA above is an observation, not a permanent integration target.
- Preserve A1 sole ownership of `world: republic civic strain`.
- Preserve the distinction among case context, resident consent, staff assignment, current obligation, and explicit closure evidence.
- Do not reinterpret this practical case-handoff discipline as a new centralized Republic super-agency; it is ordinary cross-district public-service procedure.
