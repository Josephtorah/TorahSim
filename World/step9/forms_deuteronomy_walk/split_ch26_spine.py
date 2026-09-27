import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 18 — CHAPTERS 26-28 (LEAN, 2026-09-26): the spine split by piska for the reading (sitting 17's form, split_ch22_spine.py, over
# THREE chapters of which ONE has a spine): the spine 297-303 — chapter 26's seven piskaot (297 on 26:1, 300 on 26:4, 301 on 26:5 with thirty-seven rows, 302 on
# 26:12; 298 HEADLESS inside 26:2 "and place it in a basket", 299 HEADLESS inside 26:3 "and you shall say to him", 303 HEADLESS inside 26:13 "and you shall give it
# to the Levite" with twenty rows — the dumps' "head None"); CHAPTERS 27 AND 28 HAVE NO PISKA (the Sifrei runs 303 on 26:15 to 304 on 31:14) — their shelf is
# Onkelos whole and the rows elsewhere citing them, joined here with chapter 26's outside rows less the spine; the headless piskaot read WHOLE from the export;
# the tails on the consonants: 296's rows do not carry 26:1's words; the edges 296|297 and 303|304 PRINTED (the openings and the last rows) — the asserts typed
# in the ink from this print. RUN FROM THE REPO ROOT.
import os, re, json, html, subprocess
SP = os.path.dirname(os.path.abspath(__file__))
ROOT = _ROOT
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/he.json', encoding='utf-8'))['text']
en = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/en.json', encoding='utf-8'))['text']
HEADLESS = {298: 'headless — inside 26:2 (and place it in a basket)', 299: 'headless — inside 26:3 (and you shall say to him: the declaration)', 303: 'headless — inside 26:13 (and you shall give it to the Levite: the confession of the tithe)'}
CHAPS = {26: range(297, 304), 27: range(0), 28: range(0)}
rows, out = {}, {}
for ch in (26, 27, 28):
    spine = open(f'{SP}/ch{ch}_sifrei_spine.txt', encoding='utf-8').read()
    outside = open(f'{SP}/ch{ch}_sifrei_outside.txt', encoding='utf-8').read()
    for m in re.finditer(r'^--- (\d+):(\d+) \(head ([^)]*\)?)\)\nHE: (.*)\nEN: (.*)$', spine, re.M):
        k = (int(m.group(1)), int(m.group(2))); assert k not in rows, k
        rows[k] = (m.group(3), m.group(4), m.group(5))
    blocks = re.split(r'^## Sifrei (\d+):(\d+)(?: \(head ([^\n]*)\))? (HE|EN)\n', outside, flags=re.M)
    for i in range(1, len(blocks), 5):
        p, r, head, lang, text = int(blocks[i]), int(blocks[i + 1]), blocks[i + 2], blocks[i + 3], blocks[i + 4].strip('\n')
        d = out.setdefault((p, r), {}); d.setdefault('cites', set()).add(ch)
        if lang in d: assert d[lang] == text, (p, r, lang)
        d[lang] = text
        if head: d['head'] = head
for p, why in HEADLESS.items():
    assert len(he[p - 1]) == len(en[p - 1]), (p, len(he[p - 1]), len(en[p - 1]))
    for r in range(1, len(he[p - 1]) + 1):
        assert (p, r) not in rows
        rows[(p, r)] = (f'None; {why}', clean(he[p - 1][r - 1]), clean(en[p - 1][r - 1]))
SPINE = sorted({p for p, _ in rows})
assert SPINE == list(range(297, 304)), SPINE
for k in [k for k in out if k[0] in SPINE]: assert k in rows, k; del out[k]
per = {p: sorted(r for q, r in rows if q == p) for p in SPINE}
assert all(per[p] == list(range(1, len(he[p - 1]) + 1)) for p in SPINE), 'every row of every spine piska in the files'
N = {c: sum(len(per[p]) for p in ps) for c, ps in CHAPS.items()}
assert (N[26], N[27], N[28], sum(N.values())) == (50 + 3 + 4 + 20, 0, 0, 77), N   # the dump's spine-file rows (50) + the three headless piskaot's rows from the heads table (3 + 4 + 20)
HB = lambda p: [plain(clean(x)) for x in he[p - 1]]
P296, P297, P303, P304 = (HB(p) for p in (296, 297, 303, 304))
assert not any(w in x for x in P296 for w in ('והיה כי תבוא אל הארץ', 'כי תבוא אל הארץ אשר יהוה')), [x[:80] for x in P296]
for p in SPINE:
    with open(f'{SP}/ch26_spine_p{p}.txt', 'w', encoding='utf-8') as f:
        for r in per[p]:
            h, he_, en_ = rows[(p, r)]
            f.write(f'--- {p}:{r} (head {h})\nHE: {he_}\nEN: {en_}\n')
TRUE_OUT = sorted(out)
assert all(p not in SPINE for p, _ in TRUE_OUT), TRUE_OUT
with open(f'{SP}/ch26_outside_rows.txt', 'w', encoding='utf-8') as f:
    for p, r in TRUE_OUT:
        d = out[(p, r)]; f.write(f'--- {p}:{r} (head {d.get("head")}; cites chapter {sorted(d["cites"])})\nHE: {d.get("HE", "")}\nEN: {d.get("EN", "(no EN row)")}\n')
print('spine piskaot', SPINE[0], '-', SPINE[-1], len(SPINE), '| rows per piska', {p: len(per[p]) for p in SPINE}, '| totals', N, sum(N.values()))
print('bytes per piska file', {p: os.path.getsize(f'{SP}/ch26_spine_p{p}.txt') for p in SPINE}, '| by chapter', {c: sum(os.path.getsize(f'{SP}/ch26_spine_p{p}.txt') for p in ps) for c, ps in CHAPS.items()})
for p in HEADLESS: print(f'{p}:1 opens:', HB(p)[0][:100], '| rows', len(HB(p)))
print('THE EDGES — the last rows before and the first rows after (first 70 chars HE):')
for a, b, A, B in ((296, 297, P296, P297), (303, 304, P303, P304)):
    print(f'  {a} last two rows:', [x[:70] for x in A[-2:]], f'| {b}:1 opens:', B[0][:90])
print('304:1-2 and 305:1 (the Sifrei after the gap):', [x[:80] for x in HB(304)], '|', HB(305)[0][:80])
print('the outside rows', TRUE_OUT, len(TRUE_OUT), '| bytes', os.path.getsize(f'{SP}/ch26_outside_rows.txt'), '| their heads and cites', {k: (out[k].get('head'), sorted(out[k]['cites'])) for k in TRUE_OUT})
print('first 80 chars HE', {k: plain(out[k].get('HE', ''))[:80] for k in TRUE_OUT})
