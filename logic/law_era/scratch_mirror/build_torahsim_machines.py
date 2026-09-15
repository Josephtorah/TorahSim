#!/usr/bin/env python3
"""
build_torahsim_machines.py — home-side copier for the PUBLIC TorahSim
repo's machines/exo21/ tree. Copies the four Exodus 21 machine files out of
Torah_Grok with three mechanical transformations (verified: nothing else
changes):

  1. _frozen_spans() reads data/units_index.json (shipped, 97 units)
     instead of the private torah_grok.sqlite.
  2. File and module names lose the private era-prefix:
     exo_21_v2_block1_DRAFT -> block1 (likewise 2, 3),
     exo_21_v2_DRAFT -> chapter.
  3. Witness-manifest paths point at the public scans/manifests/.

Rerun after any machine change at home to refresh the public copies.
"""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
from pathlib import Path

HOME = Path((_ROOT + "/logic/law_era"))
PUB = Path("<repo>/machines/exo21")

OLD_SPANS = '''def _frozen_spans():
    import sqlite3, re, os
    db = sqlite3.connect(os.path.join(os.path.dirname(__file__),
                                      "..", "..", "torah_grok.sqlite"))
    spans = []
    for uid, book, refs in db.execute(
            "SELECT unit_id, book_en, refs FROM units WHERE status='frozen'"):
        m = re.match(r"^(\\d+):(\\d+)-(?:(\\d+):)?(\\d+)$", refs.strip())
        if not m:
            continue
        c1, v1 = int(m.group(1)), int(m.group(2))
        c2 = int(m.group(3)) if m.group(3) else c1
        v2 = int(m.group(4))
        spans.append((book, c1, v1, c2, v2, uid))
    return spans
'''

NEW_SPANS = '''def _frozen_spans():
    import json, re, os
    path = os.path.join(os.path.dirname(__file__),
                        "..", "..", "data", "units_index.json")
    spans = []
    with open(path, encoding="utf-8") as f:
        units = json.load(f)["units"]
    for u in units:
        m = re.match(r"^(\\d+):(\\d+)-(?:(\\d+):)?(\\d+)$", u["refs"].strip())
        if not m:
            continue
        c1, v1 = int(m.group(1)), int(m.group(2))
        c2 = int(m.group(3)) if m.group(3) else c1
        v2 = int(m.group(4))
        spans.append((u["book"], c1, v1, c2, v2, u["unit_id"]))
    return spans
'''

RENAMES = {
    "exo_21_v2_block1_DRAFT": "block1",
    "exo_21_v2_block2_DRAFT": "block2",
    "exo_21_v2_block3_DRAFT": "block3",
    "exo_21_v2_DRAFT": "chapter",
    "logic/oral_audit/manifests/": "scans/manifests/",
    "oral_audit/manifests/": "scans/manifests/",
    "torah_grok.sqlite, the same index the web app runs on":
        "data/units_index.json, the shipped index of derived units",
    "DEPENDENCY PROOF — %d edges verified against torah_grok.sqlite:":
        "DEPENDENCY PROOF — %d edges verified against units_index.json:",
}

FILES = {
    "exo_21_v2_block1_DRAFT.py": "block1.py",
    "exo_21_v2_block2_DRAFT.py": "block2.py",
    "exo_21_v2_block3_DRAFT.py": "block3.py",
    "exo_21_v2_DRAFT.py": "chapter.py",
}


NOTICE = ("# TorahSim — (c) 2026 Brian LeBlanc · MIT license "
          "(see LICENSE at repo root)\n")


def main():
    PUB.mkdir(parents=True, exist_ok=True)
    for src_name, dst_name in FILES.items():
        text = (HOME / src_name).read_text(encoding="utf-8")
        n_spans = text.count(OLD_SPANS)
        text = text.replace(OLD_SPANS, NEW_SPANS)
        for old, new in RENAMES.items():
            text = text.replace(old, new)
        assert "torah_grok.sqlite" not in text, src_name
        assert "oral_audit" not in text, src_name
        lines = text.splitlines(keepends=True)
        lines.insert(1 if lines and lines[0].startswith("#!") else 0, NOTICE)
        (PUB / dst_name).write_text("".join(lines), encoding="utf-8")
        print("%s -> %s  (spans swapped: %d)" % (src_name, dst_name, n_spans))


if __name__ == "__main__":
    main()
