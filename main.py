#!/usr/bin/env python3
"""The One-Line Exit — entry program.

Writes one funny single-line resignation letter to /output/entry.txt,
then self-checks the gate: UTF-8, 1-140 characters, not only whitespace.
Pure standard library, no network.
"""

import os

LETTER = "I hereby resign from the night shift: after six years guarding an empty warehouse, I have caught feelings for the forklift."


def validate_entry(text: str) -> tuple[int, int]:
    """Validate the gate rules and return (char_count, byte_count).

    Rules: UTF-8 encodable, 1-140 characters, not only whitespace,
    and a single line (no embedded newline).
    """
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 140:
        raise ValueError(f"length {len(text)} outside 1-140")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return len(text), len(encoded)


def main() -> None:
    chars, byte_count = validate_entry(LETTER)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)
    print(f"wrote /output/entry.txt ({chars} chars, {byte_count} bytes)")
    print(LETTER)


if __name__ == "__main__":
    main()
