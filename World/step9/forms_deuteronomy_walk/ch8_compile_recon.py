#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 6b — THE COMPILE OF CHAPTER 8, Deuteronomy 8:1-20 (2026-09-18; the owner: "Next" after sitting 6's close): THE
# RECONNAISSANCE before the design (ch7_compile_recon.py's form on chapter 8) — (1) WHICH RUNNER HOLDS A CELL FOR THE CHAPTER'S MATTER (the manna and
# the humbling, the forty years, the test, "not by bread alone", the garment and the foot, the discipline of a son, the good land and its waters, the
# seven species, iron and copper, eat-be satisfied-bless, take heed lest you forget, the houses and the herds and the silver and gold, the heart lifted
# up, the exodus formula, the serpents and the thirst, the rock of flint, "my power and the might of my hand", the covenant established, the testimony,
# other gods, perishing like the nations, the heel) — every runner's ink refs scanned by regex, per def; (2) the callee modules' defs, asks, DATA keys;
# (3) the kinds and effects on file touching the chapter's matter; (4) the registry map; (5) the tape's lines the chapter retells (the manna at Exodus
# 16, the rock at 17, the craving at Numbers 11, the forty years at 14, Meribah at 20, the serpents at 21, the exodus at 12:51, the oath's lines, the
# treasure at 19:5, 4:26's testimony, 6:10-12, 7:8 and 7:12) and the tape's LAST lines and markers; (6) the sequence file's tuples, the checkpoint
# prefixes FREE, the M[] names, the daemons; (7) the dispositions and register seats naming Deut 8 (none expected — no receipt form).
import sys, io, re, contextlib, inspect, collections, yaml, glob, subprocess, os, importlib
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
sys.path.insert(0, f'{ROOT}/World/step9')
NAMES = ['pre_sinai', 'exodus_story', 'beha', 'shelach', 'chukat', 'ordinances', 'opening_speech', 'obey_horeb', 'covenant_at_horeb', 'decalogue', 'hear_o_israel', 'seven_nations', 'sanctions', 'mamre', 'joseph']
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
SEATS = [(r'Deut(?:eronomy)? 8:(\d+)', 'Deut 8'), (r'Exod(?:us)? 16:\d+\b', 'Exod 16 (manna)'), (r"ink\('16:\d", 'Exod 16 (ink)'), (r'Exod(?:us)? 17:[1-7]\b', 'Exod 17:1-7 (the rock)'), (r"ink\('17:[1-7]'", 'Exod 17 (ink)'),
         (r'Num(?:bers)? 11:(?:[4-9]|3[1-5])\b', 'Num 11 (craving/quail)'), (r'Num(?:bers)? 14:3[34]\b', 'Num 14:33-34 (forty years)'), (r'Num(?:bers)? 20:(?:[1-9]|1[0-3])\b', 'Num 20:1-13 (Meribah)'), (r'Num(?:bers)? 21:[4-9]\b', 'Num 21:4-9 (serpents)'),
         (r'Exod(?:us)? 23:25\b', 'Exod 23:25 (bread/water blessed)'), (r'Exod(?:us)? 12:51\b|Deut(?:eronomy)? 5:6\b|Deut(?:eronomy)? 6:12\b|Deut(?:eronomy)? 13:(?:6|11)\b', 'the exodus formula'),
         (r'Deut(?:eronomy)? 4:2[56]\b|Deut(?:eronomy)? 30:1[89]\b', 'testify/perish 4:26'), (r'Deut(?:eronomy)? 4:1\b|Deut(?:eronomy)? 5:33\b|Deut(?:eronomy)? 30:16\b|Deut(?:eronomy)? 11:8\b', 'that you may live'),
         (r'Deut(?:eronomy)? 6:1[0-2]\b', 'Deut 6:10-12 (houses; forget)'), (r'Deut(?:eronomy)? 17:(?:1[67]|20)\b', 'the king\'s law 17:16-20'), (r'Deut(?:eronomy)? 1:(?:19|31)\b|Deut(?:eronomy)? 2:7\b', 'Deut 1:19, 1:31, 2:7'),
         (r'Deut(?:eronomy)? 29:4\b', 'Deut 29:4 (garments)'), (r'Deut(?:eronomy)? 11:1[0-7]\b', 'Deut 11:10-17 (the land)'), (r'Lev(?:iticus)? 18:5\b', 'Lev 18:5 (live by them)'), (r'Deut(?:eronomy)? 7:(?:8|12|13)\b', 'Deut 7:8/12 (oath, heel)'),
         (r'Deut(?:eronomy)? 32:1[0-5]\b', 'Deut 32:10-15 (Jeshurun)'), (r'Deut(?:eronomy)? 28:\d', 'Deut 28'), (r'Exod(?:us)? 19:[56]\b', 'Exod 19:5-6'), (r'Exod(?:us)? 15:2[2-6]\b', 'Marah 15:22-26'), (r'Neh(?:emiah)? 9:2[01]\b|Ps(?:alm)? 78:', 'Nehemiah 9 / Psalm 78'),
         (r'\bmanna\b|\bmon\b', 'manna'), (r'forty years', 'forty years'), (r'humbl|afflict', 'humble/afflict'), (r'\btest(?:ed|ing|s)?\b|\btried\b|\btrial', 'test'), (r'bread alone|not by bread|proceeds from the mouth', 'not by bread alone'),
         (r'garment|clothing|clothes|wore out|wear out|swell|swollen|shoes', 'garment/foot'), (r'disciplin|chastis|chasten', 'discipline'), (r'good land', 'good land'), (r'brooks|springs|deeps|fountains', 'waters'),
         (r'wheat|barley|\bvine|\bfig\b|pomegranate|olive|honey|seven species|seven kinds', 'the seven species'), (r'\biron\b|copper|brass|\bhew\b', 'iron/copper'), (r'satisfied|satiety|satiat|grace after|bless(?:ing)? after|birkat', 'satisfied/grace'),
         (r'\bforget|\bforgot|forgotten', 'forget'), (r'lifted up|haughty|arrogan|\bpride\b|\bproud', 'heart lifted'), (r'house of bondage|brought you out|brought out', 'exodus formula'), (r'serpent|scorpion|flint|\brock\b|thirst', 'serpents/rock/thirst'),
         (r'my power|might of my hand|wealth|riches', 'my power/wealth'), (r'establish(?:es|ed)? (?:his|the) covenant|covenant which he swore|covenant.{0,20}sw(?:ore|orn)', 'covenant established'), (r'testif|witness against', 'testify'), (r'\bperish|surely perish|destroy you', 'perish'),
         (r'other gods', 'other gods'), (r'hearken|voice of the LORD', 'hearken/voice'), (r'because you|\bheel\b|in consequence', 'because/heel'), (r'take heed|beware|guard yourself', 'take heed'), (r'silver and gold|herds and flocks|good houses', 'houses/herds/silver')]
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
            print('     %-28s %s' % (label, dict(found[label])))

print('\n==== (2) THE CALLEES\' DEFS, ASKS, DATA KEYS ====')
PATS = ('Deut 8', 'Deuteronomy 8', 'manna', 'forty', 'humble', 'afflict', 'test', 'bread', 'garment', 'clothes', 'discipline', 'good land', 'brook', 'wheat', 'honey', 'iron', 'satisf', 'bless', 'forget', 'lifted', 'bondage', 'brought', 'serpent', 'flint', 'rock', 'thirst', 'power', 'wealth', 'covenant', 'swore', 'sworn', 'testif', 'perish', 'other gods', 'hearken', 'heel',
        'Exod 16', "'16:", 'Exod 17', "'17:", 'Num 11', "'11:", 'Num 14', 'Num 20', "'20:", 'Num 21', "'21:", 'Exod 23:25', 'Deut 4:26', 'Deut 6:1', 'installed_by', 'given_at', 'Berakhot', 'Yoma 7', 'Sotah 4', 'Sotah 5', 'Makkot 13', 'Eruvin 96', 'Bikkurim', 'Mishnah Berakhot')
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
        if hits: print('   lines with %-18r: %d  e.g. %s' % (pat, len(hits), hits[:3]))

print('\n==== (3) THE KINDS ON FILE touching the chapter\'s matter ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
print('  kinds %d, effects %d' % (len(E), len(F)))
KP = r'manna|bread|hunger|humbl|afflict|test|forty|wilderness|garment|cloth|shoe|foot|disciplin|chast|brook|spring|water|wheat|barley|vine|fig|pomegranate|olive|honey|iron|copper|\beat|satisf|bless|forget|command|statute|judgment|house|herd|flock|silver|gold|multipl|heart|lift|proud|bondage|egypt|brought|serpent|scorpion|thirst|rock|flint|\bend|power|wealth|might|covenant|oath|sworn|swore|testif|witness|perish|destroy|gods|serve|bow|hearken|hear|obey|voice|nation|because|heel|live|life|quail|craving|meribah|massah|rebel'
for k in sorted(E):
    if re.search(KP, k):
        print('    %-44s form %-8s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:100].replace('\n', ' ')))
print('  effects touching the matter:')
for f in sorted(F):
    if re.search(KP, f):
        print('    %-40s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:110].replace('\n', ' ')))
for k in [k for k in sorted(E) if re.search(r'manna|quail|rock|water|serpent|forty|massah|meribah|craving|bread|brought_out|covenant_offered|shema_declared|testing_barred|hearing_blessed|nations_devoted|stand_here|ten_words|sworn_by|oath_upheld|visitation|blessing|garment|cloth', k)]:
    print('  a kind row whole (%s): %s' % (k, str(E.get(k))[:700]))
for f in ('commanded', 'blessing_commanded', 'grace_commanded', 'bless_commanded', 'forgetting_barred', 'other_gods_barred', 'shema_commanded', 'test_barred', 'blessings_for_hearing', 'covenant_barred', 'sustained', 'fed', 'manna_provided', 'manna_given', 'humbled', 'tested', 'perished', 'testified', 'warned', 'land_promised', 'sworn', 'blessed', 'water_given', 'healed', 'serpents_sent', 'bitten', 'died', 'forty_years_decreed', 'wandering_decreed', 'treasured_people', 'pity_barred', 'favor_barred', 'accepted', 'exempt', 'lashes'):
    print('  an effect row (%s): %s' % (f, str(F.get(f))[:500] if f in F else 'ABSENT'))

print('\n==== (4) THE REGISTRY MAP for the chapter\'s tokens ====')
reg_map = CS.registry_map()
TOK = ('israel', 'israel_people', 'moses', 'the-fathers', 'egypt', 'egypt_people', 'pharaoh', 'the-manna', 'manna', 'the-land', 'the-wilderness', 'the-rock', 'the-serpents', 'the-serpent', 'the-nations', 'the-heart', 'the-house', 'silver', 'gold', 'the-lord', 'god', 'the-son', 'the-man', 'the-garment', 'the-foot', 'the-flint', 'the-scorpion', 'the-mouth', 'the-bread', 'the-water', 'the-herds', 'the-flocks')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])

print('\n==== (5) THE TAPE\'S LINES the chapter retells; the tape\'s LAST lines and markers ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
tl = tape.split('\n')
for l in tl:
    if re.search(r"'Exod 16:|'Exod 17:[1-7]\b|'Num 11:(?:[4-9]|3[1-5])\b|'Num 14:(?:2[6-9]|3[0-9])\b|'Num 20:(?:[1-9]|1[0-3])\b|'Num 21:[4-9]\b|'Exod 12:51|'Exod 19:[56]\b|'Gen 22:1[5-8]|'Gen 26:[2-5]\b|'Gen 50:2[45]|'Deut 4:2[5-6]|'Deut 6:|'Deut 7:|'Deut 1:19|'Deut 1:3[01]|'Deut 2:7\b|'Exod 23:25|'Exod 15:2[2-7]|'Exod 32:|'Exod 13:1[7-9]", l):
        print('   %s' % l.strip()[:220])
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
print('  the exodus-era section comments: %s' % re.findall(r'# ---- (Exod [^-]+?) ----', tape)[:40])
print('  the Numbers-era section comments: %s' % re.findall(r'# ---- (Num [^-]+?) ----', tape)[:40])
print('  the Exod 16-17 and Num 11/14/20/21 lines with their kinds (the manna, the rock, the craving, the forty years, Meribah, the serpents):')
for l in tl:
    m = re.search(r"w\.(?:event|write|marker|close)\('([a-z_0-9]+)'.*?'((?:Exod 1[67]|Num (?:11|14|20|21)):\d+(?:-\d+)?)'", l)
    if m: print('    %-34s %-14s %s' % (m.group(1), m.group(2), l.strip()[:150]))

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
for dn in ('law_seven_nations', 'law_hear_o_israel', 'law_obey_horeb', 'law_ordinances', 'law_pre_sinai', 'law_chukat', 'law_exodus_story'):
    print('  the daemon block %s: %s' % (dn, str(dd['daemons'].get(dn))[:600]))
for fn in ('seven_nations', 'hear_o_israel', 'pre_sinai', 'exodus_story', 'chukat', 'beha', 'shelach'):
    print('  the functions block %s: %s' % (fn, str(dd.get('functions', {}).get(fn))[:500]))
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers naming Deut 8: %s; edges naming Deut 8: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if re.search(r'Deut 8:', str(p))][:10], [e for e in dep['edges'] if re.search(r'Deut 8:', str(e))][:5]))
print('  the seven_nations edges on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], str(e.get('why', ''))[:90]) for e in dep['edges'] if e['from'] == 'seven_nations'])
print('  a CALL edge row WHOLE (seven_nations): %s' % [e for e in dep['edges'] if e['from'] == 'seven_nations' and e.get('disposition') == 'CALL'][:1])
print('  a RUN_CITATION pointer row WHOLE (hear_o_israel): %s' % [p for p in dep['pointers'] if p.get('runner') == 'hear_o_israel' and p.get('disposition') == 'RUN_CITATION'][:1])
print('  an AS_WHEN pointer row WHOLE: %s' % [p for p in dep['pointers'] if p.get('form') == 'AS_WHEN'][:1])
print('  the OWED edges on file: %s' % [(e['from'], e['to'], str(e.get('why', ''))[:120]) for e in dep['edges'] if e.get('disposition') == 'OWED'])
print('  the FALSE edges on file: %s' % [(e['from'], e['to'], str(e.get('why', ''))[:100]) for e in dep['edges'] if str(e.get('disposition')) in ('FALSE', 'False')][:8])
print('  the spans: %s' % {k: dep['spans'].get(k) for k in NAMES})
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the register seats naming Deut 8 / 7 / 6: %s' % [(sec, k, v.get('class'), str(v.get('why', ''))[:80]) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.startswith('Deut 8') or k.startswith('Deut 7') or k.startswith('Deut 6')])
print('  declared counts %d receipts %d footers %d registers %d' % tuple(len(decl.get(s, {})) for s in ('counts', 'receipts', 'footers', 'registers')))

print('\n==== (7) THE REGISTER INDEX and the readback probes on file ====')
ri = open(f'{ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read()
print('  REGISTER_INDEX lines naming Deut 8 / 7: %s' % [l[:160] for l in ri.split('\n') if re.search(r'Deut 8:|Deut 7:', l)][:6])
rp = open(f'{ROOT}/World/step9/readback_probes.py', encoding='utf-8').read()
print('  readback_probes: the Q labels on file: %s; the tail line: %s' % (re.findall(r"^def (q\d+|Q\d+)|'(Q\d+)", rp, re.M)[:24], [l for l in rp.split('\n') if 'PROBES' in l or 'probes' in l][-2:]))
print('  the Q16-Q18 heads: %s' % [l.strip()[:160] for l in rp.split('\n') if re.search(r'Q1[6-8]', l)][:8])
