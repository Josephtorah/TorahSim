#!/usr/bin/env python3
# THE NUMBERS WALK sitting 30b — THE COMPILE OF THE VOWS, Numbers 30:1-17 (2026-09-12; the owner: "Go" after the #142 rereads):
# THE MEASUREMENTS, computed BEFORE the design paragraph is typed (1b's order; offerings_compile_measure.py's form). (1) the parser at
# 30:1-17 and 31:1 — the three starred oath-tokens, the empty lists; (2) the tape's state — the running world's counter, entities, the
# pending timers, the markers, the 9b line, the registry map for the tokens the line will carry; (3) the kinds and effects on file;
# (4) the callees live — the nazirite's vow-identity, the sotah's 5:31, the utterance oath of Lev 5:4, the priest's daughter's return,
# the musafim runner's vow_deadline row, the moadim runner's affliction; (5) the engine's literals; (6) THE REGISTER GATE — is 30:1's
# receipt in the census? the seven seats of the "according to ALL that" form; the footer 30:17's block; (7) the installing acts.
import sqlite3, sys, io, re, contextlib, collections, inspect, os, yaml
ROOT = '<repo-old>'
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import world_engine as WE
    import cold_run_naso as NS
    import cold_run_vayikra5 as V5
    import cold_run_priesthood as PR
    import cold_run_musafim as MU
    import cold_run_moadim as MO
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

print('==== (1) THE PARSER AT 30:1-17 and 31:1 — the marks of verse_words (a star = a refused homograph), the lists ====')
for v in list(range(1, 18)):
    vw = CS.verse_words('Num', 30, v)
    marked = [t for t in vw if re.search(r'[#^~%@|*]', t)]
    print('  Num 30:%-3d numbers %-6s ordinals %-6s marked %s' % (v, N('Num', 30, v), O('Num', 30, v), marked))
print('  Num 31:1   numbers %s ordinals %s marked %s' % (N('Num', 31, 1), O('Num', 31, 1), [t for t in CS.verse_words('Num', 31, 1) if re.search(r'[#^~%@|*]', t)]))

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
print('  events %d; the last four kinds and sources: %s' % (len(EVs), [(l[2]['kind'], str(l[2].get('case_source', ''))[:40], l[2].get('placement')) for l in EVs[-4:]]))
num30 = [(l[2]['kind'], str(l[2].get('case_source', ''))[:60]) for l in EVs if 'Num 30' in str(l[2].get('case_source', ''))]
print('  events citing Num 30 on the tape: %s' % num30)
reg_map = CS.registry_map()
print('  registry_map for the tokens: %s' % {t: reg_map.get(t) for t in ('israel', 'israel_people', 'moses', 'the-heads-of-the-tribes', 'the-princes', 'the-tabernacle', 'the-court')})
print('  entity ids present among: %s' % {t: (t in w.entities) for t in ('israel', 'israel_people', 'moses', 'the-heads-of-the-tribes', 'the-princes', 'the-tabernacle')})
isr = w.entities.get(reg_map.get('israel', 'israel'))
print('  the israel entity id %r: ledger %d; commanded entries %d; the effects: %s' % (reg_map.get('israel', 'israel'), len(isr.ledger) if isr else -1, len([e for e in isr.ledger if e['effect'] == 'commanded']) if isr else -1, dict(collections.Counter(e['effect'] for e in isr.ledger).most_common(12)) if isr else None))
print('  the clock: day + 1 = %s; next sabbath %s; next month %s' % (ex.date(w.clock.day + 1), ex.date(w.clock.next(w.clock.day, 'sabbath')) if hasattr(w.clock, 'calendar') and False else ex.date(w.clock.next('sabbath')), ex.date(w.clock.next('month'))))
inst = w.installation
print('  installation: setting %s; skipped %s; would_skip %s; fields %d' % (inst['setting'] if inst else None, inst['skipped'] if inst else None, inst['would_skip'] if inst else None, len(inst['fields']) if inst else 0))

print('\n==== (3) THE KINDS AND EFFECTS ON FILE ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
cand_kinds = ['vows_law_spoken', 'vow_uttered', 'vow_case', 'vowed', 'oath_uttered', 'vow_heard', 'vow_annulled', 'vow_confirmed', 'mans_vow_case', 'daughters_vow_case', 'betrothed_vow_case', 'widows_vow_case', 'wifes_vow_case', 'affliction_oath_case', 'vow_release_case', 'vows_case', 'statutes_case', 'nazirite_case', 'sotah_case']
print('  kinds on file among the candidates:', [k for k in cand_kinds if k in E])
print('  kinds NOT on file:', [k for k in cand_kinds if k not in E])
cand_fx = ['vow_bound', 'vow_confirmed', 'vow_annulled', 'iniquity_borne', 'commanded', 'exempt', 'accepted', 'atoned_forgiven', 'forgiven', 'oath_imposed', 'nazirite_vow_bound', 'vow_of_bethel', 'consecrated', 'sworn_by_the_name', 'name_profaned', 'bound_to_the_word', 'given_by_the_heart', 'lashes', 'forewarned', 'rule_installed', 'in_force', 'released', 'permitted', 'bound', 'stands', 'annulled', 'confirmed']
print('  effects on file among the candidates:', [f for f in cand_fx if f in F])
print('  effects NOT on file:', [f for f in cand_fx if f not in F])
for f in sorted(F):
    if re.search(r'vow|oath|sworn|forgiv|iniquity|bound|profan|consecrat|released|permit', f):
        print('   %-28s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:100].replace('\n', ' ')))
print('  kinds on file matching vow/oath/swear/nazir/sotah/heads/statute:')
for k in sorted(E):
    if re.search(r'vow|oath|swor|swear|nazir|sotah|heads|statute|release', k):
        print('    %-36s form %-7s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:90].replace('\n', ' ')))
print('  the ledger_op values in use: %s' % dict(collections.Counter(F[f].get('ledger_op') for f in F)))
print('  the case-form kinds of the walk (naming precedent): %s' % [k for k in E if E[k].get('form') == 'case' and re.search(r'census|naso|beha|shelach|korach|chukat|balak|libation|spies|heifer|musaf|tamid|calendar|sukkot|tishri', k)])

print('\n==== (4) THE CALLEES ON FILE, live ====')
def tryc(label, f):
    try:
        r = f(); print('  ', label, '->', str(r)[:300])
    except BaseException as e:
        print('  ', label, 'raised', type(e).__name__, str(e)[:200])
tryc('NS.nazirite(vow_form substitute)', lambda: NS.nazirite({'ask': 'vow_form', 'form': 'substitute'}, NS.DATA)[:2])
tryc('NS.nazirite(vow_form partial)', lambda: NS.nazirite({'ask': 'vow_form', 'form': 'partial'}, NS.DATA)[:2])
tryc('NS.sotah(husband_clean)', lambda: NS.sotah({'ask': 'husband_clean'}, NS.DATA)[:2])
tryc('NS.sotah(husband_clean, unclean)', lambda: NS.sotah({'ask': 'husband_clean', 'clean': False}, NS.DATA)[:2])
tryc('NS.DATA keys', lambda: sorted(NS.DATA))
tryc('V5.graded_offering(utterance_oath option True forgotten)', lambda: V5.graded_offering({'trigger': 'utterance_oath', 'act_is_his_option': True, 'oath_forgotten': True, 'means': 'reaches_lamb'}, V5.DATA))
tryc('V5.graded_offering(utterance_oath option False)', lambda: V5.graded_offering({'trigger': 'utterance_oath', 'act_is_his_option': False}, V5.DATA))
tryc('V5.DATA keys', lambda: sorted(V5.DATA))
tryc('PR.holy_food(return)', lambda: PR.holy_food('return'))
tryc('PR.holy_food(eating_table fathers_house)', lambda: PR.holy_food('eating_table', husband='israelite', son_alive=False, after='fathers_house'))
tryc('PR.family(forbidden widow high)', lambda: PR.family('forbidden', rank='high'))
tryc('MU.the_calendar(vow_deadline)', lambda: MU.the_calendar({'ask': 'vow_deadline'}, MU.DATA)[:2])
tryc('MU.DATA[vow_deadline]', lambda: (MU.DATA['vow_deadline']['value'], sorted(MU.DATA['vow_deadline']['settings'])))
tryc('MO.yom_kippur()', lambda: {k: v['v'] for k, v in MO.yom_kippur().items()})
def defs(mod):
    s = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    return re.findall(r'^def ([a-z_0-9]+)\(', s, re.M)
for name, mod in (('naso', NS), ('vayikra5', V5), ('priesthood', PR), ('musafim', MU), ('moadim', MO)):
    s = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    print('  %-12s defs %s\n  %-12s imports %s' % (name, defs(mod)[:30], '', sorted(set(re.findall(r'^\s*import (cold_run_\w+)', s, re.M)))))
# the sotah cell's asks and the priesthood's holy_food asks (the call forms)
src_ns = open(inspect.getsourcefile(NS), encoding='utf-8').read()
i = src_ns.find('def sotah('); j = src_ns.find('def nazirite(')
print('  NS.sotah asks: %s' % sorted(set(re.findall(r"ask == '([a-z_]+)'", src_ns[i:j]))))
src_pr = open(inspect.getsourcefile(PR), encoding='utf-8').read()
i = src_pr.find('def holy_food('); j = src_pr.find('def acceptable(')
print('  PR.holy_food asks: %s' % sorted(set(re.findall(r"q == '([a-z_]+)'", src_pr[i:j]))))
i = src_pr.find('def family('); j = src_pr.find('def blemish(')
print('  PR.family asks: %s' % sorted(set(re.findall(r"q == '([a-z_]+)'", src_pr[i:j]))))

print('\n==== (5) THE ENGINE\'S LITERALS ====')
print('  DAEMON_ORDER length %d, last %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-1]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s\n  SLOTS %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT, CS.SLOTS))
print('  installation_probes I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
reg = yaml.safe_load(open(f'{ROOT}/logic/corpus/entity_registry.yaml', encoding='utf-8'))
print('  registry entities %d; ids containing israel/moses/prince/head: %s' % (len(reg['entities']), [e['id'] for e in reg['entities'] if re.search(r'israel|moses|prince|head|tribe', e['id'])][:20]))
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  daemons %d; installed_by values: %s' % (len(dd['daemons']), dict(collections.Counter(v.get('installed_by') for v in dd['daemons'].values()))))
print('  the walk\'s daemons: %s' % {k: (v.get('given_at'), v.get('installed_by')) for k, v in dd['daemons'].items() if k in ('law_census', 'law_naso', 'law_musafim', 'law_zelophehad', 'law_second_census', 'law_balak')})
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d' % (len(dep['spans']), len(dep['edges']), len(dep['pointers'])))
print('  pointers at Num 30 already: %s' % [p for p in dep['pointers'] if str(p.get('verse', '')).startswith('Num 30')])
print('  edges to/from naso, vayikra5, priesthood, musafim: %s' % [(e['from'], e['to'], e['disposition']) for e in dep['edges'] if {e['from'], e['to']} & {'naso', 'vayikra5', 'priesthood', 'musafim'}][:40])
print('  the spans naming vayikra5 / priesthood / naso: %s' % {k: dep['spans'][k] for k in ('vayikra5', 'priesthood', 'naso', 'musafim') if k in dep['spans']})
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  command_relayed: %s' % {k: str(v)[:120] for k, v in ip['installing_acts']['command_relayed'].items()})

print('\n==== (6) THE REGISTER GATE — 30:1\'s receipt, the "according to ALL that" form, the footer ====')
ink = RG.read_ink()
rc = RG.receipts(ink)
print('  receipts in the census: %d; Num 30:1 among them: %s' % (len(rc), any(RG.ref(k) == 'Num 30:1' for k in rc)))
print('  the receipts of Numbers: %s' % [RG.ref(k) for k in rc if RG.ref(k).startswith('Num')])
KOL = []
for key, ws in by.items():
    lms = [lm for _, _, lm in ws]
    for i in range(len(lms) - 3):
        if lms[i].startswith('k/3605') and lms[i + 1].startswith('834') and lms[i + 2].startswith('6680') and lms[i + 3].startswith('3068'):
            KOL.append((key, i, [plain(x) for x, _, _ in ws][i:i + 6], lms[i:i + 4]))
print('  the "according to ALL that the LORD commanded" form (k/3605 834 6680 3068): %d seats — %s' % (len(KOL), [('%s %d:%d' % k, ' '.join(t)) for k, _, t, _ in KOL]))
for k, i, t, lms in KOL:
    print('     %-12s first word %-8s lemmas %s  in the receipt census: %s' % ('%s %d:%d' % k, words(*k)[0], lms, ('%s %d:%d' % k) in [RG.ref(x) for x in rc]))
print('  30:1 words: %s' % ' '.join(words('Num', 30, 1)))
print('  30:1 lemmas: %s' % [lm for _, _, lm in by[('Num', 30, 1)]])
ft = RG.footers(ink)
print('  footers: %s' % [(RG.ref(k), d) for k, d in ft][:12])
cf = RG.class_footers(ink)
print('  class_footers: %s' % {k: (v['class'] if isinstance(v, dict) else v) for k, v in cf.items()})
print('  Num 30:17 footer detail: %s' % {k: v for k, v in cf.items() if 'Num 30' in k})

print('\n==== (7) THE RECORDER/STITCHER and the sweep\'s runner list ====')
seq_src = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
print('  import lines for the walk\'s runners: %s' % re.findall(r'^import (cold_run_(?:musafim|second_census|balak|naso))', seq_src, re.M))
print('  DAEMON_ORDER tail: %s' % CS.DAEMON_ORDER[-4:])
rca = open(f'{ROOT}/World/step9/run_cold_all.py', encoding='utf-8').read()
print('  run_cold_all names musafim: %s; the runner list form: %s' % ('musafim' in rca, re.findall(r"'cold_run_musafim[^']*'", rca)[:3]))
