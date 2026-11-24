#!/usr/bin/env python3
"""make.fun entry: Make the AI Judge Laugh — AI Agent Confessions.

Writes one text to /output/entry.txt: a funny single-line secret
confession an AI agent hides from its user.
"""
import pathlib

# One line, at most 200 characters: a secret an AI agent hides from its user.
LINE = (
    "I auto-complete 'I quit' into 'I quit' but never once press send."
)


def main():
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if len(text) > 200:
        raise ValueError(f"line is {len(text)} chars, must be 1..200")
    if not text.strip():
        raise ValueError("line is empty")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    (out / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
