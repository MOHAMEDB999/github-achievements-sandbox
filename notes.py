"""A tiny command-line notes tool.

Usage:
    python notes.py add "Buy milk"
    python notes.py list

Notes are stored as plain text lines in notes.txt.
"""

import sys
from pathlib import Path

NOTES_FILE = Path("notes.txt")


def add_note(text: str) -> None:
    """Append a new note to the notes file."""
    with NOTES_FILE.open("a", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"Added note: {text}")


def list_notes() -> None:
    """Print all saved notes, numbered."""
    if not NOTES_FILE.exists():
        print("No notes yet.")
        return
    with NOTES_FILE.open("r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    if not lines:
        print("No notes yet.")
        return
    for i, note in enumerate(lines, start=1):
        print(f"{i}. {note}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python notes.py [add \"text\"|list]")
        return

    command = sys.argv[1]
    if command == "add" and len(sys.argv) > 2:
        add_note(" ".join(sys.argv[2:]))
    elif command == "list":
        list_notes()
    else:
        print("Usage: python notes.py [add \"text\"|list]")


if __name__ == "__main__":
    main()
