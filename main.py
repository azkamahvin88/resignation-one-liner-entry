#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun entry.

Writes exactly one line (no trailing newline) to /output/entry.txt:
the one-line resignation letter of a cron job that ran at 3 AM.
"""

import os

LINE = "I resign. I ran at 3 AM so you could sleep, and you thanked the dashboard. Goodbye."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
