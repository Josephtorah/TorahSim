#!/usr/bin/env python3
# THE NUMBERS WALK sitting 4b — THE MEASUREMENTS, second pass (2026-09-10): the register by the wayyiqtol tag; the definite one's Torah
# seats whole; the quarter's plene form the first pass's exclusion hid (רביעית inside רביעי); the ordinal reader on Sheshai; the
# third-generation homograph (שלשים 'thirds' read as thirty); the marker verses that carry a definite one or a fraction (the stitcher's
# rows that would move); the measure nouns after the fraction forms, censused.
import sqlite3, sys, io, re, contextlib, collections
ROOT = '<repo-old>'
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
db = sqlite3.connect(f'file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by = {}
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((plain(he), pointed(he), m or ''))
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')

print('==== (6b) THE REGISTER OF 13-14 by the wayyiqtol tag (V.w) ====')
reg = {}
for (b, c, v), ws in by.items():
    if b == 'Num' and c in (13, 14):
        reg[(c, v)] = [x for x, _, m in ws if re.search(r'^H?V[a-z]w', m)]
LINES = [('spies_commanded', 13, 1, 2), ('spies_sent', 13, 3, 16), ('spies_instructed', 13, 17, 20), ('spies_went_up', 13, 21, 24), ('spies_returned', 13, 25, 26),
         ('report_given', 13, 27, 29), ('caleb_hushed_the_people', 13, 30, 30), ('evil_report_spread', 13, 31, 33), ('congregation_wept', 14, 1, 4),
         ('joshua_and_caleb_pleaded', 14, 5, 9), ('glory_appeared_at_the_threat', 14, 10, 10), ('moses_pleaded_on_the_attributes', 14, 11, 19),
         ('pardoned_and_decreed', 14, 20, 25), ('decree_declared', 14, 26, 35), ('ten_spies_died_by_plague', 14, 36, 38), ('presumed_to_go_up', 14, 39, 44), ('smitten_to_hormah', 14, 45, 45)]
regv = sorted(k for k, vv in reg.items() if vv)
print('  register verses: ch13 %d, ch14 %d, total %d' % (sum(1 for c, v in regv if c == 13), sum(1 for c, v in regv if c == 14), len(regv)))
for name, c, lo, hi in LINES:
    vv = [(v, reg[(c, v)]) for v in range(lo, hi + 1) if reg[(c, v)]]
    print('  %-32s %d:%d-%d  register %d  %s' % (name, c, lo, hi, len(vv), ' '.join('%d:%s' % (v, ','.join(x)) for v, x in vv)[:160]))
print('  lines with no register verse:', [n for n, c, lo, hi in LINES if not any(reg[(c, v)] for v in range(lo, hi + 1))])

print('\n==== (2b) THE QUARTER\'S PLENE FORM and the fraction forms before a MEASURE noun ====')
def seats(pattern):
    out = []
    for (b, c, v), ws in by.items():
        for i, (x, xp, m) in enumerate(ws):
            if re.fullmatch(pattern, x):
                out.append((b, c, v, i, xp, m, ws[i - 1][0] if i else '', ws[i + 1][0] if i + 1 < len(ws) else ''))
    return out
for pat, lab in ((r'(ו|ב|ל|כ)?רביעית', 'רביעית (plene, two yods)'), (r'(ו|ב|ל|כ)?(רבע|רבעית|רביעת|רביעית)', 'ALL quarter numeral forms'), (r'(ו|ב|ל|כ)?(שלשית|שלישת|שלישית)', 'ALL third forms'),
                 (r'(ו|ב|ל|כ)?(עשירת|עשירית)', 'ALL tenth-fraction forms'), (r'(ו|ב|ל|כ)?(עשרון|עשרן|עשרנים)', 'the unit noun tenth'), (r'(ו|ב|ל|כ|מ)?(חצי|מחצית|מחצת)', 'the half forms')):
    S = seats(pat)
    print('\n-- %s: %d tokens; next words: %s' % (lab, len(S), collections.Counter(s[7] for s in S).most_common(12)))
    for b, c, v, i, xp, m, prev, nxt in S:
        if b in T: print('     %s %d:%d  [%s] %s [%s] %s  parse %s' % (b, c, v, prev, xp, nxt, m, N(b, c, v)))

print('\n==== (2c) THE DEFINITE ONE — every Torah seat, with the word before it ====')
S = seats(r'(ו|ב|ל|כ)?האח[דת]')
tor = [s for s in S if s[0] in T]
print('  Torah tokens %d in %d verses; the word before: %s' % (len(tor), len({(s[0], s[1], s[2]) for s in tor}), collections.Counter(s[6] for s in tor).most_common(25)))
for b, c, v, i, xp, m, prev, nxt in tor:
    print('     %s %d:%d  [%s] %s [%s]  parse %s' % (b, c, v, prev, xp, nxt, N(b, c, v)))

print('\n==== (2d) THE THIRD-GENERATION HOMOGRAPH (שלשים read as thirty) and SHESHAI as the ordinal ====')
for b, c, v in (('Exod', 20, 5), ('Exod', 34, 7), ('Num', 14, 18), ('Deut', 5, 9), ('Gen', 50, 23), ('Num', 13, 22), ('Josh', 15, 14), ('Judg', 1, 10)):
    ws = by[(b, c, v)]
    print('  %s %d:%d  numbers %s  ordinals %s   %s' % (b, c, v, N(b, c, v) if b in T else '-', O(b, c, v) if b in T else '-', ' '.join(xp + '/' + m for x, xp, m in ws if re.search(r'שלש|ששי|רבע', x))))

print('\n==== (2e) THE MARKER VERSES that carry a definite one, a fraction form, a tenth or a half (the stitcher\'s rows that would move) ====')
src = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
mk = re.findall(r"assert_ink\('(Gen|Exod|Lev|Num|Deut) (\d+):(\d+)', (\[[^\]]*\])", src)
print('  marker rows', len(mk))
for b, c, v, exp in mk:
    ws = [x for x, _, _ in by[(b, int(c), int(v))]]
    hit = [w for w in ws if re.fullmatch(r'(ו|ב|ל|כ)?(האחד|האחת|רבע|רבעית|רביעת|רביעית|שלשית|שלישת|עשירת|עשירית|עשרון|עשרן|חצי|מחצית|שלשים)', w)]
    if hit: print('    %s %s:%s  expected %s  now %s  tokens %s' % (b, c, v, exp, N(b, int(c), int(v)), hit))
print('  Exod 12:29 words:', ' '.join(x for x, _, _ in by[('Exod', 12, 29)]))
