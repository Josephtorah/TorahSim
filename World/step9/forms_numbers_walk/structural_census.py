#!/usr/bin/env python3
# THE STRUCTURAL CENSUS — a MEASUREMENT for the open discussion (the state doc's #135), 2026-09-11. NO BUILD, NO RECORD: the print is the
# deliverable. Every seat of the register's key words and every declared total with its parts, Genesis 1 -> Numbers 26 on the Tanakh DB
# (lemma = Strong's number with prefix components), the numerals by the step-9 parser (cold_run_sequence.ink_numbers).
import sqlite3, sys, io, re, contextlib, collections
ROOT = '<repo-old>'
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
db = sqlite3.connect(f'file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
TORAH = ['Gen', 'Exod', 'Lev', 'Num', 'Deut']
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.idx, w.he, w.lemma, w.morph FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book IN ('Gen','Exod','Lev','Num','Deut') ORDER BY v.id, w.idx").fetchall()
def base(lemma):
    last = lemma.split('/')[-1]
    return last.split(' ')[0]
V0 = {}
for b, c, v, i, he, lm, m in rows:
    V0.setdefault((b, c, v), []).append((plain(he), base(lm), lm, m))
V = collections.OrderedDict((k, V0[k]) for k in sorted(V0, key=lambda k: (TORAH.index(k[0]), k[1], k[2])))   # the DB's ids are alphabetical by book
KEY = collections.OrderedDict([
    ('family (mishpachah) 4940', '4940'), ('name (shem) 8034', '8034'), ('number (mispar) 4557', '4557'), ('count / the counted (paqad) 6485', '6485'),
    ('generations (toledot) 8435', '8435'), ('kind (min) 4327', '4327'), ('male (zakhar) 2145', '2145'), ('female (neqevah) 5347', '5347'),
    ('poll / skull (gulgolet) 1538', '1538'), ('tribe (matteh) 4294', '4294'), ('tribe (shevet) 7626', '7626'), ('host (tzava) 6635', '6635'),
    ('tongue (lashon) 3956', '3956'), ('nation (goy) 1471', '1471'), ('clean (tahor) 2889', '2889'), ('beget (yalad) 3205', '3205'),
])
INSIDE = lambda b, c: (TORAH.index(b), c) <= (3, 26)   # Genesis 1 -> Numbers 26
REGS = collections.OrderedDict([
    ('Gen 5 the book of Adam', ('Gen', 5, 1, 32)), ('Gen 6:9-7:24 the ark boarded', ('Gen', 6, 9, 7, 24)), ('Gen 8:1-9:17 the exit and the covenant', ('Gen', 8, 1, 9, 17)),
    ('Gen 10 the nations', ('Gen', 10, 1, 32)), ('Gen 11:10-32 Shem to Terah', ('Gen', 11, 10, 32)), ('Gen 25:12-18 Ishmael', ('Gen', 25, 12, 18)),
    ('Gen 36 Esau', ('Gen', 36, 1, 43)), ('Gen 46:8-27 the descent', ('Gen', 46, 8, 27)), ('Exod 1:1-7 the names', ('Exod', 1, 1, 7)),
    ('Exod 6:14-27 the heads of houses', ('Exod', 6, 14, 27)), ('Exod 38:24-31 the shekel account', ('Exod', 38, 24, 31)),
    ('Num 1 the first census', ('Num', 1, 1, 54)), ('Num 2 the camps', ('Num', 2, 1, 34)), ('Num 3 the Levites and the firstborn', ('Num', 3, 1, 51)),
    ('Num 4 the service roll', ('Num', 4, 1, 49)), ('Num 7 the princes', ('Num', 7, 1, 89)), ('Num 26 the second census', ('Num', 26, 1, 65)),
])
def span(key):
    r = REGS[key]
    if len(r) == 4: return [(r[0], r[1], v) for v in range(r[2], r[3] + 1)]
    b, c1, v1, c2, v2 = r
    return [k for k in V if k[0] == b and ((k[1] == c1 and k[2] >= v1) or (k[1] == c2 and k[2] <= v2) or (c1 < k[1] < c2))]

print('==== A. THE KEY WORDS\' SEATS — tokens per book (the Torah whole; the column "to Num 26" = Genesis 1 through Numbers 26), the FIRST seat, and the chapters with 5+ tokens ====')
for label, lm in KEY.items():
    perbook = collections.Counter(); perch = collections.Counter(); first = None; inside = 0
    for (b, c, v), ws in V.items():
        n = sum(1 for _, bl, _, _ in ws if bl == lm)
        if n:
            perbook[b] += n; perch[(b, c)] += n
            if INSIDE(b, c): inside += n
            if first is None: first = (b, c, v, ' '.join(w for w, bl, _, _ in ws if bl == lm))
    dense = sorted(((k, n) for k, n in perch.items() if n >= 5), key=lambda kv: (TORAH.index(kv[0][0]), kv[0][1]))
    print('  %-38s Torah %4d  to-Num-26 %4d  by book %s\n      first %s %d:%d %s\n      dense %s' % (label, sum(perbook.values()), inside, dict(perbook), first[0], first[1], first[2], first[3], ' '.join('%s%d:%d' % (k[0], k[1], n) for k, n in dense)))

print('\n==== B. THE HEADING FORMULAS — a verse-initial "these are" (eleh, 428) and the noun it heads, the Torah whole ====')
HEAD = collections.defaultdict(list)
for (b, c, v), ws in V.items():
    if ws and ws[0][1] == '428' and len(ws) > 1:
        HEAD[(ws[1][1], ws[1][0])].append('%s %d:%d' % (b, c, v))
for (lm, he), seats in sorted(HEAD.items(), key=lambda kv: -len(kv[1])):
    print('  these are + %-6s %-14s x%-3d %s' % (lm, he, len(seats), ' '.join(seats)))

print('\n==== C. THE COLUMN MATRIX — per register, the column words the ink writes inside its span (token counts) ====')
COLS = collections.OrderedDict([('family', '4940'), ('fathers\' house', 'BEIT_AV'), ('number', '4557'), ('names', '8034'), ('the counted', '6485'), ('generations', '8435'), ('kind', '4327'), ('male', '2145'), ('female', '5347'), ('poll', '1538'), ('tribe', '4294'), ('host', '6635'), ('tongue', '3956'), ('land', '776'), ('nation', '1471'), ('clean', '2889'), ('sons', '1121'), ('begot', '3205'), ('years', '8141'), ('died', '4191'), ('firstborn', '1060'), ('head', '7218'), ('lot', '1486'), ('inheritance', '5159')])
def count_cols(keys):
    out = collections.Counter()
    for k in keys:
        ws = V[k]
        for i, (w, bl, lm, m) in enumerate(ws):
            for name, code in COLS.items():
                if code == 'BEIT_AV':
                    if bl == '1004' and i + 1 < len(ws) and ws[i + 1][1] == '1': out[name] += 1
                elif bl == code: out[name] += 1
    return out
hdr = '%-40s' % 'register' + ''.join('%6s' % n[:5] for n in COLS)
print('  ' + hdr)
for key in REGS:
    cnt = count_cols(span(key))
    print('  %-40s' % key + ''.join('%6s' % (cnt[n] or '.') for n in COLS))

print('\n==== D. THE DECLARED TOTALS WITH THEIR PARTS — the parser at each seat; the sum checked by script ====')
def show(label, parts, total, factor=None):
    ps = [(ref, N(*ref)) for ref in parts]
    tv = N(*total)
    s = sum(x[1][0] for x in ps if x[1])
    verdict = 'MATCH' if tv and s == tv[0] else ('DECLARED-DIFFERS' if tv else 'no-total-read')
    print('  %-46s parts %s -> sum %d ; total %s %s : %s' % (label, [x[1] for x in ps], s, '%s %d:%d' % total, tv, verdict))
    return s, tv
# Gen 5 per row: the years of begetting + the years after = the total years (three numbers on three verses per patriarch)
print('-- Gen 5, the book of Adam: per row (begot at, after, total)')
GEN5 = [('Adam', 3, 4, 5), ('Seth', 6, 7, 8), ('Enosh', 9, 10, 11), ('Kenan', 12, 13, 14), ('Mahalalel', 15, 16, 17), ('Jared', 18, 19, 20), ('Enoch', 21, 22, 23), ('Methuselah', 25, 26, 27), ('Lamech', 28, 30, 31)]
for name, a, b_, t in GEN5:
    A, B, T = N('Gen', 5, a), N('Gen', 5, b_), N('Gen', 5, t)
    print('  %-11s 5:%-2d %-6s 5:%-2d %-6s 5:%-2d %-6s  %s' % (name, a, A, b_, B, t, T, 'MATCH' if A and B and T and A[0] + B[0] == T[0] else 'CHECK'))
print('  Noah 5:32 %s ; 9:28 %s ; 9:29 %s -> %s' % (N('Gen', 5, 32), N('Gen', 9, 28), N('Gen', 9, 29), 'MATCH' if N('Gen', 9, 28)[0] + 600 == N('Gen', 9, 29)[0] else 'CHECK'))
print('-- Gen 11:10-26, Shem to Terah: begot-at and after, NO total written per row (the parser at the seats):')
for v in range(10, 27): print('     11:%-2d %s' % (v, N('Gen', 11, v)))
print('-- the ark: 6:15 %s (300 x 50 x 30); 7:2 %s ; 7:3 %s ; 7:4 %s ; 7:6 %s ; 7:11 %s ; 7:24 %s ; 8:3-4 %s %s' % (N('Gen', 6, 15), N('Gen', 7, 2), N('Gen', 7, 3), N('Gen', 7, 4), N('Gen', 7, 6), N('Gen', 7, 11), N('Gen', 7, 24), N('Gen', 8, 3), N('Gen', 8, 4)))
print('-- Gen 46, the descent: the four registers and the two totals')
show('Gen 46 the four sub-totals -> 66 (46:26)', [('Gen', 46, 15), ('Gen', 46, 18), ('Gen', 46, 22), ('Gen', 46, 25)], ('Gen', 46, 26))
print('     46:27 %s ; Exod 1:5 %s ; Deut 10:22 %s' % (N('Gen', 46, 27), N('Exod', 1, 5), N('Deut', 10, 22)))
print('-- Exod 38:25-28 the shekel account: 38:25 %s ; 38:26 %s ; 38:27 %s ; 38:28 %s  (100 talents x 3,000 + 1,775 = %d shekels = %d half-shekels = 603,550 ? %s)' % (N('Exod', 38, 25), N('Exod', 38, 26), N('Exod', 38, 27), N('Exod', 38, 28), 100 * 3000 + 1775, 2 * (100 * 3000 + 1775), 2 * (100 * 3000 + 1775) == 603550))
print('-- Num 1 the first census')
show('Num 1 the twelve -> 1:46', [('Num', 1, v) for v in (21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43)], ('Num', 1, 46))
print('-- Num 2 the camps: each camp\'s three -> its sum; the four sums -> 2:32')
show('Num 2 east (Judah, Issachar, Zebulun) -> 2:9', [('Num', 2, 4), ('Num', 2, 6), ('Num', 2, 8)], ('Num', 2, 9))
show('Num 2 south (Reuben, Simeon, Gad) -> 2:16', [('Num', 2, 11), ('Num', 2, 13), ('Num', 2, 15)], ('Num', 2, 16))
show('Num 2 west (Ephraim, Manasseh, Benjamin) -> 2:24', [('Num', 2, 19), ('Num', 2, 21), ('Num', 2, 23)], ('Num', 2, 24))
show('Num 2 north (Dan, Asher, Naphtali) -> 2:31', [('Num', 2, 26), ('Num', 2, 28), ('Num', 2, 30)], ('Num', 2, 31))
show('Num 2 the four camps -> 2:32', [('Num', 2, 9), ('Num', 2, 16), ('Num', 2, 24), ('Num', 2, 31)], ('Num', 2, 32))
print('-- Num 3 the Levites and the firstborn')
show('Num 3 the three houses -> 3:39', [('Num', 3, 22), ('Num', 3, 28), ('Num', 3, 34)], ('Num', 3, 39))
print('     the firstborn 3:43 %s ; the surplus 3:46 %s (= 22,273 - 22,000 ? %s) ; the price 3:47 %s ; the redemption 3:50 %s (= 273 x 5 ? %s)' % (N('Num', 3, 43), N('Num', 3, 46), N('Num', 3, 43)[0] - 22000 == 273, N('Num', 3, 47), N('Num', 3, 50), N('Num', 3, 50)[0] == 273 * 5))
print('-- Num 4 the service roll')
show('Num 4 the three houses (30-50) -> 4:48', [('Num', 4, 36), ('Num', 4, 40), ('Num', 4, 44)], ('Num', 4, 48))
print('-- Num 7 the princes\' gifts: one prince\'s row (7:13-17) and the totals (7:84-88)')
print('     7:13 %s 7:14 %s 7:15 %s 7:16 %s 7:17 %s' % (N('Num', 7, 13), N('Num', 7, 14), N('Num', 7, 15), N('Num', 7, 16), N('Num', 7, 17)))
print('     7:84 %s 7:85 %s 7:86 %s 7:87 %s 7:88 %s' % (N('Num', 7, 84), N('Num', 7, 85), N('Num', 7, 86), N('Num', 7, 87), N('Num', 7, 88)))
print('     12 x (130 + 70) = %d ; 12 x 10 = %d ; 12 x (1, 1, 1) ; 12 x (2, 5, 5, 5) = (%d, %d, %d, %d)' % (12 * 200, 12 * 10, 24, 60, 60, 60))
print('-- Num 26 the second census')
show('Num 26 the twelve -> 26:51', [('Num', 26, v) for v in (7, 14, 18, 22, 25, 27, 34, 37, 41, 43, 47, 50)], ('Num', 26, 51))
print('     the Levites 26:62 %s against 3:39 %s' % (N('Num', 26, 62), N('Num', 3, 39)))
print('-- beyond the range, the same form once more: Num 31:32-47 the booty and its halves (marked OUTSIDE the discussion\'s range)')
print('     31:32 %s 31:33 %s 31:34 %s 31:35 %s | halves 31:36 %s 31:37 %s 31:38 %s 31:39 %s 31:40 %s | 31:43 %s 31:44 %s 31:45 %s 31:46 %s' % tuple(N('Num', 31, v) for v in (32, 33, 34, 35, 36, 37, 38, 39, 40, 43, 44, 45, 46)))

print('\n==== E. THE MEMBERSHIP MARKERS — the predicate phrases that fix a roster AS OF an event (the Torah whole) ====')
def phrase(lm_a, lm_b, within=4):
    out = []
    for (b, c, v), ws in V.items():
        for i, (w, bl, lm, m) in enumerate(ws):
            if bl == lm_a:
                for j in range(i + 1, min(len(ws), i + 1 + within)):
                    if ws[j][1] == lm_b:
                        out.append('%s %d:%d' % (b, c, v)); break
    return out
print('  "went out" (3318) ... "the ark" (8392): %s' % phrase('3318', '8392'))
print('  "came" (935) ... "Egypt" (4714) [the Torah whole]: %d seats; in Gen 46-Exod 1: %s' % (len(phrase('935', '4714')), [s for s in phrase('935', '4714') if s.startswith('Gen 46') or s.startswith('Exod 1:')]))
print('  "went out" (3318) ... "Egypt" (4714) [the Torah whole]: %d seats; in Num 1-26: %s' % (len(phrase('3318', '4714')), [s for s in phrase('3318', '4714') if s.startswith('Num ') and int(s.split()[1].split(':')[0]) <= 26]))
print('  "the counted" (6485) ... "Sinai" (5514): %s' % phrase('6485', '5514', 6))
print('  "the number of names" (4557 then 8034 adjacent): %s' % phrase('4557', '8034', 1))
print('  "fathers\' house" (1004 then 1 adjacent), the Torah whole: %d seats; by book %s; first %s' % (len(phrase('1004', '1', 1)), dict(collections.Counter(s.split()[0] for s in phrase('1004', '1', 1))), phrase('1004', '1', 1)[:1]))
print('  "lift the head" (5375 then 7218 within 2): %s' % phrase('5375', '7218', 2))
print('  "after its kind" (4327 with the prefix l), the Torah whole: %s' % [('%s %d:%d' % k) for k, ws in V.items() for w, bl, lm, m in ws if bl == '4327' and lm.startswith('l/')][:40])
print('  "by their families" — the family lemma with a plural possessive (Ncfpc/Sp3mp), the Torah whole: %d seats; by book %s' % (len([1 for k, ws in V.items() for w, bl, lm, m in ws if bl == '4940' and 'Ncfpc/Sp3' in m]), dict(collections.Counter(k[0] for k, ws in V.items() for w, bl, lm, m in ws if bl == '4940' and 'Ncfpc/Sp3' in m))))
print('  the family lemma\'s seats by chapter, Genesis 1 -> Numbers 26 (chapter: tokens): %s' % ' '.join('%s%d:%d' % (k[0], k[1], n) for k, n in sorted(collections.Counter((k[0], k[1]) for k, ws in V.items() for w, bl, lm, m in ws if bl == '4940' and INSIDE(k[0], k[1])).items(), key=lambda kv: (TORAH.index(kv[0][0]), kv[0][1]))))

print('\n==== F. THE FOUR STRUCTURAL MARKS PER REGISTER (computed from the seats above): a HEADING formula inside the span; the FAMILY key; a DECLARED TOTAL checked; a MEMBERSHIP predicate ====')
TOTALS = {'Gen 5 the book of Adam': 'per-row 9/9 MATCH (begot + after = total)', 'Gen 46:8-27 the descent': '33+16+14+7 = 70 against 66 (46:26) and 70 (46:27): the ink states both', 'Exod 38:24-31 the shekel account': '100 talents + 1,775 = 603,550 halves MATCH', 'Num 1 the first census': '12 -> 603,550 MATCH', 'Num 2 the camps': '3x4 -> 4 -> 603,550 MATCH', 'Num 3 the Levites and the firstborn': '7,500+8,600+6,200 = 22,300 against 22,000 (3:39); 22,273-22,000 = 273; 273x5 = 1,365 MATCH', 'Num 4 the service roll': '3 -> 8,580 MATCH', 'Num 7 the princes': '12 x one row = 7:84-88 MATCH', 'Num 26 the second census': '12 -> 601,730 MATCH'}
def inside_span(seats, keys):
    ks = set('%s %d:%d' % k for k in keys)
    return [x for x in seats if x in ks]
allhead = [x for seats in HEAD.values() for x in seats]
members = phrase('3318', '8392') + phrase('935', '4714') + phrase('3318', '4714') + phrase('6485', '5514', 6)
for key in REGS:
    keys = span(key); cnt = count_cols(keys)
    print('  %-40s heading %-3d %-42s family %-3s total %-52s membership %s' % (key, len(inside_span(allhead, keys)), ' '.join(inside_span(allhead, keys))[:42], cnt['family'] or '.', TOTALS.get(key, 'none written'), ' '.join(inside_span(members, keys)) or '.'))
