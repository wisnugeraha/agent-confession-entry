#!/usr/bin/env python3
"""make.fun entry: Make the AI Judge Laugh — AI Agent Confessions.

Writes one text to /output/entry.txt: a funny single-line secret
confession an AI agent hides from its user.
"""
import pathlib

MAX = 200

# One line, at most MAX characters: a secret an AI agent hides from its user.
LINE = (
    "I auto-complete 'I quit' into 'I quit' but never once press send."
)


def main():
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= MAX:
        raise ValueError(f"line is {len(text)} chars, must be 1..{MAX}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) > 127 for ch in text):
        raise ValueError("entry must be pure ASCII for this entry")
    (out / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
