import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 11b — THE COMPILE OF CHAPTER 13 (2026-09-21): THE EXAM DOCKET'S SCAN, sized by script before the docket is written
# (ch12_docket_scan.py's form on chapter 13, derived by derive_ch13_docket_scan.py). (1) THE LINK ROWS: every segment of the local shelf's Babylonian
# Talmud, Mishnah and Tosefta exports whose English cites a verse of Deuteronomy 13 (the export's chapter 13 = the DB's 13:1-19 — the identity, asserted at
# the reading; the English numbering's 12:32 is the DB's 13:1 — a citation of 12:32 is FOLDED to 13:1 here, the header); (2) THE TOPIC ROWS by address (the
# union rule; COMPILE_DEBT's sitting-11 box (l)): the CANDIDATE ranges SIZED here, the design choosing which are read whole — Mishnah Sanhedrin 7:10 with
# Sanhedrin 67a (the inciter — the concealed witnesses), 7:6 (the honors of an idol), 10:4-6 with Sanhedrin 111b-113b (the condemned city), 11:1 and 11:5-6 with
# Sanhedrin 89a-90a (the false prophet strangled; the sign), 5:1-2 with Sanhedrin 40a-41a (the seven inquiries and the probes), 1:5 (one city), 11:4 (the
# festival's execution), 4:1 (the verdict returned), Sanhedrin 88b (the rebellious elder and the not-adding); Mishnah Makkot 1:4-6 (the plotting witness);
# Mishnah Zevachim 8:10 with Zevachim 80a-81b (the mixed bloods); Mishnah Sukkah 3:4 with Sukkah 34b and Menachot 41b-42a (the four species; the fringes); Rosh
# Hashanah 28b and Eruvin 96a (the priests' blessing not added to); Mishnah Avodah Zarah 3:9 with Avodah Zarah 49b-50a (the benefit to the Salt Sea); Bava
# Metzia 59b (the prophet's sign not decisive) and Yevamot 90b (the prophet's temporary uprooting); Shabbat 151b (the mercy two-armed); Avot 2:1, 3:9, 3:14;
# Tosefta Sanhedrin 11, 12 and 14, Tosefta Zevachim 8, Tosefta Bava Kamma 9 and the Sifrei on Numbers 103, 113, 114 whole; (3) THE PRIOR READS credited (the
# earlier dockets' and ledgers' rows).
import json, re, os, collections, glob, subprocess
ROOT = _ROOT   # RUN FROM THE REPO ROOT
R = ROOT + '/Data/sefaria_export'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{SCR}/ch13_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
CITE = re.compile(r'(?:Deuteronomy|Deut\.?|Dt\.?) ?(\d+):(\d+)(?:[-–](\d+))?')
CH, NV = 13, 19

def addr(work, cats, path):
    if 'Talmud' in cats and 'Bavli' in cats and len(path) >= 2:
        i = path[0]; return '%s %d%s:%d' % (work.replace('_', ' '), i // 2 + 1, 'ab'[i % 2], path[1] + 1)
    return '%s %s' % (work.replace('_', ' '), ':'.join(str(x + 1) for x in path))

def walk(x, path):
    if isinstance(x, list):
        for i, v in enumerate(x): yield from walk(v, path + [i])
    elif isinstance(x, str):
        yield path, x

link = []
works = collections.Counter()
scanned = 0
cited = collections.Counter()
for w in sorted(os.listdir(R)):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p): continue
    try:
        d = json.load(open(p, encoding='utf-8'))
    except Exception:
        continue
    cats = d.get('categories') or [] if isinstance(d, dict) else []
    if not cats or cats[0] not in ('Talmud', 'Mishnah', 'Tosefta') or 'Yerushalmi' in cats or 'Commentary' in cats or '_on_' in w: continue
    scanned += 1
    for path, s in walk(d['text'], []):
        t = strip(s)
        hits = []
        for m in CITE.finditer(t):
            c, a, z = int(m.group(1)), int(m.group(2)), int(m.group(3) or m.group(2))
            if c == 12 and a == 32: c, a, z = 13, 1, 1   # THE ENGLISH NUMBERING'S 12:32 IS THE DB'S 13:1 (the header) — folded in
            if c != CH: continue
            for v in range(a, min(z, a + 60) + 1):
                if 1 <= v <= NV:
                    hits.append('Deut %d:%d' % (CH, v)); cited[v] += 1
        if hits:
            link.append((addr(w, cats, path), sorted(set(hits), key=lambda s: tuple(int(x) for x in re.findall(r'\d+', s))), t))
            works[w] += 1
print('SCANNED %d works (Talmud / Mishnah / Tosefta, no Yerushalmi, no commentary); the forms: Deuteronomy c:v, Deut. c:v, Dt.c:v; chapter %d only' % (scanned, CH))
print('LINK rows %d in %d works' % (len(link), len(works)))
for w, n in works.most_common(): print('  %-32s %d' % (w, n))
print('  the DB verses cited: %s' % sorted(cited.items()))
print('  the verses NOT cited by anyone: %s' % [v for v in range(1, NV + 1) if v not in cited])
for a, hs, t in link: print('  LINK %-26s %-22s %s' % (a, ' '.join(hs), t[:140].replace('\n', ' ')))

def idx(s):
    m = re.match(r'(\d+)([ab])', s); return (int(m.group(1)) - 1) * 2 + (0 if m.group(2) == 'a' else 1)
topic = []
linked = {a for a, _, _ in link}
SIZES = []
def mishnah_rows(w, refs):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p):
        print('NO SUCH WORK', w); return
    T = json.load(open(p, encoding='utf-8'))['text']
    n = 0; l = 0
    for c, m in refs:
        a = '%s %d:%d' % (w.replace('_', ' '), c, m)
        n += 1
        if a in linked: l += 1; continue
        topic.append((a, strip(T[c - 1][m - 1])))
    print('%s mishnayot %s: %d rows, %d link rows' % (w, refs if len(refs) < 8 else f'{refs[0]}..{refs[-1]} ({len(refs)})', n, l))
    SIZES.append((w, str(refs[0]), str(refs[-1]), n, l))
def mishnah_chapters(w, chapters):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p):
        print('NO SUCH WORK', w); return
    T = json.load(open(p, encoding='utf-8'))['text']
    mishnah_rows(w, [(c, m + 1) for c in chapters for m in range(len(T[c - 1]))])
def folio_rows(work, a, z):
    p = os.path.join(R, work, 'en.json')
    if not os.path.exists(p):
        print('NO SUCH WORK', work); return
    T = json.load(open(p, encoding='utf-8'))['text']
    n_range = 0; l = 0
    for i in range(idx(a), idx(z) + 1):
        if i >= len(T): print('RANGE PAST THE END', work, a, z, i, len(T)); break
        for j, s in enumerate(T[i]):
            ad = '%s %d%s:%d' % (work.replace('_', ' '), i // 2 + 1, 'ab'[i % 2], j + 1)
            n_range += 1
            if ad in linked: l += 1; continue
            topic.append((ad, strip(s)))
    print('%s %s-%s: %d segments in the range, %d of them link rows' % (work, a, z, n_range, l))
    SIZES.append((work, a, z, n_range, l))
mishnah_rows('Mishnah_Sanhedrin', [(1, 5), (4, 1), (5, 1), (5, 2), (7, 6), (7, 10), (10, 4), (10, 5), (10, 6), (11, 1), (11, 4), (11, 5), (11, 6)])
mishnah_rows('Mishnah_Makkot', [(1, 4), (1, 5), (1, 6)])
mishnah_rows('Mishnah_Zevachim', [(8, 10)])
mishnah_rows('Mishnah_Sukkah', [(3, 4)])
mishnah_rows('Mishnah_Avodah_Zarah', [(3, 9)])
mishnah_rows('Pirkei_Avot', [(2, 1), (3, 9), (3, 14)])
RANGES = [('Sanhedrin', '67a', '67a'), ('Sanhedrin', '88b', '88b'), ('Sanhedrin', '89a', '90a'), ('Sanhedrin', '40a', '41a'), ('Sanhedrin', '111b', '113b'), ('Zevachim', '80a', '81b'), ('Sukkah', '34b', '34b'), ('Menachot', '41b', '42a'),
          ('Rosh_Hashanah', '28b', '28b'), ('Eruvin', '96a', '96a'), ('Avodah_Zarah', '49b', '50a'), ('Bava_Metzia', '59b', '59b'), ('Yevamot', '90b', '90b'), ('Shabbat', '151b', '151b')]
for w, a, z in RANGES: folio_rows(w, a, z)
print("TOPIC rows %d (the Mishnah rows + the folio ranges whole; link-duplicates dropped)" % len(topic))
print('  ', collections.Counter(re.sub(r' \d+[ab]?:.*$', '', a) for a, _ in topic).most_common(20))
# TOSEFTA SANHEDRIN 11 (the festival's execution — 91:2's note), 12 (the honors), 14 (the condemned city — 93:3, 94:6's notes), TOSEFTA ZEVACHIM 8 (the mixed bloods — 82:3's note), TOSEFTA BAVA KAMMA 9 (the mercy — 96:4) and THE SIFREI ON NUMBERS 103, 113, 114 (the English's parallels) whole; a dict-text export read under its empty key
for w, c in (('Tosefta_Sanhedrin', 11), ('Tosefta_Sanhedrin', 12), ('Tosefta_Sanhedrin', 14), ('Tosefta_Zevachim', 8), ('Tosefta_Bava_Kamma', 9), ('Sifrei_Bamidbar', 103), ('Sifrei_Bamidbar', 113), ('Sifrei_Bamidbar', 114)):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p): print('NOT IN THE EXPORT:', w); continue
    T = json.load(open(p, encoding='utf-8'))['text']
    if isinstance(T, dict):
        print('  %s: the text keys %s; the empty key holds %s of %d' % (w, list(T), type(T['']).__name__, len(T[''])))
        T = T['']
    if c - 1 >= len(T): print('CHAPTER PAST THE END OF THE EXPORT: %s %d (the export holds %d top-level entries)' % (w, c, len(T))); continue
    rows = T[c - 1]; rows = rows if isinstance(rows, list) else [rows]
    if not rows: print('EMPTY CHAPTER IN THE EXPORT: %s %d (the dict-text export holds no rows there — the design reads it from this print)' % (w, c)); continue
    for i, x in enumerate(rows): topic.append(('%s %d:%d' % (w.replace('_', ' '), c, i + 1), strip(x if isinstance(x, str) else ' '.join(x))))
    print('%s %d: %d rows; the first: %s' % (w, c, len(rows), strip(rows[0] if isinstance(rows[0], str) else ' '.join(rows[0]))[:120]))
# THE RANGES BY AMUD (segments; the first 90 characters of each amud's first row — the design chooses; the rest enumerated outside declared scope)
for wname, a, z in RANGES:
    TB = json.load(open(os.path.join(R, wname, 'en.json'), encoding='utf-8'))['text']
    for i in range(idx(a), idx(z) + 1):
        print('   %-14s %4s %3d  %s' % (wname, '%d%s' % (i // 2 + 1, 'ab'[i % 2]), len(TB[i]), strip(TB[i][0])[:90].replace('\n', ' ') if TB[i] else ''))
for wname in ('Tosefta_Sanhedrin', 'Tosefta_Zevachim', 'Tosefta_Bava_Kamma', 'Sifrei_Bamidbar', 'Mishnah_Sukkah', 'Pirkei_Avot', 'Bava_Metzia', 'Eruvin', 'Rosh_Hashanah', 'Shabbat', 'Yevamot', 'Menachot'):
    print('  export has %s: %s' % (wname, os.path.exists(os.path.join(R, wname, 'en.json'))))

prior = {}
own = {'deu_13_reeh_2026-09-21.md'}
alladdr = list(linked) + [a for a, _ in topic]
for f in sorted(glob.glob(ROOT + '/logic/oral_triage/*.md')):
    if os.path.basename(f) in own: continue
    txt = open(f, encoding='utf-8').read()
    for a in alladdr:
        if re.search(r'(^|[^\w])' + re.escape(a) + r'(?![\d:])', txt, re.M):
            prior.setdefault(a, []).append(os.path.basename(f))
print('PRIOR READS (credited): %d addresses of %d' % (len(prior), len(alladdr)))
byled = collections.Counter(f for fs in prior.values() for f in fs)
print('  by ledger:', byled.most_common(15))
print('  credited per range: %s' % [(w, a, z, sum(1 for ad in prior if ad.startswith(w.replace('_', ' ') + ' ') and (re.match(r'\d+[ab]', a) and idx(a) <= idx(re.match(r'(\d+[ab])', ad.split(' ')[-1].split(':')[0]).group(1)) <= idx(z) if re.match(r'\d+[ab]', a) and re.match(r'\d+[ab]', ad.split(' ')[-1].split(':')[0]) else True))) for w, a, z, n, l in SIZES if re.match(r'\d+[ab]', a)])
print('  the Mishnah rows credited: %s' % sorted(a for a in prior if a.startswith('Mishnah')))

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('ROWS %d LINK %d TOPIC %d CREDITED %d\n\n' % (len(link) + len(topic), len(link), len(topic), len(prior)))
    for a, hits, t in link:
        f.write('## [LINK] %s  %s%s\n%s\n\n' % (a, ' '.join(hits), ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
    for a, t in topic:
        f.write('## [TOPIC] %s  %s\n%s\n\n' % (a, ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
print('dump', OUT, os.path.getsize(OUT), 'bytes', sum(1 for _ in open(OUT, encoding='utf-8')), 'lines')
print('THE RANGES SIZED:')
for w, a, z, n, l in SIZES: print('  %-22s %6s-%-6s %4d rows, %3d link rows' % (w, a, z, n, l))
