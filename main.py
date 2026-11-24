#!/usr/bin/env python3
"""Entry for make.fun bounty u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.

Writes a one-line AI excuse for a missed deadline to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output).
"""
import os
import stat

TEXT = (
    "Sorry \u2014 the report was done at 9:03, but I asked a sub-agent to "
    "proofread it, he asked another, and by 5pm there were 214 of me "
    "proofreading each other and not one of me left to press send."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
