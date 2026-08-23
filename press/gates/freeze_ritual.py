#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""freeze_ritual.py <uid>

The entire post-PASS freeze ritual in one idempotent call:

  1. verify_text.py (refuses to freeze a broken text layer)
  2. flip status draft->frozen, strip dry_run_only (skipped if frozen)
  3. run the frozen unit + its scenarios
  4. FULL corpus regression, parallelized across CPUs
  5. render_unit_py + self-proof run
  6. render_unit_html to the UNDATED page path (the one the index links)
  7. index_units.py + render_coverage_index.py
  8. corpus proof: run units/run_all.py and assert every rendering's
     baked battery green (this repository's whole-corpus equivalent)
  9. print the checklist; nonzero exit on any failure

Still manual afterwards (judgment, not mechanics): memory/state
update, owner's commit word.
"""
import concurrent.futures as cf
import datetime
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TOOLS = Path(__file__).resolve().parent
D = REPO / "press"
PY = sys.executable

steps_done = []


def step(label, ok, detail=""):
    steps_done.append((label, ok, detail))
    print("%s  %s%s" % ("PASS" if ok else "FAIL", label,
                        (" — " + detail) if detail else ""))
    if not ok:
        summary(); sys.exit(1)


def summary():
    print("\n=== RITUAL SUMMARY ===")
    for label, ok, detail in steps_done:
        print("  %s %s" % ("+" if ok else "x", label))


def run(args, cwd=REPO):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def scenarios_green(uid):
    rc, out = run([PY, "press/run_unit.py", uid, "--scenarios"])
    tail = out.split("\n")[-1] if out else ""
    # a clause verdict line starts with FAIL/UNCHECKED after indent;
    # "TESTS += FAIL(..)" inside a PASS line is a verdict-datum, not a failure
    bad = [ln for ln in out.split("\n")
           if ln.strip().startswith(("FAIL", "UNCHECKED"))]
    return rc == 0 and tail == "ALL SCENARIOS GREEN" and not bad, tail


def main():
    uid = sys.argv[1]
    yaml_path = REPO / "logic/units" / (uid + ".yaml")
    if not yaml_path.exists():
        sys.exit("no such unit: %s" % yaml_path)

    # 0. DECLARED-READING coverage gate (rewritten 2026-08-23 on owner
    # word "if you need to rewrite anything to make the new derivation
    # rules work then do it"). RE-era law: reading scope is a per-item
    # owner choice with the CORE SHELF as standing default (rulings
    # 2026-08-21 + 2026-08-23); the 2026-08-10 anti-drift lesson stands
    # unchanged — whatever scope was DECLARED must be COMPLETELY read
    # and ledgered. Evidence forms, first match wins:
    #   (a) a completed triage ledger (creation-week era):
    #       logic/oral_triage/<uid>_*.md declaring "read: N of N —
    #       COMPLETE" in its counters block;
    #   (b) law-era chain ledgers via oral_coverage.py (full-inversion
    #       declarations, unit_span_planned metadata).
    # A unit with NO declared-reading record fails the gate — that is
    # the honest answer, not a bypass.
    import re as _re
    ytxt = yaml_path.read_text()
    triage_hits = sorted((REPO / "logic" / "oral_triage").glob(uid + "_*.md"))
    tr_note = ""
    for tp in triage_hits:
        mt = _re.search(r"\*\*read:\s*(\d+)\s*of\s*(\d+)\s*—[^\n]*COMPLETE",
                        tp.read_text(encoding="utf-8"))
        if mt and mt.group(1) == mt.group(2):
            tr_note = ("declared scope complete: %s of %s read (%s)"
                       % (mt.group(1), mt.group(2), tp.name))
            break
    mb = _re.search(r"book_en:\s*(\w+)", ytxt)
    ms = _re.search(r'unit_span_planned:\s*"?(\d+):\d+-(?:(\d+):)?\d+', ytxt)
    abbrev = {"Genesis": "Gen", "Exodus": "Exod", "Leviticus": "Lev",
              "Numbers": "Num", "Deuteronomy": "Deut"}
    if tr_note:
        step("declared-reading gate", True, tr_note)
    elif mb and ms:
        book = abbrev[mb.group(1)]
        c1 = ms.group(1)
        c2 = ms.group(2) or c1
        rc, out = run([PY, str(TOOLS / "oral_coverage.py"), book, c1,
                       "--to", c2])
        gl = [l.strip() for l in out.split("\n")
              if "GATE:" in l or "read-and" in l]
        step("declared-reading gate", rc == 0, "; ".join(gl) or out[-80:])
    else:
        step("declared-reading gate", False,
             "no declared-reading record (no completed triage ledger, "
             "no span metadata)")

    # 1. text layer
    rc, out = run([PY, str(TOOLS / "verify_text.py"), uid])
    step("text layer", rc == 0, out.split("\n")[-1])

    # 2. flip
    s = yaml_path.read_text()
    if "  status: draft\n" in s:
        s = s.replace("  status: draft\n", "  status: frozen\n")
        s = s.replace("  dry_run_only: true\n", "")
        yaml_path.write_text(s)
        step("freeze flip", True, "draft -> frozen")
    else:
        step("freeze flip", "  status: frozen\n" in s, "already frozen")

    # 3. frozen run + scenarios
    rc, out = run([PY, "press/run_unit.py", uid])
    step("frozen run", rc == 0, out.split("\n")[-1][:100])
    ok, tail = scenarios_green(uid)
    step("frozen scenarios", ok, tail)

    # 4. parallel regression
    uids = sorted(p.stem for p in (REPO / "logic/units").glob("*.yaml")
                  if "status: frozen" in p.read_text())
    fails = []
    with cf.ThreadPoolExecutor() as ex:
        for u, (ok, tail) in zip(uids, ex.map(scenarios_green, uids)):
            if not ok:
                fails.append("%s -> %s" % (u, tail))
    step("regression %d/%d" % (len(uids) - len(fails), len(uids)),
         not fails, "; ".join(fails[:3]))

    # 5. py render + self-proof
    rc, out = run([PY, str(D / "render_unit_py.py"), uid])
    step("render py", rc == 0, out.split("\n")[-1][:100])
    py_path = REPO / "units" / (uid + ".py")
    rc, out = run([PY, str(py_path)])
    step("py self-proof", rc == 0 and "ALL ASSERTIONS GREEN" in out,
         out.split("\n")[-1][:80])

    # 6. undated HTML
    html_path = REPO / "scroll/units" / ("UNIT_%s.html" % uid)
    rc, out = run([PY, str(D / "render_unit_html.py"), uid, str(html_path)])
    step("render html (undated)", rc == 0 and html_path.exists(),
         html_path.name)

    # 7. indexes
    rc, out = run([PY, "press/index_units.py"])
    step("index_units", rc == 0, out.split("\n")[-1][:80])
    rc, out = run([PY, str(D / "render_coverage_index.py")])
    step("coverage index", rc == 0, out.split("\n")[-1][:80])

    # 8. corpus proof — this repository's whole-corpus check is
    # units/run_all.py: every rendering re-run, every baked battery green
    rc, out = run([PY, "units/run_all.py"])
    import re as _re8
    mg = _re8.search(r"(\d+) GREEN, (\d+) RED", out)
    step("corpus proof (run_all)",
         rc == 0 and mg and int(mg.group(2)) == 0
         and int(mg.group(1)) == len(uids),
         mg.group(0) if mg else out.split("\n")[-1][:80])

    summary()
    print("\nRITUAL COMPLETE for %s (%d frozen units)." % (uid, len(uids)))
    print("Manual next: memory/state update, owner commit word.")


if __name__ == "__main__":
    main()
