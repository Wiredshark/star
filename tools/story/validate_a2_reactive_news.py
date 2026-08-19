#!/usr/bin/env python3
"""Focused structural validation for the A2 reactive-news production slice.

This intentionally does not replace Endless Sky's parser/runtime tests. It checks
that the A2-owned dynamic-narrative contract uses stock News conditions to read
existing authoritative persistent state and does not introduce shadow state.
"""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "human" / "a2 reactive news.txt"

NEWS_ITEMS = (
    'news "A2 Deep convoy veteran"',
    'news "A2 Deep convoy command veteran"',
    'news "A2 experienced Republic captain"',
)


def require(text: str, needle: str, failures: list[str], message: str) -> None:
    if needle not in text:
        failures.append(message)


def block(text: str, marker: str, next_marker: str | None = None) -> str:
    tail = text.split(marker, 1)[-1]
    if next_marker and next_marker in tail:
        tail = tail.split(next_marker, 1)[0]
    return tail


def main() -> int:
    failures: list[str] = []

    if not DATA.is_file():
        print(f"FAIL: missing {DATA.relative_to(ROOT)}")
        return 1

    text = DATA.read_text(encoding="utf-8")

    for item in NEWS_ITEMS:
        require(text, item, failures, f"missing production news item: {item}")

    require(text, 'has "Deep: Syndicate Convoy: done"', failures,
            "missing persistent Deep convoy history reader")
    require(text, '"combat rating" >= 5', failures,
            "missing authoritative combat-rating reader")

    convoy = block(text, NEWS_ITEMS[0], NEWS_ITEMS[1])
    require(convoy, "\tto show\n", failures,
            "Deep convoy news is not condition-gated")
    require(convoy, 'has "Deep: Syndicate Convoy: done"', failures,
            "Deep convoy news does not consume the persistent mission outcome")

    combined = block(text, NEWS_ITEMS[1], NEWS_ITEMS[2])
    require(combined, "\tto show\n", failures,
            "combined veteran news is not condition-gated")
    require(combined, 'has "Deep: Syndicate Convoy: done"', failures,
            "combined veteran news does not read Deep convoy history")
    require(combined, '"combat rating" >= 5', failures,
            "combined veteran news does not read combat rating")

    experienced = block(text, NEWS_ITEMS[2])
    require(experienced, "\tto show\n", failures,
            "experienced-captain news is not condition-gated")
    require(experienced, '"combat rating" >= 5', failures,
            "experienced-captain news does not read combat rating")

    # A2 must read existing authorities rather than writing a parallel news state.
    forbidden = (
        "on show",
        "action",
        "a2 reactive news: seen",
        "dialogue world state",
        "news memory database",
        "sqlite",
    )
    lower = text.lower()
    for token in forbidden:
        if token in lower:
            failures.append(f"forbidden shadow-state/effect marker present: {token}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: A2 reactive-news structure validated")
    print(f"PASS: news_items={len(NEWS_ITEMS)}")
    print("PASS: authoritative_inputs=Deep convoy completion, combat rating")
    print("PASS: combined_gate=mission history + combat experience")
    print("PASS: persistence_model=read-only stock News conditions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
