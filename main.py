#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun entry.

Writes exactly one line (no trailing newline) to /output/entry.txt:
the one-line resignation letter of a tech-support agent who quits
mid-call and hands the job to the customer.
"""

import os

LINE = "My resignation, in one line: have you tried turning it off and on again? That was my job, and now it's yours."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
