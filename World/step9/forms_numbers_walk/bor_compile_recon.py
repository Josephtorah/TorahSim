#!/usr/bin/env python3
# THE NUMBERS WALK sitting 14b — THE COMPILE OF THE BORDERS, Numbers 34:1-29 (2026-09-13; the owner: "Go" after the #155 rereads): THE
# RECONNAISSANCE before the measurement pass (jou_compile_recon.py's form) — the callee modules' defs, asks, DATA keys and uppercase tables
# (so the measure's calls are typed from THIS print); the kinds and effects on file touching the borders' matter; the registry map for the
# chapter's tokens (the dividers of the land — 12b's row; the princes; the tribes); the tape's lines naming the land, the lot, the grant, the
# commission (32:28) and the markers; the daemons' installed_by values; the dependency forms (the VIA row whole); the checkpoint prefixes in use
# (grepped BEFORE naming — 12b's lesson); the register gate's Num 34 seat.
import sys, io, re, contextlib, inspect, collections, yaml, glob
ROOT = '<repo-old>'
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
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
MODS = [('second_census', C2), ('gad_reuben', GR), ('shelach', SL), ('chukat', CK), ('bamidbar', CB), ('naso', NS), ('korach', KR), ('zelophehad', ZL), ('journeys', JO), ('erection', ER), ('balak', BK)]
PATS = ('34:', 'border', 'by_lot', "'lot", 'nine', 'half', 'aleb', 'leazar', 'oshua', 'prince', 'nasi', 'Hor', 'two_mount_hors', 'Kadesh', 'Zin', 'Salt', 'Chinnereth', 'Jordan', 'Josh 13', 'Josh 14', 'Josh 15', 'Josh 18', 'Josh 19', 'Josh 21', 'Josh 22', 'Ezek 47', 'Ammihud', 'the_land', 'land_possessed', 'holding_given', 'dividers', 'divide', 'inherit', 'Canaan', '1:5', '1:10', '7:11', '17:21', '13:2', '13:6', '13:21', '27:18', '27:19', '27:22', '26:52', '26:55', '32:28', '32:33', '33:54', '27:9', '27:13', '5:23', '14:3', '15:18', 'great sea', 'west', 'north', 'south', 'east', 'court', 'shoulder', 'side')
for name, mod in MODS:
    src = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    defs = re.findall(r'^def ([a-z_0-9]+)\(', src, re.M)
    print('==== %s: %d defs %s' % (name, len(defs), defs))
    for d in defs:
        i = src.find('\ndef %s(' % d); j = src.find('\ndef ', i + 1)
        body = src[i:j if j > 0 else None]
        asks = sorted(set(re.findall(r"ask'?\]?\s*==\s*'([a-z_0-9]+)'", body)) | set(re.findall(r"q == '([a-z_0-9]+)'", body)) | set(re.findall(r"ask'?\]?\s*in\s*\(([^)]*)\)", body)))
        kinds = sorted(set(re.findall(r"k == '([a-z_0-9]+)'", body)))
        if asks or kinds:
            print('   %-28s asks %s%s' % (d, asks[:60], ('  kinds ' + str(kinds[:40])) if kinds else ''))
    if hasattr(mod, 'DATA'):
        print('   DATA keys (%d): %s' % (len(mod.DATA), sorted(mod.DATA)))
    ups = [n for n in dir(mod) if n.isupper() and not n.startswith('_') and n not in ('DATA', 'PROBES', 'CASES', 'GUARDED', 'HERE', 'ROOT')]
    print('   uppercase names: %s' % ups[:80])
    print('   imports: %s' % sorted(set(re.findall(r'^\s*import (cold_run_\w+)', src, re.M))))
    for pat in PATS:
        hits = [l.strip()[:170] for l in src.split('\n') if pat in l]
        if hits: print('   lines with %-14r: %d  e.g. %s' % (pat, len(hits), hits[:3]))

print('\n==== THE KINDS ON FILE touching the chapter\'s matter ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
print('  kinds %d, effects %d' % (len(E), len(F)))
for k in sorted(E):
    if re.search(r'border|bound|lot|divid|inherit|possess|land_|commission|prince|nasi|named|roster|appoint|command|spoke|granted|holding|tribe|caleb|joshua|eleazar|spies|rods|dedication|census|court|dispossess|conquest|hor|kadesh|edom|sea|jordan|canaan', k):
        print('    %-44s form %-8s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:100].replace('\n', ' ')))
print('  effects touching the matter:')
for f in sorted(F):
    if re.search(r'border|bound|lot|divid|inherit|possess|land|commission|prince|appoint|command|granted|holding|tribe|charged|charge|named|roster|spies|dedicat|census|court|dispossess|conquest|entitle', f):
        print('    %-40s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:110].replace('\n', ' ')))
print('  the ledger_op values: %s' % dict(collections.Counter(F[f].get('ledger_op') for f in F)))
for k in ('commission_charged', 'land_granted_east', 'land_division_commanded', 'dispossession_commanded', 'journeys_written', 'spies_sent', 'rods_gathered'):
    print('  a kind row whole (%s): %s' % (k, E.get(k)))
for f in ('commanded', 'holding_given', 'land_possessed', 'charged', 'journeys_recorded', 'commissioned'):
    print('  an effect row whole (%s): %s' % (f, F.get(f)))

print('\n==== THE REGISTRY MAP for the chapter\'s tokens ====')
reg_map = CS.registry_map()
TOK = ('israel', 'israel_people', 'moses', 'eleazar', 'joshua', 'caleb', 'the-dividers-of-the-land', 'the-princes-of-israel', 'the-sons-of-gad', 'the-sons-of-reuben', 'the-half-tribe-of-manasseh', 'the-sons-of-gad-and-reuben', 'the-land', 'the-land-of-canaan', 'canaan', 'edom', 'the-jordan', 'the-sea', 'the-great-sea', 'the-salt-sea', 'the-tribes', 'israel_tribes', 'the-tribe-of-judah', 'judah', 'simeon', 'benjamin', 'dan', 'manasseh', 'ephraim', 'zebulun', 'issachar', 'asher', 'naphtali', 'the-twelve-spies', 'the-heads-of-gilead', 'the-daughters-of-zelophehad', 'the-lord', 'heaven', 'the-nine-tribes', 'the-nine-and-a-half-tribes', 'the-two-and-a-half-tribes', 'the-inhabitants-of-the-land')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])
reg = yaml.safe_load(open(f'{ROOT}/logic/corpus/entity_registry.yaml', encoding='utf-8'))
print('  registry entities %d; ids matching divid|prince|judah|simeon|benjamin|\\bdan\\b|manasseh|ephraim|zebulun|issachar|asher|naphtali|joshua|caleb|eleazar|hor|canaan|edom|sea|jordan|land|tribe: %s' % (len(reg['entities']), [e['id'] for e in reg['entities'] if re.search(r'divid|prince|judah|simeon|benjamin|\bdan\b|manasseh|ephraim|zebulun|issachar|asher|naphtali|joshua|caleb|eleazar|\bhor\b|canaan|edom|\bsea|jordan|land|tribe', e['id'])]))
print('  the rows for the dividers / joshua / caleb / eleazar / the tribes of the east / the land of canaan: %s' % [e for e in reg['entities'] if e['id'] in ('the_dividers_of_the_land', 'joshua', 'caleb', 'eleazar_son_of_aaron', 'the_sons_of_gad', 'the_sons_of_reuben', 'the_half_tribe_of_manasseh', 'the_land_of_canaan', 'the_princes_of_israel', 'the_twelve_spies')])
print('  the registry rows\' shape (the last row): %s' % reg['entities'][-1])

print('\n==== THE TAPE\'S LINES naming the land / the lot / the grant / the commission, and the markers ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
for l in tape.split('\n'):
    if re.search(r"the-dividers-of-the-land|by_lot|land_division|'lot'|land_granted|holding|commission|spies_sent|rods|dedication_|princes_|census_|Num 1:|Num 13:|Num 17:|Num 27:|Num 26:5|Num 32:2|Num 32:3|Num 33:5", l) or re.search(r'# ---- Num 3', l) or ('w.marker(' in l and re.search(r"Num (1|7|13|20|21|27|33):", l)):
        print('   %s' % l.strip()[:260])
print('  DAEMON_ORDER %d, tail %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-4:]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s\n  SLOTS %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT, CS.SLOTS))
print('  cp() checkpoint prefixes in use: %s' % sorted(collections.Counter(re.findall(r"cp\('(C[A-Z])\d", src_cs)).items()))
print('  VERDICTS labels\' prefixes: %s' % sorted(collections.Counter(re.findall(r"'(C[A-Z])\d [A-Z]+'", src_cs)).items()))
used = set(re.findall(r"cp\('(C[A-Z])\d", src_cs)) | set(re.findall(r"'(C[A-Z])\d [A-Z]+'", src_cs))
free = [c for c in ['C' + x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'] if c not in used]
print('  FREE prefixes: %s' % free)
for cand in free[:8]:
    hits = []
    for f in glob.glob(f'{ROOT}/World/step9/*.py'):
        t = open(f, encoding='utf-8').read()
        n = len(re.findall(r"\b%s\d\b" % cand, t))
        if n: hits.append((f.split('/')[-1], n))
    print('    %s used as a label elsewhere: %s' % (cand, hits))
print('  M[] marker names on file (tail): %s' % re.findall(r"M\['([a-z_0-9]+)'\] = ", src_cs)[-12:])
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  daemons %d; installed_by values: %s' % (len(dd['daemons']), dict(collections.Counter(v.get('installed_by') for v in dd['daemons'].values()))))
print('  the walk\'s daemons (given_at, installed_by): %s' % {k: (v.get('given_at'), v.get('installed_by')) for k, v in dd['daemons'].items() if k in ('law_census', 'law_naso', 'law_shelach', 'law_korach', 'law_chukat', 'law_balak', 'law_second_census', 'law_musafim', 'law_vows', 'law_midian', 'law_gad_reuben', 'law_journeys', 'law_zelophehad')})
print('  the full law_journeys block: %s' % dd['daemons'].get('law_journeys'))
print('  the full law_gad_reuben block: %s' % dd['daemons'].get('law_gad_reuben'))
print('  the functions block journeys: %s' % {k: v for k, v in dd.get('functions', {}).items() if k == 'journeys'})
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers at Num 34: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if str(p.get('verse', '')).startswith('Num 34')]))
print('  edges naming the callees as `to`: %s' % collections.Counter(e['to'] for e in dep['edges'] if e['to'] in ('second_census', 'gad_reuben', 'shelach', 'chukat', 'bamidbar', 'naso', 'korach', 'zelophehad', 'journeys', 'erection', 'balak', 'family', 'sanctions')))
print('  the spans of the callees: %s' % {k: dep['spans'][k] for k in ('second_census', 'gad_reuben', 'shelach', 'chukat', 'bamidbar', 'naso', 'korach', 'zelophehad', 'journeys', 'erection', 'balak', 'family') if k in dep['spans']})
print('  the journeys edges on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], e.get('via'), str(e.get('why', ''))[:70]) for e in dep['edges'] if e['from'] == 'journeys'])
print('  the gad_reuben edges on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], e.get('via'), str(e.get('why', ''))[:70]) for e in dep['edges'] if e['from'] == 'gad_reuben'])
print('  a VIA edge row WHOLE (the form to copy): %s' % [e for e in dep['edges'] if e.get('disposition') == 'VIA' and e['from'] == 'journeys'][:1])
print('  a FALSE edge row WHOLE: %s' % [e for e in dep['edges'] if e.get('disposition') == 'FALSE' and e['from'] in ('journeys', 'gad_reuben')][:1])
print('  a pointer row\'s shape (INTERNAL, journeys): %s' % [p for p in dep['pointers'] if p.get('span') == 'journeys' or 'Num 33' in str(p.get('verse', ''))][:2])
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the register seats naming Num 34 / Num 36 (section, key, class, why): %s' % [(sec, k, v.get('class'), str(v.get('why', ''))[:120]) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if 'Num 34' in k or 'Num 36' in k])
print('  declared counts %d receipts %d footers %d registers %d' % tuple(len(decl.get(s, {})) for s in ('counts', 'receipts', 'footers', 'registers')))
