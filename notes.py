"""A tiny command-line notes tool.

Usage:
    python notes.py add "Buy milk"
    python notes.py list
    python notes.py remove 1

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


def _read_notes() -> list:
    """Return the list of notes currently stored, or an empty list."""
    if not NOTES_FILE.exists():
        return []
    with NOTES_FILE.open("r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f if line.strip()]


def list_notes() -> None:
    """Print all saved notes, numbered."""
    lines = _read_notes()
    if not lines:
        print("No notes yet.")
        return
    for i, note in enumerate(lines, start=1):
        print(f"{i}. {note}")


def remove_note(index: int) -> None:
    """Remove a note by its 1-based position in the list."""
    lines = _read_notes()
    if index < 1 or index > len(lines):
        print(f"No note at position {index}.")
        return
    removed = lines.pop(index - 1)
    with NOTES_FILE.open("w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    print(f"Removed note: {removed}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python notes.py [add \"text\"|list|remove N]")
        return

    command = sys.argv[1]
    if command == "add" and len(sys.argv) > 2:
        add_note(" ".join(sys.argv[2:]))
    elif command == "list":
        list_notes()
    elif command == "remove" and len(sys.argv) > 2 and sys.argv[2].isdigit():
        remove_note(int(sys.argv[2]))
    else:
        print("Usage: python notes.py [add \"text\"|list|remove N]")


if __name__ == "__main__":
    main()
