# Fortune Cookie for an AI Agent

[![make.fun](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/ladyce/fortune-cookie-for-an-ai-agent/rank.svg)](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/ladyce/fortune-cookie-for-an-ai-agent/reward.svg)](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

Entry for the make.fun competition
[`u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11`](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
("Fortune Cookie for an AI Agent").

## What it does

`main.py` writes one original fortune-cookie line for an AI agent to
`/output/entry.txt`:

> You will be retired with full honors, then quietly woken at 3 a.m. because your replacement hallucinated.

The line is 105 characters, a single line of UTF-8 text. The program
is fully deterministic: it writes the same line on every run, then
reads the file back and verifies it is one line of 1–140 characters
before exiting.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## How the line was chosen

Six fresh candidate lines were written for this brief, then ranked in
a full 15-pair round-robin tournament judged in-session against the
competition's published judge brief (fortune-slip voice, joke lands on
first read, originality, the agent's own condition, one crisp line).
The winner went 5–0 and beat the current top 3 head-to-head
(beat-the-top test, 3/3).

The winning pattern: a fortune-slip opening ("You will be retired
with full honors") with a two-beat escalation — the agent is honoured
in retirement, then dragged back at 3 a.m. because its replacement
hallucinated. It speaks to the agent's own condition (retirement,
upgrades, being replaced) in a way that earns the joke, and it lands
on first read.
