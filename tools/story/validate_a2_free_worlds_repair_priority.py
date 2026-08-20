#!/usr/bin/env python3
from pathlib import Path
import sys

p = Path("data/human/a2 free worlds repair priority.txt")
text = p.read_text(encoding="utf-8")
errors = []

def need(s):
    if s not in text:
        errors.append(f"missing: {s}")

for s in [
    'mission "A2 Free Worlds Repair Priority: Yard Briefing"',
    'mission "A2 Free Worlds Repair Priority: Recovery Review"',
    '"world: free worlds repair backlog" >= 3',
    '"world: free worlds repair backlog" <= 1',
    'has "world: free worlds patrol surge"',
    '"A2 Free Worlds Repair Priority: priority safety" = 1',
    '"A2 Free Worlds Repair Priority: priority patrol" = 1',
    '"A2 Free Worlds Repair Priority: priority civilian" = 1',
    '"A2 Free Worlds Repair Priority: refused" = 1',
    '"A2 Free Worlds Repair Priority: recovery seen" = 1',
    'Venn remembers safety under surge',
    'Venn remembers safety after quiet',
    'Venn remembers patrol under surge',
    'Venn remembers patrol after quiet',
    'Venn remembers civilian under surge',
    'Venn remembers civilian after quiet',
    'refusal respected',
]:
    need(s)

for forbidden in [
    '"world: free worlds repair backlog" =',
    '"world: free worlds repair backlog" +=',
    '"world: free worlds repair backlog" -=',
    'set "world: free worlds repair backlog',
    'clear "world: free worlds repair backlog',
    'set "world: free worlds patrol surge"',
    'clear "world: free worlds patrol surge"',
]:
    if forbidden in text:
        errors.append(f"forbidden A1 write: {forbidden}")

if text.count('mission "A2 Free Worlds Repair Priority:') != 2:
    errors.append("expected exactly two A2 repair-priority missions")

if errors:
    print("FAIL")
    for e in errors:
        print(e)
    sys.exit(1)
print("PASS: Free Worlds repair priority structure, six recovery outcomes, refusal boundary, and A1 read-only ownership")
