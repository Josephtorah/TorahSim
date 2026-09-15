#!/usr/bin/env python3
"""
build_torahsim_units.py — home-side exporter for the PUBLIC TorahSim
repo's units/ tree: the 97 frozen derivation units as runnable Python
renderings, plus the machine.py library that backs them and the ALL_UNITS
runner.

Source of truth for WHICH units ship: TorahSim/data/units_index.json
(itself exported from the units table by build_torahsim_data.py) — the
exporter fails loudly if a listed unit has no rendering.

Each copied file gets the MIT notice line injected after the shebang so the
license travels with single-file copies. Nothing else is changed: the
renderings are generated files ("do not edit — regenerate") and stay
byte-faithful to home.
"""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import json
from pathlib import Path

HOME = Path((_ROOT + "/logic/py_units"))
PUB = Path("<repo>/units")
INDEX = Path("<repo>/data/units_index.json")

NOTICE = ("# TorahSim — (c) 2026 Brian LeBlanc · MIT license "
          "(see LICENSE at repo root)\n")


def copy_with_notice(src, dst):
    text = src.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    if lines and lines[0].startswith("#!"):
        lines.insert(1, NOTICE)
    else:
        lines.insert(0, NOTICE)
    dst.write_text("".join(lines), encoding="utf-8")


def main():
    PUB.mkdir(parents=True, exist_ok=True)
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    ids = [u["unit_id"] for u in index["units"]]
    missing = [uid for uid in ids if not (HOME / (uid + ".py")).exists()]
    assert not missing, "no rendering for: %s" % missing

    for uid in ids:
        copy_with_notice(HOME / (uid + ".py"), PUB / (uid + ".py"))
    for extra in ("machine.py", "ALL_UNITS.py"):
        copy_with_notice(HOME / extra, PUB / extra)
    print("exported %d units + machine.py + ALL_UNITS.py -> %s"
          % (len(ids), PUB))


if __name__ == "__main__":
    main()
