#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 8b — THE COMPILE OF CHAPTER 10, Deuteronomy 10:1-22 (2026-09-20; the owner: "Go" after the reread that followed sitting 8's
# compaction): THE RECONNAISSANCE before the design (ch9_compile_recon.py's form on chapter 10, derived by derive_ch10_recon.py) — (1) WHICH RUNNER HOLDS A
# CELL FOR THE CHAPTER'S MATTER (the second tablets, the ark and the fragments, the testimony placed, the stations and Aaron's death, the Levites' three
# offices and their portion, the third forty and the command to go, the demand's five infinitives, the attributes and the face not lifted, the bribe, the
# stranger, the heart's foreskin, the seventy and the stars, the oath to the fathers, the praise) — every runner's ink refs scanned by regex, per def;
# (2) the callee modules' defs, asks, DATA keys (the modules with hits on the kin); (3) the kinds and effects on file touching the matter; (4) the
# registry map; (5) the tape's lines the chapter retells (the second tablets Exodus 34:1-4, 28-29; the ark 25:10-22, 37:1-9, 40:20-21; the finger 31:18;
# the Levites Exodus 32:26-29, Numbers 3, 4, 8, 18; the blessing Numbers 6:23-27; the stations Numbers 33:30-39; Aaron's death 20:22-29; the go Exodus
# 32:34, 33:1; the stranger Exodus 22:20-23, 23:8-9, Leviticus 19:33-34; the seventy Genesis 46:27, Exodus 1:5) with THE CLOCK'S DAY at each (the snapshot
# world's log — the third forty's end 10 Tishri, the second tablets' day; Aaron's death the fortieth year's fifth month), the tape's LAST lines and markers;
# (6) the sequence file's tuples, the checkpoint prefixes in use (the D series — DA the open series, the next DB), the M[] names and the forties' markers,
# the daemons; (7) the dispositions and register seats naming Deut 10 (10:5 and 10:22 declared NONE — the receipt and the count), the readback probes'
# tail, the ledgers naming 10:6 or Moserah, the ark's, the journeys' and the Levites' ledgers.
import sys, io, re, contextlib, inspect, collections, yaml, glob, subprocess, os, importlib
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()   # RUN FROM THE REPO ROOT; no absolute repo path typed
sys.path.insert(0, f'{ROOT}/World/step9')

print('==== (1) THE CHAPTER\'S MATTER — every runner\'s refs, per def ====')
SEATS = [(r'Deut(?:eronomy)? 10:(\d+)', 'Deut 10'), (r'Exod(?:us)? 34:(?:[1-4]|2[89])\b', 'Exod 34:1-4, 28-29 (second tablets)'), (r"ink\('34:(?:[1-4]|2[89])'", 'Exod 34 (ink)'), (r'Exod(?:us)? 25:(?:1\d|2[0-2])\b', 'Exod 25:10-22 (the ark)'), (r"ink\('25:(?:1\d|2[0-2])'", 'Exod 25 (ink)'),
         (r'Exod(?:us)? 37:[1-9]\b', 'Exod 37:1-9 (the ark made)'), (r'Exod(?:us)? 40:(?:3|2[01])\b', 'Exod 40:3, 20-21 (the testimony in the ark)'), (r'Exod(?:us)? 31:18\b', 'Exod 31:18 (the finger)'), (r'Exod(?:us)? 24:12\b', 'Exod 24:12 (come up to Me)'), (r'Exod(?:us)? 32:(?:2[6-9]|34)\b|Exod(?:us)? 33:1\b', 'Exod 32:26-29, 32:34, 33:1 (the Levites; go)'),
         (r'Num(?:bers)? 33:3\d\b', 'Num 33:30-39 (the stations, Hor)'), (r'Num(?:bers)? 20:2[2-9]\b', 'Num 20:22-29 (Aaron at Hor)'), (r'Num(?:bers)? 3:(?:[5-9]|1[0-3]|4\d|5[01])\b', 'Num 3 (the Levites taken)'), (r'Num(?:bers)? 4:\d+\b', 'Num 4 (to carry)'), (r'Num(?:bers)? 8:(?:[5-9]|1\d|2[0-6])\b', 'Num 8:5-26 (the Levites cleansed)'),
         (r'Num(?:bers)? 18:(?:[12]|2[0-4])\b', 'Num 18:1-2, 20-24 (the dues, no portion)'), (r'Num(?:bers)? 6:2[3-7]\b', 'Num 6:23-27 (the blessing)'), (r'Deut(?:eronomy)? 4:(?:5|13)\b', 'Deut 4:5 / 4:13'), (r'Deut(?:eronomy)? 6:(?:5|13)\b', 'Deut 6:5 / 6:13'), (r'Exod(?:us)? 22:2[0-3]\b|Exod(?:us)? 23:[89]\b', 'Exod 22:20-23, 23:8-9 (the stranger, the bribe)'),
         (r'Lev(?:iticus)? 19:3[34]\b', 'Lev 19:33-34 (the stranger)'), (r'Lev(?:iticus)? 26:41\b|Deut(?:eronomy)? 30:6\b|Jer(?:emiah)? 4:4\b', "Lev 26:41 / Deut 30:6 / Jer 4:4 (the heart's foreskin)"), (r'Gen(?:esis)? 46:27\b|Exod(?:us)? 1:5\b', 'Gen 46:27 / Exod 1:5 (the seventy)'), (r'Deut(?:eronomy)? 1:10\b|Deut(?:eronomy)? 28:62\b', 'Deut 1:10 / 28:62 (the stars)'),
         (r'Deut(?:eronomy)? 16:19\b|Deut(?:eronomy)? 27:25\b', 'Deut 16:19 / 27:25 (the bribe)'), (r'Deut(?:eronomy)? 31:(?:7|9|2[56])\b|Josh(?:ua)? 1:6\b', 'Deut 31:7, 9, 25-26 / Josh 1:6'), (r'1 Kings 8:(?:9|27)\b|Neh(?:emiah)? 9:6\b|Ps(?:alm)? 136:[23]\b', '1 Kings 8:9, 27 / Neh 9:6 / Ps 136:2-3'),
         (r'Bava Batra 14|Menachot 99|Berakhot 8b|Shekalim 6', 'the two arks / the ark hidden'), (r'Berakhot 33b|Menachot 43b|Shabbat 31b|Sotah 14a', 'the demand and the attributes'), (r'Yoma 69b|Megillah 25a|Berakhot 20b|Niddah 70b', 'the attributes / lifting the face'),
         (r"Ketubot 105|Bava Metzia 59b|Yevamot 47|Ketubot 111b|Shevuot 35b|Temurah 3b|Sanhedrin 56a|Bava Batra 123|Rosh Hashanah 3a|Ta'?anit 9a|Seder Olam", "the docket's other works"),
         (r'\bark\b', 'ark'), (r'\btablets?\b', 'tablets'), (r'\bhew\b|\bhewn\b', 'hew'), (r'\bacacia\b|shittim', 'acacia'), (r'\bLevites?\b|\bLevi\b', 'Levi(tes)'), (r'\bminister', 'minister'), (r'\binheritance\b|\bportion\b', 'inheritance/portion'), (r'\bAaron\b', 'Aaron'), (r'\bburied\b|\bburial\b', 'buried'),
         (r'Moserah|Moseroth|Bene-jaakan|Jaakan|Gudgod|Hor-haggidgad|Jotbathah|Mount Hor|Eleazar', 'the stations / Hor / Eleazar'), (r'forty days', 'forty days'), (r'\bcleave\b|\bcling\b', 'cleave'), (r'\bswear\b|\bsworn\b|\boath\b', 'swear/oath'), (r'circumcis', 'circumcise'), (r'foreskin', 'foreskin'), (r'stiff[- ]neck|stiffnecked|hard of neck', 'stiff-necked'),
         (r'God of gods|Lord of lords|mighty and (?:the )?awesome|awesome God|great God', 'the attributes'), (r'lift(?:s|eth)? (?:up )?(?:His |his |the )?(?:face|countenance)|regard(?:s|eth)? (?:not )?persons|no face|partial', 'lifting the face'), (r'\bbribe\b', 'bribe'), (r'\borphan\b|fatherless|\bwidow\b', 'orphan/widow'), (r'\bstranger\b|\bsojourner\b|\bconvert\b|\bproselyte\b', 'stranger'),
         (r'\bseventy\b|\b70\b', 'seventy'), (r'stars of (?:the )?heaven|as the stars', 'the stars'), (r'\bpraise\b', 'praise'), (r'heaven of heavens|highest heavens', 'heaven of heavens'), (r'you shall love|shall love', 'you shall love'), (r'what does the LORD|what the LORD .{0,20}(?:ask|require)', 'what does the LORD ask'), (r'Tishri|Yom Kippur|Day of Atonement', 'Tishri 10'), (r'\bElul\b|\bAv\b', 'Elul / Av')]
KIN_LABELS = ('Exod 34:1-4, 28-29 (second tablets)', 'Exod 25:10-22 (the ark)', 'Exod 37:1-9 (the ark made)', 'Exod 40:3, 20-21 (the testimony in the ark)', 'Exod 31:18 (the finger)', 'Exod 32:26-29, 32:34, 33:1 (the Levites; go)', 'Num 33:30-39 (the stations, Hor)', 'Num 20:22-29 (Aaron at Hor)', 'Num 3 (the Levites taken)', 'Num 4 (to carry)', 'Num 8:5-26 (the Levites cleansed)', 'Num 18:1-2, 20-24 (the dues, no portion)', 'Num 6:23-27 (the blessing)', 'Exod 22:20-23, 23:8-9 (the stranger, the bribe)', 'Lev 19:33-34 (the stranger)', 'Gen 46:27 / Exod 1:5 (the seventy)')
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
        print('  -- %s: %s' % (name, {label: sum(found[label].values()) for label in found}))
        for label in found:
            HITS[name][label] = dict(found[label])
            if label in KIN_LABELS or label == 'Deut 10': print('     %-34s %s' % (label, dict(found[label])))
NAMES = sorted({n for n, d in HITS.items() if any(l in d for l in KIN_LABELS)} | {'opening_speech', 'obey_horeb', 'covenant_at_horeb', 'hear_o_israel', 'seven_nations', 'good_land', 'not_righteousness', 'erection', 'sanctuary_build', 'journeys', 'chukat', 'bamidbar', 'beha', 'korach', 'naso', 'joseph', 'exodus_story', 'ordinances', 'mishpatim', 'holiness', 'calendar', 'clocks', 'moadim'})
print('  THE KIN RUNNERS (a hit on a kin label) + the Deuteronomy runners + the kin named by the box + the clock runners: %s' % NAMES)
MODS = []
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    for n in NAMES:
        try: MODS.append((n, importlib.import_module('cold_run_' + n)))
        except Exception as e: print('IMPORT FAILED', n, e, file=sys.stderr)
print('  modules imported: %s' % [n for n, _ in MODS])

print('\n==== (2) THE CALLEES\' DEFS, ASKS, DATA KEYS ====')
BROAD = ('bless', 'inheritance', 'portion', 'Aaron', 'forty', 'face', 'serve', 'stiff', 'swear', 'awesome', 'stars', 'praise', 'walk in', 'fear the LORD', 'shall love', "'3:", "'4:", "'8:", "'18:", "'6:2", "'34:", "'1:5", "'33:1", "'20:2", "'22:2", "'19:3", 'installed_by', 'given_at', 'Eleazar', 'buried')
PATS = ('Deut 10', 'Deuteronomy 10', 'ark', 'tablet', 'hew', 'acacia', 'Levi', 'minister', 'bless', 'inheritance', 'portion', 'Aaron', 'buried', 'Moserah', 'Mount Hor', 'Jaakan', 'Eleazar', 'forty', 'cleave', 'swear', 'circumcis', 'foreskin', 'stiff', 'God of gods', 'awesome', 'face', 'bribe', 'orphan', 'widow', 'stranger', 'seventy', 'stars', 'praise', 'heaven of heavens', 'shall love', 'fear the LORD', 'walk in', 'serve', "'34:", "'25:1", "'37:", "'40:2", "'31:18", "'32:2", "'33:1", "'33:3", "'20:2", "'3:", "'4:", "'8:", "'18:", "'6:2", "'46:27", "'1:5", "'22:2", "'23:8", "'23:9", "'19:3",
        'installed_by', 'given_at', 'Bava Batra 14', 'Menachot 99', 'Berakhot 8b', 'Berakhot 33b', 'Menachot 43b', 'Yoma 69b', 'Berakhot 20b', 'Niddah 70b', 'Ketubot 105', 'Bava Metzia 59b', 'Yevamot 47', 'Bava Batra 123', 'Seder Olam', 'Rosh Hashanah 3a', "Ta'anit 9a", 'Shekalim', 'Sotah 7:6', 'Berakhot 9:5')
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
    broad = {}
    for pat in PATS:
        hits = [l.strip()[:150] for l in src.split('\n') if pat in l]
        if not hits: continue
        if pat in BROAD: broad[pat] = len(hits); continue
        print('   lines with %-18r: %d  e.g. %s' % (pat, len(hits), hits[:1]))
    if broad: print('   broad counts: %s' % broad)

print('\n==== (3) THE KINDS ON FILE touching the chapter\'s matter ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
print('  kinds %d, effects %d' % (len(E), len(F)))
KP = r'ark|tablet|testimony|hew|acacia|levi|minister|bless|inherit|portion|tithe|aaron|buried|burial|station|journey|encamp|\bhor\b|moserah|cleave|circumcis|foreskin|stiff|bribe|orphan|widow|stranger|sojourn|seventy|stars|praise|heaven|eleazar|fragment|broken|awesome|second_tablets|go_up|forty|finger|covenant_cut'
for k in sorted(E):
    if re.search(KP, k): print('    %-44s form %-8s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:100].replace('\n', ' ')))
print('  effects touching the matter:')
for f in sorted(F):
    if re.search(KP, f): print('    %-40s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:110].replace('\n', ' ')))
for k in [k for k in sorted(E) if re.search(r'ark|tablet|testimony|levi|aaron_died|buried|station|journey|encamp|moserah|\bhor\b|second_tablets|tablets_|bless|tithe|portion|stranger|bribe|seventy|circumcis|ascen', k)][:60]:
    print('  a kind row whole (%s): %s' % (k, str(E.get(k))[:600]))
for f in [f for f in sorted(F) if re.search(r'ark|tablet|testimony|levi|aaron|buried|portion|tithe|inherit|bless|stranger|bribe|face|seventy|circumcis|cleave|love|fear|second', f)][:50]:
    print('  an effect row (%s): %s' % (f, str(F.get(f))[:400]))

print('\n==== (4) THE REGISTRY MAP for the chapter\'s tokens ====')
reg_map = CS.registry_map()
TOK = ('israel', 'israel_people', 'moses', 'aaron', 'eleazar', 'the-levites', 'levi', 'the-priests', 'the-ark', 'the-tablets', 'the-two-tablets', 'the-testimony', 'the-fathers', 'abraham', 'isaac', 'jacob', 'egypt', 'egypt_people', 'the-land', 'the-stranger', 'the-orphan', 'the-widow', 'mount-hor', 'moserah', 'the-mountain', 'horeb', 'god', 'the-lord', 'the-people', 'the-covenant', 'the-covenant-at-sinai', 'the-tent', 'the-tabernacle')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])
print('  registry ids with ark/tablet/testimony/levi/aaron/priest/eleazar/stranger in them: %s' % sorted({v for v in reg_map.values() if re.search(r'ark|tablet|testimony|levi|aaron|priest|eleazar|stranger|orphan|widow', str(v))})[:40])

print('\n==== (5) THE TAPE\'S LINES the chapter retells; THE CLOCK\'S DAY at each; the tape\'s LAST lines and markers ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
tl = tape.split('\n')
KINRE = r"'Exod 34:(?:[1-4]|2[89])\b|'Exod 25:(?:1\d|2[0-2])\b|'Exod 37:[1-9]\b|'Exod 40:(?:3|2[01])\b|'Exod 31:18|'Exod 24:12\b|'Exod 32:(?:2[6-9]|34)\b|'Exod 33:1\b|'Num 33:3\d\b|'Num 20:2[2-9]\b|'Num 3:|'Num 4:|'Num 8:|'Num 18:|'Num 6:2[3-7]\b|'Exod 22:2[0-3]\b|'Exod 23:[89]\b|'Lev 19:3[34]\b|'Gen 46:2[67]\b|'Exod 1:[1-7]\b|'Deut 4:(?:5|13)\b|'Deut 6:(?:5|13)\b|'Deut 10:"
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
print('  the Exod 1/22/23/24/25/31/32/33/34/37/40, Lev 19, Num 3/4/6/8/18/20/33, Gen 46 lines with their kinds:')
for l in tl:
    m = re.search(r"w\.(?:event|write|marker|close)\('([a-z_0-9]+)'.*?'((?:Exod (?:1:[1-7]|22:2[0-3]|23:[89]|24:12|25:(?:1\d|2[0-2])|31:18|32:(?:2[6-9]|34)|33:1|34:(?:[1-4]|2[89])|37:[1-9]|40:(?:3|2[01]))|Lev 19:3[34]|Num (?:3:(?:[5-9]|1[0-3]|4\d|5[01])|4:\d+|6:2[3-7]|8:(?:[5-9]|1\d|2[0-6])|18:(?:[12]|2[0-4])|20:2[2-9]|33:3\d)|Gen 46:2[67])\b(?:-\d+)?)'", l)
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
print('  the chapter-10-era log rows (EVENT/marker rows whose source is the second tablets, the ark, the testimony placed, the Levites, the blessing, the stations, Aaron at Hor, the seventy; the day and its rendering):')
n = 0
for row in w.log:
    if not isinstance(row, (list, tuple)) or len(row) < 3: continue
    tag, day, ev = row[0], row[1], row[2]
    src = str(ev.get('source', ev.get('verse', ''))) if isinstance(ev, dict) else str(ev)
    if re.search(r'Exod (?:25:1\d|25:2[0-2]|31:18|34:[1-4]\b|34:2[89]|37:[1-9]\b|40:(?:3|2[01])\b|32:2[6-9]|32:34|33:1\b|1:[1-7]\b)|Num (?:33:3\d|20:2[2-9]|3:(?:[5-9]|1[0-3]|4\d|5[01])\b|4:\d|8:(?:[5-9]|1\d|2[0-6])\b|18:(?:[12]|2[0-4])\b|6:2[3-7])|Gen 46:2[67]', src):
        print('    %-6s day %-6s %-32s %s | %s' % (tag, day, ev.get('kind', '?') if isinstance(ev, dict) else '?', src[:22], render(day)))
        n += 1
        if n > 120: break
print('  the marker rows on the log (all tags): %s' % collections.Counter(r[0] for r in w.log if isinstance(r, (list, tuple))).most_common(8))
print('  markers in the world (Exod 19-34): %s' % [(m if isinstance(m, str) else str(m)[:120]) for m in (getattr(w, 'markers', []) or [])][:0])
mk = [x for x in getattr(w, 'markers', []) if re.search(r'Exod (?:19|24|31|32|33|34|40)|Num (?:9|10|20|33)|Deut', str(x))] if hasattr(w, 'markers') else []
print('  the markers Exod 19-40, Num 9-10, 20, 33, Deut: %s' % [str(x)[:160] for x in mk][:60])
print('  THE THIRD FORTY: the sequence file\'s M[] lines for the forties and the last tablets: %s' % [l.strip()[:200] for l in src_cs.split('\n') if re.search(r"M\['(?:ascent|breaking|morrow|second_ascent|second_tablets|aaron_told|speech_resumed_9)'\] = ", l)])
print('  CAL_PARAMS rows naming tablets/tishri: %s' % [(k, v) for k, v in getattr(CS, 'CAL_PARAMS', {}).items() if re.search(r'tablet|tishri|kippur', str(k) + str(v))][:6])
print('  the tape lines naming the stations or Hor by name: %s' % [l.strip()[:200] for l in tl if re.search(r'Moser|Jaakan|jaakan|Gudgod|Jotbath|Mount Hor|mount_hor|hor_haggidgad|Hor-hag', l)][:20])
print('  what a marker object looks like: %s' % (str(getattr(w, 'markers', ['?'])[0])[:300] if getattr(w, 'markers', None) else 'no w.markers'))

print('\n==== (6) THE CHECKPOINT PREFIXES, THE M[] NAMES, THE DAEMONS ====')
used = collections.Counter(re.findall(r"cp\('([A-Z]+)\d", src_cs))
print('  cp() checkpoint prefixes in use: %s' % sorted(used.items()))
free2 = [c for c in ['C' + x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'] if c not in used]
print('  FREE two-letter C-prefixes: %s' % free2)
usedD = sorted((p, n) for p, n in used.items() if p.startswith('D'))
print('  THE D SERIES in use: %s; the next name: %s' % (usedD, next(('D' + x) for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if ('D' + x) not in used)))
print('  the VERDICTS list prefixes: %s' % sorted(collections.Counter(re.findall(r"'([A-Z]+)\d[a-z\-0-9]* (?:MATCH|DIVERGE)'", src_cs)).items()))
print('  code that assumes a checkpoint name\'s first letter (startswith/== on C):')
for f in sorted(glob.glob(f'{ROOT}/World/step9/*.py')):
    for i, l in enumerate(open(f, encoding='utf-8').read().split('\n')):
        if re.search(r"startswith\('C|== 'C'|\[0\] == 'C|'C\[|\[A-Z\]\{2\}|\[A-Z\]\+\\d|\[A-Z\]\\d", l) and re.search(r'cp|checkpoint|name|prefix|VERDICT', l):
            print('    %s:%d %s' % (os.path.basename(f), i + 1, l.strip()[:150]))
print('  M[] marker names on file: %s' % re.findall(r"M\['([a-z_0-9:]+)'\] = ", src_cs))
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  daemons %d; installed_by values: %s' % (len(dd['daemons']), dict(collections.Counter(str(v.get('installed_by')).split()[0] for v in dd['daemons'].values()))))
for dn in ('law_not_righteousness', 'law_good_land', 'law_hear_o_israel'):
    print('  the daemon block %s: %s' % (dn, str(dd['daemons'].get(dn))[:500]))
print('  the functions block not_righteousness: %s' % str(dd.get('functions', {}).get('not_righteousness'))[:400])
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers naming Deut 10: %s; edges naming Deut 10: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if re.search(r'Deut 10:', str(p))][:10], [e for e in dep['edges'] if re.search(r'Deut 10:', str(e))][:5]))
print('  the not_righteousness edges on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], str(e.get('why', ''))[:90]) for e in dep['edges'] if e['from'] == 'not_righteousness'])
print('  a CALL edge row WHOLE (not_righteousness): %s' % [e for e in dep['edges'] if e['from'] == 'not_righteousness' and e.get('disposition') == 'CALL'][:1])
print('  a RUN_CITATION pointer row WHOLE (not_righteousness): %s' % [p for p in dep['pointers'] if p.get('runner') == 'not_righteousness'][:1])
print('  the spans of the kin: %s' % {k: dep['spans'].get(k) for k in NAMES})
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the register seats naming Deut 10 (WHOLE): %s' % [(sec, k, v) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.startswith('Deut 10')])
print('  the register seats naming Deut 4:5, Num 18:20, Gen 46:27, Exod 1:5: %s' % [(sec, k, v) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.split(' ')[0] + ' ' + k.split(' ')[1] in ('Deut 4:5', 'Num 18:20', 'Gen 46:27', 'Exod 1:5')][:8])
print('  the receipt finder\'s defs in register_census.py: %s' % re.findall(r'^def ([a-z_0-9]+)\(', open(f'{ROOT}/World/step9/register_census.py', encoding='utf-8').read(), re.M))

print('\n==== (7) THE READBACK PROBES on file; the ledgers naming 10:6 / Moserah; the ark, journeys and Levites ledgers ====')
rp = open(f'{ROOT}/World/step9/readback_probes.py', encoding='utf-8').read()
print('  readback_probes: the Q labels: %s' % sorted(set(re.findall(r"'(Q\d+)", rp)), key=lambda s: int(s[1:])))
print('  the Q22-Q24 heads: %s' % [l.strip()[:200] for l in rp.split('\n') if re.search(r"'Q(?:2[2-4])", l)][:6])
print('  the probes holding a marker count or a marker list literal: %s' % [l.strip()[:160] for l in rp.split('\n') if re.search(r'markers?\W+1[0-9]{2}\b|169\b|167\b', l)][:12])
print('  the readback forms on THE_LOOP\'s step-6 row: %s' % [l.strip()[:220] for l in open(f'{ROOT}/World/step9/THE_LOOP.md', encoding='utf-8').read().split('\n') if 'SIXTH' in l or 'sixth form' in l.lower()][:3])
for f in sorted(glob.glob(f'{ROOT}/logic/oral_triage/*.md')):
    t = open(f, encoding='utf-8').read()
    n = len(re.findall(r'Deut(?:eronomy)? 10:6\b|Moserah', t))
    if n: print('  ledger naming Deut 10:6 / Moserah: %s (%d)' % (os.path.basename(f), n))
print('  the ark\'s, the journeys\' and the Levites\' ledgers: %s' % [os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_triage/*.md') if re.search(r'exo_2[5-9]|exo_3[0-9]|exo_40|num_33|num_20|num_0[348]|num_18|masei|chukat|bamidbar|beha|korach|terumah|vayakhel|pekudei|naso|blessing', os.path.basename(f))])
