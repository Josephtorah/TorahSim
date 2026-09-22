import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 12b — THE COMPILE OF CHAPTER 14, Deuteronomy 14:1-29 (2026-09-21; the owner: "Go" after sitting 12's tail — the commit still on his
# word): THE RECONNAISSANCE before the design (ch13_compile_recon.py's form on chapter 14, derived by derive_ch14_recon.py) — (1) WHICH RUNNER HOLDS A CELL FOR
# THE CHAPTER'S MATTER (THE TWIN CHAPTER Leviticus 11 — the beasts' two signs, the water's two, the birds' list, the swarmers, the carcass; the carcass and the torn
# — Leviticus 17:15, 22:8, Exodus 22:30; the kid in its mother's milk — Exodus 23:19, 34:26; the cuttings and the baldness — Leviticus 19:27-28, 21:5; clean and
# unclean, holy to Me — Leviticus 20:25-26; the gleanings — Leviticus 19:9-10, 23:22; the tithe the LORD's and the herd's tithe — Leviticus 27:30-33; the Levites'
# tithe and no portion — Numbers 18:20-32; the tenth's first seats — Genesis 14:20, 28:22; clean beasts — Genesis 7:2, 8, 8:20; a holy people 7:6; the Levite's no
# portion 10:9; the sojourner, the fatherless and the widow 10:18; the place, the tithe at the place, the far place, the Levite — 12:5-28) — every runner's ink
# refs scanned by regex, per def; (2) the callee modules' defs, asks, DATA keys; (3) the kinds and effects on file touching the matter; (4) the registry map; (5)
# the tape's lines of the kin with THE CLOCK'S DAY at each, the tape's LAST lines and markers; (6) the sequence file's tuples, the checkpoint prefixes in use (the D
# series — DE the open series, the next DF), the M[] names, the daemons; (7) the dispositions and register seats naming Deut 14 (none expected — the reading's
# finder found no receipt, no header, no footer; the two number verses 14:6 [2] and 14:28 [3]), the readback probes' tail, the ledgers naming 14:n / the second
# tithe / the poor man's tithe / the carcass / the kid / the signs, the kin's ledgers.
import sys, io, re, contextlib, inspect, collections, yaml, glob, subprocess, os, importlib
ROOT = _ROOT   # RUN FROM THE REPO ROOT; no absolute repo path typed
sys.path.insert(0, f'{ROOT}/World/step9')

print('==== (1) THE CHAPTER\'S MATTER — every runner\'s refs, per def ====')
SEATS = [(r'Deut(?:eronomy)? 14:(\d+)', 'Deut 14'), (r'Lev(?:iticus)? 11:(?:[1-9]|[1-3][0-9]|4[0-7])\b', "Lev 11:1-47 (THE TWIN CHAPTER — the beasts' signs, the water's, the birds, the swarmers, the carcass)"), (r"ink\('11:(?:[1-9]|[1-3][0-9]|4[0-7])'", "ch 11 (ink — the runner's own book; shemini's is Lev 11)"), (r'Lev(?:iticus)? 17:1[35]\b', 'Lev 17:13-15 (the blood covered; the carcass and the torn eaten — the sojourner too)'), (r'Lev(?:iticus)? 19:(?:9|10|27|28)\b', 'Lev 19:9-10, 27-28 (the gleanings; the rounding, the cuttings for the dead)'), (r'Lev(?:iticus)? 20:2[56]\b', 'Lev 20:25-26 (clean and unclean separated; holy to Me)'), (r'Lev(?:iticus)? 21:5\b', "Lev 21:5 (the priests' baldness and cuttings)"), (r'Lev(?:iticus)? 22:8\b', 'Lev 22:8 (the carcass and the torn — the priest)'), (r'Lev(?:iticus)? 23:22\b', 'Lev 23:22 (the gleanings at the harvest)'), (r'Lev(?:iticus)? 27:3[0-3]\b', "Lev 27:30-33 (the tithe the LORD's; the herd's tithe under the rod)"), (r"ink\('27:3[0-3]'", 'Lev 27:30-33 (ink)'),
         (r'Exod(?:us)? 22:30\b', 'Exod 22:30 (the torn flesh to the dogs; men of holiness)'), (r'Exod(?:us)? 23:19\b', "Exod 23:19 (the kid in its mother's milk — the first seat; the firstfruits)"), (r"ink\('23:19'", 'Exod 23:19 (ink)'), (r'Exod(?:us)? 34:26\b', 'Exod 34:26 (the kid — the second seat)'), (r'Num(?:bers)? 18:(?:2[0-9]|3[0-2])\b', "Num 18:20-32 (the Levites' tithe; no portion; the tithe of the tithe)"), (r"ink\('18:(?:2[0-9]|3[0-2])'", 'Num 18:20-32 (ink)'), (r'Gen(?:esis)? (?:7:[28]|8:20)\b', 'Gen 7:2, 8, 8:20 (clean and unclean beasts — the first seats)'), (r'Gen(?:esis)? (?:14:20|28:22)\b', "Gen 14:20, 28:22 (the tenth — Abram's, Jacob's vow)"), (r'Gen(?:esis)? 43:32\b', 'Gen 43:32 (an abomination to the Egyptians)'),
         (r'Deut(?:eronomy)? 7:6\b', "Deut 7:6 (a holy people, a treasured people — 14:2's kin)"), (r'Deut(?:eronomy)? 10:(?:9|18)\b', "Deut 10:9, 18 (the Levite's no portion; the sojourner, the fatherless, the widow)"), (r'Deut(?:eronomy)? 12:(?:[5-7]|1[1-9]|2[0-8])\b', 'Deut 12:5-7, 11-28 (the place; the tithe at the place; the Levite; the far place; the slaughter; the blood)'), (r'Deut(?:eronomy)? (?:15:(?:1|19|2[0-3])|16:1[1-4]|17:1|18:1|22:[67]|23:21|24:1[7-9]|24:2[01]|26:1[2-4]|27:7|31:10|32:9)\b', 'Deut 15:1, 19-23 / 16:11-14 / 17:1 / 18:1 / 22:6-7 / 23:21 / 24:17-21 / 26:12-14 / 27:7 / 31:10 / 32:9 (the kin ahead)'), (r'Deut(?:eronomy)? (?:1[5-9]|2[0-9]|3[0-4]):\d+\b', 'Deut 15-34 (ahead)'),
         (r'1 Kings 5:3\b|2 Kings (?:17:6|18:10)\b|Amos 4:4\b|Neh(?:emiah)? (?:10:3[7-9]|13:(?:5|1[0-2]))\b|2 Chron(?:icles)? 31:(?:5|6|12)\b|Mal(?:achi)? 3:(?:8|10)\b|Isa(?:iah)? (?:65:4|66:17)\b|Ezek(?:iel)? (?:4:14|44:31)\b|1 Sam(?:uel)? 8:1[5-7]\b|Ruth 2:\d+\b|Tob(?:it)? 1:[67]\b', "the run's cases (Solomon's table; Samaria's third year; Amos' tithes; Nehemiah's storerooms; Hezekiah's tithes; Malachi's tithe; the swine's flesh; Ezekiel's carcass; Samuel's tenth; Ruth's gleaning)"),
         (r'Chullin (?:59[ab]|6[0-6][ab]|68[ab]|69a|72b|73a|77a|80a|11[3-6][ab])|Mishnah Chullin (?:1:7|3:[67]|4:4|8:[1-4])', 'Chullin (the signs; the birds; the afterbirth; the torn; the kid; the carcass)'), (r'Makkot (?:20[ab]|21a)|Mishnah Makkot 3:[56]', 'Makkot (the baldness, the cuttings — the lashes)'), (r'Yevamot (?:13b|14a|47b|86[ab])', 'Yevamot (no factions; the convert; the tithe to the Levite)'), (r'Kiddushin (?:36a|54b)', "Kiddushin (sons of the LORD; the second tithe Heaven's)"), (r'Maaser Sheni|Ma.aser Sheni', 'Maaser Sheni (the second tithe)'), (r'Maasrot|Ma.asrot', "Maasrot (the tithes' liabilities)"), (r'Rosh Hashanah 1[23][ab]', "Rosh Hashanah 12a-13a (the tithe's year)"), (r'Bekhorot (?:34[ab]|35a|53b)|Mishnah Bekhorot 9', 'Bekhorot (the firstling; the cattle tithe)'), (r'Mishnah Temurah 6:1|Mishnah Eduyot 3:2|Mishnah Zevachim 5:8|Pesachim (?:21b|50b|51a)|Bava Metzia 88a|Mishnah Peah 8|Tosefta Peah 4|Tosefta Kilayim 1|Tosefta Sanhedrin 3|Avot 3:(?:9|14)|Sifra', "the docket's other works"),
         (r'\btithe', 'tithe'), (r'\bLevite', 'Levite'), (r'\bfirstling|\bfirstborn of (?:your|the) (?:herd|flock|cattle)', 'firstling'), (r'\bclean\b|\bunclean\b', 'clean / unclean'), (r'\bcarcass|\bcarcase|\bnevelah|\bterefah|\btorn\b', 'carcass / torn'), (r'\bkid\b|mother.s milk|\bmilk\b', 'the kid / the milk'), (r'\bhoof|\bcud\b|\bcloven|\bparted\b', 'hoof / cud'), (r'\bfins?\b|\bscales?\b', 'fins / scales'), (r'\bbirds?\b|\bfowls?\b|\beagle|\bvulture|\bostrich|\bwinged', 'bird / fowl'), (r'\bswine|\bpig\b|\bcamel|\bhare\b|\bconey|\brock badger|\bhyrax', 'the four'), (r'\babominat|\bdetestab|\btoevah|\bsheketz', 'abomination'), (r'holy people|people holy|\btreasured|segulah|\bam segula', 'a holy people / treasured'), (r'cut yourselves|\bgash|\bbald|\bbaldness|\bfor the dead|\bmourn', 'the cuttings / the baldness / the dead'), (r'\bsojourner|\bstranger|\bconvert|\bproselyte|\bger\b|\bresident alien', 'the sojourner'), (r'\bfatherless|\borphan|\bwidow', 'the fatherless / the widow'), (r'\bgates?\b', 'the gates'), (r'\brejoic', 'rejoice'), (r'\bmoney\b|\bsilver\b|\bcoin|\bredeem', 'money / silver / redeem'), (r'\btoo far|\bdistance|\bfar (?:from|off)', 'the far place'), (r'\bthird year|\bthree years|\byear of (?:the )?tithe|\bpoor man.s tithe|\bpoor tithe', 'the third year'), (r'\bgrain\b|\bcorn\b|\bnew wine|\btirosh|\boil\b', 'grain, wine, oil'), (r'\bseed\b|\bfield\b|\byield|\bincrease\b|\bproduce\b', 'seed / field / yield'), (r'\bbless', 'bless'), (r'\bportion\b|\binheritance', 'portion / inheritance'), (r'\bTishri\b|\bNisan\b|\bPassover|\bPesach', 'Tishri / Nisan / Passover')]
KIN_LABELS = ("Lev 11:1-47 (THE TWIN CHAPTER — the beasts' signs, the water's, the birds, the swarmers, the carcass)", 'Lev 17:13-15 (the blood covered; the carcass and the torn eaten — the sojourner too)', 'Lev 19:9-10, 27-28 (the gleanings; the rounding, the cuttings for the dead)', 'Lev 20:25-26 (clean and unclean separated; holy to Me)', "Lev 21:5 (the priests' baldness and cuttings)", 'Lev 22:8 (the carcass and the torn — the priest)', 'Lev 23:22 (the gleanings at the harvest)', "Lev 27:30-33 (the tithe the LORD's; the herd's tithe under the rod)", 'Exod 22:30 (the torn flesh to the dogs; men of holiness)', "Exod 23:19 (the kid in its mother's milk — the first seat; the firstfruits)", 'Exod 34:26 (the kid — the second seat)', "Num 18:20-32 (the Levites' tithe; no portion; the tithe of the tithe)", 'Gen 7:2, 8, 8:20 (clean and unclean beasts — the first seats)', "Gen 14:20, 28:22 (the tenth — Abram's, Jacob's vow)", 'Gen 43:32 (an abomination to the Egyptians)', "Deut 7:6 (a holy people, a treasured people — 14:2's kin)", "Deut 10:9, 18 (the Levite's no portion; the sojourner, the fatherless, the widow)", 'Deut 12:5-7, 11-28 (the place; the tithe at the place; the Levite; the far place; the slaughter; the blood)', 'Deut 15:1, 19-23 / 16:11-14 / 17:1 / 18:1 / 22:6-7 / 23:21 / 24:17-21 / 26:12-14 / 27:7 / 31:10 / 32:9 (the kin ahead)', 'Deut 15-34 (ahead)', "the run's cases (Solomon's table; Samaria's third year; Amos' tithes; Nehemiah's storerooms; Hezekiah's tithes; Malachi's tithe; the swine's flesh; Ezekiel's carcass; Samuel's tenth; Ruth's gleaning)")
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
            if label in KIN_LABELS or label == 'Deut 14': print('     %-34s %s' % (label, dict(found[label])))
NAMES = sorted({n for n, d in HITS.items() if any(l in d for l in KIN_LABELS)} | {'opening_speech', 'obey_horeb', 'covenant_at_horeb', 'decalogue', 'hear_o_israel', 'seven_nations', 'good_land', 'not_righteousness', 'second_tablets', 'blessing_and_curse', 'place_name', 'seducers', 'shemini', 'shemini_day', 'sanctions', 'holiness', 'holiness_b', 'priesthood', 'moadim', 'temurah', 'yovel', 'korach', 'ordinances', 'calendar', 'erection', 'primeval', 'mamre', 'joseph', 'pre_sinai', 'mishpatim', 'mishpatim_2', 'mishpatim_3', 'offerings', 'tzav', 'vayikra5', 'chatat', 'clocks', 'tochacha', 'journeys', 'family', 'vows', 'minchah'})
print('  THE KIN RUNNERS (a hit on a kin label) + the Deuteronomy runners + the kin named by the box + the clock runners: %s' % NAMES)
MODS = []
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    for n in NAMES:
        try: MODS.append((n, importlib.import_module('cold_run_' + n)))
        except Exception as e: print('IMPORT FAILED', n, e, file=sys.stderr)
print('  modules imported: %s' % [n for n, _ in MODS])

print('\n==== (2) THE CALLEES\' DEFS, ASKS, DATA KEYS ====')
BROAD = ('tithe', 'clean', 'eat', 'flesh', 'beast', 'land', 'israel', 'holy', 'levite', 'bless', 'gate', 'seed', 'field', "'14:", "'11:", "'18:", "'27:", "'22:", "'23:", "'19:", "'17:", "'12:", 'installed_by', 'given_at')
PATS = ('Deut 14', 'Deuteronomy 14', 'tithe', 'Levite', 'firstling', 'clean', 'unclean', 'carcass', 'torn', 'kid', 'milk', 'hoof', 'cud', 'fin', 'scale', 'bird', 'fowl', 'eagle', 'swine', 'camel', 'hare', 'coney', 'abominat', 'detestab', 'holy people', 'treasured', 'cut yourselves', 'bald', 'for the dead', 'sojourner', 'stranger', 'convert', 'fatherless', 'widow', 'gate', 'rejoic', 'money', 'silver', 'redeem', 'far', 'third year', 'three years', 'grain', 'wine', 'oil', 'seed', 'field', 'yield', 'bless', 'portion', 'inheritance', 'eat', 'flesh', 'beast', 'israel', 'land', 'holy',
        'installed_by', 'given_at', 'Chullin', 'Makkot 3', 'Yevamot 13', 'Yevamot 14', 'Yevamot 47', 'Yevamot 86', 'Kiddushin 36', 'Kiddushin 54', 'Maaser Sheni', 'Maasrot', 'Rosh Hashanah 12', 'Rosh Hashanah 13', 'Bekhorot', 'Temurah 6', 'Eduyot 3', 'Zevachim 5:8', 'Pesachim 21', 'Pesachim 50', 'Pesachim 51', 'Bava Metzia 88', 'Peah', 'Kilayim', 'Sanhedrin 3:', 'Avot 3', 'Sifra')
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
KP = r'tithe|maaser|levite|firstling|firstborn_of|clean|carcass|nevelah|terefah|torn|kid_|_kid|milk|hoof|cud|scale|bird|fowl|eagle|swine|camel|hare|coney|abomin|detest|holy_people|treasur|segulah|gash|bald|mourn|sojourn|stranger|convert|fatherless|orphan|widow|rejoic|money|silver|redeem|distance|third_year|glean|harvest|corner|dietary|food|flesh|slaughter|locust|swarm|creeping|fins|no_portion|no_inheritance|tenth'
for k in sorted(E):
    if re.search(KP, k): print('    %-44s form %-8s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:100].replace('\n', ' ')))
print('  effects touching the matter:')
for f in sorted(F):
    if re.search(KP, f): print('    %-40s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:110].replace('\n', ' ')))
for k in [k for k in sorted(E) if re.search(KP, k)][:80]:
    print('  a kind row whole (%s): %s' % (k, str(E.get(k))[:600]))
for f in [f for f in sorted(F) if re.search(KP, f)][:60]:
    print('  an effect row (%s): %s' % (f, str(F.get(f))[:400]))

print('\n==== (4) THE REGISTRY MAP for the chapter\'s tokens ====')
reg_map = CS.registry_map()
TOK = ('israel', 'israel_people', 'moses', 'the-lord', 'god', 'the-levite', 'the-levites', 'the-sojourner', 'the-stranger', 'the-fatherless', 'the-widow', 'the-ox', 'the-sheep', 'the-goat', 'the-hart', 'the-gazelle', 'the-roebuck', 'the-camel', 'the-hare', 'the-coney', 'the-swine', 'the-eagle', 'the-vulture', 'the-raven', 'the-ostrich', 'the-bat', 'the-kid', 'the-carcass', 'the-tithe', 'the-firstlings', 'the-herd', 'the-flock', 'the-grain', 'the-wine', 'the-oil', 'the-seed', 'the-field', 'the-money', 'the-silver', 'the-place', 'the-gates', 'the-gate', 'the-dead', 'the-water', 'the-fish', 'the-bird', 'the-birds', 'the-beast', 'the-beasts', 'the-people', 'the-peoples', 'the-earth', 'the-land', 'the-house', 'the-hand', 'the-work', 'the-year', 'the-years', 'the-mother', 'egypt', 'jerusalem', 'shiloh', 'solomon', 'samaria')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])
print('  registry ids with levite/sojourn/stranger/fatherless/widow/ox/sheep/goat/hart/gazelle/camel/hare/coney/swine/eagle/raven/bird/beast/fish/kid/carcass/tithe/herd/flock/grain/wine/oil/seed/field/money/silver/place/gate/dead/water/mother/egypt/jerusalem/shiloh/samaria in them: %s' % sorted({v for v in reg_map.values() if re.search(r'levite|sojourn|stranger|fatherless|widow|\box|sheep|goat|hart|gazelle|camel|hare|coney|swine|eagle|raven|bird|beast|fish|kid|carcass|tithe|herd|flock|grain|wine|oil|seed|field|money|silver|place|gate|dead|water|mother|egypt|jerusalem|shiloh|samaria', str(v))})[:80])

print('\n==== (5) THE TAPE\'S LINES the chapter retells; THE CLOCK\'S DAY at each; the tape\'s LAST lines and markers ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
tl = tape.split('\n')
KINRE = r"'Lev (?:11:\d+|17:1[35]|19:(?:9|10|27|28)|20:2[56]|21:5|22:8|23:22|27:3[0-3])\b|'Exod (?:22:30|23:19|34:26)\b|'Num 18:(?:2[0-9]|3[0-2])\b|'Gen (?:7:[28]|8:20|14:20|28:22|43:32)\b|'Deut (?:7:6|10:(?:9|18)|12:(?:[5-7]|1[1-9]|2[0-8])|14:\d+)\b"
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
print('  the section comments of the kin (Lev 11, 17, 19, 20, 21, 22, 23, 27; Exod 22, 23, 34; Num 18; Gen 7, 8, 14, 28): %s' % [c for c in re.findall(r'# ---- ((?:Exod|Num|Lev|Gen) [^-]+?) ----', tape) if re.search(r'Exod (?:22|23|34)\b|Num 18\b|Lev (?:11|17|19|20|21|22|23|27)\b|Gen (?:7|8|14|28)\b', c)])
print('  DAEMON_ORDER %d, tail %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-3:]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT))
print('  the Lev 11/17/19/20/21/22/23/27, Exod 22/23/34, Num 18, Gen 7/8/14/28, Deut 7/10/12/14 lines with their kinds:')
for l in tl:
    m = re.search(r"w\.(?:event|write|marker|close)\('([a-z_0-9]+)'.*?'((?:Lev (?:11:\d+|17:1[35]|19:(?:9|10|27|28)|20:2[56]|21:5|22:8|23:22|27:3[0-3])|Exod (?:22:30|23:19|34:26)|Num 18:(?:2[0-9]|3[0-2])|Gen (?:7:[28]|8:20|14:20|28:22|43:32)|Deut (?:7:6|10:(?:9|18)|12:(?:[5-7]|1[1-9]|2[0-8])|14:\d+))\b(?:-\d+)?)'", l)
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
print('  the chapter-14-era log rows (EVENT/marker rows whose source is Leviticus 11, the carcass and the torn, the kid, the cuttings, the gleanings, the tithes, the tenth, the clean beasts, the place; the day and its rendering):')
n = 0
for row in w.log:
    if not isinstance(row, (list, tuple)) or len(row) < 3: continue
    tag, day, ev = row[0], row[1], row[2]
    src = str(ev.get('source', ev.get('verse', ''))) if isinstance(ev, dict) else str(ev)
    if re.search(r'Lev (?:11:\d+|17:1[35]\b|19:(?:9|10|27|28)\b|20:2[56]\b|21:5\b|22:8\b|23:22\b|27:3[0-3]\b)|Exod (?:22:30\b|23:19\b|34:26\b)|Num 18:(?:2[0-9]|3[0-2])\b|Gen (?:7:[28]\b|8:20\b|14:20\b|28:22\b|43:32\b)|Deut (?:7:6\b|10:(?:9|18)\b|12:(?:[5-7]|1[1-9]|2[0-8])\b)', src):
        print('    %-6s day %-6s %-32s %s | %s' % (tag, day, ev.get('kind', '?') if isinstance(ev, dict) else '?', src[:22], render(day)))
        n += 1
        if n > 120: break
print('  the marker rows on the log (all tags): %s' % collections.Counter(r[0] for r in w.log if isinstance(r, (list, tuple))).most_common(8))
print('  markers in the world (Exod 19-34): %s' % [(m if isinstance(m, str) else str(m)[:120]) for m in (getattr(w, 'markers', []) or [])][:0])
mk = [x for x in getattr(w, 'markers', []) if re.search(r'Lev (?:11|17|19|20|21|22|23|27)\b|Exod (?:22|23|34)\b|Num 18\b|Gen (?:7|8|14|28)\b|Deut', str(x))] if hasattr(w, 'markers') else []
print('  the markers Exod 19, 23-24, 34, 40, Num 9-10, 16, 18, 20, 33, Lev 17, 26, Deut: %s' % [str(x)[:160] for x in mk][:80])
print('  THE MARKERS THE KIN SIT UNDER: the sequence file\'s M[] lines naming the erection, the tent, Sinai, the calf, the cloud, the journey, the ark, Korah, Peor, Hormah, the speech: %s' % [l.strip()[:200] for l in src_cs.split('\n') if re.search(r"M\['[a-z_0-9]*(?:erect|tent|tabernacle|sinai|calf|cloud|journey|ark|korah|peor|hormah|balaam|speech_resumed|plains|moab)[a-z_0-9]*'\] = ", l)][:40])
print('  CAL_PARAMS rows naming erect/tishri/nisan/year/season: %s' % [(k, v) for k, v in getattr(CS, 'CAL_PARAMS', {}).items() if re.search(r'erect|tishri|nisan|year|season', str(k) + str(v))][:8])
print('  the tape lines naming the tithe / the Levite / the firstling / the carcass / the kid / the milk / the hoof / the cud / fins / scales / birds / the four / abomination / a holy people / the baldness / the cuttings / the sojourner / the fatherless / the widow / Solomon / Samaria / Hezekiah / Nehemiah / Malachi: %s' % [l.strip()[:200] for l in tl if re.search(r'tithe|Levite|firstling|carcass|\bkid\b|milk|hoof|\bcud\b|\bfins?\b|scales|\bbirds?\b|swine|camel|\bhare\b|coney|abominat|holy people|treasured|baldness|cut yourselves|sojourner|fatherless|widow|Solomon|Samaria|Hezekiah|Nehemiah|Malachi', l)][:60])
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
for dn in ('law_seducers', 'law_place_name', 'law_shemini', 'law_shemini_day', 'law_sanctions', 'law_holiness', 'law_holiness_b', 'law_priesthood', 'law_moadim', 'law_temurah', 'law_yovel', 'law_korach', 'law_ordinances', 'law_calendar', 'law_second_tablets', 'law_seven_nations', 'law_blessing_and_curse', 'law_primeval', 'law_mamre'):
    print('  the daemon block %s: %s' % (dn, str(dd['daemons'].get(dn))[:500]))
print('  the functions blocks seducers / shemini / korach / temurah: %s' % [(k, str(dd.get('functions', {}).get(k))[:400]) for k in ('seducers', 'shemini', 'korach', 'temurah')])
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers naming Deut 14: %s; edges naming Deut 14: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if re.search(r'Deut 14:', str(p))][:10], [e for e in dep['edges'] if re.search(r'Deut 14:', str(e))][:5]))
print('  the seducers edges on file (the form): %s\n  the shemini edges on file: %s\n  the edges INTO shemini: %s' % ([(e['from'], e['to'], e['disposition'], e['link'], str(e.get('why', ''))[:90]) for e in dep['edges'] if e['from'] == 'seducers'], [(e['from'], e['to'], e['disposition'], e['link'], str(e.get('why', ''))[:90]) for e in dep['edges'] if e['from'] == 'shemini'], [(e['from'], e['to'], e['disposition'], e['link'], str(e.get('why', ''))[:90]) for e in dep['edges'] if e['to'] == 'shemini']))
print('  a CALL edge row WHOLE (seducers): %s' % [e for e in dep['edges'] if e['from'] == 'seducers' and e.get('disposition') == 'CALL'][:1])
print('  a RUN_CITATION pointer row WHOLE (seducers): %s' % [p for p in dep['pointers'] if p.get('runner') == 'seducers'][:1])
print('  the spans of the kin: %s' % {k: dep['spans'].get(k) for k in NAMES})
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the register seats naming Deut 14 (WHOLE): %s' % [(sec, k, v) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.startswith('Deut 14')])
print('  the register seats naming the kin (Lev 11:1-2, 46-47, 17:15, 19:9, 19:27, 20:25, 21:5, 22:8, 23:22, 27:30; Exod 22:30, 23:19, 34:26; Num 18:20-21, 26; Deut 7:6, 10:9, 12:1, 12:5, 12:17, 12:21): %s' % [(sec, k, v) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.split(' ')[0] + ' ' + k.split(' ')[1] in ('Lev 11:1', 'Lev 11:2', 'Lev 11:46', 'Lev 11:47', 'Lev 17:15', 'Lev 19:9', 'Lev 19:27', 'Lev 20:25', 'Lev 21:5', 'Lev 22:8', 'Lev 23:22', 'Lev 27:30', 'Exod 22:30', 'Exod 23:19', 'Exod 34:26', 'Num 18:20', 'Num 18:21', 'Num 18:26', 'Deut 7:6', 'Deut 10:9', 'Deut 12:1', 'Deut 12:5', 'Deut 12:17', 'Deut 12:21')][:30])
print('  the receipt finder\'s defs in register_census.py: %s' % re.findall(r'^def ([a-z_0-9]+)\(', open(f'{ROOT}/World/step9/register_census.py', encoding='utf-8').read(), re.M))

print('\n==== (7) THE READBACK PROBES on file; the ledgers naming 14:n / the tithes / the kid / the signs / the carcass; the kin\'s ledgers ====')
rp = open(f'{ROOT}/World/step9/readback_probes.py', encoding='utf-8').read()
print('  readback_probes: the Q labels: %s' % sorted(set(re.findall(r"'(Q\d+)", rp)), key=lambda s: int(s[1:])))
print('  the Q34-Q36 heads: %s' % [l.strip()[:200] for l in rp.split('\n') if re.search(r"'Q3[4-6]", l)][:6])
print('  the probes holding a marker count or a marker list literal: %s' % [l.strip()[:160] for l in rp.split('\n') if re.search(r'markers?\W+1[0-9]{2}\b|172\b|169\b', l)][:12])
print('  the readback forms on THE_LOOP\'s step-6 row: %s' % [l.strip()[:220] for l in open(f'{ROOT}/World/step9/THE_LOOP.md', encoding='utf-8').read().split('\n') if 'COMBINE' in l or 'combined' in l.lower()][:3])
for f in sorted(glob.glob(f'{ROOT}/logic/oral_triage/*.md')):
    t = open(f, encoding='utf-8').read()
    n = len(re.findall(r'Deut(?:eronomy)? 14:\d+|second tithe|poor man.s tithe|tithe of the poor|in its mother.s milk|cloven|chews the cud|fins and scales|clean bird|carcass', t))
    if n: print('  ledger naming Deut 14:n / the second tithe / the poor man\'s tithe / the kid / the signs / the clean bird / the carcass: %s (%d)' % (os.path.basename(f), n))
print('  the kin\'s ledgers (Leviticus 11, 17, 19-23, 27; Exodus 22-23, 34; Numbers 18; Genesis 7-8, 14, 28; Deuteronomy 7-13): %s' % [os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_triage/*.md') if re.search(r'lev_11|shemini|lev_17|lev_19|lev_20|lev_21|lev_22|lev_23|lev_27|holiness|priest|moadim|temurah|yovel|exo_22|exo_23|exo_34|mishpatim|ordinances|calendar|num_18|korach|gen_07|gen_08|gen_14|gen_28|noah|deu_0[7-9]|deu_1[0-3]', os.path.basename(f))])
