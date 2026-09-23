import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK sitting 13 — the manifest's seven check words PROBED IN THE STORE FIRST (sitting 12's lesson 11): the store splits a word into pieces and the
# check is the longest piece whole with a floor of four code points — the pieces and their lengths printed before a word is typed into the manifest.
import sqlite3, subprocess
ROOT = _ROOT
db = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
plain = lambda h: ''.join(c for c in h if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
for v, word in ((1, 'שמטה'), (4, 'אביון'), (8, 'תפתח'), (12, 'העברי'), (17, 'המרצע'), (19, 'הבכור'), (21, 'מום')):
    rows = db.execute("SELECT w.idx, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=15 AND v.verse=? ORDER BY w.idx", (v,)).fetchall()
    hit = [(i, h) for i, h in rows if plain(h) == word]
    for i, h in hit[:1]:
        piece = max(h.split('/'), key=len)
        print(f'15:{v} {word} idx {i} he {h!r} pieces {h.split("/")} longest {piece!r} len {len(piece)} {"OK" if len(piece) >= 4 else "UNDER THE FLOOR"}')
    if not hit: print(f'15:{v} {word} NOT FOUND')
