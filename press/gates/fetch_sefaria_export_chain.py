#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fetch_sefaria_export_chain.py — CHAIN-OF-TRANSMISSION shelf completion
(owner ruling 2026-08-10: "Only use oral torah in the chain of
transmission" + "phase 1 go"). Completes the local mirror to the whole
Oral Torah as transmitted: tannaim/amoraim -> geonim -> rishonim ->
classical acharonim.

ADDS: Jerusalem Talmud (all text tractates, five sedarim); all 15 Bavli
minor tractates (incl. Soferim); chain midrash completions (Yalkut
Shimoni, Lekach Tov, both Pesiktas, Tanna DeBei Eliyahu, Seder Olam,
Midrash Tehillim/Mishlei/Shmuel/Aggadah/Sekhel Tov, Bereshit Rabbati,
Mishnat Rabbi Eliezer, Sefer HaYashar, Yelamdenu, the five Megillot
Rabbahs; Sifrei Zuta + Midrash Tannaim); ALL rishonim on Torah books
(book-filtered — Nach works excluded by pattern); classical acharonim
on Torah books (incl. Torah Temimah, Or HaChaim, Malbim, Gur Aryeh,
Haamek Davar, Meshech Hochma, HaKtav VeHaKabalah...); the codes:
Halakhot Gedolot (geonic), Mishneh Torah, Tur, Shulchan Arukh, and the
six primary mitzvot-codes (Chinukh, Rambam's + Saadia's Sefer
HaMitzvot, SMAG, SMAK, Yereim).

EXCLUDED AS OUTSIDE/BORDERLINE — surfaced to owner, never silent
(law #3): Ein Yaakov (Bavli-aggadah compilation, duplicative — its
links resolve through the Bavli itself); Rif (extracted Gemara, same
reason); Otzar Midrashim + Legends of the Jews + Ruth Rabbah (Lerner)
(modern compilations/editions); Reggio + Shadal + Ohev Ger (haskalah-
method — owner may rule in); Tze'enah Ure'enah (homiletic anthology);
Minchat Chinukh / Derekh Pikudekha / Sefer Charedim (commentary and
devotional layers on the codes); Arukh HaShulchan / Kitzur Shulchan
Arukh / Chayyei Adam / Ben Ish Hai / Shulchan Arukh HaRav (later
digests — owner may rule in); all Commentary/Footnotes/Modern
subtrees.

Same mechanics as the 2026-08-08/10 fetchers; APPENDS to
MIRROR_MANIFEST.txt. Usage:
  python3 logic/solo_tools/fetch_sefaria_export_chain.py
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

TORAH = r"(Genesis|Exodus|Leviticus|Numbers|Deuteronomy)"
ON_TORAH = r"((on|,) %s$|on Torah$)" % TORAH

WANT = [
    # Jerusalem Talmud — text tractates only
    ("json/Talmud/Yerushalmi/Seder Zeraim/", r"^Jerusalem Talmud "),
    ("json/Talmud/Yerushalmi/Seder Moed/", r"^Jerusalem Talmud "),
    ("json/Talmud/Yerushalmi/Seder Nashim/", r"^Jerusalem Talmud "),
    ("json/Talmud/Yerushalmi/Seder Nezikin/", r"^Jerusalem Talmud "),
    ("json/Talmud/Yerushalmi/Seder Tahorot/", r"^Jerusalem Talmud "),
    # Bavli minor tractates — all
    ("json/Talmud/Bavli/Minor Tractates/",
     r"^(Avot DeRabbi Natan(, Recension B)?|Tractate .+)$"),
    # Midrash Aggadah — chain completions
    ("json/Midrash/Aggadah/",
     r"^(Bereshit Rabbati|Midrash Aggadah|Midrash Lekach Tov"
     r"|Midrash Mishlei|Midrash Sekhel Tov|Midrash Shmuel"
     r"|Midrash Tehillim|Mishnat Rabbi Eliezer|Pesikta DeRav Kahana"
     r"|Pesikta Rabbati|Seder Olam Rabbah|Seder Olam Zutta"
     r"|Sefer HaYashar \(midrash\)|Tanna DeBei Eliyahu Rabbah"
     r"|Tanna DeBei Eliyahu Zuta|Yalkut Shimoni on Torah"
     r"|Yalkut Shimoni on Nach|Midrash Yelamdenu.*"
     r"|Eikhah Rabbah|Esther Rabbah|Kohelet Rabbah|Ruth Rabbah"
     r"|Shir HaShirim Rabbah)$"),
    # Midrash Halakhah — completions
    ("json/Midrash/Halakhah/",
     r"^(Sifrei Zuta|Midrash Tannaim on Deuteronomy)$"),
    # Rishonim on Torah — every chain rishon, Torah books only
    ("json/Tanakh/Rishonim on Tanakh/", ON_TORAH),
    # Classical acharonim on Torah — book-filtered, minus haskalah-method
    ("json/Tanakh/Acharonim on Tanakh/", ON_TORAH),
    # The codes
    ("json/Halakhah/", r"^Halakhot Gedolot$"),
    ("json/Halakhah/Mishneh Torah/", r"^Mishneh Torah"),
    ("json/Halakhah/Tur/", r"^Tur$"),
    ("json/Halakhah/Shulchan Arukh/", r"^Shulchan Arukh,"),
    ("json/Halakhah/Sifrei Mitzvot/",
     r"^(Sefer HaChinukh|Sefer HaMitzvot|Sefer Hamitzvot of Rasag"
     r"|Sefer Mitzvot Gadol|Sefer Mitzvot Katan|Sefer Yereim)$"),
]

# Book-pattern hits that are nonetheless OUT (haskalah-method / anthology
# — surfaced in the docstring; owner may rule them in):
EXCLUDE_WORKS = re.compile(
    r"^(Reggio|Shadal|Ohev Ger|Tze'enah Ure'enah|Legends of the Jews)")


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
            if (lang in ("Hebrew", "English") and re.search(pat, work)
                    and not EXCLUDE_WORKS.search(work)
                    and "/Commentary/" not in k and "/Guides/" not in k
                    and "/Modern Commentary" not in k):
                works.setdefault(work, {})[lang] = k
        for work, langs in sorted(works.items()):
            for lang, k in sorted(langs.items()):
                dest = OUT / safe(work) / ("he.json" if lang == "Hebrew" else "en.json")
                r = fetch(k, dest)
                manifest.append("%s | %s | %s" % (k, dest.relative_to(REPO), r))
                print(manifest[-1], flush=True)
    with open(OUT / "MIRROR_MANIFEST.txt", "a", encoding="utf-8") as fh:
        fh.write("\n# CHAIN-OF-TRANSMISSION completion — fetched %s (owner\n"
                 "# ruling: whole Oral Torah in the chain; see script header\n"
                 "# for the surfaced exclusions)\n%s\n"
                 % (time.strftime("%Y-%m-%d"), "\n".join(manifest)))
    fails = [m for m in manifest if "FAIL" in m]
    print("\nDONE: %d files, %d failures" % (len(manifest), len(fails)))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
