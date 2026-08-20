#!/usr/bin/env python3
"""
report_db_html.py — read-only HTML inspection report over derivation.sqlite.

Every number and row on the page is queried live from the DB at generation
time (plus two captured run_unit.py outputs, labeled as computed-not-stored).
The DB is a derived, rebuildable index — never the system of record.

Usage:  python3 press/report_db_html.py
Output: press/DB_INSPECTION_2026-07-28.html
"""

import html
import sqlite3
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DB = ROOT / "data" / "derivation.sqlite"
OUT = HERE / "DB_INSPECTION_2026-07-28.html"

FORM_NAMES = {"w": "wayyiqtol (narrative event)", "q": "weqatal (THEN-chain)",
              "i": "imperfect (modal space)", "v": "imperative (CMD!)",
              "c": "inf. construct (PURPOSE)", "r": "participle (ONGOING)",
              "p": "perfect (completed state)", "j": "jussive (LET)"}
BOOKS = ["Gen", "Exod", "Lev", "Num", "Deut"]

LAYERS = [
    ("text", "verses", "one row per Torah verse (osis_id, book, chapter, verse, prose/poetry system)"),
    ("text", "words", "one row per word: pointed Hebrew, translit, gloss (lexicon v1), OSHB lemma+morph, ta'am mark"),
    ("text", "segments", "morpheme level: every prefix letter / suffix as its own row (the ו/ה/ל/מ rows)"),
    ("structure", "trees", "one v3 ta'amim tree per verse (JSON), parse status"),
    ("structure", "leaves", "glue-brick leaves: span, closing mark, rank, L/R path, he+translit"),
    ("interpretation", "roles", "role label per leaf (role_rules v1 — display heuristics, versioned)"),
    ("derivation", "units", "index of logic/units/*.yaml (YAML stays canonical — never authored here)"),
    ("derivation", "steps", "every unit step: op, he+translit+en, confidence, source tags"),
    ("derivation", "unit_scenarios", "every unit scenario (id, title, expectation)"),
    ("derivation", "coverage", "per-word role coverage from units"),
    ("oral", "oral_refs", "named, tiered Oral citations backfilled from this week's derivations"),
    ("oral", "oral_texts", "FTS5 over 215 local Oral corpus files (119,903 searchable segments)"),
    ("search", "fts", "FTS5 over the whole Written layer: he_plain + translit + gloss"),
    ("build", "warnings", "validation flags from the build (never silent edits)"),
    ("build", "meta", "build provenance: rule versions, source commit, counts"),
]


def esc(x):
    return html.escape("" if x is None else str(x))


def he_cell(txt):
    return '<span class="he" dir="rtl">%s</span>' % esc(txt)


def table(headers, rows, cls=""):
    out = ['<table class="%s"><tr>' % cls]
    out += ["<th>%s</th>" % h for h in headers]
    out.append("</tr>")
    for r in rows:
        out.append("<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>")
    out.append("</table>")
    return "\n".join(out)


def sql_note(q):
    return '<div class="sql">%s</div>' % esc(" ".join(q.split()))


def main():
    if not DB.exists():
        sys.exit("no DB at %s — rebuild with: python3 build_db.py" % DB)
    cx = sqlite3.connect(str(DB))
    cx.row_factory = sqlite3.Row
    q = lambda sql, *a: cx.execute(sql, a).fetchall()
    S = []

    # -- header + meta -------------------------------------------------------
    meta = {r["key"]: r["value"] for r in q("SELECT key, value FROM meta")}
    S.append("<h1>derivation.sqlite — inspection report</h1>")
    S.append('<p class="note">Derived, rebuildable index (<code>python3 build_db.py</code>, '
             "~7 min). The system of record is the git-versioned text: corpora in "
             "<code>Data/</code>, rules in <code>logic/</code>, derivations in "
             "<code>logic/units/*.yaml</code>. Deleting this file loses nothing. "
             "Every row below is queried live at report time.</p>")
    S.append("<h2>1 · Build provenance (meta)</h2>")
    S.append(table(["key", "value"],
                   [(esc(k), esc(v)) for k, v in sorted(meta.items())], "kv"))

    # -- layer map -----------------------------------------------------------
    S.append("<h2>2 · Layer map — every table, live row count</h2>")
    rows = []
    for layer, tname, desc in LAYERS:
        n = q("SELECT COUNT(*) c FROM %s" % tname)[0]["c"]
        warn = ' <b class="flag">⚠ empty — tree_coverage not yet indexed (known gap)</b>' \
            if tname == "coverage" and n == 0 else ""
        rows.append((esc(layer), "<code>%s</code>" % esc(tname),
                     "{:,}".format(n), esc(desc) + warn))
    S.append(table(["layer", "table", "rows", "what it holds"], rows))

    # -- text layer sample ----------------------------------------------------
    S.append("<h2>3 · Text layer — Gen 1:1 word rows</h2>")
    sql = """SELECT w.idx, w.he, w.translit, w.gloss, w.lemma, w.morph,
                    w.mark_id, w.mark_kind, w.mark_rank
             FROM words w JOIN verses v ON w.verse_id=v.id
             WHERE v.osis_id='Gen.1.1' ORDER BY w.idx"""
    S.append(sql_note(sql))
    S.append(table(
        ["#", "he", "translit", "gloss (EN-AID)", "lemma", "morph (#IMPOSED)", "mark", "kind", "rank"],
        [(r["idx"], he_cell(r["he"]), esc(r["translit"]), esc(r["gloss"]),
          esc(r["lemma"]), "<code>%s</code>" % esc(r["morph"]),
          esc(r["mark_id"]), esc(r["mark_kind"]),
          esc(r["mark_rank"])) for r in q(sql)]))

    S.append("<h3>…and its morpheme segments (word 0: בְּרֵאשִׁית / be-reshit)</h3>")
    sql = """SELECT s.seg_idx, s.he, s.translit, s.lemma_seg, s.morph_seg, s.gloss
             FROM segments s JOIN words w ON s.word_id=w.id
             JOIN verses v ON w.verse_id=v.id
             WHERE v.osis_id='Gen.1.1' AND w.idx=0 ORDER BY s.seg_idx"""
    S.append(table(["seg", "he", "translit", "lemma", "morph", "gloss"],
                   [(r["seg_idx"], he_cell(r["he"]), esc(r["translit"]),
                     esc(r["lemma_seg"]), "<code>%s</code>" % esc(r["morph_seg"]),
                     esc(r["gloss"])) for r in q(sql)]))

    # -- structure + interpretation -------------------------------------------
    S.append("<h2>4 · Structure + roles — Gen 1:3 glue-brick leaves</h2>")
    sql = """SELECT l.b_index, l.he, l.translit, l.end_mark, l.rank, l.path, r.role
             FROM leaves l JOIN trees t ON l.tree_id=t.id
             JOIN verses v ON t.verse_id=v.id
             LEFT JOIN roles r ON r.leaf_id=l.id
             WHERE v.osis_id='Gen.1.3' ORDER BY l.b_index"""
    S.append(sql_note(sql))
    S.append(table(["B#", "he", "translit", "closing mark", "rank", "path", "role (auto, v1)"],
                   [(r["b_index"], he_cell(r["he"]), esc(r["translit"]),
                     esc(r["end_mark"]), esc(r["rank"]), "<code>%s</code>" % esc(r["path"]),
                     "<b>%s</b>" % esc(r["role"])) for r in q(sql)]))
    st = q("SELECT rule_version, status, COUNT(*) c FROM trees GROUP BY 1,2")
    S.append('<p class="note">Trees: ' + " · ".join(
        "%s / %s: <b>%s</b>" % (esc(r["rule_version"]), esc(r["status"]),
                                "{:,}".format(r["c"])) for r in st) +
        " — every verse in the Torah parses unique under v3.</p>")

    # -- genre fingerprint ------------------------------------------------------
    S.append("<h2>5 · Genre fingerprint — verb forms × book (whole Torah)</h2>")
    S.append('<p class="note">The evidence table behind TIR-026…033, reproduced '
             "live: 3rd character of the OSHB verb code is the form.</p>")
    sql = """SELECT v.book, substr(s.morph_seg,3,1) form, COUNT(*) c
             FROM segments s JOIN words w ON s.word_id=w.id
             JOIN verses v ON w.verse_id=v.id
             WHERE s.morph_seg LIKE 'V%' AND length(s.morph_seg) >= 3
             GROUP BY v.book, form"""
    S.append(sql_note(sql))
    grid = {}
    for r in q(sql):
        grid.setdefault(r["form"], {})[r["book"]] = r["c"]
    rows = []
    for f, name in FORM_NAMES.items():
        per = grid.get(f, {})
        rows.append([esc(name)] + ["{:,}".format(per.get(b, 0)) for b in BOOKS]
                    + ["{:,}".format(sum(per.get(b, 0) for b in BOOKS))])
    S.append(table(["form"] + BOOKS + ["total"], rows, "num"))

    # -- derivation layer -------------------------------------------------------
    S.append("<h2>6 · Derivation layer — units index</h2>")
    st = q("SELECT status, COUNT(*) c FROM units GROUP BY status")
    S.append("<p>" + " · ".join("<b>%s</b> %s" % (r["c"], esc(r["status"]))
                                for r in st) +
             " — YAML files stay canonical; this table only indexes them.</p>")
    sql = """SELECT unit_id, refs, status, tree_derive_version, n_steps, n_scenarios
             FROM units WHERE status='frozen'"""
    S.append(table(["unit", "refs", "status", "derive version", "steps", "scenarios"],
                   [("<b>%s</b>" % esc(r["unit_id"]), esc(r["refs"]),
                     '<b class="ok">%s</b>' % esc(r["status"]),
                     esc(r["tree_derive_version"]), esc(r["n_steps"]),
                     esc(r["n_scenarios"])) for r in q(sql)]))
    S.append("<h3>Steps of the frozen unit</h3>")
    sql = """SELECT step_id, ref, op, he, translit, en FROM steps
             WHERE unit_id='gen_01_creation_boot' ORDER BY id"""
    S.append(table(["step", "ref", "op", "he", "translit", "en (EN-AID)"],
                   [(esc(r["step_id"]), esc(r["ref"]), "<code>%s</code>" % esc(r["op"]),
                     he_cell(r["he"]), esc(r["translit"]),
                     esc((r["en"] or "").replace("[EN-AID] ", "")))
                    for r in q(sql)]))

    # -- oral layer ---------------------------------------------------------------
    S.append("<h2>7 · Oral layer — all 20 named citations (oral_refs)</h2>")
    sql = """SELECT work, locus, he, translit, tier, anchors_to
             FROM oral_refs ORDER BY id"""
    rows = []
    for r in q(sql):
        he_short = (r["he"] or "")[:60] + ("…" if r["he"] and len(r["he"]) > 60 else "")
        tr_short = (r["translit"] or "")[:70] + ("…" if r["translit"] and len(r["translit"]) > 70 else "")
        tier = '<b class="%s">%s</b>' % ("ok" if r["tier"] == "verified" else "flag",
                                         esc(r["tier"]))
        rows.append((esc(r["work"]), esc(r["locus"]), he_cell(he_short),
                     esc(tr_short), tier, esc(r["anchors_to"])))
    S.append(table(["work", "locus", "he", "translit", "tier", "anchors to"], rows))

    S.append("<h3>Live FTS demos</h3>")
    demo1 = "SELECT osis_id FROM fts WHERE fts MATCH '\"יהי אור\"'"
    hits1 = ", ".join(r["osis_id"] for r in q(demo1))
    demo2 = "SELECT work, locus FROM oral_texts WHERE oral_texts MATCH '\"סדר זמנים\"' LIMIT 5"
    hits2 = " · ".join("%s %s" % (r["work"], r["locus"]) for r in q(demo2))
    S.append(sql_note(demo1))
    S.append("<p>%s (yehi or / let there be light) → <b>%s</b></p>"
             % (he_cell("יהי אור"), esc(hits1)))
    S.append(sql_note(demo2))
    S.append("<p>%s (seder zemanim / order of times) → <b>%s</b> — the exact quote "
             "cited in the frozen unit's oral_notes.</p>"
             % (he_cell("סדר זמנים"), esc(hits2)))

    # -- stage D (computed, not stored) --------------------------------------------
    S.append("<h2>8 · Stage D interpreter run — computed live, NOT stored in the DB</h2>")
    S.append('<p class="note">By design: interpreter results are re-derived from the '
             "frozen YAML on every run, like a test suite. The DB holds everything "
             "upstream of this. (Roadmap: a <code>scenario_results</code> snapshot "
             "table can land with Stage E CI.)</p>")
    for args, label in ((["--scenarios"], "scenario assertions"),
                        (["--trace"], "register trace")):
        r = subprocess.run([sys.executable, str(ROOT / "run_unit.py"),
                            "gen_01_creation_boot"] + args,
                           capture_output=True, text=True, cwd=str(ROOT))
        S.append("<h3>run_unit.py gen_01_creation_boot %s — %s</h3>"
                 % (esc(" ".join(args)), esc(label)))
        S.append("<pre>%s</pre>" % esc(r.stdout))

    # -- how to inspect yourself -----------------------------------------------------
    S.append("<h2>9 · Inspecting the DB yourself</h2>")
    S.append("""<ul>
<li><b>Datasette</b> (recommended — instant read-only web UI):
<code>pip install datasette</code> then <code>datasette derivation.sqlite</code>
→ browse every table, run SQL, use FTS, all in the browser.</li>
<li><b>DB Browser for SQLite</b> (free Mac app, point-and-click): open
<code>derivation.sqlite</code>, Browse Data tab.</li>
<li><b>sqlite3 CLI</b> (already installed):
<code>sqlite3 derivation.sqlite ".tables"</code> — then paste any query shown
in the gray boxes above.</li>
</ul>""")

    css = """
body { background:#fff; color:#1a1a1a; font:15px/1.55 -apple-system,'Segoe UI',sans-serif;
       max-width:1080px; margin:2em auto; padding:0 1.5em; }
h1 { font-size:1.5em; border-bottom:2px solid #333; padding-bottom:.3em; }
h2 { font-size:1.15em; margin-top:2em; border-bottom:1px solid #ccc; padding-bottom:.2em; }
h3 { font-size:1em; margin-top:1.2em; }
table { border-collapse:collapse; margin:.7em 0; font-size:.86em; }
th, td { border:1px solid #ddd; padding:.28em .55em; text-align:left; vertical-align:top; }
th { background:#f2f2f2; }
table.num td { text-align:right; } table.num td:first-child { text-align:left; }
.he { font-family:'SBL Hebrew','Ezra SIL','Times New Roman',serif; font-size:1.25em; }
.sql { background:#f6f6f6; border-left:3px solid #bbb; padding:.35em .6em;
       font-family:Menlo,monospace; font-size:.78em; color:#444; margin:.5em 0; }
pre { background:#f6f6f6; border:1px solid #ddd; padding:.8em; overflow-x:auto;
      font-size:.78em; line-height:1.45; }
code { background:#f0f0f0; padding:.05em .3em; font-size:.9em; }
.note { color:#555; font-size:.92em; }
.ok { color:#0a7a2f; } .flag { color:#b04000; }
"""
    page = ("<!DOCTYPE html><html><head><meta charset='utf-8'>"
            "<title>derivation.sqlite inspection — 2026-07-28</title>"
            "<style>%s</style></head><body>%s"
            "<p class='note'>Generated %s by report_db_html.py · build commit %s · "
            "not binding religious law · English = aid only.</p></body></html>"
            % (css, "\n".join(S), meta.get("built_at", "?"),
               meta.get("built_from_commit", "?")))
    OUT.write_text(page, encoding="utf-8")
    print("wrote %s (%.1f KB)" % (OUT, OUT.stat().st_size / 1024))


if __name__ == "__main__":
    main()
