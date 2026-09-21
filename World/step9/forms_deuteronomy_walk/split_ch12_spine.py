# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12: the spine file split by piska for the reading (chapter 11's form), WITH THE THREE HEADLESS PISKAOT 68, 73, 74
# folded in from the outside file (their rows open with 12:11's and 12:17's own words — chapter 11's lesson 2: a piska's membership is decided on the consonants);
# the seven true outside rows written to their own file. Nothing typed but the piska numbers read from the dump's print.
import os, re
SP = os.path.dirname(os.path.abspath(__file__))
spine = open(f'{SP}/ch12_sifrei_spine.txt', encoding='utf-8').read()
outside = open(f'{SP}/ch12_sifrei_outside.txt', encoding='utf-8').read()
rows = {}
for m in re.finditer(r'^--- (\d+):(\d+) \(head ([^)]*\)?)\)\nHE: (.*)\nEN: (.*)$', spine, re.M):
    rows[(int(m.group(1)), int(m.group(2)))] = (m.group(3), m.group(4), m.group(5))
blocks = re.split(r'^## Sifrei (\d+):(\d+)(?: \(head ([^\n]*)\))? (HE|EN)\n', outside, flags=re.M)   # the EN header carries no head part (read at the first run's print)
# re.split with groups yields [pre, p, r, head, lang, text, p, r, head, lang, text, ...]
out = {}
for i in range(1, len(blocks), 5):
    p, r, head, lang, text = int(blocks[i]), int(blocks[i + 1]), blocks[i + 2], blocks[i + 3], blocks[i + 4].strip('\n')
    out.setdefault((p, r), {})[lang] = text
    if head: out[(p, r)]['head'] = head
HEADLESS = [68, 73, 74]
for (p, r), d in sorted(out.items()):
    if p in HEADLESS: rows[(p, r)] = (d['head'], d.get('HE', ''), d.get('EN', '(no EN row)'))
SPINE = sorted({p for p, _ in rows})
assert SPINE == list(range(59, 82)), SPINE
per = {p: sorted(r for q, r in rows if q == p) for p in SPINE}
for p in SPINE:
    with open(f'{SP}/ch12_spine_p{p}.txt', 'w', encoding='utf-8') as f:
        for r in per[p]:
            h, he, en = rows[(p, r)]
            f.write(f'--- {p}:{r} (head {h})\nHE: {he}\nEN: {en}\n')
TRUE_OUT = sorted((p, r) for p, r in out if p not in HEADLESS)
with open(f'{SP}/ch12_outside_rows.txt', 'w', encoding='utf-8') as f:
    for p, r in TRUE_OUT:
        d = out[(p, r)]; f.write(f'--- {p}:{r} (head {d["head"]})\nHE: {d.get("HE", "")}\nEN: {d.get("EN", "(no EN row)")}\n')
print('spine piskaot', SPINE, '| rows per piska', {p: len(per[p]) for p in SPINE}, '| total', sum(len(v) for v in per.values()))
print('bytes per piska file', {p: os.path.getsize(f'{SP}/ch12_spine_p{p}.txt') for p in SPINE})
print('the headless piskaot rows (first 60 chars HE):', {(p, r): rows[(p, r)][1][:60] for p, r in sorted(rows) if p in HEADLESS})
print('the true outside rows', TRUE_OUT, '| bytes', os.path.getsize(f'{SP}/ch12_outside_rows.txt'))
