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
    # The run sheds its dark skin for the site: the same parchment ground
    # as the other two pages, keyed to the shared palette. The verdict
    # colors (confirm/diverge/no-verdict/forward) are untouched — they
    # carry meaning and read on either ground.
    p = patch(p, "--bg:#12100d;--panel:#1c1915;--ink:#e8e0d0;"
              "--dim:#9a8f7a;\n--gold:#c9a45c;--line:#2e2a22;",
              "--bg:#faf7f0;--panel:#f3eee1;--ink:#151009;"
              "--dim:#57503f;\n--gold:#6e5417;--line:#e4dcc8;")
    p = patch(p, ".chip.P0{background:var(--gold);color:#241d10}",
              ".chip.P0{background:var(--gold);color:#faf7f0}")
    p = patch(p, ".chip.P1,.chip.P2{background:#3a352b;color:var(--dim)}",
              ".chip.P1,.chip.P2{background:#e4dcc8;color:#57503f}")
    p = patch(p, "form.binder select{width:100%;background:#26221b;",
              "form.binder select{width:100%;background:#fff;")
    p = patch(p, "button.go{background:var(--gold);color:#241d10;",
              "button.go{background:var(--gold);color:#faf7f0;")
    p = patch(p, "pre.out{background:#0d0b08;", "pre.out{background:#f3eee1;")
    p = patch(p, "word-break:break-word;color:#cfc4ab}",
              "word-break:break-word;color:#3a3126}")
    p = patch(p, ".filter select{background:#26221b;",
              ".filter select{background:#fff;")
    p = patch(p, "style=\"background:#26221b;", "style=\"background:#fff;")
    p = patch(p, "border-top:1px solid #333;", "border-top:1px solid #e4dcc8;")
    # The one never-changing masthead, worn here too: the app keeps its
    # own chrome beneath it, pushed down by the masthead's 54px —
    # the three viewport-height panels must shrink by the same 54.
    assert p.count("calc(100vh - 110px)") == 3, "run page height calcs moved"
    p = p.replace("calc(100vh - 110px)", "calc(100vh - 164px)")
    p = patch(p, "</style></head><body>",
              "</style></head><body><style>body{margin-top:54px}</style>"
              + masthead("../", "run"))
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
--bright:#b08a3e;--line:#e4dcc8;--panel:#f3eee1;--hh:54px}
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
padding:56px 20px 26px;font-size:inherit;line-height:1.4;
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
#menu{position:fixed;top:calc(var(--hh) + 8px);left:12px;z-index:30;
background:var(--bg);border:1px solid var(--bright);
border-radius:5px;color:var(--gold);font-size:19px;line-height:1;
padding:5px 9px;cursor:pointer}
#menu:hover{background:var(--panel)}
article{margin:0 auto}
body.flip #toc{display:none}
@media(max-width:900px){
header.site{height:auto;padding:8px 14px;flex-wrap:wrap}
header.site nav.mid{position:static;transform:none;margin-left:auto}
#toc{display:none}
body.flip #toc{display:block;position:fixed;top:var(--hh);left:0;bottom:0;
width:min(300px,85vw);background:var(--bg);z-index:10;overflow-y:auto;
border-right:1px solid var(--line);box-shadow:4px 0 18px rgba(0,0,0,.12)}
article{padding:20px 18px 70px}
body{font-size:18px}}
</style></head><body>
<header class="site">
  <span class="brand">TorahSim</span>
  <nav class="mid">
    <a class="on" href="./">Epic Disclosure</a>
    <a href="scroll/">The Scroll</a>
    <a href="run/">The Run</a>
    <a href="contact/">Contact</a>
  </nav>
  <nav class="ext">
    <a href="https://github.com/Josephtorah/TorahSim" target="_blank" rel="noopener">%s github</a>
    <a href="https://discord.gg/UXZUguY9Pb" target="_blank" rel="noopener">%s discord</a>
  </nav>
</header>
<button id="menu" aria-label="contents"
  onclick="document.body.classList.toggle('flip')">&#9776;</button>
<main>
<nav id="toc" onclick="if(event.target.tagName==='A'&&innerWidth<=900)document.body.classList.remove('flip')">%s</nav>
<article>
%s
</article>
</main>
<footer>TorahSim &middot; Epic Disclosure &middot; %s &middot;
experimental model &mdash; not binding religious law &middot;
<a href="https://github.com/Josephtorah/TorahSim" style="color:inherit">source</a></footer>
<script>
const hh=()=>document.documentElement.style.setProperty('--hh',
document.querySelector('header.site').offsetHeight+'px');
addEventListener('resize',hh);hh();
</script>
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

# The verse-tree window (settled in mockup review 2026-08-20): the leaf
# ledger's path column, drawn. Each verse's binary tree is rebuilt in the
# browser from the leaf paths already shipped in every bundle; the window
# pans by drag and magnifies only on an intentional gesture (Cmd/Ctrl +
# scroll — a trackpad pinch arrives as exactly that — double-click, touch
# pinch, or the corner controls), so a plain wheel keeps scrolling the page.
TREE_CSS = """<style>
.tvp { position:relative; height:300px; border:1px solid var(--line); border-radius:10px;
       overflow:hidden; background:#fffdf6; cursor:grab; user-select:none;
       margin:.3rem 0 .2rem; }
.tvp:active { cursor:grabbing; }
.tvp .tin { position:absolute; top:0; left:0; transform-origin:0 0; }
.tzc { position:absolute; bottom:10px; right:10px; z-index:5; display:flex;
       flex-direction:column; gap:4px; align-items:center; }
.tzc button { width:34px; height:30px; font-size:16px; font-weight:700; padding:0;
       background:#fffdf6; color:var(--acc); border:1px solid var(--line);
       border-radius:8px; box-shadow:0 2px 6px rgba(0,0,0,.08); }
.tzc button:hover { background:var(--chip); color:var(--acc); }
.tzc button.tzf { font:.62rem/1 monospace; font-weight:600; height:24px; }
.tzc .tzl { font:.62rem/1.5 monospace; color:var(--mut); background:#fffdf6;
       border:1px solid var(--line); border-radius:6px; padding:0 .35rem; }
</style>"""

LEDGER_CONST_OLD = '''const LEDGER_DESC = "The result of splitting the verse into leaves based on the " +
  "cantillation marks: one row per leaf-brick — the words the ta'amim glued together, " +
  "the pause mark that sealed them, their address in the verse's tree, and an " +
  "automatic hint at their role.";'''

TREE_CONST_NEW = '''const TREE_DESC = "The verse as the ta'amim (cantillation marks) built it: the " +
  "strongest pause splits first, each split labeled with the mark that made the cut, " +
  "down to the leaves. Drag to pan; magnify with \\u2318/Ctrl + scroll, " +
  "double-click (shift to shrink), pinch, or the corner controls; " +
  "hover a leaf for its word range and why it froze.";'''

LEDGER_ROWS_OLD = '''  const ledger = vd.leaves.map(l =>
    `<tr><td><b>B${l.b}</b></td><td>${esc(l.w)}</td><td class="code">${esc(l.path)}</td>` +
    `<td class="he">${esc(l.he)}</td><td>${esc(l.tr)}</td><td>${esc(l.en)}</td>` +
    `<td>${esc(l.mark)} · r${l.rank}</td><td>${esc(l.froze)}</td><td>${esc(l.role)}</td></tr>`).join("");

  const morph = vd.morph.map(m =>'''

LEDGER_SECT_OLD = '''  <div class="sect"><h3>Leaf ledger <span class="count">· ${vd.leaves.length} bricks</span></h3>
    <p class="desc">${LEDGER_DESC}</p>
    <table><tr><th>B#</th><th>words</th><th>path</th><th>Hebrew</th><th>Transliteration</th>
      <th>English</th><th>end mark · rank</th><th>froze because</th><th>role (auto)</th></tr>
      ${ledger}</table></div>'''

TREE_SECT_NEW = '''  <div class="sect"><h3>Verse tree <span class="count">· ${vd.leaves.length} leaves</span></h3>
    <p class="desc">${TREE_DESC}</p>
    <div class="tvp">${treeSVG(vd.leaves)}
      <div class="tzc"><button class="tzi" title="zoom in">+</button>
        <span class="tzl">100%</span>
        <button class="tzo" title="zoom out">−</button>
        <button class="tzf" title="fit the whole tree in the window">fit</button></div>
    </div></div>'''

TREE_JS = '''/* ---------------- verse tree (pan + zoom window) ----------------
   The tree is rebuilt from each leaf's path (L·R address): the split
   at any node is the pause mark that sealed the last leaf of its left
   half. Pure computation — the SVG string is generated with the verse. */
const TG = {LW:150, LH:90, SW:64, SH:26, HP:14, VG:34};
const trunc = (s, n) => (s = String(s ?? "")).length > n ? s.slice(0, n - 1) + "…" : s;

function treeBuild(ls, d) {
  if (ls.length === 1) return {leaf: ls[0].l};
  const L = ls.filter(x => x.t[d] === "L"), R = ls.filter(x => x.t[d] === "R");
  if (!L.length || !R.length) return {leaf: ls[0].l};
  const seal = L[L.length - 1].l;
  return {left: treeBuild(L, d + 1), right: treeBuild(R, d + 1),
          mark: seal.mark, rank: seal.rank};
}

function treeMeasure(m) {
  if (m.leaf) { m.w = TG.LW; m.h = TG.LH; return m; }
  treeMeasure(m.left); treeMeasure(m.right);
  m.w = Math.max(TG.SW, m.left.w + TG.HP + m.right.w);
  m.h = TG.SH + TG.VG + Math.max(m.left.h, m.right.h);
  return m;
}

function treeLayout(m, x, y) {
  m.x = x; m.y = y; m.cx = x + m.w / 2;
  if (m.leaf) { m.cx = x + TG.LW / 2; return; }
  const cy = y + TG.SH + TG.VG;
  const sx = x + (m.w - (m.left.w + TG.HP + m.right.w)) / 2;
  treeLayout(m.left, sx, cy);
  treeLayout(m.right, sx + m.left.w + TG.HP, cy);
}

function treeRender(m, lines, nodes, isRoot) {
  if (m.leaf) {
    const l = m.leaf;
    nodes.push(`<g transform="translate(${m.x},${m.y})">` +
      `<title>B${l.b} · words ${esc(l.w)} · froze: ${esc(l.froze)}</title>` +
      `<rect width="${TG.LW}" height="${TG.LH}" rx="8" fill="#fff" stroke="#c9b98a" stroke-width="1.4"/>` +
      `<text text-anchor="middle" x="${TG.LW/2}" y="21" font-family="SBL Hebrew,David,Noto Sans Hebrew,serif" font-size="15" fill="#1f2937">${esc(l.he)}</text>` +
      `<text text-anchor="middle" x="${TG.LW/2}" y="37" font-size="10" fill="#6b7280">${esc(trunc(l.tr, 26))}</text>` +
      `<text text-anchor="middle" x="${TG.LW/2}" y="51" font-size="10" fill="#1f2937">${esc(trunc(l.en, 26))}</text>` +
      `<text text-anchor="middle" x="${TG.LW/2}" y="67" font-size="9.5" font-weight="700" fill="#8a6d1a">${esc(trunc(l.role, 24))}</text>` +
      `<text text-anchor="middle" x="${TG.LW/2}" y="81" font-size="8.5" fill="#6b7280">B${l.b} · ${esc(l.mark)} · r${l.rank}</text></g>`);
    return;
  }
  const label = `${m.mark} r${m.rank}`;
  const nw = Math.max(TG.SW, label.length * 6.5 + 14), nx = m.cx - nw / 2;
  nodes.push(`<g transform="translate(${nx},${m.y})">` +
    `<rect width="${nw}" height="${TG.SH}" rx="6" fill="#f0ecdf" stroke="#d7d3c8" stroke-width="1.3"/>` +
    `<text text-anchor="middle" x="${nw/2}" y="17" font-size="10.5" font-weight="600" fill="#8a6d1a">${esc(label)}</text></g>`);
  const fy = m.y + TG.SH;
  // No hardcoded arm labels: PROCESS/RESULT was true of command-verses
  // only; a generic pair overclaims the derivation (owner ruling
  // 2026-08-21 — per-verse labels from the units may return later).
  ["left", "right"].forEach(k => {
    const ch = m[k];
    lines.push(`<line x1="${m.cx}" y1="${fy}" x2="${ch.cx}" y2="${ch.y}" ` +
      `stroke="#c4bda9" stroke-width="${isRoot ? 2 : 1.4}"/>`);
    treeRender(ch, lines, nodes, false);
  });
}

function treeSVG(leaves) {
  const m = treeMeasure(treeBuild(
    leaves.map(l => ({t: l.path ? l.path.split("·") : [], l})), 0));
  treeLayout(m, 20, 20);
  const w = m.w + 40, h = m.h + 40, lines = [], nodes = [];
  treeRender(m, lines, nodes, true);
  return `<div class="tin" data-w="${w}" data-h="${h}">` +
    `<svg width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" ` +
    `font-family="Charter,Georgia,serif">${lines.join("")}${nodes.join("")}</svg></div>`;
}

function initTVP(vp) {
  const tin = vp.querySelector(".tin"), zl = vp.querySelector(".tzl");
  const sw = +tin.dataset.w, sh = +tin.dataset.h;
  let s = 1, px = 0, py = 0, dr = false, lx = 0, ly = 0, lt = null, ld = null;
  const apply = () => {
    tin.style.transform = `translate(${px}px,${py}px) scale(${s})`;
    zl.textContent = Math.round(s * 100) + "%";
  };
  const fit = () => {
    const vw = vp.clientWidth, vh = vp.clientHeight;
    s = Math.max(0.1, Math.min(vw / sw, vh / sh, 1));
    px = (vw - sw * s) / 2; py = Math.max(4, (vh - sh * s) / 2); apply();
  };
  const zoomAt = (cx, cy, f) => {
    const r = vp.getBoundingClientRect();
    const mx = cx - r.left, my = cy - r.top;
    const bx = (mx - px) / s, by = (my - py) / s;
    s = Math.min(4, Math.max(0.1, s * f));
    px = mx - bx * s; py = my - by * s; apply();
  };
  // A plain wheel scrolls the page; zooming asks for intent —
  // Cmd/Ctrl + wheel (trackpad pinch arrives as exactly that) or double-click.
  vp.addEventListener("wheel", e => {
    if (!e.ctrlKey && !e.metaKey) return;
    e.preventDefault();
    zoomAt(e.clientX, e.clientY, e.deltaY > 0 ? 0.9 : 1.1);
  }, {passive: false});
  vp.addEventListener("dblclick", e => {
    if (e.target.closest(".tzc")) return;
    zoomAt(e.clientX, e.clientY, e.shiftKey ? 1 / 1.6 : 1.6);
  });
  vp.addEventListener("mousedown", e => {
    if (e.target.closest(".tzc")) return;
    dr = true; lx = e.clientX; ly = e.clientY; e.preventDefault();
  });
  window.addEventListener("mousemove", e => {
    if (!dr) return;
    px += e.clientX - lx; py += e.clientY - ly; lx = e.clientX; ly = e.clientY; apply();
  });
  window.addEventListener("mouseup", () => { dr = false; });
  vp.addEventListener("touchstart", e => {
    if (e.touches.length === 1) { lt = {x: e.touches[0].clientX, y: e.touches[0].clientY}; ld = null; }
    else if (e.touches.length === 2) {
      ld = Math.hypot(e.touches[0].clientX - e.touches[1].clientX,
                      e.touches[0].clientY - e.touches[1].clientY); lt = null; }
  }, {passive: true});
  vp.addEventListener("touchmove", e => {
    e.preventDefault();
    if (e.touches.length === 1 && lt) {
      px += e.touches[0].clientX - lt.x; py += e.touches[0].clientY - lt.y;
      lt = {x: e.touches[0].clientX, y: e.touches[0].clientY}; apply();
    } else if (e.touches.length === 2 && ld !== null) {
      const dd = Math.hypot(e.touches[0].clientX - e.touches[1].clientX,
                            e.touches[0].clientY - e.touches[1].clientY);
      s = Math.min(4, Math.max(0.1, s * (dd / ld))); ld = dd; apply();
    }
  }, {passive: false});
  vp.addEventListener("touchend", () => { lt = null; ld = null; });
  vp.querySelector(".tzi").onclick = () => { s = Math.min(4, s * 1.25); apply(); };
  vp.querySelector(".tzo").onclick = () => { s = Math.max(0.1, s * 0.8); apply(); };
  vp.querySelector(".tzf").onclick = fit;
  fit();
}

'''


def masthead(prefix, active):
    def link(key, href, label):
        cls = ' class="on"' if key == active else ""
        return '<a%s href="%s">%s</a>' % (cls, href, label)
    return (MAST_CSS + '<div class="mast"><span class="brand">TorahSim'
            '</span><nav class="mid">'
            + link("disclosure", prefix, "Epic Disclosure")
            + link("scroll", prefix + "scroll/", "The Scroll")
            + link("run", prefix + "run/", "The Run")
            + link("contact", prefix + "contact/", "Contact")
            + '</nav><nav class="ext">'
            '<a href="https://github.com/Josephtorah/TorahSim" '
            'target="_blank" rel="noopener">%s github</a>'
            '<a href="https://discord.gg/UXZUguY9Pb" '
            'target="_blank" rel="noopener">%s discord</a></nav></div>'
            % (GITHUB_SVG, DISCORD_SVG))


VSTAT_CSS = """<style>
.badge.vstat{background:none;border:none;color:#57503f;cursor:help}
</style>"""

VSTAT_OLD_ORAL = '''  const oral = vd.oral
    ? `<span class="badge oral" title="Oral-tradition sources anchored to this verse (tier 1 of Sefaria's link index): ${vd.oral[0]} enumerated, ${vd.oral[1]} read with a verdict in the triage ledger, ${vd.oral[2]} judged material (bearing on the frozen derivation). Enumerated / fetched / read are kept as separate honest counters; the ledger in logic/oral_triage/ is the canonical record.">\U0001F4DC oral ${vd.oral[1]}/${vd.oral[0]} read${vd.oral[2] ? ` · ${vd.oral[2]} material` : ""}</span>`
    : "";'''

VSTAT_CHIP_JS = '''  const vs = vd.vstat || {o: 0, d: 0, p: false, g: "v"};
  const otxt = vs.o === 3 ? (vs.g === "c" ? "chapter read through" : "read through")
    : vs.o === 2 ? `in reading ${vd.oral[1]}/${vd.oral[0]}` : "unopened";
  const mat = vs.o >= 2 && vd.oral && vd.oral[2] ? ` · ${vd.oral[2]} material` : "";
  const dtxt = vs.d === 2 ? "full rule" : vs.d === 1 ? "first pass" : "underived";
  const vtitle = vs.g === "c"
    ? "Verse status. Oral track: the whole chapter was read through under the law-era rule — every readable oral source on the chapter read and logged in the reading ledger (scans/ledgers/). Its rows anchor to the chapter's law, so no per-verse fraction is shown. Derivation track: " + dtxt + (vs.p ? ". Proven: the chapter is compiled to machines and its recorded cases run green." : ".")
    : "Verse status. Oral track: " + (vd.oral ? vd.oral[0] + " sources enumerated (tier 1 of the link index), " + vd.oral[1] + " read with a verdict in the triage ledger (logic/oral_triage/), " + vd.oral[2] + " judged material (bearing on the frozen derivation)" : "no oral sources enumerated yet") + ". Derivation track: " + dtxt + (vs.p ? ". Proven: compiled to machines, recorded cases green." : ".") + " Labels are computed from the records on every build — never hand-set.";
  const vchip = `<span class="badge vstat" title="${vtitle}">ⓘ ${otxt}${mat} · ${dtxt}${vs.p ? " · proven" : ""}</span>`;'''


def build_scroll_site():
    sdir = os.path.join(SITE, "scroll")
    path = os.path.join(sdir, "index.html")
    with open(path, encoding="utf-8") as f:
        t = f.read()
    assert t.count("<body>") == 1
    # The reader carries the redesign natively since the owner's build
    # order (2026-08-25) — unit bands, collapsed verse cards, the
    # verse-tree window, the vstat chip, and the rail's coverage link
    # all live in scroll/index.html itself. The dress now adds only the
    # site chrome: the masthead and the left-rail CSS. The retired
    # patch constants above stand as the dress's own history.
    t = t.replace("<body>",
                  "<body>" + masthead("../", "scroll") + SCROLL_RAIL_CSS, 1)
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
             + masthead("../../", "scroll") + UNIT_BACK + u[m.end():])
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


def build_coverage_page():
    """The Torah as a grid — one cell per verse, color = derivation
    level, fill = oral level, ring = proven-by-cases. Built from the
    bundles' vstat field (spec v2), so the page can never say more than
    the records do; regenerated on every export."""
    sdir = os.path.join(SITE, "scroll", "data")
    books = json.load(open(os.path.join(sdir, "manifest.json"),
                           encoding="utf-8"))["books"]
    ONAME = {0: "unopened", 2: "in reading", 3: "read through"}
    DNAME = {0: "underived", 1: "first pass", 2: "full rule"}
    tallies, rows_html = {}, []
    for bk in books:
        rows_html.append("<h2>%s</h2>" % bk["name"])
        for ch in range(1, len(bk["chapters"]) + 1):
            with open(os.path.join(sdir, "%s_%d.json" % (bk["id"], ch)),
                      encoding="utf-8") as f:
                verses = json.load(f)["verses"]
            cells = []
            for v in verses:
                s = v.get("vstat") or {"o": 0, "d": 0, "p": False, "g": "v"}
                key = (s["o"], s["d"], s["p"], s["g"])
                tallies[key] = tallies.get(key, 0) + 1
                oc = v.get("oral")
                ot = ("chapter read through" if s["o"] == 3 and s["g"] == "c"
                      else ONAME[s["o"]])
                if s["o"] == 2 and oc:
                    ot += " %d/%d" % (oc[1], oc[0])
                lab = "%s %d:%d — %s · %s%s" % (
                    bk["id"], ch, v["v"], ot, DNAME[s["d"]],
                    " · proven" if s["p"] else "")
                cells.append('<span class="c d%d o%d%s" title="%s"></span>'
                             % (s["d"], s["o"], " p" if s["p"] else "",
                                _html.escape(lab)))
            rows_html.append('<div class="row"><span class="rl">%s %d'
                             '</span>%s</div>'
                             % (bk["id"], ch, "".join(cells)))
    total = sum(tallies.values())
    sumrows = "".join(
        "<tr><td><span class='c d%d o%d%s'></span></td>"
        "<td>%s%s · %s%s</td><td>%d</td></tr>"
        % (d, o, " p" if p else "",
           ("chapter read through" if o == 3 and g == "c" else ONAME[o]),
           "", DNAME[d], " · proven" if p else "", n)
        for (o, d, p, g), n in sorted(tallies.items()))
    page = COVERAGE_PAGE % {
        "mast": masthead("../../", "scroll"), "total": total,
        "summary": sumrows, "rows": "".join(rows_html)}
    cdir = os.path.join(SITE, "scroll", "coverage")
    os.makedirs(cdir, exist_ok=True)
    with open(os.path.join(cdir, "index.html"), "w",
              encoding="utf-8") as f:
        f.write(page)
    print("  coverage grid           %d verses, %d status classes"
          % (total, len(tallies)))


COVERAGE_PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TorahSim — derivation coverage</title>
<style>
body{margin:54px 0 0;background:#faf7f0;color:#151009;
font:16px/1.6 Georgia,serif}
main{max-width:1180px;margin:0 auto;padding:24px 28px 90px}
h1{font-size:30px;color:#6e5417;font-weight:normal;margin:18px 0 4px}
h2{font-size:20px;color:#6e5417;font-weight:normal;margin:30px 0 6px;
border-bottom:1px solid #e4dcc8;padding-bottom:4px}
p.lead{color:#57503f;max-width:52em}
table{border-collapse:collapse;margin:14px 0;font-size:14px}
td{border:1px solid #e4dcc8;padding:3px 12px}
.row{line-height:0;margin:2px 0;white-space:nowrap;overflow-x:auto}
.rl{display:inline-block;width:64px;font:11px Georgia,serif;
color:#57503f;line-height:16px;vertical-align:middle}
.c{display:inline-block;width:9px;height:15px;margin:0 1px;
border-radius:2px;background:#efe9d8;vertical-align:middle}
.c.d1.o0{background:linear-gradient(to top,#b08a3e 22%%,#efe9d8 22%%)}
.c.d1.o2{background:linear-gradient(to top,#b08a3e 55%%,#efe9d8 55%%)}
.c.d1.o3{background:#b08a3e}
.c.d2.o0{background:linear-gradient(to top,#6e5417 22%%,#efe9d8 22%%)}
.c.d2.o2{background:linear-gradient(to top,#6e5417 55%%,#efe9d8 55%%)}
.c.d2.o3{background:#6e5417}
.c.d0.o2{background:linear-gradient(to top,#8a8171 55%%,#efe9d8 55%%)}
.c.d0.o3{background:#8a8171}
.c.p{outline:2px solid #0a7a2f;outline-offset:-2px}
.note{color:#57503f;font-size:13.5px;border-top:1px solid #e4dcc8;
margin-top:26px;padding-top:10px}
</style></head><body>
%(mast)s
<main>
<h1>Derivation coverage</h1>
<p class="lead">The whole Torah, one cell per verse — %(total)d verses.
The cell's color is the derivation track (pale: underived; gold: first
pass; deep gold: full rule); its fill is the oral track (empty: unopened;
half: in reading; full: read through); a green ring marks a chapter
proven by its recorded cases. Hover any cell for its verse and status.
Every label is computed from the records at build time — never hand-set.
</p>
<table><tr><td colspan="3"><b>Today's map</b></td></tr>%(summary)s</table>
%(rows)s
<div class="note">Labels: the oral track counts every source the link
index anchors to a verse (enumerated), how many have a logged verdict in
the triage ledger (read), and how many were judged material. Law-era
chapters carry chapter-grain attribution — their reading ledgers anchor
rows to the chapter's law, so no per-verse fraction is shown.
Experimental model — not binding religious law.</div>
</main></body></html>
"""


def build_contact():
    """The contact page (owner order 2026-08-28): one address, no form
    — a static site collects nothing."""
    os.makedirs(os.path.join(SITE, "contact"), exist_ok=True)
    page = ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, '
            'initial-scale=1"><title>TorahSim — contact</title>'
            "<style>body{margin:54px 0 0;background:#fdfbf4;color:#2a2a24;"
            "font:17px/1.6 Georgia,serif}main{max-width:640px;margin:0 auto;"
            "padding:3rem 1.5rem}h1{font-size:1.5rem;color:#6e5417}"
            "a.mail{display:inline-block;margin:.6rem 0;padding:.55rem 1.1rem;"
            "border:1px solid #b08a3e;border-radius:8px;color:#6e5417;"
            "background:#fffdf6;text-decoration:none;font-size:1.05rem}"
            "a.mail:hover{background:#f3eee1}p{color:#57503f}</style>"
            "</head><body>" + masthead("../", "contact") + "<main>"
            "<h1>Contact</h1>"
            "<p>Questions, corrections, or a source the reading missed — "
            "all welcome. Misses are part of the record here.</p>"
            '<a class="mail" href="mailto:josephtorah@gmail.com">'
            "josephtorah@gmail.com</a>"
            "<p>The project is also on "
            '<a href="https://github.com/Josephtorah/TorahSim" '
            'style="color:#6e5417">github</a> and '
            '<a href="https://discord.gg/UXZUguY9Pb" '
            'style="color:#6e5417">discord</a>.</p>'
            "</main></body></html>\n")
    with open(os.path.join(SITE, "contact", "index.html"), "w",
              encoding="utf-8") as f:
        f.write(page)
    print("  contact                  one page, one address")


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
    build_contact()

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
    build_coverage_page()
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
