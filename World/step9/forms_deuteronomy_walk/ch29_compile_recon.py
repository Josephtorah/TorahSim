import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27): THE LEAN RECON for the compile of CHAPTERS 29-31 — what the tape, the registries, the dispositions, the probes and the
# running world say BEFORE a line is typed (18b's recon over three chapters, written whole for these three: no docket scan; the kin's cells found by a STATIC scan of every
# runner's defs for the kin verses' refs, no import). Every number printed, never typed. ch26_compile_recon.py's form. RUN FROM THE REPO ROOT.
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
vl = [l for l in L if "'DL5 MATCH'" in l]; print('VERDICTS DL line:', [l[:200] for l in vl])
print('lines naming Deut 29, 30 or 31:', [(i, l[:140]) for i, l in enumerate(L, 1) if re.search(r'Deut (29|30|31)[:\b]', l)][:20])
print('the last submit lines (the tape\'s newest own-day lines):', [(i, l[:110]) for i, l in enumerate(L, 1) if l.startswith("    w.submit({'kind': '")][-3:])
print('the firstfruits_ebal_curses block in the sequence (import line, DAEMON_ORDER tuple, the cp lines):', [(i, l[:140]) for i, l in enumerate(L, 1) if 'firstfruits_ebal_curses' in l][:14])
print('the ACT / SPEECH submits in the Deuteronomy stretch (kinds not ending _declared or _commanded, after line 2400):', [(i, re.search(r"'kind': '(\w+)'", l).group(1)) for i, l in enumerate(L, 1) if i > 2400 and l.startswith("    w.submit({'kind': '") and not re.search(r"'kind': '\w+_(declared|commanded)'", l)][:30])
print('marker submits in the Deuteronomy stretch (after line 2400):', [(i, l[:120]) for i, l in enumerate(L, 1) if i > 2400 and 'marker' in l.lower() and 'submit' in l][:12])
print('==== B. THE DISPOSITIONS ====')
dep = yaml.safe_load(open(S9 + '/dependency_dispositions.yaml', encoding='utf-8'))
print('edges', len(dep['edges']), '| pointers', len(dep.get('pointers', [])), '| spans', len(dep['spans']))
print('edges naming Deut 29-31:', [(e.get('from'), e.get('to'), e.get('disposition'), e.get('link'), str(e.get('why'))[:140]) for e in dep['edges'] if re.search(r'Deut (29|30|31):', str(e))][:20])
print('pointers naming Deut 29-31 or 30:9 or 31:10:', [(p.get('verse'), p.get('runner'), p.get('disposition'), p.get('link'), str(p.get('why'))[:260]) for p in dep.get('pointers', []) if re.search(r'Deut (29|30|31):|\b31:10\b|\b30:9\b|hakhel|assembly', str(p))][:14])
print('pointers OWED (all):', [(p.get('verse'), p.get('runner'), str(p.get('why'))[:160]) for p in dep.get('pointers', []) if p.get('disposition') == 'OWED'])
print('pointer dispositions counter:', collections.Counter(p.get('disposition') for p in dep.get('pointers', [])), '| pointer links:', collections.Counter(p.get('link') for p in dep.get('pointers', [])))
print('a pointer entry whole (the first RUN_CITATION of firstfruits_ebal_curses):', [p for p in dep.get('pointers', []) if p.get('runner') == 'firstfruits_ebal_curses'][:1])
for sp in ('firstfruits_ebal_curses', 'persons_poor_court', 'release_firstborn', 'festivals_judges', 'courts_prophet', 'opening_speech', 'good_land', 'obey_horeb', 'hear_o_israel', 'blessing_and_curse', 'seven_nations', 'second_tablets', 'tochacha', 'food_tithe', 'seducers', 'place_name', 'calendar', 'moadim', 'exodus_story', 'sinai', 'decalogue', 'pre_sinai', 'primeval', 'family', 'yovel', 'journeys', 'borders', 'balak', 'chukat', 'naso', 'korach', 'pinchas', 'inheritance', 'matot', 'sanctuary_build', 'erection', 'golden_calf', 'covenant_at_horeb', 'refuge_war_family'):
    if sp in dep['spans']: print(' span', sp, ':', dep['spans'].get(sp))
print('ALL span names:', sorted(dep['spans'].keys()))
print('edges from firstfruits_ebal_curses (the newest precedent):', [(e['to'], e.get('link'), e.get('disposition'), str(e.get('carries', ''))[:30]) for e in dep['edges'] if e.get('from') == 'firstfruits_ebal_curses'])
print('edges from courts_prophet:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'courts_prophet'])
print('edges from festivals_judges:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'festivals_judges'])
print('edges from opening_speech:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'opening_speech'])
print('edges from obey_horeb:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'obey_horeb'])
print('an edge example (firstfruits_ebal_curses -> release_firstborn):', [e for e in dep['edges'] if e.get('from') == 'firstfruits_ebal_curses' and e.get('to') == 'release_firstborn'])
print('an edge example (firstfruits_ebal_curses -> a FALSE one):', [e for e in dep['edges'] if e.get('from') == 'firstfruits_ebal_curses' and e.get('disposition') == 'FALSE'][:1])
print('an edge example (firstfruits_ebal_curses -> a VIA one):', [e for e in dep['edges'] if e.get('from') == 'firstfruits_ebal_curses' and e.get('disposition') == 'VIA'][:1])
dd = yaml.safe_load(open(S9 + '/daemon_dispositions.yaml', encoding='utf-8'))
print('daemons', len(dd['daemons']), '| functions (runners)', len(dd['functions']), '| law_firstfruits_ebal_curses:', dd['daemons'].get('law_firstfruits_ebal_curses'))
print('functions firstfruits_ebal_curses:', str(dd['functions'].get('firstfruits_ebal_curses'))[:700])
for fn in ('courts_prophet', 'festivals_judges', 'release_firstborn', 'opening_speech', 'good_land', 'obey_horeb', 'hear_o_israel', 'blessing_and_curse', 'second_tablets', 'tochacha', 'seducers', 'exodus_story', 'sinai', 'decalogue', 'primeval', 'yovel', 'journeys', 'borders', 'pinchas', 'matot', 'chukat', 'naso', 'balak', 'golden_calf', 'erection', 'pre_sinai'):
    if fn in dd['functions']: print(' functions', fn, ':', str(dd['functions'].get(fn))[:400])
print('ALL the Deuteronomy daemons (given_at Deut):', [(n, d.get('given_at'), d.get('installed_by'), d.get('wraps')) for n, d in dd['daemons'].items() if str(d.get('given_at', '')).startswith('Deut')])
rg = yaml.safe_load(open(S9 + '/register_dispositions.yaml', encoding='utf-8'))
print('register keys:', list(rg.keys()))
print('register seats naming Deut 29-31:', [(sec_name, k, str(sec[k])[:300]) for sec_name, sec in rg.items() if isinstance(sec, dict) for k in sec if re.search(r'\b(29|30|31):\d|(29|30|31), \d', str(k) + str(sec[k])) and 'Deut' in (str(k) + str(sec[k]))][:10])
print('==== C. THE PROBES ====')
ip = open(S9 + '/installation_probes.py', encoding='utf-8').read().split('\n')
print('I5 lines:', [(i, l[:200]) for i, l in enumerate(ip, 1) if re.search(r"len\(real\) == \d+", l)][:3])
rp = open(S9 + '/readback_probes.py', encoding='utf-8').read().split('\n')
print('readback defs:', [l[:40] for l in rp if re.match(r'^def q\d+', l)][-3:], '| the Q47 lines:', [(i, l[:160]) for i, l in enumerate(rp, 1) if 'Q47' in l][:8])
print('the PROBES list / registration of q47 (the last lines naming q47 or q46):', [(i, l[:160]) for i, l in enumerate(rp, 1) if re.search(r'\bq4[67]\b', l)][-6:])
rc = open(S9 + '/register_census.py', encoding='utf-8').read()
print('register_census: lines naming 29-31 / hakhel / assembly / footer:', [(i, l[:160]) for i, l in enumerate(rc.split('\n'), 1) if re.search(r'Deut (29|30|31)|hakhel|footer', l)][:12])
print('==== D. THE REGISTRIES ====')
fx = yaml.safe_load(open(S9 + '/effect_vocabulary.yaml', encoding='utf-8'))['effects']; ev = yaml.safe_load(open(S9 + '/event_vocabulary.yaml', encoding='utf-8'))['events']
print('effects', len(fx), '| kinds', len(ev), '| effect ops:', collections.Counter(r.get('ledger_op') for r in fx.values()), '| kind forms:', collections.Counter(r.get('form') for r in ev.values()))
NEW_E = ['covenant_words_keeping_commanded', 'standing_before_the_lord_this_day', 'covenant_oath_sworn_this_day', 'covenant_with_those_not_here', 'heart_turning_to_other_gods_barred', 'stubborn_self_blessing_barred', 'hidden_idolater_unpardoned', 'curses_of_the_book_on_the_idolater', 'name_blotted_from_under_heaven', 'separated_for_evil_from_all_tribes', 'land_brimstone_salt_like_sodom', 'nations_question_answered_covenant_forsaken', 'uprooted_and_cast_into_another_land', 'hidden_things_the_lords', 'revealed_things_ours_to_do', 'return_to_the_lord_the_condition', 'captivity_returned_on_return', 'gathered_from_all_the_peoples', 'gathered_from_the_end_of_heaven', 'brought_into_the_fathers_land_again', 'multiplied_above_the_fathers', 'heart_circumcised_by_the_lord', 'curses_put_on_the_enemies', 'return_and_hearken_and_do_commanded', 'abounding_in_fruit_of_body_cattle_ground', 'rejoiced_over_as_over_the_fathers', 'commandment_not_too_hard_nor_far', 'commandment_not_in_heaven_nor_beyond_the_sea', 'commandment_in_mouth_and_heart_to_do', 'life_and_death_set_before_israel', 'choose_life_commanded', 'living_and_multiplying_for_hearkening', 'perishing_for_turning_away', 'length_of_days_on_the_land_promised', 'joshua_to_cross_before_israel', 'nations_dispossessed_as_sihon_and_og_promised', 'be_strong_and_courageous_commanded', 'lord_goes_with_you_not_forsaking_promised', 'joshua_charged_to_bring_israel_in', 'law_written_and_given_to_priests_and_elders', 'hakhel_reading_commanded', 'hakhel_assembly_of_all_commanded', 'hakhel_children_hear_and_learn_commanded', 'moses_days_approach_to_die', 'lord_appeared_in_the_cloud_at_the_tent', 'moses_to_sleep_with_the_fathers', 'future_whoring_after_foreign_gods_foretold', 'covenant_breaking_foretold', 'face_hidden_and_forsaken_foretold', 'evils_and_troubles_befall_foretold', 'song_writing_commanded', 'song_taught_and_put_in_mouths_commanded', 'song_a_witness_against_israel', 'song_written_and_taught_by_moses', 'joshua_commissioned_to_bring_israel_in', 'lord_with_joshua_promised', 'book_of_the_law_beside_the_ark_commanded', 'book_a_witness_against_israel', 'elders_and_officers_assembled_commanded', 'corruption_after_moses_death_foretold', 'song_spoken_to_the_assembly_to_its_end']
NEW_K = ['moab_recital_declared', 'covenant_oath_entered_declared', 'hidden_idolater_curse_declared', 'land_desolation_answer_declared', 'hidden_and_revealed_declared', 'return_and_gathering_declared', 'heart_circumcised_declared', 'commandment_near_declared', 'life_and_death_choice_declared', 'joshua_charge_crossing_declared', 'law_written_given', 'hakhel_reading_declared', 'tent_summons_cloud_appeared', 'apostasy_and_hidden_face_foretold', 'song_witness_commanded', 'song_written_taught', 'joshua_commissioned_at_tent', 'book_beside_the_ark_declared', 'assembly_and_song_spoken_declared']
print('candidate new effects', len(NEW_E), '(distinct', len(set(NEW_E)), ') present before:', [e for e in NEW_E if e in fx], '| candidate kinds', len(NEW_K), 'present before:', [k for k in NEW_K if k in ev])
NEAR = re.compile(r'covenant|oath|swore|swear|stand|hewer|drawer|stranger|enter|root|gall|wormwood|bless|stubborn|pardon|anger|smok|blot|separat|brimstone|salt|sodom|gomorrah|uproot|cast|another_land|hidden|reveal|secret|return|captiv|gather|end_of_heaven|circumcis|heart|love|cleave|rejoic|fruit|womb|command|heaven|sea|mouth|life|death|choose|witness|perish|length|days|hundred|twenty|cross|jordan|joshua|sihon|og\b|strong|courag|fear_not|forsak|fail|wrote|written|writ|law|book|priest|levite|elder|ark|release|seven_years|booth|sukkot|appear|read|assembl|hakhel|children|learn|teach|tent|cloud|pillar|commission|sleep|fathers|whor|other_gods|break|face|hide|hid|evil|trouble|song|inclin|fat|sated|milk|honey|stiff|neck|rebel|corrupt|garment|cloth|bread|wine|forty|wilderness|reuben|gad|manasseh|sign|wonder|trial|egypt|pharaoh|know|this_day|moab|horeb|decalogue|shema|hear|voice|memra|nation|people|treasur|holy|multipl|scatter|exile|desolat|confess|remember|forget|testif|call|elders|officer|heads|tribe|wives|little|camp|firstfruits|first_fruits')
print('near names (effects):', sorted(e for e in fx if NEAR.search(e)))
print('near names (kinds):', sorted(k for k in ev if NEAR.search(k)))
REUSE = ('entered_the_covenant', 'became_the_lords_people_this_day', 'heaven_and_earth_witness', 'blessing_and_curse_set', 'cleaving_commanded', 'love_the_lord_commanded', 'love_commanded', 'other_gods_barred', 'covenant_cut', 'covenant_declared', 'covenant_words_in_moab_declared', 'confessed', 'scattered_among_nations', 'scattered_among_all_peoples', 'land_desolate', 'return_to_egypt_barred', 'debt_release_owed', 'three_pilgrimages_commanded', 'feast_of_booths_commanded', 'booths_commanded', 'appearing_commanded', 'fear_not_commanded', 'fear_not', 'jordan_crossing_barred', 'moses_barred_from_the_land', 'moses_barred_from_crossing', 'joshua_appointed', 'joshua_commissioned', 'joshua_charged', 'hands_laid_on_joshua', 'spirit_in_joshua', 'cloud_descended', 'pillar_of_cloud_stood', 'lord_appeared', 'tablets_in_the_ark', 'ark_built', 'ark_made', 'law_copy_commanded', 'king_copy_of_the_law_commanded', 'copy_of_the_law_commanded', 'stiff_necked', 'stiff_neck_declared', 'face_hidden', 'forsaken', 'whoring_after_gods_barred', 'sodom_overthrown', 'brimstone_and_fire_rained', 'gathered_from_the_nations', 'returned_to_the_land', 'heart_circumcision_commanded', 'circumcise_the_heart_commanded', 'shema_commanded', 'children_taught_commanded', 'teach_children_commanded', 'garments_not_worn_out', 'clothing_not_worn', 'manna_eaten', 'sihon_defeated', 'og_defeated', 'land_given_to_reuben_gad_manasseh', 'transjordan_given', 'oath_to_the_fathers_sworn', 'witnesses_called', 'perishing_testified', 'forgetting_barred', 'israel_hears_and_fears', 'seek_and_find_promised', 'return_promised', 'song_sung', 'song_taught', 'hearken_and_do_commanded', 'statutes_this_day_commanded', 'high_above_all_nations_promised', 'blessings_for_hearing', 'curses_for_not_hearkening', 'covenant_kept', 'covenant_forsaken', 'evil_purged_from_the_midst', 'israel_declared_the_lord_god', 'lord_declared_israel_treasure_people', 'seed_as_stars', 'multiplied', 'land_sworn', 'the_land_sworn_to_the_fathers', 'law_written_very_plainly_commanded', 'stones_plastered_written_commanded', 'ark_carried_by_levites', 'levites_carry_the_ark', 'rejoicing_before_the_lord_commanded', 'few_in_number_left', 'exiled_with_king_to_serve_wood_and_stone', 'serving_wood_and_stone_among_nations')
for e in REUSE:
    r = fx.get(e); print(' E', e, '|', r['ledger_op'], '|', r['en'][:110], '| corpus', str(r.get('corpus'))[:50]) if r else print(' E', e, 'MISSING')
print('a statute kind row (trembling_ships_covenant_declared) whole:', ev.get('trembling_ships_covenant_declared'))
print('ACT kind rows naming joshua|cloud|tent|wrote|song|ark|commission|appear|spoke (name, form, fields, corpus):', [(k, r.get('form'), r.get('fields'), str(r.get('corpus'))[:40]) for k, r in ev.items() if re.search(r'joshua|cloud|tent|wrote|written|song|ark|commission|appear|spoke|summon', k)][:40])
print('SPEECH kind rows in Deuteronomy (form speech, corpus deu_):', [(k, r.get('fields')) for k, r in ev.items() if r.get('form') == 'speech' and 'deu_' in str(r.get('corpus'))][:20])
print('an effect row whole (heaven_and_earth_witness):', fx.get('heaven_and_earth_witness'), '| (entered_the_covenant):', fx.get('entered_the_covenant'), '| (blessing_and_curse_set):', fx.get('blessing_and_curse_set'), '| (became_the_lords_people_this_day):', fx.get('became_the_lords_people_this_day'), '| (confessed):', fx.get('confessed'))
print('effects by corpus unit (the kin units):', sorted((e, r.get('ledger_op')) for e, r in fx.items() if re.search(r'deu_01|deu_02|deu_03|deu_04|deu_05|deu_06|deu_08|deu_09|deu_10|deu_11|deu_13|deu_15|deu_16|deu_17|lev_26|lev_23|lev_25|exo_13|exo_15|exo_32|exo_33|exo_34|num_12|num_27|num_32|num_14|num_21|gen_06|gen_19|jos_', str(r.get('corpus')))))
print('kinds by corpus unit (the kin units):', sorted((k, r.get('form')) for k, r in ev.items() if re.search(r'deu_01|deu_02|deu_03|deu_04|deu_08|deu_09|deu_10|deu_11|deu_13|deu_15|deu_16|deu_17|lev_26|lev_23|lev_25|exo_13|exo_15|exo_32|exo_33|exo_34|num_12|num_27|num_32|num_14|num_21|gen_06|gen_19', str(r.get('corpus')))))
print('==== E. THE CALENDAR (the release year, the booths, the appearing — the hakhel\'s clock words as parameters) ====')
cal = yaml.safe_load(open(S9 + '/calendar_parameters.yaml', encoding='utf-8'))
print(' parameters', len(cal['parameters']), '| keys naming release|seventh|year|sukkot|booth|appear|pilgrim|hakhel|assembl|tithe|jubilee|count|shemitta:', [k for k in cal['parameters'] if re.search(r'release|seventh|year|sukkot|booth|appear|pilgrim|hakhel|assembl|tithe|jubilee|count|shemitt', k)][:60])
print(' parameter rows whole (release, sukkot/booths, appearing):', [(k, cal['parameters'][k]) for k in cal['parameters'] if re.search(r'release|booth|sukkot|appear|pilgrim', k)][:6])
print(' the calendar keys used by the parameters (a counter of the `keys` fields):', collections.Counter(x for k in cal['parameters'] for x in (cal['parameters'][k].get('keys') or [])).most_common(30))
print('==== F. THE KIN\'S CELLS BY STATIC SCAN (every runner\'s defs; the refs they name among the kin verses) ====')
KIN = re.compile(r'\b(Deut (?:29|30|31):\d+|Deut 5:1\b|Deut 9:5\b|Deut 1:8\b|Deut 3:2[5-8]\b|Deut 3:1[2-7]\b|Deut 8:[34]\b|Deut 4:2[5-9]\b|Deut 4:3[01]\b|Deut 6:5\b|Deut 6:10\b|Deut 10:8\b|Deut 10:16\b|Deut 11:2[6-8]\b|Deut 13:18\b|Deut 15:[12]\b|Deut 16:1[3-6]\b|Deut 17:1[89]\b|Deut 19:8\b|Deut 28:11\b|Deut 28:58\b|Deut 28:63\b|Deut 28:69\b|Deut 9:6\b|Deut 9:13\b|Deut 4:28\b|Deut 2:2[6-9]\b|Deut 2:3\d\b|Deut 3:[1-9]\b|Deut 3:1[01]\b|Num 12:5\b|Num 27:1[89]\b|Num 27:2[0-3]\b|Num 32:2[89]\b|Num 32:3[0-3]\b|Num 14:39\b|Num 21:2[1-9]\b|Num 21:3[0-5]\b|Exod 13:21\b|Exod 32:9\b|Exod 33:9\b|Exod 34:9\b|Exod 15:1\b|Gen 6:3\b|Gen 19:2[45]\b|Lev 26:4[0-5]\b|Lev 23:3[4-9]\b|Lev 23:4[0-2]\b|Lev 25:[1-9]\b|Lev 25:1[0-3]\b|Josh 1:[6-9]\b|Josh 8:34\b|1 Kgs 9:8\b|Jer 22:8\b|Neh 1:9\b|Deut 34:7\b|Deut 32:44\b|Deut 32:20\b)')
for f in sorted(glob.glob(S9 + '/cold_run_*.py')):
    src = open(f, encoding='utf-8').read(); name = os.path.basename(f)[9:-3]
    if name == 'sequence': continue
    for m in re.finditer(r'^def ([a-z_0-9]+)\(.*?(?=^def |\Z)', src, re.S | re.M):
        refs = sorted(set(KIN.findall(m.group(0))))
        if refs:
            asks = re.findall(r"if ask == '([a-z_0-9]+)':", m.group(0))
            qs = re.findall(r"^\s+'([a-z_0-9]+)':\s*\{", m.group(0), re.M)[:16]
            print(' %s.%s: refs %s | asks %d %s%s' % (name, m.group(1), refs[:18], len(asks), asks[:30], (' | keys ' + str(qs)) if (not asks and qs) else ''))
print('==== G. THE RECEIPT FINDER (good_land.receipt_seats over 29, 30, 31 — the finder\'s own count) ====')
try:
    with contextlib.redirect_stdout(io.StringIO()):
        import cold_run_good_land as GL
    for c in (29, 30, 31):
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
    for who in ('moses', 'joshua', 'the_levites', 'the_priesthood', 'the_ark', 'the_tent', 'the_tabernacle'):
        ent = w.entities.get(who)
        print(' ', who, 'ENTITY' if ent else 'NO ENTITY', '| ledger', len(ent.ledger) if ent else 0, '| by op', collections.Counter(e.get('op') for e in ent.ledger) if ent else '', '| the last six effects:', [e['effect'] for e in ent.ledger[-6:]] if ent else '')
    print(' entities', len(w.entities), '| closes', len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')]), '| markers', len([l for l in w.log if l[0] == 'MARKER']), '| events', len([l for l in w.log if l[0] == 'EVENT']), '| the day', w.clock.eras['exodus'].date(w.clock.day), '| population rows', len(w.tables['population']))
    last = [l[2] for l in w.log if l[0] == 'EVENT'][-6:]; print(' the tape\'s last six events:', [(e['kind'], str(e.get('case_source', ''))[:12]) for e in last])
    print(' entities naming joshua|moses|levite|priest|reuben|gad|manasseh|sihon|og|sodom|egypt|moab|ark|tent|cloud|aaron|eleazar|elders|heaven|earth|nations|the_land:', sorted(k for k in w.entities if re.search(r'joshua|moses|levite|priest|reuben|gad\b|manasseh|sihon|\bog\b|sodom|egypt|moab|ark|tent|cloud|aaron|eleazar|elder|heaven|earth|nations|the_land', k))[:80])
    print(' the population rows naming moses or joshua (age fields):', [r for r in w.tables['population'] if re.search(r'moses|joshua', str(r))][:6])
    print(' the EVENT kinds with form act/speech among the last 120 events:', collections.Counter(e['kind'] for e in [l[2] for l in w.log if l[0] == 'EVENT'][-120:] if not re.search(r'_(declared|commanded)$', e['kind'])).most_common(20))
except Exception as ex:
    import traceback; traceback.print_exc(); print(' THE SNAPSHOT FAILED:', repr(ex))
print('RECON DONE')
