#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""index_sefaria_export.py — Data/sefaria_export/ -> torah_grok.sqlite
local search tables (oral-first era, owner order 2026-08-08).

Creates (drop-and-rebuild, derived index; the mirror JSON/CSV stays
canonical):
  export_texts  — FTS5: (work, ref, he, en) — every text segment of the
                  curated mirror, full-text searchable.
  export_links  — (anchor_book, anchor_chapter, anchor_verse, anchor_ref,
                  source_ref, source_work, category, shard) — every
                  Sefaria citation link whose anchor is a Torah verse.

Usage:
  python3 logic/solo_tools/index_sefaria_export.py            # build
  python3 logic/solo_tools/index_sefaria_export.py --span Gen 2:4 2:17
"""
import csv
import json
import re
import sqlite3
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
MIRROR = REPO / "Data/sefaria_export"
DB = REPO / "torah_grok.sqlite"

BOOKS = {"Genesis": "Gen", "Exodus": "Exod", "Leviticus": "Lev",
         "Numbers": "Num", "Deuteronomy": "Deut"}


def walk(node, path, out):
    """Recursively walk a merged.json text node; emit (ref_suffix, text)."""
    if isinstance(node, str):
        if node.strip():
            out.append((":".join(str(p) for p in path), node))
    elif isinstance(node, list):
        for i, child in enumerate(node, 1):
            walk(child, path + [i], out)
    elif isinstance(node, dict):
        for k, child in node.items():
            walk(child, path + [k], out)


def load_work(dirpath):
    segs = {}  # ref_suffix -> [he, en]
    for lang, fname in (("he", "he.json"), ("en", "en.json")):
        f = dirpath / fname
        if not f.exists():
            continue
        data = json.loads(f.read_text(encoding="utf-8"))
        title = data.get("title", dirpath.name)
        out = []
        walk(data.get("text", []), [], out)
        for suffix, txt in out:
            segs.setdefault(suffix, ["", ""])
            segs[suffix][0 if lang == "he" else 1] = txt
    return title, segs


def build(db):
    db.executescript("""
      DROP TABLE IF EXISTS export_texts;
      DROP TABLE IF EXISTS export_links;
      CREATE VIRTUAL TABLE export_texts USING fts5(work, ref, he, en);
      CREATE TABLE export_links(
        anchor_book TEXT, anchor_chapter INT, anchor_verse INT,
        anchor_ref TEXT, source_ref TEXT, source_work TEXT,
        category TEXT, shard TEXT);
    """)
    # texts
    nseg = 0
    for d in sorted(MIRROR.iterdir()):
        if not d.is_dir() or d.name == "links":
            continue
        title, segs = load_work(d)
        rows = [(title, "%s %s" % (title, suffix.replace(":", ":")), he, en)
                for suffix, (he, en) in sorted(segs.items())]
        db.executemany("INSERT INTO export_texts VALUES (?,?,?,?)", rows)
        nseg += len(rows)
        print("  %-55s %6d segments" % (title, len(rows)), flush=True)
    # links
    rx = re.compile(r"^(Genesis|Exodus|Leviticus|Numbers|Deuteronomy) "
                    r"(\d+):(\d+)")
    nlink = 0
    for shard in sorted((MIRROR / "links").glob("links*.csv")):
        batch = []
        with open(shard, encoding="utf-8", newline="") as fh:
            for row in csv.DictReader(fh):
                for a, b in ((1, 2), (2, 1)):
                    cit = row.get("Citation %d" % a) or ""
                    txt = row.get("Text %d" % a) or ""
                    if txt in BOOKS:
                        m = rx.match(cit)
                        if m:
                            batch.append((
                                BOOKS[m.group(1)], int(m.group(2)),
                                int(m.group(3)), cit,
                                row.get("Citation %d" % b) or "",
                                row.get("Text %d" % b) or "",
                                row.get("Category %d" % b) or "",
                                shard.name))
        db.executemany("INSERT INTO export_links VALUES (?,?,?,?,?,?,?,?)",
                       batch)
        nlink += len(batch)
        print("  %-20s %7d torah-anchored links" % (shard.name, len(batch)),
              flush=True)
    db.executescript("""
      CREATE INDEX idx_el_anchor ON export_links(
        anchor_book, anchor_chapter, anchor_verse);
      CREATE INDEX idx_el_work ON export_links(source_work);
    """)
    db.commit()
    print("TOTAL: %d text segments, %d torah-anchored links" % (nseg, nlink))


def span(db, book, v1, v2):
    c1, s1 = map(int, v1.split(":"))
    c2, s2 = map(int, v2.split(":"))
    rows = db.execute("""
      SELECT source_work, category, COUNT(*) FROM export_links
      WHERE anchor_book=? AND (anchor_chapter*1000+anchor_verse)
            BETWEEN ? AND ?
      GROUP BY source_work, category ORDER BY 3 DESC LIMIT 40""",
      (book, c1 * 1000 + s1, c2 * 1000 + s2)).fetchall()
    for w, cat, n in rows:
        print("%5d  %-14s %s" % (n, cat, w))


if __name__ == "__main__":
    db = sqlite3.connect(DB)
    if len(sys.argv) > 1 and sys.argv[1] == "--span":
        span(db, sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        build(db)
