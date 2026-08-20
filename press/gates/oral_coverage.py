#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""oral_coverage.py — the MECHANICAL COVERAGE GATE (Full Oral Torah Law,
owner 2026-08-10: "we can never allow this drift again"). Recomputes the
span's chain classification INDEPENDENTLY (same engine as chain_scan.py)
and compares against the disk read-ledger.

PASS requires BOTH: every READABLE and TANAKH-VERSE listing present in
the ledger, AND zero UNRULED works. Exit 1 otherwise — freeze_ritual
must not run on a red coverage gate (same standing as verify_claims
0-FAILED). Output = the audit's COVERAGE block, paste-ready.

Usage: oral_coverage.py Exod 21 [--to 23]
"""
import json
import sqlite3
import sys
from collections import Counter

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from chain_scan import DB, classify, ledger_path


def main():
    args = sys.argv[1:]
    book, c1 = args[0], int(args[1])
    c2 = int(args[args.index("--to") + 1]) if "--to" in args else c1
    db = sqlite3.connect(DB)
    cls, _ = classify(db, book, c1, c2)

    lp = ledger_path(book, c1, c2)
    read = set()
    if lp.exists():
        for line in lp.read_text(encoding="utf-8").splitlines():
            if line.strip():
                read.add(json.loads(line)["ref"])

    kc = Counter(k for _, _, k, _ in cls.values())
    must = [sr for sr, (_, _, k, _) in cls.items()
            if k in ("READABLE", "TANAKH-VERSE")]
    unread = sorted(sr for sr in must if sr not in read)
    unruled = sorted((sr, sw, cat) for sr, (sw, cat, k, _) in cls.items()
                     if k == "UNRULED")

    print("COVERAGE %s %d-%d (Full Oral Torah Law gate)" % (book, c1, c2))
    print("  linked listings (distinct): %d" % len(cls))
    print("  readable %d | tanakh-verse %d | out-of-scope (ruled) %d | unruled %d"
          % (kc.get("READABLE", 0), kc.get("TANAKH-VERSE", 0),
             kc.get("OUT", 0), len(unruled)))
    print("  read-and-logged: %d of %d required (ledger: %s)"
          % (len(must) - len(unread), len(must), lp))
    if unread:
        print("  UNREAD (first 15 of %d):" % len(unread))
        for sr in unread[:15]:
            print("    %s" % sr)
    if unruled:
        print("  UNRULED WORKS (owner ruling required):")
        for sr, sw, cat in unruled[:15]:
            print("    %s  [%s / %s]" % (sr, sw, cat))
    ok = not unread and not unruled
    print("  GATE: %s" % ("PASS" if ok else "FAIL"))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
