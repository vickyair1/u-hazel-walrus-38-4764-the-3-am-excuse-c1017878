#!/usr/bin/env python3
"""Write the 3 AM excuse entry to /output/entry.txt."""

import os

LINE = "My keys clocked out at midnight. It's 3 AM \u2014 come back when the sun's up and your judgment is too."

def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)  # exactly one line, no trailing newline

if __name__ == "__main__":
    main()
