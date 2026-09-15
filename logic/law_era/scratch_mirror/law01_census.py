#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LAW ERA block 1 census — Exod 21:1-11 (slave-term laws), FTS5-safe.
Same design as gen08_census2.py: single pass over export_texts, classify
per chain_scope, second pass fills an indexed side DB.
Scratchpad-only — no repo writes."""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import json
import sqlite3
import sys
from collections import Counter

sys.path.insert(0, (_ROOT + "/logic/solo_tools"))
import chain_scan as cs

SCRATCH = "<scratch>"

db = sqlite3.connect(str(cs.DB))
cats, works_out = cs.load_scope()

# ---- stage 1: one full pass; shelf structures built inline ----------
refs = set()
by_work = {}
for w, r in db.execute("SELECT work, ref FROM export_texts"):
    refs.add(r)
    by_work.setdefault(w, []).append(r)
for w in by_work:
    by_work[w].sort()
print("shelf: %d refs, %d works" % (len(refs), len(by_work)), flush=True)


class Shelf2(cs.Shelf):
    def __init__(self):  # reuse resolve()/prefix() on prebuilt data
        self.refs = refs
        self.by_work = by_work
        self.works = set(by_work)


shelf = Shelf2()

# ---- stage 2: classify --------------------------------------------
rows = db.execute(
    """SELECT DISTINCT source_ref, source_work, category
       FROM export_links WHERE anchor_book='Exod' AND anchor_chapter=21
       AND anchor_verse BETWEEN 1 AND 11""").fetchall()
print("links: %d distinct source rows" % len(rows), flush=True)

cls = {}
for sr, sw, cat in rows:
    if sr in cls:
        continue
    if cat == "Tanakh" and cs.tanakh_ref(sr):
        cls[sr] = (sw, cat, "TANAKH-VERSE", None)
        continue
    ruled = None
    for pat, ruling in works_out:
        if pat.search(sw):
            ruled = ruling
            break
    if ruled is None and cat in cats:
        ruled = cats[cat]
    local = shelf.resolve(sr)
    if local:
        cls[sr] = (sw, cat, "READABLE", local)
    elif ruled:
        cls[sr] = (sw, cat, "OUT", ruled)
    else:
        cls[sr] = (sw, cat, "UNRULED", None)

kc = Counter(k for _, _, k, _ in cls.values())
print("Exod 21:1-11: %d distinct listings | %s" % (
    len(cls), " ".join("%s %d" % kv for kv in sorted(kc.items()))),
    flush=True)

# ---- stage 3: needed segments -> side DB (second single pass) ------
need = set()
for sr, (sw, cat, k, d) in cls.items():
    if k == "READABLE":
        need.update(d)
print("needed segments: %d" % len(need), flush=True)

side = sqlite3.connect(SCRATCH + "/law01_texts.sqlite")
side.execute("DROP TABLE IF EXISTS t")
side.execute("CREATE TABLE t (ref TEXT PRIMARY KEY, work TEXT, "
             "he TEXT, en TEXT)")
got = 0
for w, r, he, en in db.execute("SELECT work, ref, he, en FROM export_texts"):
    if r in need:
        side.execute("INSERT OR IGNORE INTO t VALUES (?,?,?,?)",
                     (r, w, he, en))
        got += 1
side.commit()
tot = side.execute("SELECT SUM(LENGTH(COALESCE(he,''))), "
                   "SUM(LENGTH(COALESCE(en,''))) FROM t").fetchone()
print("side DB: %d segs | He %d ch | En %d ch" % (got, tot[0], tot[1]),
      flush=True)

work_stat = {}
seen = set()
for sr, (sw, cat, k, d) in cls.items():
    if k != "READABLE":
        continue
    st = work_stat.setdefault(sw, [0, 0, 0])
    st[0] += 1
    for seg in d:
        if seg in seen:
            continue
        seen.add(seg)
        (hl,) = side.execute(
            "SELECT LENGTH(COALESCE(he,'')) FROM t WHERE ref=?",
            (seg,)).fetchone()
        st[1] += 1
        st[2] += hl
print("\nTop works by unique He volume:", flush=True)
for w, (l, s, c) in sorted(work_stat.items(), key=lambda kv: -kv[1][2])[:45]:
    print("%9d ch %5d listings %5d segs  %s" % (c, l, s, w))

queue = {sr: {"work": sw, "cat": cat, "klass": k, "segs": d}
         for sr, (sw, cat, k, d) in cls.items()}
with open(SCRATCH + "/law01_queue.json", "w", encoding="utf-8") as f:
    json.dump(queue, f, ensure_ascii=False)
print("\nqueue written", flush=True)

print("\nUNRULED:")
for sr, (sw, cat, k, d) in sorted(cls.items()):
    if k == "UNRULED":
        print("   %-55s [%s / %s]" % (sr, sw, cat))
