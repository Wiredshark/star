# B2 Avgi Dissonance Tax Appeal Compact handoff — 2026-08-20

## Verdict

PARTIAL pending repository-native validation on the exact branch head.

## Authority and isolation

- Repository: `Wiredshark/star`
- Authoritative integration base: `a44dc035658d928e4becf0398ab9ce41e0c39e0a`
- Isolated branch: `agent/b2-avgi-dissonance-tax-appeal-20260820-0424`
- B2 production commit: `8ab070b18884e6c3a4fac1c2691231281a1ecd02`
- B2 focused-validator commit: `9c116cf06a8f64e5ecc23b7f4250fa1a0ea1524c`
- Integration authority remains A3. B2 must not self-integrate.

## Character/dynamic-content slice

Adds `B2 Avgi Dissonance Tax Appeal Compact`, a three-mission Dissonance arc featuring records advocate Indigo and workshop accountant Sienna.

The arc consumes the newly integrated B1 Dissonance tax-challenge/protest history and turns its evidence discipline into a present-tense records problem: how a tax challenge should travel between worlds without either erasing the grievance or allowing an old objection to become a permanent verdict.

Initial persistent approaches:

1. preserve objection/evidence history in downstream copies;
2. prioritize the current verified assessment with a durable challenge-history link;
3. pair current assessment, challenge basis, evidence, disposition, and open/closed status;
4. refusal, which does not enter the settlement path.

The later Review resolves to exactly one of two persistent institutional outcomes:

- `settlement disposition packet`: challenge basis, evidence, current verified assessment, disposition, and open/closed status travel together;
- `settlement expiry renewal`: resolved challenges remain historical but stop propagating as active warnings unless fresh evidence opens a new review.

`Indigo Remembers` is the one-shot later reader.

## Continuity / ownership invariants

- All new persistent writes are namespaced under `B2 Avgi Dissonance Tax Appeal Compact:*`.
- `avgi:*` and `world:*` are read-only to this slice.
- No credits, reputation, cargo, outfit, ship, fleet, or combat-state mutations are introduced.
- Dissonance remains politically plural. This compact is a practical records convention, not a centralized Dissonance tax code or government.
- An objection, current verified assessment, evidence record, and disposition remain distinct concepts.
- The historical existence of a challenge is not itself fresh evidence and must not become a permanent active accusation after resolution.

## Files

- `data/avgi/b2 avgi dissonance tax appeal compact.txt`
- `tools/story/validate_b2_avgi_dissonance_tax_appeal_compact.py`
- `story/B2_AVGI_DISSONANCE_TAX_APPEAL_COMPACT_HANDOFF_20260820.md`

## Required validation before READY

Run repository-native gates on the exact final B2 head:

- focused validator: `python3 tools/story/validate_b2_avgi_dissonance_tax_appeal_compact.py`
- standard focused story/simulation suite
- changed-content style validation
- production Endless Sky configure/build
- stock save/load smoke cases used by the fork workflows

A3 should promote this handoff to READY only after those exact-head gates are terminal green.

## A3 / B3 integration notes

Base already contains the B1 Avgi Dissonance institutional-history slice. A3 should integrate only this isolated B2 branch after validation. B3 continuity review should specifically preserve the distinction between grievance memory and adjudicated/current tax state, and should reject any downstream content that treats a copied objection as proof of wrongdoing merely because it remains historically visible.
