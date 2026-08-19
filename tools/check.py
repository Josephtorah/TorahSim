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
# declared exception) — the scan records, and the derivation review pages
RECORDS = {("scans", "ledgers"), ("scans", "manifests"),
           ("scans", "notes"), ("scroll", "units")}
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
        preserved = (os.path.basename(os.path.dirname(base)),
                     os.path.basename(base)) in RECORDS
        for f in sorted(files):
            if f.endswith(LINT_EXT):
                (records if preserved else gated).append(
                    os.path.join(base, f))
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

    bad = [n for n, ok, _ in results if not ok]
    print("check: %d gates — %s" % (len(results),
          "ALL GREEN" if not bad else "RED: " + ", ".join(bad)))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
