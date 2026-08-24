#!/usr/bin/env python3
from pathlib import Path
import re
import sys

PATH = Path("data/incipias/a2 incipias license practice news.txt")
PREFIX = "A2 Incipias license practice "
EXPECTED = {
    "portable pilot": "B2 Incipias License Compact: settlement portable endorsement",
    "portable registrar": "B2 Incipias License Compact: settlement portable endorsement",
    "tiered pilot": "B2 Incipias License Compact: settlement tiered renewal",
    "tiered registrar": "B2 Incipias License Compact: settlement tiered renewal",
}
AFTERMATH = "B2 Incipias License Compact: aftermath seen"


def news_blocks(text: str):
    matches = list(re.finditer(r'^news "([^"]+)"\s*$', text, flags=re.MULTILINE))
    blocks = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks[match.group(1)] = text[start:end]
    return blocks


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else PATH
    text = path.read_text(encoding="utf-8")
    errors = []
    blocks = news_blocks(text)

    expected_names = {PREFIX + suffix for suffix in EXPECTED}
    actual_names = {name for name in blocks if name.startswith(PREFIX)}
    if actual_names != expected_names:
        errors.append(
            "expected exactly four named Incipias license-practice News groups: "
            + ", ".join(sorted(expected_names))
        )

    if len(blocks) != 4:
        errors.append(f"expected exactly four total News groups, found {len(blocks)}")

    for suffix, settlement in EXPECTED.items():
        name = PREFIX + suffix
        block = blocks.get(name)
        if block is None:
            continue
        if block.count(f'has "{AFTERMATH}"') != 1:
            errors.append(f"{name}: must require aftermath seen exactly once")
        if block.count(f'has "{settlement}"') != 1:
            errors.append(f"{name}: must require its terminal B2 settlement exactly once")
        other = (
            "B2 Incipias License Compact: settlement tiered renewal"
            if "portable" in settlement
            else "B2 Incipias License Compact: settlement portable endorsement"
        )
        if f'has "{other}"' in block:
            errors.append(f"{name}: must not cross-gate on the other settlement")
        if block.count('government "Conlatio"') != 1:
            errors.append(f"{name}: must remain scoped to Conlatio ports")
        if "\n\tname\n" not in block or "\n\tmessage\n" not in block:
            errors.append(f"{name}: must contain both name and message payloads")

    forbidden_patterns = {
        "action directive": r"(?m)^\s*action\s*$",
        "mission declaration": r"(?m)^mission\s+\"",
        "world-state reference": r'"world:',
        "declined route reference": r'B2 Incipias License Compact: declined',
        "refusal route reference": r'B2 Incipias License Compact: refusal',
        "B2 assignment": r'(?m)^\s*"B2 Incipias License Compact:[^"]+"\s*[+\-*/]?=',
        "A2 assignment": r'(?m)^\s*"A2 [^"]+"\s*[+\-*/]?=',
    }
    for label, pattern in forbidden_patterns.items():
        if re.search(pattern, text):
            errors.append(f"forbidden {label}")

    if text.count(f'has "{AFTERMATH}"') != 4:
        errors.append("aftermath gate must appear exactly four times")
    if text.count('has "B2 Incipias License Compact: settlement portable endorsement"') != 2:
        errors.append("portable settlement must gate exactly two News groups")
    if text.count('has "B2 Incipias License Compact: settlement tiered renewal"') != 2:
        errors.append("tiered settlement must gate exactly two News groups")

    if errors:
        print("FAIL")
        for error in errors:
            print("-", error)
        return 1

    print("PASS")
    print("news_groups=4")
    print("portable_groups=2")
    print("tiered_groups=2")
    print("state_writes=none")
    print("world_state_use=none")
    print("declined_or_refusal_publicized=no")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
