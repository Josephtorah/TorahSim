import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK sitting 15 — CHAPTERS 17-18 (LEAN, 2026-09-24): the two spine files split by piska for the reading (chapter 16's form, split_ch16_spine.py,
# joined over TWO chapters): the spine 147-178 — 147-162 chapter 17's sixteen heads and 163-178 chapter 18's sixteen, every head in verse order, NO headless
# piska (the dumps' prints); the outside rows the UNION of the two dumps' outside sets less the spine (each chapter's dump lists the other chapter's spine rows
# among its outside rows when they cite it — joined here). The tails on the consonants: 146's row does not carry 17:1's words (chapter 16's own check, kept);
# 162's rows do not carry 18:1's words; 178's rows do not carry 19:1's words; 163:1 opens with 18:1's citation, 179:1 with 19:1's (sitting 11's lesson 1).
import os, re, json, html, subprocess
SP = os.path.dirname(os.path.abspath(__file__))
ROOT = _ROOT
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
rows, out = {}, {}
for ch in (17, 18):
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
he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/he.json', encoding='utf-8'))['text']
SPINE = sorted({p for p, _ in rows})
assert SPINE == list(range(147, 179)), SPINE
# the other chapter's spine rows listed as outside by one dump are the spine's: moved out of `out`
for k in [k for k in out if k[0] in SPINE]: assert k in rows, k; del out[k]
per = {p: sorted(r for q, r in rows if q == p) for p in SPINE}
assert all(per[p] == list(range(1, len(he[p - 1]) + 1)) for p in SPINE), 'every row of every spine piska in the files'
N17 = sum(len(per[p]) for p in range(147, 163)); N18 = sum(len(per[p]) for p in range(163, 179))
assert (N17, N18, N17 + N18) == (106, 75, 181), (N17, N18)
P146 = [plain(clean(x)) for x in he[145]]; P147 = plain(clean(he[146][0])); P162 = [plain(clean(x)) for x in he[161]]; P163 = plain(clean(he[162][0])); P178 = [plain(clean(x)) for x in he[177]]; P179 = plain(clean(he[178][0]))
assert not any(w in x for x in P146 for w in ('לא תזבח ליהוה אלהיך שור ושה', 'שור ושה אשר יהיה בו מום')), [x[:80] for x in P146]
assert P147.startswith('(דברים יז א) לא תזבח'), P147[:80]
assert not any(w in x for x in P162 for w in ('לא יהיה לכהנים הלוים', 'כל שבט לוי חלק ונחלה')), [x[:80] for x in P162]
assert P163.startswith('(דברים יח א)') and 'לא יהיה לכהנים' in P163[:60], P163[:80]
assert not any(w in x for x in P178 for w in ('כי יכרית יהוה אלהיך את הגוים', 'יכרית יהוה אלהיך')), [x[:80] for x in P178]
assert P179.startswith('(דברים יט א)'), P179[:80]
for p in SPINE:
    with open(f'{SP}/ch17_spine_p{p}.txt', 'w', encoding='utf-8') as f:
        for r in per[p]:
            h, he_, en_ = rows[(p, r)]
            f.write(f'--- {p}:{r} (head {h})\nHE: {he_}\nEN: {en_}\n')
TRUE_OUT = sorted(out)
assert all(p not in SPINE for p, _ in TRUE_OUT) and len(TRUE_OUT) == 11, TRUE_OUT
with open(f'{SP}/ch17_outside_rows.txt', 'w', encoding='utf-8') as f:
    for p, r in TRUE_OUT:
        d = out[(p, r)]; f.write(f'--- {p}:{r} (head {d["head"]}; cites chapter {sorted(d["cites"])})\nHE: {d.get("HE", "")}\nEN: {d.get("EN", "(no EN row)")}\n')
print('spine piskaot', SPINE[0], '-', SPINE[-1], len(SPINE), '| rows per piska', {p: len(per[p]) for p in SPINE}, '| totals', N17, N18, N17 + N18)
print('bytes per piska file', {p: os.path.getsize(f'{SP}/ch17_spine_p{p}.txt') for p in SPINE})
print('piska 162 rows (first 60 chars HE):', {(162, i + 1): x[:60] for i, x in enumerate(P162)}, '| 163:1 opens:', P163[:60])
print('piska 178 rows (first 60 chars HE):', {(178, i + 1): x[:60] for i, x in enumerate(P178)}, '| 179:1 opens:', P179[:60])
print('the outside rows', TRUE_OUT, '| bytes', os.path.getsize(f'{SP}/ch17_outside_rows.txt'), '| their heads and cites', {k: (out[k]['head'], sorted(out[k]['cites'])) for k in TRUE_OUT})
print('first 80 chars HE', {k: plain(out[k].get('HE', ''))[:80] for k in TRUE_OUT})
