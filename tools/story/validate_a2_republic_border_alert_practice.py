#!/usr/bin/env python3
from pathlib import Path

p = Path("data/human/a2 republic border alert practice.txt")
s = p.read_text(encoding="utf-8")

required = [
    'mission "A2 Republic Border Alert Practice: Briefing"',
    'mission "A2 Republic Border Alert Practice: Recovery Review"',
    '"offer precedence" 8',
    '"world: republic border pressure" >= 4',
    '"world: republic border pressure" <= 2',
    '"A2 Republic Border Alert Practice: basis" = 1',
    '"A2 Republic Border Alert Practice: continuity" = 1',
    '"A2 Republic Border Alert Practice: review" = 1',
    '"A2 Republic Border Alert Practice: refusal" = 1',
    '"A2 Republic Border Alert Practice: recovery pending" = 1',
    '"A2 Republic Border Alert Practice: recovery pending" = 0',
    '"A2 Republic Border Alert Practice: recovery seen" = 1',
    'Pirate-space origin is never treated as evidence of individual guilt',
]
for token in required:
    assert token in s, f"missing required token: {token}"

assert s.count('mission "A2 Republic Border Alert Practice:') == 2
assert s.count('"offer precedence" 8') == 2

# A2 may read A1 border pressure but must never write it.
for line in s.splitlines():
    stripped = line.strip()
    if stripped.startswith('"world: republic border pressure"'):
        assert not any(op in stripped for op in ("+=", "-=", "<?=", ">?=")), stripped
        if "=" in stripped:
            assert ">=" in stripped or "<=" in stripped or "==" in stripped or "!=" in stripped, stripped

# Every persistent state mutation must stay inside this A2 namespace.
in_action = False
for line in s.splitlines():
    stripped = line.strip()
    if stripped == "action":
        in_action = True
        continue
    if in_action and stripped and not line.startswith("\t\t\t\t"):
        in_action = False
    if in_action and stripped.startswith('"') and "=" in stripped:
        assert stripped.startswith('"A2 Republic Border Alert Practice:'), stripped

# Current lifecycle invariant: these are state-only dialogue missions, so terminal
# paths close after persisting state instead of entering the accepted-mission list.
objective_tokens = (
    "\tcargo ", "\tpassengers ", "\tdestination ", "\twaypoint ",
    "\tstopover ", "\tnpc ", "\tdeadline ", "\tto complete", "\ton complete",
)
for token in objective_tokens:
    assert token not in s, f"unexpected gameplay objective in state-only slice: {token!r}"
assert "\t\t\t\taccept\n" not in s, "state-only dialogue must not terminate with accept"
assert s.count("\t\t\t\tdecline\n") == 5, "expected four briefing terminals plus one recovery terminal"

# Refusal is a real route and must not be silently rewritten as a positive route.
refusal_block = s.split("label refuse", 1)[1].split('mission "A2 Republic Border Alert Practice: Recovery Review"', 1)[0]
assert '"A2 Republic Border Alert Practice: refusal" = 1' in refusal_block
assert not any(f'"A2 Republic Border Alert Practice: {route}" = 1' in refusal_block for route in ("basis", "continuity", "review"))

assert s.endswith("\n")
print("PASS: Republic border alert practice gating, lifecycle, persistence, refusal, and A1 read-only ownership")
