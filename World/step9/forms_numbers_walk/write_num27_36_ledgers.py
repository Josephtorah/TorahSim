import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE TENT sitting 4 (2026-09-09) — THE READING of Numbers 27:1-23 (num_27_zelophehad_joshua) and 36:1-13 (num_36_heiresses):
# writes the two append-only ledgers logic/oral_triage/num_27_zelophehad_joshua_2026-09-09.md and num_36_heiresses_2026-09-09.md
# with their COVERAGE COMPUTED from the shelf files (the Sifrei on Numbers' own row counts per piska, machine-found by the
# shelf's verse heads; Onkelos Numbers' verses in each span) and the INK FACTS the reading leans on computed from the Tanakh
# DB — counts measured here, never typed; the prose rows are the reading. (Sitting 3's form, write_num15_ledger.py.)
import json, os, re, html, sqlite3
from collections import Counter
ROOT = _ROOT
OUT27 = f'{ROOT}/logic/oral_triage/num_27_zelophehad_joshua_2026-09-09.md'
OUT36 = f'{ROOT}/logic/oral_triage/num_36_heiresses_2026-09-09.md'
for o in (OUT27, OUT36):
    assert not os.path.exists(o), f'ledger exists — append, never overwrite: {o}'

sif = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/en.json'))['text']
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/en.json'))['text']
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
heads = {}
for p, rows in enumerate(sif, 1):
    if not rows: continue
    m = re.search(r'\((Bamidbar|Devarim) (\d+):(\d+)', clean(rows[0])[:60])
    heads[p] = (m.group(1), int(m.group(2)), int(m.group(3))) if m else None
# the span's piskaot by POSITION: from the first head in Num 27 to the last head in Num 27 — the Sifrei's own excursus
# (134:5, 135, 136:1-2 open on Deuteronomy verses: Moses' plea, placed by the shelf at 27:12-13) lies inside by position
in27 = [p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 27]
lo_p, hi_p = min(in27), max(in27)
span_p = list(range(lo_p, hi_p + 1))
assert span_p == list(range(133, 142)), span_p
assert [heads[p] for p in (135, 136)] == [('Devarim', 3, 26), ('Devarim', 34, 4)], [heads[p] for p in (135, 136)]
in_span = [(p, len(sif[p - 1])) for p in span_p]
sifrei_rows = sum(n for _, n in in_span)
assert sifrei_rows == 23, sifrei_rows
nb = {p: heads[p] for p in (132, 142)}
assert nb == {132: ('Bamidbar', 26, 53), 142: ('Bamidbar', 28, 1)}, nb
# chapter 36: the shelf's LAST piska opens on 35:29 — no piska on Numbers 36 (computed, the shelf's own end)
last_p = max(p for p, h in heads.items() if h)
assert last_p == len(sif) == 161 and heads[161] == ('Bamidbar', 35, 29), (last_p, heads.get(161))
assert not any(h and h[0] == 'Bamidbar' and h[1] == 36 for h in heads.values())
assert len(onk[26]) == 23 and len(onk[35]) == 13
onk27, onk36 = 23, 13
shelf_numbers = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Numbers|Bamidbar', d))
outside = [d for d in shelf_numbers if d not in ('Sifrei_Bamidbar', 'Onkelos_Numbers')]
cite27 = [f'Sifrei Bamidbar {p}:{i}' for p, n in in_span for i in range(1, n + 1)] + [f'Onkelos Num 27:{v}' for v in range(1, onk27 + 1)]
N27 = len(cite27); assert N27 == sifrei_rows + onk27 == 46, N27
cite36 = [f'Onkelos Num 36:{v}' for v in range(1, onk36 + 1)]
N36 = len(cite36); assert N36 == 13
CREDITED36 = ['Sifrei Bamidbar 133:2', 'Sifrei Bamidbar 134:1', 'Sifrei Bamidbar 134:2']   # the Sifrei's rows on 36:5-11, read whole in the 27 ledger

# ---- THE INK, computed from the Tanakh DB (consonantal: '/' and the marks U+0591..U+05C7 stripped) ----
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by = {}
for b, c, v, he, m in rows: by.setdefault((b, c, v), []).append((plain(he), m))
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def hits(sub, books=None): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) and any(sub in x for x, _ in ws)})
def phrase(seq, books=T):
    out = []
    for (b, c, v), ws in by.items():
        if b not in books: continue
        w = [x for x, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
def words(b, c, v): return [x for x, _ in by[(b, c, v)]]
approach_f = hits('ותקרבנה'); assert approach_f == ['Josh 17:4', 'Num 27:1'], approach_f
their_judgment = hits('משפטן'); assert their_judgment == ['Num 27:5'], their_judgment
hiph = sorted(f'{b} {c}:{v}' for (b, c, v), ws in by.items() if b in T and any(x == 'ויקרב' and m and 'Vhw' in m for x, m in ws))
assert 'Num 27:5' in hiph and len(hiph) == 11, hiph
frames = {}
for b, c, v in (('Lev', 24, 13), ('Num', 9, 9), ('Num', 15, 35), ('Num', 27, 6), ('Num', 36, 5)):
    w = words(b, c, v); frames[f'{b} {c}:{v}'] = (' '.join(w[:2]), 'לאמר' in w)
assert frames == {'Lev 24:13': ('וידבר יהוה', True), 'Num 9:9': ('וידבר יהוה', True), 'Num 15:35': ('ויאמר יהוה', False),
                  'Num 27:6': ('ויאמר יהוה', True), 'Num 36:5': ('ויצו משה', True)}, frames
said_saying = phrase(['ויאמר', 'יהוה', 'אל', 'משה', 'לאמר']); assert len(said_saying) == 5 and 'Num 27:6' in said_saying, said_saying
by_mouth = phrase(['על', 'פי', 'יהוה']); assert len(by_mouth) == 18 and {'Lev 24:12', 'Num 33:38', 'Num 36:5'} <= set(by_mouth), by_mouth
statute_j = phrase(['לחקת', 'משפט']); assert statute_j == ['Num 27:11', 'Num 35:29'], statute_j
flesh_near = phrase(['לשארו', 'הקרב']); assert flesh_near == ['Lev 21:2', 'Num 27:11'], flesh_near
this_thing = phrase(['זה', 'הדבר', 'אשר', 'צוה', 'יהוה']); assert len(this_thing) == 8 and 'Num 36:6' in this_thing, this_thing
NAMES = {'מחלה': 'Mahlah', 'נעה': 'Noah', 'ונעה': 'Noah', 'חגלה': 'Hoglah', 'וחגלה': 'Hoglah', 'מלכה': 'Milcah', 'ומלכה': 'Milcah', 'תרצה': 'Tirzah', 'ותרצה': 'Tirzah'}
def order(b, c, v): return [NAMES[x] for x in words(b, c, v) if x in NAMES]
o1, o2, o3, o4 = order('Num', 26, 33), order('Num', 27, 1), order('Josh', 17, 3), order('Num', 36, 11)
assert o1 == o2 == o3 == ['Mahlah', 'Noah', 'Hoglah', 'Milcah', 'Tirzah'] and o4 == ['Mahlah', 'Tirzah', 'Hoglah', 'Milcah', 'Noah'], (o1, o2, o3, o4)
pass_over = hits('והעברתם'); assert pass_over == ['Josh 4:3', 'Num 27:8'], pass_over
give = [f'Num 27:{v}' for v in (9, 10, 11) if 'ונתתם' in words('Num', 27, v)]; assert give == ['Num 27:9', 'Num 27:10', 'Num 27:11'], give
assert 'ידך' in words('Num', 27, 18) and 'ידיו' in words('Num', 27, 23)
gara = sorted(f'{b} {c}:{v}' for (b, c, v), ws in by.items() if b == 'Num' and any(re.fullmatch(r'ו?נ?(ג|י)גרע(ה|ו)?', x) or x in ('יגרע', 'נגרע', 'ונגרעה') for x, _ in ws))
assert gara == ['Num 27:4', 'Num 36:3', 'Num 36:4', 'Num 9:7'], gara     # (the DB sorts by book name; 9:7 last as a string)
approach_m = hits('ויקרבו', T); assert {'Num 9:6', 'Num 36:1'} <= set(approach_m) and len(approach_m) == 8, approach_m
jubilee = hits('היבל', T); assert 'Num 36:4' in jubilee and len(jubilee) == 9, jubilee
gathered = hits('הנועדים', T); assert gathered == ['Num 14:35', 'Num 27:3'], gathered
korah = phrase(['בעדת', 'קרח']); assert korah == ['Num 26:9', 'Num 27:3'], korah
w3338 = words('Num', 33, 38); assert {'הארבעים', 'החמישי', 'באחד', 'פי', 'יהוה'} <= set(w3338), w3338
wj174 = words('Josh', 17, 4); assert {'ותקרבנה', 'אלעזר', 'יהושע', 'פי', 'יהוה', 'נחלה'} <= set(wj174), wj174
assert {'בערבת', 'מואב'} <= set(words('Num', 36, 13)) and {'בארץ', 'מואב'} <= set(words('Deut', 1, 5))
uncles = hits('דדיהן'); assert uncles == ['Num 36:11'], uncles
nachal36 = sum(1 for (b, c, v), ws in by.items() if b == 'Num' and c == 36 for x, _ in ws if 'נחל' in x)
nachal27 = sum(1 for (b, c, v), ws in by.items() if b == 'Num' and c == 27 and v <= 11 for x, _ in ws if 'נחל' in x)
assert (nachal36, nachal27) == (17, 6), (nachal36, nachal27)
GLOSS = {'ותקרבנה': 'and they drew near (fem.)', 'ותעמדנה': 'and they stood (fem.)', 'ויקרב': 'and he brought near', 'ויאמר': 'and he said',
         'וידבר': 'and he spoke', 'ויעש': 'and he did', 'ויקח': 'and he took', 'ויעמדהו': 'and he stood him', 'ויסמך': 'and he laid',
         'ויצוהו': 'and he commanded him', 'ויקרבו': 'and they drew near', 'וידברו': 'and they spoke', 'ויאמרו': 'and they said',
         'ויצו': 'and he commanded', 'ותהיינה': 'and they were (fem.)', 'ותהי': 'and it was (fem.)'}
def register(ch, lo, hi):
    reg = {}
    for v in range(lo, hi + 1):
        reg[v] = [x + ' ("' + GLOSS[x] + '", ' + m.split('/')[-1] + ')' for x, m in by[('Num', ch, v)] if m and re.search(r'V.w', m)]
    return reg
reg27, reg36 = register(27, 1, 23), register(36, 1, 13)
assert [v for v in reg27 if reg27[v]] == [1, 2, 5, 6, 12, 15, 18, 22, 23] and [v for v in reg36 if reg36[v]] == [1, 2, 5, 11, 12], (reg27, reg36)
# Onkelos's shared verb for the two pleas' "held back" (9:7 / 27:4): computed on the Aramaic
ar = lambda c, v: clean(onk_he[c - 1][v - 1])
def ar_plain(s): return ''.join(ch for ch in s if not (0x0591 <= ord(ch) <= 0x05C7))
assert 'נתמנע' in ar_plain(ar(9, 7)) and 'יתמנע' in ar_plain(ar(27, 4)) and 'תתמנע' in ar_plain(ar(36, 3)), (ar(9, 7), ar(27, 4))

ink27 = [
    f'- THE APPROACH VERB, FEMININE: ותקרבנה ("and they drew near", fem. pl.) at {" and ".join(approach_f)} ALONE in the whole Tanakh — the case '
    f'(27:1) and its RUN in the sixth book (Josh 17:4: the daughters approach Eleazar, Joshua and the princes, cite "the LORD commanded Moses", '
    f'and Joshua "gave them BY THE MOUTH OF THE LORD an inheritance among their father\'s brothers"). The masculine ויקרבו ("and they drew near") '
    f'stands at {len(approach_m)} Torah seats, the unclean men\'s 9:6 and the tribes\' 36:1 among them: the three Numbers pleas share the verb.',
    f'- THE HALT\'S VERB: משפטן ("their judgment") at {their_judgment[0]} alone in the Tanakh; its verb ויקרב ("and he brought near", the causative '
    f'stem) at {len(hiph)} Torah seats — {", ".join(hiph)} — the others the OFFERINGS brought near (Lev 8-9), Korach\'s "he brought you near" (16:10) '
    f'and Zimri (25:6): Moses brings the judgment near as an offering is brought. No guard (Lev 24:12, Num 15:34), no "stand and I will hear" (9:8).',
    '- THE OUTPUTS\' FRAMES: ' + '; '.join(f'{k} opens "{a}" ' + ('with' if l else 'WITHOUT') + ' לאמר ("saying")' for k, (a, l) in frames.items()) +
    f' — four forms across the block\'s five outputs: spoke-saying (Lev 24:13, Num 9:9), said bare (15:35), said-saying (27:6 — {len(said_saying)} Torah '
    f'seats of that exact frame: {", ".join(said_saying)}), and MOSES commanding על פי יהוה ("by the mouth of the LORD", 36:5 — {len(by_mouth)} Torah seats, '
    f'Lev 24:12\'s halt clause and Aaron\'s death at 33:38 among them): the second output is relayed by Moses, no divine speech frame in the ink.',
    f'- A STATUTE OF JUDGMENT: לחקת משפט ("for a statute of judgment") at {" and ".join(statute_j)} ONLY — the inheritance order and the refuge '
    f'cities\' procedure (Sifrei 134:3 reads it as the sages\' authority to rank the near; 161:1 as "for the generations, in the land and outside").',
    f'- HIS FLESH WHO IS NEAR: לשארו הקרב ("to his flesh, the near one") at {" and ".join(flesh_near)} ONLY — the priest\'s mourning list and the '
    f'inheritance\'s last heir: the shared phrase behind "and he shall inherit HER" (R. Akiva, 134:2 — the husband reads off the wife\'s word).',
    f'- PASS OVER / GIVE: והעברתם ("and you shall pass over") at {" and ".join(pass_over)} — 27:8 the daughter\'s verse, the Torah\'s only seat; '
    f'ונתתם ("and you shall give") at {", ".join(give)} — the brothers, the uncles, the flesh. Rebbi\'s "in all the others GIVE, here PASS" (134:2) is '
    'the ink\'s own two verbs, and Onkelos keeps them apart (transfer / give).',
    f'- THE NAMES\' TWO ORDERS: 26:33, 27:1 and Josh 17:3 read {", ".join(o1)}; 36:11 reads {", ".join(o4)} — the Sifrei\'s "all equal" (133:2) at the '
    'computed delta (Tirzah moved second, Noah last).',
    f'- ZELOPHEHAD stands at {len(hits("צלפחד"))} Tanakh tokens ({", ".join(hits("צלפחד"))}); "in the wilderness" (במדבר, "in the wilderness") at 27:3 is one of '
    f'{len(hits("במדבר", T))} Torah seats — R. Akiva\'s verbal analogy (133:3) rides the common word to 15:32, a TRANSFER taught by its teacher; '
    f'הנועדים ("who gathered") at {" and ".join(gathered)} only in the Torah — the spies\' congregation (14:35) is the shared word, as the Sifrei reads; '
    f'בעדת קרח ("in Korach\'s congregation") at {" and ".join(korah)}.',
    f'- THE HANDS: ידך ("your hand", singular) commanded at 27:18; ידיו ("his hands", plural) laid at 27:23 — the spec/run delta the Sifrei reads as the '
    'overflowing vessel (141:3).',
    f'- THE DATE BY THE ROSTER: 33:38 stamps Aaron\'s death "in the fortieth year... in the fifth month, on the first of the month" (the words '
    'הארבעים "the fortieth", החמישי "the fifth", באחד "on the first" computed on the verse); 27:2\'s "before Eleazar the priest" places the case after it '
    '(Sifrei 133:3) — a READING-PLACED date, the ink\'s own stamp on another verse.',
    f'- THE PLEAS\' VERB: the root גרע ("be held back / diminished") at {", ".join(gara)} in Numbers — the unclean men\'s "why should we be held back" (9:7), '
    'the daughters\' "why should the name be withheld" (27:4), the tribes\' "shall be diminished" twice (36:3, 36:4); Onkelos renders all three pleas '
    'with one Aramaic verb (מנע, "hold back": computed on 9:7, 27:4, 36:3).',
    '- THE REGISTER (the "and he did" forms per verse, the morphology\'s w-stem): ' + '; '.join(f'27:{v} ' + ', '.join(reg27[v]) for v in reg27 if reg27[v]) +
    ' — the acts at 27:1-2 (the daughters), 27:5 (Moses), 27:6/12/18 (the speech frames), 27:15 (Moses speaks), 27:22-23 (the investiture); 27:3-4, 7-11, '
    '13-14, 16-17, 19-21 carry speech alone (the plea, the statute, the commission).',
]
ink36 = [
    f'- THE TRIBES\' APPROACH: ויקרבו ("and they drew near", masc. pl.) at 36:1 — the unclean men\'s verb (9:6) among {len(approach_m)} Torah seats; the daughters\' '
    'feminine form at 27:1 stands with Josh 17:4 alone.',
    f'- THE SECOND OUTPUT\'S FRAME: 36:5 opens "{frames["Num 36:5"][0]}" ("and Moses commanded") with לאמר ("saying") and על פי יהוה ("by the mouth of the LORD" '
    f'— {len(by_mouth)} Torah seats; Lev 24:12 the blasphemer\'s halt clause, 33:38 Aaron\'s death): no "and the LORD said" — the output relayed in Moses\' mouth.',
    f'- THIS IS THE THING: זה הדבר אשר צוה יהוה ("this is the thing that the LORD commanded") at {len(this_thing)} Torah seats — {", ".join(this_thing)} — '
    '36:6 among them (the formula the Talmud reads at the compile for the rule\'s reach: Bava Batra 120a).',
    f'- THE JUBILEE: היבל ("the jubilee") at {len(jubilee)} Torah seats — {", ".join(jubilee)} — 36:4 the only seat outside Exod 19:13\'s horn and Leviticus 25/27: '
    'the tribes\' argument reaches the release engine (a REFERENCE by the ink\'s own word).',
    f'- THE CLEAVING: ידבקו ("shall cleave") at 36:7 and 36:9 — Gen 2:24\'s verb (the whole-Torah list {", ".join(hits("דבק", T))}); תסב ("shall go around") at 36:7 '
    f'and 36:9 (and Gen 37:7\'s sheaves): the transfer barred in the ink\'s own circling verb.',
    f'- THE INHERITANCE WORD: the root נחל ("inherit") at {nachal36} tokens in the thirteen verses of 36 and {nachal27} in 27:1-11 — the chapter is the inheritance\'s own vocabulary; '
    f'דדיהן ("their uncles") at {uncles[0]} alone (the uncle noun\'s other Torah seats Lev 10:4, 20:20, 25:49 — the redeemer\'s list).',
    f'- THE NAMES\' SECOND ORDER at 36:11: {", ".join(o4)} against {", ".join(o1)} at 26:33 / 27:1 / Josh 17:3 (computed; Sifrei 133:2).',
    '- THE EXECUTION\'S FORMULA: 36:10 "as the LORD commanded Moses, so did the daughters" — כאשר צוה יהוה ("as the LORD commanded") and כן עשו ("so they did") — the '
    'report clause of Lev 24:23 and Num 15:36 on the fourth case; and 36:12 "their inheritance REMAINED on the tribe" — the ledger\'s close in the ink.',
    '- THE COLOPHON: 36:13 "in the plains of Moab by the Jordan of Jericho" (בערבת מואב, "in the plains of Moab") — Deut 1:5 opens "in the land of Moab": the '
    'book closes at the site where the third pass begins (the readback\'s place, computed on both verses).',
    '- THE REGISTER: ' + '; '.join(f'36:{v} ' + ', '.join(reg36[v]) for v in reg36 if reg36[v]) +
    ' — the tribes act at 36:1-2, Moses at 36:5, the daughters at 36:11-12; 36:3-4 and 36:6-9 speech; 36:10 the report (a perfect, no "and he did" form); 36:13 the colophon.',
]

body27 = r'''# Numbers 27:1-23 derivation — the Sifrei on Numbers (Sifrei Bamidbar) as the spine + Onkelos,
# THE THIRD NUMBERS READING (2026-09-09; THE TENT sitting 4 — the daughters of Zelophehad, World/step9/THE_TENT.md section 4).
# DECLARED (THE_STEPS Step 2, the spine default of 2026-08-27): the Numbers spine is the Sifrei on Numbers, beside Onkelos;
# scope = every Sifrei row of the piskaot whose heads lie in Numbers 27 (piskaot 133-141 BY POSITION, machine-found by the
# shelf's own verse heads: __SIFROWS__ rows — the Sifrei's own excursus on Moses' plea, 134:5, 135:1 and 136:1-2, opens on
# Deuteronomy verses and sits INSIDE the stretch at 27:12-13; read with it) + Onkelos Numbers 27:1-23 (__ONKROWS__ verses, the
# chapter whole). Read whole, fresh, no credits: the draft num_27_zelophehad_joshua carries 27:1-23 — the daughters' case
# (1-11), Moses' viewing (12-14) and Joshua's commission (15-23) read together, the Sifrei's own piskaot spanning them. The
# neighbors measured outside: piska 132 opens on 26:53 (the apportionment — QUICK-LOOKED, four rows, the plea's premise: "to a
# man according to his numbers" excludes women, tumtumim and hermaphrodites; R. Yoshiyah: apportioned to those who LEFT EGYPT,
# R. Yonatan: to those who ENTERED, "the dead inherit the living" — Rebbi's two-brothers-priests parable; R. Shimon b. Elazar:
# both; only by lot, Joshua and Caleb excepted; by estimate) and piska 142 on 28:1. Also QUICK-LOOKED for its shared phrase:
# 161:1 on 35:29 "a statute of judgment" (the shelf's LAST piska — computed: no piska opens on Numbers 36; the heiresses' ledger
# is Onkelos with the Sifrei's rows on 36:5-11 credited from here). THE TESTING SHELF routed to Step 5 (the compile sitting's
# own docket ledger, enumerated BY TOPIC there): Mishnah Bava Batra 8:1-8 (the inheritance order — 8:2 quotes 27:8; 8:3 the
# daughters' three portions), 9:1-2; Tosefta Bava Batra 7; Mishnah Bekhorot 8 (the firstborn's double). The Babylonian Talmud —
# Bava Batra 108b-122a (the chapter "there are those who inherit"; 110b:4 the tent's output; 111b the wife's "flesh"; 115b-116a
# the daughters' precedence; 118b-119a the portions; 119a:8 the gatherer; 119b:10 THE DAUGHTERS' OWN LEVIRATE ARGUMENT; 120a the
# names' orders and the wilderness generation), Sanhedrin 8a:4-5 (the section stated through them) — is the bridge, PER GAP at
# the compile. OUTSIDE DECLARED SCOPE, enumerated and unread (the shelf's other works on Numbers, __OUTSIDE__ directories): __OUTSIDE_LIST__.

## Sifrei Bamidbar 133-141 (__SIFROWS__ rows whole — the stretch's piskaot by position)
- Sifrei Bamidbar 133:1 — MATERIAL. On 27:1. (a) THE COUNSEL: when the daughters heard the land was to be apportioned to
  the tribes and not to females, they gathered to take counsel — "not as the mercies of flesh and blood are the mercies of the
  Place: flesh and blood's mercies are more for males than females; He who spoke and the world was — His mercies are on all"
  (Ps 145:9). The plea's PREMISE is piska 132's apportionment rule (quick-looked above: "to a man" excludes women), read by
  the daughters themselves. (b) THE PEDIGREE "son of Hepher, son of Gilead, son of Machir, son of Manasseh" — as Zelophehad
  was a FIRSTBORN so all of them were firstborn (the three portions' ground, 134:1); and to teach they were worthy daughters
  of a worthy man: whoever's deeds are veiled and Scripture traces him for praise is a righteous one, son of a righteous one;
  for denigration, a wicked one, son of a wicked one. (c) R. NATAN (the shelf's HEBREW at this row): the righteous one who
  grew in the lap of the wicked and did not do as they — Esau between two righteous ones; the English's R. Natan line here
  ("the women's strength greater than the men's", 26:65 adjoining 27:1) stands in the Hebrew at 133:4 on 27:4 against 14:4 —
  the translation's placement, noted.
- Sifrei Bamidbar 133:2 — MATERIAL. On 27:1 (with 36:11). (a) Obadiah between two wicked ones prophesying against Esau —
  aggadic frame. (b) "of the families of Manasseh son of Joseph" — as Joseph held the land dear (Gen 50:25) so did the
  daughters. (c) THE NAMES' ORDER: "or perhaps whoever precedes in Scripture precedes in worth? — it is written (36:11)
  'Mahlah, Tirzah, Hoglah, Milcah and Noah': they were all EQUAL, this as that" — the two orders computed below; the Talmud's
  age/wisdom reading at the compile (Bava Batra 120a).
- Sifrei Bamidbar 133:3 — MATERIAL. On 27:2-3. (a) THE DATE BY THE ROSTER: "they stood only in the FORTIETH YEAR, the year
  Aaron died" — 33:38 "and Aaron the priest went up to Hor the mountain by the mouth of the LORD and died there in the fortieth
  year" (computed below): Eleazar in the court's list dates the case. (b) "before Moses and before Eleazar" — if Moses did not
  know, would Eleazar? INVERT the verse and expound it (R. Yoshiyah); Abba Chanin in R. Eliezer's name: they were in the
  STUDY HOUSE and came and stood before them — the same two arms as 68:1 (9:6) and 113:1 (15:33): the halt's stage across three
  cases. (c) R. AKIVA: "wilderness" here (27:3) and "wilderness" there (15:32) — as the man there is Zelophehad so here: THE
  IDENTITY ARM at its second seat, the verbal analogy from this side (113:1 gave it from the gatherer's; R. Yehuda b. Beteira's
  rebuke stands there — the registry's arm stays UNASSIGNED, the two rows now facing each other). (d) "not in the midst of the
  congregation" — the murmurers (Exod 16:2); "who gathered against the LORD" — the congregation of the SPIES (14:35's word,
  computed); "in Korach's congregation" — Korach's; "in his own sin he died" — he did not cause others to sin with him;
  "he had no sons" — had he a son, we would make no claim.
- Sifrei Bamidbar 133:4 — MATERIAL. On 27:4-5. (a) R. YEHUDA: "name" here and "name" there (Deut 25:6, the levirate — "that
  his name be not blotted out"): as name there is INHERITANCE so here, as name there is SEED so here — THE PLEA RIDES THE
  LEVIRATE'S WORD (the daughters' own levirate argument at the compile, Bava Batra 119b:10). (b) "because he has no son" after
  "he had no sons" — why twice? THEY WERE WISE AND EXPOUNDED: had there been a son's DAUGHTER we would make no claim (the
  son's line before the daughter — 134:2's a-fortiori). (c) R. Natan (the Hebrew's seat): the women's strength greater than
  the men's — the men "let us make a head and return to Egypt" (14:4), the women "give us a holding" (27:4). (d) R. CHIDKA:
  Shimon HaShikmoni, my colleague of R. Akiva's disciples, said — MOSES KNEW THAT DAUGHTERS INHERIT; on what was the question?
  whether they inherit WHAT IS FIT (ראוי, "expected" — the land not yet possessed) as WHAT IS HELD (מוחזק, "possessed") — THE
  FOURTH HALT'S UNCERTAINTY IS THE SCOPE (the Hebrew sets this line at 27:5's "and Moses brought their judgment"; the English
  under 27:4). The section of inheritances was fit to be said through Moses, but the daughters MERITED that it be said through
  them: "merit is rolled through the meritorious and liability through the liable" — R. Chidka's line on THREE of the four
  halts (68:1 the men, 114:1 the gatherer, here).
- Sifrei Bamidbar 134:1 — MATERIAL. On 27:6-7. (a) "RIGHTLY do the daughters speak" — they claimed well, "for SO IS THIS
  SECTION WRITTEN BEFORE ME ON HIGH": the rule pre-exists the case, the output READS a standing text (the installation
  setting's own witness on the shelf — the code is written before the run reaches it); "happy the man whose words the Place
  acknowledges" — likewise 36:5 "rightly the tribe of Joseph speak", 14:20 "I have forgiven according to your word". (b) THE
  THREE PORTIONS: "given shall be given" = their father's inheritance; "among their father's brothers" = their father's FATHER'S
  (Hepher's) share; "and you shall pass over the inheritance" = the FIRSTBORN'S portion — three portions (Mishnah Bava Batra
  8:3's row, the exam's); R. Eliezer b. Akiva (the Hebrew; the English "b. Yaakov"): also their father's brothers' share, from
  "given shall be given". (c) The Hebrew's bracket cites 36:1 for the "rightly" of 36:5 — the shelf's own slip, noted.
- Sifrei Bamidbar 134:2 — MATERIAL. On 27:8 (with 36:7-8, 27:11). THE INHERITANCE ORDER DERIVED — Mishnah Bava Batra 8:1-2's
  table at its verse: (a) "to the children of Israel speak" — this tells only the HOUR; the GENERATIONS from the address
  itself (the block's charter split at its fourth seat). (b) "in all the others GIVE, here PASS OVER" — Rebbi: none passes an
  inheritance but a daughter (tribe to tribe), her son and her husband inheriting her. (c) THE FATHER PRECEDES THE BROTHERS —
  R. Yishmael b. R. Yose: "you shall pass his inheritance to his daughter" — for a daughter you pass over the father, not for
  the brothers. (d) The father INHERITS — a-fortiori: the father's brothers come only by the father's power and inherit; the
  father himself, how much more. (e) THE SON'S DAUGHTER AS THE SON — a-fortiori from the daughters of Zelophehad, "who were
  only for the hour". (f) FEMALES AS MALES in all heirs — induction: as with sons, so with all; and MALES PRECEDE FEMALES in
  all; and as with the redeemers (Lev 25:49) sons as their fathers. (g) A daughter inherits her MOTHER — 36:8 "every daughter
  who inherits an inheritance from the tribes"; the son a-fortiori. (h) THE HUSBAND INHERITS HIS WIFE — R. Akiva from 27:11
  "of his family, and he shall inherit HER" (the feminine pronoun read of the wife; the shared phrase Lev 21:2, computed);
  R. Yishmael: not needed — 36:8 + 36:7 "shall not go around from tribe to tribe" + Josh 24:33 (Eleazar buried on Phinehas's
  hill in Ephraim — whence Phinehas's land in Ephraim? he married and inherited a wife) + 1 Chr 2:22 (Yair's cities in Gilead).
- Sifrei Bamidbar 134:3 — MATERIAL. On 27:11. (a) "of his family" — the father's family, not the mother's: 1:2 "by their
  families, by their fathers' house" — families follow the fathers. (b) "and he shall inherit her" — as above. (c) "A STATUTE
  OF JUDGMENT" — the Torah gave the sages knowledge to expound and say: whoever is nearest in flesh precedes in the
  inheritance (the phrase's two Torah seats computed: 27:11, 35:29).
- Sifrei Bamidbar 134:4 — CONTEXT. On 27:12. Mount Abarim = Reuben's inheritance; Moses rejoiced at entering Reuben's and
  Gad's, thinking the decree revoked, and poured out supplication — the king's son barred at the inner chamber; the
  a-fortiori to supplication.
- Sifrei Bamidbar 134:5 — CONTEXT. On Deut 3:23 (the Sifrei's excursus placed here). "Va'etchanan" a term of entreaty;
  "to say" — tell me whether I enter; the names and attributes read clause by clause; R. Yehuda b. Bava: "repent and I will
  accept" against the royal codex; "this good mountain" Jerusalem, "the Lebanon" the Temple or the kings. Deuteronomy's own
  pass read at Numbers' seat — the third pass's material, on the record for the readback.
- Sifrei Bamidbar 135:1 — CONTEXT. On Deut 3:26. "The LORD was wroth with me because of you"; "it is enough for you"; Moses's
  requests refused one by one — enter as a commoner, as Joshua's disciple ("a Rav does not become his disciple's disciple"),
  through the air, the bones across the Jordan — and "let me see it" granted: the distant shown as near.
- Sifrei Bamidbar 136:1 — CONTEXT. On Deut 34:4 and 3:28. The land shown as a set table (R. Akiva) or the eyes empowered to
  see end to end (R. Eliezer); two seeings (Abraham's of pleasure, Moses's of pain), two drawings-near (for Heaven, not for
  Heaven); "command Joshua" — toward Torah, or the Gibeonites (R. Yehuda), or the contentions; Moses saw what he did not
  traverse.
- Sifrei Bamidbar 136:2 — CONTEXT. On Deut 3:29. Beth-Peor; R. Yehuda b. Bava: three places Israel bordered on grave sin and
  was told "repent and I will accept".
- Sifrei Bamidbar 136:3 — MATERIAL. On 27:13. "As Aaron your brother was gathered" — Moses DESIRED such a death (the
  narrative's own claim on the verse).
- Sifrei Bamidbar 137:1 — MATERIAL. On 27:14. R. SHIMON B. ELAZAR: Moses and Aaron died by KARET — "because you did not
  sanctify Me" (Deut 32:51): had you sanctified Me, your time to die had not yet come. The two leaders' deaths read as a
  SANCTION from 20:12's clause — an effects-law line on the ledger (karet as the cause of a recorded death), owed to the
  readback.
- Sifrei Bamidbar 137:2 — CONTEXT. Two leaders: David "let my sin not be recorded" (Ps 32:1), Moses "let it be recorded" —
  the two flogged women parable; R. Eliezer HaModai: wherever a righteous one's death is mentioned, his sin is mentioned
  (the sons of Aaron at four seats), that none say a hidden corruption killed him.
- Sifrei Bamidbar 138:1 — MATERIAL. On 27:15. The righteous, about to die, set aside their own concerns for the
  congregation's; "to say" = tell me whether You appoint leaders — R. Eliezer b. Azaryah's FOUR "to say" requests each
  answered (Exod 6:12 → 7:4; Num 12:13 → 12:14; Deut 3:23 → 3:26; here → 27:18 "take Joshua").
- Sifrei Bamidbar 139:1 — MATERIAL. On 27:16. "God of the spirits of all flesh" — all spirits issue from Him; R. Eliezer son of
  R. Yose HaGelili's SIGN: the living soul deposited in its Owner's hand (Job 12:10), at death in the treasury (1 Sam 25:29),
  the wicked slung out; "a man over the congregation" — this is JOSHUA (Ps 78:25's "man"), unnamed by Moses so as not to stir
  strife between his sons and his brother's sons.
- Sifrei Bamidbar 139:2 — MATERIAL. On 27:17. "Who goes out before them" — at the head, not sending others (Moses against Og,
  21:34; Joshua 5:13; Phinehas 31:6); the four clauses expounded — at the head, in a troop, on the way, in his merits, WITH A
  COUNT (31:49 "not one of us is missing"); "sheep without a shepherd" — Song 1:7-8: the shepherds to serve Israel from the
  wilderness to the resurrection shown to Moses.
- Sifrei Bamidbar 140:1 — MATERIAL. On 27:18. "Take for YOURSELF" — whom you know worthy (Prov 27:18: the keeper of the
  fig tree eats its fruit, the keeper of his master is honored); "a man in whom there is spirit" — who accommodates each
  one's spirit; "LAY YOUR HAND" — give him an interpreter to ask, expound and RULE in your lifetime, lest they say "in his
  master's lifetime he did not rule, and now he rules" — raised from the ground to the bench; R. Natan: Moses silenced the
  interpreter when Joshua entered. THE OFFICE INSTALLED by the hand-laying, in the master's lifetime — an installing act's
  shape (D3), owed forward to Deut 34:9 and the sixth book.
- Sifrei Bamidbar 140:2 — MATERIAL. On 27:20. "OF your glory" — not all of it: Moses' face as the sun, Joshua's as the moon
  (Bava Batra 75a at the compile, per gap).
- Sifrei Bamidbar 141:1 — MATERIAL. On 27:21. Joshua needs Eleazar and Eleazar Joshua; "he shall inquire of him" — not
  between himself and himself: "by the judgment of the URIM"; not in a loud voice: "of him" — he stands and moves his lips,
  the high priest answers (Yoma 73a's procedure at the compile, per gap). THE COURT'S ORACLE: the leader's going out and
  coming in "by his mouth" — the priest's word.
- Sifrei Bamidbar 141:2 — MATERIAL. On 27:22. Moses did it WITH JOY, no regret for his son or his brother's sons; "he TOOK
  Joshua" — took him with WORDS, telling the reward of Israel's leaders in the world to come.
- Sifrei Bamidbar 141:3 — MATERIAL. On 27:23. "He laid his HANDS" — a full and overflowing vessel (Exod 33:11's attendant who
  did not depart; Josh 1:8's book that shall not depart; the a-fortiori to all men); "commanded him as the LORD spoke by the
  hand of Moses" — as the Holy One commanded Moses with joy, so Moses Joshua; lest one think Moses' powers waned — Deut 34:7:
  his eye undimmed between unclean and clean, forbidden and permitted, his strength unabated in Torah. THE HANDS plural
  against 27:18's hand singular (computed): the run exceeds the spec by the Sifrei's own reading.

## Onkelos Numbers 27:1-23 (__ONKROWS__ verses, read whole)
- Onkelos Num 27:1 — MATERIAL. "And they drew near, the daughters" (וַתִּקְרַבְנָה, "and they drew near", fem.) → וְקָרֵיבָא בְּנַת
  ("and the daughters approached") the feminine kept; "of the families of Manasseh" → לְזַרְעֲיַת מְנַשֶּׁה ("of the SEED-family
  of Manasseh") — the translation's word for family is SEED (R. Yehuda's second "name" reading, 133:4: name = seed); the
  five names literal.
- Onkelos Num 27:2 — MATERIAL. "And they stood before Moses" (וַתַּעֲמֹדְנָה, "and they stood") → וְקָמָא קֳדָם משֶׁה ("and they
  STOOD before Moses") — the standing verb, against 9:8's "stand" rendered "WAIT" (אוריכו) for the unclean men: here the
  daughters are heard standing, no wait written; "at the door of the tent of meeting" → בִּתְרַע מַשְׁכַּן זִמְנָא ("at the gate of
  the tent of meeting") — THE TENT named as the case's venue in the ink itself (D4's institution entity, its own verse);
  "saying" literal.
- Onkelos Num 27:3 — MATERIAL. "Our father died in the wilderness" literal; "who gathered against the LORD" → דְּאִזְדַּמָּנוּ עַל
  יְיָ ("who assembled against the LORD"); "in his own sin he died" (בְּחֶטְאוֹ, "in his sin") → אֲרֵי בְחוֹבֵיהּ מִית ("for in his
  DEBT he died") — the translation's word for sin is חוֹבָה ("liability, debt"): the effects law's own vocabulary on the
  decedent (the ledger's entry against him; 133:3's "he did not cause others to sin"); "and sons he had not" literal.
- Onkelos Num 27:4 — MATERIAL. "Why should the name of our father be WITHHELD" (יִגָּרַע, "be diminished") → לְמָא יִתְמְנַע
  ("why should it be HELD BACK") — the SAME Aramaic verb as 9:7's "why should we be held back" (נִתְמְנַע, computed): the two
  pleas one idiom in the translation, the ink's one root (computed below); "give us a holding" → הַב לָנָא אַחֲסָנָא ("give us
  a possession") — the inheritance noun.
- Onkelos Num 27:5 — MATERIAL. "And Moses brought their judgment before the LORD" (וַיַּקְרֵב מֹשֶׁה אֶת מִשְׁפָּטָן, "and Moses
  brought near their judgment") → וְקָרֵב משֶׁה יָת דִּינְהֶן קֳדָם יְיָ ("and Moses brought near their CASE before the LORD") —
  THE HALT'S THIRD FORM: no guard, no wait — the judgment itself CARRIED IN by Moses, in the offerings' causative verb
  (computed: the same form brings the offerings near at Lev 8-9); "their judgment" a word standing once in the Tanakh.
- Onkelos Num 27:6 — MATERIAL. "And the LORD SAID to Moses, SAYING" → וַאֲמַר יְיָ לְמשֶׁה לְמֵימָר — the frame "said... saying"
  (computed: five Torah seats; the block's fourth frame form).
- Onkelos Num 27:7 — MATERIAL. "Rightly" (כֵּן, "so / rightly") → יָאוּת ("fittingly"); "given shall be given" → מִתַּן תִּתֵּן
  (the doubled infinitive kept); "a holding of inheritance" → אֲחוּדַת אַחֲסָנָא ("a holding of possession"); "and you shall
  PASS OVER the inheritance of their father to them" (וְהַעֲבַרְתָּ, "and you shall pass over") → וְתַעֲבַר ("and you shall
  TRANSFER") — the transfer verb kept distinct from 27:9-11's "give" (וְתִתְּנוּן, "and you shall give"): Rebbi's reading
  (134:2) in the translation's two verbs.
- Onkelos Num 27:8 — MATERIAL. "A man, if he dies and has no son, you shall PASS his inheritance to his daughter" →
  וְתַעְבְּרוּן יָת אַחֲסַנְתֵּיהּ לִבְרַתֵּיהּ ("you shall transfer his possession to his daughter") — the daughter's verse alone
  carries the transfer verb (computed: והעברתם at 27:8 and Josh 4:3 in the whole Tanakh); the address "to the children of
  Israel speak" → the generations' rule (134:2).
- Onkelos Num 27:9 — CONTEXT. Literal; "give" (וְתִתְּנוּן) to his brothers.
- Onkelos Num 27:10 — CONTEXT. Literal; "give" to his father's brothers.
- Onkelos Num 27:11 — MATERIAL. "To his flesh who is near to him of his family" (לִשְׁאֵרוֹ הַקָּרֹב, "to his flesh, the near")
  → לְקָרִיבֵיהּ דְּקָרִיב לֵיהּ מִזַּרְעִיתֵיהּ ("to his relative who is near to him, of his seed-family"); "and he shall inherit
  HER" (וְיָרַשׁ אֹתָהּ, "and he shall inherit her/it") → וְיֵרַת יָתַהּ ("and he shall inherit it/her") — the feminine object kept
  (R. Akiva's wife reading rides it, 134:2); "a statute of judgment" (חֻקַּת מִשְׁפָּט, "a statute of judgment") → לִגְזֵרַת דִּין
  ("a DECREE of judgment") — the translation's word for statute is DECREE, the sages' rule of the near (134:3).
- Onkelos Num 27:12 — CONTEXT. "This mountain of Abarim" → לְטוּרָא דַעֲבָרָאֵי ("the mountain of the Abarites"); "see the land"
  literal.
- Onkelos Num 27:13 — CONTEXT. "Gathered to your people, you too, as Aaron your brother" literal.
- Onkelos Num 27:14 — MATERIAL. "You rebelled against MY MOUTH" (מְרִיתֶם פִּי, "you rebelled against my mouth") → סָרֵיבְתּוּן
  עַל מֵימְרִי ("you refused My WORD") — the Memra buffer on the divine mouth; "Kadesh" → רְקַם ("Rekem") — the translation's
  geography; "the waters of Meribah of Kadesh" → מֵי מַצּוּת רְקַם ("the waters of contention of Rekem"). Moses' sin recorded at
  his death's announcement (137:1-2).
- Onkelos Num 27:15 — NOT-BEARING. Speech frame ("and Moses spoke with the LORD, saying").
- Onkelos Num 27:16 — MATERIAL. "Let the LORD APPOINT" (יִפְקֹד, "let him appoint / visit") → יְמַנֵּי יְיָ ("let the LORD
  APPOINT") — the appointment verb: the office's installation asked for; "God of the spirits of all flesh" literal.
- Onkelos Num 27:17 — CONTEXT. Literal; "shepherd" → רָעֵי ("shepherd").
- Onkelos Num 27:18 — MATERIAL. "A man in whom there is spirit" (אִישׁ אֲשֶׁר רוּחַ בּוֹ, "a man that spirit is in him") → גְּבַר
  דִּי רוּחַ נְבוּאָה בֵיהּ ("a man in whom is the spirit of PROPHECY") — prophecy SUPPLIED; "and you shall lay your HAND on him"
  (וְסָמַכְתָּ אֶת יָדְךָ, "and you shall lean your hand") → וְתִסְמוֹךְ יָת יְדָךְ ("and you shall lay your hand") — the offerings'
  hand-laying verb (Lev 1:4) kept, the hand SINGULAR (computed).
- Onkelos Num 27:19 — CONTEXT. "Stand him before Eleazar the priest and before all the congregation, and command him before
  their eyes" → וּתְקֵים ("and you shall stand him") literal.
- Onkelos Num 27:20 — MATERIAL. "Of your MAJESTY" (מֵהוֹדְךָ, "of your splendor") → מִזִּיוָךְ ("of your RADIANCE") — the face's
  shine (140:2: sun and moon); "that they may HEAR" (יִשְׁמְעוּ, "they shall hear") → דִּי יְקַבְּלוּן מִנֵּיהּ ("that they may
  ACCEPT from him") — hearing rendered as acceptance.
- Onkelos Num 27:21 — MATERIAL. "By the judgment of the Urim" (בְּמִשְׁפַּט הָאוּרִים, "by the judgment of the Urim") → בְּדִין
  אוּרַיָּא ("by the judgment of the Urim") literal; "by his MOUTH they shall go out and by his mouth come in" (עַל פִּיו, "by
  his mouth") → עַל מֵימְרֵיהּ ("by his WORD") — the priest's mouth given the Memra word: the court's oracle (141:1).
- Onkelos Num 27:22 — CONTEXT. "And Moses did as the LORD commanded him; he took Joshua and stood him before Eleazar" literal.
- Onkelos Num 27:23 — MATERIAL. "And he laid his HANDS on him" (וַיִּסְמֹךְ אֶת יָדָיו, "and he leaned his hands") → וּסְמַךְ יָת
  יְדוֹהִי ("and he laid his HANDS") — the plural kept (computed: singular at 27:18); "as the LORD spoke by the hand of Moses"
  → בִּידָא דְמשֶׁה ("by the hand of Moses") literal.

## The ink beside the shelf (computed by this script from the Tanakh DB — never recited)
__INK__

## The finds (this ledger's crowns)
- THE HALT'S THIRD FORM (27:5, computed): "and Moses brought their judgment near before the LORD" — no guard (Lev 24:12, Num
  15:34), no "stand and I will hear" (9:8): the case CARRIED IN by Moses himself, in the causative verb that brings the
  offerings near; "their judgment" a word standing once. Design consequence: a third halt kind for the tent daemon — the
  judgment brought near, the persons standing (Onkelos: STOOD, where 9:8's men WAIT), the docket's debit owed.
- THE FOURTH UNCERTAINTY IS THE SCOPE (133:4, R. Chidka in Shimon HaShikmoni's name): Moses KNEW that daughters inherit; the
  question was whether they inherit what is FIT (the land not yet possessed) as what is HELD — completing the table Sanhedrin
  78b:7 opened (liable at all / the mode) and 68:1 extended (how): whether, which, how, HOW FAR. R. Chidka's line on three
  halts — "merit through the meritorious, liability through the liable" — the shelf's own pairing of the four cases.
- THE SECTION WRITTEN BEFORE ME ON HIGH (134:1): "rightly do the daughters speak — for so is this section written before Me":
  the tent's output READS a standing text; the rule pre-exists the case. The installation setting's own witness from the
  spine (the boot setting's shelf seat beside Yoma 28b's).
- THE OUTPUT'S FRAMES, FOUR FORMS (computed): spoke-saying (Lev 24:13, Num 9:9), said bare (15:35), said-saying (27:6), and
  MOSES commanding "by the mouth of the LORD" (36:5) — the second output on the same case relayed in Moses' mouth, no divine
  frame; "by the mouth of the LORD" the blasphemer's halt clause too (Lev 24:12).
- THE INHERITANCE ORDER AT ITS VERSE (134:2-3): the father precedes the brothers (R. Yishmael b. R. Yose from "pass over... to
  his daughter"), the father inherits (a-fortiori), the son's daughter as the son (a-fortiori from the daughters), females as
  males and males first in every degree (induction from sons), the daughter inherits her mother (36:8), the husband his
  wife (R. Akiva on "inherit HER" / R. Yishmael on Phinehas and Yair), "of his family" the father's (1:2), the near in flesh
  first — Mishnah Bava Batra 8:1-2's table, the compile's spec; and THE THREE PORTIONS (134:1) = Bava Batra 8:3's row.
- PASS OVER / GIVE (134:2, computed): the daughter's verse alone carries "pass over" in the whole Tanakh's inheritance
  verses; the brothers, uncles and flesh take "give" — Rebbi's transfer-by-a-daughter reading is the ink's two verbs, kept
  apart by Onkelos.
- THE PLEA RIDES THE LEVIRATE'S WORD (133:4, R. Yehuda): "name" here / "name" at Deut 25:6 — inheritance and seed; the
  daughters' own levirate argument (Bava Batra 119b:10) is run at the compile BEFORE the answer is read (step 5's shape).
- THE IDENTITY ARM AT ITS SECOND SEAT (133:3, R. Akiva): "wilderness" / "wilderness" — the gatherer is Zelophehad, the
  analogy given from the daughters' side; 113:1's rebuke (R. Yehuda b. Beteira) stands: the registry keeps the arm UNASSIGNED
  with both seats named. On R. Akiva's arm the fourth case's decedent is the third case's stoned man, and 27:3's "in his own
  sin he died" (Onkelos: in his DEBT) is the ledger's entry against him.
- THE DATE BY THE ROSTER (133:3, computed): Eleazar in the court's list — the fortieth year, after Aaron's death (33:38: the
  fifth month, the first day). A READING-PLACED date for the tape's marker, the teacher named.
- THE RUN IN THE SIXTH BOOK (computed): the feminine approach verb stands at 27:1 and Josh 17:4 alone — the daughters approach
  the same court with Joshua for Moses, cite the statute, and are GIVEN the land "by the mouth of the LORD": the first output's
  execution lies off the Torah — the readback's item (the fourth case closes in Joshua).
- THE THREE PLEAS, ONE VERB (computed): the root "be held back" at 9:7 (the men), 27:4 (the daughters), 36:3-4 (the tribes);
  Onkelos renders all with one Aramaic verb; the men's and the tribes' approaches share the masculine "drew near".
- THE OFFICE INSTALLED (140:1, 141:3): the hand laid in the master's lifetime that Joshua rule then; the hands plural at the
  run against the hand singular at the command (computed) — an installing act for the LEADERSHIP, owed forward to Deut
  34:9's second seat and the sixth book; Moses' desired death (136:3) and the KARET of the two leaders (137:1) on the
  readback's ledger.

## CITE INDEX — every source opened, each fully named
(one name per line; grouped ledger rows above never hide a name — the round-16 lesson standing; coverage COMPUTED
against the shelf's own row counts by the ledger script write_num27_36_ledgers.py: Sifrei piskaot 133-141 __SIFROWS__ rows
(133:1-4, 134:1-5, 135:1, 136:1-3, 137:1-2, 138:1, 139:1-2, 140:1-2, 141:1-3), Onkelos Numbers 27:1-23 __ONKROWS__ verses —
missing 0, extra 0; quick looks outside the span, not counted: Sifrei Bamidbar 132:1-4, 161:1)
__CITES__
(__SIFROWS__ Sifrei Bamidbar rows + __ONKROWS__ Onkelos verses = __N__ sources in this ledger.)

**read: __N__ of __N__ — COMPLETE** (__ONKROWS__ Onkelos verses + __SIFROWS__ Sifrei Bamidbar rows, all opened and
verdicted this sitting at the shelf's row grain; coverage computed by script against the shelf's own row counts:
missing 0, extra 0; verdicts MATERIAL 17 Sifrei + 15 Onkelos, CONTEXT 6 Sifrei + 7 Onkelos, NOT-BEARING 1 Onkelos — the
counts the script's own Counter measured)
'''

body36 = r'''# Numbers 36:1-13 derivation — Onkelos as the spine's remaining half (the Sifrei on Numbers ENDS at 35:29 — computed:
# its last piska, 161, opens on 35:29 and no piska opens on chapter 36; the shelf's own end recorded, not a gap of ours),
# THE FOURTH NUMBERS READING (2026-09-09; THE TENT sitting 4 — the daughters of Zelophehad, the second output, World/step9/THE_TENT.md
# section 4). DECLARED (THE_STEPS Step 2, the spine default of 2026-08-27): scope = Onkelos Numbers 36:1-13 (__ONKROWS__ verses,
# the chapter whole, fresh) + the Sifrei's rows that treat 36:5-11 from their seat at chapter 27, CREDITED from the same sitting's
# ledger num_27_zelophehad_joshua_2026-09-09.md where they were read whole (133:2 on 36:11's order; 134:1 on 36:5's "rightly";
# 134:2 on 36:7-8 the daughter's and the husband's inheritance) — __CRED__ credits, each quick-looked again here. THE TESTING
# SHELF routed to Step 5 (the compile sitting's docket): Mishnah Bava Batra 8:1-8; Tosefta Bava Batra 7; Mishnah Taanit 4:8 (the
# fifteenth of Av — the day the tribes were permitted to intermarry, Bava Batra 121a). The Babylonian Talmud — Bava Batra
# 120a-121a (36:6 "this is the thing": the rule for that generation alone; the names' orders; the fifteenth of Av), 111b-112b
# (36:7-9 the transfer barred; the husband's inheritance) — is the bridge, PER GAP at the compile. OUTSIDE DECLARED SCOPE,
# enumerated and unread (the shelf's other works on Numbers, __OUTSIDE__ directories): __OUTSIDE_LIST__.

## Sifrei Bamidbar — rows on 36:5-11, credited from the 27 ledger (read whole this sitting; quick-looked here)
- Sifrei Bamidbar 133:2 — CREDITED (num_27_zelophehad_joshua_2026-09-09.md). The names' second order at 36:11 against 27:1 —
  "all equal, this as that" (the delta computed below).
- Sifrei Bamidbar 134:1 — CREDITED. "Rightly the tribe of Joseph speak" (36:5) beside "rightly do the daughters speak" (27:7) —
  the two acknowledgments the Sifrei pairs: the second output answers the second plea in the first's word.
- Sifrei Bamidbar 134:2 — CREDITED. 36:8 "every daughter who inherits an inheritance" — the daughter inherits her mother; 36:7
  "shall not go around from tribe to tribe" — R. Yishmael's route to the husband's inheritance (Phinehas's hill, Yair's cities).

## Onkelos Numbers 36:1-13 (__ONKROWS__ verses, read whole)
- Onkelos Num 36:1 — MATERIAL. "And the heads of the fathers drew near" (וַיִּקְרְבוּ, "and they drew near") → וְקָרִיבוּ רֵישֵׁי
  אֲבָהָתָא ("and the heads of the fathers approached") — the masculine approach verb, the unclean men's (9:6, computed); "of
  the family of the sons of Gilead" → לְזַרְעִית ("of the seed-family"); "and they spoke before Moses and before the princes,
  the heads of the fathers" literal — THE THIRD PLEA of the block, the tribe's against the daughters' grant.
- Onkelos Num 36:2 — MATERIAL. "The LORD commanded my lord to give the land by lot" (בְּגוֹרָל, "by lot") → בְּעַדְבָא ("by lot");
  "and my lord was commanded BY THE LORD" (צֻוָּה בַּיהוָה, "was commanded by the LORD") → אִתְפַּקַּד בְּמֵמְרָא דַיְיָ ("was
  commanded by the WORD of the LORD") — the Memra buffer; "to give the inheritance of Zelophehad our brother to his daughters"
  literal: THE TRIBES CITE THE FIRST OUTPUT AS STANDING LAW — the second case reads the first case's rule off the ledger, in
  the ink.
- Onkelos Num 36:3 — MATERIAL. "Their inheritance shall be DIMINISHED from our fathers' inheritance" (וְנִגְרְעָה, "and it shall
  be diminished") → וְתִתְמְנַע ("and it shall be held back") — the plea verb of 9:7 and 27:4 in the translation's one idiom
  (computed); "and added to the tribe's inheritance" → וְתִתּוֹסַף; "from the LOT of our inheritance" → וּמֵעֲדַב ("and from the
  lot") — the apportionment by lot (26:55) named in the argument.
- Onkelos Num 36:4 — MATERIAL. "And if the JUBILEE be for the children of Israel" (הַיֹּבֵל, "the jubilee") → וְאִם יְהֵי יוֹבְלָא
  ("and if the jubilee shall be") — the tribes' argument reaches the RELEASE: even the jubilee does not return an inheritance
  that passed by marriage (a sale returns, an inheritance does not) — the ninth Torah seat of the word outside Exod 19:13 and
  Lev 25/27 (computed): a REFERENCE to the jubilee engine by the ink's own word.
- Onkelos Num 36:5 — MATERIAL. "And Moses COMMANDED the children of Israel BY THE MOUTH OF THE LORD, saying" (עַל פִּי יְהוָה, "by
  the mouth of the LORD") → וּפַקִּיד משֶׁה ("and Moses commanded") with עַל מֵימְרָא דַיְיָ לְמֵימָר ("by the WORD of the LORD,
  saying") — THE SECOND OUTPUT'S FRAME is Moses' own command by the Word, no "and the LORD said" (computed: the phrase's eighteen
  Torah seats, Lev 24:12's halt among them); "rightly the tribe of the sons of Joseph speak" → יָאוּת ("fittingly") — 27:7's
  word (134:1).
- Onkelos Num 36:6 — MATERIAL. "THIS IS THE THING that the LORD commanded concerning the daughters" (זֶה הַדָּבָר, "this is the
  thing") → דֵּין פִּתְגָּמָא ("this is the word") — the formula's eight Torah seats computed (the Talmud's reach-rule at the
  compile: for this generation); "as is GOOD in their eyes they shall be wives" (לַטּוֹב בְּעֵינֵיהֶם, "to the good in their eyes")
  → לִדְתַקִּין בְּעֵינֵיהוֹן ("to whoever is FITTING in their eyes") — the permission; "ONLY to the family of their father's
  tribe" (אַךְ, "only") → בְּרַם ("however") — the restriction: permission and limit in one verse.
- Onkelos Num 36:7 — MATERIAL. "And an inheritance shall not GO AROUND from tribe to tribe" (וְלֹא תִסֹּב, "and it shall not
  turn about") → וְלָא תַסְחַר ("and it shall not circulate"); "for each man to the inheritance of his fathers' tribe shall the
  children of Israel CLEAVE" (יִדְבְּקוּ, "they shall cleave") → יִדַּבְּקוּן ("they shall cleave") — Gen 2:24's verb (computed):
  the man cleaves to his tribe's land as to a wife.
- Onkelos Num 36:8 — MATERIAL. "And every daughter who inherits an inheritance from the tribes" (יֹרֶשֶׁת, "inheriting") →
  וְכָל בְּרַתָּא יָרְתַת אַחֲסָנָא ("and every daughter inheriting a possession") — 134:2's seat for the daughter inheriting her
  MOTHER; "to one of the family of her father's tribe shall she be a wife" literal; "that the children of Israel may inherit
  each the inheritance of his fathers" literal.
- Onkelos Num 36:9 — CONTEXT. The rule of 36:7 repeated with "to ANOTHER tribe" (אַחֵר, "another") → אוֹחֲרָנָא ("another");
  "the tribes shall cleave, each man in his inheritance" literal.
- Onkelos Num 36:10 — MATERIAL. "As the LORD commanded Moses, SO DID the daughters of Zelophehad" (כֵּן עָשׂוּ, "so they did") →
  כֵּן עֲבָדוּ ("so they did") — the report formula of Lev 24:23 and Num 15:36 on the fourth case: THE EXECUTION is the
  daughters' own act, the marriage within the tribe (the Talmud at the compile: they were permitted any man and married
  within by counsel — Bava Batra 120a).
- Onkelos Num 36:11 — MATERIAL. "And Mahlah, TIRZAH, Hoglah, Milcah and NOAH the daughters of Zelophehad were wives to the sons
  of their UNCLES" (לִבְנֵי דֹדֵיהֶן, "to the sons of their uncles") → לִבְנֵי אֲחֵי אֲבוּהֶן ("to the sons of their FATHER'S
  BROTHERS") — the uncle noun expanded to the father's brothers (the tribe of the father, 36:6's limit met at its narrowest);
  the names' second order (computed).
- Onkelos Num 36:12 — MATERIAL. "Of the families of the sons of Manasseh they were wives" literal; "and their inheritance
  REMAINED on the tribe of their father's family" (וַתְּהִי נַחֲלָתָן, "and their inheritance was") → וַהֲוַת אַחֲסַנְתְּהֶן עַל
  שִׁבְטָא ("and their possession was upon the tribe") — the ledger's close in the ink: the tribe's plea satisfied, the land
  stayed.
- Onkelos Num 36:13 — CONTEXT. THE COLOPHON: "these are the commandments and the judgments that the LORD commanded by the hand
  of Moses" → אִלֵּין פִּקּוֹדַיָּא וְדִינַיָּא ("these are the commandments and the judgments"); "in the plains of Moab by the
  Jordan of Jericho" → בְּמֵישְׁרַיָּא דְמוֹאָב ("in the plains of Moab") — the book closes at the site where Deuteronomy's pass
  opens (Deut 1:5, computed): the readback's own place-name.

## The ink beside the shelf (computed by this script from the Tanakh DB — never recited)
__INK__

## The finds (this ledger's crowns)
- THE SECOND OUTPUT ON THE SAME CASE (36:5-9): a tribe's plea against the daughters' grant, answered in Moses' mouth "by the
  mouth of the LORD" — no divine speech frame (computed) — with "rightly" (27:7's word) and "THIS IS THE THING" (the formula's
  eight seats): a permission ("as is good in their eyes") and its limit ("only to their father's tribe"), the transfer barred
  in the circling verb, the cleaving verb of Gen 2:24. The statute of 27:8-11 AMENDED by a second case on the same entity —
  the tent's output form the map named (the reach: the Talmud's "this generation" at the compile).
- THE SECOND CASE READS THE FIRST'S RULE OFF THE LEDGER (36:2): "my lord was commanded by the LORD to give Zelophehad's
  inheritance to his daughters" — the tribes cite the first output as standing law in the ink; the sequence world's docket
  row of 27:6-11 is the thing they cite.
- THE JUBILEE IN THE ARGUMENT (36:4, computed): the tribes reach for the release — even the jubilee does not return it — the
  ninth Torah seat of the word: a REFERENCE edge to the jubilee engine by the ink's own token.
- THE EXECUTION IS THE DAUGHTERS' OWN ACT (36:10-12, computed): "as the LORD commanded Moses, so they did" — the report formula
  of the stoned cases' executions on a marriage; the inheritance REMAINED on the tribe: the ledger's close written in the ink.
  The first output's execution (the GIVING of the land) lies off the Torah at Josh 17:4 — the readback's item.
- THE THREE PLEAS, ONE VERB (computed): 9:7, 27:4, 36:3-4 — "be held back"; Onkelos's one idiom for all three.
- THE COLOPHON (36:13, computed): the plains of Moab — Deuteronomy opens there: the third pass's site named at the fourth book's
  last verse.

## CITE INDEX — every source opened, each fully named
(one name per line; coverage COMPUTED against the shelf by the ledger script write_num27_36_ledgers.py: Onkelos Numbers
36:1-13 __ONKROWS__ verses — missing 0, extra 0; the Sifrei on Numbers holds NO piska on chapter 36 (computed: the last piska,
161, opens on 35:29) — its three rows on 36:5-11 credited from the 27 ledger, named below as credits)
__CITES__
__CREDLINES__
(__ONKROWS__ Onkelos verses fresh + __CRED__ Sifrei Bamidbar rows credited = __N__ sources in this ledger.)

**read: __N__ of __N__ — COMPLETE** (__ONKROWS__ Onkelos verses opened and verdicted this sitting at the shelf's row grain,
coverage computed by script — missing 0, extra 0 — plus __CRED__ Sifrei rows credited from the same sitting's 27 ledger with
the quick look recorded; verdicts MATERIAL 11 Onkelos, CONTEXT 2 Onkelos, CREDITED 3 Sifrei — the counts the script's own
Counter measured)
'''
# ---- verdict census (the script's own Counter, asserted against the prose) ----
v27 = re.findall(r'^- (Sifrei Bamidbar \d+:\d+|Onkelos Num 27:\d+) — (MATERIAL|CONTEXT|NOT-BEARING)', body27, re.M)
assert [v for v, _ in v27] == cite27, (len(v27), [v for v, _ in v27][:50])
vc27 = Counter((v.split()[0], k) for v, k in v27)
assert vc27 == Counter({('Sifrei', 'MATERIAL'): 17, ('Sifrei', 'CONTEXT'): 6, ('Onkelos', 'MATERIAL'): 15, ('Onkelos', 'CONTEXT'): 7, ('Onkelos', 'NOT-BEARING'): 1}), vc27
v36 = re.findall(r'^- (Sifrei Bamidbar \d+:\d+|Onkelos Num 36:\d+) — (MATERIAL|CONTEXT|NOT-BEARING|CREDITED)', body36, re.M)
assert [v for v, _ in v36] == CREDITED36 + cite36, [v for v, _ in v36]
vc36 = Counter((v.split()[0], k) for v, k in v36)
assert vc36 == Counter({('Sifrei', 'CREDITED'): 3, ('Onkelos', 'MATERIAL'): 11, ('Onkelos', 'CONTEXT'): 2}), vc36
N36_all = N36 + len(CREDITED36)
body27 = (body27.replace('__OUTSIDE_LIST__', ', '.join(outside)).replace('__OUTSIDE__', str(len(outside)))
          .replace('__CITES__', '\n'.join(cite27)).replace('__SIFROWS__', str(sifrei_rows)).replace('__ONKROWS__', str(onk27))
          .replace('__N__', str(N27)).replace('__INK__', '\n'.join(ink27)))
body36 = (body36.replace('__OUTSIDE_LIST__', ', '.join(outside)).replace('__OUTSIDE__', str(len(outside)))
          .replace('__CITES__', '\n'.join(cite36)).replace('__CREDLINES__', '\n'.join(c + ' (credited)' for c in CREDITED36))
          .replace('__ONKROWS__', str(onk36)).replace('__CRED__', str(len(CREDITED36))).replace('__N__', str(N36_all))
          .replace('__INK__', '\n'.join(ink36)))
open(OUT27, 'w', encoding='utf-8').write(body27)
open(OUT36, 'w', encoding='utf-8').write(body36)
print('wrote', OUT27, '| sources', N27, '| Sifrei rows', sifrei_rows, 'in piskaot', span_p, '| Onkelos', onk27)
print('wrote', OUT36, '| sources', N36_all, '| Onkelos', onk36, '| Sifrei credited', len(CREDITED36), '| the shelf ends at piska', last_p, heads[last_p])
print('| outside scope', len(outside))
