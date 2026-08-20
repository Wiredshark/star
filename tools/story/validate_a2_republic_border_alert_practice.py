#!/usr/bin/env python3
from pathlib import Path

p = Path("data/human/a2 republic border alert practice.txt")
s = p.read_text(encoding="utf-8")

required = [
    'mission "A2 Republic Border Alert Practice: Briefing"',
    'mission "A2 Republic Border Alert Practice: Recovery Review"',
    '"world: republic border pressure" >= 4',
    '"world: republic border pressure" <= 2',
    '"A2 Republic Border Alert Practice: basis" = 1',
    '"A2 Republic Border Alert Practice: continuity" = 1',
    '"A2 Republic Border Alert Practice: review" = 1',
    '"A2 Republic Border Alert Practice: refusal" = 1',
    '"A2 Republic Border Alert Practice: recovery seen" = 1',
]
for token in required:
    assert token in s, f"missing required token: {token}"

# A2 may read A1 border pressure but must never write it.
for line in s.splitlines():
    stripped = line.strip()
    if stripped.startswith('"world: republic border pressure"'):
        assert not any(op in stripped for op in ("+=", "-=", "= 1", "= 0", "<?=", ">?=")), stripped

# All state mutations must stay in this A2 namespace.
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

assert s.count('mission "A2 Republic Border Alert Practice:') == 2
assert s.endswith("\n")
print("PASS: Republic border alert practice structure, persistence, and A1 read-only ownership")
