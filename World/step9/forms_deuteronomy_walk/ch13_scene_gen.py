#!/usr/bin/env python3
# THE DEUTERONOMY WALK 11b: the scene's LITERAL submits generated from PERSONS (the daemon gate reads literal submits only — 10b typed twenty-nine by hand; forty
# here are written by this script from part 4's own list, then frozen in the file), with scene() and narrative() appended to ch13_part4.py; idempotent. RUN FROM THE REPO ROOT.
import ast, os
SP = os.path.dirname(os.path.abspath(__file__))
p4 = f'{SP}/ch13_part4.py'; src = open(p4, encoding='utf-8').read()
assert 'def scene():' not in src, 'already appended'
tree = ast.parse(src); persons = None
for node in tree.body:
    if isinstance(node, ast.Assign) and node.targets[0].id == 'PERSONS': persons = ast.literal_eval(node.value)
assert persons and len(persons) == 40, len(persons)   # forty — the storekeeper with roses is a case row, not a person (its ask returns the statute's write)
sub = '\n'.join("        w.submit({'kind': 'seducers_case', 'subject': %r, 'person': %r, 'cell': %r, 'ask': %r, 'case_source': %r})" % (p, p, c, a, s) for p, c, a, s in persons)
TWO = ('the-prophet-with-a-true-sign-who-preaches-idolatry-for-a-day', 'the-inciter-who-says-it-is-our-duty')
EXEMPT = ('the-prophet-who-keeps-part-and-voids-part', 'the-prophet-who-spoke-under-duress', 'elijah-at-carmel', 'the-inciter-who-retracts-before-the-fence', 'the-enticed-who-did-not-consent', 'the-inhabitants-of-jerusalem-drawn-away')
block = '''

def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through seducers_case — forty persons: SIX EXEMPT
    (the prophet who keeps part and voids part — Sanhedrin 90a:5; the prophet who spoke under duress — the Sifrei 86:1; Elijah at Carmel — Yevamot 90b:5-6; the
    inciter who retracts before the fence — Sanhedrin 67a:5; the enticed who did not consent — 61b; the inhabitants of Jerusalem drawn away — Bava Kamma 82b),
    ONE LASHED (the one who plows with the Asherah's wood — Makkot 22a:9), the false prophet PUT TO DEATH with the evil purged (the parameter's default arm),
    the inciter STONED with the evil purged, the inhabitant put to death by the sword, THE CONDEMNED CITY DEVOTED (city_devoted — a destroy effect), the rest
    accepted on the shelf's arms. No timer; no close."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 13:1-19: chapter 13 on the shelf — Sanhedrin, Zevachim, Sukkah, Menachot, Rosh Hashanah, Eruvin, Avodah Zarah, Bava Metzia, Yevamot, Shabbat, Bava Kamma, Makkot, Temurah, Chagigah, Kiddushin, Horayot on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_seducers]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the forty persons typed out from PERSONS (ch13_scene_gen.py wrote these lines from the list; frozen here)
%s
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    SEVEN = ('accepted', 'exempt', 'lashes', 'stoned', 'put_to_death', 'evil_purged_from_the_midst', 'city_devoted')
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (tuple(sum(n(p, eff) for eff in SEVEN) for p, _, _, _ in PERSONS), tuple(n(p, 'exempt') for p in %r), sum(n(p, 'lashes') for p, _, _, _ in PERSONS), sum(n(p, 'stoned') for p, _, _, _ in PERSONS), sum(n(p, 'put_to_death') for p, _, _, _ in PERSONS), sum(n(p, 'evil_purged_from_the_midst') for p, _, _, _ in PERSONS), n('the-condemned-city', 'city_devoted'), (tset, tfire, tcan, len(w.timers)), len(w.entities), closes), w
SCENE, _W = scene()
print('THE SCENE (printed before it is asserted):', SCENE)
# THE PREDICTION (typed before the first run — the design's arithmetic): every exam person written once (the false prophet and the inciter TWICE — the death and the
# purge); the six exempt arms ONE each; ONE lashes; stoned 1, put_to_death 2, evil_purged 2, city_devoted 1; no timer; ENTITIES the forty persons; CLOSES 0.
SCENE_PREDICTED = (tuple(2 if p in %r else 1 for p, _, _, _ in PERSONS), (1,) * 6, 1, 1, 2, 2, 1, (0, 0, 0, 0), 40, 0)
assert SCENE == SCENE_PREDICTED, ('THE DEUTERONOMY WALK 11b: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE DEUTERONOMY WALK 11b (2026-09-21): the chapter's own laws AS HISTORY — FOUR own-day lines with no marker (the code's four holes compiled at the
    counter's day (40, 11, 1): word_sealed, prophet_test_declared, inciter_law_declared, condemned_city_law_declared) on a world with this runner's daemon: 8 writes
    (all on Israel — five new, three reuses), no timer, ONE entity (Israel — the written-on party; a line's subject makes no entity, 7b's lesson), the counter at
    (11, 1), no close, no row, no dated line. Recorded by the sequential run's recorder and stitched onto the tape after the last Deuteronomy 12 line. Not a graded
    cell: the tuple below is a tripwire typed from the design."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 13:1-19 on the tape — the word sealed, the prophet tested, the inciter\\'s law, the condemned city\\'s law at the counter\\'s own day, no marker (the exodus epoch)', epoch='exodus')
        w.laws = [law_seducers]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the four lines typed out; no marker; no field named `until`, `days` or `due`
        w.submit({'kind': 'word_sealed', 'subject': 'israel', 'the_word': 'all the word that I command you, it you shall keep to do (13:1) — 4:2\\'s twin in the singular', 'the_seal': "you shall not add to it nor take from it (13:1) — adding_barred REUSED, a second entry; the three grains (82:3-5)", 'case_source': LINES[0][0]})
        w.submit({'kind': 'prophet_test_declared', 'subject': 'israel', 'the_prophet': 'when a prophet arises among you, or a dreamer of a dream (13:2) — the definition of a prophet', 'the_sign': "a sign or a wonder that comes to pass (13:2-3) — real by the parameter's first arm, the hearing barred anyway (13:4)", 'the_test': 'for the LORD your God is testing you (13:4) — the participle\\'s one seat', 'the_six_verbs': 'walk, fear, keep, obey, serve, cleave (13:5) — 10:20\\'s four made six; cleaving_commanded REUSED', 'the_death': "that prophet shall be put to death (13:6) — the mode a parameter (stoning / strangling); the evil purged from the midst — the formula's first seat", 'case_source': LINES[1][0]})
        w.submit({'kind': 'inciter_law_declared', 'subject': 'israel', 'the_inciter': 'when your brother, the son of your mother … entices you in secret (13:7) — the Torah\\'s one token of the root', 'the_kin': "the brother, the son, the daughter, the wife of your bosom, the friend as your own soul (13:7) — the inclusion table (87:4-11)", 'the_five_prohibitions': 'not consent, not hearken, not pity, not spare, not conceal (13:9) — pity_barred REUSED; the court\\'s rule inverted', 'the_hand_first': 'your hand first, the hand of all the people afterward (13:10)', 'the_stoning': "stone him with stones that he die (13:11) — the wood-gatherer's rite by CALL", 'the_hearing': 'all Israel shall hear and fear (13:12) — the formula\\'s first seat of four; the timing a parameter', 'case_source': LINES[2][0]})
        w.submit({'kind': 'condemned_city_law_declared', 'subject': 'israel', 'the_city': 'when you hear in one of your cities … to dwell there (13:13) — one city at a time; Jerusalem never', 'the_seducers': "men, sons of Belial, have gone out from your midst and have drawn away the inhabitants of their city (13:14) — the parameters from one noun", 'the_inquiry': 'inquire and search and ask diligently; true and certain (13:15) — the seven interrogations, a parameter', 'the_sword': 'smite, you shall smite with the edge of the sword (13:16) — decapitation, by any means; the children disputed', 'the_whole_offering': "devote it and all in it; gather its spoil into its street; burn it wholly to the LORD (13:16-17) — the property table's four cells; Heaven's spoil", 'the_heap': 'a heap forever, not built again (13:17) — Jericho and Hiel the run\\'s', 'the_devoted_thing': "nothing of the devoted thing shall cleave to your hand (13:18) — the benefit ban; the anger keyed to idolatry; the mercy two-armed; as He swore to your fathers", 'the_footer': 'when you hearken … to do the right in the eyes of the LORD (13:19) — the condition, no line, no write', 'case_source': LINES[3][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    rows = len([l for l in w.log if l[0] == 'ROW'])
    dated = len([l for l in w.log if l[0] == 'EVENT' and l[2].get('dated') is not None])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes, rows, len(w.tables['population']), dated), w


NARRATIVE, _WN = narrative()
print('THE NARRATIVE (printed before it is asserted):', NARRATIVE, [e['effect'] for e in _WN.entity('israel_people').ledger])
NARRATIVE_PREDICTED = (8, 0, 1, (11, 1), 0, 0, 0, 0)   # DEUTERONOMY_WALK.md "Sitting 11b": 8 writes, no timer, ONE entity (Israel — the written-on party), the counter's day (11, 1), no close, no row, no population row, no dated line
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE DEUTERONOMY WALK 11b: the chapter\\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
_is = _WN.entity('israel_people').ledger
assert [e['effect'] for e in _is] == ['adding_barred', 'false_prophet_hearing_barred', 'tested_by_the_lord', 'cleaving_commanded', 'pity_barred', 'israel_hears_and_fears', 'condemned_city_inquiry_required', 'devoted_thing_cleaving_barred'] and all(e.get('dated') is None for e in _is), [(e['effect'], e.get('dated')) for e in _is]   # the eight on Israel at the counter's day — five new, three reuses
_ev = [l for l in _WN.log if l[0] == 'EVENT']
assert [l[2]['kind'] for l in _ev] == ['word_sealed', 'prophet_test_declared', 'inciter_law_declared', 'condemned_city_law_declared'] and all(l[2].get('dated') is None for l in _ev) and not [l for l in _WN.log if l[0] == 'MARKER'], [(l[2]['kind'], l[2].get('dated')) for l in _ev]
''' % (sub, EXEMPT, TWO)
open(p4, 'w', encoding='utf-8').write(src.rstrip('\n') + '\n' + block)
import py_compile; py_compile.compile(p4, doraise=True)
print('scene and narrative appended to ch13_part4.py: %d persons; compiles; %d bytes' % (len(persons), len(open(p4).read())))
