import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 12b — THE COMPILE OF GAD AND REUBEN, Numbers 32:1-42 (2026-09-12; the owner: "Go"): THE RECONNAISSANCE
# before the measurement pass — the callee modules' defs, their asks, their DATA keys and their uppercase tables (so the measure's calls
# are typed from THIS print, never guessed); the kinds and effects on file whose names touch the chapter's matter; the registry map for
# the chapter's tokens; the zelophehad runner's plea kinds (36:1-4's line is the tape's neighbour).
import sys, io, re, contextlib, inspect, collections, yaml
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import cold_run_vows as VW
    import cold_run_shelach as SL
    import cold_run_chukat as CK
    import cold_run_second_census as C2
    import cold_run_zelophehad as ZL
    import cold_run_balak as BK
    import cold_run_bamidbar as BM
    import cold_run_incense_shekel as IS
MODS = [('vows', VW), ('shelach', SL), ('chukat', CK), ('second_census', C2), ('zelophehad', ZL), ('balak', BK), ('bamidbar', BM), ('incense_shekel', IS)]
for name, mod in MODS:
    src = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    defs = re.findall(r'^def ([a-z_0-9]+)\(', src, re.M)
    print('==== %s: %d defs %s' % (name, len(defs), defs))
    # the asks per cell
    for d in defs:
        i = src.find('\ndef %s(' % d); j = src.find('\ndef ', i + 1)
        body = src[i:j if j > 0 else None]
        asks = sorted(set(re.findall(r"ask'?\]?\s*==\s*'([a-z_0-9]+)'", body)) | set(re.findall(r"ask\s+in\s+\(([^)]*)\)", body)))
        kinds = sorted(set(re.findall(r"k == '([a-z_0-9]+)'", body)))
        if asks or kinds:
            print('   %-28s asks %s%s' % (d, asks[:40], ('  kinds ' + str(kinds[:30])) if kinds else ''))
    if hasattr(mod, 'DATA'):
        print('   DATA keys (%d): %s' % (len(mod.DATA), sorted(mod.DATA)))
    ups = [n for n in dir(mod) if n.isupper() and not n.startswith('_') and n not in ('DATA', 'PROBES', 'CASES', 'GUARDED', 'HERE', 'ROOT')]
    print('   uppercase names: %s' % ups[:40])
    print('   imports: %s' % sorted(set(re.findall(r'^\s*import (cold_run_\w+)', src, re.M))))
    print('   span (registry): %s' % re.findall(r"SPAN\s*=\s*(\[[^\]]*\])", src)[:1])

print('\n==== THE KINDS ON FILE touching the chapter\'s matter ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
print('  kinds %d, effects %d' % (len(E), len(F)))
for k in sorted(E):
    if re.search(r'land|possess|inherit|cit(y|ies)|built|oath|swor|condition|stipul|cross|jordan|gilead|request|plea|grant|lot_|portion|war|arm|tribe|command|relay|rebuke|wander|forty|spies|sihon|og_|amorite|conquer|smote|took_|renam|name', k):
        print('    %-40s form %-8s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:90].replace('\n', ' ')))
print('  effects touching the matter:')
for f in sorted(F):
    if re.search(r'land|possess|inherit|cit|built|oath|swor|condition|stipul|cross|jordan|grant|lot|portion|war|arm|command|wander|forty|conquer|smote|took|renam|name|clear|sin|find|sat|rest|dwel|entitle|promise|transfer|given|hold', f):
        print('    %-34s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:100].replace('\n', ' ')))
print('  the ledger_op values: %s' % dict(collections.Counter(F[f].get('ledger_op') for f in F)))

print('\n==== THE REGISTRY MAP for the chapter\'s tokens ====')
reg_map = CS.registry_map()
TOK = ('israel', 'israel_people', 'moses', 'eleazar', 'joshua', 'caleb', 'aaron', 'gad', 'reuben', 'manasseh', 'the-sons-of-gad', 'the-sons-of-reuben', 'the-tribe-of-gad', 'the-tribe-of-reuben',
       'the-half-tribe-of-manasseh', 'half-manasseh', 'machir', 'jair', 'nobah', 'sihon', 'og', 'the-amorites', 'the-heads-of-the-fathers', 'the-princes', 'the-princes-of-the-congregation',
       'the-congregation', 'the-land', 'the-land-of-canaan', 'canaan', 'the-land-of-gilead', 'gilead', 'jazer', 'the-jordan', 'heaven', 'the-lord', 'the-tent-of-meeting', 'the-court',
       'the-generation', 'the-doomed-generation', 'the-men-of-war', 'the-spies', 'abraham', 'isaac', 'jacob', 'joseph', 'the-kenizzite', 'hezron', 'the-daughters-of-zelophehad', 'zelophehad', 'the-levites', 'the-little-ones', 'the-cattle')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])
reg = yaml.safe_load(open(f'{ROOT}/logic/corpus/entity_registry.yaml', encoding='utf-8'))
print('  registry entities %d; ids matching gad|reuben|manasseh|machir|jair|nobah|sihon|og|joshua|caleb|amorite|gilead|jazer|hezron: %s' % (len(reg['entities']), [e['id'] for e in reg['entities'] if re.search(r'gad|reuben|manasseh|machir|jair|nobah|sihon|\bog\b|joshua|caleb|amorite|gilead|jazer|hezron|kenaz', e['id'])]))
print('  the registry rows\' shape (one row): %s' % reg['entities'][-1])
print('  a tribe row if any: %s' % [e for e in reg['entities'] if e['id'] in ('gad', 'reuben', 'the_tribe_of_gad', 'the_sons_of_gad', 'manasseh')][:3])

print('\n==== THE ZELOPHEHAD RUNNER\'S TAPE KINDS (36:1-4 the neighbour line) and the tape\'s Num 30/31/36 lines ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
for l in tape.split('\n'):
    if re.search(r'Num (30|31|36):|# ---- Num 3', l): print('   %s' % l[:170])
print('  DAEMON_ORDER %d, tail %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-4:]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s\n  SLOTS %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT, CS.SLOTS))
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  daemons %d; installed_by values: %s' % (len(dd['daemons']), dict(collections.Counter(v.get('installed_by') for v in dd['daemons'].values()))))
print('  law_vows / law_midian / law_zelophehad / law_shelach / law_chukat blocks (given_at, installed_by, the comment head): %s' % {k: (v.get('given_at'), v.get('installed_by'), str(v.get('comment', v.get('note', '')))[:160]) for k, v in dd['daemons'].items() if k in ('law_vows', 'law_midian', 'law_zelophehad', 'law_shelach', 'law_chukat')})
print('  the full law_vows block: %s' % dd['daemons'].get('law_vows'))
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers at Num 32: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if str(p.get('verse', '')).startswith('Num 32')]))
print('  edges naming the callees as `to`: %s' % collections.Counter(e['to'] for e in dep['edges'] if e['to'] in ('vows', 'shelach', 'chukat', 'second_census', 'zelophehad', 'balak', 'bamidbar', 'incense_shekel')))
print('  the spans of the callees: %s' % {k: dep['spans'][k] for k in ('vows', 'shelach', 'chukat', 'second_census', 'zelophehad', 'balak', 'bamidbar', 'midian') if k in dep['spans']})
print('  an edge row\'s shape: %s' % dep['edges'][-1])
print('  a pointer row\'s shape: %s' % dep['pointers'][-1])
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
