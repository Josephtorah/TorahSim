#!/usr/bin/env python3
# THE NUMBERS WALK sitting 8b — THE COMPILE OF THE SECOND CENSUS (2026-09-11; the owner: "Ok go" on the one-sitting form with the population
# table built first): THE MEASUREMENTS, computed BEFORE the design paragraph is typed (1b's order). (1) the parser at the chapter's seats after
# 7b's rules — every numeral verse of 26 and the cross-check seats (1:20-46, 3:22-39, 25:9, 17:14, 16:35, Gen 46:15-27, Deut 2:14) — NO probe owed:
# the measurement is the proof; (2) the two censuses as tables from the ink — the twelve at both seats, the deltas, the sums, the Levites, the
# families per tribe with their gentilics, Genesis 46's names against 26's; (3) the calendar — the counter after Balak, the daughters' marker,
# the 25:19 half-verse; (4) the tape's subjects and the registry rows for the persons the chapter names; (5) the register of 26 against the
# planned lines; (6) the kinds and effects on file for the names the design will use; (7) the callees on file, live; (8) the engine's state for
# the population table — World has no table, the journal's classes, the views, the probes' counts.
import sqlite3, sys, io, re, contextlib, collections, inspect, os, unicodedata
ROOT = '<repo-old>'
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import world_engine as WE
    import world_journal as WJ
    import cold_run_bamidbar as BM
    import cold_run_balak as CB
    import cold_run_korach as KR
    import cold_run_shelach as SH
    import cold_run_zelophehad as ZL
    import cold_run_joseph as JO
    import cold_run_primeval as PV
    import cold_run_chukat as CK
    import cold_run_family as FM
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
db = sqlite3.connect(f'file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by = {}
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((plain(he), m))
def words(b, c, v): return [x for x, _ in by[(b, c, v)]]
NUMY = r'(אחד|אחת|שנים|שתים|שני|שתי|שלש|שלוש|ארבע|חמש|שש|שבע|שמנ|תשע|עשר|מאה|מאת|אלף|אלפ|מאתים|ראשון|שלישי|שביעי|רביעי|חמישי|ששי|שמיני|תשיעי)'

print('==== (1) THE PARSER AT THE CHAPTER\'S SEATS (26:1-65) after 7b\'s rules — every verse with a numeral token; no probe owed ====')
for v in range(1, 66):
    n, o = N('Num', 26, v), O('Num', 26, v)
    numy = [x for x in words('Num', 26, v) if re.search(NUMY, x)]
    if n or o or numy:
        print('  Num 26:%-3d numbers %-12s ordinals %-6s tokens %s' % (v, n, o, ' '.join(numy)))
print('-- the cross-check seats:')
for ref in (('Num', 1, 46), ('Num', 2, 32), ('Num', 3, 39), ('Num', 3, 22), ('Num', 3, 28), ('Num', 3, 34), ('Num', 25, 9), ('Num', 17, 14), ('Num', 16, 35), ('Num', 16, 2), ('Num', 14, 29), ('Deut', 2, 14), ('Gen', 46, 15), ('Gen', 46, 18), ('Gen', 46, 22), ('Gen', 46, 25), ('Gen', 46, 26), ('Gen', 46, 27), ('Exod', 1, 5), ('Num', 26, 51), ('Num', 26, 62), ('Num', 33, 54), ('Num', 35, 8), ('Josh', 17, 5)):
    print('  %s %d:%d  numbers %s  ordinals %s   tokens %s' % (ref[0], ref[1], ref[2], N(*ref) if ref[0] in ('Gen', 'Exod', 'Lev', 'Num', 'Deut') else '(outside the parser\'s books)', O(*ref) if ref[0] in ('Gen', 'Exod', 'Lev', 'Num', 'Deut') else '-', ' '.join(x for x in words(*ref) if re.search(NUMY, x))))

print('\n==== (2) THE TWO CENSUSES AS TABLES FROM THE INK ====')
TRIBES26 = [('reuben', 7), ('simeon', 14), ('gad', 18), ('judah', 22), ('issachar', 25), ('zebulun', 27), ('manasseh', 34), ('ephraim', 37), ('benjamin', 41), ('dan', 43), ('asher', 47), ('naphtali', 50)]
TRIBES1 = [('reuben', 21), ('simeon', 23), ('gad', 25), ('judah', 27), ('issachar', 29), ('zebulun', 31), ('ephraim', 33), ('manasseh', 35), ('benjamin', 37), ('dan', 39), ('asher', 41), ('naphtali', 43)]
C26 = {t: N('Num', 26, v)[0] for t, v in TRIBES26}; C1 = {t: N('Num', 1, v)[0] for t, v in TRIBES1}
T26, T1 = N('Num', 26, 51)[0], N('Num', 1, 46)[0]
print('  chapter 1  %s sum %d = 1:46 %d %s' % (C1, sum(C1.values()), T1, sum(C1.values()) == T1))
print('  chapter 26 %s sum %d = 26:51 %d %s' % (C26, sum(C26.values()), T26, sum(C26.values()) == T26))
DELTA = {t: C26[t] - C1[t] for t, _ in TRIBES26}
print('  deltas %s; fell %s (%d); rose %s (%d); whole %d' % (DELTA, [t for t in DELTA if DELTA[t] < 0], sum(v for v in DELTA.values() if v < 0), [t for t in DELTA if DELTA[t] > 0], sum(v for v in DELTA.values() if v > 0), T26 - T1))
print('  BM.TWELVE == chapter 1 here: %s; BM.TOTAL %d; the Levites 3:39 %d (BM.LEV_WRITTEN %d, the houses %s = %d) -> 26:62 %d: delta %d' % (BM.TWELVE == C1, BM.TOTAL, N('Num', 3, 39)[0], BM.LEV_WRITTEN, BM.HOUSES, sum(BM.HOUSES.values()), N('Num', 26, 62)[0], N('Num', 26, 62)[0] - BM.LEV_WRITTEN))
print('  the plague 25:9 %s (CB.COUNT %s); Simeon\'s fall %d; the remainder beyond the plague %d; Korach\'s plague 17:14 %s (KR.PLAGUE %s), the 250 (16:35) %s; the total\'s fall %d against the plague + 14,700 + 250 = %d' % (N('Num', 25, 9), CB.COUNT, DELTA['simeon'], -DELTA['simeon'] - CB.COUNT[0], N('Num', 17, 14), getattr(KR, 'PLAGUE', None), N('Num', 16, 35), T1 - T26, CB.COUNT[0] + N('Num', 17, 14)[0] + N('Num', 16, 35)[0]))
# the families per tribe: 'family of' + the next token (the gentilic) inside each tribe's span; the family NAME the token before 'the family of' form
TSPAN = {'reuben': (5, 6), 'simeon': (12, 13), 'gad': (15, 17), 'judah': (19, 21), 'issachar': (23, 24), 'zebulun': (26, 26), 'manasseh': (29, 33), 'ephraim': (35, 36), 'benjamin': (38, 40), 'dan': (42, 43), 'asher': (44, 46), 'naphtali': (48, 49), 'levi': (57, 58)}
FAM = {}
for t, (lo, hi) in TSPAN.items():
    out = []
    for v in range(lo, hi + 1):
        ws = words('Num', 26, v)
        for i, x in enumerate(ws):
            if x == 'משפחת' and i + 1 < len(ws):
                g = ws[i + 1]
                if g.startswith('ה') and g.endswith('י') and g not in ('הראובני', 'השמעני', 'הזבולני'):
                    # the family name: the token before the preposition 'of' form לX that precedes 'the family of' (e.g. לחנך משפחת החנכי)
                    name = ws[i - 1] if i >= 1 else None
                    out.append((v, name, g))
    FAM[t] = out
NFAM = {t: len(FAM[t]) for t in FAM}
print('  families per tribe %s; the twelve %d + Levi %d' % (NFAM, sum(NFAM[t] for t in NFAM if t != 'levi'), NFAM['levi']))
for t in FAM: print('    %-9s %s' % (t, ' '.join('%s>%s@%d' % (n, g, v) for v, n, g in FAM[t])))
print('  Levi\'s houses at chapter 3 (3:17-20): %s' % ' '.join(x for v in (17, 18, 19, 20) for x in words('Num', 3, v)))
print('  chapter 1 "family of" tokens: %d; chapter 26: %d' % (sum(1 for v in range(1, 55) for x in words('Num', 1, v) if x == 'משפחת'), sum(1 for v in range(1, 66) for x in words('Num', 26, v) if x == 'משפחת')))
G46 = {t: [x for x in ws] for t, ws in (('reuben', words('Gen', 46, 9)[3:]), ('simeon', words('Gen', 46, 10)[2:]), ('levi', words('Gen', 46, 11)[2:]), ('judah', words('Gen', 46, 12)), ('issachar', words('Gen', 46, 13)[2:]), ('zebulun', words('Gen', 46, 14)[2:]), ('gad', words('Gen', 46, 16)[2:]), ('asher', words('Gen', 46, 17)), ('benjamin', words('Gen', 46, 21)[2:]), ('dan', words('Gen', 46, 23)[2:]), ('naphtali', words('Gen', 46, 24)[2:]))}
for t in G46: print('    Gen 46 %-9s %s' % (t, ' '.join(G46[t])))
print('  JO.ROSTERS registers: %s; the seventy cells: jochebed -> %s; diverge -> %s; leah_living_named -> %s' % ({k: len(v) for k, v in JO.ROSTERS.items()}, JO.seventy('jochebed')['v'], JO.seventy('diverge')['v'], JO.seventy('leah_living_named')['v']))

print('\n==== (3) THE CALENDAR — the counter after Balak, the daughters\' marker, the half-verse ====')
w = WE.World(era='measure', epoch='exodus')
for y, m, d, why in ((40, 6, 1, "the counter after Balak's lines (21:4's marker) = the daughters' marker (27:1)"), (40, 5, 15, 'the fifteenth of Av — the dying ceased (Bava Batra 121a:9; shelach DATA deaths_ceased)'), (40, 5, 9, "CF3's fire — the thirty-eight years"), (40, 11, 1, 'Deut 1:3')):
    print('  (%d, %d, %d) = day %d  %s' % (y, m, d, w.clock.day_in('exodus', y, m, d), why))
print('  25:19 words: %s (numbers %s) — the half-verse; 26:1 words[:8]: %s' % (' '.join(words('Num', 25, 19)), N('Num', 25, 19), ' '.join(words('Num', 26, 1)[:8])))
src = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
for ln in src.split('\n'):
    if "w.marker('Num 27:1'" in ln: print('    27:1 marker:', ln.strip()[:160])
    if ('Num 26' in ln or 'Num 25:19' in ln) and ('w.submit' in ln or 'w.marker' in ln): print('  A LINE AT 26 ALREADY:', ln.strip()[:200])
print('  SH.DATA deaths_ceased = %s; SH decree(due) -> %s' % (SH.DATA['deaths_ceased']['value'], SH.decree({'ask': 'due'}, SH.DATA)[0]))

print('\n==== (4) THE TAPE\'S SUBJECTS AND THE REGISTRY ROWS ====')
for s in ('israel', 'moses', 'eleazar', 'the-levites', 'the-daughters-of-zelophehad', 'zelophehad', 'joshua', 'caleb', 'korach', 'dathan', 'abiram', 'miriam', 'amram', 'jochebed', 'serah', 'er', 'onan', 'nadab', 'abihu', 'machir', 'gilead', 'hepher', 'the-court', 'the-tabernacle', 'the-firstborn-of-israel', 'reuben', 'simeon', 'the-tribe-of-simeon'):
    print('  %-30s subject lines %2d   as a token %3d' % (s, src.count("'subject': '%s'" % s), src.count("'%s'" % s)))
import yaml
reg = yaml.safe_load(open(f'{ROOT}/logic/corpus/entity_registry.yaml', encoding='utf-8'))
ids = {e['id']: e for e in reg['entities']}
tok = {m.get('token'): e['id'] for e in reg['entities'] for m in e.get('members', []) if 'step9-scenes' in (m.get('units') or [])}
for eid in ('israel_people', 'moses', 'eleazar_son_of_aaron', 'the_levites', 'the_daughters_of_zelophehad', 'zelophehad', 'yehoshua', 'caleb', 'korach', 'dathan', 'abiram', 'miriam', 'amram', 'jochebed', 'serah', 'er', 'onan', 'nadab', 'abihu', 'machir', 'gilead', 'hepher', 'the_court', 'the_tent_of_meeting', 'reuben', 'simeon', 'levi', 'judah', 'joseph', 'ephraim', 'manasseh', 'dan', 'benjamin', 'gad', 'asher', 'naphtali', 'issachar', 'zebulun', 'aaron', 'the_firstborn_of_israel'):
    e = ids.get(eid)
    print('  %-28s %s' % (eid, ('kind %s; members %s' % (e.get('kind'), [m.get('token') for m in e.get('members', [])])) if e else 'NO ROW'))
print('  scene tokens -> ids for the chapter\'s names:', {t: tok.get(t) for t in ('joshua', 'caleb', 'korach', 'dathan', 'abiram', 'miriam', 'amram', 'eleazar', 'zelophehad', 'the-daughters-of-zelophehad', 'the-levites', 'israel', 'moses', 'aaron', 'reuben', 'simeon')})

print('\n==== (5) THE REGISTER OF CHAPTER 26 (V.w) against the planned lines ====')
reg2 = {v: [x for x, m in by[('Num', 26, v)] if m and re.search(r'(^|/)V[A-Za-z]w', m)] for v in range(1, 66)}
regv = [v for v in range(1, 66) if reg2[v]]
print('  register verses %d: %s' % (len(regv), ' '.join('%d:%s' % (v, ','.join(reg2[v])) for v in regv)))
LINES = [('second_census_commanded', 26, 1, 4), ('second_census_taken', 26, 5, 51), ('land_division_commanded', 26, 52, 56), ('levites_counted_second', 26, 57, 62), ('rolls_compared', 26, 63, 65)]
for name, c, lo, hi in LINES:
    vv = [(v, reg2[v]) for v in range(lo, hi + 1) if reg2[v]]
    print('  %-28s %d:%d-%d  register verses %d  %s' % (name, c, lo, hi, len(vv), ' '.join('%d:%s' % (v, ','.join(x)) for v, x in vv)[:200]))
FR = [v for v in range(1, 66) if len(words('Num', 26, v)) > 2 and words('Num', 26, v)[0] in ('וידבר', 'ויאמר') and words('Num', 26, v)[1] == 'יהוה']
print('  the frames:', FR, '; 26:3 head:', ' '.join(words('Num', 26, 3)[:6]))

print('\n==== (6) THE KINDS AND EFFECTS ON FILE — the names the design will use ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
cand_kinds = [n for n, *_ in LINES] + ['census_case', 'population_case', 'census_taken', 'levites_counted', 'census_commanded', 'levite_count_commanded', 'decree_declared', 'daughters_approached', 'plague_dead_counted']
print('  kinds on file among the candidates:', [k for k in cand_kinds if k in E])
print('  kinds NOT on file:', [k for k in cand_kinds if k not in E])
cand_fx = ['commanded', 'counted', 'exempt', 'holding_owed', 'land_apportioned', 'apportioned', 'inherits', 'inheritance_owed', 'land_divided', 'lot_cast', 'lot_owed', 'portion_added', 'sentence_pronounced', 'carcasses_fall_in_the_wilderness', 'exit_owed', 'out_of_the_ark', 'souls_counted', 'accepted', 'declaration_owed', 'rule_installed', 'in_force', 'land_release', 'land_possessed', 'holding_granted', 'excluded', 'included', 'named', 'registered', 'died_in_the_wilderness', 'died', 'dead', 'death_decreed', 'membership']
print('  effects on file among the candidates:', [f for f in cand_fx if f in F])
print('  effects NOT on file:', [f for f in cand_fx if f not in F])
for f in sorted(F):
    if re.search(r'land|lot|inherit|count|census|apportion|divid|roll|portion|holding|souls|exempt$|commanded$|died|death|carcass|sentence', f):
        print('   %-32s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:120].replace('\n', ' ')))
print('  kinds on file matching count/census/land/lot/inherit/levite/daughters/roll:')
for k in sorted(E):
    if re.search(r'count|census|land|lot\b|inherit|levite|daughters|roll|apportion|divid', k):
        print('    %-36s form %-7s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:100].replace('\n', ' ')))

print('\n==== (7) THE CALLEES ON FILE, live ====')
def tryc(label, f):
    try:
        r = f(); print('  ', label, '->', (r['v'] if isinstance(r, dict) and 'v' in r else (r[0] if isinstance(r, tuple) else r)) if not isinstance(r, str) else r)
    except Exception as e:
        print('  ', label, 'raised', type(e).__name__, str(e)[:200])
tryc('BM.census(total)', lambda: BM.census({'ask': 'total'}, BM.DATA))
tryc('BM.levites(delta)', lambda: BM.levites({'ask': 'delta'}, BM.DATA))
tryc('BM.census(lineage)', lambda: BM.census({'ask': 'lineage'}, BM.DATA))
tryc('CB.COUNT', lambda: CB.COUNT)
tryc('CB DATA keys', lambda: sorted(CB.DATA)[:40])
tryc('KR.plague_and_staffs(plague_count)', lambda: KR.plague_and_staffs({'ask': 'plague_count'}, KR.DATA))
tryc('KR.rebellion(two_hundred_fifty)', lambda: KR.rebellion({'ask': 'two_hundred_fifty'}, KR.DATA))
tryc('KR DATA keys', lambda: sorted(KR.DATA))
tryc('SH.decree(set)', lambda: SH.decree({'ask': 'set'}, SH.DATA))
tryc('SH.decree(exceptions)', lambda: SH.decree({'ask': 'exceptions'}, SH.DATA))
tryc('SH.decree(deaths_ceased)', lambda: SH.decree({'ask': 'deaths_ceased'}, SH.DATA))
tryc('ZL.the_daughters(plea)', lambda: ZL.the_daughters({'ask': 'plea'}, ZL.DATA))
tryc('ZL.the_daughters(names_order)', lambda: ZL.the_daughters({'ask': 'names_order'}, ZL.DATA))
tryc('ZL.NO_SON_SEATS', lambda: ZL.NO_SON_SEATS)
tryc('ZL.heir_of(daughter only)', lambda: ZL.heir_of({'daughter': True, 'son': False, 'sons_line': False, 'brothers': True}))
tryc('ZL DATA keys', lambda: sorted(ZL.DATA))
tryc('JO.seventy(names_by_register)', lambda: JO.seventy('names_by_register'))
tryc('JO.seventy(subtotals_parsed)', lambda: JO.seventy('subtotals_parsed'))
tryc('PV.exit(by_families)', lambda: PV.exit('by_families'))
tryc('CK.edom_and_hor(succession)', lambda: CK.edom_and_hor({'ask': 'succession'}, CK.DATA))
tryc('CK DATA succession_by', lambda: CK.DATA['succession_by']['value'])
tryc('FM.levirate(name_is_inheritance)', lambda: FM.levirate('name_is_inheritance'))
tryc('FM.testament(adopted 48:6)', lambda: [n for n in dir(FM) if not n.startswith('_')][:60])
def defs(mod):
    s = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    return re.findall(r'^def ([a-z_0-9]+)\(', s, re.M)
for name, mod in (('bamidbar', BM), ('balak', CB), ('korach', KR), ('shelach', SH), ('zelophehad', ZL), ('joseph', JO), ('primeval', PV), ('chukat', CK), ('family', FM)):
    print('  %-11s defs %s' % (name, defs(mod)[:30]))
# the import closure: none of the callees may import the new runner (it does not exist yet — the check is that none names it)
for name, mod in (('bamidbar', BM), ('balak', CB), ('korach', KR), ('shelach', SH), ('zelophehad', ZL), ('joseph', JO), ('primeval', PV), ('chukat', CK), ('family', FM)):
    s = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    print('  %-11s imports %s' % (name, sorted(set(re.findall(r'^import (cold_run_\w+)', s, re.M)))))

print('\n==== (8) THE ENGINE\'S STATE FOR THE POPULATION TABLE ====')
print('  World attributes: %s' % [a for a in vars(WE.World(era='x', epoch='exodus')) if not a.startswith('__')])
print('  World has a table? %s; a row method? %s' % (hasattr(WE.World, 'tables'), hasattr(WE.World, 'row')))
print('  the journal\'s classes (KINDS): %s' % dict(WJ.KINDS))
print('  the views: %s' % re.findall(r'CREATE VIEW (\w+)', open(f'{ROOT}/World/journal/run_views.sql', encoding='utf-8').read()))
print('  the ask questions: %s' % re.findall(r"question == '(\w+)'", open(f'{ROOT}/World/step9/world_journal.py', encoding='utf-8').read()))
print('  journal_probes J3 expects: %s' % re.findall(r'len\(kinds\) == (\d+)', open(f'{ROOT}/World/step9/journal_probes.py', encoding='utf-8').read()))
print('  installation_probes I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
print('  event_kinds.yaml run.* kinds: %s' % re.findall(r'- id: (run\.\w+)', open(f'{ROOT}/World/journal/registers/event_kinds.yaml', encoding='utf-8').read()))
print('  DAEMON_ORDER length %d, last %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-1]))
print('  RUN %s; PREVIOUS_RUN %s; NEWEST_RUNNER %s; CENSUS %s; PLACEMENT %s; SLOTS %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT, CS.SLOTS))
print('  registry entities %d' % len(reg['entities']))
