#!/usr/bin/env python3
"""Validate the durable Endless Sky story-content repository contract."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
STORY = ROOT / "story"

REQUIRED_FILES = (
    "AGENT_CONTRACT.md",
    "NARRATIVE_DIVERSITY_POLICY.md",
    "WORLD_BIBLE.md",
    "RPG_CONTENT.md",
    "DYNAMIC_STORY_LIBRARY.md",
    "BUILDER_HANDOFF.md",
    "STORY_EVOLUTION_LOG.md",
    "README.md",
)

HANDOFF_HEADINGS = (
    "CONTENT ID",
    "TYPE",
    "NARRATIVE DOMAIN",
    "LOCATION",
    "CHARACTERS",
    "PREREQUISITES",
    "TRIGGER",
    "PREMISE",
    "PLAYER OPTIONS",
    "SUCCESS STATES",
    "FAILURE STATES",
    "WORLD CONSEQUENCES",
    "CHARACTER CONSEQUENCES",
    "FUTURE HOOKS",
    "IMPLEMENTATION DEPENDENCIES",
    "DIVERSITY_CHECK",
    "PRIORITY",
)

ROUND_HEADINGS = (
    "STORY ROUND",
    "SEED",
    "FOCUS",
    "WORLD CONTENT CREATED",
    "CHARACTERS",
    "FACTIONS",
    "RPG CONTENT",
    "DYNAMIC STORY CONTENT",
    "SIMULATION CONNECTIONS",
    "BUILDER HANDOFFS",
    "CONTINUITY NOTES",
    "IMPLEMENTATION DEPENDENCIES",
    "NEXT STORY PRESSURES",
)

SUBSTANTIAL_FILES = (
    "RPG_CONTENT.md",
    "DYNAMIC_STORY_LIBRARY.md",
)


def headings(text: str) -> set[str]:
    return {
        match.group(1).strip().upper()
        for match in re.finditer(r"^#{2,6}\s+(.+?)\s*$", text, flags=re.MULTILINE)
    }


def require_headings(path: Path, required: tuple[str, ...], errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    present = headings(text)
    missing = [heading for heading in required if heading.upper() not in present]
    if missing:
        errors.append(f"{path.relative_to(ROOT)} missing headings: {', '.join(missing)}")


def main() -> int:
    errors: list[str] = []

    if not STORY.is_dir():
        errors.append("story/ directory is missing")
    else:
        for name in REQUIRED_FILES:
            path = STORY / name
            if not path.is_file():
                errors.append(f"story/{name} is missing")
            elif not path.read_text(encoding="utf-8").strip():
                errors.append(f"story/{name} is empty")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    require_headings(STORY / "BUILDER_HANDOFF.md", HANDOFF_HEADINGS, errors)
    require_headings(STORY / "STORY_EVOLUTION_LOG.md", ROUND_HEADINGS, errors)

    log = (STORY / "STORY_EVOLUTION_LOG.md").read_text(encoding="utf-8")
    if not re.search(r"STORY_SEED=\d+", log):
        errors.append("story/STORY_EVOLUTION_LOG.md does not record a numeric STORY_SEED")
    if not re.search(r"^##\s+Story Round\s+\d+\s*$", log, flags=re.MULTILINE | re.IGNORECASE):
        errors.append("story/STORY_EVOLUTION_LOG.md does not contain a numbered story round")

    for name in SUBSTANTIAL_FILES:
        text = (STORY / name).read_text(encoding="utf-8").lower()
        required_phrases = (
            "required existing systems",
            "required future systems",
            "data that can be authored now",
            "engine support needed",
            "world-state inputs",
            "world-state outputs",
        )
        missing = [phrase for phrase in required_phrases if phrase not in text]
        if missing:
            errors.append(f"story/{name} missing implementation-readiness fields: {', '.join(missing)}")

    policy = (STORY / "NARRATIVE_DIVERSITY_POLICY.md").read_text(encoding="utf-8").lower()
    for phrase in (
        "anti-repetition rule",
        "systemic-input requirement",
        "consequence diversity",
        "diversity_check",
    ):
        if phrase not in policy:
            errors.append(f"story/NARRATIVE_DIVERSITY_POLICY.md missing policy marker: {phrase}")

    handoff = (STORY / "BUILDER_HANDOFF.md").read_text(encoding="utf-8")
    ids = sorted(set(re.findall(r"`(ES-STORY-\d{4,})`", handoff)))
    if not ids:
        errors.append("story/BUILDER_HANDOFF.md has no stable ES-STORY content ID")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: story repository contract validated")
    print(f"PASS: {len(REQUIRED_FILES)} required durable files present")
    print(f"PASS: builder handoff fields={len(HANDOFF_HEADINGS)}")
    print(f"PASS: round report fields={len(ROUND_HEADINGS)}")
    print(f"PASS: handoff ids={','.join(ids)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
