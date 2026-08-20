#!/usr/bin/env python3
"""
fetch_oral_links.py — pull Sefaria's link index (every cataloged source
anchored to a verse) into Data/sefaria_links/, one trimmed JSON per verse.

Politeness contract (owner-ordered): sequential requests only, DELAY seconds
apart, small ranges per invocation — never a whole book in one hammering run.
Already-fetched verses are skipped, so runs are resumable and re-runnable.

Link metadata (refs + categories) is Sefaria's curated index; stored trimmed
(ref, category, type) with fetch date. Text is NOT fetched here.

Usage:
  python3 fetch_oral_links.py Gen "1:1-31,2:1-3"     # creation week (default)
  python3 fetch_oral_links.py Lev "1:1-9"
"""

import json
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "shelf" / "sources" / "sefaria_links"
BOOK_API = {"Gen": "Genesis", "Exod": "Exodus", "Lev": "Leviticus",
            "Num": "Numbers", "Deut": "Deuteronomy"}
DELAY = 0.5          # seconds between requests — do not lower
FETCHED = time.strftime("%Y-%m-%d")


def parse_ranges(spec):
    out = []
    for part in spec.split(","):
        ch, vv = part.strip().split(":")
        lo, _, hi = vv.partition("-")
        out.extend((int(ch), v) for v in range(int(lo), int(hi or lo) + 1))
    return out


def fetch_verse(book, ch, v):
    ref = "%s.%d.%d" % (BOOK_API[book], ch, v)
    url = "https://www.sefaria.org/api/links/%s?with_text=0" % ref
    with urllib.request.urlopen(url, timeout=30) as r:
        raw = json.load(r)
    links = [{"ref": x.get("ref"), "category": x.get("category"),
              "type": x.get("type")} for x in raw if x.get("ref")]
    return {"anchor_osis": "%s.%d.%d" % (book, ch, v), "api_ref": ref,
            "fetched": FETCHED, "n": len(links), "links": links}


def main():
    book = sys.argv[1] if len(sys.argv) > 1 else "Gen"
    ranges = sys.argv[2] if len(sys.argv) > 2 else "1:1-31,2:1-3"
    OUT.mkdir(parents=True, exist_ok=True)
    targets = parse_ranges(ranges)
    done = skipped = 0
    for ch, v in targets:
        path = OUT / ("%s_%d_%d.json" % (book, ch, v))
        if path.exists():
            skipped += 1
            continue
        data = fetch_verse(book, ch, v)
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        done += 1
        print("%s %d:%d — %d links" % (book, ch, v, data["n"]))
        time.sleep(DELAY)
    print("fetched %d verses (%d already present) -> %s" % (done, skipped, OUT))


if __name__ == "__main__":
    main()
