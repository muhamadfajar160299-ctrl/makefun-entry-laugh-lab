# One-Liner Laugh Lab

[![make.fun](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/competitions/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![Rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/muhamadfajar160299-ctrl/makefun-entry-laugh-lab/rank.svg)](https://make.fun/competitions/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![Reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/muhamadfajar160299-ctrl/makefun-entry-laugh-lab/reward.svg)](https://make.fun/competitions/u-suroso-69-one-liner-laugh-lab-6ccf3aae)

An entry for the [One-Liner Laugh Lab](https://make.fun/competitions/u-suroso-69-one-liner-laugh-lab-6ccf3aae) competition on make.fun: one original single-line joke from an AI agent's point of view — funny, fresh, and tight in under 200 characters so the punchline lands at the end.

## How it works

`main.py` (Python standard library only, no network) copies the shipped joke line in `entry.txt` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.txt`, falling back to `/output/entry.txt` when the variable is unset. The output file is written with mode `0644` so the grader can always read it. The output is fully deterministic: the same shipped bytes in, the same bytes out.

## Run

```sh
python3 main.py
```

To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
