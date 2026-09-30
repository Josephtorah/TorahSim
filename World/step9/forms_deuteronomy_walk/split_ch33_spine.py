import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 21 — CHAPTER 33, THE BLESSING (LEAN, 2026-09-29): the spine split by piska for the reading (sitting 20's form, split_ch32_spine.py, over ONE
# chapter whose spine is IN FORCE): the Sifrei's fifteen piskaot 342-356 on 33:1-29 (342 on 33:1 seven rows — its head printed with a comma, the export's one comma head,
# tolerated by the dump's regex; 355 on 33:20 thirty rows — the chapter's longest; 357 on 34:1 is chapter 34's), every head present (the dump's heads table); the outside
# rows citing chapter 33 joined less the spine; the edges 341|342 and 356|357 PRINTED (the last rows before and the first rows after) — the asserts typed in the ink from
# this print; the bytes per piska printed FOR THE RUN PLAN (the rows read whole under the whole-row rule, the runs cut by bytes). RUN FROM THE REPO ROOT.
import os, re, json, html, subprocess
SP = os.path.dirname(os.path.abspath(__file__))
ROOT = _ROOT
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/he.json', encoding='utf-8'))['text']
en = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/en.json', encoding='utf-8'))['text']
HEADLESS = {}
CHAPS = {33: range(342, 357)}
rows, out = {}, {}
for ch in (33,):
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
SPINE = sorted({p for p, _ in rows})
assert SPINE == list(range(342, 357)), SPINE
for k in [k for k in out if k[0] in SPINE]: assert k in rows, k; del out[k]
per = {p: sorted(r for q, r in rows if q == p) for p in SPINE}
assert all(per[p] == list(range(1, len(he[p - 1]) + 1)) for p in SPINE), 'every row of every spine piska in the files'
N = {c: sum(len(per[p]) for p in ps) for c, ps in CHAPS.items()}
HB = lambda p: [plain(clean(x)) for x in he[p - 1]]
P341, P342, P356, P357 = (HB(p) for p in (341, 342, 356, 357))
for p in SPINE:
    with open(f'{SP}/ch33_spine_p{p}.txt', 'w', encoding='utf-8') as f:
        for r in per[p]:
            h, he_, en_ = rows[(p, r)]
            f.write(f'--- {p}:{r} (head {h})\nHE: {he_}\nEN: {en_}\n')
TRUE_OUT = sorted(out)
assert all(p not in SPINE for p, _ in TRUE_OUT), TRUE_OUT
with open(f'{SP}/ch33_outside_rows.txt', 'w', encoding='utf-8') as f:
    for p, r in TRUE_OUT:
        d = out[(p, r)]; f.write(f'--- {p}:{r} (head {d.get("head")}; cites chapter {sorted(d["cites"])})\nHE: {d.get("HE", "")}\nEN: {d.get("EN", "(no EN row)")}\n')
BYT = {p: os.path.getsize(f'{SP}/ch33_spine_p{p}.txt') for p in SPINE}
print('spine piskaot', SPINE[0], '-', SPINE[-1], len(SPINE), '| rows per piska', {p: len(per[p]) for p in SPINE}, '| totals', N, sum(N.values()))
print('bytes per piska file', BYT, '| total', sum(BYT.values()))
# THE RUN PLAN BY BYTES — the piskaot in order cut into slices under a byte budget (the whole-row rule; a run reads its slice whole)
BUDGET = 90000; runs = []; cur = []; acc = 0
for p in SPINE:
    if cur and acc + BYT[p] > BUDGET: runs.append((cur, acc)); cur, acc = [], 0
    cur.append(p); acc += BYT[p]
if cur: runs.append((cur, acc))
print('the run plan under %d bytes a slice:' % BUDGET, [((s[0], s[-1]), len(s), b) for s, b in runs], '| slices', len(runs))
print('THE EDGES — the last rows before and the first rows after (first 70 chars HE):')
for a, b, A, B in ((341, 342, P341, P342), (356, 357, P356, P357)):
    print(f'  {a} last two rows:', [x[:70] for x in A[-2:]], f'| {b}:1 opens:', B[0][:90])
print('342:1 opens (the blessing\'s first piska):', HB(342)[0][:100], '| rows', len(HB(342)))
print('356:14 (the chapter\'s last piska, its last row):', HB(356)[-1][:160])
# the edge words: "and this is the blessing" (33:1's opening) in 341's rows; "happy are you, O Israel" (33:29's opening) in 357's rows — the ink asserts from this print
print('the words of 33:1 in 341 / the words of 33:29 in 357:', any('וזאת הברכה' in x for x in P341), any('אשריך ישראל' in x for x in P357), [x[:80] for x in P357 if 'אשריך' in x][:3])
print('the outside rows', TRUE_OUT, len(TRUE_OUT), '| bytes', os.path.getsize(f'{SP}/ch33_outside_rows.txt'), '| their heads and cites', {k: (out[k].get('head'), sorted(out[k]['cites'])) for k in TRUE_OUT})
print('first 80 chars HE', {k: plain(out[k].get('HE', ''))[:80] for k in TRUE_OUT})
