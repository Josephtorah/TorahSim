#!/usr/bin/env python3
"""
index_oral.py — Step 3 of PLAN_fullstack_architecture_2026-07-28.md

1. oral_texts (FTS5): every text segment of every Hebrew corpus file in Data/
   (*_he.json), searchable by consonantal text, with stable array path and a
   computed human locus where the corpus shape is known (chapters+1:piece+1 for
   Mishnah/Tosefta/Rabbah-style; Bavli/Yerushalmi keep path-only — daf mapping
   varies, do NOT guess).
2. oral_refs: backfill of the quotes verified during the 2026-07 week work
   (tier=verified unless noted). Named-location-only policy; anchors are
   Written verses these discussions sit on.
"""
from __future__ import annotations

import json
import re
import sqlite3
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "derivation.sqlite"

STRIP = re.compile(r"[֑-ׇ]")
TAGS = re.compile(r"<[^>]+>")


def flatten(x, path=()):
    if isinstance(x, str):
        yield path, x
    elif isinstance(x, list):
        for i, y in enumerate(x):
            yield from flatten(y, path + (i,))


def he_plain(s: str) -> str:
    return STRIP.sub("", TAGS.sub("", s))


DDL = """
DROP TABLE IF EXISTS oral_refs;
DROP TABLE IF EXISTS oral_texts;
CREATE VIRTUAL TABLE oral_texts USING fts5(work, locus, path, he_plain);
CREATE TABLE oral_refs (id INTEGER PRIMARY KEY, work TEXT, locus TEXT,
                        he TEXT, translit TEXT, en TEXT, tier TEXT,
                        anchors_to TEXT);
"""

# (work, locus, he, translit, en, tier, anchors)
REFS = [
    ("Bereshit Rabbah", "4:2", "לחים היו מעשיהם ביום הראשון ובשני קרשו. יהי רקיע — יחזק הרקיע",
     "lachim hayu ma'aseihem ba-yom ha-rishon u-va-sheni karshu",
     "heavens fluid day 1, solidified day 2 — two-phase creation", "verified", "Gen.1.6"),
    ("Bereshit Rabbah", "4:6", "למה אין כתיב בשני כי טוב — שבו נבראת גיהנם",
     "lamah ein ketiv ba-sheni ki tov — she-bo nivre'at Gehinnom",
     "why no 'good' on day 2: Gehinnom created on it", "verified", "Gen.1.7"),
    ("Bereshit Rabbah", "4:7", "נטל הקב\"ה אש ומים ופתכן זה בזה ומהן נעשו שמים",
     "natal HKBH esh u-mayim u-fetakhan zeh ba-zeh",
     "shamayim = fire+water kneaded together (naming of raqia)", "verified", "Gen.1.8"),
    ("Bereshit Rabbah", "5:8", "למה נקרא שמה ארץ? שרצתה לעשות רצון קונה",
     "lamah niqra shemah eretz? she-ratzta la'asot retzon konah",
     "eretz earned by willing its Owner's will; also yamim plural", "verified", "Gen.1.10"),
    ("Bereshit Rabbah", "5:9", "שלשה נכנסו לדין וארבעה יצאו מחיבין … ונתקללה הארץ עמהן",
     "sheloshah nikhnesu la-din ve-arba'ah yatze'u mechuyavin",
     "earth's fruit-tree deviation judged: cursed with Adam/Eve/serpent", "verified", "Gen.1.11"),
    ("Bereshit Rabbah", "3:7", "מלמד שהיה בורא עולמות ומחריבן … אמר דין הנין לי",
     "melammed she-hayah bore olamot u-machrivan … dein hanyan li",
     "worlds created and destroyed; 'very good' = these please Me", "verified", "Gen.1.31"),
    ("Bereshit Rabbah", "9:5", "בתורתו של רבי מאיר מצאו כתוב: והנה טוב מאד — והנה טוב מות",
     "be-torato shel Rabbi Meir: ve-hinneh tov me'od — tov mavet",
     "R. Meir's scroll: 'very good' ~ 'death is good'", "verified", "Gen.1.31"),
    ("Bereshit Rabbah", "8:3", "נעשה אדם — במי נמלך? במלאכת השמים והארץ נמלך",
     "na'aseh adam — be-mi nimlakh?",
     "'let us make': God consulted (heaven+earth's works / each day's works)", "verified", "Gen.1.26"),
    ("Bereshit Rabbah", "8:1", "אחור וקדם צרתני — דו פרצופים",
     "achor va-qedem tzartani — du-partzufin",
     "first human two-faced (BR parallel to Eruvin 18a)", "verified", "Gen.1.27"),
    ("Bereshit Rabbah", "11:2", "ברכו במן וקדשו במן",
     "berkho ba-man ve-qiddesho ba-man",
     "Shabbat blessed with manna, sanctified with manna", "verified", "Gen.2.3"),
    ("Bereshit Rabbah", "11:8", "שאין לו בן זוג … שבתא לית לה בן זוג",
     "she-ein lo ben zug",
     "Shabbat the only day without a partner", "verified", "Gen.2.3"),
    ("Bavli Chagigah", "12a", "מאי שמים … ששם מים … אש ומים … ועשה מהן רקיע",
     "mai shamayim … she-sham mayim … esh u-mayim",
     "shamayim etymology terminates in the raqia", "verified", "Gen.1.8"),
    ("Bavli Chagigah", "12b", "שבעה … וילון רקיע שחקים זבול מעון מכון ערבות … רקיע שבו חמה ולבנה",
     "shiv'ah reqi'im … Raqia she-bo chamah u-levanah",
     "seven heavens; Raqia = member holding the luminaries (Gen 1:17)", "verified", "Gen.1.17"),
    ("Bavli Sanhedrin", "38b", "ברא כת אחת של מלאכי השרת אמר להם רצונכם נעשה אדם בצלמנו",
     "bara kat achat shel mal'akhei ha-sharet",
     "'let us make': consultation with a company of angels", "verified", "Gen.1.26"),
    ("Bavli Eruvin", "18a", "דיו פרצוף פנים היה לו לאדם הראשון",
     "du partzuf panim hayah lo le-adam ha-rishon",
     "first human du-partzufin: him→them number flip", "verified", "Gen.1.27"),
    ("Bavli Bava Batra", "74b", "התנינים הגדולים — זה לויתן נחש בריח ולויתן נחש עקלתון",
     "zeh livyatan nachash bariach ve-livyatan nachash aqallaton",
     "the great taninim = Leviathan", "verified", "Gen.1.21"),
    ("Bavli Shabbat", "88a", "ה' יתירה למה לי? מלמד שהתנה הקב\"ה עם מעשה בראשית",
     "heh yeterah lamah li? she-hitnah HKBH im ma'aseh bereshit",
     "yom HA-shishi: creation conditional on Sinai acceptance (rollback: tohu)", "verified", "Gen.1.31"),
    ("Bavli Shabbat", "119b", "כל המתפלל … ואומר ויכולו … נעשה שותף להקב\"ה במעשה בראשית",
     "kol ha-mitpallel … va-yekhullu … na'asah shutaf",
     "saying vayekhullu = partner in creation (pual read as active plural)", "verified", "Gen.2.1"),
    ("Bavli Rosh Hashanah", "31a", "בשביעי … מזמור שיר ליום השבת — ליום שכולו שבת",
     "le-yom she-kullo shabbat",
     "seventh-day psalm: the day that is entirely Shabbat (epoch open)", "verified", "Gen.2.2"),
    ("Bereshit Rabbah", "10:9", "מה היה העולם חסר? מנוחה. באת שבת באת מנוחה",
     "mah hayah ha-olam chaser? menuchah",
     "day-7 completion paradox: rest itself was created (NOT found in local dump)",
     "observation", "Gen.2.2"),
]

RABBAH_LIKE = ("_rabbah_", "mishnah_", "tosefta_")


def main() -> None:
    con = sqlite3.connect(DB)
    con.executescript(DDL)
    t0 = time.time()
    files = sorted(p for p in (ROOT / "shelf" / "sources").glob("*_he.json"))
    n_seg = 0
    for p in files:
        try:
            doc = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        work = doc.get("title", p.stem)
        shaped = any(k in p.name for k in RABBAH_LIKE)
        rows = []
        for path, s in flatten(doc.get("text", [])):
            t = he_plain(s)
            if not t.strip():
                continue
            locus = f"{path[0]+1}:{path[1]+1}" if (shaped and len(path) >= 2) else ""
            rows.append((work, locus, json.dumps(path), t))
        con.executemany("INSERT INTO oral_texts VALUES(?,?,?,?)", rows)
        n_seg += len(rows)
    con.executemany(
        "INSERT INTO oral_refs(work, locus, he, translit, en, tier, anchors_to)"
        " VALUES(?,?,?,?,?,?,?)", REFS)
    con.execute("INSERT OR REPLACE INTO meta VALUES('oral_files_indexed', ?)", (str(len(files)),))
    con.execute("INSERT OR REPLACE INTO meta VALUES('oral_segments_indexed', ?)", (str(n_seg),))
    con.commit()
    con.close()
    print(f"indexed {len(files)} corpus files · {n_seg} segments · {len(REFS)} oral_refs · {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
