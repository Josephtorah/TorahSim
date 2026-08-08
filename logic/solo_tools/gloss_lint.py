#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gloss_lint.py — Hebrew-glossing pre-check (owner's absolute rule:
no Hebrew term, transliterated or jargon, without an English
counterpart inline). Built 2026-08-08 when the external amendment
checker went on hold: both prior external checks FAILed round 1 on
exactly this class.

Heuristic, not proof: flags (1) known Hebrew-jargon lexicon words and
(2) hyphenated translit-shaped tokens whose FIRST occurrence in each
note block lacks a nearby gloss marker — a parenthetical, a quoted
gloss, or an equals/comma gloss within the following ~90 characters.
Review flags by hand; some are false positives (proper names, ids).

Usage: python3 logic/solo_tools/gloss_lint.py <file> [<file> ...]
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
TRANSLIT = re.compile(r"\b(?:[a-z]{2,}-){1,}[a-z]{2,}\b")
try:  # English parts -> not Hebrew translit (macOS system dictionary)
    ENGLISH = set(w.strip().lower() for w in open("/usr/share/dict/words"))
except OSError:
    ENGLISH = set()


HEBREW_RUN = re.compile(r"[א-ת][֑-תװ-״]*")


def lint_text(text, label, no_translit=False):
    flags = []
    seen = set()
    # Hebrew-script runs need an English gloss marker nearby (owner rule
    # amended 2026-08-08: script IS the display form; gloss stays law)
    for m in HEBREW_RUN.finditer(text):
        run = m.group(0)
        if len(run) < 2 or run in seen:
            continue
        seen.add(run)
        tail = text[m.end():m.end() + 120]
        if not GLOSS_NEAR.match(tail):
            flags.append((label, run, text[max(0, m.start() - 30):m.end() + 40]
                          .replace("\n", " ")))
    for m in TRANSLIT.finditer(text):
        tok = m.group(0)
        if tok in seen or tok.count("-") > 3:
            continue
        seen.add(tok)
        # skip obvious non-Hebrew compounds / file-ish tokens
        if any(p in tok for p in ("http", "json", "yaml", "html", "py",
                                  "note", "self", "left", "right", "one",
                                  "first", "check", "claims", "audit",
                                  "translit")):  # tool-flag syntax, not Hebrew
            continue
        # all-English-parts compound (e.g. "chain-attested") -> not translit
        def eng(p):
            p = p.lower()
            return any(x in ENGLISH for x in
                       (p, p.rstrip("s"), p[:-1], p[:-2], p[:-3] + "e" if len(p) > 3 else p))
        if ENGLISH and all(eng(p) for p in tok.split("-")):
            continue
        if no_translit:  # 2026-08-08 rule: translit itself is a violation
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
            tail = text[i.end():i.end() + 120]
            if not GLOSS_NEAR.match(tail):
                flags.append((label, w, text[max(0, i.start() - 30):i.end() + 40]
                              .replace("\n", " ")))
    return flags


def main(paths):
    no_translit = "--no-translit" in paths
    paths = [p for p in paths if p != "--no-translit"]
    total = 0
    for p in paths:
        text = open(p, encoding="utf-8").read()
        # lint only oral_audit_note_en blocks in yaml; whole file otherwise
        if p.endswith((".yaml", ".yml")):
            m = re.search(r"oral_audit_note_en: >\n((?:    .*\n)+)", text)
            blocks = [(m.group(1), "oral_audit_note_en")] if m else []
        else:
            blocks = [(text, p)]
        for text_block, label in blocks:
            for lbl, tok, ctx in lint_text(text_block, label, no_translit):
                total += 1
                print("FLAG  %-24s ...%s..." % (tok, ctx.strip()))
    print("gloss_lint: %d flag(s)" % total)
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
