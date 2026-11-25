"""Unsent: The Micro-Confession Sprint — make.fun entry.

Writes the chosen entry (a To: line plus the unsent message itself,
exactly as typed, one line each) to MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = (
    "To: the woman in the flat below mine\n"
    "I still turn my music down at 9 p.m. even though you've been gone a year, "
    "because the night you banged on the ceiling I finally slept through till "
    "morning, and I've never told you that your anger was the only thing that "
    "ever made me feel watched over.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
