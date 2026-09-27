import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 17b (2026-09-26): the assembler, the fast checker, the ask checker, the runner chain, the tape chain, the tape wrap, the gates shell and
# THE SCAN CENSUS DERIVED from 16b's copies in the forms folder by asserted substitutions (ch19 -> ch22, 16b -> 17b, refuge_war_family -> persons_poor_court, SEVEN typed
# parts and the sixteen cells, DJ -> DK, twenty own-day lines, the seventy-nine names; the portable header made a scratch script's ROOT from git). derive_ch19_shells.py's form.
# RUN FROM THE REPO ROOT.
import subprocess, os, re
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
GIT = "ROOT = _ROOT"
def sub(text, old, new, n=None):
    c = text.count(old); assert c >= 1 and (n is None or c == n), (old[:60], c, n); return text.replace(old, new)
def strip_hdr(t):
    t = re.sub(r"\Aimport os as _os\n_ROOT = _os\.path\.normpath\([^\n]*\n", "", t, count=1)   # the copier's header at the file's head alone (the fast checker names the runner's own header in its body — left)
    return sub(t, "ROOT = _ROOT", GIT, 1)
OWN79 = ['lost_thing_return_commanded', 'hiding_from_lost_thing_barred', 'fallen_beast_raising_commanded', 'cross_dressing_barred', 'mother_bird_sending_commanded', 'parapet_commanded', 'house_bloodguilt_barred', 'vineyard_mixed_seed_barred', 'ox_ass_plowing_barred', 'wool_linen_barred', 'tassels_commanded', 'slander_fine_commanded', 'slanderer_divorce_barred', 'unchaste_bride_stoning_commanded', 'adulterers_death_commanded', 'betrothed_girl_city_field_declared', 'rapist_fifty_commanded', 'rapist_divorce_barred', 'fathers_wife_barred', 'crushed_barred_from_assembly', 'forbidden_union_offspring_barred', 'ammon_moab_barred_forever', 'ammon_moab_peace_barred', 'edom_egypt_third_generation_admitted', 'camp_evil_thing_guarded', 'nocturnal_unclean_exit_commanded', 'camp_latrine_commanded', 'camp_holiness_required', 'escaped_slave_return_barred', 'slave_oppression_barred', 'cult_prostitution_barred', 'harlots_hire_dogs_price_barred', 'interest_to_brother_barred', 'interest_to_foreigner_permitted', 'vow_delay_barred', 'vow_refraining_permitted', 'lips_utterance_binding', 'laborer_eating_permitted', 'laborer_vessel_barred', 'sickle_swinging_barred', 'bill_of_divorce_commanded', 'divorced_wife_remarriage_permitted', 'first_husband_retaking_barred', 'land_caused_to_sin_barred', 'newlywed_year_exemption_commanded', 'millstone_pledge_barred', 'kidnapper_death_commanded', 'leprosy_priests_teaching_commanded', 'miriam_remembrance_commanded', 'pledge_entry_barred', 'poor_mans_pledge_return_commanded', 'righteousness_before_the_lord', 'hireling_oppression_barred', 'hireling_wage_same_day_commanded', 'fathers_for_sons_death_barred', 'stranger_orphan_justice_commanded', 'widows_garment_pledge_barred', 'forgotten_sheaf_commanded', 'olive_second_beating_barred', 'vineyard_gleaning_barred', 'court_justification_commanded', 'lashes_by_number_commanded', 'lashes_forty_cap_declared', 'brother_degradation_barred', 'ox_muzzling_barred', 'widow_outsider_marriage_barred', 'levirate_marriage_commanded', 'firstborn_on_dead_name_commanded', 'refusal_at_gate_declared', 'shoe_loosening_rite_declared', 'house_of_unshod_named', 'wife_seizing_hand_cut_commanded', 'hand_cutting_pity_barred', 'diverse_weights_barred', 'diverse_measures_barred', 'whole_just_weight_commanded', 'amalek_remembrance_commanded', 'amalek_memory_blotting_commanded', 'amalek_forgetting_barred']
assert len(OWN79) == 79 and len(set(OWN79)) == 79
CELLS16 = '"F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 F14 F15 F16 RB"'
out = {}
a = strip_hdr(open(f'{FD}/ch19_assemble.py', encoding='utf-8').read())
a = sub(a, 'cold_run_refuge_war_family.py', 'cold_run_persons_poor_court.py'); a = sub(a, 'ch19', 'ch22'); a = sub(a, "ch17_assemble.py's form", "ch19_assemble.py's form")
a = sub(a, "for n in (1, 2, 3, 4, 5)]", "for n in (1, 2, 3, 4, 5, 6, 7)]", 1); a = sub(a, "p5 = f'{SP}/ch22_part6.py'", "p5 = f'{SP}/ch22_part8.py'", 1)   # the lean runner over four chapters: SEVEN typed parts (part 1 derived; the cells four to a part in 2-5; the readback and the data in 6; the daemon, the lines and the narrative in 7) + the generated cases (part 8)
a = sub(a, "the CASES literal from part 6", "the CASES literal from part 8", 1)
out['ch22_assemble.py'] = a
f = strip_hdr(open(f'{FD}/ch19_fastcheck.py', encoding='utf-8').read())
f = sub(f, 'ch19', 'ch22'); f = sub(f, "ch17_fastcheck.py's form", "ch19_fastcheck.py's form"); f = sub(f, "parts 1 to 5 exec'd", "parts 1 to 7 exec'd", 1)
f = sub(f, "for n in (2, 3, 4, 5):", "for n in (2, 3, 4, 5, 6, 7):", 1); f = sub(f, "print('fastcheck: part1 fails %d, part2 fails %d, part3 fails %d, part4 fails %d, part5 fails %d' % tuple(b))", "print('fastcheck: part1 fails %d, part2 fails %d, part3 fails %d, part4 fails %d, part5 fails %d, part6 fails %d, part7 fails %d' % tuple(b))", 1)
out['ch22_fastcheck.py'] = f
k = strip_hdr(open(f'{FD}/ch19_askcheck.py', encoding='utf-8').read())
k = sub(k, "['ch19_part2.py', 'ch19_part3.py', 'ch19_part4.py', 'ch19_part5.py']", "['ch22_part2.py', 'ch22_part3.py', 'ch22_part4.py', 'ch22_part5.py', 'ch22_part6.py', 'ch22_part7.py']", 1); k = sub(k, 'ch19', 'ch22'); k = sub(k, "defined in part 5", "defined in part 6", 1)
out['ch22_askcheck.py'] = k
r = open(f'{FD}/ch19_runner_chain.sh', encoding='utf-8').read()
r = sub(r, '16b', '17b'); r = sub(r, 'ch19', 'ch22'); r = sub(r, 'cold_run_refuge_war_family.py', 'cold_run_persons_poor_court.py', 1); r = sub(r, "15b's form (ch17_runner_chain.sh)", "16b's form (ch19_runner_chain.sh)", 1)
r = sub(r, '"F1 F2 F3 F4 F5 F6 F7 F8 F9 RB"', CELLS16, 1)
out['ch22_runner_chain.sh'] = r
t = open(f'{FD}/ch19_tape_chain.sh', encoding='utf-8').read()
t = sub(t, '16b', '17b'); t = sub(t, 'ch19', 'ch22'); t = sub(t, '"refuge_war_family\\|courts_prophet "', '"persons_poor_court\\|refuge_war_family "', 1); t = sub(t, 'CHECKPOINT DJ', 'CHECKPOINT DK', 1)
t = sub(t, 'thirteen own-day lines', 'twenty own-day lines', 1); t = sub(t, "15b's form (ch17_tape_chain.sh)", "16b's form (ch19_tape_chain.sh)", 1); t = sub(t, 'DJ1-DJ5', 'DK1-DK5')
out['ch22_tape_chain.sh'] = t
w = open(f'{FD}/ch19_tape_wrap.sh', encoding='utf-8').read()
w = sub(w, '16b', '17b'); w = sub(w, 'ch19', 'ch22'); w = sub(w, 'cold_run_refuge_war_family.py', 'cold_run_persons_poor_court.py', 1); w = sub(w, "ch17_tape_wrap.sh's form", "ch19_tape_wrap.sh's form", 1)
w = sub(w, '"F1 F2 F3 F4 F5 F6 F7 F8 F9 RB"', CELLS16, 1); w = sub(w, 'DJ1-DJ5', 'DK1-DK5')
out['ch22_tape_wrap.sh'] = w
g = open(f'{FD}/ch19b_gates.sh', encoding='utf-8').read()
g = sub(g, '16b', '17b'); g = sub(g, 'ch19', 'ch22'); g = sub(g, "ch17b_gates.sh's form", "ch19b_gates.sh's form", 1)
out['ch22b_gates.sh'] = g
sc = strip_hdr(open(f'{FD}/ch19_scan_census.py', encoding='utf-8').read())
i = sc.index("NEW = {'three_cities_separated_commanded'"); j = sc.index('}\n', i) + 2
sc = sc[:i] + 'NEW = ' + repr(set(OWN79)).replace('{', '{', 1) + '\n' + sc[j:]
sc = sub(sc, "THE DEUTERONOMY WALK 16b (2026-09-25): THE SCAN CENSUS EXTENDED (14b's lesson 2; 15b's lesson 2 — the tuple-of-substrings form)", "THE DEUTERONOMY WALK 17b (2026-09-26): THE SCAN CENSUS EXTENDED (14b's lesson 2; 15b's lesson 2 — the tuple-of-substrings form; 16b's B2 — the named patterns)", 1)
sc = sub(sc, "ch17_scan_census.py's form over the forty-five names", "ch19_scan_census.py's form over the seventy-nine names", 1); sc = sub(sc, "chapters 19-21 present:", "chapters 22-25 present:", 1)
sc = sub(sc, "# THE DEUTERONOMY WALK 16b: the forms copy's portable header stripped", "# THE DEUTERONOMY WALK 16b (kept at 17b): the forms copy's portable header stripped", 1)
out['ch22_scan_census.py'] = sc
for name, text in out.items():
    clean = re.sub(r"ch19_?\w*\.(?:py|sh)", '', text)   # the form citations name 16b's files on purpose
    clean2 = re.sub(r"16b's (?:form|lesson|B2)|WALK 16b \(kept|16b's exactly", '', clean)
    left = [l[:140] for l in clean.split('\n') if 'ch19' in l or 'refuge_war_family.py' in l or (name != 'ch22_scan_census.py' and '16b' in re.sub(r"16b's (?:form|lesson|B2)|WALK 16b \(kept|16b's exactly", '', l))]   # the census's comments name 16b's lessons and findings on purpose
    assert not left, (name, left[:3])
    open(f'{SP}/{name}', 'w', encoding='utf-8').write(text)
import py_compile
for n in ('ch22_assemble.py', 'ch22_fastcheck.py', 'ch22_askcheck.py', 'ch22_scan_census.py'): py_compile.compile(f'{SP}/{n}', doraise=True)
print('derived:', {k: len(v) for k, v in out.items()}, '— the four python files compile; the census NEW set', len(re.search(r"NEW = (\{.*?\})\n", out['ch22_scan_census.py'], re.S).group(1).split("', '")), 'names')
