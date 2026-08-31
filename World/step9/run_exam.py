#!/usr/bin/env python3
"""run_exam.py — put the case shelf's rows to the machine, before and after.

Phase 1 (the exam): each case is classified against the machine AS IT
STANDS — A: the machine answers; B: the machine holds the rule as witness
text but cannot apply it; C: the machine holds nothing at any anchor.
The classifications below were made by reading the actual holdings (the
claims quoted in REPORT.md), not by keyword count.

Phase 2 (the demonstration): modules compiled in engine.py answer the same
cases; expected vs produced verdicts are compared mechanically.
"""
import sys
import yaml
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine  # noqa: E402

# Phase-1 verdicts from the manual audit of holdings (sources in REPORT.md).
CLASSIFICATION = {
    "YOMA_8_7_a": ("B", "held: G18-05 'one clears the debris on the Sabbath "
                        "even in doubt' — text, not a function"),
    "YOMA_8_7_b": ("B", "held: G18-05 carries the gemara's mechanism (dig to "
                        "the nose) — richer than the Mishnah's bare verdict"),
    "YOMA_8_7_c": ("C", "held NOWHERE: the dead->stop leg is the Mishnah's "
                        "own addition at this anchor"),
    "YEV_6_6_a": ("B", "held: G14-15 carries BOTH houses — Hillel proved "
                       "from Gen 5:2, Shammai's two sons recorded"),
    "YEV_6_6_b": ("B", "held: same claim, agreed composition"),
    "YEV_6_6_c": ("B", "held — AT A DIFFERENT ANCHOR: G32-16 on Gen 16:3 "
                       "(Sarai's ten years), four seats, with riders the "
                       "exam did not know and the tradition's own grade: "
                       "'no proof, but a hint'"),
    "YEV_6_6_d": ("C", "held nowhere: the miscarriage-restart clause was "
                       "never seated"),
    "YEV_6_6_e": ("B-partial", "held for ONE side only: G06-03's ink "
                               "derivation (lean ve-khivshuha ketiv, 'subdue "
                               "HER') = not commanded; the dissent is absent "
                               "from the machine"),
    "EDU_2_10_a": ("B", "held: G17-11 — twelve months AND the five-judgment "
                        "census membership AND the date-facts to compute it; "
                        "the closest case to Class A: only arithmetic "
                        "application is missing"),
    "EDU_2_10_b": ("C", "held nowhere: the gehinom member is off-book — not "
                        "Genesis material"),
}


def load_vocabulary():
    v = yaml.safe_load((HERE / "vocabulary.yaml").read_text())
    return {d["dimension"]: d for d in v}


def validate_case(vocab, case_input):
    """A case may only be stated in registered vocabulary. Returns a list
    of violations (empty = valid)."""
    bad = []
    for dim, val in case_input.items():
        d = vocab.get(dim)
        if d is None:
            bad.append("unregistered dimension: %s" % dim)
            continue
        kind = d["kind"]
        allowed = {x["value"] for x in d.get("values", [])}
        if kind == "integer":
            if not isinstance(val, int):
                bad.append("%s must be an integer, got %r" % (dim, val))
        elif kind in ("multi_choice", "list"):
            vals = val if isinstance(val, list) else [val]
            for x in vals:
                if x not in allowed:
                    bad.append("unregistered value %r for %s" % (x, dim))
        else:
            if val not in allowed:
                bad.append("unregistered value %r for %s" % (val, dim))
    return bad


def main():
    spec = yaml.safe_load((HERE / "cases_pilot.yaml").read_text())
    vocab = load_vocabulary()
    viol = []
    for mod in spec:
        for case in mod["cases"]:
            for b in validate_case(vocab, case["input"]):
                viol.append("%s: %s" % (case["id"], b))
    if viol:
        print("VOCABULARY VIOLATIONS — a case is stated in vocabulary no "
              "source defined:")
        for b in viol:
            print("  " + b)
        return 1
    print("vocabulary: all case inputs validate against the registry "
          "(%d dimensions)" % len(vocab))
    total = a = b = cc = 0
    answered = mismatched = 0
    for mod in spec:
        print("\nMODULE %s   oracle: %s" % (mod["module"], mod["oracle"]))
        compiled = mod["module"] in engine.RULES
        print("  engine: %s" % ("COMPILED" if compiled else "not compiled"))
        for case in mod["cases"]:
            total += 1
            cls, note = CLASSIFICATION[case["id"]]
            case["class"] = cls
            case["machine_answer"] = note
            a += cls == "A"
            b += cls.startswith("B")
            cc += cls == "C"
            line = "  %-11s before: %-10s" % (case["id"], cls)
            if compiled:
                got = engine.answer(mod["module"], case["input"]) or []
                case["engine_answer"] = got
                exp = case["expected"]
                exp_set = ({d["verdict"] for d in exp["dispute"]}
                           if "dispute" in exp and exp.get("dispute")
                           else {exp["verdict"]})
                got_set = {g["verdict"] for g in got}
                ok = exp_set == got_set
                answered += 1
                mismatched += (not ok)
                case["engine_class"] = "A" if ok else "A-MISMATCH"
                line += " after: %s  %s" % (
                    "A" if ok else "MISMATCH",
                    " | ".join(sorted(got_set)))
            print(line)
    (HERE / "cases_pilot.yaml").write_text(
        yaml.safe_dump(spec, allow_unicode=True, sort_keys=False, width=78))
    # SURFACE: draft a finding for every case the machine cannot hold —
    # Class C and partial holdings feed the workshop's findings queue
    # (logic/findings/FINDINGS_QUEUE.md; filed by hand, ruled by the owner).
    drafts = []
    for mod in spec:
        for case in mod["cases"]:
            cls = case.get("class") or ""
            if cls == "C" or cls.endswith("partial"):
                drafts.append("FINDING DRAFT [%s / %s]: %s — %s"
                              % (mod["oracle"], case["id"], cls,
                                 case["machine_answer"]))
    if drafts:
        (HERE / "findings_draft.md").write_text(
            "# drafts from the last exam run — file into the workshop\n"
            "# findings queue on the owner's word; this file is overwritten\n"
            "# each run\n\n" + "\n\n".join(drafts) + "\n")
        print("\n%d finding draft(s) -> findings_draft.md" % len(drafts))
    print("\nEXAM: %d cases — before the engine: A=%d  B=%d  C=%d" %
          (total, a, b, cc))
    print("ENGINE: %d cases answered by compiled modules, %d mismatches" %
          (answered, mismatched))
    return mismatched


if __name__ == "__main__":
    sys.exit(main())
