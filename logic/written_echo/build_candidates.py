#!/usr/bin/env python3
"""
build_candidates.py — machine half of the Written<->Written echo graph.

Reads the oral_links table (already indexed from Data/sefaria_links) and promotes
category='Tanakh' rows into an echo_candidates table: curated verse<->verse links,
deduped per (anchor, target), with the link types that Sefaria's index gave them.

These are CANDIDATES only. A candidate becomes an edge of the graph solely by a
human verdict recorded in logic/written_echo/v1/edges.yaml (Pre-Code rule: the
machine surfaces, the register decides). The table is derived and rebuildable,
like every other DB table; nothing here is canonical.

Filter: a candidate target must be a bare Tanakh verse ref ("Jeremiah 4:23").
Sefaria's link index occasionally files commentary under the Tanakh category
("David Zvi Hoffmann on Exodus 3:1:4"); those are dropped and counted.
"""

import re
import sqlite3
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

TANAKH_BOOKS = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
    "Joshua", "Judges", "I Samuel", "II Samuel", "I Kings", "II Kings",
    "Isaiah", "Jeremiah", "Ezekiel", "Hosea", "Joel", "Amos", "Obadiah",
    "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai",
    "Zechariah", "Malachi",
    "Psalms", "Proverbs", "Job", "Song of Songs", "Ruth", "Lamentations",
    "Ecclesiastes", "Esther", "Daniel", "Ezra", "Nehemiah",
    "I Chronicles", "II Chronicles",
]
TORAH = set(TANAKH_BOOKS[:5])
REF_RX = re.compile(
    r"^(%s) \d+:\d+(-\d+(:\d+)?)?$" % "|".join(re.escape(b) for b in TANAKH_BOOKS))


def book_of(ref):
    return re.sub(r" \d+:.*$", "", ref)


def main():
    cx = sqlite3.connect(ROOT / "torah_grok.sqlite")
    rows = cx.execute(
        "SELECT anchor_osis, source_ref, link_type FROM oral_links "
        "WHERE category='Tanakh'").fetchall()

    pairs = defaultdict(set)
    dropped = []
    for anchor, target, ltype in rows:
        if REF_RX.match(target):
            pairs[(anchor, target)].add(ltype or "unspecified")
        else:
            dropped.append(target)

    cx.executescript("""
        DROP TABLE IF EXISTS echo_candidates;
        CREATE TABLE echo_candidates (
            anchor_osis TEXT, target_ref TEXT, target_book TEXT,
            in_torah INT, link_types TEXT, n_links INT,
            origin TEXT DEFAULT 'sefaria-link');
        CREATE INDEX ix_echo_anchor ON echo_candidates(anchor_osis);
    """)
    for (anchor, target), types in sorted(pairs.items()):
        book = book_of(target)
        cx.execute("INSERT INTO echo_candidates VALUES (?,?,?,?,?,?,?)",
                   (anchor, target, book, int(book in TORAH),
                    "+".join(sorted(types)), len(types), "sefaria-link"))
    cx.commit()

    n = len(pairs)
    n_out = sum(1 for (a, t) in pairs if book_of(t) not in TORAH)
    print("echo_candidates: %d distinct pairs (%d beyond Torah, %d within Torah)"
          % (n, n_out, n - n_out))
    print("dropped %d non-verse refs filed under Tanakh category:" % len(dropped))
    for t in sorted(set(dropped)):
        print("   ", t)
    print("\nCandidates beyond the Torah (the echo-graph frontier):")
    for (anchor, target), types in sorted(pairs.items()):
        if book_of(target) not in TORAH:
            print("  %-10s <-> %-22s [%s]" % (anchor, target, "+".join(sorted(types))))


if __name__ == "__main__":
    main()
