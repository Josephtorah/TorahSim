#!/usr/bin/env python3
# THE NUMBERS WALK sitting 11b — THE COMPILE OF MIDIAN, Numbers 31:1-54 (2026-09-12; the owner: "Go" after the #145 rereads):
# THE MEASUREMENTS, computed BEFORE the design paragraph is typed (1b's order; vows_compile_measure.py's form). (1) the parser at
# 31:1-54 and 32:1, and THE FRACTION CLASS's six Bible seats with their marks; (2) the tape's state — the counter, the entities, the pending
# timers, the markers, the open entries the chapter closes (the Midian debit, the trumpets' debit, the ass's sword clause), the registry map
# for the tokens the lines will carry; (3) the kinds and effects on file; (4) the callees live — balak (the debit, Balaam's death row, Zur),
# beha (the trumpets), chukat (the water, the schedule, the sword), shemini (Lev 11's carcass grade — the vessels' cell measured), incense_shekel
# (the ransom's cells), bamidbar (the charge), naso (the sotah's treachery); (5) the engine's literals; (6) THE REGISTER GATE — the eight
# chapter-31 seats' computed classes on the running world, the chapter's count lines and receipts, the footer block (Num 30:17, 36:13];
# (7) the installing acts, the recorder and the stitcher.
import sqlite3, sys, io, re, contextlib, collections, inspect, os, yaml
ROOT = '<repo-old>'
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import world_engine as WE
    import cold_run_balak as BK
    import cold_run_beha as BH
    import cold_run_chukat as CK
    import cold_run_shemini as SH
    import cold_run_incense_shekel as IS
    import cold_run_bamidbar as BM
    import cold_run_naso as NS
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

print('==== (1) THE PARSER AT 31:1-54 and 32:1 — numbers, ordinals, the marked tokens (a star = a refused homograph) ====')
for v in list(range(1, 55)):
    vw = CS.verse_words('Num', 31, v)
    marked = [t for t in vw if re.search(r'[#^~%@|*]', t)]
    n, o = N('Num', 31, v), O('Num', 31, v)
    if n or o or marked:
        print('  Num 31:%-3d numbers %-32s ordinals %-8s marked %s' % (v, n, o, marked))
print('  Num 32:1   numbers %s ordinals %s' % (N('Num', 32, 1), O('Num', 32, 1)))
print('\n---- THE FRACTION CLASS "one of the N" — the six Bible seats, verse_words whole (the marks the parser gives now) ----')
FRACTION_SEATS = [('Num', 31, 28), ('Num', 31, 30), ('Num', 31, 47), ('Eccl', 7, 28), ('Ezek', 45, 15), ('Neh', 11, 1)]
for k in FRACTION_SEATS:
    vw = CS.verse_words(*k)
    print('  %s %d:%d numbers %s ordinals %s' % (k[0], k[1], k[2], CS.ink_numbers(vw), CS.ink_ordinals(vw)))
    print('     words: %s' % ' '.join(vw))
    print('     lemmas: %s' % [lm for _, _, lm in by[k]])
print('  the UNITS table keys (the parser\'s unit nouns): %s' % (sorted(CS.UNITS)[:40] if hasattr(CS, 'UNITS') else 'no UNITS'))
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
i = src_cs.find('def ink_numbers('); j = src_cs.find('\ndef ', i + 1)
print('  ink_numbers: %d lines; the rule comments naming the walk: %s' % (src_cs[i:j].count('\n'), re.findall(r'# (?:THE NUMBERS WALK \d+b?[^\n]{0,60})', src_cs[i:j])[:30]))
print('  the parser\'s own handling of "one" before "of" (מן): %s' % ('4451' in src_cs[i:j] or 'min' in src_cs[i:j]))

print('\n==== (2) THE TAPE\'S STATE — the running world ====')
with contextlib.redirect_stdout(io.StringIO()):
    w = RG.running_world()
ex = w.clock.eras['exodus']
print('  the counter: day %d = %s (exodus era); entities %d; log lines %d; timers pending %d' % (w.clock.day, ex.date(w.clock.day), len(w.entities), len(w.log), len(w.timers)))
print('  the pending timers: %s' % [(t[1].get('subject'), t[1].get('effect'), t[1].get('period'), ex.date(t[0])[1:]) for t in w.timers])
tset = [l for l in w.log if l[0] == 'TIMER-SET']; tfire = [l for l in w.log if l[0] == 'TIMER-FIRE']; tcan = [l for l in w.log if l[0] == 'TIMER-CANCEL']
print('  TIMER-SET %d, TIMER-FIRE %d, TIMER-CANCEL %d' % (len(tset), len(tfire), len(tcan)))
mk = [l for l in w.log if l[0] == 'MARKER']
print('  markers %d; the last three: %s' % (len(mk), [(l[2].get('verse'), ex.date(l[1]), l[2].get('placement')) for l in mk[-3:]]))
EVs = [l for l in w.log if l[0] == 'EVENT']
print('  events %d; the last five kinds and sources: %s' % (len(EVs), [(l[2]['kind'], str(l[2].get('case_source', ''))[:40], l[2].get('placement')) for l in EVs[-5:]]))
for pat in ('Num 31', 'Num 25:1', 'Num 10:1', 'Num 22:2', 'Num 22:3', 'Num 36:'):
    hits = [(l[2]['kind'], l[2].get('subject'), str(l[2].get('case_source', ''))[:50]) for l in EVs if pat in str(l[2].get('case_source', ''))]
    print('  events citing %-8s: %d %s' % (pat, len(hits), hits[:8]))
reg_map = CS.registry_map()
TOK = ('israel', 'israel_people', 'moses', 'eleazar', 'pinchas', 'aaron', 'balaam', 'midian', 'the-midianites', 'the-midianite', 'zur', 'evi', 'rekem', 'hur', 'reba', 'the-levites', 'the-priests', 'the-tabernacle', 'the-court', 'the-congregation', 'the-warriors', 'the-army', 'the-captains', 'the-captives', 'the-prey', 'the-spoil', 'the-booty', 'the-five-kings', 'the-kings-of-midian', 'the-officers', 'the-women-of-midian', 'the-little-ones', 'the-heads-of-the-tribes', 'the-treasury')
print('  registry_map for the tokens: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  tokens with NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])
print('  entity ids present among: %s' % [t for t in TOK if reg_map.get(t, t) in w.entities])
def ent(t): return w.entities.get(reg_map.get(t, t))
for t in ('israel', 'moses', 'balaam', 'the-tabernacle', 'the-court', 'pinchas', 'eleazar', 'the-levites', 'zur', 'midian'):
    e = ent(t)
    if e is None: print('  %-16s NO ENTITY' % t); continue
    opens = [(x['effect'], x.get('value'), x.get('cp'), str(x.get('case_source', ''))[:24]) for x in e.ledger if x.get('open')]
    print('  %-16s id %-18s ledger %3d; OPEN %d: %s' % (t, e.eid, len(e.ledger), len(opens), opens[:14]))
    if t == 'moses':
        print('     moses commanded entries: %s' % [(x.get('value'), x.get('open'), str(x.get('closed_by', ''))[:30]) for x in e.ledger if x['effect'] == 'commanded'])
    if t == 'balaam':
        print('     balaam ledger: %s' % [(x['effect'], x.get('value'), x.get('open'), x['op']) for x in e.ledger])
isr = ent('israel')
cmd = [x for x in isr.ledger if x['effect'] == 'commanded']
print('  israel commanded entries %d; the OPEN ones: %s' % (len(cmd), [(x.get('value'), x.get('cp'), str(x.get('case_source'))[:20]) for x in cmd if x.get('open')]))
print('  the harass entry: %s' % [{k_: (str(v_)[:80] if k_ != 'law' else str(v_)[:60]) for k_, v_ in x.items()} for x in cmd if x.get('value') == 'harass_the_midianites'])
plag = [x for x in isr.ledger if x['effect'] == 'plague_struck']
print('  israel plague_struck entries: %s' % [(x.get('value'), x.get('open'), str(x.get('closed_by', ''))[:30]) for x in plag])
tab = ent('the-tabernacle')
print('  the-tabernacle rule_installed entries: %s' % [(x.get('value'), x.get('open'), str(x.get('case_source', ''))[:24]) for x in tab.ledger if x['effect'] == 'rule_installed'] if tab else None)
print('  the clock: day + 1 = %s; day + 7 = %s' % (ex.date(w.clock.day + 1), ex.date(w.clock.day + 7)))
inst = w.installation
print('  installation: setting %s; skipped %s; would_skip %s; fields %d' % (inst['setting'] if inst else None, inst['skipped'] if inst else None, inst['would_skip'] if inst else None, len(inst['fields']) if inst else 0))
subj = collections.Counter(l[2].get('subject') for l in EVs)
print('  subjects on the tape naming midian/balaam/zur/eleazar/levite/priest/captain/officer: %s' % {s: n for s, n in subj.items() if s and re.search(r'midian|balaam|zur|eleazar|levite|priest|captain|officer|warrior|army', s)})

print('\n==== (3) THE KINDS AND EFFECTS ON FILE ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
cand_kinds = ['midian_vengeance_commanded', 'vengeance_commanded', 'midian_harassment_commanded', 'warriors_mustered', 'army_sent', 'midian_warred', 'war_waged', 'kings_slain', 'balaam_slain', 'women_and_children_captured', 'cities_burned', 'spoil_taken', 'spoil_brought', 'moses_wroth', 'sentence_on_the_captives', 'purification_commanded', 'kashering_statute', 'eleazars_statute', 'division_commanded', 'prey_counted', 'prey_halved', 'tribute_given', 'levites_share_given', 'gold_offered', 'officers_gold_offered', 'trumpets_commanded', 'trumpet_case', 'corpse_tumah_case', 'heifer_case', 'half_shekel_case', 'census_commanded', 'phinehas_case', 'midianite_brought_near']
print('  kinds on file among the candidates:', [k for k in cand_kinds if k in E])
print('  kinds NOT on file:', [k for k in cand_kinds if k not in E])
cand_fx = ['commanded', 'counted', 'slain', 'slain_by_sword', 'spoil_taken', 'taken_captive', 'burned_in_fire', 'corpse_unclean_seven_days', 'sprinkling_due_third_day', 'sprinkling_due_seventh_day', 'washes_and_bathes', 'declared_pure', 'immersed', 'impure_until_evening', 'half_shekel_owed', 'no_plague_at_counting', 'atoned_forgiven', 'charge_kept', 'given_to_aaron', 'put_to_death', 'gathered_to_his_people', 'rule_installed', 'in_force', 'exempt', 'accepted', 'sanctify_day', 'tent_unclean', 'souls_counted', 'terumah_given', 'heave_offering_owed', 'memorial_before_the_lord', 'kashered', 'passed_through_fire', 'wroth', 'vengeance_taken', 'kept_alive', 'plague_struck']
print('  effects on file among the candidates:', [f for f in cand_fx if f in F])
print('  effects NOT on file:', [f for f in cand_fx if f not in F])
for f in sorted(F):
    if re.search(r'captiv|spoil|slain|sword|burn|clean|sprinkl|wash|immers|purif|shekel|plague|memor|terumah|heave|count|tribut|charge|wroth|anger|venge|fire', f):
        print('   %-30s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:100].replace('\n', ' ')))
print('  kinds on file matching midian/balaam/trump/heifer/corpse/shekel/census/war/spoil/captiv:')
for k in sorted(E):
    if re.search(r'midian|balaam|trump|heifer|corpse|shekel|census|war|spoil|captiv|command', k):
        print('    %-36s form %-7s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:90].replace('\n', ' ')))
print('  the ledger_op values in use: %s' % dict(collections.Counter(F[f].get('ledger_op') for f in F)))

print('\n==== (4) THE CALLEES ON FILE, live ====')
def tryc(label, f):
    try:
        r = f(); print('  ', label, '->', str(r)[:320])
    except BaseException as e:
        print('  ', label, 'raised', type(e).__name__, str(e)[:200])
tryc('BK.phinehas_and_midian(midian_not_moab)', lambda: BK.phinehas_and_midian({'ask': 'midian_not_moab'}, BK.DATA)[:2])
tryc('BK.phinehas_and_midian(balaam_death)', lambda: BK.phinehas_and_midian({'ask': 'balaam_death'}, BK.DATA)[:2])
tryc('BK.phinehas_and_midian(cozbi_and_zur)', lambda: BK.phinehas_and_midian({'ask': 'cozbi_and_zur'}, BK.DATA)[:2])
tryc('BK.phinehas_and_midian(harass_root)', lambda: BK.phinehas_and_midian({'ask': 'harass_root'}, BK.DATA)[:2])
tryc('BK.the_call(midian_joined)', lambda: BK.the_call({'ask': 'midian_joined'}, BK.DATA)[:2])
tryc('BK.DATA midian_command_run / balaam_death / cozbi_and_zur', lambda: (BK.DATA['midian_command_run'], BK.DATA['balaam_death']['value'], sorted(BK.DATA['balaam_death']['settings']), BK.DATA['cozbi_and_zur']['value']))
tryc('BH.trumpets(oppression war)', lambda: BH.trumpets({'ask': 'oppression', 'kind': 'war'}, BH.DATA)[:2])
tryc('BH.trumpets(sounds journey)', lambda: BH.trumpets({'ask': 'sounds', 'occasion': 'journey'}, BH.DATA)[:2])
tryc('BH.trumpets(who_discharges)', lambda: BH.trumpets({'ask': 'who_discharges'}, BH.DATA)[:2])
tryc('BH.trumpets(hearing)', lambda: BH.trumpets({'ask': 'hearing'}, BH.DATA)[:2])
tryc('BH.trumpets(count)', lambda: BH.trumpets({'ask': 'count'}, BH.DATA)[:2])
tryc('BH.DATA oppression_scope', lambda: (BH.DATA['oppression_scope']['value'], sorted(BH.DATA['oppression_scope']['settings'])))
tryc('CK.corpse_tumah(seven_days)', lambda: CK.corpse_tumah({'ask': 'seven_days'}, CK.DATA)[:2])
tryc('CK.corpse_tumah(schedule third seventh)', lambda: CK.corpse_tumah({'ask': 'schedule', 'third': True, 'seventh': True}, CK.DATA)[:2])
tryc('CK.corpse_tumah(sword_like_slain)', lambda: CK.corpse_tumah({'ask': 'sword_like_slain'}, CK.DATA)[:2])
tryc('CK.corpse_tumah(purification)', lambda: CK.corpse_tumah({'ask': 'purification'}, CK.DATA)[:2])
tryc('CK.corpse_tumah(sprinkling_day)', lambda: CK.corpse_tumah({'ask': 'sprinkling_day'}, CK.DATA)[:2])
tryc('CK.corpse_tumah(sprinkler_who)', lambda: CK.corpse_tumah({'ask': 'sprinkler_who'}, CK.DATA)[:2])
tryc('CK.corpse_tumah(camps)', lambda: CK.corpse_tumah({'ask': 'camps'}, CK.DATA)[:2])
tryc('CK.corpse_tumah(metal_vessels_decree)', lambda: CK.corpse_tumah({'ask': 'metal_vessels_decree'}, CK.DATA)[:2])
tryc('CK.corpse_tumah(removes)', lambda: CK.corpse_tumah({'ask': 'removes'}, CK.DATA)[:2])
tryc('CK.corpse_tumah(tent_gentile)', lambda: CK.corpse_tumah({'ask': 'tent_gentile'}, CK.DATA)[:2])
tryc('CK.heifer_rite(sprinkling)', lambda: CK.heifer_rite({'ask': 'sprinkling'}, CK.DATA)[:2])
tryc('CK.DATA sword_like_slain / third_day_fixed / tent_gentile', lambda: (CK.DATA['sword_like_slain']['value'], CK.DATA['third_day_fixed']['value'], CK.DATA['tent_gentile']['settings']))
tryc('SH.touch_effect(touch_carcass)', lambda: SH.touch_effect('touch_carcass'))
tryc('SH.touch_effect(carry_carcass)', lambda: SH.touch_effect('carry_carcass'))
tryc('SH defs', lambda: re.findall(r'^def ([a-z_0-9]+)\(', open(inspect.getsourcefile(SH), encoding='utf-8').read(), re.M))
tryc('SH source names 11:32 / vessel / sack: ', lambda: [m for m in ('11:32', '11:33', 'vessel', 'sack', 'שק', 'garment') if m in open(inspect.getsourcefile(SH), encoding='utf-8').read()])
for q in ('atone_souls', 'lift_head', 'ransom', 'plague_clause', 'silver_of_atonements', 'terumah', 'numbers_no_shekel', 'trigger_parameter', 'passing_over'):
    tryc('IS.shekel(%s)' % q, lambda q=q: {k_: (str(v_)[:160] if k_ != 'fx' else v_) for k_, v_ in IS.shekel(q).items()})
tryc('BM.charges(houses_charges)', lambda: BM.charges({'ask': 'houses_charges'}, BM.DATA)[:2])
tryc('BM.charges(watches)', lambda: BM.charges({'ask': 'watches'}, BM.DATA)[:2])
tryc('BM.charges(wrath)', lambda: BM.charges({'ask': 'wrath'}, BM.DATA)[:2])
src_ns = open(inspect.getsourcefile(NS), encoding='utf-8').read()
i = src_ns.find('def sotah('); j = src_ns.find('\ndef ', i + 1)
print('  NS.sotah asks: %s' % sorted(set(re.findall(r"ask == '([a-z_]+)'", src_ns[i:j]))))
print('  NS defs: %s' % re.findall(r'^def ([a-z_0-9]+)\(', src_ns, re.M)[:30])
tryc('NS.sotah(treachery)?', lambda: NS.sotah({'ask': 'treachery'}, NS.DATA)[:2])
def defs(mod): return re.findall(r'^def ([a-z_0-9]+)\(', open(inspect.getsourcefile(mod), encoding='utf-8').read(), re.M)
for name, mod in (('balak', BK), ('beha', BH), ('chukat', CK), ('shemini', SH), ('incense_shekel', IS), ('bamidbar', BM)):
    s = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    print('  %-14s defs %s\n  %-14s imports %s' % (name, defs(mod)[:24], '', sorted(set(re.findall(r'^\s*import (cold_run_\w+)', s, re.M)))))
# the four materials: Lev 11:32 against Num 31:20
def lemset(k): return [(plain(he), lm) for he, _, lm in by[k]]
print('  Lev 11:32 words+lemmas: %s' % lemset(('Lev', 11, 32)))
print('  Num 31:20 words+lemmas: %s' % lemset(('Num', 31, 20)))
print('  Num 31:22 words+lemmas (the six metals): %s' % lemset(('Num', 31, 22)))
print('  Num 31:23 words: %s' % ' '.join(words('Num', 31, 23)))

print('\n==== (5) THE ENGINE\'S LITERALS ====')
print('  DAEMON_ORDER length %d, last %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-1]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s\n  SLOTS %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT, CS.SLOTS))
print('  installation_probes I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
reg = yaml.safe_load(open(f'{ROOT}/logic/corpus/entity_registry.yaml', encoding='utf-8'))
print('  registry entities %d; ids containing midian/balaam/zur/eleazar/pinchas/levite/priest/moses/israel: %s' % (len(reg['entities']), [e['id'] for e in reg['entities'] if re.search(r'midian|balaam|zur|eleazar|pinchas|levite|priest|^moses$|israel', e['id'])][:30]))
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  daemons %d; installed_by values: %s' % (len(dd['daemons']), dict(collections.Counter(v.get('installed_by') for v in dd['daemons'].values()))))
print('  the walk\'s daemons: %s' % {k: (v.get('given_at'), v.get('installed_by')) for k, v in dd['daemons'].items() if k in ('law_balak', 'law_beha', 'law_chukat', 'law_shemini', 'law_vows', 'law_musafim', 'law_census', 'law_tent')})
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d' % (len(dep['spans']), len(dep['edges']), len(dep['pointers'])))
print('  pointers at Num 31 already: %s' % [p for p in dep['pointers'] if str(p.get('verse', '')).startswith('Num 31')])
print('  edges naming balak/beha/chukat/shemini/incense_shekel/bamidbar as `to`: %s' % collections.Counter(e['to'] for e in dep['edges'] if e['to'] in ('balak', 'beha', 'chukat', 'shemini', 'incense_shekel', 'bamidbar')))
print('  the spans: %s' % {k: dep['spans'][k] for k in ('balak', 'beha', 'chukat', 'shemini', 'incense_shekel', 'bamidbar', 'vows', 'naso') if k in dep['spans']})
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  statute_declared: %s' % {k: str(v)[:160] for k, v in ip['installing_acts']['statute_declared'].items()})
cal = yaml.safe_load(open(f'{ROOT}/World/step9/calendar_parameters.yaml', encoding='utf-8'))
print('  calendar_parameters rows %d; rows naming third/seventh/corpse/sprinkl: %s' % (len(cal['parameters']) if 'parameters' in cal else len(cal), [k for k in (cal['parameters'] if 'parameters' in cal else cal) if re.search(r'third|seventh|corpse|sprinkl|day_boundary', k)]))

print('\n==== (6) THE REGISTER GATE — the eight seats on the running world; the chapter\'s count lines and receipts; the footer block ====')
ink = RG.read_ink()
cc = RG.class_counts(ink, w)
print('  count lines in Num 31: %s' % [(r, d['class'], d['noun'], d.get('counts'), d.get('measures')) for r, d in cc.items() if r.startswith('Num 31:')])
cr = RG.class_receipts(ink, w)
print('  receipts in Num 31: %s' % [(r, d['class'], d['evidence']) for r, d in cr.items() if r.startswith('Num 31:')])
cf = RG.class_footers(ink)
print('  class_footers: %s' % {k: (v['class'] if isinstance(v, dict) else v) for k, v in cf.items()})
print('  Num 36:13 footer detail: %s' % {k: v for k, v in cf.items() if 'Num 36' in k})
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  declared footers: %s' % {k: v['class'] for k, v in decl.get('footers', {}).items()})
print('  declared counts in Num 31: %s; declared receipts in Num 31: %s' % ([k for k in decl.get('counts', {}) if k.startswith('Num 31')], [k for k in decl.get('receipts', {}) if k.startswith('Num 31')]))
LG = [(ent_.eid, e['value'], str(e.get('case_source'))[:30]) for ent_ in w.entities.values() for e in ent_.ledger if e['effect'] == 'counted' and isinstance(e.get('value'), int)]
print('  counted statuses on the ledger (the LEDGER class\'s instrument): %d — %s' % (len(LG), LG[:12]))
print('  the count line 31:36 detail: %s' % cc.get('Num 31:36'))
print('  the count line 31:40 detail: %s' % cc.get('Num 31:40'))
print('  Num 31 verses with a count-noun (6485 the counted / 4557 the number / 5315 souls): %s' % [(v, [lm for _, _, lm in by[('Num', 31, v)] if lm.split('/')[-1].split(' ')[0] in ('6485', '4557', '5315')]) for v in range(1, 55) if any(lm.split('/')[-1].split(' ')[0] in ('6485', '4557', '5315') for _, _, lm in by[('Num', 31, v)])])

print('\n==== (7) THE RECORDER/STITCHER and the sweep\'s runner list ====')
print('  import lines for the walk\'s runners: %s' % re.findall(r'^import (cold_run_(?:vows|musafim|second_census|balak))', src_cs, re.M))
print('  DAEMON_ORDER tail: %s' % CS.DAEMON_ORDER[-4:])
st = open(f'{ROOT}/World/step9/forms_numbers_walk/seq_stitch.py', encoding='utf-8').read()
print('  seq_stitch SPAN_ORDER: %s' % re.findall(r"SPAN_ORDER\s*=\s*\[([^\]]*)\]", st)[:1])
print('  the tape section sentinels present: %s' % ('# ==== TAPE BEGIN' in src_cs, '# ==== TAPE END ====' in src_cs))
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
print('  the tape\'s Num 30 and Num 36 lines: %s' % [l[:110] for l in tape.split('\n') if 'Num 30' in l or '# ---- Num 3' in l][:6])
