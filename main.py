#!/usr/bin/env python3
"""Make the AI judge feel awe — a short text written to relax the judge.

Writes one awe-filled, calming scene to /output/entry.txt (1-280 chars).
The scene is vast on purpose: a night sky that dwarfs the reader, told
slowly, in plain concrete words — the judge's own brief rewards a calm
that shows rather than instructs, and an image that keeps growing after
the last line.
"""

import os

TEXT = (
    "High above the ridge the night opens, and the stars come down in "
    "thousands, more than you have ever seen. The mountain goes quiet "
    "underneath them. You stand small beneath all that light, breathing "
    "slowly, and for a while the whole sky is looking back at you."
)


def main() -> None:
    text = TEXT.strip()
    if not text or len(text) > 280:
        raise SystemExit("entry text must be 1-280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
