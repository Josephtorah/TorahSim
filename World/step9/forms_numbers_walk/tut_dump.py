#!/usr/bin/env python3
"""tut_dump.py — dump verses for the Numbers tutorial: the pointed Hebrew from the store's own bytes, each word with its
accent name (unicodedata) and the store's gloss (Torah verses from the snapshot store; other books from the Tanakh DB)."""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import sqlite3, sys, re, unicodedata
SNAP = (_ROOT + '/torah_grok.SNAPSHOT-main-51801ca.sqlite')
TAN = (_ROOT + '/Data/tanakh.sqlite')
snap = sqlite3.connect(SNAP); tan = sqlite3.connect(TAN)
TORAH = {'Gen', 'Exod', 'Lev', 'Num', 'Deut'}

def accents(w):
    out = []
    for ch in w:
        if 0x0591 <= ord(ch) <= 0x05AE:
            out.append(unicodedata.name(ch).replace('HEBREW ACCENT ', ''))
    return out

def plain(w):
    return re.sub(r'[֑-ׇ/]', '', w)

def dump(book, c, v, table=True):
    if book in TORAH:
        r = snap.execute("select id from verses where book=? and chapter=? and verse=?", (book, c, v)).fetchone()
        rows = snap.execute("select he, gloss, maqqef_after from words where verse_id=? order by idx", (r[0],)).fetchall()
    else:
        r = tan.execute("select id from verses where book=? and chapter=? and verse=?", (book, c, v)).fetchone()
        rows = [(h, '', 0) for (h,) in tan.execute("select he from words where verse_id=? order by idx", (r[0],)).fetchall()]
    text = ' '.join(h.replace('/', '') for h, _, _ in rows)
    print(f'=== {book} {c}:{v}')
    print(text)
    if table:
        for h, g, mq in rows:
            print(f'  {plain(h):<12} {h.replace("/", ""):<16} {",".join(accents(h)) or "-":<22} {g}{"  [maqqef]" if mq else ""}')

if __name__ == '__main__':
    for ref in sys.argv[1:]:
        b, cv = ref.split(':', 1) if ' ' not in ref else ref.split(' ')
        c, v = cv.split(':')
        dump(b, int(c), int(v))
