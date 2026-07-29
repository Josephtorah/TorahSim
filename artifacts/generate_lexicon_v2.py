#!/usr/bin/env python3
"""
Generate logic/lexicon/v2/lexicon.yaml — whole-Torah gloss table (EN-AID).

v2 over v1 (2026-07-29), per versioned-rules discipline (new dir, no silent edits):
  1. Common words: prefer Strong's *definition* over the KJV usage list — the
     KJV list is ALPHABETICAL, so v1's first-pick gave 'act' for davar (word),
     'an--other' for elleh (these), 'city' for sha'ar (gate), etc.
  2. Proper nouns (detected from the corpus: >50% of a lemma's tokens tagged Np)
     keep KJV-first (it carries familiar English names: Moses, Egypt), with
     '.-Compare-H####' artifacts stripped and xlit fallback for '?' names.
  3. ~100 new hand overrides curated 2026-07-29 from the top-240 frequency list.
Hand overrides always win. English = aid only, never derivation source.
"""
import json
import re
import sqlite3
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "logic" / "lexicon" / "v2"

# ---- v1 hand set (carried forward verbatim) --------------------------------
HAND_V1 = {
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
    "3068": "YHWH", "3069": "YHWH", "8085": "hear", "1696": "speak", "5375": "lift/carry",
    "935": "come/bring", "5927": "go-up", "7126": "bring-near",
    "1121 a": "son", "1121": "son", "4480 a": "from", "4480": "from", "1241": "herd",
    "7133 a": "offering", "6629": "flock", "834": "which", "3808": "not",
}
# ---- v2 curation (2026-07-29): top-240 frequency review — these win over v1 --
HAND_V2 = {
    "1": "father", "376": "man", "398": "eat", "3947": "take", "3027": "hand",
    "2088": "this", "2063": "this", "1004 b": "house", "802": "woman", "5704": "until",
    "4191": "die", "518 a": "if", "854": "with", "3548": "priest", "251": "brother",
    "428": "these", "8033": "there", "176 a": "or", "1697": "word/thing", "8034": "name",
    "6680": "command", "3212": "go", "6944": "holiness", "5869 a": "eye", "168": "tent",
    "5973 a": "with", "5971 a": "people", "834 d": "as/which", "1323": "daughter",
    "7971": "send", "3427": "dwell/sit", "7725": "return", "5650": "servant",
    "1571": "also", "3045": "know", "859 a": "you", "859 d": "you", "5892 b": "city",
    "7760 a": "put/set", "8104": "keep/guard", "5930 a": "burnt-offering",
    "6965 b": "arise", "7218 a": "head", "4294": "staff/tribe", "2568": "five",
    "1320": "flesh", "2403 b": "sin-offering", "6485 a": "count/visit", "4100": "what",
    "5674 a": "pass-over", "369": "there-is-not", "6310": "mouth", "4672": "find",
    "5265": "journey", "1992": "they", "352 a": "ram", "1870": "way/road",
    "7969": "three", "899 b": "garment", "5647": "work/serve", "4503": "grain-offering",
    "4994": "please", "8081": "oil", "4908": "tabernacle", "4264": "camp",
    "408": "do-not", "6963 a": "voice/sound", "3423": "possess/inherit",
    "5221": "strike", "3627": "vessel", "1471 a": "nation", "68": "stone",
    "3381": "go-down", "2583": "encamp", "1980": "walk/go", "6258": "now",
    "5975": "stand", "4941": "judgment", "5656": "service/work", "2421": "live",
    "1285": "covenant", "3372": "fear", "5785": "skin", "4616": "so-that",
    "3722 a": "atone", "5159": "inheritance", "5769": "forever", "2398": "sin",
    "2077": "sacrifice", "5387 a": "prince", "7650": "swear", "3772": "cut",
    "1060": "firstborn", "1616": "sojourner", "3820 a": "heart", "7227 a": "many/great",
    "4687": "commandment", "4639": "deed/work", "801": "fire-offering", "517": "mother",
    "2351": "outside", "7901": "lie-down", "6435": "lest", "1755": "generation",
    "7272": "foot", "5307": "fall", "3709": "palm-of-hand", "8269": "officer",
    "8179": "gate", "2708": "statute", "7223": "first", "5493": "turn-aside",
    "5046": "tell", "6240": "-teen", "5750": "still/again", "1931": "he/it",
}
HAND = {**HAND_V1, **HAND_V2}

PAREN = re.compile(r"\([^)]*\)")
QUALIFIERS = re.compile(
    r"^(properly|by implication|figuratively|causatively|hence|specifically"
    r"|generally|literally|occasionally|euphemistically|morally|adverbially"
    r"|intensively|perhaps properly|probably|i\.e\.|adverb or preposition"
    r"|used (very )?widely|at this time)[, ]+", re.I)
ARTICLES = re.compile(r"^(a|an|the|to|be|so)\s+", re.I)


def clean_def(s: str) -> str:
    """First clause of a Strong's definition -> compact display gloss."""
    s = PAREN.sub("", s or "")
    s = re.sub(r"\[[^\]]*\]", "", s).replace("×", " ").replace("{", "").replace("}", "")
    for clause in s.split(";"):
        g = clause.strip()
        for _ in range(3):
            g = QUALIFIERS.sub("", g).strip(" ,")
        g = g.split(",")[0].strip()
        g = ARTICLES.sub("", g).strip(" .")
        if " or " in g:
            g = g.split(" or ")[0].strip()
        if g and not g.startswith("-") and len(g) > 1:
            return g.replace(" ", "-")[:28]
    return ""


def clean_name(kjv: str, xlit: str) -> str:
    """Proper noun -> familiar English name; strip 'Compare H####' artifacts."""
    s = re.sub(r"[.;,]?\s*[Cc]ompare\s+H?\d+.*$", "", kjv or "")
    s = PAREN.sub("", s)
    m = re.match(r"\s*([A-Z][\w' -]*)", s)
    if m:
        return m.group(1).strip().replace(" ", "-")[:28]
    return (xlit or "").strip().title().replace(" ", "-")[:28] or ""


def simple_xlit(x: str) -> str:
    x = unicodedata.normalize("NFD", x)
    x = "".join(c for c in x if not unicodedata.combining(c))
    return x.replace("ʼ", "'").replace("ʻ", "'")


def main():
    con = sqlite3.connect(ROOT / "torah_grok.sqlite")
    lemmas = sorted({r[0] for r in con.execute(
        "SELECT DISTINCT lemma_seg FROM segments WHERE morph_seg NOT LIKE 'S%'")}
        - {"b", "c", "d", "l", "m", "i", "k", "s", ""})
    np_ratio = {r[0]: r[1] for r in con.execute(
        """SELECT lemma_seg,
                  SUM(CASE WHEN morph_seg LIKE 'Np%' THEN 1 ELSE 0 END)*1.0/COUNT(*)
           FROM segments WHERE morph_seg NOT LIKE 'S%' GROUP BY lemma_seg""")}
    strongs = json.load(open(ROOT / "Data" / "strongs_hebrew_dictionary.json",
                             encoding="utf-8"))

    OUT.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Lexicon v2 — whole-Torah gloss table (EN-AID only, never derivation source)",
        "# v2 2026-07-29: Strong's-definition-first for common words (v1's first-KJV",
        "# pick was alphabetical: 'act' for davar); KJV-name-first for proper nouns",
        "# (corpus Np ratio > 0.5) with Compare-H#### stripped; ~100 new hand rows.",
        "# Generated by artifacts/generate_lexicon_v2.py — regenerate, don't hand-edit.",
        "meta:",
        "  version: v2",
        "  date: 2026-07-29",
        "  strongs_entries: %d" % len(strongs),
        "prefixes:  # single-letter morphemes riding on words",
        "  b: in", "  c: and", "  d: the", "  l: to", "  m: from",
        "  i: the", "  k: like", "  s: which",
        "suffix_pronouns:",
        "  1cs: me/my", "  1cp: us/our", "  2ms: you/your", "  2fs: you/your",
        "  2mp: you/your (pl)", "  3ms: him/its", "  3fs: her/its",
        "  3mp: them/their", "  3fp: them/their",
        "entries:",
    ]
    n_hand = n_auto = n_name = n_missing = 0
    for lem in lemmas:
        num = lem.split()[0]
        s = strongs.get(f"H{num}", {})
        he, tr = s.get("lemma", ""), simple_xlit(s.get("xlit", ""))
        if lem in HAND:
            en, src = HAND[lem], "hand"
            n_hand += 1
        elif np_ratio.get(lem, 0) > 0.5:
            en = clean_name(s.get("kjv_def", ""), tr)
            src = f"strongs-H{num}-name"
            if en:
                n_name += 1
            else:
                en, src = "?", "missing"
                n_missing += 1
        else:
            en = clean_def(s.get("strongs_def", "")) or clean_def(s.get("kjv_def", ""))
            src = f"strongs-H{num}"
            if en:
                n_auto += 1
            else:
                en, src = "?", "missing"
                n_missing += 1
        esc = lambda v: '"' + str(v).replace('"', "'") + '"'
        lines.append(f'  "{lem}": {{he: {esc(he)}, translit: {esc(tr)}, '
                     f'en: {esc(en)}, src: {esc(src)}}}')
    for lem, en in HAND.items():
        if lem not in lemmas:
            num = lem.split()[0]
            s = strongs.get(f"H{num}", {})
            lines.append(f'  "{lem}": {{he: "{s.get("lemma", "")}", '
                         f'translit: "{simple_xlit(s.get("xlit", ""))}", '
                         f'en: "{en}", src: "hand"}}')
    (OUT / "lexicon.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (OUT.parent / "CURRENT").write_text("v2\n")
    print(f"wrote {OUT/'lexicon.yaml'}: {len(lemmas)} lemmas · hand={n_hand} "
          f"auto={n_auto} names={n_name} missing={n_missing} · CURRENT -> v2")


if __name__ == "__main__":
    main()
