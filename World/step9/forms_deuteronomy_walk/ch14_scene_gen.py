#!/usr/bin/env python3
# THE DEUTERONOMY WALK 12b: the scene's LITERAL submits generated from PERSONS (the daemon gate reads literal submits only — the seventy-one persons are written by
# this script from part 4's own list, then frozen in the file), with scene() and narrative() appended to ch14_part4.py; the prediction typed from the design's
# arithmetic (every person once; the eater of the torn TWICE — the lashes and the torn to the dog; eight exempt; ten lashed; eleven barred; two impure; one torn
# to the dog; one left for the poor); idempotent. ch13_scene_gen.py's form. RUN FROM THE REPO ROOT.
import ast, os
SP = os.path.dirname(os.path.abspath(__file__))
p4 = f'{SP}/ch14_part4.py'; src = open(p4, encoding='utf-8').read()
assert 'def scene():' not in src, 'already appended'
tree = ast.parse(src); persons = None
for node in tree.body:
    if isinstance(node, ast.Assign) and node.targets[0].id == 'PERSONS': persons = ast.literal_eval(node.value)
assert persons and len(persons) == 71, len(persons)   # seventy-one — the seven write asks are case rows, not persons (11b's lesson 3)
sub = '\n'.join("        w.submit({'kind': 'food_tithe_case', 'subject': %r, 'person': %r, 'cell': %r, 'ask': %r, 'case_source': %r})" % (p, p, c, a, s) for p, c, a, s in persons)
TWO = ('the-eater-of-the-torn',)
EXEMPT = ('the-one-who-cuts-himself-for-his-fallen-house', 'the-eater-of-the-putrid-carcass', 'the-one-who-cooks-fowl-in-milk', 'the-one-who-eats-a-casual-snack-before-the-pile-is-smoothed', 'the-one-who-brings-a-firstling-from-babylonia', 'the-one-who-would-tithe-the-seventh-years-produce', 'the-resident-alien-at-the-gate', 'the-herdsman-today')
block = '''

def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through food_tithe_case — seventy-one persons: EIGHT EXEMPT
    (the one who cuts himself for his fallen house — Makkot 20b:10; the eater of the putrid carcass — Avodah Zarah 67b:8; the one who cooks fowl in milk — the
    Sifrei 104:10; the casual snack before the pile is smoothed — Mishnah Maasrot 1:5; the firstling from Babylonia — Temurah 21b:3; the seventh year's produce —
    the Sifrei 109:4; the resident alien at the gate — Pesachim 21b:9; the herdsman today — Bekhorot 53b:5), TEN LASHED (the mourner who cuts himself, the bald
    spots, the eater of the camel, of the eel, of the clawer, of the hornet, of the torn, of the carcass, the second tithe outside the wall), ELEVEN BARRED (the
    hire of a harlot, the ostrich's egg, the kid in its mother's milk, the benefit, the new for the old, no Temple, the sale, the blank coin, the money in the sea,
    water and salt, the debt), TWO IMPURE (the swine's carcass touched, the priest and the clean bird's carcass), the torn to the dog, the corner left for the poor,
    the rest accepted on the shelf's arms. No timer; no close."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 14:1-29: chapter 14 on the shelf — Chullin, Makkot, Yevamot, Kiddushin, Maaser Sheni, Maasrot, Rosh Hashanah, Bekhorot, Pesachim, Bava Metzia, Temurah, Eruvin, Peah, Zevachim, Avodah Zarah on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_food_tithe]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the seventy-one persons typed out from PERSONS (ch14_scene_gen.py wrote these lines from the list; frozen here)
%s
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    SEVEN = ('accepted', 'exempt', 'lashes', 'barred_from_it', 'impure_until_evening', 'torn_flesh_to_dogs', 'left_for_the_poor')
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (tuple(sum(n(p, eff) for eff in SEVEN) for p, _, _, _ in PERSONS), tuple(n(p, 'exempt') for p in %r), sum(n(p, 'lashes') for p, _, _, _ in PERSONS), sum(n(p, 'barred_from_it') for p, _, _, _ in PERSONS), sum(n(p, 'impure_until_evening') for p, _, _, _ in PERSONS), sum(n(p, 'torn_flesh_to_dogs') for p, _, _, _ in PERSONS), sum(n(p, 'left_for_the_poor') for p, _, _, _ in PERSONS), (tset, tfire, tcan, len(getattr(w, 'timers', []) or [])), len(w.entities), closes), w
SCENE, _W = scene()
print('THE SCENE (printed before it is asserted):', SCENE)
# THE PREDICTION (typed before the first run — the design's arithmetic): every exam person written once (the eater of the torn TWICE — the lashes and the torn to
# the dog); the eight exempt arms ONE each; TEN lashes; barred_from_it 11, impure_until_evening 2, torn_flesh_to_dogs 1, left_for_the_poor 1; no timer; ENTITIES the
# seventy-one persons (the dog and the poor counterparties named, not entities); CLOSES 0.
SCENE_PREDICTED = (tuple(2 if p in %r else 1 for p, _, _, _ in PERSONS), (1,) * 8, 10, 11, 2, 1, 1, (0, 0, 0, 0), 71, 0)
assert SCENE == SCENE_PREDICTED, ('THE DEUTERONOMY WALK 12b: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE DEUTERONOMY WALK 12b (2026-09-22): the chapter's own laws AS HISTORY — FIVE own-day lines with no marker (the code's five holes compiled at the
    counter's day (40, 11, 1): sons_and_mourning_declared, food_law_declared, carcass_and_kid_declared, second_tithe_declared, third_year_tithe_declared) on a
    world with this runner's daemon: 7 writes (all on Israel — five new, two reuses), no timer, ONE entity (Israel — the written-on party; a line's subject makes
    no entity, 7b's lesson), the counter at (11, 1), no close, no row, no dated line. Recorded by the sequential run's recorder and stitched onto the tape after
    the last Deuteronomy 13 line. Not a graded cell: the tuple below is a tripwire typed from the design."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 14:1-29 on the tape — the sons and the cuttings, the food law, the carcass and the kid, the second tithe, the third year\\'s tithe at the counter\\'s own day, no marker (the exodus epoch)', epoch='exodus')
        w.laws = [law_food_tithe]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the five lines typed out; no marker; no field named `until`, `days` or `due`
        w.submit({'kind': 'sons_and_mourning_declared', 'subject': 'israel', 'the_sons': 'sons you are to the LORD your God (14:1) — R. Yehuda conditional, R. Meir either way', 'the_cuttings': "you shall not cut yourselves (14:1) — the mourners' cutting and 'no factions' from one word", 'the_baldness': "nor make baldness between your eyes for the dead (14:1) — the whole head, per spot, by the analogy both ways with the priests'", 'the_holy_people': "for you are a holy people (14:2) — 7:6 said again; treasured_people unmoved", 'case_source': LINES[0][0]})
        w.submit({'kind': 'food_law_declared', 'subject': 'israel', 'the_abomination': 'you shall not eat any abomination (14:3) — what I have made abominable for you', 'the_ten': 'the ox, the sheep and the goat, the hart, the gazelle, the roebuck, the wild goat, the ibex, the antelope and the mountain sheep (14:4-5) — ten named and no more', 'the_signs': 'the hoof parted and cloven in two, the cud chewed (14:6) — the twin chapter by CALL', 'the_four': 'the camel, the hare, the coney, the swine (14:7-8) — closed by "it"', 'the_water': 'fins and scales (14:9-10)', 'the_birds': 'every clean bird you may eat (14:11, 14:20) — the permission Leviticus lacks; the_birds_signs a parameter', 'case_source': LINES[1][0]})
        w.submit({'kind': 'carcass_and_kid_declared', 'subject': 'israel', 'the_carcass': 'you shall not eat any carcass (14:21) — the ban\\'s seat the sanctions engine names; the torn included', 'the_sojourner': 'to the sojourner in your gates you may give it (14:21) — the resident alien, sustained', 'the_foreigner': 'or sell it to a foreigner (14:21) — the four-cell table a parameter; the sale clause the paradigm of a permitted benefit', 'the_kid': "you shall not boil a kid in its mother's milk (14:21) — the third seat's gain the assignment; no new write", 'case_source': LINES[2][0]})
        w.submit({'kind': 'second_tithe_declared', 'subject': 'israel', 'the_tithe': 'tithe, you shall tithe (14:22) — named the second by the shelf', 'the_place': 'and you shall eat before the LORD your God in the place which He will choose (14:23) — the wall, the House, the year', 'the_far_place': 'and when the way is too long for you (14:24) — of place not time', 'the_money': 'then you shall turn it into money, and bind up the money in your hand (14:25) — the_moneys_form a parameter', 'the_rejoicing': 'and rejoice, you and your household (14:26) — rejoicing_before_the_lord_commanded REUSED', 'the_levite': 'and the Levite who is in your gates, you shall not forsake him (14:27) — levite_forsaking_barred REUSED', 'case_source': LINES[3][0]})
        w.submit({'kind': 'third_year_tithe_declared', 'subject': 'israel', 'the_third_year': 'at the end of three years you shall bring out all the tithe of your yield in that year (14:28) — one tithe not two; the_removal_date, the_tithes_new_year', 'the_gates': 'and lay it up within your gates (14:28) — the courtyard\\'s liability', 'the_four': 'the Levite, the sojourner, the fatherless and the widow shall come and eat and be satisfied (14:29) — sons of the covenant', 'case_source': LINES[4][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    rows = len([l for l in w.log if l[0] == 'ROW'])
    dated = len([l for l in w.log if l[0] == 'EVENT' and l[2].get('dated') is not None])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes, rows, len(w.tables['population']), dated), w


NARRATIVE, _WN = narrative()
print('THE NARRATIVE (printed before it is asserted):', NARRATIVE, [e['effect'] for e in _WN.entity('israel_people').ledger])
NARRATIVE_PREDICTED = (7, 0, 1, (11, 1), 0, 0, 0, 0)   # DEUTERONOMY_WALK.md "Sitting 12b": 7 writes, no timer, ONE entity (Israel — the written-on party), the counter's day (11, 1), no close, no row, no population row, no dated line
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE DEUTERONOMY WALK 12b: the chapter\\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
_is = _WN.entity('israel_people').ledger
assert [e['effect'] for e in _is] == ['cuttings_for_the_dead_barred', 'abomination_eating_barred', 'carcass_eating_barred', 'second_tithe_owed', 'rejoicing_before_the_lord_commanded', 'levite_forsaking_barred', 'poor_tithe_owed'] and all(e.get('dated') is None for e in _is), [(e['effect'], e.get('dated')) for e in _is]   # the seven on Israel at the counter's day — five new, two reuses
_ev = [l for l in _WN.log if l[0] == 'EVENT']
assert [l[2]['kind'] for l in _ev] == ['sons_and_mourning_declared', 'food_law_declared', 'carcass_and_kid_declared', 'second_tithe_declared', 'third_year_tithe_declared'] and all(l[2].get('dated') is None for l in _ev) and not [l for l in _WN.log if l[0] == 'MARKER'], [(l[2]['kind'], l[2].get('dated')) for l in _ev]
''' % (sub, EXEMPT, TWO)
open(p4, 'w', encoding='utf-8').write(src + block)
import py_compile; py_compile.compile(p4, doraise=True)
print('scene generated: %d persons written into ch14_part4.py (the eater of the torn twice; %d exempt); scene() and narrative() appended; compiles' % (len(persons), len(EXEMPT)))
