#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 1b — THE COMPILE OF THE OPENING SPEECH, Deuteronomy 1:1-3:29 (2026-09-15; the owner: "Go 1b right"): THE
# RECONNAISSANCE before the measurement pass (ref_compile_recon.py's form) — the callee modules' defs, asks, DATA keys and uppercase tables (so the
# measure's calls are typed from THIS print); the kinds and effects on file touching the speech's matter (the spies, the oath, Hormah, Edom, Moab,
# Ammon, Sihon, Og, the east's grants, Jair, Machir, the judges, the officers, Joshua's charge, the plea, Pisgah, the ban); the registry map for the
# chapters' tokens; the tape's lines the speech retells and the markers between Paran and the plains; the daemons' installed_by values; the
# dependency forms; the checkpoint prefixes in use (grepped BEFORE naming); the register gate's seats in Deuteronomy 1-3; the parser's own comments
# naming the fraction.
import sys, io, re, contextlib, inspect, collections, yaml, glob, subprocess, os
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import cold_run_exodus_story as ES
    import cold_run_shelach as SL
    import cold_run_chukat as CK
    import cold_run_gad_reuben as GR
    import cold_run_zelophehad as ZL
    import cold_run_journeys as JO
    import cold_run_borders as BO
    import cold_run_second_census as C2
    import cold_run_balak as BK
    import cold_run_primeval as PR
    import cold_run_mamre as MA
    import cold_run_joseph as JS
    import cold_run_ordinances as OR
    import cold_run_holiness as HO
    import cold_run_erection as ER
    import cold_run_bamidbar as CB
    import cold_run_beha as BH
    import cold_run_refuge as RF
    import cold_run_korach as KO
MODS = [('exodus_story', ES), ('shelach', SL), ('chukat', CK), ('gad_reuben', GR), ('zelophehad', ZL), ('journeys', JO), ('borders', BO), ('second_census', C2), ('balak', BK), ('primeval', PR), ('mamre', MA), ('joseph', JS), ('ordinances', OR), ('holiness', HO), ('erection', ER), ('bamidbar', CB), ('beha', BH), ('refuge', RF), ('korach', KO)]
PATS = ('Deut 1', 'Deut 2', 'Deut 3', 'Deuteronomy 1', 'Deuteronomy 2', 'Deuteronomy 3', 'Kadesh', 'kadesh', 'Horeb', 'horeb', 'spies', 'Hormah', 'hormah', 'Seir', 'seir', 'Edom', 'edom', 'Moab', 'moab', 'Ammon', 'ammon', 'Zered', 'Arnon', 'arnon', 'Sihon', 'sihon', 'Og ', "Og'", 'og_', 'Bashan', 'bashan', 'Jair', 'jair', 'Machir', 'machir', 'half', 'armed', 'Joshua', 'joshua', 'Caleb', 'caleb', 'Pisgah', 'Abarim', 'Nebo', 'judges', 'officers', 'thousands', 'Jethro', 'jethro', '78,600', '78600', 'Anak', 'anak', 'Rephaim', 'rephaim', 'Emim', 'Horite', 'Avvim', 'Caphtor', 'Lot', 'lot_', 'Esau', 'esau', 'manna', 'forty years', 'thirty-eight', 'decree', 'oath', 'little ones', 'good and evil', 'Peor', 'peor', 'barred', 'Meribah', 'meribah', 'plea', 'pray', 'wroth', 'enough', 'eleven days', 'fortieth', 'eleventh', 'Shevat', 'bribe', 'respect', 'small and', 'hard matter', 'hard case', 'Havvoth', 'Argob', 'Hermon', 'Chinnereth', 'Salt Sea', 'Jabbok', 'iron', 'bed', 'cubit', 'Beth-peor', 'Amalek', 'amalek', 'Zin', 'Paran', 'paran', 'eagle', 'carried', 'pillar', 'fire by night', 'cloud')
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
            print('   %-28s asks %s%s' % (d, asks[:90], ('  kinds ' + str(kinds[:40])) if kinds else ''))
    if hasattr(mod, 'DATA'):
        print('   DATA keys (%d): %s' % (len(mod.DATA), sorted(mod.DATA)))
    ups = [n for n in dir(mod) if n.isupper() and not n.startswith('_') and n not in ('DATA', 'PROBES', 'CASES', 'GUARDED', 'HERE', 'ROOT')]
    print('   uppercase names: %s' % ups[:90])
    print('   imports: %s' % sorted(set(re.findall(r'^\s*import (cold_run_\w+)', src, re.M))))
    for pat in PATS:
        hits = [l.strip()[:170] for l in src.split('\n') if pat in l]
        if hits: print('   lines with %-14r: %d  e.g. %s' % (pat, len(hits), hits[:3]))

print('\n==== THE KINDS ON FILE touching the speech\'s matter ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
print('  kinds %d, effects %d' % (len(E), len(F)))
KP = r'spies|spy|report|caleb|hushed|evil_report|wept|pleaded|glory_appeared|attributes|pardoned|decree|died_by_plague|presumed|hormah|messengers|edom|highway|came_out|sihon|heshbon|jazer|og_|land_requested|rebuked|offered_to_arm|condition|accepted|commission|answered|granted|cities_built|machir|jair|nobah|jethro|judges|sentence_at_meribah|barred|spoke_to_moses|speech|commanded|relayed|charged|prayed|plea|entreat|blessed|horeb|departed|journeyed|manna|amalek|marker|seir|moab|ammon|lot|esau|horite|rephaim|anak|giant|ban|utterly|destroyed|possessed|dwelt|inherited|rest|strengthen|encourag|ascend|viewed|pisgah|abarim|died|buried|peor'
for k in sorted(E):
    if re.search(KP, k):
        print('    %-44s form %-8s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:100].replace('\n', ' ')))
print('  effects touching the matter:')
for f in sorted(F):
    if re.search(KP + r'|oath|commanded|decreed|forty|set_|holding|land_held|granted|possession|cities|villages|hard_cases|appointed|judge|barred_from_the_land|heaven|status|block|debit', f):
        print('    %-40s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:110].replace('\n', ' ')))
print('  the ledger_op values: %s' % dict(collections.Counter(F[f].get('ledger_op') for f in F)))
for k in ('judges_appointed', 'spies_commanded', 'decree_declared', 'pardoned_and_decreed', 'smitten_to_hormah', 'edom_refused', 'edom_came_out_against', 'israel_pleaded_the_highway', 'messengers_sent_to_sihon', 'sihon_smitten_land_possessed', 'og_smitten', 'og_came_out_and_fear_not', 'land_granted_east', 'condition_stipulated', 'commission_charged', 'sentence_at_meribah', 'command_relayed', 'plea_made', 'moses_pleaded_on_the_attributes', 'gilead_taken_by_machir', 'villages_taken_by_jair', 'presumed_to_go_up', 'israel_dwelt_and_jazer_taken', 'heshbon_and_the_parable'):
    if k in E: print('  a kind row whole (%s): %s' % (k, str(E.get(k))[:1200]))
for f in ('barred_from_the_land', 'commanded', 'decreed_to_die_in_the_wilderness', 'set_to_die', 'holding_given', 'land_held', 'hard_cases_to_moses', 'plea_made', 'oath_sworn', 'hormah_named', 'in_force', 'rule_installed', 'declaration_owed', 'accepted', 'exempt', 'possession_entitled', 'armed_crossing_owed', 'blessed', 'rest_given', 'strengthened', 'commissioned', 'invested_office'):
    if f in F: print('  an effect row whole (%s): %s' % (f, str(F.get(f))[:1200]))

print('\n==== THE REGISTRY MAP for the chapters\' tokens ====')
reg_map = CS.registry_map()
TOK = ('israel', 'israel_people', 'moses', 'joshua', 'caleb', 'aaron', 'eleazar', 'edom', 'esau', 'the-sons-of-esau', 'moab', 'the-sons-of-lot', 'ammon', 'the-sons-of-ammon', 'lot', 'sihon', 'og', 'the-amorite', 'the-amorites', 'the-emim', 'the-rephaim', 'the-horites', 'the-horim', 'the-avvim', 'the-caphtorim', 'the-anakim', 'the-sons-of-gad', 'the-sons-of-reuben', 'the-half-tribe-of-manasseh', 'the-sons-of-gad-and-reuben', 'jair', 'the-sons-of-machir', 'machir', 'the-judges', 'the-officers', 'the-court', 'the-twelve-spies', 'the-ten-spies', 'the-generation-of-the-wilderness', 'the-men-of-war', 'the-land', 'the-land-of-canaan', 'the-jordan', 'heaven', 'the-lord', 'jethro', 'the-heads', 'the-tribes', 'the-levites', 'the-amalekite', 'the-canaanite', 'kadesh-barnea', 'seir', 'the-tent-of-meeting', 'the-dividers-of-the-land', 'egypt_people', 'the-heads-of-gilead', 'the-daughters-of-zelophehad', 'jacob', 'abraham', 'isaac')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])
reg = yaml.safe_load(open(f'{ROOT}/logic/corpus/entity_registry.yaml', encoding='utf-8'))
print('  registry entities %d; ids matching edom|esau|moab|ammon|lot|sihon|og|amor|emim|repha|hor|avv|caphtor|anak|gad|reuben|manasseh|jair|machir|judge|officer|court|spies|joshua|caleb|jethro|amalek|canaanite|seir|kadesh: %s' % (len(reg['entities']), [e['id'] for e in reg['entities'] if re.search(r'edom|esau|moab|ammon|^lot|sihon|^og|amor|emim|repha|hor|avv|caphtor|anak|gad|reuben|manasseh|jair|machir|judge|officer|court|spies|joshua|caleb|jethro|amalek|canaanite|seir|kadesh', e['id'])]))
print('  the rows for joshua / caleb / edom / moab / the-court / sihon / og / the-sons-of-gad: %s' % [e for e in reg['entities'] if e['id'] in ('yehoshua', 'joshua', 'caleb', 'edom', 'edom_people', 'moab', 'moab_people', 'the_court', 'sihon', 'og', 'the_sons_of_gad', 'gad_tribe', 'reuben_tribe', 'half_manasseh')])
print('  the registry rows\' shape (the last row): %s' % reg['entities'][-1])
print('  institution rows: %s' % [e['id'] for e in reg['entities'] if e.get('kind') == 'institution'])

print('\n==== THE TAPE\'S LINES the speech retells, and the markers from Paran to the plains ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
for l in tape.split('\n'):
    if re.search(r"Exod 18:|Exod 33:1|Num 1[34]:|Num 20:1[4-9]|Num 20:2[01]|Num 21:1[0-9]|Num 21:2|Num 21:3|Num 32:|Num 27:1[2-9]|Num 27:2|Num 10:1[12]|Num 12:16|Num 13:25|Num 25:1 ", l) or ('w.marker(' in l and re.search(r"Num (1[0-9]|2[0-9]|3[0-9]):", l)):
        print('   %s' % l.strip()[:300])
print('  DAEMON_ORDER %d, tail %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-4:]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s\n  SLOTS %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT, CS.SLOTS))
print('  cp() checkpoint prefixes in use: %s' % sorted(collections.Counter(re.findall(r"cp\('(C[A-Z])\d", src_cs)).items()))
print('  VERDICTS labels\' prefixes: %s' % sorted(collections.Counter(re.findall(r"'(C[A-Z])\d [A-Z]+'", src_cs)).items()))
used = set(re.findall(r"cp\('(C[A-Z])\d", src_cs)) | set(re.findall(r"'(C[A-Z])\d [A-Z]+'", src_cs))
free = [c for c in ['C' + x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'] if c not in used]
print('  FREE prefixes: %s' % free)
for cand in free:
    hits = []
    for f in glob.glob(f'{ROOT}/World/step9/*.py'):
        t = open(f, encoding='utf-8').read()
        n = len(re.findall(r"\b%s\d\b" % cand, t))
        if n: hits.append((f.split('/')[-1], n))
    print('    %s used as a label elsewhere: %s' % (cand, hits))
print('  M[] marker names on file: %s' % re.findall(r"M\['([a-z_0-9]+)'\] = ", src_cs))
print('  THE PARSER\'S OWN COMMENTS naming half / the fraction / Fraction: %s' % [(i + 1, l.strip()[:220]) for i, l in enumerate(src_cs.split('\n')) if re.search(r'half|fraction|Fraction|חצי|one of the', l)][:20])
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  daemons %d; installed_by values: %s' % (len(dd['daemons']), dict(collections.Counter(v.get('installed_by') for v in dd['daemons'].values()))))
print('  the walk\'s daemons (given_at, installed_by): %s' % {k: (v.get('given_at'), v.get('installed_by')) for k, v in dd['daemons'].items() if k in ('law_shelach', 'law_chukat', 'law_gad_reuben', 'law_journeys', 'law_borders', 'law_refuge', 'law_zelophehad', 'law_exodus_story', 'law_ordinances', 'law_holiness', 'law_vows', 'law_midian')})
print('  the full law_refuge block: %s' % dd['daemons'].get('law_refuge'))
print('  the full law_exodus_story block head: %s' % {k: str(v)[:400] for k, v in dd['daemons'].get('law_exodus_story', {}).items()})
print('  the full law_gad_reuben block: %s' % dd['daemons'].get('law_gad_reuben'))
print('  the functions block refuge: %s' % {k: v for k, v in dd.get('functions', {}).items() if k == 'refuge'})
print('  the functions block exodus_story: %s' % {k: v for k, v in dd.get('functions', {}).items() if k == 'exodus_story'})
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers naming Deut: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if 'Deut' in str(p)][:10]))
print('  edges naming the callees as `to`: %s' % collections.Counter(e['to'] for e in dep['edges'] if e['to'] in [m for m, _ in MODS]))
print('  the refuge edges on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], e.get('via'), str(e.get('why', ''))[:70]) for e in dep['edges'] if e['from'] == 'refuge'])
print('  a VIA edge row WHOLE (the form to copy): %s' % [e for e in dep['edges'] if e.get('disposition') == 'VIA' and e['from'] == 'refuge'][:1])
print('  a FALSE edge row WHOLE: %s' % [e for e in dep['edges'] if e.get('disposition') == 'FALSE' and e['from'] == 'refuge'][:1])
print('  a REFERENCE-link CALL edge row WHOLE: %s' % [e for e in dep['edges'] if e.get('disposition') == 'CALL' and e['from'] == 'refuge'][:1])
print('  a PARAMETER edge row WHOLE: %s' % [e for e in dep['edges'] if e.get('disposition') == 'PARAMETER'][:1])
print('  a RUN_CITATION pointer row WHOLE: %s' % [p for p in dep['pointers'] if p.get('disposition') == 'RUN_CITATION'][:1])
print('  an INTERNAL pointer row WHOLE: %s' % [p for p in dep['pointers'] if p.get('disposition') == 'INTERNAL'][:1])
print('  a TRANSFER edge row WHOLE (taught_by): %s' % [e for e in dep['edges'] if e.get('link') == 'transfer' and e.get('taught_by')][:1])
print('  a HYPOTHESIS edge row WHOLE: %s' % [e for e in dep['edges'] if e.get('link') == 'hypothesis'][:1])
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the register seats naming Deut (section, key, class, why): %s' % [(sec, k, v.get('class'), str(v.get('why', ''))[:160]) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.startswith('Deut')])
print('  declared counts %d receipts %d footers %d registers %d' % tuple(len(decl.get(s, {})) for s in ('counts', 'receipts', 'footers', 'registers')))
print('  the footer Num 36:13 whole: %s' % decl.get('footers', {}).get('Num 36:13'))
cal = yaml.safe_load(open(f'{ROOT}/World/step9/calendar_parameters.yaml', encoding='utf-8'))
print('  calendar top keys: %s; rows/parameters keys: %s' % (list(cal), list(cal.get('rows', cal.get('parameters', {})))[:60]))
print('  the exodus era rows: %s' % [ (k, str(v)[:200]) for k, v in (cal.get('eras') or {}).items()] if isinstance(cal.get('eras'), dict) else str(cal.get('eras'))[:600])
