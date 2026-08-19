#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
"""
fetch_texts.py — step 2 of building your local source shelf: download the
TEXT of every oral-law source that the link index (shelf/links/, built by
fetch_links.py) anchors to your verse span. One small request per source
section — never whole books — into shelf/texts/.

By default this fetches the categories a derivation scan actually walks:
Talmud ("the learning"), Mishnah ("the repeated teaching"), Tosefta ("the
supplement"), Midrash ("exposition" — includes the legal expositions like
the Mekhilta on Exodus), Halakhah ("the law" — the codes), and Targum
("translation" — the early Aramaic renderings). Pass a comma-separated
category list as a third argument to widen or narrow, or 'all'.

POLITENESS CONTRACT (do not weaken it): sequential requests, DELAY seconds
apart, small verse spans per invocation. Existing files are skipped, so
runs are resumable.

Each saved file records the version titles Sefaria served — check the
version's license on its Sefaria page before REDISTRIBUTING any text;
reading, scanning, and citing are what this shelf is for. The shelf/
directory is a gitignored cache, never part of the repository record.

Usage:
  python3 tools/fetch_links.py Exodus "21:1-11"          # run step 1 first
  python3 tools/fetch_texts.py Exodus.21.1 Exodus.21.11
  python3 tools/fetch_texts.py Exodus.21.1 Exodus.21.11 Talmud,Midrash
"""
import hashlib
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINKS = ROOT / "shelf" / "links"
OUT = ROOT / "shelf" / "texts"
DELAY = 0.5          # seconds between requests — do not lower
FETCHED = time.strftime("%Y-%m-%d")
DEFAULT_CATEGORIES = {"Talmud", "Mishnah", "Tosefta", "Midrash",
                      "Halakhah", "Targum"}


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
            "he_license": d.get("heLicense"), "en_license": d.get("license"),
            "he": flatten(d.get("he")), "en": flatten(d.get("text"))}


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    lo, hi = sys.argv[1], sys.argv[2]
    cats = DEFAULT_CATEGORIES
    if len(sys.argv) > 3 and sys.argv[3] != "all":
        cats = set(sys.argv[3].split(","))
    book, ch, v1 = lo.rsplit(".", 2)
    _, _, v2 = hi.rsplit(".", 2)

    refs = set()
    missing = []
    for v in range(int(v1), int(v2) + 1):
        path = LINKS / ("%s_%s_%d.json" % (book.replace(" ", "_"), ch, v))
        if not path.exists():
            missing.append("%s %s:%d" % (book, ch, v))
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        for link in data["links"]:
            if sys.argv[3:4] == ["all"] or link.get("category") in cats:
                refs.add(link["ref"])
    if missing:
        print("no link index yet for: %s" % ", ".join(missing))
        print("run first:  python3 tools/fetch_links.py %s \"%s:%s-%s\""
              % (book, ch, v1, v2))
        sys.exit(1)

    OUT.mkdir(parents=True, exist_ok=True)
    done = skipped = failed = 0
    for ref in sorted(refs):
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
        path.write_text(json.dumps(data, ensure_ascii=False),
                        encoding="utf-8")
        done += 1
        if done % 40 == 0:
            print("... %d fetched" % done)
        time.sleep(DELAY)
    print("span %s-%s: %d refs · fetched %d · already had %d · failed %d -> %s"
          % (lo, hi, len(refs), done, skipped, failed, OUT))


if __name__ == "__main__":
    main()
