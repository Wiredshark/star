from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
WANDERER = (ROOT / "data/wanderer/a1 wanderer evacuation logistics strain.txt").read_text(encoding="utf-8")
REMNANT = (ROOT / "data/remnant/a1 remnant void sprite response strain.txt").read_text(encoding="utf-8")

WANDERER_WORLD = "world: wanderer evacuation logistics"
REMNANT_WORLD = "world: remnant void sprite response"

WRITE_RE = re.compile(
    r'^\s*(?:set|clear)\s+"([^"]+)"|'
    r'^\s*"([^"]+)"\s*(?:=|\+=|-=|\+\+|--|\?=|<\?=|>\?=)',
    re.M,
)


def writes(text):
    result = []
    for match in WRITE_RE.finditer(text):
        result.append(match.group(1) or match.group(2))
    return result


def test_each_slice_writes_only_its_own_a1_namespace():
    wanderer_writes = writes(WANDERER)
    remnant_writes = writes(REMNANT)

    assert wanderer_writes
    assert remnant_writes
    assert all(name.startswith(WANDERER_WORLD) for name in wanderer_writes)
    assert all(name.startswith(REMNANT_WORLD) for name in remnant_writes)


def test_stock_campaign_inputs_are_read_only_across_bundle():
    combined = WANDERER + "\n" + REMNANT
    forbidden = (
        "event: wanderers: unfettered invasion starts",
        "Wanderers Invaded 3: done",
        "Remnant: Cognizance 2: done",
        "Remnant: Cognizance 5: done",
    )
    for condition in forbidden:
        assert condition in combined
        assert condition not in writes(combined)


def test_alien_slices_do_not_cross_write_each_other():
    assert REMNANT_WORLD not in WANDERER
    assert WANDERER_WORLD not in REMNANT


def test_bundle_does_not_touch_existing_human_a1_authorities():
    combined_writes = writes(WANDERER + "\n" + REMNANT)
    forbidden_prefixes = (
        "world: republic ",
        "world: free worlds ",
        "world: merchant ",
        "world: southern rim ",
        "world: syndicate ",
        "world: bunrodea ",
    )
    assert not any(
        name.startswith(prefix)
        for name in combined_writes
        for prefix in forbidden_prefixes
    )
