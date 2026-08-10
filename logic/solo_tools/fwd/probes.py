#!/usr/bin/env python3
"""probes.py — forward-era claim-probe helpers against the SNAPSHOT.
Import from a per-run probe script (run from repo root):

    import sys; sys.path.insert(0, "logic/solo_tools/fwd")
    from probes import census, adjacency, hp, he, vlen, g

Every manifest row gets probed BEFORE it is claimed (the FWD-8 law:
probe-before-claim kept all five manifests first-run clean). The
verifier's adjacency matches the SECOND token by TRANSLIT — probe
accordingly (the EX17-05 pausal/contextual lesson).
"""
import sqlite3

DB = "torah_grok.SNAPSHOT-main-51801ca.sqlite"
_db = sqlite3.connect(DB)


def census(sp):
    """All (book, ch, vs) where the slash-stripped he_plain equals sp —
    NOTE: ordered ALPHABETICALLY by book (Deut<Exod<Gen<Lev<Num)."""
    return _db.execute("""SELECT v.book, v.chapter, v.verse FROM words w
        JOIN verses v ON w.verse_id=v.id
        WHERE replace(w.he_plain,'/','')=?
        ORDER BY v.book, v.chapter, v.verse""", (sp,)).fetchall()


def adjacency(first, second_set):
    """(book, ch, vs) where token `first` (he_plain) is immediately followed
    by a token whose he_plain is in second_set. The VERIFIER's adjacency
    check matches the second token by TRANSLIT — confirm the translit
    before writing the manifest row."""
    hits = []
    for b, c, v, i in _db.execute("""SELECT v.book, v.chapter, v.verse, w.idx
            FROM words w JOIN verses v ON w.verse_id=v.id
            WHERE replace(w.he_plain,'/','')=?""", (first,)):
        nxt = _db.execute("""SELECT w.he_plain FROM words w
            JOIN verses vv ON w.verse_id=vv.id
            WHERE vv.book=? AND vv.chapter=? AND vv.verse=? AND w.idx=?""",
            (b, c, v, i + 1)).fetchone()
        if nxt and nxt[0].replace("/", "") in second_set:
            hits.append((b, c, v))
    return sorted(hits)


def hp(ch, vs, idx, book="Exod"):
    """Slash-stripped he_plain of one token (the skeleton layer)."""
    return _db.execute("""SELECT w.he_plain FROM words w
        JOIN verses v ON w.verse_id=v.id
        WHERE v.book=? AND v.chapter=? AND v.verse=? AND w.idx=?""",
        (book, ch, vs, idx)).fetchone()[0].replace("/", "")


def he(ch, vs, idx, book="Exod"):
    """Fully pointed he of one token (dagesh PRECEDES the vowel in
    codepoints — substring-assert with the לּ-style forms)."""
    return _db.execute("""SELECT w.he FROM words w
        JOIN verses v ON w.verse_id=v.id
        WHERE v.book=? AND v.chapter=? AND v.verse=? AND w.idx=?""",
        (book, ch, vs, idx)).fetchone()[0]


def vlen(ch, vs, book="Exod"):
    """Word count of a verse."""
    return _db.execute("""SELECT COUNT(*) FROM words w
        JOIN verses v ON w.verse_id=v.id
        WHERE v.book=? AND v.chapter=? AND v.verse=?""",
        (book, ch, vs)).fetchone()[0]


G = {"א": 1, "ב": 2, "ג": 3, "ד": 4, "ה": 5, "ו": 6, "ז": 7, "ח": 8, "ט": 9,
     "י": 10, "כ": 20, "ך": 20, "ל": 30, "מ": 40, "ם": 40, "נ": 50, "ן": 50,
     "ס": 60, "ע": 70, "פ": 80, "ף": 80, "צ": 90, "ץ": 90, "ק": 100,
     "ר": 200, "ש": 300, "ת": 400}


def g(s):
    """Standard-value gematria of a string (finals = base values).
    Assert only EXACT equalities; off-by-one is the tradition's own
    with-the-kollel device — name it, never assert it."""
    return sum(G[c] for c in s if c in G)
