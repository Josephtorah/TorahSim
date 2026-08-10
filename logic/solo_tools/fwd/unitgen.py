#!/usr/bin/env python3
"""unitgen.py — forward-era unit skeleton generator (run from repo root).

Builds boot_steps + scenarios for a verse-per-step unit, slicing every
Hebrew string from the SNAPSHOT (never retyped). The per-unit build
script supplies meta prose, per-verse EN translations, operators, and
scenario expects; this module supplies verified trees and tokens.
"""
import re
import sqlite3

DB = "torah_grok.SNAPSHOT-main-51801ca.sqlite"
ETNACHTA = "֑"
TIFCHA = "֖"
ZAQEF_QATAN = "֔"
ACCENTS = re.compile("[\u0591-\u05AF\u05BD]")  # accents + meteg only (verify_text canon)
MAQQEF = "־"


def verse_tokens(db, book, ch, vs):
    rows = db.execute(
        """SELECT w.idx, w.he, w.translit, w.maqqef_after FROM words w
        JOIN verses v ON w.verse_id=v.id
        WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx""",
        (book, ch, vs)).fetchall()
    assert rows, (book, ch, vs)
    return rows


def join_tokens(rows, strip_accents, keep_maqqef=None):
    """Join tokens; step/operator layer keeps maqqef (plain text), tree
    layer drops it to a space (accented text) — the corpus convention."""
    if keep_maqqef is None:
        keep_maqqef = strip_accents
    out = []
    for idx, he, tr, mq in rows:
        h = he.replace("/", "")
        if strip_accents:
            h = ACCENTS.sub("", h)
        out.append((h, tr, mq))
    text, translit = "", ""
    for i, (h, tr, mq) in enumerate(out):
        text += h
        translit += tr
        if mq and keep_maqqef:
            text += MAQQEF
            translit += "-"
        elif mq:
            text += " "
            translit += "-"
        elif i < len(out) - 1:
            text += " "
            translit += " "
    return text, translit


def split_point(rows, db=None, book=None, ch=None, vs=None):
    """(idx, kind): etnachta token, else the strongest disjunctive by
    mark_rank — mirroring verify_text.py's fallback exactly (min rank,
    earliest, non-final token)."""
    for idx, he, tr, mq in rows:
        if ETNACHTA in he:
            return idx, "etnachta"
    if db is not None:
        mk = db.execute(
            """SELECT w.idx, w.mark_id, w.mark_rank FROM words w
            JOIN verses v ON w.verse_id=v.id
            WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx""",
            (book, ch, vs)).fetchall()
        cands = [(mr, idx) for idx, mid, mr in mk[:-1] if mr and mr < 9]
        if cands:
            mr, idx = min(cands)
            name = next(mid for i, mid, r in mk if i == idx)
            return idx, name.replace("_", " ")
    return len(rows) - 1, "verse-final"


STEP_PREFIX = {"Gen": "Gn", "Exod": "Ex", "Lev": "Lv", "Num": "Nm", "Deut": "Dt"}


def build_step(db, book_abbr, book_dot, ch, vs, order, spec):
    rows = verse_tokens(db, book_abbr, ch, vs)
    sp_idx, sp_kind = split_point(rows, db, book_abbr, ch, vs)
    left, right = [r for r in rows if r[0] <= sp_idx], [r for r in rows if r[0] > sp_idx]
    he_plain, tr_plain = join_tokens(rows, strip_accents=True)
    lhe, ltr = join_tokens(left, strip_accents=False)
    rhe, rtr = join_tokens(right, strip_accents=False)
    sp_tok = next(r for r in rows if r[0] == sp_idx)
    if sp_kind == "etnachta":
        lnote = "%s (etnachta on %s) [VERIFIED: SNAPSHOT %s.%d.%d idx%d etnachta in-stream]" % (
            spec["left_en"], sp_tok[2], book_dot, ch, vs, sp_idx)
    else:
        lnote = "%s (NO etnachta in verse: split at %s on %s) [VERIFIED: SNAPSHOT %s.%d.%d idx%d %s; no etnachta token]" % (
            spec["left_en"], sp_kind, sp_tok[2], book_dot, ch, vs, sp_idx, sp_kind)
    rnote = "%s (verse-final %s) [VERIFIED: SNAPSHOT %s.%d.%d idx%d-%d]" % (
        spec["right_en"], rows[-1][2], book_dot, ch, vs, sp_idx + 1, rows[-1][0])
    step = {
        "id": "STEP_%s_%d_%d" % (STEP_PREFIX.get(book_abbr, "Gn"), ch, vs),
        "order": order,
        "ref": "%s.%d.%d" % (book_dot, ch, vs),
        "op": spec["op"],
        "he": he_plain,
        "he_translit": tr_plain,
        "en": "[EN-AID] " + spec["en"],
        "tree_left": {"he": lhe, "he_translit": ltr, "en": lnote},
        "tree_right": {"he": rhe, "he_translit": rtr, "en": rnote},
        "operators": [],
        "comment": spec["comment"],
        "confidence": "tested",
        "source": "[HE-WRITTEN][HE-STRUCT]",
    }
    for od in spec["operators"]:
        lo, hi = od.get("he_span", (0, min(3, len(rows) - 1)))
        ohe, otr = join_tokens([r for r in rows if lo <= r[0] <= hi], strip_accents=True)
        step["operators"].append({
            "op": od["op"], "expr_en": od["expr_en"],
            "he": ohe, "he_translit": otr,
            "en": od["prose"], "cites": [], "confidence": "tested",
        })
    return step


def yaml_quote(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def emit_block(text, indent):
    """Emit a folded-scalar body: wrap prose at ~68 cols."""
    import textwrap
    lines = []
    for para in text.split("\n\n"):
        wrapped = textwrap.fill(" ".join(para.split()), width=68)
        for ln in wrapped.split("\n"):
            lines.append(indent + ln)
        lines.append("")
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def emit_unit(meta_yaml, derivation_log_yaml, steps, scenarios, out_path):
    parts = [meta_yaml.rstrip("\n"), derivation_log_yaml.rstrip("\n"), "scenarios:"]
    for sc in scenarios:
        parts.append("- id: %s" % sc["id"])
        parts.append("  title_en: %s" % yaml_quote(sc["title_en"]))
        parts.append("  given_en: %s" % yaml_quote(sc["given_en"]))
        parts.append("  expect_en: |")
        for ln in sc["expect_en"]:
            parts.append("    " + ln)
        parts.append("  value_he: %s" % sc["value_he"])
        parts.append("  value_he_translit: %s" % yaml_quote(sc["value_he_translit"]))
        parts.append("")
    parts.append("boot_steps:")
    for st in steps:
        parts.append("- id: %s" % st["id"])
        parts.append("  order: %d" % st["order"])
        parts.append("  ref: %s" % st["ref"])
        parts.append("  op: %s" % st["op"])
        parts.append("  he: %s" % st["he"])
        parts.append("  he_translit: %s" % st["he_translit"])
        parts.append("  en: %s" % yaml_quote(st["en"]))
        parts.append("  tree_left:")
        parts.append("    he: %s" % st["tree_left"]["he"])
        parts.append("    he_translit: %s" % st["tree_left"]["he_translit"])
        parts.append("    en: %s" % yaml_quote(st["tree_left"]["en"]))
        parts.append("  tree_right:")
        parts.append("    he: %s" % st["tree_right"]["he"])
        parts.append("    he_translit: %s" % st["tree_right"]["he_translit"])
        parts.append("    en: %s" % yaml_quote(st["tree_right"]["en"]))
        parts.append("  operators:")
        for op in st["operators"]:
            parts.append("  - op: %s" % op["op"])
            parts.append("    expr_en: %s" % yaml_quote(op["expr_en"]))
            parts.append("    he: %s" % op["he"])
            parts.append("    he_translit: %s" % op["he_translit"])
            parts.append("    en: >")
            parts.append(emit_block(op["en"], "      "))
            parts.append("    cites: []")
            parts.append("    confidence: tested")
        parts.append("  comment: >")
        parts.append(emit_block(st["comment"], "    "))
        parts.append("  confidence: tested")
        parts.append('  source: "[HE-WRITTEN][HE-STRUCT]"')
        parts.append("")
    open(out_path, "w", encoding="utf-8").write("\n".join(parts).rstrip("\n") + "\n")


def scenario_for(db, book_abbr, ch, vs, sid, title, given, expects):
    rows = verse_tokens(db, book_abbr, ch, vs)
    frag = rows[: min(4, len(rows))]
    vhe, vtr = join_tokens(frag, strip_accents=False)
    return {"id": sid, "title_en": title, "given_en": given,
            "expect_en": expects, "value_he": vhe, "value_he_translit": vtr}
