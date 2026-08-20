#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""prestage.py <book> <ch1>:<v1>-<ch2>:<v2>   (e.g. prestage.py Gen 31:22-31:54)

One-call pre-stage for a derivation span. Emits, in one pass:
  1. span shape: verse count, token count, verses lacking an etnachta
     ("rest," the mid-verse pause mark) with
     their fallback split points
  2. compact token map (idx.translit, etnachta ("rest," the mid-verse
     pause) starred, ketiv ("written" form) marked)
  3. volitive census (imperatives / jussives / cohortatives by morph)
  4. in-span DEBUTS (ordinal 1) with totals
  5. full career of EVERY distinct strong in-span whose total <= CAP
     (small careers are where the finds live), plus in-span positions +
     nearest neighbors for larger careers
No hand-picked strong lists — nothing to forget, no gap-fill round-trips.
"""
import re
import sqlite3
import sys
from collections import OrderedDict
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CAP = 30          # full career printed when total <= CAP
NEAR = 3          # neighbors shown either side for big careers
VOW = re.compile("[ְ-ׇּׁׂ]")


def parse_span(s):
    m = re.match(r"(\d+):(\d+)-(\d+):(\d+)$", s)
    if not m:
        sys.exit("span format: ch1:v1-ch2:v2")
    return tuple(int(x) for x in m.groups())


def main():
    book, span = sys.argv[1], parse_span(sys.argv[2])
    ch1, v1, ch2, v2 = span
    db = sqlite3.connect(str(REPO / "source-snapshot.sqlite"))
    db.execute("ATTACH ? AS dm",
               (str(REPO / "debut-snapshot.sqlite"),))
    if ch1 == ch2:
        cond, args = "v.chapter=? AND v.verse BETWEEN ? AND ?", (ch1, v1, v2)
    else:
        cond = ("((v.chapter=? AND v.verse>=?) OR (v.chapter>? AND v.chapter<?)"
                " OR (v.chapter=? AND v.verse<=?))")
        args = (ch1, v1, ch1, ch2, ch2, v2)
    rows = db.execute(
        "SELECT v.chapter, v.verse, w.idx, w.id, w.he, w.translit, w.lemma, "
        "w.morph, w.mark_id, w.mark_rank FROM words w "
        "JOIN verses v ON v.id=w.verse_id WHERE v.book=? AND %s "
        "ORDER BY v.chapter, v.verse, w.idx" % cond, (book,) + args).fetchall()
    if not rows:
        sys.exit("no tokens in span")
    in_span = {(r[0], r[1], r[2]) for r in rows}

    # 1. shape
    verses = OrderedDict()
    for r in rows:
        verses.setdefault((r[0], r[1]), []).append(r)
    print("=== SHAPE: %s %d:%d-%d:%d — %d verses, %d tokens ==="
          % (book, ch1, v1, ch2, v2, len(verses), len(rows)))
    for (ch, vs), toks in verses.items():
        if not any(t[8] == "etnachta" for t in toks):
            cands = [(t[9], t[2], t[8]) for t in toks[:-1] if t[9] and t[9] < 9]
            r_, i_, m_ = min(cands)
            print("  %d:%d NO ETNACHTA -> split at %s idx%d (rank %d)"
                  % (ch, vs, m_, i_, r_))

    # 2. token map
    print("\n=== TOKEN MAP (etnachta *, ketiv !) ===")
    for (ch, vs), toks in verses.items():
        parts = []
        for t in toks:
            tag = "*" if t[8] == "etnachta" else ""
            tag += "!" if not VOW.search(t[4]) else ""
            parts.append("%d.%s%s" % (t[2], t[5], tag))
        print("%d:%d :: %s" % (ch, vs, " ".join(parts)))

    # 3. volitives
    print("\n=== VOLITIVES (V?v imperative / V?j jussive / V?h cohortative) ===")
    n = 0
    for ch, vs, idx, wid, he, tr, lem, mo, mk, mr in rows:
        # person digit follows the form letter directly (Vqv2ms), so \b
        # would never fire mid-morph; require the digit instead
        for m in re.finditer(r"V([a-zA-Z])([vjh])(?=\d)", mo or ""):
            kind = {"v": "imperative", "j": "jussive", "h": "cohortative"}[m.group(2)]
            print("  %d:%d idx%d %-18s %-14s %s (%s)"
                  % (ch, vs, idx, tr, mo, kind, lem))
            n += 1
    if not n:
        print("  none")

    # 4+5. careers of every in-span strong
    seen = OrderedDict()
    for ch, vs, idx, wid, he, tr, lem, mo, mk, mr in rows:
        row = db.execute("SELECT strong, ordinal, total FROM dm.token_ordinals "
                         "WHERE word_id=?", (wid,)).fetchone()
        if row:
            seen.setdefault(row[0], []).append((row[1], ch, vs, idx, tr))
    print("\n=== IN-SPAN DEBUTS (ordinal 1) ===")
    for strong, toks in seen.items():
        firsts = [t for t in toks if t[0] == 1]
        if firsts:
            total = db.execute("SELECT total FROM dm.token_ordinals WHERE "
                               "strong=? LIMIT 1", (strong,)).fetchone()[0]
            for o, ch, vs, idx, tr in firsts:
                print("  %d:%d idx%d %-18s strong=%s (1/%d)"
                      % (ch, vs, idx, tr, strong, total))

    print("\n=== CAREERS (full if total<=%d; else in-span+%d neighbors) ==="
          % (CAP, NEAR))
    for strong, toks in seen.items():
        career = db.execute(
            "SELECT o.ordinal, o.total, v.book, v.chapter, v.verse, w.idx, "
            "w.translit, w.morph FROM dm.token_ordinals o "
            "JOIN words w ON w.id=o.word_id JOIN verses v ON v.id=w.verse_id "
            "WHERE o.strong=? ORDER BY o.ordinal", (strong,)).fetchall()
        total = career[0][1]
        if total == len([c for c in career
                         if (c[3], c[4], c[5]) in in_span and c[2] == book]):
            note = "  <<< WHOLE CAREER IN-SPAN"
        else:
            note = ""
        print("### %s (total %d; in-span %d)%s"
              % (strong, total, len(toks), note))
        if total <= CAP:
            show = career
        else:
            ords = {t[0] for t in toks}
            keep = set()
            for o in ords:
                keep.update(range(max(1, o - NEAR), min(total, o + NEAR) + 1))
            show = [c for c in career if c[0] in keep or c[0] <= 3]
        for o, t, bk, ch, vs, idx, tr, mo in show:
            mark = " <IN-SPAN>" if (bk == book and (ch, vs, idx) in in_span) else ""
            print("  %d/%d %s %d:%d idx%d %s %s%s"
                  % (o, t, bk, ch, vs, idx, tr, mo, mark))
        print()


if __name__ == "__main__":
    main()
