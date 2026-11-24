#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one line -- an alien tourist's review of planet Earth -- to
/output/entry.txt. Python standard library only, deterministic, no
network access, no files read from outside this repository.
"""

import os

ENTRY = (
    "Visited Earth for two days. The locals bag their pets' waste and "
    "carry it home like treasure, then complain the planet smells. "
    "2/5 stars, would not rebook."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
