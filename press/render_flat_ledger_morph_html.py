#!/usr/bin/env python3
"""
Render FLAT + LEAF LEDGER + MORPH (morpheme-level OSHB) HTML report.

Format spec: logic/Parse_tree_2026-07-27/MOCKUP_flat_ledger_oshb_morph_2026-07-27.md
Structure = ta'amim v3 trees (taamim_tree_parse.py). Morph = OSHB @lemma/@morph
(#IMPOSED labeled aid). English glosses/translit = EN-AID only, never derivation source.

Usage: python3 press/render_flat_ledger_morph_html.py Gen 1 1 20 out.html
"""
import html
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import sys as _vsys; from pathlib import Path as _VP; _vsys.path.insert(0, str(_VP(__file__).resolve().parent / "vendor"))
import yaml

ROOT = Path(__file__).resolve().parents[1]  # repo root (file lives at logic/<topic>/)

# ---------------------------------------------------------------- lexicon (versioned)
# Loaded from logic/lexicon/<CURRENT>/lexicon.yaml — EN-AID glosses, #IMPOSED
# provenance recorded in the file. Hand entries override Strong's auto glosses.
LEX_DIR = ROOT / "logic" / "lexicon"
LEX_VERSION = (LEX_DIR / "CURRENT").read_text().strip()
_lexdoc = yaml.safe_load((LEX_DIR / LEX_VERSION / "lexicon.yaml").read_text(encoding="utf-8"))
PREFIX_LEMMA = _lexdoc["prefixes"]
SUFFIX_GLOSS = {str(k): v for k, v in _lexdoc["suffix_pronouns"].items()}
LEX_FULL = _lexdoc["entries"]
LEX = {k: v["en"] for k, v in LEX_FULL.items()}

VERSE_EN = {
    (1, 1): "In the beginning God created the heavens and the earth.",
    (1, 2): "The earth was formless and void, with darkness over the deep, and the spirit of God hovering over the waters.",
    (1, 3): "And God said, Let there be light — and there was light.",
    (1, 4): "God saw that the light was good, and God divided the light from the darkness.",
    (1, 5): "God called the light Day and the darkness Night; evening and morning — day one.",
    (1, 6): "God said: let there be a firmament amid the waters, dividing waters from waters.",
    (1, 7): "God made the firmament and divided the waters beneath it from the waters above it — and it was so.",
    (1, 8): "God called the firmament Heavens; evening and morning — a second day.",
    (1, 9): "God said: let the waters under the heavens gather to one place, and let the dry land appear — and it was so.",
    (1, 10): "God called the dry land Earth and the gathered waters Seas; and God saw that it was good.",
    (1, 11): "God said: let the earth sprout grass, seed-bearing herb, and fruit trees bearing fruit by kind with their seed in them — and it was so.",
    (1, 12): "The earth brought forth grass, seed-bearing herb by kind, and trees bearing fruit with seed by kind; and God saw that it was good.",
    (1, 13): "Evening and morning — a third day.",
    (1, 14): "God said: let there be lights in the firmament of the heavens to divide day from night; they shall serve for signs, seasons, days, and years.",
    (1, 15): "And they shall be lights in the firmament of the heavens to give light on the earth — and it was so.",
    (1, 16): "God made the two great lights — the greater to rule the day, the smaller to rule the night — and the stars.",
    (1, 17): "God set them in the firmament of the heavens to give light on the earth,",
    (1, 18): "and to rule the day and the night, and to divide the light from the darkness; and God saw that it was good.",
    (1, 19): "Evening and morning — a fourth day.",
    (1, 20): "God said: let the waters swarm with living creatures, and let flying creatures fly over the earth across the face of the firmament of the heavens.",
    (1, 21): "God created the great sea-creatures, every living being that moves, with which the waters swarmed, by their kinds, and every winged flying creature by its kind; and God saw that it was good.",
    (1, 22): "God blessed them, saying: be fruitful and multiply and fill the waters in the seas, and let the flying creatures multiply on the earth.",
    (1, 23): "Evening and morning — a fifth day.",
    (1, 24): "God said: let the earth bring forth living beings by their kinds — livestock, creepers, and wild animals of the earth by their kinds — and it was so.",
    (1, 25): "God made the wild animals by their kinds, the livestock by its kind, and every creeper of the ground by its kind; and God saw that it was good.",
    (1, 26): "God said: let us make a human in our image, after our likeness; and let them rule the fish of the sea, the flying creatures of the heavens, the livestock, all the earth, and every creeper that creeps on the earth.",
    (1, 27): "God created the human in his image; in the image of God he created him; male and female he created them.",
    (1, 28): "God blessed them, and God said to them: be fruitful and multiply, fill the earth and subdue it, and rule the fish of the sea, the flying creatures of the heavens, and every living thing that creeps on the earth.",
    (1, 29): "God said: behold, I have given you every seed-bearing herb on the face of all the earth, and every tree with seed-bearing tree-fruit — for you it shall be for food.",
    (1, 30): "And for every wild animal, every flying creature of the heavens, and every creeper on the earth with a living soul in it — every green herb for food; and it was so.",
    (1, 31): "God saw all that he had made, and behold: very good. Evening and morning — the sixth day.",
    (2, 1): "The heavens and the earth were completed, and all their host.",
    (2, 2): "God completed on the seventh day his work which he had made, and he ceased on the seventh day from all his work which he had made.",
    (2, 3): "God blessed the seventh day and sanctified it, for on it he ceased from all his work which God had created to make.",
}

# ---------------------------------------------------------------- morph decode
STEM = {"q": "qal", "N": "niphal", "p": "piel", "P": "pual", "h": "hifil", "H": "hofal", "t": "hitpael"}
VFORM = {
    "p": "perfect", "q": "weqatal (sequential)", "i": "imperfect", "w": "wayyiqtol (narrative past)",
    "h": "cohortative", "j": "jussive", "v": "imperative", "r": "participle", "s": "passive participle",
    "a": "infinitive absolute", "c": "infinitive construct",
}
GENDER = {"m": "masc", "f": "fem", "b": "either-gender", "c": "common"}
NUMBER = {"s": "singular", "p": "plural", "d": "dual"}
STATE = {"a": "absolute", "c": "construct", "d": "determined"}
PERSON = {"1": "1st", "2": "2nd", "3": "3rd"}


def decode_morph(code: str) -> str:
    """Decode one OSHB morph segment (no leading H) to English."""
    if not code:
        return "?"
    t = code[0]
    rest = code[1:]
    if t == "C":
        return "conjunction"
    if t == "D":
        return "adverb"
    if t == "R":
        return "preposition" + (" (definite)" if rest == "d" else "")
    if t == "T":
        return {"d": "particle: definite article", "o": "particle: object marker",
                "i": "particle: interrogative", "n": "particle: negative",
                "r": "particle: relative", "a": "particle: affirmation"}.get(rest, "particle")
    if t == "S":
        kind = {"p": "pronoun suffix", "d": "directional suffix", "h": "paragogic suffix", "n": "paragogic nun"}.get(rest[:1], "suffix")
        pgn = rest[1:]
        gloss = SUFFIX_GLOSS.get(pgn, "")
        return f"{kind} · {PERSON.get(pgn[:1],'')} {GENDER.get(pgn[1:2],'')} {NUMBER.get(pgn[2:3],'')} {('— ' + gloss) if gloss else ''}".strip()
    if t == "N":
        if rest[:1] == "p":
            return "proper name"
        r = rest[1:] if rest[:1] == "c" else rest
        parts = ["noun", "common" if rest[:1] == "c" else ""]
        if len(r) > 0:
            parts.append(GENDER.get(r[0], ""))
        if len(r) > 1:
            parts.append(NUMBER.get(r[1], ""))
        if len(r) > 2:
            parts.append(STATE.get(r[2], ""))
        return " · ".join(p for p in parts if p)
    if t == "A":
        parts = ["adjective"]
        if len(rest) > 0:
            parts.append(GENDER.get(rest[0], ""))
        if len(rest) > 1:
            parts.append(NUMBER.get(rest[1], ""))
        if len(rest) > 2:
            parts.append(STATE.get(rest[2], ""))
        return " · ".join(p for p in parts if p)
    if t == "P":
        return "pronoun"
    if t == "V":
        parts = ["verb", STEM.get(rest[:1], rest[:1])]
        form = rest[1:2]
        parts.append(VFORM.get(form, form))
        pgn = rest[2:]
        if form in ("r", "s"):
            if len(pgn) > 0:
                parts.append(GENDER.get(pgn[0], ""))
            if len(pgn) > 1:
                parts.append(NUMBER.get(pgn[1], ""))
        elif pgn:
            parts.append(f"{PERSON.get(pgn[:1],'')} {GENDER.get(pgn[1:2],'')} {NUMBER.get(pgn[2:3],'')}".strip())
        return " · ".join(p for p in parts if p)
    return code


# ---------------------------------------------------------------- transliteration
CONS = {
    "א": "", "ב": "v", "ג": "g", "ד": "d", "ה": "h", "ו": "v", "ז": "z", "ח": "ch",
    "ט": "t", "י": "y", "כ": "kh", "ך": "kh", "ל": "l", "מ": "m", "ם": "m", "נ": "n",
    "ן": "n", "ס": "s", "ע": "", "פ": "f", "ף": "f", "צ": "tz", "ץ": "tz", "ק": "q",
    "ר": "r", "ש": "sh", "ת": "t",
}
DAGESH_HARD = {"ב": "b", "כ": "k", "ך": "k", "פ": "p", "ת": "t", "ג": "g", "ד": "d"}
VOWEL = {
    "ְ": "e",   # shva (vocal heuristic)
    "ֱ": "e", "ֲ": "a", "ֳ": "o",  # hatafs
    "ִ": "i", "ֵ": "e", "ֶ": "e", "ַ": "a", "ָ": "a",
    "ֹ": "o", "ֺ": "o", "ֻ": "u",
}
SHVA = "ְ"
DAGESH = "ּ"
SHIN_DOT = "ׁ"
SIN_DOT = "ׂ"
HOLAM = "ֹ"

TRANSLIT_OVERRIDE = {
    "יהוה": "YHWH", "אלהים": "Elohim", "אל": "el", "את": "et", "כי": "ki",
}


def translit_segment(seg: str, is_last_seg: bool) -> str:
    """Rule-based transliteration of one pointed-Hebrew morpheme segment."""
    plain = "".join(c for c in seg if "א" <= c <= "ת")
    if plain in TRANSLIT_OVERRIDE:
        return TRANSLIT_OVERRIDE[plain]
    # group each base consonant with its trailing marks
    groups = []
    for ch in unicodedata.normalize("NFD", seg):
        if "א" <= ch <= "ת":
            groups.append([ch, set()])
        elif groups:
            groups[-1][1].add(ch)
    out = []
    n = len(groups)
    for gi, (base, marks) in enumerate(groups):
        cons = CONS.get(base, "")
        if base == "ש":
            cons = "s" if SIN_DOT in marks else "sh"
        elif DAGESH in marks and base in DAGESH_HARD:
            cons = DAGESH_HARD[base]
        # matres lectionis
        if base == "ו":
            if DAGESH in marks and not any(v in marks for v in VOWEL):
                out.append("u")          # shuruk
                continue
            if HOLAM in marks:
                out.append("o")          # holam male
                continue
        if base == "י" and not any(v in marks for v in VOWEL) and out and out[-1] and out[-1][-1] in "ie":
            continue                      # yod as mater after i/e
        if base == "ה" and gi == n - 1 and not any(v in marks for v in VOWEL) and is_last_seg:
            continue                      # final silent he
        if base == "א" and not any(v in marks for v in VOWEL) and gi == n - 1:
            out.append("")                # final quiescent alef
            continue
        vowel = ""
        for vm, vt in VOWEL.items():
            if vm in marks:
                vowel = vt
                break
        if SHVA in marks:
            vowel = "e" if gi == 0 else ""  # vocal at segment start, else silent
        out.append(cons + vowel)
    return "".join(out) or plain


# ---------------------------------------------------------------- data loading
def load_oshb_words(book_xml: Path, chapter: int, verse: int):
    xml = book_xml.read_text(encoding="utf-8")
    m = re.search(rf'<verse osisID="[A-Za-z]+\.{chapter}\.{verse}">(.*?)</verse>', xml, re.S)
    if not m:
        raise SystemExit(f"verse {chapter}:{verse} not found")
    body = m.group(1)
    words = []
    token_re = re.compile(r'<w [^>]*?lemma="([^"]*)"[^>]*?morph="([^"]*)"[^>]*>(.*?)</w>|<seg type="x-maqqef">', re.S)
    for tok in token_re.finditer(body):
        if tok.group(0).startswith("<seg"):
            if words:
                words[-1]["maqqef_after"] = True
            continue
        lemma, morph, text = tok.group(1), tok.group(2), tok.group(3)
        # strip nested markup (e.g. <seg type="x-large"> around the big letters of
        # the Shema, Lev 11:42's vav, Num 27:5's nun) but keep its letter content
        text = re.sub(r"<[^>]+>", "", text)
        words.append({"lemma": lemma, "morph": morph, "text": text.strip(), "maqqef_after": False})
    return words


def parse_verse(osis_id: str):
    out = subprocess.run([sys.executable, str(ROOT / "taamim_tree_parse.py"), osis_id],
                         capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def collect_leaves(tree):
    """Depth-first leaves with L/R path strings."""
    leaves = []

    def walk(node, path):
        if node["kind"] == "leaf":
            leaves.append({"indices": node["word_indices"], "mark": node["mark_id"],
                           "rank": node["rank"], "path": path or "ROOT"})
            return
        for i, child in enumerate(node["children"]):
            walk(child, path + ("L" if i == 0 else "R"))

    walk(tree, "")
    return leaves


# ---------------------------------------------------------------- glossing
def seg_lemma_gloss(seg_lemma: str, morph_seg: str) -> str:
    seg_lemma = seg_lemma.strip()
    if morph_seg.startswith("S"):
        pgn = morph_seg[2:]
        return SUFFIX_GLOSS.get(pgn, "suffix")
    if seg_lemma in PREFIX_LEMMA:
        return PREFIX_LEMMA[seg_lemma]
    return LEX.get(seg_lemma, "?")


def word_segments(word):
    """Split OSHB word into aligned (text, lemma, morph) segments."""
    texts = word["text"].split("/")
    lemmas = word["lemma"].split("/")
    morphs = word["morph"][1:].split("/")  # drop leading H (language marker)
    # OSHB suffix segments share the final lemma slot; pad lemma list if needed
    while len(lemmas) < len(texts):
        lemmas.append(lemmas[-1])
    while len(morphs) < len(texts):
        morphs.append(morphs[-1])
    return list(zip(texts, lemmas, morphs))


def word_gloss(word) -> str:
    return "-".join(seg_lemma_gloss(l, m) for _, l, m in word_segments(word))


def word_translit(word) -> str:
    segs = word_segments(word)
    return "-".join(translit_segment(t, i == len(segs) - 1) for i, (t, _, _) in enumerate(segs))


# ---------------------------------------------------------------- role rules (versioned)
# Loaded from logic/role_rules/<CURRENT>/rules.yaml. Auto illustrative labels,
# NOT logic derivation. Error -> new rules version, never silent edits.
RR_DIR = ROOT / "logic" / "role_rules"
RR_VERSION = (RR_DIR / "CURRENT").read_text().strip()
_rrdoc = yaml.safe_load((RR_DIR / RR_VERSION / "rules.yaml").read_text(encoding="utf-8"))
ROLE_RULESET = f"role_rules-{_rrdoc['meta']['version']}-{_rrdoc['meta']['date']}"
FRAMES = _rrdoc["frames"]
NIPHAL_IRREG = _rrdoc["niphal_irregular"]
ORD_GLOSS = {str(k): v for k, v in _rrdoc["ord_gloss"].items()}
VERBLESS = _rrdoc["verbless"]


def _compile_rule(spec):
    any_l = set(spec.get("any", []))
    all_l = set(spec.get("all", []))
    any_m = tuple(spec.get("any_morph", []))
    not_l = set(spec.get("not_any", []))
    not_m = tuple(spec.get("not_morph", []))

    def test(lemset, morphset):
        if any_l and not (lemset & any_l):
            return False
        if not all_l <= lemset:
            return False
        if any_m and not any(m.startswith(pfx) for m in morphset for pfx in any_m):
            return False
        if lemset & not_l:
            return False
        if not_m and any(m.startswith(pfx) for m in morphset for pfx in not_m):
            return False
        return True

    return test, spec["role"]


ROLE_RULES = [_compile_rule(s) for s in _rrdoc["lemma_rules"]]


def _semantic_role(lemset, morphset):
    for test, role in ROLE_RULES:
        if test(lemset, morphset):
            return role
    return None


def leaf_role(segs):
    """Role = lemma layer (ROLE_RULES) framed by the verb-form layer (OSHB morph).

    segs = ordered [(text, lemma, morph), ...] for the leaf.
    Form frames (mechanical, from the OSHB form letter):
      CMD  = jussive ("let it…")      CMD! = imperative      CMD? = imperfect in
      command speech (hypothesis)      THEN = weqatal ("and it shall…")
      PURPOSE = ל + infinitive construct    ONGOING = participle
      EVENT / STATE = wayyiqtol / perfect fallback when no lemma rule matched
    Verbless leaves: OBJ_FRAME (et), BETWEEN, REL, PREP, DAY-COUNT, NP by particles
    and phrase shape. Decorations: +et-obj, +eval(good).
    """
    lemset = {l.strip() for _, l, _ in segs}
    morphset = {m for _, _, m in segs}
    base = _semantic_role(lemset, morphset)

    def vgloss(lemma, morph):
        g = LEX.get(lemma, "?")
        if morph[1:2] == "N":  # niphal ≈ passive/middle voice of the root
            g = NIPHAL_IRREG.get(g, g if g.startswith("be-") else "be-" + g)
        return g

    heads = [seg_lemma_gloss(l, m) for _, l, m in segs
             if m[:1] in ("N", "A") and not m.startswith("S")]
    head = "·".join(heads[:3]) if heads else "…"

    verb = next(((l.strip(), m) for _, l, m in segs if m.startswith("V")), None)
    if verb:
        vlem, vm = verb
        form = vm[2:3]
        vg = vgloss(vlem, vm)
        frame = {"c": "PURPOSE", "r": "ONGOING", "s": "ONGOING",
                 "j": "CMD", "v": "CMD!", "i": "CMD?", "q": "THEN",
                 "h": "CMD-US"}.get(form)  # cohortative: "let US…" (na'aseh)
        if frame:
            role = f"{frame}({vg})"
        elif base:
            role = base
        else:
            role = f"EVENT({vg})" if form == "w" else f"STATE({vg})"
    else:
        if VERBLESS["between"] in lemset:
            role = f"BETWEEN({head})"
        elif VERBLESS["relative"] in lemset:
            role = f"REL({base or head})"
        elif base == "OBJ_FRAME":
            role = f"OBJ_FRAME({head})"
        elif base == "PREP_PHRASE":
            prep = next((seg_lemma_gloss(l, m) for _, l, m in segs if m[:1] == "R"), "?")
            role = f"PREP({prep}·{head})"
        elif base == "ORDINAL/DAY-COUNT":
            n = next((ORD_GLOSS[o] for o in ORD_GLOSS if o in lemset), "?")
            role = f"DAY-COUNT({n})" if VERBLESS["day_lemma"] in lemset else f"NP({head})"
        elif base:
            role = base
        elif VERBLESS["intensifier"] in lemset:
            role = "INTENSIFIER(very)"      # me'od as its own brick (Gen 1:31, on the etnachta)
        elif VERBLESS["present"] in lemset:
            role = "PRESENT(behold)"        # hinneh presentative
        elif heads:
            role = f"NP({head})"
        else:
            role = "—"

    if "853" in lemset and "OBJ" not in role:
        role += " +et-obj"
    if "2896 a" in lemset and "EVAL" not in role and "good" not in role:
        role += " +eval(good)"
    return role


# ---------------------------------------------------------------- HTML
CSS = """
:root { --bg:#ffffff; --fg:#1f2937; --mut:#6b7280; --line:#d7d3c8; --acc:#8a6d1a;
        --chip:#f5f2ea; --hd:#f0ecdf; --code:#f7f5ee; }
* { box-sizing: border-box; }
body { margin:0; padding:2rem 1rem 6rem; background:var(--bg); color:var(--fg);
       font:15px/1.55 "Charter","Georgia",serif; }
main { max-width: 1080px; margin:0 auto; }
h1 { font-size:1.5rem; } h2 { font-size:1.2rem; margin-top:3rem; border-bottom:2px solid var(--acc);
     padding-bottom:.3rem;} h3 { font-size:.95rem; letter-spacing:.06em; text-transform:uppercase;
     color:var(--mut); margin:1.4rem 0 .5rem; }
.meta { color:var(--mut); font-size:.85rem; }
.banner { background:var(--chip); border:1px solid var(--line); border-radius:8px;
          padding:.8rem 1rem; font-size:.85rem; margin:1rem 0 2rem; }
.flat { border-left:3px solid var(--acc); padding:.6rem .9rem; background:var(--code);
        border-radius:0 8px 8px 0; margin:.6rem 0 1rem; overflow-x:auto; }
.flat .row { margin:.25rem 0; white-space:nowrap; }
.flat .lab { display:inline-block; width:2.2rem; color:var(--mut); font:.75rem/1 monospace; }
.flat .he-row { direction:rtl; text-align:left; font-size:1.25rem; }
.flat .he-row .lab { direction:ltr; float:left; margin-top:.45rem;}
.brick { display:inline-block; background:var(--chip); border:1px solid var(--line);
         border-radius:6px; padding:.05rem .45rem; margin:.1rem .15rem; }
.guide { color:var(--mut); font-size:.78rem; margin-top:.4rem; }
.fen { font-style:italic; color:var(--mut); margin:.2rem 0 .8rem; }
table { border-collapse:collapse; width:100%; font-size:.83rem; margin:.4rem 0 1.2rem; }
th { background:var(--hd); text-align:left; font-size:.72rem; letter-spacing:.05em;
     text-transform:uppercase; }
th,td { border:1px solid var(--line); padding:.3rem .5rem; vertical-align:top; }
td.he { font-size:1.1rem; white-space:nowrap; direction:rtl; text-align:right;}
td.code { font-family:monospace; font-size:.78rem; white-space:nowrap; }
tr.bstart td { border-top:2px solid var(--acc); }
.wrap { overflow-x:auto; }
nav { font-size:.85rem; line-height:2; } nav a { color:var(--acc); text-decoration:none;
      margin-right:.7rem; } nav a:hover { text-decoration:underline; }
.tag { font-family:monospace; font-size:.75rem; background:var(--chip);
       border-radius:4px; padding:0 .35rem; }
"""


def esc(s):
    return html.escape(str(s), quote=False)


def render_verse(book, chapter, vnum, oshb, parsed):
    words = parsed["words"]
    assert len(words) == len(oshb), f"word count mismatch {book}.{chapter}.{vnum}"
    leaves = collect_leaves(parsed["tree"])
    nb = len(leaves)
    osis = f"{book}.{chapter}.{vnum}"

    he_chips, tr_chips, en_chips = [], [], []
    for li, leaf in enumerate(leaves):
        idx = leaf["indices"]
        he = ""
        for j, i in enumerate(idx):
            he += oshb[i]["text"].replace("/", "")
            if j < len(idx) - 1:
                he += "־" if oshb[i]["maqqef_after"] else " "
        tr = " ".join(word_translit(oshb[i]) for i in idx)
        en = " ".join(word_gloss(oshb[i]) for i in idx)
        he_chips.append(f'<span class="brick">(⁨{esc(he)}⁩)</span>')
        tr_chips.append(f'<span class="brick">({esc(tr)})</span>')
        en_chips.append(f'<span class="brick">({esc(en)})</span>')
        leaf["he"], leaf["tr"], leaf["en"] = he, tr, en

    out = [f'<h2 id="v{chapter}_{vnum}">Gen {chapter}:{vnum}</h2>']
    out.append(f'<div class="meta">FLAT · taamim {esc(parsed["rule_set_version"])} · {esc(parsed["system"])} · '
               f'{len(words)} words → {nb} leaves · parser status: {esc(parsed["status"])}</div>')
    out.append(f'<div class="fen">en: “{esc(VERSE_EN.get((chapter, vnum), ""))}”</div>')
    out.append('<div class="flat">')
    out.append(f'<div class="row he-row"><span class="lab">he:</span> {" ".join(he_chips)}</div>')
    out.append(f'<div class="row"><span class="lab">tr:</span> {" ".join(tr_chips)}</div>')
    out.append(f'<div class="row"><span class="lab">en:</span> {" ".join(en_chips)}</div>')
    out.append(f'<div class="guide">B0 … B{nb-1} in reading order — Hebrew row runs right-to-left '
               f'(B0 is the right-most paren); en = literal word glosses, verse line above = free English.</div>')
    out.append('</div>')

    # ---- leaf ledger
    out.append('<h3>Leaf ledger</h3><div class="wrap"><table>')
    out.append('<tr><th>B#</th><th>words</th><th>path</th><th>he</th><th>translit</th><th>en (literal)</th>'
               '<th>end mark · rank</th><th>froze because</th><th>role (auto, illustrative)</th></tr>')
    for li, leaf in enumerate(leaves):
        idx = leaf["indices"]
        wspan = f"w{idx[0]}" if len(idx) == 1 else f"w{idx[0]}–{idx[-1]}"
        if len(idx) == 1:
            froze = "single word"
        else:
            inner = sorted({words[i]["mark_id"] for i in idx[:-1]})
            froze = "only " + ", ".join(inner) + " (conj) inside"
        leaf_segs = []
        for i in idx:
            leaf_segs.extend(word_segments(oshb[i]))
        role = leaf_role(leaf_segs)
        path = "·".join(leaf["path"]) if leaf["path"] != "ROOT" else "ROOT"
        out.append(f'<tr><td><b>B{li}</b></td><td>{wspan}</td><td class="code">{esc(path)}</td>'
                   f'<td class="he">{esc(leaf["he"])}</td><td>{esc(leaf["tr"])}</td><td>{esc(leaf["en"])}</td>'
                   f'<td>{esc(leaf["mark"])} · r{leaf["rank"]}</td><td>{esc(froze)}</td><td>{esc(role)}</td></tr>')
    out.append('</table></div>')

    # ---- morph table
    out.append('<h3>Morph — every word and every morpheme letter (OSHB)</h3><div class="wrap"><table>')
    out.append('<tr><th>B#</th><th>w</th><th>he</th><th>translit</th><th>en</th><th>OSHB code</th>'
               '<th>grammar (English aid)</th></tr>')
    for li, leaf in enumerate(leaves):
        first_row_of_brick = True
        for i in leaf["indices"]:
            segs = word_segments(oshb[i])
            multi = len(segs) > 1
            for si, (t, l, m) in enumerate(segs):
                wid = f"{i}{chr(97+si)}" if multi else f"{i}"
                gram = decode_morph(m)
                lemma = l.strip()
                if lemma in PREFIX_LEMMA and m[:1] in ("C", "R", "T"):
                    gram += " — prefix letter, not a standalone word"
                elif m.startswith("S"):
                    gram += " — suffix letters, not a standalone word"
                elif lemma not in PREFIX_LEMMA and not m.startswith("S"):
                    gram += f' — “{seg_lemma_gloss(lemma, m)}” (H{lemma.split()[0]})'
                cls = ' class="bstart"' if first_row_of_brick else ""
                first_row_of_brick = False
                out.append(f'<tr{cls}><td><b>B{li}</b></td><td class="code">{wid}</td>'
                           f'<td class="he">{esc(t)}</td><td>{esc(translit_segment(t, si == len(segs)-1))}</td>'
                           f'<td>{esc(seg_lemma_gloss(l, m))}</td><td class="code">{esc(m)}</td>'
                           f'<td>{esc(gram)}</td></tr>')
    out.append('</table></div>')
    return "\n".join(out)


def main():
    # spec: either "1 1 20" (chapter v1 v2, legacy) or "1:1-31,2:1-3" (multi-range)
    book = sys.argv[1]
    if len(sys.argv) == 6:
        chapter, v1, v2, outpath = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
        ranges, title_span = [(chapter, v1, v2)], f"{chapter}:{v1}–{v2}"
    else:
        spec, outpath = sys.argv[2], sys.argv[3]
        ranges = []
        for seg in spec.split(","):
            ch, span = seg.split(":")
            a, b = (span.split("-") + [span.split("-")[0]])[:2]
            ranges.append((int(ch), int(a), int(b)))
        title_span = f"{ranges[0][0]}:{ranges[0][1]}–{ranges[-1][0]}:{ranges[-1][2]}"
    xml = ROOT / "shelf" / "sources" / f"{book}.xml"
    sections, toc = [], []
    for chapter, v1, v2 in ranges:
        for v in range(v1, v2 + 1):
            osis = f"{book}.{chapter}.{v}"
            parsed = parse_verse(osis)
            oshb = load_oshb_words(xml, chapter, v)
            sections.append(render_verse(book, chapter, v, oshb, parsed))
            toc.append(f'<a href="#v{chapter}_{v}">{chapter}:{v}</a>')
            print(f"ok {osis}: {len(oshb)} words, status={parsed['status']}")

    page = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gen {title_span} — FLAT · LEDGER · MORPH</title>
<style>{CSS}</style></head><body><main>
<h1>Genesis {title_span} — FLAT parens · LEAF LEDGER · OSHB MORPH</h1>
<div class="meta">Generated 2026-07-28 · structure = ta'amim rules <span class="tag">v3</span>
(<span class="tag">taamim_tree_parse.py</span>) · morphology = OSHB <span class="tag">@lemma/@morph</span>
(#IMPOSED labeled aid) · English &amp; translit = EN-AID only, never derivation source ·
roles = expanded auto heuristics (Gen-1 narrative + frame tags), illustrative only · not binding religious law · not TIR-frozen</div>
<div class="banner"><b>How to read:</b> each verse shows (1) <b>FLAT</b> — the full verse in
Hebrew / transliteration / literal-gloss English with parentheses around each ta'amim leaf brick;
(2) <b>LEAF LEDGER</b> — one row per brick with its tree path and the disjunctive mark that closed it;
(3) <b>MORPH</b> — one row per <i>morpheme segment</i>: prefix letters (ו=and, ה=the, ל=to, ב=in, מ=from)
and pronoun suffixes (־הם=them, ־כם=your-pl) get their own rows. Row ids like <span class="tag">4a/4b</span>
= segments of word 4. Spec: <span class="tag">logic/Parse_tree_2026-07-27/MOCKUP_flat_ledger_oshb_morph_2026-07-27.md</span><br><br>
<b>Role column vocabulary</b> (auto, illustrative — verb-<i>form</i> frames from OSHB morph):
<span class="tag">CMD</span> jussive "let it…" · <span class="tag">CMD!</span> imperative ·
<span class="tag">CMD?</span> imperfect inside command speech (labeled hypothesis, not forced) ·
<span class="tag">THEN</span> weqatal "and it shall…" · <span class="tag">PURPOSE</span> ל+infinitive "in order to…" ·
<span class="tag">ONGOING</span> participle · <span class="tag">EVENT</span>/<span class="tag">STATE</span> wayyiqtol/perfect ·
named verbs (SPEAK, CREATE, NAME, DIVIDE…) = narrative lemma rules. Verbless leaves:
<span class="tag">OBJ_FRAME</span> = has את object-marker (TIR-014) · <span class="tag">BETWEEN</span> = בין pair ·
<span class="tag">REL</span> = אשר clause · <span class="tag">PREP</span>/<span class="tag">NP</span> = phrase shape ·
<span class="tag">+et-obj</span>/<span class="tag">+eval(good)</span> = secondary particles present.</div>
<nav><b>Verses:</b> {' '.join(toc)}</nav>
{''.join(sections)}
</main></body></html>"""
    Path(outpath).write_text(page, encoding="utf-8")
    print("wrote", outpath)


if __name__ == "__main__":
    main()
