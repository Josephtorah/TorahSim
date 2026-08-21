#!/usr/bin/env python3
"""changelog_gate.py — the RE-era constitution's one tax on unit edits.

Unit logic is freely rewritable (METHOD_LAWS constitution, owner ruling
2026-08-21), but any diff to a canonical unit YAML must arrive with a
new changelog line (and its bumped rev). This is the workshop port of
the TorahSim check.py "changelog" gate: compares logic/units against
git HEAD; a clean tree passes trivially; exits 1 naming each edited
YAML that lacks a new changelog line.

Run: python3 logic/solo_tools/changelog_gate.py
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def clog_count(text):
    m = re.search(r"^  changelog:\n((?:    - .*\n)+)", text, re.M)
    return len(m.group(1).splitlines()) if m else 0


def main():
    r = subprocess.run(["git", "diff", "--name-only", "HEAD", "--",
                        "logic/units"], cwd=ROOT,
                       capture_output=True, text=True)
    if r.returncode != 0:
        print("changelog  SKIP  git unavailable")
        return 0
    changed = [l.strip() for l in r.stdout.splitlines() if l.strip()]
    bad = []
    for rel in changed:
        path = ROOT / rel
        now = clog_count(path.read_text(encoding="utf-8")) \
            if path.exists() else 0
        h = subprocess.run(["git", "show", "HEAD:%s" % rel], cwd=ROOT,
                           capture_output=True, text=True)
        before = clog_count(h.stdout) if h.returncode == 0 else 0
        if now <= before:
            bad.append(Path(rel).name)
    if bad:
        for b in bad:
            print("changelog  RED  EDIT WITHOUT CHANGELOG: %s" % b)
        return 1
    print("changelog  GREEN  %d unit YAML(s) edited, each carries its "
          "new changelog line" % len(changed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
