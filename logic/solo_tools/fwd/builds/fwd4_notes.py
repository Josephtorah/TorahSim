#!/usr/bin/env python3
"""Dump MS or KB notes for an Exodus chapter (run from repo root)."""
import sqlite3, sys
db = sqlite3.connect("torah_grok.sqlite")
kind, ch = sys.argv[1], sys.argv[2]
if kind == "ms":
    like = "Minchat Shai on Torah Exodus:%s:%%" % ch
    rows = db.execute("SELECT ref, he, en FROM export_texts WHERE work='Minchat Shai on Torah' AND ref LIKE ? ORDER BY ref", (like,)).fetchall()
else:
    like = "Kitzur Ba'al HaTurim on Exodus %s:%%" % ch
    rows = db.execute("SELECT ref, he, en FROM export_texts WHERE work=\"Kitzur Ba'al HaTurim on Exodus\" AND ref LIKE ? ORDER BY ref", (like,)).fetchall()
for ref, he, en in rows:
    print("=== %s ===" % ref)
    print(he or "")
    print("--- EN ---")
    print(en or "")
    print()
print("TOTAL %d notes" % len(rows))
