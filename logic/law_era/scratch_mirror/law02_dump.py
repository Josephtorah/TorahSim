#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""law02_dump.py — batch reader for the gen_08 read-only check.
Dumps the NEXT unread chain-readable listings from law02_queue.json,
logging each to the scratchpad ledger (the ledger is the cursor).
He preferred (En only when He missing) to keep volume sane.

  law02_dump.py                # next batch, default cap
  law02_dump.py --work "Rashi" # only listings of works containing str
  law02_dump.py --cap 30000    # char cap per call
  law02_dump.py --status       # remaining counts per work, no dump
  law02_dump.py --tanakh       # dump the TANAKH-VERSE cross-refs
"""
import json
import re
import sqlite3
import sys
import time

SCRATCH = "<scratch>"
DB = SCRATCH + "/law02_texts.sqlite"  # indexed side DB (FTS5 workaround)
TANAKH_DB = "<repo-old>/elijah_docket/tanakh.sqlite"
QUEUE = SCRATCH + "/law02_queue.json"
LEDGER = "<repo-old>/logic/oral_audit/ledgers/Exod_21.jsonl"
SEEN = SCRATCH + "/law02_seen_segs.txt"

# reading order: verse-indexed chain digest first, then talmud/midrash,
# then the rest alphabetically
PRIORITY = ["Torah Temimah", "Mekhilta", "Sifra", "Sifrei", "Mishnah",
            "Tosefta", "Kiddushin", "Arakhin", "Yevamot", "Ketubot",
            "Bava Kamma", "Bava Metzia", "Bava Batra", "Gittin", "Sotah",
            "Makkot", "Sanhedrin", "Bekhorot", "Niddah", "Nedarim",
            "Shevuot", "Temurah", "Chagigah", "Rosh Hashanah",
            "Jerusalem Talmud", "Mishneh Torah", "Sefer HaMitzvot",
            "Sefer Mitzvot", "Sefer HaChinukh", "Onkelos", "Targum",
            "Rashi", "Midrash", "Shemot Rabbah", "Tanchuma",
            "Pirkei DeRabbi Eliezer", "Ibn Ezra", "Ramban", "Sforno",
            "Radak", "Chizkuni", "Tur", "Rabbeinu", "Bekhor Shor",
            "Kitzur", "Minchat Shai"]


def prio(work):
    for i, p in enumerate(PRIORITY):
        if p in work:
            return (i, work)
    return (len(PRIORITY), work)


def natkey(ref):
    return [int(t) if t.isdigit() else t
            for t in re.split(r"(\d+)", ref)]


def main():
    args = sys.argv[1:]
    cap = int(args[args.index("--cap") + 1]) if "--cap" in args else 32000
    want = args[args.index("--work") + 1] if "--work" in args else None

    q = json.load(open(QUEUE, encoding="utf-8"))
    done = set()
    try:
        for line in open(LEDGER, encoding="utf-8"):
            if line.strip():
                done.add(json.loads(line)["ref"])
    except IOError:
        pass
    seen = set()
    try:
        seen = set(open(SEEN, encoding="utf-8").read().split("\n"))
    except IOError:
        pass

    if "--status" in args:
        from collections import Counter
        rem = Counter()
        for sr, e in q.items():
            if e["klass"] == "READABLE" and sr not in done:
                rem[e["work"]] += 1
        tv = sum(1 for sr, e in q.items()
                 if e["klass"] == "TANAKH-VERSE" and sr not in done)
        print("REMAINING readable listings: %d (+%d tanakh)"
              % (sum(rem.values()), tv))
        for w in sorted(rem, key=prio):
            print("  %4d  %s" % (rem[w], w))
        return

    db = sqlite3.connect(DB)
    lf = open(LEDGER, "a", encoding="utf-8")
    sf = open(SEEN, "a", encoding="utf-8")

    if "--tanakh" in args:
        tdb = sqlite3.connect(TANAKH_DB)
        sys.path.insert(0, "<repo-old>/logic/solo_tools")
        from chain_scan import tanakh_ref
        n = 0
        for sr in sorted((s for s, e in q.items()
                          if e["klass"] == "TANAKH-VERSE" and s not in done),
                         key=natkey):
            b, c, v1, v2 = tanakh_ref(sr)
            print("=== %s ===" % sr)
            for v in range(v1, v2 + 1):
                he = " ".join(x[0].replace("/", "") for x in tdb.execute(
                    """SELECT w.he FROM words w JOIN verses vv
                       ON w.verse_id=vv.id WHERE vv.book=? AND vv.chapter=?
                       AND vv.verse=? ORDER BY w.idx""", (b, c, v)))
                print("%s %d:%d  %s" % (b, c, v, he))
            lf.write(json.dumps({"ref": sr, "work": q[sr]["work"],
                                 "at": time.strftime("%H:%M")}) + "\n")
            lf.flush()
            n += 1
        print("\n[tanakh dumped: %d]" % n)
        return

    todo = [(sr, e) for sr, e in q.items()
            if e["klass"] == "READABLE" and sr not in done
            and (want is None or want in e["work"])]
    todo.sort(key=lambda x: (prio(x[1]["work"]), natkey(x[0])))

    out_chars, n = 0, 0
    for sr, e in todo:
        if out_chars >= cap:
            break
        buf = ["=== %s ===" % sr]
        for seg in e["segs"]:
            he, en = db.execute(
                "SELECT he, en FROM t WHERE ref=?",
                (seg,)).fetchone()
            txt = he or en or ""
            if seg in seen:
                buf.append("--- %s [read earlier] ---" % seg)
                continue
            if seg != sr:
                buf.append("--- %s ---" % seg)
            txt = re.sub(r"<[^>]+>", "", txt)
            if "Minchat Shai" not in e["work"]:  # pointing IS content there
                txt = re.sub(r"[֑-ׇ]", "", txt)
            buf.append(txt)
            sf.write(seg + "\n")
            seen.add(seg)
        block = "\n".join(buf)
        print(block)
        out_chars += len(block)
        lf.write(json.dumps({"ref": sr, "work": e["work"],
                             "at": time.strftime("%H:%M")}) + "\n")
        lf.flush()
        n += 1
    sf.flush()
    left = len(todo) - n
    print("\n[batch: %d listings, %d chars; remaining%s: %d]"
          % (n, out_chars, (" in filter" if want else ""), left))


if __name__ == "__main__":
    main()
