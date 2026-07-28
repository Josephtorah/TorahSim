#!/usr/bin/env python3
"""
Generate logic/lexicon/v1/lexicon.yaml — whole-Torah gloss table (EN-AID).

Sources: distinct lemmas from torah_grok.sqlite (OSHB tags) + Strong's Hebrew
dictionary (Data/strongs_hebrew_dictionary.json, public domain, #IMPOSED) +
hand-curated glosses (previously inline in render_flat_ledger_morph_html.py),
which OVERRIDE auto glosses. Stage A of PLAN_fullstack_architecture_2026-07-28.
"""
import json
import re
import sqlite3
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "logic" / "lexicon" / "v1"

# hand-curated glosses (Gen-1 seeded set; src: hand — these win)
HAND = {
    "215": "give-light", "216": "light", "226": "signs", "259": "one", "413": "to",
    "430": "God", "559": "say", "776": "earth", "853": "obj-marker·et", "914": "divide",
    "922": "void", "996": "between", "1242": "morning", "1876": "sprout", "1877": "grass",
    "1961": "be", "2232": "yield-seed", "2233": "seed", "2822": "darkness", "3004": "dry-land",
    "3117": "day", "3220": "seas", "3318": "bring-forth", "3556": "stars", "3915": "night",
    "3974": "lights", "4150": "seasons", "4325": "waters", "4327": "kind", "4475": "dominion",
    "4725": "place", "4910": "rule", "5315": "living-being", "5414": "set", "5775": "flying-creature",
    "6086": "tree", "6153": "evening", "6212": "herb", "6440": "face", "6529": "fruit",
    "7121": "call", "7200": "see", "7225": "beginning", "7243": "fourth", "7307": "spirit",
    "7549": "firmament", "7992": "third", "8064": "heavens", "8141": "years", "8145": "second",
    "8147": "two", "8317": "swarm", "8318": "swarming-creature", "8414": "formless", "8415": "deep",
    "8432": "midst", "8478": "under", "834 a": "which", "1254 a": "create", "1419 a": "great",
    "2416 a": "living", "2896 a": "good", "3588 a": "that", "3651 c": "so", "4723 c": "gathering",
    "5774 a": "fly", "5921 a": "over", "6213 a": "make", "6960 b": "be-gathered",
    "6996 b": "small", "7363 b": "hovering",
    "120": "human", "127": "ground", "1288": "bless", "1710": "fish", "1823": "likeness",
    "2009": "behold", "2145": "male", "2416 c": "living", "2549": "fifth", "3418": "green",
    "3533": "subdue", "3605": "all", "3615": "be-complete", "3671": "wing", "3966": "very",
    "402": "food", "4390": "fill", "4399": "work", "5347": "female", "6509": "be-fruitful",
    "6635 a": "host", "6754": "image", "6942": "sanctify", "7235 a": "multiply",
    "7287 a": "rule-over", "7430": "creep", "7431": "creeper", "7637": "seventh",
    "7673 a": "cease", "8345": "sixth", "8577 b": "sea-monster", "929": "livestock",
    # high-frequency curation (2026-07-28): divine name + core verbs
    "3068": "YHWH", "3069": "YHWH", "8085": "hear", "1696": "speak", "5375": "lift/carry",
    "935": "come/bring", "3318": "go-out/bring-forth", "5927": "go-up", "7126": "bring-near",
    "1121 a": "son", "1121": "son", "4480 a": "from", "4480": "from", "1241": "herd",
    "7133 a": "offering", "6629": "flock", "413": "to", "834": "which", "3808": "not",
}

PAREN = re.compile(r"\([^)]*\)")


def clean_gloss(s: str) -> str:
    s = PAREN.sub("", s)
    s = re.sub(r"\[[^\]]*\]", "", s)
    s = s.replace("×", " ").replace(";", ",")
    for part in s.split(","):
        g = part.strip().strip(".").strip()
        g = re.sub(r"^(a|an|the|to|be|i\.e\.|specifically|properly|figuratively)\s+", "", g, flags=re.I)
        g = g.strip()
        if g and not g.startswith("-") and len(g) > 1 and "[" not in g and "]" not in g:
            return g.replace(" ", "-")[:28]
    return ""


def simple_xlit(x: str) -> str:
    x = unicodedata.normalize("NFD", x)
    x = "".join(c for c in x if not unicodedata.combining(c))
    return x.replace("ʼ", "'").replace("ʻ", "'")


def main():
    con = sqlite3.connect(ROOT / "torah_grok.sqlite")
    lemmas = sorted({r[0] for r in con.execute(
        "SELECT DISTINCT lemma_seg FROM segments WHERE morph_seg NOT LIKE 'S%'")}
        - {"b", "c", "d", "l", "m", "i", "k", "s", ""})
    strongs = json.load(open(ROOT / "Data" / "strongs_hebrew_dictionary.json", encoding="utf-8"))

    OUT.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Lexicon v1 — whole-Torah gloss table (EN-AID only, never derivation source)",
        "# Provenance: OSHB lemma tags → Strong's Hebrew dictionary (openscriptures,",
        "# public domain) = #IMPOSED external aid, auto-extracted first KJV gloss;",
        "# src: hand = curated (overrides auto). Generated 2026-07-28 by",
        "# artifacts/generate_lexicon_v1.py — regenerate, don't hand-edit auto rows.",
        "meta:",
        "  version: v1",
        "  date: 2026-07-28",
        "  strongs_entries: %d" % len(strongs),
        "prefixes:  # single-letter morphemes riding on words",
        "  b: in",
        "  c: and",
        "  d: the",
        "  l: to",
        "  m: from",
        "  i: the",
        "  k: like",
        "  s: which",
        "suffix_pronouns:",
        "  1cs: me/my",
        "  1cp: us/our",
        "  2ms: you/your",
        "  2fs: you/your",
        "  2mp: you/your (pl)",
        "  3ms: him/its",
        "  3fs: her/its",
        "  3mp: them/their",
        "  3fp: them/their",
        "entries:",
    ]
    n_hand = n_auto = n_missing = 0
    for lem in lemmas:
        num = lem.split()[0]
        s = strongs.get(f"H{num}", {})
        he = s.get("lemma", "")
        tr = simple_xlit(s.get("xlit", ""))
        if lem in HAND:
            en, src = HAND[lem], "hand"
            n_hand += 1
        else:
            en = clean_gloss(s.get("kjv_def", "")) or clean_gloss(s.get("strongs_def", ""))
            src = f"strongs-H{num}"
            if en:
                n_auto += 1
            else:
                en, src = "?", "missing"
                n_missing += 1
        esc = lambda v: '"' + str(v).replace('"', "'") + '"'
        lines.append(f'  "{lem}": {{he: {esc(he)}, translit: {esc(tr)}, en: {esc(en)}, src: {esc(src)}}}')
    # hand entries not present in Torah segments (keep anyway)
    for lem, en in HAND.items():
        if lem not in lemmas:
            num = lem.split()[0]
            s = strongs.get(f"H{num}", {})
            lines.append(f'  "{lem}": {{he: "{s.get("lemma","")}", translit: "{simple_xlit(s.get("xlit",""))}", en: "{en}", src: "hand"}}')
    (OUT / "lexicon.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (OUT.parent / "CURRENT").write_text("v1\n")
    print(f"wrote {OUT/'lexicon.yaml'}: {len(lemmas)} lemmas · hand={n_hand} auto={n_auto} missing={n_missing}")


if __name__ == "__main__":
    main()
