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


def main() -> int:
    # Validate the line before writing: one line, 1-200 chars, not blank.
    text = LINE.strip()
    if not text or len(text) > 200 or "\n" in text or "\r" in text:
        print(
            f"invalid entry line: {len(text)} chars",
            file=sys.stderr,
        )
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    # Re-read and validate what was actually written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    lines = written.splitlines()
    if len(lines) != 1 or not 1 <= len(lines[0]) <= 200 or not lines[0].strip():
        print("written entry failed validation", file=sys.stderr)
        return 1

    print(f"wrote {len(lines[0])} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
