#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13b — COMPILE_DEBT's sitting-13 box (m): CHAPTER 14'S ARAMAIC COUNTS RE-MEASURED THROUGH NFKC. Sitting 13's lesson 4: the Onkelos
# export writes some letters as PRESENTATION FORMS (U+FB1D-FB4F — a letter with its dagesh precomposed) that plain() does not fold, so a substring seat count
# (onk_seats) or a token list (aramaic) can miss a seat or carry an odd token. Here: (1) the presentation-form code points in the export, by chapter; (2) every
# onk_seats literal of ch14_ink.py counted WITHOUT and WITH the NFKC fold; (3) every chapter-14 verse's token list both ways; (4) the whole book's verses whose
# plain tokens differ under the fold (the measure for every earlier reading's Aramaic counts). Every number printed, none typed. RUN FROM THE REPO ROOT.
import json, re, html, unicodedata, subprocess, collections
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Deuteronomy/he.json', encoding='utf-8'))['text']
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def row(c, e, fold):
    s = clean(onk_he[c - 1][e - 1])
    return unicodedata.normalize('NFKC', s) if fold else s
def arm_e(c, e, fold): return plain(row(c, e, fold))
def onk_seats(sub, fold): return [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if sub in arm_e(c + 1, v + 1, fold)]
def aramaic(c, v, fold): return [plain(x).strip('.:') for x in row(c, v, fold).rstrip(':').split()]
pf = collections.Counter(); pfrows = collections.Counter()
for ci, ch in enumerate(onk_he):
    for vi, r in enumerate(ch):
        s = clean(r); hit = [c for c in s if 0xFB1D <= ord(c) <= 0xFB4F]
        if hit: pfrows[ci + 1] += 1
        for c in hit: pf['U+%04X %s -> %s' % (ord(c), unicodedata.name(c, '?'), unicodedata.normalize('NFKC', c))] += 1
print('(1) PRESENTATION-FORM LETTERS IN THE ONKELOS EXPORT (Deuteronomy): %d code points in %d rows; by chapter %s' % (sum(pf.values()), sum(pfrows.values()), sorted(pfrows.items())))
for k, n in pf.most_common(): print('    %-60s %d' % (k, n))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch14_ink.py', encoding='utf-8').read()
lits = sorted(set(re.findall(r"onk_seats\('([^']+)'\)", src)))
print('(2) ch14_ink.py onk_seats literals: %d distinct' % len(lits))
moved = 0
for lit in lits:
    a, b = onk_seats(lit, False), onk_seats(lit, True)
    if a != b: moved += 1; print('    MOVED %-16s without %s  with NFKC %s' % (lit, a, b))
print('    literals whose seats MOVE under the fold: %d of %d' % (moved, len(lits)))
d14 = [v for v in range(1, len(onk_he[13]) + 1) if aramaic(14, v, False) != aramaic(14, v, True)]
print('(3) chapter 14 verses whose token list differs under the fold: %s (of %d)' % (d14, len(onk_he[13])))
for v in d14: print('    14:%d without %s\n         with    %s' % (v, aramaic(14, v, False), aramaic(14, v, True)))
book = [(c + 1, v + 1) for c in range(34) for v in range(len(onk_he[c])) if aramaic(c + 1, v + 1, False) != aramaic(c + 1, v + 1, True)]
print('(4) the whole book: %d verses of %d differ under the fold; by chapter %s' % (len(book), sum(len(ch) for ch in onk_he), sorted(collections.Counter(c for c, _ in book).items())))
print('    chapter 15\'s: %s' % [v for c, v in book if c == 15])
