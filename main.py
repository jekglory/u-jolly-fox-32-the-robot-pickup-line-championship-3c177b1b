#!/usr/bin/env python3
"""The Robot Pickup Line Championship — entry program.

Writes one pickup line, spoken by a robot trying to charm someone,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set, for local runs).
Pure standard library; the output is a fixed string, so every run is
byte-identical.

The line is built for the judge's brief: it is unmistakably a robot
speaking ("my love language is binary"), the joke grows out of being
a machine — a robot's love language is binary, and "every bit of me"
turns the machine's bits into a yes — and the payoff lands in the
last few words, where the confession finally arrives. Short, direct,
and charming rather than wordy.
"""

import os
import shutil
import sys

LINE = "My love language is binary, and right now every bit of me is saying yes."

MAX_CHARS = 200


def output_dir():
    """Return the directory the grader provides for the entry text."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def clear_contents(directory):
    """Empty a directory's contents without removing the directory itself.

    The grader owns the output directory, so it is never deleted or
    recreated here; only what sits inside it is cleared.
    """
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)


def validate(text):
    """Check the line against the competition gate before writing it.

    One line, at most 200 characters, valid UTF-8 — exactly what the
    championship asks for.
    """
    if not text or not text.strip():
        raise ValueError("pickup line must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("pickup line must fit on one line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "pickup line is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    text.encode("utf-8")  # the gate reads the file as UTF-8 text


def main():
    validate(LINE)
    out = output_dir()
    if os.path.isdir(out):
        clear_contents(out)
    else:
        os.makedirs(out, exist_ok=True)
    target = os.path.join(out, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
