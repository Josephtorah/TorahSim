#!/usr/bin/env python3
"""
fetch_oral_texts.py — download the TEXT of every tier-1 source anchored to a
verse span (per Sefaria's link index in oral_links) into Data/sefaria_texts/.

One small request per SOURCE SECTION (never whole books), sequential, DELAY
apart — the owner's politeness contract. Resumable: existing files skipped.
Stores Hebrew + English (when Sefaria has it) + version titles + fetch date.

Usage:
  python3 fetch_oral_texts.py Gen.1.1 Gen.1.5      # day-1 span
"""

import hashlib
import json
import re
import sqlite3
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "shelf" / "sources" / "sefaria_texts"
DELAY = 0.5
FETCHED = time.strftime("%Y-%m-%d")


def safe_name(ref):
    slug = re.sub(r"[^A-Za-z0-9]+", "_", ref).strip("_")[:80]
    return "%s__%s.json" % (slug, hashlib.sha1(ref.encode()).hexdigest()[:8])


def flatten(x):
    if isinstance(x, str):
        return [x]
    out = []
    for y in (x or []):
        out.extend(flatten(y))
    return out


def fetch_ref(ref):
    url = ("https://www.sefaria.org/api/texts/%s?context=0&commentary=0"
           % urllib.parse.quote(ref))
    with urllib.request.urlopen(url, timeout=30) as r:
        d = json.load(r)
    return {"ref": ref, "fetched": FETCHED,
            "he_version": d.get("heVersionTitle"),
            "en_version": d.get("versionTitle"),
            "he": flatten(d.get("he")), "en": flatten(d.get("text"))}


def main():
    lo = sys.argv[1] if len(sys.argv) > 1 else "Gen.1.1"
    hi = sys.argv[2] if len(sys.argv) > 2 else "Gen.1.5"
    book, ch, v1 = lo.split(".")
    _, _, v2 = hi.split(".")
    span = ["%s.%s.%d" % (book, ch, v) for v in range(int(v1), int(v2) + 1)]

    cx = sqlite3.connect(ROOT / "data" / "derivation.sqlite")
    q = ",".join("?" * len(span))
    refs = sorted({r[0] for r in cx.execute(
        f"SELECT DISTINCT source_ref FROM oral_links WHERE tier=1 "
        f"AND anchor_osis IN ({q})", span)})

    OUT.mkdir(parents=True, exist_ok=True)
    done = skipped = failed = 0
    for ref in refs:
        path = OUT / safe_name(ref)
        if path.exists():
            skipped += 1
            continue
        try:
            data = fetch_ref(ref)
        except Exception as e:
            print("FAILED %s: %s" % (ref, e))
            failed += 1
            time.sleep(DELAY)
            continue
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        done += 1
        if done % 40 == 0:
            print("... %d fetched" % done)
        time.sleep(DELAY)
    print("span %s-%s: %d refs · fetched %d · already had %d · failed %d -> %s"
          % (lo, hi, len(refs), done, skipped, failed, OUT))


if __name__ == "__main__":
    main()
