#!/usr/bin/env python3
"""build_program_outline.py — the program itself, outlined in scroll order.

Walks every FROZEN unit in canonical order (Genesis 1:1 through the last
frozen Numbers span; the fourth book added 2026-09-13) and writes, for each unit, what its code does:
every step in verse order with the machine operators it installs
(PRECONDITION_STATE, EVENT, DECLARE, RESULT, REGISTRY_INSTALL, STATUTE,
HANDLER, CASE, TEST, ...), the witness readings it records, and the
claims its manifest carries for that verse. Where a span has a
cold-compiled function, the unit header points at it.

Read-only over the repository. Writes ONLY into ARCHITECTURE/program/:
  PROGRAM_OUTLINE.md               the index: every unit, one row
  PROGRAM_GENESIS.md               the Genesis units, step by step
  PROGRAM_EXODUS.md                the Exodus units
  PROGRAM_LEVITICUS.md             the Leviticus units
  PROGRAM_OUTLINE.html             all of it, one page, collapsible

    python3 ARCHITECTURE/tools/build_program_outline.py

Hebrew rule: transliterated tokens inside operator expressions get their
English appended on first use in each unit, from the word database's
own per-verse glosses (gloss_db.build_translit_gloss). Hebrew script in
authored notes is passed through as authored (those notes carry their
glosses inline).
"""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(os.path.dirname(HERE), "program")
os.makedirs(OUT, exist_ok=True)
sys.path.insert(0, ROOT)
import corpus_world as cw          # read-only: frozen_units_in_canonical_order()
import gloss_db                    # read-only: build_translit_gloss()

BOOK = {"gen": "Genesis", "exo": "Exodus", "lev": "Leviticus", "num": "Numbers"}
REFBOOK = {"Gen": "Genesis", "Exod": "Exodus", "Lev": "Leviticus", "Num": "Numbers", "Deut": "Deuteronomy"}
STEP_LABEL = {
    "ETNACHTA_SPLIT": "top split", "TREE_CLAIM": "claim",
    "COND_כי": 'case opener כִּי ("when")', "COND_וכי": 'case opener וְכִי ("and when")',
    "COND_אם": 'branch אִם ("if")', "COND_ואם": 'branch וְאִם ("and if")',
}
MACHINE_OPS = {"PRECONDITION_STATE", "EVENT", "DECLARE", "RESULT", "REGISTRY_INSTALL", "STATUTE",
               "HANDLER", "CASE", "TEST", "NAME", "BLESS", "ASSIGN", "INVARIANT", "COMMIT", "TRIPLE",
               "TIME_ANCHOR", "EVENT_PARTITION", "SECTION", "PATTERN", "ORAL_UTTERANCE"}
NOTE_OPS = {"WITNESS_READ", "WITNESS_STATE", "NOTE_PRESUPPOSED", "NOTE_SPEC_DELTA", "NOTE_ZERO_EVENTS"}

# the compiled functions, by unit id prefix (from FUNCTION_CATALOG.md)
COMPILED = [
    ("exo_12", "cold_run_pesach.py 24/24"), ("exo_13", "cold_run_pesach.py 24/24"),
    ("exo_20", "cold_run_decalogue.py 12/12"),
    ("exo_21", "cold_run_mishpatim.py 23/23 + cold_run_mishpatim_2.py 9/9"),
    ("exo_22", "cold_run_guardians.py 12/12 (22:6-14); mishpatim theft multiples (22:2-3); mishpatim_2 the seducer (22:15-16)"),
    ("exo_23_justice", "cold_run_calendar.py 14/14 (23:10-19)"),
    ("lev_05", "cold_run_vayikra5.py 27/27; cold_run_offerings.py 40/40 (the Lev 1-8 dispatcher)"),
    ("lev_06", "cold_run_tzav.py 33/33; cold_run_offerings.py 40/40"),
    ("lev_07", "cold_run_tzav.py 33/33; cold_run_offerings.py 40/40"),
    ("lev_08", "cold_run_tzav.py 33/33 (the installation); cold_run_offerings.py 40/40"),
    ("lev_01", "cold_run_offerings.py 40/40 (the Lev 1-8 dispatcher)"),
    ("lev_02", "cold_run_offerings.py 40/40"), ("lev_03", "cold_run_offerings.py 40/40"),
    ("lev_04", "cold_run_offerings.py 40/40"),
    ("lev_11", "cold_run_shemini.py 19/19"),
    ("lev_13", "cold_run_negaim.py 16/16 + the ten houses 10/10"), ("lev_14", "cold_run_negaim.py 16/16 + the ten houses 10/10"),
    ("lev_16", "cold_run_yoma.py 18/18"),
    ("lev_23", "cold_run_moadim.py 24/24"),
    ("lev_24_blasphemer", "cold_run_lev24.py 23/23 (exports talion(), called by Mishpatim)"),
    # the fourth book (2026-09-13), the scores from catalog_facts.json's rerun
    ("num_01", "cold_run_bamidbar.py 66/66"),
    ("num_02", "cold_run_bamidbar.py 66/66"),
    ("num_03", "cold_run_bamidbar.py 66/66"),
    ("num_04_kehat", "cold_run_bamidbar.py 66/66"),
    ("num_04_gershon_merari", "cold_run_naso.py 274/274"),
    ("num_05", "cold_run_naso.py 274/274"),
    ("num_06", "cold_run_naso.py 274/274"),
    ("num_07", "cold_run_naso.py 274/274"),
    ("num_08", "cold_run_beha.py 154/154"),
    ("num_09", "cold_run_pesach_sheni.py 26/26"),
    ("num_10", "cold_run_beha.py 154/154"),
    ("num_11", "cold_run_beha.py 154/154"),
    ("num_12", "cold_run_beha.py 154/154"),
    ("num_13", "cold_run_shelach.py 172/172"),
    ("num_14", "cold_run_shelach.py 172/172"),
    ("num_15_offerings_laws", "cold_run_shelach.py 172/172"),
    ("num_15_wood_tzitzit", "cold_run_mekoshesh.py 34/34"),
    ("num_16", "cold_run_korach.py 155/155"),
    ("num_17", "cold_run_korach.py 155/155"),
    ("num_18", "cold_run_korach.py 155/155"),
    ("num_19", "cold_run_chukat.py 159/159"),
    ("num_20", "cold_run_chukat.py 159/159"),
    ("num_21", "cold_run_chukat.py 159/159"),
    ("num_22", "cold_run_balak.py 105/105"),
    ("num_23", "cold_run_balak.py 105/105"),
    ("num_24", "cold_run_balak.py 105/105"),
    ("num_25", "cold_run_balak.py 105/105"),
    ("num_26", "cold_run_second_census.py 70/70"),
    ("num_27", "cold_run_zelophehad.py 55/55"),
    ("num_28", "cold_run_musafim.py 110/110"),
    ("num_29", "cold_run_musafim.py 110/110"),
    ("num_30", "cold_run_vows.py 147/147"),
    ("num_31", "cold_run_midian.py 99/99"),
    ("num_32", "cold_run_gad_reuben.py 74/74"),
    ("num_33", "cold_run_journeys.py 53/53"),
    ("num_34", "cold_run_borders.py 56/56"),
    ("num_35", "cold_run_refuge.py 51/51"),
    ("num_36", "cold_run_zelophehad.py 55/55"),
]


def compiled_for(uid):
    for pre, note in COMPILED:
        if uid.startswith(pre):
            return note
    return None


def ref_str(ref):
    """'Gen.1.1' -> 'Genesis 1:1'"""
    m = re.match(r"([A-Za-z]+)\.(\d+)\.(\d+)", str(ref or ""))
    if not m:
        return str(ref or "")
    return "%s %s:%s" % (REFBOOK.get(m.group(1), m.group(1)), m.group(2), m.group(3))


def clean_en(en):
    en = str(en or "").strip()
    en = re.sub(r"^\[EN-AID(?:/JPS)?\]\s*", "", en)
    if en.startswith("From top split"):
        return ""
    return en


def step_label(op):
    if op in STEP_LABEL:
        return STEP_LABEL[op]
    return str(op or "").replace("_", " ").lower()


def gloss_translits(text, gmap, seen):
    """append (english) after transliterated tokens on first use per unit"""
    def rep(m):
        tok = m.group(0)
        key = tok.replace("-", "_").strip("_")
        if key in seen:
            return tok
        en = gmap.get(key) or gmap.get(tok)
        if not en or en.lower() == key.lower() or len(key) < 3:
            return tok
        seen.add(key)
        return "%s (%s)" % (tok, en)
    return re.sub(r"[a-z][a-z_'\-]{2,}", rep, text)


JARGON_GLOSS = {
    "wayyiqtol": "the narrative past-tense verb form", "weqatal": "the and-then future verb form",
    "jussive": "the let-it-be command mood", "etnachta": "the verse's main pause mark",
    "ketiv": "as written", "qere": "as read", "maqqef": "the joining stroke", "dagesh": "the doubling dot",
    "sheva": "the null vowel", "paseq": "the separator bar", "silluq": "the verse-end accent",
    "zaqef": "a major pause accent", "tifcha": "a minor pause accent", "munach": "a conjunctive accent",
    "gematria": "letter arithmetic", "masorah": "the scribal tradition", "notarikon": "acrostic reading",
    "toledot": "generations", "midrash": "the rabbinic commentary", "targum": "the Aramaic translation",
    "halakha": "law", "aggadah": "narrative teaching", "tanna": "a Mishnah-era teacher",
    "amora": "a Talmud-era teacher", "gezerah": "a decree", "qamatz": "a vowel sign", "patach": "a vowel sign",
    "segol": "a vowel sign", "tzere": "a vowel sign", "chiriq": "a vowel sign", "cholam": "a vowel sign",
    "shuruk": "a vowel sign", "mappiq": "the sounded-letter dot",
}
_JARGON_RE = re.compile(r"\b(%s)\b" % "|".join(sorted(JARGON_GLOSS, key=len, reverse=True)), re.I)


def gloss_jargon(text, seen):
    def rep(m):
        w = m.group(0); k = w.lower()
        if k in seen:
            return w
        seen.add(k)
        return "%s (%s)" % (w, JARGON_GLOSS[k])
    return _JARGON_RE.sub(rep, text)


_HEB_RUN = re.compile(r"[\u05d0-\u05ea][\u0591-\u05ea\u05f0-\u05f4]*")
_GLOSS_NEAR = re.compile(r'^[^.]{0,90}?(\(|"|\'|=|,\s*(the|a|an)\s|—\s*(the|a|an)\s)')


def gloss_hebrew_runs(text, ref):
    """Hebrew script without an English marker within ~90 chars gets the
    word database's interlinear gloss appended (gloss_db.translate_span)."""
    out, last = [], 0
    for m in _HEB_RUN.finditer(text):
        run = m.group(0)
        if len(re.sub(r"[^\u05d0-\u05ea]", "", run)) < 2:
            continue
        tail = text[m.end():m.end() + 120]
        if _GLOSS_NEAR.match(tail):
            continue
        try:
            en = gloss_db.translate_span(run, ref.replace(" ", ".").replace(":", ".") if ref else "")
        except Exception:
            en = ""
        if not en or en == run:
            continue
        out.append(text[last:m.end()]); out.append(' ("%s")' % en); last = m.end()
    out.append(text[last:])
    return "".join(out)


def shorten(s, n):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + " ..."


def load_manifest(uid):
    p = os.path.join(ROOT, "logic", "oral_audit", "manifests", uid + "_claims.json")
    if not os.path.exists(p):
        return {}
    d = json.load(open(p, encoding="utf-8"))
    claims = d.get("claims") if isinstance(d, dict) else d
    by_ref = {}
    for c in claims or []:
        # 'Exod 21:8', 'Exod 21:8-9', 'Exod 21:8, 21:12', 'Exod 21:8-9, 22:1-3' -> first verse
        m = re.match(r"\s*([A-Za-z]+)\s+(\d+):(\d+)", str(c.get("ref", "")))
        key = "%s.%s.%s" % (m.group(1), m.group(2), m.group(3)) if m else ""
        by_ref.setdefault(key, []).append(c)
    return by_ref


def norm_ref_key(ref):
    # 'Exod.21.8' and 'Exod 21:8' -> 'Exod.21.8'
    return str(ref or "").replace(" ", ".").replace(":", ".")


def unit_outline(uid, d):
    """-> (header dict, list of step dicts)"""
    meta = d.get("meta", {})
    steps = d.get("boot_steps") or []
    refs = [s.get("ref") for s in steps if s.get("ref")]
    try:
        gmap = gloss_db.build_translit_gloss(refs)
    except Exception:
        gmap = {}
    seen = set()
    seen_j = set()
    manifest = load_manifest(uid)
    claim_total = sum(len(v) for v in manifest.values())
    out_steps = []
    for s in steps:
        ops = []
        for o in s.get("operators") or []:
            op = str(o.get("op") or "")
            if op in NOTE_OPS:
                txt = gloss_jargon(gloss_translits(gloss_hebrew_runs(shorten(o.get("en") or o.get("expr_en"), 320), s.get("ref")), gmap, seen), seen_j)
                kind = "note"
            else:
                txt = str(o.get("expr_en") or o.get("en") or "").strip()
                txt = gloss_jargon(gloss_translits(shorten(txt, 260), gmap, seen), seen_j)
                kind = "machine"
            if txt:
                ops.append((op, kind, txt))
        claims = manifest.get(norm_ref_key(s.get("ref")), [])
        out_steps.append({
            "ref": ref_str(s.get("ref")), "label": step_label(s.get("op")),
            "en": gloss_jargon(clean_en(s.get("en")), seen_j), "ops": ops,
            "claims": [(c.get("id"), gloss_jargon(gloss_translits(gloss_hebrew_runs(shorten(c.get("claim_en"), 300), s.get("ref")), gmap, seen), seen_j)) for c in claims],
        })
    step_keys = {norm_ref_key(s.get("ref")) for s in steps}
    unanchored = [(c.get("id"), gloss_jargon(gloss_translits(shorten(c.get("claim_en"), 300), gmap, seen), seen_j))
                  for key, cl in manifest.items() if key not in step_keys for c in cl]
    unanchored = [(cid, gloss_hebrew_runs(txt, refs[0] if refs else "")) for cid, txt in unanchored]
    exports = [e.get("en") for e in (d.get("exports") or []) if e.get("en")
               and not str(e.get("en")).startswith(("Joseph-cycle span", "Tree-derived"))]
    after = [a.get("en") for a in (d.get("state_after") or []) if a.get("en")
             and not str(a.get("en")).startswith("Tree-derived")]
    header = {
        "uid": uid, "title": str(meta.get("title_en") or uid).strip(),
        "book": BOOK.get(uid[:3], uid[:3]), "refs": str(meta.get("refs") or ""),
        "n_steps": len(steps), "n_ops": sum(len(s["ops"]) for s in out_steps),
        "n_claims": claim_total, "compiled": compiled_for(uid),
        "exports": exports[:6], "after": after[:2], "unanchored": unanchored,
    }
    return header, out_steps


# ------------------------------------------------------------------ writers
def md_unit(h, steps):
    L = ["### %s — %s %s — %s" % (h["uid"], h["book"], h["refs"], h["title"]), ""]
    meta = "%d steps · %d operators · %d claims" % (h["n_steps"], h["n_ops"], h["n_claims"])
    if h["compiled"]:
        meta += " · compiled: " + h["compiled"]
    L += [meta, ""]
    if h["after"]:
        L += ["State after: " + " ".join(h["after"]), ""]
    for s in steps:
        head = "- **%s** %s" % (s["ref"], s["label"])
        if s["en"]:
            head += ": " + shorten(s["en"], 200)
        L.append(head)
        for op, kind, txt in s["ops"]:
            L.append("  - %s%s: %s" % ("" if kind == "machine" else "", op, txt))
        for cid, txt in s["claims"]:
            L.append("  - claim %s: %s" % (cid, txt))
    if h["unanchored"]:
        L.append("- **claims without a single verse anchor**")
        for cid, txt in h["unanchored"]:
            L.append("  - claim %s: %s" % (cid, txt))
    if h["exports"]:
        L += ["", "Exports: " + "; ".join(shorten(e, 120) for e in h["exports"])]
    L.append("")
    return "\n".join(L)


def html_unit(h, steps, open_default):
    e = html.escape
    parts = ['<details class="unit"%s id="%s"><summary><b>%s</b> <span class="refs">%s %s</span> %s'
             '<span class="counts">%d steps · %d operators · %d claims</span>%s</summary>'
             % (" open" if open_default else "", e(h["uid"]), e(h["uid"]), e(h["book"]), e(h["refs"]),
                e(h["title"]), h["n_steps"], h["n_ops"], h["n_claims"],
                (' <span class="compiled">compiled: %s</span>' % e(h["compiled"])) if h["compiled"] else "")]
    if h["after"]:
        parts.append('<p class="after"><b>State after:</b> %s</p>' % e(" ".join(h["after"])))
    parts.append("<ul>")
    for s in steps:
        head = '<li><b>%s</b> <span class="label">%s</span>' % (e(s["ref"]), e(s["label"]))
        if s["en"]:
            head += ": " + e(shorten(s["en"], 200))
        parts.append(head)
        if s["ops"] or s["claims"]:
            parts.append("<ul>")
            for op, kind, txt in s["ops"]:
                parts.append('<li class="%s"><code>%s</code> %s</li>' % (kind, e(op), e(txt)))
            for cid, txt in s["claims"]:
                parts.append('<li class="claim"><code>%s</code> %s</li>' % (e(cid), e(txt)))
            parts.append("</ul>")
        parts.append("</li>")
    if h["unanchored"]:
        parts.append('<li><b>claims without a single verse anchor</b><ul>')
        for cid, txt in h["unanchored"]:
            parts.append('<li class="claim"><code>%s</code> %s</li>' % (e(cid), e(txt)))
        parts.append("</ul></li>")
    parts.append("</ul>")
    if h["exports"]:
        parts.append('<p class="exports"><b>Exports:</b> %s</p>' % e("; ".join(shorten(x, 120) for x in h["exports"])))
    parts.append("</details>")
    return "\n".join(parts)


CSS = """<style>
body{font-family:Georgia,serif;max-width:1000px;margin:1.5rem auto;padding:0 1rem;line-height:1.5;color:#1e1b14;background:#fbf8f0}
h1{color:#6e5417;border-bottom:2px solid #cdb56a;padding-bottom:.3rem}h2{color:#6e5417;margin-top:2.4rem}
nav{position:sticky;top:0;background:#fffdf6;border:1px solid #cdb56a;border-radius:8px;padding:.6rem 1rem;margin-bottom:1rem;z-index:2}
nav a{margin-right:1rem;color:#2f5d8a}input#q{width:60%;padding:.35rem .6rem;border:1px solid #cdb56a;border-radius:6px;font:inherit}
details.unit{background:#fffdf6;border:1px solid #cdb56a;border-radius:8px;padding:.3rem .9rem;margin:.6rem 0}
details.unit summary{cursor:pointer;line-height:1.4}.refs{color:#8a6d2f}.counts{color:#57503f;font-size:.85em;margin-left:.6rem}
.compiled{display:block;color:#a33b1f;font-size:.85em}.label{color:#8a6d2f;font-style:italic}
li.machine code{background:#e4eedd}li.note code{background:#f7ecd0}li.claim code{background:#dde7f0}
code{padding:.05rem .3rem;border-radius:4px;font-size:.85em}ul{margin:.2rem 0 .4rem 0}li{margin:.15rem 0}
p.after,p.exports{font-size:.9em;color:#57503f;margin:.4rem 0}.legend{font-size:.9em;color:#57503f}
.hidden{display:none}
</style>"""

JS = """<script>
const q=document.getElementById('q');
q.addEventListener('input',()=>{const t=q.value.trim().toLowerCase();
 document.querySelectorAll('details.unit').forEach(u=>{const hit=!t||u.textContent.toLowerCase().includes(t);
 u.classList.toggle('hidden',!hit); if(t&&hit) u.open=true;});});
document.getElementById('openall').onclick=()=>document.querySelectorAll('details.unit').forEach(u=>u.open=true);
document.getElementById('closeall').onclick=()=>document.querySelectorAll('details.unit').forEach(u=>u.open=false);
</script>"""


def main():
    units = cw.frozen_units_in_canonical_order()
    outlined = [unit_outline(uid, d) for uid, d in units]
    by_book = {"Genesis": [], "Exodus": [], "Leviticus": [], "Numbers": []}
    for h, steps in outlined:
        by_book.setdefault(h["book"], []).append((h, steps))
    tot = {"units": len(outlined), "steps": sum(h["n_steps"] for h, _ in outlined),
           "ops": sum(h["n_ops"] for h, _ in outlined), "claims": sum(h["n_claims"] for h, _ in outlined)}

    legend = ("How to read a unit. Each bullet is one verse-step of the unit's program, in verse order: "
              "the verse, the step's kind, and the verse's English where the unit gives one. Under it, "
              "the operators the step installs. Machine operators (green in the HTML) are the code: "
              "PRECONDITION_STATE holds a fact, EVENT records an act, DECLARE issues a command, RESULT "
              "receipts it, REGISTRY_INSTALL adds an entity to the world, NAME binds a name, STATUTE binds a "
              "standing law, HANDLER and CASE install branches, TEST checks, COMMIT closes a ledger day. "
              "Notes (amber) are witness readings: what the teacher's shelf says about that verse, with the "
              "claim id in brackets. Claims (blue) are the unit's manifest rows for that verse, each "
              "machine-checked against the ink. Transliterated tokens carry their English in parentheses "
              "on first use in each unit.")

    # index
    idx = ["# PROGRAM OUTLINE — what the code does, Genesis 1:1 onward", "",
           "Generated %s from the frozen units in canonical order. %d units, %d verse-steps, %d operators, %d claims."
           % ("2026-09-13", tot["units"], tot["steps"], tot["ops"], tot["claims"]),
           "", legend, "",
           "The step-by-step outline is in three files: [Genesis](PROGRAM_GENESIS.md), [Exodus](PROGRAM_EXODUS.md), "
           "[Leviticus](PROGRAM_LEVITICUS.md), [Numbers](PROGRAM_NUMBERS.md); or all at once in [PROGRAM_OUTLINE.html](PROGRAM_OUTLINE.html), "
           "which folds each unit and has a search box. The same walk said in plain English, one bullet per "
           "verse, is [PLAIN_OUTLINE.md](PLAIN_OUTLINE.md).", ""]
    for book in ("Genesis", "Exodus", "Leviticus", "Numbers"):
        rows = by_book.get(book, [])
        idx += ["## %s — %d units" % (book, len(rows)), "",
                "| Unit | Span | What it covers | Steps | Operators | Claims | Compiled function |", "|---|---|---|---|---|---|---|"]
        for h, _ in rows:
            idx.append("| %s | %s | %s | %d | %d | %d | %s |" % (
                h["uid"], h["refs"], h["title"].replace("|", "/"), h["n_steps"], h["n_ops"], h["n_claims"], h["compiled"] or ""))
        idx.append("")
    open(os.path.join(OUT, "PROGRAM_OUTLINE.md"), "w", encoding="utf-8").write("\n".join(idx))

    # per-book markdown
    for book in ("Genesis", "Exodus", "Leviticus", "Numbers"):
        rows = by_book.get(book, [])
        L = ["# PROGRAM — %s, step by step" % book, "", legend, "",
             "Back to the [index](PROGRAM_OUTLINE.md).", ""]
        for h, steps in rows:
            L.append(md_unit(h, steps))
        open(os.path.join(OUT, "PROGRAM_%s.md" % book.upper()), "w", encoding="utf-8").write("\n".join(L))

    # one html
    H = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
         "<title>Program Outline, Genesis through Numbers</title>", CSS, "</head><body>",
         "<h1>The program, outlined: what the code does from Genesis 1:1 onward</h1>",
         '<p class="legend">%s</p>' % html.escape(legend),
         '<p class="legend">%d units · %d verse-steps · %d operators · %d claims · generated 2026-09-13 from the frozen units in canonical order.</p>'
         % (tot["units"], tot["steps"], tot["ops"], tot["claims"]),
         '<nav><input id="q" placeholder="search every unit, step, operator, and claim ..."> '
         '<a href="#Genesis">Genesis</a><a href="#Exodus">Exodus</a><a href="#Leviticus">Leviticus</a><a href="#Numbers">Numbers</a> '
         '<a href="#" id="openall">open all</a><a href="#" id="closeall">close all</a></nav>']
    for book in ("Genesis", "Exodus", "Leviticus", "Numbers"):
        rows = by_book.get(book, [])
        H.append('<h2 id="%s">%s — %d units</h2>' % (book, book, len(rows)))
        for i, (h, steps) in enumerate(rows):
            H.append(html_unit(h, steps, open_default=(book == "Genesis" and i < 7)))
    H += [JS, "</body></html>"]
    open(os.path.join(OUT, "PROGRAM_OUTLINE.html"), "w", encoding="utf-8").write("\n".join(H))

    for f in sorted(os.listdir(OUT)):
        print("wrote program/%-24s %6d KB" % (f, os.path.getsize(os.path.join(OUT, f)) // 1024))
    print("units %d · steps %d · operators %d · claims %d" % (tot["units"], tot["steps"], tot["ops"], tot["claims"]))


if __name__ == "__main__":
    main()
