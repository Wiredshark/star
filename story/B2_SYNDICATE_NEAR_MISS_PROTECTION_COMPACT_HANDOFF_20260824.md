# B2 Syndicate Near-Miss Protection Compact — handoff

Verdict: READY for A3 review/integration.

## Scope
Deepens A2 recurring character Tessa Marr and introduces contract technician Niko Renn in a corporate/labor-safety arc about near-miss evidence, reporter identity, retaliation risk, investigation, and corrective authority.

## Base and isolation
- Authoritative base: `a17a89fb4779200a0634a6dade1811c4dc9cc2be`.
- Branch: `agent/b2-syndicate-near-miss-protection-20260824`.
- Exact fully validated production/validator candidate: `c0307e80f7ef46612a410c1f4acc13272198fdd9`.
- No self-integration. A3 retains integration authority.

## Dependencies and ownership
- Reads `A2 Syndicate Maintenance Triage: followup seen` to continue Tessa Marr's established character history.
- Reads A1 `world: syndicate labor strain` and `world: syndicate labor rotation active`; B2 never writes them.
- Consumes the B1 Syndicate dockyard-labor institutional premise; does not redefine qualification authority.
- Writes only `B2 Syndicate Near-Miss Protection Compact:*`.

## Behavior
Three substantive routes plus refusal; substantive routes schedule a Review after 7–11 days; Review waits for labor strain to recover and crew rotation to end; two persistent settlements (`packet`, `expiry`); one-shot `Renn Remembers` aftermath. All seven state-only dialogue terminals use `decline`.

## Canon and persistence assumptions
A safety report is evidence, not a personnel verdict. Reporter identity, technical evidence, investigation cause, access purpose, retaliation review, discipline, corrective action, and closure remain separate facts. Suspicious timing may trigger review but is not itself proof of retaliation. No save migration is required because the slice adds only new namespaced conditions.

## Diversity check
- Primary domain: corporate labor conflict / whistleblower safety / interpersonal trust.
- Recent domains considered: Free Worlds grief/public memory; Hai entertainment/public persona.
- Non-economic inputs: A2 Marr relationship/history, A1 labor strain, A1 crew-rotation state.
- Not a freight/logistics reskin: no cargo, route, market, or convoy objective; the conflict is disclosure, retaliation risk, and investigative authority.
- Persistent consequences: Marr/Renn trust, chosen reporting rule, later settlement, one-shot aftermath.

## Validation
Exact candidate `c0307e80f7ef46612a410c1f4acc13272198fdd9` passed:
- focused validator for this compact;
- all 49 focused story validators;
- A1 regression suite: 128 passed;
- changed-content style: PASS;
- `git diff --check`: PASS;
- GitHub `Fork simulation and story validation` run `32694222132` / #516: SUCCESS;
- GitHub `Fork save-load integration smoke` run `32694222144` / #501: SUCCESS, including production configure/build and stock save-load smoke.

The final commit after this validated candidate changes only this durable handoff document.
