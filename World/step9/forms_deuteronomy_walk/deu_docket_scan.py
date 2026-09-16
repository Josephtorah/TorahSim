#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 1b — THE COMPILE OF THE OPENING SPEECH (2026-09-15): THE EXAM DOCKET'S SCAN, sized by script before the docket is
# written (ref_docket_scan.py's form). (1) THE LINK ROWS: every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta exports whose
# English cites a verse of Deuteronomy 1:1-3:29; (2) THE TOPIC ROWS by address (the union rule; COMPILE_DEBT's Deuteronomy sitting-1 box (l)):
# Mishnah Sanhedrin 1:1-6 and 4:1 with Sanhedrin 2a-2b, 32a-32b; Sanhedrin 3:1-8 with 23a-31b (6b-7a the compromise); 1:6 with 16b-17a; Avot 1:1;
# Sheviit 9:2; Rosh Hashanah 1:1 with 2b-3a; Sotah 7:5 and 34a-35a; Berakhot 4:5-6 with 30a; Makkot 2:4-8 and 9b-10a; Kelim 17:9-10 and Eruvin
# 4:8; Sanhedrin 90b-91a; (3) THE PRIOR READS credited.
import json, re, os, collections, glob, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
R = ROOT + '/Data/sefaria_export'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{SCR}/deu_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
SPAN = {(1, v) for v in range(1, 47)} | {(2, v) for v in range(1, 38)} | {(3, v) for v in range(1, 30)}
CITE = re.compile(r'(?:Deuteronomy|Deut\.?|Dt\.?) ?(\d+):(\d+)(?:[-–](\d+))?')

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
            for v in range(a, min(z, a + 60) + 1):
                if (c, v) in SPAN: hits.append('Deut %d:%d' % (c, v))
        if hits:
            link.append((addr(w, cats, path), sorted(set(hits), key=lambda s: tuple(int(x) for x in re.findall(r'\d+', s))), t))
            works[w] += 1
print('SCANNED %d works (Talmud / Mishnah / Tosefta, no Yerushalmi, no commentary); the forms: Deuteronomy c:v, Deut. c:v, Dt.c:v' % scanned)
print('LINK rows %d in %d works' % (len(link), len(works)))
for w, n in works.most_common(): print('  %-32s %d' % (w, n))
print('  the verses cited: %s' % collections.Counter(h for _, hs, _ in link for h in hs).most_common(80))
for a, hs, t in link: print('  LINK %-26s %-22s %s' % (a, ' '.join(hs), t[:140].replace('\n', ' ')))

# ---- THE TOPIC ROWS BY ADDRESS ----
def idx(s):
    m = re.match(r'(\d+)([ab])', s); return (int(m.group(1)) - 1) * 2 + (0 if m.group(2) == 'a' else 1)
topic = []
linked = {a for a, _, _ in link}
def mishnah_rows(w, refs):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p):
        print('NO SUCH WORK', w); return
    T = json.load(open(p, encoding='utf-8'))['text']
    for c, m in refs:
        a = '%s %d:%d' % (w.replace('_', ' '), c, m)
        if a in linked: print('  %s already a link row' % a); continue
        topic.append((a, strip(T[c - 1][m - 1])))
        print('  %s: %s' % (a, strip(T[c - 1][m - 1])[:200]))
    print('%s single mishnayot: %s' % (w, refs))
SIZES = []
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
mishnah_rows('Mishnah_Sanhedrin', [(1, m) for m in range(1, 7)] + [(4, 1)] + [(3, m) for m in range(1, 9)])
mishnah_rows('Pirkei_Avot', [(1, 1)])
mishnah_rows('Mishnah_Sheviit', [(9, 2)])
mishnah_rows('Mishnah_Rosh_Hashanah', [(1, 1)])
mishnah_rows('Mishnah_Sotah', [(7, 5)])
mishnah_rows('Mishnah_Berakhot', [(4, 5), (4, 6)])
mishnah_rows('Mishnah_Makkot', [(2, m) for m in range(4, 9)])
mishnah_rows('Mishnah_Kelim', [(17, 9), (17, 10)])
mishnah_rows('Mishnah_Eruvin', [(4, 8)])
RANGES = [('Sanhedrin', '2a', '2b'), ('Sanhedrin', '32a', '32b'), ('Sanhedrin', '6b', '7a'), ('Sanhedrin', '23a', '31b'), ('Sanhedrin', '16b', '17a'), ('Sanhedrin', '90b', '91a'), ('Rosh_Hashanah', '2b', '3a'), ('Sotah', '34a', '35a'), ('Berakhot', '30a', '30a'), ('Makkot', '9b', '10a')]
for w, a, z in RANGES: folio_rows(w, a, z)
print("TOPIC rows %d (the Mishnah rows + the folio ranges whole; link-duplicates dropped)" % len(topic))
print('  ', collections.Counter(re.sub(r' \d+[ab]?:.*$', '', a) for a, _ in topic).most_common(20))

# ---- THE PRIOR READS ----
prior = {}
own = {'deu_01_03_devarim_2026-09-15.md'}
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

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('ROWS %d LINK %d TOPIC %d CREDITED %d\n\n' % (len(link) + len(topic), len(link), len(topic), len(prior)))
    for a, hits, t in link:
        f.write('## [LINK] %s  %s%s\n%s\n\n' % (a, ' '.join(hits), ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
    for a, t in topic:
        f.write('## [TOPIC] %s  %s\n%s\n\n' % (a, ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
print('dump', OUT, os.path.getsize(OUT), 'bytes', sum(1 for _ in open(OUT, encoding='utf-8')), 'lines')
print('THE RANGES SIZED:')
for w, a, z, n, l in SIZES: print('  %-14s %4s-%-4s %4d segments, %3d link rows' % (w, a, z, n, l))
