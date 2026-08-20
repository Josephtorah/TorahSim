#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_text.py <uid>

Independent text-layer check: recomputes every step's plain he line, tree
halves (etnachta split with strongest-disjunctive fallback), operator he
fragments, and scenario value fragments from the SNAPSHOT with logic
written separately from the builder, and diffs against the unit YAML.
Exit 0 = green.
"""
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

import sys as _vsys; from pathlib import Path as _VP; _vsys.path.insert(0, str(_VP(__file__).resolve().parent.parent / "vendor"))
import yaml

REPO = Path(__file__).resolve().parents[2]
DB = REPO / "source-snapshot.sqlite"
ACC = re.compile("[֑-ֽ֯]")   # cantillation + meteg, explicit
VOW = re.compile("[ְ-ׇּׁׂ]")
MAQ = "־"


def nfc(s):
    return unicodedata.normalize("NFC", s)


def main():
    uid = sys.argv[1]
    U = yaml.safe_load(open(REPO / "logic/units" / (uid + ".yaml")))
    db = sqlite3.connect(str(DB))
    fails = []

    def check(label, got, want):
        if nfc(got) != nfc(want):
            fails.append((label, want, got))

    for st in U["boot_steps"]:
        bk, ch, vs = st["ref"].split(".")
        ch, vs = int(ch), int(vs)
        rows = db.execute(
            "SELECT w.idx, w.he, w.maqqef_after, w.mark_id, w.mark_rank "
            "FROM words w JOIN verses v ON v.id=w.verse_id "
            "WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx",
            (bk, ch, vs)).fetchall()
        plain = ""
        for i, (idx, he, mq, mk, mr) in enumerate(rows):
            plain += ACC.sub("", he.replace("/", ""))
            if i < len(rows) - 1:
                plain += MAQ if mq else " "
        check(st["ref"] + " he", st["he"], plain)
        if not VOW.search(st["he"]):
            fails.append((st["ref"] + " VOWELLESS", "", st["he"]))
        et = [idx for idx, he, mq, mk, mr in rows if mk == "etnachta"]
        if et:
            e = et[0]
        else:
            e = min((mr, idx) for idx, he, mq, mk, mr in rows[:-1]
                    if mr and mr < 9)[1]
        left = " ".join(he.replace("/", "") for idx, he, mq, mk, mr in rows
                        if idx <= e)
        right = " ".join(he.replace("/", "") for idx, he, mq, mk, mr in rows
                         if idx > e)
        check(st["ref"] + " tree_left", st["tree_left"]["he"], left)
        check(st["ref"] + " tree_right", st["tree_right"]["he"], right)
        for op in st.get("operators", []):
            oh = op.get("he", "")
            if oh and nfc(oh) not in nfc(plain):
                fails.append((st["ref"] + " op-frag not in plain", oh, plain))

    book = U["boot_steps"][0]["ref"].split(".")[0]
    for sc in U.get("scenarios", []):
        m = re.search(r"STEP_\w\w_(\d+)_(\d+)", sc["title_en"])
        if not m:
            fails.append((sc["id"] + " no step anchor", "", sc["title_en"]))
            continue
        rows = db.execute(
            "SELECT w.he FROM words w JOIN verses v ON v.id=w.verse_id "
            "WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx",
            (book, int(m.group(1)), int(m.group(2)))).fetchall()
        acc_line = " ".join(h.replace("/", "") for (h,) in rows)
        if nfc(sc["value_he"]) not in nfc(acc_line):
            fails.append((sc["id"] + " value_he not in verse",
                          sc["value_he"], acc_line))

    if fails:
        for label, want, got in fails:
            print("FAIL", label)
            print("  want:", want)
            print("  got :", got)
        sys.exit(1)
    print("TEXT LAYER GREEN: %d steps, %d scenarios — %s"
          % (len(U["boot_steps"]), len(U.get("scenarios", [])), uid))


if __name__ == "__main__":
    main()
