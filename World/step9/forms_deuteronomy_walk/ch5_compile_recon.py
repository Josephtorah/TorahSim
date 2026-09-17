import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 3b — THE COMPILE OF CHAPTER 5, Deuteronomy 5:1-33 (2026-09-16; the owner: "go"): THE RECONNAISSANCE before the
# design (ch4_compile_recon.py's form on chapter 5) — (1) WHICH RUNNER HOLDS A CELL FOR EACH OF THE TEN WORDS (the laws' readback grades code
# against code: every runner's ink refs to Exodus 20 and to the words' other seats — 21:12-17, 23:1, Leviticus 19:3, 19:11-13, 20:10, 24:10-16 —
# scanned by regex, per def); (2) the callee modules' defs, asks, DATA keys and uppercase tables (the measure's calls typed from THIS print);
# (3) the kinds and effects on file touching the chapter's matter; (4) the registry map; (5) the tape's lines the chapter retells (Horeb, the
# covenant, the tablets, the mob and the elders) and the tape's LAST lines and markers (the stretch open or closed — 2b's lesson 2); (6) the
# sequence file's tuples, the checkpoint prefixes in use and FREE, the M[] names, the daemons' installed_by; (7) the dispositions on file for the
# callees, the pointers and register seats naming Deut 5, and THE REGISTER GATE'S CLASS RULES from its own code (the class predicted, lesson viii).
import sys, io, re, contextlib, inspect, collections, yaml, glob, subprocess, os, importlib
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
NAMES = ['exodus_story', 'erection', 'decalogue', 'ordinances', 'mishpatim', 'mishpatim_3', 'sanctions', 'holiness', 'family', 'refuge',
         'incense_shekel', 'pre_sinai', 'musafim', 'obey_horeb', 'opening_speech', 'lev24', 'vows', 'shelach', 'chukat', 'sanctuary_build']
MODS = []
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    for n in NAMES:
        try:
            MODS.append((n, importlib.import_module('cold_run_' + n)))
        except Exception as e:
            print('IMPORT FAILED', n, e, file=sys.stderr)
print('modules imported: %s' % [n for n, _ in MODS])

print('\n==== (1) THE TEN WORDS\' CELLS — every runner\'s refs to the first copy and the words\' other seats, per def ====')
SEATS = [(r'Exod(?:us)? 20:(\d+)', 'Exod 20'), (r"ink\('20:(\d+)'", 'Exod 20 (ink)"'), (r'Exod(?:us)? 21:1([2-7])', 'Exod 21:1x'), (r'Exod(?:us)? 23:1\b', 'Exod 23:1'),
         (r'Lev(?:iticus)? 19:(3|11|12|13)\b', 'Lev 19'), (r'Lev(?:iticus)? 20:10\b', 'Lev 20:10'), (r'Lev(?:iticus)? 24:1([0-6])', 'Lev 24:1x'),
         (r'Deut(?:eronomy)? 5:(\d+)', 'Deut 5'), (r'Deut(?:eronomy)? 19:1([6-9])', 'Deut 19:1x'), (r'Deut(?:eronomy)? 19:2[01]', 'Deut 19:2x'),
         (r'covet|Covet', 'covet'), (r'adulter', 'adultery'), (r'murder', 'murder'), (r'false witness|false report|conspiring', 'false witness'),
         (r'honor.{0,12}(father|parent)|father and .{0,10}mother', 'honor parents'), (r'in vain|vain_name|vain oath', 'vain'), (r'other gods|graven|no_image', 'other gods / image'),
         (r'[Ss]abbath', 'sabbath'), (r'ten words|Ten Words|Decalogue|decalogue', 'decalogue'), (r'do and hear|hear and do|we will do|naaseh', 'do and hear'),
         (r'face to face|face in face', 'face to face'), (r'Horeb|horeb', 'Horeb')]
for f in sorted(glob.glob(f'{ROOT}/World/step9/cold_run_*.py')):
    name = os.path.basename(f)[9:-3]
    src = open(f, encoding='utf-8').read()
    lines = src.split('\n')
    defs = [(m.start(), m.group(1)) for m in re.finditer(r'^def ([a-z_0-9]+)\(', src, re.M)]
    def def_at(pos):
        d = 'MODULE'
        for p, n in defs:
            if p <= pos: d = n
            else: break
        return d
    found = collections.defaultdict(lambda: collections.Counter())
    for pat, label in SEATS:
        for m in re.finditer(pat, src):
            found[label][def_at(m.start())] += 1
    if found:
        print('  -- %s:' % name)
        for label in found:
            print('     %-20s %s' % (label, dict(found[label])))

print('\n==== (2) THE CALLEES\' DEFS, ASKS, DATA KEYS ====')
PATS = ('Deut 5', 'Deuteronomy 5', 'Horeb', 'face to face', 'ten words', 'Decalogue', 'tablet', 'abbath', 'remember', 'Remember', 'keep', 'honor', 'murder', 'adulter',
        'steal', 'theft', 'witness', 'covet', 'desire', 'vain', 'other gods', 'graven', 'jealous', 'thousands', 'third and fourth', 'servant', 'your ox', 'stranger',
        'mediator', 'between the LORD', 'Memra', 'voice', 'thick darkness', 'added no more', 'two tablets', 'elders', 'heads', 'came near', 'we will hear', 'do and hear',
        'hear and do', 'done well', 'stand here', 'prolong', 'go well', 'turn aside', 'installed_by', 'given_at', 'covenant', 'this day', 'Exod 20', 'Exodus 20',
        '24:7', '24:3', '19:16', '19:17', '19:18', '19:19', '20:18', '20:19', '20:21', 'Shevuot', 'Kiddushin 3', 'Sanhedrin 86', 'Bava Metzia 5', 'Makkot 24', 'Yoma 4', 'Sotah 37', 'Shabbat 88', 'Berakhot 12', 'Sanhedrin 17')
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

print('\n==== (3) THE KINDS ON FILE touching the chapter\'s matter ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
print('  kinds %d, effects %d' % (len(E), len(F)))
KP = r'sabbath|murder|adulter|theft|steal|stolen|witness|covet|honor|parent|father|mother|oath|vain|name_|gods|image|idol|tablet|covenant|voice|fire|hear|request|elder|mediat|stand|command|statute|decalogue|ten_|declared|lashes|put_to_death|stoned|labor|rest_|sanctif|kidnap|blasphem|swear|sworn|false|horeb|sinai|thunder|descend|ascend|expound|speech|torah|bounds|feared|afraid|approach|near|charge'
for k in sorted(E):
    if re.search(KP, k):
        print('    %-44s form %-8s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:100].replace('\n', ' ')))
print('  effects touching the matter:')
for f in sorted(F):
    if re.search(KP, f):
        print('    %-40s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:110].replace('\n', ' ')))
print('  the ledger_op values: %s' % dict(collections.Counter(F[f].get('ledger_op') for f in F)))
for k in ('ten_words_declared', 'tablets_given', 'thunder_and_horn', 'lord_descended', 'moses_went_up', 'covenant_cut_at_sinai', 'covenant_blood_thrown', 'people_feared', 'people_stood_afar', 'moses_drew_near', 'speech_opened', 'add_nothing_commanded', 'witnesses_called', 'name_sworn_in_vain', 'sabbath_remembered', 'sabbath_labor', 'person_stolen', 'horeb_case', 'came_near_to_moses', 'spies_proposed'):
    if k in E: print('  a kind row whole (%s): %s' % (k, str(E.get(k))[:900]))
for f in ('covenant_declared', 'tablets_delivered', 'torah_expounded', 'adding_barred', 'heaven_and_earth_witness', 'lashes', 'sanctify_day', 'labor_barred', 'rest_required', 'put_to_death', 'accepted', 'exempt', 'commanded', 'covenant_upheld', 'covenant_accepted', 'obeyed', 'charged'):
    print('  an effect row (%s): %s' % (f, str(F.get(f))[:700] if f in F else 'ABSENT'))

print('\n==== (4) THE REGISTRY MAP for the chapter\'s tokens ====')
reg_map = CS.registry_map()
TOK = ('israel', 'israel_people', 'moses', 'the-elders', 'the-elders-of-israel', 'the-heads', 'the-heads-of-tribes', 'the-fathers', 'egypt', 'egypt_people', 'the-tablets', 'the-mountain', 'horeb', 'sinai', 'the-court', 'heaven', 'the-lord', 'the-fire', 'the-cloud', 'the-servant', 'the-stranger', 'the-ox', 'the-ass', 'the-household', 'the-swearer', 'the-kidnapper', 'aaron', 'joshua')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])
reg = yaml.safe_load(open(f'{ROOT}/logic/corpus/entity_registry.yaml', encoding='utf-8'))
print('  registry entities %d; ids matching elder|head|tribe|father|tablet|mountain|sinai|horeb|court|household|egypt|people|nation: %s' % (len(reg['entities']), [e['id'] for e in reg['entities'] if re.search(r'elder|head|tribe|father|tablet|mountain|sinai|horeb|court|household|egypt|people|nation', e['id'])]))

print('\n==== (5) THE TAPE\'S LINES the chapter retells; the tape\'s LAST lines and markers ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
tl = tape.split('\n')
for l in tl:
    if re.search(r"'Exod 19:|'Exod 20:|'Exod 24:[1-9]'|'Exod 24:1[0-8]|'Exod 31:1[6-8]|'Exod 32:1[5-9]|'Exod 34:2[7-9]|'Deut 1:2[0-9]|'Deut 1:3[0-9]|'Deut 3:2[3-9]|'Deut 4:|Exod 19:|Exod 20:1|Exod 24:3|Exod 24:7|Exod 24:8|Exod 31:18", l):
        print('   %s' % l.strip()[:230])
print('  --- the tape\'s last 12 lines:')
for l in [x for x in tl if x.strip()][-12:]:
    print('   %s' % l.strip()[:230])
print('  --- every marker row in the Deut section (verse, retrograde?, placement):')
deut = tape[tape.find('# ---- Deut 1'):] if '# ---- Deut 1' in tape else tape[-20000:]
for l in deut.split('\n'):
    if 'w.marker(' in l:
        m = re.search(r"w\.marker\('([^']+)', M\['([^']+)'\]", l)
        print('   %s  %s  retrograde=%s  placement=%s' % (m.group(1) if m else '?', m.group(2) if m else '?', 'retrograde' in l, re.search(r"placement='([a-z_]+)'", l).group(1) if re.search(r"placement='([a-z_]+)'", l) else 'text_constrained(default?)'))
print('  the section comments in the Deut stretch: %s' % re.findall(r'# ---- (Deut [^-]+?) ----', deut))
print('  DAEMON_ORDER %d, tail %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-3:]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s\n  SLOTS %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT, CS.SLOTS))

print('\n==== (6) THE CHECKPOINT PREFIXES, THE M[] NAMES, THE DAEMONS ====')
print('  cp() checkpoint prefixes in use: %s' % sorted(collections.Counter(re.findall(r"cp\('(C[A-Z])\d", src_cs)).items()))
used = set(re.findall(r"cp\('(C[A-Z])\d", src_cs)) | set(re.findall(r"'(C[A-Z])\d [A-Z]+'", src_cs))
free = [c for c in ['C' + x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'] if c not in used]
print('  FREE prefixes: %s' % free)
for cand in free[:6]:
    hits = []
    for f in glob.glob(f'{ROOT}/World/step9/*.py'):
        t = open(f, encoding='utf-8').read()
        n = len(re.findall(r"\b%s\d\b" % cand, t))
        if n: hits.append((f.split('/')[-1], n))
    print('    %s used as a label elsewhere: %s' % (cand, hits))
print('  M[] marker names on file: %s' % re.findall(r"M\['([a-z_0-9:]+)'\] = ", src_cs))
print('  the GLOBAL-COUNT checkpoints: %s' % [(i + 1, l.strip()[:150]) for i, l in enumerate(src_cs.split('\n')) if re.search(r"cp\('C[A-Z]\d", l) and re.search(r'len\(cmd_v\)|isr_cmd|len\(w\.entities\)|closes_done|len\(markers|pend|len\(CS\.DAEMON_ORDER\)|daemons\)|MARKER', l)][:40])
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  daemons %d; installed_by values: %s' % (len(dd['daemons']), dict(collections.Counter(str(v.get('installed_by')).split()[0] for v in dd['daemons'].values()))))
print('  the full law_decalogue block: %s' % dd['daemons'].get('law_decalogue'))
print('  the full law_obey_horeb block: %s' % dd['daemons'].get('law_obey_horeb'))
print('  the functions block decalogue: %s' % dd.get('functions', {}).get('decalogue'))
print('  the functions block obey_horeb: %s' % dd.get('functions', {}).get('obey_horeb'))
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers naming Deut 5: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if re.search(r'Deut 5:', str(p))][:10]))
print('  the obey_horeb edges on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], e.get('via'), str(e.get('why', ''))[:100]) for e in dep['edges'] if e['from'] == 'obey_horeb'])
print('  the obey_horeb pointers on file: %s' % [(p.get('verse'), p.get('form'), p.get('disposition'), str(p.get('why', ''))[:80]) for p in dep['pointers'] if p.get('runner') == 'obey_horeb'][:20])
print('  a CALL edge row WHOLE (obey_horeb): %s' % [e for e in dep['edges'] if e['from'] == 'obey_horeb' and e.get('disposition') == 'CALL'][:1])
print('  the OWED edges on file: %s' % [(e['from'], e['to'], str(e.get('why', ''))[:120]) for e in dep['edges'] if e.get('disposition') == 'OWED'])
print('  a RUN_CITATION pointer row WHOLE (obey_horeb): %s' % [p for p in dep['pointers'] if p.get('runner') == 'obey_horeb' and p.get('disposition') == 'RUN_CITATION'][:1])
print('  the spans: %s' % {k: dep['spans'].get(k) for k in ('decalogue', 'ordinances', 'mishpatim', 'mishpatim_3', 'sanctions', 'holiness', 'refuge', 'obey_horeb', 'opening_speech', 'erection', 'exodus_story', 'lev24', 'incense_shekel', 'pre_sinai')})
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the register seats naming Deut 5 / 4 (section, key, class, why): %s' % [(sec, k, v.get('class'), str(v.get('why', ''))[:100]) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.startswith('Deut 5') or k.startswith('Deut 4')])
print('  declared counts %d receipts %d footers %d registers %d' % tuple(len(decl.get(s, {})) for s in ('counts', 'receipts', 'footers', 'registers')))
cal = yaml.safe_load(open(f'{ROOT}/World/step9/calendar_parameters.yaml', encoding='utf-8'))
print('  sinai_days row: %s' % {k: cal.get('parameters', cal.get('rows', {})).get(k) for k in ('sinai_days',)})

print('\n==== (7) THE REGISTER GATE\'S CLASS RULES (its own code) ====')
rc = open(f'{ROOT}/World/step9/register_census.py', encoding='utf-8').read().split('\n')
for i, l in enumerate(rc):
    if re.search(r"'(ACT|CHAPTER|DAEMONS|NONE|CLOSE|RUN|EMPTY|SPEC)'|def classify|def receipt_class|def footer_class|receipts\b.*class|contains", l) and not l.strip().startswith('#'):
        print('   %4d: %s' % (i + 1, l.strip()[:200]))
print('  the receipt seats the gate scans (its regex or list): %s' % [l.strip()[:200] for l in rc if re.search(r"commanded|צוה|RECEIPT", l) and ('=' in l or 'def ' in l)][:12])
