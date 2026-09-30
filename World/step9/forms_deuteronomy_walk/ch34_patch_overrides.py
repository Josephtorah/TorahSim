import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 22 — CHAPTER 34, THE DEATH OF MOSES (LEAN, 2026-09-30; THE TAIL): the store's glosses at the chapter's seats read back into the display
# layer's override file — BY GLOSS where the store's every token of the gloss is the one word read the same at every seat (the families PROBED FIRST by ch34_patch_probe.py,
# the counts read from its print: "his natural force", "was dim", "his grave", "from the plains of", "when he died" (two tokens — Aaron's at Numbers 33:39 and Moses' at
# 34:7, the same words), "the plain" (seven — Sodom's and Jericho's), "the palms", "to your seed" (seven), "the weeping of"), BY REFERENCE at the chapter's own seats where
# the family is mixed — the nine acts' verbs (and went up, and showed him, and said, and died, and wept, and were ended, and hearkened, and did, arose), THE ONE "?" SEAT
# (34:6's "house" of Beth-peor — blanked by an earlier walk's by-gloss row "?" -> ""; written "Beth" and "Peor" by reference as 3:29 and 4:46 were), the oath's first
# person (I swore, I will give it, I have caused you to see), "you shall cross over", "the servant of", "according to the mouth of", "aged" and "the children of", the
# days of weeping and the mourning, "for", "since", "knew him", "wrought", "the terror", "in the sight of". "Daniel" -> "Dan", "the-seas" -> "the-sea", "in-gorge" ->
# "in-the-valley", "and-inter" -> "and-bury", "prop" -> "lay" ALREADY by gloss from earlier walks (the design's candidates, found in force). THE LEAN FORM: the worst
# glosses only; the rest OWED. Display only; the frozen unit untouched. Run ONCE (the anchors assert the rows absent first). Sitting 21's form (ch33_patch_overrides.py):
# the anchors the LAST ROWS of sitting 21's two blocks — the by_gloss block's last row found by walking from sitting 21's marker (never typed), the by_ref block's last
# row 33:24's "he said". Every by-reference row carries the OLD gloss and asserts it at the seat. RUN FROM THE REPO ROOT; after the freeze chain.
import re, sqlite3, subprocess, yaml
ROOT = _ROOT
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for v, i, hp, g in store.execute("SELECT v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=34 ORDER BY v.id, w.idx"):
    SG.setdefault(v, []).append((i, hp.replace('/', ''), g))
def sg(v, tok, nth=0):
    hit = [g for _, hp, g in SG[v] if hp == tok]; assert len(hit) > nth, (v, tok, nth, hit); return hit[nth]
def sidx(v, tok, nth=0):
    hit = [i for i, hp, _ in SG[v] if hp == tok]; assert len(hit) > nth, (v, tok, nth, hit); return hit[nth]
GL0 = [('be-weak', 'was-dim'), ('freshness-him/its', 'his-natural-force'), ('from-desert', 'from-the-plains-of'), ('in-death-him/its', 'when-he-died'), ('sepulture-him/its', 'his-grave'),
       ('the-circle', 'the-plain'), ('the-palm-tree', 'the-palms'), ('to-seed-you/your', 'to-your-seed'), ('weeping', 'the-weeping-of')]
ACTS = ('and-go-up', 'and-see-him/its', 'and-say', 'and-die', 'and-weep', 'and-complete', 'and-hear', 'and-make', 'arise')
P = f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'
t = open(P, encoding='utf-8').read()
d0 = yaml.safe_load(t); BG0 = d0['by_gloss']
DROP = [g for g, _ in GL0 if g in BG0]; GL = [(g, n) for g, n in GL0 if g not in BG0]
print('by-gloss candidates already rewritten by an earlier walk (dropped):', DROP)
SPEC = [
 (1, 'ויעל', 'and-went-up', 0, 'and-go-up'), (1, 'ראש', 'the-top-of', 0, 'head'), (1, 'פני', 'against', 0, 'face'), (1, 'ויראהו', 'and-showed-him', 0, 'and-see-him/its'), (1, 'הארץ', 'the-land', 0, 'the-earth'), (1, 'עד', 'as-far-as', 0, 'until'),
 (2, 'עד', 'as-far-as', 0, 'until'), (3, 'עד', 'as-far-as', 0, 'until'), (3, 'בקעת', 'the-valley-of', 0, 'split'),
 (4, 'ויאמר', 'and-said', 0, 'and-say'), (4, 'אליו', 'to-him', 0, 'to-him/its'), (4, 'הארץ', 'the-land', 0, 'the-earth'), (4, 'נשבעתי', 'I-swore', 0, 'swear'), (4, 'אתננה', 'I-will-give-it', 0, 'set-her/its'), (4, 'הראיתיך', 'I-have-caused-you-to-see', 0, 'see-you/your'), (4, 'תעבר', 'you-shall-cross-over', 0, 'pass-over'),
 (5, 'וימת', 'and-died', 0, 'and-die'), (5, 'עבד', 'the-servant-of', 0, 'servant'), (5, 'על', 'according-to', 0, 'over'), (5, 'פי', 'the-mouth-of', 0, 'mouth'),
 (6, 'בית', 'Beth', 0, '?'), (6, 'פעור', 'Peor', 0, 'Bethpeor'), (6, 'ידע', 'knows', 0, 'know'), (6, 'עד', 'unto', 0, 'until'), (6, 'הזה', 'this', 0, 'the-this'),
 (7, 'בן', 'aged', 0, 'son'), (7, 'עינו', 'his-eye', 0, 'eye-him/its'),
 (8, 'ויבכו', 'and-wept', 0, 'and-weep'), (8, 'בני', 'the-children-of', 0, 'son'), (8, 'בערבת', 'in-the-plains-of', 0, 'in-desert'), (8, 'יום', 'days', 0, 'day'), (8, 'ימי', 'the-days-of', 0, 'day'), (8, 'אבל', 'the-mourning-for', 0, 'lamentation'), (8, 'ויתמו', 'and-were-ended', 0, 'and-complete'),
 (9, 'בן', 'the-son-of', 0, 'son'), (9, 'מלא', 'full-of', 0, 'full'), (9, 'כי', 'for', 0, 'that'), (9, 'ידיו', 'his-hands', 0, 'hand-him/its'), (9, 'עליו', 'upon-him', 0, 'over-him/its'), (9, 'וישמעו', 'and-hearkened', 0, 'and-hear'), (9, 'אליו', 'to-him', 0, 'to-him/its'), (9, 'בני', 'the-children-of', 0, 'son'), (9, 'ויעשו', 'and-did', 0, 'and-make'), (9, 'צוה', 'commanded', 0, 'command'),
 (10, 'קם', 'arose', 0, 'arise'), (10, 'עוד', 'since', 0, 'still/again'), (10, 'ידעו', 'knew-him', 0, 'know-him/its'),
 (11, 'שלחו', 'sent-him', 0, 'send-him/its'), (11, 'לעשות', 'to-do', 0, 'to-make'), (11, 'עבדיו', 'his-servants', 0, 'servant-him/its'), (11, 'והמופתים', 'and-the-wonders', 0, 'and-the-miracle'),
 (12, 'עשה', 'wrought', 0, 'make'), (12, 'המורא', 'the-terror', 0, 'the-fear'), (12, 'לעיני', 'in-the-sight-of', 0, 'to-eye')]
bad = [(v, tok, nth, sg(v, tok, nth), old) for v, tok, new, nth, old in SPEC if sg(v, tok, nth) != old]; assert not bad, bad   # the old gloss at the seat as read
REF3 = [(f'Deut.34.{v}:{sidx(v, tok, nth)}', new, tok) for v, tok, new, nth, old in SPEC]
REF = [(k, v) for k, v, _ in REF3]; TOK = {k: t_ for k, _, t_ in REF3}
assert len(REF) == len({k for k, _ in REF}) == len(SPEC) and len(GL) == len({g for g, _ in GL})
assert all(sg(v, tok, nth) != new for v, tok, new, nth, old in SPEC)   # no row rewrites a gloss to itself
CLASH = [(v, tok, old) for v, tok, _, nth, old in SPEC if old in dict(GL)]; assert not CLASH, CLASH   # a seat patched by gloss is not patched again by reference
GLSEATS = {g: [(v, i, hp) for v, L in SG.items() for i, hp, gg in L if gg == g] for g, _ in GL}; NOSEAT = [g for g, s in GLSEATS.items() if not s]; assert not NOSEAT, NOSEAT   # every by-gloss row has a seat in the chapter
QSEATS = [(v, i, hp) for v, L in SG.items() for i, hp, g in L if g == '?']; assert QSEATS == [(6, 6, 'בית')], QSEATS   # the one "?" seat — the house of Beth-peor
assert not re.search(r'"Deut\.34\.', t) and all(g not in BG0 for g, _ in GL)
MARK = 'THE DEUTERONOMY WALK sitting 22 (2026-09-30, Deuteronomy 34, LEAN)'
assert MARK not in t
M21 = 'THE DEUTERONOMY WALK sitting 21 (2026-09-29, Deuteronomy 33, LEAN)'
i = t.index(f'  # {M21}: the worst glosses of the blessing\'s seats')
j = t.index('\n', i) + 1
rows = []
while True:
    m = re.match(r'  "[^"]+": "[^"]*"[^\n]*\n', t[j:])
    if not m: break
    rows.append(m.group(0)); j += len(m.group(0))
assert len(rows) == 71, len(rows)   # sitting 21's by-gloss rows (the probe's walk 71)
A1 = rows[-1]; assert t.count(A1) == 1
gl_block = A1 + f'\n  # {MARK}: the worst glosses of the death\'s seats, the families probed in the store first (ch34_patch_probe.py) — the lean form\'s patch; the rest OWED (COMPILE_DEBT\'s lean-pass box)\n' + ''.join(f'  "{k}": "{v}"\n' for k, v in GL)
t = t.replace(A1, gl_block)
m2 = re.search(r'^  "Deut\.33\.24:1": "he-said"[^\n]*\n', t, re.M); assert m2 and t.count('"Deut.33.24:1": "he-said"') == 1
A2 = m2.group(0)
ref_block = A2 + f'  # {MARK}: the chapter\'s seats by reference — the token named beside each; the indices the store\'s own (the one "?" seat at 34:6 — the house of Beth-peor, "Beth" and "Peor" as at 3:29 and 4:46; the nine acts\' verbs; the oath\'s first person; the servant of the LORD and according to the mouth of; aged a hundred and twenty; the children of Israel; the days of weeping and the mourning for Moses; the terror in the sight of all Israel; the old gloss asserted at every seat)\n' + ''.join(f'  "{k}": "{v}"   # {TOK[k]}\n' for k, v in REF)
t = t.replace(A2, ref_block)
open(P, 'w', encoding='utf-8').write(t)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert all(d['by_ref'][k] == v for k, v in REF) and all(d['by_gloss'][k] == v for k, v in GL)
print('override rows written: by_ref', len(REF), 'by_gloss', len(GL), '| by_ref total', len(d['by_ref']), '| by_gloss total', len(d['by_gloss']), '| dropped (already by gloss)', len(DROP), '| the "?" seat by reference', sum(1 for _, _, _, _, old in SPEC if old == '?'), '| the acts\' verbs by reference', sum(1 for _, _, _, _, old in SPEC if old in ACTS), '| by-gloss seats in the chapter', sum(len(s) for s in GLSEATS.values()), '| by-gloss tokens over the store', sum(len(store.execute("SELECT 1 FROM words w WHERE w.gloss=?", (g,)).fetchall()) for g, _ in GL))
