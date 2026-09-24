import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 14 — CHAPTER 16 (LEAN, 2026-09-23): the store's glosses at the chapter's seats read back into the display layer's override file
# — BY GLOSS where the store's every token of the gloss is the one word or one family read the same at every seat (the families PROBED FIRST by ch16_patch_probe.py,
# the counts read from its print), BY REFERENCE at the chapter's own seats where the family is mixed. THE LEAN FORM: the worst glosses only; the rest OWED to the
# full process. Display only; the draft unit untouched. Run ONCE (the anchors assert the rows absent first). Sitting 13's form (ch15_patch_overrides.py): the
# anchors the LAST ROWS of sitting 13's two blocks — the by_gloss block's last row found by walking from sitting 13's marker (never typed), the by_ref block's
# last row 15:23's. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad; after the freeze chain (the yaml is not touched while the ritual runs).
import os, re, subprocess, sys, io, contextlib, yaml
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
with contextlib.redirect_stdout(io.StringIO()):
    import ch16_ink as I
GL = [('pretermission', 'Passover'), ('the-pretermission', 'the-Passover'), ('the-sweetness', 'the-unleavened-bread'), ('barm', 'leaven'), ('the-sevened', 'the-weeks'), ('the-donation', 'the-bribe'), ('something-stationed', 'a-pillar'), ('in-hasty-flight', 'in-haste'), ('to-score-with-a-mark-as-a-tally', 'to-count'), ('from-bore', 'from-the-beginning-of'), ('to-scion-you/your', 'for-your-tribes'), ('in-gather-for-any-purpose-you/your', 'when-you-gather-in'), ('from-threshing-floor-you/your', 'from-your-threshing-floor'), ('blithe', 'joyful'), ('to-tent-you/your', 'to-your-tents'), ('male-you/your', 'your-males'), ("'Asherah", 'an-Asherah'), ('alive-you/your', 'your-life'), ('to-morning', 'until-morning'), ('in-new-moon', 'in-the-month-of'), ('the-hut', 'the-booths'), ('seasons', 'the-appointed-time-of'), ('and-boil-up', 'and-you-shall-cook'), ('like-benediction-x', None)]
GL = [(g, v) for g, v in GL if v]   # the probe's one-family glosses (or one family read the same): 'the-hut' two spellings of booths; 'seasons' the one root; 'and-boil-up' two forms of the one verb
SPEC = [(1, 'שמור', 'observe', 0), (1, 'חדש', 'the-month-of', 0), (1, 'האביב', 'the-Aviv', 0), (1, 'האביב', 'the-Aviv', 1), (1, 'ועשית', 'and-you-shall-keep', 0), (1, 'כי', 'for', 0), (1, 'הוציאך', 'He-brought-you-out', 0),
        (2, 'וזבחת', 'and-you-shall-sacrifice', 0), (2, 'שמו', 'His-name', 0),
        (3, 'מצות', 'unleavened-bread', 0), (3, 'עני', 'affliction', 0), (3, 'כי', 'for', 0), (3, 'יצאת', 'you-went-out', 0), (3, 'תזכר', 'you-shall-remember', 0), (3, 'צאתך', 'your-going-out', 0), (3, 'ימי', 'the-days-of', 0), (3, 'ימים', 'days', 0), (3, 'מארץ', 'from-the-land-of', 0), (3, 'מארץ', 'from-the-land-of', 1),
        (4, 'ימים', 'days', 0), (4, 'ילין', 'remain-overnight', 0), (4, 'תזבח', 'you-sacrifice', 0),
        (5, 'לזבח', 'to-sacrifice', 0),
        (6, 'כי', 'but', 0), (6, 'אם', 'only', 0), (6, 'שמו', 'His-name', 0), (6, 'תזבח', 'you-shall-sacrifice', 0), (6, 'כבוא', 'at-the-going-down-of', 0), (6, 'צאתך', 'your-going-out', 0),
        (8, 'מצות', 'unleavened-bread', 0), (8, 'עצרת', 'a-solemn-assembly', 0), (8, 'תעשה', 'you-shall-do', 0),
        (9, 'שבעת', 'weeks', 0), (9, 'תספר', 'you-shall-count', 0), (9, 'בקמה', 'on-the-standing-grain', 0), (9, 'תחל', 'you-shall-begin', 0), (9, 'שבעות', 'weeks', 0),
        (10, 'ועשית', 'and-you-shall-keep', 0), (10, 'חג', 'the-feast-of', 0), (10, 'שבעות', 'weeks', 0), (10, 'מסת', 'the-measure-of', 0), (10, 'נדבת', 'the-freewill-offering-of', 0), (10, 'תתן', 'you-give', 0),
        (11, 'לפני', 'before', 0), (11, 'ובנך', 'and-your-son', 0), (11, 'ובתך', 'and-your-daughter', 0), (11, 'ועבדך', 'and-your-manservant', 0), (11, 'שמו', 'His-name', 0),
        (12, 'עבד', 'a-slave', 0), (12, 'היית', 'you-were', 0), (12, 'ושמרת', 'and-you-shall-keep', 0), (12, 'ועשית', 'and-do', 0),
        (13, 'חג', 'the-feast-of', 0), (13, 'תעשה', 'you-shall-keep', 0), (13, 'ימים', 'days', 0),
        (14, 'בחגך', 'in-your-feast', 0), (14, 'ובנך', 'and-your-son', 0), (14, 'ובתך', 'and-your-daughter', 0), (14, 'ועבדך', 'and-your-manservant', 0),
        (15, 'ימים', 'days', 0), (15, 'תחג', 'you-shall-keep-the-feast', 0), (15, 'כי', 'for', 0), (15, 'ידיך', 'your-hands', 0), (15, 'והיית', 'and-you-shall-be', 0),
        (16, 'פעמים', 'times', 0), (16, 'בשנה', 'in-the-year', 0), (16, 'יראה', 'shall-appear', 0), (16, 'פני', 'the-face-of', 0), (16, 'בחג', 'at-the-feast-of', 0), (16, 'ובחג', 'and-at-the-feast-of', 0), (16, 'ובחג', 'and-at-the-feast-of', 1), (16, 'יראה', 'shall-he-appear', 1), (16, 'פני', 'the-face-of', 1),
        (17, 'איש', 'each-man', 0), (17, 'כמתנת', 'according-to-the-gift-of', 0), (17, 'ידו', 'his-hand', 0), (17, 'נתן', 'He-has-given', 0),
        (18, 'שפטים', 'judges', 0), (18, 'תתן', 'you-shall-set', 0), (18, 'נתן', 'gives', 0), (18, 'ושפטו', 'and-they-shall-judge', 0), (18, 'צדק', 'righteous', 0),
        (19, 'תטה', 'you-shall-wrest', 0), (19, 'תכיר', 'you-shall-respect', 0), (19, 'פנים', 'persons', 0), (19, 'תקח', 'you-shall-take', 0), (19, 'כי', 'for', 0), (19, 'יעור', 'blinds', 0), (19, 'עיני', 'the-eyes-of', 0), (19, 'חכמים', 'the-wise', 0), (19, 'ויסלף', 'and-perverts', 0), (19, 'דברי', 'the-words-of', 0), (19, 'צדיקם', 'the-righteous', 0),
        (20, 'צדק', 'justice', 0), (20, 'צדק', 'justice', 1), (20, 'תרדף', 'you-shall-pursue', 0), (20, 'הארץ', 'the-land', 0), (20, 'נתן', 'gives', 0),
        (21, 'אצל', 'beside', 0), (21, 'מזבח', 'the-altar-of', 0), (21, 'תעשה', 'you-shall-make', 0),
        (22, 'תקים', 'you-shall-set-up', 0), (22, 'שנא', 'hates', 0)]
REF3 = [(f'Deut.16.{v}:{I.sidx(16, v, tok, nth)}', new, tok) for v, tok, new, nth in SPEC]
REF = [(k, v) for k, v, _ in REF3]; TOK = {k: t for k, _, t in REF3}
assert len(REF) == len({k for k, _ in REF}) == len(SPEC) and len(GL) == len({g for g, _ in GL})
assert all(I.sg(16, v, tok, nth) != new for v, tok, new, nth in SPEC), [(v, tok) for v, tok, new, nth in SPEC if I.sg(16, v, tok, nth) == new]   # no row rewrites a gloss to itself
assert all(I.sg(16, v, tok, nth) not in dict(GL) for v, tok, _, nth in SPEC), [(v, tok, I.sg(16, v, tok, nth)) for v, tok, _, nth in SPEC if I.sg(16, v, tok, nth) in dict(GL)]   # a seat patched by gloss is not patched again by reference
P = f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'
t = open(P, encoding='utf-8').read()
d0 = yaml.safe_load(t); BG0 = d0['by_gloss']
assert '"Deut.16.' not in t and all(g not in BG0 for g, _ in GL), [g for g, _ in GL if g in BG0]
MARK = 'THE DEUTERONOMY WALK sitting 14 (2026-09-23, Deuteronomy 16, LEAN)'
assert MARK not in t
M13 = 'THE DEUTERONOMY WALK sitting 13 (2026-09-22, Deuteronomy 15)'
i = t.index(f'  # {M13}: the store\'s glosses whose every token')
j = t.index('\n', i) + 1
rows = []
while True:
    m = re.match(r'  "[^"]+": "[^"]*"[^\n]*\n', t[j:])
    if not m: break
    rows.append(m.group(0)); j += len(m.group(0))
assert len(rows) == 44, len(rows)   # sitting 13's forty-four by-gloss rows (its patch print)
A1 = rows[-1]; assert t.count(A1) == 1
gl_block = A1 + f'\n  # {MARK}: the worst glosses of the chapter\'s seats, the families probed in the store first (ch16_patch_probe.py) — the lean form\'s patch; the rest OWED (COMPILE_DEBT\'s lean-pass box)\n' + ''.join(f'  "{k}": "{v}"\n' for k, v in GL)
t = t.replace(A1, gl_block)
m2 = re.search(r'^  "Deut\.15\.23:7": "you-shall-pour-it"[^\n]*\n', t, re.M); assert m2 and t.count('"Deut.15.23:7": "you-shall-pour-it"') == 1
A2 = m2.group(0)
ref_block = A2 + f'  # {MARK}: the chapter\'s seats by reference — the token named beside each; the indices the store\'s own\n' + ''.join(f'  "{k}": "{v}"   # {TOK[k]}\n' for k, v in REF)
t = t.replace(A2, ref_block)
open(P, 'w', encoding='utf-8').write(t)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert all(d['by_ref'][k] == v for k, v in REF) and all(d['by_gloss'][k] == v for k, v in GL)
print('override rows written: by_ref', len(REF), 'by_gloss', len(GL), '| by_ref total', len(d['by_ref']), '| by_gloss total', len(d['by_gloss']))
