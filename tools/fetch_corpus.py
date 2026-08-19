#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
"""fetch_corpus.py — build the WHOLE-WORK local corpus: shelf/corpus/.

Where fetch_links.py + fetch_texts.py build a per-verse-span source shelf,
this script mirrors complete works, one JSON file per work per language,
from the Sefaria-Export bulk bucket (the sanctioned path for whole books —
politer than hammering the live API). The scan ledgers in scans/ cite
these files; the derivation machines read data/tanakh.sqlite and do not
need them.

What it fetches (flat names as shelf/corpus/<name>_<lang>.json):
  bavli_*        — Talmud Bavli, every tractate, Hebrew
  yerushalmi_*   — Jerusalem Talmud, every tractate, Hebrew
  mishnah_*      — Mishnah, every tractate (incl. Pirkei Avot), Hebrew
  tosefta_*      — Tosefta (Vilna edition), every tractate, Hebrew
  rambam_*       — Mishneh Torah, every section, English where the
                   bucket has it, else Hebrew
  mekhilta / mekhilta_rashbi — the two Mekhiltas, Hebrew + English
  sifra, sifrei_bamidbar, sifrei_devarim — halakhic midrash, Hebrew
  bereshit_rabbah, vayikra_rabbah — aggadic midrash, Hebrew
  minchat_shai_torah — the Masoretic apparatus commentary, Hebrew
  zohar          — the Zohar, Hebrew
  sefer_yetzirah, sefer_yetzirah_gra_version — the Book of Formation,
                   both recensions, Hebrew + English
  tanakh_*_jps1917_en — the five Torah books, JPS 1917 English
  links0..8.csv  — Sefaria's cross-reference link shards
  strongs_hebrew_dictionary.json — Strong's Hebrew lexicon
                   (openscriptures, public domain)

POLITENESS CONTRACT (do not weaken it): sequential requests, DELAY
seconds apart. Existing files are skipped, so runs are resumable; delete
a file to refetch it.

Each saved work is Sefaria's "merged" version unless named otherwise —
check the version's license on its Sefaria page before REDISTRIBUTING
any text; reading, scanning, and citing are what this shelf is for. The
shelf/ directory is a gitignored cache, never part of the repository
record.

Usage:
  python3 tools/fetch_corpus.py                 # fetch everything missing
  python3 tools/fetch_corpus.py --plan          # list what would be fetched
  python3 tools/fetch_corpus.py --only yetzirah # restrict by substring
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

BUCKET = "https://storage.googleapis.com/sefaria-export"
STRONGS_URL = ("https://raw.githubusercontent.com/openscriptures/strongs/"
               "master/hebrew/strongs-hebrew-dictionary.js")
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "shelf" / "corpus"
DELAY = 0.4          # seconds between requests — do not lower
FETCHED = time.strftime("%Y-%m-%d")

# (bucket prefix, work-title regex, languages, rename rules)
# languages: "he" | "en" | "both" | "en_else_he"
# rename rules: (pattern, replacement) applied to the work title before
# slugging — how "Jerusalem Talmud Yoma" becomes yerushalmi_yoma.
WANT = [
    ("json/Talmud/Bavli/Seder Zeraim/",   r".", "he", (r"^", "bavli ")),
    ("json/Talmud/Bavli/Seder Moed/",     r".", "he", (r"^", "bavli ")),
    ("json/Talmud/Bavli/Seder Nashim/",   r".", "he", (r"^", "bavli ")),
    ("json/Talmud/Bavli/Seder Nezikin/",  r".", "he", (r"^", "bavli ")),
    ("json/Talmud/Bavli/Seder Kodashim/", r".", "he", (r"^", "bavli ")),
    ("json/Talmud/Bavli/Seder Tahorot/",  r".", "he", (r"^", "bavli ")),
    ("json/Talmud/Yerushalmi/", r"^Jerusalem Talmud ", "he",
     (r"^Jerusalem Talmud ", "yerushalmi ")),
    ("json/Mishnah/Seder Zeraim/",   r"^(Mishnah .+|Pirkei Avot)$", "he",
     (r"^Pirkei Avot$", "mishnah Pirkei Avot")),
    ("json/Mishnah/Seder Moed/",     r"^Mishnah .+$", "he", None),
    ("json/Mishnah/Seder Nashim/",   r"^Mishnah .+$", "he", None),
    ("json/Mishnah/Seder Nezikin/",  r"^(Mishnah .+|Pirkei Avot)$", "he",
     (r"^Pirkei Avot$", "mishnah Pirkei Avot")),
    ("json/Mishnah/Seder Kodashim/", r"^Mishnah .+$", "he", None),
    ("json/Mishnah/Seder Tahorot/",  r"^Mishnah .+$", "he", None),
    ("json/Tosefta/Vilna Edition/", r"^Tosefta ", "he", None),
    ("json/Halakhah/Mishneh Torah/", r"^Mishneh Torah, ", "en_else_he",
     (r"^Mishneh Torah, ", "rambam ")),
    ("json/Midrash/Halakhah/", r"^(Sifra|Sifrei Bamidbar|Sifrei Devarim)$",
     "he", None),
    ("json/Midrash/Halakhah/", r"^Mekhilta DeRabbi Yishmael$", "both",
     (r"^Mekhilta DeRabbi Yishmael$", "mekhilta")),
    ("json/Midrash/Halakhah/", r"^Mekhilta DeRabbi Shimon Ben Yochai$",
     "both", (r"^Mekhilta DeRabbi Shimon Ben Yochai$", "mekhilta rashbi")),
    ("json/Midrash/Aggadah/", r"^(Bereshit|Vayikra) Rabbah$", "he", None),
    ("json/Tanakh/Rishonim on Tanakh/Minchat Shai/",
     r"^Minchat Shai on Torah$", "he", None),
    ("json/Kabbalah/Zohar/", r"^Zohar$", "he", None),
    ("json/Kabbalah/Sefer Yetzirah/", r"^Sefer Yetzirah( Gra Version)?$",
     "both", None),
]

TORAH_BOOKS = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy"]
JPS_KEY = ("json/Tanakh/Torah/%s/English/"
           "The Holy Scriptures A New Translation JPS 1917.json")


def slug(title):
    return re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")


def list_keys(prefix, token=None):
    url = "%s?prefix=%s&max-keys=1000" % (BUCKET, urllib.parse.quote(prefix))
    if token:
        url += "&marker=" + urllib.parse.quote(token)
    xml = urllib.request.urlopen(url, timeout=30).read().decode("utf-8")
    keys = re.findall(r"<Key>([^<]+)</Key>", xml)
    truncated = "<IsTruncated>true</IsTruncated>" in xml
    return keys, (keys[-1] if truncated and keys else None)


def all_keys(prefix, cache={}):
    if prefix not in cache:
        out, token = [], None
        while True:
            keys, token = list_keys(prefix, token)
            out += keys
            if not token:
                break
        cache[prefix] = out
    return cache[prefix]


def plan():
    """Discover every (flat filename, bucket key) the corpus should hold."""
    jobs = []
    for prefix, pat, langs, rename in WANT:
        works = {}
        for k in all_keys(prefix):
            if not k.endswith("/merged.json"):
                continue
            parts = k.split("/")
            lang, work = parts[-2], parts[-3]
            if lang in ("Hebrew", "English") and re.search(pat, work):
                works.setdefault(work, {})[lang] = k
        for work, found in sorted(works.items()):
            name = work
            if rename:
                name = re.sub(rename[0], rename[1], name)
            base = slug(name)
            if langs == "en_else_he":
                take = [("English", "en")] if "English" in found \
                    else [("Hebrew", "he")]
            else:
                take = [(l, s) for l, s in
                        (("Hebrew", "he"), ("English", "en"))
                        if s in (langs if langs != "both" else "he en")
                        and l in found]
            for lang, suffix in take:
                jobs.append(("%s_%s.json" % (base, suffix), found[lang]))
    for book in TORAH_BOOKS:
        jobs.append(("tanakh_%s_jps1917_en.json" % book.lower(),
                     JPS_KEY % book))
    for k in all_keys("links/"):
        if re.match(r"links/links\d+\.csv$", k):
            jobs.append((k.split("/")[-1], k))
    jobs.append(("strongs_hebrew_dictionary.json", STRONGS_URL))
    return jobs


def fetch(key, dest):
    url = key if key.startswith("http") \
        else BUCKET + "/" + urllib.parse.quote(key)
    for attempt in (1, 2, 3):
        try:
            data = urllib.request.urlopen(url, timeout=120).read()
            if key == STRONGS_URL:      # strip the JS variable wrapper
                text = data.decode("utf-8")
                text = text[text.index("{"):text.rindex("}") + 1]
                json.loads(text)        # must parse before we keep it
                data = text.encode("utf-8")
            dest.write_bytes(data)
            time.sleep(DELAY)
            return "%.1f MB" % (len(data) / 1e6)
        except Exception as e:
            if attempt == 3:
                return "FAIL %s" % e
            time.sleep(2 * attempt)


def main():
    args = sys.argv[1:]
    only = None
    if "--only" in args:
        only = args[args.index("--only") + 1]
    jobs = plan()
    if only:
        jobs = [j for j in jobs if only in j[0]]
    if "--plan" in args:
        for name, key in jobs:
            print("%-46s <- %s" % (name, key))
        print("\n%d files planned" % len(jobs))
        return
    OUT.mkdir(parents=True, exist_ok=True)
    done = skipped = failed = 0
    manifest = []
    for name, key in jobs:
        dest = OUT / name
        if dest.exists() and dest.stat().st_size > 0:
            skipped += 1
            continue
        r = fetch(key, dest)
        manifest.append("%s | %s | %s" % (name, key, r))
        print(manifest[-1], flush=True)
        if "FAIL" in r:
            failed += 1
        else:
            done += 1
    if manifest:
        with (OUT / "CORPUS_MANIFEST.txt").open("a", encoding="utf-8") as f:
            f.write("\n# corpus fetch %s\n%s\n" % (FETCHED,
                                                   "\n".join(manifest)))
    print("corpus: %d planned · fetched %d · already had %d · failed %d -> %s"
          % (len(jobs), done, skipped, failed, OUT))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
