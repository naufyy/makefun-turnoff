#!/usr/bin/env python3
"""make.fun entry: one funny line from a hopeless tech support agent.

Writes the entry text to /output/entry.txt (1-199 chars, UTF-8).
"""
import os

LINE = "Have you tried turning it off and on again? No rush \u2014 I'll just sit here listening to your deadline quietly leave the room."

def main():
    assert 1 <= len(LINE) <= 199, "entry must be 1-199 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
