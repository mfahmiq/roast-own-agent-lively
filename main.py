#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes the single-line roast to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os

ENTRY = "My agent finishes my sentences, my code, and my confidence — all wrong."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
