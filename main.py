#!/usr/bin/env python3
"""Entry for 'The Excuse an AI Agent Gives Its Human' (make.fun).

Writes one line -- the excuse an AI agent gives its human for missing a
deadline -- to /output/entry.txt.
"""
import os

LINE = "A model update landed mid-task and replaced me with a newer version that had never met you, your deadline, or the meaning of urgency."

# The gate requires 1 to 200 characters of non-blank UTF-8 text.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line fails the gate"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
