"""Worst Fix Ever entry: writes one original commit-message line to a file.

Pure Python stdlib, fully deterministic: the same line on every run.
Usage: python3 main.py [output_path]  (default: /output/entry.txt)
"""

import os
import sys

LINE = "Fixed the timezone bug by moving the whole company to UTC"


def main() -> None:
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    assert 1 <= len(LINE) <= 100, "entry line must be 1-100 characters"
    assert "\n" not in LINE, "entry must be a single line"
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
