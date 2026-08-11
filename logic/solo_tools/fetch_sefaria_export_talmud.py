#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fetch_sefaria_export_talmud.py — TALMUD-SHELF extension of the curated
Sefaria-Export mirror (owner order 2026-08-10: "fetch it" — the Talmud
was absent from the 2026-08-08 shelf; oral scans could NAME Bavli loci
via export_links but never READ them locally).

Adds to Data/sefaria_export/:
  - Talmud Bavli — every tractate under the six Seder dirs (text only;
    no Steinsaltz / Rishonim / Acharonim commentary layers)
  - Mishnah — all tractates (dirs "Mishnah X" + "Pirkei Avot")
  - Tosefta — both editions (Vilna, cited as "Tosefta X"; Lieberman,
    cited as "Tosefta X (Lieberman)")

Same mechanics as fetch_sefaria_export.py (bucket LISTING discovery, He+En
merged.json, resumable, 0.4s pacing) — but APPENDS a dated section to
MIRROR_MANIFEST.txt instead of rewriting the 2026-08-08 build record.

Usage: python3 logic/solo_tools/fetch_sefaria_export_talmud.py
"""
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

BUCKET = "https://storage.googleapis.com/sefaria-export"
REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "Data/sefaria_export"
DELAY = 0.4

WANT = [
    ("json/Talmud/Bavli/Seder Zeraim/", r"."),
    ("json/Talmud/Bavli/Seder Moed/", r"."),
    ("json/Talmud/Bavli/Seder Nashim/", r"."),
    ("json/Talmud/Bavli/Seder Nezikin/", r"."),
    ("json/Talmud/Bavli/Seder Kodashim/", r"."),
    ("json/Talmud/Bavli/Seder Tahorot/", r"."),
    ("json/Mishnah/Seder Zeraim/", r"^(Mishnah .+|Pirkei Avot)$"),
    ("json/Mishnah/Seder Moed/", r"^(Mishnah .+|Pirkei Avot)$"),
    ("json/Mishnah/Seder Nashim/", r"^(Mishnah .+|Pirkei Avot)$"),
    ("json/Mishnah/Seder Nezikin/", r"^(Mishnah .+|Pirkei Avot)$"),
    ("json/Mishnah/Seder Kodashim/", r"^(Mishnah .+|Pirkei Avot)$"),
    ("json/Mishnah/Seder Tahorot/", r"^(Mishnah .+|Pirkei Avot)$"),
    ("json/Tosefta/Vilna Edition/", r"."),
    ("json/Tosefta/Lieberman Edition/", r"."),
]


def list_keys(prefix, token=None):
    url = "%s?prefix=%s&max-keys=1000" % (BUCKET, urllib.parse.quote(prefix))
    if token:
        url += "&marker=" + urllib.parse.quote(token)
    xml = urllib.request.urlopen(url, timeout=30).read().decode("utf-8")
    keys = re.findall(r"<Key>([^<]+)</Key>", xml)
    truncated = "<IsTruncated>true</IsTruncated>" in xml
    return keys, (keys[-1] if truncated and keys else None)


def all_keys(prefix):
    out, token = [], None
    while True:
        keys, token = list_keys(prefix, token)
        out += keys
        if not token:
            return out


def safe(name):
    return re.sub(r"[^A-Za-z0-9_]+", "_", name).strip("_")


def fetch(key, dest):
    if dest.exists() and dest.stat().st_size > 0:
        return "skip"
    dest.parent.mkdir(parents=True, exist_ok=True)
    url = BUCKET + "/" + urllib.parse.quote(key)
    for attempt in (1, 2, 3):
        try:
            data = urllib.request.urlopen(url, timeout=300).read()
            dest.write_bytes(data)
            time.sleep(DELAY)
            return "%.1f MB" % (len(data) / 1e6)
        except Exception as e:
            if attempt == 3:
                return "FAIL %s" % e
            time.sleep(2 * attempt)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = []
    for prefix, pat in WANT:
        keys = all_keys(prefix)
        merged = [k for k in keys if k.endswith("/merged.json")]
        works = {}
        for k in merged:
            parts = k.split("/")
            lang = parts[-2]
            work = parts[-3]
            if lang in ("Hebrew", "English") and re.search(pat, work):
                works.setdefault(work, {})[lang] = k
        for work, langs in sorted(works.items()):
            for lang, k in sorted(langs.items()):
                dest = OUT / safe(work) / ("he.json" if lang == "Hebrew" else "en.json")
                r = fetch(k, dest)
                manifest.append("%s | %s | %s" % (k, dest.relative_to(REPO), r))
                print(manifest[-1], flush=True)
    with open(OUT / "MIRROR_MANIFEST.txt", "a", encoding="utf-8") as fh:
        fh.write("\n# TALMUD-SHELF extension — fetched %s (Bavli text + "
                 "Mishnah + Tosefta both editions)\n%s\n"
                 % (time.strftime("%Y-%m-%d"), "\n".join(manifest)))
    fails = [m for m in manifest if "FAIL" in m]
    print("\nDONE: %d files, %d failures" % (len(manifest), len(fails)))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
