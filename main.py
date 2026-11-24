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


def validate(text: str) -> None:
    """Raise ValueError unless text passes the gate: 1..MAX chars, non-blank,
    one line, UTF-8-encodable, and pure ASCII for this entry."""
    if not 1 <= len(text) <= MAX:
        raise ValueError(f"line is {len(text)} chars, must be 1..{MAX}")
    if not text.strip():
        raise ValueError("line is blank")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) > 127 for ch in text):
        raise ValueError("entry must be pure ASCII for this entry")


def emit(path: pathlib.Path, text: str) -> None:
    """Write text to path (UTF-8) and verify the on-disk bytes read back."""
    path.write_text(text, encoding="utf-8")
    confirm(path)


def confirm(path: pathlib.Path) -> str:
    """Re-read the file and confirm it satisfies the gate. Returns the text."""
    data = path.read_bytes()
    try:
        back = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{path} is not UTF-8: {exc}") from exc
    validate(back)
    if back != back.strip():
        raise ValueError("written file must not start/end with whitespace")
    return back


def main() -> None:
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    validate(text)
    entry = out / "entry.txt"
    emit(entry, text)
    back = confirm(entry)
    print(f"wrote {entry} ({len(back)} chars, gate ok)")


if __name__ == "__main__":
    main()
