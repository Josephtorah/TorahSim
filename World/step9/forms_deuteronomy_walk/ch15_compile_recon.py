#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13b — THE COMPILE OF CHAPTER 15, Deuteronomy 15:1-23 (2026-09-22; the owner: "Go" after sitting 13's commit b0eaa56): THE
# RECONNAISSANCE before the design (ch14_compile_recon.py's form on chapter 15, typed in two parts — ch15_compile_recon_p1.py and _p2.py — and assembled) — (1)
# WHICH RUNNER HOLDS A CELL FOR THE CHAPTER'S MATTER (the sabbatical year and the jubilee — Leviticus 25:1-17; the poor brother, the interest, the sold brother —
# Leviticus 25:35-55; the Hebrew slave, the maidservant, the awl — Exodus 21:2-11; the loan and the pledge — Exodus 22:24-26; the seventh year's land — Exodus
# 23:10-11; the firstborn of man and beast — Exodus 13:2, 11-16, 22:28-29, 34:19-20, Numbers 3:12-13, 8:16-17; the firstling the priest's — Numbers 18:15-18; the
# firstling no man sanctifies — Leviticus 27:26-27; the blemishes — Leviticus 22:17-27, 21:16-23; the leper's right ear — Leviticus 14:14-28; the gleanings and
# the hireling's wages — Leviticus 19:9-10, 13, 23:22; Abel's firstlings, the servitude, Egypt's slaves — Genesis 4:4, 15:13-14, 47:19-26; a slave in Egypt 5:15;
# the second paragraph 11:13-17; the firstlings at the place, the blemished in the gates, the blood on the ground 12:6, 15-18, 22-24; base fellows 13:13-14; the
# tithe and the third year 14:22-29) — every runner's ink refs scanned by regex, per def; (2) the callee modules' defs, asks, DATA keys; (3) the kinds and effects
# on file touching the matter; (4) the registry map; (5) the tape's lines of the kin with THE CLOCK'S DAY at each, THE RUNNING WORLD'S SABBATICAL COUNT (the
# clock's year and the calendar parameters — the release's year a date parameter read from the world), the tape's LAST lines and markers; (6) the sequence
# file's tuples, the checkpoint prefixes in use (the D series — DF the open series, the next DG), the M[] names, the daemons; (7) the dispositions and register
# seats naming Deut 15 (none expected — the reading's finder found no receipt, no header, no footer; 15:6's "as He spoke to you" and 15:2's "this is the
# manner" outside the finder's forms — THE FINDER'S FORMS PRINTED), the readback probes' tail, the ledgers naming 15:n / the release / the prozbul / the Hebrew
# slave / the awl / the firstling, the kin's ledgers.
import sys, io, re, contextlib, inspect, collections, yaml, glob, subprocess, os, importlib
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()   # RUN FROM THE REPO ROOT; no absolute repo path typed
sys.path.insert(0, f'{ROOT}/World/step9')

print('==== (1) THE CHAPTER\'S MATTER — every runner\'s refs, per def ====')
SEATS = [(r'Deut(?:eronomy)? 15:(\d+)', 'Deut 15'),
         (r'Lev(?:iticus)? 25:(?:[1-9]|1[0-7]|3[5-9]|4[0-9]|5[0-5])\b', 'Lev 25:1-17, 35-55 (the sabbatical; the jubilee; the poor brother and the interest; the sold brother)'), (r"ink\('25:(?:[1-9]|1[0-7]|3[5-9]|4[0-9]|5[0-5])'", "Lev 25 (ink — the runner's own book)"),
         (r'Lev(?:iticus)? 27:2[67]\b', 'Lev 27:26-27 (the firstling no man sanctifies; the unclean beast redeemed)'), (r"ink\('27:2[67]'", 'Lev 27:26-27 (ink)'),
         (r'Lev(?:iticus)? (?:22:(?:1[7-9]|2[0-7])|21:(?:1[6-9]|2[0-3]))\b', 'Lev 22:17-27, 21:16-23 (the blemishes — the offering; the priest)'), (r"ink\('2[12]:(?:1[6-9]|2[0-7])'", 'Lev 21-22 blemishes (ink)'),
         (r'Lev(?:iticus)? 14:(?:14|17|25|28)\b', "Lev 14:14-28 (the leper's right ear, thumb and toe — the awl's analogy)"),
         (r'Lev(?:iticus)? (?:19:(?:9|10|13)|23:22)\b', "Lev 19:9-10, 13, 23:22 (the gleanings; the hireling's wages)"),
         (r'Exod(?:us)? 21:(?:[2-9]|1[01])\b', 'Exod 21:2-11 (the Hebrew slave; the awl; the maidservant)'), (r"ink\('21:(?:[2-9]|1[01])'", 'Exod 21:2-11 (ink)'),
         (r'Exod(?:us)? 22:2[4-6]\b', 'Exod 22:24-26 (the loan to the poor; no interest; the pledge returned by sunset)'), (r"ink\('22:2[4-6]'", 'Exod 22:24-26 (ink)'),
         (r'Exod(?:us)? 23:1[01]\b', "Exod 23:10-11 (the seventh year — the land let go, the poor eat)"), (r"ink\('23:1[01]'", 'Exod 23:10-11 (ink)'),
         (r'Exod(?:us)? (?:13:(?:2|1[1-6])|22:2[89]|34:(?:19|20))\b', 'Exod 13:2, 11-16 / 22:28-29 / 34:19-20 (the firstborn of man and beast)'), (r"ink\('(?:13:(?:2|1[1-6])|34:(?:19|20))'", 'Exod 13 / 34 firstborn (ink)'),
         (r'Num(?:bers)? 18:1[5-8]\b', "Num 18:15-18 (the firstling the priest's — its blood dashed, its flesh his)"), (r"ink\('18:1[5-8]'", 'Num 18:15-18 (ink)'),
         (r'Num(?:bers)? (?:3:1[23]|8:1[67])\b', 'Num 3:12-13, 8:16-17 (the firstborn of Israel Mine — the Levites instead)'),
         (r'Gen(?:esis)? (?:4:4|15:1[34]|47:(?:19|2[0-6]))\b', "Gen 4:4, 15:13-14, 47:19-26 (Abel's firstlings; the servitude foretold; Egypt's slaves)"),
         (r'Deut(?:eronomy)? 5:15\b', "Deut 5:15 (a slave in Egypt — the Sabbath's ground; 15:15's kin)"), (r'Deut(?:eronomy)? 11:1[3-7]\b', "Deut 11:13-17 (the second paragraph — the rain; the release after the conquest at 41:3)"),
         (r'Deut(?:eronomy)? 12:(?:6|1[5-8]|2[2-4])\b', 'Deut 12:6, 15-18, 22-24 (the firstlings at the place; the blemished in the gates; the blood on the ground)'), (r'Deut(?:eronomy)? 13:1[34]\b', "Deut 13:13-14 (base fellows — 15:9's analogy)"),
         (r'Deut(?:eronomy)? 14:2[2-9]\b', 'Deut 14:22-29 (the tithe; the third year; the four at the gate)'),
         (r'Deut(?:eronomy)? (?:16:(?:5|1[0-4])|17:1|17:18|21:3|23:1[6-9]|23:2[0-2]|24:(?:6|1[0-9]|2[0-2])|26:1[2-9]|28:(?:[1-9]|1[0-2])|29:1[12]|31:1[0-3])\b', 'Deut 16:5, 10-14 / 17:1, 18 / 21:3 / 23:16-22 / 24:6, 10-22 / 26:12-19 / 28:1-12 / 29:11-12 / 31:10-13 (the kin ahead)'), (r'Deut(?:eronomy)? (?:1[6-9]|2[0-9]|3[0-4]):\d+\b', 'Deut 16-34 (ahead)'),
         (r'Jer(?:emiah)? 34:(?:[89]|1[0-9]|2[0-2])\b|2 Kings 4:1\b|Neh(?:emiah)? (?:5:(?:[1-9]|1[0-3])|10:32)\b|Judg(?:es)? 1:7\b|1 Sam(?:uel)? 22:2\b|2 Chron(?:icles)? 36:21\b|Ezek(?:iel)? 46:17\b|Amos 2:6\b|Isa(?:iah)? 61:1\b', "the run's cases (Zedekiah's release; the widow's creditor; Nehemiah's release; Adoni-bezek; David's debtors; the land's sabbaths; the year of liberty; Amos' sale for silver)"),
         (r'Sheviit|Shevi.it', 'Sheviit (the seventh year; the release; the prozbul)'), (r'Gittin 3[67][ab]', 'Gittin 36a-37b (the prozbul; the release by decree)'), (r'Arakhin (?:32b|33a)|Mishnah Arakhin 8:7', "Arakhin (the jubilee's condition; sanctify for its value)"), (r'Makkot 3b', "Makkot 3b (the loan's witnesses; the release's condition)"), (r'Rosh Hashanah (?:8b|9a)', "Rosh Hashanah 8b-9a (the year's edge for the release)"),
         (r'Kiddushin (?:1[4-9][ab]|2[0-2][ab])|Mishnah Kiddushin 1:[23]', 'Kiddushin (the Hebrew slave; the maidservant; the awl)'), (r'Bava Metzia (?:31b|71a)', 'Bava Metzia (the pledge; the poor of your city first)'), (r'Ketubot 67b|Mishnah Peah 8:[7-9]', 'Ketubot 67b / Mishnah Peah 8 (the measure of need)'), (r'Bekhorot (?:2[5-8][ab]|3[3-7][ab]|53b)|Mishnah Bekhorot', 'Bekhorot (the firstling; its year; its blemishes; its shearing and work)'), (r'Mishnah Temurah 3:5|Mishnah Shekalim 5:6|Mishnah Chullin 2:9|Sifra|Mekhilta', "the docket's other works"),
         (r'\brelease\b|\bremission\b|\bshemitt?ah|\bshmit', 'release'), (r'\bcreditor|\bdebtor|\bdebt\b|\bloan\b|\blend|\bborrow', 'debt / loan / lend'), (r'\bprozbul|\bprosbul', 'the prozbul'), (r'\bseventh year|\bsabbatical|\byear of release', 'the seventh year'), (r'\bjubilee|\byovel', 'the jubilee'), (r'\bneedy\b|\bpoor\b|\bdestitute', 'the needy / the poor'), (r'\bpledge|\bsurety|\bcollateral', 'the pledge'), (r'\bHebrew (?:slave|servant|man|woman)|\bslave\b|\bservant\b|\bbondman|\bmaidservant|\bbondwoman', 'the slave / the servant'), (r'\bawl\b|\bpierce|\bbore\b|\bear\b', 'the awl / the ear'), (r'\bfor ever\b|\bforever\b|\bperpetual', 'for ever'), (r'\bhire(?:d|ling)?\b|\bwages?\b', 'the hireling / the wages'), (r'\bfirstling|\bfirstborn|\bfirst-born|\bbekhor', 'the firstling / the firstborn'), (r'\bblemish|\blame\b|\bblind\b|\bdefect', 'the blemish'), (r'\bblood\b', 'the blood'), (r'\bshear|\bfleece|\bwool\b|\bplow|\bplough|\bwork with|\blabou?r with', 'the shearing / the work'), (r'\bsanctif|\bconsecrat', 'sanctify / consecrate'), (r'\bgates?\b', 'the gates'), (r'\bbrother\b', 'the brother'), (r'\bforeigner|\bstranger|\bsojourner|\bgentile|\balien\b', 'the foreigner / the sojourner'), (r'\bbless', 'bless'), (r'\bheart\b', 'the heart'), (r'\bhand\b', 'the hand'), (r'\bEgypt', 'Egypt'), (r'\bredeem', 'redeem'), (r'\bsin\b|\btransgress', 'sin'), (r'\bcry\b|\bcries\b', 'the cry'), (r'\byear by year|\bevery year|\byearly', 'year by year'), (r'\bunclean\b|\bclean\b', 'clean / unclean'), (r'\bgazelle|\bhart\b|\bdeer\b', 'the gazelle / the hart'), (r'\bTishri\b|\bNisan\b|\bElul\b', 'Tishri / Nisan / Elul')]
KIN_LABELS = ('Lev 25:1-17, 35-55 (the sabbatical; the jubilee; the poor brother and the interest; the sold brother)', 'Lev 27:26-27 (the firstling no man sanctifies; the unclean beast redeemed)', 'Lev 22:17-27, 21:16-23 (the blemishes — the offering; the priest)', "Lev 14:14-28 (the leper's right ear, thumb and toe — the awl's analogy)", "Lev 19:9-10, 13, 23:22 (the gleanings; the hireling's wages)", 'Exod 21:2-11 (the Hebrew slave; the awl; the maidservant)', 'Exod 22:24-26 (the loan to the poor; no interest; the pledge returned by sunset)', "Exod 23:10-11 (the seventh year — the land let go, the poor eat)", 'Exod 13:2, 11-16 / 22:28-29 / 34:19-20 (the firstborn of man and beast)', "Num 18:15-18 (the firstling the priest's — its blood dashed, its flesh his)", 'Num 3:12-13, 8:16-17 (the firstborn of Israel Mine — the Levites instead)', "Gen 4:4, 15:13-14, 47:19-26 (Abel's firstlings; the servitude foretold; Egypt's slaves)", "Deut 5:15 (a slave in Egypt — the Sabbath's ground; 15:15's kin)", "Deut 11:13-17 (the second paragraph — the rain; the release after the conquest at 41:3)", 'Deut 12:6, 15-18, 22-24 (the firstlings at the place; the blemished in the gates; the blood on the ground)', "Deut 13:13-14 (base fellows — 15:9's analogy)", 'Deut 14:22-29 (the tithe; the third year; the four at the gate)', 'Deut 16:5, 10-14 / 17:1, 18 / 21:3 / 23:16-22 / 24:6, 10-22 / 26:12-19 / 28:1-12 / 29:11-12 / 31:10-13 (the kin ahead)', 'Deut 16-34 (ahead)', "the run's cases (Zedekiah's release; the widow's creditor; Nehemiah's release; Adoni-bezek; David's debtors; the land's sabbaths; the year of liberty; Amos' sale for silver)")
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
            if label in KIN_LABELS or label == 'Deut 15': print('     %-34s %s' % (label, dict(found[label])))
NAMES = sorted({n for n, d in HITS.items() if any(l in d for l in KIN_LABELS)} | {'opening_speech', 'obey_horeb', 'covenant_at_horeb', 'decalogue', 'hear_o_israel', 'seven_nations', 'good_land', 'not_righteousness', 'second_tablets', 'blessing_and_curse', 'place_name', 'seducers', 'food_tithe', 'shemini', 'shemini_day', 'sanctions', 'holiness', 'holiness_b', 'priesthood', 'moadim', 'temurah', 'yovel', 'korach', 'ordinances', 'calendar', 'erection', 'primeval', 'mamre', 'joseph', 'pre_sinai', 'mishpatim', 'mishpatim_2', 'mishpatim_3', 'offerings', 'tzav', 'vayikra5', 'chatat', 'clocks', 'tochacha', 'journeys', 'family', 'vows', 'minchah'})
print('  THE KIN RUNNERS (a hit on a kin label) + the Deuteronomy runners + the kin named by the box + the clock runners: %s' % NAMES)
MODS = []
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    for n in NAMES:
        try: MODS.append((n, importlib.import_module('cold_run_' + n)))
        except Exception as e: print('IMPORT FAILED', n, e, file=sys.stderr)
print('  modules imported: %s' % [n for n, _ in MODS])

print('\n==== (2) THE CALLEES\' DEFS, ASKS, DATA KEYS ====')
BROAD = ('year', 'land', 'israel', 'holy', 'bless', 'gate', 'hand', 'heart', 'eat', 'flesh', 'beast', 'clean', "'15:", "'25:", "'21:", "'22:", "'23:", "'27:", "'18:", "'13:", "'12:", "'14:", 'installed_by', 'given_at')
PATS = ('Deut 15', 'Deuteronomy 15', 'release', 'remission', 'shemit', 'sabbatical', 'seventh year', 'jubilee', 'yovel', 'creditor', 'debtor', 'debt', 'loan', 'lend', 'borrow', 'prozbul', 'pledge', 'needy', 'poor', 'Hebrew', 'slave', 'servant', 'maidservant', 'bondman', 'awl', 'pierce', 'ear', 'for ever', 'forever', 'hireling', 'hired', 'wages', 'firstling', 'firstborn', 'bekhor', 'blemish', 'lame', 'blind', 'blood', 'shear', 'wool', 'plow', 'sanctif', 'consecrat', 'brother', 'foreigner', 'stranger', 'sojourner', 'Egypt', 'redeem', 'sin', 'cry', 'year by year', 'gazelle', 'hart', 'Tishri', 'Nisan', 'Elul', 'year', 'land', 'israel', 'holy', 'bless', 'gate', 'hand', 'heart', 'eat', 'flesh', 'beast', 'clean',
        'installed_by', 'given_at', 'Sheviit', 'Gittin 36', 'Gittin 37', 'Arakhin', 'Makkot 3', 'Rosh Hashanah 8', 'Rosh Hashanah 9', 'Kiddushin 1', 'Kiddushin 2', 'Bava Metzia 31', 'Bava Metzia 71', 'Ketubot 67', 'Peah', 'Bekhorot', 'Temurah 3', 'Shekalim 5', 'Chullin 2', 'Sifra', 'Mekhilta')
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
KP = r'release|remission|shemit|sabbatical|seventh_year|jubilee|yovel|debt|loan|lend|borrow|creditor|pledge|needy|poor|slave|servant|bond|maidservant|awl|pierce|_ear|ear_|hire|wage|firstling|firstborn|bekhor|blemish|blood|shear|sanctif|consecrat|gate|brother|foreigner|stranger|sojourn|bless|heart|hand_open|egypt|redeem|sin_|_sin|cry|clean|gazelle|hart|slaughter|interest|usury|surety|tithe|levite|liberty|freed|free_'
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
TOK = ('israel', 'israel_people', 'moses', 'the-lord', 'god', 'the-creditor', 'the-neighbor', 'the-brother', 'the-foreigner', 'the-stranger', 'the-sojourner', 'the-needy', 'the-poor', 'the-hebrew', 'the-slave', 'the-servant', 'the-maidservant', 'the-master', 'the-awl', 'the-ear', 'the-door', 'the-hireling', 'the-firstling', 'the-firstborn', 'the-herd', 'the-flock', 'the-ox', 'the-sheep', 'the-goat', 'the-gazelle', 'the-hart', 'the-blood', 'the-blemish', 'the-land', 'the-earth', 'the-place', 'the-gates', 'the-gate', 'the-house', 'the-hand', 'the-heart', 'the-work', 'the-year', 'the-years', 'the-loan', 'the-debt', 'the-money', 'the-silver', 'the-water', 'the-threshing-floor', 'the-winepress', 'the-levite', 'egypt', 'jerusalem', 'zedekiah', 'jeremiah', 'nehemiah', 'hillel')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])
print('  registry ids with creditor/neighbor/brother/foreigner/stranger/sojourn/needy/poor/hebrew/slave/servant/maid/master/awl/ear/door/hireling/firstling/firstborn/herd/flock/ox/sheep/goat/gazelle/hart/blood/blemish/land/place/gate/house/hand/heart/work/year/loan/debt/money/silver/water/threshing/winepress/levite/egypt/jerusalem/zedekiah/jeremiah/nehemiah/hillel in them: %s' % sorted({v for v in reg_map.values() if re.search(r'creditor|neighbor|brother|foreigner|stranger|sojourn|needy|poor|hebrew|slave|servant|maid|master|awl|\bear|door|hireling|firstling|firstborn|herd|flock|\box|sheep|goat|gazelle|hart|blood|blemish|land|place|gate|house|hand|heart|work|year|loan|debt|money|silver|water|threshing|winepress|levite|egypt|jerusalem|zedekiah|jeremiah|nehemiah|hillel', str(v))})[:80])

print('\n==== (5) THE TAPE\'S LINES of the kin; THE CLOCK\'S DAY at each; THE SABBATICAL COUNT; the tape\'s LAST lines and markers ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
tl = tape.split('\n')
KINRE = r"'Lev (?:25:\d+|27:2[67]|22:(?:1[7-9]|2[0-7])|21:(?:1[6-9]|2[0-3])|14:(?:14|17|25|28)|19:(?:9|10|13)|23:22)\b|'Exod (?:21:(?:[2-9]|1[01])|22:2[4-9]|23:1[01]|13:(?:2|1[1-6])|34:(?:19|20))\b|'Num (?:18:1[5-8]|3:1[23]|8:1[67])\b|'Gen (?:4:4|15:1[34]|47:(?:19|2[0-6]))\b|'Deut (?:5:15|11:1[3-7]|12:(?:6|1[5-8]|2[2-4])|13:1[34]|14:2[2-9]|15:\d+)\b"
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
print('  the section comments of the kin (Lev 14, 19, 21, 22, 23, 25, 27; Exod 13, 21, 22, 23, 34; Num 3, 8, 18; Gen 4, 15, 47): %s' % [c for c in re.findall(r'# ---- ((?:Exod|Num|Lev|Gen) [^-]+?) ----', tape) if re.search(r'Exod (?:13|21|22|23|34)\b|Num (?:3|8|18)\b|Lev (?:14|19|21|22|23|25|27)\b|Gen (?:4|15|47)\b', c)])
print('  DAEMON_ORDER %d, tail %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-3:]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT))
print('  the kin lines with their kinds:')
for l in tl:
    m = re.search(r"w\.(?:event|write|marker|close)\('([a-z_0-9]+)'.*?'((?:Lev (?:25:\d+|27:2[67]|22:(?:1[7-9]|2[0-7])|21:(?:1[6-9]|2[0-3])|14:(?:14|17|25|28)|19:(?:9|10|13)|23:22)|Exod (?:21:(?:[2-9]|1[01])|22:2[4-9]|23:1[01]|13:(?:2|1[1-6])|34:(?:19|20))|Num (?:18:1[5-8]|3:1[23]|8:1[67])|Gen (?:4:4|15:1[34]|47:(?:19|2[0-6]))|Deut (?:5:15|11:1[3-7]|12:(?:6|1[5-8]|2[2-4])|13:1[34]|14:2[2-9]|15:\d+))\b(?:-\d+)?)'", l)
    if m: print('    %-34s %-14s %s' % (m.group(1), m.group(2), l.strip()[:150]))
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
print('  THE RUNNING WORLD\'S SABBATICAL COUNT — the clock now: day %s -> %s' % (getattr(w.clock, 'day', '?'), render(getattr(w.clock, 'day', 0))))
calp = f'{ROOT}/World/step9/calendar_parameters.yaml'
cal = yaml.safe_load(open(calp, encoding='utf-8')) if os.path.exists(calp) else {}
print('  calendar_parameters.yaml: %s; keys %s' % (os.path.exists(calp), list(cal)[:40] if isinstance(cal, dict) else type(cal).__name__))
if isinstance(cal, dict):
    for k, v in cal.items():
        if re.search(r'year|sabbat|shemit|release|jubilee|yovel|tishri|count|epoch|seven', str(k) + str(v), re.I): print('    calendar row %s: %s' % (k, str(v)[:300]))
print('  CAL_PARAMS (the sequence file) rows naming year/sabbat/jubilee/epoch/tishri/shemit: %s' % [(k, str(v)[:160]) for k, v in getattr(CS, 'CAL_PARAMS', {}).items() if re.search(r'year|sabbat|jubilee|yovel|epoch|tishri|shemit', str(k) + str(v), re.I)][:20])
led = getattr(w, 'ledger', None)
if isinstance(led, dict): print('  the ledger rows on the running world naming sabbat/shemit/release/jubilee/seventh/yovel: %s' % [(k, str(v)[:160]) for k, v in led.items() if re.search(r'sabbat|shemit|release|jubilee|yovel|seventh', str(k) + str(v), re.I)][:20])
else: print('  no w.ledger dict: %s; world attrs: %s' % (type(led).__name__, [a for a in dir(w) if not a.startswith('_')][:40]))
yp = f'{ROOT}/World/step9/cold_run_yovel.py'
if os.path.exists(yp):
    ys = open(yp, encoding='utf-8').read().split('\n')
    print('  THE YOVEL CELL\'S CLOCK READS (cold_run_yovel.py lines naming clock/year/sabbat/jubilee/count, code only): %d lines' % len([l for l in ys if re.search(r'clock|sabbat|jubilee|yovel_count|year_count|count', l, re.I) and not l.strip().startswith('#')]))
    for l in [l for l in ys if re.search(r'clock|sabbat|jubilee|year', l, re.I) and not l.strip().startswith('#')][:40]: print('    %s' % l.strip()[:200])
else: print('  no cold_run_yovel.py')
print('  the chapter-15-era log rows (EVENT/marker rows whose source is a kin verse; the day and its rendering):')
n = 0
for row in w.log:
    if not isinstance(row, (list, tuple)) or len(row) < 3: continue
    tag, day, ev = row[0], row[1], row[2]
    src = str(ev.get('source', ev.get('verse', ''))) if isinstance(ev, dict) else str(ev)
    if re.search(r'Lev (?:25:\d+|27:2[67]|22:(?:1[7-9]|2[0-7])|21:(?:1[6-9]|2[0-3])|14:(?:14|17|25|28)|19:(?:9|10|13)|23:22)\b|Exod (?:21:(?:[2-9]|1[01])|22:2[4-9]|23:1[01]|13:(?:2|1[1-6])|34:(?:19|20))\b|Num (?:18:1[5-8]|3:1[23]|8:1[67])\b|Gen (?:4:4|15:1[34]|47:(?:19|2[0-6]))\b|Deut (?:5:15|11:1[3-7]|12:(?:6|1[5-8]|2[2-4])|13:1[34]|14:2[2-9])\b', src):
        print('    %-6s day %-6s %-32s %s | %s' % (tag, day, ev.get('kind', '?') if isinstance(ev, dict) else '?', src[:22], render(day)))
        n += 1
        if n > 120: break
print('  the marker rows on the log (all tags): %s' % collections.Counter(r[0] for r in w.log if isinstance(r, (list, tuple))).most_common(8))
mk = [x for x in getattr(w, 'markers', []) if re.search(r'Lev (?:14|19|21|22|23|25|27)\b|Exod (?:13|21|22|23|34)\b|Num (?:3|8|18)\b|Gen (?:4|15|47)\b|Deut', str(x))] if hasattr(w, 'markers') else []
print('  the markers of the kin and of Deut: %s' % [str(x)[:160] for x in mk][:80])
print('  THE MARKERS THE KIN SIT UNDER: the sequence file\'s M[] lines naming the erection, the tent, Sinai, the calf, the cloud, the journey, the ark, Korah, Peor, Hormah, the speech: %s' % [l.strip()[:200] for l in src_cs.split('\n') if re.search(r"M\['[a-z_0-9]*(?:erect|tent|tabernacle|sinai|calf|cloud|journey|ark|korah|peor|hormah|balaam|speech_resumed|plains|moab)[a-z_0-9]*'\] = ", l)][:40])
print('  the tape lines naming the release / the seventh year / the jubilee / the debt / the loan / the pledge / the slave / the servant / the awl / the hireling / the firstling / the firstborn / the blemish / the blood / Zedekiah / Jeremiah / Nehemiah / Hillel: %s' % [l.strip()[:200] for l in tl if re.search(r'release|seventh year|sabbatical|jubilee|\bdebt|\bloan|pledge|\bslave|\bservant|\bawl\b|hireling|firstling|firstborn|blemish|\bblood\b|Zedekiah|Jeremiah|Nehemiah|Hillel', l)][:60])

print('\n==== (6) THE CHECKPOINT PREFIXES, THE M[] NAMES, THE DAEMONS ====')
used = collections.Counter(re.findall(r"cp\('([A-Z]+)\d", src_cs))
print('  cp() checkpoint prefixes in use: %s' % sorted(used.items()))
usedD = sorted((p, n) for p, n in used.items() if p.startswith('D'))
print('  THE D SERIES in use: %s; the next name: %s' % (usedD, next(('D' + x) for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if ('D' + x) not in used)))
print('  the VERDICTS list prefixes: %s' % sorted(collections.Counter(re.findall(r"'([A-Z]+)\d[a-z\-0-9]* (?:MATCH|DIVERGE)'", src_cs)).items()))
print('  M[] marker names on file: %s' % re.findall(r"M\['([a-z_0-9:]+)'\] = ", src_cs))
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  daemons %d; installed_by values: %s' % (len(dd['daemons']), dict(collections.Counter(str(v.get('installed_by')).split()[0] for v in dd['daemons'].values()))))
for dn in ('law_food_tithe', 'law_seducers', 'law_place_name', 'law_yovel', 'law_ordinances', 'law_mishpatim', 'law_mishpatim_2', 'law_mishpatim_3', 'law_temurah', 'law_vows', 'law_korach', 'law_holiness', 'law_holiness_b', 'law_priesthood', 'law_pre_sinai', 'law_calendar', 'law_shemini', 'law_sanctions', 'law_blessing_and_curve', 'law_blessing_and_curse', 'law_primeval'):
    if dd['daemons'].get(dn) is not None: print('  the daemon block %s: %s' % (dn, str(dd['daemons'].get(dn))[:500]))
    else: print('  no daemon block %s' % dn)
print('  the functions blocks food_tithe / yovel / ordinances / mishpatim / korach: %s' % [(k, str(dd.get('functions', {}).get(k))[:400]) for k in ('food_tithe', 'yovel', 'ordinances', 'mishpatim', 'korach')])
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers naming Deut 15: %s; edges naming Deut 15: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if re.search(r'Deut 15:', str(p))][:10], [e for e in dep['edges'] if re.search(r'Deut 15:', str(e))][:5]))
print('  the food_tithe edges on file (the form): %s\n  the edges INTO yovel: %s\n  the edges INTO ordinances / mishpatim: %s' % ([(e['from'], e['to'], e['disposition'], e['link'], str(e.get('why', ''))[:90]) for e in dep['edges'] if e['from'] == 'food_tithe'], [(e['from'], e['to'], e['disposition'], e['link'], str(e.get('why', ''))[:90]) for e in dep['edges'] if e['to'] == 'yovel'], [(e['from'], e['to'], e['disposition'], e['link'], str(e.get('why', ''))[:90]) for e in dep['edges'] if e['to'] in ('ordinances', 'mishpatim', 'mishpatim_2', 'mishpatim_3')]))
print('  a CALL edge row WHOLE (food_tithe): %s' % [e for e in dep['edges'] if e['from'] == 'food_tithe' and e.get('disposition') == 'CALL'][:1])
print('  a RUN_CITATION pointer row WHOLE (food_tithe): %s' % [p for p in dep['pointers'] if p.get('runner') == 'food_tithe'][:1])
print('  the spans of the kin: %s' % {k: dep['spans'].get(k) for k in NAMES})
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the register seats naming Deut 15 (WHOLE): %s' % [(sec, k, v) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.startswith('Deut 15')])
KINSEATS = ('Lev 25:1', 'Lev 25:2', 'Lev 25:8', 'Lev 25:35', 'Lev 25:39', 'Lev 27:26', 'Exod 21:1', 'Exod 21:2', 'Exod 22:24', 'Exod 23:10', 'Exod 13:2', 'Exod 13:11', 'Exod 34:19', 'Num 18:15', 'Lev 22:17', 'Lev 21:16', 'Lev 14:14', 'Deut 5:15', 'Deut 12:6', 'Deut 12:15', 'Deut 14:22', 'Deut 14:28')
print('  the register seats naming the kin: %s' % [(sec, k, v) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.split(' ')[0] + ' ' + k.split(' ')[1] in KINSEATS][:30])
rc_src = open(f'{ROOT}/World/step9/register_census.py', encoding='utf-8').read()
print('  the receipt finder\'s defs in register_census.py: %s' % re.findall(r'^def ([a-z_0-9]+)\(', rc_src, re.M))
print('  THE FINDER\'S FORMS (register_census.py code lines naming spoke/commanded/receipt/header/footer/manner/statute — read for 15:2 "this is the manner" and 15:6 "as He spoke to you"):')
n = 0
for i, l in enumerate(rc_src.split('\n')):
    if re.search(r'spoke|commanded|receipt|RECEIPT|header|HEADER|footer|FOOTER|manner|statute', l) and not l.strip().startswith('#'):
        print('    %4d %s' % (i + 1, l.strip()[:190])); n += 1
        if n >= 70: break

print('\n==== (7) THE READBACK PROBES on file; the ledgers naming 15:n / the release / the prozbul / the slave / the awl / the firstling; the kin\'s ledgers ====')
rp = open(f'{ROOT}/World/step9/readback_probes.py', encoding='utf-8').read()
QL = sorted(set(re.findall(r"'(Q\d+)", rp)), key=lambda s: int(s[1:]))
print('  readback_probes: the Q labels: %s' % QL)
print('  the last Q heads: %s' % [l.strip()[:200] for l in rp.split('\n') if re.search(r"'(?:%s)" % '|'.join(QL[-3:]), l)][:6])
print('  the probes holding a marker count or a marker list literal: %s' % [l.strip()[:160] for l in rp.split('\n') if re.search(r'markers?\W+1[0-9]{2}\b|172\b|169\b', l)][:12])
for f in sorted(glob.glob(f'{ROOT}/logic/oral_triage/*.md')):
    t = open(f, encoding='utf-8').read()
    n = len(re.findall(r'Deut(?:eronomy)? 15:\d+|prozbul|prosbul|seventh year|year of release|Hebrew slave|Hebrew servant|\bthe awl\b|firstling|sabbatical', t))
    if n: print('  ledger naming Deut 15:n / the release / the prozbul / the Hebrew slave / the awl / the firstling / the sabbatical: %s (%d)' % (os.path.basename(f), n))
print('  the kin\'s ledgers (Leviticus 14, 19, 21-23, 25, 27; Exodus 13, 21-23, 34; Numbers 3, 8, 18; Genesis 4, 15, 47; Deuteronomy 5, 11-14): %s' % [os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_triage/*.md') if re.search(r'lev_14|metzora|tazria|lev_19|lev_2[1-3]|lev_25|behar|yovel|lev_27|bechukotai|vows|holiness|priest|emor|moadim|exo_13|\bbo_|pre_sinai|exo_2[1-3]|mishpatim|ordinances|exo_34|num_0?3|num_0?8|num_18|korach|gen_0?4|gen_15|gen_47|deu_0?5|deu_1[1-4]', os.path.basename(f))])
