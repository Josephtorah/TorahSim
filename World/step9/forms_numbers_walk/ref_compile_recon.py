#!/usr/bin/env python3
# THE NUMBERS WALK sitting 15b — THE COMPILE OF THE REFUGE CITIES, Numbers 35:1-34 (2026-09-13; the owner: "Go" after the #158 rereads): THE
# RECONNAISSANCE before the measurement pass (bor_compile_recon.py's form) — the callee modules' defs, asks, DATA keys and uppercase tables
# (so the measure's calls are typed from THIS print); the kinds and effects on file touching the refuge law's matter (the killer, the blood, the
# flight, the refuge, the exile, the avenger, the witnesses, the ransom, the death, the priest, the city, the Levite, the pasture, the pollution,
# the atonement); the registry map for the chapter's tokens; the tape's lines naming the Levites, Eleazar's succession, the burglar's blood, the
# place of refuge, the land and the markers; the daemons' installed_by values; the dependency forms; the checkpoint prefixes in use (grepped
# BEFORE naming); the register gate's seats in 35; the parser's own comments naming the bare dual.
import sys, io, re, contextlib, inspect, collections, yaml, glob
ROOT = '<repo-old>'
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
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
MODS = [('mishpatim_3', M3), ('mishpatim', M1), ('lev24', L24), ('shelach', SL), ('vayikra5', V5), ('naso', NS), ('second_census', C2), ('journeys', JO), ('borders', BO), ('zelophehad', ZL), ('gad_reuben', GR), ('chukat', CK), ('primeval', PR), ('bamidbar', CB), ('decalogue', DC), ('priesthood', PH), ('mekoshesh', MK), ('sanctions', SA), ('balak', BK)]
PATS = ('35:', 'refuge', 'flee', 'has_blood', 'no_blood', 'blood', 'murder', 'manslay', 'slayer', 'killer', 'avenger', 'ransom', 'kofer', 'witness', 'exile', 'high_priest', 'high priest', 'anoint', 'succession', 'leazar', 'levite', 'Levite', 'pasture', 'cubit', 'two thousand', 'thousand', 'forty-eight', 'six cities', 'pollute', 'defile', 'atone', 'unwitting', 'shogeg', 'suddenly', 'enmity', 'hatred', 'lying in wait', 'stone', 'iron', 'wood', 'congregation', 'twenty-three', 'court', 'Sanhedrin', 'Makkot', 'Josh 20', 'Josh 21', 'Deut 4:4', 'Deut 19', 'Deut 21', 'Exod 21:1', 'Exod 22:1', 'Exod 22:2', 'Lev 24:17', 'Gen 9:6', '3:15', '5:3', '6:9', '15:2', '26:54', '33:5', '34:2', '27:11', '20:2', 'sides', 'camp', 'dwell', 'shekhinah', 'Presence', 'in the midst', 'city', 'cities')
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
            print('   %-28s asks %s%s' % (d, asks[:80], ('  kinds ' + str(kinds[:40])) if kinds else ''))
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
    if re.search(r'kill|murder|slay|smite|struck|blood|flee|refuge|exile|aveng|witness|ransom|death|die|priest|city|cities|levit|pasture|pollut|defil|atone|unwit|sudden|enmity|hatred|stone|iron|congregation|court|judg|border|command|spoke|dwell|camp', k):
        print('    %-44s form %-8s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:100].replace('\n', ' ')))
print('  effects touching the matter:')
for f in sorted(F):
    if re.search(r'kill|murder|slay|smite|blood|flee|refuge|exile|aveng|witness|ransom|death|die|priest|city|cities|levit|pasture|pollut|defil|atone|unwit|enmity|stone|congregation|court|judg|commanded|dwell|camp|beheaded|has_blood|exempt|put_to_death|term|status|heaven', f):
        print('    %-40s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:110].replace('\n', ' ')))
print('  the ledger_op values: %s' % dict(collections.Counter(F[f].get('ledger_op') for f in F)))
for k in ('killer_case', 'burglar_case', 'refuge_case', 'manslayer_case', 'murderer_case', 'blasphemed_the_name', 'stoned_as_commanded', 'sentence_declared', 'placed_in_custody', 'borders_commanded', 'dividers_named', 'journeys_commanded', 'dispossession_commanded', 'aaron_died', 'eleazar_clothed', 'succession'):
    if k in E: print('  a kind row whole (%s): %s' % (k, E.get(k)))
for f in ('has_blood', 'flees_to_refuge', 'put_to_death', 'beheaded', 'exempt', 'ransom_imposed', 'stoned', 'commanded', 'borders_declared', 'in_force', 'holding_given', 'high_priest', 'priesthood_held', 'exiled', 'exiled_to_refuge', 'exile', 'in_custody', 'declaration_owed', 'barred_from_the_land', 'polluted', 'defiled'):
    if f in F: print('  an effect row whole (%s): %s' % (f, F.get(f)))

print('\n==== THE REGISTRY MAP for the chapter\'s tokens ====')
reg_map = CS.registry_map()
TOK = ('israel', 'israel_people', 'moses', 'eleazar', 'aaron', 'joshua', 'the-levites', 'levi', 'the-tribe-of-levi', 'levites', 'the-land', 'the-land-of-canaan', 'canaan', 'the-jordan', 'the-congregation', 'the-court', 'the-high-priest', 'the-priest', 'the-slayer', 'the-manslayer', 'the-murderer', 'the-avenger-of-blood', 'the-avenger', 'the-cities-of-refuge', 'the-six-cities', 'the-levite-cities', 'the-lord', 'heaven', 'the-tabernacle', 'the-camp', 'the-stranger', 'the-sojourner', 'the-sons-of-gad', 'the-sons-of-reuben', 'the-half-tribe-of-manasseh', 'the-dividers-of-the-land', 'the-burglar', 'the-householder', 'the-altar', 'the-tent-of-meeting')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])
reg = yaml.safe_load(open(f'{ROOT}/logic/corpus/entity_registry.yaml', encoding='utf-8'))
print('  registry entities %d; ids matching levi|priest|eleazar|aaron|canaan|land|court|congregation|city|cities|refuge|slayer|avenger|jordan|camp|tabernacle|tent: %s' % (len(reg['entities']), [e['id'] for e in reg['entities'] if re.search(r'levi|priest|eleazar|aaron|canaan|land|court|congregation|city|cities|refuge|slayer|avenger|jordan|camp|tabernacle|tent', e['id'])]))
print('  the rows for the levites / eleazar / the land of canaan / the court / the congregation: %s' % [e for e in reg['entities'] if e['id'] in ('the_levites', 'levites', 'tribe_of_levi', 'eleazar_son_of_aaron', 'the_land_of_canaan', 'the_court', 'the_congregation', 'the_priesthood', 'the_high_priest', 'israel_people')])
print('  the registry rows\' shape (the last row): %s' % reg['entities'][-1])
print('  institution rows: %s' % [e for e in reg['entities'] if e.get('kind') == 'institution'])

print('\n==== THE TAPE\'S LINES naming the Levites / Eleazar / the burglar / the refuge / the land, and the markers ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
for l in tape.split('\n'):
    if re.search(r"levite|eleazar|aaron_died|succession|clothed|has_blood|flees_to_refuge|refuge|burglar|killer|murder|the-land-of-canaan|borders_|dividers_|Num 20:2|Num 34:|Num 33:5|Num 36:|Num 26:5|Num 5:|Num 6:", l) or re.search(r'# ---- Num 3', l) or ('w.marker(' in l and re.search(r"Num (1|7|20|21|27|33):", l)):
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
print('  THE PARSER\'S OWN COMMENTS naming the dual / two thousand: %s' % [(i + 1, l.strip()[:220]) for i, l in enumerate(src_cs.split('\n')) if re.search(r'two thousand|dual|אלפים|אַלְפַּיִם|35:5', l)][:12])
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  daemons %d; installed_by values: %s' % (len(dd['daemons']), dict(collections.Counter(v.get('installed_by') for v in dd['daemons'].values()))))
print('  the walk\'s daemons (given_at, installed_by): %s' % {k: (v.get('given_at'), v.get('installed_by')) for k, v in dd['daemons'].items() if k in ('law_census', 'law_naso', 'law_shelach', 'law_korach', 'law_chukat', 'law_balak', 'law_second_census', 'law_musafim', 'law_vows', 'law_midian', 'law_gad_reuben', 'law_journeys', 'law_borders', 'law_zelophehad', 'law_mishpatim_3', 'law_lev24', 'law_tent')})
print('  the full law_borders block: %s' % dd['daemons'].get('law_borders'))
print('  the full law_mishpatim_3 block: %s' % dd['daemons'].get('law_mishpatim_3'))
print('  the full law_chukat block head: %s' % {k: str(v)[:400] for k, v in dd['daemons'].get('law_chukat', {}).items()})
print('  the functions block borders: %s' % {k: v for k, v in dd.get('functions', {}).items() if k == 'borders'})
print('  the functions block mishpatim_3: %s' % {k: v for k, v in dd.get('functions', {}).items() if k == 'mishpatim_3'})
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers at Num 35: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if str(p.get('verse', '')).startswith('Num 35')]))
print('  edges naming the callees as `to`: %s' % collections.Counter(e['to'] for e in dep['edges'] if e['to'] in ('mishpatim_3', 'mishpatim', 'lev24', 'shelach', 'vayikra5', 'naso', 'second_census', 'journeys', 'borders', 'zelophehad', 'gad_reuben', 'chukat', 'primeval', 'bamidbar', 'decalogue', 'priesthood', 'mekoshesh', 'sanctions', 'family', 'balak', 'sanctuary_build', 'erection', 'holiness')))
print('  the spans of the callees: %s' % {k: dep['spans'][k] for k in ('mishpatim_3', 'mishpatim', 'lev24', 'shelach', 'vayikra5', 'naso', 'second_census', 'journeys', 'borders', 'zelophehad', 'gad_reuben', 'chukat', 'primeval', 'bamidbar', 'decalogue', 'priesthood', 'mekoshesh', 'sanctions', 'family', 'holiness', 'sanctuary_build') if k in dep['spans']})
print('  the borders edges on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], e.get('via'), str(e.get('why', ''))[:70]) for e in dep['edges'] if e['from'] == 'borders'])
print('  the edges INTO mishpatim_3 / lev24 / priesthood / decalogue on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], str(e.get('why', ''))[:60]) for e in dep['edges'] if e['to'] in ('mishpatim_3', 'lev24', 'priesthood', 'decalogue')])
print('  a VIA edge row WHOLE (the form to copy): %s' % [e for e in dep['edges'] if e.get('disposition') == 'VIA' and e['from'] == 'borders'][:1])
print('  a FALSE edge row WHOLE: %s' % [e for e in dep['edges'] if e.get('disposition') == 'FALSE' and e['from'] in ('borders', 'journeys')][:1])
print('  a REFERENCE-link CALL edge row WHOLE: %s' % [e for e in dep['edges'] if e.get('disposition') == 'CALL' and e['from'] == 'borders'][:1])
print('  a TRANSFER edge row WHOLE (taught_by): %s' % [e for e in dep['edges'] if e.get('link') == 'transfer' and e.get('taught_by')][:1])
print('  a pointer row\'s shape (INTERNAL, borders/journeys): %s' % [p for p in dep['pointers'] if p.get('span') in ('borders', 'journeys')][:2])
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the register seats naming Num 35 / Num 36 (section, key, class, why): %s' % [(sec, k, v.get('class'), str(v.get('why', ''))[:120]) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if 'Num 35' in k or 'Num 36' in k])
print('  declared counts %d receipts %d footers %d registers %d' % tuple(len(decl.get(s, {})) for s in ('counts', 'receipts', 'footers', 'registers')))
cal = yaml.safe_load(open(f'{ROOT}/World/step9/calendar_parameters.yaml', encoding='utf-8'))
print('  calendar rows %d; keys: %s' % (len(cal.get('rows', cal.get('parameters', {}))), list(cal.get('rows', cal.get('parameters', {})))[:60]))
print('  calendar top keys: %s' % list(cal))
