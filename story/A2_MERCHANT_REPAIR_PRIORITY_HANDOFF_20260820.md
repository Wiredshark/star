# A2 Merchant Repair Priority handoff

Verdict: PARTIAL until exact-head repository CI and actual-game acceptance complete.

- Authoritative base: `main@cfa1b0e4744b31540f59543185024de0ddcb8db9`.
- Branch: `agent/a2-merchant-repair-priority-20260820-0004`.
- Production commit: `deb5890e09cdbfb4790c61c4fa045ae7c45ef683`.
- Validator commit: `445ff9cb145d2176a4e45cea1b87ca665225e84a`.
- Loop: A1 Merchant repair backlog >=3 -> player chooses safety/freight/oldest-obligation/refusal -> backlog recovers <=1 -> later review distinguishes A1 repair surge active versus quiet for each positive policy.
- Ownership invariant: `world: merchant repair backlog`, `world: merchant repair surge`, and `world: merchant rescue load` are read-only to A2. New writes are confined to `A2 Merchant Repair Priority:*`.
- Persistence: standard condition-based persistence; absent conditions are safe defaults for old saves.
- A3 integration: do not integrate until focused/story/style CI, production build/save-load smoke, and actual-game offer/branch/one-shot behavior are accepted. Preserve A1 sole-writer authority.
- Runtime/process boundary: no authoritative `Wiredshark/star` execution host/process checkout was available to this run; do not infer runtime evidence from unrelated hosts.
- Remaining acceptance: exact-head focused validator; repository story/simulation/style suite; production build/save-load smoke; actual-game backlog >=3 offer; all four initial routes; six surge/quiet recovery outcomes; refusal handling; save/reload between stages; duplicate-offer suppression; Merchant offer-precedence regression.
