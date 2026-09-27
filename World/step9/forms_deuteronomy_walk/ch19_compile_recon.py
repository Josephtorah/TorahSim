import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16b (2026-09-25): THE LEAN RECON for the compile of CHAPTERS 19-21 — what the tape, the registries, the dispositions, the probes and the
# running world say BEFORE a line is typed (15b's recon over three chapters: no docket scan; the kin's cells found by a STATIC scan of every runner's defs for the kin
# verses' refs, no import). Every number printed, never typed. ch17_compile_recon.py's form. RUN FROM THE REPO ROOT.
import os, re, sys, subprocess, io, contextlib, collections, glob
ROOT = _ROOT
sys.path.insert(0, ROOT + '/World/step9')
import yaml
S9 = ROOT + '/World/step9'
print('==== A. THE TAPE (cold_run_sequence.py) ====')
seq = open(S9 + '/cold_run_sequence.py', encoding='utf-8').read(); L = seq.split('\n')
for i, l in enumerate(L, 1):
    if re.match(r'^(RUN|PREVIOUS_RUN|NEWEST_RUNNER|PLACEMENT) = ', l): print('%d: %s' % (i, l[:170]))
    if re.match(r'^\s+\d+\)\s+#', l): print('%d: %s' % (i, l[:120]))
print('import lines:', sum(1 for l in L if l.startswith('import cold_run_')), '| DAEMON_ORDER tuples:', len(re.findall(r"^\s+\('cold_run_\w+', 'law_\w+'\)", seq, re.M)))
cps = re.findall(r"cp\('([A-Z]{2}\d+) ", seq); print('checkpoints:', len(cps), '| the D series in use:', sorted({c[:2] for c in cps if c[0] == 'D'}), '| last:', cps[-1])
vl = [l for l in L if "'DI5 MATCH'" in l]; print('VERDICTS DI line:', [l[:160] for l in vl])
print('lines naming Deut 19, 20 or 21:', [(i, l[:120]) for i, l in enumerate(L, 1) if re.search(r'Deut (?:19|2[01])[:\b]', l)][:14])
print('the last submit lines (the tape\'s newest own-day lines):', [(i, l[:110]) for i, l in enumerate(L, 1) if l.startswith("    w.submit({'kind': '")][-3:])
print('==== B. THE DISPOSITIONS ====')
dep = yaml.safe_load(open(S9 + '/dependency_dispositions.yaml', encoding='utf-8'))
print('edges', len(dep['edges']), '| pointers', len(dep.get('pointers', [])), '| spans', len(dep['spans']))
print('edges/pointers naming Deut 19/20/21 or refuge_war_family:', [(e.get('from'), e.get('to'), e.get('disposition'), str(e.get('why'))[:90]) for e in dep['edges'] if 'refuge_war_family' in str(e) or re.search(r'Deut (?:19|2[01]):', str(e))][:16], [(p.get('verse'), p.get('runner'), p.get('disposition'), str(p.get('why'))[:100]) for p in dep.get('pointers', []) if re.search(r'Deut (?:19|2[01]):', str(p)) or 'refuge_war_family' in str(p)][:8])
print('span courts_prophet (two ranges):', dep['spans'].get('courts_prophet'), '| refuge:', dep['spans'].get('refuge'), '| family:', dep['spans'].get('family'), '| seven_nations:', dep['spans'].get('seven_nations'))
print('an edge example (courts_prophet -> refuge):', [e for e in dep['edges'] if e.get('from') == 'courts_prophet' and e.get('to') == 'refuge'])
print('edges from seducers:', [(e['to'], e.get('link')) for e in dep['edges'] if e.get('from') == 'seducers'])
print('edges from courts_prophet:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'courts_prophet'])
print('edges from refuge:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'refuge'])
print('edges from seven_nations:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'seven_nations'])
print('edges INTO seducers/korach/priesthood/refuge (the count):', collections.Counter(e['to'] for e in dep['edges'] if e['to'] in ('refuge', 'seven_nations', 'family', 'zelophehad', 'seducers', 'courts_prophet', 'festivals_judges', 'lev24', 'midian', 'ordinances', 'mishpatim', 'gad_reuben', 'borders', 'opening_speech', 'sanctions', 'chukat', 'balak')))
dd = yaml.safe_load(open(S9 + '/daemon_dispositions.yaml', encoding='utf-8'))
print('daemons', len(dd['daemons']), '| functions (runners)', len(dd['functions']), '| law_courts_prophet:', dd['daemons'].get('law_courts_prophet'), '| law_refuge:', dd['daemons'].get('law_refuge'))
print('functions courts_prophet:', dd['functions'].get('courts_prophet'))
print('functions refuge:', dd['functions'].get('refuge'))
print('functions family:', dd['functions'].get('family'))
print('daemons of the kin:', [(n, d.get('given_at'), d.get('installed_by')) for n, d in dd['daemons'].items() if d.get('wraps') in ('refuge', 'seven_nations', 'family', 'zelophehad', 'seducers', 'courts_prophet', 'festivals_judges', 'lev24', 'midian', 'ordinances', 'mishpatim', 'gad_reuben', 'sanctions', 'chukat')])
rg = yaml.safe_load(open(S9 + '/register_dispositions.yaml', encoding='utf-8'))
print('register keys:', list(rg.keys()), '| seats naming Deut 19/20/21:', [(k, str(sec[k])[:160]) for sec in rg.values() if isinstance(sec, dict) for k in sec if re.search(r'Deut (?:19|2[01]):', str(k))])
print('==== C. THE PROBES ====')
ip = open(S9 + '/installation_probes.py', encoding='utf-8').read().split('\n')
print('I5 lines:', [(i, l[:200]) for i, l in enumerate(ip, 1) if re.search(r"len\(real\) == \d+", l)][:3])
rp = open(S9 + '/readback_probes.py', encoding='utf-8').read().split('\n')
print('readback defs:', [l[:40] for l in rp if re.match(r'^def q\d+', l)][-3:], '| the Q44 lines:', [(i, l[:160]) for i, l in enumerate(rp, 1) if 'Q44' in l][:6])
print('==== D. THE REGISTRIES ====')
fx = yaml.safe_load(open(S9 + '/effect_vocabulary.yaml', encoding='utf-8'))['effects']; ev = yaml.safe_load(open(S9 + '/event_vocabulary.yaml', encoding='utf-8'))['events']
NEW_E = ['three_cities_separated_commanded', 'way_prepared_commanded', 'land_divided_in_three_commanded', 'three_more_cities_conditioned', 'manslayer_flight_permitted', 'murderer_extradition_commanded', 'murderer_pity_barred', 'innocent_blood_purge_commanded', 'landmark_removal_barred', 'two_or_three_witnesses_required', 'witnesses_inquiry_commanded', 'plotting_witness_talion_commanded', 'talion_pity_barred', 'war_fear_barred', 'priest_war_speech_commanded', 'officers_exemptions_commanded', 'fearful_exemption_commanded', 'captains_appointed_commanded', 'peace_call_commanded', 'tribute_service_commanded', 'siege_males_smitten_commanded', 'spoil_permitted', 'far_cities_scope_declared', 'nothing_alive_left_commanded', 'abominations_teaching_barred', 'fruit_tree_cutting_barred', 'siege_works_permitted', 'slain_found_measuring_commanded', 'heifer_neck_broken_commanded', 'priests_approach_commanded', 'elders_hands_washed_commanded', 'elders_declaration_commanded', 'innocent_blood_atoned', 'captive_wife_permitted', 'captive_mourning_month_commanded', 'captive_sale_barred', 'captive_release_commanded', 'firstborn_double_portion_commanded', 'firstborn_right_transfer_barred', 'rebellious_son_seized_commanded', 'rebellious_son_stoning_commanded', 'hanging_after_death_commanded', 'corpse_overnight_barred', 'same_day_burial_commanded', 'land_defilement_barred']
NEW_K = ['refuge_cities_declared', 'manslayer_and_murderer_declared', 'landmark_declared', 'witnesses_law_declared', 'war_speech_declared', 'siege_law_declared', 'seven_nations_herem_declared', 'siege_trees_declared', 'heifer_rite_declared', 'captive_wife_declared', 'firstborn_portion_declared', 'rebellious_son_declared', 'hanged_burial_declared']
print('effects', len(fx), '| kinds', len(ev), '| the candidate new effects present before:', [e for e in NEW_E if e in fx], '| the candidate kinds present before:', [k for k in NEW_K if k in ev])
NEAR = re.compile(r'refuge|flee|fled|avenger|blood|murder|kill|slay|slain|witness|plot|talion|landmark|boundar|war|fear|peace|siege|spoil|tribute|herem|cherem|devot|tree|heifer|neck|measur|atone|captive|wife|wives|firstborn|double|inherit|rebel|stubborn|glutton|hang|bur|corpse|curse|purge|pity|nations|anoint|officer|exempt|vineyard|betroth|city|cities|iron|hate|innocent|elder|life_for|eye_for|cursed|way|road|hear|month|nails|sold|sell|portion|stone|death|driven')
print('near names (effects):', sorted(e for e in fx if NEAR.search(e)))
print('near names (kinds):', sorted(k for k in ev if NEAR.search(k)))
REUSE = ('cities_set_apart', 'dwells_in_refuge', 'flees_to_refuge', 'blood_required', 'has_blood', 'land_polluted_by_blood', 'purge_deadline', 'pity_barred', 'evil_purged_from_the_midst', 'israel_hears_and_fears', 'stoned', 'put_to_death', 'one_witness_barred', 'two_witnesses_required', 'witnesses_hand_first_commanded', 'witness_declared', 'boundary_witnessed', 'fear_not_promised', 'feared', 'peace_given', 'spoil_taken', 'taken_captive', 'city_devoted', 'cherem_vowed', 'devoted_thing_cleaving_barred', 'nations_driven_out', 'abominations_learning_barred', 'condemned_city_inquiry_required', 'hanged', 'slain', 'buried', 'burial_owed', 'atoned_forgiven', 'inheritance_stayed_in_tribe', 'firstborn_by_the_head', 'hated', 'consecrated_firstborn', 'substituted_for_the_firstborn', 'wife_taken', 'lashes', 'exempt', 'barred_from_it', 'courts_established', 'judges_charged', 'idolater_inquiry_required', 'substitution', 'burned_by_court', 'vineyard_planted', 'tree_planted', 'blemish_barred', 'anointed')
for e in REUSE:
    r = fx.get(e); print(' E', e, '|', r['ledger_op'], '|', r['en'][:110], '| corpus', str(r.get('corpus'))[:40]) if r else print(' E', e, 'MISSING')
print('a statute kind row (prophet_law_declared) fields:', ev.get('prophet_law_declared', {}).get('fields'), '| form', ev.get('prophet_law_declared', {}).get('form'), '| corpus', ev.get('prophet_law_declared', {}).get('corpus'))
print('effects by corpus unit (the kin units):', sorted((e, r.get('ledger_op')) for e, r in fx.items() if re.search(r'num_35|deu_04|deu_07|num_27|num_31|num_36|deu_02|deu_13|deu_17|deu_18|lev_24|exo_21|num_10|deu_16', str(r.get('corpus')))))
for k in ('three_cities_set_apart', 'refuge_law_given', 'refuge_statute_case', 'killer_case', 'killed', 'levite_cities_commanded', 'hanging_commanded', 'hanged', 'heifer_case', 'heifer_statute_given', 'peace_given', 'tribute_given', 'sihon_war_commanded', 'war_waged', 'nations_devoted', 'seven_nations_case', 'purge_commanded', 'captives_and_spoil_taken', 'midian_war_case', 'inheritance_crossed_tribes', 'firstborn_son', 'rival_wife_taken', 'plot_spoken', 'witnesses_called', 'parent_cursed', 'god_or_ruler_cursed', 'burial_commanded', 'boundary_sworn', 'elders_case', 'elders_commanded', 'city_spared', 'condemned_city_law_declared', 'og_came_out_and_fear_not', 'inciter_law_declared', 'prophet_law_declared', 'idolater_trial_declared', 'vessel_of_war_case', 'warriors_purification_commanded', 'betrothed_vow_case', 'firstborn_redemption_case'):
    r = ev.get(k); print(' K', k, '|', r.get('form'), '|', r['en'][:130], '| corpus', str(r.get('corpus'))[:40]) if r else print(' K', k, 'MISSING')
print('==== E. THE CALENDAR (no clock datum expected — the chapters\' laws carry no date) ====')
cal = yaml.safe_load(open(S9 + '/calendar_parameters.yaml', encoding='utf-8'))
print(' parameters', len(cal['parameters']), '| keys naming refuge|war|heifer|captive|month|firstborn|witness|siege:', [k for k in cal['parameters'] if re.search(r'refuge|war|heifer|captive|month|firstborn|witness|siege', k)])
print('==== F. THE KIN\'S CELLS BY STATIC SCAN (every runner\'s defs; the refs they name among the kin verses) ====')
KIN = re.compile(r'\b(Deut (?:19|2[01]):\d+|Num 35:\d+|Deut 4:4[1-3]\b|Exod 21:1[2-4]\b|Exod 21:2[3-5]\b|Lev 24:1[7-9]\b|Lev 24:2[0-2]\b|Deut 17:[67]\b|Deut 17:1[23]\b|Deut 13:1[2-6]\b|Deut 13:6\b|Exod 20:13\b|Exod 23:[17]\b|Deut 1:2[19]\b|Deut 1:30\b|Deut 3:22\b|Deut 7:[12]\b|Deut 7:1[6-9]\b|Deut 7:2[0-6]\b|Deut 2:2[4-9]\b|Deut 2:3[0-7]\b|Num 21:2[1-9]\b|Num 21:3[0-5]\b|Num 10:9\b|Num 31:\d+|Num 27:(?:[1-9]|1[01])\b|Num 36:\d+|Gen 25:3[1-4]\b|Gen 48:22\b|Gen 49:[34]\b|Gen 29:3[01]\b|Gen 4:19\b|Exod 13:1[23]\b|Exod 34:20\b|Num 19:\d+|Exod 21:1[57]\b|Lev 20:9\b|Exod 22:27\b|Num 25:4\b|Deut 12:2[35]\b|Deut 24:7\b|Deut 24:16\b|Josh 8:29\b|Josh 10:2[67]\b|Josh 20:\d+|2 Sam 21:\d+|Deut 22:2[1-4]\b|Lev 19:1[45]\b|Num 15:3[0-6]\b|Deut 16:1[89]\b|Deut 16:20\b|Num 5:\d+|Exod 22:1[6-9]\b|Deut 24:1\b|Lev 27:\d+|Deut 12:29\b|Exod 17:1[4-6]\b|Deut 25:1[7-9]\b|Gen 9:[56]\b|Gen 4:1[0-5]\b|Exod 14:1[34]\b|Num 14:[89]\b|Num 21:34\b|Deut 3:2\b)')
for f in sorted(glob.glob(S9 + '/cold_run_*.py')):
    src = open(f, encoding='utf-8').read(); name = os.path.basename(f)[9:-3]
    if name == 'sequence': continue
    for m in re.finditer(r'^def ([a-z_0-9]+)\(.*?(?=^def |\Z)', src, re.S | re.M):
        refs = sorted(set(KIN.findall(m.group(0))))
        if refs:
            asks = re.findall(r"if ask == '([a-z_0-9]+)':", m.group(0))
            qs = re.findall(r"^\s+'([a-z_0-9]+)':\s*\{", m.group(0), re.M)[:16]
            print(' %s.%s: refs %s | asks %d %s%s' % (name, m.group(1), refs[:16], len(asks), asks[:26], (' | keys ' + str(qs)) if (not asks and qs) else ''))
print('==== G. THE RUNNING WORLD (the snapshot) ====')
try:
    import register_census as R
    with contextlib.redirect_stdout(io.StringIO()):
        w = R.running_world()
    def nall(eff): return [(ent.name if hasattr(ent, 'name') else k, e.get('op')) for k, ent in w.entities.items() for e in ent.ledger if e['effect'] == eff]
    for eff in REUSE + tuple(NEW_E):
        print(' W', eff, len(nall(eff)), nall(eff)[:6])
    isr = w.entities['israel'].ledger if 'israel' in w.entities else []
    print(' israel ledger entries', len(isr), '| open debits', len([e for e in isr if e.get('op') == 'debit' and not e.get('closed_by')]), '| blocks', len([e for e in isr if e.get('op') == 'block']))
    ip_ = w.entities.get('israel_people'); ipl = ip_.ledger if ip_ else []
    print(' israel_people ledger entries', len(ipl), '| blocks', len([e for e in ipl if e.get('op') == 'block']), '| statuses', len([e for e in ipl if e.get('op') == 'status']), '| the last eight effects:', [e['effect'] for e in ipl[-8:]])
    print(' entities', len(w.entities), '| closes', len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')]), '| markers', len([l for l in w.log if l[0] == 'MARKER']), '| events', len([l for l in w.log if l[0] == 'EVENT']), '| the day', w.clock.eras['exodus'].date(w.clock.day), '| population rows', len(w.tables['population']))
    last = [l[2] for l in w.log if l[0] == 'EVENT'][-6:]; print(' the tape\'s last six events:', [(e['kind'], str(e.get('case_source', ''))[:12]) for e in last])
    print(' entities naming refuge|city|avenger|witness|priest|elder|heifer|captive|firstborn|reuben|joseph|sihon|og|midian|amalek|canaan|hittite|amorite|court:', sorted(k for k in w.entities if re.search(r'refuge|city|cities|avenger|witness|priest|elder|heifer|captive|firstborn|reuben|joseph|sihon|og\b|midian|amalek|canaan|hittite|amorite|perizzite|hivite|jebusite|girgash|the_court', k))[:40])
except Exception as ex:
    import traceback; traceback.print_exc(); print(' THE SNAPSHOT FAILED:', repr(ex))
print('RECON DONE')
