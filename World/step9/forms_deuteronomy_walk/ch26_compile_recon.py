import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 18b (2026-09-26): THE LEAN RECON for the compile of CHAPTERS 26-28 — what the tape, the registries, the dispositions, the probes and the
# running world say BEFORE a line is typed (17b's recon over four chapters, written whole for three: no docket scan; the kin's cells found by a STATIC scan of every
# runner's defs for the kin verses' refs, no import). Every number printed, never typed. ch22_compile_recon.py's form. RUN FROM THE REPO ROOT.
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
vl = [l for l in L if "'DK5 MATCH'" in l]; print('VERDICTS DK line:', [l[:200] for l in vl])
print('lines naming Deut 26, 27 or 28:', [(i, l[:120]) for i, l in enumerate(L, 1) if re.search(r'Deut 2[6-8][:\b]', l)][:16])
print('the last submit lines (the tape\'s newest own-day lines):', [(i, l[:110]) for i, l in enumerate(L, 1) if l.startswith("    w.submit({'kind': '")][-3:])
print('the persons_poor_court block in the sequence (import line, DAEMON_ORDER tuple, the cp lines):', [(i, l[:140]) for i, l in enumerate(L, 1) if 'persons_poor_court' in l][:12])
print('==== B. THE DISPOSITIONS ====')
dep = yaml.safe_load(open(S9 + '/dependency_dispositions.yaml', encoding='utf-8'))
print('edges', len(dep['edges']), '| pointers', len(dep.get('pointers', [])), '| spans', len(dep['spans']))
print('edges naming Deut 26-28:', [(e.get('from'), e.get('to'), e.get('disposition'), e.get('link'), str(e.get('why'))[:120]) for e in dep['edges'] if re.search(r'Deut 2[6-8]:|\b2[6-8]:\d', str(e))][:20])
print('pointers naming Deut 26-28 or 15:6 or 17:16:', [(p.get('verse'), p.get('runner'), p.get('disposition'), p.get('link'), str(p.get('why'))[:200]) for p in dep.get('pointers', []) if re.search(r'Deut 2[6-8]:|\b28:3\b|Deut 15:6|Deut 17:16|AS_WHEN', str(p))][:12])
print('a pointer entry whole (the first naming Deut 15:6):', [p for p in dep.get('pointers', []) if 'Deut 15:6' in str(p.get('verse'))][:1])
print('pointer dispositions counter:', collections.Counter(p.get('disposition') for p in dep.get('pointers', [])), '| pointer links:', collections.Counter(p.get('link') for p in dep.get('pointers', [])))
for sp in ('persons_poor_court', 'refuge_war_family', 'release_firstborn', 'food_tithe', 'festivals_judges', 'place_name', 'second_tablets', 'hear_o_israel', 'seven_nations', 'good_land', 'obey_horeb', 'covenant_at_horeb', 'tochacha', 'courts_prophet', 'sanctions', 'holiness', 'ordinances', 'mishpatim', 'exodus_story', 'sinai', 'decalogue', 'korach', 'moadim', 'musafim'):
    print(' span', sp, ':', dep['spans'].get(sp))
print('edges from persons_poor_court (the newest precedent):', [(e['to'], e.get('link'), e.get('disposition'), str(e.get('carries', ''))[:30]) for e in dep['edges'] if e.get('from') == 'persons_poor_court'])
print('edges from release_firstborn:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'release_firstborn'])
print('edges from food_tithe:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'food_tithe'])
print('edges from second_tablets:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'second_tablets'])
print('edges from tochacha:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'tochacha'])
print('an edge example (persons_poor_court -> good_land):', [e for e in dep['edges'] if e.get('from') == 'persons_poor_court' and e.get('to') == 'good_land'])
print('an edge example (persons_poor_court -> a FALSE one):', [e for e in dep['edges'] if e.get('from') == 'persons_poor_court' and e.get('disposition') == 'FALSE'][:1])
KINSET = ('persons_poor_court', 'refuge_war_family', 'courts_prophet', 'festivals_judges', 'seducers', 'release_firstborn', 'food_tithe', 'place_name', 'second_tablets', 'good_land', 'seven_nations', 'hear_o_israel', 'covenant_at_horeb', 'obey_horeb', 'tochacha', 'holiness', 'holiness_b', 'ordinances', 'mishpatim', 'mishpatim_2', 'mishpatim_3', 'sanctions', 'priesthood', 'yovel', 'korach', 'moadim', 'musafim', 'exodus_story', 'sinai', 'decalogue', 'pre_sinai', 'primeval', 'family', 'joseph', 'balak', 'refuge', 'lev24', 'shemini', 'tzav')
print('edges INTO the kin set (the count):', collections.Counter(e['to'] for e in dep['edges'] if e['to'] in KINSET))
dd = yaml.safe_load(open(S9 + '/daemon_dispositions.yaml', encoding='utf-8'))
print('daemons', len(dd['daemons']), '| functions (runners)', len(dd['functions']), '| law_persons_poor_court:', dd['daemons'].get('law_persons_poor_court'))
print('functions persons_poor_court:', str(dd['functions'].get('persons_poor_court'))[:600])
for fn in ('food_tithe', 'release_firstborn', 'festivals_judges', 'place_name', 'second_tablets', 'hear_o_israel', 'seven_nations', 'good_land', 'obey_horeb', 'covenant_at_horeb', 'tochacha', 'courts_prophet', 'refuge_war_family', 'sanctions', 'exodus_story', 'sinai', 'decalogue', 'korach'):
    print(' functions', fn, ':', str(dd['functions'].get(fn))[:400])
print('ALL the Deuteronomy daemons (given_at Deut) and the kin\'s:', [(n, d.get('given_at'), d.get('installed_by'), d.get('wraps')) for n, d in dd['daemons'].items() if str(d.get('given_at', '')).startswith('Deut') or d.get('wraps') in KINSET])
rg = yaml.safe_load(open(S9 + '/register_dispositions.yaml', encoding='utf-8'))
print('register keys:', list(rg.keys()))
print('register seats naming Deut 26-28 or 28:69:', [(sec_name, k, str(sec[k])[:300]) for sec_name, sec in rg.items() if isinstance(sec, dict) for k in sec if re.search(r'2[6-8]:\d|28, 69|28:69', str(k) + str(sec[k]))][:10])
print('==== C. THE PROBES ====')
ip = open(S9 + '/installation_probes.py', encoding='utf-8').read().split('\n')
print('I5 lines:', [(i, l[:200]) for i, l in enumerate(ip, 1) if re.search(r"len\(real\) == \d+", l)][:3])
rp = open(S9 + '/readback_probes.py', encoding='utf-8').read().split('\n')
print('readback defs:', [l[:40] for l in rp if re.match(r'^def q\d+', l)][-3:], '| the Q46 lines:', [(i, l[:160]) for i, l in enumerate(rp, 1) if 'Q46' in l][:8])
print('the PROBES list / registration of q46 (the last lines naming q46 or q45):', [(i, l[:160]) for i, l in enumerate(rp, 1) if re.search(r'\bq4[56]\b', l)][-6:])
rc = open(S9 + '/register_census.py', encoding='utf-8').read()
print('register_census: the footer seats / 28:69 / moab lines:', [(i, l[:160]) for i, l in enumerate(rc.split('\n'), 1) if re.search(r'28, 69|28:69|moab|footer', l)][:12])
print('==== D. THE REGISTRIES ====')
fx = yaml.safe_load(open(S9 + '/effect_vocabulary.yaml', encoding='utf-8'))['effects']; ev = yaml.safe_load(open(S9 + '/event_vocabulary.yaml', encoding='utf-8'))['events']
print('effects', len(fx), '| kinds', len(ev), '| effect ops:', collections.Counter(r.get('ledger_op') for r in fx.values()), '| kind forms:', collections.Counter(r.get('form') for r in ev.values()))
NEW_E = ['first_fruits_basket_commanded', 'first_fruits_declaration_commanded', 'first_fruits_recital_commanded', 'first_fruits_set_before_altar_commanded', 'first_fruits_rejoicing_commanded', 'third_year_tithe_given_commanded', 'tithe_confession_commanded', 'tithe_in_mourning_barred', 'tithe_in_uncleanness_barred', 'tithe_for_the_dead_barred', 'statutes_this_day_commanded', 'israel_declared_the_lord_god', 'lord_declared_israel_treasure_people', 'high_above_all_nations_promised', 'holy_people_promised', 'great_stones_commanded', 'stones_plastered_written_commanded', 'whole_stones_altar_commanded', 'iron_on_altar_barred', 'ebal_offerings_rejoicing_commanded', 'law_written_very_plainly_commanded', 'became_the_lords_people_this_day', 'six_tribes_on_gerizim_to_bless', 'six_tribes_on_ebal_for_the_curse', 'levites_loud_voice_commanded', 'image_maker_cursed', 'parent_dishonorer_cursed', 'landmark_mover_cursed', 'blind_misleader_cursed', 'judgment_perverter_cursed', 'fathers_wife_lier_cursed', 'beast_lier_cursed', 'sister_lier_cursed', 'mother_in_law_lier_cursed', 'secret_smiter_cursed', 'bribe_for_blood_taker_cursed', 'law_non_upholder_cursed', 'amen_answered', 'blessings_for_hearkening_set', 'blessed_in_city_and_field', 'blessed_fruit_of_womb_ground_beast', 'blessed_basket_and_trough', 'blessed_coming_in_and_going_out', 'enemies_flee_seven_ways', 'storehouses_blessed', 'established_holy_people', 'peoples_fear_israel', 'heavens_good_treasure_opened', 'lend_not_borrow', 'head_not_tail', 'turning_aside_barred', 'curses_for_not_hearkening_set', 'cursed_in_city_and_field', 'cursed_basket_and_trough', 'cursed_fruit_of_womb_ground_beast', 'cursed_coming_in_and_going_out', 'curse_confusion_rebuke_sent', 'pestilence_cleaving', 'consumption_fever_inflammation_sent', 'sword_blight_mildew_sent', 'heavens_brass_earth_iron', 'rain_turned_to_dust', 'smitten_before_enemies_seven_ways', 'carcass_food_for_birds', 'boil_of_egypt_hemorrhoids_scab_itch', 'madness_blindness_astonishment', 'wife_house_vineyard_taken', 'ox_ass_flock_taken', 'sons_daughters_given_to_another_people', 'fruit_eaten_by_unknown_nation', 'sore_boils_sole_to_crown', 'exiled_with_king_to_serve_wood_and_stone', 'astonishment_proverb_byword', 'seed_vines_olives_lost', 'sons_daughters_into_captivity', 'stranger_head_israel_tail', 'curses_pursue_until_destroyed', 'service_without_joy_the_ground', 'iron_yoke_on_neck', 'eagle_nation_devours', 'siege_in_all_gates_walls_fall', 'sons_flesh_eaten_in_siege', 'plagues_made_wonderful', 'diseases_of_egypt_returned', 'few_in_number_left', 'scattered_among_all_peoples', 'serving_wood_and_stone_among_nations', 'trembling_heart_no_rest', 'life_hanging_in_doubt', 'returned_to_egypt_in_ships', 'sold_and_none_buys', 'covenant_words_in_moab_declared']
NEW_K = ['first_fruits_declared', 'tithe_confession_declared', 'covenant_formula_declared', 'stones_altar_declared', 'people_this_day_declared', 'gerizim_ebal_tribes_declared', 'twelve_curses_declared', 'blessings_condition_declared', 'enemies_storehouses_blessing_declared', 'holy_people_fear_declared', 'heavens_treasure_lending_declared', 'curses_condition_declared', 'curse_diseases_brass_declared', 'defeat_carcass_boil_madness_declared', 'wife_house_vineyard_king_taken_declared', 'harvests_failed_stranger_head_declared', 'curses_pursue_iron_yoke_declared', 'eagle_nation_siege_declared', 'sons_flesh_siege_declared', 'plagues_scattered_declared', 'trembling_ships_covenant_declared']
print('candidate new effects', len(NEW_E), '(distinct', len(set(NEW_E)), ') present before:', [e for e in NEW_E if e in fx], '| candidate kinds', len(NEW_K), 'present before:', [k for k in NEW_K if k in ev])
NEAR = re.compile(r'first|fruit|bikkur|basket|tithe|third|confess|remov|levite|stranger|orphan|widow|rejoic|joy|treasur|holy|high|nation|stone|altar|plaster|writ|ebal|gerizim|bless|curs|amen|image|secret|father|mother|landmark|blind|judgment|bribe|innocent|uphold|city|field|womb|ground|beast|knead|coming|going|enem|seven|storehouse|rain|heaven|lend|borrow|head|tail|right|left|pestilence|consumption|fever|sword|blight|mildew|brass|iron|dust|carcass|bird|boil|egypt|madness|wife|house|vineyard|ox\b|ass\b|flock|sons|daughter|locust|worm|olive|captiv|yoke|eagle|siege|gate|wall|flesh|plague|disease|few|star|scatter|wood|rest|trembl|ship|slave|sold|covenant|moab|horeb|hearken|obey|voice|memra|declar|people|aramean|laban|sojourn|bondage|cried|affliction|milk|honey|mighty|outstretched|signs|wonders|priest|swore|swear|oath|forget|transgress|mourn|unclean|dead|look_down|habitation|hearing|statute|walk|ways|name|praise|glory')
print('near names (effects):', sorted(e for e in fx if NEAR.search(e)))
print('near names (kinds):', sorted(k for k in ev if NEAR.search(k)))
REUSE = ('blessings_for_hearing', 'work_of_the_hand_blessed', 'rain_in_season', 'heavens_shut', 'rain_withheld', 'land_yield_given', 'treasure_people', 'holy_people', 'chosen_people', 'lends_to_nations', 'lending_to_nations', 'rules_over_nations', 'tithe_eaten_before_the_lord', 'second_tithe_commanded', 'third_year_tithe_commanded', 'poor_tithe_commanded', 'levite_not_forsaken', 'rejoicing_commanded', 'rejoice_before_the_lord', 'first_fruits_brought', 'firstfruits_commanded', 'bikkurim_commanded', 'mezuzah_commanded', 'doorposts_written', 'blessing_set_on_gerizim', 'curse_set_on_ebal', 'blessing_and_curse_set', 'earth_altar_commanded', 'hewn_stones_barred', 'scattered_among_nations', 'land_desolate', 'eat_flesh_of_sons', 'sevenfold_chastisement', 'consumption_and_fever', 'heavens_as_iron', 'pestilence_sent', 'sword_brought', 'besieged', 'yoke_broken', 'bribe_barred', 'landmark_removal_barred', 'stranger_orphan_justice_commanded', 'fathers_wife_barred', 'cursed', 'curse', 'blessed', 'amen', 'return_to_egypt_barred', 'horses_multiplying_barred', 'diseases_of_egypt_removed', 'boils', 'boils_on_man_and_beast', 'israel_hears_and_fears', 'evil_purged_from_the_midst', 'put_to_death', 'stoned', 'abomination_barred', 'house_abomination_barred', 'forgetting_barred', 'wood_and_stone_served', 'few_in_number', 'stars_of_heaven', 'hard_bondage', 'cry_heard', 'affliction_seen', 'milk_and_honey_promised', 'the_land_sworn', 'covenant_cut', 'covenant_words_written', 'tablets_written', 'high_above_nations', 'name_dwelling_place', 'place_chosen', 'peace_offerings_eaten', 'burnt_offerings_offered')
for e in REUSE:
    r = fx.get(e); print(' E', e, '|', r['ledger_op'], '|', r['en'][:110], '| corpus', str(r.get('corpus'))[:50]) if r else print(' E', e, 'MISSING')
print('a statute kind row (amalek_remembrance_declared) fields:', ev.get('amalek_remembrance_declared', {}).get('fields'), '| form', ev.get('amalek_remembrance_declared', {}).get('form'), '| corpus', ev.get('amalek_remembrance_declared', {}).get('corpus'), '| whole row:', ev.get('amalek_remembrance_declared'))
print('an effect row whole (amalek_forgetting_barred):', fx.get('amalek_forgetting_barred'), '| (righteousness_before_the_lord):', fx.get('righteousness_before_the_lord'), '| (blessings_for_hearing):', fx.get('blessings_for_hearing'))
print('effects by corpus unit (the kin units):', sorted((e, r.get('ledger_op')) for e, r in fx.items() if re.search(r'lev_26|lev_19|exo_19|exo_20|exo_23|exo_34|num_18|deu_04|deu_06|deu_07|deu_08|deu_09|deu_10|deu_11|deu_12|deu_14|deu_15|deu_16|deu_17|deu_19|deu_20|deu_24|deu_25', str(r.get('corpus')))))
print('kinds by corpus unit (the kin units):', sorted((k, r.get('form')) for k, r in ev.items() if re.search(r'lev_26|exo_19|exo_23|exo_34|num_18|deu_04|deu_06|deu_07|deu_08|deu_09|deu_10|deu_11|deu_12|deu_14|deu_15|deu_16|deu_17|deu_19|deu_20|deu_24|deu_25', str(r.get('corpus')))))
print('==== E. THE CALENDAR (the year, the feasts, the third year — clock words as parameters) ====')
cal = yaml.safe_load(open(S9 + '/calendar_parameters.yaml', encoding='utf-8'))
print(' parameters', len(cal['parameters']), '| keys naming year|shavuot|weeks|sukkot|booths|passover|pesach|third|seventh|tithe|remov|first|omer|chanukah|release|jubilee|count:', [k for k in cal['parameters'] if re.search(r'year|shavuot|weeks|sukkot|booth|passover|pesach|third|seventh|tithe|remov|first|omer|chanukah|release|jubilee|count', k)][:60])
print(' a parameter row whole (the first naming release or tithe):', [(k, cal['parameters'][k]) for k in cal['parameters'] if re.search(r'release|tithe', k)][:2])
print('==== F. THE KIN\'S CELLS BY STATIC SCAN (every runner\'s defs; the refs they name among the kin verses) ====')
KIN = re.compile(r'\b(Deut 2[6-8]:\d+|Exod 23:19\b|Exod 34:26\b|Num 18:1[23]\b|Deut 14:2[2-9]\b|Deut 14:2\b|Deut 12:[5-7]\b|Deut 12:1[12]\b|Deut 12:1[78]\b|Deut 16:1[01]\b|Deut 16:1[45]\b|Deut 11:1[3-7]\b|Deut 11:2[6-9]\b|Deut 11:12\b|Deut 7:6\b|Deut 7:1[2-5]\b|Deut 6:9\b|Deut 6:3\b|Exod 20:2[2-6]\b|Exod 20:4\b|Deut 15:[4-6]\b|Deut 17:1[6-9]\b|Deut 20:[5-7]\b|Deut 24:17\b|Deut 19:14\b|Exod 21:17\b|Lev 20:9\b|Lev 19:14\b|Lev 18:(?:8|9|17|23)\b|Lev 20:1[0-7]\b|Exod 23:8\b|Deut 16:19\b|Deut 4:2[6-8]\b|Deut 8:1[1-9]\b|Lev 26:\d+|Exod 13:5\b|Exod 19:[5-6]\b|Deut 10:22\b|Gen 15:5\b|Exod 1:1[1-4]\b|Exod 3:7\b|Exod 15:26\b|Exod 9:9\b|Deut 5:15\b|Deut 4:[6-8]\b|Deut 13:7\b|Deut 13:1[7-8]\b|Josh 8:3[0-5]\b|Josh 4:\d+|Gen 47:4\b|Gen 46:27\b|Exod 34:28\b|Deut 29:\d+|Deut 31:1[0-3]\b|Deut 30:9\b|1 Kgs 8:9\b|Jer 7:33\b|Deut 9:9\b|Exod 12:1[1-4]\b)')
for f in sorted(glob.glob(S9 + '/cold_run_*.py')):
    src = open(f, encoding='utf-8').read(); name = os.path.basename(f)[9:-3]
    if name == 'sequence': continue
    for m in re.finditer(r'^def ([a-z_0-9]+)\(.*?(?=^def |\Z)', src, re.S | re.M):
        refs = sorted(set(KIN.findall(m.group(0))))
        if refs:
            asks = re.findall(r"if ask == '([a-z_0-9]+)':", m.group(0))
            qs = re.findall(r"^\s+'([a-z_0-9]+)':\s*\{", m.group(0), re.M)[:16]
            print(' %s.%s: refs %s | asks %d %s%s' % (name, m.group(1), refs[:18], len(asks), asks[:30], (' | keys ' + str(qs)) if (not asks and qs) else ''))
print('==== G. THE RECEIPT FINDER (good_land.receipt_seats over 26, 27, 28 — the finder\'s own count) ====')
try:
    with contextlib.redirect_stdout(io.StringIO()):
        import cold_run_good_land as GL
    for c in (26, 27, 28):
        try: print(' receipt_seats(%d) = %r' % (c, GL.receipt_seats(c)))
        except Exception as ex: print(' receipt_seats(%d) FAILED %s: %s' % (c, type(ex).__name__, str(ex)[:200]))
    print(' good_land defs:', [f for f in dir(GL) if callable(getattr(GL, f)) and not f.startswith('_')][:50])
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
    print(' israel_people HEAVEN entries (all):', [e['effect'] for e in ipl if e.get('op') == 'heaven'][:80])
    print(' entities', len(w.entities), '| closes', len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')]), '| markers', len([l for l in w.log if l[0] == 'MARKER']), '| events', len([l for l in w.log if l[0] == 'EVENT']), '| the day', w.clock.eras['exodus'].date(w.clock.day), '| population rows', len(w.tables['population']))
    last = [l[2] for l in w.log if l[0] == 'EVENT'][-6:]; print(' the tape\'s last six events:', [(e['kind'], str(e.get('case_source', ''))[:12]) for e in last])
    print(' entities naming levite|stranger|orphan|widow|priest|egypt|moab|reuben|simeon|judah|joseph|benjamin|gad|asher|zebulun|dan|naphtali|issachar|levi|the_court|heaven|the_land|the_ground|the_nations|amalek|laban|aram:', sorted(k for k in w.entities if re.search(r'levite|stranger|orphan|widow|priest|egypt|moab|reuben|simeon|judah|joseph|benjamin|gad\b|asher|zebulun|dan\b|naphtali|issachar|levi\b|the_court|heaven|the_land|the_ground|nations|amalek|laban|aram', k))[:80])
    print(' the heavens/the rain state on the running world (effects naming rain|heaven on any entity):', [(k, e['effect'], e.get('op')) for k, ent in w.entities.items() for e in ent.ledger if re.search(r'rain|heaven', e['effect'])][:20])
except Exception as ex:
    import traceback; traceback.print_exc(); print(' THE SNAPSHOT FAILED:', repr(ex))
print('RECON DONE')
