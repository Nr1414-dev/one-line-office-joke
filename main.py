#!/usr/bin/env python3
"""One-Line Office Joke: writes the chosen office joke to /output/entry.txt.

The joke below is a fixed text picked by the build session after scoring six
candidates against the judge brief (one-line office joke, max 200 chars).
The program validates it and writes it out byte-identically.
"""

import os

JOKE = "The thermostat belongs to whoever shouts loudest \u2014 HR now issues sweaters in July."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validated(text):
    line = text.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if len(line.encode("utf-8")) > 200:
        raise ValueError("entry must fit 200 bytes of UTF-8")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 and ch != "\t" for ch in line):
        raise ValueError("entry must not contain control characters")
    return line


def main():
    line = validated(JOKE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
