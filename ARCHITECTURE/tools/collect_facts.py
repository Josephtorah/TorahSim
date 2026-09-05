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
for path in sorted(glob.glob(os.path.join(STEP9, "cold_run_*.py"))):
    name = os.path.basename(path)[:-3]
    src = open(path, encoding="utf-8").read()
    p = subprocess.run([sys.executable, path], cwd=STEP9, capture_output=True, text=True)
    out = p.stdout + p.stderr
    rec = {"exit": p.returncode, "lines": len(src.splitlines()),
           "top_level_defs": re.findall(r"^def (\w+)\(", src, re.M)}
    m = re.search(r"(MATRIX:.*|RESULT:.*|\w+ PASS: .*|PASS 2: .*|\w+ MACHINE: .*|\w+ COMPLETE: .*)", out)
    rec["score_line"] = m.group(1).strip() if m else None
    m = re.search(r"((?:PASS-2 |PROVENANCE )?FRACTIONS.*)", out)
    rec["fractions_line"] = m.group(1).strip() if m else None
    m = re.search(r"LEDGER OPS.*", out)
    rec["ledger_ops_line"] = m.group(0).strip() if m else None
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
    b: sum(1 for u in frozen if os.path.basename(u).startswith(b + "_")) for b in ("gen", "exo", "lev")}
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
