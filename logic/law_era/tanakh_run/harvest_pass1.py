#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""harvest_pass1.py — TANAKH RUN pass-1 harvest, channels 1 + 3.

Channel 1: export_links Tanakh-category crossrefs anchored at Exod 21
           (the tradition's own verse-links).
Channel 3: lexical sweep of tanakh.sqlite on the statute's OWN lemmas —
           every lemma that occurs in Exod 21:1-37 + 22:1-3 (the tail
           border) with a whole-Tanakh frequency <= CAP is swept in
           full; plus curated surface-form patterns (the capital
           formula, the fourfold word).

Channel 2 (the scan digests' crossrefs) is curated by hand into the
scene catalog — see scene_catalog_*.json; this script covers the two
mechanical channels. Idempotent; writes JSON next to itself.

Experimental standing (like logic/gork/): not binding law, no gates.
"""
import json
import re
import sqlite3
import sys
from collections import Counter

HERE = "<repo-old>/logic/law_era/tanakh_run"
TANAKH = "<repo-old>/elijah_docket/tanakh.sqlite"
CAP = 90          # lemma sweep threshold (whole-Tanakh occurrences)

sys.path.insert(0, "<repo-old>/logic/solo_tools")
import chain_scan as cs  # noqa: E402  (links DB + tanakh_ref resolver)

STRIP = re.compile(r"[֑-ׇ]")   # pointing/accents
PREFIX = re.compile(r"^[^/]*/")


def base(lem):
    """'c/3588 a' -> '3588' (strip clitic prefixes + variant letters)."""
    if not lem:
        return None
    p = lem.split("/")[-1].strip().split(" ")[0]
    return p if p.isdigit() else None


# Hand gloss map for the operative swept lemmas (Hebrew never without
# English — display form is Hebrew script, gloss inline at use-site).
GLOSS = {
    "7794": ("שור", "ox"), "7716": ("שה", "lamb/sheep"),
    "5055": ("נגח", "gore (verb)"), "5056": ("נגח", "goring-prone"),
    "953": ("בור", "pit/cistern"), "1589": ("גנב", "steal (verb)"),
    "1590": ("גנב", "thief"), "1591": ("גנבה", "theft/stolen thing"),
    "4376": ("מכר", "sell"), "4465": ("ממכר", "sale"),
    "519": ("אמה", "maidservant"), "2670": ("חפשי", "free(d)"),
    "5619": ("סקל", "stone (verb)"), "5358": ("נקם", "avenge"),
    "5359": ("נקם", "vengeance"), "3724": ("כפר", "ransom-price"),
    "6306": ("פדין", "redemption-price"), "6299": ("פדה", "redeem"),
    "3259": ("יעד", "designate/appoint"), "2600": ("חנם", "gratis/for nothing"),
    "1610": ("גף", "body/alone"), "8127": ("שן", "tooth"),
    "4290": ("מחתרת", "breaking-in/tunnel"), "155": ("אגרף", "fist"),
    "2030": ("הרה", "pregnant"), "6414": ("פלילים", "assessors/judges"),
    "6415": ("פלילה", "judgment"), "2873": ("טבח", "slaughter (verb)"),
    "2874": ("טבח", "slaughter (noun)"), "4836": ("מרצע", "awl"),
    "7527": ("רצע", "bore/pierce"), "8628": ("תקע", "thrust/blow"),
    "2490": ("חלל", "profane/slain"), "6083": ("עפר", "dust"),
}

# Surface-form patterns (consonantal, prefix-tolerant where noted)
SURFACE = [
    ("מות יומת", "the capital formula: he shall surely be put to death"),
    ("ארבעתים", "fourfold (2 Sam 12:6's word)"),
    ("שבעתים", "sevenfold (Prov 6:31 family)"),
    ("אין לו דמים", "he has no blood(-claim) — burglar clause idiom"),
    ("דמיו בו", "his blood is upon him"),
]


def main():
    db = sqlite3.connect(TANAKH)

    # ---- verse text cache (consonantal) --------------------------------
    verses = {}   # (book, ch, v) -> consonantal text
    order = {}    # (book, ch, v) -> verse rowid (canonical file order)
    for vid, b, c, v in db.execute(
            "SELECT id, book, chapter, verse FROM verses"):
        order[(b, c, v)] = vid
    for b, c, v, he in db.execute(
            """SELECT vv.book, vv.chapter, vv.verse,
                      GROUP_CONCAT(w.he, ' ')
               FROM words w JOIN verses vv ON w.verse_id = vv.id
               GROUP BY vv.id"""):
        verses[(b, c, v)] = STRIP.sub("", (he or "").replace("/", ""))

    # ---- statute lemma inventory ----------------------------------------
    in_statute = Counter()
    for (lem,) in db.execute(
            """SELECT w.lemma FROM words w JOIN verses v ON w.verse_id=v.id
               WHERE v.book='Exod' AND (v.chapter=21
                     OR (v.chapter=22 AND v.verse<=3))"""):
        bl = base(lem)
        if bl:
            in_statute[bl] += 1

    total = Counter()
    occ = {}     # lemma -> [(book, ch, v, word)]
    for b, c, v, he, lem in db.execute(
            """SELECT vv.book, vv.chapter, vv.verse, w.he, w.lemma
               FROM words w JOIN verses vv ON w.verse_id=vv.id"""):
        bl = base(lem)
        if bl in in_statute:
            total[bl] += 1
            occ.setdefault(bl, []).append(
                (b, c, v, STRIP.sub("", he.replace("/", ""))))

    extra = {"1590", "1591", "6299", "5359", "2873", "2874",
             "4836", "6415", "4465"}   # operative kin not in the span
    for bl in sorted(extra):
        if bl in occ:
            continue
        for b, c, v, he, lem in db.execute(
                """SELECT vv.book, vv.chapter, vv.verse, w.he, w.lemma
                   FROM words w JOIN verses vv ON w.verse_id=vv.id"""):
            if base(lem) == bl:
                total[bl] += 1
                occ.setdefault(bl, []).append(
                    (b, c, v, STRIP.sub("", he.replace("/", ""))))

    sweep = {}
    for bl, n in sorted(total.items(), key=lambda kv: kv[1]):
        if bl not in GLOSS:
            continue              # function words / non-operative
        if n > CAP and bl not in extra:
            continue
        heb, gloss = GLOSS[bl]
        hits = [{"ref": "%s.%d.%d" % (b, c, v), "word": w,
                 "in_statute": (b == "Exod" and (c == 21 or (c == 22 and v <= 3)))}
                for b, c, v, w in sorted(occ.get(bl, []),
                                         key=lambda t: order[(t[0], t[1], t[2])])]
        sweep[bl] = {"hebrew": heb, "gloss": gloss, "total": n,
                     "hits": hits}

    # ---- surface patterns ------------------------------------------------
    surface = {}
    for pat, note in SURFACE:
        hits = []
        for (b, c, v), txt in verses.items():
            if pat in txt:
                hits.append({"ref": "%s.%d.%d" % (b, c, v)})
        hits.sort(key=lambda h: order[tuple(
            (h["ref"].split(".")[0], int(h["ref"].split(".")[1]),
             int(h["ref"].split(".")[2])))])
        surface[pat] = {"note": note, "hits": hits}

    with open(HERE + "/harvest_ch3_lexical.json", "w", encoding="utf-8") as f:
        json.dump({"cap": CAP, "lemmas": sweep, "surface": surface}, f,
                  ensure_ascii=False, indent=1)

    print("CH3 lemma sweep (statute-derived, total <= %d):" % CAP)
    for bl, e in sorted(sweep.items(), key=lambda kv: kv[1]["total"]):
        out = sum(1 for h in e["hits"] if not h["in_statute"])
        print("  %6s %-8s %-28s total %3d, outside statute %3d"
              % (bl, e["hebrew"], "(" + e["gloss"] + ")", e["total"], out))
    for pat, e in surface.items():
        print("  surface %-14s hits %2d  (%s)"
              % ("'" + pat + "'", len(e["hits"]), e["note"]))

    # ---- channel 1: export_links Tanakh crossrefs ------------------------
    ldb = sqlite3.connect(str(cs.DB))
    rows = ldb.execute(
        """SELECT DISTINCT anchor_verse, source_ref, source_work
           FROM export_links WHERE anchor_book='Exod' AND anchor_chapter=21
           AND category='Tanakh'""").fetchall()
    ch1 = []
    for av, sr, sw in sorted(rows):
        t = cs.tanakh_ref(sr)      # category 'Tanakh' includes commentaries
        if not t:                  # ON Tanakh — keep only true verse refs
            continue
        ch1.append({"anchor": "Exod.21.%d" % av, "source_ref": sr,
                    "work": sw, "resolved": "%s.%d.%d-%d" % t})
    with open(HERE + "/harvest_ch1_links.json", "w", encoding="utf-8") as f:
        json.dump(ch1, f, ensure_ascii=False, indent=1)
    print("\nCH1 export_links true VERSE crossrefs anchored Exod 21: %d"
          % len(ch1))
    for e in ch1:
        print("  21:%-2s <- %s" % (e["anchor"].split(".")[2], e["source_ref"]))


if __name__ == "__main__":
    main()
