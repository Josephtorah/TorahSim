#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
"""run_all.py — run every derivation unit in this directory, in canon
order, and report. Each unit file re-proves itself: its assertion block
was baked from the derivation machine's actual final state, so a GREEN
means the rendering still computes exactly what was frozen."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
INDEX = HERE.parent / "data" / "units_index.json"

ids = [u["unit_id"] for u in
       json.loads(INDEX.read_text(encoding="utf-8"))["units"]]
bad = 0
for uid in ids:
    path = HERE / (uid + ".py")
    r = subprocess.run([sys.executable, str(path)], capture_output=True)
    ok = (r.returncode == 0)
    bad += (not ok)
    print("%-44s %s" % (uid, "GREEN" if ok else "RED"))
print("%d units: %d GREEN, %d RED" % (len(ids), len(ids) - bad, bad))
sys.exit(1 if bad else 0)
