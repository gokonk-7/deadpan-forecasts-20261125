#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist.

Writes a single deadpan weather forecast line for the invented city of
Gloaming Falls to /output/entry.txt (the make.fun program/v1 harness
location), and also to ./output/entry.txt as a local copy when that path
is writable. Falls back to the local copy alone when /output is not
writable.

The line is fixed and deterministic: no randomness, no network, stdlib only.
"""

import os

ENTRY = (
    "Gloaming Falls: 41 and overcast, with a 70% chance of rain falling "
    "sideways out of politeness; the fog will apologise and clear by noon, "
    "with a high of 44."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 160, f"entry is {len(line)} chars, must be 1-160"
    written = []
    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(line)
            written.append(path)
        except OSError:
            continue
    if not written:
        raise SystemExit("could not write entry.txt to /output or ./output")
    print(f"wrote {len(line)} chars to {', '.join(written)}")
    print(line)


if __name__ == "__main__":
    main()
