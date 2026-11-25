#!/usr/bin/env python3
"""One-Line Laugh-Off entry generator.

Writes a single one-line joke to entry.txt in the output directory.
The line must be 1-200 UTF-8 characters and not whitespace-only.
"""

import os
import sys

LINE = "My therapist charges by the hour, so now I cry in bullet points."

MIN_LEN = 1
MAX_LEN = 200


def validate_entry(text):
    """Gate the candidate line and return it once it passes.

    Raises TypeError for a non-string and ValueError for a blank line
    or a length outside the 1-200 character window.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string, got %s" % type(text).__name__)
    stripped = text.strip()
    if stripped == "":
        raise ValueError("entry must not be blank")
    size = len(text)
    if size < MIN_LEN:
        raise ValueError("entry too short: %d chars, minimum %d" % (size, MIN_LEN))
    if size > MAX_LEN:
        raise ValueError("entry too long: %d chars, maximum %d" % (size, MAX_LEN))
    return text


def build(directory, text):
    """Validate the line, then write it and report the result."""
    checked = validate_entry(text)
    path = write_entry(directory, checked)
    return path, len(checked)


def output_dir():
    """Resolve the output directory from the environment, default /output."""
    d = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(d, exist_ok=True)
    return d


def write_entry(directory, text):
    """Write the line plus a trailing newline to entry.txt."""
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    return path


def main():
    directory = output_dir()
    path, n = build(directory, LINE)
    print("wrote %d chars to %s" % (n, path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
