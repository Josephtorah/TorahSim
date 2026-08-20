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
  8. insert the py unit into ALL_UNITS.py before the lev_13 banner,
     recompute the header count from disk (skipped if already present),
     then run ALL_UNITS.py and assert the green count == frozen count
  9. print the checklist; nonzero exit on any failure

Still manual afterwards (judgment, not mechanics): watchlist file in
logic/middot_scan/, state-doc update, owner's commit word.
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

    # 0. FULL ORAL TORAH coverage gate (owner law 2026-08-10): every
    # chain-readable listing on the span read-and-ledgered, zero
    # unruled works. Exit 1 here = no freeze, same standing as the
    # other gates.
    import re as _re
    ytxt = yaml_path.read_text()
    mb = _re.search(r"book_en:\s*(\w+)", ytxt)
    ms = _re.search(r'unit_span_planned:\s*"?(\d+):\d+-(?:(\d+):)?\d+', ytxt)
    abbrev = {"Genesis": "Gen", "Exodus": "Exod", "Leviticus": "Lev",
              "Numbers": "Num", "Deuteronomy": "Deut"}
    if mb and ms:
        book = abbrev[mb.group(1)]
        c1 = ms.group(1)
        c2 = ms.group(2) or c1
        rc, out = run([PY, str(TOOLS / "oral_coverage.py"), book, c1,
                       "--to", c2])
        gl = [l.strip() for l in out.split("\n")
              if "GATE:" in l or "read-and" in l]
        step("oral coverage gate", rc == 0, "; ".join(gl) or out[-80:])
    else:
        step("oral coverage gate", False, "no span metadata — cannot gate")

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
    py_path = REPO / "logic/py_units" / (uid + ".py")
    rc, out = run([PY, str(py_path)])
    step("py self-proof", rc == 0 and "ALL ASSERTIONS GREEN" in out,
         out.split("\n")[-1][:80])

    # 6. undated HTML
    html_path = D / ("UNIT_%s.html" % uid)
    rc, out = run([PY, str(D / "render_unit_html.py"), uid, str(html_path)])
    step("render html (undated)", rc == 0 and html_path.exists(),
         html_path.name)

    # 7. indexes
    rc, out = run([PY, "index_units.py"])
    step("index_units", rc == 0, out.split("\n")[-1][:80])
    rc, out = run([PY, str(D / "render_coverage_index.py")])
    step("coverage index", rc == 0, out.split("\n")[-1][:80])

    # 8. ALL_UNITS insert + corpus proof
    allp = REPO / "logic/py_units/ALL_UNITS.py"
    s = allp.read_text()
    banner = "# UNIT: %s" % uid
    if banner in s:
        step("ALL_UNITS insert", True, "already present")
    else:
        unit = py_path.read_text()
        m = re.search(r"^from machine import Machine\n", unit, re.M)
        body = ("#" * 79 + "\n%s\n" % banner + "#" * 79 + "\n"
                + unit[m.end():])
        i = s.index("# UNIT: lev_13_intake_quarantine")
        j = s.rindex("#" * 79 + "\n", 0, i)
        s = s[:j] + body.rstrip() + "\n\n\n" + s[j:]
        s = re.sub(
            r'"""ALL_UNITS\.py — frozen only \([^)]*\)\."""',
            '"""ALL_UNITS.py — frozen only (%s frozen %s; %d frozen units)."""'
            % (uid.split("_")[0] + "_" + uid.split("_")[1],
               datetime.date.today().isoformat(), len(uids)),
            s, count=1)
        allp.write_text(s)
        step("ALL_UNITS insert", True, "before lev_13 banner; header count %d"
             % len(uids))
    rc, out = run([PY, str(allp)])
    green = out.count("ALL ASSERTIONS GREEN")
    step("ALL_UNITS corpus proof", rc == 0 and green == len(uids),
         "%d/%d green" % (green, len(uids)))

    summary()
    print("\nRITUAL COMPLETE for %s (%d frozen units)." % (uid, len(uids)))
    print("Manual next: watchlist (logic/middot_scan/), state-doc update, "
          "owner commit word.")


if __name__ == "__main__":
    main()
