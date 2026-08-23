#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data/korath/a2 kor efret reconstruction echo.txt"
text = PATH.read_text(encoding="utf-8")
lines = text.splitlines()

required = [
    'mission "A2 Kor Efret Reconstruction Echo: Practice"',
    'mission "A2 Kor Efret Reconstruction Echo: Reflection"',
    'has "B2 Kor Efret Reconstruction Compact: aftermath seen"',
    'has "B2 Kor Efret Reconstruction Compact: settlement restoration priority"',
    '"A2 Kor Efret Reconstruction Echo: route local" = 1',
    '"A2 Kor Efret Reconstruction Echo: route method" = 1',
    '"A2 Kor Efret Reconstruction Echo: route example" = 1',
    '"A2 Kor Efret Reconstruction Echo: reflection seen" = 1',
]
for needle in required:
    assert needle in text, f"missing required contract: {needle}"

assert text.count('mission "A2 Kor Efret Reconstruction Echo:') == 2
assert text.count("offer precedence 9") == 2, "both state-only missions need current precedence"
assert text.count("\n\t\t\tdecline") == 4, "three Practice routes plus Reflection must decline"
assert "\n\t\t\taccept" not in text, "state-only missions must not remain accepted"
assert text.count('"A2 Kor Efret Reconstruction Echo: route ') == 6, "each route should be written once and read once"
assert text.count('has "B2 Kor Efret Reconstruction Compact: aftermath seen"') == 2, "both stages must recheck the B2 aftermath"

reflection = text.split('mission "A2 Kor Efret Reconstruction Echo: Reflection"', 1)[1]
for route in ("local", "method", "example"):
    assert f"branch {route}" in reflection, f"reflection missing explicit {route} branch"
    assert f'has "A2 Kor Efret Reconstruction Echo: route {route}"' in reflection, f"reflection missing {route} route gate"
    assert f"label {route}" in reflection, f"reflection missing {route} label"

# This consumer may read B2 state, but never write it. It has no world-state authority.
for line in lines:
    stripped = line.strip()
    if stripped.startswith('"B2 Kor Efret Reconstruction Compact:'):
        assert "=" not in stripped and "+=" not in stripped and "-=" not in stripped, f"illegal B2 write: {stripped}"
    if stripped.startswith('"world:'):
        raise AssertionError(f"A2 reconstruction echo must not use world-state authority: {stripped}")
    if stripped.startswith('"') and any(op in stripped for op in (" = ", " += ", " -= ")):
        assert stripped.startswith('"A2 Kor Efret Reconstruction Echo:'), f"write outside A2 namespace: {stripped}"

# These are dialogue/state-only missions. Reject actual objective-bearing directives while
# ignoring ordinary prose inside backtick conversation lines.
objective_directives = (
    "destination ", "stopover ", "waypoint ", "npc ", "cargo ", "passenger ",
    "deadline ", "timer ", "outfit ", "ship ", "fleet ", "credits ", "reputation ",
)
for line in lines:
    stripped = line.strip().lower()
    if not stripped or stripped.startswith("`") or stripped.startswith("#"):
        continue
    for directive in objective_directives:
        assert not stripped.startswith(directive), f"unexpected gameplay objective/mutation directive: {line.strip()}"

for phrase in [
    "does not make me an authority",
    "borrowed authority",
    "evidence, not command",
    "neither title nor standing authority",
]:
    assert phrase in text, f"missing authority-boundary phrase: {phrase}"

print("PASS: A2 Kor Efret Reconstruction Echo current-main contracts")
