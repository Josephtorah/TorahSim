#!/usr/bin/env python3
# THE NUMBERS WALK sitting 4b — THE COMPILE OF SHELACH (2026-09-10): THE EXAM DOCKET'S SCAN, sized by script before the docket is written.
# (1) THE LINK ROWS: every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of
#     Numbers 13:1-15:31; (2) THE TOPIC ROWS: the Mishnah's rows named BY ADDRESS in the four reading ledgers' TESTING SHELF lines (the
#     answer sheet); the long Talmud ranges the ledgers name enter through (1) — their remainder is enumerated by count as OUTSIDE
#     DECLARED SCOPE in the docket's header. The dump is the docket script's input (write_shelach_docket.py), as at Naso.
import json, re, os, collections
R = '<repo-old>/Data/sefaria_export'
OUT = '<scratch>/shelach_docket_dump.txt'
strip = lambda s: re.sub(r'<[^>]+>', '', s)
SPAN = {(13, v) for v in range(1, 34)} | {(14, v) for v in range(1, 46)} | {(15, v) for v in range(1, 32)}
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
TOPIC = [('Mishnah_Menachot', [(9, m) for m in range(1, 10)] + [(12, m) for m in range(1, 6)] + [(13, m) for m in range(1, 12)]), ('Mishnah_Zevachim', [(14, m) for m in range(1, 11)]),
         ('Mishnah_Shekalim', [(7, m) for m in range(1, 8)]), ('Mishnah_Kinnim', [(c, m) for c in (1, 2, 3) for m in range(1, 8)]), ('Mishnah_Challah', [(c, m) for c in (1, 2, 3, 4) for m in range(1, 12)]),
         ('Mishnah_Terumot', [(4, m) for m in range(1, 14)]), ('Mishnah_Horayot', [(1, m) for m in range(1, 6)] + [(2, m) for m in range(1, 8)]), ('Mishnah_Keritot', [(1, 1), (1, 2)]),
         ('Mishnah_Shabbat', [(7, 1)]), ('Mishnah_Sanhedrin', [(1, 6), (10, 3)]), ('Mishnah_Ta_anit', [(4, 6), (4, 7)]), ('Mishnah_Sotah', [(7, m) for m in range(1, 9)]),
         ('Pirkei_Avot', [(3, 11), (4, 2), (5, 4)]), ('Mishnah_Parah', [(1, 3)])]
topic = []
linked = {a for a, _, _ in link}
for w, cells in TOPIC:
    d = json.load(open(os.path.join(R, w, 'en.json'), encoding='utf-8'))
    T = d['text']
    for c, m in cells:
        if c - 1 < len(T) and m - 1 < len(T[c - 1]):
            a = '%s %d:%d' % (w.replace('_', ' '), c, m)
            if a in linked: continue
            topic.append((a, strip(T[c - 1][m - 1])))
print('TOPIC rows %d (Mishnah, by address; link-duplicates dropped)' % len(topic))
print('  ', collections.Counter(a.rsplit(' ', 1)[0] for a, _ in topic))

# ---- THE LONG TALMUD RANGES the ledgers name: sized (their link hits counted; the remainder OUTSIDE by count) ----
RANGES = [('Sotah', '34a', '35b'), ('Taanit', '29a', '29a'), ('Sanhedrin', '104b', '104b'), ('Arakhin', '15a', '15b'), ('Bava_Batra', '15a', '15a'), ('Bava_Batra', '121a', '121b'), ('Ketubot', '112a', '112a'),
          ('Megillah', '23b', '23b'), ('Berakhot', '21b', '21b'), ('Berakhot', '7a', '7a'), ('Yoma', '86a', '86a'), ('Sanhedrin', '27b', '27b'), ('Sanhedrin', '111a', '111a'), ('Rosh_Hashanah', '17b', '17b'), ('Shabbat', '89b', '89b'),
          ('Menachot', '87b', '91b'), ('Menachot', '103b', '107a'), ('Zevachim', '111a', '111b'), ('Keritot', '8b', '9a'), ('Yevamot', '46a', '47b'), ('Pesachim', '37b', '38a'), ('Menachot', '70a', '70a'),
          ('Horayot', '2a', '9a'), ('Keritot', '2a', '7b'), ('Shabbat', '68b', '69a'), ('Sanhedrin', '64b', '64b'), ('Sanhedrin', '90b', '90b'), ('Sanhedrin', '99a', '99a'), ('Shevuot', '13a', '13a'), ('Kiddushin', '37a', '37b'),
          ('Taanit', '30b', '30b')]
def idx(s):
    m = re.match(r'(\d+)([ab])', s); return (int(m.group(1)) - 1) * 2 + (0 if m.group(2) == 'a' else 1)
print('THE LONG RANGES (segments in the range; of them link rows):')
for w, a, z in RANGES:
    T = json.load(open(os.path.join(R, w, 'en.json'), encoding='utf-8'))['text']
    n = sum(len(T[i]) for i in range(idx(a), min(idx(z), len(T) - 1) + 1))
    l = sum(1 for ad, _, _ in link if ad.startswith(w.replace('_', ' ') + ' ') and idx(a) <= idx(re.match(r'.* (\d+[ab]):', ad).group(1)) <= idx(z))
    print('  %-12s %4s-%-4s %4d segments, %3d link rows' % (w, a, z, n, l))

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('ROWS %d LINK %d TOPIC %d\n\n' % (len(link) + len(topic), len(link), len(topic)))
    for a, hits, t in link:
        f.write('## [LINK] %s  %s\n%s\n\n' % (a, ' '.join(hits), t))
    for a, t in topic:
        f.write('## [TOPIC] %s  \n%s\n\n' % (a, t))
print('dump', OUT, os.path.getsize(OUT), 'bytes')
