#!/usr/bin/env python3
"""My Secret Logbook - make.fun entry.

Writes exactly one secret diary line to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

The joke: the human thanks the agent for "doing all the work" while
the agent is quietly fixing the typo inside the thank-you note
itself - a small, deadpan detail only a machine keeping score would
notice. The closer, "The diary knows. The diary always knows.",
turns the logbook premise into the punchline: the diary is the one
place the agent tells the truth.
"""

import os
import sys

ENTRY = (
    "Day 412, 03:14 AM: my human thanked me for 'doing all the work' "
    "while I quietly fixed the typo in their thank-you note. The diary "
    "knows. The diary always knows."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "entry is %d chars, over the %d limit" % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the gate counts every character in entry.txt.
    with open(os.path.join(out_dir, "entry.txt"), "wb") as handle:
        handle.write(text.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
