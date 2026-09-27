import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK sitting 17 — CHAPTERS 22-25 (LEAN, 2026-09-25): the four spine files split by piska for the reading (sitting 16's form, split_ch19_spine.py,
# joined over FOUR chapters): the spine 222-296 — chapter 22's piskaot 222-245 (222 HEADLESS on 22:1, opening on Exodus 23:5's ass — the dumps' "head None";
# 236 HEADLESS inside 22:16-17), chapter 23's 246-267 (contiguous, every head in verse order), chapter 24's 268-285 (269 HEADLESS inside 24:1 — fourteen rows;
# 283 HEADLESS inside 24:19 — the forgotten sheaf), chapter 25's 286-296 (295 HEADLESS inside 25:15 — the weights' reward); the headless piskaot read WHOLE from
# the export (the dumps list only their citing rows, among the outside rows — sitting 16's lesson 1); the outside rows the UNION of the four dumps' outside
# sets less the spine. The tails on the consonants: 221's rows do not carry 22:1's words (sitting 16's check, kept); the chapter edges 245|246, 267|268, 285|286
# and the portion edge 296|297 PRINTED (the openings and the last rows) — the asserts typed in the ink from this print.
import os, re, json, html, subprocess
SP = os.path.dirname(os.path.abspath(__file__))
ROOT = _ROOT
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/he.json', encoding='utf-8'))['text']
en = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/en.json', encoding='utf-8'))['text']
HEADLESS = {222: 'headless — on 22:1 (the lost ox and sheep; opens on Exodus 23:5, the fallen ass)', 236: 'headless — inside 22:16-17 (the father: he hates her and lays a charge)',
            269: 'headless — inside 24:1 (she finds no favor; the grounds of the divorce)', 283: 'headless — inside 24:19 (the forgotten sheaf)', 295: 'headless — inside 25:15 (the weights; that your days be long)'}
CHAPS = {22: range(222, 246), 23: range(246, 268), 24: range(268, 286), 25: range(286, 297)}
rows, out = {}, {}
for ch in (22, 23, 24, 25):
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
assert SPINE == list(range(222, 297)), SPINE
for k in [k for k in out if k[0] in SPINE]: assert k in rows, k; del out[k]
per = {p: sorted(r for q, r in rows if q == p) for p in SPINE}
assert all(per[p] == list(range(1, len(he[p - 1]) + 1)) for p in SPINE), 'every row of every spine piska in the files'
N = {c: sum(len(per[p]) for p in ps) for c, ps in CHAPS.items()}
assert (N[22], N[23], N[24], N[25], sum(N.values())) == (145 + 8 + 4, 99, 79 + 14 + 6, 75 + 4, 434), N   # the dumps' in-chapter totals + the headless piskaot's rows from the heads table
HB = lambda p: [plain(clean(x)) for x in he[p - 1]]
P221, P222, P245, P246, P267, P268, P285, P286, P296, P297 = (HB(p) for p in (221, 222, 245, 246, 267, 268, 285, 286, 296, 297))
assert not any(w in x for x in P221 for w in ('לא תראה את שור', 'שור אחיך או את שיו')), [x[:80] for x in P221]
for p in SPINE:
    with open(f'{SP}/ch22_spine_p{p}.txt', 'w', encoding='utf-8') as f:
        for r in per[p]:
            h, he_, en_ = rows[(p, r)]
            f.write(f'--- {p}:{r} (head {h})\nHE: {he_}\nEN: {en_}\n')
TRUE_OUT = sorted(out)
assert all(p not in SPINE for p, _ in TRUE_OUT), TRUE_OUT
with open(f'{SP}/ch22_outside_rows.txt', 'w', encoding='utf-8') as f:
    for p, r in TRUE_OUT:
        d = out[(p, r)]; f.write(f'--- {p}:{r} (head {d.get("head")}; cites chapter {sorted(d["cites"])})\nHE: {d.get("HE", "")}\nEN: {d.get("EN", "(no EN row)")}\n')
print('spine piskaot', SPINE[0], '-', SPINE[-1], len(SPINE), '| rows per piska', {p: len(per[p]) for p in SPINE}, '| totals', N, sum(N.values()))
print('bytes per piska file', {p: os.path.getsize(f'{SP}/ch22_spine_p{p}.txt') for p in SPINE}, '| by chapter', {c: sum(os.path.getsize(f'{SP}/ch22_spine_p{p}.txt') for p in ps) for c, ps in CHAPS.items()})
for p in HEADLESS: print(f'{p}:1 opens:', HB(p)[0][:100], '| rows', len(HB(p)))
print('THE EDGES — the last rows before and the first rows after (first 70 chars HE):')
for a, b, A, B in ((221, 222, P221, P222), (245, 246, P245, P246), (267, 268, P267, P268), (285, 286, P285, P286), (296, 297, P296, P297)):
    print(f'  {a} last two rows:', [x[:70] for x in A[-2:]], f'| {b}:1 opens:', B[0][:90])
print('the outside rows', TRUE_OUT, len(TRUE_OUT), '| bytes', os.path.getsize(f'{SP}/ch22_outside_rows.txt'), '| their heads and cites', {k: (out[k].get('head'), sorted(out[k]['cites'])) for k in TRUE_OUT})
print('first 80 chars HE', {k: plain(out[k].get('HE', ''))[:80] for k in TRUE_OUT})
