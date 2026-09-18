import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 5b — THE COMPILE OF CHAPTER 7, Deuteronomy 7:1-26 (2026-09-18; the owner: "Go"): THE RECONNAISSANCE before the
# design (ch6_compile_recon.py's form on chapter 7) — (1) WHICH RUNNER HOLDS A CELL FOR THE CHAPTER'S MATTER (the seven nations and the ban, no
# covenant and no favor, the marriage, the altars and the Asherim, the chosen people and the treasure, the oath to the fathers, the faithful God and
# the thousand generations, the blessings and the diseases of Egypt, no pity and the snare, the fear, the trials and the signs, the hornet, little by
# little, the kings and the name, the images' silver and gold and the coveting, the abomination and the devoted thing) — every runner's ink refs
# scanned by regex, per def; (2) the callee modules' defs, asks, DATA keys; (3) the kinds and effects on file touching the chapter's matter; (4) the
# registry map; (5) the tape's lines the chapter retells (the angel's clauses at Exodus 23, the renewed covenant at 34, the dispossession at Numbers 33,
# the plagues and the sea, the oath to the fathers, the treasure at 19:5, Amalek's name) and the tape's LAST lines and markers; (6) the sequence file's
# tuples, the checkpoint prefixes FREE, the M[] names, the daemons; (7) the dispositions and register seats naming Deut 7 (none expected — no receipt form).
import sys, io, re, contextlib, inspect, collections, yaml, glob, subprocess, os, importlib
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
NAMES = ['ordinances', 'erection', 'journeys', 'decalogue', 'covenant_at_horeb', 'exodus_story', 'obey_horeb', 'hear_o_israel', 'opening_speech', 'shemini', 'balak', 'mamre', 'joseph']
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
SEATS = [(r'Deut(?:eronomy)? 7:(\d+)', 'Deut 7'), (r'Exod(?:us)? 23:(?:2\d|3[0-3])\b', 'Exod 23:20-33'), (r"ink\('23:(?:2\d|3[0-3])'", 'Exod 23 (ink)'),
         (r'Exod(?:us)? 34:1[0-6]\b', 'Exod 34:10-16'), (r"ink\('34:1[0-6]'", 'Exod 34 (ink)'), (r'Num(?:bers)? 33:5[0-6]\b', 'Num 33:50-56'),
         (r'Exod(?:us)? 20:17\b|Deut(?:eronomy)? 5:21\b', 'covet 20:17/5:21'), (r'Exod(?:us)? 20:[3-6]\b|Deut(?:eronomy)? 5:(?:[7-9]|10)\b', 'other gods 20:3-6'),
         (r'Deut(?:eronomy)? 20:1[0-8]\b', 'Deut 20:10-18'), (r'Deut(?:eronomy)? 12:[23]\b', 'Deut 12:2-3'), (r'Deut(?:eronomy)? 13:\d', 'Deut 13'),
         (r'Exod(?:us)? 19:[56]\b', 'Exod 19:5-6'), (r'Exod(?:us)? 15:26\b|Exod(?:us)? 23:2[56]\b', 'diseases/barren'), (r'Exod(?:us)? 17:1[4-6]\b|Deut(?:eronomy)? 25:1[7-9]\b', 'Amalek'),
         (r'Josh(?:ua)? 24:1[12]\b|Josh(?:ua)? 1:5\b|Josh(?:ua)? 7:\d', 'Joshua'), (r'Lev(?:iticus)? 11:4[1-3]\b|Lev(?:iticus)? 20:2[35]\b', 'Lev 11 detest'),
         (r'Deut(?:eronomy)? 14:2\b|Deut(?:eronomy)? 26:1[89]\b', 'holy people'), (r'Deut(?:eronomy)? 4:3[4-8]\b|Deut(?:eronomy)? 10:1[5-7]\b', 'chose/trials'),
         (r'Deut(?:eronomy)? 28:\d', 'Deut 28'), (r'Num(?:bers)? 25:\d', 'Baal Peor'),
         (r'[Hh]ornet', 'hornet'), (r'[Cc]herem|devoted|\bban\b|utterly destroy|annihilat', 'cherem/ban'), (r'covenant with them|no covenant|make a covenant|cut a covenant|treaty', 'no covenant'),
         (r'show them favor|no favor|mercy on them', 'favor'), (r'intermarr|son-in-law|marry|marriage|their daughters|his daughter', 'marriage'),
         (r'[Aa]sher(?:ah|im)|pillar|tear down|graven|image', 'altars/asherim/images'), (r'treasure|segull|holy people|chose you|chosen people', 'treasure/chosen'),
         (r'thousand generations|to thousands|those who hate', 'thousand/haters'), (r'faithful God|keeps the covenant', 'faithful'), (r'barren|miscarr', 'barren'),
         (r'diseases? of Egypt|sickness|plague', 'diseases'), (r'\bsnare|stumbling', 'snare'), (r'\bpity|spare them', 'pity'), (r'little by little|beasts of the field|in one year', 'little by little'),
         (r'no man shall stand|their name|from under heaven|blot out', 'name from under heaven'), (r'covet|silver and gold', 'covet/silver and gold'), (r'abomination|detest|abhor', 'abomination'),
         (r'\bfear\b|afraid|terrified|dread', 'fear'), (r'signs and wonders|strong hand|outstretched arm|\btrials', 'signs/wonders/trials'), (r'sw(?:ore|orn) to .{0,12}fathers|oath to the fathers|the oath\b', 'sworn to fathers'),
         (r'seven nations|Hittite|Girgashite|Amorite|Canaanite|Perizzite|Hivite|Jebusite|six nations', 'the nations'), (r'dispossess|drive out|cast out|clear away|drive them', 'dispossess')]
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
            print('     %-24s %s' % (label, dict(found[label])))

print('\n==== (2) THE CALLEES\' DEFS, ASKS, DATA KEYS ====')
PATS = ('Deut 7', 'Deuteronomy 7', 'hornet', 'cherem', 'devoted', 'covenant with', 'intermarr', 'daughter', 'Asher', 'pillar', 'altar', 'graven', 'treasure', 'chose', 'thousand',
        'hate', 'faithful', 'barren', 'disease', 'snare', 'pity', 'little by little', 'beasts', 'covet', 'silver and gold', 'abomination', 'detest', 'fear', 'wonders', 'strong hand',
        'swore', 'sworn', 'Exod 23', "'23:2", "'23:3", 'Exod 34', "'34:1", 'Num 33', "'33:5", 'installed_by', 'given_at', 'Avodah Zarah', 'Kiddushin 68', 'Yevamot 23', 'Sotah 36',
        'Chullin 89', 'Makkot 22', 'Sanhedrin 56', 'Mishnah Avodah', 'Mishnah Kiddushin')
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
KP = r'nation|cherem|\bban|devot|covenant|favor|marr|daughter|altar|pillar|asher|image|idol|treasur|chose|chosen|holy|love|oath|sworn|swore|faithful|thousand|hate|repay|command|statute|judgment|hear|obey|bless|fruit|womb|grain|wine|oil|cattle|flock|barren|disease|sick|plague|consume|eat|pity|serve|gods|snare|fear|afraid|remember|pharaoh|egypt|trial|sign|wonder|hand|arm|hornet|remain|hide|midst|awesome|little|beast|field|confus|king|name|heaven|stand|burn|fire|covet|silver|gold|abomin|detest|abhor|house|dispossess|drive|angel|escort|land|inherit|destroy|amalek|blot'
for k in sorted(E):
    if re.search(KP, k):
        print('    %-44s form %-8s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:100].replace('\n', ' ')))
print('  effects touching the matter:')
for f in sorted(F):
    if re.search(KP, f):
        print('    %-40s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:110].replace('\n', ' ')))
for k in ('angel_sent', 'angel_promised', 'hornet_promised', 'hornet_sent', 'little_by_little', 'nations_driven', 'covenant_renewed', 'covenant_barred', 'dispossession_commanded', 'ten_words_declared', 'plague_struck', 'sea_split', 'brought_out', 'sworn_by_himself', 'oath_upheld', 'visitation_promised', 'treasure_promised', 'treasured', 'chosen', 'shema_declared', 'testing_barred', 'amalek_blotted', 'amalek_war', 'diseases_removed', 'healer_promised', 'idols_destroyed', 'altars_torn', 'stand_here_commanded'):
    if k in E: print('  a kind row whole (%s): %s' % (k, str(E.get(k))[:700]))
for f in ('other_gods_barred', 'coveting_barred', 'commanded', 'sworn', 'land_promised', 'feared', 'served', 'covenant_barred', 'idols_destroyed', 'hornet_sent', 'angel_sent', 'treasured', 'chosen', 'blessed', 'dispossessed', 'devoted', 'banned', 'shema_commanded', 'test_barred', 'images_barred', 'image_barred'):
    print('  an effect row (%s): %s' % (f, str(F.get(f))[:500] if f in F else 'ABSENT'))

print('\n==== (4) THE REGISTRY MAP for the chapter\'s tokens ====')
reg_map = CS.registry_map()
TOK = ('israel', 'israel_people', 'moses', 'the-nations', 'the-peoples', 'the-hittite', 'the-girgashite', 'the-amorite', 'the-canaanite', 'the-perizzite', 'the-hivite', 'the-jebusite', 'the-fathers', 'egypt', 'egypt_people', 'pharaoh', 'the-hornet', 'the-kings', 'the-land', 'the-house', 'the-son', 'the-daughter', 'the-altars', 'the-images', 'silver', 'gold', 'the-beasts', 'amalek')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])

print('\n==== (5) THE TAPE\'S LINES the chapter retells; the tape\'s LAST lines and markers ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
tl = tape.split('\n')
for l in tl:
    if re.search(r"'Exod (?:7|8|9|10|11|12|14):|'Exod 23:(?:2\d|3[0-3])\b|'Exod 34:1[0-6]\b|'Num 33:5[0-6]\b|'Gen 22:1[5-8]|'Gen 26:[2-5]\b|'Gen 50:2[45]|'Exod 19:[56]\b|'Exod 17:1[4-6]\b|'Exod 15:26\b|'Deut 4:3[4-8]|'Deut 6:|'Exod 3:(?:8|17)\b|'Num 25:|'Exod 33:2\b|'Exod 32:1[0-4]", l):
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
for dn in ('law_hear_o_israel', 'law_ordinances', 'law_erection', 'law_journeys', 'law_covenant_at_horeb'):
    print('  the daemon block %s: %s' % (dn, str(dd['daemons'].get(dn))[:600]))
for fn in ('hear_o_israel', 'ordinances', 'erection', 'journeys'):
    print('  the functions block %s: %s' % (fn, str(dd.get('functions', {}).get(fn))[:500]))
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers naming Deut 7: %s; edges naming Deut 7: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if re.search(r'Deut 7:', str(p))][:10], [e for e in dep['edges'] if re.search(r'Deut 7:', str(e))][:5]))
print('  the hear_o_israel edges on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], str(e.get('why', ''))[:90]) for e in dep['edges'] if e['from'] == 'hear_o_israel'])
print('  a CALL edge row WHOLE (hear_o_israel): %s' % [e for e in dep['edges'] if e['from'] == 'hear_o_israel' and e.get('disposition') == 'CALL'][:1])
print('  a RUN_CITATION pointer row WHOLE (hear_o_israel): %s' % [p for p in dep['pointers'] if p.get('runner') == 'hear_o_israel' and p.get('disposition') == 'RUN_CITATION'][:1])
print('  an AS_WHEN pointer row WHOLE: %s' % [p for p in dep['pointers'] if p.get('form') == 'AS_WHEN'][:1])
print('  the OWED edges on file: %s' % [(e['from'], e['to'], str(e.get('why', ''))[:120]) for e in dep['edges'] if e.get('disposition') == 'OWED'])
print('  the FALSE edges on file: %s' % [(e['from'], e['to'], str(e.get('why', ''))[:100]) for e in dep['edges'] if str(e.get('disposition')) in ('FALSE', 'False')][:8])
print('  the spans: %s' % {k: dep['spans'].get(k) for k in NAMES})
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the register seats naming Deut 7 / 6 / 5: %s' % [(sec, k, v.get('class'), str(v.get('why', ''))[:80]) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.startswith('Deut 7') or k.startswith('Deut 6') or k.startswith('Deut 5')])
print('  declared counts %d receipts %d footers %d registers %d' % tuple(len(decl.get(s, {})) for s in ('counts', 'receipts', 'footers', 'registers')))

print('\n==== (7) THE REGISTER INDEX and the readback probes on file ====')
ri = open(f'{ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read()
print('  REGISTER_INDEX lines naming Deut 7 / 6: %s' % [l[:160] for l in ri.split('\n') if re.search(r'Deut 7:|Deut 6:', l)][:6])
rp = open(f'{ROOT}/World/step9/readback_probes.py', encoding='utf-8').read()
print('  readback_probes: the Q labels on file: %s; the tail line: %s' % (re.findall(r"^def (q\d+|Q\d+)|'(Q\d+)", rp, re.M)[:20], [l for l in rp.split('\n') if 'PROBES' in l or 'probes' in l][-2:]))
print('  the Q13-Q15 heads: %s' % [l.strip()[:160] for l in rp.split('\n') if re.search(r'Q1[3-5]', l)][:8])
