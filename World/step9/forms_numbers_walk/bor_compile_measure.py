import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 14b — THE COMPILE OF THE BORDERS, Numbers 34:1-29 (2026-09-13; the owner: "Go" after the #155 rereads):
# THE MEASUREMENTS, computed BEFORE the design paragraph is typed (1b's order; jou_compile_measure.py's form; every call typed from
# bor_compile_recon.out). (1) the parser at 34:1-29; (2) the tape's state — the counter, the dividers' ledger (12b's commission_charged
# line), israel_people's commanded entries (the global counts CV2 / CX2 as they stand), the lot's debit, the grant's three transfers,
# the population table's two and a half, Caleb's, Joshua's, Eleazar's, the daughters' court, the land entities; (3) the kinds and
# effects on file; (4) the callees live; (5) the installation forms and the global-count checkpoints; (6) THE REGISTER GATE on chapter
# 34; (7) the recorder and the stitcher; (8) the sanctuary runner's span (Exodus 27:9, 27:13 — the court's sides).
import sqlite3, sys, io, re, contextlib, collections, inspect, os, yaml
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import world_engine as WE
    import cold_run_second_census as C2
    import cold_run_gad_reuben as GR
    import cold_run_shelach as SL
    import cold_run_chukat as CK
    import cold_run_bamidbar as CB
    import cold_run_naso as NS
    import cold_run_korach as KR
    import cold_run_zelophehad as ZL
    import cold_run_journeys as JO
    import cold_run_erection as ER
    import cold_run_balak as BK
    import cold_run_sanctuary_build as SB
    import register_census as RG
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph, w.lemma FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by = collections.OrderedDict()
for b, c, v, he, m, lm in rows:
    by.setdefault((b, c, v), []).append((he, m, lm))
def words(b, c, v): return [plain(x) for x, _, _ in by[(b, c, v)]]
def lem(lm): return lm.split('/')[-1].split(' ')[0] if lm else ''

print('==== (1) THE PARSER AT 34:1-29 — numbers, ordinals, the marked tokens ====')
for v in range(1, 30):
    vw = CS.verse_words('Num', 34, v)
    marked = [t for t in vw if re.search(r'[#^~%@|*]', t)]
    n, o = N('Num', 34, v), O('Num', 34, v)
    if n or o or marked:
        print('  Num 34:%-3d numbers %-12s ordinals %-8s marked %s' % (v, n, o, marked))
print('  Num 35:1   numbers %s ordinals %s' % (N('Num', 35, 1), O('Num', 35, 1)))

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
def LG(t):
    e = ent(t); return e.ledger if e is not None else None
def show(t, n=40):
    e = ent(t)
    if e is None: print('  %-28s NO ENTITY on the running world (registry id %s)' % (t, reg_map.get(t))); return
    print('  %-28s id %-26s kind %-8s ledger %3d; OPEN %d' % (t, e.eid, getattr(e, 'kind', '?'), len(e.ledger), sum(1 for x in e.ledger if x.get('open'))))
    for x in e.ledger[:n]:
        print('     %-34s %-60s op %-8s open %-5s cp %-24s day %-16s src %s' % (x['effect'], str(x.get('value'))[:60], x.get('op'), x.get('open'), str(x.get('cp'))[:24], dt(x.get('day')), str(x.get('case_source', ''))[:36]))
for t in ('the-dividers-of-the-land', 'caleb', 'joshua', 'eleazar', 'the-land-of-canaan', 'the-land', 'canaan', 'the-sea', 'edom', 'the-sons-of-gad', 'the-sons-of-reuben', 'the-half-tribe-of-manasseh', 'the-daughters-of-zelophehad', 'the-court', 'the-princes-of-israel', 'the-twelve-spies'):
    show(t)
isr = ent('israel')
cmd = [x for x in isr.ledger if x['effect'] == 'commanded']
print('  israel_people ledger %d; commanded entries %d (THE GLOBAL COUNT CV2\'s len(cmd_v) kin): %s' % (len(isr.ledger), len(cmd), [(str(x.get('value'))[:44], x.get('open'), str(x.get('case_source', ''))[:14]) for x in cmd]))
print('  israel_people OPEN commanded entries %d (CX2\'s kin): %s' % (sum(1 for x in cmd if x.get('open')), [str(x.get('value'))[:44] for x in cmd if x.get('open')]))
print('  the newest commanded entry on israel_people: %s' % (str(cmd[-1].get('value'))[:60] if cmd else None))
lot = [x for x in isr.ledger if x.get('value') == 'divide_the_land']
print('  the lot\'s debit divide_the_land on israel_people: %d, open %s, source %s' % (len(lot), [x.get('open') for x in lot], [str(x.get('case_source', ''))[:20] for x in lot]))
print('  israel_people OPEN entries (all effects): %s' % [(x['effect'], str(x.get('value'))[:40], x.get('cp'), str(x.get('case_source', ''))[:20]) for x in isr.ledger if x.get('open')])
hg = [(e_.eid, x) for e_ in w.entities.values() for x in e_.ledger if x['effect'] == 'holding_given']
print('  holding_given entries on the world %d: %s' % (len(hg), [(eid, str(x.get('value'))[:50], x.get('cp'), str(x.get('case_source', ''))[:16]) for eid, x in hg]))
print('  ENTRIES ANYWHERE naming border / bound / lot / divide / inherit / Canaan / dividers (effect, value, op, open, source):')
for e_ in w.entities.values():
    for x in e_.ledger:
        s = str(x.get('effect')) + ' ' + str(x.get('value')) + ' ' + str(x.get('case_source'))
        if re.search(r'border|bound|\blot\b|divid|inherit|canaan|dividers|holding_owed|possess', s, re.I):
            print('     %-28s %-30s %-64s %-8s %-5s %s' % (e_.eid, x['effect'], str(x.get('value'))[:64], x.get('op'), x.get('open'), str(x.get('case_source', ''))[:36]))
print('  the entities whose id names land / sea / jordan / canaan / dividers / court / tribe: %s' % sorted(k for k in w.entities if re.search(r'land|sea|jordan|canaan|divid|court|tribe|prince', k)))
pop = w.population(level='tribe')
print('  population rows (level tribe) %d; the two and a half at the second census: %s' % (len(pop), [(r.get('tribe'), r.get('as_of'), r.get('count')) for r in pop if r.get('tribe') in ('reuben', 'gad', 'manasseh')]))
print('  the two and a half: 43730 + 40500 + 52700 // 2 = %d' % (43730 + 40500 + 52700 // 2))
inst = w.installation
print('  installation: setting %s; skipped %s; would_skip %s' % (inst['setting'] if inst else None, inst['skipped'] if inst else None, inst['would_skip'] if inst else None))
tfire = [l for l in w.log if l[0] == 'TIMER-FIRE']
print('  log classes: %s' % dict(collections.Counter(l[0] for l in w.log)))
print('  the clock: day + 1 = %s' % (ex.date(w.clock.day + 1),))

print('\n==== (3) THE KINDS AND EFFECTS ON FILE ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
cand_kinds = ['borders_commanded', 'land_bounded', 'borders_spoken', 'the_borders_commanded', 'moses_commanded_the_nine_and_a_half', 'nine_and_a_half_commanded', 'dividers_named', 'dividers_appointed', 'commission_named', 'borders_case', 'dividers_case', 'commission_charged', 'land_division_commanded', 'dispossession_commanded', 'command_relayed', 'spies_commanded', 'spies_sent', 'staffs_commanded', 'dedication_order_commanded', 'census_commanded']
print('  kinds on file among the candidates:', [k for k in cand_kinds if k in E])
print('  kinds NOT on file:', [k for k in cand_kinds if k not in E])
cand_fx = ['borders_declared', 'land_bounded', 'bounded', 'bounds_set', 'dividers_named', 'dividers_appointed', 'appointed_by_name', 'commanded', 'commissioned', 'agent_commissioned', 'holding_given', 'holding_owed', 'land_possessed', 'accepted', 'exempt', 'journeys_recorded', 'named', 'named_by_the_lord', 'charged']
print('  effects on file among the candidates:', [f for f in cand_fx if f in F])
print('  effects NOT on file:', [f for f in cand_fx if f not in F])
for f in ('bounds_set', 'appointed_by_name', 'agent_commissioned', 'commanded', 'holding_owed', 'accepted', 'exempt'):
    if f in F: print('   %-24s %-8s he=%s\n        %s' % (f, F[f].get('ledger_op'), str(F[f].get('he', ''))[:90], str(F[f].get('en', ''))[:260].replace('\n', ' ')))
print('  the command_relayed kind row whole: %s' % E.get('command_relayed'))
print('  kinds whose en/ink names Num 34: %s' % [(k, re.findall(r'Num 34[^;,)]*', str(E[k].get('ink', '')) + str(E[k].get('en', '')))) for k in E if 'Num 34' in str(E[k].get('ink', '')) + str(E[k].get('en', ''))])
print('  effects whose en/ink names Num 34: %s' % [(f, re.findall(r'Num 34[^;,)]*', str(F[f].get('ink', '')) + str(F[f].get('en', '')))) for f in F if 'Num 34' in str(F[f].get('ink', '')) + str(F[f].get('en', ''))])

print('\n==== (4) THE CALLEES ON FILE, live (every call typed from the recon\'s asks) ====')
def tryc(label, f):
    try:
        r = f(); print('  ', label, '->', str(r)[:640])
    except BaseException as e:
        print('  ', label, 'raised', type(e).__name__, str(e)[:200])
for q in ('by_lot', 'lots_mouth', 'by_number_of_names', 'land_divided_among', 'possession_before_assignment', 'only_excludes', 'thirteen_tribes', 'spies_portions', 'morasha', 'ten_parts', 'tribes_or_skulls', 'the_estimate', 'compensation'):
    tryc('C2.the_land(%s)' % q, lambda q=q: C2.the_land({'ask': q}, C2.DATA)[:2])
tryc('C2.DATA division_by / thirteen_tribes / spies_protesters_portions / urim_judgment', lambda: {k: C2.DATA[k] for k in ('division_by', 'thirteen_tribes', 'spies_protesters_portions', 'urim_judgment')})
for q in ('the_commission', 'second_doubling'):
    tryc('GR.the_acceptance_and_the_charge(%s)' % q, lambda q=q: GR.the_acceptance_and_the_charge({'ask': q}, GR.DATA)[:2])
for q in ('three_parties', 'the_count', 'not_by_lot', 'land_held', 'two_kingdoms', 'half_manassehs_stipulation', 'bequeath_not_inherit'):
    tryc('GR.the_grant(%s)' % q, lambda q=q: GR.the_grant({'ask': q}, GR.DATA)[:2])
for q in ('the_nine', 'the_parties', 'the_triad'):
    tryc('GR.the_request(%s)' % q, lambda q=q: GR.the_request({'ask': q}, GR.DATA)[:2])
tryc('GR.DATA the_land_east_status / half_manassehs_stipulation / the_two_crossed_cities', lambda: {k: GR.DATA[k] for k in ('the_land_east_status', 'half_manassehs_stipulation', 'the_two_crossed_cities')})
tryc('GR uppercase TRIAD_32 / TRIAD_JOSH / TRIAD_JOSH21 / HALF_MANASSEH len', lambda: (GR.TRIAD_32, GR.TRIAD_JOSH, GR.TRIAD_JOSH21, len(GR.HALF_MANASSEH), GR.HALF_MANASSEH[-3:]))
for q in ('one_per_tribe', 'fourth_order', 'joshua_caleb_equal', 'joshua_name', 'hebron_visitor', 'send_for_yourself'):
    tryc('SL.spies(%s)' % q, lambda q=q: SL.spies({'ask': q}, SL.DATA)[:2])
for q in ('caleb_entitlement', 'exceptions', 'spies_portions', 'joshua_childless'):
    tryc('SL.decree(%s)' % q, lambda q=q: SL.decree({'ask': q}, SL.DATA)[:2])
tryc('SL.SPY_TRIBES / TRIBE_LINES / JOSHUA_BEFORE len', lambda: (SL.SPY_TRIBES, SL.TRIBE_LINES, len(SL.JOSHUA_BEFORE)))
for q in ('two_mount_hors', 'succession', 'edom_passage'):
    tryc('CK.edom_and_hor(%s)' % q, lambda q=q: CK.edom_and_hor({'ask': q}, CK.DATA)[:2])
tryc('CK.well_and_kings(land_east)', lambda: CK.well_and_kings({'ask': 'land_east'}, CK.DATA)[:2])
for q in ('by_names', 'designated', 'orders', 'lineage', 'three_seats', 'threshold', 'total'):
    tryc('CB.census(%s)' % q, lambda q=q: CB.census({'ask': q}, CB.DATA)[:2])
tryc('CB.camp(sides)', lambda: CB.camp({'ask': 'sides'}, CB.DATA)[:2])
tryc('CB.TRIBES / TWELVE', lambda: (CB.TRIBES, CB.TWELVE))
for q in ('per_day', 'order', 'first_day', 'exceptions'):
    tryc('NS.dedication(%s)' % q, lambda q=q: NS.dedication({'ask': q}, NS.DATA)[:2])
tryc('NS.wagons(shoulder)', lambda: NS.wagons({'ask': 'shoulder'}, NS.DATA)[:2])
tryc('NS.work_count(princes)', lambda: NS.work_count({'ask': 'princes'}, NS.DATA)[:2])
tryc('NS.sotah(scroll_erasure)', lambda: NS.sotah({'ask': 'scroll_erasure'}, NS.DATA)[:2])
tryc('NS.DATA princes_order / prince_exceptions', lambda: {k: NS.DATA[k] for k in ('princes_order', 'prince_exceptions')})
tryc('NS.NAMES / PRINCE_TOKENS / ORDER_7 / ORDER_2', lambda: (NS.NAMES, NS.PRINCE_TOKENS, NS.ORDER_7, NS.ORDER_2))
tryc('NS.prince_of(7, 12) / (7, 18)', lambda: (NS.prince_of(7, 12), NS.prince_of(7, 18)))
for q in ('staffs_count', 'budded', 'staff_hidden'):
    tryc('KR.plague_and_staffs(%s)' % q, lambda q=q: KR.plague_and_staffs({'ask': q}, KR.DATA)[:2])
tryc('KR.STAFFS / STAFFS_21 / ONE_ONE', lambda: (KR.STAFFS, KR.STAFFS_21, KR.ONE_ONE))
for q in ('land_status', 'apportionment', 'ten_parts', 'source_of_rule'):
    tryc('ZL.inheritance_order(%s)' % q, lambda q=q: ZL.inheritance_order({'ask': q}, ZL.DATA)[:2])
for q in ('the_run', 'execution', 'reach', 'three_portions'):
    tryc('ZL.the_daughters(%s)' % q, lambda q=q: ZL.the_daughters({'ask': q}, ZL.DATA)[:2])
tryc('ZL.DATA land_divided_among / eretz_yisrael_status', lambda: {k: ZL.DATA[k] for k in ('land_divided_among', 'eretz_yisrael_status')})
for q in ('the_lot_restated', 'the_lot_arms', 'possess_and_dwell', 'when_you_pass', 'the_frame'):
    tryc('JO.the_command(%s)' % q, lambda q=q: JO.the_command({'ask': q}, JO.DATA)[:2])
tryc('JO.DATA the_lot_restated / the_three_objects values', lambda: (JO.DATA['the_lot_restated']['value'], JO.DATA['the_three_objects']['value']))
tryc('JO.STATIONS len / PLACES_EN len / the Kadesh, Mount Hor stations', lambda: (len(JO.STATIONS), len(JO.PLACES_EN), [s for s in JO.STATIONS if re.search(r'Kadesh|Hor|Zin', str(s.get('en', '')))][:4]))
for q in ('nations_seven_orders', 'demolition_grows', 'no_bow_by_call'):
    tryc('ER.covenant(%s)' % q, lambda q=q: (ER.covenant(q)['v'], ER.covenant(q)['fx']))
tryc('BK.the_call(last_camp)', lambda: BK.the_call({'ask': 'last_camp'}, BK.DATA)[:2])
src_sb = open(inspect.getsourcefile(SB), encoding='utf-8').read()
print('  SB (sanctuary_build) defs: %s' % re.findall(r'^def ([a-z_0-9]+)\(', src_sb, re.M))
print('  SB lines naming 27:9 / 27:13 / side / south / east / court: %s' % [l.strip()[:200] for l in src_sb.split('\n') if re.search(r"27:9|27:13|'side|south|east side|the court|פאת", l)][:12])
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  the spans of sanctuary_build / erection / vestments: %s' % {k: dep['spans'][k] for k in ('sanctuary_build', 'erection', 'vestments') if k in dep['spans']})

print('\n==== (5) THE INSTALLATION FORMS AND THE GLOBAL-COUNT CHECKPOINTS (grepped BEFORE the tape run — 13b\'s lesson) ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
for pat in (r"the-dividers-of-the-land", r"len\(cmd_v\)", r"isr_cmd", r"holding_given", r"len\(w\.entities\)", r"closes_done", r"'commanded'", r"the_dividers", r"divide_the_land", r"caleb", r"holding_owed"):
    hits = [l.strip()[:200] for l in src_cs.split('\n') if re.search(pat, l) and ('cp(' in l or re.search(r"^\s*[a-z_0-9]+ = \[", l.strip()))]
    print('  %-28s %d lines: %s' % (pat, len(hits), hits[:6]))
print('  the CZ7 line whole: %s' % [l.strip()[:900] for l in src_cs.split('\n') if "cp('CZ7" in l][:1])
print('  the CV2 line whole: %s' % [l.strip()[:700] for l in src_cs.split('\n') if "cp('CV2" in l][:1])
print('  the CX2 line whole: %s' % [l.strip()[:700] for l in src_cs.split('\n') if "cp('CX2" in l][:1])
print('  the CY lines naming the dividers or the commission: %s' % [l.strip()[:500] for l in src_cs.split('\n') if "cp('CY" in l and re.search(r'divider|commission|charge', l)][:3])
print('  the lines defining cmd_v / isr_cmd / gr_* lists: %s' % [l.strip()[:220] for l in src_cs.split('\n') if re.search(r"^\s*(cmd_v|isr_cmd|div_cmd|gr_[a-z_]+|dv_[a-z_]+) = ", l)][:12])
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing act command_relayed: %s' % {kk: str(vv)[:300] for kk, vv in ip['installing_acts']['command_relayed'].items()})
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  law_zelophehad block head: %s' % {k: str(v)[:300] for k, v in dd['daemons']['law_zelophehad'].items() if k != 'watches'})
print('  register_probes count: %s; census_probes count: %s' % (len(re.findall(r"^def (R\d+|probe_\w+)\(", open(f'{ROOT}/World/step9/register_probes.py', encoding='utf-8').read(), re.M)), len(re.findall(r"^\s*\('[A-Z]+\d+", open(f'{ROOT}/World/step9/census_probes.py', encoding='utf-8').read(), re.M))))

print('\n==== (6) THE REGISTER GATE on chapter 34 (computed on the running world) ====')
ink = RG.read_ink()
cc = RG.class_counts(ink, w)
print('  count lines in Num 34: %s' % [(r, d['class'], d['noun'], d.get('counts'), d.get('measures')) for r, d in cc.items() if r.startswith('Num 34:')])
cr = RG.class_receipts(ink, w)
print('  receipts in Num 34: %s' % [(r, d['class'], d['evidence']) for r, d in cr.items() if r.startswith('Num 34:')])
cf = RG.class_footers(ink)
print('  footers naming Num 3x: %s' % {k: (v['class'] if isinstance(v, dict) else v) for k, v in cf.items() if 'Num 3' in k})
try:
    rh = RG.register_headers(ink)
    items = rh.items() if isinstance(rh, dict) else enumerate(rh)
    print('  register headers naming Num 34: %s' % [(k, str(v)[:300]) for k, v in items if 'Num 34' in str(k) + str(v)][:5])
except BaseException as e:
    print('  register_headers raised', type(e).__name__, str(e)[:120])
try:
    print('  RG names with header/register: %s' % [n for n in dir(RG) if re.search(r'header|register|census', n)])
except BaseException as e:
    print('  dir raised', e)
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the declared Num 34 seat whole: %s' % decl.get('registers', {}).get('Num 34'))
print('  the registers section keys: %s' % list(decl.get('registers', {}).keys()))
print('  a PAID/LEDGER register seat\'s form (if any): %s' % [(k, v) for k, v in decl.get('registers', {}).items() if v.get('class') != 'NONE'][:2])

print('\n==== (7) THE RECORDER/STITCHER ====')
print('  import lines for the walk\'s runners: %s' % re.findall(r'^import (cold_run_(?:journeys|gad_reuben|midian|vows))', src_cs, re.M))
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
print('  the CZ1 checkpoint\'s whole line (the form to copy): %s' % [l.strip()[:700] for l in src_cs.split('\n') if "cp('CZ1" in l][:1])
print('  the CZ9 line whole: %s' % [l.strip()[:500] for l in src_cs.split('\n') if "cp('CZ9" in l][:1])
print('  the lines before CZ1 (JO_KINDS, ev_jo, i36v definitions): %s' % [l.strip()[:200] for l in src_cs.split('\n') if re.search(r"^\s*(JO_KINDS|ev_jo|i36v|ev_gr) = ", l)][:6])
