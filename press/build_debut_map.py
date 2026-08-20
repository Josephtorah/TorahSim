#!/usr/bin/env python3
"""Build the DEBUT MAP — a derived, gitignored census cache.

For every word token in the Torah, precompute its ORDINAL within its
lemma (1st, 2nd, 3rd ... token of that Strong-coded lemma in canonical
book/chapter/verse/word order) and the lemma's TOTAL Torah count. A
span query then answers "which words here are debuts / early tokens /
rare words" as a lookup instead of a per-lemma census.

Survey tier only (ein adam dan me-atzmo — "one may not derive on his
own"): the map counts tokens; it ranks, reads, and derives nothing.

Lemma normalization matches the derivation censuses (gen18_census.py):
take the segment after the last '/', then the part before any space
(strips ' a'/' b' homograph letters).

Source: source-snapshot.sqlite (canonical snapshot).
Output: debut-snapshot.sqlite at repo root
(*.sqlite is gitignored; this script is the committed provenance).

Acceptance gate: the map must reproduce the gen_18 review's verified
censuses exactly, or nothing is written.
"""
import os
import sqlite3
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "source-snapshot.sqlite")
OUT = os.path.join(ROOT, "debut-snapshot.sqlite")
BOOK_ORD = {"Gen": 1, "Exod": 2, "Lev": 3, "Num": 4, "Deut": 5}


def norm(lemma):
    seg = (lemma or "").split("/")[-1].strip()
    return seg.split(" ")[0]


def main():
    src = sqlite3.connect(SRC)
    rows = src.execute(
        """SELECT w.id, vv.book, vv.chapter, vv.verse, w.idx, w.lemma
           FROM words w JOIN verses vv ON w.verse_id = vv.id
           WHERE vv.book IN ('Gen','Exod','Lev','Num','Deut')""").fetchall()
    rows.sort(key=lambda r: (BOOK_ORD[r[1]], r[2], r[3], r[4]))

    counts, ordinals = {}, []
    for wid, book, ch, vs, idx, lemma in rows:
        strong = norm(lemma)
        if not strong:
            continue
        counts[strong] = counts.get(strong, 0) + 1
        ordinals.append((wid, strong, counts[strong]))

    # acceptance gate: reproduce the gen_18 review's verified censuses
    first = {}
    for wid, strong, o in ordinals:
        if o == 1:
            first[strong] = wid
    wid_ref = {r[0]: (r[1], r[2], r[3]) for r in rows}
    expect = {
        "7604": (29, ("Gen", 7, 23)),   # shaar 'be left' — the remnant root
        "1396": (7,  ("Gen", 7, 18)),   # gavar 'prevail'
        "5397": (3,  ("Gen", 2, 7)),    # neshamah 'breath'
        "3351": (3,  ("Gen", 7, 4)),    # yequm 'standing-substance'
        "5375": (168, ("Gen", 4, 13)),  # nasa 'lift/carry'
        "2724": (2,  ("Gen", 7, 22)),   # charavah 'dry land'
    }
    for strong, (total, ref) in expect.items():
        assert counts.get(strong) == total, (
            f"Strong {strong}: got {counts.get(strong)} tokens, expected {total}")
        assert wid_ref[first[strong]] == ref, (
            f"Strong {strong}: first token at {wid_ref[first[strong]]}, expected {ref}")
    print(f"acceptance gate GREEN ({len(expect)} verified censuses reproduced)")

    if os.path.exists(OUT):
        os.remove(OUT)
    out = sqlite3.connect(OUT)
    out.execute("CREATE TABLE token_ordinals (word_id INTEGER PRIMARY KEY, "
                "strong TEXT NOT NULL, ordinal INTEGER NOT NULL, total INTEGER NOT NULL)")
    out.executemany("INSERT INTO token_ordinals VALUES (?,?,?,?)",
                    [(wid, s, o, counts[s]) for wid, s, o in ordinals])
    out.execute("CREATE INDEX ix_strong ON token_ordinals(strong, ordinal)")
    out.commit()
    n_lemmas = len(counts)
    print(f"wrote {OUT}")
    print(f"{len(ordinals)} Torah tokens mapped across {n_lemmas} lemmas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
