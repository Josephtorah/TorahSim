import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 17b (2026-09-26): the design of the compile of CHAPTERS 22-25 — LEAN — appended to the map after sitting 17's AS BUILT (the newest section),
# every number read from the recon's print (ch22_compile_recon.out), the exam rows' print (ch22_exam_rows.out) and the callees' prints and asserted here before the
# text is built from its four parts (ch22b_design_a/b/c/d.txt); NO Hebrew script in the map (the lint 0). write_ch19b_design.py's form over four chapters. RUN FROM THE REPO ROOT.
import re, os, subprocess, sys
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MAP = ROOT + '/World/step9/DEUTERONOMY_WALK.md'
m = open(MAP, encoding='utf-8').read()
assert '## Sitting 17b — THE COMPILE OF CHAPTERS 22-25' not in m, 'already written'
i = m.rfind('## Sitting 17 — CHAPTERS 22-25 — AS BUILT — LEAN'); assert i > 0 and m.find('\n## ', i + 10) < 0, 'the AS BUILT of sitting 17 is the newest section'
rec = open(SP + '/ch22_compile_recon.out', encoding='utf-8').read()
def R(pat):
    g = re.search(pat, rec, re.M); assert g, pat; return g.group(1)
RUN = R(r"^\d+: RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),"); assert RUN == '1362, 96, 88, 0, 12, 1754, 49, 319', RUN
PREV = R(r"^\d+: PREVIOUS_RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),"); assert PREV == '1349, 96, 88, 0, 12, 1709, 48, 319', PREV
PL = R(r"^\d+: PLACEMENT = (\{.*?\}\})"); assert PL == "{'markers': {'text_constrained': 108, 'reading_placed': 49}, 'events': {'text_constrained': 110, 'page_order': 1194, 'reading_placed': 58}}", PL
assert R(r"^\d+: NEWEST_RUNNER = '(\w+)'") == 'refuge_war_family'
assert R(r"the D series in use: (\[.*?\])") == "['DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI', 'DJ']"
assert "VERDICTS DJ line: [\"            'DJ1 MATCH', 'DJ2 MATCH', 'DJ3 MATCH', 'DJ4 MATCH', 'DJ5 MATCH'," in rec
assert 'lines naming Deut 22, 23, 24 or 25: []' in rec, 'NO tape line names the chapters'
assert "(2480, \"    w.submit({'kind': 'hanged_burial_declared'" in rec
IMP, DO = R(r'^import lines: (\d+)'), R(r'\| DAEMON_ORDER tuples: (\d+)'); assert (IMP, DO) == ('32', '46'), (IMP, DO)
CPS = R(r'^checkpoints: (\d+)'); assert CPS == '309', CPS
E, P, S = R(r'^edges (\d+)'), R(r'\| pointers (\d+)'), R(r'\| spans (\d+)'); assert (E, P, S) == ('778', '214', '73'), (E, P, S)
assert "('family', 'deut_family', 'OWED', \"Deut 25:5-10 — THE LEVIRATE AND THE SHOE | 38:8 'perform the levir's duty'" in rec, 'the one OWED edge naming the chapters'
assert "edges from refuge_war_family: [('place_name', 'reference', 'CALL'), ('chatat', 'none', False), ('pesach', 'none', False)" in rec and "edges from holiness: [('offerings', 'reference', 'VIA'), ('pre_sinai', 'reference', 'REVERSE'), ('tzav', 'reference', 'CALL'), ('vayikra5', 'reference', 'CALL'), ('yovel', 'transfer', 'CALL')]" in rec
D, FN = R(r'^daemons (\d+)'), R(r'\| functions \(runners\) (\d+)'); assert (D, FN) == ('78', '72'), (D, FN)
assert "daemons of the kin: [('law_family', 'Gen 23:1', 'boot'), ('law_pre_sinai', 'Gen 1:1', 'boot'), ('law_mishpatim_2', 'Exod 21:22', 'covenant_blood_thrown'), ('law_lev24', 'Lev 24:10', 'sentence_declared'), ('law_mekoshesh', 'Num 15:32', 'sentence_declared'), ('law_refuge', 'Num 35:1', 'boot')" in rec
assert "| seats naming Deut 22-25: []" in rec and "len(real) == 78 and all(" in rec and "readback defs: ['def q43():', 'def q44():', 'def q45():']" in rec
FX, KD = R(r'^effects (\d+)'), R(r'\| kinds (\d+)'); assert (FX, KD) == ('1170', '1192'), (FX, KD)
assert 'the candidate new effects present before: [] | the candidate kinds present before: []' in rec
W = {k: R(r'^ W %s (\d+)' % k) for k in ('evil_purged_from_the_midst', 'pity_barred', 'talion_pity_barred', 'put_to_death', 'stoned', 'lashes', 'pays', 'exempt', 'israel_hears_and_fears', 'hanged', 'buried', 'same_day_burial_commanded', 'captive_release_commanded', 'fearful_exemption_commanded', 'officers_exemptions_commanded', 'bribe_barred', 'judges_charged', 'courts_established', 'interest_barred', 'pledge_returned_by_sunset', 'sent_outside_the_camp', 'firstborn_by_the_head', 'inheritance_stayed_in_tribe', 'peace_call_commanded', 'blood_required', 'innocent_blood_purge_commanded')}
assert W == {'evil_purged_from_the_midst': '0', 'pity_barred': '2', 'talion_pity_barred': '1', 'put_to_death': '7', 'stoned': '2', 'lashes': '0', 'pays': '1', 'exempt': '1', 'israel_hears_and_fears': '1', 'hanged': '1', 'buried': '9', 'same_day_burial_commanded': '1', 'captive_release_commanded': '1', 'fearful_exemption_commanded': '1', 'officers_exemptions_commanded': '1', 'bribe_barred': '1', 'judges_charged': '1', 'courts_established': '1', 'interest_barred': '0', 'pledge_returned_by_sunset': '0', 'sent_outside_the_camp': '2', 'firstborn_by_the_head': '2', 'inheritance_stayed_in_tribe': '1', 'peace_call_commanded': '1', 'blood_required': '1', 'innocent_blood_purge_commanded': '1'}, W
assert 'NEW_E on the running world (any): []' in rec
IPL, IPB, IPS = R(r'^ israel_people ledger entries (\d+)'), R(r'ledger entries \d+ \| blocks (\d+)'), R(r'\| statuses (\d+)'); assert (IPL, IPB, IPS) == ('318', '72', '168'), (IPL, IPB, IPS)
assert "the last eight effects: ['firstborn_double_portion_commanded', 'firstborn_right_transfer_barred', 'rebellious_son_seized_commanded', 'rebellious_son_stoning_commanded', 'hanging_after_death_commanded', 'corpse_overnight_barred', 'same_day_burial_commanded', 'land_defilement_barred']" in rec
ENT, CL, MK, EV = R(r'^ entities (\d+)'), R(r'\| closes (\d+)'), R(r'\| markers (\d+)'), R(r'\| events (\d+)'); assert (ENT, CL, MK, EV) == ('319', '127', '172', '1362'), (ENT, CL, MK, EV)
assert '| the day (40, 11, 1) | population rows 148' in rec and "the tape's last six events: [('siege_trees_declared', 'Deut 20:19-2'), ('heifer_rite_declared', 'Deut 21:1-9 '), ('captive_wife_declared', 'Deut 21:10-1'), ('firstborn_portion_declared', 'Deut 21:15-1'), ('rebellious_son_declared', 'Deut 21:18-2'), ('hanged_burial_declared', 'Deut 21:22-2')]" in rec
F = rec[rec.index('==== F. THE KIN'):rec.index('==== G. THE RUNNING WORLD')]
N_KIN_DEFS = len(re.findall(r'^ [a-z_0-9]+\.[a-z_0-9]+: refs \[', F, re.M)); assert N_KIN_DEFS > 100, N_KIN_DEFS
ex = open(SP + '/ch22_exam_rows.out', encoding='utf-8').read()
g = re.search(r'^CITED AT LEAST TWICE: (\d+) \| distinct citations: (\d+) \|', ex, re.M); assert g, 'the exam rows print'
NROWS, NCITE = g.group(1), g.group(2); assert (NROWS, NCITE) == ('44', '111'), (NROWS, NCITE)
assert ex.count('==== Mishnah ') == 44 and 'TOTAL CHARS 85699' in ex
ca = ''.join(open(SP + '/ch22_callees%s.out' % s, encoding='utf-8').read() for s in ('', '2', '3'))
NFACT, NFAIL = len(re.findall(r'^FACT ', ca, re.M)), len(re.findall(r'^FAIL ', ca, re.M)); assert (NFACT, NFAIL) == (72 + 173 + 62, 3 + 36 + 0), (NFACT, NFAIL)
for s in ("FACT good_land.receipt_seats(22..25) = [[], [], [], []]", "FACT yovel.interest_scope(foreigner) = ('permitted', 'MOVE', ['—'], \"IMPORT EDGE (M-07):", " W levirate_owed 2 [('shelah', 'debit', 'Gen 38:14'), ('onan', 'debit', 'Gen 38:8')]", " W amalek_to_be_blotted 1 [('amaleq', 'heaven', 'Exod 17:14-16')]", "FACT naso.camp_purity(who_is_sent, {'what': 'seed_emitter'}) = ('no verdict in span', ['—'])", "PROBES: list | 6 items | hits ['fifty', 'dowry'] | head: [('dowry', 4119, 'Exod', 22, 16), ('fifty', 2572, 'Deut', 22, 29)", "the last Deut 21 submit line: [(2480,"):
    assert s in ca, s[:60]
T = ''.join(open(SP + '/ch22b_design_%s.txt' % p, encoding='utf-8').read() for p in 'abcd')
SUB = dict(RUN=RUN, PREV=PREV, PL=PL, IMP=IMP, DO=DO, CPS=CPS, E=E, P=P, S=S, D=D, FN=FN, FX=FX, KD=KD, ENT=ENT, CL=CL, MK=MK, EV=EV, IPL=IPL, IPB=IPB, IPS=IPS, NKIN=str(N_KIN_DEFS), NROWS=NROWS, NCITE=NCITE, NFACT=str(NFACT), NFAIL=str(NFAIL), EVN=RUN.split(', ')[0], WRN=RUN.split(', ')[5], DMN=RUN.split(', ')[6])
for k, v in SUB.items():
    T = T.replace('%%(%s)s' % k, v)
assert '%(' not in T, [x for x in re.findall(r'%\(\w+\)s', T)]
assert not re.search(r'[֐-׿]', T), 'NO HEBREW SCRIPT IN THE MAP'
assert T.startswith('## Sitting 17b — THE COMPILE OF CHAPTERS 22-25') and T.endswith('the ten deferred records.\n')
if '--check' in sys.argv:
    print('CHECK ONLY: %d bytes of design; the kin defs %d; the exam rows %s of %s citations; the callees %d facts, %d fails; no write' % (len(T.encode()), N_KIN_DEFS, NROWS, NCITE, NFACT, NFAIL)); sys.exit(0)
open(MAP, 'w', encoding='utf-8').write(m.rstrip('\n') + '\n\n' + T)
print('THE DESIGN WRITTEN: %d bytes appended; the map %d bytes; the kin defs %d' % (len(T.encode()), os.path.getsize(MAP), N_KIN_DEFS))
