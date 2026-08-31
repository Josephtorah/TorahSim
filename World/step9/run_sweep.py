#!/usr/bin/env python3
"""run_sweep.py — run the Genesis sweep's case rows against the engine.

Loads cases_gen_sweep.yaml, validates every input against the vocabulary
registry, poses each case, and compares the engine's verdict set to the
exam's expectation. Every miss printed; silence never assumed to be
agreement.
"""
import sys
import yaml
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine  # noqa: E402
from run_exam import load_vocabulary, validate_case  # noqa: E402


def verdict_set(verdicts):
    return sorted(v["verdict"] for v in (verdicts or []))


def main():
    spec = yaml.safe_load(open(HERE / "cases_gen_sweep.yaml",
                               encoding="utf-8"))
    modules = [m for m in spec if isinstance(m, dict) and "module" in m]
    vocab = load_vocabulary()
    total = answered = matched = 0
    misses = []
    for mod in modules:
        name = mod["module"]
        print("== %s [%s] — %s" % (name, mod["tractate"], mod["oracle"]))
        for case in mod.get("cases", []):
            total += 1
            cid = case["id"]
            inp = case["input"]
            bad = validate_case(vocab, inp)
            if bad:
                print("   %-12s VOCABULARY REJECT: %s" % (cid, bad))
                misses.append((cid, "vocabulary", bad))
                continue
            out = engine.answer(name, inp)
            if not out:
                print("   %-12s ENGINE SILENT (expected: %s)"
                      % (cid, case["expected"].get("verdict")))
                misses.append((cid, "silent", case["expected"]))
                continue
            answered += 1
            got = verdict_set(out)
            exp = case["expected"].get("verdict", "")
            # a dispute expectation matches when the engine returns >1
            # labeled verdicts; a named expectation must appear in the set
            if exp.startswith("dispute"):
                ok = len(out) > 1 and all("authority" in v or i == 0
                                          for i, v in enumerate(out))
            else:
                ok = exp in got or (len(got) == 1 and got[0].startswith(exp))
            flag = "OK " if ok else "MISS"
            if ok:
                matched += 1
            else:
                misses.append((cid, "mismatch", {"expected": exp,
                                                 "got": got}))
            print("   %-12s %s expected=%-28s got=%s"
                  % (cid, flag, exp[:28], ", ".join(got)))
    print("\nSWEEP: %d cases, %d answered, %d matched, %d misses"
          % (total, answered, matched, len(misses)))
    for m in misses:
        print("  MISS:", m)
    held = spec[-1].get("held_rows", []) if isinstance(spec[-1], dict) \
        else []
    # held_rows rides on the last module mapping only if structured so;
    # find it wherever it lives
    for node in spec:
        if isinstance(node, dict) and "held_rows" in node:
            held = node["held_rows"]
    print("held rows classified (not compiled): %d" % len(held))
    return 0 if not misses else 1


if __name__ == "__main__":
    sys.exit(main())
