import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK sitting 14 — CHAPTER 16 (LEAN): the spine file split by piska for the reading (chapter 15's form, split_ch15_spine.py): the spine
# 127-146 WITH PISKA 135 FOLDED IN — its head row carries no citation in the Hebrew ("on the seventh day", 16:8's), so the dump's computed SPINE skipped it
# and listed its three rows among the outside rows; HEADLESS, IN THE SPINE BY POSITION (between 134 on 16:7 and 136 on 16:9). The tails on the consonants:
# 146's one row does not carry 17:1's words, 147:1 opens with 17:1's citation (sitting 11's lesson 1). The three true outside rows (52:4, 147:2, 281:1) to their own file.
import os, re, json, html, subprocess
SP = os.path.dirname(os.path.abspath(__file__))
ROOT = _ROOT
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(s): return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))   # the consonants — the export's rows are pointed (the dump's own plain)
spine = open(f'{SP}/ch16_sifrei_spine.txt', encoding='utf-8').read()
outside = open(f'{SP}/ch16_sifrei_outside.txt', encoding='utf-8').read()
rows = {}
for m in re.finditer(r'^--- (\d+):(\d+) \(head ([^)]*\)?)\)\nHE: (.*)\nEN: (.*)$', spine, re.M):
    rows[(int(m.group(1)), int(m.group(2)))] = (m.group(3), m.group(4), m.group(5))
blocks = re.split(r'^## Sifrei (\d+):(\d+)(?: \(head ([^\n]*)\))? (HE|EN)\n', outside, flags=re.M)   # the EN header carries no head part
out = {}
for i in range(1, len(blocks), 5):
    p, r, head, lang, text = int(blocks[i]), int(blocks[i + 1]), blocks[i + 2], blocks[i + 3], blocks[i + 4].strip('\n')
    out.setdefault((p, r), {})[lang] = text
    if head: out[(p, r)]['head'] = head
he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/he.json', encoding='utf-8'))['text']
en = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/en.json', encoding='utf-8'))['text']
SPINE = sorted({p for p, _ in rows})
assert SPINE == [p for p in range(127, 147) if p != 135], SPINE
# PISKA 135 FOLDED IN from the outside file (HEADLESS): its rows moved from `out` to `rows`
for (p, r), d in sorted(out.items()):
    if p == 135: rows[(p, r)] = ('None', d.get('HE', ''), d.get('EN', '(no EN row)'))
for k in [k for k in out if k[0] == 135]: del out[k]
SPINE = sorted({p for p, _ in rows})
assert SPINE == list(range(127, 147)), SPINE
per = {p: sorted(r for q, r in rows if q == p) for p in SPINE}
assert all(per[p] == list(range(1, len(he[p - 1]) + 1)) for p in SPINE), 'every row of every spine piska in the file'
assert sum(len(per[p]) for p in SPINE) == 111, sum(len(per[p]) for p in SPINE)
# THE TAILS ON THE CONSONANTS: piska 126's rows do not carry 16:1's words (chapter 15's own check, kept); piska 146's row does not carry 17:1's words; 147:1 opens with 17:1's citation
P126 = [plain(clean(x)) for x in he[125]]; P146 = [plain(clean(x)) for x in he[145]]; P147 = plain(clean(he[146][0]))
assert not any(w in x for x in P126 for w in ('שמור את חדש האביב', 'חדש האביב')), [x[:80] for x in P126]
assert not any(w in x for x in P146 for w in ('לא תזבח ליהוה אלהיך שור ושה', 'שור ושה אשר יהיה בו מום')), [x[:80] for x in P146]
assert P147.startswith('(דברים יז א) לא תזבח'), P147[:80]
for p in SPINE:
    with open(f'{SP}/ch16_spine_p{p}.txt', 'w', encoding='utf-8') as f:
        for r in per[p]:
            h, he_, en_ = rows[(p, r)]
            f.write(f'--- {p}:{r} (head {h})\nHE: {he_}\nEN: {en_}\n')
TRUE_OUT = sorted(out)
assert all(p not in SPINE for p, _ in TRUE_OUT) and len(TRUE_OUT) == 3 and TRUE_OUT == [(52, 4), (147, 2), (281, 1)], TRUE_OUT
with open(f'{SP}/ch16_outside_rows.txt', 'w', encoding='utf-8') as f:
    for p, r in TRUE_OUT:
        d = out[(p, r)]; f.write(f'--- {p}:{r} (head {d["head"]})\nHE: {d.get("HE", "")}\nEN: {d.get("EN", "(no EN row)")}\n')
print('spine piskaot', SPINE, '| rows per piska', {p: len(per[p]) for p in SPINE}, '| total', sum(len(v) for v in per.values()))
print('bytes per piska file', {p: os.path.getsize(f'{SP}/ch16_spine_p{p}.txt') for p in SPINE})
print('piska 135 rows (HEADLESS, folded in; first 90 chars HE):', {(135, r): plain(clean(he[134][r - 1]))[:90] for r in range(1, len(he[134]) + 1)})
print('piska 146 rows (first 70 chars HE):', {(146, i + 1): x[:70] for i, x in enumerate(P146)}, '| 147:1 opens:', P147[:60])
print('the outside rows', TRUE_OUT, '| bytes', os.path.getsize(f'{SP}/ch16_outside_rows.txt'), '| their heads', {k: out[k]['head'] for k in TRUE_OUT}, '| first 70 chars HE', {k: plain(out[k].get('HE', ''))[:70] for k in TRUE_OUT})
