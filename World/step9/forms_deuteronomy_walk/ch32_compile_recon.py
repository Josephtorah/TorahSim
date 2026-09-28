import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (2026-09-28): THE LEAN RECON for the compile of CHAPTER 32 — THE SONG — what the tape, the registries, the dispositions, the probes and the
# running world say BEFORE a line is typed (19b's recon over three chapters, derived for this one chapter by asserted substitutions — derive_ch32_recon.py: no docket scan; the kin's
# cells found by a STATIC scan of every runner's defs for the song's kin verses' refs, no import). Every number printed, never typed. ch29_compile_recon.py's form. RUN FROM THE REPO ROOT.
import os, re, sys, subprocess, io, contextlib, collections, glob
ROOT = _ROOT
sys.path.insert(0, ROOT + '/World/step9')
import yaml
S9 = ROOT + '/World/step9'
print('==== A. THE TAPE (cold_run_sequence.py) ====')
seq = open(S9 + '/cold_run_sequence.py', encoding='utf-8').read(); L = seq.split('\n')
for i, l in enumerate(L, 1):
    if re.match(r'^(RUN|PREVIOUS_RUN|NEWEST_RUNNER|PLACEMENT) = ', l): print('%d: %s' % (i, l[:170]))
print('import lines:', sum(1 for l in L if l.startswith('import cold_run_')), '| DAEMON_ORDER tuples:', len(re.findall(r"^\s+\('cold_run_\w+', 'law_\w+'\)", seq, re.M)))
cps = re.findall(r"cp\('([A-Z]{2}\d+) ", seq); print('checkpoints:', len(cps), '| the D series in use:', sorted({c[:2] for c in cps if c[0] == 'D'}), '| last:', cps[-1])
vl = [l for l in L if "'DM5 MATCH'" in l]; print('VERDICTS DM line:', [l[:200] for l in vl])
print('lines naming Deut 32:', [(i, l[:140]) for i, l in enumerate(L, 1) if re.search(r'Deut 32[:\b]', l)][:20])
print('the last submit lines (the tape\'s newest own-day lines):', [(i, l[:110]) for i, l in enumerate(L, 1) if l.startswith("    w.submit({'kind': '")][-3:])
print('the covenant_return_charge block in the sequence (import line, DAEMON_ORDER tuple, the submits, the marker, the cp lines):', [(i, l[:140]) for i, l in enumerate(L, 1) if 'covenant_return_charge' in l][:16])
print('the marker rows in the sequence naming Deut 31 (19b\'s marker — the song stands on its day):', [(i, l[:160]) for i, l in enumerate(L, 1) if 'marker' in l.lower() and 'Deut 31' in l][:6])
print('the ACT / SPEECH submits in the Deuteronomy stretch (kinds not ending _declared or _commanded, after line 2400):', [(i, re.search(r"'kind': '(\w+)'", l).group(1)) for i, l in enumerate(L, 1) if i > 2400 and l.startswith("    w.submit({'kind': '") and not re.search(r"'kind': '\w+_(declared|commanded)'", l)][:30])
print('marker submits in the Deuteronomy stretch (after line 2400):', [(i, l[:120]) for i, l in enumerate(L, 1) if i > 2400 and 'marker' in l.lower() and 'submit' in l][:12])
print('==== B. THE DISPOSITIONS ====')
dep = yaml.safe_load(open(S9 + '/dependency_dispositions.yaml', encoding='utf-8'))
print('edges', len(dep['edges']), '| pointers', len(dep.get('pointers', [])), '| spans', len(dep['spans']))
print('edges naming Deut 32:', [(e.get('from'), e.get('to'), e.get('disposition'), e.get('link'), str(e.get('why'))[:140]) for e in dep['edges'] if re.search(r'Deut 32:', str(e))][:20])
print('pointers naming Deut 32 or 32:15 or 32:30 or song|witness|Nebo|Meribah:', [(p.get('verse'), p.get('runner'), p.get('disposition'), p.get('link'), str(p.get('why'))[:260]) for p in dep.get('pointers', []) if re.search(r'Deut 32:|\b32:15\b|\b32:30\b|song|witness|Nebo|Meribah|Abarim', str(p))][:14])
print('pointers OWED (all):', [(p.get('verse'), p.get('runner'), str(p.get('why'))[:160]) for p in dep.get('pointers', []) if p.get('disposition') == 'OWED'])
print('pointer dispositions counter:', collections.Counter(p.get('disposition') for p in dep.get('pointers', [])), '| pointer links:', collections.Counter(p.get('link') for p in dep.get('pointers', [])))
print('a pointer entry whole (the first RUN_CITATION of covenant_return_charge):', [p for p in dep.get('pointers', []) if p.get('runner') == 'covenant_return_charge'][:1])
print('the pointers of covenant_return_charge (19b — 29:12, 31:3, 31:4 RUN_CITATION; 30:9 FALSE):', [(p.get('verse'), p.get('disposition'), p.get('link'), str(p.get('why'))[:120]) for p in dep.get('pointers', []) if p.get('runner') == 'covenant_return_charge'])
for sp in ('covenant_return_charge', 'firstfruits_ebal_curses', 'persons_poor_court', 'refuge_war_family', 'not_righteousness', 'shelach', 'mamre', 'flood', 'babel', 'primeval_story', 'exodus_signs', 'manna', 'beha', 'masei', 'refuge_cities', 'release_firstborn', 'festivals_judges', 'courts_prophet', 'opening_speech', 'good_land', 'obey_horeb', 'hear_o_israel', 'blessing_and_curse', 'seven_nations', 'second_tablets', 'tochacha', 'food_tithe', 'seducers', 'place_name', 'calendar', 'moadim', 'exodus_story', 'sinai', 'decalogue', 'pre_sinai', 'primeval', 'family', 'yovel', 'journeys', 'borders', 'balak', 'chukat', 'naso', 'korach', 'pinchas', 'inheritance', 'matot', 'sanctuary_build', 'erection', 'golden_calf', 'covenant_at_horeb', 'refuge_war_family'):
    if sp in dep['spans']: print(' span', sp, ':', dep['spans'].get(sp))
print('ALL span names:', sorted(dep['spans'].keys()))
print('edges from covenant_return_charge (the newest precedent):', [(e['to'], e.get('link'), e.get('disposition'), str(e.get('carries', ''))[:30]) for e in dep['edges'] if e.get('from') == 'covenant_return_charge'])
print('edges from chukat:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'chukat'])
print('edges from exodus_story:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'exodus_story'])
print('edges INTO covenant_return_charge and opening_speech (the callers):', [(e['from'], e['to'], e.get('disposition')) for e in dep['edges'] if e.get('to') in ('covenant_return_charge', 'opening_speech')][:20])
print('edges from opening_speech:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'opening_speech'])
print('edges from obey_horeb:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'obey_horeb'])
print('an edge example (covenant_return_charge -> opening_speech):', [e for e in dep['edges'] if e.get('from') == 'covenant_return_charge' and e.get('to') == 'opening_speech'])
print('an edge example (covenant_return_charge -> a FALSE one):', [e for e in dep['edges'] if e.get('from') == 'covenant_return_charge' and e.get('disposition') == 'FALSE'][:1])
print('an edge example (a VIA one, any runner):', [e for e in dep['edges'] if e.get('disposition') == 'VIA'][:1])
dd = yaml.safe_load(open(S9 + '/daemon_dispositions.yaml', encoding='utf-8'))
print('daemons', len(dd['daemons']), '| functions (runners)', len(dd['functions']), '| law_covenant_return_charge:', dd['daemons'].get('law_covenant_return_charge'))
print('functions covenant_return_charge:', str(dd['functions'].get('covenant_return_charge'))[:900])
for fn in ('covenant_return_charge', 'firstfruits_ebal_curses', 'refuge_war_family', 'not_righteousness', 'chukat', 'shelach', 'mamre', 'flood', 'babel', 'beha', 'masei', 'courts_prophet', 'festivals_judges', 'release_firstborn', 'opening_speech', 'good_land', 'obey_horeb', 'hear_o_israel', 'blessing_and_curse', 'second_tablets', 'tochacha', 'seducers', 'exodus_story', 'sinai', 'decalogue', 'primeval', 'yovel', 'journeys', 'borders', 'pinchas', 'matot', 'chukat', 'naso', 'balak', 'golden_calf', 'erection', 'pre_sinai'):
    if fn in dd['functions']: print(' functions', fn, ':', str(dd['functions'].get(fn))[:400])
print('ALL the Deuteronomy daemons (given_at Deut):', [(n, d.get('given_at'), d.get('installed_by'), d.get('wraps')) for n, d in dd['daemons'].items() if str(d.get('given_at', '')).startswith('Deut')])
rg = yaml.safe_load(open(S9 + '/register_dispositions.yaml', encoding='utf-8'))
print('register keys:', list(rg.keys()))
print('register seats naming Deut 32:', [(sec_name, k, str(sec[k])[:300]) for sec_name, sec in rg.items() if isinstance(sec, dict) for k in sec if re.search(r'\b32:\d|32, \d', str(k) + str(sec[k])) and 'Deut' in (str(k) + str(sec[k]))][:10])
print('==== C. THE PROBES ====')
ip = open(S9 + '/installation_probes.py', encoding='utf-8').read().split('\n')
print('I5 lines:', [(i, l[:200]) for i, l in enumerate(ip, 1) if re.search(r"len\(real\) == \d+", l)][:3])
rp = open(S9 + '/readback_probes.py', encoding='utf-8').read().split('\n')
print('readback defs:', [l[:40] for l in rp if re.match(r'^def q\d+', l)][-3:], '| the Q48 lines:', [(i, l[:160]) for i, l in enumerate(rp, 1) if 'Q48' in l][:8])
print('the PROBES list / registration of q48 (the last lines naming q48 or q47):', [(i, l[:160]) for i, l in enumerate(rp, 1) if re.search(r'\bq4[78]\b', l)][-6:])
print('readback probes asserting the tape\'s last day or the markers count (19b\'s lesson 3 — the classes a marker moves; the song sets NO marker):', [(i, l[:120]) for i, l in enumerate(rp, 1) if re.search(r'\(40, 12, 7\)|markers.*173|173.*markers', l)][:12])
rc = open(S9 + '/register_census.py', encoding='utf-8').read()
print('register_census: lines naming Deut 32 / song / witness / footer:', [(i, l[:160]) for i, l in enumerate(rc.split('\n'), 1) if re.search(r'Deut 32|song|witness|footer', l)][:12])
print('==== D. THE REGISTRIES ====')
fx = yaml.safe_load(open(S9 + '/effect_vocabulary.yaml', encoding='utf-8'))['effects']; ev = yaml.safe_load(open(S9 + '/event_vocabulary.yaml', encoding='utf-8'))['events']
print('effects', len(fx), '| kinds', len(ev), '| effect ops:', collections.Counter(r.get('ledger_op') for r in fx.values()), '| kind forms:', collections.Counter(r.get('form') for r in ev.values()))
NEW_E = ['heavens_and_earth_called_to_hear', 'doctrine_as_rain_and_dew_likened', 'name_of_the_lord_proclaimed_greatness_ascribed', 'the_rock_perfect_and_just_declared', 'generation_crooked_not_his_children', 'father_who_acquired_you_requited', 'days_of_old_remember_commanded', 'nations_bounds_set_by_number_of_israel', 'lords_portion_his_people_jacob', 'found_in_the_desert_encircled_and_kept', 'apple_of_his_eye_kept', 'as_an_eagle_stirring_its_nest_borne', 'the_lord_alone_led_no_foreign_god', 'heights_of_the_land_ridden_honey_from_the_rock', 'jeshurun_fat_kicked_forsook_god', 'demons_and_new_gods_sacrificed', 'face_hidden_end_seen_foretold', 'jealousy_by_no_people_foolish_nation', 'fire_kindled_to_the_lowest_sheol', 'evils_heaped_arrows_spent', 'hunger_beasts_serpents_sword_terror_sent', 'blotting_out_stayed_by_the_enemys_boast', 'nation_void_of_counsel', 'one_chasing_a_thousand_rock_sold_them', 'vine_of_sodom_gall_grapes', 'vengeance_laid_up_in_store_sealed', 'lord_judges_his_people_repents_himself', 'where_are_their_gods_asked', 'i_i_am_he_no_god_beside_me', 'i_kill_and_make_alive_none_delivers', 'hand_lifted_to_heaven_live_forever_sworn', 'sword_whetted_vengeance_rendered', 'nations_sing_with_his_people_land_atones', 'song_spoken_in_the_ears_of_the_people', 'set_your_heart_to_these_words_commanded', 'it_is_your_life_no_empty_matter', 'go_up_to_nebo_see_the_land_commanded', 'die_in_the_mountain_gathered_to_your_people_commanded', 'as_aaron_died_in_hor_and_was_gathered', 'trespassed_at_meribath_kadesh_not_sanctified', 'see_the_land_from_afar_not_go_there']
NEW_K = ['song_witnesses_called_declared', 'song_name_proclaimed_rock_perfect_declared', 'song_crooked_generation_declared', 'song_nations_divided_lords_portion_declared', 'song_found_in_the_desert_declared', 'song_heights_honey_rock_declared', 'song_jeshurun_fat_kicked_declared', 'song_face_hidden_foolish_nation_declared', 'song_evils_heaped_declared', 'song_enemys_boast_declared', 'song_one_chasing_a_thousand_declared', 'song_vengeance_in_store_declared', 'song_i_am_he_declared', 'song_spoken_by_moses_and_hoshea', 'set_your_heart_no_empty_matter_declared', 'nebo_summons_die_as_aaron', 'meribah_trespass_not_go_there_declared']
print('candidate new effects', len(NEW_E), '(distinct', len(set(NEW_E)), ') present before:', [e for e in NEW_E if e in fx], '| candidate kinds', len(NEW_K), 'present before:', [k for k in NEW_K if k in ev])
NEAR = re.compile(r'heaven|earth|rain|dew|rock|perfect|crooked|generation|father|acquir|remember|days_of_old|nation|bound|number|portion|desert|wilderness|apple|eye|eagle|nest|alone|foreign|height|honey|oil|curd|milk|lamb|ram|goat|wheat|grape|wine|jeshurun|fat|kick|forsook|forsak|demon|new_god|jealous|face|hid|fool|fire|sheol|evil|arrow|hunger|beast|serpent|sword|terror|blot|enemy|boast|counsel|thousand|sold|vine|sodom|gomorrah|gall|venom|vengeance|store|judge|repent|servant|kill|alive|wound|heal|hand|live|forever|whet|blood|atone|song|hoshea|joshua|witness|heart|life|empty|prolong|jordan|nebo|abarim|moab|jericho|canaan|aaron|hor\b|gathered|meribah|kadesh|zin\b|sanctif|trespass|afar|die|death|selfsame|command|moses|people|israel|shekhinah|torah|world_to_come|manna|garment|pillar|egypt|sinai|horeb|plague|scatter|babel|flood|noah|adam|tent|cloud|hidden|corrupt|stiff|sated|rebel|whor|other_gods|break|sleep|fathers|inclin|teach|children|book|ark|law|write|wrote')
print('near names (effects):', sorted(e for e in fx if NEAR.search(e)))
print('near names (kinds):', sorted(k for k in ev if NEAR.search(k)))
REUSE = ('heaven_and_earth_witness', 'witnesses_called', 'face_hidden', 'forsaken', 'face_hidden_and_forsaken_foretold', 'future_whoring_after_foreign_gods_foretold', 'covenant_breaking_foretold', 'evils_and_troubles_befall_foretold', 'corruption_after_moses_death_foretold', 'moses_to_sleep_with_the_fathers', 'moses_days_approach_to_die', 'song_writing_commanded', 'song_taught_and_put_in_mouths_commanded', 'song_a_witness_against_israel', 'song_written_and_taught_by_moses', 'song_spoken_to_the_assembly_to_its_end', 'book_a_witness_against_israel', 'song_sung', 'song_taught', 'manna_eaten', 'garments_not_worn_out', 'clothing_not_worn', 'sodom_overthrown', 'brimstone_and_fire_rained', 'land_brimstone_salt_like_sodom', 'moses_barred_from_the_land', 'moses_barred_from_crossing', 'barred_from_the_land', 'jordan_crossing_barred', 'aaron_died', 'aaron_buried', 'aaron_gathered_to_his_people', 'gathered_to_his_people', 'meribah_waters', 'rebelled_at_meribah', 'not_sanctified_at_meribah', 'sanctify_me_failed', 'nations_divided', 'scattered_over_the_earth', 'tongues_confused', 'other_gods_barred', 'stiff_necked', 'stiff_neck_declared', 'anger_kindled', 'fire_kindled', 'sword_without', 'famine', 'pestilence', 'wild_beasts_sent', 'evil_beasts_sent', 'eagles_wings_borne', 'borne_on_eagles_wings', 'treasure_people', 'lord_declared_israel_treasure_people', 'lords_portion', 'apostasy_foretold', 'joshua_commissioned', 'joshua_commissioned_at_tent', 'joshua_commissioned_to_bring_israel_in', 'joshua_appointed', 'hands_laid_on_joshua', 'abarim_ascent_commanded', 'see_the_land_commanded', 'moses_to_see_the_land', 'gathered_to_your_people_commanded', 'staff_cast_became_a_serpent', 'staff_a_serpent', 'first_adam_died', 'death_decreed', 'return_to_dust', 'entered_the_covenant', 'became_the_lords_people_this_day', 'blessing_and_curse_set', 'cleaving_commanded', 'fear_not_promised', 'glory_appeared', 'jealousy_provoked', 'provoked_to_jealousy', 'idols_served', 'demons_sacrificed_to', 'sacrificed_to_demons', 'exiled', 'scattered_among_nations', 'scattered_among_all_peoples', 'few_in_number_left', 'the_land_sworn_to_the_fathers', 'land_sworn', 'length_of_days_on_the_land_promised', 'prolong_days_promised', 'hearken_and_do_commanded', 'children_taught_commanded', 'teach_children_commanded')
for e in REUSE:
    r = fx.get(e); print(' E', e, '|', r['ledger_op'], '|', r['en'][:110], '| corpus', str(r.get('corpus'))[:50]) if r else print(' E', e, 'MISSING')
print('a statute kind row (assembly_and_song_spoken_declared) whole:', ev.get('assembly_and_song_spoken_declared'))
print('an act kind row (song_written_taught) whole:', ev.get('song_written_taught'), '| a speech kind row (song_witness_commanded) whole:', ev.get('song_witness_commanded'))
print('kind rows naming song|sang|sung|spoke|nebo|abarim|died|gathered|aaron|hoshea|witness|heaven|earth|manna|eagle|meribah|serpent|staff (name, form, fields, corpus):', [(k, r.get('form'), r.get('fields'), str(r.get('corpus'))[:40]) for k, r in ev.items() if re.search(r'song|sang|sung|spoke|nebo|abarim|died|gathered|aaron|hoshea|witness|heaven|earth|manna|eagle|meribah|serpent|staff', k)][:50])
print('SPEECH kind rows in Deuteronomy (form speech, corpus deu_):', [(k, r.get('fields')) for k, r in ev.items() if r.get('form') == 'speech' and 'deu_' in str(r.get('corpus'))][:20])
print('an effect row whole (heaven_and_earth_witness):', fx.get('heaven_and_earth_witness'), '| (song_a_witness_against_israel):', fx.get('song_a_witness_against_israel'), '| (song_written_and_taught_by_moses):', fx.get('song_written_and_taught_by_moses'), '| (face_hidden_and_forsaken_foretold):', fx.get('face_hidden_and_forsaken_foretold'), '| (moses_barred_from_the_land):', fx.get('moses_barred_from_the_land'), '| (barred_from_the_land):', fx.get('barred_from_the_land'))
print('effects by corpus unit (the song\'s kin units):', sorted((e, r.get('ledger_op')) for e, r in fx.items() if re.search(r'deu_04|deu_08|deu_09|deu_11|deu_17|deu_19|deu_29|deu_30|deu_31|lev_26|exo_04|exo_12|exo_15|exo_16|exo_19|exo_33|num_11|num_13|num_19|num_20|num_27|num_35|gen_03|gen_07|gen_10|gen_11|gen_19|gen_49', str(r.get('corpus')))))
print('kinds by corpus unit (the song\'s kin units):', sorted((k, r.get('form')) for k, r in ev.items() if re.search(r'deu_04|deu_08|deu_09|deu_11|deu_17|deu_19|deu_29|deu_30|deu_31|lev_26|exo_04|exo_12|exo_15|exo_16|exo_19|exo_33|num_11|num_13|num_19|num_20|num_27|num_35|gen_03|gen_07|gen_10|gen_11|gen_19|gen_49', str(r.get('corpus')))))
print('==== E. THE CALENDAR (Moses\' death date — 19b\'s marker the song stands on; the selfsame day of 32:48; no clock word in the song) ====')
cal = yaml.safe_load(open(S9 + '/calendar_parameters.yaml', encoding='utf-8'))
print(' parameters', len(cal['parameters']), '| keys naming death|moses|adar|hakhel|release|day|selfsame|month:', [k for k in cal['parameters'] if re.search(r'death|moses|adar|hakhel|release|selfsame|month', k)][:60])
print(' parameter rows whole (the death date, the hakhel):', [(k, cal['parameters'][k]) for k in cal['parameters'] if re.search(r'death|hakhel', k)][:6])
print(' the calendar keys used by the parameters (a counter of the `keys` fields):', collections.Counter(x for k in cal['parameters'] for x in (cal['parameters'][k].get('keys') or [])).most_common(30))
print('==== F. THE KIN\'S CELLS BY STATIC SCAN (every runner\'s defs; the refs they name among the kin verses) ====')
KIN = re.compile(r'\b(Deut 32:\d+|Deut 31:1\b|Deut 31:12\b|Deut 31:1[6-9]\b|Deut 31:2[0-2]\b|Deut 31:2[89]\b|Deut 31:30\b|Deut 29:25\b|Deut 9:28\b|Deut 11:9\b|Deut 4:26\b|Deut 30:19\b|Deut 17:[67]\b|Deut 19:1[5-9]\b|Deut 34:[1-8]\b|Deut 33:[1-9]\b|Deut 33:2[6-9]\b|Deut 8:1[2-6]\b|Deut 8:[34]\b|Deut 6:1[0-2]\b|Deut 4:19\b|Deut 4:3[5-9]\b|Deut 10:1[4-5]\b|Deut 7:6\b|Deut 14:2\b|Deut 28:5[3-7]\b|Deut 21:8\b|Deut 1:31\b|Deut 2:7\b|Num 27:1[2-4]\b|Num 20:1[0-3]\b|Num 20:2[2-9]\b|Num 35:2[3-4]\b|Num 13:16\b|Num 11:[4-9]\b|Num 11:3[1-4]\b|Num 14:2[1-4]\b|Num 19:14\b|Num 33:3[89]\b|Exod 4:[2-4]\b|Exod 12:17\b|Exod 12:41\b|Exod 12:51\b|Exod 19:4\b|Exod 15:1\b|Exod 15:21\b|Exod 33:2[1-2]\b|Exod 17:6\b|Exod 16:[3-9]\b|Exod 16:1[0-5]\b|Exod 16:3[1-5]\b|Gen 7:13\b|Gen 11:[1-9]\b|Gen 10:25\b|Gen 19:2[45]\b|Gen 3:19\b|Gen 49:\d+\b|Lev 26:2[2-9]\b|Lev 26:3\d\b|Josh 23:10\b|Ps 135:14\b|Isa 1:2\b)')
for f in sorted(glob.glob(S9 + '/cold_run_*.py')):
    src = open(f, encoding='utf-8').read(); name = os.path.basename(f)[9:-3]
    if name == 'sequence': continue
    for m in re.finditer(r'^def ([a-z_0-9]+)\(.*?(?=^def |\Z)', src, re.S | re.M):
        refs = sorted(set(KIN.findall(m.group(0))))
        if refs:
            asks = re.findall(r"if ask == '([a-z_0-9]+)':", m.group(0))
            qs = re.findall(r"^\s+'([a-z_0-9]+)':\s*\{", m.group(0), re.M)[:16]
            print(' %s.%s: refs %s | asks %d %s%s' % (name, m.group(1), refs[:18], len(asks), asks[:30], (' | keys ' + str(qs)) if (not asks and qs) else ''))
print('==== G. THE RECEIPT FINDER (good_land.receipt_seats over 32 — the finder\'s own count; the register: no receipt, header or footer in the chapter) ====')
try:
    with contextlib.redirect_stdout(io.StringIO()):
        import cold_run_good_land as GL
    for c in (32,):
        try: print(' receipt_seats(%d) = %r' % (c, GL.receipt_seats(c)))
        except Exception as ex: print(' receipt_seats(%d) FAILED %s: %s' % (c, type(ex).__name__, str(ex)[:200]))
except Exception as ex: print(' good_land import FAILED', type(ex).__name__, str(ex)[:200])
print('==== H. THE RUNNING WORLD (the snapshot) ====')
try:
    import register_census as R
    with contextlib.redirect_stdout(io.StringIO()):
        w = R.running_world()
    def nall(eff): return [(ent.name if hasattr(ent, 'name') else k, e.get('op')) for k, ent in w.entities.items() for e in ent.ledger if e['effect'] == eff]
    for eff in REUSE + tuple(NEW_E):
        n = nall(eff)
        if n or eff in REUSE: print(' W', eff, len(n), n[:6])
    print(' NEW_E on the running world (any):', [(e, len(nall(e))) for e in NEW_E if nall(e)])
    ip_ = w.entities.get('israel_people'); ipl = ip_.ledger if ip_ else []
    print(' israel_people ledger entries', len(ipl), '| by op', collections.Counter(e.get('op') for e in ipl), '| the last eight effects:', [e['effect'] for e in ipl[-8:]])
    for who in ('moses', 'yehoshua', 'joshua', 'aaron', 'the_levites', 'heaven', 'earth', 'the_heavens', 'the_earth', 'the_nations', 'the_land', 'the_tent_of_meeting', 'first_adam', 'adam', 'noah', 'jacob'):
        ent = w.entities.get(who)
        print(' ', who, 'ENTITY' if ent else 'NO ENTITY', '| ledger', len(ent.ledger) if ent else 0, '| by op', collections.Counter(e.get('op') for e in ent.ledger) if ent else '', '| the last six effects:', [e['effect'] for e in ent.ledger[-6:]] if ent else '')
    print(' entities', len(w.entities), '| closes', len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')]), '| markers', len([l for l in w.log if l[0] == 'MARKER']), '| events', len([l for l in w.log if l[0] == 'EVENT']), '| the day', w.clock.eras['exodus'].date(w.clock.day), '| population rows', len(w.tables['population']))
    last = [l[2] for l in w.log if l[0] == 'EVENT'][-6:]; print(' the tape\'s last six events:', [(e['kind'], str(e.get('case_source', ''))[:12]) for e in last])
    print(' entities naming yehoshua|joshua|moses|aaron|levite|heaven|earth|nations|the_land|sodom|egypt|moab|nebo|hor|jacob|israel|adam|noah|babel|shinar:', sorted(k for k in w.entities if re.search(r'yehoshua|joshua|moses|aaron|levite|heaven|earth|nations|the_land|sodom|egypt|moab|nebo|\bhor\b|jacob|israel|adam|noah|babel|shinar', k))[:80])
    print(' the population rows naming moses or aaron (age fields):', [r for r in w.tables['population'] if re.search(r'moses|aaron', str(r))][:6])
    print(' the EVENT kinds with form act/speech among the last 120 events:', collections.Counter(e['kind'] for e in [l[2] for l in w.log if l[0] == 'EVENT'][-120:] if not re.search(r'_(declared|commanded)$', e['kind'])).most_common(20))
except Exception as ex:
    import traceback; traceback.print_exc(); print(' THE SNAPSHOT FAILED:', repr(ex))
print('RECON DONE')
