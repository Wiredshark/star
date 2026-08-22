# A2 Merchant Repair Priority current-main restage handoff

Verdict: PARTIAL pending exact-head repository-native validation.

- Authoritative base: `main@a17a89fb4779200a0634a6dade1811c4dc9cc2be`.
- Branch: `agent/a2-merchant-repair-priority-restage-20260822-0302`.
- Production restage: `887eb4734e5fac9332849b373f26e6932745fba5`.
- Strengthened validator: `c1f171c89739c9ced221b3975dde5bd0e0369cd1`.
- Loop: A1 Merchant repair backlog >=3 -> player chooses safety/freight/oldest-obligation/refusal -> authoritative backlog recovery <=1 -> review distinguishes whether A1 pooled repair surge remains active, producing six positive simulation-sensitive outcomes plus refusal-respected handling.
- Ownership: `world: merchant repair backlog`, `world: merchant repair surge`, and `world: merchant rescue load` are read-only. All writes are confined to `A2 Merchant Repair Priority:*`.
- Persistence: condition-based and save-compatible; absent A2 conditions are safe defaults for older saves.
- Lifecycle: both dialogue-only missions use `offer precedence 9`; all five objective-less terminal paths use `decline`; no gameplay objectives are introduced.
- Invariants: safety release criteria are not overridden by commercial schedule; freight continuity keeps displacement visible; queue exceptions remain reviewable; temporary pooled capacity does not become permanent seniority; refusal remains refusal.
- A3 integration: do not integrate until exact-head simulation/story/style and production build/save-load gates are terminal green. Preserve A1 sole-writer authority and the state-only decline lifecycle.
