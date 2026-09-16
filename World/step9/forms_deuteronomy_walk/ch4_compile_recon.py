import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 2b — THE COMPILE OF CHAPTER 4, Deuteronomy 4:1-49 (2026-09-16; the owner: "then we finish 4"): THE RECONNAISSANCE
# before the measurement pass (deu_compile_recon.py's form on chapter 4) — the callee modules' defs, asks, DATA keys and uppercase tables (so the
# measure's calls are typed from THIS print); the kinds and effects on file touching the chapter's matter (Horeb, the ten words, the tablets, the
# image, the host of heaven, Baal-peor, the bar, the exodus's instruments, the creation, the exile and the return, the witnesses, the refuge
# cities, the two frames); the registry map for the chapter's tokens; the tape's lines the chapter retells; the daemons' installed_by values; the
# dependency forms; the checkpoint prefixes in use (grepped BEFORE naming); the register gate's seats in chapter 4.
import sys, io, re, contextlib, inspect, collections, yaml, glob, subprocess, os
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import cold_run_exodus_story as ES
    import cold_run_erection as ER
    import cold_run_decalogue as DC
    import cold_run_balak as BK
    import cold_run_refuge as RF
    import cold_run_opening_speech as OS
    import cold_run_primeval as PR
    import cold_run_pre_sinai as PS
    import cold_run_tochacha as TC
    import cold_run_holiness as HO
    import cold_run_sanctions as SA
    import cold_run_shelach as SL
    import cold_run_chukat as CK
    import cold_run_gad_reuben as GR
    import cold_run_borders as BO
    import cold_run_journeys as JO
    import cold_run_sanctuary_build as SB
    import cold_run_mishpatim as M1
MODS = [('exodus_story', ES), ('erection', ER), ('decalogue', DC), ('balak', BK), ('refuge', RF), ('opening_speech', OS), ('primeval', PR), ('pre_sinai', PS), ('tochacha', TC), ('holiness', HO), ('sanctions', SA), ('shelach', SL), ('chukat', CK), ('gad_reuben', GR), ('borders', BO), ('journeys', JO), ('sanctuary_build', SB), ('mishpatim', M1)]
PATS = ('Deut 4', 'Deuteronomy 4', 'Peor', 'peor', 'Horeb', 'horeb', 'tablet', 'ten words', 'Ten Words', 'ten commandments', 'Decalogue', 'decalogue', 'image', 'idol', 'graven', 'likeness', 'host of heaven', 'the sun', 'the moon', 'stars', 'exile', 'scatter', 'witness', 'heaven and earth', 'refuge', 'Bezer', 'Ramoth', 'Golan', 'set apart', 'iron furnace', 'strong hand', 'mighty hand', 'outstretched arm', 'from the midst', 'consuming fire', 'jealous', 'created', 'creation', 'Sion', 'Hermon', 'Pisgah', 'Beth-peor', 'Aroer', 'Arnon', 'add ', 'diminish', 'seek', 'forget', 'covenant', 'statutes and', 'Sihon', 'Og ', 'Amorite', 'testimonies', 'judgments', 'assemble', 'voice of', 'fire', 'cloud', 'thick darkness', 'ascend', 'forty days', 'seventeenth', 'Tammuz', 'Sivan', 'giving', 'apportion', 'divide', 'bowed', 'serve', 'wood and stone', 'few in number', 'perish', 'dispossess', 'nations greater', 'loved your fathers', 'chose', 'presence', 'great power', 'installed_by', 'given_at')
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
            print('   %-28s asks %s%s' % (d, asks[:90], ('  kinds ' + str(kinds[:60])) if kinds else ''))
    if hasattr(mod, 'DATA'):
        print('   DATA keys (%d): %s' % (len(mod.DATA), sorted(mod.DATA)))
    ups = [n for n in dir(mod) if n.isupper() and not n.startswith('_') and n not in ('DATA', 'PROBES', 'CASES', 'GUARDED', 'HERE', 'ROOT')]
    print('   uppercase names: %s' % ups[:120])
    print('   imports: %s' % sorted(set(re.findall(r'^\s*import (cold_run_\w+)', src, re.M))))
    for pat in PATS:
        hits = [l.strip()[:170] for l in src.split('\n') if pat in l]
        if hits: print('   lines with %-16r: %d  e.g. %s' % (pat, len(hits), hits[:3]))

print('\n==== THE KINDS ON FILE touching the chapter\'s matter ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
print('  kinds %d, effects %d' % (len(E), len(F)))
KP = r'peor|tablet|assembl|voice|covenant|image|idol|calf|exile|witness|refuge|horeb|sinai|creat|host|forget|seek|jealous|oath|barred|frame|speech|torah|statute|commandment|teach|learn|showed|shown|tried|furnace|redeem|apportion|scatter|bowed|served|other_god|decalogue|ten_|words|fire|cloud|mountain|descend|lord_|brought_out|thunder|bounds|sanctif|ascend|declared|commanded|expound|set_apart|cities|sworn|sware|swore|dispossess|possess|chose|love'
for k in sorted(E):
    if re.search(KP, k):
        print('    %-44s form %-8s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:100].replace('\n', ' ')))
print('  effects touching the matter:')
for f in sorted(F):
    if re.search(KP + r'|status|block|debit|heaven|body|granted|destroyed|smitten|plague|died|holding|presence|dwell|in_force|rule_installed|declaration', f):
        print('    %-40s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:110].replace('\n', ' ')))
print('  the ledger_op values: %s' % dict(collections.Counter(F[f].get('ledger_op') for f in F)))
for k in ('lord_descended', 'thunder_and_horn', 'moses_went_up', 'moses_ascended', 'tablets_broken', 'covenant_cut_at_sinai', 'covenant_blood_thrown', 'israel_yoked_to_baal_peor', 'judges_commanded_to_slay', 'plague_dead_counted', 'brought_out', 'sentence_at_meribah', 'refuge_law_given', 'speech_opened', 'evening_and_morning', 'formed_from_dust', 'people_exiled', 'warning_refused', 'sihon_smitten_land_possessed', 'og_smitten', 'encamped_in_the_plains_of_moab', 'people_sanctified', 'bounds_set'):
    if k in E: print('  a kind row whole (%s): %s' % (k, str(E.get(k))[:900]))
for f in ('tablets_delivered', 'covenant_declared', 'covenant_upheld', 'covenant_remembered', 'scattered_among_nations', 'torah_expounded', 'contending_barred', 'commanded', 'barred_from_the_land', 'yoked_to_baal_peor', 'plague_struck', 'land_granted', 'destroyed', 'in_force', 'rule_installed', 'presence_dwells', 'heaven_and_earth_witness', 'cities_set_apart', 'adding_barred', 'witnesses_called', 'labor_barred', 'sanctify_day', 'lashes', 'accepted', 'exempt', 'stoned', 'put_to_death'):
    print('  an effect row (%s): %s' % (f, str(F.get(f))[:700] if f in F else 'ABSENT'))

print('\n==== THE REGISTRY MAP for the chapter\'s tokens ====')
reg_map = CS.registry_map()
TOK = ('israel', 'israel_people', 'moses', 'joshua', 'the-mountain', 'horeb', 'sinai', 'mount-sinai', 'the-tablets', 'heaven', 'the-heavens', 'earth', 'the-earth', 'the-sun', 'the-moon', 'the-stars', 'the-host-of-heaven', 'egypt', 'egypt_people', 'the-peoples', 'the-nations', 'bezer', 'ramoth', 'golan', 'the-three-cities', 'the-six-cities', 'the-manslayer', 'sihon', 'og', 'the-amorite', 'the-lord', 'god', 'adam', 'the-world', 'the-land', 'the-land-of-canaan', 'the-jordan', 'baal-peor', 'the-court', 'the-fathers', 'abraham', 'isaac', 'jacob', 'the-calf')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])
reg = yaml.safe_load(open(f'{ROOT}/logic/corpus/entity_registry.yaml', encoding='utf-8'))
print('  registry entities %d; ids matching mountain|sinai|horeb|tablet|heaven|earth|sun|moon|star|host|egypt|bezer|ramoth|golan|cit|peor|world|adam|nation|people: %s' % (len(reg['entities']), [e['id'] for e in reg['entities'] if re.search(r'mountain|sinai|horeb|tablet|heaven|earth|^sun|moon|star|host|egypt|bezer|ramoth|golan|cit|peor|world|^adam|nation|people', e['id'])]))
print('  institution rows: %s' % [e['id'] for e in reg['entities'] if e.get('kind') == 'institution'])

print('\n==== THE TAPE\'S LINES the chapter retells ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
for l in tape.split('\n'):
    if re.search(r"Exod 19:|Exod 20:|Exod 24:1[2-8]|Exod 31:|Exod 32:1[5-9]|Exod 34:2[7-9]|Num 25:[1-9]|Exod 12:(29|41|51)|Exod 13:21|Gen 1:2[7-9]|Gen 1:31|Gen 2:7|Num 20:1[2-3]|Num 21:2[3-5]|Num 21:3[3-5]|Num 35:|Num 33:5[0-6]|Deut 1:1|Deut 3:2", l):
        print('   %s' % l.strip()[:260])
print('  DAEMON_ORDER %d, tail %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-3:]))
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
print('  M[] marker names on file: %s' % re.findall(r"M\['([a-z_0-9:]+)'\] = ", src_cs))
print('  the GLOBAL-COUNT checkpoints (len(...cmd / isr_cmd / markers / closes / entities / pend / daemons): %s' % [(i + 1, l.strip()[:150]) for i, l in enumerate(src_cs.split('\n')) if re.search(r"cp\('C[A-Z]\d", l) and re.search(r'len\(cmd_v\)|isr_cmd|len\(w\.entities\)|closes_done|len\(markers|pend|len\(CS\.DAEMON_ORDER\)|daemons\)|MARKER', l)][:40])
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  daemons %d; installed_by values: %s' % (len(dd['daemons']), dict(collections.Counter(str(v.get('installed_by')).split()[0] for v in dd['daemons'].values()))))
print('  the daemons with installed_by an event: %s' % {k: (v.get('given_at'), v.get('installed_by')) for k, v in dd['daemons'].items() if str(v.get('installed_by')) != 'boot'})
print('  the full law_decalogue block: %s' % dd['daemons'].get('law_decalogue'))
print('  the functions block decalogue: %s' % {k: v for k, v in dd.get('functions', {}).items() if k == 'decalogue'})
print('  the functions block erection keys: %s' % list((dd.get('functions', {}).get('erection') or {}).keys()))
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers naming Deut 4: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if re.search(r'Deut 4:', str(p))][:10]))
print('  the opening_speech edges on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], e.get('via'), str(e.get('why', ''))[:60]) for e in dep['edges'] if e['from'] == 'opening_speech'])
print('  the opening_speech pointers on file: %s' % [(p.get('verse'), p.get('form'), p.get('disposition'), str(p.get('why', ''))[:60]) for p in dep['pointers'] if p.get('runner') == 'opening_speech'][:20])
print('  a CALL edge row WHOLE (opening_speech): %s' % [e for e in dep['edges'] if e['from'] == 'opening_speech' and e.get('disposition') == 'CALL'][:1])
print('  a FALSE edge row WHOLE (opening_speech): %s' % [e for e in dep['edges'] if e['from'] == 'opening_speech' and e.get('disposition') == 'FALSE'][:1])
print('  a RUN_CITATION pointer row WHOLE (opening_speech): %s' % [p for p in dep['pointers'] if p.get('runner') == 'opening_speech' and p.get('disposition') == 'RUN_CITATION'][:1])
print('  an INTERNAL pointer row WHOLE (opening_speech): %s' % [p for p in dep['pointers'] if p.get('runner') == 'opening_speech' and p.get('disposition') == 'INTERNAL'][:1])
print('  a REFERENCE (by lemma) edge row WHOLE: %s' % [e for e in dep['edges'] if e.get('link') == 'reference' and e.get('reference_by')][:1])
print('  the spans of decalogue / erection / opening_speech: %s' % {k: dep['spans'].get(k) for k in ('decalogue', 'erection', 'opening_speech', 'refuge')})
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the register seats naming Deut 4 / 1 (section, key, class, why): %s' % [(sec, k, v.get('class'), str(v.get('why', ''))[:120]) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.startswith('Deut 4') or k.startswith('Deut 1')])
print('  declared counts %d receipts %d footers %d registers %d' % tuple(len(decl.get(s, {})) for s in ('counts', 'receipts', 'footers', 'registers')))
cal = yaml.safe_load(open(f'{ROOT}/World/step9/calendar_parameters.yaml', encoding='utf-8'))
print('  sinai_days / second_tablets_given rows: %s' % {k: cal.get('parameters', cal.get('rows', {})).get(k) for k in ('sinai_days', 'second_tablets_given')})
