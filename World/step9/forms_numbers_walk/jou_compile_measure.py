#!/usr/bin/env python3
# THE NUMBERS WALK sitting 13b — THE COMPILE OF THE JOURNEYS, Numbers 33:1-56 (2026-09-12; the owner: "Go" after the #152 rereads):
# THE MEASUREMENTS, computed BEFORE the design paragraph is typed (1b's order; gad_compile_measure.py's form; every call typed from
# jou_compile_recon.out). (1) the parser at 33:1-56 and at the retellings' number verses; (2) the tape's state — the counter, the
# markers WHOLE (the dated stations), the encamped_at entries on israel_people, the station events with their fields, the entries citing
# Exodus 12:12 or naming judgments/gods, Aaron's, Arad's, Egypt's and Heaven's dockets, the open entries on israel_people, the land
# entities; (3) the kinds and effects on file; (4) the callees live; (5) the engine's literals and the installation registry's forms;
# (6) THE REGISTER GATE on chapter 33; (7) the recorder and the stitcher; (8) THE STATIONS BY LEMMA on the DB — every proper name of
# 33:5-49 with its lemma's seats in the whole Bible (the first telling computed, never typed).
import sqlite3, sys, io, re, contextlib, collections, inspect, os, yaml
ROOT = '<repo-old>'
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import world_engine as WE
    import cold_run_exodus_story as ES
    import cold_run_beha as BH
    import cold_run_shelach as SL
    import cold_run_chukat as CK
    import cold_run_balak as BK
    import cold_run_second_census as C2
    import cold_run_zelophehad as ZL
    import cold_run_gad_reuben as GR
    import cold_run_tochacha as TC
    import cold_run_holiness as HL
    import cold_run_erection as ER
    import cold_run_pesach as PS
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
TORAH = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def lem(lm): return lm.split('/')[-1].split(' ')[0] if lm else ''

print('==== (1) THE PARSER AT 33:1-56 — numbers, ordinals, the marked tokens ====')
for v in range(1, 57):
    vw = CS.verse_words('Num', 33, v)
    marked = [t for t in vw if re.search(r'[#^~%@|*]', t)]
    n, o = N('Num', 33, v), O('Num', 33, v)
    if n or o or marked:
        print('  Num 33:%-3d numbers %-12s ordinals %-8s marked %s' % (v, n, o, marked))
print('  Num 34:1   numbers %s ordinals %s' % (N('Num', 34, 1), O('Num', 34, 1)))
print('---- the retellings and the callees\' number verses ----')
for k in [('Exod', 7, 7), ('Deut', 34, 7), ('Deut', 1, 3), ('Exod', 12, 37), ('Exod', 12, 40), ('Exod', 12, 41), ('Exod', 12, 51), ('Exod', 16, 1), ('Exod', 19, 1), ('Exod', 15, 22), ('Exod', 15, 27), ('Num', 10, 11), ('Num', 10, 33), ('Num', 14, 33), ('Num', 14, 34), ('Num', 20, 29), ('Num', 21, 4), ('Deut', 2, 14), ('Deut', 10, 6), ('Deut', 10, 7), ('Josh', 5, 10), ('Josh', 5, 11), ('Josh', 5, 12), ('1Kgs', 6, 1), ('Num', 26, 55), ('Num', 26, 56), ('Lev', 26, 30), ('Lev', 26, 1), ('Lev', 19, 4), ('Exod', 32, 4), ('Exod', 12, 12), ('Josh', 23, 13), ('Judg', 2, 3), ('Exod', 23, 24), ('Exod', 34, 13), ('Deut', 7, 5), ('Deut', 12, 2), ('Deut', 12, 3)]:
    if k in by:
        vw = CS.verse_words(*k)
        print('  %s %d:%d numbers %s ordinals %s   words: %s' % (k[0], k[1], k[2], CS.ink_numbers(vw), CS.ink_ordinals(vw), ' '.join(words(*k))[:170]))
    else:
        print('  %s NOT IN DB under that book key' % (k,))

print('\n==== (2) THE TAPE\'S STATE — the running world ====')
with contextlib.redirect_stdout(io.StringIO()):
    w = RG.running_world()
ex = w.clock.eras['exodus']
def dt(d):
    try: return ex.date(d)
    except BaseException: return ('pre-exodus day', d)
print('  the counter: day %d = %s (exodus era); entities %d; log lines %d; timers pending %d' % (w.clock.day, ex.date(w.clock.day), len(w.entities), len(w.log), len(w.timers)))
print('  the pending timers: %s' % [(t[1].get('subject'), t[1].get('effect'), t[1].get('period'), dt(t[0])) for t in w.timers])
mk = [l for l in w.log if l[0] == 'MARKER']
print('  markers %d — ALL, in order (verse, date, placement, value head):' % len(mk))
for l in mk:
    print('     %-12s %-22s %-17s %s' % (l[2].get('verse'), dt(l[1]), l[2].get('placement'), str(l[2].get('value', ''))[:95]))
EVs = [l for l in w.log if l[0] == 'EVENT']
print('  events %d; the last four kinds: %s' % (len(EVs), [(l[2]['kind'], str(l[2].get('case_source', ''))[:30], dt(l[1])) for l in EVs[-4:]]))
print('  THE STATION EVENTS on the tape (kind, subject, the to/at/stations field, date, placement, source):')
for l in EVs:
    k = l[2]['kind']
    if re.search(r'^journeyed|encamped|paran_reached|arad_fought|garments_transferred|aaron_brought|miriam_died|calf_made|land_division_commanded|cities_built_east|people_whored|firstborn_death|saved_at_the_sea|sea_split|sea_returned|manna_fell|amalek_came|jethro_came|pillar_set', k) and l[2].get('subject') in ('israel', 'israel_people', 'aaron', 'moses', 'the-king-of-arad', 'miriam', 'the-sons-of-gad-and-reuben', 'pharaoh', 'the-people'):
        print('     %-40s %-22s %-70s %-20s %-16s %s' % (k, l[2].get('subject'), str(l[2].get('to', l[2].get('at', l[2].get('stations', l[2].get('from', '')))))[:70], dt(l[1]), l[2].get('placement'), str(l[2].get('case_source', ''))[:40]))
reg_map = CS.registry_map()
def ent(t): return w.entities.get(reg_map.get(t, t))
isr = ent('israel')
print('  israel_people ledger %d entries; the encamped_at entries (%d) — value head, date, source:' % (len(isr.ledger), sum(1 for x in isr.ledger if x['effect'] == 'encamped_at')))
for x in isr.ledger:
    if x['effect'] == 'encamped_at':
        print('     %-22s %-90s %s' % (dt(x.get('day')), str(x.get('value'))[:90], str(x.get('case_source', ''))[:36]))
print('  israel_people OPEN entries: %s' % [(x['effect'], str(x.get('value'))[:50], x.get('cp'), str(x.get('case_source', ''))[:24]) for x in isr.ledger if x.get('open')])
print('  israel_people entries citing Exod 12 / 13 / 14 (the exodus and the sea): %s' % [(x['effect'], str(x.get('value'))[:40], x.get('op'), x.get('open'), str(x.get('case_source', ''))[:20]) for x in isr.ledger if re.match(r'Exod 1[234]:', str(x.get('case_source', '')))])
print('  ENTRIES ANYWHERE naming judgments / gods / idols / 12:12 (effect, value, op, open, source):')
for e_ in w.entities.values():
    for x in e_.ledger:
        s = str(x.get('effect')) + ' ' + str(x.get('value')) + ' ' + str(x.get('case_source')) + ' ' + str(x.get('law'))
        if re.search(r'judg|gods|idol|12:12|high_place|molten|figured|drive|dispossess|nations_driven', s, re.I):
            print('     %-26s %-32s %-60s %-8s %-5s %s' % (e_.eid, x['effect'], str(x.get('value'))[:60], x.get('op'), x.get('open'), str(x.get('case_source', ''))[:40]))
for t in ('aaron', 'the-king-of-arad', 'moses', 'eleazar', 'egypt_people', 'the_land_of_egypt', 'pharaoh', 'the-nations', 'the-land', 'the_land_of_canaan', 'canaan', 'the-calf', 'the-tabernacle', 'heaven', 'moab', 'edom'):
    e = w.entities.get(reg_map.get(t, t))
    if e is None: print('  %-20s NO ENTITY (registry id %s)' % (t, reg_map.get(t))); continue
    opens = [(x['effect'], str(x.get('value'))[:40], x.get('cp'), str(x.get('case_source', ''))[:24]) for x in e.ledger if x.get('open')]
    print('  %-20s id %-24s kind %-10s ledger %3d; OPEN %d: %s' % (t, e.eid, getattr(e, 'kind', '?'), len(e.ledger), len(opens), opens[:12]))
    if t in ('aaron', 'the-king-of-arad', 'the-nations', 'the-land', 'the_land_of_canaan', 'canaan', 'the-calf', 'egypt_people', 'the_land_of_egypt', 'pharaoh'):
        print('     ledger whole: %s' % [(x['effect'], str(x.get('value'))[:36], x.get('op'), x.get('open'), str(x.get('case_source', ''))[:18]) for x in e.ledger][:30])
print('  the entities whose id names a land / people / place: %s' % sorted(k for k in w.entities if re.search(r'land|nation|people|egypt|canaan|moab|edom|amorite|midian|arad|the-calf|heaven|the-mountain|the-sea', k))[:60])
tfire = [l for l in w.log if l[0] == 'TIMER-FIRE']
print('  fired timers naming forty/carcass/decree: %s' % [(l[2].get('subject'), l[2].get('effect'), dt(l[1])) for l in tfire if re.search(r'forty|carcass|decree|wander', str(l[2]))][:8])
inst = w.installation
print('  installation: setting %s; skipped %s; would_skip %s; fields %d' % (inst['setting'] if inst else None, inst['skipped'] if inst else None, inst['would_skip'] if inst else None, len(inst['fields']) if inst else 0))
print('  registry_map for the chapter\'s tokens: %s' % {t: reg_map.get(t) for t in ('israel', 'moses', 'aaron', 'eleazar', 'egypt', 'the-egyptians', 'pharaoh', 'the-canaanite', 'the-king-of-arad', 'edom', 'the-land', 'the-land-of-canaan', 'canaan', 'the-inhabitants-of-the-land', 'the-nations', 'the-lord', 'heaven', 'the-calf', 'the-tabernacle', 'moab', 'the-sons-of-gad', 'the-sons-of-gad-and-reuben') if reg_map.get(t)})
print('  the clock: day + 1 = %s' % (ex.date(w.clock.day + 1),))
print('  population table tribe rows (as_of, count) — the count at the last census: %s' % [(r.get('tribe'), r.get('as_of'), r.get('count')) for r in w.population(level='tribe')][-14:])

print('\n==== (3) THE KINDS AND EFFECTS ON FILE ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
cand_kinds = ['journeys_written', 'itinerary_written', 'stations_written', 'moses_wrote_the_journeys', 'departed_with_a_high_hand', 'departed_from_rameses', 'egypt_buried_its_firstborn', 'judgments_on_the_gods_recorded', 'stations_recorded', 'station_recorded', 'itinerary_station', 'aaron_died_on_mount_hor', 'aaron_death_dated', 'arad_heard', 'dispossession_commanded', 'inhabitants_to_be_driven_out', 'possession_commanded', 'lot_division_commanded', 'negative_arm_warned', 'command_in_the_plains_of_moab', 'journeys_case', 'stations_case', 'dispossession_case', 'lot_case', 'journeyed', 'encamped_in_the_plains_of_moab', 'land_division_commanded', 'calf_made', 'entered_the_land', 'covenant_cut_at_sinai', 'nations_driven_out']
print('  kinds on file among the candidates:', [k for k in cand_kinds if k in E])
print('  kinds NOT on file:', [k for k in cand_kinds if k not in E])
cand_fx = ['commanded', 'encamped_at', 'journeys_written', 'written', 'wrote', 'recorded', 'judgments_executed', 'gods_judged', 'nations_driven_out', 'inhabitants_driven_out', 'dispossessed', 'to_dispossess', 'high_places_banned', 'high_places_demolished', 'molten_image_barred', 'molten_images_destroyed', 'figured_stones_destroyed', 'idols_destroyed', 'land_possessed', 'holding_given', 'holding_owed', 'possessed_and_dwelt', 'dwelt_in_the_land', 'divided_by_lot', 'inherited_by_lot', 'thorns_in_your_eyes', 'harassed', 'land_desolate', 'died', 'died_on_mount_hor', 'garments_inherited', 'plague_struck', 'plague_removed', 'firstborn_struck', 'firstborn_death_decreed', 'nation_to_be_judged', 'brought_out', 'to_be_brought_to_the_land', 'accepted', 'exempt', 'disqualified', 'plea_made', 'sentence_pronounced', 'defeated', 'taken_captive', 'devoted']
print('  effects on file among the candidates:', [f for f in cand_fx if f in F])
print('  effects NOT on file:', [f for f in cand_fx if f not in F])
for f in ('commanded', 'nations_driven_out', 'high_places_banned', 'molten_image_barred', 'land_possessed', 'nation_to_be_judged', 'firstborn_struck', 'brought_out', 'to_be_brought_to_the_land', 'plague_struck', 'plague_removed', 'land_desolate', 'taken_captive', 'devoted', 'died'):
    if f in F: print('   %-24s %-8s he=%s\n        %s' % (f, F[f].get('ledger_op'), str(F[f].get('he', ''))[:80], str(F[f].get('en', ''))[:240].replace('\n', ' ')))
print('  the effects whose en names Exod 12:12 or "judgments": %s' % [f for f in F if re.search(r'12:12|judgments on|gods of egypt', str(F[f].get('en', '')) + str(F[f].get('ink', '')))])
print('  the kinds whose en/ink names Exod 12:12 or "gods of Egypt": %s' % [k for k in E if re.search(r'12:12|gods of egypt|judgments', str(E[k].get('en', '')) + str(E[k].get('ink', '')), re.I)])
print('  kinds whose ink names Num 33: %s' % [(k, re.findall(r'Num 33[^;,)]*', str(E[k].get('ink', '')))) for k in E if 'Num 33' in str(E[k].get('ink', ''))])
print('  effects whose ink names Num 33: %s' % [(f, re.findall(r'Num 33[^;,)]*', str(F[f].get('ink', '')))) for f in F if 'Num 33' in str(F[f].get('ink', ''))])

print('\n==== (4) THE CALLEES ON FILE, live ====')
def tryc(label, f):
    try:
        r = f(); print('  ', label, '->', str(r)[:520])
    except BaseException as e:
        print('  ', label, 'raised', type(e).__name__, str(e)[:200])
for q in ('stations', 'firstborn', 'midnight', 'wage', 'transitions', 'garments', 'sent_formula', 'by_day'):
    tryc('ES.night(%s)' % q, lambda q=q: ES.night(q))
for q in ('ten', 'removed', 'first_divine', 'agents', 'sea_count', 'twelve_months'):
    tryc('ES.plagues(%s)' % q, lambda q=q: ES.plagues(q))
tryc('ES.marah(three_days)', lambda: ES.marah('three_days'))
tryc('ES.manna(forty_years)', lambda: ES.manna('forty_years'))
tryc('ES.sinai(new_moon)', lambda: ES.sinai('new_moon'))
tryc('ES.trials(count_by_exodus)', lambda: ES.trials('count_by_exodus'))
tryc('ES.STRUCK / REMOVED / PLAGUES', lambda: (ES.STRUCK, ES.REMOVED, ES.PLAGUES))
for q in ('date', 'three_days', 'day_stack', 'order', 'clouds', 'year_turns'):
    tryc('BH.march(%s)' % q, lambda q=q: BH.march({'ask': q}, BH.DATA)[:2])
tryc('BH.taberah_and_quail(graves)', lambda: BH.taberah_and_quail({'ask': 'graves'}, BH.DATA)[:2])
tryc('BH.DATA spies_sent_day', lambda: BH.DATA['spies_sent_day'])
tryc('BH.DATE / DATE_ORD / DAY_LADDER / THREE_DAYS', lambda: (BH.DATE, BH.DATE_ORD, BH.DAY_LADDER, BH.THREE_DAYS))
tryc('SL.spies(forty_days)', lambda: SL.spies({'ask': 'forty_days'}, SL.DATA)[:2])
for q in ('turn_back', 'hormah', 'count_from', 'deaths_ceased', 'due', 'set', 'wilderness_share', 'day_for_year'):
    tryc('SL.decree(%s)' % q, lambda q=q: SL.decree({'ask': q}, SL.DATA)[:2])
tryc('SL.high_hand(high_hand_posture)', lambda: SL.high_hand({'ask': 'high_hand_posture'}, SL.DATA)[:2])
tryc('SL.FORTY / FORTY_YEARS / DUE_38 / RETURN_DAY', lambda: (SL.FORTY, SL.FORTY_YEARS, SL.DUE_38, SL.RETURN_DAY))
for q in ('aaron_age', 'arad_heard', 'death_dates', 'moserah', 'seder_olam_walk', 'thirty_days', 'two_mount_hors', 'succession', 'edom_passage'):
    tryc('CK.edom_and_hor(%s)' % q, lambda q=q: CK.edom_and_hor({'ask': q}, CK.DATA)[:2])
for q in ('hormah', 'turn_back', 'captive_acquired', 'cherem_law'):
    tryc('CK.arad_and_the_serpent(%s)' % q, lambda q=q: CK.arad_and_the_serpent({'ask': q}, CK.DATA)[:2])
for q in ('zered_date', 'land_east', 'mattanah_reading'):
    tryc('CK.well_and_kings(%s)' % q, lambda q=q: CK.well_and_kings({'ask': q}, CK.DATA)[:2])
tryc('CK.DATA moserah / arad_heard / miriam_death_day / captive_count', lambda: {k: CK.DATA[k] for k in ('moserah', 'arad_heard', 'miriam_death_day', 'captive_count')})
tryc('CK.AARON_AGE / AARON_DATE / D_AARON / D_DEPART / D_HOR / D_ZIN / DAYS30 / D_DUE38 / D33 / D34 / D35', lambda: (CK.AARON_AGE, CK.AARON_DATE, CK.D_AARON, CK.D_DEPART, CK.D_HOR, CK.D_ZIN, CK.DAYS30, CK.D_DUE38, CK.D33, CK.D34, CK.D35))
tryc('CK.MOSES_MOURNED / FIRST_MONTH / D_DEPART', lambda: (CK.MOSES_MOURNED, CK.FIRST_MONTH, CK.D_DEPART))
tryc('BK.the_call(last_camp)', lambda: BK.the_call({'ask': 'last_camp'}, BK.DATA)[:2])
tryc('BK.peor(shittim_name)', lambda: BK.peor({'ask': 'shittim_name'}, BK.DATA)[:2])
tryc('BK.DATA shittim_name', lambda: BK.DATA['shittim_name'])
for q in ('by_lot', 'lots_mouth', 'by_number_of_names', 'land_divided_among', 'thirteen_tribes', 'possession_before_assignment', 'ten_parts', 'the_estimate', 'tribes_or_skulls'):
    tryc('C2.the_land(%s)' % q, lambda q=q: C2.the_land({'ask': q}, C2.DATA)[:2])
tryc('C2.DATA division_by / thirteen_tribes', lambda: {k: C2.DATA[k] for k in ('division_by', 'thirteen_tribes')})
tryc('ZL.inheritance_order(land_status)', lambda: ZL.inheritance_order({'ask': 'land_status'}, ZL.DATA)[:2])
tryc('ZL.DATA eretz_yisrael_status', lambda: ZL.DATA['eretz_yisrael_status'])
tryc('GR.the_cities(dibon_gad)', lambda: GR.the_cities({'ask': 'dibon_gad'}, GR.DATA)[:2])
tryc('GR.the_grant(not_by_lot)', lambda: GR.the_grant({'ask': 'not_by_lot'}, GR.DATA)[:2])
tryc('GR.the_condition(negative_arm_outcome)', lambda: GR.the_condition({'ask': 'negative_arm_outcome'}, GR.DATA)[:2])
tryc('GR.DATA the_land_east_status / negative_arm_outcome', lambda: {k: GR.DATA[k] for k in ('the_land_east_status', 'negative_arm_outcome')})
tryc('HL.frame(molten_warnings)', lambda: HL.frame('molten_warnings'))
tryc('HL.frame(idols_look)', lambda: HL.frame('idols_look'))
for q in ('molten_two_seats', 'demolition_first_seat', 'demolition_grows', 'pillars_exod', 'nations_seven_orders', 'no_bow_by_call'):
    tryc('ER.covenant(%s)' % q, lambda q=q: ER.covenant(q))
tryc('ER.calf(molten_calf)', lambda: ER.calf('molten_calf'))
tryc('ER.DEMOL', lambda: ER.DEMOL)
src_tc = open(inspect.getsourcefile(TC), encoding='utf-8').read()
print('  TC (tochacha) lines naming 26:1 / 26:30 / high places / figured / pillar / idols: %s' % [l.strip()[:200] for l in src_tc.split('\n') if re.search(r"26:1\b|26:30|high place|figured|pillar|idol|DESOLATE", l)][:14])
tryc('TC.DESOLATE', lambda: TC.DESOLATE)
tryc('TC cells (defs with their first lines)', lambda: [l.strip()[:100] for l in src_tc.split('\n') if l.startswith('def ')])
src_ps = open(inspect.getsourcefile(PS), encoding='utf-8').read()
i = src_ps.find('\ndef firstborn('); j = src_ps.find('\ndef ', i + 1)
print('  PS.firstborn body head: %s' % src_ps[i:i + 600].replace('\n', ' | '))
print('  PS lines naming 12:12 / gods / judgments: %s' % [l.strip()[:200] for l in src_ps.split('\n') if re.search(r'12:12|gods|judgment', l)][:8])
src_es = open(inspect.getsourcefile(ES), encoding='utf-8').read()
print('  ES lines naming 12:12 / gods / nation_to_be_judged / 12:29: %s' % [l.strip()[:240] for l in src_es.split('\n') if re.search(r'12:12|gods of|nation_to_be_judged|12:29', l)][:10])
print('  ES.night cell whole (the stations line and its neighbours): %s' % [l.strip()[:300] for l in src_es.split('\n') if "q == 'stations'" in l or "q == 'firstborn'" in l or "q == 'transitions'" in l][:4])

print('\n==== (5) THE ENGINE\'S LITERALS AND THE INSTALLATION FORMS ====')
print('  DAEMON_ORDER length %d, last %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-1]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s\n  SLOTS %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT, CS.SLOTS))
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
for k in ('called_from_the_tent', 'statute_declared', 'command_relayed', 'entered_the_land'):
    print('  installing act %s: %s' % (k, {kk: str(vv)[:300] for kk, vv in ip['installing_acts'][k].items()}))
print('  installation_parameters top keys: %s; the boot note: %s' % (list(ip), str(ip.get('boot', ip.get('notes', '')))[:400]))
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  daemons %d; installed_by values: %s' % (len(dd['daemons']), dict(collections.Counter(v.get('installed_by') for v in dd['daemons'].values()))))
print('  the daemons installed_by called_from_the_tent (given_at): %s' % {k: v.get('given_at') for k, v in dd['daemons'].items() if v.get('installed_by') == 'called_from_the_tent'})
print('  the law_musafim block head (given_at, installed_by, the comment): %s' % {k: str(v)[:400] for k, v in dd['daemons']['law_musafim'].items() if k != 'watches'})
print('  the law_vows block head: %s' % {k: str(v)[:400] for k, v in dd['daemons']['law_vows'].items() if k != 'watches'})
print('  the law_chukat block head: %s' % {k: str(v)[:300] for k, v in dd['daemons']['law_chukat'].items() if k != 'watches'})
print('  register_probes count: %s; census_probes count: %s' % (len(re.findall(r"^def (R\d+|probe_\w+)\(", open(f'{ROOT}/World/step9/register_probes.py', encoding='utf-8').read(), re.M)), len(re.findall(r"^\s*\('[A-Z]+\d+", open(f'{ROOT}/World/step9/census_probes.py', encoding='utf-8').read(), re.M))))
cal = yaml.safe_load(open(f'{ROOT}/World/step9/calendar_parameters.yaml', encoding='utf-8'))
P_ = cal['parameters'] if 'parameters' in cal else cal
print('  calendar_parameters rows %d; rows naming aaron/hor/av/mourn/manna/morrow: %s' % (len(P_), {k: str(P_[k])[:200] for k in P_ if re.search(r'aaron|hor|\bav\b|mourn|manna|morrow|passover|nisan', k, re.I)}))

print('\n==== (6) THE REGISTER GATE on chapter 33 (computed on the running world) ====')
ink = RG.read_ink()
cc = RG.class_counts(ink, w)
print('  count lines in Num 33: %s' % [(r, d['class'], d['noun'], d.get('counts'), d.get('measures')) for r, d in cc.items() if r.startswith('Num 33:')])
cr = RG.class_receipts(ink, w)
print('  receipts in Num 33: %s' % [(r, d['class'], d['evidence']) for r, d in cr.items() if r.startswith('Num 33:')])
cf = RG.class_footers(ink)
print('  footers naming Num 3x: %s' % {k: (v['class'] if isinstance(v, dict) else v) for k, v in cf.items() if 'Num 3' in k})
try:
    rh = RG.register_headers(ink)
    print('  register headers in Num 33: %s' % [(k, v) for k, v in (rh.items() if isinstance(rh, dict) else enumerate(rh)) if 'Num 33' in str(k) + str(v)][:5])
except BaseException as e:
    print('  register_headers raised', type(e).__name__, str(e)[:120])
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  declared seats naming Num 33 (counts / receipts / footers / registers): %s' % [(sec, [k for k in decl.get(sec, {}) if 'Num 33' in k]) for sec in ('counts', 'receipts', 'footers', 'registers')])
print('  declared counts %d receipts %d footers %d registers %d' % tuple(len(decl.get(s, {})) for s in ('counts', 'receipts', 'footers', 'registers')))
print('  the receipt classes on file (a sample of the receipt rows\' evidence forms): %s' % collections.Counter(d['class'] for d in cr.values()))
print('  the "by the mouth of the LORD" receipts on file (class, verse): %s' % [(r, d['class'], str(d['evidence'])[:60]) for r, d in cr.items() if 'פי' in str(d['evidence']) or 'mouth' in str(d['evidence'])][:20])
print('  Num 33 verses with a count-noun (6485 / 4557 / 5315): %s' % [(v, [lem(lm) for _, _, lm in by[('Num', 33, v)] if lem(lm) in ('6485', '4557', '5315')]) for v in range(1, 57) if any(lem(lm) in ('6485', '4557', '5315') for _, _, lm in by[('Num', 33, v)])])
print('  Num 33 verses with the receipt formula lemmas (834 + 6680 + 3068): %s' % [v for v in range(1, 57) if {'834', '6680', '3068'} <= {lem(lm) for _, _, lm in by[('Num', 33, v)]}])
print('  Num 33 verses with "by the mouth of the LORD" (6310 + 3068 adjacent): %s' % [v for v in range(1, 57) if any(lem(by[('Num', 33, v)][i][2]) == '6310' and lem(by[('Num', 33, v)][i + 1][2]) == '3068' for i in range(len(by[('Num', 33, v)]) - 1))])

print('\n==== (7) THE RECORDER/STITCHER ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
print('  import lines for the walk\'s runners: %s' % re.findall(r'^import (cold_run_(?:vows|midian|gad_reuben|second_census|balak))', src_cs, re.M))
SP = os.path.dirname(os.path.abspath(__file__))
st = open(f'{SP}/seq_stitch.py', encoding='utf-8').read()
print('  seq_stitch SPAN_ORDER: %s' % re.findall(r"SPAN_ORDER\s*=\s*\[([^\]]*)\]", st)[:1])
rc = open(f'{SP}/seq_record.py', encoding='utf-8').read()
print('  seq_record recording path: %s' % re.findall(r"seq_recording\.json[^\n]*", rc)[:2])
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
print('  the tape\'s Num 32 last line and Num 36 first line: %s' % [l.strip()[:140] for l in tape.split('\n') if 'kenath_taken_by_nobah' in l or 'tribes_approached' in l])
print('  the section markers in the tape: %s' % re.findall(r'# ---- (Num \d+) ----', tape))
print('  cp() checkpoints on file (tail): %s' % re.findall(r"cp\('(C[A-Z]\d)", src_cs)[-12:])
print('  the VERDICTS block\'s CY lines: %s' % [l.strip()[:120] for l in src_cs.split('\n') if re.search(r"^\s*\('CY\d'|CY\d.*VERDICT", l)][:10])
print('  the CY1 checkpoint\'s whole line (the form to copy): %s' % [l.strip()[:600] for l in src_cs.split('\n') if "cp('CY1" in l][:1])
print('  the walk\'s runner registration lines (the tail of the imports): %s' % [l.strip()[:120] for l in src_cs.split('\n') if 'cold_run_gad_reuben' in l][:4])

print('\n==== (8) THE STATIONS BY LEMMA — every proper name of 33:5-49 with its lemma\'s seats (the first telling computed) ====')
seats_by_lemma = collections.defaultdict(list)
for (b, c, v), ws in by.items():
    for he, m, lm in ws:
        if 'Np' in (m or ''):
            seats_by_lemma[lem(lm)].append((b, c, v))
order = {b: i for i, b in enumerate(['Gen', 'Exod', 'Lev', 'Num', 'Deut', 'Josh', 'Judg', '1Sam', '2Sam', '1Kgs', '2Kgs', 'Isa', 'Jer', 'Ezek', 'Hos', 'Joel', 'Amos', 'Obad', 'Jonah', 'Mic', 'Nah', 'Hab', 'Zeph', 'Hag', 'Zech', 'Mal', 'Ps', 'Prov', 'Job', 'Song', 'Ruth', 'Lam', 'Eccl', 'Esth', 'Dan', 'Ezra', 'Neh', '1Chr', '2Chr'])}
def sk(s): return (order.get(s[0], 99), s[1], s[2])
def fmt(s): return '%s %d:%d' % s
for v in range(1, 57):
    ws = by[('Num', 33, v)]
    names = [(plain(he), lem(lm), m) for he, m, lm in ws if 'Np' in (m or '')]
    if not names: continue
    out = []
    for he, lm, m in names:
        seats = sorted(set(seats_by_lemma[lm]), key=sk)
        outside = [s for s in seats if not (s[0] == 'Num' and s[1] == 33)]
        torah_out = [s for s in outside if s[0] in TORAH]
        out.append('%s(%s) seats %d; first outside 33: %s; Torah outside 33: %s%s' % (he, lm, len(seats), fmt(outside[0]) if outside else 'NONE', [fmt(s) for s in torah_out][:6], ' ...' if len(torah_out) > 6 else ''))
    print('  33:%-2d %s' % (v, ' | '.join(out)))
print('  the departure/camp verbs by verse (journeyed / camped present):')
print('   ', {v: ('J' if any(plain(he) == 'ויסעו' for he, _, _ in by[('Num', 33, v)]) else '-') + ('C' if any(plain(he) == 'ויחנו' for he, _, _ in by[('Num', 33, v)]) else '-') for v in range(1, 57)})
