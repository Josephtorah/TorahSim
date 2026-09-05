#!/usr/bin/env python3
"""build_linked.py — one page, five layers, each opening in place.

  block   (the 31 weekly-portion blocks: mode, counts, plain sentences)
   └ unit     (one line per span: what it installs, its compiled function)
      └ verse    (the verse in plain English, what the code does with it)
         └ code     (the operators as written, the claims checked here)
            └ evidence (per claim: full text, source row, the check run;
                        per verse: the Hebrew with its English, the two
                        cantillation arms; per operator: citations)

Outward links (not embedded): each unit to its existing page, runnable
rendering, and manifest; each block to the exam reports and reading
ledgers whose names match it; each book to its topic-level exam reports.

Read-only over the repository. Writes ONLY ARCHITECTURE/program/LINKED.html.

    python3 ARCHITECTURE/tools/build_linked.py
"""
import glob, html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_program_outline import (ROOT, OUT, cw, gloss_db, unit_outline, load_manifest, norm_ref_key,
                                   gloss_translits, gloss_jargon, gloss_hebrew_runs, shorten, compiled_for)
from build_plain_outline import unit_plain, unshout, plural
from build_summary import BLOCKS, COUNT_OPS
import collections

E = html.escape
REL = "../.."   # from ARCHITECTURE/program/ to the repo root

# topic-level exam reports that do not carry a portion's name
BOOK_REPORTS = {
    "Genesis": ["ALTAR_PRESINAI", "BETROTHAL", "BIRTH_BODY", "CIRCUMCISION", "CONDUCT_GEN", "COURTS_GEN",
                "COVENANT", "INHERITANCE", "KINDNESS", "LEVIRATE", "NAME_INK", "PRAYERBOOK", "TABLE_KNIFE", "NOAHIDE"],
    "Exodus": ["LEAVEN", "COURTS", "PERSONS_OATHS", "PESACH", "SHABBAT", "MATZA", "EGYPT", "CALENDAR", "CAPITAL",
               "COVENANT", "CONDUCT", "INK", "SANCTUARY", "VESTMENTS", "SERVICE", "DECALOGUE", "FESTIVALS",
               "MISHPATIM_COMPILATION", "BACKFILL"],
    "Leviticus": ["CODE_EXECUTION"],
}
EXTRA_BLOCK_REPORTS = {   # portion -> reports whose subject is that portion's span
    "Bo": ["PESACH", "LEAVEN", "MATZA", "EGYPT"], "Yitro": ["DECALOGUE", "COURTS"],
    "Mishpatim": ["MISHPATIM_COMPILATION", "PERSONS_OATHS", "CAPITAL", "CALENDAR", "COVENANT"],
    "Terumah": ["TERUMAH", "SANCTUARY"], "Tetzaveh": ["TETZAVEH", "VESTMENTS", "SERVICE"],
    "Ki Tisa": ["KITISA", "SHABBAT"], "Vayakhel": ["VAYAKHEL_PEKUDEI"], "Pekudei": ["VAYAKHEL_PEKUDEI"],
    "Vayikra": ["VAYIKRA"], "Tzav": ["TZAV"], "Shemini": ["SHEMINI"], "Tazria": ["TAZRIA"], "Metzora": ["TAZRIA"],
    "Acharei Mot": ["ACHAREI"], "Kedoshim": ["ACHAREI"], "Emor": ["EMOR", "LEV24"],
}


PARASHAH_GLOSS = {
    "Bereshit": "in the beginning", "Noach": "Noah", "Lech Lecha": "go forth", "Vayera": "and He appeared",
    "Chayei Sarah": "the life of Sarah", "Toledot": "generations", "Vayetze": "and he went out",
    "Vayishlach": "and he sent", "Vayeshev": "and he settled", "Miketz": "at the end", "Vayigash": "and he drew near",
    "Vayechi": "and he lived", "Shemot": "names", "Va'era": "and I appeared", "Bo": "come", "Beshalach": "when he sent",
    "Yitro": "Jethro", "Mishpatim": "ordinances", "Terumah": "the offering", "Tetzaveh": "you shall command",
    "Ki Tisa": "when you take a census", "Vayakhel": "and he assembled", "Pekudei": "the accounts",
    "Vayikra": "and He called", "Tzav": "command", "Shemini": "the eighth", "Tazria": "she conceives",
    "Metzora": "the leper", "Acharei Mot": "after the death", "Kedoshim": "holy ones", "Emor": "say",
    "Behar": "on the mount", "Bechukotai": "in My statutes",
}


def read_narrative(path):
    """NARRATIVE.md -> {block name: [(bullet, paragraph), ...]}"""
    out, cur = {}, None
    if not os.path.exists(path):
        return out
    for line in open(path, encoding="utf-8").read().split("\n"):
        if line.startswith("## "):
            name = line[3:].split(" — ")[0]
            name = re.sub(r"\s*\(.*?\)\s*$", "", name).strip()
            cur = out.setdefault(name, [])
        elif cur is not None and line.startswith("- "):
            cur.append([line[2:].strip(), ""])
        elif cur is not None and line.startswith("  ") and line.strip() and cur:
            cur[-1][1] = (cur[-1][1] + " " + line.strip()).strip()
    return out


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def records_for(name, uids):
    reports = set(EXTRA_BLOCK_REPORTS.get(name, []))
    toks = [t for t in re.split(r"[^a-z]+", name.lower()) if len(t) >= 4]
    for p in glob.glob(os.path.join(ROOT, "World", "step9", "REPORT_*.md")):
        b = os.path.basename(p)[7:-3]
        if any(t in b.lower() for t in toks):
            reports.add(b)
    ledgers = []
    prefixes = tuple(sorted({"_".join(u.split("_")[:2]) for u in uids}))
    for p in sorted(glob.glob(os.path.join(ROOT, "logic", "oral_triage", "*.md"))):
        b = os.path.basename(p)
        if b.startswith(prefixes) or any(t in b.lower() for t in toks):
            ledgers.append(b)
    out = []
    for r in sorted(reports):
        if os.path.exists(os.path.join(ROOT, "World", "step9", "REPORT_%s.md" % r)):
            out.append(("report %s" % r.replace("_", " ").lower(), "%s/World/step9/REPORT_%s.md" % (REL, r)))
    # block-level: only the ledgers that carry the portion's own name (exam ledgers);
    # per-unit reading ledgers are linked from their units instead
    for l in ledgers:
        if not l.startswith(prefixes):
            out.append(("ledger %s" % l[:-3], "%s/logic/oral_triage/%s" % (REL, l)))
    return out


def unit_ledgers(uid):
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, "logic", "oral_triage", uid + "_*.md"))):
        b = os.path.basename(p)
        out.append(("reading ledger %s" % b[len(uid) + 1:-3], "%s/logic/oral_triage/%s" % (REL, b)))
    return out


def links_html(pairs):
    return " ".join('<a class="out" href="%s">%s</a>' % (E(href), E(label)) for label, href in pairs)


def glossed(text, ref, gmap):
    """gloss every Hebrew run and transliteration in a standalone evidence text"""
    return gloss_jargon(gloss_translits(gloss_hebrew_runs(str(text or ""), ref), gmap, set()), set())


def evidence_for_claim(c, ref, gmap):
    parts = []
    full = glossed(unshout(str(c.get("claim_en") or "")), ref, gmap)
    parts.append('<p><b>The claim in full.</b> %s</p>' % E(full))
    if c.get("source"):
        parts.append('<p><b>Source row.</b> %s</p>' % E(glossed(str(c["source"]), ref, gmap)))
    if c.get("ref"):
        parts.append('<p><b>Anchored at.</b> %s</p>' % E(str(c["ref"])))
    chk = c.get("check")
    if chk:
        try:
            txt = json.dumps(chk, ensure_ascii=False)
        except Exception:
            txt = str(chk)
        parts.append('<p><b>The check the machine ran.</b> <code>%s</code></p>' % E(glossed(txt, ref, gmap)))
    for k in ("status", "verdict", "result"):
        if c.get(k):
            parts.append('<p><b>%s.</b> %s</p>' % (k.title(), E(str(c[k]))))
    return "".join(parts)


def evidence_for_verse(step, verse_en, ref, gmap):
    parts = []
    he = str(step.get("he") or "").strip()
    if he:
        tr = str(step.get("he_translit") or "").strip()
        parts.append('<p><b>The verse.</b> <span dir="rtl" class="he">%s</span>%s — %s</p>'
                     % (E(he), (" <i>%s</i>" % E(tr)) if tr else "", E(verse_en or "")))
    for side, label in (("tree_left", "left arm, before the main pause"), ("tree_right", "right arm, after it")):
        t = step.get(side) or {}
        if t.get("he"):
            parts.append('<p><b>%s.</b> <span dir="rtl" class="he">%s</span> — %s</p>'
                         % (label.capitalize(), E(str(t["he"])), E(glossed(str(t.get("en") or ""), ref, gmap))))
    if step.get("comment"):
        parts.append('<p><b>The unit\'s note.</b> %s</p>' % E(glossed(unshout(shorten(step["comment"], 600)), ref, gmap)))
    return "".join(parts)


def op_cites(o):
    cites = o.get("cites") or []
    conf = o.get("confidence")
    bits = []
    if cites:
        bits.append("cites " + ", ".join(str(c) for c in cites[:6]))
    if conf:
        bits.append("confidence: %s" % conf)
    return " · ".join(bits)


def build_unit(uid, d):
    ph, prows = unit_plain(uid, d)
    ch, csteps = unit_outline(uid, d)
    raw_steps = d.get("boot_steps") or []
    refs = [s.get("ref") for s in raw_steps if s.get("ref")]
    try:
        gmap = gloss_db.build_translit_gloss(refs)
    except Exception:
        gmap = {}
    manifest = load_manifest(uid)
    line = "; ".join(ph["summary"]) if ph["summary"] else "reads %d verses into claims" % ph["n_steps"]
    outs = []
    for label, rel in (("unit page", "logic/pre_logic_methods_2026-07-28/UNIT_%s.html" % uid),
                       ("runnable rendering", "logic/py_units/%s.py" % uid),
                       ("manifest", "logic/oral_audit/manifests/%s_claims.json" % uid),
                       ("unit source", "logic/units/%s.yaml" % uid)):
        if os.path.exists(os.path.join(ROOT, rel)):
            outs.append((label, "%s/%s" % (REL, rel)))
    outs += unit_ledgers(uid)
    H = ['<details class="unit" id="u-%s"><summary><span class="ref">%s %s</span> <b>%s</b> '
         '<span class="counts">%s; %s checked</span>%s</summary>'
         % (E(uid), E(ph["book"]), E(ph["refs"]), E(ph["title"]), E(line), E(plural(ph["n_claims"], "claim")),
            (' <span class="compiled">compiled: %s</span>' % E(ph["compiled"])) if ph["compiled"] else "")]
    H.append('<p class="links">%s</p>' % links_html([(l + " →", h) for l, h in outs]))
    if ph["after"]:
        H.append('<p class="after"><b>Afterwards:</b> %s</p>' % E(ph["after"][0]))
    H.append("<ul class=\"verses\">")
    for i, (pr, cs, raw) in enumerate(zip(prows, csteps, raw_steps)):
        ref = str(raw.get("ref") or "")
        vid = "v-%s-%d" % (uid, i + 1)
        H.append('<li class="verse" id="%s"><b>%s</b> %s%s' % (E(vid), E(pr["ref"]), E(pr["verse"]),
                                                              ' <i class="wbw">(word by word)</i>' if pr["wbw"] else ""))
        if pr["does"]:
            H.append('<div class="does"><b>What the code does:</b> %s.</div>' % E("; ".join(pr["does"])))
        for n in pr["notes"]:
            H.append('<div class="note"><b>The shelf adds:</b> %s</div>' % E(n))
        # ---- code layer
        claims_raw = manifest.get(norm_ref_key(ref), [])
        H.append('<details class="code"><summary>code</summary>')
        if cs["ops"]:
            H.append("<ul>")
            for (op, kind, txt), o in zip(cs["ops"], [o for o in (raw.get("operators") or []) if (o.get("expr_en") or o.get("en"))]):
                extra = op_cites(o)
                H.append('<li class="op %s"><code>%s</code> %s%s</li>'
                         % (kind, E(op), E(txt), (' <small>%s</small>' % E(extra)) if extra else ""))
            H.append("</ul>")
        if claims_raw:
            H.append('<ul class="claims">')
            for c in claims_raw:
                H.append('<li class="claim"><code>%s</code> %s<details class="evidence"><summary>evidence</summary>%s</details></li>'
                         % (E(str(c.get("id"))), E(glossed(unshout(shorten(c.get("claim_en"), 220)), ref, gmap)),
                            evidence_for_claim(c, ref, gmap)))
            H.append("</ul>")
        H.append('<details class="evidence"><summary>the verse\'s letters</summary>%s</details>'
                 % evidence_for_verse(raw, pr["verse"], ref, gmap))
        H.append("</details></li>")
    # claims with no single verse anchor
    step_keys = {norm_ref_key(s.get("ref")) for s in raw_steps}
    loose = [c for k, cl in manifest.items() if k not in step_keys for c in cl]
    if loose:
        H.append('<li class="verse"><b>Checked across the span</b><details class="code"><summary>code</summary><ul class="claims">')
        for c in loose:
            H.append('<li class="claim"><code>%s</code> %s<details class="evidence"><summary>evidence</summary>%s</details></li>'
                     % (E(str(c.get("id"))), E(glossed(unshout(shorten(c.get("claim_en"), 220)), refs[0] if refs else "", gmap)),
                        evidence_for_claim(c, refs[0] if refs else "", gmap)))
        H.append("</ul></details></li>")
    H.append("</ul>")
    if ph["exports"]:
        H.append('<p class="exports"><b>What this span hands forward:</b> %s.</p>' % E("; ".join(ph["exports"])))
    H.append("</details>")
    return "\n".join(H), ph


CSS = """<style>
body{font-family:Georgia,serif;max-width:1040px;margin:1.2rem auto;padding:0 1rem;line-height:1.5;color:#1e1b14;background:#fbf8f0}
h1{color:#6e5417;border-bottom:2px solid #cdb56a;padding-bottom:.3rem;font-size:1.5rem}h2{color:#6e5417;margin-top:2.2rem}
p.intro,p.booklinks{color:#57503f;font-size:.95em}
nav{position:sticky;top:0;background:#fffdf6;border:1px solid #cdb56a;border-radius:8px;padding:.6rem 1rem;margin:1rem 0;z-index:3;display:flex;gap:.8rem;flex-wrap:wrap;align-items:center}
nav a{color:#2f5d8a}nav input#q{flex:1;min-width:220px;padding:.35rem .6rem;border:1px solid #cdb56a;border-radius:6px;font:inherit}
nav label{font-size:.9em;color:#57503f}
details{border-radius:8px}summary{cursor:pointer}
section.block{margin:0 0 1.2rem}h3{margin:1.6rem 0 .2rem;color:#1e1b14}h3 span{color:#8a6d2f;font-weight:normal}
p.mode{color:#a33b1f;font-style:italic;margin:0 0 .3rem}p.counts{font-size:.85em;color:#57503f;margin:.2rem 0 .5rem}
.compiled{font-size:.85em;color:#2f5d8a}
details.story summary{list-style:none;cursor:pointer;text-decoration:underline dotted #b89a4a;text-underline-offset:3px}details.story summary::-webkit-details-marker{display:none}
details.story summary:hover{color:#2f5d8a}details.story[open] summary{color:#6e5417}details.story p{margin:.4rem 0 .6rem 1rem;padding-left:.8rem;border-left:3px solid #cdb56a;color:#33302a}
h3 i.gl{color:#57503f;font-size:.8em;font-weight:normal}
details.units{margin:.3rem 0 .6rem}details.units>summary{color:#2f5d8a;text-decoration:underline;font-size:.95em}
details.unit{background:#fbf8f0;border:1px solid #e2d5a8;padding:.3rem .9rem;margin:.5rem 0}
details.unit>summary .ref{color:#8a6d2f}
ul.verses{margin:.3rem 0 .4rem;padding-left:1.2rem}li.verse{margin:.35rem 0}
.does{color:#2f5d8a;font-size:.95em;margin:.1rem 0 .1rem 1rem}.note{color:#7a5a10;font-size:.93em;margin:.1rem 0 .1rem 1rem}
.wbw{color:#8a6d2f;font-size:.85em}
details.code{margin:.15rem 0 .3rem 1rem;font-size:.92em}details.code>summary{color:#8a6d2f;font-size:.85em}
details.code ul{margin:.2rem 0;padding-left:1.1rem}li.op code{background:#e4eedd;padding:.05rem .3rem;border-radius:4px}
li.op.note code{background:#f7ecd0}li.claim code{background:#dde7f0;padding:.05rem .3rem;border-radius:4px}li.op small{color:#57503f}
details.evidence{margin:.1rem 0 .2rem 1rem;font-size:.95em;background:#fff;border:1px dashed #cdb56a;padding:.1rem .7rem}
details.evidence>summary{color:#a33b1f;font-size:.85em}details.evidence p{margin:.35rem 0}.he{font-size:1.15em}
p.links a.out,p.booklinks a.out{font-size:.85em;color:#2f5d8a;margin-right:.7rem}p.links{margin:.2rem 0}
p.after,p.exports{font-size:.9em;color:#57503f;margin:.4rem 0}
.hidden{display:none}body.showcode details.code{display:block}
</style>"""

JS = """<script>
const q=document.getElementById('q');let timer=null;
function filter(){const t=q.value.trim().toLowerCase();
 document.querySelectorAll('section.block').forEach(b=>{let bhit=false;
  b.querySelectorAll('details.unit').forEach(u=>{let uhit=false;
   u.querySelectorAll('li.verse').forEach(v=>{const hit=!t||v.textContent.toLowerCase().includes(t);v.classList.toggle('hidden',!hit);if(hit)uhit=true;});
   const own=!t||u.querySelector('summary').textContent.toLowerCase().includes(t);
   if(own&&t){u.querySelectorAll('li.verse').forEach(v=>v.classList.remove('hidden'));uhit=true;}
   u.classList.toggle('hidden',!(uhit||own));if(t&&(uhit||own))u.open=true;if(uhit||own)bhit=true;});
  const bown=!t||b.querySelector('h3').textContent.toLowerCase().includes(t)||[...b.querySelectorAll(':scope>ul>li')].some(li=>li.textContent.toLowerCase().includes(t));
  if(bown&&t){b.querySelectorAll('details.unit,li.verse').forEach(x=>x.classList.remove('hidden'));bhit=true;}
  b.classList.toggle('hidden',!(bhit||bown));const du=b.querySelector('details.units');if(du&&t&&bhit)du.open=true;});}
q.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(filter,250);});
document.getElementById('openall').onclick=e=>{e.preventDefault();document.querySelectorAll('details.units,details.unit').forEach(x=>x.open=true);};
document.getElementById('closeall').onclick=e=>{e.preventDefault();document.querySelectorAll('details').forEach(x=>x.open=false);};
document.getElementById('codetoggle').onchange=e=>{document.querySelectorAll('details.code').forEach(x=>x.open=e.target.checked);};
if(location.hash){const el=document.querySelector(location.hash);if(el){let p=el;while(p){if(p.tagName==='DETAILS')p.open=true;p=p.parentElement;}el.scrollIntoView();}}
</script>"""


NARRATIVE = {}


def main():
    global NARRATIVE
    narrative_mode = "--narrative" in sys.argv
    NARRATIVE = read_narrative(os.path.join(os.path.dirname(HERE), "NARRATIVE.md")) if narrative_mode else {}
    units = dict(cw.frozen_units_in_canonical_order())
    manifests_dir = os.path.join(ROOT, "logic", "oral_audit", "manifests")
    built = {}
    for uid, d in units.items():
        built[uid] = build_unit(uid, d)
    n_units = len(units); n_steps = sum(len(d.get("boot_steps") or []) for d in units.values())
    H = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
         "<title>The Program, Linked</title>", CSS, "</head><body>",
         "<h1>The program, linked: block, unit, verse, code, evidence</h1>",
         '<p class="intro">%d blocks from Genesis 1:1 to %s %s, cut at the scroll\'s weekly-portion breaks. ' % (len(BLOCKS), BLOCKS[-1][0], BLOCKS[-1][2].split("-")[-1]) +
         ('Click a bullet to open its paragraph. ' if NARRATIVE else '') + 'Under each block, a link opens its units. Open a unit for its verses in plain English. Open a verse\'s <i>code</i> for the operators '
         'as written and the claims checked there. Open a claim\'s <i>evidence</i> for its full text, its source row, and the check '
         'the machine ran; open <i>the verse\'s letters</i> for the Hebrew with its English and the two cantillation arms. '
         'Links marked &rarr; leave the page for the unit\'s own files and the block\'s records. '
         'Generated 2026-09-05 from the frozen units: %d units, %d verses.</p>' % (n_units, n_steps),
         '<nav><input id="q" placeholder="search blocks, units, verses, code, and claims ..."> '
         '<a href="#Genesis">Genesis</a><a href="#Exodus">Exodus</a><a href="#Leviticus">Leviticus</a> '
         '<a href="#" id="openall">open all</a><a href="#" id="closeall">close all</a> '
         '<label><input type="checkbox" id="codetoggle"> show code under every verse</label></nav>']
    cur = None
    for book, name, span, mode, prefixes, bullets, compiled in BLOCKS:
        if book != cur:
            cur = book
            n_blocks = sum(1 for b in BLOCKS if b[0] == book)
            H.append('<h2 id="%s">%s — %d blocks</h2>' % (book, book, n_blocks))
            br = [("report %s" % r.replace("_", " ").lower(), "%s/World/step9/REPORT_%s.md" % (REL, r))
                  for r in BOOK_REPORTS.get(book, []) if os.path.exists(os.path.join(ROOT, "World", "step9", "REPORT_%s.md" % r))]
            if br:
                H.append('<p class="booklinks">Book-level exam reports, by topic: %s</p>' % links_html([(l + " →", h) for l, h in br]))
        uids = [u for u in units if any(u.startswith(p) for p in prefixes)]
        c = collections.Counter(); n_v = 0; n_claims = 0
        for u in uids:
            for s in units[u].get("boot_steps") or []:
                n_v += 1
                for o in s.get("operators") or []:
                    k = COUNT_OPS.get(o.get("op"))
                    if k:
                        c[k] += 1
            p = os.path.join(manifests_dir, u + "_claims.json")
            if os.path.exists(p):
                m = json.load(open(p, encoding="utf-8"))
                n_claims += len(m.get("claims") if isinstance(m, dict) else m)
        order = ["acts", "commands", "results", "standing facts", "world entries", "names", "day commits", "cases", "rules", "statutes", "shelf readings"]
        cparts = ["%d %s" % (c[k], k) for k in order if c[k]]
        countline = "%d units, %d verses; %s; %d claims checked" % (len(uids), n_v, ", ".join(cparts) if cparts else "specification steps, no operators", n_claims)
        # the summary's own markup, unchanged (h3, mode, counts, bullets) ...
        H.append('<section class="block" id="b-%s">' % slug(name))
        gl = PARASHAH_GLOSS.get(name)
        H.append('<h3>%s%s <span>%s %s</span></h3>' % (E(name), (' <i class="gl">(%s)</i>' % E(gl)) if (NARRATIVE and gl) else "", E(book), E(span)))
        H.append('<p class="mode">Mode: %s.</p>' % E(mode))
        H.append('<p class="counts">%s%s</p>' % (E(countline), (' <span class="compiled">· compiled: %s</span>' % E(compiled)) if compiled else ""))
        story = NARRATIVE.get(name, []) if NARRATIVE else []
        items = []
        for i, b in enumerate(bullets):
            text, para = (story[i] if i < len(story) else (b, ""))
            text = text or b
            if para:
                items.append('<li><details class="story"><summary>%s</summary><p>%s</p></details></li>' % (E(text), E(para)))
            else:
                items.append("<li>%s</li>" % E(text))
        H.append("<ul>" + "".join(items) + "</ul>")
        # ... then the links added beneath it
        recs = records_for(name, uids)
        if recs:
            H.append('<p class="links">Records for this portion: %s</p>' % links_html([(l + " →", h) for l, h in recs]))
        H.append('<details class="units"><summary>Open the %s of this block</summary>' % plural(len(uids), "unit"))
        for u in uids:
            H.append(built[u][0])
        H.append("</details></section>")
    H += [JS, "</body></html>"]
    fname = "LINKED_NARRATIVE.html" if narrative_mode else "LINKED.html"
    out = os.path.join(OUT, fname)
    open(out, "w", encoding="utf-8").write("\n".join(H))
    n_par = sum(1 for v in NARRATIVE.values() for b, p in v if p)
    print("wrote program/%s %d KB · %d units · %d verses%s" % (fname, os.path.getsize(out) // 1024, n_units, n_steps,
          (" · %d bullets with a paragraph" % n_par) if narrative_mode else ""))


if __name__ == "__main__":
    main()
