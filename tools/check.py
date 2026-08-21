#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
"""check.py — the one green button.

Every mechanical gate in the repository, run in pipeline order, one exit
code. The method laws (docs/METHOD_LAWS.md) are enforced by gates; this
program is the gates, assembled:

  1. the gloss lint (method law 8) over every shipped .py/.md/.html file
     — the preserved records (the scans/ ledgers, manifests, and notes,
     and the scroll/units/ derivation review pages) are the declared
     exception: their flags are REPORTED, never gated, as the law states;
  2. the derivation units (units/run_all.py) — each unit re-proves the
     state its derivation froze;
  3. the assembled chapter machine (machines/exo21/chapter.py) — the
     assert battery and the 60-edge dependency proof;
  4. the Tanakh run replayed headlessly — all 64 scene stamps compared
     against the frozen baseline (app/scene_stamps_baseline.json).
     Any change that flips a stamp must answer for it (roadmap
     component 9); after it has answered, re-freeze deliberately with
     --rebaseline;
  5. the simulation sketch (sim/house_of_david.py) — its two findings
     ride as assertions.

Usage:  python3 tools/check.py [--rebaseline]
Exit 0 only when every gate is green. Stock Python 3; nothing to install.
"""
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BASELINE = os.path.join(ROOT, "app", "scene_stamps_baseline.json")

SKIP_DIRS = {".git", ".github", "__pycache__", "shelf", "BriansTemp",
             "site"}   # site/ is generated; its sources are linted here
# preserved records: reported by the lint, never gated (method law 8's
# declared exception) — the scan records, the derivation review pages,
# and the workshop records that crossed with the press (method docs,
# triage ledgers, parser rule notes, the append-only fetch log): shipped
# as received, under the one documented redaction.
RECORD_PREFIXES = (os.path.join("scans", "ledgers"),
                   os.path.join("scans", "manifests"),
                   os.path.join("scans", "notes"),
                   os.path.join("scroll", "units"),
                   os.path.join("logic", "docs"),
                   os.path.join("logic", "oral_triage"),
                   os.path.join("logic", "oral_audit"),
                   os.path.join("logic", "taamim_rules"))
RECORD_FILES = {os.path.join("logic", "FETCHLOG.md")}
LINT_EXT = (".py", ".md", ".html")

results = []   # (gate name, ok, one-line report)


def report(name, ok, line):
    results.append((name, ok, line))
    print("%-10s %s  %s" % (name, "GREEN" if ok else "RED", line))


def lint_files():
    """Every shipped lintable file, minus the preserved records."""
    gated, records = [], []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        rel_base = os.path.relpath(base, ROOT)
        preserved = any(rel_base == p or rel_base.startswith(p + os.sep)
                        for p in RECORD_PREFIXES)
        for f in sorted(files):
            if f.endswith(LINT_EXT):
                rel = os.path.normpath(os.path.join(rel_base, f))
                (records if preserved or rel in RECORD_FILES
                 else gated).append(os.path.join(base, f))
    return gated, records


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)


def main():
    rebaseline = "--rebaseline" in sys.argv[1:]

    # -- gate 1: the gloss lint (method law 8) ---------------------------
    gated, records = lint_files()
    r = run([sys.executable, os.path.join(HERE, "gloss_lint.py")] + gated)
    if r.returncode:
        print(r.stdout, end="")
    report("gloss", r.returncode == 0,
           "%d shipped files, %s" % (len(gated), r.stdout.strip()
                                     .splitlines()[-1]))
    if records:   # the declared exception: reported, never gated
        a = run([sys.executable, os.path.join(HERE, "gloss_lint.py")]
                + records)
        print("           note   preserved records (scans/, scroll/units/): "
              "%s (declared exception, not gated)"
              % a.stdout.strip().splitlines()[-1])

    # -- gate 2: the derivation units ------------------------------------
    r = run([sys.executable, os.path.join(ROOT, "units", "run_all.py")])
    if r.returncode:
        print(r.stdout, end="")
    report("units", r.returncode == 0, r.stdout.strip().splitlines()[-1])

    # -- gate 3: the chapter machine + dependency proof ------------------
    r = run([sys.executable,
             os.path.join(ROOT, "machines", "exo21", "chapter.py")])
    if r.returncode:
        print(r.stdout, r.stderr, end="")
    report("chapter", r.returncode == 0,
           "assert battery + dependency proof"
           if r.returncode == 0 else "FAILED — output above")

    # -- gate 4: the Tanakh run vs. the frozen stamps --------------------
    spec = importlib.util.spec_from_file_location(
        "app", os.path.join(ROOT, "app", "app.py"))
    app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app)
    stamps = {sid: app.HANDLERS[sid](app.SCENES[sid])["stamp"]
              for sid in sorted(app.SCENES)}
    counts = {}
    for st in stamps.values():
        counts[st] = counts.get(st, 0) + 1
    board = " / ".join("%d %s" % (counts[k], k) for k in
                       ("CONFIRM", "DIVERGE", "FORWARD",
                        "NO-VERDICT-IN-TEXT") if k in counts)
    if rebaseline:
        with open(BASELINE, "w", encoding="utf-8") as f:
            json.dump({"meta": {
                "note": "The frozen stamps of the 64-scene Tanakh run — "
                        "the regression baseline. A change that flips a "
                        "stamp must answer for it; after it has, "
                        "re-freeze with: python3 tools/check.py "
                        "--rebaseline"},
                "stamps": stamps}, f, ensure_ascii=False, indent=1)
            f.write("\n")
        report("scenes", True, "baseline RE-FROZEN: %s" % board)
    else:
        with open(BASELINE, encoding="utf-8") as f:
            frozen = json.load(f)["stamps"]
        flips = sorted(set(list(frozen) + list(stamps)))
        flips = [(sid, frozen.get(sid), stamps.get(sid))
                 for sid in flips if frozen.get(sid) != stamps.get(sid)]
        for sid, was, now in flips:
            print("  FLIP  %-28s %s -> %s" % (sid, was, now))
        report("scenes", not flips,
               "%d scenes vs. baseline: %s" % (len(stamps), board)
               if not flips else "%d stamp(s) flipped — answer for them "
               "or --rebaseline" % len(flips))

    # -- gate 5: the simulation sketch -----------------------------------
    r = run([sys.executable, os.path.join(ROOT, "sim", "house_of_david.py")])
    if r.returncode:
        print(r.stdout, r.stderr, end="")
    report("sim", r.returncode == 0,
           "house of David run, findings hold"
           if r.returncode == 0 else "FAILED — output above")

    # -- gate 6: the receipts — the front page's recorded figures --------
    # The recital says the law chapter's reading was logged, 4,903 rows,
    # against a census. Assert the shipped evidence still says so: the
    # reading ledger's row count and the three census queues' entry
    # counts must equal their documented figures.
    try:
        with open(os.path.join(ROOT, "scans", "ledgers",
                               "Exod_21.jsonl"), encoding="utf-8") as f:
            rows = sum(1 for line in f if line.strip())
        import json as _json
        qn = []
        for n in (1, 2, 3):
            with open(os.path.join(ROOT, "scans", "queues",
                                   "law0%d_queue.json" % n),
                      encoding="utf-8") as f:
                qn.append(len(_json.load(f)))
        ok = rows == 4903 and qn == [3286, 2450, 1702]
        report("receipts", ok,
               "reading ledger 4,903 rows · census queues 3,286/2,450/"
               "1,702 — as recorded" if ok else
               "MISMATCH: ledger %d rows, queues %s" % (rows, qn))
    except OSError as e:
        report("receipts", False, "missing evidence file: %s" % e)

    # -- gate 7: the labels — vstat vs. the records ----------------------
    # The verse-status chips and the coverage grid render the bundles'
    # vstat field; this gate re-derives every claim from the committed
    # records and refuses drift: no read-through without the counters, no
    # chapter grain without its reading ledger, no derivation level
    # outside a frozen span, no full-rule stamp the DB cannot show, no
    # proven flag without a compiled chapter and a green scene baseline.
    import glob as _glob
    import json as _json2
    import re as _re
    scenes_green = any(n == "scenes" and ok for n, ok, _ in results)
    spans = set()
    _ABBR = {"Genesis": "Gen", "Exodus": "Exod", "Leviticus": "Lev",
             "Numbers": "Num", "Deuteronomy": "Deut"}
    shape = {}
    for bpath in sorted(_glob.glob(os.path.join(ROOT, "scroll", "data",
                                                "*_*.json"))):
        with open(bpath, encoding="utf-8") as f:
            _d = _json2.load(f)
        shape[(_d["book"], _d["chapter"])] = len(_d["verses"])
    for u in _json2.load(open(os.path.join(ROOT, "data",
                                           "units_index.json"),
                              encoding="utf-8"))["units"]:
        bid = _ABBR[u["book"]]
        m = _re.match(r"^(\d+):(\d+)\s*[-–]\s*(?:(\d+):)?(\d+)$",
                      u["refs"].strip())
        c1, v1 = int(m.group(1)), int(m.group(2))
        c2 = int(m.group(3)) if m.group(3) else c1
        v2 = int(m.group(4))
        for c in range(c1, c2 + 1):
            hi = v2 if c == c2 else shape[(bid, c)]
            for v in range((v1 if c == c1 else 1), hi + 1):
                spans.add((bid, c, v))
    compiled = set()
    _A3 = {"gen": "Gen", "exo": "Exod", "lev": "Lev", "num": "Num",
           "deu": "Deut"}
    for dname in os.listdir(os.path.join(ROOT, "machines")):
        m = _re.match(r"^([a-z]{3})(\d+)$", dname)
        if m and m.group(1) in _A3:
            compiled.add((_A3[m.group(1)], int(m.group(2))))
    bad, n_checked = [], 0
    for bpath in sorted(_glob.glob(os.path.join(ROOT, "scroll", "data",
                                                "*_*.json"))):
        with open(bpath, encoding="utf-8") as f:
            _d = _json2.load(f)
        b, ch = _d["book"], _d["chapter"]
        has_ledger = os.path.exists(os.path.join(
            ROOT, "scans", "ledgers", "%s_%d.jsonl" % (b, ch)))
        for v in _d["verses"]:
            s = v.get("vstat")
            if not s:
                bad.append("%s %d:%d no vstat" % (b, ch, v["v"]))
                continue
            n_checked += 1
            oc = v.get("oral")
            key = (b, ch, v["v"])
            ok = True
            if s["g"] == "c":
                ok = has_ledger and s["o"] == 3
            elif s["o"] == 3:
                ok = bool(oc) and oc[0] > 0 and oc[1] == oc[0]
            elif s["o"] == 2:
                ok = bool(oc) and oc[0] > 0 and oc[1] < oc[0]
            else:
                ok = not oc or oc[0] == 0
            if s["d"] >= 1 and key not in spans:
                ok = False
            if s["d"] == 0 and key in spans:
                ok = False
            if s["d"] == 2:
                ok = False   # no full-rule stamp exists yet; the first
                             # one must extend this gate to verify it
            if s["p"] and not ((b, ch) in compiled and scenes_green):
                ok = False
            if not ok:
                bad.append("%s %d:%d %r oral=%r" % (b, ch, v["v"], s, oc))
    report("labels", not bad,
           "%d verse labels re-derived from the records: consistent"
           % n_checked if not bad else
           "DRIFT in %d labels, e.g. %s" % (len(bad), bad[0]))

    # -- the changelog gate — rewritable code must say what changed ------
    # Re-era constitution (METHOD_LAWS): unit logic is freely rewritable,
    # but any diff to a canonical unit YAML must arrive with a new
    # changelog line (and its bumped rev). Compared against git HEAD; a
    # clean tree or a fresh clone passes trivially.
    r = run(["git", "diff", "--name-only", "HEAD", "--",
             os.path.join("logic", "units")])
    if r.returncode == 0:
        import re as _re2

        def _clog(text):
            m = _re2.search(r"^  changelog:\n((?:    - .*\n)+)",
                            text, _re2.M)
            return len(m.group(1).splitlines()) if m else 0

        changed = [l.strip() for l in r.stdout.splitlines() if l.strip()]
        bad = []
        for rel in changed:
            path = os.path.join(ROOT, rel)
            if not os.path.exists(path):
                bad.append(os.path.basename(rel) + " (deleted)")
                continue
            now = open(path, encoding="utf-8").read()
            h = run(["git", "show", "HEAD:" + rel])
            before = h.stdout if h.returncode == 0 else ""
            if _clog(now) <= _clog(before):
                bad.append(os.path.basename(rel))
        report("changelog", not bad,
               ("%d unit YAML(s) edited, each carries its new changelog "
                "line" % len(changed)) if changed and not bad else
               ("no unit edits pending" if not bad else
                "EDIT WITHOUT CHANGELOG: " + ", ".join(bad)))
    else:
        print("           note   changelog gate skipped — git unavailable")

    # -- the press — the shipped pool must be reprintable ----------------
    # Regenerate all 97 unit renderings from the canonical YAML (logic/
    # units/) through press/render_unit_py.py into a temp dir and diff
    # them against units/. Self-sufficiency is not a claim; it re-proves
    # here on every run. Needs the derivation DB (uncommitted, like
    # shelf/) — absent, the gate reports itself skipped rather than red.
    db = os.path.join(ROOT, "data", "derivation.sqlite")
    if os.path.exists(db):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            env = dict(os.environ, TS_OUT=td)
            r = subprocess.run(
                [sys.executable, os.path.join(ROOT, "press",
                                              "render_unit_py.py")],
                capture_output=True, text=True, cwd=ROOT, env=env)
            drift = []
            if r.returncode == 0:
                for f in sorted(os.listdir(td)):
                    a = open(os.path.join(td, f), encoding="utf-8").read()
                    b_path = os.path.join(ROOT, "units", f)
                    b = (open(b_path, encoding="utf-8").read()
                         if os.path.exists(b_path) else None)
                    if a != b:
                        drift.append(f)
            report("press", r.returncode == 0 and not drift,
                   "97 units reprinted from canonical YAML, "
                   "diff vs units/: clean" if r.returncode == 0
                   and not drift else
                   ("REPRINT FAILED — run press/render_unit_py.py"
                    if r.returncode else "DRIFT: " + ", ".join(drift[:5])))
    else:
        print("           note   press gate skipped — data/derivation."
              "sqlite absent (rebuild per docs/SOURCES.md)")

    bad = [n for n, ok, _ in results if not ok]
    print("check: %d gates — %s" % (len(results),
          "ALL GREEN" if not bad else "RED: " + ", ".join(bad)))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
