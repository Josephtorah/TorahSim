#!/usr/bin/env python3
"""
index_oral_links.py — Data/sefaria_links/*.json -> oral_links table.
Derived index like everything else in the DB; JSON files stay canonical.

Tier policy (PROPOSED, pending owner sign-off in the method charter):
  tier 1 = Midrash, Talmud, Mishnah, Targum, Halakhah  (Oral proper — must triage)
  tier 2 = Commentary, Quoting Commentary              (Rishonim/Acharonim)
  tier 3 = everything else (Kabbalah, Chasidut, Musar, Liturgy, ...)
"""

import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "shelf" / "sources" / "sefaria_links"
TIER1 = {"Midrash", "Talmud", "Mishnah", "Targum", "Halakhah"}
TIER2 = {"Commentary", "Quoting Commentary"}


def tier(cat):
    return 1 if cat in TIER1 else 2 if cat in TIER2 else 3


def main():
    cx = sqlite3.connect(ROOT / "data" / "derivation.sqlite")
    cx.executescript("""
        DROP TABLE IF EXISTS oral_links;
        CREATE TABLE oral_links (
            anchor_osis TEXT, source_ref TEXT, category TEXT,
            link_type TEXT, tier INT, fetched TEXT);
        CREATE INDEX ix_oral_links_anchor ON oral_links(anchor_osis);
    """)
    n_files = n_links = 0
    for path in sorted(SRC.glob("*.json")):
        d = json.loads(path.read_text(encoding="utf-8"))
        rows = [(d["anchor_osis"], x["ref"], x["category"], x.get("type"),
                 tier(x["category"]), d["fetched"]) for x in d["links"]]
        cx.executemany("INSERT INTO oral_links VALUES (?,?,?,?,?,?)", rows)
        n_files += 1
        n_links += len(rows)
    cx.commit()
    t1 = cx.execute("SELECT COUNT(*) FROM oral_links WHERE tier=1").fetchone()[0]
    print("indexed %d verses · %d links (%d tier-1) -> oral_links"
          % (n_files, n_links, t1))


if __name__ == "__main__":
    main()
