#!/usr/bin/env python3
"""
check_coverage.py — golden-style guard for the provenance register:
every distinct work in oral_links must match exactly one register rule
(ordered prefix, first match wins). Prints the day-1 and whole-week
breakdown by chain status. Exit 1 if any work is unmatched.
"""

import re
import sqlite3
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
REG = yaml.safe_load((Path(__file__).parent / "v1" / "works.yaml").read_text(encoding="utf-8"))
RULES = REG["rules"]


def work_of(ref):
    w = re.sub(r"[,]? \d+[ab]?[:.].*$", "", ref)
    w = re.sub(r" \d+[ab]?(:\d+)*(-.*)?$", "", w)
    return w.strip()


def classify(ref):
    w = work_of(ref)
    for r in RULES:
        if w.startswith(r["prefix"].strip()):
            return r["status"]
    return None


def main():
    cx = sqlite3.connect(ROOT / "torah_grok.sqlite")
    refs = [r[0] for r in cx.execute("SELECT DISTINCT source_ref FROM oral_links WHERE tier=1")]
    unmatched = sorted({work_of(r) for r in refs if classify(r) is None})
    if unmatched:
        print("UNMATCHED WORKS (extend the register):")
        for w in unmatched:
            print("  ", w)
        sys.exit(1)

    day1 = [r[0] for r in cx.execute(
        """SELECT DISTINCT source_ref FROM oral_links WHERE tier=1
           AND anchor_osis IN ('Gen.1.1','Gen.1.2','Gen.1.3','Gen.1.4','Gen.1.5')""")]
    for label, pool in (("day-1 (483)", day1), ("whole week", refs)):
        c = Counter(classify(r) for r in pool)
        print("%s: %s" % (label, " · ".join("%s=%d" % kv for kv in c.most_common())))
    print("ALL WORKS MATCHED · register v1 (%s)" % REG["meta"]["status"])


if __name__ == "__main__":
    main()
