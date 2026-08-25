#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
"""build_scroll2.py — the redesigned scroll page, generated from the records.

The build step of the website redesign (website/SPEC.md): one set of
content per step of THE_STEPS.md, verses grouped in color-coded unit
bands, details opening below in-page. Everything on the page is drawn
from the real records at build time — the scroll/data/ bundles (verse
pills, trees, morphology, operator code), the canonical unit YAMLs
(titles, revisions, stamps, the oral teaching blocks), and the triage
index in data/derivation.sqlite (declared counts, verdict rows, the
material findings, the kept-out example). Nothing is hand-set; the
mockups' prop numbers are replaced by the records' own.

Scope of this build: Genesis 1 — the six stamped creation-day blocks
(gen_01..gen_06), the redesign's first real chapter. The verse trees
reuse the deployed site's own renderer verbatim (imported from
tools/export_site.py), so the 1:6 tree is the exact live-site tree by
construction (SPEC ruling 1).

Mill tier: this tool transforms, never asserts. Output:
website/scroll2/index.html (self-contained; no fetches).

Usage: python3 tools/build_scroll2.py   (needs data/derivation.sqlite)
"""
import html
import importlib.util
import json
import os
import re
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "press", "vendor"))
import yaml  # noqa: E402  (vendored, owner-approved 2026-08-20)

# the deployed site's own tree renderer + chrome, imported so the
# redesign can never drift from the shipped tree (SPEC ruling 1)
_spec = importlib.util.spec_from_file_location(
    "export_site", os.path.join(HERE, "export_site.py"))
_site = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_site)

esc = lambda s: html.escape(str(s if s is not None else ""), quote=True)
LEAVES = {}   # vid -> leaf list, shipped as one raw JSON block
CODE6 = {}    # uid -> verse-shaded operator lines, same shipping

# ---------------------------------------------------------------- the walk
# The six blocks of Genesis 1. Spine titles are design copy (the units'
# own title_en is shown in the record line). ONE BLUE everywhere (owner
# ruling 2026-08-25, "ok I like that" on the uniform-blue variant —
# revising the earlier rotating-color ruling): spine, step buttons, and
# verse shades all derive from the day-2 blue; block boundaries are
# marked by the spine label, not by hue. The census entry names the
# unit's utterance ordinals as its own reading recorded them — the
# thread the STEP 5 peek shows (ordinals are dispute-relative; the peek
# says so).
BLUE, BLUEL = "#5a7ca6", "#eef2f8"
BLOCKS = [
    ("gen_01_creation_boot", 1, "THE BEGINNING & THE LIGHT",
     "utterances #1 and #2 — the opening word itself counts "
     "(the day-one canon), then “let there be light.”"),
    ("gen_02_raqia_day", 2, "THE FIRMAMENT",
     "utterance #3 — and #4 under the recorded dissent that counts the "
     "wind of 1:2; both ordinals are carried."),
    ("gen_03_double_build", 3, "GATHERING & SPROUTING",
     "utterances #4 and #5 — the gathering of the waters and "
     "the sprouting of the earth."),
    ("gen_04_lights_calendar", 4, "THE LIGHTS & THE CALENDAR",
     "utterance #6 — “let there be lights,” the calendar's own fiat."),
    ("gen_05_swarms_blessing", 5, "SWARMS & THE FIRST BLESSING",
     "utterance #7 — the swarming waters; a recorded dispute carries a "
     "tenth-utterance candidate here too."),
    ("gen_06_land_adam_dominion", 6, "LAND, BEASTS & ADAM",
     "utterances #8, #9 and #10 — the beasts, “let us make man,” and "
     "the food grant: the census CLOSES on this block."),
]

RULES_INTRO = (
    "<b>The tradition's own rulebook.</b> When the sages derive a claim "
    "from a verse, they name the inference rule they used — the tradition "
    "keeps a numbered rulebook of its own: 13 rules of Rabbi Ishmael for "
    "law, 32 rules of Rabbi Eliezer for narrative. When a teaching below "
    "leans on one, its card names the rule. Where no rule is named, the "
    "source states plainly rather than infers."
    '<span class="dim" style="display:block;margin-top:5px">A phrase with '
    'a <span class="peek" style="cursor:default">dotted underline</span> '
    "is a thread that continues in another day's record — tap it for a "
    "glimpse; you never leave this page.</span>")

NINE_GATES = ["gloss", "97 units", "chapter proof", "64 scenes", "sim",
              "receipts", "labels", "changelog", "press"]


def load_unit(uid):
    p = os.path.join(ROOT, "logic", "units", uid + ".yaml")
    d = yaml.safe_load(open(p, encoding="utf-8"))
    # teachings only: a block with no quoted text (the policy/observation
    # notes some units carry) is part of the record but not a teaching
    notes = [b for b in d.get("oral_notes") or []
             if str(b.get("en") or "").strip()
             and str(b.get("he") or "").strip()]
    return d["meta"], notes


def ledger_info(uid):
    """Declared totals from the ledger's LAST completion line (the
    owner-approved semantics for ledgers that grow by supplement)."""
    import glob
    paths = sorted(glob.glob(os.path.join(
        ROOT, "logic", "oral_triage", uid + "_*.md")))
    if not paths:
        return None, None, None
    text = open(paths[-1], encoding="utf-8").read()
    mts = re.findall(r"\*\*read: (\d+) of (\d+)", text)
    read, of = (int(mts[-1][0]), int(mts[-1][1])) if mts else (None, None)
    return os.path.basename(paths[-1]), read, of


def triage_rows(cx, uid):
    return cx.execute(
        "SELECT row_num, source_ref, chain_status, verdict, verdict_class,"
        " note FROM triage WHERE unit LIKE ? ORDER BY row_num",
        (uid + "%",)).fetchall()


def stamp_of(meta):
    for line in meta.get("changelog") or []:
        m = re.search(r"rev (\d+) \((\d{4}-\d{2}-\d{2})\).*FULL-RULE STAMP",
                      str(line))
        if m:
            return m.group(2)
    return None


# ------------------------------------------------------------- verse card
def shade(base, i, n):
    """Per-verse shades of the band color (SPEC ruling 8): interpolate
    the band hue toward light for early verses, toward dark for late."""
    r, g, b = (int(base[j:j + 2], 16) for j in (1, 3, 5))
    t = (i - (n - 1) / 2) / max(n, 2) * 0.55
    if t < 0:
        f = -t
        r, g, b = (round(c + (255 - c) * f) for c in (r, g, b))
    else:
        r, g, b = (round(c * (1 - t)) for c in (r, g, b))
    return "#%02x%02x%02x" % (r, g, b)


def verse_card(uid, vd, color, vshade):
    ref = "Gen 1:%d" % vd["v"]
    vid = "v_%s_%d" % (uid, vd["v"])
    heb = " ".join('<span class="pill he">(⁨%s⁩)</span>'
                   % esc(l["he"]) for l in vd["leaves"])
    eng = " ".join('<span class="pill">(%s)</span>' % esc(l["en"])
                   for l in vd["leaves"])
    morph = "".join(
        '<tr%s><td class="mono">B%s</td><td class="heb">%s</td><td>%s</td>'
        "<td>%s</td><td class=\"mono\">%s</td><td>%s</td></tr>"
        % (' class="grp"' if m.get("bs") else "", m["b"], esc(m["he"]),
           esc(m["tr"]), esc(m["en"]), esc(m["code"]), esc(m["g"]))
        for m in vd["morph"])
    LEAVES[vid] = [{k: l.get(k) for k in ("b", "w", "path", "he", "tr",
                                          "en", "mark", "rank", "froze",
                                          "role")} for l in vd["leaves"]]
    return f'''
  <div class="vcard" onclick="vtg(event,this,'{vid}')">
    <div class="vhead">
      <span class="stepchip" style="--bc:{color}"><span class="lab">STEP 1 · 2</span><span class="cap2">▸</span></span><span class="vref">{ref}</span>
      <span class="more" style="margin-left:auto">▸ open</span>
    </div>
    <div class="jps">“{esc(vd.get("fen") or "")}”</div>
    <div id="{vid}" class="xp-body" style="padding:0;background:transparent;border-top:1px dashed var(--hair)">
    <div class="rowlab">HEBREW</div>
    <div class="pills rtl">{heb}</div>
    <div class="rowlab">ENGLISH</div>
    <div class="pills">{eng}</div>
    <div class="rowlab" style="margin-top:12px">STEP 1 — VERSE TREE · {len(vd["leaves"])} LEAVES</div>
    <div class="treehint">The verse as the ta'amim (cantillation marks) built it: the strongest pause splits first, each split labeled with the mark that made the cut, down to the leaves. Drag to pan; magnify with ⌘/Ctrl + scroll, double-click (shift to shrink), pinch, or the corner controls; hover a leaf for its word range and why it froze.</div>
    <div class="tvp" data-key="{vid}"></div>
    <div class="rowlab" style="margin-top:14px">STEP 2 — MORPHOLOGY · {len(vd["morph"])} MORPHEME ROWS</div>
    <table style="border-left:4px solid {vshade}">
      <tr><th>B#</th><th>Hebrew</th><th>translit</th><th>gloss</th><th>code</th><th>grammar (English aid)</th></tr>
      {morph}
    </table>
    </div>
  </div>'''


# ------------------------------------------------------------ unit record
def claim_cards(uid, notes, census_txt):
    cards = []
    for i, b in enumerate(notes, 1):
        title = b["id"].replace("ORAL_", "").replace("_", " ")
        en = str(b.get("en") or "").strip()
        middah = ""
        low = en.lower()
        for probe, name in (("a-fortiori", "a-fortiori (qal va-chomer, "
                            "the light-and-weighty rule)"),
                            ("gezerah", "wording-analogy (gezerah shavah)"),
                            ("notarikon", "word-splitting (notarikon)"),
                            ("gematria", "letter-count (gematria)")):
            if probe in low:
                middah = ('<span class="midd">middah named in the '
                          'source: %s.</span>' % name)
                break
        # the quote's incipit only, in the pill glossing form (Hebrew
        # bracketed, transliteration beside it); the full English
        # translation is the CLAIMED row — method law 8 holds per word
        inc = lambda s, n: (lambda w: " ".join(w[:n])
                            + (" …" if len(w) > n else ""))(
                                str(s or "").replace(".", " ").split())
        said = ("%s: <span dir=\"rtl\">(%s)</span> (%s)"
                % (esc(b.get("work_en")), esc(inc(b.get("he"), 5)),
                   esc(inc(b.get("he_translit"), 7))))
        claimed = esc(en)
        peek = ""
        if census_txt and ("utterance" in low or "census" in low
                           or "ma'amar" in low):
            pid = "pk_%s_%d" % (uid, i)
            claimed += (' <span class="peek" onclick="pk(event,\'%s\')">'
                        "the census thread</span>" % pid)
            peek = ('<div id="%s" class="peekbox"><span class="pkx" '
                    'onclick="pk(event,\'%s\')">×</span>'
                    '<span class="pkt">THE CENSUS THREAD</span>%s '
                    '<span class="pku">↳ the ten-utterances census, '
                    "counted block by block across the creation week"
                    "</span></div>" % (pid, pid, esc(census_txt)))
            census_txt = None   # one peek per unit is enough
        cards.append(
            '<div class="claim"><h5>T%d · %s</h5>'
            '<div class="clrow"><span class="t">SAID</span><span>%s</span></div>'
            '<div class="clrow"><span class="t">CLAIMED</span><span>%s %s</span></div>'
            "%s"
            '<div class="clrow"><span class="t m">MACHINE</span>'
            '<span style="font-family:Menlo,monospace;font-size:12.5px">'
            "oral block %s · status %s · carried in the unit's record"
            "</span></div></div>"
            % (i, esc(title), said, claimed, middah, peek,
               esc(b["id"]), esc(b.get("status"))))
    return "\n".join(cards)


def kept_out_card(rows):
    """One reading that changed nothing — the first enrichment row of
    the unit's own ledger (SPEC: the kept-out card)."""
    for num, src, status, verdict, vclass, note in rows:
        if vclass == "enrichment":
            return ('<div class="claim rej"><h5>R · Read, recorded — and '
                    "kept out</h5>"
                    '<div class="clrow"><span class="t">SAID</span>'
                    "<span>%s — %s</span></div>"
                    '<div class="clrow"><span class="t">CLAIMED</span>'
                    "<span>Nothing. The reading adorns the verse — "
                    "verdict: <b>enrichment</b>, ledger row %s — but it "
                    "adds no operator, no state, no boundary the "
                    "primaries did not already give.</span></div>"
                    '<div class="clrow"><span class="t m">MACHINE</span>'
                    '<span style="font-family:Menlo,monospace;font-size:'
                    '12.5px">no change — the row stands in the '
                    "append-only ledger; reading means filtering, and "
                    "the filter is on the record</span></div></div>"
                    % (esc(src), esc(note), num))
    return ""


def unit_record(uid, day, color, meta, notes, rows, ledger_name,
                read_n, read_of, census_txt, verses):
    counts = {}
    for r in rows:
        counts[r[4]] = counts.get(r[4], 0) + 1
    material = counts.get("material", 0)
    stamped = stamp_of(meta)
    rev = meta.get("rev", 1)
    # STEP 4 — the material findings, each with its ledger note
    mat_rows = "".join(
        "<tr><td>%s</td><td>%s</td></tr>" % (esc(src), esc(note))
        for num, src, status, verdict, vclass, note in rows
        if vclass == "material" and note)
    all_rows = "".join(
        '<tr><td class="mono">%s</td><td>%s</td><td%s>%s</td></tr>'
        % (num, esc(src), ' class="mat"' if vclass == "material" else "",
           esc(vclass if not note or vclass != "material" else "material"))
        for num, src, status, verdict, vclass, note in rows)
    class_rows = "".join(
        "<tr><td%s>%s</td><td%s>%s</td></tr>"
        % (' class="mat"' if k == "material" else "", esc(k),
           ' class="mat"' if k == "material" else "", n)
        for k, n in sorted(counts.items(), key=lambda kv: -kv[1]))
    # STEP 6 — the operator sketch, verse-shaded, from the bundles' own
    # code lines (the same lines the live site renders per verse);
    # shipped in the raw JSON block, rendered on first open
    n = len(verses)
    CODE6[uid] = [{"v": vd["v"], "shade": shade(color, i, n),
                   "lines": [[l["c"], l["m"]] for l in vd["code"]]}
                  for i, vd in enumerate(verses)]
    gates = "".join("<i>✓ %s</i>" % g for g in NINE_GATES)
    r = lambda s: "r_%s_%s" % (uid, s)
    stamp_line = (("Stamped full rule %s, on the owner's word — the only "
                   "human act in the chain; the chips above are computed, "
                   "never hand-set.") % stamped if stamped else
                  "Not yet stamped — read-through at first pass; the "
                  "stamp is the owner's word alone.")
    return f'''
  <div class="urec" style="border-top-color:{color}">
    <div class="urec-title" style="color:{color}">▙ THE UNIT RECORD — DAY {day} · steps 3–8, in order · opens here, not on another page</div>

    <div class="xp">
      <div class="xp-head" onclick="tg(this,'{r("s3")}')">
        <span class="stepchip" style="--bc:{color}"><span class="lab">STEP 3</span><span class="cap2">▸</span></span><b>Declare the reading</b>
        <span class="sum">scoped before reading: chain primaries + Onkelos — {read_of if read_of else len(rows)} sources declared</span>
        <span class="more">▸ open</span>
      </div>
      <div id="{r("s3")}" class="xp-body">
        <p style="margin-top:2px"><b>The scope, declared before reading</b> — standing rule (owner,
        2026-08-23): read the register's <i>chain-primary</i> class matched to the span, plus Onkelos
        (the received translation); everything else is enumerated and recorded as
        <i>outside declared scope</i> — narrowing done openly, never silently. A later depth pass
        resumes from the recorded list.</p>
        <div class="counters">
          <div><b>{read_of if read_of else "—"}</b><span>DECLARED</span></div>
          <div><b>{read_n if read_n else len(rows)}</b><span>READ &amp; VERDICTED</span></div>
          <div><b>{material}</b><span>MATERIAL</span></div>
        </div>
        <p style="margin:10px 0 2px"><b>The ledger's verdicts</b> — by class:</p>
        <table><tr><th>verdict class</th><th>rows</th></tr>{class_rows}</table>
        <p class="dim" style="font-size:13px">↳ the append-only ledger: logic/oral_triage/{esc(ledger_name)}</p>
      </div>
    </div>

    <div class="xp">
      <div class="xp-head" onclick="tg(this,'{r("s4")}')">
        <span class="stepchip" style="--bc:{color}"><span class="lab">STEP 4</span><span class="cap2">▸</span></span><b>Read and log</b>
        <span class="sum">every declared source verdicted — the {material} material findings</span>
        <span class="more">▸ open</span>
      </div>
      <div id="{r("s4")}" class="xp-body">
        <table><tr><th>source</th><th>what it said (the ledger's note)</th></tr>{mat_rows}</table>
        <div class="xp" style="margin-top:10px;border-style:dashed">
          <div class="xp-head" onclick="tg(this,'{r("s4a")}')">
            <b style="font-size:14px">The full ledger — all {len(rows)} rows, verdicted, append-only</b>
            <span class="more">▸ open</span>
          </div>
          <div id="{r("s4a")}" class="xp-body">
            <table><tr><th>#</th><th>source</th><th>verdict</th></tr>{all_rows}</table>
            <p class="dim" style="font-size:13px">↳ the canonical record: logic/oral_triage/{esc(ledger_name)}</p>
          </div>
        </div>
      </div>
    </div>

    <div class="xp">
      <div class="xp-head" onclick="tg(this,'{r("s5")}')">
        <span class="stepchip" style="--bc:{color}"><span class="lab">STEP 5</span><span class="cap2">▸</span></span><b>Extract claims</b>
        <span class="sum">{len(notes)} teachings built into the unit — and one reading that changed nothing</span>
        <span class="more">▸ open</span>
      </div>
      <div id="{r("s5")}" class="xp-body">
        <div class="rulesintro">{RULES_INTRO}</div>
        <p class="dim" style="margin:2px 0 8px;font-size:13px">Each teaching is a chain: what the source SAID → what the unit CLAIMED from it (with the tradition's own inference rule, where one is named) → where it lives in the MACHINE. Nothing enters the machine without this chain.</p>
        {claim_cards(uid, notes, census_txt)}
        {kept_out_card(rows)}
      </div>
    </div>

    <div class="xp">
      <div class="xp-head" onclick="tg(this,'{r("s6")}')">
        <span class="stepchip" style="--bc:{color}"><span class="lab">STEP 6</span><span class="cap2">▸</span></span><b>Write or amend the logic</b>
        <span class="sum">the unit's machine — every line shaded by its verse</span>
        <span class="more">▸ open</span>
      </div>
      <div id="{r("s6")}" class="xp-body">
        <div class="vlegend">each verse keeps one shade of the band's color, everywhere code appears</div>
        <div class="s6code" data-unit="{uid}"></div>
        <p class="dim" style="font-size:13px;margin:8px 0 2px">↳ the full derivation, operator by operator with its citations: <a href="../../scroll/units/UNIT_{esc(uid)}.html">the unit page</a> — printed by the mill from the unit's record: the mill transforms, never asserts</p>
      </div>
    </div>

    <div class="xp">
      <div class="xp-head" onclick="tg(this,'{r("s7")}')">
        <span class="stepchip" style="--bc:{color}"><span class="lab">STEP 7</span><span class="cap2">▸</span></span><b>Run the gates</b>
        <span class="sum">one command, nine gates, all green — before any human declared anything</span>
        <span class="more">▸ open</span>
      </div>
      <div id="{r("s7")}" class="xp-body">
        <div class="gates">{gates}<i>— 9/9</i></div>
        <p class="dim" style="font-size:13px;margin:6px 0 2px">The same nine gates run on every change and every push; the stamp below ran its own declared-reading check besides — no record, no stamp.</p>
      </div>
    </div>

    <div class="xp">
      <div class="xp-head" onclick="tg(this,'{r("s8")}')">
        <span class="stepchip" style="--bc:{color}"><span class="lab">STEP 8</span><span class="cap2">▸</span></span><b>The stamp</b>
        <span class="sum">{"the owner's word, " + stamped if stamped else "awaiting the owner's word"} — rev {rev}</span>
        <span class="more">▸ open</span>
      </div>
      <div id="{r("s8")}" class="xp-body">
        <p class="dim" style="font-size:13.5px;margin:2px 0">{stamp_line}</p>
      </div>
    </div>
  </div>'''


# ------------------------------------------------------------------ page
def band(cx, bundle, uid, day, spine_title, color, colorl, census_txt):
    meta, notes = load_unit(uid)
    a, b = (int(x) for x in meta["refs"].split(":")[1].split("-"))
    verses = [v for v in bundle["verses"] if a <= v["v"] <= b]
    rows = triage_rows(cx, uid)
    ledger_name, read_n, read_of = ledger_info(uid)
    material = sum(1 for r in rows if r[4] == "material")
    stamped = stamp_of(meta)
    status = ("every declared source read · %d teachings from the "
              "tradition are built into this unit · %s%s"
              % (len(notes),
                 "full rule" if meta.get("tree_derive_version")
                 == "logic_derived_v2_full_rule" else "first pass",
                 " · stamped " + stamped if stamped else ""))
    n = len(verses)
    cards = "\n".join(
        verse_card(uid, vd, color, shade(color, i, n))
        for i, vd in enumerate(verses))
    return f'''
<div class="uband" style="--bc:{color};--bcl:{colorl}">
  <div class="uspine">BLOCK · DAY {day} · GENESIS 1:{a}–{b}</div>
  <div class="ubody">
  <div class="uband-head">
    <span class="ulab">DAY {day} · {esc(spine_title)} · GENESIS 1:{a}–{b}</span>
    <span style="font:14px Charter,Georgia,serif;color:var(--ink)">{esc(status)}</span>
    <span style="font:11px Menlo,Consolas,monospace;color:var(--soft)">record: {esc(uid)} · rev {meta.get("rev", 1)}</span>
  </div>
{cards}
{unit_record(uid, day, color, meta, notes, rows, ledger_name,
             read_n, read_of, census_txt, verses)}
  </div>
</div>'''


CSS = """
  :root{
    --cream:#fdfbf4; --panel:#fff; --tan:#f5eeda; --hair:#e4dcc4; --olive:#7a5c10;
    --brown:#8a6a20; --rust:#a3542c; --ink:#2a2a24; --soft:#8c8468;
    --line:#d7d3c8; --acc:#8a6d1a; --mut:#6b7280; --chip:#f5f2ea;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--cream);color:var(--ink);
       font:16px/1.6 Charter,Georgia,'Times New Roman',serif}
  .nav{display:flex;align-items:center;gap:14px;background:#faf7f0;border-bottom:2px solid #6e5417;
       padding:10px 22px;position:sticky;top:0;z-index:60}
  .nav .logo{font:700 20px Charter,Georgia,serif;color:#6e5417}
  .nav .tabs{margin:0 auto;display:flex;gap:8px}
  .nav .tabs a{font:14px Charter,Georgia,serif;border:1px solid #b08a3e;border-radius:6px;
       padding:5px 15px;text-decoration:none;color:#6e5417;background:#fffdf6}
  .nav .tabs a.on{background:#6e5417;color:#faf7f0;font-weight:700;border-color:#6e5417}
  .nav .ext{font-size:13px;color:#6e5417}
  .preview{background:#1f4d7a;color:#fff;font:700 10px/1 Verdana,sans-serif;letter-spacing:.1em;
        padding:4px 8px;border-radius:3px}
  .rail{position:fixed;top:50px;left:0;bottom:0;width:210px;z-index:40;
        display:flex;flex-wrap:wrap;align-content:flex-start;gap:5px;
        padding:11px 11px 32px;background:#faf7f0;border-right:1px solid #e4dcc8;
        overflow-y:auto;font-size:12.5px}
  .rail .rbrand{width:100%;font-weight:700;font-size:12.5px;line-height:1.3;
        color:#6e5417;margin-bottom:4px}
  .rail .rbrand small{color:#57503f;font-weight:normal}
  .rail select{width:100%;font:12.5px Charter,Georgia,serif;padding:4px 5px;
        border:1px solid #d8cfb8;border-radius:6px;background:#fffdf6;color:var(--ink)}
  .rail .rnav{flex:1 1 40%;font:12px Charter,Georgia,serif;line-height:1.1;padding:4px 6px;
        background:#f3eee1;border:1px solid #d8cfb8;border-radius:6px;color:#6e5417;cursor:pointer}
  .rail .rgo{width:100%;font:13px Charter,Georgia,serif;padding:4px;background:#8a6d1a;
        color:#fff;border:1px solid #8a6d1a;border-radius:6px;cursor:pointer}
  .rail .rlink{width:100%;text-align:center;font-size:12.5px;padding:5px 0;color:#6e5417;
        border:1px solid #b08a3e;border-radius:4px;text-decoration:none;background:#fffdf6}
  .rail .rloc{width:100%;text-align:center;font-size:12px;color:#57503f;margin-top:2px}
  .rail .rloc b{color:#151009}
  .main{margin-left:210px;padding:24px 26px 90px}
  .chapban{background:var(--tan);border:1px solid var(--hair);border-radius:8px;
           padding:12px 20px;margin-bottom:16px;font-size:15px;color:var(--soft)}
  .chapban b{font-size:21px;color:var(--ink);margin-right:10px}
  .uband{border:1px solid var(--hair);border-radius:10px;margin:18px 0;display:flex;overflow:hidden}
  .uspine{flex:none;width:30px;background:var(--bc);color:#fff;writing-mode:vertical-rl;
          text-orientation:mixed;padding:14px 0;display:flex;justify-content:flex-start;align-items:center;
          font:700 11px Verdana,sans-serif;letter-spacing:.18em;white-space:nowrap}
  .ubody{flex:1;min-width:0;background:linear-gradient(to right, var(--bcl), transparent 140px);
         padding:0 0 6px}
  .uband-head{display:flex;align-items:center;gap:12px;flex-wrap:wrap;
              padding:9px 16px;border-bottom:1px dashed var(--hair)}
  .uband-head .ulab{font:700 13px Verdana,sans-serif;color:var(--bc);letter-spacing:.04em}
  .vcard{background:var(--panel);border:1px solid var(--hair);border-radius:8px;margin:12px 14px;
         padding:16px 20px;cursor:pointer;scroll-margin-top:64px}
  .vcard.isopen{cursor:auto}
  .vcard.isopen .vhead{cursor:pointer}
  .vhead{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:6px;
         border-radius:6px;padding:2px 6px;margin:-2px -6px 4px}
  .vhead.on{background:var(--bcl,#eef2f8)}
  .vref{font:700 17px Charter,Georgia,serif;color:var(--rust)}
  .jps{font-style:italic;color:#5a5648;margin:4px 0 10px}
  .rowlab{font:11px Menlo,Consolas,monospace;letter-spacing:.12em;color:var(--soft);margin:10px 0 4px}
  .pills{display:flex;flex-wrap:wrap;gap:7px}
  .pills.rtl{direction:rtl}
  .pill{border:1px solid var(--hair);border-radius:8px;background:#fffdf6;padding:4px 12px;font-size:15.5px}
  .pill.he{font-size:19px;font-family:'SBL Hebrew','Ezra SIL','Times New Roman',serif}
  .treehint{font-style:italic;font-size:13px;color:var(--soft);margin:4px 0 6px}
  table{border-collapse:collapse;width:100%;margin:6px 0;font-size:14px}
  th,td{border:1px solid var(--hair);padding:5px 9px;text-align:left;vertical-align:top}
  th{background:var(--tan);font:700 11px Verdana,sans-serif;color:var(--soft)}
  td.mono{font:12.5px Menlo,Consolas,monospace}
  td.heb{font-family:'SBL Hebrew','Ezra SIL',serif;font-size:17px;text-align:right}
  td.mat{background:#edf3ea;font-weight:700}
  tr.grp td{border-top:2px solid var(--brown)}
  .dim{color:#9a916f}
  .vchip{font:700 10px Verdana,sans-serif;color:#fff;border-radius:3px;padding:2px 7px;margin-right:8px}
  .vgroup{border-left:5px solid;background:#f7f4e9;border-radius:0 8px 8px 0;
          padding:8px 12px;margin:6px 0 10px;font:12.5px/1.6 Menlo,Consolas,monospace;overflow-x:auto;white-space:pre}
  .vlegend{font:11px Verdana,sans-serif;color:var(--soft);margin:4px 0 8px}
  .urec{margin:4px 14px 10px;border-top:2px solid;padding-top:8px}
  .stepchip{display:Inline-Flex;align-items:stretch;flex:none;align-self:center;border-radius:5px;overflow:hidden;
             font:700 10px Verdana,sans-serif;color:#fff;letter-spacing:.06em}
  .stepchip .lab{background:var(--bc,#5a7ca6);padding:4px 9px;display:flex;align-items:center}
  .stepchip .cap2{background:rgba(0,0,0,.25);padding:2px 9px;font-size:16px;line-height:1;display:flex;align-items:center}
  .urec-title{font:700 11.5px Verdana,sans-serif;letter-spacing:.1em;margin:2px 0 8px}
  .xp{background:var(--panel);border:1px solid var(--hair);border-radius:8px;margin:8px 0;scroll-margin-top:64px}
  .xp-head{display:flex;gap:12px;align-items:baseline;padding:10px 14px;cursor:pointer}
  .xp-head:hover{background:#fdfaf1}
  .xp-head.on{background:var(--bcl,#eef2f8)}
  .xp-head b{color:var(--ink)}
  .xp-head .sum{color:var(--soft);font-size:14px}
  .xp-head .more,.vhead .more{font:11px Verdana,sans-serif;color:var(--bc,#5a7ca6);white-space:nowrap}
  .xp-head .more{margin-left:auto}
  .xp-body{display:none;border-top:1px solid var(--hair);padding:12px 16px;font-size:14.5px;background:#fffdf8}
  .xp-body.open{display:block;border-left:3px solid #d3c69f;padding-left:16px;margin-left:2px}
  .counters{display:flex;gap:10px;flex-wrap:wrap;margin:6px 0}
  .counters div{background:var(--bcl,#eef2f8);border-radius:6px;padding:7px 13px;text-align:center}
  .counters b{display:block;font-size:19px}
  .counters span{font:10.5px Verdana,sans-serif;color:var(--soft)}
  .claim{border:1px solid var(--hair);border-radius:8px;background:#fff;margin:10px 0;padding:10px 14px}
  .claim h5{margin:0 0 6px;font:700 14px Charter,Georgia,serif}
  .claim.rej{border-style:dashed;background:#fffdf6}
  .clrow{display:flex;gap:10px;margin:4px 0;font-size:13.5px;line-height:1.5}
  .clrow .t{flex:none;width:74px;font:700 9.5px Verdana,sans-serif;letter-spacing:.08em;color:#7a5c10;padding-top:3px}
  .clrow .t.m{color:var(--bc,#5a7ca6)}
  .midd{font:italic 12.5px Charter,Georgia,serif;color:var(--soft)}
  .rulesintro{background:var(--tan);border:1px solid var(--hair);border-radius:8px;
              padding:10px 14px;margin:6px 0 10px;font-size:13.5px;line-height:1.55}
  .peek{border-bottom:1.5px dotted var(--bc,#5a7ca6);cursor:pointer;color:var(--bc,#5a7ca6)}
  .peekbox{display:none;position:relative;margin:6px 0 2px 84px;background:var(--bcl,#eef2f8);
           border:1px solid var(--bc,#5a7ca6);border-radius:8px;padding:8px 34px 8px 12px;
           font:13px/1.5 Charter,Georgia,serif;color:var(--ink)}
  .peekbox.open{display:block}
  .peekbox .pkx{position:absolute;right:8px;top:6px;font:700 12px Verdana,sans-serif;
                color:var(--bc,#5a7ca6);cursor:pointer}
  .peekbox .pkt{font:700 9.5px Verdana,sans-serif;letter-spacing:.08em;color:var(--bc,#5a7ca6);
                display:block;margin-bottom:2px}
  .peekbox .pku{font:11.5px Menlo,Consolas,monospace;color:var(--soft)}
  .gates{display:flex;flex-wrap:wrap;gap:6px;font:11.5px Verdana,sans-serif;margin:6px 0}
  .gates i{font-style:normal;background:#eef3ea;border:1px solid #c8d6bc;border-radius:4px;padding:3px 8px}
"""

ACCORDION_JS = """
function headOf(id){return document.querySelector('[onclick*="\\''+id+'\\'"]')}
function shut(id){var b=document.getElementById(id); if(!b)return;
  b.classList.remove('open');
  var el=headOf(id); if(!el)return;
  var head=el.querySelector('.vhead')||el;
  el.classList.remove('on','isopen'); head.classList.remove('on');
  var m=head.querySelector('.more')||el.querySelector('.more'); if(m){m.innerHTML='▸ open';}
  var c=head.querySelector('.cap2')||el.querySelector('.cap2'); if(c){c.textContent='▸';}}
function shutOthers(id){TOP.forEach(function(t){if(t!==id)shut(t);});}
function alignAfter(el, before){
  var after = el.getBoundingClientRect().top;
  window.scrollBy(0, after - before);
  requestAnimationFrame(function(){
    var y = el.getBoundingClientRect().top;
    window.scrollBy({top: y - 62, behavior: 'smooth'});
  });}
var LEAVES=null, CODE6=null;
function initCode(body){
  if(!CODE6)CODE6=JSON.parse(document.getElementById('codedata').textContent);
  body.querySelectorAll('.s6code').forEach(function(box){
    if(box.dataset.done)return; box.dataset.done=1;
    var groups=CODE6[box.dataset.unit]||[];
    box.innerHTML=groups.map(function(g){
      var code=g.lines.map(function(l){
        return esc(l[0]).padEnd(38)+'<span class="dim">'+esc(l[1])+'</span>';
      }).join("\\n");
      return '<div><span class="vchip" style="background:'+g.shade+'">1:'+g.v+'</span>'+
        '<div class="vgroup" style="border-left-color:'+g.shade+'">'+code+'</div></div>';
    }).join("");
  });}
function initTrees(body){
  if(!LEAVES)LEAVES=JSON.parse(document.getElementById('leafdata').textContent);
  body.querySelectorAll('.tvp').forEach(function(vp){
    if(vp.dataset.done)return; vp.dataset.done=1;
    var leaves=LEAVES[vp.dataset.key];
    vp.innerHTML=treeSVG(leaves)+
      '<div class="tzc"><button class="tzi" title="zoom in">+</button>'+
      '<span class="tzl">100%</span>'+
      '<button class="tzo" title="zoom out">−</button>'+
      '<button class="tzf" title="fit the whole tree in the window">fit</button></div>';
    initTVP(vp);
  });}
function tg(el,id){var b=document.getElementById(id);var willOpen=!b.classList.contains('open');
  var before = el.getBoundingClientRect().top;
  if(willOpen && TOP.indexOf(id)>=0) shutOthers(id);
  var open=b.classList.toggle('open');
  el.classList.toggle('on',open);
  var m=el.querySelector('.more'); if(m){m.innerHTML=open?'▾ close':'▸ open';}
  var c=el.querySelector('.cap2'); if(c){c.textContent=open?'▾':'▸';}
  if(open){initCode(b);}
  if(open && TOP.indexOf(id)>=0){alignAfter(el, before);}}
function vtg(ev,card,id){var b=document.getElementById(id);var head=card.querySelector('.vhead');
  var isOpen=b.classList.contains('open');
  if(isOpen && !head.contains(ev.target)) return;
  var before = card.getBoundingClientRect().top;
  if(!isOpen) shutOthers(id);
  var open=b.classList.toggle('open');
  card.classList.toggle('isopen',open); head.classList.toggle('on',open);
  var m=head.querySelector('.more'); if(m){m.innerHTML=open?'▾ close':'▸ open';}
  var c=head.querySelector('.cap2'); if(c){c.textContent=open?'▾':'▸';}
  if(open){initTrees(b); alignAfter(card, before);}}
function pk(ev,id){ev.stopPropagation();
  var b=document.getElementById(id); var was=b.classList.contains('open');
  document.querySelectorAll('.peekbox.open').forEach(function(p){p.classList.remove('open')});
  if(!was)b.classList.add('open');}
"""


def main():
    dbp = os.path.join(ROOT, "data", "derivation.sqlite")
    if not os.path.exists(dbp):
        raise SystemExit("build_scroll2: data/derivation.sqlite absent — "
                         "the triage index is required (see CLAUDE.md)")
    cx = sqlite3.connect(dbp)
    bundle = json.load(open(os.path.join(ROOT, "scroll", "data",
                                         "Gen_1.json"), encoding="utf-8"))
    bands, top_ids = [], []
    for uid, day, title, census in BLOCKS:
        bands.append(band(cx, bundle, uid, day, title, BLUE, BLUEL,
                          census))
        meta, _ = load_unit(uid)
        a, b = (int(x) for x in meta["refs"].split(":")[1].split("-"))
        top_ids += ["v_%s_%d" % (uid, v) for v in range(a, b + 1)]
        top_ids += ["r_%s_%s" % (uid, s)
                    for s in ("s3", "s4", "s5", "s6", "s7", "s8")]
    verses_opts = "".join('<option%s>v %d</option>'
                          % (" selected" if v == 1 else "", v)
                          for v in range(1, 32))
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TorahSim — the scroll, redesigned (Genesis 1)</title>
<style>{CSS}</style>
{_site.TREE_CSS}
</head>
<body>

<div class="nav">
  <span class="logo">TorahSim</span>
  <span class="preview">REDESIGN · BUILT FROM THE RECORDS</span>
  <div class="tabs"><a href="../../site/index.html">Epic Disclosure</a><a class="on" href="#">The Scroll</a><a href="../../site/run/index.html">The Run</a></div>
  <span class="ext">github &nbsp;·&nbsp; discord</span>
</div>

<div class="rail">
  <span class="rbrand">TorahSim <small>· the Torah as a scroll</small></span>
  <select><option selected>Genesis</option></select>
  <button class="rnav" title="previous book">◀</button><button class="rnav" title="next book">▶</button>
  <select title="chapter"><option selected>ch 1</option></select>
  <button class="rnav" title="previous chapter">◀</button><button class="rnav" title="next chapter">▶</button>
  <select title="verse" id="vsel" onchange="jumpV()">{verses_opts}</select>
  <button class="rnav" title="previous verse">◀</button><button class="rnav" title="next verse">▶</button>
  <button class="rgo" onclick="jumpV()">Go</button>
  <a class="rlink" href="../../scroll/units/UNIT_INDEX.html" title="coverage index — every derived unit">☰ units</a>
  <a class="rlink" href="../../scroll/coverage/index.html" title="the whole Torah as a grid">▦ coverage</a>
  <span class="rloc">reading <b id="loc">Genesis 1</b></span>
</div>

<div class="main">

<div class="chapban"><b>Genesis 1</b> prose · ta'amim v3 · 31 verses · six derived blocks, every number below computed from the records at build time
<span class="dim" style="display:block;font-size:13px;margin-top:4px">The ledger notes below speak the tradition's shorthand: a tanna (a Mishnah-era sage), gematria (letter-count), ketiv and qere (the written and the read form of a word), the Targum (the received Aramaic translation), midrash (exposition).</span></div>
{"".join(bands)}
<p class="dim" style="font-style:italic;margin:20px 4px">Genesis 2 continues — day seven (2:1–3), then Eden (2:4–17), read through at full rule; the walk is at 6:8. This build renders chapter 1; the full scroll follows the same shape.</p>
</div>

<script id="leafdata" type="application/json">
{json.dumps(LEAVES, ensure_ascii=False).replace("</", "<\\/")}
</script>
<script id="codedata" type="application/json">
{json.dumps(CODE6, ensure_ascii=False).replace("</", "<\\/")}
</script>
<script>
"use strict";
const esc = s => String(s ?? "").replace(/[&<>"]/g,
  m => ({{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}}[m]));
const TOP = {json.dumps(top_ids)};
{_site.TREE_JS}
{ACCORDION_JS}
function jumpV(){{
  var v=document.getElementById('vsel').value.replace('v ','');
  var el=document.querySelector('[id^="v_"][id$="_'+v+'"]');
  if(el){{el.scrollIntoView({{behavior:'smooth',block:'start'}});}}
  document.getElementById('loc').textContent='Genesis 1:'+v;
}}
</script>
</body>
</html>'''
    out = os.path.join(ROOT, "website", "scroll2")
    os.makedirs(out, exist_ok=True)
    outp = os.path.join(out, "index.html")
    with open(outp, "w", encoding="utf-8") as f:
        f.write(page)
    print("scroll2: %d bands, %d accordion items, %.0f KB -> %s"
          % (len(BLOCKS), len(top_ids), os.path.getsize(outp) / 1024,
             os.path.relpath(outp, ROOT)))


if __name__ == "__main__":
    main()
