#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
"""export_site.py — torahsim.org, frozen for static hosting.

The site's front door is Epic Disclosure (Disclosure/Epic_Disclosure.md
rendered to site/index.html by the small markdown converter below —
stock Python, no packages). The Tanakh-run app lives under site/run/:
the live app (app/app.py) is one self-contained page and six JSON
endpoints, and this program renders every endpoint to a file and
patches the page's fetch paths, so the identical interface serves
from any static host (torahsim.org rides Cloudflare Pages):

  api/scenes.json  api/run/<id>.json  api/verse/<ref>.json
  api/forms.json   api/replay.json    api/summary.json
  api/custom/<form>.json   — the custom-facts engines, precomputed over
                             every combination of their offered values

The scroll reader (scroll/: the whole Torah verse by verse, plus the 97
derivation review pages) is already static and is copied through whole;
the exported Tanakh-run header gains a link to it.

Nothing is mocked: every scene, verse, replay event, and custom-facts
result is produced by the real machines at build time. The one shape
change: free-typed parameters (a pit's depth, an ox's value) become
curated value lists so the whole space precomputes — the live app
still takes any value. Each page patch asserts its target exists, so
an app.py edit that would silently break the static site fails loudly.

Usage:  python3 tools/export_site.py        (writes site/, ~a minute)
"""
import importlib.util
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SITE = os.path.join(ROOT, "site")

spec = importlib.util.spec_from_file_location(
    "app", os.path.join(ROOT, "app", "app.py"))
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


DISC = os.path.join(ROOT, "Disclosure", "Epic_Disclosure.md")


def dump(rel, obj):
    path = os.path.join(SITE, "run", rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, default=str)


def ref_slug(ref):
    return re.sub(r"[^A-Za-z0-9.]", "_", ref)


# The free-typed parameters, given their offered values. Every list
# holds the legally interesting neighborhood (the 10-handbreadth pit
# line, the 24-hour slave window) and includes the live default.
OFFER = {
    ("slave_window", "survived_hours"): ["0", "12", "23", "24", "25",
                                         "30", "48"],
    ("pit", "depth"): ["3", "9", "10", "11", "20"],
    ("ox_vs_ox", "gorer_live_value"): ["50", "100", "200", "400"],
    ("ox_vs_ox", "gored_value"): ["100", "200", "400"],
    ("ox_vs_ox", "carcass_value"): ["0", "50", "100", "150"],
    ("court_sale", "theft"): ["200", "500", "1000", "2000"],
    ("court_sale", "worth_six_years_labor"): ["200", "500", "1000",
                                              "2000"],
    # goring-day lists ride dash-joined (the choice format owns the
    # comma); restored to commas before the machine call below
    ("ox_lifecycle", "gorings_on_days"): ["1", "1-2", "1-2-3", "1-2-3-4",
                                          "1-3-20", "1-2-3-10"],
    ("ox_lifecycle", "petting_days_after"): ["0", "1", "2", "3"],
}


def offered_params(fname, spec_params):
    """The form's params with every free-typed one made a choice list."""
    out = []
    for pname, ptype, pdefault in spec_params:
        if ptype in ("int", "str"):
            vals = OFFER[(fname, pname)]
            d = str(pdefault).replace(",", "-")
            assert d in vals, (fname, pname, d)
            out.append((pname, "choice:" + ",".join(vals), d))
        elif ptype == "bool":
            out.append((pname, ptype, pdefault))
        else:
            out.append((pname, ptype, pdefault))
    return out


def combos(params):
    grid = [[]]
    for pname, ptype, _ in params:
        vals = (["true", "false"] if ptype == "bool"
                else ptype[len("choice:"):].split(","))
        grid = [row + [v] for row in grid for v in vals]
    return grid


def build_custom_tables():
    total = 0
    for fname, fspec in app.FORMS.items():
        params = offered_params(fname, fspec["params"])
        table = {}
        for row in combos(params):
            args = {p[0]: v for p, v in zip(params, row)}
            live = dict(args)
            if fname == "ox_lifecycle":
                live["gorings_on_days"] = \
                    live["gorings_on_days"].replace("-", ",")
            try:
                table["|".join(row)] = app.run_form(fname, live)
            except Exception as e:   # surfaced honestly, as the live app does
                table["|".join(row)] = {"error": "%s: %s"
                                        % (type(e).__name__, e)}
        dump(os.path.join("api", "custom", fname + ".json"),
             {"params": params, "table": table})
        total += len(table)
        print("  custom/%-14s %5d combinations" % (fname, len(table)))
    return total


def patch(page, old, new):
    assert page.count(old) == 1, "page patch target not unique: %r" % old
    return page.replace(old, new)


def build_page():
    p = app.PAGE
    p = patch(p, "fetch('/api/scenes')", "fetch('api/scenes.json')")
    p = patch(p, "fetch('/api/forms')", "fetch('api/forms.json')")
    p = patch(p, "fetch('/api/run/'+id)", "fetch('api/run/'+id+'.json')")
    p = patch(p, "fetch('/api/verse?ref='+encodeURIComponent(r))",
              "fetch('api/verse/'+r.replace(/[^A-Za-z0-9.]/g,'_')+'.json')")
    p = patch(p, "fetch('/api/replay')", "fetch('api/replay.json')")
    p = patch(p, "fetch('/api/summary')", "fetch('api/summary.json')")
    p = patch(p, "'run. Every result is a live machine call.</p>';",
              "'run. Every result is a real machine call, precomputed '+"
              "'over the offered values when this site was built (the '+"
              "'live instrument takes any value: python3 app/app.py in '+"
              "'the repository).</p>';")
    p = patch(p,
              "async function runForm(){\n"
              "const k=$('fsel').value,f=new FormData($('fform')),args={};\n"
              "for(const[n,v]of f.entries())args[n]=v;\n"
              "const r=await (await fetch('/api/custom',{method:'POST',\n"
              "headers:{'Content-Type':'application/json'},\n"
              "body:JSON.stringify({form:k,args:args})})).json();\n"
              "$('fout').textContent=JSON.stringify(r,null,2);}",
              "let LOOK={};\n"
              "async function runForm(){\n"
              "const k=$('fsel').value,f=new FormData($('fform')),args={};\n"
              "for(const[n,v]of f.entries())args[n]=v;\n"
              "if(!LOOK[k])LOOK[k]=await (await fetch('api/custom/'+k+"
              "'.json')).json();\n"
              "const key=LOOK[k].params.map(p=>String(args[p[0]]))"
              ".join('|');\n"
              "const r=LOOK[k].table[key]||{note:'combination not in the "
              "precomputed table'};\n"
              "$('fout').textContent=JSON.stringify(r,null,2);}")
    p = patch(p, "experimental model, not binding law</small>",
              "experimental model, not binding law &middot; "
              '<a href="../" style="color:var(--gold);'
              'text-decoration:none">Epic Disclosure</a> &middot; '
              '<a href="../scroll/" style="color:var(--gold);'
              'text-decoration:none">the scroll</a></small>')
    p = patch(p, "TorahSim &middot; MIT license",
              "TorahSim &middot; "
              '<a href="https://github.com/Josephtorah/TorahSim" '
              'style="color:inherit">source</a> &middot; MIT license')
    with open(os.path.join(SITE, "run", "index.html"), "w",
              encoding="utf-8") as f:
        f.write(p)


# ---------------------------------------------------------------------------
# EPIC DISCLOSURE — the front door: Disclosure/Epic_Disclosure.md rendered
# to site/index.html by this small converter (headers, emphasis, lists, one
# table — the only markdown the recital uses). The design was settled in
# mockup review 2026-08-19: one long scroll, fixed table of contents, the
# button masthead, minimum linking into the instruments.
# ---------------------------------------------------------------------------
import html as _html

DISC_LINKS = [
    ("github.com/Josephtorah/TorahSim",
     "https://github.com/Josephtorah/TorahSim", 2),
    ("Genesis 1:1", "scroll/#Gen/1/1", 1),
    ("Sixty-four recorded cases", "run/", 1),
    ("The Ark and the Book",
     "https://github.com/Josephtorah/TorahSim/blob/main/docs/"
     "ARK_AND_THE_BOOK.md", 1),
    ("a Discord channel for this project",
     "https://discord.gg/UXZUguY9Pb", 1),
    ("Ninety-seven units", "scroll/units/UNIT_INDEX.html", 1),
]

GITHUB_SVG = ('<svg class="ic" viewBox="0 0 16 16" aria-hidden="true">'
              '<path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 '
              '2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49'
              '-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15'
              '-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33'
              '.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87'
              '.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82'
              '.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2'
              '-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87'
              ' 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0'
              ' .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>'
              '</svg>')
DISCORD_SVG = ('<svg class="ic" viewBox="0 0 24 24" aria-hidden="true">'
               '<path fill="currentColor" d="M20.317 4.3698a19.7913 19.7913 '
               '0 00-4.8851-1.5152.0741.0741 0 00-.0785.0371c-.211.3753'
               '-.4447.8648-.6083 1.2495-1.8447-.2762-3.68-.2762-5.4868 0'
               '-.1636-.3933-.4058-.8742-.6177-1.2495a.077.077 0 00-.0785'
               '-.037 19.7363 19.7363 0 00-4.8852 1.515.0699.0699 0 00-.0321'
               '.0277C.5334 9.0458-.319 13.5799.0992 18.0578a.0824.0824 0 00'
               '.0312.0561c2.0528 1.5076 4.0413 2.4228 5.9929 3.0294a.0777'
               '.0777 0 00.0842-.0276c.4616-.6304.8731-1.2952 1.226-1.9942a'
               '.076.076 0 00-.0416-.1057c-.6528-.2476-1.2743-.5495-1.8722'
               '-.8923a.077.077 0 01-.0076-.1277c.1258-.0943.2517-.1923'
               '.3718-.2914a.0743.0743 0 01.0776-.0105c3.9278 1.7933 8.18 '
               '1.7933 12.0614 0a.0739.0739 0 01.0785.0095c.1202.099.246'
               '.1981.3728.2924a.077.077 0 01-.0066.1276 12.2986 12.2986 0 '
               '01-1.873.8914.0766.0766 0 00-.0407.1067c.3604.698.7719 '
               '1.3628 1.225 1.9932a.076.076 0 00.0842.0286c1.961-.6067 '
               '3.9495-1.5219 6.0023-3.0294a.077.077 0 00.0313-.0552c.5004'
               '-5.177-.8382-9.6739-3.5485-13.6604a.061.061 0 00-.0312'
               '-.0286zM8.02 15.3312c-1.1825 0-2.1569-1.0857-2.1569-2.419 0'
               '-1.3332.9555-2.4189 2.157-2.4189 1.2108 0 2.1757 1.0952 '
               '2.1568 2.419 0 1.3332-.9555 2.4189-2.1569 2.4189zm7.9748 0c'
               '-1.1825 0-2.1569-1.0857-2.1569-2.419 0-1.3332.9554-2.4189 '
               '2.1569-2.4189 1.2108 0 2.1757 1.0952 2.1568 2.419 0 1.3332'
               '-.946 2.4189-2.1568 2.4189Z"/></svg>')

DISC_PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TorahSim — Epic Disclosure</title>
<style>
:root{--bg:#faf7f0;--ink:#151009;--dim:#57503f;--gold:#6e5417;
--bright:#b08a3e;--line:#e4dcc8;--panel:#f3eee1}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
font:20px/1.7 Georgia,'Times New Roman',serif}
header.site{border-bottom:2px solid var(--gold);padding:0 22px;
display:flex;align-items:center;gap:18px;height:54px;
position:sticky;top:0;background:var(--bg);z-index:20}
header.site .brand{font-size:20px;color:var(--gold);font-weight:bold}
header.site nav{display:flex;gap:10px;font-size:14px;align-items:center}
header.site nav.mid{position:absolute;left:50%%;transform:translateX(-50%%)}
header.site nav.ext{margin-left:auto}
header.site nav a{border:1px solid var(--bright);border-radius:6px;
padding:6px 15px;color:var(--gold);text-decoration:none;
font-family:Georgia,serif;white-space:nowrap;line-height:1}
header.site nav a:hover{background:var(--panel)}
header.site nav a.on{background:var(--gold);color:var(--bg);
border-color:var(--gold);font-weight:bold}
header.site nav.ext a{border:none;padding:6px 4px}
svg.ic{width:15px;height:15px;vertical-align:-2px;margin-right:5px}
main{display:flex;max-width:1320px;margin:0 auto}
#toc{width:330px;flex-shrink:0;position:sticky;top:54px;
align-self:flex-start;max-height:calc(100vh - 80px);overflow-y:auto;
padding:26px 20px;font-size:inherit;line-height:1.4;
border-right:1px solid var(--line)}
#toc a{display:block;color:var(--dim);text-decoration:none;padding:7px 0}
#toc a:hover{color:var(--gold)}
article{max-width:46em;padding:30px 34px 90px;min-width:0}
h1{font-size:44px;line-height:1.15;color:var(--gold);font-weight:normal;
margin:26px 0 6px;letter-spacing:.01em}
h1 + p b{font-size:19px;color:var(--dim);font-weight:normal;
font-style:italic}
h2{font-size:29px;color:var(--gold);font-weight:normal;
margin:56px 0 12px;border-bottom:1px solid var(--line);padding-bottom:8px;
scroll-margin-top:72px}
h3{font-size:21px;color:var(--ink);margin:34px 0 8px}
p{margin:0 0 1.05em}
a{color:var(--gold);text-decoration:none;
border-bottom:1px dotted var(--bright)}
code{font:14px ui-monospace,Menlo,monospace;background:var(--panel);
padding:1px 5px;border-radius:3px}
ul{margin:0 0 1.05em;padding-left:1.4em}
hr{border:none;border-top:1px solid var(--line);margin:34px 0}
.tablewrap{overflow-x:auto;margin:0 0 1.05em}
table{border-collapse:collapse;font-size:14.5px;line-height:1.5}
th,td{border:1px solid var(--line);padding:7px 12px;text-align:left;
vertical-align:top}
th{background:var(--panel);color:var(--gold);font-weight:normal;
text-transform:uppercase;font-size:11.5px;letter-spacing:.09em}
footer{border-top:1px solid var(--line);color:var(--dim);
font-size:12.5px;padding:18px 34px;text-align:center}
#menu{display:none;background:none;border:1px solid var(--line);
border-radius:5px;color:var(--gold);font-size:19px;line-height:1;
padding:5px 9px;cursor:pointer}
@media(max-width:900px){
header.site{height:auto;padding:8px 14px;flex-wrap:wrap}
header.site nav.mid{position:static;transform:none;margin-left:auto}
#toc{display:none}
#toc.open{display:block;position:fixed;top:54px;left:0;bottom:0;
width:min(300px,85vw);background:var(--bg);z-index:10;
border-right:1px solid var(--line);box-shadow:4px 0 18px rgba(0,0,0,.12)}
#menu{display:inline-block}
article{padding:20px 18px 70px}
body{font-size:18px}}
</style></head><body>
<header class="site">
  <button id="menu" aria-label="contents"
    onclick="document.getElementById('toc').classList.toggle('open')">&#9776;</button>
  <span class="brand">TorahSim</span>
  <nav class="mid">
    <a class="on" href="./">Epic Disclosure</a>
    <a href="scroll/">The Scroll</a>
    <a href="run/">The Run</a>
  </nav>
  <nav class="ext">
    <a href="https://github.com/Josephtorah/TorahSim" target="_blank" rel="noopener">%s github</a>
    <a href="https://discord.gg/UXZUguY9Pb" target="_blank" rel="noopener">%s discord</a>
  </nav>
</header>
<main>
<nav id="toc" onclick="if(event.target.tagName==='A')this.classList.remove('open')">%s</nav>
<article>
%s
</article>
</main>
<footer>TorahSim &middot; Epic Disclosure &middot; %s &middot;
experimental model &mdash; not binding religious law &middot;
<a href="https://github.com/Josephtorah/TorahSim" style="color:inherit">source</a></footer>
</body></html>
"""


# ---------------------------------------------------------------------------
# THE SCROLL'S SITE DESIGN — settled in mockup review 2026-08-20 and applied
# at export time as asserted patches, so the received pages in scroll/ stay
# exactly as delivered and a future refresh cannot erase the design:
#   · the button masthead on the scroll page and every unit page
#   · the control bar restyled as a parchment left rail
#   · the chip convention (a border means it goes somewhere; an i-mark
#     means it explains) — frozen chips gold-bordered, oral counters flat
#   · a back button under the masthead on unit pages
# ---------------------------------------------------------------------------
MAST_CSS = """<style>
.mast{border-bottom:2px solid #6e5417;padding:0 22px;display:flex;
align-items:center;gap:18px;height:54px;position:fixed;top:0;left:0;right:0;
background:#faf7f0;z-index:60;font:14px Georgia,serif;box-sizing:border-box}
.mast .brand{font-size:20px;color:#6e5417;font-weight:bold}
.mast nav{display:flex;gap:10px;align-items:center}
.mast nav.mid{position:absolute;left:50%;transform:translateX(-50%)}
.mast nav.ext{margin-left:auto}
.mast nav a{border:1px solid #b08a3e;border-radius:6px;padding:6px 15px;
color:#6e5417;text-decoration:none;white-space:nowrap;line-height:1}
.mast nav a:hover{background:#f3eee1}
.mast nav a.on{background:#6e5417;color:#faf7f0;border-color:#6e5417;
font-weight:bold}
.mast nav.ext a{border:none;padding:6px 4px}
.mast svg.ic{width:15px;height:15px;vertical-align:-2px;margin-right:5px}
</style>"""

SCROLL_RAIL_CSS = """<style>
body{margin-top:54px}
header{position:fixed !important;top:54px;left:0;bottom:0;width:210px;
z-index:40}
.bar{flex-direction:row;flex-wrap:wrap;align-items:stretch;gap:.3rem;
height:100%;overflow-y:auto;max-width:none;padding:.7rem .7rem 2rem;
align-content:flex-start;font-size:12.5px;background:#faf7f0;
border-right:1px solid #e4dcc8}
.bar .brand{width:100%;font-size:12.5px;line-height:1.3;
margin-bottom:.25rem;color:#6e5417}
.bar .brand small{color:#57503f}
.bar select{width:100%;margin:0;font-size:12.5px;padding:.22rem .3rem}
.bar button{font-size:12px;padding:.2rem .4rem}
.bar button.nav{flex:1 1 40%;line-height:1.1;background:#f3eee1;
border:1px solid #d8cfb8;color:#6e5417}
.bar button.nav:hover{background:#e9e2cf;color:#6e5417}
.bar button:not(.nav){width:100%}
.bar a.nav{width:100%;text-align:center;flex:none;font-size:12.5px;
padding:.3rem 0;color:#6e5417 !important;border:1px solid #b08a3e;
border-radius:4px;text-decoration:none}
.bar .search{width:100%;box-sizing:border-box;font-size:12.5px;
padding:.25rem .4rem;background:#fff;border:1px solid #d8cfb8}
.bar .loc{width:100%;text-align:center;font-size:12px;color:#57503f}
.bar .loc b{color:#151009}
main{margin-left:210px;max-width:none;padding:1rem 2rem 8rem}
.results{left:6px;right:auto;width:198px}
.badge.frozen{background:#faf7f0;color:#6e5417 !important;
border:1px solid #b08a3e}
.badge.frozen:hover{background:#6e5417;color:#faf7f0 !important}
.badge.oral{background:none;border:none;color:#57503f}
</style>"""

UNIT_BACK = ('<div style="padding:12px 22px 0">'
             '<button onclick="history.back()" style="border:1px solid '
             '#b08a3e;border-radius:6px;padding:5px 14px;color:#6e5417;'
             'background:none;font:14px Georgia,serif;cursor:pointer">'
             '&#8592; back</button></div>')


def masthead(prefix):
    return (MAST_CSS + '<div class="mast"><span class="brand">TorahSim'
            '</span><nav class="mid">'
            '<a href="%s">Epic Disclosure</a>'
            '<a class="on" href="%sscroll/">The Scroll</a>'
            '<a href="%srun/">The Run</a></nav><nav class="ext">'
            '<a href="https://github.com/Josephtorah/TorahSim" '
            'target="_blank" rel="noopener">%s github</a>'
            '<a href="https://discord.gg/UXZUguY9Pb" '
            'target="_blank" rel="noopener">%s discord</a></nav></div>'
            % (prefix, prefix, prefix, GITHUB_SVG, DISCORD_SVG))


def build_scroll_site():
    sdir = os.path.join(SITE, "scroll")
    path = os.path.join(sdir, "index.html")
    with open(path, encoding="utf-8") as f:
        t = f.read()
    assert t.count("<body>") == 1 and t.count("\U0001F4DC oral") == 1
    t = t.replace("\U0001F4DC oral", "ⓘ oral")
    t = t.replace("<body>", "<body>" + masthead("../") + SCROLL_RAIL_CSS, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(t)
    n = 0
    for name in sorted(os.listdir(os.path.join(sdir, "units"))):
        if not name.endswith(".html"):
            continue
        upath = os.path.join(sdir, "units", name)
        with open(upath, encoding="utf-8") as f:
            u = f.read()
        m = re.search(r"<body[^>]*>", u)
        u = (u[:m.end()] + "<style>body{margin-top:54px}</style>"
             + masthead("../../") + UNIT_BACK + u[m.end():])
        with open(upath, "w", encoding="utf-8") as f:
            f.write(u)
        n += 1
    print("  scroll design            rail + masthead; %d unit pages "
          "stamped" % n)


def _md_inline(s):
    s = _html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", s)
    return s


def build_disclosure():
    text = open(DISC, encoding="utf-8").read()
    m = re.search(r"\*\*Date:\*\* (\S+)\n*", text)
    page_date = m.group(1) if m else ""
    if m:
        text = text.replace(m.group(0), "", 1)

    body, toc = [], []
    lines = text.split("\n")
    i, para = 0, []

    def flush():
        if para:
            body.append("<p>" + _md_inline(" ".join(para)) + "</p>")
            para.clear()

    while i < len(lines):
        ln = lines[i]
        if ln.startswith("# "):
            flush(); body.append("<h1>" + _md_inline(ln[2:]) + "</h1>")
        elif ln.startswith("## "):
            flush()
            sid = "s%d" % (len(toc) + 1)
            toc.append((sid, ln[3:]))
            body.append('<h2 id="%s">%s</h2>' % (sid, _md_inline(ln[3:])))
        elif ln.startswith("### "):
            flush(); body.append("<h3>" + _md_inline(ln[4:]) + "</h3>")
        elif ln.startswith("- "):
            flush()
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append("<li>" + _md_inline(lines[i][2:]) + "</li>")
                i += 1
            body.append("<ul>" + "".join(items) + "</ul>")
            continue
        elif ln.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip("|").split("|")]
                if not set("".join(cells)) <= set("- :"):
                    tag = "th" if not rows else "td"
                    rows.append("<tr>" + "".join(
                        "<%s>%s</%s>" % (tag, _md_inline(c), tag)
                        for c in cells) + "</tr>")
                i += 1
            body.append('<div class="tablewrap"><table>%s</table></div>'
                        % "".join(rows))
            continue
        elif ln.strip() == "---":
            flush(); body.append("<hr>")
        elif ln.strip() == "":
            flush()
        else:
            para.append(ln.strip())
        i += 1
    flush()
    content = "\n".join(body)

    for phrase, url, count in DISC_LINKS:
        assert content.count(phrase) >= count, phrase
        target = "" if url.startswith("http") is False else \
            ' target="_blank" rel="noopener"'
        content = content.replace(
            phrase, '<a href="%s"%s>%s</a>' % (url, target, phrase), count)

    toc_html = "".join('<a href="#%s">%s</a>'
                       % (sid, _html.escape(t)) for sid, t in toc)
    page = DISC_PAGE % (GITHUB_SVG, DISCORD_SVG, toc_html, content,
                        _html.escape(page_date))
    with open(os.path.join(SITE, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    print("  disclosure             %5d sections rendered" % len(toc))


def main():
    if os.path.isdir(SITE):
        shutil.rmtree(SITE)
    os.makedirs(os.path.join(SITE, "run"))
    build_disclosure()

    scenes = []
    for s in app.CAT["scenes"]:
        r = app.HANDLERS[s["id"]](s)
        scenes.append({"id": s["id"], "title_en": s["title_en"],
                       "priority": s["priority"], "mode": s["mode"],
                       "chronology_key": s["chronology_key"],
                       "stamp": r["stamp"]})
    dump("api/scenes.json", scenes)
    for sid in app.SCENES:
        dump(os.path.join("api", "run", sid + ".json"), app.run_scene(sid))
    print("  scenes                 %5d rendered" % len(scenes))

    refs = sorted({r for s in app.CAT["scenes"] for r in s["refs"]})
    for ref in refs:
        dump(os.path.join("api", "verse", ref_slug(ref) + ".json"),
             app.verse_words(ref))
    print("  verses                 %5d interlinear" % len(refs))

    dump("api/forms.json",
         {k: {"label": v["label"],
              "params": offered_params(k, v["params"])}
          for k, v in app.FORMS.items()})
    dump("api/replay.json", app.build_replay())
    dump("api/summary.json", app.build_summary())
    total = build_custom_tables()

    build_page()
    shutil.copy(os.path.join(ROOT, "viz", "inheritance.html"),
                os.path.join(SITE, "inheritance.html"))
    shutil.copytree(os.path.join(ROOT, "scroll"),
                    os.path.join(SITE, "scroll"))
    build_scroll_site()
    # A real 404 page: without one, Pages answers every unknown path with
    # index.html and status 200, which fools the scroll reader's dev-server
    # probe into showing its regenerate button on the public site.
    with open(os.path.join(SITE, "404.html"), "w", encoding="utf-8") as f:
        f.write('<!DOCTYPE html><html lang="en"><head><meta charset='
                '"utf-8"><title>TorahSim — not found</title></head>'
                '<body style="font:15px/1.6 Georgia,serif;background:'
                '#12100d;color:#e8e0d0;padding:40px"><p>Not found. '
                'The front door: <a href="/" style="color:#c9a45c">'
                'torahsim.org</a>.</p></body></html>\n')

    n = sum(len(fs) for _, _, fs in os.walk(SITE))
    mb = sum(os.path.getsize(os.path.join(b, f))
             for b, _, fs in os.walk(SITE) for f in fs) / 1e6
    print("site/: %d files, %.1f MB, %d precomputed machine calls"
          % (n, mb, total))


if __name__ == "__main__":
    main()
