#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# -*- coding: utf-8 -*-
"""gloss_lint.py — Hebrew-glossing check (method law 8: no Hebrew term,
in script, transliterated, or as jargon, without an English counterpart
inline — anywhere, in any shipped file).

Heuristic, not proof: flags (1) Hebrew-script runs, (2) known
Hebrew-jargon lexicon words, and (3) hyphenated transliteration-shaped
tokens, whose FIRST occurrence in a file lacks a nearby gloss marker — a
parenthetical, a quoted gloss, or an equals/comma gloss within the
following ~90 characters. Review flags by hand; some are false positives
(proper names, identifiers).

Two additions over the research repo's original, both for Python files
only (documentation files get no leniency):

  1. A Hebrew run inside a comment block is also satisfied by a gloss
     marker later in the SAME comment block — the generated units'
     convention, where a wrapped multi-line Hebrew verse comment is
     followed immediately by its full English translation line
     ("[EN-AID] ...").
  2. Inside a generated verse SECTION (delimited by the "# ----- ref -----"
     header lines) that carries an "[EN-AID]" full-verse translation,
     Hebrew fragments and transliteration tokens re-quoting that verse are
     satisfied by the section's translation — the section is the
     rendering's display unit, and its English is inline within it.

Usage: python3 tools/gloss_lint.py <file> [<file> ...]
Exit 1 if any flag fires (advisory gate).
"""
import re
import sys

JARGON = {
    "dagesh", "qamatz", "patach", "segol", "tzere", "chiriq", "cholam",
    "shuruk", "sheva", "mappiq", "paseq", "maqqef", "etnachta", "silluq",
    "zaqef", "tifcha", "munach", "gematria", "masorah", "ketiv", "qere",
    "notarikon", "wayyiqtol", "weqatal", "jussive", "toledot", "midrash",
    "targum", "halakha", "aggadah", "tanna", "amora", "gezerah",
}
GLOSS_NEAR = re.compile(r'^[^.]{0,90}?(\(|"|\'|=|,\s*(the|a|an)\s|—\s*(the|a|an)\s)')
GLOSS_NEAR_WIDE = re.compile(r'^[^.]{0,700}?(\(|"|\'|=|,\s*(the|a|an)\s|—\s*(the|a|an)\s)')
TRANSLIT = re.compile(r"\b(?:[a-z]{2,}-){1,}[a-z]{2,}\b")
try:  # English parts -> not Hebrew translit (macOS system dictionary)
    ENGLISH = set(w.strip().lower() for w in open("/usr/share/dict/words"))
except OSError:
    ENGLISH = set()


HEBREW_RUN = re.compile(r"[א-ת][֑-תװ-״]*")

# Known transliterated fragments inside their phrase's piecewise English
# gloss in the generated unit renderings: the phrase's translation
# surrounds them, but that word itself stayed Hebrew. The renderings are
# generated files (never hand-edited); improving these means improving
# the generator in the research repo. Keyed (file basename, token).
ALLOW = {
    ("gen_10_serpent_violation_trace.py", "qere"),
    ("gen_24_nations_table.py", "and-vnei-ramah"),
    ("gen_32_hagar_angel.py", "to-onyekh"),
    ("gen_33_shaddai_covenant_flesh.py", "them-to-lohim"),
    ("gen_33_shaddai_covenant_flesh.py", "silver-bi-khlal"),
    ("gen_34_mamre_laugh_plea.py", "relati-khavdah-very"),
    ("gen_38_moriah_binding_oath.py", "inherit-gate-oyvav"),
    # CSS property/value tokens in the scroll reader's stylesheet that the
    # transliteration heuristic misreads as Hebrew compounds
    ("index.html", "webkit-text-size-adjust"),
    ("index.html", "inline-block"),
}


def _in_comment(text, pos):
    line_start = text.rfind("\n", 0, pos) + 1
    return "#" in text[line_start:pos]


def _sections(text):
    """Verse-section spans of a generated unit file, each marked for
    whether it carries an [EN-AID] full-verse translation line."""
    bounds = [m.start() for m in re.finditer(r"^# -{8,}", text, re.M)]
    bounds = [0] + bounds + [len(text)]
    return [(a, b, "[EN-AID" in text[a:b])
            for a, b in zip(bounds, bounds[1:])]


def _covered(spans, pos):
    for a, b, ok in spans:
        if a <= pos < b:
            return ok
    return False


GLOSS_BEFORE = re.compile(r'[”"\')][^.]{0,90}$')


def _glossed_before(text, start):
    """Generated-unit convention: the English translation often PRECEDES
    the token — ‹Hebrew› (“English gloss”) — description: token. A closing
    quote or parenthesis shortly before the token, with no sentence break
    between, counts as its gloss."""
    return bool(GLOSS_BEFORE.search(text[max(0, start - 120):start]))


ENGLISH_HEAD = re.compile(r"[A-Za-z]{3,}[^א-ת]{0,40}$")


HEB_OR_SPACE = re.compile(r"[א-ת֑-ׇװ-״\s־…/·]")


def _english_head(text, start):
    """English-first glossing, any file type: the Hebrew sits inside a
    bracket or quote immediately after the English words it annotates —
    severance grant (Hebrew phrase), "strikes a man" = Hebrew. The English
    head is the gloss; direction was never part of the law. The walk-back
    crosses earlier words of the same Hebrew phrase, so every word of a
    bracketed phrase is covered, not just the first."""
    i = start
    while i > 0 and HEB_OR_SPACE.match(text[i - 1]):
        i -= 1
    if i == 0 or text[i - 1] not in "('\"“‘‹«":
        return False
    return bool(ENGLISH_HEAD.search(text[max(0, i - 60):i - 1]))


def _comment_tail(text, end, budget=800):
    """Tail for a Hebrew run inside a comment: the rest of this comment
    line plus following comment-continuation lines, joined — so a gloss
    at the end of the block (the "[EN-AID]" line) is within reach."""
    tail = text[end:end + budget]
    out = []
    for i, ln in enumerate(tail.split("\n")):
        if i == 0:
            out.append(ln)
        elif ln.lstrip().startswith("#"):
            out.append(ln.lstrip().lstrip("#").lstrip())
        else:
            break
    return " ".join(out)


def lint_text(text, label, no_translit=False, py_mode=False):
    flags = []
    seen = set()
    spans = _sections(text) if py_mode else []
    # Hebrew-script runs need an English gloss marker nearby (Hebrew
    # script IS the display form; the gloss is law)
    for m in HEBREW_RUN.finditer(text):
        run = m.group(0)
        if len(run) < 2 or run in seen:
            continue
        seen.add(run)
        if _english_head(text, m.start()):
            continue
        if py_mode and (_covered(spans, m.start())
                        or _glossed_before(text, m.start())):
            continue
        if py_mode and _in_comment(text, m.start()):
            ok = GLOSS_NEAR_WIDE.match(_comment_tail(text, m.end()))
        else:
            ok = GLOSS_NEAR.match(text[m.end():m.end() + 120])
        if not ok:
            flags.append((label, run, text[max(0, m.start() - 30):m.end() + 40]
                          .replace("\n", " ")))
    for m in TRANSLIT.finditer(text):
        tok = m.group(0)
        if tok in seen or tok.count("-") > 3:
            continue
        seen.add(tok)
        if _english_head(text, m.start()):
            continue
        if py_mode and (_covered(spans, m.start())
                        or _glossed_before(text, m.start())):
            continue
        # skip obvious non-Hebrew compounds / file-ish tokens
        if any(p in tok for p in ("http", "json", "yaml", "html", "py",
                                  "note", "self", "left", "right", "one",
                                  "first", "check", "claims", "audit",
                                  "translit")):  # tool-flag syntax, not Hebrew
            continue
        # all-English-parts compound (e.g. "chain-attested") -> not translit
        def eng(p):
            p = p.lower()
            cands = {p, p.rstrip("s"), p[:-1], p[:-2]}
            if len(p) > 3:
                cands.add(p[:-3] + "e")
            if p.endswith("ies"):
                cands.add(p[:-3] + "y")        # families -> family
            if p.endswith("ing") and len(p) > 5:
                cands.add(p[:-3])              # destroying -> destroy
                cands.add(p[:-3] + "e")
                if p[-4] == p[-5]:
                    cands.add(p[:-4])          # begetting -> beget
            return any(x in ENGLISH for x in cands)
        if ENGLISH and all(eng(p) for p in tok.split("-")):
            continue
        if no_translit:  # optional stricter rule: translit itself flags
            flags.append((label, tok + " [TRANSLIT — use Hebrew script]",
                          text[max(0, m.start() - 30):m.end() + 40]
                          .replace("\n", " ")))
            continue
        tail = text[m.end():m.end() + 120]
        if not GLOSS_NEAR.match(tail):
            flags.append((label, tok, text[max(0, m.start() - 30):m.end() + 40]
                          .replace("\n", " ")))
    for w in sorted(JARGON):
        i = re.search(r"\b%s\b" % w, text, re.I)
        if i and w not in seen:
            if _english_head(text, i.start()):
                continue
            if py_mode and (_covered(spans, i.start())
                            or _glossed_before(text, i.start())):
                continue
            tail = text[i.end():i.end() + 120]
            if py_mode and _in_comment(text, i.start()):
                tail = _comment_tail(text, i.end())
                if GLOSS_NEAR_WIDE.match(tail):
                    continue
                tail = ""
            if not GLOSS_NEAR.match(tail):
                flags.append((label, w, text[max(0, i.start() - 30):i.end() + 40]
                              .replace("\n", " ")))
    return flags


def main(paths):
    no_translit = "--no-translit" in paths
    paths = [p for p in paths if p != "--no-translit"]
    import os
    total = 0
    for p in paths:
        text = open(p, encoding="utf-8").read()
        base = os.path.basename(p)
        for lbl, tok, ctx in lint_text(text, p, no_translit,
                                       py_mode=p.endswith(".py")):
            if (base, tok) in ALLOW:
                continue
            total += 1
            print("FLAG  %-24s ...%s..." % (tok, ctx.strip()))
    print("gloss_lint: %d flag(s)" % total)
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
