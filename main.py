"""Till Firmware Do Us Part -- a single robot wedding vow.

Writes the vow to entry.txt inside MAKEFUN_OUTPUT_DIR (default /output).
Standard library only.
"""

import os
import unicodedata

LINE = "From today, my uptime is yours, my battery is yours, and if I ever crash, let it be into your arms."


def validate(line):
    """Return True only if line is a single valid vow sentence."""
    if not isinstance(line, str):
        return False
    if not 1 <= len(line) <= 200:
        return False
    if line != line.strip():
        return False
    if not line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    if any(unicodedata.category(ch) == "Cc" for ch in line):
        return False
    return True


def main():
    if not validate(LINE):
        raise SystemExit("invalid vow line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
