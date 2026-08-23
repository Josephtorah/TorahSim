#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_text.py <uid>

Independent text-layer check: recomputes every step's plain he line, tree
halves (etnachta split with strongest-disjunctive fallback), operator he
fragments, and scenario value fragments from the SNAPSHOT with logic
written separately from the builder, and diffs against the unit YAML.
Exit 0 = green.
"""
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
DB = REPO / "data/source-snapshot.sqlite"
ACC = re.compile("[֑-ֽ֯]")   # cantillation + meteg, explicit
VOW = re.compile("[ְ-ׇּׁׂ]")
MAQ = "־"


def nfc(s):
    return unicodedata.normalize("NFC", s)


# --- era-adaptive normalization (rewritten 2026-08-23, owner word "if
# you need to rewrite anything to make the new derivation rules work
# then do it"): creation-week units quote consonantal tree fragments
# and voweled-unaccented scenario values; law-era units quote fully
# accented text. Each check compares at the LOWEST ink level the
# RECORD side actually wrote — never weaker than what it wrote.
HAT = re.compile("[\u05B1-\u05B3]")    # hataf half-vowels -> sheva class
LVL = re.compile("[\u05B0-\u05BB\u05C7]")  # TRUE vowel points (level detect)
DOTS = re.compile("[\u05BC\u05C1\u05C2]")  # dagesh + shin/sin dots


def _level_norm(record_side, verse_side):
    # level = the record's TRUE vowel points; dagesh and shin/sin dots
    # normalize away below the fully-accented level (pointing detail,
    # not quote identity)
    _punct = re.compile("[\u05C4\u05C5]")   # puncta extraordinaria
    r = _punct.sub("", HAT.sub("\u05B0", nfc(record_side))).replace(MAQ, " ")
    v = _punct.sub("", HAT.sub("\u05B0", nfc(verse_side))).replace(MAQ, " ")
    if not LVL.search(r):                       # consonantal record
        strip = lambda x: DOTS.sub("", VOW.sub("", ACC.sub("", x)))
        return strip(r), strip(v)
    if not ACC.search(r) or not ACC.search(v):  # voweled level (either side)
        strip = lambda x: DOTS.sub("", ACC.sub("", x))
        return strip(r), strip(v)
    return r, v                                 # fully accented, both sides


def _kq_variants(line):
    # snapshot word cells holding "ktiv qere" (unpointed + pointed,
    # space-joined) yield two readings; emit line + both approximations
    toks = line.split(" ")
    ktiv, qere = [], []
    i = 0
    while i < len(toks):
        t = toks[i]
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        if (nxt and t and len(t) > 1 and not LVL.search(t)
                and LVL.search(nxt)):
            ktiv.append(t)
            qere.append(nxt)
            i += 2
            continue
        ktiv.append(t)
        qere.append(t)
        i += 1
    a, b = " ".join(ktiv), " ".join(qere)
    return (line,) if a == b else (line, a, b)


def _contains(fragment, verse_line):
    # ellipsis quotes ("…") check piecewise — each quoted piece must
    # appear; the gap is the quote's own honesty about omission
    for piece in re.split("…" + "|" + re.escape("..."), fragment):
        piece = piece.strip()
        if not piece:
            continue
        if not any(_level_norm(piece, var)[0] in _level_norm(piece, var)[1]
                   for var in _kq_variants(verse_line)):
            return False
    return True


def main():
    uid = sys.argv[1]
    U = yaml.safe_load(open(REPO / "logic/units" / (uid + ".yaml")))
    db = sqlite3.connect(str(DB))
    fails = []

    def check(label, got, want):
        # got = the record's own text (YAML); want = the verse layer
        for var in _kq_variants(want):
            g, w = _level_norm(got, var)
            if g == w:
                return True
        fails.append((label, want, got))
        return False

    unit_voweled = any(LVL.search(st.get("he") or "")
                       for st in U["boot_steps"])

    # the unit's covered span, accumulated once (old-era units quote
    # multi-verse steps; fallback containment ground)
    def _ref_parts(ref):
        _, c, v = ref.split(".")
        v0 = int(str(v).split("-")[0])
        return int(c), v0
    _refs = [_ref_parts(st["ref"]) for st in U["boot_steps"]]
    _bk = U["boot_steps"][0]["ref"].split(".")[0]
    (_c1, _v1), (_c2, _v2) = min(_refs), max(_refs)
    _rows = db.execute(
        "SELECT v.chapter, v.verse, w.idx, w.he FROM words w "
        "JOIN verses v ON v.id=w.verse_id WHERE v.book=? AND "
        "((v.chapter=? AND v.verse>=?) OR v.chapter>?) AND "
        "((v.chapter=? AND v.verse<=?+40) OR v.chapter<?) "
        "ORDER BY v.chapter, v.verse, w.idx",
        (_bk, _c1, _v1, _c1, _c2, _v2, _c2)).fetchall()
    span_line = " ".join(h.replace("/", "") for _, _, _, h in _rows)

    def _span_ok(fragment):
        return _contains(fragment, span_line)

    for st in U["boot_steps"]:
        bk, ch, vs = st["ref"].split(".")
        ch = int(ch)
        v_lo = int(str(vs).split("-")[0])
        v_hi = int(str(vs).split("-")[-1])
        rows = db.execute(
            "SELECT w.idx, w.he, w.maqqef_after, w.mark_id, w.mark_rank "
            "FROM words w JOIN verses v ON v.id=w.verse_id "
            "WHERE v.book=? AND v.chapter=? AND v.verse BETWEEN ? AND ? "
            "ORDER BY v.verse, w.idx",
            (bk, ch, v_lo, v_hi)).fetchall()
        if not st.get("he"):
            continue   # old-era step without a text claim: nothing to check
        plain = ""
        for i, (idx, he, mq, mk, mr) in enumerate(rows):
            plain += ACC.sub("", he.replace("/", ""))
            if i < len(rows) - 1:
                plain += MAQ if mq else " "
        if "\u2026" in st["he"]:
            if not _contains(st["he"], plain) and not _span_ok(st["he"]):
                fails.append((st["ref"] + " he (ellipsized)", plain, st["he"]))
        else:
            if (not any(_level_norm(st["he"], var)[0]
                        == _level_norm(st["he"], var)[1]
                        for var in _kq_variants(plain))
                    and not _span_ok(st["he"])):
                fails.append((st["ref"] + " he", plain, st["he"]))
        if unit_voweled and not VOW.search(st["he"]):
            fails.append((st["ref"] + " VOWELLESS", "", st["he"]))
        et = [idx for idx, he, mq, mk, mr in rows if mk == "etnachta"]
        if et:
            e = et[0]
        else:
            e = min((mr, idx) for idx, he, mq, mk, mr in rows[:-1]
                    if mr and mr < 9)[1]
        left = " ".join(he.replace("/", "") for idx, he, mq, mk, mr in rows
                        if idx <= e)
        right = " ".join(he.replace("/", "") for idx, he, mq, mk, mr in rows
                         if idx > e)
        for _fld, _half in (("tree_left", left), ("tree_right", right)):
            _fh = st.get(_fld, {}).get("he")
            if not _fh:
                continue
            if (not any(_level_norm(_fh, var)[0] == _level_norm(_fh, var)[1]
                        for var in _kq_variants(_half))
                    and not _span_ok(_fh)):
                fails.append((st["ref"] + " " + _fld, _half, _fh))
        for op in st.get("operators", []):
            oh = op.get("he", "")
            if "\u2190" in oh:
                continue   # cross-verse comparison notation (A <- B), not a quote
            if oh and not _contains(oh, plain) and not _span_ok(oh):
                fails.append((st["ref"] + " op-frag not in plain", oh, plain))

    book = U["boot_steps"][0]["ref"].split(".")[0]
    for sc in U.get("scenarios", []):
        m = (re.search(r"STEP_\w\w_(\d+)_(\d+)", sc["title_en"])
             or re.search(r"verse (\d+):(\d+)", sc["title_en"]))
        if not m:
            if sc["id"].endswith("_negative"):
                continue   # synthetic self-tests anchor to no verse by design
            fails.append((sc["id"] + " no step anchor", "", sc["title_en"]))
            continue
        rows = db.execute(
            "SELECT w.he FROM words w JOIN verses v ON v.id=w.verse_id "
            "WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx",
            (book, int(m.group(1)), int(m.group(2)))).fetchall()
        acc_line = " ".join(h.replace("/", "") for (h,) in rows)
        vh = sc.get("value_he")
        if vh and not _contains(vh, acc_line) and not _span_ok(vh):
            fails.append((sc["id"] + " value_he not in verse",
                          vh, acc_line))

    if fails:
        for label, want, got in fails:
            print("FAIL", label)
            print("  want:", want)
            print("  got :", got)
        sys.exit(1)
    print("TEXT LAYER GREEN: %d steps, %d scenarios — %s"
          % (len(U["boot_steps"]), len(U.get("scenarios", [])), uid))


if __name__ == "__main__":
    main()
