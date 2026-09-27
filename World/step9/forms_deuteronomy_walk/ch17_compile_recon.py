import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 15b (2026-09-24): THE LEAN RECON for the compile of CHAPTERS 17-18 — what the tape, the registries, the dispositions, the probes and the
# running world say BEFORE a line is typed (14b's recon over two chapters: no docket scan; the kin's cells found by a STATIC scan of every runner's defs for the kin
# verses' refs, no import). Every number printed, never typed. ch16_compile_recon.py's form. RUN FROM THE REPO ROOT.
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
vl = [l for l in L if "'DH5 MATCH'" in l]; print('VERDICTS DH line:', [l[:160] for l in vl])
print('lines naming Deut 17 or 18:', [(i, l[:120]) for i, l in enumerate(L, 1) if re.search(r'Deut 1[78][:\b]', l)][:14])
print('the last submit lines (the tape\'s newest own-day lines):', [(i, l[:110]) for i, l in enumerate(L, 1) if l.startswith("    w.submit({'kind': '")][-3:])
print('==== B. THE DISPOSITIONS ====')
dep = yaml.safe_load(open(S9 + '/dependency_dispositions.yaml', encoding='utf-8'))
print('edges', len(dep['edges']), '| pointers', len(dep.get('pointers', [])), '| spans', len(dep['spans']))
print('edges/pointers naming Deut 17/18 or courts_prophet:', [(e.get('from'), e.get('to'), e.get('disposition')) for e in dep['edges'] if 'courts_prophet' in str(e) or re.search(r'Deut 1[78]:', str(e))][:12], [(p.get('verse'), p.get('runner'), p.get('disposition')) for p in dep.get('pointers', []) if re.search(r'Deut 1[78]:', str(p)) or 'courts_prophet' in str(p)][:8])
print('span festivals_judges:', dep['spans'].get('festivals_judges'), '| opening_speech (a multi-chapter span):', dep['spans'].get('opening_speech')[:2])
print('an edge example (festivals_judges -> opening_speech):', [e for e in dep['edges'] if e.get('from') == 'festivals_judges' and e.get('to') == 'opening_speech'])
print('edges from seducers:', [(e['to'], e.get('link')) for e in dep['edges'] if e.get('from') == 'seducers'])
print('edges from festivals_judges:', [(e['to'], e.get('link')) for e in dep['edges'] if e.get('from') == 'festivals_judges'])
print('edges INTO seducers/korach/priesthood/refuge (the count):', collections.Counter(e['to'] for e in dep['edges'] if e['to'] in ('seducers', 'korach', 'priesthood', 'refuge', 'ordinances', 'sanctions', 'holiness_b', 'opening_speech', 'exodus_story')))
dd = yaml.safe_load(open(S9 + '/daemon_dispositions.yaml', encoding='utf-8'))
print('daemons', len(dd['daemons']), '| functions (runners)', len(dd['functions']), '| law_festivals_judges:', dd['daemons'].get('law_festivals_judges'))
print('functions festivals_judges:', dd['functions'].get('festivals_judges'))
print('daemons of the kin (seducers, korach, priesthood, refuge, sanctions, holiness_b, ordinances):', [(n, d.get('given_at'), d.get('installed_by')) for n, d in dd['daemons'].items() if d.get('wraps') in ('seducers', 'korach', 'priesthood', 'refuge', 'sanctions', 'holiness_b', 'ordinances')])
rg = yaml.safe_load(open(S9 + '/register_dispositions.yaml', encoding='utf-8'))
print('register keys:', list(rg.keys()), '| seats naming Deut 17/18:', [k for sec in rg.values() if isinstance(sec, dict) for k in sec if re.search(r'Deut 1[78]:', str(k))])
print('==== C. THE PROBES ====')
ip = open(S9 + '/installation_probes.py', encoding='utf-8').read().split('\n')
print('I5 lines:', [(i, l[:200]) for i, l in enumerate(ip, 1) if re.search(r"len\(real\) == \d+", l)][:3])
rp = open(S9 + '/readback_probes.py', encoding='utf-8').read().split('\n')
print('readback defs:', [l[:40] for l in rp if re.match(r'^def q\d+', l)][-3:], '| the Q43 lines:', [(i, l[:160]) for i, l in enumerate(rp, 1) if 'Q43' in l][:6])
print('==== D. THE REGISTRIES ====')
fx = yaml.safe_load(open(S9 + '/effect_vocabulary.yaml', encoding='utf-8'))['effects']; ev = yaml.safe_load(open(S9 + '/event_vocabulary.yaml', encoding='utf-8'))['events']
NEW_E = ['blemished_offering_barred', 'idolater_inquiry_required', 'two_witnesses_required', 'one_witness_barred', 'witnesses_hand_first_commanded', 'high_court_at_the_place_commanded', 'sentence_binding_commanded', 'turning_from_the_word_barred', 'rebel_elder_death', 'king_from_the_brothers_commanded', 'foreign_king_barred', 'horses_multiplying_barred', 'return_to_egypt_barred', 'wives_multiplying_barred', 'silver_and_gold_multiplying_barred', 'law_copy_commanded', 'heart_lifting_barred', 'levi_inheritance_barred', 'shoulder_cheeks_maw_owed', 'first_fleece_owed', 'priests_standing_chosen', 'levite_service_at_the_place_permitted', 'equal_portions_commanded', 'abominations_learning_barred', 'passing_through_fire_barred', 'diviner_barred', 'soothsayer_barred', 'augur_barred', 'sorcerer_barred', 'charmer_barred', 'ghost_consulting_barred', 'familiar_spirit_barred', 'necromancer_barred', 'wholeness_commanded', 'prophet_hearkening_commanded', 'prophet_like_moses_promised', 'word_required_of_the_hearer', 'presumptuous_prophet_death', 'false_word_test_declared', 'false_prophet_fear_barred']
NEW_K = ['blemished_offering_barred_declared', 'idolater_trial_declared', 'high_court_declared', 'king_law_declared', 'priests_dues_declared', 'levite_at_the_place_declared', 'diviners_barred', 'prophet_law_declared']
print('effects', len(fx), '| kinds', len(ev), '| the candidate new effects present before:', [e for e in NEW_E if e in fx], '| the candidate kinds present before:', [k for k in NEW_K if k in ev])
NEAR = re.compile(r'court|king|prophet|witness|divin|sorcer|blemish|fleece|shoulder|priest|levi|purge|evil_|presum|horse|wives|egypt|fire|molech|whole|ghost|spirit|necro|augur|sooth|charm|abomin|inherit|portion|due|gift|first|appeal|elder|rebel|sentence|ston|sun|moon|host|throne|copy|fear|hear|witch|omen|idol|other_gods|death|lash|strang|foreign|brother|maw|cheek|learn|require')
print('near names (effects):', sorted(e for e in fx if NEAR.search(e)))
print('near names (kinds):', sorted(k for k in ev if NEAR.search(k)))
REUSE = ('blemish_barred', 'evil_purged_from_the_midst', 'stoned', 'put_to_death', 'lashes', 'false_prophet_hearing_barred', 'tested_by_the_lord', 'cleaving_commanded', 'pity_barred', 'israel_hears_and_fears', 'prophet_declared', 'kings_promised', 'kingdom_founded', 'priestly_dues_granted', 'levites_portion_given', 'levite_forsaking_barred', 'inheritance_barred', 'other_gods_barred', 'wholeness_owed', 'sentence_pronounced', 'witness_declared', 'foreign_rite_inquiry_barred', 'house_abomination_barred', 'returned_to_egypt', 'due_to_priest', 'strange_offering_barred', 'holy_things_in_the_gates_barred', 'courts_established', 'judges_charged', 'judges_and_officers_commanded', 'justice_pursuit_commanded', 'bribe_barred', 'condemned_city_inquiry_required', 'descent_to_egypt_barred', 'burned_by_court', 'adding_barred')
for e in REUSE:
    r = fx.get(e); print(' E', e, '|', r['ledger_op'], '|', r['en'][:110], '| corpus', str(r.get('corpus'))[:40]) if r else print(' E', e, 'MISSING')
print('a statute kind row (asherah_and_pillar_barred) fields:', ev.get('asherah_and_pillar_barred', {}).get('fields'), '| form', ev.get('asherah_and_pillar_barred', {}).get('form'))
for k in ('prophet_test_declared', 'inciter_law_declared', 'purge_commanded', 'sentence_declared', 'priestly_gifts_case', 'stoned_as_commanded', 'witnesses_called', 'seed_given_to_molech', 'ghost_pit_consulted', 'sorcery_done', 'abomination_barred', 'kings_demand_refused', 'king_arose', 'kingdom_begun', 'portion_declared'):
    r = ev.get(k); print(' K', k, '|', r.get('form'), '|', r['en'][:130], '| corpus', str(r.get('corpus'))[:40]) if r else print(' K', k, 'MISSING')
print('==== E. THE CALENDAR (no clock datum expected — the chapters\' laws carry no date) ====')
cal = yaml.safe_load(open(S9 + '/calendar_parameters.yaml', encoding='utf-8'))
print(' parameters', len(cal['parameters']), '| keys naming king|court|prophet|witness:', [k for k in cal['parameters'] if re.search(r'king|court|prophet|witness|levi|priest', k)])
print('==== F. THE KIN\'S CELLS BY STATIC SCAN (every runner\'s defs; the refs they name among the kin verses) ====')
KIN = re.compile(r'\b(Deut 1[78]:\d+|Deut 13:\d+|Deut 16:(?:18|19|20)\b|Deut 1:(?:1[5-7])\b|Exod 18:(?:1[3-9]|2[0-6])\b|Exod 22:(?:1[6-9])\b|Exod 23:(?:[1-3]|[6-8])\b|Lev 19:(?:15|26|31)\b|Lev 20:(?:[1-6]|27)\b|Lev 22:(?:1[7-9]|2[0-5])\b|Lev 21:(?:1[6-9]|2[0-3])\b|Num 18:(?:[8-9]|1\d|2\d|3[0-2])\b|Num 35:30\b|Deut 10:(?:8|9)\b|Deut 12:(?:12|18|19|29|30|31)\b|Deut 14:(?:27|28|29)\b|Deut 5:(?:2[2-9]|3[0-1])\b|Exod 20:(?:1[5-8])\b|Gen 17:(?:6|16)\b|Gen 35:11\b|Gen 49:10\b|Exod 13:17\b|Exod 14:13\b|Num 14:4\b|Deut 4:(?:2|10|19)\b|Deut 7:(?:[1-5]|2[5-6])\b|Lev 24:(?:14|16)\b|Num 15:3[5-6]\b|Deut 9:10\b|Num 11:2[5-9]\b|Num 12:[6-8]\b|Exod 7:1\b|Gen 20:7\b|Num 27:21\b|Exod 21:14\b|Num 16:\d+|Deut 18:22|1 Kgs 1[01]:\d+|1 Sam 8:\d+|Lev 27:(?:2[6-8])\b|Num 3:(?:[5-9]|10)\b|Exod 29:2[6-8]\b|Lev 7:3[0-4]\b|Lev 10:1[4-5]\b)')
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
    print(' entities naming court|king|prophet|levi|priest|witness:', sorted(k for k in w.entities if re.search(r'court|king|prophet|levi|priest|witness|aaron|samuel|david|solomon', k))[:30])
except Exception as ex:
    import traceback; traceback.print_exc(); print(' THE SNAPSHOT FAILED:', repr(ex))
print('RECON DONE')
