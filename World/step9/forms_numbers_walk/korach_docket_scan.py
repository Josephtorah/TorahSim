import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 5b — THE COMPILE OF KORACH (2026-09-10): THE EXAM DOCKET'S SCAN, sized by script before the docket is written.
# (1) THE LINK ROWS: every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of
#     Numbers 16:1-18:32; (2) THE TOPIC ROWS: the Mishnah's rows named BY ADDRESS in the three reading ledgers' TESTING SHELF lines and the
#     COMPILE_DEBT line (Bekhorot 1, 4, 8; Zevachim 5:8; Terumot 1, 2, 4; Ma'aserot 1; Ma'aser Sheni 5; Challah 1:9, 4:9; Arakhin 8:6-7; Ketubot
#     5:2-3; Yoma 2; Sanhedrin 9:6, 10:3; Middot 1, 5:4; Avot 4:13, 5:6, 5:17; Tamid 1:1-2); the long Talmud ranges the ledgers name enter
#     through (1) — their remainder is enumerated by count as OUTSIDE DECLARED SCOPE in the docket's header. (3) THE PRIOR READS: every
#     address already verdicted in an earlier logic/oral_triage ledger (the exam dockets and the reading ledgers; this sitting's own three
#     excluded) is listed as CREDITED with its ledger — speed ruling (b), credit guard (1): a quick look, not a blind credit. The dump is the
#     docket script's input (write_korach_docket.py), as at Shelach.
import json, re, os, collections, glob
R = (_ROOT + '/Data/sefaria_export')
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{SCR}/korach_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
SPAN = {(16, v) for v in range(1, 36)} | {(17, v) for v in range(1, 29)} | {(18, v) for v in range(1, 33)}
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

# ---- THE TOPIC ROWS BY ADDRESS: the Mishnah chapters and mishnayot the ledgers name (the answer sheet) ----
TOPIC = [('Mishnah_Bekhorot', [(1, m) for m in range(1, 8)] + [(4, m) for m in range(1, 11)] + [(8, m) for m in range(1, 11)]), ('Mishnah_Zevachim', [(5, 8)]),
         ('Mishnah_Terumot', [(c, m) for c in (1, 2, 4) for m in range(1, 14)]), ('Mishnah_Maasrot', [(1, m) for m in range(1, 9)]), ('Mishnah_Maaser_Sheni', [(5, m) for m in range(1, 16)]),
         ('Mishnah_Challah', [(1, 9), (4, 9)]), ('Mishnah_Arakhin', [(8, 6), (8, 7)]), ('Mishnah_Ketubot', [(5, 2), (5, 3)]), ('Mishnah_Yoma', [(2, m) for m in range(1, 8)]),
         ('Mishnah_Sanhedrin', [(9, 6), (10, 3)]), ('Mishnah_Middot', [(1, m) for m in range(1, 10)] + [(5, 4)]), ('Pirkei_Avot', [(4, 13), (5, 6), (5, 17)]), ('Mishnah_Tamid', [(1, 1), (1, 2)])]
topic = []
linked = {a for a, _, _ in link}
for w, cells in TOPIC:
    p = os.path.join(R, w, 'en.json')
    if not os.path.exists(p):
        print('NO SUCH WORK', w); continue
    d = json.load(open(p, encoding='utf-8'))
    T = d['text']
    for c, m in cells:
        if c - 1 < len(T) and m - 1 < len(T[c - 1]):
            a = '%s %d:%d' % (w.replace('_', ' '), c, m)
            if a in linked: continue
            topic.append((a, strip(T[c - 1][m - 1])))
print('TOPIC rows %d (Mishnah, by address; link-duplicates dropped)' % len(topic))
print('  ', collections.Counter(a.rsplit(' ', 1)[0] for a, _ in topic))

# ---- THE PRIOR READS: addresses already verdicted in an earlier ledger (this sitting's three reading ledgers excluded) ----
prior = {}
own = {'num_16_korach_2026-09-10.md', 'num_17_plague_staff_2026-09-10.md', 'num_18_priest_levite_dues_2026-09-10.md'}
for f in sorted(glob.glob((_ROOT + '/logic/oral_triage/*.md'))):
    if os.path.basename(f) in own: continue
    txt = open(f, encoding='utf-8').read()
    for a in list(linked) + [a for a, _ in topic]:
        if re.search(r'(^|[^\w])' + re.escape(a) + r'(?![\d:])', txt, re.M):
            prior.setdefault(a, []).append(os.path.basename(f))
print('PRIOR READS (credited): %d addresses' % len(prior))
for a, fs in sorted(prior.items()): print('   %-32s %s' % (a, ', '.join(fs)[:120]))

# ---- THE LONG TALMUD RANGES the ledgers name: sized (their link hits counted; the remainder OUTSIDE by count) ----
RANGES = [('Sanhedrin', '109b', '110a'), ('Bava_Batra', '74a', '74a'), ('Sotah', '13b', '13b'), ('Shabbat', '97a', '97a'), ('Yoma', '44a', '44b'), ('Pesachim', '54a', '54a'),
          ('Shabbat', '89a', '89a'), ('Menachot', '28b', '28b'), ('Yoma', '52b', '52b'), ('Horayot', '12a', '12a'), ('Keritot', '5b', '5b'), ('Shabbat', '88a', '88a'),
          ('Bekhorot', '3b', '13a'), ('Bekhorot', '26b', '27a'), ('Bekhorot', '49b', '51b'), ('Zevachim', '37a', '37b'), ('Zevachim', '57a', '57a'), ('Yevamot', '86a', '86b'), ('Yevamot', '89b', '89b'),
          ('Chullin', '130b', '131b'), ('Bekhorot', '58b', '59a'), ('Arakhin', '28b', '29a'), ('Ketubot', '57b', '58a'), ('Kiddushin', '5a', '5a'), ('Kiddushin', '10b', '10b'), ('Yoma', '22a', '26a'),
          ('Chullin', '106a', '107a'), ('Sanhedrin', '81b', '84a'), ('Arakhin', '11a', '11b'), ('Bava_Kamma', '110b', '110b'), ('Chullin', '133b', '133b'), ('Pesachim', '36a', '36a'), ('Yevamot', '73b', '74a')]
def idx(s):
    m = re.match(r'(\d+)([ab])', s); return (int(m.group(1)) - 1) * 2 + (0 if m.group(2) == 'a' else 1)
print('THE LONG RANGES (segments in the range; of them link rows):')
for w, a, z in RANGES:
    T = json.load(open(os.path.join(R, w, 'en.json'), encoding='utf-8'))['text']
    n = sum(len(T[i]) for i in range(idx(a), min(idx(z), len(T) - 1) + 1))
    l = sum(1 for ad, _, _ in link if ad.startswith(w.replace('_', ' ') + ' ') and idx(a) <= idx(re.match(r'.* (\d+[ab]):', ad).group(1)) <= idx(z))
    print('  %-12s %4s-%-4s %4d segments, %3d link rows' % (w, a, z, n, l))

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('ROWS %d LINK %d TOPIC %d CREDITED %d\n\n' % (len(link) + len(topic), len(link), len(topic), len(prior)))
    for a, hits, t in link:
        f.write('## [LINK] %s  %s%s\n%s\n\n' % (a, ' '.join(hits), ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
    for a, t in topic:
        f.write('## [TOPIC] %s  %s\n%s\n\n' % (a, ('  {CREDITED: ' + ', '.join(prior[a]) + '}') if a in prior else '', t))
print('dump', OUT, os.path.getsize(OUT), 'bytes')
