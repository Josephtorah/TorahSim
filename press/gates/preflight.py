#!/usr/bin/env python3
"""preflight.py <uid>

Interpreter preflight for a DRAFT unit: copies it to a temp uid with
status flipped to frozen and dry_run_only stripped, runs run_unit.py
plain and --scenarios from the repo root, prints the tails, deletes the
temp copy. Exit 0 only if both runs succeed and scenarios end GREEN.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


def main():
    uid = sys.argv[1]
    src = REPO / "logic/units" / (uid + ".yaml")
    tmp_uid = "tmp_preflight_" + uid
    tmp = REPO / "logic/units" / (tmp_uid + ".yaml")
    s = src.read_text()
    s = s.replace("  status: draft\n", "  status: frozen\n")
    s = s.replace("  dry_run_only: true\n", "")
    tmp.write_text(s)
    try:
        ok = True
        r1 = subprocess.run([sys.executable, "press/run_unit.py", tmp_uid],
                            cwd=REPO, capture_output=True, text=True)
        print("\n".join((r1.stdout + r1.stderr).strip().split("\n")[-2:]))
        ok &= r1.returncode == 0
        r2 = subprocess.run([sys.executable, "press/run_unit.py", tmp_uid,
                             "--scenarios"], cwd=REPO,
                            capture_output=True, text=True)
        tail = (r2.stdout + r2.stderr).strip().split("\n")[-1]
        print(tail)
        bad = [ln for ln in r2.stdout.split("\n")
               if ln.strip().startswith(("FAIL", "UNCHECKED"))]
        for ln in bad[:10]:
            print(ln)
        ok &= r2.returncode == 0 and tail == "ALL SCENARIOS GREEN" and not bad
    finally:
        tmp.unlink(missing_ok=True)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
