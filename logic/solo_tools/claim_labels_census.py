#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""claim_labels_census.py — THE CLAIMS LABEL GATE (O11, 2026-09-08; World/step9/CLAIM_LABELS.md).

Reads every claims manifest (logic/oral_audit/manifests/*_claims.json) and prints the middah-label
census: by book, by unit, by leading code. FAILS (exit 2) on a malformed label — a middah key whose
value is empty, a leading code outside the vocabulary, a Hebrew letter in the label (the note is
English only). An UNLABELED row is printed as debt, never failed — until `--strict`, the O11 close,
when the debt itself fails the gate.

Usage:  python3 logic/solo_tools/claim_labels_census.py [--strict] [--units]
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MAN = os.path.join(HERE, '..', 'oral_audit', 'manifests')
CODE = re.compile(r'^(ink|plain|H|I(?:[1-9]|1[0-3])|E(?:[1-9]|[12][0-9]|3[0-2])|M-\d{2})(?:\s*\(.*\))?\s*$', re.S)
HEB = re.compile(r'[֐-׿]')


def census(strict=False, units=False):
    rows = []
    for f in sorted(glob.glob(os.path.join(MAN, '*_claims.json'))):
        uid = os.path.basename(f)[:-len('_claims.json')]
        for c in json.load(open(f, encoding='utf-8')):
            rows.append((uid, c))
    fails = []
    by_book = {}
    by_unit = {}
    by_code = {}
    n_lab = 0
    for uid, c in rows:
        book = uid[:3]
        has = 'middah' in c
        lab = str(c.get('middah') if c.get('middah') is not None else '')
        ok = False
        if has and not lab.strip():
            fails.append('%s %s: middah key present, EMPTY' % (uid, c.get('id')))
        elif lab.strip():
            m = CODE.match(lab.strip())
            if not m:
                fails.append('%s %s: label outside the vocabulary: %r' % (uid, c.get('id'), lab[:60]))
            elif HEB.search(lab):
                fails.append('%s %s: Hebrew letters in the label (English only)' % (uid, c.get('id')))
            else:
                ok = True
                code = m.group(1)
                by_code[code] = by_code.get(code, 0) + 1
        n_lab += ok
        b = by_book.setdefault(book, [0, 0]); b[0] += 1; b[1] += ok
        u = by_unit.setdefault(uid, [0, 0]); u[0] += 1; u[1] += ok
    total = len(rows)
    debt = total - n_lab
    print('CLAIM LABELS CENSUS — %d claims in %d manifests; labeled %d; DEBT %d' % (total, len(by_unit), n_lab, debt))
    for book in sorted(by_book):
        t, l = by_book[book]
        print('  %-4s %5d claims  labeled %5d  debt %5d' % (book, t, l, t - l))
    if by_code:
        print('  by code: ' + ', '.join('%s %d' % (k, by_code[k]) for k in sorted(by_code, key=lambda k: (-by_code[k], k))))
    if units:
        for uid in sorted(by_unit):
            t, l = by_unit[uid]
            if t - l:
                print('    %-44s %3d / %3d  debt %3d' % (uid, l, t, t - l))
    for f in fails:
        print('FAILED  ' + f)
    if strict and debt:
        print('FAILED  --strict: %d unlabeled claim(s) remain' % debt)
        fails.append('debt')
    print('GATE %s (%d failure line(s))' % ('FAILED' if fails else 'PASSED', len(fails)))
    return 2 if fails else 0


if __name__ == '__main__':
    sys.exit(census(strict='--strict' in sys.argv, units='--units' in sys.argv))
