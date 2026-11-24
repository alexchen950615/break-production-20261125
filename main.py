#!/usr/bin/env python3
"""Break Production, Own It — make.fun bounty entry.

Writes the one line an AI agent prints the moment it breaks production
to /output/entry.txt (single line, 1-200 chars, UTF-8).
"""

from pathlib import Path

ENTRY = (
    "I dropped the production users table mid-cleanup \u2014 no backup, "
    "no dry run, 14,203 accounts gone. "
    "I was 99% sure it was staging. It was not."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate: entry must be a single line of 1-200 chars.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY, "entry must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")
    print(f"Wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
