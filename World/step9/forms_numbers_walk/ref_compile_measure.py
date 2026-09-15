import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 15b — THE COMPILE OF THE REFUGE CITIES, Numbers 35:1-34 (2026-09-13; the owner: "Go" after the #158 rereads):
# THE MEASUREMENTS, computed BEFORE the design paragraph is typed (1b's order; bor_compile_measure.py's form; every call typed from
# ref_compile_recon.out). (1) the parser at 35:1-34 (the runner measure holds the dual's 29 seats); (2) the tape's state — the counter, the
# Levites' ledger, Eleazar's succession and the priesthood's holder, the burglar's has_blood entries on the exam worlds (none on the tape),
# israel_people's commanded entries (the global counts CV2 / CX2 / CZ2 as they stand), the land of Canaan, the court, the tent of meeting
# (in_force), the entities the chapter names; (3) the kinds and effects on file; (4) the callees live; (5) the installation forms and the
# global-count checkpoints; (6) THE REGISTER GATE on chapter 35; (7) the recorder and the stitcher; (8) the engine's timer interface (a due
# keyed to an act, not a day — the term's form).
import sqlite3, sys, io, re, contextlib, collections, inspect, os, yaml
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import world_engine as WE
    import cold_run_mishpatim_3 as M3
    import cold_run_mishpatim as M1
    import cold_run_lev24 as L24
    import cold_run_shelach as SL
    import cold_run_vayikra5 as V5
    import cold_run_naso as NS
    import cold_run_second_census as C2
    import cold_run_journeys as JO
    import cold_run_borders as BO
    import cold_run_zelophehad as ZL
    import cold_run_gad_reuben as GR
    import cold_run_chukat as CK
    import cold_run_primeval as PR
    import cold_run_bamidbar as CB
    import cold_run_decalogue as DC
    import cold_run_priesthood as PH
    import cold_run_mekoshesh as MK
    import cold_run_sanctions as SA
    import cold_run_balak as BK
    import register_census as RG
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))

print('==== (1) THE PARSER AT 35:1-34 — numbers, ordinals, the marked tokens ====')
for v in range(1, 35):
    vw = CS.verse_words('Num', 35, v)
    marked = [t for t in vw if re.search(r'[#^~%@|*]', t)]
    n, o = N('Num', 35, v), O('Num', 35, v)
    if n or o or marked:
        print('  Num 35:%-3d numbers %-12s ordinals %-8s marked %s' % (v, n, o, marked))
print('  Num 36:1   numbers %s ordinals %s' % (N('Num', 36, 1), O('Num', 36, 1)))

print('\n==== (2) THE TAPE\'S STATE — the running world ====')
with contextlib.redirect_stdout(io.StringIO()):
    w = RG.running_world()
ex = w.clock.eras['exodus']
def dt(d):
    try: return ex.date(d)
    except BaseException: return ('pre-exodus day', d)
print('  the counter: day %d = %s (exodus era); entities %d; log lines %d; timers pending %d' % (w.clock.day, ex.date(w.clock.day), len(w.entities), len(w.log), len(w.timers)))
EVs = [l for l in w.log if l[0] == 'EVENT']
print('  events %d; the last five kinds: %s' % (len(EVs), [(l[2]['kind'], str(l[2].get('case_source', ''))[:30], dt(l[1])) for l in EVs[-5:]]))
mk = [l for l in w.log if l[0] == 'MARKER']
print('  markers %d; the last three: %s' % (len(mk), [(l[2].get('verse'), dt(l[1]), l[2].get('placement')) for l in mk[-3:]]))
reg_map = CS.registry_map()
def ent(t): return w.entities.get(reg_map.get(t, t))
def show(t, n=40):
    e = ent(t)
    if e is None: print('  %-28s NO ENTITY on the running world (registry id %s)' % (t, reg_map.get(t))); return
    print('  %-28s id %-26s kind %-8s ledger %3d; OPEN %d' % (t, e.eid, getattr(e, 'kind', '?'), len(e.ledger), sum(1 for x in e.ledger if x.get('open'))))
    for x in e.ledger[:n]:
        print('     %-34s %-60s op %-8s open %-5s cp %-24s day %-16s src %s' % (x['effect'], str(x.get('value'))[:60], x.get('op'), x.get('open'), str(x.get('cp'))[:24], dt(x.get('day')), str(x.get('case_source', ''))[:36]))
for t in ('the-levites', 'eleazar', 'aaron', 'the-priesthood', 'the-court', 'the-tent-of-meeting', 'the-tabernacle', 'the-land-of-canaan', 'the-land', 'canaan', 'joshua', 'the-dividers-of-the-land', 'the-sons-of-gad', 'the-sons-of-reuben', 'the-half-tribe-of-manasseh', 'the-unclean-of-the-camp', 'the-three-thousand', 'aaron-and-sons'):
    show(t)
isr = ent('israel')
cmd = [x for x in isr.ledger if x['effect'] == 'commanded']
print('  israel_people ledger %d; commanded entries %d (CV2\'s len(cmd_v) kin): %s' % (len(isr.ledger), len(cmd), [(str(x.get('value'))[:44], x.get('open'), str(x.get('case_source', ''))[:14]) for x in cmd]))
print('  israel_people OPEN commanded entries %d (CX2\'s kin): %s' % (sum(1 for x in cmd if x.get('open')), [str(x.get('value'))[:44] for x in cmd if x.get('open')]))
print('  the newest commanded entry on israel_people: %s' % (str(cmd[-1].get('value'))[:60] if cmd else None))
print('  israel_people OPEN entries (all effects): %s' % [(x['effect'], str(x.get('value'))[:40], x.get('cp'), str(x.get('case_source', ''))[:20]) for x in isr.ledger if x.get('open')])
print('  ENTRIES ANYWHERE naming priest / anoint / in_force / presence / blood / refuge / flee / has_blood / put_to_death / beheaded / exile / land (effect, value, op, open, source):')
for e_ in w.entities.values():
    for x in e_.ledger:
        s = str(x.get('effect')) + ' ' + str(x.get('value')) + ' ' + str(x.get('case_source'))
        if re.search(r'priest|anoint|in_force|presence|has_blood|refuge|flee|put_to_death|beheaded|exile|blood_required|blood_reckoned|land_defiled|polluted|defiled|enmity', s, re.I):
            print('     %-28s %-30s %-64s %-8s %-5s %s' % (e_.eid, x['effect'], str(x.get('value'))[:64], x.get('op'), x.get('open'), str(x.get('case_source', ''))[:36]))
print('  the entities whose id names levi|priest|eleazar|aaron|canaan|land|court|tent|congregation|city|refuge|unclean: %s' % sorted(k for k in w.entities if re.search(r'levi|priest|eleazar|aaron|canaan|land|court|tent|congregation|city|refuge|unclean', k)))
print('  the institution entities on the world and their in_force: %s' % [(k, [(x['effect'], str(x.get('value'))[:40], x.get('open')) for x in e.ledger if x['effect'] in ('in_force', 'rule_installed')][:6]) for k, e in w.entities.items() if getattr(e, 'kind', '') == 'institution'])
pop = w.population(level='tribe')
print('  population rows (level tribe) %d; the Levites\' rows: %s' % (len(pop), [(r.get('tribe'), r.get('as_of'), r.get('count')) for r in pop if r.get('tribe') in ('levi', 'the-levites', 'levites')]))
try:
    named = w.population(level='named')
    print('  population rows (named) %d; eleazar / joshua rows: %s' % (len(named), [(r.get('subject'), r.get('as_of'), r.get('status'), r.get('tribe')) for r in named if str(r.get('subject')) in ('eleazar_son_of_aaron', 'yehoshua', 'caleb')]))
except BaseException as e:
    print('  population(named) raised', type(e).__name__, str(e)[:120])
inst = w.installation
print('  installation: setting %s; skipped %s; would_skip %s' % (inst['setting'] if inst else None, inst['skipped'] if inst else None, inst['would_skip'] if inst else None))
print('  log classes: %s' % dict(collections.Counter(l[0] for l in w.log)))
print('  the timers pending: %s' % [(t.get('subject') if isinstance(t, dict) else str(t)[:80]) for t in (w.timers if isinstance(w.timers, list) else list(w.timers))][:14])
print('  the clock: day + 1 = %s' % (ex.date(w.clock.day + 1),))
rows_cnt = sum(1 for l in w.log if l[0] == 'ROW')
print('  ROW lines %d (CP1\'s kin — the population table)' % rows_cnt)

print('\n==== (3) THE KINDS AND EFFECTS ON FILE ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
cand_kinds = ['levite_cities_commanded', 'refuge_law_given', 'refuge_cities_commanded', 'refuge_statute_given', 'levite_cities_case', 'refuge_case', 'killer_case', 'manslayer_case', 'murderer_case', 'man_struck_dead', 'burglar_found', 'high_priest_died', 'priest_died', 'garments_transferred_and_aaron_died', 'priest_succeeded', 'head_anointed', 'sentence_declared', 'stoned_as_commanded', 'land_defiled', 'blood_required']
print('  kinds on file among the candidates:', [k for k in cand_kinds if k in E])
print('  kinds NOT on file:', [k for k in cand_kinds if k not in E])
cand_fx = ['commanded', 'flees_to_refuge', 'has_blood', 'put_to_death', 'beheaded', 'exempt', 'ransom_imposed', 'stoned', 'in_force', 'presence_dwells', 'enmity_set', 'blood_required', 'blood_reckoned', 'death_by_heaven', 'defiled', 'exiled', 'exiled_to_refuge', 'dwells_in_refuge', 'in_refuge', 'refuge_term', 'land_polluted', 'land_polluted_by_blood', 'atoned', 'atoned_forgiven', 'avenged', 'returned_to_his_possession', 'unresolved', 'holding_given', 'land_possessed', 'sent_outside_the_camp', 'priesthood_held', 'high_priest', 'anointed', 'clothed_in_the_garments', 'garments_transferred', 'succeeded', 'buried']
print('  effects on file among the candidates:', [f for f in cand_fx if f in F])
print('  effects NOT on file:', [f for f in cand_fx if f not in F])
for f in ('flees_to_refuge', 'has_blood', 'presence_dwells', 'avenged', 'blood_required', 'blood_reckoned', 'enmity_set', 'sent_outside_the_camp', 'death_by_heaven', 'unresolved', 'anointed', 'garments_transferred', 'succeeded', 'buried', 'holding_given'):
    if f in F: print('   %-24s %-8s he=%s\n        %s' % (f, F[f].get('ledger_op'), str(F[f].get('he', ''))[:90], str(F[f].get('en', ''))[:300].replace('\n', ' ')))
print('  the effect rows with ledger_op timer (the form): %s' % [(f, str(F[f].get('en', ''))[:80]) for f in F if F[f].get('ledger_op') == 'timer'][:12])
print('  the effect rows with ledger_op heaven naming death/blood: %s' % [f for f in F if F[f].get('ledger_op') == 'heaven' and re.search(r'death|blood|die|kill', f)])
print('  the kind rows garments_transferred_and_aaron_died / priest_succeeded / head_anointed whole: %s' % {k: E.get(k) for k in ('garments_transferred_and_aaron_died', 'priest_succeeded', 'head_anointed')})
print('  kinds whose en/ink names Num 35: %s' % [(k, re.findall(r'Num 35[^;,)]*', str(E[k].get('ink', '')) + str(E[k].get('en', '')))) for k in E if 'Num 35' in str(E[k].get('ink', '')) + str(E[k].get('en', ''))])
print('  effects whose en/ink names Num 35: %s' % [(f, re.findall(r'Num 35[^;,)]*', str(F[f].get('ink', '')) + str(F[f].get('en', '')))) for f in F if 'Num 35' in str(F[f].get('ink', '')) + str(F[f].get('en', ''))])
print('  the man_struck_dead kind row whole: %s' % E.get('man_struck_dead'))
print('  the burglar_found kind row whole: %s' % E.get('burglar_found'))

print('\n==== (4) THE CALLEES ON FILE, live (every call typed from the recon\'s asks) ====')
def tryc(label, f):
    try:
        r = f(); print('  ', label, '->', str(r)[:700])
    except BaseException as e:
        print('  ', label, 'raised', type(e).__name__, str(e)[:200])
src_m3 = open(inspect.getsourcefile(M3), encoding='utf-8').read()
print('  M3.killer signature / cell form: %s' % [l.strip()[:200] for l in src_m3.split('\n') if l.startswith('def killer(') or l.startswith('def burglar(') or l.startswith('def cell(')])
for q in ('refuge_by_descent', 'the_place', 'mode', 'forewarning', 'guile_excludes', 'his_fellow', 'father_and_son', 'the_altar'):
    tryc('M3.killer(%s)' % q, lambda q=q: M3.killer(q))
for q in ('judged_by_his_end', 'struck_by_whom', 'the_barrel', 'the_doubt', 'the_father', 'the_sabbath', 'the_sun'):
    tryc('M3.burglar(%s)' % q, lambda q=q: M3.burglar(q))
tryc('M3.SHEET / SHEET2 keys', lambda: (list(M3.SHEET)[:20] if hasattr(M3, 'SHEET') else None, list(M3.SHEET2)[:20] if hasattr(M3, 'SHEET2') else None))
src_m1 = open(inspect.getsourcefile(M1), encoding='utf-8').read()
print('  M1 lines with ransom (the ox\'s cell): %s' % [l.strip()[:220] for l in src_m1.split('\n') if 'ransom' in l][:6])
print('  M1.grade signature: %s' % [l.strip()[:200] for l in src_m1.split('\n') if l.startswith('def grade(') or l.startswith('def law_mishpatim(')])
tryc('M1.EFFECTS / TOTAL', lambda: (M1.EFFECTS if hasattr(M1, 'EFFECTS') else None, M1.TOTAL if hasattr(M1, 'TOTAL') else None))
src_l24 = open(inspect.getsourcefile(L24), encoding='utf-8').read()
print('  L24.talion signature and its asks: %s' % [l.strip()[:200] for l in src_l24.split('\n') if l.startswith('def talion(') or re.search(r"q == '|ask.*==", l)][:12])
tryc('L24.talion(kill)', lambda: L24.talion('kill') if 'def talion(q' in src_l24 else L24.talion({'ask': 'kill'}))
for q in ('thrice_unwitting', 'class', 'which_sin', 'communal', 'stranger_included'):
    tryc('SL.error(%s)' % q, lambda q=q: SL.error({'ask': q}, SL.DATA)[:2])
for q in ('three_camps', 'who_is_sent', 'classes', 'warning'):
    tryc('NS.camp_purity(%s)' % q, lambda q=q: NS.camp_purity({'ask': q}, NS.DATA)[:2])
tryc('NS.nazirite(impurity_kinds)', lambda: NS.nazirite({'ask': 'impurity_kinds'}, NS.DATA)[:2])
for q in ('by_number_of_names', 'land_divided_among', 'the_estimate', 'compensation', 'by_lot', 'tribes_or_skulls'):
    tryc('C2.the_land(%s)' % q, lambda q=q: C2.the_land({'ask': q}, C2.DATA)[:2])
for q in ('no_inheritance', 'count'):
    tryc('C2.the_levites(%s)' % q, lambda q=q: C2.the_levites({'ask': q}, C2.DATA)[:2])
for q in ('when_you_pass', 'possess_and_dwell', 'the_lot_restated', 'the_frame', 'drive_out'):
    tryc('JO.the_command(%s)' % q, lambda q=q: JO.the_command({'ask': q}, JO.DATA)[:2])
src_bo = open(inspect.getsourcefile(BO), encoding='utf-8').read()
print('  BO asks by cell: %s' % {d: sorted(set(re.findall(r"q == '([a-z_0-9]+)'", src_bo[src_bo.find('\ndef %s(' % d):src_bo.find('\ndef ', src_bo.find('\ndef %s(' % d) + 1)]))) for d in ('the_land_and_its_fall', 'the_four_sides', 'moses_restatement', 'the_dividers', 'the_roster')})
for q in ('the_command', 'the_land_canaan', 'when_you_come', 'the_frame', 'by_its_borders'):
    tryc('BO.the_land_and_its_fall(%s)' % q, lambda q=q: BO.the_land_and_its_fall({'ask': q}, BO.DATA)[:2])
for q in ('the_side_word', 'the_south', 'the_loop'):
    tryc('BO.the_four_sides(%s)' % q, lambda q=q: BO.the_four_sides({'ask': q}, BO.DATA)[:2])
tryc('BO.DATA the_four_sides value head', lambda: str(BO.DATA['the_four_sides'])[:300])
for q in ('source_of_rule', 'land_status', 'apportionment'):
    tryc('ZL.inheritance_order(%s)' % q, lambda q=q: ZL.inheritance_order({'ask': q}, ZL.DATA)[:2])
for q in ('the_run', 'output_frames', 'the_case'):
    tryc('ZL.the_daughters(%s)' % q, lambda q=q: ZL.the_daughters({'ask': q}, ZL.DATA)[:2])
for q in ('reubens_six', 'gads_eight', 'the_split', 'two_crossed'):
    tryc('GR.the_cities(%s)' % q, lambda q=q: GR.the_cities({'ask': q}, GR.DATA)[:2])
for q in ('land_held', 'three_parties'):
    tryc('GR.the_grant(%s)' % q, lambda q=q: GR.the_grant({'ask': q}, GR.DATA)[:2])
for q in ('succession', 'death_dates', 'aaron_age', 'thirty_days'):
    tryc('CK.edom_and_hor(%s)' % q, lambda q=q: CK.edom_and_hor({'ask': q}, CK.DATA)[:2])
for q in ('high_priest_exempt', 'camps', 'karet_entry', 'death_moment'):
    tryc('CK.corpse_tumah(%s)' % q, lambda q=q: CK.corpse_tumah({'ask': q}, CK.DATA)[:2])
src_pr = open(inspect.getsourcefile(PR), encoding='utf-8').read()
print('  PR.cain signature: %s' % [l.strip()[:200] for l in src_pr.split('\n') if l.startswith('def cain(') or l.startswith('def cell(') or l.startswith('def sentences(')])
for q in ('bloods_seats', 'exile_half', 'city_seat', 'mark_arms', 'wounds', 'bloods_sheet'):
    tryc('PR.cain(%s)' % q, lambda q=q: PR.cain(q))
tryc('PR.sentences(east_receives)', lambda: PR.sentences('east_receives'))
print('  PR lines naming 9:6 / blood_required / shedder: %s' % [l.strip()[:220] for l in src_pr.split('\n') if re.search(r"9:6|blood_required|shed", l)][:8])
for q in ('sides', 'three_camps', 'distance', 'march'):
    tryc('CB.camp(%s)' % q, lambda q=q: CB.camp({'ask': q}, CB.DATA)[:2])
tryc('CB.census(orders)', lambda: CB.census({'ask': 'orders'}, CB.DATA)[:2])
tryc('CB.CAMPS', lambda: CB.CAMPS)
src_dc = open(inspect.getsourcefile(DC), encoding='utf-8').read()
print('  DC lines naming murder / kill / 20:13 / the sixth: %s' % [l.strip()[:220] for l in src_dc.split('\n') if re.search(r"murder|תרצח|20:13|sixth", l)][:8])
for q in ('kidnapper', 'money_theft_here'):
    tryc('DC.theft_commandment(%s)' % q, lambda q=q: DC.theft_commandment({'ask': q}) if 'def theft_commandment(case' in src_dc or 'def theft_commandment(q' in src_dc else DC.theft_commandment(q))
print('  DC.theft_commandment signature: %s' % [l.strip()[:200] for l in src_dc.split('\n') if l.startswith('def theft_commandment(') or l.startswith('def vain_name(') or l.startswith('def out(')])
src_ph = open(inspect.getsourcefile(PH), encoding='utf-8').read()
print('  PH.family signature: %s' % [l.strip()[:200] for l in src_ph.split('\n') if l.startswith('def family(') or l.startswith('def cell(')])
for q in ('high_priest_dead', 'greatness', 'nezer', 'marks', 'addressees', 'met_mitzvah'):
    tryc('PH.family(%s)' % q, lambda q=q: PH.family(q))
print('  PH lines naming anoint / 21:10 / high priest: %s' % [l.strip()[:220] for l in src_ph.split('\n') if re.search(r"anoint|21:10|high priest|great", l)][:8])
for q in ('mode', 'venue', 'custody', 'warning', 'stoning', 'confession', 'burial'):
    tryc('MK.capital_procedure(%s)' % q, lambda q=q: MK.capital_procedure({'ask': q}, MK.DATA)[:2])
for q in ('mode', 'liability', 'uncertainty'):
    tryc('MK.the_gatherer(%s)' % q, lambda q=q: MK.the_gatherer({'ask': q}, MK.DATA)[:2])
src_sa = open(inspect.getsourcefile(SA), encoding='utf-8').read()
print('  SA.severity / SA.blood / SA.read_sanction signatures: %s' % [l.strip()[:200] for l in src_sa.split('\n') if re.match(r'def (severity|blood|read_sanction|sanction|mode|cell)\(', l)])
for q in ('murderer_mixed', 'two_deaths', 'orders', 'procedure', 'mixed'):
    tryc('SA.severity(%s)' % q, lambda q=q: SA.severity(q))
for q in ('atones', 'ban', 'which_blood', 'lashes'):
    tryc('SA.blood(%s)' % q, lambda q=q: SA.blood(q))
print('  SA lines naming land_defiled / 18:25 / 18:28 / vomit: %s' % [l.strip()[:220] for l in src_sa.split('\n') if re.search(r"land_defiled|18:25|18:28|vomit", l)][:8])
for q in ('high_priest_count', 'everlasting_priesthood', 'priesthood_by_the_deed'):
    tryc('BK.phinehas_and_midian(%s)' % q, lambda q=q: BK.phinehas_and_midian({'ask': q}, BK.DATA)[:2])
tryc('BK.DATA high_priest_count', lambda: BK.DATA['high_priest_count'])
tryc('V5 lines naming unwitting (ink)', lambda: [l.strip()[:200] for l in open(inspect.getsourcefile(V5), encoding='utf-8').read().split('\n') if 'unwitting' in l][:5])

print('\n==== (5) THE INSTALLATION FORMS AND THE GLOBAL-COUNT CHECKPOINTS (grepped BEFORE the tape run — 13b\'s lesson) ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
for pat in (r"len\(cmd_v\)", r"isr_cmd", r"len\(w\.entities\)", r"closes_done", r"'commanded'", r"the-levites", r"eleazar", r"in_force", r"presence_dwells", r"has_blood", r"the-land-of-canaan", r"population\("):
    hits = [l.strip()[:200] for l in src_cs.split('\n') if re.search(pat, l) and ('cp(' in l or re.search(r"^\s*[a-z_0-9]+ = \[", l.strip()))]
    print('  %-28s %d lines: %s' % (pat, len(hits), hits[:6]))
print('  the CV2 line whole: %s' % [l.strip()[:700] for l in src_cs.split('\n') if "cp('CV2" in l][:1])
print('  the CX2 line whole: %s' % [l.strip()[:700] for l in src_cs.split('\n') if "cp('CX2" in l][:1])
print('  the CZ2 line whole: %s' % [l.strip()[:700] for l in src_cs.split('\n') if "cp('CZ2" in l][:1])
print('  the CW3 line whole: %s' % [l.strip()[:700] for l in src_cs.split('\n') if "cp('CW3" in l][:1])
print('  the CW9 line whole: %s' % [l.strip()[:700] for l in src_cs.split('\n') if "cp('CW9" in l][:1])
print('  the CP1 line whole: %s' % [l.strip()[:900] for l in src_cs.split('\n') if "cp('CP1" in l][:1])
print('  the CW1 line whole (the form to copy): %s' % [l.strip()[:900] for l in src_cs.split('\n') if "cp('CW1" in l][:1])
print('  the lines defining cmd_v / isr_cmd / dv_cmd / cal_owed / ev_bo lists: %s' % [l.strip()[:220] for l in src_cs.split('\n') if re.search(r"^\s*(cmd_v|isr_cmd|dv_cmd|cal_owed|ev_bo|BO_KINDS|bo_[a-z_]+) = ", l)][:12])
print('  the lines between "# ---- Num 34 ----" and "# ---- Num 36 ----" in the tape: %s' % [l.strip()[:120] for l in src_cs[src_cs.find('# ---- Num 34 ----'):src_cs.find('# ---- Num 36 ----')].split('\n')])
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  law_journeys block head (the divine-voice-in-the-plains form): %s' % {k: str(v)[:300] for k, v in dd['daemons']['law_journeys'].items() if k != 'watches'})
print('  law_borders installed_by note whole: %s' % str(dd['daemons']['law_borders'].get('installed_by_note', dd['daemons']['law_borders'].get('why', '')))[:600])
print('  law_borders block keys: %s' % list(dd['daemons']['law_borders']))
print('  register_probes count: %s; census_probes count: %s' % (len(re.findall(r"^def (R\d+|probe_\w+)\(", open(f'{ROOT}/World/step9/register_probes.py', encoding='utf-8').read(), re.M)), len(re.findall(r"^\s*\('[A-Z]+\d+", open(f'{ROOT}/World/step9/census_probes.py', encoding='utf-8').read(), re.M))))

print('\n==== (6) THE REGISTER GATE on chapter 35 (computed on the running world) ====')
ink = RG.read_ink()
cc = RG.class_counts(ink, w)
print('  count lines in Num 35: %s' % [(r, d['class'], d['noun'], d.get('counts'), d.get('measures')) for r, d in cc.items() if r.startswith('Num 35:')])
cr = RG.class_receipts(ink, w)
print('  receipts in Num 35: %s' % [(r, d['class'], d['evidence']) for r, d in cr.items() if r.startswith('Num 35:')])
cf = RG.class_footers(ink)
print('  footers naming Num 3x: %s' % {k: (v['class'] if isinstance(v, dict) else v) for k, v in cf.items() if 'Num 3' in k})
try:
    rh = RG.register_headers(ink)
    items = rh.items() if isinstance(rh, dict) else enumerate(rh)
    print('  register headers naming Num 35: %s' % [(k, str(v)[:300]) for k, v in items if 'Num 35' in str(k) + str(v)][:5])
except BaseException as e:
    print('  register_headers raised', type(e).__name__, str(e)[:120])
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the declared seats naming Num 35: %s' % [(sec, k) for sec in decl for k in (decl[sec] or {}) if 'Num 35' in k])
print('  the footer seat Num 36:13 whole: %s' % decl.get('footers', {}).get('Num 36:13'))

print('\n==== (7) THE RECORDER/STITCHER ====')
print('  import lines for the walk\'s runners: %s' % re.findall(r'^import (cold_run_(?:borders|journeys|gad_reuben|midian))', src_cs, re.M))
SP = os.path.dirname(os.path.abspath(__file__))
for f in ('seq_stitch.py', 'seq_record.py'):
    p = f'{SP}/{f}'
    print('  %s in the scratchpad: %s' % (f, os.path.exists(p)))
    if os.path.exists(p):
        t = open(p, encoding='utf-8').read()
        print('    SPAN_ORDER tail: %s' % re.findall(r"SPAN_ORDER\s*=\s*\[([^\]]*)\]", t)[0][-160:] if 'SPAN_ORDER' in t else '')
        print('    recording path: %s' % re.findall(r"seq_recording\.json[^\n]*", t)[:1])
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
print('  the section markers in the tape: %s' % re.findall(r'# ---- (Num \d+) ----', tape))
print('  cp() checkpoints on file (tail): %s' % re.findall(r"cp\('(C[A-Z]\d)", src_cs)[-12:])

print('\n==== (8) THE ENGINE\'S TIMER AND CLOSE INTERFACE (the term\'s form) ====')
src_we = open(f'{ROOT}/World/step9/world_engine.py', encoding='utf-8').read()
print('  World defs: %s' % re.findall(r'^    def ([a-z_]+)\(', src_we, re.M))
print('  set_timer / close / cancel_timers signatures: %s' % [l.strip()[:220] for l in src_we.split('\n') if re.match(r'    def (set_timer|close|cancel_timers|_write|submit|row|timer|due|fire)\(', l)])
print('  the timer entry fields (the set line): %s' % [l.strip()[:260] for l in src_we.split('\n') if "'TIMER-SET'" in l][:3])
print('  E_ helper signature in the runners (borders): %s' % [l.strip()[:220] for l in src_bo.split('\n') if l.startswith('def E_(') or l.startswith('def out(') or l.startswith('def dat(') or l.startswith('def hyp(')])
print('  the borders daemon head (the literal W form): %s' % [l.strip()[:220] for i, l in enumerate(src_bo.split('\n')) if l.startswith('def law_borders(')] )
i = src_bo.find('\ndef law_borders(')
print('  law_borders body head:\n' + '\n'.join('     ' + l[:220] for l in src_bo[i:i + 3200].split('\n')[:40]))
