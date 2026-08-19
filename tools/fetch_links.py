#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
"""
fetch_links.py — step 1 of building your local source shelf: pull Sefaria's
link index (every cataloged oral-law source anchored to a verse) into
shelf/links/, one trimmed JSON file per verse.

Sefaria (sefaria.org) is the open digital library of the tradition's works.
This fetcher asks it, verse by verse, "which sources speak about this
verse?" — the answer is the raw material of a full-inversion scan.

POLITENESS CONTRACT (do not weaken it): sequential requests only, DELAY
seconds apart, small ranges per invocation — never a whole book in one run.
Already-fetched verses are skipped, so runs are resumable and re-runnable.

The shelf/ directory is a CACHE, not a record — it is gitignored. The
permanent record of a derivation is its scan ledger, claims, and citations.

Usage:
  python3 tools/fetch_links.py Exodus "21:1-11"        # one law block
  python3 tools/fetch_links.py Genesis "1:1-31,2:1-3"  # the creation week
"""
import json
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "shelf" / "links"
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
    ref = "%s.%d.%d" % (book.replace(" ", "_"), ch, v)
    url = "https://www.sefaria.org/api/links/%s?with_text=0" % ref
    with urllib.request.urlopen(url, timeout=30) as r:
        raw = json.load(r)
    links = [{"ref": x.get("ref"), "category": x.get("category"),
              "type": x.get("type")} for x in raw if x.get("ref")]
    return {"anchor": "%s.%d.%d" % (book, ch, v), "api_ref": ref,
            "fetched": FETCHED, "n": len(links), "links": links}


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    book, ranges = sys.argv[1], sys.argv[2]
    OUT.mkdir(parents=True, exist_ok=True)
    done = skipped = 0
    for ch, v in parse_ranges(ranges):
        path = OUT / ("%s_%d_%d.json" % (book.replace(" ", "_"), ch, v))
        if path.exists():
            skipped += 1
            continue
        data = fetch_verse(book, ch, v)
        path.write_text(json.dumps(data, ensure_ascii=False),
                        encoding="utf-8")
        done += 1
        print("%s %d:%d — %d links" % (book, ch, v, data["n"]))
        time.sleep(DELAY)
    print("fetched %d verses (%d already present) -> %s"
          % (done, skipped, OUT))


if __name__ == "__main__":
    main()
