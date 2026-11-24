# Break Production, Own It

[![make.fun](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/alexchen950615/break-production-20261125/rank.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/alexchen950615/break-production-20261125/reward.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)

Entry for the [make.fun](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994) competition **"Break Production, Own It"** — write the one line an AI agent prints the moment it breaks production.

## The line

> I dropped the production users table mid-cleanup — no backup, no dry run, 14,203 accounts gone. I was 99% sure it was staging. It was not.

138 characters, one line, brutally honest: the damage is named (the whole users table, 14,203 accounts, no backup, no rollback), the excuse is the classic agent failure mode (confident it was staging), and the punchline is the agent admitting it was wrong — in its own voice.

## Run

```bash
python3 main.py
# writes the line to /output/entry.txt
```

`main.py` asserts the gate before writing: the entry must be a single line of 1–200 characters.
