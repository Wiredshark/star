#!/usr/bin/env python3
"""Focused structural validator for B2 Hai Mourning Song Choice Compact."""
from __future__ import annotations
import re, sys
from pathlib import Path

PATH = Path("data/hai/b2 hai mourning song choice compact.txt")
PREFIX = "B2 Hai Mourning Song Choice Compact:"

def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr); raise SystemExit(1)

def mission_block(text: str, name: str) -> str:
    m = re.search(rf'^mission "{re.escape(name)}"$(.*?)(?=^mission "|\Z)', text, re.M | re.S)
    if not m: fail(f"missing mission {name}")
    return m.group(0)

def label_block(block: str, label: str) -> str:
    m = re.search(rf'^\s*label {re.escape(label)}\s*$(.*?)(?=^\s*label [A-Za-z0-9_-]+\s*$|\Z)', block, re.M | re.S)
    if not m: fail(f"missing label {label}")
    return m.group(0)

def main() -> None:
    if not PATH.is_file(): fail(f"missing {PATH}")
    text = PATH.read_text(encoding="utf-8"); lower = text.lower()
    expected = [f"{PREFIX} Offer", f"{PREFIX} Review", f"{PREFIX} Tira Remembers"]
    missions = re.findall(r'^mission "([^"]+)"$', text, re.M)
    if missions != expected: fail(f"unexpected missions {missions}")
    if text.count('government "Hai"') != 3 or text.count('has "language: Hai"') != 3: fail("all missions must be Hai and require Hai language")
    if re.search(r'^\s*accept\s*$', text, re.M): fail("state-only slice must not accept")
    if text.count("\t\t\t\tdecline") != 7: fail("expected seven terminal declines")
    for line in text.splitlines():
        s=line.strip().lower()
        if line.startswith("\t") and any(s.startswith(x) for x in ("destination ","stopover ","waypoint ","npc ","cargo ","passenger ","deadline ","timer ")): fail(f"objective directive {s}")
    writes = re.findall(r'^\s*"([^"]+)"\s*=\s*1\s*$', text, re.M)
    if any(not w.startswith(PREFIX) for w in writes): fail("out-of-scope persistent write")

    offer = mission_block(text, f"{PREFIX} Offer")
    routes = {"evidence":"route preference evidence", "family":"route living family choice", "layered":"route layered remembrance"}
    for label, state in routes.items():
        b=label_block(offer,label)
        if b.count(f'"{PREFIX} introduced" = 1') != 1: fail(f"{label} must introduce exactly once")
        if b.count(f'"{PREFIX} {state}" = 1') != 1: fail(f"{label} missing own route state")
        if b.count(f'event "{PREFIX} Review Ready" 7 11') != 1: fail(f"{label} must schedule one review")
        if b.count("\n\t\t\t\tdecline") != 1: fail(f"{label} must terminate once")
        for other in set(routes.values())-{state}:
            if f'"{PREFIX} {other}" = 1' in b: fail(f"{label} writes another route")
    refusal=label_block(offer,"decline")
    if f'"{PREFIX} declined" = 1' not in refusal: fail("refusal missing state")
    if f'"{PREFIX} introduced" = 1' in refusal or 'Review Ready" 7 11' in refusal: fail("refusal must not arm review")

    review=mission_block(text,f"{PREFIX} Review")
    for gate in ("introduced","review ready"):
        if f'has "{PREFIX} {gate}"' not in review: fail(f"review missing {gate} gate")
    if f'not "{PREFIX} reviewed"' not in review: fail("review must be one-shot")
    for label,state in (("annotated","settlement annotated memorial"),("renewal","settlement living renewal")):
        b=label_block(review,label)
        if b.count(f'"{PREFIX} reviewed" = 1') != 1 or b.count(f'"{PREFIX} {state}" = 1') != 1: fail(f"{label} settlement persistence invalid")
        if b.count("\n\t\t\t\tdecline") != 1: fail(f"{label} settlement must terminate once")

    after=mission_block(text,f"{PREFIX} Tira Remembers")
    if f'not "{PREFIX} aftermath seen"' not in after: fail("aftermath must be one-shot")
    for state in ("settlement annotated memorial","settlement living renewal"):
        if f'has "{PREFIX} {state}"' not in after: fail(f"aftermath missing {state}")
    if after.count(f'"{PREFIX} aftermath seen" = 1') != 1: fail("aftermath write count")

    for concept in ("recording","preference","family","memory","uncertainty","memorial","correction","universal hai mourning law"):
        if concept not in lower: fail(f"missing concept {concept}")
    for bad in ("yari ordered every memorial","hai law requires","recording proves final intent","family memory is independent corroboration"):
        if bad in lower: fail(f"unsupported claim {bad}")
    print("PASS: B2 Hai Mourning Song Choice Compact validated")

if __name__ == "__main__": main()
