#!/usr/bin/env python3
"""Span scan against the DEBUT MAP: the complete first-token/rare-token
survey of a verse range, as a lookup.

Usage: python3 debut_scan.py <book> <chapter> <v_from> <v_to>
       e.g.  python3 debut_scan.py Gen 8 1 14

Flags per lemma (survey tier — counting only, no interpretation):
  DEBUT    the lemma's Torah token 1 is in this span
  EARLY    the span holds one of the lemma's first 6 tokens
  RARE     the lemma has 8 or fewer Torah tokens in total
  CLUSTER  3+ tokens of the lemma inside the span

Every romanized Hebrew word prints with its English gloss beside it.
Requires debut-snapshot.sqlite (build_debut_map.py).
"""
import os
import sqlite3
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "source-snapshot.sqlite")
MAP = os.path.join(ROOT, "debut-snapshot.sqlite")


def main():
    book, ch, v1, v2 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    src = sqlite3.connect(SRC)
    src.execute("ATTACH ? AS dm", (MAP,))
    rows = src.execute(
        """SELECT vv.chapter, vv.verse, w.idx, w.translit, w.gloss,
                  t.strong, t.ordinal, t.total
           FROM words w
           JOIN verses vv ON w.verse_id = vv.id
           JOIN dm.token_ordinals t ON t.word_id = w.id
           WHERE vv.book = ? AND vv.chapter = ? AND vv.verse BETWEEN ? AND ?
           ORDER BY vv.verse, w.idx""", (book, ch, v1, v2)).fetchall()

    lemmas = {}
    for c, v, i, tr, gl, strong, o, total in rows:
        lemmas.setdefault(strong, []).append((c, v, tr, gl, o, total))

    flagged = []
    for strong, toks in lemmas.items():
        total = toks[0][5]
        ords = [t[4] for t in toks]
        flags = []
        if 1 in ords:
            flags.append("DEBUT")
        elif min(ords) <= 6:
            flags.append("EARLY")
        if total <= 8:
            flags.append("RARE")
        if len(toks) >= 3:
            flags.append("CLUSTER")
        if flags:
            flagged.append((min(ords), strong, flags, toks, total))
    flagged.sort()

    print(f"== debut scan {book} {ch}:{v1}-{v2} — {len(rows)} tokens, "
          f"{len(lemmas)} lemmas, {len(flagged)} flagged ==")
    for min_o, strong, flags, toks, total in flagged:
        locs = ", ".join(f"{c}:{v} {tr} ('{gl}') tok {o}" for c, v, tr, gl, o, _ in toks)
        print(f"[{'+'.join(flags):>13}] Strong {strong:>5} ({total:>3} Torah tokens): {locs}")
    print(f"(unflagged lemmas: {len(lemmas) - len(flagged)} — common vocabulary, no early/rare signal)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
