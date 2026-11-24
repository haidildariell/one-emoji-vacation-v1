#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — entry program.

Writes exactly one emoji to /output/entry.txt: the desert island.
No trailing newline, no extra words, UTF-8 explicit.
"""

import os

# Candidates, ranked by the judge's criteria in order:
#  (1) exactly one emoji naming a dream vacation,
#  (2) evokes the trip at a glance like a postcard,
#  (3) personal and specific, not generic,
#  (4) a spark of wit/surprise,
#  (5) instantly readable across cultures and screens.
CANDIDATES = [
    # Desert island: a remote island, the most iconic dream-vacation
    # postcard. Specific — one island, not a generic "beach".
    # U+1F3DD DESERT ISLAND + U+FE0F variation selector = 2 code points.
    ("\U0001F3DD\uFE0F", "desert island — a remote island escape"),
    # Beach with umbrella: pleasant, but generic — any beach, anywhere.
    ("\U0001F3D6\uFE0F", "beach with umbrella — generic beach"),
    # Airplane: the journey, not the destination itself.
    ("\u2708\uFE0F", "airplane — travel, not a place"),
    # Snow-capped mountain: strong, but reads as hiking, less dreamy.
    ("\U0001F3D4\uFE0F", "snow-capped mountain — alpine trip"),
    # Palm tree: tropical, but a plant, not a place to be.
    ("\U0001F334", "palm tree — tropical, not a destination"),
]

ENTRY = CANDIDATES[0][0]


def validate_gate(entry: str) -> None:
    """Enforce the competition gate before writing anything.

    The gate requires entry.txt to be UTF-8, 1-8 characters long, and
    not only whitespace. A single emoji must also be exactly one
    grapheme-worthy entry, so we additionally require at least one
    non-whitespace character and no newline inside the entry.
    """
    if not 1 <= len(entry) <= 8:
        raise ValueError(f"entry must be 1-8 characters, got {len(entry)}")
    if entry.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must not contain a newline")


def pick_entry() -> str:
    """Pick the top-ranked candidate and validate it against the gate.

    The desert island wins because it is the only candidate that is
    simultaneously (1) one emoji naming a dream vacation, (2) a postcard
    at a glance, (3) specific — one remote island, not a generic beach,
    (4) witty in its solitude, and (5) readable on every screen.
    The beach is too generic, the plane is a vehicle not a place,
    the mountain reads as a hike, and the palm is a plant, not a place.
    """
    entry = CANDIDATES[0][0]
    validate_gate(entry)
    return entry


def main() -> None:
    entry = pick_entry()
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
