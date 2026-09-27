import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 16 — CHAPTERS 19-21 (LEAN, 2026-09-24; RUN 2): the store's glosses at the three chapters' seats read back into the display layer's
# override file — BY GLOSS where the store's every token of the gloss is the one word or one family read the same at every seat (the families PROBED FIRST by
# ch19_patch_probe.py, the counts read from its print; the glosses the earlier walks already rewrote by gloss excluded — the probe's own list), BY REFERENCE at the
# chapters' own seats where the family is mixed. THE LEAN FORM: the worst glosses only; the rest OWED. Display only; the draft units untouched. Run ONCE (the anchors
# assert the rows absent first). Sitting 15's form (ch17_patch_overrides.py): the anchors the LAST ROWS of sitting 15's two blocks — the by_gloss block's last row found
# by walking from sitting 15's marker (never typed), the by_ref block's last row 18:22's. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad; after the freeze chain.
import os, re, subprocess, sys, io, contextlib, yaml
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
with contextlib.redirect_stdout(io.StringIO()):
    import ch19_ink as I
GL = [('and-be--triplicate', 'and-divide-into-three'), ('in-copse-of-bushes', 'into-the-forest'), ('to-chop', 'to-cut'), ('to-push-off', 'to-swing'), ('be-hot', 'is-hot'), ('and-reach-him/its', 'and-overtakes-him'), ('the-contest', 'the-dispute'), ('contest', 'dispute'), ('and-the-swell-up', 'and-the-remaining'), ('and-vehicle', 'and-chariot'), ('the-go-up-you/your', 'who-brings-you-up'), ('like-bring-near-you/your (pl)', 'when-you-draw-near'), ('soften', 'be-faint'), ('start-up-suddenly', 'be-hasty'), ('to-feed-on', 'to-fight'), ('to-be-open', 'to-save'), ('the-scribe', 'the-officers'), ('engage-for-matrimony', 'betroth'), ('the-fearing', 'the-fearful'), ('and-tender', 'and-faint'), ('like-be-complete', 'when-they-have-finished'), ('mass-of-persons', 'hosts'), ('to-safe', 'for-peace'), ('to-burden', 'for-tribute'), ('male-her/its', 'its-males'), ('and-the-family', 'and-the-little-ones'), ('puff', 'breath'), ('seclude-them/their', 'utterly-destroy-them'), ('something-disgusting-them/their', 'their-abominations'), ('to-manipulate-her/its', 'to-capture-it'), ('and-manipulate', 'and-seize'), ('in-something-hemming-in', 'in-the-siege'), ('something-hemming-in', 'siege-works'), ('eatable', 'food'), ('go-down-her/its', 'it-falls'), ('pierced', 'slain'), ('the-pierced', 'the-slain'), ('in-ground', 'on-the-ground'), ('in-yoke', 'in-a-yoke'), ('in-stream', 'in-the-valley'), ('the-break-the-neck', 'the-broken-necked'), ('lave', 'wash'), ('exiled-him/its', 'its-captives'), ('in-exile', 'among-the-captives'), ('exile-her/its', 'her-captivity'), ('outline', 'form'), ('and-cling', 'and-desire'), ('and-be-bald', 'and-shave'), ('claw-her/its', 'her-nails'), ('dress', 'garment'), ('and-be-master-her/its', 'and-be-her-husband'), ('incline-to', 'desire'), ('to-living-being-her/its', 'to-herself'), ('gather-grain', 'deal-as-a-slave'), ('depress-literally-her/its', 'humbled-her'), ('the-have-affection-for', 'the-loved'), ('the-hate', 'the-hated'), ('and-the-hate', 'and-the-hated'), ('to-hated', 'to-the-hated'), ('to-give-the-birthright', 'to-make-firstborn'), ('scrutinize', 'recognize'), ('ability-him/its', 'his-strength'), ('the-firstling-of-man', 'the-birthright'), ('turn-away', 'stubborn'), ('there-is-not-him/its', 'he-is-not'), ('shake', 'a-glutton'), ('and-potation', 'and-a-drunkard'), ('and-cast-together-him/its', 'and-stone-him'), ('flabby-thing-him/its', 'his-corpse'), ('inter-him/its', 'bury-him'), ('vilification', 'curse'), ('and-judge-you/your', 'and-your-judges'), ('old-you/your', 'your-elders'), ('and-lurk', 'and-lies-in-wait'), ('run-after--gone-by)', 'pursue'), ('untruth', 'falsehood'), ('and-hind-part', 'and-after'), ('and-eye-us/our', 'and-our-eyes'), ('eye-us/our', 'our-eyes'), ('hand-us/our', 'our-hands'), ('mouth-them/their', 'their-word'), ('son-us/our', 'our-son'), ('in-voice/sound-us/our', 'our-voice'), ('and-in-voice/sound', 'and-the-voice-of'), ('like-heart-him/its', 'like-his-heart'), ('the-find', 'the-found'), ('in-inheritance-you/your', 'in-your-inheritance'), ('in-tooth', 'for-tooth'), ('in-foot', 'for-foot')]
SPEC = [(19, 1, 'יכרית', 'cuts-off', 0), (19, 2, 'תבדיל', 'separate', 0), (19, 7, 'תבדיל', 'separate', 0), (19, 3, 'תכין', 'prepare', 0), (19, 3, 'רצח', 'manslayer', 0), (19, 6, 'גאל', 'the-avenger-of', 0), (19, 12, 'גאל', 'the-avenger-of', 0), (19, 13, 'תחוס', 'pity', 0), (19, 13, 'ובערת', 'and-you-shall-purge', 0), (19, 14, 'תסיג', 'move', 0), (19, 14, 'גבלו', 'bounded', 0),
        (19, 15, 'עון', 'iniquity', 0), (19, 15, 'חטאת', 'sin', 0), (19, 16, 'לענות', 'to-testify', 0), (19, 18, 'העד', 'the-witness', 0), (19, 18, 'ענה', 'testified', 0), (19, 19, 'זמם', 'plotted', 0), (19, 19, 'ובערת', 'and-you-shall-purge', 0), (19, 21, 'תחוס', 'pity', 0), (19, 21, 'בנפש', 'for-life', 0), (19, 21, 'בעין', 'for-eye', 0),
        (20, 1, 'תצא', 'you-go-out', 0), (20, 2, 'ונגש', 'and-shall-come-near', 0), (20, 5, 'חנכו', 'dedicated-it', 0), (20, 5, 'יחנכנו', 'dedicate-it', 0), (20, 6, 'כרם', 'a-vineyard', 0), (20, 6, 'חללו', 'used-its-fruit', 0), (20, 6, 'יחללנו', 'use-its-fruit', 0), (20, 9, 'ופקדו', 'and-they-shall-appoint', 0), (20, 10, 'תקרב', 'you-draw-near', 0), (20, 11, 'תענך', 'it-answers-you', 0), (20, 11, 'ופתחה', 'and-opens', 0), (20, 12, 'תשלים', 'it-makes-peace', 0), (20, 12, 'וצרת', 'and-you-shall-besiege', 0), (20, 13, 'חרב', 'the-sword', 0), (20, 14, 'תבז', 'you-shall-take-as-spoil', 0), (20, 14, 'שלל', 'the-spoil-of', 0), (20, 19, 'תצור', 'you-besiege', 0), (20, 19, 'תשחית', 'destroy', 0), (20, 20, 'תשחית', 'destroy', 0),
        (21, 1, 'הכהו', 'struck-him', 0), (21, 2, 'ומדדו', 'and-measure', 0), (21, 2, 'סביבת', 'around', 0), (21, 3, 'עגלת', 'a-heifer-of', 0), (21, 4, 'העגלה', 'the-heifer', 0), (21, 4, 'העגלה', 'the-heifer', 1), (21, 6, 'העגלה', 'the-heifer', 0), (21, 4, 'נחל', 'a-valley', 0), (21, 4, 'איתן', 'rough', 0), (21, 4, 'יזרע', 'sown', 0), (21, 5, 'ונגשו', 'and-shall-come-near', 0), (21, 5, 'נגע', 'plague', 0), (21, 7, 'וענו', 'and-they-shall-answer', 0), (21, 8, 'פדית', 'redeemed', 0), (21, 9, 'תבער', 'shall-purge', 0), (21, 10, 'ושבית', 'and-you-capture', 0), (21, 13, 'ירח', 'a-month', 0), (21, 18, 'ומורה', 'and-rebellious', 0), (21, 20, 'ומרה', 'and-rebellious', 0), (21, 21, 'באבנים', 'with-stones', 0), (21, 21, 'ובערת', 'and-you-shall-purge', 0), (21, 22, 'ותלית', 'and-you-hang', 0), (21, 23, 'תלין', 'shall-stay-overnight', 0), (21, 23, 'תלוי', 'a-hanged-one', 0)]
REF3 = [(f'Deut.{c}.{v}:{I.sidx(c, v, tok, nth)}', new, tok) for c, v, tok, new, nth in SPEC]
REF = [(k, v) for k, v, _ in REF3]; TOK = {k: t for k, _, t in REF3}
assert len(REF) == len({k for k, _ in REF}) == len(SPEC) and len(GL) == len({g for g, _ in GL})
assert all(I.sg(c, v, tok, nth) != new for c, v, tok, new, nth in SPEC), [(c, v, tok) for c, v, tok, new, nth in SPEC if I.sg(c, v, tok, nth) == new]   # no row rewrites a gloss to itself
assert all(I.sg(c, v, tok, nth) not in dict(GL) for c, v, tok, _, nth in SPEC), [(c, v, tok, I.sg(c, v, tok, nth)) for c, v, tok, _, nth in SPEC if I.sg(c, v, tok, nth) in dict(GL)]   # a seat patched by gloss is not patched again by reference
P = f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'
t = open(P, encoding='utf-8').read()
d0 = yaml.safe_load(t); BG0 = d0['by_gloss']
assert '"Deut.19.' not in t and '"Deut.20.' not in t and '"Deut.21.' not in t and all(g not in BG0 for g, _ in GL), [g for g, _ in GL if g in BG0]
MARK = 'THE DEUTERONOMY WALK sitting 16 (2026-09-24, Deuteronomy 19-21, LEAN)'
assert MARK not in t
M15 = 'THE DEUTERONOMY WALK sitting 15 (2026-09-24, Deuteronomy 17-18, LEAN)'
i = t.index(f'  # {M15}: the worst glosses of the two chapters\' seats')
j = t.index('\n', i) + 1
rows = []
while True:
    m = re.match(r'  "[^"]+": "[^"]*"[^\n]*\n', t[j:])
    if not m: break
    rows.append(m.group(0)); j += len(m.group(0))
assert len(rows) == 30, len(rows)   # sitting 15's thirty by-gloss rows (its patch print "by_gloss 30")
A1 = rows[-1]; assert t.count(A1) == 1
gl_block = A1 + f'\n  # {MARK}: the worst glosses of the three chapters\' seats, the families probed in the store first (ch19_patch_probe.py) — the lean form\'s patch; the rest OWED (COMPILE_DEBT\'s lean-pass box)\n' + ''.join(f'  "{k}": "{v}"\n' for k, v in GL)
t = t.replace(A1, gl_block)
m2 = re.search(r'^  "Deut\.18\.22:20": "be-afraid"[^\n]*\n', t, re.M); assert m2 and t.count('"Deut.18.22:20": "be-afraid"') == 1
A2 = m2.group(0)
ref_block = A2 + f'  # {MARK}: the three chapters\' seats by reference — the token named beside each; the indices the store\'s own\n' + ''.join(f'  "{k}": "{v}"   # {TOK[k]}\n' for k, v in REF)
t = t.replace(A2, ref_block)
open(P, 'w', encoding='utf-8').write(t)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert all(d['by_ref'][k] == v for k, v in REF) and all(d['by_gloss'][k] == v for k, v in GL)
print('override rows written: by_ref', len(REF), 'by_gloss', len(GL), '| by_ref total', len(d['by_ref']), '| by_gloss total', len(d['by_gloss']))
