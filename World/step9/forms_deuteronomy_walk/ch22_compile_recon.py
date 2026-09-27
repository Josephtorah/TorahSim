import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 17b (2026-09-26): THE LEAN RECON for the compile of CHAPTERS 22-25 — what the tape, the registries, the dispositions, the probes and the
# running world say BEFORE a line is typed (16b's recon over three chapters, written whole for four: no docket scan; the kin's cells found by a STATIC scan of every
# runner's defs for the kin verses' refs, no import). Every number printed, never typed. ch19_compile_recon.py's form. RUN FROM THE REPO ROOT.
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
vl = [l for l in L if "'DJ5 MATCH'" in l]; print('VERDICTS DJ line:', [l[:160] for l in vl])
print('lines naming Deut 22, 23, 24 or 25:', [(i, l[:120]) for i, l in enumerate(L, 1) if re.search(r'Deut 2[2-5][:\b]', l)][:16])
print('the last submit lines (the tape\'s newest own-day lines):', [(i, l[:110]) for i, l in enumerate(L, 1) if l.startswith("    w.submit({'kind': '")][-3:])
print('==== B. THE DISPOSITIONS ====')
dep = yaml.safe_load(open(S9 + '/dependency_dispositions.yaml', encoding='utf-8'))
print('edges', len(dep['edges']), '| pointers', len(dep.get('pointers', [])), '| spans', len(dep['spans']))
print('edges/pointers naming Deut 22-25:', [(e.get('from'), e.get('to'), e.get('disposition'), str(e.get('why'))[:90]) for e in dep['edges'] if re.search(r'Deut 2[2-5]:', str(e))][:20], [(p.get('verse'), p.get('runner'), p.get('disposition'), str(p.get('why'))[:100]) for p in dep.get('pointers', []) if re.search(r'Deut 2[2-5]:', str(p))][:10])
print('span refuge_war_family (three ranges):', dep['spans'].get('refuge_war_family'), '| holiness:', dep['spans'].get('holiness'), '| holiness_b:', dep['spans'].get('holiness_b'), '| ordinances:', dep['spans'].get('ordinances'), '| mishpatim:', dep['spans'].get('mishpatim'), '| mishpatim_2:', dep['spans'].get('mishpatim_2'), '| mishpatim_3:', dep['spans'].get('mishpatim_3'), '| vows:', dep['spans'].get('vows'), '| release_firstborn:', dep['spans'].get('release_firstborn'))
print('an edge example (refuge_war_family -> lev24):', [e for e in dep['edges'] if e.get('from') == 'refuge_war_family' and e.get('to') == 'lev24'])
print('edges from refuge_war_family:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'refuge_war_family'])
print('edges from holiness:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'holiness'])
print('edges from ordinances:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'ordinances'])
print('edges from release_firstborn:', [(e['to'], e.get('link'), e.get('disposition')) for e in dep['edges'] if e.get('from') == 'release_firstborn'])
KINSET = ('refuge_war_family', 'courts_prophet', 'festivals_judges', 'seducers', 'release_firstborn', 'holiness', 'holiness_b', 'ordinances', 'mishpatim', 'mishpatim_2', 'mishpatim_3', 'guardians', 'sanctions', 'priesthood', 'yovel', 'vows', 'negaim', 'metzora', 'beha', 'balak', 'naso', 'exodus_story', 'pre_sinai', 'joseph', 'family', 'mekoshesh', 'lev24', 'decalogue', 'hear_o_israel', 'covenant_at_horeb', 'seven_nations', 'place_name', 'refuge', 'primeval', 'mamre', 'moadim', 'tochacha', 'food_tithe')
print('edges INTO the kin set (the count):', collections.Counter(e['to'] for e in dep['edges'] if e['to'] in KINSET))
dd = yaml.safe_load(open(S9 + '/daemon_dispositions.yaml', encoding='utf-8'))
print('daemons', len(dd['daemons']), '| functions (runners)', len(dd['functions']), '| law_refuge_war_family:', dd['daemons'].get('law_refuge_war_family'))
print('functions refuge_war_family:', dd['functions'].get('refuge_war_family'))
print('functions holiness:', dd['functions'].get('holiness'), '| holiness_b:', dd['functions'].get('holiness_b'))
print('functions mishpatim:', dd['functions'].get('mishpatim'), '| mishpatim_2:', dd['functions'].get('mishpatim_2'), '| mishpatim_3:', dd['functions'].get('mishpatim_3'), '| ordinances:', dd['functions'].get('ordinances'))
print('functions vows:', dd['functions'].get('vows'), '| negaim:', dd['functions'].get('negaim'), '| beha:', dd['functions'].get('beha'), '| joseph:', dd['functions'].get('joseph'), '| exodus_story:', dd['functions'].get('exodus_story'), '| balak:', dd['functions'].get('balak'), '| naso:', dd['functions'].get('naso'), '| yovel:', dd['functions'].get('yovel'), '| priesthood:', dd['functions'].get('priesthood'))
print('daemons of the kin:', [(n, d.get('given_at'), d.get('installed_by')) for n, d in dd['daemons'].items() if d.get('wraps') in KINSET])
rg = yaml.safe_load(open(S9 + '/register_dispositions.yaml', encoding='utf-8'))
print('register keys:', list(rg.keys()), '| seats naming Deut 22-25:', [(k, str(sec[k])[:160]) for sec in rg.values() if isinstance(sec, dict) for k in sec if re.search(r'Deut 2[2-5]:', str(k))])
print('==== C. THE PROBES ====')
ip = open(S9 + '/installation_probes.py', encoding='utf-8').read().split('\n')
print('I5 lines:', [(i, l[:200]) for i, l in enumerate(ip, 1) if re.search(r"len\(real\) == \d+", l)][:3])
rp = open(S9 + '/readback_probes.py', encoding='utf-8').read().split('\n')
print('readback defs:', [l[:40] for l in rp if re.match(r'^def q\d+', l)][-3:], '| the Q45 lines:', [(i, l[:160]) for i, l in enumerate(rp, 1) if 'Q45' in l][:6])
print('==== D. THE REGISTRIES ====')
fx = yaml.safe_load(open(S9 + '/effect_vocabulary.yaml', encoding='utf-8'))['effects']; ev = yaml.safe_load(open(S9 + '/event_vocabulary.yaml', encoding='utf-8'))['events']
NEW_E = ['lost_thing_return_commanded', 'hiding_from_lost_thing_barred', 'fallen_beast_raising_commanded', 'cross_dressing_barred', 'mother_bird_sending_commanded', 'parapet_commanded', 'house_bloodguilt_barred', 'vineyard_mixed_seed_barred', 'ox_ass_plowing_barred', 'wool_linen_barred', 'tassels_commanded', 'slander_fine_commanded', 'slanderer_divorce_barred', 'unchaste_bride_stoning_commanded', 'adulterers_death_commanded', 'betrothed_girl_city_field_declared', 'rapist_fifty_commanded', 'rapist_divorce_barred', 'fathers_wife_barred', 'crushed_barred_from_assembly', 'forbidden_union_offspring_barred', 'ammon_moab_barred_forever', 'ammon_moab_peace_barred', 'edom_egypt_third_generation_admitted', 'camp_evil_thing_guarded', 'nocturnal_unclean_exit_commanded', 'camp_latrine_commanded', 'camp_holiness_required', 'escaped_slave_return_barred', 'slave_oppression_barred', 'cult_prostitution_barred', 'harlots_hire_dogs_price_barred', 'interest_to_brother_barred', 'interest_to_foreigner_permitted', 'vow_delay_barred', 'vow_refraining_permitted', 'lips_utterance_binding', 'laborer_eating_permitted', 'laborer_vessel_barred', 'sickle_swinging_barred', 'bill_of_divorce_commanded', 'divorced_wife_remarriage_permitted', 'first_husband_retaking_barred', 'newlywed_year_exemption_commanded', 'millstone_pledge_barred', 'kidnapper_death_commanded', 'leprosy_priests_teaching_commanded', 'miriam_remembrance_commanded', 'pledge_entry_barred', 'poor_mans_pledge_return_commanded', 'hireling_wage_same_day_commanded', 'hireling_oppression_barred', 'fathers_for_sons_death_barred', 'stranger_orphan_justice_commanded', 'widows_garment_pledge_barred', 'forgotten_sheaf_commanded', 'olive_second_beating_barred', 'vineyard_gleaning_barred', 'court_justification_commanded', 'lashes_by_number_commanded', 'lashes_forty_cap_declared', 'brother_degradation_barred', 'ox_muzzling_barred', 'levirate_marriage_commanded', 'widow_outsider_marriage_barred', 'firstborn_on_dead_name_commanded', 'refusal_at_gate_declared', 'shoe_loosening_rite_declared', 'house_of_unshod_named', 'wife_seizing_hand_cut_commanded', 'hand_cutting_pity_barred', 'diverse_weights_barred', 'diverse_measures_barred', 'whole_just_weight_commanded', 'amalek_remembrance_commanded', 'amalek_memory_blotting_commanded', 'amalek_forgetting_barred']
NEW_K = ['lost_thing_declared', 'garments_nest_parapet_declared', 'mixtures_tassels_declared', 'slandered_bride_declared', 'adultery_betrothed_seducer_declared', 'fathers_wife_assembly_declared', 'camp_holiness_declared', 'slave_hire_interest_declared', 'vows_law_declared', 'laborer_vineyard_grain_declared', 'divorce_declared', 'newlywed_millstone_kidnapper_declared', 'leprosy_miriam_declared', 'pledge_wage_declared', 'fathers_sons_stranger_gleanings_declared', 'lashes_declared', 'muzzle_declared', 'levirate_declared', 'wrestlers_weights_declared', 'amalek_remembrance_declared']
print('effects', len(fx), '| kinds', len(ev), '| the candidate new effects present before:', [e for e in NEW_E if e in fx], '| the candidate kinds present before:', [k for k in NEW_K if k in ev])
NEAR = re.compile(r'lost|stray|ass\b|burden|garment|dress|cloth|bird|nest|parapet|roof|seed|kilayim|mixed|mingled|plow|wool|linen|tassel|tzitzit|fringe|corner|virgin|bride|slander|hundred|stone|adulter|betroth|seduc|rap|fifty|father|wife|wives|assembl|crush|mamzer|forbidden_union|ammon|moab|edom|egypt|generation|camp|unclean|emission|latrine|spade|holy|slave|servant|oppress|harlot|prostitut|dog|hire|interest|usury|lend|loan|vow|refrain|lips|vineyard|grape|grain|sickle|divorce|bill|remarr|newlywed|year|millstone|pledge|kidnap|steal|thief|lepros|leper|priest|miriam|wage|poor|sun|cry|sin|orphan|widow|stranger|sojourn|justice|sheaf|forgot|olive|glean|lash|flog|forty|strip|degrad|muzzle|ox\b|thresh|levir|yibbum|brother|shoe|sandal|spit|refus|hand|weight|measure|ephah|amalek|remember|blot|forget|abomination|purge|pity|talion|money|hang|bur|capital|death|put_to_death|firstborn|name|inherit|balaam|curse|bless')
print('near names (effects):', sorted(e for e in fx if NEAR.search(e)))
print('near names (kinds):', sorted(k for k in ev if NEAR.search(k)))
REUSE = ('evil_purged_from_the_midst', 'pity_barred', 'talion_pity_barred', 'put_to_death', 'stoned', 'lashes', 'pays', 'exempt', 'fined', 'israel_hears_and_fears', 'abomination_barred', 'hanged', 'buried', 'same_day_burial_commanded', 'captive_release_commanded', 'fearful_exemption_commanded', 'officers_exemptions_commanded', 'bribe_barred', 'justice_perversion_barred', 'judges_charged', 'courts_established', 'interest_barred', 'pledge_returned_by_sunset', 'wages_withheld_barred', 'gleanings_left', 'corner_left', 'mixed_seed_barred', 'mixed_kinds_barred', 'just_weights_commanded', 'adulterers_put_to_death', 'seducer_pays', 'kidnapper_put_to_death', 'vow_binding', 'vow_annulled', 'leprous', 'quarantined', 'miriam_shut_out', 'amalek_memory_blotting_sworn', 'amalek_war_sworn', 'balaam_hired', 'curse_turned_to_blessing', 'sent_outside_the_camp', 'fathers_wife_barred', 'priest_divorcee_barred', 'slave_oppression_barred', 'stranger_oppression_barred', 'widow_orphan_affliction_barred', 'sin_in_you', 'needy_cry_heard', 'slave_in_egypt_remembered', 'sabbath_remembered', 'tassels_commanded', 'tzitzit_commanded', 'levirate_duty', 'seed_raised_for_brother', 'slain_by_the_lord', 'harlotry_barred', 'firstborn_by_the_head', 'inheritance_stayed_in_tribe', 'nations_devoted', 'peace_call_commanded', 'has_blood', 'blood_required', 'innocent_blood_purge_commanded')
for e in REUSE:
    r = fx.get(e); print(' E', e, '|', r['ledger_op'], '|', r['en'][:110], '| corpus', str(r.get('corpus'))[:40]) if r else print(' E', e, 'MISSING')
print('a statute kind row (hanged_burial_declared) fields:', ev.get('hanged_burial_declared', {}).get('fields'), '| form', ev.get('hanged_burial_declared', {}).get('form'), '| corpus', ev.get('hanged_burial_declared', {}).get('corpus'))
print('effects by corpus unit (the kin units):', sorted((e, r.get('ledger_op')) for e, r in fx.items() if re.search(r'exo_21|exo_22|exo_23|exo_17|lev_13|lev_14|lev_18|lev_19|lev_20|lev_21|lev_22|lev_25|num_05|num_12|num_15|num_22|num_23|num_24|num_30|gen_38|gen_20|deu_05|deu_07|deu_13|deu_15|deu_16|deu_19|deu_20|deu_21', str(r.get('corpus')))))
for k in ('purge_commanded', 'inciter_law_declared', 'witnesses_law_declared', 'war_speech_declared', 'captive_wife_declared', 'hanged_burial_declared', 'release_law_declared', 'needy_law_declared', 'hebrew_slave_law_declared', 'firstling_law_declared', 'judges_law_declared', 'ordinances_declared', 'holiness_declared', 'kilayim_declared', 'vow_law_declared', 'tzitzit_commanded', 'leprosy_law_declared', 'miriam_leprous', 'miriam_shut_out', 'amalek_war', 'amalek_blotting_sworn', 'balaam_hired', 'balaam_blessed', 'judah_tamar_case', 'onan_died', 'tamar_judged', 'camp_purity_commanded', 'unclean_sent_out', 'interest_barred', 'pledge_law_declared', 'seducer_case', 'adulterers_case', 'kidnapper_case', 'father_wife_case', 'sabbath_declared', 'decalogue_declared', 'seven_nations_case', 'abomination_declared', 'idolater_trial_declared', 'prophet_law_declared', 'king_law_declared', 'refuge_cities_declared', 'levite_dues_declared'):
    r = ev.get(k); print(' K', k, '|', r.get('form'), '|', r['en'][:130], '| corpus', str(r.get('corpus'))[:40]) if r else print(' K', k, 'MISSING')
print('==== E. THE CALENDAR (the sunset, the year, the month, the generations — clock words as parameters) ====')
cal = yaml.safe_load(open(S9 + '/calendar_parameters.yaml', encoding='utf-8'))
print(' parameters', len(cal['parameters']), '| keys naming sunset|year|month|day|generation|thirty|wage|pledge|feast:', [k for k in cal['parameters'] if re.search(r'sunset|year|month|day|generation|thirty|wage|pledge|feast', k)][:40])
print('==== F. THE KIN\'S CELLS BY STATIC SCAN (every runner\'s defs; the refs they name among the kin verses) ====')
KIN = re.compile(r'\b(Deut 2[2-5]:\d+|Exod 23:[4-9]\b|Exod 22:1[5-9]\b|Exod 22:2[0-6]\b|Exod 21:16\b|Exod 21:2[3-5]\b|Lev 19:(?:9|10|13|15|19|29|3[3-6])\b|Lev 18:8\b|Lev 20:10\b|Lev 21:7\b|Lev 22:24\b|Lev 25:3[5-9]\b|Lev 25:4[0-3]\b|Lev 13:[1-9]\b|Lev 14:[1-9]\b|Lev 15:16\b|Num 15:3[7-9]\b|Num 15:4[01]\b|Num 30:\d+|Num 12:\d+|Num 22:[5-7]\b|Num 23:7\b|Num 24:9\b|Num 5:[1-4]\b|Exod 17:(?:8|9|1[0-6])\b|Gen 38:\d+|Gen 20:3\b|Deut 5:1[2-5]\b|Deut 7:2[56]\b|Deut 12:31\b|Deut 13:6\b|Deut 15:(?:9|15)\b|Deut 16:19\b|Deut 16:20\b|Deut 17:1\b|Deut 18:12\b|Deut 19:1[39]\b|Deut 19:21\b|Deut 20:7\b|Deut 21:14\b|Deut 21:2[23]\b|Deut 27:15\b|Num 35:3[01]\b|Lev 24:(?:19|20)\b|2 Kgs 14:6\b|1 Sam 15:[2-3]\b|Ruth 4:[7-8]\b|Deut 10:1[89]\b|Exod 22:20\b|Lev 27:\d+|Deut 4:40\b|Deut 5:16\b|Deut 6:2\b|Deut 11:9\b|Exod 20:12\b|Josh 7:15\b|Gen 34:7\b|Judg 19:2[3-4]\b|2 Sam 13:12\b)')
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
        n = nall(eff)
        if n or eff in REUSE: print(' W', eff, len(n), n[:6])
    print(' NEW_E on the running world (any):', [(e, len(nall(e))) for e in NEW_E if nall(e)])
    isr = w.entities['israel'].ledger if 'israel' in w.entities else []
    print(' israel ledger entries', len(isr), '| open debits', len([e for e in isr if e.get('op') == 'debit' and not e.get('closed_by')]), '| blocks', len([e for e in isr if e.get('op') == 'block']))
    ip_ = w.entities.get('israel_people'); ipl = ip_.ledger if ip_ else []
    print(' israel_people ledger entries', len(ipl), '| blocks', len([e for e in ipl if e.get('op') == 'block']), '| statuses', len([e for e in ipl if e.get('op') == 'status']), '| the last eight effects:', [e['effect'] for e in ipl[-8:]])
    print(' entities', len(w.entities), '| closes', len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')]), '| markers', len([l for l in w.log if l[0] == 'MARKER']), '| events', len([l for l in w.log if l[0] == 'EVENT']), '| the day', w.clock.eras['exodus'].date(w.clock.day), '| population rows', len(w.tables['population']))
    last = [l[2] for l in w.log if l[0] == 'EVENT'][-6:]; print(' the tape\'s last six events:', [(e['kind'], str(e.get('case_source', ''))[:12]) for e in last])
    print(' entities naming judah|tamar|onan|amalek|miriam|balaam|moab|ammon|edom|egypt|court|priest|leper|slave|widow|orphan|stranger|the_poor|hireling|wife|bride:', sorted(k for k in w.entities if re.search(r'judah|tamar|onan|amalek|miriam|balaam|moab|ammon|edom|egypt|the_court|the_priesthood|leper|slave|widow|orphan|stranger|sojourn|poor|hire|wife|bride|harlot|firstborn', k))[:60])
except Exception as ex:
    import traceback; traceback.print_exc(); print(' THE SNAPSHOT FAILED:', repr(ex))
print('RECON DONE')
