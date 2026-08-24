#!/usr/bin/env python3
from pathlib import Path
import re
import sys

path = Path("data/human/a2 free worlds repair priority.txt")
text = path.read_text(encoding="utf-8")
errors: list[str] = []


def need(token: str) -> None:
    if token not in text:
        errors.append(f"missing: {token}")


for token in [
    'mission "A2 Free Worlds Repair Priority: Yard Briefing"',
    'mission "A2 Free Worlds Repair Priority: Recovery Review"',
    '"offer precedence" 9',
    '"world: free worlds repair backlog" >= 3',
    '"world: free worlds repair backlog" <= 1',
    'has "world: free worlds patrol surge"',
    '"A2 Free Worlds Repair Priority: priority safety" = 1',
    '"A2 Free Worlds Repair Priority: priority patrol" = 1',
    '"A2 Free Worlds Repair Priority: priority civilian" = 1',
    '"A2 Free Worlds Repair Priority: refused" = 1',
    '"A2 Free Worlds Repair Priority: refusal respected" = 1',
    '"A2 Free Worlds Repair Priority: recovery seen" = 1',
    '"A2 Free Worlds Repair Priority: Venn remembers safety under surge" = 1',
    '"A2 Free Worlds Repair Priority: Venn remembers safety after quiet" = 1',
    '"A2 Free Worlds Repair Priority: Venn remembers patrol under surge" = 1',
    '"A2 Free Worlds Repair Priority: Venn remembers patrol after quiet" = 1',
    '"A2 Free Worlds Repair Priority: Venn remembers civilian under surge" = 1',
    '"A2 Free Worlds Repair Priority: Venn remembers civilian after quiet" = 1',
    'label mobilized',
    'label choose',
    'label safety',
    'label patrol',
    'label civilian',
    'label refuse',
    'label safety_surge',
    'label safety_quiet',
    'label patrol_surge',
    'label patrol_quiet',
    'label civilian_surge',
    'label civilian_quiet',
    'label finish',
]:
    need(token)

if text.count('mission "A2 Free Worlds Repair Priority:') != 2:
    errors.append("expected exactly two A2 Free Worlds Repair Priority missions")
if text.count('"offer precedence" 9') != 2:
    errors.append("expected offer precedence 9 on both state-only missions")
if text.count('\n\t\t\t\tdecline') != 5:
    errors.append("expected exactly five state-only terminal decline commands")
if re.search(r"(?m)^\s*accept\s*$", text):
    errors.append("state-only A2 missions must not use terminal accept")

# Both missions are dialogue/state-only. Reject actual objective-bearing directives,
# while ignoring words that merely occur in backtick dialogue prose.
for raw_line in text.splitlines():
    stripped = raw_line.lstrip("\t")
    if raw_line == stripped or stripped.startswith("`"):
        continue
    directive = stripped.split(maxsplit=1)[0] if stripped else ""
    if directive in {
        "cargo", "passengers", "destination", "waypoint", "stopover",
        "npc", "deadline", "date", "outfit", "ship", "fleet",
    }:
        errors.append(f"unexpected gameplay objective directive: {stripped}")

# A1 owns both consumed signals. Comparisons and `has` reads are allowed;
# assignments and explicit set/clear operations are not.
for line in text.splitlines():
    if "world: free worlds repair backlog" in line or "world: free worlds patrol surge" in line:
        stripped = line.strip()
        if re.search(r'"world: free worlds (?:repair backlog|patrol surge)"\s*(?:=|\+=|-=)', stripped):
            errors.append(f"forbidden A1 assignment: {stripped}")
        if stripped.startswith("set ") or stripped.startswith("clear "):
            errors.append(f"forbidden A1 mutation: {stripped}")

# All writes in this slice must remain A2-namespaced.
for line in text.splitlines():
    stripped = line.strip()
    if re.search(r'"[^\"]+"\s*=\s*-?\d+', stripped):
        key = stripped.split('"', 2)[1]
        if not key.startswith("A2 Free Worlds Repair Priority:"):
            errors.append(f"write outside A2 namespace: {stripped}")

# Recovery review must expose all six world-state-sensitive outcomes and a refusal path.
for route in ("safety", "patrol", "civilian"):
    need(f'branch {route}_surge')
    need(f'branch {route}_quiet')
    need(f'has "A2 Free Worlds Repair Priority: priority {route}"')

if text.count("goto finish") != 6:
    errors.append("expected six positive/refusal recovery paths to converge on finish")

if errors:
    print("FAIL")
    for error in errors:
        print(error)
    sys.exit(1)

print("PASS: Free Worlds repair priority preserves A1 ownership, five-decline dialogue lifecycle, refusal boundary, and six surge/quiet recovery outcomes")
