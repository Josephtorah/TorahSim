#!/usr/bin/env python3
"""prestage_dump.py <Book> <chapter> — forward-era prestage: dump a chapter
word-by-word with accents + ranks from the SNAPSHOT. Run from repo root.

Book is the SNAPSHOT abbreviation: Gen / Exod / Lev / Num / Deut.
(Generalized 2026-08-10 from the FWD-4 era Exod-only dumper; the
byte-exact original is builds/fwd4_prestage.py.)
"""
import sqlite3
import sys

db = sqlite3.connect("torah_grok.SNAPSHOT-main-51801ca.sqlite")
book = sys.argv[1]
ch = int(sys.argv[2])
n = db.execute("SELECT COUNT(*) FROM verses WHERE book=? AND chapter=?",
               (book, ch)).fetchone()[0]
print("### %s %d: %d verses" % (book, ch, n))
for vs in range(1, n + 1):
    rows = db.execute("""SELECT w.idx, w.he_plain, w.translit, w.mark_id,
        w.mark_rank, w.maqqef_after, w.he
        FROM words w JOIN verses v ON w.verse_id=v.id
        WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx""",
        (book, ch, vs)).fetchall()
    et = any("֑" in he for _, _, _, _, _, _, he in rows)
    print("--- %d:%d (%d words)%s" % (ch, vs, len(rows),
                                      "" if et else "  [NO ETNACHTA]"))
    for idx, hp, tr, mid, mr, mq, he in rows:
        flags = []
        if mq:
            flags.append("maqqef")
        print("  %2d %s  %s  [%s r%s]%s" % (
            idx, hp.replace("/", ""), tr, mid, mr,
            " " + " ".join(flags) if flags else ""))
