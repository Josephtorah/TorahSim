#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 9b — THE COMPILE OF CHAPTER 11, Deuteronomy 11:1-32 (2026-09-20; the owner: "9b go" after sitting 9's commit 2f4ec5b):
# THE RECONNAISSANCE before the design (ch10_compile_recon.py's form on chapter 11, derived by derive_ch11_recon.py) — (1) WHICH RUNNER HOLDS A CELL FOR
# THE CHAPTER'S MATTER (the discipline retold — Egypt's signs, the sea, the wilderness, Dathan and Abiram; the good land watered by heaven; the rain
# conditional and the shut heavens; the frontlets, the teaching and the doorposts; the dispossession, the borders and the dread with the receipt "as He
# spoke to you"; the blessing and the curse set, Gerizim and Ebal, Gilgal and Moreh) — every runner's ink refs scanned by regex, per def; (2) the callee
# modules' defs, asks, DATA keys (the modules with hits on the kin); (3) the kinds and effects on file touching the matter; (4) the registry map; (5) the
# tape's lines the chapter retells (the sea Exodus 14-15; the exodus 12:29-51; Dathan and Abiram Numbers 16 and 26:9-11; the Shema 6:4-9 with Exodus 13:9,
# 16; the good land 8; the escort and the borders Exodus 23:20-33; the rains Leviticus 26; the borders Numbers 34:1-15; the pilgrimage guarded Exodus
# 34:23-24; the flood Genesis 7; Moreh and Lot Genesis 12:6, 13:10; the river 15:18) with THE CLOCK'S DAY at each, the tape's LAST lines and markers;
# (6) the sequence file's tuples, the checkpoint prefixes in use (the D series — DB the open series, the next DC), the M[] names, the daemons; (7) the
# dispositions and register seats naming Deut 11 (none expected — 11:25's "as He spoke to you" is the finder's third form), the readback probes' tail,
# the ledgers naming 11:25 / Gerizim / Dathan, the sea's, Korah's, the borders', the rains' and the Shema's ledgers.
import sys, io, re, contextlib, inspect, collections, yaml, glob, subprocess, os, importlib
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()   # RUN FROM THE REPO ROOT; no absolute repo path typed
sys.path.insert(0, f'{ROOT}/World/step9')

print('==== (1) THE CHAPTER\'S MATTER — every runner\'s refs, per def ====')
SEATS = [(r'Deut(?:eronomy)? 11:(\d+)', 'Deut 11'), (r'Exod(?:us)? 14:(?:1\d|2\d|3[01])\b', 'Exod 14 (the sea)'), (r"ink\('14:(?:1\d|2\d|3[01])'", 'Exod 14 (ink)'), (r'Exod(?:us)? 15:(?:[1-9]|1\d|2[01])\b', 'Exod 15 (the song)'), (r'Exod(?:us)? 12:(?:29|3\d|4\d|51)\b', 'Exod 12:29-51 (the exodus)'), (r'Exod(?:us)? (?:7:3|10:1|10:2)\b', 'Exod 7:3 / 10:1-2 (signs and wonders)'),
         (r'Num(?:bers)? 16:(?:[1-9]|[12]\d|3[0-5])\b', 'Num 16 (Korah, Dathan and Abiram)'), (r"ink\('16:(?:[1-9]|[12]\d|3[0-5])'", 'Num 16 (ink)'), (r'Num(?:bers)? 26:(?:9|1[01])\b', 'Num 26:9-11 (Dathan and Abiram recalled)'), (r'Deut(?:eronomy)? 6:[4-9]\b', 'Deut 6:4-9 (the Shema)'), (r'Exod(?:us)? 13:(?:9|16)\b', 'Exod 13:9, 16 (the frontlets)'),
         (r'Deut(?:eronomy)? 8:(?:[1-9]|1\d|20)\b', 'Deut 8 (the good land; the wilderness)'), (r'Exod(?:us)? 23:(?:2\d|3[0-3])\b', 'Exod 23:20-33 (the escort, the dread, the borders)'), (r'Lev(?:iticus)? 26:(?:[3-9]|[1-3]\d|4[0-6])\b', 'Lev 26 (the rains; the heavens as iron)'), (r'Num(?:bers)? 34:(?:[1-9]|1[0-5])\b', 'Num 34:1-15 (the borders)'), (r'Gen(?:esis)? 15:18\b', 'Gen 15:18 (the river)'),
         (r'Deut(?:eronomy)? 7:(?:1|2[0-4])\b', 'Deut 7:1, 20-24 (seven nations; the dread)'), (r'Exod(?:us)? 34:2[34]\b', 'Exod 34:23-24 (the pilgrimage guarded)'), (r'Deut(?:eronomy)? 16:16\b', 'Deut 16:16 (three times a year)'), (r'Deut(?:eronomy)? 9:(?:1|12)\b|Deut(?:eronomy)? 4:38\b', 'Deut 4:38 / 9:1 / 9:12 (than you; turn aside)'), (r'Deut(?:eronomy)? 30:(?:15|19|20)\b', 'Deut 30:15-20 (the choice)'),
         (r'Deut(?:eronomy)? 27:1[1-3]\b|Josh(?:ua)? 8:3[0-5]\b', 'Deut 27:11-13 / Josh 8:30-35 (Gerizim and Ebal)'), (r'Gen(?:esis)? 12:6\b', 'Gen 12:6 (Moreh)'), (r'Gen(?:esis)? 13:10\b', 'Gen 13:10 (Lot; like the land of Egypt)'), (r'Gen(?:esis)? 7:(?:4|2[1-3])\b', 'Gen 7:4, 21-23 (the flood; every living thing)'), (r'Deut(?:eronomy)? 28:12\b|1 Kings 8:35\b', 'Deut 28:12 / 1 Kings 8:35 (the treasure; no rain)'),
         (r'Josh(?:ua)? (?:1:[3-5]|1:11|2:10|5:6|22:5|23:16|24:31)\b|Judg(?:es)? 2:7\b', "Joshua's receipts of the chapter"), (r'Berakhot 1[3-6][ab]|Berakhot 33a', "the paragraphs' order / the mention of rain"), (r"Ta'?anit (?:[23]|[7-9]|10)[ab]|Rosh Hashanah 1[67][ab]", 'the rain and the year judged'), (r'Menachot 3[4-7][ab]|Kiddushin (?:29|30)[ab]', 'tefillin / mezuzah / sons (4b)'), (r'Kiddushin (?:36|37|40)[ab]', 'land-bound / study and deed'),
         (r'Sotah 3[2-7][ab]|Gittin 8a|Ketubot 11[01][ab]|Sanhedrin 90b|Pesachim 8b|Sukkah 52a|Sheviit 6', "the docket's other works"),
         (r'\brain\b|\brains\b', 'rain'), (r'early rain|latter rain|late rain|former rain', 'the early and the late rain'), (r'\bfrontlets?\b|tefillin|phylacter', 'frontlets / tefillin'), (r'mezuz|doorpost', 'mezuzah / doorposts'), (r'your sons\b|teach them', 'teach your sons'), (r'\bborders?\b|Euphrates|western sea|hinder sea', 'the borders'), (r'\bdread\b|\bterror\b|fear of you', 'the dread'),
         (r'Gerizim|Ebal', 'Gerizim / Ebal'), (r'Gilgal', 'Gilgal'), (r'\bMoreh\b', 'Moreh'), (r'Dathan|Abiram|\bswallow', 'Dathan and Abiram / swallowed'), (r'Red Sea|Sea of Reeds|Reed Sea|\bchariots?\b', 'the Red Sea / the chariots'), (r'\bdiscipline\b|\bchasten|\bchastise', 'discipline'), (r'\bgarden\b', 'garden'), (r'milk and honey', 'milk and honey'), (r'\bcleave\b|\bcling\b', 'cleave'),
         (r'\bdispossess|little by little|\bhornet', 'dispossess / little by little / the hornet'), (r'blessing and (?:a |the )?curse|\bcurses?\b', 'blessing and curse'), (r'shut (?:up )?the heavens|heavens? (?:be |are )?shut|\bwithhold|no rain', 'the heavens shut'), (r'\bgrass\b|\bcattle\b|\bsatisf', 'grass / cattle / satisfied'), (r'\bprolong|multipl(?:y|ied) .{0,25}days|your days', 'prolong your days'), (r'every place|sole of your foot', 'every place your foot treads'),
         (r'\bthe LORD (?:your God )?swore|which .{0,12}swore', 'the oath to the fathers'), (r'as (?:He|the LORD) (?:has )?spoke', 'as He spoke (the receipt)'), (r'possess it and dwell', 'possess it and dwell in it'), (r'\bElul\b|\bAv\b|Tishri', 'Elul / Av / Tishri')]
KIN_LABELS = ('Exod 14 (the sea)', 'Exod 15 (the song)', 'Exod 12:29-51 (the exodus)', 'Exod 7:3 / 10:1-2 (signs and wonders)', 'Num 16 (Korah, Dathan and Abiram)', 'Num 26:9-11 (Dathan and Abiram recalled)', 'Deut 6:4-9 (the Shema)', 'Exod 13:9, 16 (the frontlets)', 'Deut 8 (the good land; the wilderness)', 'Exod 23:20-33 (the escort, the dread, the borders)', 'Lev 26 (the rains; the heavens as iron)', 'Num 34:1-15 (the borders)', 'Gen 15:18 (the river)', 'Deut 7:1, 20-24 (seven nations; the dread)', 'Exod 34:23-24 (the pilgrimage guarded)', 'Deut 16:16 (three times a year)', 'Deut 4:38 / 9:1 / 9:12 (than you; turn aside)', 'Deut 30:15-20 (the choice)', 'Deut 27:11-13 / Josh 8:30-35 (Gerizim and Ebal)', 'Gen 12:6 (Moreh)', 'Gen 13:10 (Lot; like the land of Egypt)', 'Gen 7:4, 21-23 (the flood; every living thing)', 'Deut 28:12 / 1 Kings 8:35 (the treasure; no rain)')
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
            if label in KIN_LABELS or label == 'Deut 11': print('     %-34s %s' % (label, dict(found[label])))
NAMES = sorted({n for n, d in HITS.items() if any(l in d for l in KIN_LABELS)} | {'opening_speech', 'obey_horeb', 'covenant_at_horeb', 'decalogue', 'hear_o_israel', 'seven_nations', 'good_land', 'not_righteousness', 'second_tablets', 'exodus_story', 'pesach', 'korach', 'second_census', 'borders', 'tochacha', 'mishpatim', 'mishpatim_2', 'mishpatim_3', 'ordinances', 'moadim', 'calendar', 'clocks', 'primeval', 'mamre', 'family', 'erection', 'shelach', 'journeys'})
print('  THE KIN RUNNERS (a hit on a kin label) + the Deuteronomy runners + the kin named by the box + the clock runners: %s' % NAMES)
MODS = []
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    for n in NAMES:
        try: MODS.append((n, importlib.import_module('cold_run_' + n)))
        except Exception as e: print('IMPORT FAILED', n, e, file=sys.stderr)
print('  modules imported: %s' % [n for n, _ in MODS])

print('\n==== (2) THE CALLEES\' DEFS, ASKS, DATA KEYS ====')
BROAD = ('blessing', 'curse', 'possess', 'sons', 'satisf', 'shut', 'rain', 'land', 'fathers', 'swore', 'heaven', 'fear', 'love', "'6:", "'8:", "'14:", "'16:", "'23:", "'26:", "'34:", 'installed_by', 'given_at', 'border', 'sea')
PATS = ('Deut 11', 'Deuteronomy 11', 'rain', 'frontlet', 'tefillin', 'mezuz', 'doorpost', 'sons', 'border', 'Euphrates', 'dread', 'terror', 'Gerizim', 'Ebal', 'Gilgal', 'Moreh', 'Dathan', 'Abiram', 'swallow', 'Red Sea', 'chariot', 'discipline', 'garden', 'milk and honey', 'cleave', 'dispossess', 'little by little', 'hornet', 'curse', 'blessing', 'shut', 'grass', 'satisf', 'possess', 'sea', 'land', 'fathers', 'swore', 'heaven', 'fear', 'love', 'as He spoke', 'as the LORD spoke', 'every place',
        'installed_by', 'given_at', 'Berakhot 13', 'Berakhot 14', 'Berakhot 15', 'Berakhot 16', 'Berakhot 33a', "Ta'anit", 'Taanit', 'Rosh Hashanah 16', 'Rosh Hashanah 17', 'Menachot 34', 'Menachot 35', 'Menachot 36', 'Menachot 37', 'Kiddushin 29', 'Kiddushin 30', 'Kiddushin 36', 'Kiddushin 37', 'Kiddushin 40', 'Sotah 32', 'Sotah 33', 'Sotah 34', 'Sotah 37', 'Gittin 8a', 'Ketubot 110', 'Ketubot 111', 'Sanhedrin 90', 'Pesachim 8b', 'Sukkah 52', 'Sheviit')
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
KP = r'rain|heaven|shut|early|latter|grass|satisf|frontlet|tefillin|mezuz|doorpost|teach|border|euphrates|\bsea\b|sea_|dread|terror|bless|curse|gerizim|ebal|gilgal|moreh|dathan|abiram|swallow|korah|discipline|red_sea|pursu|chariot|drown|garden|milk|honey|possess|dispossess|little|hornet|cleave|shema|sign|frontlet|gate|prolong|land_|the_land|oath|sworn|swore|escort|angel_sent|nations|deliver|treasure'
for k in sorted(E):
    if re.search(KP, k): print('    %-44s form %-8s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:100].replace('\n', ' ')))
print('  effects touching the matter:')
for f in sorted(F):
    if re.search(KP, f): print('    %-40s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:110].replace('\n', ' ')))
for k in [k for k in sorted(E) if re.search(r'sea|drown|chariot|pursu|swallow|korah|dathan|shema|frontlet|tefillin|mezuz|rain|heaven|bless|curse|border|dread|terror|escort|hornet|nations|possess|gerizim|ebal|gilgal|oath|sworn|swore|land_|good_land|treasure|discipline|garden', k)][:80]:
    print('  a kind row whole (%s): %s' % (k, str(E.get(k))[:600]))
for f in [f for f in sorted(F) if re.search(r'sea|drown|swallow|shema|frontlet|tefillin|mezuz|rain|heaven|bless|curse|border|dread|terror|hornet|nations|possess|gerizim|ebal|oath|sworn|land|discipline|love|fear|cleave|teach|sons', f)][:60]:
    print('  an effect row (%s): %s' % (f, str(F.get(f))[:400]))

print('\n==== (4) THE REGISTRY MAP for the chapter\'s tokens ====')
reg_map = CS.registry_map()
TOK = ('israel', 'israel_people', 'moses', 'dathan', 'abiram', 'korah', 'eliab', 'the-earth', 'egypt', 'egypt_people', 'pharaoh', 'the-egyptians', 'the-sea', 'the-red-sea', 'the-land', 'the-heavens', 'the-rain', 'the-fathers', 'the-sons', 'the-tefillin', 'the-frontlets', 'the-doorposts', 'the-house', 'the-gates', 'mount-gerizim', 'mount-ebal', 'gilgal', 'the-jordan', 'the-nations', 'the-euphrates', 'the-wilderness', 'lebanon', 'the-western-sea', 'the-ground', 'the-produce', 'the-cattle', 'god', 'the-lord', 'the-people', 'the-canaanite', 'moreh', 'the-garden', 'the-good-land')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])
print('  registry ids with sea/egypt/dathan/abiram/korah/heaven/rain/land/gerizim/ebal/gilgal/jordan/nations in them: %s' % sorted({v for v in reg_map.values() if re.search(r'sea|egypt|dathan|abiram|korah|heaven|rain|land|gerizim|ebal|gilgal|jordan|nation|tefillin|frontlet|doorpost|mezuz', str(v))})[:60])

print('\n==== (5) THE TAPE\'S LINES the chapter retells; THE CLOCK\'S DAY at each; the tape\'s LAST lines and markers ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
tl = tape.split('\n')
KINRE = r"'Exod 14:|'Exod 15:|'Exod 12:(?:29|3\d|4\d|51)\b|'Exod 13:(?:9|16)\b|'Exod 23:(?:2\d|3[0-3])\b|'Exod 34:2[34]\b|'Num 16:|'Num 26:(?:9|1[01])\b|'Num 34:(?:[1-9]|1[0-5])\b|'Lev 26:|'Gen 7:(?:4|2[1-3])\b|'Gen 12:6\b|'Gen 13:10\b|'Gen 15:18\b|'Deut 6:[4-9]\b|'Deut 7:(?:1|2[0-4])\b|'Deut 8:|'Deut 9:(?:1|12)\b|'Deut 4:38\b|'Deut 11:"
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
print('  the section comments of the kin (Exod 12-15, 23; Num 16, 34; Lev 26; Gen 7, 12-13): %s' % [c for c in re.findall(r'# ---- ((?:Exod|Num|Lev|Gen) [^-]+?) ----', tape) if re.search(r'Exod (?:1[2-5]|23)|Num (?:16|34)|Lev 26|Gen (?:7|1[23])\b', c)])
print('  DAEMON_ORDER %d, tail %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-3:]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT))
print('  the Exod 12-15/13/23/34, Lev 26, Num 16/26/34, Gen 7/12/13/15, Deut 4/6/7/8/9 lines with their kinds:')
for l in tl:
    m = re.search(r"w\.(?:event|write|marker|close)\('([a-z_0-9]+)'.*?'((?:Exod (?:14:\d+|15:\d+|12:(?:29|3\d|4\d|51)|13:(?:9|16)|23:(?:2\d|3[0-3])|34:2[34])|Num (?:16:\d+|26:(?:9|1[01])|34:(?:[1-9]|1[0-5]))|Lev 26:\d+|Gen (?:7:(?:4|2[1-3])|12:6|13:10|15:18)|Deut (?:6:[4-9]|7:(?:1|2[0-4])|8:\d+|9:(?:1|12)|4:38|11:\d+))\b(?:-\d+)?)'", l)
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
print('  the chapter-11-era log rows (EVENT/marker rows whose source is the sea, the exodus, Dathan and Abiram, the Shema, the good land, the escort and the borders, the rains, the borders, the flood, Moreh; the day and its rendering):')
n = 0
for row in w.log:
    if not isinstance(row, (list, tuple)) or len(row) < 3: continue
    tag, day, ev = row[0], row[1], row[2]
    src = str(ev.get('source', ev.get('verse', ''))) if isinstance(ev, dict) else str(ev)
    if re.search(r'Exod (?:14:\d+|15:\d+|12:(?:29|3\d|4\d|51)\b|13:(?:9|16)\b|23:(?:2\d|3[0-3])\b|34:2[34]\b)|Num (?:16:\d+|26:(?:9|1[01])\b|34:(?:[1-9]|1[0-5])\b)|Lev 26:\d+|Gen (?:7:(?:4|2[1-3])\b|12:6\b|13:10\b|15:18\b)', src):
        print('    %-6s day %-6s %-32s %s | %s' % (tag, day, ev.get('kind', '?') if isinstance(ev, dict) else '?', src[:22], render(day)))
        n += 1
        if n > 120: break
print('  the marker rows on the log (all tags): %s' % collections.Counter(r[0] for r in w.log if isinstance(r, (list, tuple))).most_common(8))
print('  markers in the world (Exod 19-34): %s' % [(m if isinstance(m, str) else str(m)[:120]) for m in (getattr(w, 'markers', []) or [])][:0])
mk = [x for x in getattr(w, 'markers', []) if re.search(r'Exod (?:1[2-5]|19|23|24|34|40)|Num (?:9|10|16|20|33|34)|Lev 26|Deut', str(x))] if hasattr(w, 'markers') else []
print('  the markers Exod 12-15, 19, 23-24, 34, 40, Num 9-10, 16, 20, 33-34, Lev 26, Deut: %s' % [str(x)[:160] for x in mk][:80])
print('  THE MARKERS THE KIN SIT UNDER: the sequence file\'s M[] lines naming the sea, the exodus, Korah, the rains, the escort, the borders, the speech: %s' % [l.strip()[:200] for l in src_cs.split('\n') if re.search(r"M\['[a-z_0-9]*(?:sea|exodus|pesach|plague|korah|dathan|swallow|rain|escort|angel|border|bless|curse|speech_resumed|calf|tochacha|sinai)[a-z_0-9]*'\] = ", l)][:40])
print('  CAL_PARAMS rows naming rain/tishri/year: %s' % [(k, v) for k, v in getattr(CS, 'CAL_PARAMS', {}).items() if re.search(r'rain|tishri|year|season', str(k) + str(v))][:8])
print('  the tape lines naming Dathan / Abiram / Korah / the Red Sea / the Euphrates / Gerizim / Ebal / Gilgal / Moreh / the frontlets / the doorposts / the hornet: %s' % [l.strip()[:200] for l in tl if re.search(r'Dathan|Abiram|Korah|Red Sea|Reed Sea|Euphrates|Gerizim|Ebal|Gilgal|Moreh|frontlet|tefillin|mezuz|doorpost|early rain|latter rain|hornet|little by little', l)][:30])
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
for dn in ('law_second_tablets', 'law_good_land', 'law_hear_o_israel', 'law_seven_nations'):
    print('  the daemon block %s: %s' % (dn, str(dd['daemons'].get(dn))[:500]))
print('  the functions block second_tablets: %s' % str(dd.get('functions', {}).get('second_tablets'))[:400])
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers naming Deut 11: %s; edges naming Deut 11: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if re.search(r'Deut 11:', str(p))][:10], [e for e in dep['edges'] if re.search(r'Deut 11:', str(e))][:5]))
print('  the second_tablets edges on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], str(e.get('why', ''))[:90]) for e in dep['edges'] if e['from'] == 'second_tablets'])
print('  a CALL edge row WHOLE (second_tablets): %s' % [e for e in dep['edges'] if e['from'] == 'second_tablets' and e.get('disposition') == 'CALL'][:1])
print('  a RUN_CITATION pointer row WHOLE (second_tablets): %s' % [p for p in dep['pointers'] if p.get('runner') == 'second_tablets'][:1])
print('  the spans of the kin: %s' % {k: dep['spans'].get(k) for k in NAMES})
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the register seats naming Deut 11 (WHOLE): %s' % [(sec, k, v) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.startswith('Deut 11')])
print('  the register seats naming Deut 6:8, Deut 8:1, Exod 23:27, Lev 26:4, Num 34:6, Num 16:32: %s' % [(sec, k, v) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.split(' ')[0] + ' ' + k.split(' ')[1] in ('Deut 6:8', 'Deut 8:1', 'Exod 23:27', 'Lev 26:4', 'Num 34:6', 'Num 16:32')][:8])
print('  the receipt finder\'s defs in register_census.py: %s' % re.findall(r'^def ([a-z_0-9]+)\(', open(f'{ROOT}/World/step9/register_census.py', encoding='utf-8').read(), re.M))

print('\n==== (7) THE READBACK PROBES on file; the ledgers naming 11:25 / Gerizim / Dathan; the sea, Korah, borders, rains and Shema ledgers ====')
rp = open(f'{ROOT}/World/step9/readback_probes.py', encoding='utf-8').read()
print('  readback_probes: the Q labels: %s' % sorted(set(re.findall(r"'(Q\d+)", rp)), key=lambda s: int(s[1:])))
print('  the Q25-Q27 heads: %s' % [l.strip()[:200] for l in rp.split('\n') if re.search(r"'Q(?:2[5-7])", l)][:6])
print('  the probes holding a marker count or a marker list literal: %s' % [l.strip()[:160] for l in rp.split('\n') if re.search(r'markers?\W+1[0-9]{2}\b|169\b|167\b', l)][:12])
print('  the readback forms on THE_LOOP\'s step-6 row: %s' % [l.strip()[:220] for l in open(f'{ROOT}/World/step9/THE_LOOP.md', encoding='utf-8').read().split('\n') if 'COMBINE' in l or 'combined' in l.lower()][:3])
for f in sorted(glob.glob(f'{ROOT}/logic/oral_triage/*.md')):
    t = open(f, encoding='utf-8').read()
    n = len(re.findall(r'Deut(?:eronomy)? 11:25\b|Gerizim|Dathan', t))
    if n: print('  ledger naming Deut 11:25 / Gerizim / Dathan: %s (%d)' % (os.path.basename(f), n))
print('  the sea\'s, Korah\'s, the borders\', the rains\', the escort\'s and the Shema\'s ledgers: %s' % [os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_triage/*.md') if re.search(r'exo_1[2-5]|exo_23|num_16|num_26|num_34|lev_26|deu_06|deu_08|korach|borders|beshalach|matza|sea', os.path.basename(f))])
