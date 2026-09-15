import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE ARCHITECTURE CENSUS — a second MEASUREMENT for the open discussion (2026-09-11). NO BUILD, NO RECORD. Three questions on the ink:
# (a) does each "these are ..." formula OPEN a register (no numeral, a list follows) or CLOSE one (a numeral on the line: the checksum)?
# (b) how are the LAW blocks headed and closed — the speech formula "and the LORD spoke to Moses saying" and the footers "these are the
#     statutes / commandments"; (c) the date rows — the ink's own timestamps (the year-month-day formula) and where they sit.
import sqlite3, sys, io, contextlib, collections
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
TORAH = ['Gen', 'Exod', 'Lev', 'Num', 'Deut']
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.idx, w.he, w.lemma, w.morph FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book IN ('Gen','Exod','Lev','Num','Deut') ORDER BY v.id, w.idx").fetchall()
def base(lemma): return lemma.split('/')[-1].split(' ')[0]
V0 = {}
for b, c, v, i, he, lm, m in rows: V0.setdefault((b, c, v), []).append((plain(he), base(lm), lm, m))
KEYS = sorted(V0, key=lambda k: (TORAH.index(k[0]), k[1], k[2]))
V = collections.OrderedDict((k, V0[k]) for k in KEYS)
POS = {k: i for i, k in enumerate(KEYS)}
GLOSS = {'8435': 'generations', '8034': 'names', '1121': 'sons', '4940': 'families', '6485': 'the counted', '2706': 'statutes', '4687': 'commandments', '4941': 'judgments', '1697': 'words', '4550': 'journeys', '4150': 'appointed times', '7218': 'heads', '441': 'chiefs', '4428': 'kings', '3117': 'days', '8141': 'years', '5713': 'testimonies'}

print('==== (a) OPEN OR CLOSE — every verse-initial "these are" in the Torah, with the numerals on its own line and on the line before; a numeral on the line = a CLOSE (the checksum); none = an OPEN (the header) ====')
tally = collections.Counter()
for k in KEYS:
    ws = V[k]
    if ws and ws[0][1] == '428' and len(ws) > 1:
        noun = ws[1][1]; here = N(*k); prev = KEYS[POS[k] - 1]; before = N(*prev)
        kind = 'CLOSE' if here else 'OPEN'
        tally[(GLOSS.get(noun, noun), kind)] += 1
        print('  %-11s these are + %-16s %-5s numerals here %-24s before %s' % ('%s %d:%d' % k, GLOSS.get(noun, noun) + ' ' + ws[1][0], kind, here, before))
print('  -- tally by noun: %s' % {('%s' % n): '%d open / %d close' % (tally[(n, 'OPEN')], tally[(n, 'CLOSE')]) for n in sorted(set(n for n, _ in tally))})

print('\n==== (b) THE LAW BLOCKS — the speech formula "and the LORD spoke to Moses saying" (dabar 1696 + YHWH 3068 + Moses 4872 + le\'mor 559 on one line) per book and per chapter; the footers "these are the statutes / commandments / judgments" ====')
SPEAK = []
for k in KEYS:
    bl = [x[1] for x in V[k]]
    if bl[:1] == ['1696'] and '3068' in bl[:3] and '4872' in bl[:6] and '559' in bl[:8]: SPEAK.append(k)
print('  the formula at the head of a verse: %d seats; by book %s' % (len(SPEAK), dict(collections.Counter(k[0] for k in SPEAK))))
byc = collections.Counter((k[0], k[1]) for k in SPEAK)
print('  chapters by count of the formula (the densest twenty): %s' % ' '.join('%s%d:%d' % (b, c, n) for (b, c), n in sorted(byc.items(), key=lambda kv: -kv[1])[:20]))
# the variant "and the LORD said to Moses" (amar 559 at the head)
SAID = [k for k in KEYS if [x[1] for x in V[k]][:1] == ['559'] and '3068' in [x[1] for x in V[k]][:3] and '4872' in [x[1] for x in V[k]][:6]]
print('  the variant "and the LORD said to Moses" at the head: %d seats; by book %s' % (len(SAID), dict(collections.Counter(k[0] for k in SAID))))
FOOT = [k for k in KEYS if V[k][0][1] == '428' and len(V[k]) > 1 and V[k][1][1] in ('2706', '4687', '4941', '1697', '5713')]
for k in FOOT: print('  footer/header %-11s %s' % ('%s %d:%d' % k, ' '.join(w for w, _, _, _ in V[k])[:110]))
# the place-and-time stamp on a law block: "in Mount Sinai" (2022 + 5514) and "in the plains of Moab" (6160 + 4124) on the same line as a footer or the speech formula
def has(k, a, b_, within=3):
    bl = [x[1] for x in V[k]]
    return any(bl[i] == a and b_ in bl[i + 1:i + 1 + within] for i in range(len(bl)))
print('  "in Mount Sinai" on a speech-formula or footer line: %s' % ['%s %d:%d' % k for k in SPEAK + FOOT if has(k, '2022', '5514')])
print('  "in the plains of Moab" on a speech-formula or footer line: %s' % ['%s %d:%d' % k for k in SPEAK + FOOT if has(k, '6160', '4124')])
print('  "in the tent of meeting" (168 + 4150) on a speech-formula line: %s' % ['%s %d:%d' % k for k in SPEAK if has(k, '168', '4150')])

print('\n==== (c) THE DATE ROWS — the ink\'s own timestamps: a verse carrying "year" (8141) AND "month" (2320) AND "day" (3117) — the tape\'s markers are these lines ====')
DATES = [k for k in KEYS if {'8141', '2320', '3117'} <= set(x[1] for x in V[k])]
print('  %d lines; by book %s' % (len(DATES), dict(collections.Counter(k[0] for k in DATES))))
for k in DATES: print('  %-11s ordinals %-14s numbers %-14s %s' % ('%s %d:%d' % k, O(*k), N(*k), ' '.join(w for w, _, _, _ in V[k])[:90]))
DM = [k for k in KEYS if {'2320', '3117'} <= set(x[1] for x in V[k]) and '8141' not in set(x[1] for x in V[k]) and (N(*k) or O(*k))]
print('  month-and-day lines without a year (the calendar\'s fixed dates): %d; by book %s' % (len(DM), dict(collections.Counter(k[0] for k in DM))))

print('\n==== (d) THE CASE FORM — a question brought and answered: "and Moses brought their cause before the LORD" (7126/5066 + 4941 + 6440 + 3068) and "and the LORD said/spoke to Moses" following ====')
CASE = [k for k in KEYS if any(x[1] == '4941' for x in V[k]) and any(x[1] == '6440' for x in V[k]) and any(x[1] == '3068' for x in V[k]) and any(x[1] in ('7126', '5066', '5975') for x in V[k])]
for k in CASE: print('  %-11s %s' % ('%s %d:%d' % k, ' '.join(w for w, _, _, _ in V[k])[:110]))
