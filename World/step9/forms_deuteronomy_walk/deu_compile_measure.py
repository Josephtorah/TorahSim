#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 1b — THE COMPILE OF THE OPENING SPEECH (2026-09-15; the owner: "Go 1b right", then "Yes 1. Go" on the readback's
# first form): THE MEASUREMENTS, computed BEFORE the design paragraph is typed (ref_compile_measure.py's form; every call typed from
# deu_compile_recon.out). (1) the parser at the fraction seats; (2) THE TAPE'S STATE — the counter, THE ENTRIES THE SPEECH RETELLS on the running
# world (the readback's first specimens: the oath, Hormah, Edom, Sihon, Og, the grants, the condition, the commission, Moses barred, Caleb, the
# court, the spies), israel_people's commanded entries (the global counts), THE PENDING TIMERS and their dues (the date marker (40, 11, 1) would
# cross them); (3) the callees live; (4) the installation forms and the global-count checkpoints; (5) THE REGISTER GATE on Deuteronomy 1-3;
# (6) the recorder and the stitcher; (7) the engine's marker and close interface.
import sqlite3, sys, io, re, contextlib, collections, inspect, os, yaml, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import world_engine as WE
    import cold_run_exodus_story as ES
    import cold_run_shelach as SL
    import cold_run_chukat as CK
    import cold_run_gad_reuben as GR
    import cold_run_zelophehad as ZL
    import cold_run_journeys as JO
    import cold_run_borders as BO
    import cold_run_second_census as C2
    import cold_run_balak as BK
    import cold_run_primeval as PR
    import cold_run_mamre as MA
    import cold_run_joseph as JS
    import cold_run_ordinances as OR
    import cold_run_holiness as HO
    import cold_run_erection as ER
    import cold_run_bamidbar as CB
    import cold_run_beha as BH
    import cold_run_refuge as RF
    import register_census as RG
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))

print('==== (1) THE PARSER AT THE FRACTION SEATS ====')
for k in (('Deut', 3, 12), ('Deut', 3, 13), ('Num', 32, 33), ('Num', 34, 13), ('Num', 34, 14), ('Num', 34, 15), ('Josh', 13, 7), ('Josh', 14, 2), ('Josh', 14, 3), ('Josh', 4, 12), ('Josh', 22, 7), ('1Chr', 5, 18), ('1Chr', 12, 38), ('Exod', 25, 10), ('Exod', 30, 13), ('Num', 15, 9), ('Deut', 29, 7)):
    vw = CS.verse_words(*k); print('  %s %d:%d numbers %s ordinals %s marked %s' % (k[0], k[1], k[2], CS.ink_numbers(vw), CS.ink_ordinals(vw), [t for t in vw if re.search(r'[#^~%@|*]', t)]))

print('\n==== (2) THE TAPE\'S STATE — the running world ====')
with contextlib.redirect_stdout(io.StringIO()):
    w = RG.running_world()
ex = w.clock.eras['exodus']
def dt(d):
    try: return ex.date(d)
    except BaseException: return ('pre-exodus day', d)
print('  the counter: day %d = %s (exodus era); entities %d; log lines %d; timers pending %d' % (w.clock.day, ex.date(w.clock.day), len(w.entities), len(w.log), len(w.timers)))
print('  (40, 11, 1) = day %d; (40, 6, 1) = day %d; (2, 5, 9) = day %d; (40, 1, 1) = day %d; (40, 5, 1) = day %d; (41, 1, 10) = day %d' % (w.clock.day_in('exodus', 40, 11, 1), w.clock.day_in('exodus', 40, 6, 1), w.clock.day_in('exodus', 2, 5, 9), w.clock.day_in('exodus', 40, 1, 1), w.clock.day_in('exodus', 40, 5, 1), w.clock.day_in('exodus', 41, 1, 10)))
EVs = [l for l in w.log if l[0] == 'EVENT']
print('  events %d; the last five kinds: %s' % (len(EVs), [(l[2]['kind'], str(l[2].get('case_source', ''))[:30], dt(l[1])) for l in EVs[-5:]]))
mk = [l for l in w.log if l[0] == 'MARKER']
print('  markers %d; the last three: %s' % (len(mk), [(l[2].get('verse'), dt(l[1]), l[2].get('placement')) for l in mk[-3:]]))
print('  THE PENDING TIMERS (subject, effect/value, due day = date, period): ')
TL = w.timers if isinstance(w.timers, list) else list(w.timers)
for t in TL:
    if isinstance(t, dict):
        print('     %s' % {k: (dt(v) if k in ('due', 'at', 'day') and isinstance(v, int) else str(v)[:80]) for k, v in t.items()})
    else:
        print('     %s' % str(t)[:300])
print('  the timer log classes: %s' % dict(collections.Counter(l[0] for l in w.log if l[0].startswith('TIMER'))))
tset = [l for l in w.log if l[0] == 'TIMER-SET']
print('  TIMER-SET lines with a period (recurring): %s' % [(str(l[2])[:200]) for l in tset if 'period' in str(l[2])][:12])
print('  the last five TIMER-SET lines: %s' % [str(l[2])[:200] for l in tset[-5:]])
reg_map = CS.registry_map()
def ent(t): return w.entities.get(reg_map.get(t, t))
def show(t, n=200, only=None):
    e = ent(t)
    if e is None: print('  %-28s NO ENTITY on the running world (registry id %s)' % (t, reg_map.get(t))); return
    print('  %-28s id %-26s kind %-8s ledger %3d; OPEN %d' % (t, e.eid, getattr(e, 'kind', '?'), len(e.ledger), sum(1 for x in e.ledger if x.get('open'))))
    for x in e.ledger[:n]:
        if only and not re.search(only, str(x.get('effect')) + ' ' + str(x.get('value')) + ' ' + str(x.get('case_source'))): continue
        print('     %-34s %-70s op %-8s open %-5s cp %-24s day %-16s src %s' % (x['effect'], str(x.get('value'))[:70], x.get('op'), x.get('open'), str(x.get('cp'))[:24], dt(x.get('day')), str(x.get('case_source', ''))[:40]))
for t in ('moses', 'joshua', 'caleb', 'aaron', 'eleazar', 'edom', 'esau', 'moab', 'lot', 'sihon', 'og', 'the-amorite', 'the-sons-of-gad', 'the-sons-of-reuben', 'the-half-tribe-of-manasseh', 'the-sons-of-gad-and-reuben', 'jair', 'the-sons-of-machir', 'the-officers', 'the-court', 'the-twelve-spies', 'the-ten-spies', 'the-men-of-war', 'the-land-of-canaan', 'jethro', 'the-dividers-of-the-land', 'hormah', 'the-tabernacle', 'the-tent-of-meeting', 'the-camp', 'the-priesthood', 'the-levites'):
    show(t)
isr = ent('israel')
print('  israel_people ledger %d entries; by effect: %s' % (len(isr.ledger), collections.Counter(x['effect'] for x in isr.ledger).most_common(60)))
show('israel', only=r'Num 1[34]:|Num 20:|Num 21:|Num 32:|Num 33:5|Exod 18:|decree|oath|forty|wander|carcass|hormah|defeated|smitten|refused|highway|plea|possessed|land_|holding|commanded|dispossess|presence|barred|hard_cases|court')
cmd = [x for x in isr.ledger if x['effect'] == 'commanded']
print('  israel_people commanded entries %d (CV2\'s kin): %s' % (len(cmd), [(str(x.get('value'))[:44], x.get('open'), str(x.get('case_source', ''))[:14]) for x in cmd]))
print('  israel_people OPEN commanded entries %d (CX2\'s kin): %s' % (sum(1 for x in cmd if x.get('open')), [str(x.get('value'))[:44] for x in cmd if x.get('open')]))
print('  israel_people OPEN entries (all effects): %s' % [(x['effect'], str(x.get('value'))[:40], x.get('cp'), str(x.get('case_source', ''))[:20]) for x in isr.ledger if x.get('open')])
print('  ENTRIES ANYWHERE naming Deut / forty years / the oath / the decree / spies / Hormah / Edom / Sihon / Og / Gilead / Bashan / Joshua / Caleb / barred (effect, value, op, open, source):')
for e_ in w.entities.values():
    for x in e_.ledger:
        s = str(x.get('effect')) + ' ' + str(x.get('value')) + ' ' + str(x.get('case_source'))
        if re.search(r'Deut|forty years|oath|decree|spies|Hormah|hormah|Edom|edom|Sihon|sihon|\bOg\b|Gilead|Bashan|Joshua|joshua|Caleb|caleb|barred|judges|court', s):
            print('     %-28s %-30s %-70s %-8s %-5s %s' % (e_.eid, x['effect'], str(x.get('value'))[:70], x.get('op'), x.get('open'), str(x.get('case_source', ''))[:36]))
print('  the entities whose id names edom|esau|moab|ammon|lot|sihon|og|amor|gad|reuben|manasseh|jair|machir|judge|officer|court|spies|joshua|caleb|jethro|amalek|hormah|kadesh|seir: %s' % sorted(k for k in w.entities if re.search(r'edom|esau|moab|ammon|^lot|sihon|^og$|amor|gad|reuben|manasseh|jair|machir|judge|officer|court|spies|yehoshua|joshua|caleb|jethro|yitro|amalek|hormah|kadesh|seir', k)))
print('  the institution entities on the world and their in_force: %s' % [(k, [(x['effect'], str(x.get('value'))[:40], x.get('open')) for x in e.ledger if x['effect'] in ('in_force', 'rule_installed')][:6]) for k, e in w.entities.items() if getattr(e, 'kind', '') == 'institution'])
pop = w.population(level='tribe')
print('  population rows (level tribe) %d; gad / reuben / manasseh rows: %s' % (len(pop), [(r.get('tribe'), r.get('as_of'), r.get('count')) for r in pop if r.get('tribe') in ('gad', 'reuben', 'manasseh', 'half-manasseh', 'the-half-tribe-of-manasseh')]))
try:
    named = w.population(level='named')
    print('  population rows (named) %d; joshua / caleb / eleazar rows: %s' % (len(named), [(r.get('subject'), r.get('as_of'), r.get('status'), r.get('tribe')) for r in named if str(r.get('subject')) in ('yehoshua', 'caleb', 'eleazar_son_of_aaron', 'moses')]))
except BaseException as e:
    print('  population(named) raised', type(e).__name__, str(e)[:120])
inst = w.installation
print('  installation: setting %s; skipped %s; would_skip %s' % (inst['setting'] if inst else None, inst['skipped'] if inst else None, inst['would_skip'] if inst else None))
print('  log classes: %s' % dict(collections.Counter(l[0] for l in w.log)))
rows_cnt = sum(1 for l in w.log if l[0] == 'ROW')
print('  ROW lines %d (CP1\'s kin — the population table)' % rows_cnt)
closes = [l for l in w.log if l[0] == 'CLOSE']
print('  CLOSE lines %d; the last three: %s' % (len(closes), [str(l[2])[:160] for l in closes[-3:]]))

print('\n==== (3) THE CALLEES ON FILE, live (every call typed from the recon\'s asks) ====')
def sig(mod, name):
    src = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    return [l.strip()[:160] for l in src.split('\n') if l.startswith('def %s(' % name)]
def tryc(label, f):
    try:
        r = f(); print('  ', label, '->', str(r)[:900])
    except BaseException as e:
        print('  ', label, 'raised', type(e).__name__, str(e)[:200])
for mod, name in ((ES, 'jethro'), (ES, 'manna'), (ES, 'trials'), (ES, 'sinai'), (ES, 'cell'), (SL, 'spies'), (SL, 'decree'), (CK, 'edom_and_hor'), (CK, 'well_and_kings'), (CK, 'meribah'), (GR, 'the_rebuke'), (GR, 'the_grant'), (ZL, 'the_daughters'), (JO, 'aarons_death_retold'), (BO, 'moses_restatement'), (C2, 'the_rolls'), (BK, 'peor'), (PR, 'war'), (PR, 'cell'), (MA, 'sodom'), (MA, 'cell'), (JS, 'edom'), (JS, 'esau_met'), (JS, 'cell'), (OR, 'courts'), (OR, 'cell'), (HO, 'conduct'), (HO, 'cell'), (ER, 'presence'), (ER, 'covenant'), (ER, 'cell'), (CB, 'census'), (BH, 'march'), (BH, 'seventy_elders'), (RF, 'the_refuge_law')):
    print('  signature %s.%s: %s' % (mod.__name__, name, sig(mod, name)))
def call(mod, fn, q):
    f = getattr(mod, fn)
    src = sig(mod, fn)[0] if sig(mod, fn) else ''
    if re.match(r'def \w+\(q\b', src) or re.match(r'def \w+\(ask\b', src): return f(q)
    if re.match(r'def \w+\(case, data', src): return f({'ask': q}, mod.DATA)[:2]
    if re.match(r'def \w+\(case\b', src): return f({'ask': q})
    return f(q)
for mod, fn, qs in ((ES, 'jethro', ['denominations', 'hard_cases', 'judges', 'sanhedrin_sizes', 'timing']), (ES, 'manna', ['forty_years']), (ES, 'trials', ['ten_list', 'count_by_exodus']), (ES, 'sinai', ['names_count']), (ES, 'amalek', ['weakened_seat', 'blotting']),
                    (SL, 'spies', ['one_per_tribe', 'send_for_yourself', 'joshua_caleb_equal', 'report_answers', 'grasshoppers', 'giants', 'eshcol', 'cluster', 'stronger_than', 'punished_for', 'joshua_name', 'forty_days', 'fourth_order', 'named_after_deeds']),
                    (SL, 'decree', ['set', 'exceptions', 'day_for_year', 'count_from', 'deaths_ceased', 'caleb_entitlement', 'turn_back', 'hormah', 'presumption', 'upon_children', 'plea', 'wilderness_share', 'as_i_live', 'ten_trials', 'due', 'set_edges', 'ability', 'fell_and_rent', 'egypt_will_hear', 'pardon', 'that_night', 'joshua_childless', 'spies_death_mode', 'stones_upward', 'ninth_of_av_reading']),
                    (CK, 'edom_and_hor', ['edom_passage', 'messengers_word', 'two_messages', 'succession', 'death_dates', 'seder_olam_walk', 'moserah', 'aaron_age', 'thirty_days', 'two_mount_hors', 'arad_heard']),
                    (CK, 'well_and_kings', ['zered_date', 'deut3_delta', 'sihon_refused', 'land_east', 'og_lore', 'ammon_border', 'from_his_hand', 'joshua_refrain', 'spy_verb', 'sihon_purified', 'lawgiver', 'arnon_miracle', 'jeremiah_quote', 'parable_tellers', 'book_of_wars']),
                    (CK, 'meribah', ['sentence', 'sin', 'died_for_sin', 'disgrace_written', 'meribah_seats', 'first_meribah_clauses']),
                    (CK, 'arad_and_the_serpent', ['hormah', 'turn_back', 'cherem_law']),
                    (GR, 'the_rebuke', ['brood', 'brothers_to_war', 'caleb_the_kenizzite', 'calebs_hebron', 'evil_formula', 'forty_years', 'generation_consumed', 'hinder_root', 'joshua_nothing_owed', 'made_them_wander', 'slow_to_anger', 'the_exceptions', 'the_oath_supplied', 'the_set', 'the_spies_verb', 'the_threat', 'two_of_six_hundred_thousand']),
                    (GR, 'the_offer', ['joshuas_armed', 'we_will_arm', 'not_return']), (GR, 'the_condition', ['positive_arm', 'negative_arm', 'the_scope', 'four_limbs', 'the_clearance', 'the_verb_future']), (GR, 'the_acceptance_and_the_charge', ['the_commission', 'the_lords_word', 'servants_will_do']),
                    (GR, 'the_grant', ['bequeath_not_inherit', 'half_manassehs_stipulation', 'land_held', 'not_by_lot', 'the_count', 'three_parties', 'two_kingdoms']), (GR, 'the_cities', ['two_crossed', 'the_split', 'moses_grave', 'dibon_gad']), (GR, 'machir_jair_nobah', ['gilead_given', 'jair', 'jairs_lineage', 'nobah', 'sons_of_machir', 'survivors']),
                    (ZL, 'the_daughters', ['the_case', 'halt', 'the_run', 'identity', 'section_on_high', 'counsel']), (ZL, 'inheritance_order', ['source_of_rule', 'land_status']),
                    (JO, 'aarons_death_retold', ['verbal_analogy', 'the_era_new_year', 'the_date', 'moses_seventh_adar', 'the_eras_stamps', 'the_order', 'no_write']), (JO, 'the_stations', ['kadesh_hor', 'chapter_21', 'the_last_camp', 'forty_two', 'moseroth_seven', 'rithmah_paran']), (JO, 'the_command', ['when_you_pass', 'the_lot_restated']),
                    (BO, 'moses_restatement', ['joshuas_receipt', 'one_tribe_noun', 'the_count', 'the_grant_read', 'the_lot_by_call', 'the_nine_and_a_half', 'the_pair', 'the_relay']), (BO, 'the_four_sides', ['the_east', 'the_jordan_as_border', 'chinnereth', 'the_spies_walked_it', 'the_three_lands', 'the_promised_extents']),
                    (C2, 'the_rolls', ['except_caleb_joshua', 'decree_consumed', 'membership_predicate', 'age_edges', 'levi_outside']), (C2, 'the_land', ['by_lot', 'land_divided_among', 'spies_portions', 'thirteen_tribes']), (C2, 'the_command', ['exodus_generation', 'after_the_plague']),
                    (BK, 'the_call', ['last_camp']), (BK, 'peor', ['judges_count', 'shittim_name', 'spec_run']), (BK, 'phinehas_and_midian', ['midian_not_moab', 'harass_root']),
                    (PR, 'war', ['og', 'annal', 'raised_hand']), (PR, 'nations', ['cities_four', 'amraphel']), (PR, 'call', ['land_seats', 'go_receipt']), (PR, 'pieces', ['ten_nations', 'fourth_generation', 'four_hundred']),
                    (MA, 'sodom', ['two_peoples_named', 'daughters_two_nights']), (MA, 'blessing', ['esau_blessing_clauses']), (MA, 'grudge', ['exile_table']),
                    (JS, 'edom', ['kings_count', 'parted_for_room', 'timna_amalek', 'kings_named', 'holding_homograph']), (JS, 'esau_met', ['seir_promised', 'widen_the_road']),
                    (OR, 'courts', ['bribe', 'asymmetry', 'one_vs_two', 'twenty_three', 'poor_not_glorified', 'needy_in_his_cause', 'keep_far', 'majority_hapax', 'measure', 'onkelos_teaching']), (OR, 'land', ['angel', 'borders', 'little_by_little', 'hornet']),
                    (HO, 'conduct', ['no_favor', 'equal_treatment', 'judge_is_measurer', 'bribe', 'great_rule', 'protocol', 'five_effects']),
                    (ER, 'presence', ['horev_plene', 'ruling_distance', 'sheet_avot_1_1', 'tent_outside']), (ER, 'covenant', ['nations_seven_orders']), (ER, 'ascent', ['forty']),
                    (CB, 'census', ['total', 'orders', 'three_seats']), (CB, 'camp', ['sides', 'march']),
                    (BH, 'march', ['date', 'three_days', 'spy_verb', 'hobab', 'jethro_at_sinai', 'year_turns', 'eighty_five']), (BH, 'seventy_elders', ['sanhedrin', 'count_when', 'elder_means']),
                    (RF, 'the_refuge_law', ['six_cities', 'the_debit']), (RF, 'the_manslayer', ['the_term'])):
    for q in qs:
        tryc('%s.%s(%s)' % (mod.__name__.replace('cold_run_', ''), fn, q), lambda mod=mod, fn=fn, q=q: call(mod, fn, q))
for mod, keys in ((SL, ['count_from', 'deaths_ceased', 'the_ten_trials', 'spies_share', 'wilderness_share', 'return_day', 'tammuz_length']), (CK, ['edom_passage', 'moserah', 'succession_by', 'meribah_sin', 'og_lore', 'deaths_ceased', 'sihon_purified', 'spy_verb', 'ammon_border', 'captive_count']), (GR, ['caleb_the_kenizzite', 'count_from', 'deaths_ceased', 'the_oath_supplied', 'the_land_east_status', 'jair_and_machir_survived', 'jairs_lineage', 'the_forty_thousand', 'moses_grave', 'the_conditions_four_limbs', 'the_clearance', 'negative_arm_outcome', 'half_manassehs_stipulation']), (JO, ['the_deuteronomy_order', 'the_eras_stamps', 'the_death_date', 'aarons_age', 'the_stations']), (BO, ['the_nine_and_a_half', 'the_relay_form', 'the_jordan_as_border', 'the_three_lands', 'the_promised_extents']), (C2, ['decree_age_edges', 'wilderness_survivors', 'spies_protesters_portions', 'urim_judgment']), (BH, ['spies_sent_day', 'sanhedrin_size', 'jethro_at_sinai', 'seven_clouds']), (BK, ['judges_count' if False else 'shittim_name', 'midian_command_run']), (ZL, ['eretz_yisrael_status', 'tribe_transfer_reach', 'land_divided_among'])):
    for k in keys:
        if hasattr(mod, 'DATA') and k in mod.DATA: print('  %s.DATA[%s] = %s' % (mod.__name__.replace('cold_run_', ''), k, str(mod.DATA[k])[:600]))
for name in ('AARON_DATE', 'AARON_AGE', 'MOSES_120', 'SHEVAT_DATE', 'PLACES_EN', 'STATIONS', 'CAMPS'):
    for mod in (CK, JO, CB):
        if hasattr(mod, name): print('  %s.%s = %s' % (mod.__name__.replace('cold_run_', ''), name, str(getattr(mod, name))[:400]))
src_es = open(inspect.getsourcefile(ES), encoding='utf-8').read()
print('  ES lines naming 78,600 / Sanhedrin 10:2 / denominations: %s' % [l.strip()[:260] for l in src_es.split('\n') if re.search(r'78,?600|Sanhedrin 10:2|denominations', l)][:8])

print('\n==== (4) THE INSTALLATION FORMS AND THE GLOBAL-COUNT CHECKPOINTS (grepped BEFORE the tape run) ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
for pat in (r"len\(cmd_v\)", r"isr_cmd", r"len\(w\.entities\)", r"closes_done", r"'commanded'", r"barred_from_the_land", r"yehoshua", r"'caleb'", r"holding_given", r"presence_dwells", r"in_force", r"population\(", r"len\(w\.log\)", r"len\(mk\)|markers", r"w\.timers", r"defeated|hormah", r"the_court|courts_established|hard_cases"):
    hits = [l.strip()[:200] for l in src_cs.split('\n') if re.search(pat, l) and ('cp(' in l or re.search(r"^\s*[a-z_0-9]+ = \[", l.strip()))]
    print('  %-28s %d lines: %s' % (pat, len(hits), hits[:8]))
for lab in ('CV2', 'CX2', 'CW3', 'CZ2', 'CR2', 'CR3', 'CP1', 'CW1', 'CR1', 'CR9', 'CT2', 'CT9', 'CV9', 'CX9', 'CY2', 'CY9', 'CZ9', 'CW9', 'CK1', 'CK2', 'CF9', 'CE1', 'CG9'):
    print('  the %s line whole: %s' % (lab, [l.strip()[:700] for l in src_cs.split('\n') if "cp('%s" % lab in l][:1]))
print('  the lines defining cmd_v / isr_cmd lists: %s' % [l.strip()[:220] for l in src_cs.split('\n') if re.search(r"^\s*(cmd_v|isr_cmd|dv_cmd|cal_owed|ev_bo) = ", l)][:12])
print('  the lines between "# ---- Num 35 ----" and "# ==== TAPE END": %s' % [l.strip()[:120] for l in src_cs[src_cs.find('# ---- Num 35 ----'):src_cs.find('# ==== TAPE END ====')].split('\n')])
print('  the checkpoint block\'s head (def checkpoints): %s' % [(i + 1, l.strip()[:200]) for i, l in enumerate(src_cs.split('\n')) if re.match(r'def checkpoints\(|def checkpoints_partial\(|def run\(|def run_world\(|def rest_world\(|def run_to\(', l)])
i0 = src_cs.find('def checkpoints(')
print('  checkpoints() head 30 lines:\n' + '\n'.join('     ' + l[:200] for l in src_cs[i0:i0 + 4000].split('\n')[:30]))
print('  the VERDICTS list head: %s' % [l.strip()[:200] for l in src_cs.split('\n') if l.startswith('VERDICTS')][:1])
print('  how a marker with a FORWARD date is placed (the Num 20:1 line) and its bound: %s' % [l.strip()[:400] for l in src_cs.split('\n') if "w.marker('Num 20:1'" in l or "w.marker('Num 25:19'" in l][:2])
print('  assert_ink signature and marker(): %s' % [l.strip()[:200] for l in src_cs.split('\n') if l.startswith('def assert_ink(') or l.startswith('def marker(')])
src_we = open(f'{ROOT}/World/step9/world_engine.py', encoding='utf-8').read()
print('  World defs: %s' % re.findall(r'^    def ([a-z_]+)\(', src_we, re.M))
print('  marker / advance / close / submit / set_timer signatures: %s' % [l.strip()[:220] for l in src_we.split('\n') if re.match(r'    def (marker|advance|close|submit|set_timer|cancel_timers|_fire|fire_due|_write|row|entity|dated|retro)\(', l)])
i1 = src_we.find('    def marker(')
print('  marker() body head:\n' + '\n'.join('     ' + l[:200] for l in src_we[i1:i1 + 2600].split('\n')[:34]))
i2 = src_we.find('    def advance(')
print('  advance() body head:\n' + '\n'.join('     ' + l[:200] for l in src_we[i2:i2 + 2600].split('\n')[:34]))
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  law_shelach block whole: %s' % dd['daemons']['law_shelach'])
print('  law_chukat watches: %s' % dd['daemons']['law_chukat'].get('watches'))
print('  law_exodus_story watches for judges_appointed: %s' % dd['daemons']['law_exodus_story'].get('watches', {}).get('judges_appointed'))
print('  register_probes count: %s; census_probes count: %s' % (len(re.findall(r"^def (R\d+|probe_\w+)\(", open(f'{ROOT}/World/step9/register_probes.py', encoding='utf-8').read(), re.M)), len(re.findall(r"^\s*\('[A-Z]+\d+", open(f'{ROOT}/World/step9/census_probes.py', encoding='utf-8').read(), re.M))))
cp_src = open(f'{ROOT}/World/step9/census_probes.py', encoding='utf-8').read()
print('  census_probes: the D1-D9 rows (the form to copy) and the R-row form: %s' % [l.strip()[:220] for l in cp_src.split('\n') if re.match(r"\s*\('D[1-9]'|\s*\('R7[0-3]'", l)][:12])
print('  census_probes head 25: \n' + '\n'.join('     ' + l[:200] for l in cp_src.split('\n')[:25]))

print('\n==== (5) THE REGISTER GATE on Deuteronomy 1-3 (computed on the running world) ====')
ink = RG.read_ink()
cc = RG.class_counts(ink, w)
print('  count lines in Deut 1-3: %s' % [(r, d['class'], d['noun'], d.get('counts'), d.get('measures')) for r, d in cc.items() if re.match(r'Deut [123]:', r)])
cr = RG.class_receipts(ink, w)
print('  receipts in Deut 1-3: %s' % [(r, d['class'], str(d['evidence'])[:300]) for r, d in cr.items() if re.match(r'Deut [123]:', r)])
cf = RG.class_footers(ink)
print('  footers naming Deut: %s' % {k: (v if isinstance(v, dict) else v) for k, v in cf.items() if 'Deut' in k})
try:
    rh = RG.register_headers(ink)
    items = rh.items() if isinstance(rh, dict) else enumerate(rh)
    print('  register headers naming Deut 1-3: %s' % [(k, str(v)[:300]) for k, v in items if re.search(r'Deut [123]:', str(k) + str(v))][:5])
except BaseException as e:
    print('  register_headers raised', type(e).__name__, str(e)[:120])
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the declared seats naming Deut 1-3 (whole): %s' % [(sec, k, decl[sec][k]) for sec in decl for k in (decl[sec] or {}) if re.match(r'Deut [123]:', k)])
src_rg = open(f'{ROOT}/World/step9/register_census.py', encoding='utf-8').read()
print('  register_census: the receipt classes and the footer classes (the green forms): %s' % [l.strip()[:220] for l in src_rg.split('\n') if re.search(r"'(GREEN|CLOSE|DAEMONS|ROWS|MEASURE-ONLY|RUN|EMPTY|NONE|CALL|STALE)'", l)][:30])
print('  register_census defs: %s' % re.findall(r'^def ([a-z_]+)\(', src_rg, re.M))
i3 = src_rg.find('def class_receipts(')
print('  class_receipts() head:\n' + '\n'.join('     ' + l[:220] for l in src_rg[i3:i3 + 5000].split('\n')[:60]))
i4 = src_rg.find('def class_footers(')
print('  class_footers() head:\n' + '\n'.join('     ' + l[:220] for l in src_rg[i4:i4 + 4000].split('\n')[:50]))

print('\n==== (6) THE RECORDER/STITCHER ====')
print('  import lines for the walk\'s runners: %s' % re.findall(r'^import (cold_run_(?:borders|journeys|gad_reuben|midian|refuge|zelophehad))', src_cs, re.M))
SP = os.path.dirname(os.path.abspath(__file__))
for f in ('seq_stitch.py', 'seq_record.py'):
    p = f'{ROOT}/World/step9/forms_numbers_walk/{f}'
    t = open(p, encoding='utf-8').read()
    print('  %s in the forms: SPAN_ORDER tail: %s' % (f, (re.findall(r"SPAN_ORDER\s*=\s*\[([^\]]*)\]", t)[0][-200:] if 'SPAN_ORDER' in t else '')))
    print('    recording path / OUT lines: %s' % [l.strip()[:200] for l in t.split('\n') if re.search(r"seq_recording|OUT =|_ROOT|scratch", l)][:6])
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
print('  the section markers in the tape: %s' % re.findall(r'# ---- ([A-Za-z]+ \d+) ----', tape)[-12:])
print('  cp() checkpoints on file (tail): %s' % re.findall(r"cp\('(C[A-Z]\d)", src_cs)[-12:])
print('  the tape\'s Num 27 lines: %s' % [l.strip()[:200] for l in tape.split('\n') if 'Num 27:' in l][:10])
print('  the tape\'s Num 36 lines and the marker names after Num 27: %s' % [l.strip()[:120] for l in tape.split('\n') if 'Num 36:' in l or ("w.marker(" in l and re.search(r"Num (2[6-9]|3\d):", l))][:10])
