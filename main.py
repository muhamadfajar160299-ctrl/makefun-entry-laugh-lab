"""Copy entry.txt next to this program into the grader output dir.

Single direct write, no temp file or rename, so the output keeps mode 0644
and stays readable by the grader.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

try:
    data = (HERE / "entry.txt").read_bytes()
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / "entry.txt"
    target.write_bytes(data)
    os.chmod(target, 0o644)
except OSError as exc:
    raise SystemExit(f"cannot write entry: {exc}") from exc
