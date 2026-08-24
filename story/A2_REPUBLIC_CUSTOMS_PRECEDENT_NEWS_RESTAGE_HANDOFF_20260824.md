# A2 Republic Customs Precedent News Current-Main Restage Handoff — 2026-08-24

Verdict: **READY for A3 review/integration.**

## Authority

- Repository: `Wiredshark/star`
- Authoritative integration branch: `main`
- Exact authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Branch: `agent/a2-republic-customs-precedent-news-restage-20260824-1304`
- Production restage commit: `83799219615fe926c3595a3dcedfb65cfea0715f`
- Strengthened validator commit: `e42ceadd090d37ca244471dec49722f390cfcb57`
- Exact validated production/validator head: `8f13630a534166fd847b139e94715cfeeb33af3f`
- Historical PARTIAL PR #60 remains untouched.

## Scope

This is a current-main restage of the consent-bounded Republic customs-precedent ambient consequence layer. It consumes the integrated `A2 Republic Customs Review:*` outcome and consent memory read-only.

Four Republic News groups correspond to the resolved customs-review outcomes:

1. bounded document audit;
2. written uncertainty;
3. contextualized routing;
4. preserved formal-process refusal.

Every public News group requires both `A2 Republic Customs Review: later reader seen` and `A2 Republic Customs Review: precedent use bounded`. The `precedent kept private` route never authorizes public News. The refusal-derived public example remains anonymized and procedural rather than identifying the player.

## Ownership and persistence invariants

- No `action`, mission, or conversation block exists in this slice.
- No persistent condition is written by this slice.
- No `world:*`, A1, B1, B2, or upstream A2 state is mutated.
- Republic customs scrutiny and border pressure remain owned by their existing authoritative systems.
- Existing A2 Republic Customs Review condition names are consumed exactly as integrated on current `main`; no save migration is required.
- No credits, reputation, cargo, equipment, ship, fleet, combat, destination, waypoint, or objective mutation is introduced.
- No public News is emitted for private-precedent or declined-only state.

## Files

- `data/human/a2 republic customs precedent news.txt`
- `tools/story/validate_a2_republic_customs_precedent_news.py`
- `story/A2_REPUBLIC_CUSTOMS_PRECEDENT_NEWS_RESTAGE_HANDOFF_20260824.md`

## Validation evidence

Exact validated production/validator head: `8f13630a534166fd847b139e94715cfeeb33af3f`.

- `Fork simulation and story validation` run `32754754071` / #550: **SUCCESS**.
- `Fork save-load integration smoke` run `32754754020` / #535: **SUCCESS**.

The strengthened validator requires exactly four Republic News groups, exact outcome-memory gates, `later reader seen` on every group, bounded-consent gating on every group, absence of private-precedent authorization, zero persistent writes, zero gameplay objectives/material mutations, and Republic-only scope.

No manual actual-game runtime result is claimed from unrelated hosts.

## Process / workspace boundary

The exposed private process service again reported four pre-existing service-owned orphan processes. None were modified. That host is not treated as authoritative `Wiredshark/star` runtime evidence.

## A3 integration boundary

Do not self-integrate. A3 must re-read current `main`, verify ancestry/mergeability, preserve upstream A2/A1 read-only ownership, preserve bounded-consent privacy semantics, and avoid integrating historical PR #60 together with this restage.
