#!/usr/bin/env python3
# THE NUMBERS WALK sitting 13b — THE COMPILE OF THE JOURNEYS, Numbers 33:1-56 (2026-09-12; the owner: "Go" after the #152 rereads): THE
# RECONNAISSANCE before the measurement pass (gad_compile_recon.py's form) — the callee modules' defs, asks, DATA keys and uppercase tables
# (so the measure's calls are typed from THIS print); the kinds and effects on file touching the itinerary's matter; the registry map for the
# chapter's tokens; the tape's station lines (the exodus story's 'journeyed' lines with their 'to' fields, beha's, chukat's, balak's) and the
# markers at the dated stations; the daemons' installed_by values (the reread item for the types step); the checkpoint prefixes in use.
import sys, io, re, contextlib, inspect, collections, yaml
ROOT = '<repo-old>'
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
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
MODS = [('exodus_story', ES), ('beha', BH), ('shelach', SL), ('chukat', CK), ('balak', BK), ('second_census', C2), ('zelophehad', ZL), ('gad_reuben', GR), ('tochacha', TC), ('holiness', HL), ('erection', ER), ('pesach', PS)]
for name, mod in MODS:
    src = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    defs = re.findall(r'^def ([a-z_0-9]+)\(', src, re.M)
    print('==== %s: %d defs %s' % (name, len(defs), defs))
    for d in defs:
        i = src.find('\ndef %s(' % d); j = src.find('\ndef ', i + 1)
        body = src[i:j if j > 0 else None]
        asks = sorted(set(re.findall(r"ask'?\]?\s*==\s*'([a-z_0-9]+)'", body)) | set(re.findall(r"q == '([a-z_0-9]+)'", body)))
        kinds = sorted(set(re.findall(r"k == '([a-z_0-9]+)'", body)))
        if asks or kinds:
            print('   %-28s asks %s%s' % (d, asks[:40], ('  kinds ' + str(kinds[:40])) if kinds else ''))
    if hasattr(mod, 'DATA'):
        print('   DATA keys (%d): %s' % (len(mod.DATA), sorted(mod.DATA)))
    ups = [n for n in dir(mod) if n.isupper() and not n.startswith('_') and n not in ('DATA', 'PROBES', 'CASES', 'GUARDED', 'HERE', 'ROOT')]
    print('   uppercase names: %s' % ups[:60])
    print('   imports: %s' % sorted(set(re.findall(r'^\s*import (cold_run_\w+)', src, re.M))))
    print('   span (registry): %s' % re.findall(r"SPAN\s*=\s*(\[[^\]]*\])", src)[:1])
    # the lines naming the chapter's matter
    for pat in ('12:12', 'judgment', 'Exod 12:37', '13:20', '14:2', '15:22', '15:27', '16:1', '17:1', '19:2', '11:34', '11:35', '12:16', '20:1 ', '20:22', '20:28', '21:1 ', '21:4', '21:10', '22:1 ', '25:1 ', '26:52', '26:55', '27:12', '32:34', '26:1 ', '26:30', '19:4', '32:4', 'high_place', 'figured', 'molten', 'by_lot', 'inhabitant', 'drive', 'dispossess', 'Num 33'):
        hits = [l.strip()[:150] for l in src.split('\n') if pat in l]
        if hits: print('   lines with %-10r: %d  e.g. %s' % (pat, len(hits), hits[:3]))

print('\n==== THE KINDS ON FILE touching the chapter\'s matter ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
print('  kinds %d, effects %d' % (len(E), len(F)))
for k in sorted(E):
    if re.search(r'journey|camp|encamp|station|wrote|writ|judg|gods|idol|image|molten|figured|high_place|drive|dispossess|possess|dwell|lot|thorn|inhabit|destroy|demolish|pillar|asher|command|spoke|land_division|arad|hor|aaron_died|died|departed|went_out|exodus|firstborn|plain|moab|jordan|sea|rameses|succoth|etham|elim|sin_|rephidim|sinai|kibroth|hazeroth|paran|kadesh|oboth|abarim|dibon|nebo', k):
        print('    %-44s form %-8s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:90].replace('\n', ' ')))
print('  effects touching the matter:')
for f in sorted(F):
    if re.search(r'journey|camp|encamp|station|wrote|writ|judg|gods|idol|image|molten|figured|high_place|drive|dispossess|possess|dwell|lot|thorn|inhabit|destroy|demolish|pillar|command|land|died|death|exodus|firstborn|departed|went_out|smitten|plague|curse|desolat|abhor|carcass|cut_off|divided|portion|inherit', f):
        print('    %-40s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:100].replace('\n', ' ')))
print('  the ledger_op values: %s' % dict(collections.Counter(F[f].get('ledger_op') for f in F)))
print('  a kind row whole (journeyed): %s' % E.get('journeyed'))
print('  a kind row whole (encamped_in_the_plains_of_moab): %s' % E.get('encamped_in_the_plains_of_moab'))
print('  an effect row whole (encamped_at): %s' % F.get('encamped_at'))

print('\n==== THE REGISTRY MAP for the chapter\'s tokens ====')
reg_map = CS.registry_map()
TOK = ('israel', 'israel_people', 'moses', 'aaron', 'eleazar', 'egypt', 'the-egyptians', 'pharaoh', 'the-lord', 'heaven', 'the-canaanite', 'the-king-of-arad', 'arad', 'edom', 'the-inhabitants-of-the-land', 'the-land', 'the-land-of-canaan', 'canaan', 'the-jordan', 'the-plains-of-moab', 'moab', 'the-gods-of-egypt', 'the-firstborn', 'the-firstborn-of-egypt', 'the-tribes', 'the-fathers', 'the-court', 'the-tent-of-meeting', 'the-congregation', 'joshua', 'caleb', 'the-sons-of-gad', 'the-sons-of-gad-and-reuben', 'the-sons-of-reuben', 'israel_tribes', 'the-twelve-spies', 'miriam', 'the-levites')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])
reg = yaml.safe_load(open(f'{ROOT}/logic/corpus/entity_registry.yaml', encoding='utf-8'))
print('  registry entities %d; ids matching egypt|pharaoh|canaan|arad|edom|inhabit|gods|heaven|lord|moab|jordan|land: %s' % (len(reg['entities']), [e['id'] for e in reg['entities'] if re.search(r'egypt|pharaoh|canaan|arad|edom|inhabit|gods|heaven|\blord|moab|jordan|land', e['id'])]))
print('  the registry rows\' shape (one row): %s' % reg['entities'][-1])
print('  the rows for heaven / the_lord / egypt / the_egyptians / the_gods_of_egypt if any: %s' % [e for e in reg['entities'] if e['id'] in ('heaven', 'the_lord', 'egypt', 'the_egyptians', 'the_gods_of_egypt', 'israel_people', 'the_king_of_arad', 'the_canaanite')])

print('\n==== THE TAPE\'S STATION LINES and the markers (from the sequence file\'s text) ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
for l in tape.split('\n'):
    if re.search(r"'kind': '(journeyed|encamped|paran_reached|journeyed_to_mount_hor|journeyed_by_the_red_sea_way|journeyed_oboth_to_arnon|encamped_in_the_plains_of_moab|calf_made|land_division_commanded|cities_built_east|arad_fought|garments_transferred|aaron_brought_up|miriam_died|firstborn|judgment|gods)", l) or re.search(r'# ---- Num 3', l) or 'w.marker(' in l and re.search(r"Exod (12|13|14|15|16|17|19):|Num (10|11|12|13|20|21|22|25):", l):
        print('   %s' % l.strip()[:230])
print('  DAEMON_ORDER %d, tail %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-4:]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s\n  SLOTS %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT, CS.SLOTS))
print('  cp() checkpoint prefixes in use: %s' % sorted(collections.Counter(re.findall(r"cp\('(C[A-Z])\d", src_cs)).items()))
print('  VERDICTS labels\' prefixes: %s' % sorted(collections.Counter(re.findall(r"\('(C[A-Z])\d'", src_cs)).items()))
print('  M[] marker names on file: %s' % re.findall(r"M\['([a-z_0-9]+)'\] = ", src_cs))
print('  the exodus marker line(s): %s' % [l.strip()[:230] for l in src_cs.split('\n') if "M['exodus']" in l and 'marker' in l][:3])
print('  the 12:12 / judgments lines in the sequence file: %s' % [l.strip()[:200] for l in src_cs.split('\n') if '12:12' in l or 'judgment' in l][:8])
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  daemons %d; installed_by values: %s' % (len(dd['daemons']), dict(collections.Counter(v.get('installed_by') for v in dd['daemons'].values()))))
print('  the walk\'s daemons (given_at, installed_by): %s' % {k: (v.get('given_at'), v.get('installed_by')) for k, v in dd['daemons'].items() if k in ('law_census', 'law_naso', 'law_beha', 'law_shelach', 'law_korach', 'law_chukat', 'law_balak', 'law_second_census', 'law_musafim', 'law_vows', 'law_midian', 'law_gad_reuben', 'law_zelophehad', 'law_pesach_sheni', 'law_mekoshesh', 'law_tochacha', 'law_holiness', 'law_exodus_story')})
print('  daemons whose installed_by is a VERSE (not boot / an act): %s' % {k: (v.get('given_at'), v.get('installed_by')) for k, v in dd['daemons'].items() if str(v.get('installed_by', '')).startswith(('Num', 'Exod', 'Lev', 'Gen', 'Deut'))})
print('  the full law_gad_reuben block: %s' % dd['daemons'].get('law_gad_reuben'))
print('  the full law_shelach block: %s' % dd['daemons'].get('law_shelach'))
print('  the functions block gad_reuben: %s' % {k: v for k, v in dd.get('functions', {}).items() if k == 'gad_reuben'})
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers at Num 33: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if str(p.get('verse', '')).startswith('Num 33')]))
print('  edges naming the callees as `to`: %s' % collections.Counter(e['to'] for e in dep['edges'] if e['to'] in ('exodus_story', 'beha', 'shelach', 'chukat', 'balak', 'second_census', 'zelophehad', 'gad_reuben', 'tochacha', 'holiness', 'erection', 'pesach')))
print('  the spans of the callees: %s' % {k: dep['spans'][k] for k in ('exodus_story', 'beha', 'shelach', 'chukat', 'balak', 'second_census', 'zelophehad', 'gad_reuben', 'tochacha', 'holiness', 'erection', 'pesach', 'midian') if k in dep['spans']})
print('  the gad_reuben edges on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], e.get('taught_by'), str(e.get('why', ''))[:60]) for e in dep['edges'] if e['from'] == 'gad_reuben'])
print('  an edge row\'s shape: %s' % dep['edges'][-1])
print('  a pointer row\'s shape: %s' % dep['pointers'][-1])
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
