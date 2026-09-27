import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16b (2026-09-25): the design of the compile of CHAPTERS 19-21 — LEAN — appended to the map after sitting 16's AS BUILT (the newest section),
# every number read from the recon's print (ch19_compile_recon.out) and the exam rows' print (ch19_exam_rows.out) and asserted here before the text is built from its
# three parts (ch19b_design_a/b/c.txt); NO Hebrew script in the map (the lint 0). write_ch17b_design.py's form over three chapters. RUN FROM THE REPO ROOT.
import re, os, subprocess, sys
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MAP = ROOT + '/World/step9/DEUTERONOMY_WALK.md'
m = open(MAP, encoding='utf-8').read()
assert '## Sitting 16b — THE COMPILE OF CHAPTERS 19-21' not in m, 'already written'
i = m.rfind('## Sitting 16 — CHAPTERS 19-21 — AS BUILT — LEAN'); assert i > 0 and m.find('\n## ', i + 10) < 0, 'the AS BUILT of sitting 16 is the newest section'
rec = open(SP + '/ch19_compile_recon.out', encoding='utf-8').read()
def R(pat):
    g = re.search(pat, rec, re.M); assert g, pat; return g.group(1)
RUN = R(r"^\d+: RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),"); assert RUN == '1349, 96, 88, 0, 12, 1709, 48, 319', RUN
PREV = R(r"^\d+: PREVIOUS_RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),"); assert PREV == '1341, 96, 88, 0, 12, 1672, 47, 319', PREV
PL = R(r"^\d+: PLACEMENT = (\{.*?\}\})"); assert PL == "{'markers': {'text_constrained': 108, 'reading_placed': 49}, 'events': {'text_constrained': 110, 'page_order': 1181, 'reading_placed': 58}}", PL
assert R(r"^\d+: NEWEST_RUNNER = '(\w+)'") == 'courts_prophet'
assert R(r"the D series in use: (\[.*?\])") == "['DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI']"
assert "VERDICTS DI line: [\"            'DI1 MATCH', 'DI2 MATCH', 'DI3 MATCH', 'DI4 MATCH', 'DI5 MATCH'," in rec
NL = R(r"^(lines naming Deut 19, 20 or 21: .*)$"); assert NL.startswith("lines naming Deut 19, 20 or 21: [(234, ") and "(3378, " in NL and 'w.submit' not in NL, 'NO tape line names the chapters — a comment and DE8 only'
IMP, DO = R(r'^import lines: (\d+)'), R(r'\| DAEMON_ORDER tuples: (\d+)'); assert (IMP, DO) == ('31', '45'), (IMP, DO)
CPS = R(r'^checkpoints: (\d+)'); assert CPS == '304', CPS
E, P, S = R(r'^edges (\d+)'), R(r'\| pointers (\d+)'), R(r'\| spans (\d+)'); assert (E, P, S) == ('752', '211', '72'), (E, P, S)
EP = R(r"^(edges/pointers naming Deut 19/20/21 or refuge_war_family: .*)$"); assert EP.startswith("edges/pointers naming Deut 19/20/21 or refuge_war_family: [('ordinances', 'family', False, ") and "('balak', 'mekoshesh', 'CALL', " in EP and EP.endswith(")] []"), 'two edges name a chapter verse in their why, no pointer'
assert "edges from courts_prophet: [('seducers', 'reference', 'CALL'), ('festivals_judges', 'reference', 'CALL')" in rec and "('refuge', 'reference', 'PARAMETER')" in rec and "('good_land', 'reference', 'PARAMETER'), ('balak', 'reference', 'CALL'), ('pre_sinai', 'reference', 'CALL'), ('family', 'none', False)]" in rec
D, FN = R(r'^daemons (\d+)'), R(r'\| functions \(runners\) (\d+)'); assert (D, FN) == ('77', '71'), (D, FN)
assert "daemons of the kin: [('law_family', 'Gen 23:1', 'boot'), ('law_lev24', 'Lev 24:10', 'sentence_declared'), ('law_refuge', 'Num 35:1', 'boot'), ('law_seven_nations', 'Deut 7:1', 'boot'), ('law_seducers', 'Deut 13:1', 'boot'), ('law_festivals_judges', 'Deut 16:1', 'boot'), ('law_courts_prophet', 'Deut 17:1', 'boot'), ('law_chukat', 'Num 19:1', 'boot'), ('law_midian', 'Num 31:21', 'boot'), ('law_gad_reuben', 'Num 32:20', 'boot'), ('law_zelophehad', 'Num 27:1', 'statute_declared')]" in rec
assert "seats naming Deut 19/20/21: [('Deut 20:17', \"{'class': 'NONE', 'why': 'Deuteronomy is not on the tape (the book not read) — the seat waits for its reading and compile'}\")]" in rec
assert "len(real) == 77 and all(" in rec and "readback defs: ['def q42():', 'def q43():', 'def q44():']" in rec
FX, KD = R(r'^effects (\d+)'), R(r'\| kinds (\d+)'); assert (FX, KD) == ('1125', '1179'), (FX, KD)
assert 'the candidate new effects present before: [] | the candidate kinds present before: []' in rec
W = {k: R(r'^ W %s (\d+)' % k) for k in ('cities_set_apart', 'pity_barred', 'israel_hears_and_fears', 'one_witness_barred', 'two_witnesses_required', 'witnesses_hand_first_commanded', 'idolater_inquiry_required', 'abominations_learning_barred', 'condemned_city_inquiry_required', 'devoted_thing_cleaving_barred', 'cherem_vowed', 'fear_not_promised', 'taken_captive', 'spoil_taken', 'boundary_witnessed', 'hanged', 'buried', 'burial_owed', 'atoned_forgiven', 'blood_required', 'firstborn_by_the_head', 'hated', 'inheritance_stayed_in_tribe', 'substituted_for_the_firstborn', 'stoned', 'put_to_death', 'courts_established', 'judges_charged', 'evil_purged_from_the_midst', 'dwells_in_refuge', 'flees_to_refuge', 'land_polluted_by_blood', 'city_devoted', 'nations_driven_out', 'lashes')}
assert W == {'cities_set_apart': '1', 'pity_barred': '2', 'israel_hears_and_fears': '1', 'one_witness_barred': '1', 'two_witnesses_required': '1', 'witnesses_hand_first_commanded': '1', 'idolater_inquiry_required': '1', 'abominations_learning_barred': '1', 'condemned_city_inquiry_required': '1', 'devoted_thing_cleaving_barred': '1', 'cherem_vowed': '1', 'fear_not_promised': '4', 'taken_captive': '3', 'spoil_taken': '2', 'boundary_witnessed': '1', 'hanged': '1', 'buried': '9', 'burial_owed': '1', 'atoned_forgiven': '7', 'blood_required': '1', 'firstborn_by_the_head': '2', 'hated': '3', 'inheritance_stayed_in_tribe': '1', 'substituted_for_the_firstborn': '1', 'stoned': '2', 'put_to_death': '7', 'courts_established': '1', 'judges_charged': '1', 'evil_purged_from_the_midst': '0', 'dwells_in_refuge': '0', 'flees_to_refuge': '0', 'land_polluted_by_blood': '0', 'city_devoted': '0', 'nations_driven_out': '0', 'lashes': '0'}, W
assert " W cities_set_apart 1 [('israel_people', 'status')]" in rec and " W fear_not_promised 4 [('isaac', 'heaven'), ('jacob', 'heaven'), ('moses', 'heaven'), ('yehoshua', 'heaven')]" in rec and " W taken_captive 3 [('lot', 'body'), ('israel_people', 'body'), ('the_captives_of_midian', 'body')]" in rec and " W hanged 1 [('the_baker', 'body')]" in rec and " W blood_required 1 [('noach', 'heaven')]" in rec and " W firstborn_by_the_head 2 [('esau', 'status'), ('perez', 'status')]" in rec and " W boundary_witnessed 1 [('the_heap_and_pillar', 'status')]" in rec
IPL, IPB, IPS = R(r'^ israel_people ledger entries (\d+)'), R(r'ledger entries \d+ \| blocks (\d+)'), R(r'\| statuses (\d+)'); assert (IPL, IPB, IPS) == ('273', '62', '134'), (IPL, IPB, IPS)
assert "the last eight effects: ['familiar_spirit_barred', 'necromancer_barred', 'wholeness_commanded', 'prophet_like_moses_promised', 'prophet_hearkening_commanded', 'word_required_of_the_hearer', 'false_word_test_declared', 'false_prophet_fear_barred']" in rec
ENT, CL, MK, EV = R(r'^ entities (\d+)'), R(r'\| closes (\d+)'), R(r'\| markers (\d+)'), R(r'\| events (\d+)'); assert (ENT, CL, MK, EV) == ('319', '127', '172', '1349'), (ENT, CL, MK, EV)
assert '| the day (40, 11, 1) | population rows 148' in rec and "the tape's last six events: [('high_court_declared', 'Deut 17:8-13'), ('king_law_declared', 'Deut 17:14-2'), ('priests_dues_declared', 'Deut 18:1-5 '), ('levite_at_the_place_declared', 'Deut 18:6-8 '), ('diviners_barred', 'Deut 18:9-14'), ('prophet_law_declared', 'Deut 18:15-2')]" in rec
F = rec[rec.index('==== F. THE KIN'):rec.index('==== G. THE RUNNING WORLD')]
N_KIN_DEFS = len(re.findall(r'^ [a-z_0-9]+\.[a-z_0-9]+: refs \[', F, re.M)); assert N_KIN_DEFS > 100, N_KIN_DEFS
ex = open(SP + '/ch19_exam_rows.out', encoding='utf-8').read()
g = re.search(r'^CITED AT LEAST TWICE: (\d+) \| distinct citations: (\d+) \|', ex, re.M); assert g, 'the exam rows print'
NROWS, NCITE = g.group(1), g.group(2); assert (NROWS, NCITE) == ('28', '56'), (NROWS, NCITE)
assert ex.count('==== Mishnah ') == 28 and 'TOTAL CHARS 65637' in ex
T = ''.join(open(SP + '/ch19b_design_%s.txt' % p, encoding='utf-8').read() for p in 'abc')
SUB = dict(RUN=RUN, PREV=PREV, PL=PL, IMP=IMP, DO=DO, CPS=CPS, E=E, P=P, S=S, D=D, FN=FN, FX=FX, KD=KD, ENT=ENT, CL=CL, MK=MK, EV=EV, IPL=IPL, IPB=IPB, IPS=IPS, NKIN=str(N_KIN_DEFS), NROWS=NROWS, NCITE=NCITE, EVN=RUN.split(', ')[0], WRN=RUN.split(', ')[5], DMN=RUN.split(', ')[6])
for k, v in SUB.items():
    T = T.replace('%%(%s)s' % k, v)
assert '%(' not in T, [x for x in re.findall(r'%\(\w+\)s', T)]
assert not re.search(r'[֐-׿]', T), 'NO HEBREW SCRIPT IN THE MAP'
assert T.startswith('## Sitting 16b — THE COMPILE OF CHAPTERS 19-21') and T.endswith('the ten deferred records.\n')
if '--check' in sys.argv:
    print('CHECK ONLY: %d bytes of design; the kin defs %d; the exam rows %s of %s citations; no write' % (len(T.encode()), N_KIN_DEFS, NROWS, NCITE)); sys.exit(0)
open(MAP, 'w', encoding='utf-8').write(m.rstrip('\n') + '\n\n' + T)
print('THE DESIGN WRITTEN: %d bytes appended; the map %d bytes; the kin defs %d' % (len(T.encode()), os.path.getsize(MAP), N_KIN_DEFS))
