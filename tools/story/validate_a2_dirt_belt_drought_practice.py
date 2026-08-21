#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/human/a2 dirt belt drought practice.txt"
text = PATH.read_text(encoding="utf-8")

required = [
    'mission "A2 Dirt Belt Drought Practice: Briefing"',
    'mission "A2 Dirt Belt Drought Practice: Recovery Review"',
    '"world: dirt belt drought pressure" >= 3',
    '"world: dirt belt irrigation reserve strain" >= 2',
    '"world: dirt belt drought pressure" <= 1',
    '"world: dirt belt irrigation reserve strain" <= 1',
    '"A2 Dirt Belt Drought Practice: reserve floor" = 1',
    '"A2 Dirt Belt Drought Practice: restoration obligations" = 1',
    '"A2 Dirt Belt Drought Practice: current conditions" = 1',
    '"A2 Dirt Belt Drought Practice: declined" = 1',
    '"A2 Dirt Belt Drought Practice: recovery seen" = 1',
]
for needle in required:
    assert needle in text, f"missing required contract: {needle}"

# A2 may consume A1 world state, but every persistent write must stay A2-local.
for line in text.splitlines():
    stripped = line.strip()
    if " = " in stripped:
        assert '"A2 Dirt Belt Drought Practice:' in stripped, f"foreign state write: {stripped}"
    assert '"world: dirt belt drought pressure" =' not in stripped
    assert '"world: dirt belt irrigation reserve strain" =' not in stripped

# Both missions are state-only conversations. None may use mission acceptance,
# because that would leave an objective-less mission in the accepted list.
assert "\n\t\t\taccept" not in text, "state-only dialogue endpoint must not accept"
assert text.count("\n\t\t\tdecline") == 5, "all four briefing routes and recovery review must decline"

assert text.count('"A2 Dirt Belt Drought Practice: introduced" = 1') == 3
assert text.count('"A2 Dirt Belt Drought Practice: recovery seen" = 1') == 1
assert 'not "A2 Dirt Belt Drought Practice: declined"' in text
assert 'not "A2 Dirt Belt Drought Practice: recovery seen"' in text
print("A2 Dirt Belt Drought Practice validator: PASS")
