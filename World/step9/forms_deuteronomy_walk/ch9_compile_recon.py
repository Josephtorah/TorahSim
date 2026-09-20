import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 7b — THE COMPILE OF CHAPTER 9, Deuteronomy 9:1-29 (2026-09-19; the owner: "Ok do ch 9"): THE RECONNAISSANCE before the
# design (ch8_compile_recon.py's form on chapter 9) — (1) WHICH RUNNER HOLDS A CELL FOR THE CHAPTER'S MATTER (the calf, the tablets, the forty days, the
# ascent, the second tablets, the finger of God, Aaron's peril, the stiff neck, Taberah, Massah, Kibroth-hattaavah, Kadesh-barnea, the intercession, the
# offer of a nation, the nations' taunt, the fathers' merit, righteousness, the Anakim, the consuming fire, the dust into the brook) — every runner's ink
# refs scanned by regex, per def; (2) the callee modules' defs, asks, DATA keys (the modules with hits on the kin); (3) the kinds and effects on file
# touching the matter; (4) the registry map; (5) the tape's lines the chapter retells (the ascent Exodus 24:12-18, the craftsmen 31:18, the calf 32,
# the second tablets 34; Massah 17:1-7; Taberah and Kibroth Numbers 11; the spies and the rejection 13-14; chapter 1's retelling) with THE CLOCK'S DAY at
# each (the snapshot world's log — the dates the answer sheet names: Ta'anit 4:6 the tablets broken on 17 Tammuz), the tape's LAST lines and markers;
# (6) the sequence file's tuples, the checkpoint prefixes in use and FREE, any code assuming a prefix's first letter, the M[] names, the daemons;
# (7) the dispositions and register seats naming Deut 9 (none expected — no receipt form), the readback probes' tail, the ledgers naming 9:20.
import sys, io, re, contextlib, inspect, collections, yaml, glob, subprocess, os, importlib
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')

print('==== (1) THE CHAPTER\'S MATTER — every runner\'s refs, per def ====')
SEATS = [(r'Deut(?:eronomy)? 9:(\d+)', 'Deut 9'), (r'Exod(?:us)? 32:\d+\b', 'Exod 32 (the calf)'), (r"ink\('32:\d", 'Exod 32 (ink)'), (r'Exod(?:us)? 24:1[2-8]\b', 'Exod 24:12-18 (the ascent)'), (r"ink\('24:1[2-8]'", 'Exod 24 (ink)'),
         (r'Exod(?:us)? 31:18\b', 'Exod 31:18 (the finger)'), (r'Exod(?:us)? 34:(?:[1-9]|2[89]|3[0-5])\b', 'Exod 34 (second tablets)'), (r"ink\('34:(?:[1-9]|2[89])'", 'Exod 34 (ink)'), (r'Exod(?:us)? 17:[1-7]\b', 'Exod 17:1-7 (Massah)'),
         (r'Num(?:bers)? 11:[1-3]\b', 'Num 11:1-3 (Taberah)'), (r'Num(?:bers)? 11:3[1-5]\b', 'Num 11:31-35 (Kibroth)'), (r'Num(?:bers)? 1[34]:\d+\b', 'Num 13-14 (the spies)'), (r'Deut(?:eronomy)? 1:(?:2[6-9]|3\d|4[0-6])\b', 'Deut 1:26-46 (the rejection retold)'),
         (r'Deut(?:eronomy)? 4:2[34]\b', 'Deut 4:23-24 (consuming fire)'), (r'Deut(?:eronomy)? 4:38\b', 'Deut 4:38 (nations greater)'), (r'Deut(?:eronomy)? 10:(?:[1-9]|1[01])\b', 'Deut 10:1-11 (the second tablets retold)'), (r'Deut(?:eronomy)? 31:27\b|Deut(?:eronomy)? 32:7\b', 'Deut 31:27 / 32:7'),
         (r'Exod(?:us)? 33:[3-5]\b|Exod(?:us)? 34:9\b', 'Exod 33:3-5, 34:9 (stiff-necked)'), (r'1 Kings 8:5[01]\b|Neh(?:emiah)? 1:10\b', 'Solomon / Nehemiah quoting'), (r'Ta\'?anit 4:6|Taanit 4:6|Ta\'?anit 28', "Ta'anit 4:6 / 28b"), (r'Shabbat 8[6-9][ab]', 'Shabbat 86-89'),
         (r'Berakhot 32a|Berakhot 7a', 'Berakhot 32a / 7a'), (r'Avodah Zarah 4[34][ab]|Avodah Zarah 3:3', 'Avodah Zarah 43b-44a / 3:3'), (r'Sanhedrin 102a|Vayikra Rabbah 10', 'Sanhedrin 102a (Aaron)'), (r'Menachot 99|Bava Batra 14b', 'the broken tablets in the ark'),
         (r'\bcalf\b|\bcalves\b', 'calf'), (r'\btablets?\b', 'tablets'), (r'stiff[- ]neck|hard of neck|stiffnecked', 'stiff-necked'), (r'forty days', 'forty days'), (r'\bAaron\b', 'Aaron'), (r'Taberah|Massah|Kibroth|Kadesh[- ]barnea', 'the four places'),
         (r'provok|rebell', 'provoke/rebel'), (r'let me alone|let me be|leave me', 'let Me alone'), (r'righteousness', 'righteousness'), (r'Anak', 'Anakim'), (r'consuming fire', 'consuming fire'), (r'not able|unable', 'not able'), (r'corrupt', 'corrupt'),
         (r'\bgrind|\bground\b|\bdust\b|\bbrook\b', 'grind/dust/brook'), (r'finger of God', 'finger of God'), (r'day of the assembly', 'day of the assembly'), (r'\bpray|intercede|intercession|entreat', 'pray/intercede'), (r'\brelent|repent(?:ed)? of the evil', 'relent'),
         (r'blot out|destroy them|destroy you|destroy him', 'blot out / destroy'), (r'great nation|mightier|more numerous', 'the offer'), (r'why should the Egyptians|lest the land say|slaughter(?:ed)? them|kill them', 'the taunt'), (r'remember Abraham|remember Your servants|merit of the fathers|zekhut', 'the fathers remembered'),
         (r'Your people and Your inheritance|Your inheritance', 'Your inheritance'), (r'mighty hand|outstretched arm|great power', 'mighty hand / arm'), (r'\bmolten\b', 'molten'), (r'seventeenth of Tammuz|17 Tammuz|Tammuz', 'Tammuz'), (r'Yom Kippur|Day of Atonement|10 Tishri|tenth of Tishri', 'Tishri 10'), (r'\bElul\b|\bAv\b', 'Elul / Av')]
HITS = collections.defaultdict(dict)
for f in sorted(glob.glob(f'{ROOT}/World/step9/cold_run_*.py')):
    name = os.path.basename(f)[9:-3]
    if name == 'sequence': continue
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
            print('     %-34s %s' % (label, dict(found[label])))
            HITS[name][label] = dict(found[label])
KIN_LABELS = ('Exod 32 (the calf)', 'Exod 24:12-18 (the ascent)', 'Exod 31:18 (the finger)', 'Exod 34 (second tablets)', 'Exod 17:1-7 (Massah)', 'Num 11:1-3 (Taberah)', 'Num 11:31-35 (Kibroth)', 'Num 13-14 (the spies)')
NAMES = sorted({n for n, d in HITS.items() if any(l in d for l in KIN_LABELS)} | {'opening_speech', 'obey_horeb', 'covenant_at_horeb', 'hear_o_israel', 'seven_nations', 'good_land', 'calendar', 'clocks', 'moadim'})
print('  THE KIN RUNNERS (a hit on Exodus 32 / 24:12-18 / 31:18 / 34 / 17:1-7 / Numbers 11 / 13-14) + the Deuteronomy runners + the clock runners: %s' % NAMES)
MODS = []
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    for n in NAMES:
        try: MODS.append((n, importlib.import_module('cold_run_' + n)))
        except Exception as e: print('IMPORT FAILED', n, e, file=sys.stderr)
print('  modules imported: %s' % [n for n, _ in MODS])

print('\n==== (2) THE CALLEES\' DEFS, ASKS, DATA KEYS ====')
PATS = ('Deut 9', 'Deuteronomy 9', 'calf', 'tablet', 'stiff', 'forty', 'Aaron', 'Taberah', 'Massah', 'Kibroth', 'Kadesh', 'provok', 'rebel', 'let me', 'righteous', 'Anak', 'consuming', 'not able', 'corrupt', 'grind', 'dust', 'brook', 'finger', 'assembly', 'pray', 'interce', 'relent',
        'blot', 'destroy', 'great nation', 'mightier', 'Egyptians say', 'remember Abraham', 'inheritance', 'mighty hand', 'molten', 'Tammuz', 'Tishri', 'Elul', "'32:", "'24:1", "'31:18", "'34:", "'17:", "'11:", "'13:", "'14:", 'installed_by', 'given_at', 'Ta\'anit', 'Taanit', 'Shabbat 8', 'Berakhot 32', 'Berakhot 7a', 'Avodah Zarah 4', 'Sanhedrin 102', 'Menachot 99', 'Bava Batra 14')
for name, mod in MODS:
    src = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    defs = re.findall(r'^def ([a-z_0-9]+)\(', src, re.M)
    print('==== %s: %d defs %s' % (name, len(defs), defs))
    for d in defs:
        i = src.find('\ndef %s(' % d); j = src.find('\ndef ', i + 1)
        body = src[i:j if j > 0 else None]
        asks = sorted(set(re.findall(r"ask'?\]?\s*==\s*'([a-z_0-9]+)'", body)) | set(re.findall(r"q == '([a-z_0-9]+)'", body)) | set(re.findall(r"ask'?\]?\s*in\s*\(([^)]*)\)", body)))
        kinds = sorted(set(re.findall(r"k == '([a-z_0-9]+)'", body)))
        if asks or kinds: print('   %-28s asks %s%s' % (d, asks[:90], ('  kinds ' + str(kinds[:60])) if kinds else ''))
    if hasattr(mod, 'DATA'): print('   DATA keys (%d): %s' % (len(mod.DATA), sorted(mod.DATA)[:80]))
    print('   imports: %s' % sorted(set(re.findall(r'^\s*import (cold_run_\w+)', src, re.M))))
    for pat in PATS:
        hits = [l.strip()[:170] for l in src.split('\n') if pat in l]
        if hits: print('   lines with %-18r: %d  e.g. %s' % (pat, len(hits), hits[:2]))

print('\n==== (3) THE KINDS ON FILE touching the chapter\'s matter ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
print('  kinds %d, effects %d' % (len(E), len(F)))
KP = r'calf|tablet|stiff|forty|aaron|taberah|massah|kibroth|quail|craving|spies|spy|reject|decree|interce|pray|relent|repent|anger|wrath|destroy|blot|nation|ascen|descen|fire|mountain|horeb|sinai|finger|assembly|grind|dust|brook|righteous|wicked|provok|rebel|hearken|redeem|inherit|fathers|abraham|servant|stubborn|hate|kill|wilderness|power|arm\b|corrupt|molten|image|idol|burn|fast|plead|offer|great_nation|word|covenant_cut|blood|second'
for k in sorted(E):
    if re.search(KP, k): print('    %-44s form %-8s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:100].replace('\n', ' ')))
print('  effects touching the matter:')
for f in sorted(F):
    if re.search(KP, f): print('    %-40s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:110].replace('\n', ' ')))
for k in [k for k in sorted(E) if re.search(r'calf|tablet|ascen|forty|finger|interce|pray|relent|taberah|massah|kibroth|quail|spies|decree|rebel|stiff|second_tablets|tablets_', k)][:40]:
    print('  a kind row whole (%s): %s' % (k, str(E.get(k))[:600]))
for f in [f for f in sorted(F) if re.search(r'calf|tablet|stiff|forty|aaron|interce|pray|relent|blot|destroy|nation|corrupt|molten|second', f)][:30]:
    print('  an effect row (%s): %s' % (f, str(F.get(f))[:400]))

print('\n==== (4) THE REGISTRY MAP for the chapter\'s tokens ====')
reg_map = CS.registry_map()
TOK = ('israel', 'israel_people', 'moses', 'aaron', 'the-calf', 'the-golden-calf', 'the-tablets', 'the-two-tablets', 'the-fathers', 'abraham', 'isaac', 'jacob', 'egypt', 'egypt_people', 'the-land', 'the-nations', 'the-anakim', 'anak', 'horeb', 'the-mountain', 'mount-sinai', 'the-brook', 'taberah', 'massah', 'kibroth-hattaavah', 'kadesh-barnea', 'the-wilderness', 'god', 'the-lord', 'the-people', 'the-covenant', 'the-ark')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])
print('  registry ids with calf/tablet/aaron/moses/israel/fathers in them: %s' % sorted({v for v in reg_map.values() if re.search(r'calf|tablet|aaron|moses|israel|father|abraham', str(v))})[:30])

print('\n==== (5) THE TAPE\'S LINES the chapter retells; THE CLOCK\'S DAY at each; the tape\'s LAST lines and markers ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
tl = tape.split('\n')
KINRE = r"'Exod 32:|'Exod 24:1[2-8]\b|'Exod 31:18|'Exod 34:(?:[1-9]|2[89]|3[0-5])\b|'Exod 33:|'Exod 17:[1-7]\b|'Num 11:(?:[1-3]|3[1-5])\b|'Num 1[34]:|'Deut 1:(?:2[6-9]|3\d|4[0-6])\b|'Deut 4:2[3-6]|'Deut 9:|'Deut 10:"
for l in tl:
    if re.search(KINRE, l): print('   %s' % l.strip()[:230])
print('  --- the tape\'s last 8 lines:')
for l in [x for x in tl if x.strip()][-8:]: print('   %s' % l.strip()[:230])
print('  --- every marker row in the Deut section:')
deut = tape[tape.find('# ---- Deut 1'):] if '# ---- Deut 1' in tape else tape[-20000:]
for l in deut.split('\n'):
    if 'w.marker(' in l:
        m = re.search(r"w\.marker\('([^']+)', M\['([^']+)'\]", l)
        print('   %s  %s  retrograde=%s  placement=%s' % (m.group(1) if m else '?', m.group(2) if m else '?', 'retrograde' in l, re.search(r"placement='([a-z_]+)'", l).group(1) if re.search(r"placement='([a-z_]+)'", l) else 'text_constrained'))
print('  the section comments in the Deut stretch: %s' % re.findall(r'# ---- (Deut [^-]+?) ----', deut))
print('  the Exod 24-34 section comments: %s' % [c for c in re.findall(r'# ---- (Exod [^-]+?) ----', tape) if re.search(r'Exod (?:2[4-9]|3[0-4])', c)])
print('  DAEMON_ORDER %d, tail %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-3:]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT))
print('  the Exod 24/31/32/33/34 and Exod 17, Num 11/13/14 lines with their kinds:')
for l in tl:
    m = re.search(r"w\.(?:event|write|marker|close)\('([a-z_0-9]+)'.*?'((?:Exod (?:17|24|31|32|33|34)|Num (?:11|13|14)):\d+(?:-\d+)?)'", l)
    if m: print('    %-34s %-14s %s' % (m.group(1), m.group(2), l.strip()[:150]))
# THE CLOCK'S DAY at the calf — the snapshot world's log
import register_census as RC
w = RC.running_world()
print('  the snapshot world: entities %d, log %d; clock %s day %s' % (len(w.entities), len(w.log), type(w.clock).__name__, getattr(w.clock, 'day', '?')))
print('  clock attrs: %s' % {k: (str(v)[:80]) for k, v in vars(w.clock).items() if not k.startswith('_')})
print('  clock methods: %s' % [m for m in dir(w.clock) if not m.startswith('_') and callable(getattr(w.clock, m))])
def render(day):
    for meth in ('ymd', 'date', 'render', 'calendar', 'to_date', 'as_date', 'label', 'describe'):
        if hasattr(w.clock, meth):
            try: return '%s=%s' % (meth, getattr(w.clock, meth)(day))
            except Exception as e: return '%s raised %r' % (meth, e)
    return '?'
print('  the calf-era log rows (EVENT/marker rows whose source is Exod 24:12-18, 31:18, 32, 33, 34:1-35; the day and its rendering):')
n = 0
for row in w.log:
    if not isinstance(row, (list, tuple)) or len(row) < 3: continue
    tag, day, ev = row[0], row[1], row[2]
    src = str(ev.get('source', ev.get('verse', ''))) if isinstance(ev, dict) else str(ev)
    if re.search(r'Exod (?:24:1[2-8]|31:18|32:|33:|34:)', src):
        print('    %-6s day %-6s %-32s %s | %s' % (tag, day, ev.get('kind', '?') if isinstance(ev, dict) else '?', src[:22], render(day)))
        n += 1
        if n > 40: break
print('  the marker rows on the log (all tags): %s' % collections.Counter(r[0] for r in w.log if isinstance(r, (list, tuple))).most_common(8))
print('  markers in the world (Exod 19-34): %s' % [(m if isinstance(m, str) else str(m)[:120]) for m in (getattr(w, 'markers', []) or [])][:0])
mk = [x for x in getattr(w, 'markers', []) if re.search(r'Exod (?:19|24|31|32|33|34)', str(x))] if hasattr(w, 'markers') else []
print('  the markers Exod 19-34: %s' % [str(x)[:160] for x in mk][:20])
print('  what a marker object looks like: %s' % (str(getattr(w, 'markers', ['?'])[0])[:300] if getattr(w, 'markers', None) else 'no w.markers'))

print('\n==== (6) THE CHECKPOINT PREFIXES, THE M[] NAMES, THE DAEMONS ====')
used = collections.Counter(re.findall(r"cp\('([A-Z]+)\d", src_cs))
print('  cp() checkpoint prefixes in use: %s' % sorted(used.items()))
free2 = [c for c in ['C' + x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'] if c not in used]
print('  FREE two-letter C-prefixes: %s' % free2)
print('  the VERDICTS list prefixes: %s' % sorted(collections.Counter(re.findall(r"'([A-Z]+)\d[a-z\-0-9]* (?:MATCH|DIVERGE)'", src_cs)).items()))
print('  code that assumes a checkpoint name\'s first letter (startswith/== on C):')
for f in sorted(glob.glob(f'{ROOT}/World/step9/*.py')):
    for i, l in enumerate(open(f, encoding='utf-8').read().split('\n')):
        if re.search(r"startswith\('C|== 'C'|\[0\] == 'C|'C\[|\[A-Z\]\{2\}|\[A-Z\]\+\\d|\[A-Z\]\\d", l) and re.search(r'cp|checkpoint|name|prefix|VERDICT', l):
            print('    %s:%d %s' % (os.path.basename(f), i + 1, l.strip()[:150]))
print('  M[] marker names on file: %s' % re.findall(r"M\['([a-z_0-9:]+)'\] = ", src_cs))
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  daemons %d; installed_by values: %s' % (len(dd['daemons']), dict(collections.Counter(str(v.get('installed_by')).split()[0] for v in dd['daemons'].values()))))
for dn in ('law_good_land', 'law_seven_nations', 'law_hear_o_israel'):
    print('  the daemon block %s: %s' % (dn, str(dd['daemons'].get(dn))[:500]))
print('  the functions block good_land: %s' % str(dd.get('functions', {}).get('good_land'))[:400])
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers naming Deut 9: %s; edges naming Deut 9: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if re.search(r'Deut 9:', str(p))][:10], [e for e in dep['edges'] if re.search(r'Deut 9:', str(e))][:5]))
print('  the good_land edges on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], str(e.get('why', ''))[:90]) for e in dep['edges'] if e['from'] == 'good_land'])
print('  a CALL edge row WHOLE (good_land): %s' % [e for e in dep['edges'] if e['from'] == 'good_land' and e.get('disposition') == 'CALL'][:1])
print('  a RUN_CITATION pointer row WHOLE (good_land): %s' % [p for p in dep['pointers'] if p.get('runner') == 'good_land'][:1])
print('  the spans of the kin: %s' % {k: dep['spans'].get(k) for k in NAMES})
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the register seats naming Deut 9: %s' % [(sec, k) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.startswith('Deut 9')])

print('\n==== (7) THE READBACK PROBES on file; the ledgers naming 9:20 ====')
rp = open(f'{ROOT}/World/step9/readback_probes.py', encoding='utf-8').read()
print('  readback_probes: the Q labels: %s' % sorted(set(re.findall(r"'(Q\d+)", rp)), key=lambda s: int(s[1:])))
print('  the Q19-Q21 heads: %s' % [l.strip()[:200] for l in rp.split('\n') if re.search(r"'Q(?:19|2[01])", l)][:6])
print('  the readback forms on THE_LOOP\'s step-6 row: %s' % [l.strip()[:220] for l in open(f'{ROOT}/World/step9/THE_LOOP.md', encoding='utf-8').read().split('\n') if 'FIFTH' in l or 'fifth form' in l.lower()][:3])
for f in sorted(glob.glob(f'{ROOT}/logic/oral_triage/*.md')):
    t = open(f, encoding='utf-8').read()
    n = len(re.findall(r'Deut(?:eronomy)? 9:20\b', t))
    if n: print('  ledger naming Deut 9:20: %s (%d)' % (os.path.basename(f), n))
print('  the calf runner\'s ledger(s): %s' % [os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_triage/*.md') if re.search(r'exo_3[24]|calf|kitisa|ki_tisa', os.path.basename(f))])
