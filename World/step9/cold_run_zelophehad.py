#!/usr/bin/env python3
# NUM 27:1-11 + 36:1-12 — THE DAUGHTERS OF ZELOPHEHAD (THE TENT sitting 4, 2026-09-09; World/step9/THE_TENT.md section 4).
# The third Numbers span compiled, and the FOURTH CASE-BORN LAW: the run halts on the daughters' plea — the halt's THIRD FORM
# ("and Moses brought their judgment near before the LORD", 27:5: no guard, no wait; the uncertainty THE SCOPE, the fit against
# the held) — and the tent's output (27:6-11) is the statute of inheritances itself: THE LADDER for the generations (Mishnah Bava
# Batra 8:2), the instance's verdict inside it ("given shall be given"). A second plea on the same case (the tribes, 36:1-4) does
# not halt and is answered RELAYED in Moses' mouth (36:5-9): a rule inside the case-born law, with a reach ("this is the thing" —
# this generation; lapsed on the fifteenth of Av). The execution is the daughters' own marriage (36:10-12); the giving lies in the
# sixth book (Josh 17:4) — OPEN on the ledger, the readback's item. G2's owed-forward edge (the family engine's 48:6) PAID here:
# what Genesis holds is CALLED (the no-son clause census, the firstborn's double and the held, the jubilee's non-return, name =
# inheritance); what Numbers holds is compiled — the ladder, the nearness key, the husband and the wife, the mother's property, the
# Sadducees' row, the apportionment's three arms, the ten parts of Joshua 17:5, the fit and the held, the daughters' own levirate
# dilemma (run BEFORE the output at the cursor — THE LOOP step 5), the reach and the lapse. Five motions of the deliverable rule,
# the wrap the sixth; every cell cites its source; every token probed (zero-report law); effects on every cell (the effects law).
# Reading ledgers: logic/oral_triage/num_27_zelophehad_joshua_2026-09-09.md, num_36_heiresses_2026-09-09.md (the Sifrei on Numbers
# 133-141 + Onkelos 27 and 36); the exam's docket: num_27_inheritance_exam_2026-09-09.md.

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 55, ("the guard counted %d expectations, the tripwire holds 55" % GUARDED)   # measured by the guard before the first run (55; the hand had 46), then typed
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, contextlib
import effects_layer as FX
import world_engine as WE
import cold_run_family as FAM            # THE EDGE (dependency_dispositions.yaml: zelophehad -> family CALL, reference — the no-son clause census, the firstborn's double and the held, the jubilee's non-return, name = inheritance)
import cold_run_sanctions as SAN         # THE EDGE (zelophehad -> sanctions CALL, reference — the levirate bond's brother condition for the dilemma's second horn)

db = sqlite3.connect('<repo-old>/elijah_docket/tanakh.sqlite')

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def verse_text(book, ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=?
        AND v.chapter=? AND v.verse=? ORDER BY w.idx""", (book, ch, vs)).fetchall()
    return ' '.join(strip(h) for (h,) in rows)

# ---- zero-report probes: the span's load-bearing tokens ---------------------------------------------------
PROBES = [
    ('Num', 'ותקרבנה', 27, 1, 'and they drew near (fem.) — the case and Josh 17:4 alone'),
    ('Num', 'ותעמדנה', 27, 2, 'and they stood — before Moses and Eleazar'),
    ('Num', 'במדבר',   27, 3, 'in the wilderness — R. Akiva\'s shared word with 15:32'),
    ('Num', 'בחטאו',   27, 3, 'in his own sin — the decedent\'s debt (Onkelos)'),
    ('Num', 'יגרע',    27, 4, 'be withheld — the three pleas\' verb (9:7, 36:3-4)'),
    ('Num', 'אחזה',    27, 4, 'a holding — the plea\'s noun, the effect'),
    ('Num', 'ויקרב',   27, 5, 'and he brought near — the halt\'s third form'),
    ('Num', 'משפטן',   27, 5, 'their judgment — once in the Tanakh (the large nun)'),
    ('Num', 'לאמר',    27, 6, 'saying — the frame said-saying'),
    ('Num', 'כן',      27, 7, 'rightly — the section written on high'),
    ('Num', 'והעברת',  27, 7, 'and you shall pass over — the firstborn\'s portion (Sifrei 134:1)'),
    ('Num', 'והעברתם', 27, 8, 'and you shall pass over — the daughter\'s verb, the Torah\'s one seat'),
    ('Num', 'ונתתם',   27, 9, 'and you shall give — the brothers'),
    ('Num', 'לשארו',   27, 11, 'to his flesh — the wife\'s word (Lev 21:2)'),
    ('Num', 'הקרב',    27, 11, 'the near — the ladder\'s key'),
    ('Num', 'אתה',     27, 11, 'her — the husband inherits the wife'),
    ('Num', 'לחקת',    27, 11, 'for a statute — of judgment (35:29 the other seat)'),
    ('Num', 'ויקרבו',  36, 1, 'and they drew near — the tribes\' heads (9:6\'s verb)'),
    ('Num', 'בגורל',   36, 2, 'by lot — the apportionment cited'),
    ('Num', 'היבל',    36, 4, 'the jubilee — reached in the argument'),
    ('Num', 'פי',      36, 5, 'the mouth — by the mouth of the LORD, the relayed frame'),
    ('Num', 'זה',      36, 6, 'this — this is the thing: the reach'),
    ('Num', 'אך',      36, 6, 'only — the limit'),
    ('Num', 'תסב',     36, 7, 'shall go around — the transfer barred'),
    ('Num', 'ידבקו',   36, 7, 'shall cleave — Gen 2:24\'s verb'),
    ('Num', 'ירשת',    36, 8, 'inheriting — every daughter who inherits'),
    ('Num', 'עשו',     36, 10, 'they did — as the LORD commanded'),
    ('Num', 'דדיהן',   36, 11, 'their uncles — the husbands'),
    ('Num', 'ותהי',    36, 12, 'and it remained — the inheritance on the tribe'),
    ('Num', 'בנות',    26, 33, 'daughters — the census names them first'),
    ('Num', 'בגורל',   26, 55, 'by lot — the apportionment\'s rule'),
    ('Num', 'ינחלו',   34, 17, 'shall apportion — Eleazar and Joshua, the court that owes the holding'),
    ('Deut', 'ובן',    25, 5, 'and a son — the levirate\'s clause (OWED FORWARD to Deuteronomy)'),
    ('Deut', 'שנים',   21, 17, 'two — the firstborn\'s double portion (OWED FORWARD)'),
    ('Lev', 'לשארו',   21, 2, 'to his flesh — the priest\'s mourning list'),
    ('Exod', 'מורשה',  6, 8, 'a heritage — the scope\'s uncertainty read off the promise (Bava Batra 119b:3)'),
    ('Josh', 'ויתן',   17, 4, 'and he gave — the run in the sixth book'),
    ('Josh', 'עשרה',   17, 5, 'ten — the ten parts'),
    ('Josh', 'פינחס',  24, 33, 'Phinehas — his hill in Ephraim: the husband inherits (R. Yishmael)'),
]
for book, tok, ch, vs, note in PROBES:
    if tok not in verse_text(book, ch, vs).split():
        sys.exit('ZERO-REPORT LAW: probe %r (%s) failed at %s %d:%d — refusing to run' % (tok, note, book, ch, vs))
print('probes: all %d token probes fired  [zero-report law satisfied]\n' % len(PROBES))

# the sixth book's houses (Josh 17:2), counted from the ink — the ten parts' arithmetic (Bava Batra 118b:8-10)
HOUSES_17_2 = [w for w in verse_text('Josh', 17, 2).split() if w in ('לבני', 'ולבני')][1:]   # the first 'to the sons of' is Manasseh's own; the six that follow are the houses
assert len(HOUSES_17_2) == 6, HOUSES_17_2
FRAMES = {}
for b, c, v in (('Lev', 24, 13), ('Num', 9, 9), ('Num', 15, 35), ('Num', 27, 6), ('Num', 36, 5)):
    ws = verse_text(b, c, v).split()
    FRAMES['%s %d:%d' % (b, c, v)] = (' '.join(ws[:2]), 'לאמר' in ws)
NO_SON_SEATS = FAM.levirate('no_son_clause')['v']                    # CALLED: the census of 'and he has no son' — Deut 25:5 and Num 27:8 alone
assert NO_SON_SEATS == ['Deut 25:5', 'Num 27:8'], NO_SON_SEATS
HELD_NOT_DUE = FAM.inheritance('held_not_due')['v']                  # CALLED: Bekhorot 8:9's held-not-due on 48:21-22 (the held 'I took', the due 'bring you back')
JUBILEE_RETURNS = FAM.inheritance('gift_returns_dispute')['v']       # CALLED: Bekhorot 8:10 — what does NOT return in the jubilee (the wife's inheritor among them)
NAME_IS_INHERITANCE = FAM.levirate('name_is_inheritance')['v']       # CALLED: Yevamot 24a — 'name' at Deut 25:6 means inheritance, from 48:6
BOND_NOT_IN_WORLD = SAN.levirate('not_in_world')['v']                # CALLED: the bond's brother condition — 'when brothers dwell together' (Deut 25:5)

P = []  # the provenance trail of the case being run
def ink(ref, note):  P.append(('INK',  '%s — %s' % (ref, note)))
def move(src, note): P.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P.append(('DATA', note))

def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P)


# ===== THE DATA CHANNEL — the parameter rows the ink leaves open (motion 2's recorded settings) ============
DATA = {
    'land_divided_among': {
        'value': 'left_egypt',
        'settings': {
            'left_egypt': "the land was divided among those who LEFT EGYPT — R. Yoshiyah, from 'by the names of the tribes of their fathers they shall inherit' (26:55); 'unto these' (26:53) excludes the minors (Bava Batra 117a:2 = Sifrei Bamidbar 132:1); the Mishnah's three portions follow it (117a:1)",
            'entered': "among those who ENTERED the land — R. Yonatan, from 'unto these the land shall be divided' (26:53); 'by the names of their fathers' — the dead inherit the living (117a:3; Rebbi's two brothers, priests, at the threshing floor, 117a:4)",
            'both': "to these and to these — R. Shimon b. Elazar: a share with the leavers and a share with the enterers, both verses satisfied (Sifrei 132:1)"},
        'source': "the ink gives two verses (26:53, 26:55) and names no rule between them — the arm is a DATUM"},
    'eretz_yisrael_status': {
        'value': 'held',
        'settings': {
            'held': "the land of Israel is HELD (in possession) before its assignment — Rabba (Bava Batra 119a:5, from R. Yehuda's four parts, Josh 17:5): the firstborn's double applies to it",
            'due': "the land was merely DUE to Hepher; the Mishnah's double is in tent pegs and movables — Rav Yehuda in Shmuel's name (119a:4)"},
        'source': "Exod 6:8 'I will give it to you as a HERITAGE' — read both ways (119b:3-4: an inheritance from your fathers / the generation bequeaths and does not inherit); THE SCOPE Moses asked about"},
    'mothers_property': {
        'value': 'son_first',
        'settings': {
            'son_first': "in the mother's property the son precedes the daughter — the first tanna (Bava Batra 111a:2: 'from the place you came')",
            'equal': "the son and the daughter are EQUAL in the mother's property — R. Zekharya b. HaKatzav: 'it is sufficient that the conclusion be like its source' (111a:3, the dayo cap)"},
        'source': "36:8 'every daughter who inherits from the TRIBES' gives the daughter her mother's (111a:1); the son's is an a-fortiori (111a:2) — its reach is the tradition's fork"},
    'daughters_marriage': {
        'value': 'permitted_advised',
        'settings': {
            'permitted_advised': "the daughters of Zelophehad were PERMITTED any tribe — 'to whom is good in their eyes' (36:6); 'only to their father's tribe' is GOOD ADVICE — Rav Yehuda in Shmuel's name (Bava Batra 120a:6); the generation commanded, the daughters excepted (120a:9)",
            'commanded': "the whole generation commanded, the daughters included — the baraita of 120a:8 as Rabba first read it"},
        'source': "36:6 writes the permission and the limit in one verse; whose the limit binds is the tradition's fork"},
    'tribe_transfer_reach': {
        'value': 'this_generation',
        'settings': {
            'this_generation': "'THIS is the thing that the LORD commanded' (36:6) — this thing is practiced in THIS GENERATION alone — Rava (Bava Batra 120a:10); the silence test: had it been for all generations the verse would be silent (120b:2); LAPSED on the fifteenth of Av — the day the tribes were permitted to intermarry (121a:7; Mishnah Taanit 4:8)",
            'all_generations': "for the generations — the formula read as the outside-slaughter's (Lev 17:2, 'throughout their generations' 17:7) — refused at 120a:11 / 120b:2: no other teaching hangs on the phrase here"},
        'source': "the ink's formula 'this is the thing' at eight Torah seats (computed) — the reach is read off it, not stated"},
    'names_order': {
        'value': 'wisdom_then_age',
        'settings': {
            'wisdom_then_age': "27:1 lists them by WISDOM (Mahlah, Noah, Hoglah, Milcah, Tirzah), 36:11 by AGE (Mahlah, Tirzah, Hoglah, Milcah, Noah) — R. Ami: in judgment and learning by wisdom, at a meal by age (Bava Batra 120a:4)",
            'equal': "all EQUAL — 'vatihyena', one existence: the school of R. Yishmael (120a:5); Sifrei Bamidbar 133:2"},
        'source': "the two orders are the ink's own (computed: 26:33, 27:1, Josh 17:3 against 36:11); what they mean is the tradition's fork"},
}
LADDER = [('son', 'the son'), ('sons_line', "the son's line"), ('daughter', 'the daughter'), ('daughters_line', "the daughter's line"),
          ('father', 'the father'), ('brothers', 'the brothers'), ('brothers_line', "the brothers' line"),
          ('fathers_brothers', "the father's brothers"), ('fathers_brothers_line', "the father's brothers' line")]
def heir_of(survivors):
    """THE LADDER (Num 27:8-11 read by Mishnah Bava Batra 8:2 with the nearness key of Bava Batra 108b:3): the first degree present"""
    for key, name in LADDER:
        if survivors.get(key):
            return key, name
    return 'nearest_flesh', 'the nearest of flesh — the line climbed to Reuben son of Jacob'


# ===== F1: THE INHERITANCE ORDER — the ladder, the shares, the apportionment (Num 27:8-11, 26:53-55; Deut 21:17) =============
def inheritance_order(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'ladder':
        ink('Num 27:8-11', '"if a man dies and has no son, you shall PASS his inheritance to his daughter; if no daughter, GIVE it to his brothers; '
                           'if no brothers, to his father\'s brothers; if his father has no brothers, to his flesh who is NEAR to him of his family"')
        move('Mishnah Bava Batra 8:2', 'the son precedes the daughter, and his line; the daughter precedes the brothers, and her line; the brothers '
             'precede the uncles, and their line — whoever precedes, his line precedes; the father who inherits precedes all his line')
        move('Bava Batra 108b:3, 110b:5', '"his flesh" is the FATHER — before the deceased\'s brothers; "the NEAR to him" — the nearer the earlier: '
             'the son, and the daughter, before the father (109a:2: the levirate\'s brother is no evidence of nearness)')
        key, name = heir_of(case['survivors'])
        if key == 'nearest_flesh':
            move('Bava Batra 115b:1', 'no offspring, no father, no brother, no uncle: the family line examined up to Reuben son of Jacob — a tribe is '
                 'never wholly cut off (Abaye: a tradition)')
        if case['survivors'].get('daughter') and case['survivors'].get('sons_line') and case.get('claimant_degree') == 'daughter':
            move('Bava Batra 115b:2-6', 'the daughter WITH the son\'s daughter — the Sadducees\' act (Rav Huna in Rav\'s name; Rabban Yochanan b. '
                 'Zakkai: grandchildren are as children, Gen 36:20/24); refused')
            return out("the son's line — not the daughter with her (the Sadducees' act, refused)", ['exempt'])
        fx = ['holding_owed'] if case.get('claimant_degree') == key else ['exempt']
        return out(name, fx)
    if ask == 'nearness_key':
        ink('Num 27:11', '"to his flesh who is NEAR to him" — the key word הקרב ("the near"), computed')
        move('Bava Batra 108b:3-4', 'the nearer the earlier — the son nearer than the father (he stands in his place for the maidservant and the '
             'ancestral field); the father nearer than the brothers ("his flesh")')
        return out('the nearer the earlier — the son before the father, the father before the brothers', [FX.NONE])
    if ask == 'source_of_rule':
        ink('Num 27:4, 27:8', 'the plea "because he has no son" against the output "if a man dies and has no son"')
        move('Bava Batra 110b:3-4', 'Rav Acha b. Yaakov reads the son\'s precedence off the PLEA (27:4); the difficulty — perhaps the daughters '
             'spoke by the custom of their time and the Torah then equalized? — settles it: the rule is read off the OUTPUT (27:8, Abaye)')
        return out('from the output (27:8), not the plea (27:4)', [FX.NONE])
    if ask == 'husband':
        ink('Num 27:11', '"his flesh who is near to him of his family, and he shall inherit HER" (the feminine object, computed; "his flesh" at Lev 21:2 alone besides)')
        move('Bava Batra 111b:8', '"his flesh" is the WIFE; "and he shall inherit HER" — he inherits her, she does not inherit him (Mishnah 8:1: a man '
             'his wife — inherits, does not bequeath); Sifrei 134:2: R. Akiva\'s reading; R. Yishmael from Phinehas\'s hill (Josh 24:33) and Yair\'s cities (1 Chr 2:22)')
        if case.get('claimant') == 'wife':
            return out('the wife does not inherit her husband', ['exempt'])
        return out('the husband inherits the wife; she does not inherit him', ['holding_owed'])
    if ask == 'mothers_property':
        ink('Num 36:8', '"every daughter who inherits an inheritance from the TRIBES of the children of Israel" — the plural: a daughter of two tribes inherits both — her mother\'s too')
        move('Bava Batra 111a:1-2', 'the daughter inherits her mother (36:8); the son a-fortiori; and from the same place — the son precedes the daughter in the mother\'s property (the first tanna)')
        row = data['mothers_property']['value']
        dat('the row mothers_property = %s (%s)' % (row, data['mothers_property']['settings'][row]))
        if row == 'equal':
            return out('the son and the daughter equal in the mother\'s property (R. Zekharya b. HaKatzav — the dayo cap)', ['holding_owed'])
        return out('the son precedes the daughter in the mother\'s property (the first tanna)', ['holding_owed'])
    if ask == 'firstborn_double':
        ink('Deut 21:17', '"to give him a double portion of all that HE has, for he is the first fruits of HIS strength; the right of the firstborn is HIS" (OWED FORWARD to Deuteronomy; cited as ink)')
        move('Bava Batra 111b:1-7', 'not in the mother\'s property — Abaye: "all that HE has"; Rav Nachman b. Yitzchak: "HIS strength"; Rava: "the right of the firstborn is HIS" — for a man, not a woman')
        move('Mishnah Bekhorot 8:9 (CALLED)', 'the family engine\'s held_not_due -> %r: the double in the HELD, not the DUE (48:22 "which I took" against 48:21 "bring you back")' % (HELD_NOT_DUE,))
        prop = case.get('property')
        if prop == 'mothers':
            return out('no double in the mother\'s property', ['exempt'])
        if prop == 'due':
            return out('no double in the due — only in the held', ['exempt'])
        return out('double — in the father\'s property, in the held', ['portion_added'])
    if ask == 'land_status':
        ink('Exod 6:8', '"and I will give it to you as a HERITAGE (morasha)" — the promise\'s word')
        row = data['eretz_yisrael_status']['value']
        dat('the row eretz_yisrael_status = %s (%s)' % (row, data['eretz_yisrael_status']['settings'][row]))
        move('Bava Batra 119a:1, 119a:5, 119b:3-4', 'the daughters took the firstborn\'s portion — the land is HELD before its assignment (Rabba, from Josh 17:5\'s ten parts); '
             'THIS was Moses\' uncertainty: an inheritance from the fathers (held) or the generation bequeaths without inheriting — God: both')
        if row == 'due':
            return out('due — movables only (Shmuel)', ['exempt'])
        return out('held — the firstborn\'s double applies to the land (Rabba)', ['portion_added'])
    if ask == 'apportionment':
        ink('Num 26:53, 26:55', '"unto these the land shall be divided" / "by the names of the tribes of their fathers they shall inherit" — two verses')
        row = data['land_divided_among']['value']
        dat('the row land_divided_among = %s (%s)' % (row, data['land_divided_among']['settings'][row]))
        move('Bava Batra 117a:1-4', 'the Mishnah\'s three portions follow "those who left Egypt" (R. Yoshiyah); R. Yonatan: those who entered — the dead inherit the living; Sifrei 132:1: R. Shimon b. Elazar both')
        return out({'left_egypt': 'those who left Egypt (R. Yoshiyah)', 'entered': 'those who entered the land (R. Yonatan)', 'both': 'both (R. Shimon b. Elazar)'}[row], [FX.NONE])
    if ask == 'excluded':
        ink('Num 27:3', '"he was not among the congregation that gathered against the LORD in Korach\'s congregation" — the plea\'s exclusions')
        move('Bava Batra 118b:5-7', '"the congregation" the spies, "gathered against the LORD" the protesters — Korach\'s two hundred fifty, whose portions Joshua and Caleb took; Sifrei 133:3 the same three')
        return out('no portion — the spies, the protesters (Korach\'s two hundred fifty) and Korach\'s congregation', ['exempt'])
    if ask == 'ten_parts':
        ink('Josh 17:2, 17:5-6', '"and ten parts fell to Manasseh... because the daughters of Manasseh inherited among his sons" — the sixth book\'s run; the houses of 17:2 counted from the ink: %d' % len(HOUSES_17_2))
        move('Bava Batra 118b:8-10', 'six fathers\' houses + the daughters\' portions: the Mishnah\'s three make nine — so an unmentioned paternal uncle who died childless: the tenth (R. Yehuda: the daughters took four)')
        return out('ten — six fathers\' houses, the daughters\' three, and one uncle\'s (%d + 3 + 1)' % len(HOUSES_17_2), ['portion_added'])
    if ask == 'tumtum':
        ink('Num 26:54', '"to a man according to his numbers" — the apportionment excludes women, tumtumim and hermaphrodites (Sifrei 132:1-2)')
        move('Mishnah Bava Batra 9:2', 'sons, daughters and a tumtum: a large estate — the males push him to the females; a small one — the females push him to the males')
        return out('pushed to the females — no inheritance' if case.get('estate') == 'large' else 'pushed to the males — no sustenance', ['exempt'])
    return out('no_case', [FX.NONE])


# ===== F2: THE DAUGHTERS — the case as the tent's fourth (Num 27:1-11, 36:1-12; Josh 17:3-6) ================================
def the_daughters(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'plea':
        ink('Num 27:3-4', '"he had no sons... because he has no son" — the clause doubled; "give us a holding among our father\'s brothers"')
        move('Sifrei Bamidbar 133:4 / Bava Batra 119b:11', 'they were wise and expounded: had there been a son\'s daughter we would not have spoken (Abaye\'s reading of the baraita)')
        return out('no son and no son\'s line — the daughters claim; a son\'s daughter would have barred them', ['holding_owed'])
    if ask == 'counsel':
        ink('Num 27:1', '"and the daughters of Zelophehad drew near" — the feminine verb here and at Josh 17:4 alone (computed)')
        move('Sifrei Bamidbar 133:1', 'they heard the land was apportioned to the tribes and not to females and took counsel: not as the mercies of flesh and blood are the mercies of the Place — His are on all (Ps 145:9)')
        return out('the counsel — the mercies of the Place are on males and females alike', [FX.NONE])
    if ask == 'halt':
        ink('Num 27:5', '"and Moses brought their judgment NEAR before the LORD" — the offerings\' causative verb (eleven Torah seats), "their judgment" once in the Tanakh: no guard (Lev 24:12, Num 15:34), no "stand and I will hear" (9:8)')
        move('Sanhedrin 8a:4', 'R. Chanina: Moses punished for the presumption of "bring to me"; Rav Nachman b. Yitzchak: "I will HEAR it" — if I have learned, I have learned; if not, I go and learn')
        return out('the third form — the judgment carried in by Moses; no body entry on the persons; the docket alone', ['declaration_owed'])
    if ask == 'uncertainty':
        ink('Exod 6:8', '"as a HERITAGE" — the word the scope was read from')
        move('Sifrei Bamidbar 133:4 / Bava Batra 119a:6, 119b:3-4', 'R. Chidka from Shimon HaShikmoni: Moses KNEW that daughters inherit; the question was whether they inherit the FIT as the HELD — '
             'the land not yet possessed; resolved BOTH: an inheritance from the fathers, and the generation bequeaths without inheriting')
        return out('the scope — the fit against the held (not whether, not the mode, not how)', [FX.NONE])
    if ask == 'levirate_dilemma':
        ink('Deut 25:5 / Num 27:8', '"and he has no son" at %s alone in the Torah — the family engine\'s census CALLED: one clause opens two institutions' % (NO_SON_SEATS,))
        move('Bava Batra 119b:10', 'Moses was expounding the levirate; the daughters: if we are as a son, give us an inheritance as a son; if not, let our mother enter levirate marriage — at once "Moses brought their judgment near"')
        move('Mishnah Yevamot 2:5 / Yevamot 22b:6', 'a CHILD of any kind exempts the father\'s wife — "no son": look into him, any child at all; the bond needs brothers together (the sanctions engine CALLED: not_in_world -> %r)' % (BOND_NOT_IN_WORLD,))
        return out('both horns from one clause: as offspring they inherit (27:8), and as offspring they exempt their mother (Deut 25:5) — no bond', ['holding_owed', 'exempt'])
    if ask == 'child_of_any_kind':
        ink('Deut 25:5', '"and he has no son" — the levirate\'s condition (OWED FORWARD; cited as ink)')
        ch = case.get('children', {})
        if ch.get('daughters') or ch.get('sons'):
            move('Mishnah Yevamot 2:5; Yevamot 22b:6', 'anyone who has a child of any kind — that child exempts his father\'s wife: "no son" read "look into him"')
            return out('exempt — a child of any kind (a daughter too) exempts the mother', ['exempt'])
        move('Deut 25:5 (the sanctions engine CALLED)', 'no child: the bond forms when brothers dwell together — not_in_world -> %r' % (BOND_NOT_IN_WORLD,))
        return out('bound — no child, a brother in the world', ['levirate_owed'])
    if ask == 'three_portions':
        ink('Num 27:7', '"given shall be GIVEN to them a holding of inheritance AMONG THEIR FATHER\'S BROTHERS, and you shall PASS OVER the inheritance of their father to them" — three clauses')
        move('Sifrei Bamidbar 134:1 / Bava Batra 118b:11 / Mishnah Bava Batra 8:3', 'their father\'s share; Hepher\'s share among the brothers; the firstborn\'s double — THREE; R. Eliezer b. Yaakov: also an uncle\'s, from the doubled "given" (118b:12)')
        return out(3, ['portion_added'])
    if ask == 'section_on_high':
        ink('Num 27:7', '"RIGHTLY do the daughters of Zelophehad speak"')
        move('Sifrei Bamidbar 134:1', 'they claimed well — for so is this section WRITTEN BEFORE ME ON HIGH; happy the man whose words the Place acknowledges (likewise 36:5, 14:20)')
        return out('the rule pre-exists the case — the output reads a standing text', [FX.NONE])
    if ask == 'output_frames':
        ink('Lev 24:13; Num 9:9, 15:35, 27:6, 36:5', 'the five outputs\' frames computed: %s' % (FRAMES,))
        return out(FRAMES, [FX.NONE])
    if ask == 'tribes_plea':
        ink('Num 36:3-4', '"their inheritance shall be diminished... and if the JUBILEE be, it shall be added to the tribe into which they marry" — the release reached in the argument (the word\'s ninth Torah seat)')
        move('Mishnah Bekhorot 8:10 (CALLED)', 'the family engine\'s gift_returns_dispute -> %r: these do not return in the jubilee — the firstborn\'s portion, the WIFE\'S INHERITOR, the levir\'s; a gift (R. Meir; the sages as a sale): the tribes were RIGHT — the release would not bring it back' % (JUBILEE_RETURNS,))
        return out('the diminution is real — the wife\'s inheritor keeps it through the jubilee (Bekhorot 8:10)', ['marries_within_tribe'])
    if ask == 'second_output':
        ink('Num 36:5-6', '"and Moses COMMANDED the children of Israel BY THE MOUTH OF THE LORD, saying: rightly the tribe of the sons of Joseph speak; this is the thing... to whom is good in their eyes they shall be wives, ONLY to the family of the tribe of their father" — no divine frame (computed)')
        row = data['daughters_marriage']['value']
        dat('the row daughters_marriage = %s (%s)' % (row, data['daughters_marriage']['settings'][row]))
        move('Bava Batra 120a:6-9', 'Shmuel: the daughters permitted any tribe, the limit good advice; the baraita: the generation commanded — Rabba: everyone except the daughters')
        if row == 'commanded':
            return out('the daughters commanded to their father\'s tribe with the generation', ['marries_within_tribe'])
        return out('the daughters permitted any tribe; their father\'s tribe advised (Shmuel)', ['exempt'])
    if ask == 'reach':
        ink('Num 36:6', '"THIS is the thing that the LORD commanded" — the formula at eight Torah seats (computed)')
        row = data['tribe_transfer_reach']['value']
        dat('the row tribe_transfer_reach = %s (%s)' % (row, data['tribe_transfer_reach']['settings'][row]))
        move('Bava Batra 120a:10, 120b:2', 'Rava: this thing is practiced in THIS GENERATION alone; the silence test — had it been for all generations the verse would be silent (the outside-slaughter\'s "throughout their generations" the contrast)')
        if row == 'all_generations':
            return out('for all generations (refused at 120b:2)', ['marries_within_tribe'])
        return out('this generation — the one that divided the land', ['marries_within_tribe'])
    if ask == 'lapse':
        ink('Num 36:6', '"this is the thing" — the reach\'s formula')
        move('Bava Batra 121a:6-7 / Mishnah Taanit 4:8', 'the fifteenth of Av — the day the tribes were PERMITTED to intermarry: the sages of that time expounded "this is the thing" and lifted the rule (Rav Yehuda in Shmuel\'s name)')
        return out('lapsed on the fifteenth of Av — a rule installed by the tent with a generation\'s reach, closed by a later court\'s reading', ['exempt'])
    if ask == 'execution':
        ink('Num 36:10-12', '"as the LORD commanded Moses, so did the daughters" — the report clause (computed: Lev 24:23, Num 15:36); "wives to the sons of their uncles"; "their inheritance remained on the tribe"')
        move('Bava Batra 119b:12-13', 'righteous — they married those fit for them; R. Eliezer b. Yaakov: not under forty; the miracle as Jochebed\'s')
        return out('married the sons of their uncles; the inheritance remained on the tribe of their father', ['wife_taken', 'inheritance_stayed_in_tribe'])
    if ask == 'the_run':
        ink('Josh 17:3-6', '"and they drew near before Eleazar the priest and before Joshua... and he GAVE them, by the mouth of the LORD, an inheritance among their father\'s brothers" — the feminine verb\'s second seat; ten parts')
        move('Bava Batra 118b:8-119a:1', 'the ten parts count the daughters\' portions — they took the firstborn\'s: the land held')
        return out('given in the sixth book by the mouth of the LORD — the holding owed at 27:7 closed off the Torah (the readback\'s item)', ['holding_owed'])
    if ask == 'names_order':
        ink('Num 26:33, 27:1, 36:11; Josh 17:3', 'two orders computed — Tirzah second and Noah last at 36:11 alone')
        row = data['names_order']['value']
        dat('the row names_order = %s (%s)' % (row, data['names_order']['settings'][row]))
        return out('by wisdom at 27:1, by age at 36:11 (R. Ami)' if row == 'wisdom_then_age' else 'all equal (the school of R. Yishmael)', [FX.NONE])
    if ask == 'identity':
        ink('Num 27:3', '"our father died in the wilderness" — "wilderness" here and at 15:32')
        move('Sifrei Bamidbar 133:3 / 113:1', 'R. Akiva: the gatherer is Zelophehad, by the verbal analogy; R. Yehuda b. Beteira rebukes the naming — UNASSIGNED at both entries')
        return out('unassigned: Zelophehad the wood-gatherer (R. Akiva) against the concealment (R. Yehuda b. Beteira)', [FX.NONE])
    if ask == 'name_is_inheritance':
        ink('Num 27:4 / Deut 25:6', '"why should the NAME of our father be withheld" — "shall rise on the NAME of his brother"')
        move('Sifrei Bamidbar 133:4 (R. Yehuda) / Yevamot 24a (CALLED)', 'name here / name there — inheritance and seed; the family engine\'s name_is_inheritance -> %r (48:6\'s "after the name of their brothers in their inheritance")' % (NAME_IS_INHERITANCE,))
        return out('the plea\'s "name" is inheritance — the levirate\'s word (Deut 25:6) read from 48:6', [FX.NONE])
    if ask == 'the_case':
        ink('Num 27:1-11; 36:1-12', 'the plea, the judgment brought near, the statute with the verdict inside it; the tribes\' plea, the relayed command; the marriage')
        return out('drew near and stood, the judgment brought near, rightly — a holding among their father\'s brothers and the ladder for the generations; the tribes: rightly — within the tribe, this generation; married their uncles\' sons, the inheritance remained; the giving in Joshua', ['holding_owed', 'declaration_owed', 'marries_within_tribe', 'wife_taken', 'inheritance_stayed_in_tribe'])
    return out('no_case', [FX.NONE])


# ===== THE WRAP (motion 6): the daemon on the world engine =====================================================
def law_zelophehad(event, world):
    """THE FOURTH CASE-BORN LAW (given_at Num 27:1, installed_by statute_declared — the daughters' output; its tribe-transfer cell
    installed by the relayed command at 36:5-9). A branch per registered kind; the cells above are the verdicts; every effect registry-validated."""
    k = event['kind']
    if k == 'daughters_approached':
        persons = event.get('persons') or [event['subject']]
        key, name = heir_of({'daughter': True, 'son': not event.get('no_son', True), 'sons_line': not event.get('no_sons_line', True), 'brothers': True})
        if key != 'daughter':
            return []
        return [{'effect': 'holding_owed', 'subject': p, 'counterparty': 'the-court', 'amount': None, 'due': None, 'value': name,
                 'source_law': 'law_zelophehad — the ladder at the plea [INK Num 27:4 give us a holding; Num 27:8 no son — to his daughter; Mishnah Bava Batra 8:2; '
                 'the court that owes the giving: Num 34:17 Eleazar and Joshua; the giving Josh 17:4 — OPEN until then]', 'case_source': event['case_source']} for p in persons]
    if k == 'estate_claimed':
        v, fx, _ = inheritance_order({'ask': 'ladder', 'survivors': event.get('survivors', {}), 'claimant_degree': event.get('claimant_degree')}, DATA)
        if 'holding_owed' in fx:
            return [{'effect': 'holding_owed', 'subject': event.get('claimant', event['subject']), 'counterparty': 'the-court', 'amount': None, 'due': None, 'value': v,
                     'source_law': 'law_zelophehad — the ladder [Num 27:8-11; Mishnah Bava Batra 8:2; Bava Batra 108b:3]', 'case_source': event['case_source']}]
        return [{'effect': 'exempt', 'subject': event.get('claimant', event['subject']), 'counterparty': None, 'amount': None, 'due': None, 'value': v,
                 'source_law': 'law_zelophehad — the ladder: another degree precedes [Mishnah Bava Batra 8:2; 115b:2 the Sadducees refused]', 'case_source': event['case_source']}]
    if k == 'estate_divided':
        if event.get('firstborn'):
            v, fx, _ = inheritance_order({'ask': 'firstborn_double', 'property': event.get('property', 'fathers')}, DATA)
            if 'portion_added' in fx:
                return [{'effect': 'portion_added', 'subject': event.get('firstborn'), 'counterparty': None, 'amount': None, 'due': None, 'value': v,
                         'source_law': 'law_zelophehad — the firstborn\'s double [Deut 21:17; Mishnah Bava Batra 8:4; Bekhorot 8:9 by CALL; Bava Batra 111b:7]', 'case_source': event['case_source']}]
            return [{'effect': 'exempt', 'subject': event.get('firstborn'), 'counterparty': None, 'amount': None, 'due': None, 'value': v,
                     'source_law': 'law_zelophehad — no double here [the mother\'s property, the due — Bava Batra 111b:7; Bekhorot 8:9]', 'case_source': event['case_source']}]
        return [{'effect': 'exempt', 'subject': event['subject'], 'counterparty': None, 'amount': None, 'due': None, 'value': 'no firstborn — equal shares',
                 'source_law': 'law_zelophehad — the shares [Mishnah Bava Batra 8:4]', 'case_source': event['case_source']}]
    if k == 'tribes_approached':
        persons = event.get('against') or []
        return [{'effect': 'marries_within_tribe', 'subject': p, 'counterparty': None, 'amount': None, 'due': None,
                 'value': 'the tribe of their father — the bar in force; the daughters permitted, advised (Shmuel)',
                 'source_law': 'law_zelophehad — the tribe-transfer bar at the tribes\' plea [INK Num 36:6-9; Bava Batra 120a:6-10; Bekhorot 8:10 by CALL: the jubilee returns it not]',
                 'case_source': event['case_source']} for p in persons]
    if k == 'inheritance_crossed_tribes':
        if event.get('daughters_of_zelophehad') and DATA['daughters_marriage']['value'] == 'permitted_advised':
            return [{'effect': 'exempt', 'subject': event.get('heiress', event['subject']), 'counterparty': None, 'amount': None, 'due': None, 'value': 'permitted any tribe (Shmuel)',
                     'source_law': 'law_zelophehad — the daughters excepted [Bava Batra 120a:6, 120a:9]', 'case_source': event['case_source']}]
        if event.get('generation') != 'first' and DATA['tribe_transfer_reach']['value'] == 'this_generation':
            return [{'effect': 'exempt', 'subject': event.get('heiress', event['subject']), 'counterparty': None, 'amount': None, 'due': None, 'value': 'lapsed — this generation alone (the fifteenth of Av)',
                     'source_law': 'law_zelophehad — the reach [Num 36:6 this is the thing; Bava Batra 120a:10, 121a:7]', 'case_source': event['case_source']}]
        return [{'effect': 'marries_within_tribe', 'subject': event.get('heiress', event['subject']), 'counterparty': None, 'amount': None, 'due': None, 'value': 'the tribe of her father',
                 'source_law': 'law_zelophehad — the bar [INK Num 36:7-9; Bava Batra 120a:8]', 'case_source': event['case_source']}]
    if k == 'daughters_married':
        persons = event.get('persons') or [event['subject']]
        out_ = []
        for p in persons:
            out_.append({'effect': 'wife_taken', 'subject': p, 'counterparty': None, 'amount': None, 'due': None, 'value': event.get('husbands', 'sons_of_their_uncles'),
                         'source_law': 'law_zelophehad — the execution as a marriage [INK Num 36:11: wives to the sons of their uncles; Onkelos: their father\'s brothers]', 'case_source': event['case_source']})
            out_.append({'effect': 'inheritance_stayed_in_tribe', 'subject': p, 'counterparty': None, 'amount': None, 'due': None, 'value': event.get('tribe', 'manasseh'),
                         'source_law': 'law_zelophehad — the ledger\'s close in the ink [INK Num 36:12: their inheritance remained on the tribe of the family of their father]', 'case_source': event['case_source']})
        return out_
    if k == 'levirate_claimed':
        v, fx, _ = the_daughters({'ask': 'child_of_any_kind', 'children': event.get('children', {})}, DATA)
        widow = event.get('widow', event['subject'])
        if 'exempt' in fx:
            return [{'effect': 'exempt', 'subject': widow, 'counterparty': None, 'amount': None, 'due': None, 'value': 'child_of_any_kind',
                     'source_law': 'law_zelophehad — the dilemma\'s second horn [Deut 25:5 and he has no son; Mishnah Yevamot 2:5; Yevamot 22b:6; Bava Batra 119b:10]', 'case_source': event['case_source']}]
        if event.get('brothers_in_world'):
            return [{'effect': 'levirate_owed', 'subject': event.get('levir', widow), 'counterparty': widow, 'amount': None, 'due': None, 'value': 'no child',
                     'source_law': 'law_zelophehad — the bond [Deut 25:5; the sanctions engine\'s not_in_world by CALL]', 'case_source': event['case_source']}]
        return [{'effect': 'exempt', 'subject': widow, 'counterparty': None, 'amount': None, 'due': None, 'value': 'no brother in the world',
                 'source_law': 'law_zelophehad — no bond [Deut 25:5 when brothers dwell together; the sanctions engine by CALL]', 'case_source': event['case_source']}]
    return []


def scene():
    """THE WRAP's scene: the exam's rows replayed on a bench world under law_zelophehad alone — the effect count per submit, typed from the design"""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='the inheritance order on the bench (clock unit: days)')
        w.laws = [law_zelophehad]
        w.advance(1)
        counts = (   # LITERAL submits — the daemon gate's submit parser reads literal calls only (W7's lesson)
            w.submit({'kind': 'estate_claimed', 'subject': 'a-daughter', 'claimant': 'a-daughter', 'claimant_degree': 'daughter', 'survivors': {'daughter': True, 'brothers': True}, 'case_source': 'Num 27:8 — the daughter before the brothers (Mishnah Bava Batra 8:2)'}),
            w.submit({'kind': 'estate_claimed', 'subject': 'a-daughter', 'claimant': 'a-daughter', 'claimant_degree': 'daughter', 'survivors': {'son': True, 'daughter': True}, 'case_source': 'Num 27:8 — the son before the daughter (Mishnah Bava Batra 8:2)'}),
            w.submit({'kind': 'estate_claimed', 'subject': 'a-daughter', 'claimant': 'a-daughter', 'claimant_degree': 'daughter', 'survivors': {'daughter': True, 'sons_line': True}, 'case_source': 'Num 27:8 — the son\'s daughter before the daughter (Bava Batra 115b:2, the Sadducees refused)'}),
            w.submit({'kind': 'estate_divided', 'subject': 'the-heirs', 'firstborn': 'the-firstborn', 'property': 'fathers', 'case_source': 'Deut 21:17 — the double in the father\'s held (Mishnah Bava Batra 8:4)'}),
            w.submit({'kind': 'estate_divided', 'subject': 'the-heirs', 'firstborn': 'the-firstborn', 'property': 'mothers', 'case_source': 'Deut 21:17 — no double in the mother\'s (Bava Batra 111b:7)'}),
            w.submit({'kind': 'inheritance_crossed_tribes', 'subject': 'an-heiress', 'heiress': 'an-heiress', 'generation': 'first', 'case_source': 'Num 36:8 — the first generation barred (Bava Batra 120a:8)'}),
            w.submit({'kind': 'inheritance_crossed_tribes', 'subject': 'an-heiress', 'heiress': 'an-heiress', 'generation': 'later', 'case_source': 'Num 36:6 — this is the thing: lapsed (Bava Batra 120a:10, 121a:7)'}),
            w.submit({'kind': 'levirate_claimed', 'subject': 'a-widow', 'widow': 'a-widow', 'children': {'daughters': 1, 'sons': 0}, 'brothers_in_world': True, 'case_source': 'Deut 25:5 — a child of any kind exempts (Mishnah Yevamot 2:5)'}),
            w.submit({'kind': 'levirate_claimed', 'subject': 'a-widow', 'widow': 'a-widow', 'levir': 'the-levir', 'children': {}, 'brothers_in_world': True, 'case_source': 'Deut 25:5 — no child: the bond'}),
        )
    return counts, w


SCENE, _W = scene()
SCENE_PREDICTED = (1, 1, 1, 1, 1, 1, 1, 1, 1)   # THE_TENT.md section 4: one effect per row — holding_owed, exempt, exempt (the Sadducees), portion_added, exempt, marries_within_tribe, exempt (lapsed), exempt (a child), levirate_owed
assert SCENE == SCENE_PREDICTED, ('THE TENT: the daughters\' scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE TENT sitting 4 (2026-09-09; THE_TENT.md section 4): the chapter's own case AS HISTORY — the six lines of Num 27:1-11 and 36:1-12 in
    the text's order on a world with the library's tent daemon registered first and this runner's daemon second; recorded by the sequential
    run's recorder and stitched onto the tape (the marker at 27:1 is the tape's, reading-placed — not the scene's). Not a graded cell: the
    tuple below is a tripwire typed from THE_TENT.md's design; the sequence world's RUN tuple grades the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 27:1-11 + 36:1-12: the daughters of Zelophehad on the tape — the plea, the judgment brought near, the statute; the tribes, the relayed command, the marriage (clock unit: days)')
        w.laws = [WE.law_tent, law_zelophehad]
        w.advance(1)
        d = 'the-daughters-of-zelophehad'; g = 'the-heads-of-gilead'
        w.submit({'kind': 'daughters_approached', 'subject': d, 'persons': [d], 'decedent': 'zelophehad', 'no_son': True, 'no_sons_line': True, 'ground': 'name_withheld', 'case_source': 'Num 27:1-4 — and the daughters of Zelophehad drew near... and they stood before Moses and before Eleazar the priest and before the princes and all the congregation at the door of the tent of meeting, saying: our father died in the wilderness... in his own sin he died, and he had no sons; why should the name of our father be withheld from his family because he has no son? give us a holding among our father\'s brothers'})
        w.submit({'kind': 'judgment_brought_near', 'subject': d, 'persons': [d], 'case_of': 'Num 27:1', 'uncertainty': 'the_scope', 'brought_by': 'moses', 'case_source': 'Num 27:5 — and Moses brought their judgment near before the LORD (Sifrei Bamidbar 133:4 / Bava Batra 119a:6: Moses knew daughters inherit — the fit against the held; Sanhedrin 8a:4: I will hear it)'})
        w.submit({'kind': 'statute_declared', 'subject': d, 'persons': [d], 'installs': 'law_zelophehad', 'verdict': 'holding_owed', 'case_source': 'Num 27:6-11 — and the LORD said to Moses, saying: rightly do the daughters of Zelophehad speak; given shall be given to them a holding of inheritance among their father\'s brothers, and you shall pass over the inheritance of their father to them; and to the children of Israel speak, saying: if a man dies and has no son, you shall pass his inheritance to his daughter... and it shall be to the children of Israel a statute of judgment'})
        w.submit({'kind': 'tribes_approached', 'subject': g, 'persons': [g], 'against': [d], 'ground': 'tribal_diminution', 'jubilee_raised': True, 'first_output_cited': True, 'case_source': 'Num 36:1-4 — and the heads of the fathers of the family of the sons of Gilead drew near and spoke before Moses and before the princes: the LORD commanded my lord to give the land by lot... and my lord was commanded by the LORD to give the inheritance of Zelophehad our brother to his daughters; if they become wives to one of the sons of the tribes their inheritance shall be diminished... and if the jubilee be, it shall be added'})
        w.submit({'kind': 'command_relayed', 'subject': d, 'persons': [d], 'installs': 'law_zelophehad:tribe_transfer', 'verdict': 'marries_within_tribe', 'permission': 'good_in_their_eyes', 'limit': 'fathers_tribe', 'reach': 'this_generation', 'case_source': 'Num 36:5-9 — and Moses commanded the children of Israel by the mouth of the LORD, saying: rightly the tribe of the sons of Joseph speak; this is the thing that the LORD commanded concerning the daughters of Zelophehad: to whom is good in their eyes they shall be wives, only to the family of the tribe of their father; and an inheritance shall not go around from tribe to tribe'})
        w.submit({'kind': 'daughters_married', 'subject': d, 'persons': [d], 'husbands': 'sons_of_their_uncles', 'tribe': 'manasseh', 'case_source': 'Num 36:11-12 — and Mahlah, Tirzah, Hoglah, Milcah and Noah the daughters of Zelophehad were wives to the sons of their uncles; of the families of the sons of Manasseh son of Joseph they were wives, and their inheritance remained on the tribe of the family of their father (36:10: as the LORD commanded Moses, so did the daughters)'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: [e.get('open') for e in w.entity(eid).ledger if e['effect'] == eff]
    owed = [e for e in w.entity('the-court').ledger if e['effect'] == 'declaration_owed']
    rule = [e for e in w.entity('the-tabernacle').ledger if e['effect'] == 'rule_installed']
    d = 'the-daughters-of-zelophehad'
    return (n(d, 'holding_owed'), is_open(d, 'holding_owed'), len(owed), owed[0].get('open') if owed else None, (owed[0].get('covered_by') or None) if owed else None,
            len(rule), [r.get('value') for r in rule], n(d, 'marries_within_tribe'), n(d, 'wife_taken'), n(d, 'inheritance_stayed_in_tribe')), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (1, [True], 1, False, ['law_zelophehad'], 2, ['law_zelophehad', 'law_zelophehad:tribe_transfer'], 1, 1, 1)   # THE_TENT.md section 4: the holding owed at the plea (OPEN — the giving is Josh 17:4); the docket owed at the third-form halt and closed by the statute, covered by law_zelophehad; two rules installed (the daemon; the cell); the bar at the tribes' plea; the marriage and the remaining
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE TENT: the daughters narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the Mishnah's rows (num_27_inheritance_exam_2026-09-09.md) and the Talmud's per gap.
# =====================================================================
D_EQUAL = dict(DATA, mothers_property=dict(DATA['mothers_property'], value='equal'))
D_DUE = dict(DATA, eretz_yisrael_status=dict(DATA['eretz_yisrael_status'], value='due'))
D_ENTERED = dict(DATA, land_divided_among=dict(DATA['land_divided_among'], value='entered'))
D_BOTH = dict(DATA, land_divided_among=dict(DATA['land_divided_among'], value='both'))
D_COMMANDED = dict(DATA, daughters_marriage=dict(DATA['daughters_marriage'], value='commanded'))
D_ALLGEN = dict(DATA, tribe_transfer_reach=dict(DATA['tribe_transfer_reach'], value='all_generations'))
D_EQUALNAMES = dict(DATA, names_order=dict(DATA['names_order'], value='equal'))
CASES = [
    # F1 — the ladder (Mishnah Bava Batra 8:2)
    ('Mishnah Bava Batra 8:2 — a son and a daughter: the son',
     lambda: inheritance_order({'ask': 'ladder', 'survivors': {'son': True, 'daughter': True}, 'claimant_degree': 'daughter'}, DATA), 'the son'),
    ('Mishnah Bava Batra 8:2 — the son\'s line and a daughter',
     lambda: inheritance_order({'ask': 'ladder', 'survivors': {'sons_line': True, 'daughter': True}, 'claimant_degree': 'sons_line'}, DATA), "the son's line"),
    ('Mishnah Bava Batra 8:2 / Num 27:8 — a daughter and brothers: the daughter',
     lambda: inheritance_order({'ask': 'ladder', 'survivors': {'daughter': True, 'brothers': True}, 'claimant_degree': 'daughter'}, DATA), 'the daughter'),
    ('Mishnah Bava Batra 8:2 — the daughter\'s line and brothers',
     lambda: inheritance_order({'ask': 'ladder', 'survivors': {'daughters_line': True, 'brothers': True}, 'claimant_degree': 'daughters_line'}, DATA), "the daughter's line"),
    ('Mishnah Bava Batra 8:2 / Num 27:9 — brothers and uncles: the brothers',
     lambda: inheritance_order({'ask': 'ladder', 'survivors': {'brothers': True, 'fathers_brothers': True}, 'claimant_degree': 'brothers'}, DATA), 'the brothers'),
    ('Mishnah Bava Batra 8:2 — the brothers\' line and uncles',
     lambda: inheritance_order({'ask': 'ladder', 'survivors': {'brothers_line': True, 'fathers_brothers': True}, 'claimant_degree': 'brothers_line'}, DATA), "the brothers' line"),
    ('Bava Batra 108b:3 — the father and the brothers: the father ("his flesh")',
     lambda: inheritance_order({'ask': 'ladder', 'survivors': {'father': True, 'brothers': True}, 'claimant_degree': 'father'}, DATA), 'the father'),
    ('Bava Batra 108b:3 — the father and a son: the son ("the near")',
     lambda: inheritance_order({'ask': 'ladder', 'survivors': {'father': True, 'son': True}, 'claimant_degree': 'son'}, DATA), 'the son'),
    ('Bava Batra 109a:2 — the father and a daughter: the daughter (the offspring before the father)',
     lambda: inheritance_order({'ask': 'ladder', 'survivors': {'father': True, 'daughter': True}, 'claimant_degree': 'daughter'}, DATA), 'the daughter'),
    ('Num 27:11 — the father\'s brothers when no brothers',
     lambda: inheritance_order({'ask': 'ladder', 'survivors': {'fathers_brothers': True}, 'claimant_degree': 'fathers_brothers'}, DATA), "the father's brothers"),
    ('Bava Batra 115b:1 — no heir found: the line climbed to Reuben',
     lambda: inheritance_order({'ask': 'ladder', 'survivors': {}}, DATA), 'the nearest of flesh — the line climbed to Reuben son of Jacob'),
    ('Bava Batra 115b:2 — the daughter WITH the son\'s daughter: the Sadducees\' act, refused',
     lambda: inheritance_order({'ask': 'ladder', 'survivors': {'daughter': True, 'sons_line': True}, 'claimant_degree': 'daughter'}, DATA), "the son's line — not the daughter with her (the Sadducees' act, refused)"),
    ('Bava Batra 108b:3-4 — the nearness key',
     lambda: inheritance_order({'ask': 'nearness_key'}, DATA), 'the nearer the earlier — the son before the father, the father before the brothers'),
    ('Bava Batra 110b:3-4 — the source of the rule: the output, not the plea',
     lambda: inheritance_order({'ask': 'source_of_rule'}, DATA), 'from the output (27:8), not the plea (27:4)'),
    # F1 — the husband, the mother's property, the firstborn
    ('Mishnah Bava Batra 8:1 / Bava Batra 111b:8 — the husband inherits the wife',
     lambda: inheritance_order({'ask': 'husband'}, DATA), 'the husband inherits the wife; she does not inherit him'),
    ('Mishnah Bava Batra 8:1 — the wife does not inherit the husband',
     lambda: inheritance_order({'ask': 'husband', 'claimant': 'wife'}, DATA), 'the wife does not inherit her husband'),
    ('Bava Batra 111a:2 — the mother\'s property: the son first (the first tanna, the running setting)',
     lambda: inheritance_order({'ask': 'mothers_property'}, DATA), 'the son precedes the daughter in the mother\'s property (the first tanna)'),
    ('Bava Batra 111a:3 — R. Zekharya b. HaKatzav: equal (the row\'s other setting)',
     lambda: inheritance_order({'ask': 'mothers_property'}, D_EQUAL), 'the son and the daughter equal in the mother\'s property (R. Zekharya b. HaKatzav — the dayo cap)'),
    ('Mishnah Bava Batra 8:4 / Deut 21:17 — the firstborn\'s double in the father\'s',
     lambda: inheritance_order({'ask': 'firstborn_double', 'property': 'fathers'}, DATA), 'double — in the father\'s property, in the held'),
    ('Mishnah Bava Batra 8:4 / Bava Batra 111b:7 — no double in the mother\'s',
     lambda: inheritance_order({'ask': 'firstborn_double', 'property': 'mothers'}, DATA), 'no double in the mother\'s property'),
    ('Mishnah Bekhorot 8:9 (the family engine called) — no double in the due',
     lambda: inheritance_order({'ask': 'firstborn_double', 'property': 'due'}, DATA), 'no double in the due — only in the held'),
    ('Bava Batra 119a:5 — the land held before its assignment (Rabba, the running setting)',
     lambda: inheritance_order({'ask': 'land_status'}, DATA), 'held — the firstborn\'s double applies to the land (Rabba)'),
    ('Bava Batra 119a:4 — Shmuel: movables only (the row\'s other setting)',
     lambda: inheritance_order({'ask': 'land_status'}, D_DUE), 'due — movables only (Shmuel)'),
    # F1 — the apportionment
    ('Bava Batra 117a:2 / Sifrei 132:1 — those who left Egypt (R. Yoshiyah, the running setting)',
     lambda: inheritance_order({'ask': 'apportionment'}, DATA), 'those who left Egypt (R. Yoshiyah)'),
    ('Bava Batra 117a:3 — those who entered (R. Yonatan)',
     lambda: inheritance_order({'ask': 'apportionment'}, D_ENTERED), 'those who entered the land (R. Yonatan)'),
    ('Sifrei Bamidbar 132:1 — both (R. Shimon b. Elazar)',
     lambda: inheritance_order({'ask': 'apportionment'}, D_BOTH), 'both (R. Shimon b. Elazar)'),
    ('Bava Batra 118b:5-7 — the excluded: the spies, the protesters, Korach\'s',
     lambda: inheritance_order({'ask': 'excluded', 'person': 'spies'}, DATA), 'no portion — the spies, the protesters (Korach\'s two hundred fifty) and Korach\'s congregation'),
    ('Bava Batra 118b:8-10 / Josh 17:5 — the ten parts (the houses counted from the ink)',
     lambda: inheritance_order({'ask': 'ten_parts'}, DATA), 'ten — six fathers\' houses, the daughters\' three, and one uncle\'s (6 + 3 + 1)'),
    ('Mishnah Bava Batra 9:2 — the tumtum, a large estate',
     lambda: inheritance_order({'ask': 'tumtum', 'estate': 'large'}, DATA), 'pushed to the females — no inheritance'),
    ('Mishnah Bava Batra 9:2 — the tumtum, a small estate',
     lambda: inheritance_order({'ask': 'tumtum', 'estate': 'small'}, DATA), 'pushed to the males — no sustenance'),
    # F2 — the daughters
    ('Sifrei Bamidbar 133:4 / Bava Batra 119b:11 — the plea: no son, no son\'s line',
     lambda: the_daughters({'ask': 'plea'}, DATA), 'no son and no son\'s line — the daughters claim; a son\'s daughter would have barred them'),
    ('Sifrei Bamidbar 133:1 — the counsel',
     lambda: the_daughters({'ask': 'counsel'}, DATA), 'the counsel — the mercies of the Place are on males and females alike'),
    ('Num 27:5 / Sanhedrin 8a:4 — the halt\'s third form',
     lambda: the_daughters({'ask': 'halt'}, DATA), 'the third form — the judgment carried in by Moses; no body entry on the persons; the docket alone'),
    ('Sifrei Bamidbar 133:4 / Bava Batra 119b:3-4 — the fourth uncertainty: the scope',
     lambda: the_daughters({'ask': 'uncertainty'}, DATA), 'the scope — the fit against the held (not whether, not the mode, not how)'),
    ('Bava Batra 119b:10 — THE LEVIRATE DILEMMA: both horns from one clause (the family and sanctions engines called)',
     lambda: the_daughters({'ask': 'levirate_dilemma'}, DATA), 'both horns from one clause: as offspring they inherit (27:8), and as offspring they exempt their mother (Deut 25:5) — no bond'),
    ('Mishnah Yevamot 2:5 / Yevamot 22b:6 — a child of any kind exempts the mother',
     lambda: the_daughters({'ask': 'child_of_any_kind', 'children': {'daughters': 5, 'sons': 0}}, DATA), 'exempt — a child of any kind (a daughter too) exempts the mother'),
    ('Deut 25:5 — no child: the bond (the sanctions engine called)',
     lambda: the_daughters({'ask': 'child_of_any_kind', 'children': {}}, DATA), 'bound — no child, a brother in the world'),
    ('Mishnah Bava Batra 8:3 / Sifrei 134:1 / Bava Batra 118b:11 — the three portions',
     lambda: the_daughters({'ask': 'three_portions'}, DATA), 3),
    ('Sifrei Bamidbar 134:1 — the section written before Me on high',
     lambda: the_daughters({'ask': 'section_on_high'}, DATA), 'the rule pre-exists the case — the output reads a standing text'),
    ('the five outputs\' frames — computed from the ink (Lev 24:13, Num 9:9, 15:35, 27:6, 36:5)',
     lambda: the_daughters({'ask': 'output_frames'}, DATA), {'Lev 24:13': ('וידבר יהוה', True), 'Num 9:9': ('וידבר יהוה', True), 'Num 15:35': ('ויאמר יהוה', False), 'Num 27:6': ('ויאמר יהוה', True), 'Num 36:5': ('ויצו משה', True)}),
    ('Num 36:3-4 / Mishnah Bekhorot 8:10 (the family engine called) — the tribes\' jubilee argument',
     lambda: the_daughters({'ask': 'tribes_plea'}, DATA), 'the diminution is real — the wife\'s inheritor keeps it through the jubilee (Bekhorot 8:10)'),
    ('Bava Batra 120a:6 — Shmuel: the daughters permitted, advised (the running setting)',
     lambda: the_daughters({'ask': 'second_output'}, DATA), 'the daughters permitted any tribe; their father\'s tribe advised (Shmuel)'),
    ('Bava Batra 120a:8 — the generation commanded, the daughters with it (the row\'s other setting)',
     lambda: the_daughters({'ask': 'second_output'}, D_COMMANDED), 'the daughters commanded to their father\'s tribe with the generation'),
    ('Bava Batra 120a:10, 120b:2 — the reach: this generation (Rava, the running setting)',
     lambda: the_daughters({'ask': 'reach'}, DATA), 'this generation — the one that divided the land'),
    ('Bava Batra 120a:11 / 120b:2 — for all generations (refused; the row\'s other setting)',
     lambda: the_daughters({'ask': 'reach'}, D_ALLGEN), 'for all generations (refused at 120b:2)'),
    ('Bava Batra 121a:7 / Mishnah Taanit 4:8 — the lapse on the fifteenth of Av',
     lambda: the_daughters({'ask': 'lapse'}, DATA), 'lapsed on the fifteenth of Av — a rule installed by the tent with a generation\'s reach, closed by a later court\'s reading'),
    ('Num 36:10-12 / Bava Batra 119b:12 — the execution as a marriage',
     lambda: the_daughters({'ask': 'execution'}, DATA), 'married the sons of their uncles; the inheritance remained on the tribe of their father'),
    ('Josh 17:3-6 — the run in the sixth book',
     lambda: the_daughters({'ask': 'the_run'}, DATA), 'given in the sixth book by the mouth of the LORD — the holding owed at 27:7 closed off the Torah (the readback\'s item)'),
    ('Bava Batra 120a:4 — the names\' two orders (R. Ami, the running setting)',
     lambda: the_daughters({'ask': 'names_order'}, DATA), 'by wisdom at 27:1, by age at 36:11 (R. Ami)'),
    ('Bava Batra 120a:5 / Sifrei 133:2 — all equal (the row\'s other setting)',
     lambda: the_daughters({'ask': 'names_order'}, D_EQUALNAMES), 'all equal (the school of R. Yishmael)'),
    ('Sifrei Bamidbar 133:3 / 113:1 — the identity arm, unassigned',
     lambda: the_daughters({'ask': 'identity'}, DATA), 'unassigned: Zelophehad the wood-gatherer (R. Akiva) against the concealment (R. Yehuda b. Beteira)'),
    ('Sifrei Bamidbar 133:4 / Yevamot 24a (the family engine called) — name is inheritance',
     lambda: the_daughters({'ask': 'name_is_inheritance'}, DATA), 'the plea\'s "name" is inheritance — the levirate\'s word (Deut 25:6) read from 48:6'),
    ('Num 27:1-11 + 36:1-12 — the chapter\'s own case as one pipeline',
     lambda: the_daughters({'ask': 'the_case'}, DATA), 'drew near and stood, the judgment brought near, rightly — a holding among their father\'s brothers and the ladder for the generations; the tribes: rightly — within the tribe, this generation; married their uncles\' sons, the inheritance remained; the giving in Joshua'),
    # THE WRAP: the scene and the narrative on the world engine
    ('THE SCENE on the world engine — the wrap: nine exam rows, one effect each (the tuple typed from THE_TENT.md section 4)',
     lambda: (SCENE, [FX.NONE], [('INK', 'Num 27:8-11, 36:3-9; Deut 21:17, 25:5 — the recorded rows replayed')]),
     (1, 1, 1, 1, 1, 1, 1, 1, 1)),
    ('THE NARRATIVE on the world engine — the tape\'s six lines with the tent daemon first (the tripwire typed from THE_TENT.md section 4)',
     lambda: (NARRATIVE, [FX.NONE], [('INK', 'Num 27:1-11, 36:1-12 — the plea, the judgment brought near, the statute; the tribes, the relayed command, the marriage')]),
     (1, [True], 1, False, ['law_zelophehad'], 2, ['law_zelophehad', 'law_zelophehad:tribe_transfer'], 1, 1, 1)),
]

if __name__ == '__main__':
    ok = 0
    frac = {'INK': 0, 'MOVE': 0, 'DATA': 0}
    used_effects = []
    print()
    for label, fn, want in CASES:
        got, effects, prov = fn()
        hit = got == want
        ok += hit
        kinds = [k for k, _ in prov]
        cls = 'INK' if all(k == 'INK' for k in kinds) else ('MOVE' if 'MOVE' in kinds else 'DATA')
        frac[cls] += 1
        print('%s  [%s]  %s' % ('PASS' if hit else 'MISS', cls, label))
        if not hit:
            print('      expected: %s' % (want,))
            print('      got     : %s' % (got,))
        used_effects.extend(e for e in effects if e != FX.NONE)
        for kind, line in prov:
            print('        ->%s' % line)
    print()
    print('WATCH COVERAGE (the wrap):')
    _WN.print_coverage()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, len(CASES)))
    n = len(CASES)
    print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%) · data %d/%d (%.0f%%)' %
          (frac['INK'], n, 100.0 * frac['INK'] / n, frac['MOVE'], n, 100.0 * frac['MOVE'] / n, frac['DATA'], n, 100.0 * frac['DATA'] / n))
    ops = {}
    for e in used_effects:
        ops[FX.REGISTRY[e]['ledger_op']] = ops.get(FX.REGISTRY[e]['ledger_op'], 0) + 1
    print('LEDGER OPS this span writes:', ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
    print('THE PARAMETER ROWS: land_divided_among = %s; eretz_yisrael_status = %s; mothers_property = %s; daughters_marriage = %s; tribe_transfer_reach = %s; names_order = %s (the other settings recorded in DATA)' %
          tuple(DATA[k]['value'] for k in ('land_divided_among', 'eretz_yisrael_status', 'mothers_property', 'daughters_marriage', 'tribe_transfer_reach', 'names_order')))
    print('THE FORK PRINTED: under tribe_transfer_reach = all_generations the bar would hold every heiress forever — refused at Bava Batra 120b:2 (the silence test); under daughters_marriage = commanded the tape\'s 36:5-9 would bind the daughters as the generation — Rabba resolved: everyone except them.')
    print('THE RULE INSIDE A CASE-BORN LAW: the relayed command at 36:5-9 installs law_zelophehad:tribe_transfer — a cell of this daemon with a reach (this generation), lapsed on the fifteenth of Av; its in-force gate is the second pass\'s (D2).')
    print('THE HOLDING STAYS OPEN: the daughters\' holding_owed is closed by no Torah verse — the giving is Josh 17:4, the readback\'s item beside the men\'s second Passover.')
    if ok == len(CASES):
        print('\nTHE DAUGHTERS OF ZELOPHEHAD COMPILE — the third Numbers span, the fourth case-born law: the ladder for the generations, the halt\'s third form, the scope, the dilemma run before the answer, the second output relayed with its reach; G2\'s owed edge paid.')
