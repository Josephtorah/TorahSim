import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 11b — THE COMPILE OF CHAPTER 13, Deuteronomy 13:1-19 (2026-09-21; the owner: "Go" after sitting 11's tail — the commit still on his
# word): THE RECONNAISSANCE before the design (ch12_compile_recon.py's form on chapter 13, derived by derive_ch13_recon.py) — (1) WHICH RUNNER HOLDS A CELL FOR
# THE CHAPTER'S MATTER (the sacrificer devoted — Exodus 22:19; the calf's 'these are your gods' — Exodus 32; the stonings — Leviticus 20:2, 27, 24:14-23, Numbers
# 15:32-36; the high hand — Numbers 15:30-31; the devoted thing — Leviticus 27:28-29, Deuteronomy 7:26; Hormah — Numbers 21:2-3; the fierce anger turned — Numbers
# 25:4; the dream — Numbers 12:6-8; the cloud's march — Numbers 9-10; the testing — Genesis 22:1, Deuteronomy 8:2, 16; the header's twin 4:2; the preamble 5:6; the
# six verbs' kin 6:13, 10:20, 11:22; 'other gods which you have not known' 11:28; the right in His eyes 12:25, 28) — every runner's ink refs scanned by regex, per
# def; (2) the callee modules' defs, asks, DATA keys; (3) the kinds and effects on file touching the matter; (4) the registry map; (5) the tape's lines of the kin
# with THE CLOCK'S DAY at each, the tape's LAST lines and markers; (6) the sequence file's tuples, the checkpoint prefixes in use (the D series — DD the open
# series, the next DE), the M[] names, the daemons; (7) the dispositions and register seats naming Deut 13 (none expected — the reading's finder found no
# receipt), the readback probes' tail, the ledgers naming 13:n / Hananiah / Jericho / Achan / Belial, the kin's ledgers.
import sys, io, re, contextlib, inspect, collections, yaml, glob, subprocess, os, importlib
ROOT = _ROOT   # RUN FROM THE REPO ROOT; no absolute repo path typed
sys.path.insert(0, f'{ROOT}/World/step9')

print('==== (1) THE CHAPTER\'S MATTER — every runner\'s refs, per def ====')
SEATS = [(r'Deut(?:eronomy)? 13:(\d+)', 'Deut 13'), (r'Exod(?:us)? 22:19\b', "Exod 22:19 (the sacrificer devoted — the ban's first seat)"), (r"ink\('22:19'", 'Exod 22:19 (ink)'), (r'Exod(?:us)? 32:(?:[1-8]|2[0-9]|3[0-5])\b', 'Exod 32:1-8, 20-35 (the calf — these are your gods; the destruction)'), (r'Lev(?:iticus)? 20:(?:2|27)\b', 'Lev 20:2, 27 (the stoning by the people; the necromancer)'), (r'Lev(?:iticus)? 24:(?:1[0-6]|23)\b', "Lev 24:10-16, 23 (the blasphemer stoned; the witnesses' hands)"), (r"ink\('24:(?:1[0-6]|23)'", 'Lev 24 (ink)'), (r'Lev(?:iticus)? 27:2[89]\b', 'Lev 27:28-29 (the devoted thing)'), (r'Num(?:bers)? 15:3[0-6]\b', 'Num 15:30-36 (the high hand; the wood-gatherer stoned)'), (r'Num(?:bers)? 21:[23]\b', "Num 21:2-3 (Hormah's vow)"), (r'Num(?:bers)? 25:4\b', 'Num 25:4 (the fierce anger turned)'), (r'Num(?:bers)? 12:[68]\b', 'Num 12:6-8 (the dream; mouth to mouth)'), (r'Num(?:bers)? (?:9:1[5-9]|9:2[0-3]|10:1[12]|10:3[3-6])\b', "Num 9:15-23, 10:11-12, 33-36 (the cloud's march; the ark's rest)"), (r'Gen(?:esis)? 22:1\b', "Gen 22:1 (the testing's first seat)"),
         (r'Deut(?:eronomy)? 4:2\b', "Deut 4:2 (not add nor take away — the header's twin)"), (r'Deut(?:eronomy)? 5:6\b', 'Deut 5:6 (the preamble)'), (r'Deut(?:eronomy)? 6:1[3-5]\b', 'Deut 6:13-15 (fear, serve, swear; the gods round about)'), (r'Deut(?:eronomy)? 7:(?:[1-5]|16|2[56])\b', 'Deut 7:1-5, 16, 25-26 (the ban; the unpitying eye; the devoted thing)'), (r'Deut(?:eronomy)? 8:(?:2|16)\b', 'Deut 8:2, 16 (the testing)'), (r'Deut(?:eronomy)? 9:26\b', 'Deut 9:26 (whom You redeemed)'), (r'Deut(?:eronomy)? 10:20\b', 'Deut 10:20 (the four verbs)'), (r'Deut(?:eronomy)? 11:(?:13|22|28)\b', 'Deut 11:13, 22, 28 (heart and soul; cleave; other gods not known)'), (r'Deut(?:eronomy)? 12:(?:2[5-9]|3[01])\b', 'Deut 12:25-31 (the right in His eyes; the nations cut off)'), (r'Deut(?:eronomy)? (?:17:[2-7]|17:1[23]|18:2[0-2]|19:1[5-9]|19:20|21:2[01]|22:2[1-4]|24:16|28:64)\b', 'Deut 17:2-7, 12-13 / 18:20-22 / 19:15-20 / 21:21 / 22:21-24 / 24:16 / 28:64 (the kin ahead)'), (r'Deut(?:eronomy)? 1[4-9]:\d+\b', 'Deut 14-19 (ahead)'),
         (r'Josh(?:ua)? (?:6:1[7-9]|6:2[0-6]|7:\d+|8:2[6-9]|10:28)\b|1 Kings (?:13:\d+|16:34|21:\d+|22:43)\b|1 Sam(?:uel)? (?:7:9|15:3|26:19)\b|Jer(?:emiah)? 28:\d+\b|2 Kings 23:26\b|Jonah 3:9\b', "the run's cases (Jericho, Achan, Ai, Makkedah; Jeroboam's altar, Naboth, Jehoshaphat, Hiel; Samuel's lamb, Amalek, Saul; Hananiah)"), (r'Judg(?:es)? (?:6:3[6-9]|6:40|19:22|20:13)\b', "Judges (Gideon's fleece; Gibeah's sons of Belial)"),
         (r'Sanhedrin (?:40[ab]|41[ab]|67[ab]|88b|89[ab]|90a|11[1-3][ab])|Mishnah Sanhedrin (?:1:5|4:1|5:[12]|7:6|7:10|10:[4-6]|11:[1456])', 'Sanhedrin (the inciter; the false prophet; the inquiries; the condemned city; the festival; the honors)'), (r'Makkot 1:[4-6]', 'Makkot 1:4-6 (the plotting witness)'), (r'Zevachim 8:10|Zevachim 8[01][ab]|Tosefta Zevachim 8', 'Zevachim (the mixed bloods)'), (r'Sukkah 3:4|Sukkah 34b|Menachot 4[12][ab]', 'Sukkah / Menachot (the four species; the fringes)'), (r'Rosh Hashanah 28b|Eruvin 96a', "Rosh Hashanah 28b / Eruvin 96a (the priests' blessing)"), (r'Avodah Zarah 3:9|Avodah Zarah (?:49b|50a)', 'Avodah Zarah 3:9 (the benefit to the Salt Sea)'), (r'Bava Metzia 59b|Yevamot 90b|Shabbat 151b|Bava Kamma 9:30|Avot (?:2:1|3:9|3:14)|Sifrei (?:Numbers|Bamidbar) (?:103|113|114)', "the docket's other works"),
         (r'\bprophet', 'prophet'), (r'\bdream', 'dream'), (r'\bsign\b|\bwonder\b', 'sign / wonder'), (r'\btest(?:s|ed|ing)?\b|\btrial\b', 'test'), (r'\bentic|\bincit|\bseduc', 'entice / incite / seduce'), (r'\bston(?:e|ed|ing)\b', 'stoning'), (r'\bstrangl', 'strangling'), (r'\bban\b|\bdevote|\bherem\b|\bcherem\b|\bproscri', 'the ban / the devoted thing'), (r'\bpurge\b|remove the evil|burn out', 'purge the evil'), (r'Belial|worthless|base fellows', 'Belial'), (r'condemned city|idolatrous city|subverted city|nidachat', 'the condemned city'), (r'\binquir|\bprobe|\bexamin', 'inquire / the inquiries'), (r'edge of the sword|\bsword\b', 'the sword'), (r'\bheap\b|\bmound\b', 'the heap'), (r'\bwholly\b|whole offering|kalil', 'wholly'), (r'fierce anger|fierceness of (?:his|His) anger|burning anger', 'the fierce anger'), (r'\bmercy\b|compassion', 'mercy'), (r'\bcleave|\bcling', 'cleave'), (r'\bthrust|draw(?:n)? away|\bapostas', 'thrust away / draw away'), (r'other gods', 'other gods'), (r'\bidol', 'idol'), (r'hear and fear|hear and be afraid', 'hear and fear'), (r'hand first|hand of the witnesses|hand of all the people', 'the hand first'), (r'\bTishri\b|\bNisan\b', 'Tishri / Nisan')]
KIN_LABELS = ("Exod 22:19 (the sacrificer devoted — the ban's first seat)", 'Exod 32:1-8, 20-35 (the calf — these are your gods; the destruction)', 'Lev 20:2, 27 (the stoning by the people; the necromancer)', "Lev 24:10-16, 23 (the blasphemer stoned; the witnesses' hands)", 'Lev 27:28-29 (the devoted thing)', 'Num 15:30-36 (the high hand; the wood-gatherer stoned)', "Num 21:2-3 (Hormah's vow)", 'Num 25:4 (the fierce anger turned)', 'Num 12:6-8 (the dream; mouth to mouth)', "Num 9:15-23, 10:11-12, 33-36 (the cloud's march; the ark's rest)", "Gen 22:1 (the testing's first seat)", "Deut 4:2 (not add nor take away — the header's twin)", 'Deut 5:6 (the preamble)', 'Deut 6:13-15 (fear, serve, swear; the gods round about)', 'Deut 7:1-5, 16, 25-26 (the ban; the unpitying eye; the devoted thing)', 'Deut 8:2, 16 (the testing)', 'Deut 9:26 (whom You redeemed)', 'Deut 10:20 (the four verbs)', 'Deut 11:13, 22, 28 (heart and soul; cleave; other gods not known)', 'Deut 12:25-31 (the right in His eyes; the nations cut off)', 'Deut 17:2-7, 12-13 / 18:20-22 / 19:15-20 / 21:21 / 22:21-24 / 24:16 / 28:64 (the kin ahead)', 'Deut 14-19 (ahead)', "the run's cases (Jericho, Achan, Ai, Makkedah; Jeroboam's altar, Naboth, Jehoshaphat, Hiel; Samuel's lamb, Amalek, Saul; Hananiah)", "Judges (Gideon's fleece; Gibeah's sons of Belial)")
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
            if label in KIN_LABELS or label == 'Deut 13': print('     %-34s %s' % (label, dict(found[label])))
NAMES = sorted({n for n, d in HITS.items() if any(l in d for l in KIN_LABELS)} | {'opening_speech', 'obey_horeb', 'covenant_at_horeb', 'decalogue', 'hear_o_israel', 'seven_nations', 'good_land', 'not_righteousness', 'second_tablets', 'blessing_and_curse', 'place_name', 'sanctions', 'ordinances', 'erection', 'temurah', 'beha', 'lev24', 'mekoshesh', 'shelach', 'chukat', 'balak', 'holiness', 'holiness_b', 'mamre', 'pre_sinai', 'mishpatim', 'mishpatim_2', 'mishpatim_3', 'journeys', 'calendar', 'clocks', 'primeval', 'tochacha'})
print('  THE KIN RUNNERS (a hit on a kin label) + the Deuteronomy runners + the kin named by the box + the clock runners: %s' % NAMES)
MODS = []
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    for n in NAMES:
        try: MODS.append((n, importlib.import_module('cold_run_' + n)))
        except Exception as e: print('IMPORT FAILED', n, e, file=sys.stderr)
print('  modules imported: %s' % [n for n, _ in MODS])

print('\n==== (2) THE CALLEES\' DEFS, ASKS, DATA KEYS ====')
BROAD = ('prophet', 'stone', 'ban', 'land', 'israel', 'gods', 'idol', 'city', 'test', 'witness', 'sword', "'13:", "'22:", "'32:", "'20:", "'24:", "'27:", "'15:", "'21:", "'25:", 'installed_by', 'given_at')
PATS = ('Deut 13', 'Deuteronomy 13', 'prophet', 'dream', 'sign', 'wonder', 'test', 'entice', 'incite', 'seduce', 'stone', 'stoning', 'strangl', 'ban', 'devote', 'herem', 'purge', 'Belial', 'condemned city', 'inquir', 'probe', 'sword', 'heap', 'wholly', 'fierce anger', 'mercy', 'cleave', 'thrust', 'draw away', 'other gods', 'idol', 'hear and fear', 'hand first', 'witness', 'city', 'brother', 'secret', 'Jericho', 'Achan', 'Hananiah', 'Naboth', 'calf', 'cloud', 'gods', 'israel', 'land',
        'installed_by', 'given_at', 'Sanhedrin', 'Makkot 1', 'Zevachim 8', 'Sukkah 3', 'Menachot 41', 'Menachot 42', 'Rosh Hashanah 28', 'Eruvin 96', 'Avodah Zarah 3:9', 'Avodah Zarah 49', 'Avodah Zarah 50', 'Bava Metzia 59', 'Yevamot 90', 'Shabbat 151', 'Bava Kamma 9', 'Avot 2:1', 'Avot 3', 'Sifrei Numbers', 'Sifrei Bamidbar')
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
KP = r'prophet|dream|sign|wonder|test|trial|entic|incit|seduc|ston|strangl|\bban|devot|herem|purge|belial|condemn|city|inquir|probe|sword|heap|wholly|anger|mercy|cleave|thrust|draw|apostas|other_gods|idol|image|hear_and_fear|hand_first|witness|death|execut|karet|sacrific|calf|cloud|redeem|rebellion|curse|blasphem|molech|necroman|wood|high_hand|hormah|peor|fear|burn'
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
TOK = ('israel', 'israel_people', 'moses', 'the-lord', 'god', 'the-prophet', 'the-dreamer', 'the-dream', 'the-sign', 'the-wonder', 'the-gods', 'other-gods', 'the-way', 'the-brother', 'the-son', 'the-daughter', 'the-wife', 'the-friend', 'the-mother', 'the-fathers', 'the-peoples', 'the-earth', 'the-eye', 'the-hand', 'the-people', 'the-stones', 'the-city', 'the-cities', 'the-inhabitants', 'the-men', 'sons-of-belial', 'belial', 'the-sword', 'the-cattle', 'the-spoil', 'the-street', 'the-fire', 'the-heap', 'the-devoted-thing', 'the-anger', 'the-mercy', 'the-voice', 'the-commandments', 'egypt', 'the-house-of-bondage', 'the-land', 'the-nations', 'the-calf', 'the-cloud', 'the-court', 'the-witnesses', 'jericho', 'achan', 'hananiah')
print('  mapped: %s' % {t: reg_map.get(t) for t in TOK if reg_map.get(t)})
print('  NO registry row: %s' % [t for t in TOK if not reg_map.get(t)])
print('  registry ids with prophet/dream/gods/idol/city/belial/sword/heap/devoted/anger/mercy/calf/cloud/court/witness/stone/egypt/nation/land in them: %s' % sorted({v for v in reg_map.values() if re.search(r'prophet|dream|gods|idol|city|belial|sword|heap|devoted|anger|mercy|calf|cloud|court|witness|stone|egypt|nation|land', str(v))})[:60])

print('\n==== (5) THE TAPE\'S LINES the chapter retells; THE CLOCK\'S DAY at each; the tape\'s LAST lines and markers ====')
src_cs = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
tape = src_cs[src_cs.find('# ==== TAPE BEGIN'):src_cs.find('# ==== TAPE END ====')]
tl = tape.split('\n')
KINRE = r"'Exod 22:19\b|'Exod 32:|'Lev 20:(?:2|27)\b|'Lev 24:(?:1[0-6]|23)\b|'Lev 27:2[89]\b|'Num 15:3[0-6]\b|'Num 21:[23]\b|'Num 25:4\b|'Num 12:[68]\b|'Num 9:(?:1[5-9]|2[0-3])\b|'Num 10:(?:1[12]|3[3-6])\b|'Gen 22:1\b|'Deut (?:4:2|5:6|6:1[3-5]|7:(?:[1-5]|16|2[56])|8:(?:2|16)|9:26|10:20|11:(?:13|22|28)|12:(?:2[5-9]|3[01])|13:\d+)\b"
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
print('  the section comments of the kin (Exod 22, 32; Lev 20, 24, 27; Num 9, 10, 12, 15, 21, 25; Gen 22): %s' % [c for c in re.findall(r'# ---- ((?:Exod|Num|Lev|Gen) [^-]+?) ----', tape) if re.search(r'Exod (?:22|32)\b|Num (?:9|10|12|15|21|25)\b|Lev (?:20|24|27)\b|Gen 22\b', c)])
print('  DAEMON_ORDER %d, tail %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-3:]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT))
print('  the Exod 22/32, Lev 20/24/27, Num 9/10/12/15/21/25, Gen 22, Deut 4-13 lines with their kinds:')
for l in tl:
    m = re.search(r"w\.(?:event|write|marker|close)\('([a-z_0-9]+)'.*?'((?:Exod (?:22:19|32:\d+)|Lev (?:20:(?:2|27)|24:(?:1[0-6]|23)|27:2[89])|Num (?:15:3[0-6]|21:[23]|25:4|12:[68]|9:(?:1[5-9]|2[0-3])|10:(?:1[12]|3[3-6]))|Gen 22:1|Deut (?:4:2|5:6|6:1[3-5]|7:(?:[1-5]|16|2[56])|8:(?:2|16)|9:26|10:20|11:(?:13|22|28)|12:(?:2[5-9]|3[01])|13:\d+))\b(?:-\d+)?)'", l)
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
print('  the chapter-13-era log rows (EVENT/marker rows whose source is Exodus 22:19, the calf, the stonings, the devoted thing, Hormah, Peor, the dream, the cloud, the testing; the day and its rendering):')
n = 0
for row in w.log:
    if not isinstance(row, (list, tuple)) or len(row) < 3: continue
    tag, day, ev = row[0], row[1], row[2]
    src = str(ev.get('source', ev.get('verse', ''))) if isinstance(ev, dict) else str(ev)
    if re.search(r'Exod (?:22:19\b|32:\d+)|Lev (?:20:(?:2|27)\b|24:(?:1[0-6]|23)\b|27:2[89]\b)|Num (?:15:3[0-6]\b|21:[23]\b|25:4\b|12:[68]\b|9:(?:1[5-9]|2[0-3])\b|10:(?:1[12]|3[3-6])\b)|Gen 22:1\b', src):
        print('    %-6s day %-6s %-32s %s | %s' % (tag, day, ev.get('kind', '?') if isinstance(ev, dict) else '?', src[:22], render(day)))
        n += 1
        if n > 120: break
print('  the marker rows on the log (all tags): %s' % collections.Counter(r[0] for r in w.log if isinstance(r, (list, tuple))).most_common(8))
print('  markers in the world (Exod 19-34): %s' % [(m if isinstance(m, str) else str(m)[:120]) for m in (getattr(w, 'markers', []) or [])][:0])
mk = [x for x in getattr(w, 'markers', []) if re.search(r'Exod (?:19|24|32|34|40)\b|Num (?:9|10|12|15|21|25)\b|Lev (?:20|24|27)\b|Gen 22\b|Deut', str(x))] if hasattr(w, 'markers') else []
print('  the markers Exod 19, 23-24, 34, 40, Num 9-10, 16, 18, 20, 33, Lev 17, 26, Deut: %s' % [str(x)[:160] for x in mk][:80])
print('  THE MARKERS THE KIN SIT UNDER: the sequence file\'s M[] lines naming the erection, the tent, Sinai, the calf, the cloud, the journey, the ark, Korah, Peor, Hormah, the speech: %s' % [l.strip()[:200] for l in src_cs.split('\n') if re.search(r"M\['[a-z_0-9]*(?:erect|tent|tabernacle|sinai|calf|cloud|journey|ark|korah|peor|hormah|balaam|speech_resumed|plains|moab)[a-z_0-9]*'\] = ", l)][:40])
print('  CAL_PARAMS rows naming erect/tishri/nisan/year/season: %s' % [(k, v) for k, v in getattr(CS, 'CAL_PARAMS', {}).items() if re.search(r'erect|tishri|nisan|year|season', str(k) + str(v))][:8])
print('  the tape lines naming Jericho / Achan / Hananiah / Naboth / the calf / the cloud / a prophet / a dream / stoning / the ban / the devoted thing / Belial / purge / idols / other gods: %s' % [l.strip()[:200] for l in tl if re.search(r'Jericho|Achan|Hananiah|Naboth|\bcalf\b|\bcloud\b|prophet|dream|ston(?:e|ed|ing)\b|\bban\b|devoted|Belial|purge|idol|other gods', l)][:40])
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
for dn in ('law_place_name', 'law_sanctions', 'law_ordinances', 'law_lev24', 'law_temurah', 'law_beha', 'law_erection', 'law_seven_nations', 'law_obey_horeb', 'law_mekoshesh', 'law_shelach', 'law_chukat', 'law_balak', 'law_holiness', 'law_blessing_and_curse'):
    print('  the daemon block %s: %s' % (dn, str(dd['daemons'].get(dn))[:500]))
print('  the functions block place_name: %s' % str(dd.get('functions', {}).get('place_name'))[:400])
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d; pointers naming Deut 13: %s; edges naming Deut 13: %s' % (len(dep['spans']), len(dep['edges']), len(dep['pointers']), [p for p in dep['pointers'] if re.search(r'Deut 13:', str(p))][:10], [e for e in dep['edges'] if re.search(r'Deut 13:', str(e))][:5]))
print('  the place_name edges on file: %s' % [(e['from'], e['to'], e['disposition'], e['link'], str(e.get('why', ''))[:90]) for e in dep['edges'] if e['from'] == 'place_name'])
print('  a CALL edge row WHOLE (place_name): %s' % [e for e in dep['edges'] if e['from'] == 'place_name' and e.get('disposition') == 'CALL'][:1])
print('  a RUN_CITATION pointer row WHOLE (place_name): %s' % [p for p in dep['pointers'] if p.get('runner') == 'place_name'][:1])
print('  the spans of the kin: %s' % {k: dep['spans'].get(k) for k in NAMES})
ip = yaml.safe_load(open(f'{ROOT}/World/step9/installation_parameters.yaml', encoding='utf-8'))
print('  installing acts: %s' % list(ip['installing_acts']))
print('  I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
decl = yaml.safe_load(open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8'))
print('  the register seats naming Deut 13 (WHOLE): %s' % [(sec, k, v) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.startswith('Deut 13')])
print('  the register seats naming Exod 22:19, Exod 32:1, Lev 20:2, Lev 24:14, Num 15:30, Num 21:2, Deut 4:2, Deut 5:6, Deut 6:13, Deut 7:2, Deut 10:20, Deut 11:22, Deut 12:25: %s' % [(sec, k, v) for sec in ('counts', 'receipts', 'footers', 'registers') for k, v in decl.get(sec, {}).items() if k.split(' ')[0] + ' ' + k.split(' ')[1] in ('Exod 22:19', 'Exod 32:1', 'Lev 20:2', 'Lev 24:14', 'Num 15:30', 'Num 21:2', 'Deut 4:2', 'Deut 5:6', 'Deut 6:13', 'Deut 7:2', 'Deut 10:20', 'Deut 11:22', 'Deut 12:25')][:14])
print('  the receipt finder\'s defs in register_census.py: %s' % re.findall(r'^def ([a-z_0-9]+)\(', open(f'{ROOT}/World/step9/register_census.py', encoding='utf-8').read(), re.M))

print('\n==== (7) THE READBACK PROBES on file; the ledgers naming 13:n / Hananiah / Jericho / Achan / Belial; the kin\'s ledgers ====')
rp = open(f'{ROOT}/World/step9/readback_probes.py', encoding='utf-8').read()
print('  readback_probes: the Q labels: %s' % sorted(set(re.findall(r"'(Q\d+)", rp)), key=lambda s: int(s[1:])))
print('  the Q31-Q33 heads: %s' % [l.strip()[:200] for l in rp.split('\n') if re.search(r"'Q3[1-3]", l)][:6])
print('  the probes holding a marker count or a marker list literal: %s' % [l.strip()[:160] for l in rp.split('\n') if re.search(r'markers?\W+1[0-9]{2}\b|172\b|169\b', l)][:12])
print('  the readback forms on THE_LOOP\'s step-6 row: %s' % [l.strip()[:220] for l in open(f'{ROOT}/World/step9/THE_LOOP.md', encoding='utf-8').read().split('\n') if 'COMBINE' in l or 'combined' in l.lower()][:3])
for f in sorted(glob.glob(f'{ROOT}/logic/oral_triage/*.md')):
    t = open(f, encoding='utf-8').read()
    n = len(re.findall(r'Deut(?:eronomy)? 13:\d+|Hananiah|Jericho|Achan|Belial|condemned city|the inciter|false prophet', t))
    if n: print('  ledger naming Deut 13:n / Hananiah / Jericho / Achan / Belial / the condemned city / the inciter / the false prophet: %s (%d)' % (os.path.basename(f), n))
print('  the kin\'s ledgers (Exodus 22, 32; Leviticus 20, 24, 27; Numbers 9-10, 12, 15, 21, 25; Genesis 22; Deuteronomy 4-12): %s' % [os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_triage/*.md') if re.search(r'exo_22|exo_32|lev_20|lev_24|lev_27|num_09|num_10|num_12|num_15|num_21|num_25|gen_22|deu_0[4-9]|deu_1[0-2]|sanctions|calf|blasphem|mekoshesh|wood|hormah|peor|akedah|beha', os.path.basename(f))])
