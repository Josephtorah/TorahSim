#!/usr/bin/env python3
"""o11_print.py — print a label batch with the script's PROPOSAL and flags beside every row (the reader's aid).
Usage: python3 o11_print.py <batch> <outfile>   batch in B1 B2 B3 B4 B5
"""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import glob, json, os, re, sys, collections

MAN = (_ROOT + '/logic/oral_audit/manifests')
LAW_UNITS = re.compile(r'^(lev_|law0|exo_2[0-3]_|exo_2[5-9]_|exo_3[01]_|exo_3[5-9]_|exo_40_)')

def fam(s):
    s = re.sub(r'\s+', ' ', s or '').strip()
    if re.match(r'^Minchat Shai', s): return 'minchat_shai'
    if re.match(r'^Onkelos', s): return 'onkelos'
    if re.match(r'^(Kitzur )?Baal HaTurim', s): return 'kitzur_bht'
    if re.match(r'^Sifra', s): return 'sifra'
    if re.match(r'^Bereshit Rabbah', s): return 'bereshit_rabbah'
    return 'teacher'

INFER = collections.OrderedDict([
    ('E29', r'gematria|letter-value|numerical value|numeric value|letter values'),
    ('E30', r'notarikon|acronym|initial letters|initials|final letters|final-letters|end-letters|word-ends|anagram|rearranged'),
    ('E7',  r'exactly twice|exactly two|stands twice|twice in the torah|two in the masorah|pair-leg|the pair|the same word|same wording|equal decree|verbal analogy|gezerah shavah|here and (at|in)|concordance'),
    ('E5',  r'a[- ]fortiori|qal wa-?chomer|kal va-?chomer|all the more'),
    ('E10', r'repeated|repetition|doubled|doubling'),
    ('E27', r'symmetry|chiasm|mirror|measure for measure'),
    ('E26', r'parable|mashal'),
    ('E1',  r'to include|includes|inclusion|ribui'),
    ('E2',  r'to exclude|excludes|exclusion|miut'),
    ('E31', r'earlier and later|no earlier|not in chronological'),
    ('I12', r'from (its )?context|me-?inyano'),
    ('I13', r'third verse|contradict'),
    ('I4',  r'kelal|general and particular|particular and general|general then particular'),
    ('LEARN', r'\bto teach\b|\bteaches\b|\bwe learn\b|\blearn(ed|s)? from\b|\bderiv(e|es|ed)\b|\binfer'),
])

def flags(text):
    t = text.lower()
    return [k for k, rx in INFER.items() if re.search(rx, t)]

def propose(uid, c, fl):
    f = fam(c.get('source', ''))
    ct = (c.get('check') or {}).get('type')
    law = bool(LAW_UNITS.match(uid))
    if f in ('minchat_shai', 'onkelos'):
        return 'ink'
    if f == 'kitzur_bht':
        if ct in ('final_letters', 'initial_letters', 'letters_multiset') or 'E30' in fl: return 'E30'
        if 'E29' in fl: return 'E29'
        if 'E7' in fl or ct in ('token_count', 'adjacency'): return 'I2' if law else 'E7'
        if 'E10' in fl: return 'E10'
        return '?'
    # teachers: propose the first inference flag, span-twinned
    for k in fl:
        if k == 'LEARN': continue
        if k == 'E5': return 'I1' if law else 'E5'
        if k == 'E7': return 'I2' if law else 'E7'
        return k
    return '?'

def select(batch, uid, c):
    f = fam(c.get('source', ''))
    if batch == 'B1': return f == 'minchat_shai' or (f == 'onkelos' and not uid.startswith('lev'))  # B5 amendment 2026-09-09: Leviticus's 15 Onkelos rows (deferred at B1, all unlabeled) move to B5
    if batch == 'B2': return f == 'kitzur_bht'
    if batch == 'B3': return uid.startswith('gen') and f not in ('minchat_shai', 'onkelos', 'kitzur_bht')  # incl. G11-18, the one Sifra row of Genesis (found at B3's first print: 676 of 677)
    if batch == 'B4': return (uid.startswith('exo') or uid.startswith('law')) and f == 'teacher'
    if batch == 'B5': return uid.startswith('lev') and f in ('sifra', 'teacher', 'onkelos')  # amended 2026-09-09: + the Onkelos family of Leviticus
    return False

def main(batch, out):
    rows = []
    for fpath in sorted(glob.glob(os.path.join(MAN, '*_claims.json'))):
        uid = os.path.basename(fpath)[:-len('_claims.json')]
        for c in json.load(open(fpath, encoding='utf-8')):
            if select(batch, uid, c): rows.append((uid, c))
    n_lab = sum(1 for u, c in rows if str(c.get('middah') or '').strip())
    prop = collections.Counter(); flagged = 0
    lines = []
    for uid, c in rows:
        text = re.sub(r'\s+', ' ', c.get('claim_en', ''))
        fl = flags(text + ' ' + c.get('source', ''))
        p = propose(uid, c, fl)
        prop[p] += 1
        full = bool(fl) or p != 'ink'
        flagged += bool(fl)
        body = text if full else text[:240] + (' ...' if len(text) > 240 else '')
        lines.append('%s | %s | src=%s | check=%s | flags=%s | PROPOSE %s%s\n    %s' % (
            uid, c['id'], re.sub(r'\s+', ' ', c.get('source', ''))[:90], (c.get('check') or {}).get('type'),
            ','.join(fl) or '-', p, ' | HAS-LABEL ' + str(c.get('middah')) if str(c.get('middah') or '').strip() else '', body))
    open(out, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    print('%s rows %d (already labeled %d); flagged %d; proposals %s; written %s (%d chars)' % (
        batch, len(rows), n_lab, flagged, dict(prop), out, sum(len(l) for l in lines)))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
