#!/usr/bin/env python3
"""bacher_scan.py — test Bacher's catalogued exegetical terms against our cache.

Wilhelm Bacher, *Die exegetische Terminologie der juedischen
Traditionsliteratur* ("The Exegetical Terminology of Jewish Traditional
Literature"), 2 vols., Leipzig 1899/1905: the scholarly lexicon of the Oral
chain's technical vocabulary — vol. I the Tannaitic (Mishnah-era) terms,
vol. II the Amoraic (Talmud-era) terms. Public domain.

PROVENANCE (honest): the archive.org scan (dieexegetischet00bachgoog) was
fetched 2026-07-31, but its Google OCR preserved ZERO Hebrew characters —
every headword is destroyed. The Hebrew translation (Erkhei Midrash, "Entries
of Midrash", A.Z. Rabinovitz) is not on Sefaria (name-API checked, logged).
The candidate list below is therefore reconstructed from scholarship on
Bacher's entries, NOT OCR-extracted — and every candidate is tested
empirically against OUR OWN cache, which is the project's honest instrument.
Survey tier only; nothing here mints a rule (ein adam dan me-atzmo — "one may
not derive on his own").

Run: python3 logic/middot_scan/bacher_scan.py
Output: counts per term (document frequency over cached sources).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from discover_devices import load_oral_texts

# (rulebook-tag-if-adopted, "name (gloss)", [needles])
CANDIDATES = [
    ("bacher", "minayin ('from where [is this derived]?' — the tannaitic derivation question)",
     ["מנין ש", "ומנין ש", "מניין ש", "מנין לו", "מנין את"]),
    ("bacher", "mena hani mili (Aramaic 'from where are these words?' — the Bavli's source-demand)",
     ["מנא הני מילי", "מנהני מילי"]),
    ("bacher", "mai dikhtiv (Aramaic 'what is [the meaning of] what is written?')",
     ["מאי דכתיב"]),
    ("bacher", "haynu dikhtiv (Aramaic 'this is what is written' — Bavli cousin of hada hu dikhtiv)",
     ["היינו דכתיב"]),
    ("bacher", "ein li ela ('I have [from the verse] only…' — scope-limit opener)",
     ["אין לי אלא"]),
    ("bacher", "shema tomar ('lest you say' — pre-empted objection)",
     ["שמא תאמר"]),
    ("bacher", "mah ra'ah ('what did he see [to prompt this]' — motivation question)",
     ["מה ראה"]),
    ("bacher", "ka-yotze bo ('similarly / a parallel case' — precedent-array operator)",
     ["כיוצא בו", "כיוצא בדבר"]),
    ("bacher", "keneged ('corresponding to' — correspondence/typology operator)",
     ["כנגד"]),
    ("bacher", "lo ba ha-katuv ela ('the verse comes only to…' — purpose-restriction)",
     ["לא בא הכתוב אלא", "בא הכתוב ללמד"]),
    ("bacher", "eino omer … ela ('it does not say … but rather' — diff-operator variant)",
     ["אינו אומר אלא", "אינו אומר כן אלא"]),
    ("bacher", "dibber ha-katuv ba-hoveh ('Scripture speaks of the usual case' — typical-case scoping rule)",
     ["דבר הכתוב בהוה", "דיבר הכתוב בהוה"]),
    ("bacher", "dibberah Torah ki-lshon benei adam ('the Torah speaks in human language' — meta-rule)",
     ["כלשון בני אדם"]),
    ("bacher", "le-mah ha-davar domeh ('to what may the matter be compared' — parable announcement)",
     ["למה הדבר דומה", "משלו משל"]),
    ("bacher", "ma'aseh be- ('an incident concerning' — case/precedent marker)",
     ["מעשה ב"]),
    ("bacher", "she-ne'emar ('as it is said' — the baseline prooftext citator; density meter)",
     ["שנאמר"]),
    ("bacher", "ve-omer ('and it says' — stacked additional prooftext; noisy needle, DF only)",
     ["ואומר"]),
    ("bacher", "ktiv hakha u-khtiv hatam (Aramaic 'written here and written there' — the Bavli's verbal-analogy executor)",
     ["כתיב הכא וכתיב התם", "וכתיב התם"]),
    ("bacher", "ta shema (Aramaic 'come [and] hear' — proof summons)",
     ["תא שמע"]),
    ("bacher", "bo u-re'eh ('come and see' — demonstration summons)",
     ["בא וראה", "בוא וראה"]),
    ("bacher", "u-mah ani mekayyem ('how then do I uphold [the other verse]' — harmonization)",
     ["מה אני מקיים", "הא מה אני מקיים"]),
    ("bacher", "ein mikra yotze midei peshuto ('a verse never leaves its plain sense' — meta-rule)",
     ["מידי פשוטו"]),
    ("bacher", "ein mukdam u-me'uchar ba-Torah ('no earlier-and-later in the Torah' — the policy phrase)",
     ["אין מוקדם ומאוחר"]),
    ("bacher", "tanya / tanu rabbanan ('it was taught / the Rabbis taught' — tannaitic-source markers)",
     ["תניא", "תנו רבנן"]),
    ("bacher", "klal amru ('they stated a general rule' — rule-summary marker)",
     ["כלל אמרו"]),
    ("bacher", "ribah/miet ha-katuv ('Scripture included / excluded' — inclusion-exclusion execution verbs)",
     ["ריבה הכתוב", "מיעט הכתוב", "ריבה לך הכתוב"]),
]


def main():
    texts = load_oral_texts()
    print("corpus: %d cached sources\n" % len(texts))
    rows = []
    for _tag, name, needles in CANDIDATES:
        srcs = [ref for ref, toks in texts.items()
                if any(n in " ".join(toks) for n in needles)]
        rows.append((len(srcs), name, sorted(srcs)[:4]))
    rows.sort(reverse=True)
    for n, name, ex in rows:
        print("%4d  %s" % (n, name))
        if n:
            print("      e.g. %s" % ", ".join(ex[:3]))


if __name__ == "__main__":
    main()
