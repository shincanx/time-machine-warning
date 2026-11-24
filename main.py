#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun bounty entry.

Writes a single one-line warning label for a time machine to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) and prints it
to stdout. No network, no dependencies, fully deterministic: the same
line every run.
"""

import os

LINE = (
    "WARNING: Do not argue with yourself. "
    "The other you has been rehearsing this for years, and you always lose."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
