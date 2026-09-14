#!/usr/bin/env python3
# THE NUMBERS WALK sitting 12b — THE COMPILE OF GAD AND REUBEN, Numbers 32:1-42 (2026-09-12; the owner: "Go" after the #149 rereads):
# THE MEASUREMENTS, computed BEFORE the design paragraph is typed (1b's order; midian_compile_measure.py's form). (1) the parser at 32:1-42
# and 33:1 and at the retellings' number verses; (2) the tape's state — the counter, the entities, the pending timers, the markers, the open
# entries the chapter touches (israel_people's divide_the_land, the decree's entries, caleb's entitlement, the conquests' land_possessed),
# the registry map and the HOMOGRAPH TRAPS (gad and reuben are Jacob's sons; the_pillar_of_gilead is Genesis 31's; the_men_of_war is
# Midian's party); (3) the kinds and effects on file (the recon's filtered list re-checked by name); (4) the callees live — vows (the
# utterance rule), shelach (the oath, the forty years, Caleb's entitlement), chukat (Sihon and Og, Jazer, the land east), second_census (the
# three counts; Machir's clan; the division), zelophehad (Machir's line; the tribes' plea), balak (Peor's anger), bamidbar (the census
# formula), incense_shekel (Exod 30:14's formula); (5) the engine's literals; (6) THE REGISTER GATE on chapter 32 — its count lines, receipts,
# footers and register headers computed on the running world; (7) the recorder and the stitcher.
import sqlite3, sys, io, re, contextlib, collections, inspect, os, yaml
ROOT = '<repo-old>'
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import world_engine as WE
    import cold_run_vows as VW
    import cold_run_shelach as SL
    import cold_run_chukat as CK
    import cold_run_second_census as C2
    import cold_run_zelophehad as ZL
    import cold_run_balak as BK
    import cold_run_bamidbar as BM
    import cold_run_incense_shekel as IS
    import register_census as RG
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
db = sqlite3.connect(f'file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph, w.lemma FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by = collections.OrderedDict()
for b, c, v, he, m, lm in rows:
    by.setdefault((b, c, v), []).append((he, m, lm))
def words(b, c, v): return [plain(x) for x, _, _ in by[(b, c, v)]]

print('==== (1) THE PARSER AT 32:1-42 and 33:1 — numbers, ordinals, the marked tokens ====')
for v in range(1, 43):
    vw = CS.verse_words('Num', 32, v)
    marked = [t for t in vw if re.search(r'[#^~%@|*]', t)]
    n, o = N('Num', 32, v), O('Num', 32, v)
    if n or o or marked:
        print('  Num 32:%-3d numbers %-20s ordinals %-8s marked %s' % (v, n, o, marked))
print('  Num 33:1   numbers %s ordinals %s' % (N('Num', 33, 1), O('Num', 33, 1)))
print('---- the retellings and the callees\' number verses ----')
for k in [('Josh', 4, 13), ('Josh', 13, 30), ('1 Chr', 5, 18), ('Deut', 3, 4), ('Deut', 3, 14), ('Judg', 10, 4), ('1 Kgs', 4, 13), ('1 Chr', 2, 22), ('Deut', 2, 14), ('Num', 14, 33), ('Num', 14, 34), ('Num', 26, 7), ('Num', 26, 18), ('Num', 26, 34), ('Num', 26, 29), ('Num', 1, 21), ('Num', 1, 25), ('Num', 1, 35), ('Exod', 30, 14), ('Num', 1, 3), ('Num', 26, 2), ('Josh', 22, 8)]:
    if k in by:
        vw = CS.verse_words(*k)
        print('  %s %d:%d numbers %s ordinals %s   words: %s' % (k[0], k[1], k[2], CS.ink_numbers(vw), CS.ink_ordinals(vw), ' '.join(words(*k))[:150]))
    else:
        print('  %s NOT IN DB under that book key' % (k,))
print('  the DB\'s book keys: %s' % sorted({b for b, _, _ in by})[:50])

print('\n==== (2) THE TAPE\'S STATE — the running world ====')
with contextlib.redirect_stdout(io.StringIO()):
    w = RG.running_world()
ex = w.clock.eras['exodus']
def dt(d):
    try: return ex.date(d)
    except BaseException: return ('pre-exodus day', d)
print('  the counter: day %d = %s (exodus era); entities %d; log lines %d; timers pending %d' % (w.clock.day, ex.date(w.clock.day), len(w.entities), len(w.log), len(w.timers)))
print('  the pending timers: %s' % [(t[1].get('subject'), t[1].get('effect'), t[1].get('period'), ex.date(t[0])[1:]) for t in w.timers])
tset = [l for l in w.log if l[0] == 'TIMER-SET']; tfire = [l for l in w.log if l[0] == 'TIMER-FIRE']; tcan = [l for l in w.log if l[0] == 'TIMER-CANCEL']
print('  TIMER-SET %d, TIMER-FIRE %d, TIMER-CANCEL %d' % (len(tset), len(tfire), len(tcan)))
print('  the fired timers naming forty/thirty-eight/decree/wilderness: %s' % [(l[2].get('subject'), l[2].get('effect'), dt(l[1])) for l in tfire if re.search(r'forty|38|thirty|decree|wilderness|generation|die', str(l[2]))][:12])
mk = [l for l in w.log if l[0] == 'MARKER']
print('  markers %d; the last four: %s' % (len(mk), [(l[2].get('verse'), ex.date(l[1]), l[2].get('placement')) for l in mk[-4:]]))
EVs = [l for l in w.log if l[0] == 'EVENT']
print('  events %d; the last six kinds and sources: %s' % (len(EVs), [(l[2]['kind'], str(l[2].get('case_source', ''))[:40], l[2].get('placement')) for l in EVs[-6:]]))
for pat in ('Num 32', 'Num 14:2', 'Num 14:3', 'Num 21:2', 'Num 21:3', 'Num 26:5', 'Num 27:1', 'Num 36:'):
    hits = [(l[2]['kind'], l[2].get('subject'), str(l[2].get('case_source', ''))[:50]) for l in EVs if pat in str(l[2].get('case_source', ''))]
    print('  events citing %-8s: %d %s' % (pat, len(hits), hits[:10]))
reg_map = CS.registry_map()
TOK = ('israel', 'moses', 'eleazar', 'joshua', 'caleb', 'gad', 'reuben', 'sihon', 'og', 'the-amorite', 'the-amorites', 'the-sons-of-machir', 'the-heads-of-gilead', 'the-pillar-of-gilead', 'the-land-of-canaan', 'canaan', 'the-men-of-war', 'the-levites', 'the-court', 'the-tent-of-meeting', 'the-tabernacle', 'joseph', 'jacob', 'the-heads-of-the-tribes', 'the-princes')
print('  registry_map for the tokens: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  tokens with NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])
print('  entity ids present among: %s' % [t for t in TOK if reg_map.get(t, t) in w.entities])
def ent(t): return w.entities.get(reg_map.get(t, t))
for t in ('israel', 'moses', 'eleazar', 'joshua', 'caleb', 'gad', 'reuben', 'sihon', 'og', 'the-amorite', 'the-sons-of-machir', 'the-heads-of-gilead', 'the-land-of-canaan', 'the-men-of-war', 'the-court', 'the-tabernacle'):
    e = ent(t)
    if e is None: print('  %-20s NO ENTITY' % t); continue
    opens = [(x['effect'], x.get('value'), x.get('cp'), str(x.get('case_source', ''))[:24]) for x in e.ledger if x.get('open')]
    print('  %-20s id %-24s kind %-10s ledger %3d; OPEN %d: %s' % (t, e.eid, getattr(e, 'kind', '?'), len(e.ledger), len(opens), opens[:16]))
    if t in ('caleb', 'joshua', 'sihon', 'og', 'gad', 'reuben', 'the-sons-of-machir', 'the-amorite'):
        print('     ledger whole: %s' % [(x['effect'], str(x.get('value'))[:40], x.get('op'), x.get('open'), str(x.get('case_source', ''))[:20]) for x in e.ledger][:20])
isr = ent('israel')
cmd = [x for x in isr.ledger if x['effect'] == 'commanded']
print('  israel commanded entries %d; the OPEN ones: %s' % (len(cmd), [(x.get('value'), x.get('cp'), str(x.get('case_source'))[:20]) for x in cmd if x.get('open')]))
print('  the divide_the_land entry: %s' % [{k_: (str(v_)[:90] if k_ != 'law' else str(v_)[:60]) for k_, v_ in x.items()} for x in cmd if x.get('value') == 'divide_the_land'])
for eff in ('land_possessed', 'land_granted', 'land_promised', 'decreed', 'barred_from_the_land', 'die_in_the_wilderness', 'wander', 'counted'):
    hits = [(e_.eid, x.get('value'), x.get('op'), x.get('open'), str(x.get('case_source', ''))[:22]) for e_ in w.entities.values() for x in e_.ledger if x['effect'] == eff]
    print('  entries with effect %-22s: %d %s' % (eff, len(hits), hits[:10]))
print('  effects on israel_people naming the decree (shelach\'s writes at Num 14): %s' % sorted({x['effect'] for x in isr.ledger if 'Num 14' in str(x.get('case_source', ''))}))
print('  all effects on israel_people from Num 13-14, 21, 26, 27: %s' % [(x['effect'], str(x.get('value'))[:30], x.get('open'), str(x.get('case_source', ''))[:14]) for x in isr.ledger if re.match(r'Num (13|14|21|26|27):', str(x.get('case_source', '')))][:40])
print('  the clock: day + 1 = %s' % (ex.date(w.clock.day + 1),))
inst = w.installation
print('  installation: setting %s; skipped %s; would_skip %s; fields %d' % (inst['setting'] if inst else None, inst['skipped'] if inst else None, inst['would_skip'] if inst else None, len(inst['fields']) if inst else 0))
subj = collections.Counter(l[2].get('subject') for l in EVs)
print('  subjects on the tape naming gad/reuben/manasseh/machir/gilead/joshua/caleb/sihon/og/amorite: %s' % {s: n for s, n in subj.items() if s and re.search(r'gad|reuben|manasseh|machir|gilead|joshua|yehoshua|caleb|sihon|\bog\b|amorite', s)})
print('  population table rows for gad / reuben / manasseh (as_of, count): %s' % [(r.get('tribe'), r.get('as_of'), r.get('count'), r.get('family')) for r in w.population(tribe='gad')] if hasattr(w, 'population') else None)
print('  the tribe rows in the population table (grain counted, level tribe): %s' % [(r.get('tribe'), r.get('as_of'), r.get('count')) for r in w.population(level='tribe')][:30])

print('\n==== (3) THE KINDS AND EFFECTS ON FILE ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
cand_kinds = ['land_requested', 'land_asked', 'tribes_requested_the_land', 'moses_rebuked_the_tribes', 'oath_retold', 'tribes_offered_to_arm', 'condition_stipulated', 'condition_accepted', 'commission_charged', 'land_granted', 'cities_built', 'cities_renamed', 'gilead_taken', 'villages_taken', 'kenath_taken', 'tribes_approached', 'command_relayed', 'land_division_commanded', 'land_promised', 'israel_dwelt_and_jazer_taken', 'heshbon_and_the_parable', 'plea_brought', 'daughters_approached', 'city_built', 'stipulation_case', 'clearance_case', 'land_east_case', 'oath_case']
print('  kinds on file among the candidates:', [k for k in cand_kinds if k in E])
print('  kinds NOT on file:', [k for k in cand_kinds if k not in E])
for k in ('tribes_approached', 'command_relayed', 'land_division_commanded', 'land_promised', 'israel_dwelt_and_jazer_taken', 'cities_built', 'city_built', 'daughters_approached', 'heshbon_and_the_parable'):
    if k in E: print('    %-32s form %-7s seats %s\n        %s' % (k, E[k].get('form'), str(E[k].get('seats', E[k].get('verses', '')))[:120], str(E[k].get('en', ''))[:200].replace('\n', ' ')))
print('  a kind row\'s full shape (israel_dwelt_and_jazer_taken): %s' % E.get('israel_dwelt_and_jazer_taken'))
cand_fx = ['commanded', 'land_possessed', 'land_granted', 'holding_given', 'holding_owed', 'dwelling_granted', 'portion_added', 'name_changed', 'name_given', 'oath_sworn', 'sworn_by_himself', 'cities_built', 'city_built', 'inheritance_barred', 'mark_of_anger', 'counted', 'accepted', 'entitled', 'possession_entitled', 'clear_before_the_lord', 'sin_will_find', 'armed_to_cross', 'crossed_armed', 'subdued', 'rest_given', 'land_subdued', 'vow_bound', 'exempt', 'wander', 'wandered', 'consumed', 'died_in_the_wilderness', 'pardoned', 'decreed', 'stipulated', 'condition_bound']
print('  effects on file among the candidates:', [f for f in cand_fx if f in F])
print('  effects NOT on file:', [f for f in cand_fx if f not in F])
for f in ('land_possessed', 'land_granted', 'holding_given', 'holding_owed', 'dwelling_granted', 'name_changed', 'cities_built', 'city_built', 'oath_sworn', 'commanded', 'accepted', 'vow_bound', 'mark_of_anger', 'inheritance_barred'):
    if f in F: print('   %-22s %-8s he=%s\n        %s' % (f, F[f].get('ledger_op'), str(F[f].get('he', ''))[:80], str(F[f].get('en', ''))[:260].replace('\n', ' ')))
print('  an effect row\'s full shape (holding_given): %s' % F.get('holding_given'))
print('  the ledger_op values in use: %s' % dict(collections.Counter(F[f].get('ledger_op') for f in F)))

print('\n==== (4) THE CALLEES ON FILE, live ====')
def tryc(label, f):
    try:
        r = f(); print('  ', label, '->', str(r)[:420])
    except BaseException as e:
        print('  ', label, 'raised', type(e).__name__, str(e)[:200])
src_vw = open(inspect.getsourcefile(VW), encoding='utf-8').read()
tryc('VW.the_man(all_that_proceeds)', lambda: VW.the_man({'ask': 'all_that_proceeds'}, VW.DATA)[:2])
tryc('VW.the_man(frame)', lambda: VW.the_man({'ask': 'frame'}, VW.DATA)[:2])
tryc('VW.the_man(this_is_the_thing)', lambda: VW.the_man({'ask': 'this_is_the_thing'}, VW.DATA)[:2])
tryc('VW.the_man(heads_of_the_tribes)', lambda: VW.the_man({'ask': 'heads_of_the_tribes'}, VW.DATA)[:2])
tryc('VW.the_man(delay_clocks)', lambda: VW.the_man({'ask': 'delay_clocks'}, VW.DATA)[:2])
tryc('VW.the_man(vow_vs_oath)', lambda: VW.the_man({'ask': 'vow_vs_oath'}, VW.DATA)[:2])
tryc('VW.the_statutes asks', lambda: sorted(set(re.findall(r"ask == '([a-z_]+)'", src_vw[src_vw.find('def the_statutes('):src_vw.find('def law_vows(')]))))
tryc('VW.HEADS / FOOTER / LINE / NUMBERS', lambda: (VW.HEADS, VW.FOOTER, VW.LINE, VW.NUMBERS))
tryc('VW.DATA hearing_of_the_law / vow_support_base', lambda: (VW.DATA['hearing_of_the_law'], VW.DATA['vow_support_base']))
tryc('SL.decree(as_i_live)', lambda: SL.decree({'ask': 'as_i_live'}, SL.DATA)[:2])
tryc('SL.decree(count_from)', lambda: SL.decree({'ask': 'count_from'}, SL.DATA)[:2])
tryc('SL.decree(day_for_year)', lambda: SL.decree({'ask': 'day_for_year'}, SL.DATA)[:2])
tryc('SL.decree(due)', lambda: SL.decree({'ask': 'due'}, SL.DATA)[:2])
tryc('SL.decree(exceptions)', lambda: SL.decree({'ask': 'exceptions'}, SL.DATA)[:2])
tryc('SL.decree(caleb_entitlement)', lambda: SL.decree({'ask': 'caleb_entitlement'}, SL.DATA)[:2])
tryc('SL.decree(wilderness_share)', lambda: SL.decree({'ask': 'wilderness_share'}, SL.DATA)[:2])
tryc('SL.decree(set)', lambda: SL.decree({'ask': 'set'}, SL.DATA)[:2])
tryc('SL.decree(set_edges)', lambda: SL.decree({'ask': 'set_edges'}, SL.DATA)[:2])
tryc('SL.decree(congregation)', lambda: SL.decree({'ask': 'congregation'}, SL.DATA)[:2])
tryc('SL.decree(deaths_ceased)', lambda: SL.decree({'ask': 'deaths_ceased'}, SL.DATA)[:2])
tryc('SL.decree(upon_children)', lambda: SL.decree({'ask': 'upon_children'}, SL.DATA)[:2])
tryc('SL.decree(ten_trials)', lambda: SL.decree({'ask': 'ten_trials'}, SL.DATA)[:2])
tryc('SL.decree(pardon)', lambda: SL.decree({'ask': 'pardon'}, SL.DATA)[:2])
tryc('SL.spies(eshcol)', lambda: SL.spies({'ask': 'eshcol'}, SL.DATA)[:2])
tryc('SL.spies(one_per_tribe)', lambda: SL.spies({'ask': 'one_per_tribe'}, SL.DATA)[:2])
tryc('SL.spies(joshua_name)', lambda: SL.spies({'ask': 'joshua_name'}, SL.DATA)[:2])
tryc('SL.spies(send_for_yourself)', lambda: SL.spies({'ask': 'send_for_yourself'}, SL.DATA)[:2])
tryc('SL.spies(forty_days)', lambda: SL.spies({'ask': 'forty_days'}, SL.DATA)[:2])
tryc('SL.spies(joshua_caleb_equal)', lambda: SL.spies({'ask': 'joshua_caleb_equal'}, SL.DATA)[:2])
tryc('SL.spies(caleb_hushed)', lambda: SL.spies({'ask': 'caleb_hushed'}, SL.DATA)[:2])
tryc('SL.FORTY / FORTY_YEARS / DUE_38 / DAY_YEAR / GENERATIONS / E34 / JOSHUA_BEFORE / N18', lambda: (SL.FORTY, SL.FORTY_YEARS, SL.DUE_38, SL.DAY_YEAR, SL.GENERATIONS, SL.E34, SL.JOSHUA_BEFORE, SL.N18))
tryc('SL.DATA count_from / deaths_ceased / spies_share / the_ten_trials / return_day', lambda: {k: SL.DATA[k] for k in ('count_from', 'deaths_ceased', 'spies_share', 'the_ten_trials', 'return_day')})
tryc('CK.well_and_kings(land_east)', lambda: CK.well_and_kings({'ask': 'land_east'}, CK.DATA)[:2])
tryc('CK.well_and_kings(deut3_delta)', lambda: CK.well_and_kings({'ask': 'deut3_delta'}, CK.DATA)[:2])
tryc('CK.well_and_kings(og_lore)', lambda: CK.well_and_kings({'ask': 'og_lore'}, CK.DATA)[:2])
tryc('CK.well_and_kings(joshua_refrain)', lambda: CK.well_and_kings({'ask': 'joshua_refrain'}, CK.DATA)[:2])
tryc('CK.well_and_kings(sihon_refused)', lambda: CK.well_and_kings({'ask': 'sihon_refused'}, CK.DATA)[:2])
tryc('CK.well_and_kings(sihon_purified)', lambda: CK.well_and_kings({'ask': 'sihon_purified'}, CK.DATA)[:2])
tryc('CK.well_and_kings(from_his_hand)', lambda: CK.well_and_kings({'ask': 'from_his_hand'}, CK.DATA)[:2])
tryc('CK.well_and_kings(spy_verb)', lambda: CK.well_and_kings({'ask': 'spy_verb'}, CK.DATA)[:2])
tryc('CK.well_and_kings(ammon_border)', lambda: CK.well_and_kings({'ask': 'ammon_border'}, CK.DATA)[:2])
tryc('CK.well_and_kings(lawgiver)', lambda: CK.well_and_kings({'ask': 'lawgiver'}, CK.DATA)[:2])
tryc('CK.DATA og_lore / sihon_purified / captive_count', lambda: {k: CK.DATA[k] for k in ('og_lore', 'sihon_purified', 'captive_count')})
tryc('CK.D_DUE38 / D33 / D34 / D35 / JER', lambda: (CK.D_DUE38, CK.D33, CK.D34, CK.D35, str(CK.JER)[:200]))
tryc('C2.the_roll(twelve_counts)', lambda: C2.the_roll({'ask': 'twelve_counts'}, C2.DATA)[:2])
tryc('C2.the_roll(total)', lambda: C2.the_roll({'ask': 'total'}, C2.DATA)[:2])
tryc('C2.the_roll(families)', lambda: C2.the_roll({'ask': 'families'}, C2.DATA)[:2])
tryc('C2.the_roll(deltas)', lambda: C2.the_roll({'ask': 'deltas'}, C2.DATA)[:2])
tryc('C2.the_roll(daughters_row)', lambda: C2.the_roll({'ask': 'daughters_row'}, C2.DATA)[:2])
tryc('C2.the_land(by_lot)', lambda: C2.the_land({'ask': 'by_lot'}, C2.DATA)[:2])
tryc('C2.the_land(land_divided_among)', lambda: C2.the_land({'ask': 'land_divided_among'}, C2.DATA)[:2])
tryc('C2.the_land(thirteen_tribes)', lambda: C2.the_land({'ask': 'thirteen_tribes'}, C2.DATA)[:2])
tryc('C2.the_land(ten_parts)', lambda: C2.the_land({'ask': 'ten_parts'}, C2.DATA)[:2])
tryc('C2.the_land(possession_before_assignment)', lambda: C2.the_land({'ask': 'possession_before_assignment'}, C2.DATA)[:2])
tryc('C2.the_land(tribes_or_skulls)', lambda: C2.the_land({'ask': 'tribes_or_skulls'}, C2.DATA)[:2])
tryc('C2.the_land(morasha)', lambda: C2.the_land({'ask': 'morasha'}, C2.DATA)[:2])
tryc('C2.the_rolls(except_caleb_joshua)', lambda: C2.the_rolls({'ask': 'except_caleb_joshua'}, C2.DATA)[:2])
tryc('C2.the_rolls(decree_consumed)', lambda: C2.the_rolls({'ask': 'decree_consumed'}, C2.DATA)[:2])
tryc('C2.C26 (the counts)', lambda: C2.C26)
tryc('C2.C1', lambda: C2.C1)
tryc('C2.FAMILIES gad / reuben / manasseh', lambda: {k: v for k, v in (C2.FAMILIES.items() if isinstance(C2.FAMILIES, dict) else enumerate(C2.FAMILIES)) if re.search(r'gad|reuben|manasseh|machir|gilead', str(k) + str(v))})
tryc('C2.HOUSES', lambda: C2.HOUSES)
tryc('C2.DATA thirteen_tribes / division_by / wilderness_survivors / decree_age_edges', lambda: {k: C2.DATA[k] for k in ('thirteen_tribes', 'division_by', 'wilderness_survivors', 'decree_age_edges')})
tryc('ZL.the_daughters(tribes_plea)', lambda: ZL.the_daughters({'ask': 'tribes_plea'}, ZL.DATA)[:2])
tryc('ZL.the_daughters(reach)', lambda: ZL.the_daughters({'ask': 'reach'}, ZL.DATA)[:2])
tryc('ZL.the_daughters(the_run)', lambda: ZL.the_daughters({'ask': 'the_run'}, ZL.DATA)[:2])
tryc('ZL.the_daughters(identity)', lambda: ZL.the_daughters({'ask': 'identity'}, ZL.DATA)[:2])
tryc('ZL.the_daughters(three_portions)', lambda: ZL.the_daughters({'ask': 'three_portions'}, ZL.DATA)[:2])
tryc('ZL.inheritance_order(land_status)', lambda: ZL.inheritance_order({'ask': 'land_status'}, ZL.DATA)[:2])
tryc('ZL.inheritance_order(apportionment)', lambda: ZL.inheritance_order({'ask': 'apportionment'}, ZL.DATA)[:2])
tryc('ZL.inheritance_order(ten_parts)', lambda: ZL.inheritance_order({'ask': 'ten_parts'}, ZL.DATA)[:2])
tryc('ZL.HOUSES_17_2 / FAM / NO_SON_SEATS', lambda: (ZL.HOUSES_17_2, ZL.FAM, ZL.NO_SON_SEATS))
tryc('ZL.DATA eretz_yisrael_status / tribe_transfer_reach / land_divided_among', lambda: {k: ZL.DATA[k] for k in ('eretz_yisrael_status', 'tribe_transfer_reach', 'land_divided_among')})
src_bk = open(inspect.getsourcefile(BK), encoding='utf-8').read()
for d in ('census', 'the_call', 'the_stands', 'peor', 'phinehas_and_midian'):
    i = src_bk.find('\ndef %s(' % d); j = src_bk.find('\ndef ', i + 1)
    print('  BK.%s asks: %s' % (d, sorted(set(re.findall(r"'([a-z_0-9]+)'", src_bk[i:j][:200])))[:12], ))
    print('     the cell\'s first lines: %s' % src_bk[i:i + 260].replace('\n', ' | '))
tryc('BK.DATA moment_of_anger / zealot_rule / midian_command_run', lambda: {k: BK.DATA[k] for k in ('moment_of_anger', 'zealot_rule', 'midian_command_run')})
tryc('BK.ATONED_FOR / DWELT', lambda: (BK.ATONED_FOR, BK.DWELT))
tryc('BM.census(threshold)', lambda: BM.census({'ask': 'threshold'}, BM.DATA)[:2])
tryc('BM.census(total)', lambda: BM.census({'ask': 'total'}, BM.DATA)[:2])
tryc('BM.census(three_seats)', lambda: BM.census({'ask': 'three_seats'}, BM.DATA)[:2])
tryc('BM.census(orders)', lambda: BM.census({'ask': 'orders'}, BM.DATA)[:2])
tryc('BM.TRIBES / TOTAL / TOTAL_2 / TWELVE', lambda: (BM.TRIBES, BM.TOTAL, BM.TOTAL_2, BM.TWELVE))
tryc('BM.DATA threshold_edge', lambda: BM.DATA['threshold_edge'])
src_is = open(inspect.getsourcefile(IS), encoding='utf-8').read()
i = src_is.find('\ndef shekel('); j = src_is.find('\ndef ', i + 1)
print('  IS.shekel asks: %s' % sorted(set(re.findall(r"q == '([a-z_]+)'", src_is[i:j])) | set(re.findall(r"'([a-z_]+)':\s*\{", src_is[i:j])))[:60])
for q in ('twenty', 'twenty_and_upward', 'age', 'threshold', 'lift_head', 'trigger_parameter', 'numbers_no_shekel', 'passing_over'):
    tryc('IS.shekel(%s)' % q, lambda q=q: {k_: (str(v_)[:160] if k_ != 'fx' else v_) for k_, v_ in IS.shekel(q).items()})
def defs(mod): return re.findall(r'^def ([a-z_0-9]+)\(', open(inspect.getsourcefile(mod), encoding='utf-8').read(), re.M)
for name, mod in (('vows', VW), ('shelach', SL), ('chukat', CK), ('second_census', C2), ('zelophehad', ZL), ('balak', BK), ('bamidbar', BM)):
    s = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    print('  %-14s imports %s' % (name, sorted(set(re.findall(r'^\s*import (cold_run_\w+)', s, re.M)))))

print('\n==== (5) THE ENGINE\'S LITERALS ====')
print('  DAEMON_ORDER length %d, last %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-1]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s\n  SLOTS %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT, CS.SLOTS))
print('  installation_probes I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
reg = yaml.safe_load(open(f'{ROOT}/logic/corpus/entity_registry.yaml', encoding='utf-8'))
print('  registry entities %d' % len(reg['entities']))
for e in reg['entities']:
    if e['id'] in ('gad', 'reuben', 'the_amorite', 'the_pillar_of_gilead', 'the_sons_of_machir', 'the_heads_of_gilead', 'caleb', 'sihon', 'og', 'yehoshua', 'the_land_of_canaan', 'the_men_of_war', 'the_midianites'):
        print('    %s' % {k: (str(v)[:200] if k == 'en' else v) for k, v in e.items()})
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  daemons %d; installed_by values: %s' % (len(dd['daemons']), dict(collections.Counter(v.get('installed_by') for v in dd['daemons'].values()))))
print('  the law_midian block whole: %s' % dd['daemons']['law_midian'])
print('  the functions block midian: %s' % {k: v for k, v in dd.get('functions', {}).items() if k == 'midian'})
print('  the top-level keys of daemon_dispositions: %s' % list(dd))
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers at Num 32: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if str(p.get('verse', '')).startswith('Num 32')]))
print('  the midian edges on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], e.get('taught_by')) for e in dep['edges'] if e['from'] == 'midian' or e['to'] == 'midian'])
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  command_relayed: %s' % {k: str(v)[:200] for k, v in ip['installing_acts']['command_relayed'].items()})
cal = yaml.safe_load(open(f'{ROOT}/World/step9/calendar_parameters.yaml', encoding='utf-8'))
P_ = cal['parameters'] if 'parameters' in cal else cal
print('  calendar_parameters rows %d; rows naming forty/wilderness/decree/year: %s' % (len(P_), [k for k in P_ if re.search(r'forty|wilderness|decree|thirty|year', k)]))
ps = yaml.safe_load(open(f'{ROOT}/World/step9/population_schema.yaml', encoding='utf-8'))
print('  population_schema keys: %s' % list(ps))

print('\n==== (6) THE REGISTER GATE on chapter 32 — count lines, receipts, footers, registers (computed on the running world) ====')
ink = RG.read_ink()
cc = RG.class_counts(ink, w)
print('  count lines in Num 32: %s' % [(r, d['class'], d['noun'], d.get('counts'), d.get('measures')) for r, d in cc.items() if r.startswith('Num 32:')])
cr = RG.class_receipts(ink, w)
print('  receipts in Num 32: %s' % [(r, d['class'], d['evidence']) for r, d in cr.items() if r.startswith('Num 32:')])
cf = RG.class_footers(ink)
print('  footers naming Num 3x: %s' % {k: (v['class'] if isinstance(v, dict) else v) for k, v in cf.items() if 'Num 3' in k})
try:
    rh = RG.register_headers(ink)
    print('  register headers in Num 32: %s' % [(k, v) for k, v in (rh.items() if isinstance(rh, dict) else enumerate(rh)) if 'Num 32' in str(k) + str(v)][:5])
except BaseException as e:
    print('  register_headers raised', type(e).__name__, str(e)[:120])
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  declared seats in Num 32 (counts / receipts / footers / registers): %s' % [(sec, [k for k in decl.get(sec, {}) if 'Num 32' in k]) for sec in ('counts', 'receipts', 'footers', 'registers')])
print('  declared counts %d receipts %d footers %d registers %d' % tuple(len(decl.get(s, {})) for s in ('counts', 'receipts', 'footers', 'registers')))
print('  Num 32 verses with a count-noun (6485 / 4557 / 5315): %s' % [(v, [lm for _, _, lm in by[('Num', 32, v)] if lm.split('/')[-1].split(' ')[0] in ('6485', '4557', '5315')]) for v in range(1, 43) if any(lm.split('/')[-1].split(' ')[0] in ('6485', '4557', '5315') for _, _, lm in by[('Num', 32, v)])])
print('  Num 32 verses with the receipt formula lemmas (834 + 6680 + 3068): %s' % [v for v in range(1, 43) if {'834', '6680', '3068'} <= {lm.split('/')[-1].split(' ')[0] for _, _, lm in by[('Num', 32, v)]}])

print('\n==== (7) THE RECORDER/STITCHER ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
print('  import lines for the walk\'s runners: %s' % re.findall(r'^import (cold_run_(?:vows|midian|second_census|balak|zelophehad))', src_cs, re.M))
SP = os.path.dirname(os.path.abspath(__file__))
st = open(f'{SP}/seq_stitch.py', encoding='utf-8').read()
print('  seq_stitch SPAN_ORDER: %s' % re.findall(r"SPAN_ORDER\s*=\s*\[([^\]]*)\]", st)[:1])
rc = open(f'{SP}/seq_record.py', encoding='utf-8').read()
print('  seq_record recording path: %s' % re.findall(r"seq_recording\.json[^\n]*", rc)[:2])
print('  the tape section sentinels present: %s %s' % ('# ==== TAPE BEGIN' in src_cs, '# ==== TAPE END ====' in src_cs))
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
print('  the tape\'s Num 31 last line and Num 36 first line: %s' % [l[:140] for l in tape.split('\n') if 'officers_gold_brought' in l or 'tribes_approached' in l])
print('  cp() checkpoints on file: %s' % re.findall(r"cp\('(C[A-Z]\d)'", src_cs)[-12:])
print('  VERDICTS entries naming CX: %s' % re.findall(r"\('(CX\d)'[^\n]{0,80}", src_cs)[:9])
