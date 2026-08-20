#!/usr/bin/env python3
"""
gloss_db.py — word-by-word English for the display layer (Pre-Code).

Owner's absolute rule: no Hebrew anywhere without English inline. Units
frozen before gen_26 carry authored per-word tables (tree_coverage);
later units do not. This module supplies the missing words WITHOUT
touching frozen files: per-word English from the pinned SNAPSHOT DB's
gloss column, corrected by an authored override table
(logic/glosses/word_gloss_overrides.yaml), with a unit's own
tree_coverage words taking precedence where present.

Used by render_unit_py.py:
  set_unit_tree(unit)          -> load the unit's authored word table
  translate_span(he, ref)      -> interlinear English for a quoted span
  build_translit_gloss(refs)   -> translit-core -> en map layered under
                                  step_unit.GLOSS_UNIT
  write_audit(path)            -> dump every span translated this run
"""
import re
import sqlite3
from pathlib import Path

import sys as _vsys; from pathlib import Path as _VP; _vsys.path.insert(0, str(_VP(__file__).resolve().parent / "vendor"))
import yaml

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "source-snapshot.sqlite"
OVERRIDES_PATH = ROOT / "logic" / "glosses" / "word_gloss_overrides.yaml"

_POINTING = re.compile(r"[֑-ׇ]")   # accents + vowels + dots
_DROP = re.compile(r"[׀׃׆׀׃]")  # paseq, sof-pasuq
_db = None
_overrides = None
_verse_cache = {}
_tree_words = {}      # ref -> {plain: en} from the unit's tree_coverage
_span_audit = []      # (ref, he, en) for review
_miss_audit = []


def _conn():
    global _db
    if _db is None:
        _db = sqlite3.connect(str(DB_PATH))
    return _db


def _load_overrides():
    global _overrides
    if _overrides is None:
        if OVERRIDES_PATH.exists():
            d = yaml.safe_load(OVERRIDES_PATH.read_text(encoding="utf-8")) or {}
        else:
            d = {}
        _overrides = {"by_gloss": d.get("by_gloss") or {},
                      "replace": [tuple(p) for p in (d.get("replace") or [])],
                      "by_ref": d.get("by_ref") or {},
                      "by_skeleton": d.get("by_skeleton") or {}}
    return _overrides


def _fix_gloss(en):
    """Exact by_gloss override, else the ordered substring fixes."""
    ov = _load_overrides()
    if en in ov["by_gloss"]:
        return ov["by_gloss"][en]
    for frm, to in ov["replace"]:
        if frm in en:
            en = en.replace(frm, to)
    return en


def norm_plain(s):
    """Accented or pointed Hebrew -> bare consonantal skeleton."""
    return _DROP.sub("", _POINTING.sub("", s)).replace("/", "").strip()


def span_tokens(fragment):
    """Split a span fragment into consonantal tokens (maqqef = joiner).
    Non-Hebrew notation inside spans (arrows, parens, dots) is dropped."""
    out = []
    for chunk in fragment.replace("־", " ").split():
        t = re.sub(r"[^א-ת]", "", norm_plain(chunk))
        if t:
            out.append(t)
    return out


def _ref_parts(ref):
    """'Gen.41.1' -> (Gen, 41, 1, 1); 'Gen.10.2-5' -> (Gen, 10, 2, 5)."""
    book, ch, vs = ref.split(".")
    lo, _, hi = vs.partition("-")
    return book, int(ch), int(lo), int(hi or lo)


def verse_words(ref):
    """[(plain, translit, en)] for one verse (or verse range), overrides
    applied. Range refs concatenate their verses' words in order."""
    if ref in _verse_cache:
        return _verse_cache[ref]
    ov = _load_overrides()
    book, ch, lo, hi = _ref_parts(ref)
    out = []
    for vs in range(lo, hi + 1):
        rows = _conn().execute(
            "SELECT w.idx, w.he_plain, w.translit, w.gloss FROM words w "
            "JOIN verses v ON w.verse_id=v.id "
            "WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx",
            (book, ch, vs)).fetchall()
        for idx, plain, translit, gloss in rows:
            skel = norm_plain(plain or "")
            en = ov["by_skeleton"].get(skel) or _fix_gloss(str(gloss or ""))
            en = ov["by_ref"].get("%s.%d.%d:%d" % (book, ch, vs, idx), en)
            out.append((skel, translit or "", en))
    _verse_cache[ref] = out
    return out


def _word_en(ref, i):
    """English for verse word i — the unit's authored table wins."""
    plain, _tr, en = verse_words(ref)[i]
    tree = _tree_words.get(ref)
    if tree and plain in tree:
        return tree[plain]
    return en


def _match_run(toks, words):
    """First index where toks appear consecutively in the verse words."""
    plains = [w[0] for w in words]
    n = len(toks)
    for i in range(len(plains) - n + 1):
        if plains[i:i + n] == toks:
            return i
    return -1


def _lookup_anywhere(plain):
    """Corpus-wide most-common gloss for a bare skeleton (last resort);
    retries without a leading vav ('and-') for plene/joined spellings."""
    ov = _load_overrides()
    if plain in ov["by_skeleton"]:
        return ov["by_skeleton"][plain]
    row = _conn().execute(
        "SELECT w.gloss FROM words w "
        "WHERE replace(w.he_plain,'/','')=? "
        "GROUP BY w.gloss ORDER BY count(*) DESC LIMIT 1",
        (plain,)).fetchone()
    if row and row[0]:
        return _fix_gloss(row[0])
    if plain.startswith("ו") and len(plain) > 2:
        g = _lookup_anywhere(plain[1:])
        if g:
            return "and-" + g
    return None


def translate_span(he, ref):
    """Interlinear English for one quoted span (fragments join on …)."""
    parts = []
    for fragment in str(he).replace("\n", " ").split("…"):
        toks = span_tokens(fragment)
        if not toks:
            continue
        words = verse_words(ref)
        i = _match_run(toks, words)
        if i >= 0:
            ens = [_word_en(ref, i + k) for k in range(len(toks))]
        else:
            ens = []
            plains = [w[0] for w in words]
            for t in toks:
                if t in plains:
                    ens.append(_word_en(ref, plains.index(t)))
                else:
                    g = _lookup_anywhere(t)
                    ens.append(g or t)
                    if not g:
                        _miss_audit.append((ref, t))
        parts.append(" ".join(e for e in ens if e))
    en = " … ".join(parts)
    _span_audit.append((ref, str(he).replace("\n", " "), en))
    return en


def set_unit_tree(unit):
    """Load the unit's authored tree_coverage words (highest precedence)."""
    _tree_words.clear()
    for verse in (unit.get("tree_coverage") or {}).get("verses", []):
        ref = verse.get("ref", "")
        m = {}
        for w in verse.get("words", []):
            plain = norm_plain(str(w.get("he", "")))
            en = _fix_gloss(str(w.get("en", "")))
            if plain and en and plain not in m:
                m[plain] = en
        if m:
            _tree_words[ref] = m


_TR_PRE = ("va-", "ve-", "ha-", "la-", "le-", "be-", "mi-", "me-", "u-", "ke-")
_EN_PRE = ("and-", "the-", "to-", "in-", "from-", "for-", "like-")


def build_translit_gloss(refs):
    """translit-core -> en map from the DB over the unit's verses (the
    layer under any authored tree_coverage map in GLOSS_UNIT)."""
    g = {}
    for ref in refs:
        for _plain, tr, en in verse_words(ref):
            tr, en = str(tr), str(en)
            changed = True
            while changed:
                changed = False
                for p in _TR_PRE:
                    if tr.startswith(p):
                        tr, changed = tr[len(p):], True
                for p in _EN_PRE:
                    if en.startswith(p):
                        en, changed = en[len(p):], True
            if not tr or not en:
                continue
            for key in (tr.replace("-", "_").strip("_"), tr):
                if key and key not in g:
                    g[key] = en
    return g


def write_audit(path):
    with open(path, "w", encoding="utf-8") as f:
        for ref, he, en in _span_audit:
            f.write("%s\t%s\t%s\n" % (ref, he, en))
        if _miss_audit:
            f.write("\n# MISSES (no gloss found)\n")
            for ref, t in _miss_audit:
                f.write("%s\t%s\n" % (ref, t))
    return len(_span_audit), len(_miss_audit)
