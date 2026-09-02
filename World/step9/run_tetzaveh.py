#!/usr/bin/env python3
"""run_tetzaveh.py — run the Tetzaveh exam's case rows against the engine.

Loads cases_tetzaveh.yaml, validates every input against the vocabulary
registry, poses each case, and compares the engine's verdict set to the
exam's expectation. A list-valued expectation is a recorded dispute:
the engine must return EXACTLY that verdict set, every side labeled
with its authority. Every miss printed; silence never assumed to be
agreement. Same discipline as run_backfill.py."""
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine  # noqa: E402
from run_exam import load_vocabulary, validate_case  # noqa: E402


def verdict_set(verdicts):
    return sorted(str(v["verdict"]) for v in (verdicts or []))


def main():
    spec = yaml.safe_load(open(HERE / "cases_tetzaveh.yaml",
                               encoding="utf-8"))
    modules = [m for m in spec if isinstance(m, dict) and "module" in m]
    vocab = load_vocabulary()
    total = answered = matched = 0
    misses = []
    for mod in modules:
        name = mod["module"]
        print("== %s [%s]" % (name, mod["tractate"]))
        for case in mod.get("cases", []):
            total += 1
            cid = case["id"]
            inp = case["input"]
            bad = validate_case(vocab, inp)
            if bad:
                print("   %-26s VOCABULARY REJECT: %s" % (cid, bad))
                misses.append((cid, "vocabulary", bad))
                continue
            out = engine.answer(name, inp)
            if not out:
                print("   %-26s ENGINE SILENT (expected: %s)"
                      % (cid, case["expected"].get("verdict")))
                misses.append((cid, "silent", case["expected"]))
                continue
            answered += 1
            got = verdict_set(out)
            exp = case["expected"].get("verdict")
            if isinstance(exp, list):
                ok = got == sorted(str(x) for x in exp) and \
                    all("authority" in v for v in out)
                exp_disp = "+".join(str(x) for x in exp)
            else:
                ok = str(exp) in got
                exp_disp = str(exp)
            flag = "OK " if ok else "MISS"
            if ok:
                matched += 1
            else:
                misses.append((cid, "mismatch", {"expected": exp,
                                                 "got": got}))
            print("   %-26s %s expected=%-30s got=%s"
                  % (cid, flag, exp_disp[:30], ", ".join(got)))
    print("\nTETZAVEH: %d cases, %d answered, %d matched, %d misses"
          % (total, answered, matched, len(misses)))
    for m in misses:
        print("  MISS:", m)
    return 0 if not misses else 1


if __name__ == "__main__":
    sys.exit(main())
