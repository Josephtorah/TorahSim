#!/usr/bin/env python3
"""collect_facts.py — re-verifies the mechanical facts the catalog cites.

Runs every World/step9/cold_run_*.py (all are read-only over the corpus
and touch no unit), captures its printed matrix line, provenance
fractions, ledger operations, and the registry effects its source
names, plus the layer counts the README states, and writes them to
ARCHITECTURE/catalog_facts.json. Writes nothing anywhere else.

    python3 ARCHITECTURE/tools/collect_facts.py

If a number in the markdown disagrees with this file, the markdown is
stale, not the code.
"""
import glob, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
STEP9 = os.path.join(ROOT, "World", "step9")
OUT = os.path.join(os.path.dirname(HERE), "catalog_facts.json")

try:
    import yaml
except ImportError:
    yaml = None

facts = {"spans": {}, "layers": {}}

# ---- the effects registry -------------------------------------------------
reg_ids = []
if yaml:
    reg = yaml.safe_load(open(os.path.join(STEP9, "effect_vocabulary.yaml"), encoding="utf-8"))
    effs = reg["effects"]
    if isinstance(effs, dict):
        for k, v in effs.items():
            reg_ids.append((k, (v or {}).get("ledger_op")))
    else:
        for e in effs:
            reg_ids.append((e.get("id") or e.get("effect"), e.get("ledger_op")))
facts["layers"]["effects_registered"] = len(reg_ids)
ops = {}
for _, op in reg_ids:
    ops[op] = ops.get(op, 0) + 1
facts["layers"]["effects_by_ledger_op"] = ops

# ---- run every cold run, read-only ----------------------------------------
# 2026-09-13: a runner's OWN lines are the LAST it prints — the runners it imports print theirs first (the first-match
# read of 2026-09-05 took an imported runner's matrix for the fourth book's); the runs go in a pool of six, and every
# output is saved beside this file's scratch (COLLECT_OUT, if set) so a later reading needs no rerun.
from concurrent.futures import ThreadPoolExecutor   # threads: each run is a subprocess; a process pool re-imports this script under spawn

def _run(path):
    p = subprocess.run([sys.executable, path], cwd=STEP9, capture_output=True, text=True)
    return path, p.returncode, p.stdout + p.stderr

_paths = sorted(glob.glob(os.path.join(STEP9, "cold_run_*.py")))
_save = os.environ.get("COLLECT_OUT")
with ThreadPoolExecutor(max_workers=int(os.environ.get("COLLECT_WORKERS", "6"))) as ex:
    _results = dict((pth, (rc, out)) for pth, rc, out in ex.map(_run, _paths))
for path in _paths:
    name = os.path.basename(path)[:-3]
    src = open(path, encoding="utf-8").read()
    rc, out = _results[path]
    if _save:
        os.makedirs(_save, exist_ok=True)
        open(os.path.join(_save, name + ".out"), "w", encoding="utf-8").write(out)
    rec = {"exit": rc, "lines": len(src.splitlines()),
           "top_level_defs": re.findall(r"^def (\w+)\(", src, re.M)}
    # THE SWEEP'S OWN RULE (run_cold_all.py): the runner's score is the LAST line matching its SCORE regex — an imported
    # runner prints earlier, and a runner may import late; the fractions and ledger-ops lines are read only AFTER that line
    SCORE = re.compile(r"(\d+)\s*/\s*(\d+)\s*(?:cells|checkpoints|match|test)")
    olines = out.split("\n"); idx = [i for i, l in enumerate(olines) if SCORE.search(l)]
    if idx:
        i = idx[-1]; rec["score_line"] = olines[i].strip()[:220]
        after = olines[i + 1:i + 8]
        fr = [l for l in after if "FRACTIONS" in l]; lo = [l for l in after if l.startswith("LEDGER OPS")]
        rec["fractions_line"] = fr[0].strip() if fr else None
        rec["ledger_ops_line"] = lo[0].strip() if lo else None
    else:
        rec["score_line"] = rec["fractions_line"] = rec["ledger_ops_line"] = None
    rec["functions_graded"] = re.findall(r"FUNCTION: (.+?)\s+\(answer sheet: (.+?)\)", out)
    rec["effects_named_in_source"] = sorted(
        k for k, _ in reg_ids if re.search(r"['\"]%s['\"]" % re.escape(k), src))
    rec["cross_span_python_imports"] = sorted(set(re.findall(r"(?:from|import)\s+(cold_run_\w+)", src)))
    facts["spans"][name] = rec

# ---- layer counts ----------------------------------------------------------
units = glob.glob(os.path.join(ROOT, "logic", "units", "*.yaml"))
frozen = [u for u in units if re.search(r"^\s*status: frozen", open(u, encoding="utf-8").read(), re.M)]
facts["layers"]["unit_files"] = len(units)
facts["layers"]["units_frozen"] = len(frozen)
facts["layers"]["units_frozen_by_book"] = {
    b: sum(1 for u in frozen if os.path.basename(u).startswith(b + "_")) for b in ("gen", "exo", "lev", "num", "deu")}   # the fourth book added 2026-09-13
facts["layers"]["py_renderings"] = len(glob.glob(os.path.join(ROOT, "logic", "py_units", "*.py")))
facts["layers"]["rules_modules"] = len(glob.glob(os.path.join(STEP9, "*_rules.py")))
facts["layers"]["case_files"] = len(glob.glob(os.path.join(STEP9, "cases_*.yaml")))
try:
    ids = json.load(open(os.path.join(STEP9, "rule_catalog_ids.json")))
    facts["layers"]["rule_ids"] = len(ids) if isinstance(ids, list) else len(ids.get("rules", ids))
except Exception:
    facts["layers"]["rule_ids"] = None
if yaml:
    v = yaml.safe_load(open(os.path.join(STEP9, "vocabulary.yaml"), encoding="utf-8"))
    facts["layers"]["vocab_dimensions"] = len(v)
    facts["layers"]["vocab_values"] = sum(len(d.get("values", [])) for d in v)
ct = open(os.path.join(ROOT, "logic", "corpus", "CORPUS_TRUTH.py"), encoding="utf-8").read()
facts["layers"]["corpus_truth_asserts"] = re.findall(r"^assert (len\(W\[\"\w+\"\]\) == \d+|.*_state_hash.*)$", ct, re.M)
led = open(os.path.join(STEP9, "EXAM_LEDGER.md"), encoding="utf-8").read()
rounds = re.findall(r"^## ROUND (\d+) .*?: (\d+/\d+)\s*$", led, re.M)
facts["layers"]["exam_last_round"] = rounds[-1] if rounds else None
m = re.findall(r"\((\d+/\d+) across", led)
facts["layers"]["exam_running_total"] = m[-1] if m else None
we = open(os.path.join(STEP9, "world_engine.py"), encoding="utf-8").read()
facts["layers"]["engine_daemons"] = re.findall(r"^def (law_\w+)\(", we, re.M)
mc = open(os.path.join(ROOT, "logic", "MOVE_CATALOG.md"), encoding="utf-8").read()
facts["layers"]["moves"] = sorted(set(re.findall(r"^## (M-\d+)", mc, re.M)))

json.dump(facts, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("wrote", os.path.relpath(OUT, ROOT))
for k, r in facts["spans"].items():
    print("  %-24s exit %d  %s" % (k, r["exit"], r["score_line"]))
