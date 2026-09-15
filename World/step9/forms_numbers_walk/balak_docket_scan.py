import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 7b — THE COMPILE OF BALAK (2026-09-11): THE EXAM DOCKET'S SCAN, sized by script before the docket is written.
# (1) THE LINK ROWS: every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of
#     Numbers 22:1-25:19; (2) THE TOPIC ROWS: the rows the four reading ledgers' TESTING SHELF lines and the COMPILE_DEBT box name BY
#     ADDRESS — Mishnah Sanhedrin 7:6 (baring to Peor), 9:6 (the zealots), 10:2 (Balaam's share), Pirkei Avot 5:6 (the mouth of the ass),
#     5:19 (Balaam's disciples), SANHEDRIN 105a-106b WHOLE (the Balaam sugya — every segment not already a link row), the Jerusalem Talmud's
#     Taanit 4:5 (R. Akiva's star) and Sanhedrin 10:2 (Balaam's share) by address; Seder Olam 9:2 and 10:2 were read at 6b's docket
#     (credited). The other Talmud folios the ledgers name (Sanhedrin 35a, 60b-64a, 81b-82b, 90a; Berakhot 7a, 12b, 21b; Avodah Zarah
#     4a-b, 36b; Makkot 10b; Nazir 23b; Sotah 47a; Horayot 10b; Niddah 31a; Bava Batra 14b-15a, 60a; Zevachim 101b, 116a; Bava Kamma
#     110b; Yoma 9a, 18a; Taanit 20a; Yevamot 4a) enter through (1), their remainder enumerated by count as OUTSIDE DECLARED SCOPE.
# (3) THE PRIOR READS: every address already verdicted in an earlier logic/oral_triage ledger (this sitting's own four reading ledgers
#     excluded) is listed as CREDITED with its ledger — speed ruling (b), credit guard (1): a quick look, not a blind credit.
import json, re, os, collections, glob
R = (_ROOT + '/Data/sefaria_export')
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{SCR}/balak_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
SPAN = {(22, v) for v in range(1, 42)} | {(23, v) for v in range(1, 31)} | {(24, v) for v in range(1, 26)} | {(25, v) for v in range(1, 20)}
CITE = re.compile(r'Numbers?\.? (\d+):(\d+)(?:[-–](\d+))?')

def addr(work, cats, path):
    if 'Talmud' in cats and 'Bavli' in cats and len(path) >= 2:
        i = path[0]; return '%s %d%s:%d' % (work.replace('_', ' '), i // 2 + 1, 'ab'[i % 2], path[1] + 1)
    return '%s %s' % (work.replace('_', ' '), ':'.join(str(x + 1) for x in path))

def walk(x, path):
    if isinstance(x, list):
        for i, v in enumerate(x): yield from walk(v, path + [i])
    elif isinstance(x, str):
        yield path, x

link = []   # (addr, cites, text)
works = collections.Counter()
for w in sorted(os.listdir(R)):
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p): continue
    try:
        d = json.load(open(p, encoding='utf-8'))
    except Exception:
        continue
    cats = d.get('categories') or [] if isinstance(d, dict) else []
    if not cats or cats[0] not in ('Talmud', 'Mishnah', 'Tosefta') or 'Yerushalmi' in cats or 'Commentary' in cats or '_on_' in w: continue   # the three exam shelves only — no commentaries
    for path, s in walk(d['text'], []):
        t = strip(s)
        hits = []
        for m in CITE.finditer(t):
            c, a, z = int(m.group(1)), int(m.group(2)), int(m.group(3) or m.group(2))
            for v in range(a, min(z, a + 40) + 1):
                if (c, v) in SPAN: hits.append('Num %d:%d' % (c, v))
        if hits:
            link.append((addr(w, cats, path), sorted(set(hits), key=lambda s: tuple(int(x) for x in re.findall(r'\d+', s))), t))
            works[w] += 1
print('LINK rows %d in %d works' % (len(link), len(works)))
for w, n in works.most_common(): print('  %-32s %d' % (w, n))

# ---- THE TOPIC ROWS BY ADDRESS ----
def idx(s):
    m = re.match(r'(\d+)([ab])', s); return (int(m.group(1)) - 1) * 2 + (0 if m.group(2) == 'a' else 1)
topic = []
linked = {a for a, _, _ in link}
def mishnah_rows(w, cells):
    T = json.load(open(os.path.join(R, w, 'en.json'), encoding='utf-8'))['text']
    for c, m in cells:
        if c - 1 < len(T) and m - 1 < len(T[c - 1]):
            a = '%s %d:%d' % (w.replace('_', ' '), c, m)
            if a in linked: continue
            topic.append((a, strip(T[c - 1][m - 1])))
        else:
            print('NO SUCH ROW', w, c, m)
mishnah_rows('Mishnah_Sanhedrin', [(7, 6), (9, 6), (10, 1), (10, 2)])
mishnah_rows('Pirkei_Avot', [(5, 6), (5, 19)])
# Sanhedrin 105a-106b whole: every segment in the range not already a link row
T = json.load(open(os.path.join(R, 'Sanhedrin', 'en.json'), encoding='utf-8'))['text']
n_range = 0
for i in range(idx('105a'), idx('106b') + 1):
    for j, s in enumerate(T[i]):
        a = 'Sanhedrin %d%s:%d' % (i // 2 + 1, 'ab'[i % 2], j + 1)
        n_range += 1
        if a in linked: continue
        topic.append((a, strip(s)))
print('Sanhedrin 105a-106b: %d segments in the range' % n_range)
# the Jerusalem Talmud by address (chapter:halakha, every segment)
for w, c, h in (('Jerusalem_Talmud_Taanit', 4, 5), ('Jerusalem_Talmud_Sanhedrin', 10, 2)):
    d = json.load(open(os.path.join(R, w, 'en.json'), encoding='utf-8'))
    JT = d['text']
    node = JT[c - 1][h - 1] if isinstance(JT, list) else None
    if node is None:
        print('NO SUCH NODE', w, c, h, type(JT)); continue
    segs = list(walk(node, []))
    print('%s %d:%d — %d segments' % (w, c, h, len(segs)))
    for path, s in segs:
        a = '%s %d:%d:%s' % (w.replace('_', ' '), c, h, ':'.join(str(x + 1) for x in path))
        topic.append((a, strip(s)))
print("TOPIC rows %d (Mishnah by address + Sanhedrin 105a-106b whole + the Jerusalem Talmud's two halakhot; link-duplicates dropped)" % len(topic))
print('  ', collections.Counter(a.rsplit(' ', 1)[0] if ':' in a else a for a, _ in topic).most_common(8))

# ---- THE PRIOR READS ----
prior = {}
own = {'num_22_balak_bilam_call_2026-09-11.md', 'num_23_oracles_1_2_2026-09-11.md', 'num_24_oracles_3_4_2026-09-11.md', 'num_25_peor_pinchas_2026-09-11.md'}
alladdr = list(linked) + [a for a, _ in topic]
for f in sorted(glob.glob((_ROOT + '/logic/oral_triage/*.md'))):
    if os.path.basename(f) in own: continue
    txt = open(f, encoding='utf-8').read()
    for a in alladdr:
        if re.search(r'(^|[^\w])' + re.escape(a) + r'(?![\d:])', txt, re.M):
            prior.setdefault(a, []).append(os.path.basename(f))
print('PRIOR READS (credited): %d addresses' % len(prior))
for a, fs in sorted(prior.items()): print('   %-32s %s' % (a, ', '.join(fs)[:120]))

# ---- THE LONG TALMUD RANGES the ledgers name: sized ----
RANGES = [('Sanhedrin', '105a', '106b'), ('Sanhedrin', '35a', '35a'), ('Sanhedrin', '60b', '64a'), ('Sanhedrin', '81b', '82b'), ('Sanhedrin', '90a', '90a'), ('Berakhot', '7a', '7a'), ('Berakhot', '12b', '12b'), ('Berakhot', '21b', '21b'),
          ('Avodah_Zarah', '4a', '4b'), ('Avodah_Zarah', '36b', '36b'), ('Makkot', '10b', '10b'), ('Nazir', '23b', '23b'), ('Sotah', '47a', '47a'), ('Horayot', '10b', '10b'), ('Niddah', '31a', '31a'), ('Bava_Batra', '14b', '15a'), ('Bava_Batra', '60a', '60a'),
          ('Zevachim', '101b', '101b'), ('Zevachim', '116a', '116a'), ('Bava_Kamma', '110b', '110b'), ('Yoma', '9a', '9a'), ('Yoma', '18a', '18a'), ('Taanit', '20a', '20a'), ('Yevamot', '4a', '4a')]
print('THE LONG RANGES (segments in the range; of them link rows):')
for w, a, z in RANGES:
    TT = json.load(open(os.path.join(R, w, 'en.json'), encoding='utf-8'))['text']
    n = sum(len(TT[i]) for i in range(idx(a), min(idx(z), len(TT) - 1) + 1))
    l = sum(1 for ad, _, _ in link if ad.startswith(w.replace('_', ' ') + ' ') and idx(a) <= idx(re.match(r'.* (\d+[ab]):', ad).group(1)) <= idx(z))
    print('  %-12s %4s-%-4s %4d segments, %3d link rows' % (w, a, z, n, l))

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('ROWS %d LINK %d TOPIC %d CREDITED %d\n\n' % (len(link) + len(topic), len(link), len(topic), len(prior)))
    for a, hits, t in link:
        f.write('## [LINK] %s  %s%s\n%s\n\n' % (a, ' '.join(hits), ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
    for a, t in topic:
        f.write('## [TOPIC] %s  %s\n%s\n\n' % (a, ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
print('dump', OUT, os.path.getsize(OUT), 'bytes')
