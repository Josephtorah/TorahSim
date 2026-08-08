#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fetch_sefaria_export.py — one-time curated mirror of the Sefaria-Export
GCS bucket (oral-first era, owner order 2026-08-08: local search).

Discovers exact keys via the bucket LISTING API (no guessed paths), then
downloads Hebrew + English merged.json per work into
Data/sefaria_export/<safe_work_name>/{he,en}.json plus the links CSV
shards into Data/sefaria_export/links/. Resumable: existing files are
skipped. Sequential, modest pacing — the bulk bucket is the sanctioned
path (politer than per-verse API calls forever).

Usage: python3 logic/solo_tools/fetch_sefaria_export.py
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

# Category prefixes to search, and the work-title patterns to take.
WANT = [
    ("json/Tanakh/Rishonim on Tanakh/Rashi/", r"Rashi on (Genesis|Exodus|Leviticus|Numbers|Deuteronomy)$"),
    ("json/Tanakh/Rishonim on Tanakh/Kitzur Ba'al HaTurim/", r"Kitzur Ba'al HaTurim on \w+$"),
    ("json/Tanakh/Rishonim on Tanakh/Ba'al HaTurim/", r"Ba'al HaTurim on \w+$"),
    ("json/Tanakh/Rishonim on Tanakh/Minchat Shai/", r"Minchat Shai on Torah$"),
    ("json/Midrash/Aggadah/", r"^(Bereshit|Shemot|Vayikra|Bamidbar|Devarim) Rabbah$|^Midrash Tanchuma( Buber)?$|^Pirkei DeRabbi Eliezer$|^Aggadat Bereshit$"),
    ("json/Midrash/Halakhah/", r"^Sifra$|^Sifrei (Bamidbar|Devarim)$|^Mekhilta DeRabbi (Yishmael|Shimon Ben Yochai)$"),
    ("json/Talmud/Bavli/Minor Tractates/", r"^Avot D[e']Rabbi Natan$"),
    ("json/Tanakh/Targum/", r"^Onkelos (Genesis|Exodus|Leviticus|Numbers|Deuteronomy)$|^Targum Jonathan on (Genesis|Exodus|Leviticus|Numbers|Deuteronomy)$"),
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
            data = urllib.request.urlopen(url, timeout=120).read()
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
    # 1. texts
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
    # 2. links shards
    for k in sorted(all_keys("links/")):
        if re.match(r"links/links\d+\.csv$", k):
            dest = OUT / "links" / k.split("/")[-1]
            r = fetch(k, dest)
            manifest.append("%s | %s | %s" % (k, dest.relative_to(REPO), r))
            print(manifest[-1], flush=True)
    (OUT / "MIRROR_MANIFEST.txt").write_text(
        "# Sefaria-Export curated mirror — fetched %s\n%s\n"
        % (time.strftime("%Y-%m-%d"), "\n".join(manifest)), encoding="utf-8")
    fails = [m for m in manifest if "FAIL" in m]
    print("\nDONE: %d files, %d failures" % (len(manifest), len(fails)))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
