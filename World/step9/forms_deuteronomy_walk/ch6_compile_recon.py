import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 4b — THE COMPILE OF CHAPTER 6, Deuteronomy 6:1-25 (2026-09-17; the owner: "Go"): THE RECONNAISSANCE before the
# design (ch5_compile_recon.py's form on chapter 6) — (1) WHICH RUNNER HOLDS A CELL FOR THE CHAPTER'S MATTER (the Shema's duties, the tefillin's
# Exodus 13 seats, the son's question at Exodus 13:14 / 12:26, Massah at Exodus 17, the other gods and the jealous God at the second word, the
# oath by the Name, the fringes at Numbers 15) — every runner's ink refs scanned by regex, per def; (2) the callee modules' defs, asks, DATA keys;
# (3) the kinds and effects on file touching the chapter's matter; (4) the registry map; (5) the tape's lines the chapter retells (the exodus's
# signs and wonders, the going out, the oath to the fathers, Massah) and the tape's LAST lines and markers; (6) the sequence file's tuples, the
# checkpoint prefixes FREE, the M[] names, the daemons; (7) the dispositions and register seats naming Deut 6, and THE REGISTER GATE'S RECEIPT
# SCANNER from its own code (does it see "as He commanded us" at 6:25?).
import sys, io, re, contextlib, inspect, collections, yaml, glob, subprocess, os, importlib
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
NAMES = ['exodus_story', 'pre_sinai', 'decalogue', 'covenant_at_horeb', 'obey_horeb', 'opening_speech', 'holiness', 'shelach', 'erection', 'sanctions', 'mishpatim_3', 'ordinances']
MODS = []
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    for n in NAMES:
        try:
            MODS.append((n, importlib.import_module('cold_run_' + n)))
        except Exception as e:
            print('IMPORT FAILED', n, e, file=sys.stderr)
print('modules imported: %s' % [n for n, _ in MODS])

print('\n==== (1) THE CHAPTER\'S MATTER — every runner\'s refs, per def ====')
SEATS = [(r'Deut(?:eronomy)? 6:(\d+)', 'Deut 6'), (r'Deut(?:eronomy)? 11:1[3-9]\b|Deut(?:eronomy)? 11:2[01]\b', 'Deut 11:13-21'), (r'Deut(?:eronomy)? 10:20\b', 'Deut 10:20'),
         (r'Exod(?:us)? 13:(\d+)', 'Exod 13'), (r"ink\('13:(\d+)'", 'Exod 13 (ink)'), (r'Exod(?:us)? 12:2[67]\b', 'Exod 12:26-27'), (r'Exod(?:us)? 17:([1-7])\b', 'Exod 17:1-7'),
         (r'Num(?:bers)? 15:3[7-9]\b|Num(?:bers)? 15:4[01]\b', 'Num 15:37-41'), (r'Lev(?:iticus)? 19:12\b', 'Lev 19:12'), (r'Exod(?:us)? 20:[3-7]\b', 'Exod 20:3-7'),
         (r'[Tt]efillin|phylacter|frontlet|totafot', 'tefillin'), (r'[Mm]ezuz|doorpost', 'mezuzah'), (r'[Ss]hema\b|recit', 'shema/recite'), (r'[Ff]ringe|tzitzit', 'fringes'),
         (r'other gods|other_gods', 'other gods'), (r'jealous|visiting', 'jealous/visiting'), (r'[Mm]assah|tested|tempt', 'test/Massah'), (r'\bswear|\boath', 'swear/oath'),
         (r'right and .{0,6}good|the_right_and', 'right and good'), (r'son asks|your son|four sons|ask.{0,12}son', 'son asks'), (r'signs and wonders|strong hand|mighty hand', 'signs/strong hand'),
         (r'righteousness|tzedak', 'righteousness'), (r'sw(?:ore|orn) to .{0,12}fathers|oath to the fathers|promised.{0,12}fathers', 'sworn to fathers'),
         (r'love the LORD|all your heart|all your soul|all your might', 'love/heart'), (r'fear the LORD|fear_the|feared', 'fear'), (r'house of bondage|slaves? to Pharaoh|we were slaves', 'slaves'),
         (r'milk and honey', 'milk and honey'), (r'eat and be satisfied|be satisfied', 'satisfied'), (r'forget the LORD|lest you forget', 'forget')]
for f in sorted(glob.glob(f'{ROOT}/World/step9/cold_run_*.py')):
    name = os.path.basename(f)[9:-3]
    src = open(f, encoding='utf-8').read()
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
PATS = ('Deut 6', 'Deuteronomy 6', 'Shema', 'tefillin', 'mezuz', 'fringe', 'Massah', 'tested', 'swear', 'oath', 'other gods', 'jealous', 'wonders', 'strong hand', 'your son',
        'Exod 13', 'Exodus 13', "'13:9", "'13:16", "'13:14", "'13:8", "'12:26", "'17:7", "'17:2", 'swore', 'sworn', 'righteous', 'installed_by', 'given_at',
        'Berakhot', 'Menachot', 'Kiddushin 3', 'Pesachim 56', 'Pesachim 116', 'Sanhedrin 74', 'Sanhedrin 4b', 'Bava Metzia 108', 'Yoma 11', 'Shabbat 103', 'Temurah', 'Shevuot')
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
    print('   imports: %s' % sorted(set(re.findall(r'^\s*import (cold_run_\w+)', src, re.M))))
    for pat in PATS:
        hits = [l.strip()[:170] for l in src.split('\n') if pat in l]
        if hits: print('   lines with %-16r: %d  e.g. %s' % (pat, len(hits), hits[:3]))

print('\n==== (3) THE KINDS ON FILE touching the chapter\'s matter ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
print('  kinds %d, effects %d' % (len(E), len(F)))
KP = r'shema|recit|hear|love|heart|soul|might|teach|_son|sign|hand|frontlet|tefillin|write|doorpost|mezuz|gate|swear|sworn|oath|fear|serve|forget|gods|jealous|anger|destroy|test|massah|command|statute|testimon|judgment|right|enem|ask|slave|egypt|pharaoh|wonder|plague|brought|righteous|land|cities|house|cistern|vineyard|olive|eat|satisf|possess|swore|exodus|left|departed|firstborn|fringe|water|rock|quarrel|promise'
for k in sorted(E):
    if re.search(KP, k):
        print('    %-44s form %-8s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:100].replace('\n', ' ')))
print('  effects touching the matter:')
for f in sorted(F):
    if re.search(KP, f):
        print('    %-40s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:110].replace('\n', ' ')))
for k in ('ten_words_declared', 'people_answered', 'israel_went_out', 'exodus', 'plague_struck', 'firstborn_struck', 'water_from_the_rock', 'people_tested', 'massah_named', 'oath_sworn', 'land_sworn', 'speech_opened', 'mediator_requested', 'stand_here_commanded', 'firstborn_consecrated', 'passover_commanded', 'son_asks', 'fringes_commanded'):
    if k in E: print('  a kind row whole (%s): %s' % (k, str(E.get(k))[:700]))
for f in ('other_gods_barred', 'coveting_barred', 'torah_through_moses', 'commanded', 'put_to_death', 'exempt', 'accepted', 'obeyed', 'sworn', 'land_promised', 'feared', 'served'):
    print('  an effect row (%s): %s' % (f, str(F.get(f))[:500] if f in F else 'ABSENT'))

print('\n==== (4) THE REGISTRY MAP for the chapter\'s tokens ====')
reg_map = CS.registry_map()
TOK = ('israel', 'israel_people', 'moses', 'the-son', 'the-sons', 'the-fathers', 'abraham', 'isaac', 'jacob', 'egypt', 'egypt_people', 'pharaoh', 'the-house', 'the-gates', 'the-hand', 'the-eyes', 'the-doorposts', 'the-heart', 'the-land', 'the-cities', 'the-enemies', 'massah', 'the-peoples', 'the-nations')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])

print('\n==== (5) THE TAPE\'S LINES the chapter retells; the tape\'s LAST lines and markers ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
tl = tape.split('\n')
for l in tl:
    if re.search(r"'Exod (?:7|8|9|10|11|12|13|14):|'Exod 17:[1-7]\b|'Gen 22:1[5-8]|'Gen 26:[2-5]\b|'Gen 50:2[45]|'Exod 33:1\b|'Exod 3:(?:8|17)\b|'Deut 4:3[4-8]|'Deut 5:", l):
        print('   %s' % l.strip()[:200])
print('  --- the tape\'s last 10 lines:')
for l in [x for x in tl if x.strip()][-10:]:
    print('   %s' % l.strip()[:230])
print('  --- every marker row in the Deut section:')
deut = tape[tape.find('# ---- Deut 1'):] if '# ---- Deut 1' in tape else tape[-20000:]
for l in deut.split('\n'):
    if 'w.marker(' in l:
        m = re.search(r"w\.marker\('([^']+)', M\['([^']+)'\]", l)
        print('   %s  %s  retrograde=%s  placement=%s' % (m.group(1) if m else '?', m.group(2) if m else '?', 'retrograde' in l, re.search(r"placement='([a-z_]+)'", l).group(1) if re.search(r"placement='([a-z_]+)'", l) else 'text_constrained(default?)'))
print('  the section comments in the Deut stretch: %s' % re.findall(r'# ---- (Deut [^-]+?) ----', deut))
print('  DAEMON_ORDER %d, tail %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-3:]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT))
print('  the exodus-era section comments: %s' % re.findall(r'# ---- (Exod [^-]+?) ----', tape)[:30])

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
print('  the full law_covenant_at_horeb block: %s' % dd['daemons'].get('law_covenant_at_horeb'))
print('  the functions block covenant_at_horeb: %s' % dd.get('functions', {}).get('covenant_at_horeb'))
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers naming Deut 6: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if re.search(r'Deut 6:', str(p))][:10]))
print('  the covenant_at_horeb edges on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], str(e.get('why', ''))[:90]) for e in dep['edges'] if e['from'] == 'covenant_at_horeb'])
print('  a CALL edge row WHOLE (covenant_at_horeb): %s' % [e for e in dep['edges'] if e['from'] == 'covenant_at_horeb' and e.get('disposition') == 'CALL'][:1])
print('  a RUN_CITATION pointer row WHOLE (covenant_at_horeb): %s' % [p for p in dep['pointers'] if p.get('runner') == 'covenant_at_horeb' and p.get('disposition') == 'RUN_CITATION'][:1])
print('  the OWED edges on file: %s' % [(e['from'], e['to'], str(e.get('why', ''))[:120]) for e in dep['edges'] if e.get('disposition') == 'OWED'])
print('  the spans: %s' % {k: dep['spans'].get(k) for k in ('exodus_story', 'pre_sinai', 'decalogue', 'covenant_at_horeb', 'obey_horeb', 'opening_speech', 'holiness', 'shelach', 'erection', 'sanctions')})
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the register seats naming Deut 6 / 5 / 4:45: %s' % [(sec, k, v.get('class'), str(v.get('why', ''))[:80]) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.startswith('Deut 6') or k.startswith('Deut 5') or k.startswith('Deut 4:45')])
print('  declared counts %d receipts %d footers %d registers %d' % tuple(len(decl.get(s, {})) for s in ('counts', 'receipts', 'footers', 'registers')))

print('\n==== (7) THE REGISTER GATE\'S RECEIPT SCANNER (its own code) — does it see 6:25\'s "as He commanded us"? ====')
rc = open(f'{ROOT}/World/step9/register_census.py', encoding='utf-8').read()
for i, l in enumerate(rc.split('\n')):
    if re.search(r"commanded|צוה|RECEIPT|receipt", l) and not l.strip().startswith('#'):
        print('   %4d: %s' % (i + 1, l.strip()[:220]))
ri = open(f'{ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read()
print('  REGISTER_INDEX lines naming Deut 4:45 / 6: %s' % [l[:160] for l in ri.split('\n') if re.search(r'Deut 4:45|Deut 6:', l)][:6])
