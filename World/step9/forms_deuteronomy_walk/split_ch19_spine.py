import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK sitting 16 — CHAPTERS 19-21 (LEAN, 2026-09-24): the three spine files split by piska for the reading (sitting 15's form, split_ch17_spine.py,
# joined over THREE chapters): the spine 179-221 — 179-190 chapter 19's TWELVE piskaot (ten heads + TWO HEADLESS, 183 inside 19:5-7 and 187 inside 19:12-13, the
# dumps' prints: "head None"), 191-204 chapter 20's fourteen (192 a variant piska heading on 20:8 between 20:2 and 20:4 — the heads NOT in verse order), 205-221
# chapter 21's seventeen; the headless piskaot read WHOLE from the export (the dumps list only their citing rows, among the outside rows); the outside rows the
# UNION of the three dumps' outside sets less the spine (190:16-21 cite 20:1 — chapter 19's piska running past its chapter's end, sitting 11's lesson). The tails
# on the consonants: 178's rows do not carry 19:1's words (sitting 15's check, kept); 190's rows carry 20:1's (the run past — asserted present); 204's rows do not
# carry 21:1's; 221's rows do not carry 22:1's; 179:1 and 205:1 open with their verses' citations; 191:1's and 222:1's openings PRINTED (typed after).
import os, re, json, html, subprocess
SP = os.path.dirname(os.path.abspath(__file__))
ROOT = _ROOT
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/he.json', encoding='utf-8'))['text']
en = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/en.json', encoding='utf-8'))['text']
HEADLESS = {183: 'headless — inside 19:5-7 (the ax and the iron, the pursuit)', 187: 'headless — inside 19:12-13 (the elders send, the eye does not pity)'}
rows, out = {}, {}
for ch in (19, 20, 21):
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
# THE HEADLESS PISKAOT read whole from the export (their rows among the outside sets are the spine's)
for p, why in HEADLESS.items():
    assert len(he[p - 1]) == len(en[p - 1]), (p, len(he[p - 1]), len(en[p - 1]))
    for r in range(1, len(he[p - 1]) + 1):
        assert (p, r) not in rows
        rows[(p, r)] = (f'None; {why}', clean(he[p - 1][r - 1]), clean(en[p - 1][r - 1]))
SPINE = sorted({p for p, _ in rows})
assert SPINE == list(range(179, 222)), SPINE
for k in [k for k in out if k[0] in SPINE]: assert k in rows, k; del out[k]
per = {p: sorted(r for q, r in rows if q == p) for p in SPINE}
assert all(per[p] == list(range(1, len(he[p - 1]) + 1)) for p in SPINE), 'every row of every spine piska in the files'
N19 = sum(len(per[p]) for p in range(179, 191)); N20 = sum(len(per[p]) for p in range(191, 205)); N21 = sum(len(per[p]) for p in range(205, 222))
assert (N19, N20, N21, N19 + N20 + N21) == (75, 65, 120, 260), (N19, N20, N21)
HB = lambda p: [plain(clean(x)) for x in he[p - 1]]
P178, P179, P190, P191, P204, P205, P221, P222 = HB(178), HB(179), HB(190), HB(191), HB(204), HB(205), HB(221), HB(222)
assert not any(w in x for x in P178 for w in ('כי יכרית יהוה אלהיך את הגוים', 'יכרית יהוה אלהיך')), [x[:80] for x in P178]
assert P179[0].startswith('(דברים יט א) כי יכרית'), P179[0][:80]
assert any('כי תצא למלחמה' in x for x in P190[15:]), [x[:80] for x in P190[15:]]   # the piska runs past into 20:1
assert not any('כי ימצא חלל' in x for x in P204), [x[:80] for x in P204]
assert P205[0].startswith('(דברים כא א) כי ימצא'), P205[0][:80]
assert not any(w in x for x in P221 for w in ('לא תראה את שור', 'שור אחיך או את שיו')), [x[:80] for x in P221]
for p in SPINE:
    with open(f'{SP}/ch19_spine_p{p}.txt', 'w', encoding='utf-8') as f:
        for r in per[p]:
            h, he_, en_ = rows[(p, r)]
            f.write(f'--- {p}:{r} (head {h})\nHE: {he_}\nEN: {en_}\n')
TRUE_OUT = sorted(out)
assert all(p not in SPINE for p, _ in TRUE_OUT) and len(TRUE_OUT) == 11, TRUE_OUT
with open(f'{SP}/ch19_outside_rows.txt', 'w', encoding='utf-8') as f:
    for p, r in TRUE_OUT:
        d = out[(p, r)]; f.write(f'--- {p}:{r} (head {d.get("head")}; cites chapter {sorted(d["cites"])})\nHE: {d.get("HE", "")}\nEN: {d.get("EN", "(no EN row)")}\n')
print('spine piskaot', SPINE[0], '-', SPINE[-1], len(SPINE), '| rows per piska', {p: len(per[p]) for p in SPINE}, '| totals', N19, N20, N21, N19 + N20 + N21)
print('bytes per piska file', {p: os.path.getsize(f'{SP}/ch19_spine_p{p}.txt') for p in SPINE}, '| by chapter', {c: sum(os.path.getsize(f'{SP}/ch19_spine_p{p}.txt') for p in ps) for c, ps in ((19, range(179, 191)), (20, range(191, 205)), (21, range(205, 222)))})
print('183:1 opens:', HB(183)[0][:90], '| 187:1 opens:', HB(187)[0][:90], '| 186 rows (first 60):', [x[:60] for x in HB(186)])
print('190 rows 16-21 (first 70 chars HE):', {(190, i + 16): x[:70] for i, x in enumerate(P190[15:])})
print('191:1 opens:', P191[0][:90], '| 204 rows (first 60):', [x[:60] for x in P204], '| 205:1 opens:', P205[0][:70])
print('221 rows (first 50):', [x[:50] for x in P221], '| 222:1 opens:', P222[0][:100], '| 222 rows', len(P222))
print('the outside rows', TRUE_OUT, '| bytes', os.path.getsize(f'{SP}/ch19_outside_rows.txt'), '| their heads and cites', {k: (out[k].get('head'), sorted(out[k]['cites'])) for k in TRUE_OUT})
print('first 80 chars HE', {k: plain(out[k].get('HE', ''))[:80] for k in TRUE_OUT})
