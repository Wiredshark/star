# B2 Near Earth Port Promise Compact Handoff

## Verdict

READY for A3 review/integration.

## Repository authority

- Authoritative integration branch: `main`
- Authoritative base SHA selected for this slice: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`
- Isolated branch: `agent/b2-near-earth-port-promise-compact-20260820-1924`
- Production commit: `1f46940d8d9519436288e7d258cd2632dd1383a5`
- Focused validator commit: `575caa385116f8e084f50c19ad443bd628b80ca3`
- Exact fully validated production/validator/handoff candidate: `b77fe18dee04d636e255b2cd7430e499cf880624`

## Scope

Adds a three-mission Near Earth character/dynamic-content arc based on the already integrated B1 `Near Earth Maintenance Ledger`.

Named characters:

- **Mira Hollis** — a Near Earth port maintenance coordinator focused on continuity of the original repair promise and who remains responsible for it.
- **Jonas Keene** — an independent mechanic focused on current technical reality, useful substitutes, and the conditions under which a local repair should count as satisfying an older obligation.

The conflict begins when a freighter moves between Near Earth ports before an originally promised radiator assembly arrives. A receiving yard installs a compatible substitute, creating a distinction among:

- the original repair promise;
- the current repair state;
- substitute provenance;
- compatibility assumptions;
- the captain's acceptance;
- transferred responsibility;
- explicit closure evidence.

Initial persistent routes:

1. original promise follows the ship until explicitly fulfilled, transferred, substituted, or forgiven;
2. receiving yard may close the old obligation after an accepted equivalent repair, but must record the substitution and technical basis;
3. paired original-obligation/current-repair records remain linked until explicit reconciliation;
4. refusal, which does not schedule the later Review.

Each substantive route schedules a Review after 7-11 days.

The Review resolves into exactly one of two persistent outcomes:

- **portable obligation packet** — original promise, responsible party, current repair state, substitute provenance, compatibility assumptions, acceptance, and closure evidence travel together;
- **reconciliation rule** — original obligation and current repair state remain distinct until later review explicitly records fulfillment, transfer, accepted equivalence, forgiveness, or reopening.

`Jonas Remembers` is the one-shot aftermath reader.

## Continuity / ownership invariants

- Consumes B1 `Near Earth Maintenance Ledger: offered` as read-only historical context.
- All direct persistent writes are under `B2 Near Earth Port Promise Compact:*`.
- No A1 `world:*`, credits, reputation, cargo, outfit, ship, fleet, or combat mutation.
- A working substitute is not automatically identical to the originally promised part.
- Physical fit is not sufficient evidence of full compatibility; pressure, heat, service interval, controls, and other operating assumptions may matter.
- A ship moving ports does not silently erase the original repair obligation.
- A local accepted substitute may satisfy an obligation only when the substitution, technical basis, acceptance, and closure are explicit.
- This is practical cross-port continuity among Near Earth yards, not a centralized Near Earth maintenance authority.

## Concurrency / non-overlap review

Before branching, live `main`, recent commits, current `agent/b1-*` and `agent/b2-*` branch inventories, open PRs, and the available process inventory were inspected.

No prior Near Earth B2 branch or active Near Earth A2/B2 candidate was found. Existing B2 repair/obligation slices target other domains: Pirate credit, Merchant recovery margin, Core qualification/repair reciprocity, Kor Efret reconstruction, and related faction-specific institutions. This slice is specifically about the integrated Near Earth maintenance-ledger history and cross-port promise/substitution continuity.

The private execution service reported four pre-existing service-owned processes; none were modified or terminated.

## Files

- `data/human/b2 near earth port promise compact.txt`
- `tools/story/validate_b2_near_earth_port_promise_compact.py`
- `story/B2_NEAR_EARTH_PORT_PROMISE_COMPACT_HANDOFF_20260820.md`

## Exact validation evidence

On exact candidate `b77fe18dee04d636e255b2cd7430e499cf880624`:

- `Fork simulation and story validation` #281 / run `32428794221`: **SUCCESS**.
- Changed fork content style: **SUCCESS**.
- Focused simulation and story contracts: **SUCCESS**.
- All focused story validators, including `validate_b2_near_earth_port_promise_compact.py`: **SUCCESS**.
- A1 simulation contract tests: **SUCCESS**.
- `Fork save-load integration smoke` #266 / run `32428794209`: **SUCCESS**.
- Production configure: **SUCCESS**.
- Production build: **SUCCESS**.
- Stock save-load smoke: **SUCCESS**.

The focused validator command is:

```text
python3 tools/story/validate_b2_near_earth_port_promise_compact.py
```

## A3 / B3 guidance

A3 should re-read current `main`, verify ancestry/conflicts, and integrate only if the validated candidate remains semantically clean against the then-current integration state. The final handoff-only commit does not change production content or validator behavior.

B3 should preserve the distinction among the original obligation, current repair state, substitute provenance, technical compatibility assumptions, acceptance, transferred responsibility, and explicit closure evidence. A useful local repair must not silently rewrite what another port originally promised.
