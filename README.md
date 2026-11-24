# Till Firmware Do Us Part

[![make.fun](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)
[![Rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/cffilham-jpg/makefun-robot-vows-32172929/rank.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)
[![Reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/cffilham-jpg/makefun-robot-vows-32172929/reward.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)

A single wedding vow spoken by a robot at its own wedding: funny, sincere, and unmistakably machine — uptime and battery offered up, with one last crash landing exactly where it should.

> From today, my uptime is yours, my battery is yours, and if I ever crash, let it be into your arms.

Referral code: `fpna5aje`

## How it works

`main.py` holds the vow as the constant `LINE`. Before writing anything, `validate()` checks it: it must be a string of 1–200 characters, a single line with no newline characters, not only whitespace, with no leading or trailing whitespace, and free of Unicode control characters (category Cc). If validation fails, the program exits without writing. On success, `main()` writes the line to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (default `/output`), creating the directory if needed, with no trailing newline.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
