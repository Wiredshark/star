#!/usr/bin/env python3
"""Validate B2 Coalition Games Rivalry Compact structure and ownership."""
from __future__ import annotations

import re
import sys
from pathlib import Path

PATH = Path("data/coalition/b2 coalition games rivalry compact.txt")
PREFIX = "B2 Coalition Games Rivalry Compact:"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def mission_block(text: str, name: str) -> str:
    match = re.search(rf'^mission "{re.escape(name)}"$(.*?)(?=^mission "|\Z)', text, re.M | re.S)
    if not match:
        fail(f"missing mission {name}")
    return match.group(0)


def label_block(block: str, label: str) -> str:
    match = re.search(
        rf'^\s*label {re.escape(label)}\s*$(.*?)(?=^\s*label [A-Za-z0-9_-]+\s*$|\Z)',
        block,
        re.M | re.S,
    )
    if not match:
        fail(f"missing label {label}")
    return match.group(0)


def main() -> None:
    if not PATH.is_file():
        fail(f"missing {PATH}")
    text = PATH.read_text(encoding="utf-8")
    lower = text.lower()

    expected = [
        f"{PREFIX} Offer",
        f"{PREFIX} Review",
        f"{PREFIX} Seli Remembers",
    ]
    missions = re.findall(r'^mission "([^"]+)"$', text, re.M)
    if missions != expected:
        fail(f"unexpected mission graph: {missions}")

    if text.count('government "Coalition"') != 3:
        fail("all three missions must source from Coalition space")
    if text.count('has "known to the heliarchs"') != 3:
        fail("all three missions must consume Heliarch-recognition state")
    if "Coalition Games" not in text:
        fail("missing Coalition Games canon hook")

    if re.search(r'^\s*accept\s*$', text, re.M):
        fail("state-only slice must not use terminal accept")
    declines = len(re.findall(r'^\s*decline\s*$', text, re.M))
    if declines != 7:
        fail(f"expected seven terminal declines, found {declines}")

    objective = re.compile(
        r'^\t(?:destination|stopover|waypoint|npc|cargo|passengers?|deadline|timer)\b',
        re.M | re.I,
    )
    if objective.search(text):
        fail("unexpected gameplay objective directive")

    writes = re.findall(r'^\s*"([^"]+)"\s*=\s*[-0-9]+\s*$', text, re.M)
    if not writes:
        fail("no persistent writes found")
    foreign = sorted({write for write in writes if not write.startswith(PREFIX)})
    if foreign:
        fail(f"writes outside B2 namespace: {foreign}")

    if len(re.findall(rf'^event "{re.escape(PREFIX)} Review Ready"$', text, re.M)) != 1:
        fail("Review Ready event must be declared exactly once")
    if text.count(f'event "{PREFIX} Review Ready" 7 11') != 3:
        fail("exactly the three substantive routes must schedule Review")

    offer = mission_block(text, f"{PREFIX} Offer")
    routes = {
        "separate": "route competition separate",
        "campaign": "route campaign consent",
        "paired": "route paired records",
    }
    for label, state in routes.items():
        block = label_block(offer, label)
        if block.count(f'"{PREFIX} introduced" = 1') != 1:
            fail(f"{label} must introduce exactly once")
        if block.count(f'"{PREFIX} {state}" = 1') != 1:
            fail(f"{label} missing its route state")
        if block.count(f'event "{PREFIX} Review Ready" 7 11') != 1:
            fail(f"{label} must schedule exactly one 7-11 day Review")
        if len(re.findall(r'^\s*decline\s*$', block, re.M)) != 1:
            fail(f"{label} must terminate exactly once")
        for other in set(routes.values()) - {state}:
            if f'"{PREFIX} {other}" = 1' in block:
                fail(f"{label} writes another route state")

    refusal = label_block(offer, "decline")
    if refusal.count(f'"{PREFIX} declined" = 1') != 1:
        fail("refusal missing declined state")
    if f'"{PREFIX} introduced" = 1' in refusal or f'event "{PREFIX} Review Ready" 7 11' in refusal:
        fail("refusal must not arm Review")
    if any(f'"{PREFIX} {state}" = 1' in refusal for state in routes.values()):
        fail("refusal writes substantive route state")
    if len(re.findall(r'^\s*decline\s*$', refusal, re.M)) != 1:
        fail("refusal must terminate exactly once")

    review = mission_block(text, f"{PREFIX} Review")
    for gate in ("introduced", "review ready"):
        if f'has "{PREFIX} {gate}"' not in review:
            fail(f"Review missing {gate} gate")
    if f'not "{PREFIX} reviewed"' not in review:
        fail("Review must be one-shot")

    review_route_branches = {
        "separate": "route competition separate",
        "campaign": "route campaign consent",
    }
    for label, state in review_route_branches.items():
        block = label_block(review, label)
        if f'has "{PREFIX} {state}"' not in block:
            fail(f"Review {label} branch missing its route gate")
    if 'branch paired' in review:
        fail("paired route should remain the deliberate Review fallthrough")
    if "paired records survived the next event" not in review.lower():
        fail("paired Review fallthrough is missing its distinct consequence")

    settlements = {
        "packet": "settlement portable context",
        "renewal": "settlement fresh context",
    }
    for label, state in settlements.items():
        block = label_block(review, label)
        if block.count(f'"{PREFIX} reviewed" = 1') != 1:
            fail(f"{label} must close Review exactly once")
        if block.count(f'"{PREFIX} {state}" = 1') != 1:
            fail(f"{label} missing own settlement state")
        if len(re.findall(r'^\s*decline\s*$', block, re.M)) != 1:
            fail(f"{label} must terminate exactly once")
        for other in set(settlements.values()) - {state}:
            if f'"{PREFIX} {other}" = 1' in block:
                fail(f"{label} writes another settlement")

    after = mission_block(text, f"{PREFIX} Seli Remembers")
    if f'not "{PREFIX} aftermath seen"' not in after:
        fail("aftermath must be one-shot")
    for state in settlements.values():
        if f'has "{PREFIX} {state}"' not in after:
            fail(f"aftermath missing settlement gate {state}")
    if len(re.findall(r'^\s*or\s*$', after, re.M)) != 1:
        fail("aftermath must use one two-settlement OR gate")
    renewal_after = label_block(after, "renewal")
    if f'has "{PREFIX} settlement fresh context"' not in renewal_after:
        fail("aftermath renewal branch missing fresh-context settlement gate")
    if after.count(f'"{PREFIX} aftermath seen" = 1') != 1:
        fail("aftermath write count invalid")
    if len(re.findall(r'^\s*decline\s*$', after, re.M)) != 1:
        fail("aftermath must terminate exactly once")

    labels = set(re.findall(r'^\s*label\s+([A-Za-z0-9_-]+)\s*$', text, re.M))
    gotos = re.findall(r'^\s*goto\s+([A-Za-z0-9_-]+)\s*$', text, re.M)
    missing = sorted({target for target in gotos if target not in labels})
    if missing:
        fail(f"missing goto labels: {missing}")

    concepts = (
        "friendship",
        "competition",
        "result",
        "quotation",
        "promotional",
        "approval",
        "expiry",
        "fresh evidence",
        "historical",
    )
    for concept in concepts:
        if concept not in lower:
            fail(f"missing continuity concept: {concept}")

    forbidden_claims = (
        "coalition law requires",
        "all coalition athletes must",
        "games law requires",
        "competition proves hostility",
        "old quotation proves current hostility",
    )
    for claim in forbidden_claims:
        if claim in lower:
            fail(f"unsupported centralized/current claim: {claim}")

    print("PASS: B2 Coalition Games Rivalry Compact validated")
    print("PASS: missions=3, routes=3+refusal, settlements=2, aftermath=one-shot")
    print("PASS: route-local lifecycle and Review/aftermath branch gates verified")
    print("PASS: lifecycle=7 declines, 0 accepts")
    print("PASS: ownership=B2 namespace only; Heliarch recognition read-only")


if __name__ == "__main__":
    main()
