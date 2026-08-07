#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""superlative_lint.py <unit.yaml>

Pre-review checklist generator: every review FAIL in the corpus's history
has been a prose ABSOLUTE (a false "first"/"only"/"all"/"whole
career"/"verbatim"/exhaustive list), never a numeric ordinal. This tool
lists every absolute-claim line in a draft so each can be DB-checked (or
fenced) BEFORE the adversarial reviewer sees it. It cannot verify claims;
it makes the dangerous ones impossible to miss.

Exit code is always 0 — output is a checklist, not a gate.
"""
import re
import sys

PATTERNS = [
    (r"\bFIRST\b", "first"),
    (r"\bfirst\b(?! (?:block|piece|token of the verse))", "first"),
    (r"\bONLY\b|\bonly\b", "only"),
    (r"\bALL\b(?!_)|\ball (?:five|four|three|six|seven|its|of)\b", "all/every"),
    (r"\bevery\b|\bEVERY\b", "all/every"),
    (r"\bwhole\b|\bWHOLE\b|\bentire\b|\bENTIRE\b", "whole/entire"),
    (r"\bverbatim\b", "verbatim"),
    (r"\bnever\b|\bNEVER\b", "never"),
    (r"\bexactly\b|\bEXACTLY\b", "exactly"),
    (r"\bno (?:earlier|later|other|prior)\b|\bNO (?:earlier|later|other|prior)\b",
     "no-other"),
    (r"\bdensest\b|\bstrongest\b|\bboldest\b|\blargest\b|\bbiggest\b",
     "superlative"),
    (r"\bDEBUT\b(?!\w)", "debut"),
    (r"\bcareer (?:closes|completes|CLOSES|COMPLETES)\b|\bCAREER CLOSES\b",
     "career-closes"),
    (r"\bhapax\b|\bHAPAX\b", "hapax"),
]


def main():
    path = sys.argv[1]
    hits = {}
    for lineno, line in enumerate(open(path, encoding="utf-8"), 1):
        # prose layers only: draft note (indented text), en: blocks, titles
        stripped = line.strip()
        if stripped.startswith(("he:", "he_translit:", "value_he",
                                "expr_en:", "id:", "ref:", "order:",
                                "cites:", "confidence:", "source:")):
            continue
        for pat, label in PATTERNS:
            if re.search(pat, line):
                hits.setdefault(lineno, (set(), stripped))
                hits[lineno][0].add(label)
    if not hits:
        print("no absolute-claim lines found (unusual — check the file)")
        return
    print("ABSOLUTE-CLAIM CHECKLIST — DB-check or fence each before review "
          "(%d lines):\n" % len(hits))
    for lineno in sorted(hits):
        labels, text = hits[lineno]
        print("L%-5d [%s]" % (lineno, ",".join(sorted(labels))))
        print("       %s" % text[:110])
    print("\nEvery reviewer FAIL to date lived in lines like these. "
          "Verify the claim, or fence it (cite the counterexample), "
          "before requesting review.")


if __name__ == "__main__":
    main()
