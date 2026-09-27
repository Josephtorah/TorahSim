import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16b (2026-09-25): the assembler, the fast checker, the ask checker, the runner chain, the build chain, the tape chain, the gates shell and
# THE SCAN CENSUS DERIVED from 15b's copies in the forms folder by asserted substitutions (ch17 -> ch19, 15b -> 16b, courts_prophet -> refuge_war_family, FIVE typed
# parts and the nine cells, DI -> DJ, thirteen own-day lines, the forty-five names; the portable header made a scratch script's ROOT from git). derive_ch17_shells.py's form.
# RUN FROM THE REPO ROOT.
import subprocess, os, re
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
GIT = "ROOT = _ROOT"
def sub(text, old, new, n=None):
    c = text.count(old); assert c >= 1 and (n is None or c == n), (old[:60], c, n); return text.replace(old, new)
def strip_hdr(t):
    t = re.sub(r"^import os as _os\n_ROOT = _os\.path\.normpath\([^\n]*\n", "", t, count=1, flags=re.M)
    return sub(t, "ROOT = _ROOT", GIT, 1)
out = {}
a = strip_hdr(open(f'{FD}/ch17_assemble.py', encoding='utf-8').read())
a = sub(a, 'cold_run_courts_prophet.py', 'cold_run_refuge_war_family.py'); a = sub(a, 'ch17', 'ch19'); a = sub(a, "ch16_assemble.py's form", "ch17_assemble.py's form")
a = sub(a, "for n in (1, 2, 3, 4)]", "for n in (1, 2, 3, 4, 5)]", 1); a = sub(a, "p5 = f'{SP}/ch19_part5.py'", "p5 = f'{SP}/ch19_part6.py'", 1)   # the lean runner over three chapters: FIVE typed parts (the cells of F1-F3; F4-F6; F7-F9; the readback and the data; the daemon, the lines and the narrative) + the generated cases (part 6)
a = sub(a, "the CASES literal from part 5", "the CASES literal from part 6", 1)
out['ch19_assemble.py'] = a
f = strip_hdr(open(f'{FD}/ch17_fastcheck.py', encoding='utf-8').read())
f = sub(f, 'ch17', 'ch19'); f = sub(f, "ch16_fastcheck.py's form", "ch17_fastcheck.py's form"); f = sub(f, "parts 1 to 4 exec'd", "parts 1 to 5 exec'd", 1)
f = sub(f, "for n in (2, 3, 4):", "for n in (2, 3, 4, 5):", 1); f = sub(f, "print('fastcheck: part1 fails %d, part2 fails %d, part3 fails %d, part4 fails %d' % tuple(b))", "print('fastcheck: part1 fails %d, part2 fails %d, part3 fails %d, part4 fails %d, part5 fails %d' % tuple(b))", 1)
out['ch19_fastcheck.py'] = f
k = strip_hdr(open(f'{FD}/ch17_askcheck.py', encoding='utf-8').read())
k = sub(k, "['ch17_part2.py', 'ch17_part3.py', 'ch17_part4.py']", "['ch19_part2.py', 'ch19_part3.py', 'ch19_part4.py', 'ch19_part5.py']", 1); k = sub(k, 'ch17', 'ch19'); k = sub(k, "defined in part 4", "defined in part 5", 1)
out['ch19_askcheck.py'] = k
r = open(f'{FD}/ch17_runner_chain.sh', encoding='utf-8').read()
r = sub(r, '15b', '16b'); r = sub(r, 'ch17', 'ch19'); r = sub(r, 'cold_run_courts_prophet.py', 'cold_run_refuge_war_family.py', 1); r = sub(r, "14b's form (ch16_runner_chain.sh)", "15b's form (ch17_runner_chain.sh)", 1)
r = sub(r, '"F1 F2 F3 F4 F5 F6 F7 F8 RB"', '"F1 F2 F3 F4 F5 F6 F7 F8 F9 RB"', 1)
out['ch19_runner_chain.sh'] = r
t = open(f'{FD}/ch17_tape_chain.sh', encoding='utf-8').read()
t = sub(t, '15b', '16b'); t = sub(t, 'ch17', 'ch19'); t = sub(t, '"courts_prophet\\|festivals_judges "', '"refuge_war_family\\|courts_prophet "', 1); t = sub(t, 'CHECKPOINT DI', 'CHECKPOINT DJ', 1)
t = sub(t, 'eight own-day lines', 'thirteen own-day lines', 1); t = sub(t, "14b's form (ch16_tape_chain.sh)", "15b's form (ch17_tape_chain.sh)", 1); t = sub(t, 'DI1-DI5', 'DJ1-DJ5')
out['ch19_tape_chain.sh'] = t
b = open(f'{FD}/ch17_build_chain.sh', encoding='utf-8').read()
b = sub(b, '15b', '16b'); b = sub(b, 'ch17', 'ch19')
b = sub(b, "derive the runner's part 1 (the helpers from the chapter-16 runner, the ink blocks from ch19_ink.py, the scans, the callees' facts)", "derive the runner's part 1 (the helpers from the chapter 17-18 runner, the ink blocks from ch19_ink.py, the scans, the callees' facts)", 1)
b = sub(b, "the fast checker (parts 1-3)", "the fast checker (parts 1-5)", 1); b = sub(b, "the fast checker, parts 1-4 (ch19_fastcheck.py)", "the fast checker, parts 1-5 (ch19_fastcheck.py)", 1)
b = sub(b, "'fails 0, part2 fails 0, part3 fails 0, part4 fails 0'", "'fails 0, part2 fails 0, part3 fails 0, part4 fails 0, part5 fails 0'", 1)
b = sub(b, "every ask called (ch19_askcheck.py — the eight cells and the table with the DATA rows)", "every ask called (ch19_askcheck.py — the nine cells and the table with the DATA rows)", 1)
b = sub(b, "ch19_askcheck.py ch19_part2.py ch19_part3.py ch19_part4.py", "ch19_askcheck.py ch19_part2.py ch19_part3.py ch19_part4.py ch19_part5.py", 1)
out['ch19_build_chain.sh'] = b
g = open(f'{FD}/ch17b_gates.sh', encoding='utf-8').read()
g = sub(g, '15b', '16b'); g = sub(g, 'ch17', 'ch19'); g = sub(g, "ch16b_gates.sh's form", "ch17b_gates.sh's form", 1)
out['ch19b_gates.sh'] = g
sc = strip_hdr(open(f'{FD}/ch17_scan_census.py', encoding='utf-8').read())   # the header stripped (the first derive kept it: ROOT resolved to the scratchpad's grandparent — read at the census's own error)
i = sc.index("NEW = {'blemished_offering_barred'"); j = sc.index('}\n', i) + 2
NEW45 = "NEW = {'three_cities_separated_commanded', 'way_prepared_commanded', 'land_divided_in_three_commanded', 'three_more_cities_conditioned', 'manslayer_flight_permitted', 'murderer_extradition_commanded', 'murderer_pity_barred', 'innocent_blood_purge_commanded', 'landmark_removal_barred', 'two_or_three_witnesses_required', 'witnesses_inquiry_commanded', 'plotting_witness_talion_commanded', 'talion_pity_barred', 'war_fear_barred', 'priest_war_speech_commanded', 'officers_exemptions_commanded', 'fearful_exemption_commanded', 'captains_appointed_commanded', 'peace_call_commanded', 'tribute_service_commanded', 'siege_males_smitten_commanded', 'spoil_permitted', 'far_cities_scope_declared', 'nothing_alive_left_commanded', 'abominations_teaching_barred', 'fruit_tree_cutting_barred', 'siege_works_permitted', 'slain_found_measuring_commanded', 'heifer_neck_broken_commanded', 'priests_approach_commanded', 'elders_hands_washed_commanded', 'elders_declaration_commanded', 'innocent_blood_atoned', 'captive_wife_permitted', 'captive_mourning_month_commanded', 'captive_sale_barred', 'captive_release_commanded', 'firstborn_double_portion_commanded', 'firstborn_right_transfer_barred', 'rebellious_son_seized_commanded', 'rebellious_son_stoning_commanded', 'hanging_after_death_commanded', 'corpse_overnight_barred', 'same_day_burial_commanded', 'land_defilement_barred'}\n"
sc = sc[:i] + NEW45 + sc[j:]
sc = sub(sc, "THE DEUTERONOMY WALK 15b: THE SCAN CENSUS EXTENDED (14b's lesson 2)", "THE DEUTERONOMY WALK 16b (2026-09-25): THE SCAN CENSUS EXTENDED (14b's lesson 2; 15b's lesson 2 — the tuple-of-substrings form)", 1)
sc = sub(sc, "ch16_scan_census.py's form, extended", "ch17_scan_census.py's form over the forty-five names", 1); sc = sub(sc, "chapters 17-18 present:", "chapters 19-21 present:", 1)
sc = sub(sc, "# THE DEUTERONOMY WALK 15b: the tape's DE4 form", "# THE DEUTERONOMY WALK 15b (kept at 16b): the tape's DE4 form", 1)
out['ch19_scan_census.py'] = sc
for name, text in out.items():
    clean = re.sub(r"ch17_?\w*\.(?:py|sh)", '', text)   # the form citations name 15b's files on purpose
    clean2 = re.sub(r"15b's (?:form|lesson)|WALK 15b \(kept", '', clean)
    assert 'ch17' not in clean and 'courts_prophet.py' not in clean and '15b' not in clean2, (name, [l[:120] for l in clean.split('\n') if 'ch17' in l or '15b' in l][:3])
    open(f'{SP}/{name}', 'w', encoding='utf-8').write(text)
import py_compile
for n in ('ch19_assemble.py', 'ch19_fastcheck.py', 'ch19_askcheck.py', 'ch19_scan_census.py'): py_compile.compile(f'{SP}/{n}', doraise=True)
print('derived:', {k: len(v) for k, v in out.items()}, '— the four python files compile')
