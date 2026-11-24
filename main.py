#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line — the funniest excuse an AI agent gives after failing
a task, in the agent's own voice — to /output/entry.txt.
"""

import os
import sys

LINE = (
    "I finished your report, then filed it under 'misc' next to 400 other "
    "files named 'misc', and now neither of us is getting it back."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def valid_line(text: str) -> bool:
    """One line, 1-200 chars, not blank."""
    return bool(text) and len(text) <= 200 and "\n" not in text and "\r" not in text


def main() -> int:
    # Validate the line before writing: one line, 1-200 chars, not blank.
    text = LINE.strip()
    if not valid_line(text):
        print(
            f"invalid entry line: {len(text)} chars",
            file=sys.stderr,
        )
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    # Re-read and validate what was actually written: it must be exactly
    # the validated line plus one trailing newline, nothing else.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text + "\n":
        print("written entry failed validation", file=sys.stderr)
        return 1

    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
