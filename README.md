# One-Line Office Joke: 24-Hour Sprint

[![make.fun](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/c/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/Nr1414-dev/one-line-office-joke/rank.svg)](https://make.fun/c/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/Nr1414-dev/one-line-office-joke/reward.svg)](https://make.fun/c/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

Entry for the [One-Line Office Joke: 24-Hour Sprint](https://make.fun/c/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
bounty on [make.fun](https://make.fun/): a program that writes one short joke
about office life (at most 200 characters) to `/output/entry.txt`.

## The joke

> The thermostat belongs to whoever shouts loudest — HR now issues sweaters in July.

## How it works

`main.py` validates the chosen line (one line, 1–200 characters, no control
characters) and writes it to `/output/entry.txt` with mode `0644`.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
