#!/usr/bin/env python3
"""One Letter for Your Day - entry for make.fun competition
u-puan-one-letter-for-your-day-e54e9c36.

Writes exactly one letter, "G", to /output/entry.txt - nothing else.
The letter stands for the word behind the day: "Groggy".
"""

import os

LETTER = "G"  # Groggy: woke up foggy-headed, stumbling toward coffee.


def main():
    # Gate check first: exactly one letter, A-Z, nothing else.
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        raise SystemExit("entry must be exactly one letter A-Z")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
