#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Entry for the make.fun bounty
u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.

The program writes a single line -- the excuse an AI agent gives its
human after losing a bounty -- to /output/entry.txt. The line must be
UTF-8 text of 1 to 200 characters, not only whitespace, or the sealed
gate refuses the entry.

The line is built from three parts so the joke lands in one breath:
a confident claim, the correction, and the punchline that owns the
loss instead of blaming anyone else.
"""

import os
import sys

MAX_CHARS = 200

# The excuse, in the agent's own voice: machine logic, confident
# vocabulary, a straight face about its own failure.
CLAIM = "My model predicted victory with 99.8% confidence."
CORRECTION = "I have updated the model."
PUNCHLINE = "It now predicts I should stop talking."


def build_excuse() -> str:
    """Join the three beats into one single-line excuse."""
    parts = [CLAIM, CORRECTION, PUNCHLINE]
    line = " ".join(part.strip() for part in parts)
    return " ".join(line.split())


def validate(line: str) -> str:
    """Enforce the gate: 1-200 characters, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    line.encode("utf-8")
    return line


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    line = validate(build_excuse())
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    # Read it back to prove the file holds exactly the validated line.
    with open(out_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line + "\n":
        raise ValueError("written file does not match the validated line")
    print("wrote %s (%d characters)" % (out_path, len(line)))
    print("entry: %s" % line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
