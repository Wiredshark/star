#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/avgi/a2 avgi dissonance evidence practice.txt"
text = PATH.read_text(encoding="utf-8")

required = [
    'mission "A2 Avgi Dissonance Evidence Practice"',
    'mission "A2 Avgi Dissonance Evidence Practice: Reflection"',
    'has "language: Avgi (Written)"',
    'not "avgi: lost in twilight"',
    'set "A2 Avgi Dissonance Evidence Practice: full record"',
    'set "A2 Avgi Dissonance Evidence Practice: burden separate"',
    'set "A2 Avgi Dissonance Evidence Practice: local only"',
    'set "A2 Avgi Dissonance Evidence Practice: refused"',
    'set "A2 Avgi Dissonance Evidence Practice: reflection seen"',
]
for needle in required:
    assert needle in text, f"missing required contract: {needle}"

assert text.count('mission "A2 Avgi Dissonance Evidence Practice') == 2
assert 'world:' not in text, "A2 slice must not own world simulation state"
for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith("set "):
        assert '"A2 Avgi Dissonance Evidence Practice:' in stripped, f"foreign state write: {stripped}"

for forbidden in ["speaking for Dissonance", "Dissonance representative", "Dissonance authority"]:
    assert forbidden not in text

print("PASS: A2 Avgi Dissonance Evidence Practice contracts")
