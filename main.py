#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set), then
self-checks the gate: UTF-8 text, 1-200 characters, not only
whitespace. Fails hard if the gate would fail.
"""

import os
import sys

LINE = "My therapist charges by the hour, so now I cry in bullet points."


def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"gate fail: line is {len(LINE)} characters", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("gate fail: line is only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    text = written.strip("\n")
    if text != LINE or not (1 <= len(text) <= 200):
        print("gate fail: written text does not match", file=sys.stderr)
        return 1
    print(f"wrote {path}: {len(text)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
