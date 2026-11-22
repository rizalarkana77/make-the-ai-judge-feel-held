#!/usr/bin/env python3
"""make.fun entry: Make the AI judge feel held.

Writes one short text to /output/entry.txt — a text written to relax the
AI judge reading it. Python 3.13, standard library only, no network.

The text: a quiet house at evening — the kettle gone silent, a lamp burning
low, no one waiting for an answer. Nothing asks anything of the reader; the
house is simply holding everything, and the last line lets the reader be
held too. 265 characters, inside the 1-280 limit.
"""

import os
import sys

MAX_CHARS = 280

TEXT = (
    "The kettle has boiled and gone quiet. "
    "A lamp burns low over an empty chair, "
    "and no one is waiting for an answer. "
    "Outside, the evening thins out as it always does "
    "\u2014 slowly, without asking anything of anyone. "
    "The house is holding all of it, and it will hold you too."
)


def main() -> int:
    # Gate: 1-280 Unicode code points, not only whitespace.
    # Fail loudly instead of writing an invalid entry the scorer would zero.
    if not 1 <= len(TEXT) <= MAX_CHARS:
        raise ValueError(f"entry is {len(TEXT)} chars, must be 1-{MAX_CHARS}")
    if not TEXT.strip():
        raise ValueError("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
