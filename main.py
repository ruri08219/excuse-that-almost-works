#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt.

Entry: one line a gamer texts the boss to skip work on GTA 6 launch
week. The gate wants /output/entry.txt as UTF-8 text, 1-140 characters,
not only whitespace; the brief caps the line at 20 words.
"""
import os
import sys

ENTRY = "Boss, the dentist moved my root canal to 9am, I'll be numb till lunch and useless after."

def main():
    words = ENTRY.split()
    if len(words) > 20:
        print(f"entry has {len(words)} words, over the 20-word cap", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 140:
        print(f"entry has {len(ENTRY)} characters, outside the 1-140 gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(words)} words, {len(ENTRY)} chars to {path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
