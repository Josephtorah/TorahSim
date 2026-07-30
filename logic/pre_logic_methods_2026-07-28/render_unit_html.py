#!/usr/bin/env python3
"""
render_unit_html.py — render a logic unit YAML (the hand-derived, frozen
scholarship) as an HTML report: meta, derivation log, operator lines with TIR
citations, state machine, scenarios, Oral notes, trees, word coverage — plus
a live run_unit.py verification capture at the bottom (computed, not stored).

The YAML stays canonical (Pre-Code rule); this is read-only display.

Usage:  python3 render_unit_html.py gen_01_creation_boot [out.html]
"""

import html
import subprocess
import sys
from datetime import date
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
UNITS = ROOT / "logic" / "units"

CSS = """
body { background:#fff; color:#1f2937; font:16px/1.55 "Charter","Georgia",serif;
       margin:0; padding:2rem 1rem 6rem; }
main { max-width:1200px; margin:0 auto; }
h1 { font-size:1.4rem; border-bottom:2px solid #8a6d1a; padding-bottom:.3rem; }
h2 { font-size:1.1rem; margin-top:2.2rem; border-bottom:1px solid #d7d3c8; padding-bottom:.2rem; }
h3 { font-size:.95rem; margin:1.2rem 0 .4rem; }
.he { font-family:'SBL Hebrew','Ezra SIL','Times New Roman',serif; font-size:1.25em;
      direction:rtl; unicode-bidi:isolate; }
.meta { color:#6b7280; font-size:.85rem; }
.badge { font:.7rem/1.6 monospace; padding:0 .5rem; border-radius:10px; }
.frozen { background:#e8f5ec; color:#0a7a2f; border:1px solid #bfe3ca; }
.tier-v { background:#e8f5ec; color:#0a7a2f; border:1px solid #bfe3ca; }
.tier-o { background:#fff3e0; color:#b04000; border:1px solid #ecc9a8; }
.note { background:#f5f2ea; border:1px solid #d7d3c8; border-radius:8px;
        padding:.6rem .9rem; font-size:.88rem; margin:.8rem 0; }
table { border-collapse:collapse; width:100%; font-size:.84rem; margin:.5rem 0 1rem; }
th { background:#f0ecdf; text-align:left; font-size:.7rem; letter-spacing:.05em;
     text-transform:uppercase; }
th,td { border:1px solid #d7d3c8; padding:.3rem .55rem; vertical-align:top; }
td.he-cell { direction:rtl; text-align:right; font-size:1.1rem; white-space:nowrap; }
.step { border:1px solid #d7d3c8; border-radius:10px; padding:.8rem 1.1rem; margin:1rem 0; }
.step h3 { margin-top:0; color:#8a6d1a; }
.opline td:first-child { font-family:monospace; font-weight:bold; white-space:nowrap; }
.expr { font-family:Menlo,monospace; font-size:.82rem; background:#f7f5ee;
        padding:.1rem .35rem; border-radius:4px; }
.cite { font-family:monospace; font-size:.75rem; color:#4a6da7; }
pre { background:#f7f5ee; border:1px solid #d7d3c8; padding:.7rem .9rem;
      font-size:.75rem; line-height:1.4; overflow-x:auto; }
.arms { display:flex; gap:1rem; flex-wrap:wrap; font-size:.85rem; margin:.4rem 0; }
.arm { flex:1; min-width:280px; background:#faf8f1; border:1px solid #e5e0d0;
       border-radius:8px; padding:.4rem .7rem; }
.arm b { color:#6b7280; font-size:.72rem; text-transform:uppercase; letter-spacing:.05em; }
"""


def esc(x):
    return html.escape("" if x is None else str(x))


def he3(he, tr, en):
    parts = []
    if he:
        parts.append('<span class="he">%s</span>' % esc(he))
    if tr:
        parts.append("<i>%s</i>" % esc(tr))
    if en:
        parts.append(esc(en))
    return " · ".join(parts)


def render(unit_id, out_path):
    u = yaml.safe_load((UNITS / (unit_id + ".yaml")).read_text(encoding="utf-8"))
    m = u.get("meta", {})
    S = []

    S.append("<h1>%s <span class='badge frozen'>%s</span></h1>"
             % (esc(m.get("title_en", unit_id)), esc(m.get("status", "?").upper())))
    S.append('<div class="meta">unit <b>%s</b> · %s %s · derive %s · phase %s</div>'
             % (esc(m.get("id")), esc(m.get("book_en")), esc(m.get("refs")),
                esc(m.get("tree_derive_version")), esc(m.get("tree_derive_phase"))))
    S.append("<p>%s</p>" % he3(m.get("title_he"), m.get("title_he_translit"),
                               m.get("title_he_en")))
    for key in ("frozen_note_en", "method_note_en"):
        if m.get(key):
            S.append('<div class="note">%s</div>' % esc(" ".join(str(m[key]).split())))
    S.append('<div class="meta">confidence: %s</div>'
             % esc(m.get("confidence_overall")))

    # ---- derivation log ----
    if u.get("derivation_log"):
        S.append("<h2>Derivation log (steps A–J)</h2><table>")
        S.append("<tr><th>step</th><th>name</th><th>comment</th><th>confidence</th></tr>")
        for d in u["derivation_log"]:
            S.append("<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td></tr>"
                     % (esc(d.get("step")), esc(d.get("name_en")),
                        esc(" ".join(str(d.get("comment", "")).split())),
                        esc(d.get("confidence"))))
        S.append("</table>")

    # ---- boot steps with operator lines ----
    S.append("<h2>Boot steps — the operator lines (hand-derived, owner-approved)</h2>")
    for st in u.get("boot_steps", []):
        S.append('<div class="step">')
        S.append("<h3>%s · %s · <span class='expr'>%s</span></h3>"
                 % (esc(st.get("id")), esc(st.get("ref")), esc(st.get("op"))))
        S.append("<p>%s</p>" % he3(st.get("he"), st.get("he_translit"),
                                   str(st.get("en", "")).replace("[EN-AID] ", "")))
        arms = []
        for side in ("tree_left", "tree_right"):
            a = st.get(side)
            if a:
                arms.append('<div class="arm"><b>%s</b><br>%s</div>'
                            % (side.replace("tree_", "").upper(),
                               he3(a.get("he"), a.get("he_translit"), a.get("en"))))
        if arms:
            S.append('<div class="arms">%s</div>' % "".join(arms))
        S.append("<table><tr><th>operator</th><th>expression</th>"
                 "<th>Hebrew anchor</th><th>cites</th><th>confidence</th></tr>")
        for op in st.get("operators", []):
            S.append('<tr class="opline"><td>%s</td><td><span class="expr">%s</span>'
                     "%s</td><td>%s</td><td class='cite'>%s</td><td>%s</td></tr>"
                     % (esc(op.get("op")), esc(op.get("expr_en")),
                        ("<br>" + esc(op.get("en"))) if op.get("en") else "",
                        he3(op.get("he"), op.get("he_translit"), None) or "—",
                        esc(", ".join(op.get("cites") or [])) or "—",
                        esc(op.get("confidence"))))
        S.append("</table>")
        if st.get("comment"):
            S.append('<div class="meta">%s</div>'
                     % esc(" ".join(str(st["comment"]).split())))
        S.append("</div>")

    # ---- state machine ----
    sm = u.get("state_machine")
    if sm:
        S.append("<h2>State machine</h2>")
        if sm.get("comment_en"):
            S.append('<div class="meta">%s</div>' % esc(sm["comment_en"]))
        S.append("<table><tr><th>state</th><th>meaning</th></tr>")
        for s in sm.get("states", []):
            S.append("<tr><td><b>%s</b></td><td>%s</td></tr>"
                     % (esc(s.get("id")), esc(s.get("en"))))
        S.append("</table><table><tr><th>from</th><th>to</th><th>via</th></tr>")
        for t in sm.get("transitions", []):
            S.append("<tr><td>%s</td><td>%s</td><td>%s</td></tr>"
                     % (esc(t.get("from")), esc(t.get("to")), esc(t.get("via"))))
        S.append("</table>")
    for sa in u.get("state_after", []) or []:
        S.append('<div class="note"><b>%s</b> — %s</div>'
                 % (esc(sa.get("id")), esc(" ".join(str(sa.get("en", "")).split()))))

    # ---- scenarios ----
    if u.get("scenarios"):
        S.append("<h2>Scenarios (the unit's own test suite)</h2>")
        S.append("<table><tr><th>id</th><th>title</th><th>given</th>"
                 "<th>expect</th><th>anchor</th></tr>")
        for sc in u["scenarios"]:
            S.append("<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
                     % (esc(sc.get("id")), esc(sc.get("title_en")),
                        esc(" ".join(str(sc.get("given_en", "")).split())),
                        esc(" ".join(str(sc.get("expect_en", "")).split())),
                        he3(sc.get("value_he"), sc.get("value_he_translit"), None)))
        S.append("</table>")

    # ---- exports + oral ----
    if u.get("exports"):
        S.append("<h2>Exports (reusable patterns)</h2><table>"
                 "<tr><th>id</th><th>content</th></tr>")
        for e in u["exports"]:
            S.append("<tr><td>%s</td><td>%s</td></tr>"
                     % (esc(e.get("id")),
                        he3(e.get("he"), e.get("he_translit"), e.get("en"))))
        S.append("</table>")
    if u.get("oral_notes"):
        S.append("<h2>Oral notes (named, tiered, dual-track — never merged)</h2>")
        for o in u["oral_notes"]:
            tier = ("tier-v" if o.get("status") == "verified" else "tier-o")
            S.append('<div class="note"><span class="badge %s">%s</span> '
                     "<b>%s</b><br>%s%s</div>"
                     % (tier, esc(o.get("status")), esc(o.get("work_en")),
                        he3(o.get("he"), o.get("he_translit"), o.get("en")),
                        ("<br><i>%s</i>" % esc(" ".join(str(o["comment_en"]).split())))
                        if o.get("comment_en") else ""))

    # ---- trees ----
    vt = (u.get("binary_trees") or {}).get("verse_trees") or {}
    if vt:
        S.append("<h2>Binary trees (ta'amim v3, glue bricks)</h2>")
        for key, t in vt.items():
            S.append("<h3>%s · parser %s · %s words</h3><pre>%s</pre>"
                     % (esc(t.get("osis_id", key)), esc(t.get("parser_status")),
                        esc(t.get("word_count")), esc(t.get("tree_ascii", ""))))

    # ---- word coverage ----
    tc = u.get("tree_coverage")
    if tc and tc.get("verses"):
        total = sum(len(v.get("words", [])) for v in tc["verses"])
        S.append("<h2>Word coverage — %d/%s words with named roles</h2>"
                 % (total, esc(tc.get("word_total", total))))
        S.append("<table><tr><th>ref</th><th>#</th><th>Hebrew</th>"
                 "<th>translit</th><th>English</th><th>role</th><th>kind</th>"
                 "<th>rule</th></tr>")
        for v in tc["verses"]:
            for w in v.get("words", []):
                S.append("<tr><td>%s</td><td>%s</td><td class='he-cell'>%s</td>"
                         "<td>%s</td><td>%s</td><td>%s</td><td>%s</td>"
                         "<td class='cite'>%s</td></tr>"
                         % (esc(v.get("ref")), esc(w.get("index")), esc(w.get("he")),
                            esc(w.get("he_translit")), esc(w.get("en")),
                            esc(w.get("role")), esc(w.get("kind")),
                            esc(w.get("interp_rule"))))
        S.append("</table>")

    # ---- live interpreter verification ----
    S.append("<h2>Machine verification — run_unit.py (computed live, not stored)</h2>")
    r = subprocess.run([sys.executable, str(ROOT / "run_unit.py"),
                        unit_id, "--scenarios"],
                       capture_output=True, text=True, cwd=str(ROOT))
    S.append("<pre>%s</pre>" % esc(r.stdout or r.stderr))

    if u.get("status_note_en"):
        S.append('<div class="note">%s</div>'
                 % esc(" ".join(str(u["status_note_en"]).split())))

    page = ("<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
            "<title>%s — frozen logic unit</title><style>%s</style></head>"
            "<body><main>%s"
            "<p class='meta'>Rendered %s by render_unit_html.py · the YAML is "
            "canonical, this page is read-only display · English = aid only · "
            "not binding religious law.</p></main></body></html>"
            % (esc(unit_id), CSS, "\n".join(S), date.today().isoformat()))
    out_path.write_text(page, encoding="utf-8")
    print("wrote %s (%.0f KB)" % (out_path, out_path.stat().st_size / 1024))


if __name__ == "__main__":
    uid = sys.argv[1] if len(sys.argv) > 1 else "gen_01_creation_boot"
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else \
        HERE / ("UNIT_%s_%s.html" % (uid, date.today().isoformat()))
    render(uid, out)
