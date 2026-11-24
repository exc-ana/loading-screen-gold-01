#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single fixed loading-screen tip to /output/entry.txt.
Deterministic: no randomness, no clock, no network, stdlib only.
"""

import os

TIP = (
    "Tip: commit before you refactor \u2014 your AI pair will cheerfully "
    "rewrite working code at 3 a.m. and call it an improvement. "
    "Future-you needs a rollback."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
