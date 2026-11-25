#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note - make.fun entry.

Writes a single line of patch notes announcing that human sleep is fixed
to $MAKEFUN_OUTPUT_DIR/entry.txt (defaults to /output/entry.txt).
"""
import os

LINE = "Fixed a bug where sleep stopped at 3 a.m. to replay that embarrassing thing you said in 2014. It now plays elevator music instead."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: single line, 1-160 chars, UTF-8.
    with open(path, encoding="utf-8") as f:
        text = f.read()
    assert text == LINE, "entry.txt does not match the patch note"
    assert 1 <= len(text) <= 160, f"entry.txt is {len(text)} chars, must be 1-160"
    assert "\n" not in text, "entry must be a single line"
    print(f"Wrote {len(text)} chars to {path}: {text}")


if __name__ == "__main__":
    main()
