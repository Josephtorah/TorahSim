import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 15 — CHAPTERS 17-18 (LEAN, 2026-09-24): the store's glosses at the two chapters' seats read back into the display layer's override
# file — BY GLOSS where the store's every token of the gloss is the one word or one family read the same at every seat (the families PROBED FIRST by
# ch17_patch_probe.py, the counts read from its print; the glosses the earlier walks already rewrote by gloss excluded), BY REFERENCE at the chapters' own seats
# where the family is mixed (three self-rewrites dropped on the first run — the store already reads 'and-fear', 'turn-aside', 'to-stand'; four by-gloss rows the earlier walks already carry dropped on the second). THE LEAN FORM: the worst glosses only; the rest OWED. Display only; the draft units untouched. Run ONCE (the anchors assert the rows
# absent first). Sitting 14's form (ch16_patch_overrides.py): the anchors the LAST ROWS of sitting 14's two blocks — the by_gloss block's last row found by walking
# from sitting 14's marker (never typed), the by_ref block's last row 16:22's. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad; after the freeze chain.
import os, re, subprocess, sys, io, contextlib, yaml
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
with contextlib.redirect_stdout(io.StringIO()):
    import ch17_ink as I
GL = [('like-smoothness', 'as-a-portion'), ('the-die', 'the-dead'), ('dark', 'left'), ('seethe-suffix', 'act-presumptuously'), ('mumble', 'a-ghost'), ('like-something-disgusting', 'like-the-abominations-of'), ('in-arrogance', 'presumptuously'), ('flow-as-water-you/your', 'they-teach-you'), ('writing', 'a-book'), ('the-arm', 'the-shoulder'), ('and-the-paunch', 'and-the-maw'), ('and-the-cheek', 'and-the-cheeks'), ('to-attend-as-a-menial', 'to-minister'), ('and-hiss', 'and-an-omen-reader'), ('and-whisper-aspell', 'and-a-sorcerer'), ('society', 'a-charm'), ('and-knowing-one', 'and-a-familiar-spirit'), ("form-of-the-prefix-'k-'-me/my", 'like-me'), ('and-be-weighty-them/their', 'and-you-shall-stone-them'), ('judgement', 'plea'), ('to-judgement', 'to-plea'), ('dominion-him/its', 'his-kingdom'), ('and-in-circumstance', 'and-because-of'), ('speak-him/its', 'spoke-it'), ('in-name-me/my', 'in-my-name'), ('alive-him/its', 'his-life'), ('circle-me/my', 'around-me'), ('fleece', 'the-fleece-of'), ('and-beginning', 'and-the-first-of'), ('beginning', 'the-first-of')]
SPEC = [(17, 2, 'לעבר', 'to-transgress', 0), (17, 3, 'צויתי', 'I-have-commanded', 0), (17, 4, 'והגד', 'and-it-is-told', 0), (17, 4, 'נכון', 'certain', 0), (17, 4, 'נעשתה', 'was-done', 0), (17, 5, 'והוצאת', 'and-you-shall-bring-out', 0), (17, 5, 'עשו', 'did', 0), (17, 5, 'ומתו', 'and-they-shall-die', 0),
        (17, 6, 'יומת', 'shall-die', 0), (17, 6, 'יומת', 'shall-die', 1), (17, 7, 'העדים', 'the-witnesses', 0), (17, 7, 'תהיה', 'shall-be', 0), (17, 7, 'בראשנה', 'first', 0), (17, 7, 'ובערת', 'and-you-shall-purge', 0), (17, 7, 'הרע', 'the-evil', 0),
        (17, 8, 'יפלא', 'is-too-hard', 0), (17, 8, 'למשפט', 'for-judgment', 0), (17, 8, 'נגע', 'stroke', 0), (17, 8, 'לנגע', 'to-stroke', 0), (17, 8, 'ריבת', 'of-dispute', 0), (17, 8, 'וקמת', 'and-you-shall-rise', 0), (17, 8, 'יבחר', 'will-choose', 0),
        (17, 9, 'והגידו', 'and-they-shall-tell', 0), (17, 10, 'יגידו', 'they-tell', 0), (17, 10, 'יבחר', 'will-choose', 0), (17, 11, 'יאמרו', 'they-say', 0), (17, 11, 'תסור', 'you-shall-turn', 0), (17, 11, 'יגידו', 'they-tell', 0),
        (17, 12, 'העמד', 'who-stands', 0), (17, 12, 'ומת', 'shall-die', 0), (17, 12, 'ובערת', 'and-you-shall-purge', 0), (17, 12, 'הרע', 'the-evil', 0), 
        (17, 14, 'תבא', 'you-come', 0), (17, 14, 'וירשתה', 'and-possess-it', 0), (17, 14, 'אשימה', 'I-will-set', 0), (17, 15, 'תשים', 'you-shall-set', 0), (17, 15, 'תשים', 'you-shall-set', 1), (17, 15, 'יבחר', 'will-choose', 0), (17, 15, 'תוכל', 'you-may', 0), (17, 15, 'נכרי', 'foreign', 0),
        (17, 16, 'ירבה', 'he-shall-multiply', 0), (17, 16, 'ישיב', 'he-shall-return', 0), (17, 16, 'הרבות', 'multiplying', 0), (17, 16, 'תספון', 'you-shall-again', 0), (17, 17, 'ירבה', 'he-shall-multiply', 0), (17, 17, 'ירבה', 'he-shall-multiply', 1), 
        (17, 18, 'כשבתו', 'when-he-sits', 0), (17, 18, 'כסא', 'the-throne-of', 0), (17, 18, 'וכתב', 'and-he-shall-write', 0), (17, 18, 'משנה', 'a-copy-of', 0), (17, 19, 'וקרא', 'and-he-shall-read', 0), (17, 19, 'לעשתם', 'to-do-them', 0), (17, 20, 'רום', 'be-lifted', 0), (17, 20, 'סור', 'turn', 0), (17, 20, 'יאריך', 'he-may-prolong', 0),
        (18, 1, 'חלק', 'portion', 0), (18, 3, 'משפט', 'the-due-of', 0), (18, 3, 'זבחי', 'those-who-sacrifice', 0), (18, 4, 'תתן', 'you-shall-give', 0), (18, 5, 'בחר', 'chose', 0), 
        (18, 6, 'גר', 'sojourns', 0), (18, 6, 'ובא', 'and-comes', 0), (18, 7, 'ושרת', 'and-he-shall-minister', 0), (18, 7, 'העמדים', 'who-stand', 0), (18, 8, 'ממכריו', 'his-sales', 0), (18, 8, 'האבות', 'the-fathers', 0), (18, 9, 'תלמד', 'you-shall-learn', 0),
        (18, 10, 'ימצא', 'be-found', 0), (18, 10, 'מעביר', 'one-who-passes', 0), (18, 10, 'קסם', 'a-diviner-of', 0), (18, 10, 'קסמים', 'divinations', 0), (18, 10, 'מעונן', 'a-soothsayer', 0), (18, 11, 'וחבר', 'and-a-charmer-of', 0), (18, 11, 'ושאל', 'and-one-who-asks', 0), (18, 11, 'ודרש', 'and-one-who-inquires', 0),
        (18, 12, 'עשה', 'who-does', 0), (18, 12, 'מוריש', 'dispossesses', 0), (18, 13, 'תמים', 'whole', 0), (18, 14, 'יורש', 'dispossess', 0), (18, 14, 'מעננים', 'soothsayers', 0), (18, 14, 'קסמים', 'diviners', 0), (18, 14, 'ישמעו', 'hearken', 0),
        (18, 15, 'יקים', 'will-raise-up', 0), (18, 16, 'שאלת', 'you-asked', 0), (18, 16, 'אסף', 'let-me-again', 0), (18, 16, 'אראה', 'let-me-see', 0), (18, 16, 'אמות', 'let-me-die', 0), (18, 17, 'היטיבו', 'they-have-done-well', 0),
        (18, 18, 'אקים', 'I-will-raise-up', 0), (18, 18, 'ונתתי', 'and-I-will-put', 0), (18, 18, 'אצונו', 'I-command-him', 0), (18, 19, 'אדרש', 'I-will-require', 0), (18, 20, 'יזיד', 'presumes', 0), (18, 20, 'צויתיו', 'I-commanded-him', 0), (18, 21, 'נדע', 'shall-we-know', 0), (18, 22, 'יבוא', 'come-to-pass', 0), (18, 22, 'תגור', 'be-afraid', 0)]
REF3 = [(f'Deut.{c}.{v}:{I.sidx(c, v, tok, nth)}', new, tok) for c, v, tok, new, nth in SPEC]
REF = [(k, v) for k, v, _ in REF3]; TOK = {k: t for k, _, t in REF3}
assert len(REF) == len({k for k, _ in REF}) == len(SPEC) and len(GL) == len({g for g, _ in GL})
assert all(I.sg(c, v, tok, nth) != new for c, v, tok, new, nth in SPEC), [(c, v, tok) for c, v, tok, new, nth in SPEC if I.sg(c, v, tok, nth) == new]   # no row rewrites a gloss to itself
assert all(I.sg(c, v, tok, nth) not in dict(GL) for c, v, tok, _, nth in SPEC), [(c, v, tok, I.sg(c, v, tok, nth)) for c, v, tok, _, nth in SPEC if I.sg(c, v, tok, nth) in dict(GL)]   # a seat patched by gloss is not patched again by reference
P = f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'
t = open(P, encoding='utf-8').read()
d0 = yaml.safe_load(t); BG0 = d0['by_gloss']
assert '"Deut.17.' not in t and '"Deut.18.' not in t and all(g not in BG0 for g, _ in GL), [g for g, _ in GL if g in BG0]
MARK = 'THE DEUTERONOMY WALK sitting 15 (2026-09-24, Deuteronomy 17-18, LEAN)'
assert MARK not in t
M14 = 'THE DEUTERONOMY WALK sitting 14 (2026-09-23, Deuteronomy 16, LEAN)'
i = t.index(f'  # {M14}: the worst glosses of the chapter\'s seats')
j = t.index('\n', i) + 1
rows = []
while True:
    m = re.match(r'  "[^"]+": "[^"]*"[^\n]*\n', t[j:])
    if not m: break
    rows.append(m.group(0)); j += len(m.group(0))
assert len(rows) == 23, len(rows)   # sitting 14's twenty-three by-gloss rows (its patch print)
A1 = rows[-1]; assert t.count(A1) == 1
gl_block = A1 + f'\n  # {MARK}: the worst glosses of the two chapters\' seats, the families probed in the store first (ch17_patch_probe.py) — the lean form\'s patch; the rest OWED (COMPILE_DEBT\'s lean-pass box)\n' + ''.join(f'  "{k}": "{v}"\n' for k, v in GL)
t = t.replace(A1, gl_block)
m2 = re.search(r'^  "Deut\.16\.22:5": "hates"[^\n]*\n', t, re.M); assert m2 and t.count('"Deut.16.22:5": "hates"') == 1
A2 = m2.group(0)
ref_block = A2 + f'  # {MARK}: the two chapters\' seats by reference — the token named beside each; the indices the store\'s own\n' + ''.join(f'  "{k}": "{v}"   # {TOK[k]}\n' for k, v in REF)
t = t.replace(A2, ref_block)
open(P, 'w', encoding='utf-8').write(t)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert all(d['by_ref'][k] == v for k, v in REF) and all(d['by_gloss'][k] == v for k, v in GL)
print('override rows written: by_ref', len(REF), 'by_gloss', len(GL), '| by_ref total', len(d['by_ref']), '| by_gloss total', len(d['by_gloss']))
