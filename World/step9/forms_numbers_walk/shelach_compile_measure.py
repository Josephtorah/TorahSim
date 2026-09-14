#!/usr/bin/env python3
# THE NUMBERS WALK sitting 4b — THE COMPILE OF SHELACH (2026-09-10; the owner: "Go"): THE MEASUREMENTS, computed BEFORE the design
# paragraph is typed (1b's order). (1) the parser's state at the portion's seats after 3b's rules; (2) THE FRACTION CLASS censused on the
# whole Tanakh DB — the quarter, the third, the half, the unit noun "a tenth", the definite "the one" — every form with its seats and the
# parser's current reading there; (3) the calendar's arithmetic for the forty days and the thirty-eight years; (4) the callees on file;
# (5) the tape's subjects; (6) the register verses of chapters 13-14 against the planned lines; (7) the trials on the tape.
import sqlite3, sys, io, re, contextlib, collections, unicodedata
ROOT = '<repo-old>'
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import world_engine as WE
    import cold_run_bamidbar as BM
    import cold_run_chatat as CH
    import cold_run_minchah as MN
    import cold_run_offerings as OF
    import cold_run_moadim as MO
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
db = sqlite3.connect(f'file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by = {}
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((plain(he), pointed(he), m))
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
print('==== (1) THE PARSER AT THE PORTION\'S SEATS (13:1-15:31) ====')
for c, lo, hi in ((13, 1, 33), (14, 1, 45), (15, 1, 31)):
    for v in range(lo, hi + 1):
        ws = [x for x, _, _ in by[('Num', c, v)]]
        n = N('Num', c, v)
        numy = [w for w in ws if re.search(r'(אחד|אחת|שנים|שתים|שלש|ארבע|חמש|שש|שבע|שמנ|תשע|עשר|מאה|מאת|אלף|רבע|רביע|שליש|חצי|עשרן|עשרון)', w)]
        if n or numy:
            print('  Num %d:%d  parse %s   tokens %s' % (c, v, n, ' '.join(numy)))

print('\n==== (2) THE FRACTION CLASS ON THE TANAKH DB ====')
def census(pattern, label, exclude=None):
    forms = collections.Counter(); seats = collections.defaultdict(list)
    for (b, c, v), ws in by.items():
        for i, (x, xp, m) in enumerate(ws):
            if re.search(pattern, x) and not (exclude and re.search(exclude, x)):
                forms[x] += 1; seats[x].append((b, c, v, i, xp, m, ws[i - 1][0] if i else '', ws[i + 1][0] if i + 1 < len(ws) else ''))
    print('\n-- %s: %d forms, %d tokens' % (label, len(forms), sum(forms.values())))
    for f, n in forms.most_common():
        S = seats[f]
        tor = [s for s in S if s[0] in T]
        print('   %-12s %3d  (Torah %d)  morph %s' % (f, n, len(tor), collections.Counter(s[5] for s in S).most_common(2)))
        for b, c, v, i, xp, m, prev, nxt in S[:14] if n > 14 else S:
            print('        %s %d:%d  [%s] %s [%s]  parse %s' % (b, c, v, prev, xp, nxt, N(b, c, v) if b in T else '-'))
    return forms, seats
Q = census(r'רבע|רביע', 'THE QUARTER (רבע / רביע)', exclude=r'ארבע|רבעים$|רביעי|תרבע|תרביע|לרבעה|רבצ')
TH = census(r'שליש|שלשית|שלשת$', 'THE THIRD (שליש / שלשית)', exclude=r'שלישי$|שלישים|שלשים')
HF = census(r'חצי|מחצ|חצית|חצות', 'THE HALF (חצי / מחצית)', exclude=r'חצר|חצצר|חצב|חצן')
TN = census(r'עשרן|עשרון|עשירת|עשירית', 'THE TENTH (עשרון / עשירית)')
DO = census(r'^(ו|ל|ב|כ)?האח[דת]$', 'THE DEFINITE ONE (האחד / האחת)')

print('\n==== (3) THE CALENDAR ====')
w = WE.World(era='measure', epoch='exodus')
ex = w.clock.eras['exodus']
d0 = w.clock.day_in('exodus', 2, 3, 29)
print('  the sending day (2, 3, 29) = day', d0, ex.date(d0))
for n in (39, 40, 41):
    print('  +%d days -> %s' % (n, ex.date(d0 + n)))
d9 = w.clock.day_in('exodus', 2, 5, 9)
print('  the ninth of Av (2, 5, 9) = day', d9, 'delta from the sending', d9 - d0)
cal = w.clock.calendar
for m in (3, 4, 5):
    for start, y, mm, ln in cal._months:
        if y == 2 and mm == m: print('  year 2 month %d length %d' % (m, ln))
print('  Sivan 30 / Tammuz / Av of year 2:', [ex.date(w.clock.day_in('exodus', 2, m, 30)) for m in (3, 4, 5)])
d38 = cal.add(d9, 38, 'year'); d40 = cal.add(d9, 40, 'year')
print('  +38 years from the decree (2, 5, 9) ->', ex.date(d38), 'day', d38, '; +40 years ->', ex.date(d40))
dd = w.clock.day_in('exodus', 40, 5, 1)
print('  the daughters\' marker (40, 5, 1) = day', dd, '; the decree\'s due after it by', d38 - dd, 'days')
print('  the year at the decree:', ex.year(d9), '; 40 - 38 =', 40 - 38)
print('  (40, 5, 15) the fifteenth of Av =', w.clock.day_in('exodus', 40, 5, 15) - d38, 'days after the due')
print('  Deut 1:3 (40, 11, 1) =', ex.date(w.clock.day_in('exodus', 40, 11, 1)), 'day', w.clock.day_in('exodus', 40, 11, 1))
print('  the exodus epoch day 1 date', ex.date(w.clock.day_in('exodus', 1, 1, 1)), '; forty years from the epoch (41, 1, 1) ->', ex.date(w.clock.day_in('exodus', 41, 1, 1)))

print('\n==== (4) THE CALLEES ON FILE ====')
print('  bamidbar.census total ->', BM.census({'ask': 'total'}, BM.DATA)['v'] if isinstance(BM.census({'ask': 'total'}, BM.DATA), dict) else BM.census({'ask': 'total'}, BM.DATA))
print('  chatat.rank(congregation, idolatry) ->', CH.rank('congregation', sin='idolatry')['v'], '| rank(commoner, idolatry) ->', CH.rank('commoner', sin='idolatry')['v'], '| rank(anointed, idolatry) ->', CH.rank('anointed', sin='idolatry')['v'])
print('  chatat.domain(intentional) ->', CH.domain({'intent': 'intentional'})['v'], CH.domain({'intent': 'intentional'})['fx'])
print('  chatat.domain(unwitting) ->', CH.domain({'intent': 'unwitting'})['v'])
print('  chatat.domain(karet_when_intentional=False) ->', CH.domain({'karet_when_intentional': False})['v'])
print('  minchah.adjuncts(libation) ->', MN.adjuncts('libation')['v'] if isinstance(MN.adjuncts('libation'), dict) else MN.adjuncts('libation'))
print('  moadim omer libation cell exists:', 'quarter_hin' in open(f'{ROOT}/World/step9/cold_run_moadim.py', encoding='utf-8').read())
print('  offerings.dispatch signature:', OF.dispatch.__doc__.split('\n')[0][:200] if OF.dispatch.__doc__ else '(no doc)')
import inspect
print('  offerings.dispatch args:', inspect.signature(OF.dispatch))
print('  chatat.court args:', inspect.signature(CH.court), '| chatat.tribes:', inspect.signature(CH.tribes))
try:
    print('  chatat.court(idolatry, tribes=...) ->', CH.court({'sin': 'idolatry', 'erred': 'court', 'majority_acted': True})['v'])
except Exception as e:
    print('  chatat.court probe raised', type(e).__name__, e)

print('\n==== (5) THE TAPE\'S SUBJECTS (cold_run_sequence.py) ====')
src = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
for s in ('caleb', 'joshua', 'yehoshua', 'the-spies', 'the-twelve-spies', 'the-ten-spies', 'the-tent-of-meeting', 'amalek', 'israel', 'moses', 'aaron', 'the-land-of-canaan'):
    print('  %-20s subject lines %2d   as a token %3d' % (s, src.count("'subject': '%s'" % s), src.count("'%s'" % s)))
print('  murmured lines on the tape:', src.count("'kind': 'murmured'"))

print('\n==== (6) THE REGISTER OF CHAPTERS 13-14 (V.w — the narrative verb) ====')
reg = {}
for (b, c, v), ws in by.items():
    if b == 'Num' and c in (13, 14):
        reg[(c, v)] = [x for x, _, m in ws if m and m.startswith('V.w')]
LINES = [('spies_commanded', 13, 1, 2), ('spies_sent', 13, 3, 16), ('spies_instructed', 13, 17, 20), ('spies_went_up', 13, 21, 24), ('spies_returned', 13, 25, 26),
         ('report_given', 13, 27, 29), ('caleb_hushed_the_people', 13, 30, 30), ('evil_report_spread', 13, 31, 33), ('congregation_wept', 14, 1, 4),
         ('joshua_and_caleb_pleaded', 14, 5, 9), ('glory_appeared_at_the_threat', 14, 10, 10), ('moses_pleaded_on_the_attributes', 14, 11, 19),
         ('pardoned_and_decreed', 14, 20, 25), ('decree_declared', 14, 26, 35), ('ten_spies_died_by_plague', 14, 36, 38), ('presumed_to_go_up', 14, 39, 44), ('smitten_to_hormah', 14, 45, 45)]
regv = sorted(k for k, vv in reg.items() if vv)
print('  register verses: ch13 %d, ch14 %d, total %d' % (sum(1 for c, v in regv if c == 13), sum(1 for c, v in regv if c == 14), len(regv)))
for name, c, lo, hi in LINES:
    vv = [(v, reg[(c, v)]) for v in range(lo, hi + 1) if reg[(c, v)]]
    print('  %-32s %d:%d-%d  register verses %d  %s' % (name, c, lo, hi, len(vv), ' '.join('%d:%s' % (v, ','.join(x)) for v, x in vv)[:150]))
covered = {(c, v) for _, c, lo, hi in LINES for v in range(lo, hi + 1)}
print('  every verse of 13-14 in a line:', covered == {(c, v) for c in (13, 14) for v in range(1, (34 if c == 13 else 46))}, '; uncovered register verses:', [k for k in regv if k not in covered])
