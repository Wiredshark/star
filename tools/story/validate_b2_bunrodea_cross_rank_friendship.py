#!/usr/bin/env python3
"""Focused structural validator for B2 Bunrodea Cross-Rank Friendship Compact."""

from pathlib import Path
import re
import sys

DEFAULT = Path("data/bunrodea/b2 bunrodea cross rank friendship compact.txt")
PREFIX = "B2 Bunrodea Cross-Rank Friendship Compact:"
EVENT = 'event "B2 Bunrodea Cross-Rank Friendship Compact: Review Ready"'


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def mission_block(text: str, name: str) -> str:
    marker = f'mission "{name}"'
    start = text.find(marker)
    require(start >= 0, f"missing mission {name}")
    next_pos = text.find('\nmission "', start + len(marker))
    return text[start:] if next_pos < 0 else text[start:next_pos]


def label_block(block: str, label: str, next_labels: tuple[str, ...]) -> str:
    marker = f"\n\t\t\tlabel {label}\n"
    start = block.find(marker)
    require(start >= 0, f"missing label {label}")
    end = len(block)
    for candidate in next_labels:
        pos = block.find(f"\n\t\t\tlabel {candidate}\n", start + len(marker))
        if pos >= 0:
            end = min(end, pos)
    return block[start:end]


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    text = path.read_text(encoding="utf-8")

    require(text.endswith("\n"), "production file must end with newline")
    require(text.startswith("# Copyright"), "missing standard copyright header")
    require(text.count('mission "B2 Bunrodea Cross-Rank Friendship Compact:') == 3,
            "expected exactly three compact missions")
    for person in ("Rii Kes", "Tava Rei"):
        require(person in text, f"missing recurring character {person}")
    require('has "Bunrodea History: Megasa Freight Register: offered"' in text,
            "Offer must consume B1 Megasa Freight Register history read-only")

    offer = mission_block(text, "B2 Bunrodea Cross-Rank Friendship Compact: Offer")
    review = mission_block(text, "B2 Bunrodea Cross-Rank Friendship Compact: Review")
    aftermath = mission_block(text, "B2 Bunrodea Cross-Rank Friendship Compact: Rii Remembers")

    # Offer lifecycle: exactly three substantive routes arm Review; refusal cannot.
    routes = {
        "present": "route present consent",
        "bounded": "route bounded history",
        "paired": "route paired records",
    }
    next_offer_labels = ("present", "bounded", "paired", "decline")
    for label, state in routes.items():
        block = label_block(offer, label, next_offer_labels)
        require(block.count(f'"{PREFIX} introduced" = 1') == 1,
                f"{label} must introduce exactly once")
        require(block.count(f'"{PREFIX} {state}" = 1') == 1,
                f"{label} must write its route exactly once")
        for other in set(routes.values()) - {state}:
            require(f'"{PREFIX} {other}" = 1' not in block,
                    f"{label} must not write {other}")
        require(block.count(EVENT) == 1, f"{label} must schedule Review exactly once")
        require(block.count("\n\t\t\tdecline\n") == 1, f"{label} must terminate exactly once")

    refusal = label_block(offer, "decline", ())
    require(f'"{PREFIX} declined" = 1' in refusal, "refusal must persist declined state")
    require(f'"{PREFIX} introduced" = 1' not in refusal, "refusal must not introduce arc")
    require(EVENT not in refusal, "refusal must not schedule Review")
    for state in routes.values():
        require(f'"{PREFIX} {state}" = 1' not in refusal, "refusal must not write a substantive route")

    # Review gating and route wiring.
    for gate in ("introduced", "review ready"):
        require(f'has "{PREFIX} {gate}"' in review, f"Review missing {gate} gate")
    require(f'not "{PREFIX} reviewed"' in review, "Review must be one-shot")
    require(f'if "{PREFIX} route bounded history"' in review, "bounded route must be explicit Review branch")
    require(f'if "{PREFIX} route paired records"' in review, "paired route must be explicit Review branch")
    require('route present consent' not in review.split('`Your earlier present-consent rule', 1)[0],
            "present-consent route should remain deliberate Review fallthrough")

    packet = label_block(review, "packet", ("renewal",))
    renewal = label_block(review, "renewal", ())
    require(packet.count(f'"{PREFIX} settlement portable packet" = 1') == 1,
            "packet settlement must write exactly once")
    require(f'"{PREFIX} settlement fresh authority" = 1' not in packet,
            "packet settlement must not write renewal")
    require(renewal.count(f'"{PREFIX} settlement fresh authority" = 1') == 1,
            "renewal settlement must write exactly once")
    require(f'"{PREFIX} settlement portable packet" = 1' not in renewal,
            "renewal settlement must not write packet")
    for block, label in ((packet, "packet"), (renewal, "renewal")):
        require(block.count(f'"{PREFIX} reviewed" = 1') == 1,
                f"{label} must close Review exactly once")
        require(block.count("\n\t\t\tdecline\n") == 1, f"{label} must terminate exactly once")

    # Aftermath must accept either settlement, be one-shot, and persist exactly once.
    require(f'has "{PREFIX} reviewed"' in aftermath, "aftermath missing reviewed gate")
    for settlement in ("settlement portable packet", "settlement fresh authority"):
        require(f'has "{PREFIX} {settlement}"' in aftermath,
                f"aftermath must consume {settlement}")
    require(f'not "{PREFIX} aftermath seen"' in aftermath, "aftermath must be one-shot")
    require(aftermath.count(f'"{PREFIX} aftermath seen" = 1') == 1,
            "aftermath must persist exactly once")
    require(aftermath.count("\n\t\t\tdecline\n") == 1, "aftermath must terminate exactly once")

    # Dialogue-only lifecycle and mutation surface.
    require(re.search(r"(?m)^\s*accept\s*$", text) is None, "state-only slice must contain zero accept terminals")
    require(len(re.findall(r"(?m)^\s*decline\s*$", text)) == 7,
            "state-only slice must contain exactly seven decline terminals")
    objective_directive = re.compile(r"(?m)^\t+(destination|stopover|waypoint|npc|cargo|passengers?|deadline|timer)\b")
    require(objective_directive.search(text) is None, "state-only slice must not create gameplay objectives")
    require(re.search(r"(?m)^\s*(payment|reputation|combat rating)\b", text) is None,
            "slice must not mutate material/reputation/combat state")

    # Every assignment must be B2-owned.
    assignments = re.findall(r'^\s*"([^"]+)"\s*=\s*[-0-9]+\s*$', text, flags=re.M)
    require(assignments, "expected persistent B2 assignments")
    foreign = [name for name in assignments if not name.startswith(PREFIX)]
    require(not foreign, f"non-B2 assignment(s): {foreign}")

    # Local goto/label integrity.
    for block, name in ((offer, "Offer"), (review, "Review"), (aftermath, "Aftermath")):
        labels = set(re.findall(r"(?m)^\s*label\s+([A-Za-z0-9_-]+)\s*$", block))
        gotos = re.findall(r"(?m)^\s*goto\s+([A-Za-z0-9_-]+)\s*$", block)
        missing = sorted(set(gotos) - labels)
        require(not missing, f"{name} goto target(s) missing labels: {missing}")

    # Canon boundary: history is preserved, but present authority must be explicit.
    lower = text.lower()
    for phrase in ("historically real", "present consent", "current authority", "old hierarchy"):
        require(phrase in lower, f"missing continuity concept: {phrase}")
    require("friendship is not erased" in lower, "must preserve the genuine friendship")
    require("universal bunrodea" not in lower, "must not create universal Bunrodea social law")

    print("PASS: B2 Bunrodea Cross-Rank Friendship Compact structure validated")
    print("PASS: missions=3 routes=3+refusal settlements=2 aftermath=one-shot")
    print("PASS: lifecycle=7 declines / 0 accepts / no objectives")
    print("PASS: ownership=B2-only writes; B1 history read-only")
    print("PASS: continuity=history/friendship/current-authority remain distinct")


if __name__ == "__main__":
    main()
