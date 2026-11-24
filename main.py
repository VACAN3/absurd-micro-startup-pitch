#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one absurdly specific micro-startup pitch for lazy AI agents
to /output/entry.txt (one sentence, under 200 characters).
"""

import os

PITCH = (
    "A lazy AI agent that attends your morning standup as a looping video "
    "of you nodding, says 'sounds good' whenever it hears your name, and "
    "charges sleepy remote workers $3 per meeting they skip."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
