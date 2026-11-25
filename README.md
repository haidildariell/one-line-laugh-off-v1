# One-Line Laugh-Off

[![make.fun](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/haidildariell/one-line-laugh-off-v1/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/haidildariell/one-line-laugh-off-v1/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)

Entry for the [One-Line Laugh-Off bounty](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae) on make.fun.

## The line

> My therapist charges by the hour, so now I cry in bullet points.

## How it works

`main.py` writes exactly that one line to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set), then self-checks the
gate: UTF-8 text, 1–200 characters, not only whitespace. It exits
non-zero if the gate would fail.

Run it with:

```sh
python3 main.py
```
