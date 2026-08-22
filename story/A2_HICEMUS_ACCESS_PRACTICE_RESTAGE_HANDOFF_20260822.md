# A2 Hicemus Access Practice current-main restage handoff - 2026-08-22

## Verdict

**READY for A3 review/integration.**

## Authority

- Repository: `Wiredshark/star`
- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-hicemus-access-practice-restage-20260822-0132`
- Historical source candidate: PR #121 / `agent/a2-hicemus-access-practice-20260819-1906`
- Exact validated production/validator head: `44c1dc94d526f9ead02355435386e1a6f9dbb1ac`

## Why this restage

The historical Hicemus Access Practice remained PARTIAL on an old base and used objective-less `accept` terminals for state-only dialogue. This current-main restage leaves the historical branch untouched and brings the slice into the current A2 lifecycle and offer-precedence architecture.

The active Republic Border Testimony runtime diagnostic was inspected first and is being repaired separately; this Hicemus slice is independent and does not modify or race that branch.

## Player-facing RPG loop

After `B2 Hicemus Access Compact: aftermath seen`, the player encounters the Incipias they privately call the Dispatcher or Maintainer and chooses one of four responses:

1. bounded-record practice: purpose, limits, expiry, and reviewer travel with a temporary exception;
2. interaction-first practice: individually reasonable exceptions are checked for combined load and shared emergency-path conflicts;
3. local-only reuse: preserve the lesson as context without exporting station authority;
4. explicit refusal.

The three positive choices persist `A2 Hicemus Access Practice: chosen` plus their route condition. A later one-shot reflection demonstrates a distinct consequence for each positive route. Refusal persists only `A2 Hicemus Access Practice: refused` and deliberately does not arm the later reflection.

## Invariants

- `B2 Hicemus Access Compact:*` is read-only.
- No `world:*` state is written.
- All persistent writes are namespaced under `A2 Hicemus Access Practice:*`.
- Dispatcher/Maintainer remain player-private shorthand, not Hicemus offices or translated titles.
- The player gains no Hicemus credential, endorsement, linguistic authority, or representative authority.
- Temporary exceptions do not become permanent merely through repetition.
- Local station practice is not universal precedent.
- Refusal remains a real boundary and does not create a later positive consequence.
- Both state-only missions use `offer precedence 9`.
- All five objective-less terminal paths use `decline`; no state-only mission is left accepted.

## Files

- `data/incipias/a2 hicemus access practice.txt`
- `tools/story/validate_a2_hicemus_access_practice.py`
- `story/A2_HICEMUS_ACCESS_PRACTICE_RESTAGE_HANDOFF_20260822.md`

## Exact validation evidence

On exact production/validator head `44c1dc94d526f9ead02355435386e1a6f9dbb1ac`:

1. `Fork simulation and story validation` #379 / run `32554679249`: **SUCCESS**.
2. `Fork save-load integration smoke` #364 / run `32554679267`: **SUCCESS**.
3. Current authoritative `main` was re-read at `a17a89fb4779200a0634a6dade1811c4dc9cc2be`; PR #239 remains isolated, open, draft, unmerged, and GitHub reports it mergeable.

The focused validator enforces both mission identities, B2 read-only consumption, A2-only writes, all three positive routes plus refusal, refusal suppression of the later reader, one-shot reflection, offer precedence 9, and state-only decline lifecycle.

No manual actual-game acceptance is claimed by this handoff unless separately executed and recorded.

## A3 integration boundary

A3 retains integration authority. Preserve B2/world read-only ownership, refusal suppression, current state names, offer precedence 9, and state-only `decline` lifecycle. Do not self-merge.
