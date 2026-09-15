#!/usr/bin/env python3
"""Re-rank on ALIGNED chapters only.

Sefaria's Onkelos and our Hebrew divide some chapters differently (the
Decalogue above all). Pairing verse N to verse N there compares unrelated
sentences and manufactures expansion. Any chapter whose verse counts disagree
is excluded and named.
"""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import json, re, sqlite3
from statistics import mean

REPO = _ROOT
BOOKS = {"Gen": "Onkelos_Genesis", "Exod": "Onkelos_Exodus",
         "Lev": "Onkelos_Leviticus", "Num": "Onkelos_Numbers",
         "Deut": "Onkelos_Deuteronomy"}
NIQQUD = re.compile(r"[֑-ׇ]")

c = sqlite3.connect(f"{REPO}/torah_grok.SNAPSHOT-main-51801ca.sqlite")
hcount, hwords = {}, {}
for osis, he in c.execute("""select v.osis_id, w.he from words w
        join verses v on v.id=w.verse_id order by v.id, w.idx"""):
    if not NIQQUD.search(he or ""):
        continue
    hwords[osis] = hwords.get(osis, 0) + 1
for b, ch, n in c.execute("select book, chapter, count(*) from verses group by book, chapter"):
    hcount[(b, ch)] = n

aligned, skipped, exp = {}, [], {}
for b, d in BOOKS.items():
    text = json.load(open(f"{REPO}/Data/sefaria_export/{d}/he.json"))["text"]
    for ci, ch in enumerate(text, 1):
        vv = [" ".join(v) if isinstance(v, list) else v for v in ch]
        vv = [v for v in vv if v and v.strip()]
        if len(vv) != hcount.get((b, ci)):
            skipped.append((b, ci, hcount.get((b, ci)), len(vv)))
            continue
        rates = []
        for vi, v in enumerate(vv, 1):
            ref = f"{b}.{ci}.{vi}"
            if hwords.get(ref):
                rates.append(len(v.split()) / hwords[ref])
                exp[ref] = rates[-1]
        aligned[(b, ci)] = rates

print(f"ALIGNMENT AUDIT over {len(aligned) + len(skipped)} Torah chapters")
print(f"  aligned  : {len(aligned)}")
print(f"  EXCLUDED : {len(skipped)} (verse counts disagree — index pairing "
      f"would compare unrelated sentences)")
for b, ci, h, o in skipped:
    print(f"      {b} {ci}: Hebrew {h} vv vs Onkelos {o} vv")

rank = sorted(((mean(v), b, ci, len(v)) for (b, ci), v in aligned.items()), reverse=True)
WHAT = {("Gen", 49): "Jacob's blessings", ("Deut", 33): "the Blessing of Moses",
        ("Deut", 32): "the Song of Moses", ("Num", 24): "Balaam, oracles 3-7",
        ("Num", 23): "Balaam, oracles 1-2", ("Exod", 15): "the Song of the Sea"}
print(f"\nTOP 12 ALIGNED CHAPTERS BY ONKELOS EXPANSION (of {len(rank)})")
print(f"{'#':>3} {'chapter':>9} {'vv':>4} {'expansion':>10}   poem?")
for i, (e, b, ci, n) in enumerate(rank[:12], 1):
    tag = "POEM — " + WHAT[(b, ci)] if (b, ci) in WHAT else ""
    print(f"{i:>3} {b + ' ' + str(ci):>9} {n:>4} {e:>10.3f}   {tag}")
pr = {(b, ci): i for i, (e, b, ci, n) in enumerate(rank, 1)}
print(f"\nEVERY TORAH POEM'S RANK among the {len(rank)} aligned chapters:")
for k, name in sorted(WHAT.items(), key=lambda kv: pr[kv[0]]):
    print(f"   rank {pr[k]:>3} of {len(rank)}   {k[0]} {k[1]:<3} {name}")
allm = mean(e for e, b, ci, n in rank)
print(f"\n   mean over all aligned chapters: {allm:.3f}")
print(f"   ALL SIX POEMS RANK IN THE TOP {max(pr[k] for k in WHAT)} "
      f"— none is below it.")
