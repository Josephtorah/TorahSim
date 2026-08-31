#!/usr/bin/env python3
"""pose_case.py — state a hypothetical in the tradition's own vocabulary
and hear the machine's verdict.

    python3 pose_case.py                       # interactive: menus
    python3 pose_case.py life_override event=rockslide_burial day=shabbat \
            found=dead_mid_clearing            # direct: key=value args

The menus ARE the registry (vocabulary.yaml): every choice offered was
introduced by a source actually read, shown with its own Hebrew ink and
English. A case cannot be stated in vocabulary no source defined — that is
the guard against the simulator drifting into invented law. Verdicts come
from engine.py and always carry provenance; a dispute is two labeled
verdicts, never an error.
"""
import sys
import yaml
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine  # noqa: E402
from run_exam import load_vocabulary, validate_case  # noqa: E402


def show_verdicts(verdicts):
    if not verdicts:
        print("\n  THE MACHINE IS SILENT — no rule in the compiled modules")
        print("  matches this case. (Silence is honest: nothing is guessed.)")
        return
    print()
    if len(verdicts) > 1 and any("authority" in v for v in verdicts):
        print("  A RECORDED DISPUTE — the machine returns every side, labeled:")
    for v in verdicts:
        head = "  VERDICT: %s" % v["verdict"]
        if v.get("authority"):
            head += "   [%s]" % v["authority"]
        print(head)
        print("    basis: %s" % v["basis"])
        for k, val in (v.get("provenance") or {}).items():
            print("    %s: %s" % (k, val))
        print()


def interactive(vocab):
    mods = list(engine.RULES)
    print("\nPOSE A CASE — choose a module:")
    for i, m in enumerate(mods, 1):
        print("  %d. %s [%s]" % (i, m, engine.RULES[m]["tractate"]))
    try:
        mi = int(input("module #: ").strip())
        module = mods[mi - 1]
    except (ValueError, IndexError, EOFError):
        sys.exit("no module chosen")

    case = {}
    print("\nNow the case. For each dimension: pick a number, or press "
          "Enter to leave it out of the case.\n")
    for dim, d in vocab.items():
        kind = d["kind"]
        if kind == "integer":
            raw = input("%s (a number, Enter to skip): " % dim).strip()
            if raw:
                try:
                    case[dim] = int(raw)
                except ValueError:
                    print("  not a number — skipped")
            continue
        vals = d.get("values", [])
        print("%s   [%s]" % (dim, d.get("introduced_by", "")))
        for i, v in enumerate(vals, 1):
            he = v.get("he", "")
            gl = v.get("gloss", "")
            print("  %d. %-24s %s (%s)" % (i, v["value"], he, gl))
        raw = input("choice%s (Enter to skip): "
                    % ("s, comma-separated" if kind in ("multi_choice", "list")
                       else "")).strip()
        if not raw:
            continue
        picks = []
        for p in raw.split(","):
            p = p.strip()
            try:
                picks.append(vals[int(p) - 1]["value"])
            except (ValueError, IndexError):
                print("  bad choice %r — skipped" % p)
        if picks:
            case[dim] = picks if kind in ("multi_choice", "list") else picks[0]
    return module, case


def direct(args, vocab):
    module = args[0]
    if module not in engine.RULES:
        sys.exit("unknown or uncompiled module: %s (have: %s)"
                 % (module, ", ".join(engine.RULES)))
    case = {}
    for a in args[1:]:
        if "=" not in a:
            sys.exit("expected key=value, got %r" % a)
        k, v = a.split("=", 1)
        if "," in v:
            case[k] = [x.strip() for x in v.split(",")]
        else:
            try:
                case[k] = int(v)
            except ValueError:
                case[k] = v
    # lists for multi dims even when single-valued
    for k in list(case):
        d = vocab.get(k)
        if d and d["kind"] in ("multi_choice", "list") \
                and not isinstance(case[k], list):
            case[k] = [case[k]]
    return module, case


def main():
    vocab = load_vocabulary()
    if len(sys.argv) > 1:
        module, case = direct(sys.argv[1:], vocab)
    else:
        module, case = interactive(vocab)
    bad = validate_case(vocab, case)
    if bad:
        print("\nTHE CASE CANNOT BE STATED — vocabulary no source defined:")
        for b in bad:
            print("  " + b)
        print("(To extend the vocabulary, read the source that introduces "
              "the value and register it with provenance.)")
        sys.exit(1)
    print("\nTHE CASE: %s" % case)
    show_verdicts(engine.answer(module, case))


if __name__ == "__main__":
    main()
