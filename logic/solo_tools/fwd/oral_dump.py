#!/usr/bin/env python3
"""oral_dump.py <BookEnglish> <chapter> — dump the two anchor commentaries
for a chapter from the LOCAL mirror (torah_grok.sqlite export_texts):
Kitzur Baal HaTurim, then Minchat Shai. Zero web fetches. Run from repo
root; redirect stdout per run (e.g. > scratch/kb_ms_exo22.txt).

BookEnglish is the mirror's English name: Genesis / Exodus / Leviticus /
Numbers / Deuteronomy. Ref formats in the mirror differ per work:
  Kitzur:       "Kitzur Ba'al HaTurim on Exodus 21:6:1"
  Minchat Shai: "Minchat Shai on Torah Exodus:21:6:1"
Further works (Rashi etc.) are pulled ad hoc:
  SELECT ref, he, en FROM export_texts WHERE ref LIKE 'Rashi on Exodus 19:2%'
"""
import sqlite3
import sys

db = sqlite3.connect("torah_grok.sqlite")
book = sys.argv[1]
ch = int(sys.argv[2])

def dump(title, sql, args):
    rows = db.execute(sql, args).fetchall()
    print("########## %s — %d notes ##########\n" % (title, len(rows)))
    for ref, he, en in rows:
        print("=== %s ===" % ref)
        print(he or "")
        print("--- EN ---")
        print(en or "")
        print()

dump("Kitzur Baal HaTurim on %s %d" % (book, ch),
     "SELECT ref, he, en FROM export_texts WHERE ref LIKE ? ORDER BY ref",
     ("Kitzur Ba'al HaTurim on %s %d:%%" % (book, ch),))
dump("Minchat Shai on Torah %s %d" % (book, ch),
     "SELECT ref, he, en FROM export_texts WHERE work='Minchat Shai on Torah' "
     "AND ref LIKE ? ORDER BY ref",
     ("%%%s:%d:%%" % (book, ch),))
