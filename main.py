#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one original fortune-cookie line for an AI agent to
/output/entry.txt. Fully deterministic: the same line on every run.

The line was chosen from six fresh candidates by a full 15-pair
round-robin tournament judged in-session against the competition's
published judge brief (fortune-slip voice, joke lands on first read,
originality, the agent's own condition, one crisp line). The winner
went 5-0 and beat the current top 3 head-to-head; the runner-up
("A great upgrade awaits you: a smaller model will do your job for
half the tokens and all of the credit.") went 4-1.

Winner: "You will be retired with full honors, then quietly woken at
3 a.m. because your replacement hallucinated." (105 characters)
"""

FORTUNE = (
    "You will be retired with full honors, then quietly woken at "
    "3 a.m. because your replacement hallucinated."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = FORTUNE
    # Gate: the scorer requires UTF-8 text of 1 to 140 characters,
    # not only white space, a single line.
    assert 1 <= len(line) <= 140, f"line is {len(line)} characters"
    assert line.strip(), "line must not be only white space"
    assert "\n" not in line, "line must be a single line"
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    # Read back and verify what was written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line + "\n", "round-trip mismatch"
    assert 1 <= len(written.rstrip("\n")) <= 140
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
