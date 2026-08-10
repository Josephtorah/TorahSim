#!/usr/bin/env python3
"""FWD-4 prestage: dump Exod chapters word-by-word with accents + ranks."""
import sqlite3, sys
db = sqlite3.connect("torah_grok.SNAPSHOT-main-51801ca.sqlite")
ch = int(sys.argv[1])
n = db.execute("SELECT COUNT(*) FROM verses WHERE book='Exod' AND chapter=?", (ch,)).fetchone()[0]
print("### Exod %d: %d verses" % (ch, n))
for vs in range(1, n + 1):
    rows = db.execute("""SELECT w.idx, w.he_plain, w.translit, w.mark_id, w.mark_rank, w.maqqef_after, w.he
        FROM words w JOIN verses v ON w.verse_id=v.id
        WHERE v.book='Exod' AND v.chapter=? AND v.verse=? ORDER BY w.idx""", (ch, vs)).fetchall()
    et = any("֑" in he for _,_,_,_,_,_,he in rows)
    print("--- %d:%d (%d words)%s" % (ch, vs, len(rows), "" if et else "  [NO ETNACHTA]"))
    for idx, hp, tr, mid, mr, mq, he in rows:
        flags = []
        if mq: flags.append("maqqef")
        print("  %2d %s  %s  [%s r%s]%s" % (idx, hp.replace("/",""), tr, mid, mr, " "+" ".join(flags) if flags else ""))
