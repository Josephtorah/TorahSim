#!/usr/bin/env python3
"""
check_golden.py — regression contract for the versioned role rules.

Recomputes roles for the golden verses and diffs against
logic/role_rules/<CURRENT>/tests/golden.json. A mismatch means the rules or
lexicon changed behavior: either fix the regression, or cut a NEW rules/lexicon
version and regenerate goldens deliberately — never silently.
Run: python3 logic/role_rules/check_golden.py
"""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import taamim_tree_parse as ttp  # noqa: E402

spec = importlib.util.spec_from_file_location(
    "rendermod", ROOT / "logic/pre_logic_methods_2026-07-28/render_flat_ledger_morph_html.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)

version = (ROOT / "logic/role_rules/CURRENT").read_text().strip()
doc = json.load(open(ROOT / "logic/role_rules" / version / "tests/golden.json", encoding="utf-8"))

fails = 0
for osis, expected in doc["golden"].items():
    book, ch, v = osis.split(".")[0], int(osis.split(".")[1]), int(osis.split(".")[2])
    parsed = ttp.parse_verse(osis)
    oshb = r.load_oshb_words(ROOT / "Data" / f"{book}.xml", ch, v)
    got = []
    for leaf in r.collect_leaves(parsed["tree"]):
        segs = []
        for i in leaf["indices"]:
            segs.extend(r.word_segments(oshb[i]))
        got.append(r.leaf_role(segs))
    if got != expected:
        fails += 1
        print(f"FAIL {osis}")
        for i, (g, e) in enumerate(zip(got, expected)):
            if g != e:
                print(f"  B{i}: got {g!r} expected {e!r}")
    else:
        print(f"ok   {osis}")

print(f"\n{'ALL GREEN' if not fails else str(fails) + ' FAILURES'} · rules {doc['ruleset']} · lexicon {doc['lexicon']}")
sys.exit(1 if fails else 0)
