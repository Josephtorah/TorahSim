#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""chain_scan.py — the FULL-INVERSION oral scanner (Full Oral Torah Law,
owner 2026-08-10). For a Torah span: invert export_links, classify every
linked listing under chain_scope.yaml, and dump chain-readable segments
for reading. Every dumped listing is logged to a DISK ledger
INCREMENTALLY (compaction/crash survival — scan progress never lives
only in conversation context).

Usage (from repo root):
  chain_scan.py Exod 21            # whole chapter; --to 23 for a range
  chain_scan.py Exod 21 --list    # classification summary only, no dump
  chain_scan.py Exod 21 --works   # per-work listing counts
  chain_scan.py Exod 21 --work "Bava Kamma"        # dump one work
  chain_scan.py Exod 21 --tanakh                   # dump verse cross-refs
Ledger: logic/oral_audit/ledgers/<book>_<c1>[_<c2>].jsonl (JSONL,
append-only; the gate oral_coverage.py checks it for completeness).

Classification (see chain_scope.yaml — NO scope change without owner
ruling): READABLE (in export_texts -> must read), TANAKH-VERSE (Bible
cross-ref -> resolved via elijah_docket/tanakh.sqlite), OUT (ruled out,
ruling named), UNRULED (surfaced, blocks the coverage gate).
"""
import json
import re
import sqlite3
import sys
import time
from bisect import bisect_left
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DB = REPO / "derivation.sqlite"
TANAKH_DB = REPO / "elijah_docket/tanakh.sqlite"
SCOPE = REPO / "logic/solo_tools/chain_scope.yaml"
LEDGER_DIR = REPO / "logic/oral_audit/ledgers"

BIBLE = {  # Sefaria English name -> tanakh.sqlite book code
 "Genesis": "Gen", "Exodus": "Exod", "Leviticus": "Lev", "Numbers": "Num",
 "Deuteronomy": "Deut", "Joshua": "Josh", "Judges": "Judg",
 "I Samuel": "1Sam", "II Samuel": "2Sam", "I Kings": "1Kgs",
 "II Kings": "2Kgs", "Isaiah": "Isa", "Jeremiah": "Jer", "Ezekiel": "Ezek",
 "Hosea": "Hos", "Joel": "Joel", "Amos": "Amos", "Obadiah": "Obad",
 "Jonah": "Jonah", "Micah": "Mic", "Nahum": "Nah", "Habakkuk": "Hab",
 "Zephaniah": "Zeph", "Haggai": "Hag", "Zechariah": "Zech",
 "Malachi": "Mal", "Psalms": "Ps", "Proverbs": "Prov", "Job": "Job",
 "Song of Songs": "Song", "Ruth": "Ruth", "Lamentations": "Lam",
 "Ecclesiastes": "Eccl", "Esther": "Esth", "Daniel": "Dan",
 "Ezra": "Ezra", "Nehemiah": "Neh", "I Chronicles": "1Chr",
 "II Chronicles": "2Chr"}


def load_scope():
    """Minimal YAML read of chain_scope.yaml (flat, known shape)."""
    cats, works = {}, []
    txt = SCOPE.read_text(encoding="utf-8")
    for m in re.finditer(r"\{category:\s*([^,}]+),\s*ruling:\s*([^}]+)\}",
                         txt, re.S):
        cats[m.group(1).strip()] = " ".join(m.group(2).split())
    for m in re.finditer(r"\{pattern:\s*(['\"])(.+?)\1,\s*ruling:\s*([^}]+)\}",
                         txt, re.S):
        works.append((re.compile(m.group(2)), " ".join(m.group(3).split())))
    return cats, works


class Shelf(object):
    """export_texts refs, with prefix/range resolution."""
    def __init__(self, db):
        self.refs = set()
        self.by_work = {}
        for w, r in db.execute("SELECT work, ref FROM export_texts"):
            self.refs.add(r)
            self.by_work.setdefault(w, []).append(r)
        for w in self.by_work:
            self.by_work[w].sort()
        self.works = set(self.by_work)

    def prefix(self, p):
        hits, seen = [], set()
        for w, lst in self.by_work.items():
            if not p.startswith(w):
                continue
            i = bisect_left(lst, p)
            while i < len(lst) and lst[i].startswith(p):
                if lst[i] not in seen:
                    hits.append(lst[i]); seen.add(lst[i])
                i += 1
        return hits

    def resolve(self, ref):
        """Concrete local segment refs for a citation (exact, seg-range,
        daf-range, or coarse prefix). Empty list = nothing local."""
        if ref in self.refs:
            return [ref]
        m = re.match(r"^(.*[ :])(\d+)-(\d+)$", ref)  # trailing seg/verse range
        if m:
            out = []
            for n in range(int(m.group(2)), int(m.group(3)) + 1):
                out += self.resolve(m.group(1) + str(n))
            if out:
                return out
        m = re.match(r"^(.+ )(\d+)([ab])-(\d+)([ab])$", ref)  # daf range
        if m:
            base, d1, a1, d2, a2 = m.groups()
            sides, out = ["a", "b"], []
            cur = (int(d1), sides.index(a1))
            end = (int(d2), sides.index(a2))
            while cur <= end:
                out += self.prefix("%s%d%s:" % (base, cur[0], sides[cur[1]]))
                cur = (cur[0] + (cur[1] == 1), 1 - cur[1]) if cur[1] == 0 \
                    else (cur[0] + 1, 0)
            if out:
                return out
        return self.prefix(ref if ref.endswith(":") else ref + ":")


def tanakh_ref(ref):
    """(book_code, chapter, v1, v2) for a Bible citation, else None."""
    m = re.match(r"^(%s) (\d+):(\d+)(?:-(?:(\d+):)?(\d+))?$"
                 % "|".join(re.escape(b) for b in BIBLE), ref)
    if not m:
        return None
    b, c, v1 = BIBLE[m.group(1)], int(m.group(2)), int(m.group(3))
    v2 = int(m.group(5)) if m.group(5) and not m.group(4) else v1
    return (b, c, v1, v2)  # cross-chapter ranges: first chapter only


def classify(db, book, c1, c2):
    """-> dict of source_ref -> (work, category, klass, detail)."""
    cats, works_out = load_scope()
    shelf = Shelf(db)
    out = {}
    for sr, sw, cat in db.execute(
            """SELECT DISTINCT source_ref, source_work, category
               FROM export_links WHERE anchor_book=?
               AND anchor_chapter BETWEEN ? AND ?""", (book, c1, c2)):
        if sr in out:
            continue
        if cat == "Tanakh" and tanakh_ref(sr):
            out[sr] = (sw, cat, "TANAKH-VERSE", "")
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
            out[sr] = (sw, cat, "READABLE", local)
        elif ruled:
            out[sr] = (sw, cat, "OUT", ruled)
        else:
            out[sr] = (sw, cat, "UNRULED", "")
    return out, shelf


def ledger_path(book, c1, c2):
    LEDGER_DIR.mkdir(parents=True, exist_ok=True)
    tag = "%s_%02d" % (book, c1) if c1 == c2 else "%s_%02d_%02d" % (book, c1, c2)
    return LEDGER_DIR / ("%s.jsonl" % tag)


def log_read(fh, ref, work):
    fh.write(json.dumps({"ref": ref, "work": work,
                         "at": time.strftime("%Y-%m-%d %H:%M")}) + "\n")
    fh.flush()


def main():
    args = sys.argv[1:]
    book, c1 = args[0], int(args[1])
    c2 = int(args[args.index("--to") + 1]) if "--to" in args else c1
    db = sqlite3.connect(DB)
    cls, shelf = classify(db, book, c1, c2)

    if "--list" in args or "--works" in args:
        from collections import Counter
        kc = Counter(k for _, _, k, _ in cls.values())
        print("SPAN %s %d-%d: %d distinct listings | %s"
              % (book, c1, c2, len(cls),
                 " ".join("%s %d" % kv for kv in sorted(kc.items()))))
        if "--works" in args:
            wc = Counter()
            for sr, (sw, cat, k, d) in cls.items():
                if k == "READABLE":
                    wc[sw] += 1
            for w, n in wc.most_common():
                print("  %4d  %s" % (n, w))
        for sr, (sw, cat, k, d) in sorted(cls.items()):
            if k == "UNRULED":
                print("  UNRULED: %-60s [%s / %s]" % (sr, sw, cat))
        return

    want_work = args[args.index("--work") + 1] if "--work" in args else None
    lp = ledger_path(book, c1, c2)
    done = set()
    if lp.exists():
        for line in lp.read_text(encoding="utf-8").splitlines():
            if line.strip():
                done.add(json.loads(line)["ref"])
    fh = open(lp, "a", encoding="utf-8")

    if "--tanakh" in args:  # dump Bible cross-refs via the Tanakh DB
        tdb = sqlite3.connect(TANAKH_DB)
        for sr, (sw, cat, k, d) in sorted(cls.items()):
            if k != "TANAKH-VERSE" or sr in done:
                continue
            b, c, v1, v2 = tanakh_ref(sr)
            print("=== %s ===" % sr)
            for v in range(v1, v2 + 1):
                he = " ".join(x[0].replace("/", "") for x in tdb.execute(
                    """SELECT w.he_plain FROM words w JOIN verses vv
                       ON w.verse_id=vv.id WHERE vv.book=? AND vv.chapter=?
                       AND vv.verse=? ORDER BY w.idx""", (b, c, v)))
                print("%s %d:%d  %s" % (b, c, v, he))
            log_read(fh, sr, sw)
        return

    n = 0
    for sr, (sw, cat, k, d) in sorted(cls.items()):
        if k != "READABLE" or sr in done:
            continue
        if want_work and sw != want_work:
            continue
        print("=== %s ===" % sr)
        for seg in d:
            he, en = db.execute(
                "SELECT he, en FROM export_texts WHERE ref=?", (seg,)).fetchone()
            if seg != sr:
                print("--- %s ---" % seg)
            if he:
                print(he)
            if en:
                print("EN: %s" % en)
        log_read(fh, sr, sw)
        n += 1
    print("\n[dumped %d listings -> %s]" % (n, lp))


if __name__ == "__main__":
    main()
