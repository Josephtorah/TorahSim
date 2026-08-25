#!/usr/bin/env python3
"""
index_triage.py — logic/oral_triage/*.md ledger tables -> DB triage table.

The promotion step for the reference-tracking system: the hand-written triage
ledgers (canonical, git-versioned, KB-scale) become a derived, queryable index —
same architecture as index_oral_links.py. Answers, in one query: every source
ever read, on which unit, with what verdict and what we think it means. The
web app can later surface "N sources read on this verse, k material" from here.

Ledger contract (what this parser relies on):
  - filename: <unit>_<YYYY-MM-DD>.md
  - a '## Ledger' section (or '## Row table', the Eden-era heading)
    containing a markdown table
    | # | source | status | verdict | note |
  - verdict cell may carry ** emphasis and qualifiers ('material (already
    cited)', 'dup-of:<ref>'); the first token normalizes to verdict_class
    ('no-bearing' is the Eden-era spelling of 'not-bearing' — both stand)

Never writes ledgers. DB is never the system of record.
"""

import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "logic" / "oral_triage"

VERDICT_CLASSES = {"material", "enrichment", "context", "not-bearing",
                   "no-bearing", "dup-of", "read-partial"}


def verdict_class(raw):
    head = raw.strip().strip("*").split()[0].split(":")[0].rstrip(",")
    return head if head in VERDICT_CLASSES else "UNRECOGNIZED"


def parse_ledger(path):
    m = re.match(r"(.+)_(\d{4}-\d{2}-\d{2})\.md$", path.name)
    unit, ledger_date = m.group(1), m.group(2)
    text = path.read_text(encoding="utf-8")
    parts = re.split(r"## (?:Ledger|Row table)", text, maxsplit=1)
    if len(parts) < 2:
        raise SystemExit(f"{path.name}: no '## Ledger' / '## Row table' section")
    body = parts[1]
    rows = []
    for line in body.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 5 or not cells[0].isdigit():
            continue
        num, source, status, verdict, note = cells
        rows.append((unit, ledger_date, int(num), source, status,
                     verdict.replace("**", ""), verdict_class(verdict), note))
    return rows


def main():
    cx = sqlite3.connect(ROOT / "data" / "derivation.sqlite")
    cx.executescript("""
        DROP TABLE IF EXISTS triage;
        CREATE TABLE triage (
            unit TEXT, ledger_date TEXT, row_num INT, source_ref TEXT,
            chain_status TEXT, verdict TEXT, verdict_class TEXT, note TEXT);
        CREATE INDEX ix_triage_source ON triage(source_ref);
    """)
    total = 0
    for path in sorted(SRC.glob("*.md")):
        rows = parse_ledger(path)
        cx.executemany("INSERT INTO triage VALUES (?,?,?,?,?,?,?,?)", rows)
        total += len(rows)
        print("%-40s %3d rows" % (path.name, len(rows)))
    cx.commit()

    bad = cx.execute(
        "SELECT unit, row_num, verdict FROM triage "
        "WHERE verdict_class='UNRECOGNIZED'").fetchall()
    if bad:
        print("UNRECOGNIZED verdicts (fix the ledger or extend the vocabulary):")
        for u, n, v in bad:
            print("   %s row %d: %r" % (u, n, v))

    print("triage: %d rows indexed" % total)
    for unit, cls, n in cx.execute(
            "SELECT unit, verdict_class, COUNT(*) FROM triage "
            "GROUP BY unit, verdict_class ORDER BY unit, 3 DESC"):
        print("   %-25s %-12s %d" % (unit, cls, n))


if __name__ == "__main__":
    main()
