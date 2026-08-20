#!/usr/bin/env python3
"""
render_flat_ledger_from_db.py — the FLAT · LEAF LEDGER · OSHB MORPH report,
sourced entirely from derivation.sqlite (no re-parse; PLAN §4 upgrade of
render_flat_ledger_morph_html.py). Because the DB covers the whole Torah,
this renders ANY verse range, not just Genesis 1.

Reuses from the original renderer (single source of truth for display):
CSS, VERSE_EN (free-English lines), decode_morph (OSHB code -> English aid).

Usage (from anywhere):
  python3 render_flat_ledger_from_db.py                          # Gen 1:1-31,2:1-3
  python3 render_flat_ledger_from_db.py Gen "1:1-5" out.html
  python3 render_flat_ledger_from_db.py Lev "1:1-9" lev.html
"""

import html as _html
import importlib.util
import os
import re
import sqlite3
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
os.chdir(ROOT)  # original module loads logic/lexicon/CURRENT etc. relative to root

_spec = importlib.util.spec_from_file_location(
    "rflm", HERE / "render_flat_ledger_morph_html.py")
R = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(R)
CSS, VERSE_EN, decode_morph = R.CSS, R.VERSE_EN, R.decode_morph

DB = ROOT / "data" / "derivation.sqlite"
BOOK_FULL = {"Gen": "Genesis", "Exod": "Exodus", "Lev": "Leviticus",
             "Num": "Numbers", "Deut": "Deuteronomy"}
FSI, PDI = "⁨", "⁩"  # keep Hebrew-inside-parens display order stable

CODE_CSS = """
pre.codepre { background:#f7f5ee; border:1px solid var(--line); border-left:3px solid #4a6da7;
  border-radius:0 8px 8px 0; padding:.7rem .9rem; font:.76rem/1.55 Menlo,Consolas,monospace;
  overflow-x:auto; margin:.4rem 0 1.2rem; }
pre.codepre .cmt { color:#6b7280; }
"""

STEM_NAMES = {"q": "qal", "N": "niphal", "p": "piel", "P": "pual",
              "h": "hifil", "H": "hofal", "t": "hitpael"}
FORM_NAMES = {"w": "wayyiqtol", "p": "perfect", "q": "weqatal", "i": "imperfect",
              "v": "imperative", "j": "jussive", "h": "cohortative",
              "r": "participle", "s": "participle-passive", "c": "inf-construct",
              "a": "inf-absolute"}


def leaf_verb_tag(d, lf):
    """'[Vqj3ms qal jussive]' for the first verb inside the leaf span, else ''."""
    for wi in range(lf["w_start"], lf["w_end"] + 1):
        for s in d["segs"][wi]:
            code = s["morph_seg"] or ""
            if code.startswith("V") and len(code) >= 3:
                stem = STEM_NAMES.get(code[1], code[1])
                form = FORM_NAMES.get(code[2], code[2])
                return " [%s %s %s]" % (code, stem, form)
    return ""


# role column -> code emitter. Mechanical rendering of DB facts only:
# role vocabulary maps CMD=jussive->LET, CMD?=imperfect->LET_Q ('?' never removed,
# TIR-028), CMD!=imperative->CMD. Anything unmapped becomes a context comment.
ROLE_EMIT = {
    "SPEAK":     lambda a: 'DECLARE(%s)' % (a or '"?"'),
    "CMD":       lambda a: 'SPECS.push(LET("%s"))' % a,
    "CMD?":      lambda a: 'SPECS.push(LET_Q("%s"))' % a,
    "CMD!":      lambda a: 'CMD("%s")' % a,
    "CMD-US":    lambda a: 'CMD_US("%s")' % a,
    "THEN":      lambda a: 'THEN("%s")' % a,
    "PURPOSE":   lambda a: 'PURPOSE("%s")' % a,
    "ONGOING":   lambda a: 'WORLD.invariant("%s")' % a,
    "RESULT":    lambda a: 'RESULT("%s")' % (a or "khen"),
    "EVAL":      lambda a: 'TESTS.record(PASS("%s"))' % (a or "tov"),
    "TIME-STAMP": lambda a: 'LEDGER.cycle("erev -> boqer")',
    "DAY-COUNT": lambda a: 'LEDGER.commit(day_label="%s")' % a,
    "NAME":      lambda a: 'REGISTRY.name(...)',
    "OBJ_FRAME": lambda a: 'THEME("%s")' % a,
    "BETWEEN":   lambda a: 'BETWEEN("%s")' % a,
}
EVENT_ROLES = {"CREATE", "MAKE", "DIVIDE", "GATHER", "SEE/ASSESS", "BECOME/WAS",
               "BLESS", "SANCTIFY", "COMPLETE", "CEASE/REST", "GIVE", "SET/PLACE"}
TIR_NOTE = {"CMD": "TIR-026", "CMD?": "TIR-028", "CMD!": "TIR-027",
            "CMD-US": "TIR-033", "THEN": "TIR-029", "PURPOSE": "TIR-030",
            "ONGOING": "TIR-031", "OBJ_FRAME": "TIR-014", "NAME": "TIR-022"}


def code_section(d, frozen_rows):
    lines = []
    lines.append("# CODE (auto, illustrative) — mechanical rendering of the role "
                 "column + verb forms.")
    lines.append("# Not a frozen derivation; LET_Q keeps its '?' — never "
                 "auto-upgraded [TIR-028].")
    if frozen_rows:
        for fr in frozen_rows:
            lines.append("# frozen coverage: %s · %s (%s) — owner-derived "
                         "operators live in that unit"
                         % (fr["unit_id"], fr["step_id"], fr["op"]))
    lines.append("")
    for lf in d["leaves"]:
        role = lf["role"] or ""
        head, _, rest = role.partition("(")
        arg = rest.rstrip(")")
        tag = leaf_verb_tag(d, lf)
        cmt = "# B%d %s — %s%s" % (lf["b_index"], lf["translit"], lf["en"], tag)
        if head in ROLE_EMIT:
            code = ROLE_EMIT[head](arg)
            if head in TIR_NOTE:
                cmt += "  [%s]" % TIR_NOTE[head]
            lines.append("%-46s %s" % (code, cmt))
        elif head in EVENT_ROLES:
            verb = head.split("/")[0].lower()
            code = 'EVENT("%s"%s)' % (verb, ', "%s"' % arg if arg else "")
            lines.append("%-46s %s" % (code, cmt))
        else:
            lines.append("%-46s %s" % ("pass", cmt + ("  (context: %s)" % role
                                                      if role else "")))
    html_lines = []
    for ln in lines:
        if "#" in ln:
            code_part, _, cmt_part = ln.partition("#")
            html_lines.append(esc(code_part) + '<span class="cmt">#'
                              + esc(cmt_part) + "</span>")
        else:
            html_lines.append(esc(ln))
    return ('<h3>Code — machine-operator sketch (auto, illustrative)</h3>'
            '<pre class="codepre">%s</pre>' % "\n".join(html_lines))


def esc(s):
    return _html.escape("" if s is None else str(s))


def parse_ranges(spec_str):
    """'1:1-31,2:1-3' -> [(1,1),(1,2),...,(2,3)]"""
    out = []
    for part in spec_str.split(","):
        ch, vv = part.strip().split(":")
        lo, _, hi = vv.partition("-")
        for v in range(int(lo), int(hi or lo) + 1):
            out.append((int(ch), v))
    return out


def fetch_verse(cx, book, ch, v):
    osis = "%s.%d.%d" % (book, ch, v)
    vr = cx.execute("SELECT * FROM verses WHERE osis_id=?", (osis,)).fetchone()
    if not vr:
        return None
    tree = cx.execute("SELECT * FROM trees WHERE verse_id=?", (vr["id"],)).fetchone()
    words = cx.execute("SELECT * FROM words WHERE verse_id=? ORDER BY idx",
                       (vr["id"],)).fetchall()
    leaves = cx.execute(
        """SELECT l.*, r.role FROM leaves l LEFT JOIN roles r ON r.leaf_id=l.id
           WHERE l.tree_id=? ORDER BY l.b_index""", (tree["id"],)).fetchall()
    segs = {}
    for w in words:
        segs[w["idx"]] = cx.execute(
            "SELECT * FROM segments WHERE word_id=? ORDER BY seg_idx",
            (w["id"],)).fetchall()
    return {"osis": osis, "verse": vr, "tree": tree, "words": words,
            "leaves": leaves, "segs": segs}


def froze_because(words, ws, we):
    if ws == we:
        return "single word"
    inner = sorted({words[i]["mark_id"] for i in range(ws, we)
                    if words[i]["mark_id"]})
    return "only " + ", ".join(inner) + " (conj) inside" if inner else "maqqef-glued"


def main_seg_idx(segs):
    """The lexical segment of a word: single-segment words are their own main;
    otherwise the last non-suffix segment carrying a numeric Strong's lemma
    (prefix letters carry letter lemmas like 'b'/'l'/'c', real words like
    bein/tachat carry numbers even though both are coded R)."""
    if len(segs) == 1:
        return segs[0]["seg_idx"]
    cands = [s["seg_idx"] for s in segs
             if not (s["morph_seg"] or "").startswith("S")
             and re.match(r"\d", s["lemma_seg"] or "")]
    return cands[-1] if cands else None


def grammar_text(seg, is_main):
    base = decode_morph(seg["morph_seg"] or "")
    if (seg["morph_seg"] or "").startswith("S"):
        # decode_morph already renders the pronoun meaning from the PGN code
        return "%s — suffix letters, not a standalone word" % base
    if not is_main:
        return "%s — prefix letter, not a standalone word" % base
    mnum = re.match(r"(\d+)", seg["lemma_seg"] or "")
    strongs = " (H%s)" % mnum.group(1) if mnum else ""
    return "%s — “%s”%s" % (base, seg["gloss"] or "", strongs)


def render_verse(book, ch, v, d, frozen_rows=None):
    vr, words, leaves = d["verse"], d["words"], d["leaves"]
    out = ['<h2 id="v%d_%d">%s %d:%d</h2>' % (ch, v, book, ch, v)]
    out.append('<div class="meta">FLAT · taamim %s · %s · %d words → %d bricks · '
               'parser status: %s · source: derivation.sqlite</div>'
               % (esc(d["tree"]["rule_version"]), esc(vr["system"]), len(words),
                  len(leaves), esc(d["tree"]["status"])))
    fen = VERSE_EN.get((ch, v)) if book == "Gen" else None
    if fen:
        out.append('<div class="fen">en: “%s”</div>' % esc(fen))
    else:
        chain = " ".join(w["gloss"] or "?" for w in words)
        out.append('<div class="fen">en (word glosses): %s</div>' % esc(chain))

    rows = {"he": [], "tr": [], "en": []}
    for lf in leaves:
        rows["he"].append('<span class="brick">(%s%s%s)</span>'
                          % (FSI, esc(lf["he"]), PDI))
        rows["tr"].append('<span class="brick">(%s)</span>' % esc(lf["translit"]))
        rows["en"].append('<span class="brick">(%s)</span>' % esc(lf["en"]))
    out.append('<div class="flat">')
    out.append('<div class="row he-row"><span class="lab">he:</span> %s</div>'
               % " ".join(rows["he"]))
    out.append('<div class="row"><span class="lab">tr:</span> %s</div>'
               % " ".join(rows["tr"]))
    out.append('<div class="row"><span class="lab">en:</span> %s</div>'
               % " ".join(rows["en"]))
    out.append('<div class="guide">B0 … B%d in reading order — Hebrew row runs '
               'right-to-left (B0 is the right-most paren); en = literal word '
               'glosses, verse line above = free English.</div></div>'
               % (len(leaves) - 1))

    out.append('<h3>Leaf ledger</h3><div class="wrap"><table>')
    out.append('<tr><th>B#</th><th>words</th><th>path</th><th>he</th><th>translit</th>'
               '<th>en (literal)</th><th>end mark · rank</th><th>froze because</th>'
               '<th>role (auto, illustrative)</th></tr>')
    for lf in leaves:
        ws, we = lf["w_start"], lf["w_end"]
        wlab = "w%d" % ws if ws == we else "w%d–%d" % (ws, we)
        out.append('<tr><td><b>B%d</b></td><td>%s</td><td class="code">%s</td>'
                   '<td class="he">%s</td><td>%s</td><td>%s</td><td>%s · r%s</td>'
                   '<td>%s</td><td>%s</td></tr>'
                   % (lf["b_index"], wlab, esc(lf["path"]), esc(lf["he"]),
                      esc(lf["translit"]), esc(lf["en"]), esc(lf["end_mark"]),
                      esc(lf["rank"]), esc(froze_because(words, ws, we)),
                      esc(lf["role"] or "")))
    out.append("</table></div>")

    out.append('<h3>Morph — every word and every morpheme letter (OSHB)</h3>'
               '<div class="wrap"><table>')
    out.append('<tr><th>B#</th><th>w</th><th>he</th><th>translit</th><th>en</th>'
               '<th>OSHB code</th><th>grammar (English aid)</th></tr>')
    for lf in leaves:
        first_in_brick = True
        for wi in range(lf["w_start"], lf["w_end"] + 1):
            segs = d["segs"][wi]
            main_idx = main_seg_idx(segs)
            for s in segs:
                wlab = str(wi) if len(segs) == 1 \
                    else "%d%s" % (wi, chr(ord("a") + s["seg_idx"]))
                cls = ' class="bstart"' if first_in_brick else ""
                first_in_brick = False
                out.append('<tr%s><td><b>B%d</b></td><td class="code">%s</td>'
                           '<td class="he">%s</td><td>%s</td><td>%s</td>'
                           '<td class="code">%s</td><td>%s</td></tr>'
                           % (cls, lf["b_index"], wlab, esc(s["he"]),
                              esc(s["translit"]), esc(s["gloss"]),
                              esc(s["morph_seg"]),
                              esc(grammar_text(s, s["seg_idx"] == main_idx))))
    out.append("</table></div>")
    out.append(code_section(d, frozen_rows))
    return "\n".join(out)


def main():
    book = sys.argv[1] if len(sys.argv) > 1 else "Gen"
    ranges = sys.argv[2] if len(sys.argv) > 2 else "1:1-31,2:1-3"
    out_path = Path(sys.argv[3]) if len(sys.argv) > 3 else \
        HERE / ("DB_FLAT_LEDGER_MORPH_%s_%s_2026-07-28.html"
                % (book, ranges.replace(":", "_").replace(",", "_").replace("-", "to")))

    cx = sqlite3.connect(str(DB))
    cx.row_factory = sqlite3.Row
    meta = dict(cx.execute("SELECT key, value FROM meta"))

    frozen_steps = {}
    for r in cx.execute("""SELECT s.ref, s.unit_id, s.step_id, s.op FROM steps s
                           JOIN units u ON u.unit_id = s.unit_id
                           WHERE u.status = 'frozen' AND s.ref IS NOT NULL"""):
        frozen_steps.setdefault(r["ref"], []).append(r)

    targets = parse_ranges(ranges)
    sections, nav, missing = [], [], []
    for ch, v in targets:
        d = fetch_verse(cx, book, ch, v)
        if d is None:
            missing.append("%s %d:%d" % (book, ch, v))
            continue
        nav.append('<a href="#v%d_%d">%s %d:%d</a>' % (ch, v, book, ch, v))
        sections.append(render_verse(book, ch, v, d,
                                     frozen_steps.get(d["osis"])))
    if missing:
        sys.exit("not in DB: %s" % ", ".join(missing))

    title_span = ranges.replace(",", " · ")
    page = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s %s — FLAT · LEDGER · MORPH (DB)</title>
<style>%s%s</style></head><body><main>
<h1>%s %s — FLAT parens · LEAF LEDGER · OSHB MORPH</h1>
<div class="meta"><b>DB-backed:</b> every row queried from <span class="tag">derivation.sqlite</span>
(no re-parse) · index built %s from commit <span class="tag">%s</span> ·
structure = ta'amim rules <span class="tag">%s</span> · roles <span class="tag">%s</span> ·
lexicon <span class="tag">%s</span> · morphology = OSHB (#IMPOSED labeled aid) ·
English &amp; translit = EN-AID only, never derivation source · roles auto, illustrative only ·
not binding religious law · not TIR-frozen</div>
<div class="banner"><b>How to read:</b> each verse shows (1) <b>FLAT</b> — the full verse in
Hebrew / transliteration / literal-gloss English with parentheses around each ta'amim leaf brick;
(2) <b>LEAF LEDGER</b> — one row per brick with its tree path and the disjunctive mark that closed it;
(3) <b>MORPH</b> — one row per <i>morpheme segment</i>: prefix letters (ו=and, ה=the, ל=to, ב=in, מ=from)
and pronoun suffixes get their own rows; ids like <span class="tag">4a/4b</span> = segments of word 4;
(4) <b>CODE</b> — a machine-operator sketch generated mechanically from the role column and verb forms
(role CMD=jussive→LET · CMD?=imperfect→LET_Q, the '?' never auto-removed · CMD!=imperative→CMD);
auto + illustrative, not a frozen derivation — verses covered by a frozen unit cite it as provenance.
Format spec: <span class="tag">MOCKUP_flat_ledger_oshb_morph_2026-07-27.md</span> · role vocabulary:
see the original report banner (<span class="tag">GEN_1_1_to_2_3_flat_ledger_morph_2026-07-28.html</span>).</div>
<nav>%s</nav>
%s
<p class="meta">Generated by render_flat_ledger_from_db.py · the DB is a derived, rebuildable
index — the system of record stays the git-versioned text (Pre-Code rule).</p>
</main></body></html>""" % (esc(book), esc(title_span), CSS, CODE_CSS,
                            esc(BOOK_FULL.get(book, book)),
                            esc(title_span), esc(meta.get("built_at", "?")),
                            esc(meta.get("built_from_commit", "?")),
                            esc(meta.get("taamim_rule_version", "?")),
                            esc(meta.get("role_ruleset", "?")),
                            esc(meta.get("lexicon_version", "?")),
                            " ".join(nav), "\n".join(sections))
    out_path.write_text(page, encoding="utf-8")
    print("wrote %s (%.0f KB, %d verses)" % (out_path,
                                             out_path.stat().st_size / 1024,
                                             len(sections)))


if __name__ == "__main__":
    main()
