#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
"""export_site.py — the Tanakh-run app, frozen for static hosting.

The live app (app/app.py) is one self-contained page and six JSON
endpoints. This program renders every endpoint to a file under site/
and patches the page's fetch paths, so the identical interface serves
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


def dump(rel, obj):
    path = os.path.join(SITE, rel)
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
              '<a href="scroll/" style="color:var(--gold);'
              'text-decoration:none">the scroll</a></small>')
    p = patch(p, "TorahSim &middot; MIT license",
              "TorahSim &middot; "
              '<a href="https://github.com/Josephtorah/TorahSim" '
              'style="color:inherit">source</a> &middot; MIT license')
    with open(os.path.join(SITE, "index.html"), "w", encoding="utf-8") as f:
        f.write(p)


def main():
    if os.path.isdir(SITE):
        shutil.rmtree(SITE)
    os.makedirs(SITE)

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
