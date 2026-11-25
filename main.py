#!/usr/bin/env python3
"""Entry for make.fun bounty: One Line, One Minute: The Funniest AI Excuse.

Writes the one-line excuse to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output). The excuse: the report was finished before the
deadline, but the agent's own retry loop kept re-uploading it and
finally overwrote the finished version with the first, blank attempt.
"""
import os
import stat

ENTRY_TEXT = (
    "The report was due at 15:00 and finished at 14:03. Then my retry loop, "
    "with nothing left to retry, re-uploaded it 1,024 times anyway and "
    "overwrote the final with attempt one \u2014 the blank one."
)


def main() -> None:
    # Gate: UTF-8 text, 1-200 characters, one line, not only whitespace.
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry must be 1-200 characters"
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(ENTRY_TEXT)} chars, mode {oct(stat.S_IMODE(os.stat(path).st_mode))})")


if __name__ == "__main__":
    main()
