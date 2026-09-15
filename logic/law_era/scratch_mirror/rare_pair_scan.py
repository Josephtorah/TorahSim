#!/usr/bin/env python3
"""
rare_pair_scan.py — the exclusive-join scanner: find every unpointed
phrase (3-gram and 4-gram) that occurs EXACTLY TWICE in the whole
Tanakh, in two DIFFERENT books. These are the candidate deliberate
cross-book channels (the gezerah-shavah class: mot tamut, the two
tardemah sleeps, the land-sabbath idiom), mined systematically.

Parallel-block suppression: verse-pairs sharing >=3 distinct exclusive
n-grams are synoptic duplicates (Kings/Chronicles, Ps 18/2 Sam 22,
Isa 36-39/2 Kgs 18-20) and are set aside into their own list.

Output: scratchpad files rare_pairs_3.txt / rare_pairs_4.txt, ranked by
token rarity (rarest component words first).
Usage: python3 logic/law_era/scratch_mirror/rare_pair_scan.py
"""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import re
import sqlite3
from collections import defaultdict

ROOT = _ROOT
SCRATCH = ("<scratch-root>/"
           "4ca32657-770b-417a-8a21-73333c8d5f75/scratchpad")
POINT = re.compile(u"[֑-ׇ]")

db = sqlite3.connect(ROOT + "/Data/tanakh.sqlite")
verses = {}   # id -> (book, ref, [tokens])
freq = defaultdict(int)
for vid, book, ch, vs in db.execute(
        "SELECT id, book, chapter, verse FROM verses"):
    verses[vid] = (book, "%s %d:%d" % (book, ch, vs), [])
for vid, he in db.execute(
        "SELECT verse_id, he FROM words ORDER BY verse_id, idx"):
    tok = POINT.sub("", he or "").replace("/", "").replace("־", " ")
    for t in tok.split():
        if t:
            verses[vid][2].append(t)
            freq[t] += 1

def scan(n):
    grams = defaultdict(list)
    for vid, (book, ref, toks) in verses.items():
        seen = set()
        for i in range(len(toks) - n + 1):
            g = " ".join(toks[i:i + n])
            if g not in seen:          # count once per verse
                grams[g].append(vid)
                seen.add(g)
    pairs = {g: v for g, v in grams.items()
             if len(v) == 2 and verses[v[0]][0] != verses[v[1]][0]}
    by_vpair = defaultdict(list)
    for g, (a, b) in pairs.items():
        by_vpair[(a, b)].append(g)
    parallel = {vp for vp, gs in by_vpair.items() if len(gs) >= 3}
    gems, dupes = [], []
    for g, (a, b) in pairs.items():
        rarity = sum(freq[t] for t in g.split())
        row = (rarity, g, verses[a][1], verses[b][1])
        (dupes if (a, b) in parallel else gems).append(row)
    gems.sort()
    dupes.sort()
    return gems, dupes, len(grams)

for n in (3, 4):
    gems, dupes, total = scan(n)
    with open("%s/rare_pairs_%d.txt" % (SCRATCH, n), "w",
              encoding="utf-8") as f:
        for rarity, g, r1, r2 in gems:
            f.write("%6d | %s | %s | %s\n" % (rarity, g, r1, r2))
    print("%d-grams: %d distinct; exclusive cross-book pairs: %d "
          "(+%d in parallel blocks)" % (n, total, len(gems), len(dupes)))
