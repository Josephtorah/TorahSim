import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK sitting 12 — CHAPTER 14: the spine file split by piska for the reading (chapter 13's form), WITH PISKA 96's TAIL (rows 9-12 — 14:1's:
# 96:9, 96:11 and 96:12 in the outside file by their citations of 14:1; 96:10 cites Amos 9:6 alone and is FETCHED FROM THE EXPORT and folded by the consonant
# rule — sitting 11's lesson 1, chapter 11's lesson 2 a sixth time: a piska's membership is decided on the consonants); the three true outside rows written to
# their own file. Nothing typed but the piska numbers read from the dump's print (97-110; 96's rows 9-12).
import os, re, json, html, subprocess
SP = os.path.dirname(os.path.abspath(__file__))
ROOT = _ROOT
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))   # the consonants — the export's rows are pointed (the dump's own plain)
spine = open(f'{SP}/ch14_sifrei_spine.txt', encoding='utf-8').read()
outside = open(f'{SP}/ch14_sifrei_outside.txt', encoding='utf-8').read()
rows = {}
for m in re.finditer(r'^--- (\d+):(\d+) \(head ([^)]*\)?)\)\nHE: (.*)\nEN: (.*)$', spine, re.M):
    rows[(int(m.group(1)), int(m.group(2)))] = (m.group(3), m.group(4), m.group(5))
blocks = re.split(r'^## Sifrei (\d+):(\d+)(?: \(head ([^\n]*)\))? (HE|EN)\n', outside, flags=re.M)   # the EN header carries no head part
out = {}
for i in range(1, len(blocks), 5):
    p, r, head, lang, text = int(blocks[i]), int(blocks[i + 1]), blocks[i + 2], blocks[i + 3], blocks[i + 4].strip('\n')
    out.setdefault((p, r), {})[lang] = text
    if head: out[(p, r)]['head'] = head
TAIL = [(96, 9), (96, 10), (96, 11), (96, 12)]   # piska 96's tail on 14:1 — sitting 11 left them (asserted there on the rows' own bytes)
he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/he.json', encoding='utf-8'))['text']
en = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/en.json', encoding='utf-8'))['text']
assert len(he[95]) == 12 and len(en[95]) == 12, (len(he[95]), len(en[95]))
for p, r in TAIL:
    h, e = clean(he[p - 1][r - 1]), clean(en[p - 1][r - 1])
    if (p, r) in out: assert out[(p, r)].get('HE', '') == h, (p, r, 'the outside file and the export differ')
    rows[(p, r)] = ("(13, 17) — THE TAIL ON 14:1", h, e)
assert (96, 10) not in out and all(k in out for k in ((96, 9), (96, 11), (96, 12))), sorted(k for k in out if k[0] == 96)
assert 'בנים אתם' in plain(rows[(96, 9)][1]), plain(rows[(96, 9)][1])[:80]   # 96:9 opens with 14:1's citation
assert any(w in plain(rows[(96, 10)][1]) for w in ('תתגדדו', 'תתגודדו', 'קרחה', 'אגדות', 'אגודות')), plain(rows[(96, 10)][1])[:120]   # 96:10 — 14:1's clause by the consonants (the Amos citation its only bracket)
assert all(w not in plain(rows[(96, 8)][1]) for w in ('בנים אתם', 'תתגדדו')) if (96, 8) in rows else True
SPINE = sorted({p for p, _ in rows})
assert SPINE == list(range(96, 111)), SPINE
per = {p: sorted(r for q, r in rows if q == p) for p in SPINE}
assert per[96] == [9, 10, 11, 12] and sum(len(per[p]) for p in range(97, 111)) == 107, (per[96], sum(len(per[p]) for p in range(97, 111)))
for p in SPINE:
    with open(f'{SP}/ch14_spine_p{p}.txt', 'w', encoding='utf-8') as f:
        for r in per[p]:
            h, he_, en_ = rows[(p, r)]
            f.write(f'--- {p}:{r} (head {h})\nHE: {he_}\nEN: {en_}\n')
TRUE_OUT = sorted((p, r) for p, r in out if p != 96)
with open(f'{SP}/ch14_outside_rows.txt', 'w', encoding='utf-8') as f:
    for p, r in TRUE_OUT:
        d = out[(p, r)]; f.write(f'--- {p}:{r} (head {d["head"]})\nHE: {d.get("HE", "")}\nEN: {d.get("EN", "(no EN row)")}\n')
print('spine piskaot', SPINE, '| rows per piska', {p: len(per[p]) for p in SPINE}, '| total', sum(len(v) for v in per.values()))
print('bytes per piska file', {p: os.path.getsize(f'{SP}/ch14_spine_p{p}.txt') for p in SPINE})
print('piska 96 rows 8-12 (first 90 chars HE — where 14:1 begins):', {(96, r): plain(clean(he[95][r - 1]))[:90] for r in range(8, 13)})
print('the tail rows (first 60 chars EN):', {(p, r): rows[(p, r)][2][:60] for p, r in TAIL})
print('the true outside rows', TRUE_OUT, '| bytes', os.path.getsize(f'{SP}/ch14_outside_rows.txt'), '| their heads', {k: out[k]['head'] for k in TRUE_OUT}, '| first 60 chars HE', {k: out[k].get('HE', '')[:60] for k in TRUE_OUT})
