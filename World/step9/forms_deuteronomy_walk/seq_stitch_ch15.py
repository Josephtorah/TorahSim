import os as _os, subprocess as _sp
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
"""seq_stitch.py — THE STITCHER (THE SEQUENTIAL RUN, 2026-09-07; SEQUENTIAL_RUN.md section 3): from the recorder's
seq_recording.json, FILTER the scenes' submits to HISTORY (form / source / register), DEDUP exact repeats across
runners, SORT into canonical verse order, RE-BASE the scene-clock fields, MERGE the markers (section 4 — every number
verified against the ink's parse here, and again at run time), and WRITE the tape section of
World/step9/cold_run_sequence.py between its sentinels as LITERAL marker/submit/close lines. Then PREDICT: the
markers' days on a bare world (the calendar arithmetic, before the runner runs), and print the census. Also appends
the sequential tape to the registry's tape lines (event_vocabulary.yaml) for every history kind."""
import sys, os, io, re, json, collections, sqlite3, contextlib
from fractions import Fraction   # THE DEUTERONOMY WALK 1b (2026-09-15): the exodus marker's verse reads the half since rule 30
HERE = (_ROOT + '/World/step9')
SCR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import yaml
import world_engine as WE

RUNNER = os.path.join(HERE, 'cold_run_sequence.py')
SRC = open(RUNNER, encoding='utf-8').read()
# ONE copy of the parser: exec the runner's INK block into this namespace
ink_src = SRC.split('# ==== INK BEGIN')[1].split('# ==== INK END ====')[0]
ink_src = ink_src.split('\n', 1)[1]
INK = {'re': re, 'sqlite3': sqlite3, 'os': os, 'WE': WE}
INK['_ROOT'] = _ROOT   # THE PORTABLE REPO (2026-09-15): the INK block reads the store through the root; the exec'd namespace must carry it
exec(ink_src, INK)
ink_numbers, ink_ordinals, verse_words = INK['ink_numbers'], INK['ink_ordinals'], INK['verse_words']

J = json.load(open(os.path.join(SCR, 'seq_recording.json'), encoding='utf-8'))
REC = J['rec']
ev = yaml.safe_load(open(os.path.join(HERE, 'event_vocabulary.yaml'), encoding='utf-8'))
E = ev.get('events') or ev
FORM = {k: v.get('form') for k, v in E.items()}
BO = {'Gen': 1, 'Exod': 2, 'Lev': 3, 'Num': 4, 'Deut': 5}   # THE DEUTERONOMY WALK 1b (2026-09-15): the fifth book; THE TENT sitting 2 (2026-09-09): the fourth
VREF = re.compile(r'(Gen|Exod|Lev|Num|Deut|1 Sam|2 Sam|1 Kgs|2 Kgs|1 Chr|2 Chr|Neh)\s+(\d+):(\d+)')
FIRST = re.compile(r'^(Gen|Exod|Lev|Num|Deut)\s+(\d+):(\d+)')
con = sqlite3.connect(('file:' + _ROOT + '/Data/tanakh.sqlite?mode=ro'), uri=True)

# the runners whose daemon reads the event's `day` as the CLOCK (measured by grep at the design: the idiom
# `day = event.get('day', world.clock.day)` or `event['day'] + n`); a `day` on their history events is DROPPED
CLOCK_DAY_RUNNERS = {'joseph', 'mamre', 'primeval', 'exodus_story', 'erection', 'incense_shekel', 'priesthood', 'holiness', 'metzora', 'negaim', 'clocks', 'pesach', 'tzav', 'chatat', 'offerings', 'ordinances'}
SPAN_ORDER = ['pre_sinai', 'primeval', 'mamre', 'joseph', 'family', 'exodus_story', 'pesach', 'decalogue', 'ordinances', 'mishpatim', 'mishpatim_2', 'guardians', 'calendar', 'erection',
              'sanctuary_build', 'vestments', 'incense_shekel', 'offerings', 'minchah', 'chatat', 'vayikra5', 'tzav', 'shemini_day', 'shemini',
              'clocks', 'negaim', 'metzora', 'yoma', 'sanctions', 'holiness', 'holiness_b', 'priesthood', 'moadim', 'lev24', 'yovel', 'tochacha', 'temurah', 'pesach_sheni', 'mekoshesh', 'zelophehad', 'bamidbar', 'naso', 'beha', 'shelach', 'korach', 'chukat', 'balak', 'second_census', 'musafim', 'vows', 'midian', 'gad_reuben', 'journeys', 'borders', 'refuge', 'opening_speech', 'obey_horeb', 'covenant_at_horeb', 'hear_o_israel', 'seven_nations', 'good_land']   # THE DEUTERONOMY WALK 6b (2026-09-19): good_land joins the order — three lines at 8:7-20, no marker row   # THE DEUTERONOMY WALK 5b (2026-09-18): seven_nations joins the order — three lines at 7:1-26, no marker row   # THE DEUTERONOMY WALK 2b (2026-09-16): obey_horeb joins the order — five lines at 4:1-43, two RETROGRADE marker rows (Deut 4:10 the giving, 4:13 the tablets)   # THE NUMBERS WALK 15b (2026-09-13): refuge joins the order — two lines at 35:1-34, no marker row   # THE NUMBERS WALK 12b (2026-09-12): gad_reuben joins the order — twelve lines at 32:1-42, no marker row   # THE NUMBERS WALK 11b (2026-09-12): midian joins the order — thirteen lines at 31:1-54, no marker row   # THE NUMBERS WALK 10b (2026-09-12): vows joins the order — one speech line at 30:2, no marker row   # THE NUMBERS WALK 9b (2026-09-11): musafim joins the order — one speech line at 28:1, no marker row   # THE NUMBERS WALK 8b (2026-09-11): second_census joins the order — its narrative re-submits Bamidbar's census_taken and levites_counted (the SHARED kinds) at their verses: DEDUPED here, bamidbar first in the order; the 25:19 marker row below   # THE NUMBERS WALK 7b (2026-09-11): balak joins the order (no marker rows — the stretch undated)   # THE NUMBERS WALK 1b (2026-09-09): Bamidbar's thirteen lines; 2b (2026-09-10): Naso's eleven


# ---- THE REGISTER TEST: the wayyiqtol off the Tanakh DB's morphology ----
def _morphs(book, ch, vs):
    r = con.cursor().execute("select id from verses where book=? and chapter=? and verse=?", (book, ch, vs)).fetchone()
    return [] if r is None else list(con.cursor().execute("select he, morph from words where verse_id=? order by idx", (r[0],)))


def _wayy(book, ch, vs, speech_ok):
    """a consecutive-imperfect verb in the verse (OSHB morph: V?w, any stem — the 'and he did' form); with speech_ok False a
    speech-frame verb (אמר 'said', דבר 'spoke') does not count"""
    for he, m in _morphs(book, ch, vs):
        if not m or not re.search(r'(^|/)V[A-Za-z]w', m):   # O8 S3 (2026-09-08): the stem codes are CASE-SENSITIVE — Niphal N, Pual P, Hophal H are uppercase; 18:1's וירא ('and He appeared', Niphal) was invisible to [a-z]
            continue
        w = re.sub(r'[֑-ׇ/]', '', he)
        core = re.sub(r'^(ו[יתנא]?)', '', w)
        if not speech_ok and (core.startswith('אמר') or core.startswith('דבר')):
            continue
        return True
    return False


RANGE = re.compile(r'(Gen|Exod|Lev|Num|Deut)\s+(\d+):(\d+)(?:-(\d+))?')   # THE DEUTERONOMY WALK 1b (2026-09-15): the fifth book
WINDOW = 10   # a narrative stretch: within ten verses of a narrative verb in the same chapter (measured at the design — the law chapters
              # Lev 21, 24 and Exod 30 carry no non-speech wayyiqtol within ten verses of their rows; the narrative chapters always do)


SHORT = re.compile(r',\s*(\d+):(\d+)(?:-(\d+))?')


def cited(cs):
    """every (book, chapter, verse) the source cites in the three books — ranges expanded, and the scenes' short form
    after a full reference ('Exod 24:1, 24:9'; 'Gen 17:23, 17:27') carrying the book forward"""
    out = []
    cs = cs or ''
    for m in RANGE.finditer(cs):
        a, z = int(m.group(3)), int(m.group(4) or m.group(3))
        out += [(m.group(1), int(m.group(2)), v) for v in range(a, min(z, a + 12) + 1)]
        tail = cs[m.end():]
        for sm in SHORT.finditer(tail):
            if sm.start() != 0 and not re.match(r'^(,\s*\d+:\d+(?:-\d+)?)+', tail[:sm.start()]):
                break
            a2, z2 = int(sm.group(2)), int(sm.group(3) or sm.group(2))
            out += [(m.group(1), int(sm.group(1)), v) for v in range(a2, min(z2, a2 + 12) + 1)]
    return out


def narrative(form, cs):
    if form == 'statute':
        return True, 'statute by form'
    for book, ch, vs in cited(cs):
        for v in range(vs, max(0, vs - WINDOW), -1):
            if _wayy(book, ch, v, speech_ok=(form == 'speech')):
                return True, '%s: wayyiqtol at %s %d:%d' % (form, book, ch, v)
    return False, '%s with no narrative verb within %d verses of %s — a law clause, not a narrated act' % (form, WINDOW, cs[:40])


def first_ref(s):
    m = FIRST.match(s or '')
    return (BO[m.group(1)], int(m.group(2)), int(m.group(3))) if m and m.group(1) in BO else None


# ---- 1. FILTER ----
hist, off = [], collections.OrderedDict((k, []) for k in ('case', 'source', 'register', 'unregistered'))
per = collections.OrderedDict()
for runner, wk, op, day, payload in REC:
    if op != 'submit':
        continue
    c = per.setdefault(runner, collections.Counter()); c['scanned'] += 1
    form = FORM.get(payload['kind'])
    if form is None:
        off['unregistered'].append((runner, payload['kind'])); continue
    if form == 'case':
        c['case'] += 1; off['case'].append((runner, payload['kind'])); continue
    key = first_ref(payload.get('case_source'))
    if key is None:
        c['source'] += 1; off['source'].append((runner, payload['kind'], payload['subject'], (payload.get('case_source') or '')[:60])); continue
    ok, why = narrative(form, payload.get('case_source'))
    if not ok:
        c['register'] += 1; off['register'].append((runner, payload['kind'], payload['subject'], payload.get('case_source'), why)); continue
    c['history'] += 1
    hist.append({'key': key, 'runner': runner, 'scene_day': day, 'event': payload, 'why': why})

# ---- 2. DEDUP exact (kind, subject, verse) across runners; keep the first in canonical runner order ----
rank = {r: i for i, r in enumerate(SPAN_ORDER)}
seen, kept, dups = {}, [], []
for h in sorted(hist, key=lambda h: (rank.get(h['runner'], 99),)):
    k = (h['event']['kind'], h['event']['subject'], h['key'])          # one act at one verse on one subject
    if k in seen and seen[k] != h['runner']:
        dups.append((k, seen[k], h['runner'])); continue
    seen.setdefault(k, h['runner']); kept.append(h)
hist = kept

# ---- 3. RE-BASE the scene-clock fields ----
rebased = []
for h in hist:
    e = h['event']
    if 'day' in e and h['runner'] in CLOCK_DAY_RUNNERS:
        rebased.append((e['kind'], e['subject'], 'day', e['day'], 'dropped: the clock')); del e['day']
    if 'until' in e:
        rel = e['until'] - h['scene_day']
        rebased.append((e['kind'], e['subject'], 'until', e['until'], 'relative: clock + %d' % rel)); e['until'] = ('__CLOCK__', rel)
    for k in ('bound', 'dated'):
        e.pop(k, None)

# ---- the closes, keyed by their first verse ----
closes = []
for runner, wk, op, day, payload in REC:
    if op == 'close':
        key = first_ref(payload[2])
        if key is not None:
            closes.append({'key': key, 'runner': runner, 'args': payload})

# ---- 4. THE MARKERS (SEQUENTIAL_RUN.md section 4): each with its verse, the ink's numbers, its class and its code ----
def V(verse):
    m = FIRST.match(verse); return (BO[m.group(1)], int(m.group(2)), int(m.group(3)))

MK = []   # (verse, cls, nums, ords, code, note, at, words, place) — `at` is the tape POSITION when it differs from the verse whose numbers are checked;
          # `place` (O9 T2, 2026-09-08; CLOCK.md 12b) is TYPED only where a shelf number sits in the code — the class is otherwise COMPUTED below
def mk(verse, cls, nums, code, note, ords=None, at=None, words=None, place=None):
    MK.append((verse, cls, nums, ords, code, note, at or verse, words, place))

# the creation days: day n = clock day n-1; Adam's era at the sixth day
for verse, n in (('Gen 1:5', 1), ('Gen 1:8', 2), ('Gen 1:13', 3), ('Gen 1:19', 4), ('Gen 1:23', 5), ('Gen 1:31', 6), ('Gen 2:2', 7)):
    nums = [1] if n == 1 else []
    ords = [] if n == 1 else ([7, 7] if n == 7 else [n])
    era = ", era='life:the_human'" if n == 6 else ''
    born = "M['born:the_human'] = 5; " if n == 6 else ''
    mk(verse, 'F', nums, "M['day%d'] = %d; %sw.marker('%s', %d, value='the %s day%s'%s)" % (n, n - 1, born, verse, n - 1, ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh'][n - 1], ' — Adam created (1:27)' if n == 6 else '', era), 'the creation days (the ordinal - 1)', ords)
# the begettings: the child born in the father's year + N (modeled at the year's first day)
BEGOT = [('Gen 5:3', 'the_human', 'seth', 130), ('Gen 5:6', 'seth', 'enosh', 105), ('Gen 5:9', 'enosh', 'kenan', 90), ('Gen 5:12', 'kenan', 'mahalalel', 70),
         ('Gen 5:15', 'mahalalel', 'jared', 65), ('Gen 5:18', 'jared', 'enoch', 162), ('Gen 5:21', 'enoch', 'methuselah', 65), ('Gen 5:25', 'methuselah', 'lamech', 187),
         ('Gen 5:28', 'lamech', 'noach', 182), ('Gen 5:32', 'noach', 'shem', 500),
         ('Gen 11:12', 'arpachshad', 'shelah', 35), ('Gen 11:14', 'shelah', 'eber', 30), ('Gen 11:16', 'eber', 'peleg', 34), ('Gen 11:18', 'peleg', 'reu', 30),
         ('Gen 11:20', 'reu', 'serug', 32), ('Gen 11:22', 'serug', 'nahor', 30), ('Gen 11:24', 'nahor', 'terah', 29), ('Gen 11:26', 'terah', 'abraham', 70)]
for verse, f, ch, n in BEGOT:
    mk(verse, 'F', [n], "M['born:%s'] = birth_day(w, yr(w, M['born:%s']) + %d, '%s'); w.marker('%s', M['born:%s'], value='%s lived %d years and begot %s', era='life:%s')" % (ch, f, n, ch, verse, ch, f, n, ch, ch), 'a begetting: the child born in the father\'s year + N (the day by birth_day: the shelf\'s row where it gives one)')
# the totals: proleptic
TOTAL = [('Gen 5:5', 'the_human', 930), ('Gen 5:8', 'seth', 912), ('Gen 5:11', 'enosh', 905), ('Gen 5:14', 'kenan', 910), ('Gen 5:17', 'mahalalel', 895),
         ('Gen 5:20', 'jared', 962), ('Gen 5:23', 'enoch', 365), ('Gen 5:27', 'methuselah', 969), ('Gen 5:31', 'lamech', 777), ('Gen 9:29', 'noach', 950),
         ('Gen 11:32', 'terah', 205), ('Gen 25:7', 'abraham', 175), ('Gen 25:17', 'ishmael', 137), ('Gen 35:28', 'isaac', 180), ('Gen 50:26', 'joseph', 110)]
for verse, p, n in TOTAL:
    mk(verse, 'P', [n], "M['died:%s'] = year_day(w, yr(w, M['born:%s']) + %d); w.marker('%s', M['died:%s'], value='all the days of %s: %d years — the closing total', proleptic=True)" % (p, p, n, verse, p, p, n), 'a lifespan total: proleptic')
# the flood's dates (inside Noah's 600th and 601st years, the ordinal months of the creation era)
mk('Gen 7:11', 'F', [600, 17], "M['flood'] = w.clock.day_in('life:noach', 600, 2, 17); M['flood_ordinal'] = w.clock.day_in('life:noach', 600, 2, 17, reading='ordinal'); w.marker('Gen 7:11', M['flood'], value='the 600th year of Noah, the second month, the seventeenth: the flood')", 'the flood', [2])
mk('Gen 8:4', 'F', [17], "M['ark_rested'] = next_date(w, 7, 17); w.marker('Gen 8:4', M['ark_rested'], value='the seventh month, the seventeenth: the ark rested')", 'the ark rested', [7])
mk('Gen 8:5', 'F', [1], "M['mountains'] = next_date(w, 10, 1); w.marker('Gen 8:5', M['mountains'], value='the tenth month, the first: the mountaintops seen')", 'the mountaintops (the ink names the tenth twice)', [10, 10])
mk('Gen 8:13', 'F', [601, 1], "M['dried'] = w.clock.day_in('life:noach', 601, 1, 1); w.marker('Gen 8:13', M['dried'], value='the 601st year, the first month, the first: the waters dried')", 'the waters dried', [1])
mk('Gen 8:14', 'F', [27], "M['dry'] = next_date(w, 2, 27); w.marker('Gen 8:14', M['dry'], value='the second month, the twenty-seventh: the earth dry')", 'the earth dry', [2])
# Shem's line: Arpachshad two years after the flood (Shem a son of 100 — checkpoint C4)
mk('Gen 11:10', 'F', [100, 2], "M['born:arpachshad'] = w.clock.calendar.add(M['flood'], 2, 'year'); M['born:shem_by_11_10'] = w.clock.calendar.add(M['born:arpachshad'], -100, 'year'); w.marker('Gen 11:10', M['born:arpachshad'], value='Shem a son of 100 begot Arpachshad two years after the flood', era='life:arpachshad')", 'Arpachshad')
# the ages at events (the year grain the ink; the day modeled at the year's first day)
AGES = [('Gen 12:4', 'abraham', 75, 'Abram a son of seventy-five years at his going out from Haran', None),
        ('Gen 16:16', 'abraham', 86, 'Abram a son of eighty-six years when Hagar bore Ishmael', 'ishmael'),
        ('Gen 17:1', 'abraham', 99, 'Abram a son of ninety-nine years', None),
        ('Gen 21:5', 'abraham', 100, 'Abraham a son of a hundred years when Isaac was born', 'isaac'),
        ('Gen 25:20', 'isaac', 40, 'Isaac a son of forty years when he took Rebekah', None),
        ('Gen 25:26', 'isaac', 60, 'Isaac a son of sixty years when they were born', 'jacob'),
        ('Gen 26:34', 'esau', 40, 'Esau a son of forty years', None),
        ('Gen 47:9', 'jacob', 130, 'the days of the years of my sojourning: a hundred and thirty years — THE DESCENT', None),
        ('Gen 47:28', 'jacob', 147, 'the days of Jacob: a hundred and forty-seven years — the deathbed (49:33)', None)]
for verse, p, n, label, child in AGES:
    nums = [17, 147] if verse == 'Gen 47:28' else [n]
    name = {'Gen 47:9': 'descent', 'Gen 47:28': 'jacob_147'}.get(verse, 'age:%s:%d' % (p, n))
    code = "M['%s'] = year_day(w, yr(w, M['born:%s']) + %d); " % (name, p, n)
    if child:
        code += "M['born:%s'] = birth_day(w, yr(w, M['%s']), '%s'); " % (child, name, child)
        if child == 'jacob':
            code += "M['born:esau'] = M['born:jacob']; "
    code += "w.marker('%s', M['%s'], value='%s'%s)" % ('Gen 21:2' if verse == 'Gen 21:5' else verse, ("born:%s" % child) if child else name, label.replace("'", "\\'"), (", era='life:%s'" % child) if child else '')   # O9 T2: the call names the POSITION (21:5's number at the birth verse)
    if child == 'jacob':
        code += "; w.clock.set_era('life:esau', M['born:esau'], None)"
    mk(verse, 'F', nums, code, 'an age at an event' + (' — placed at the birth verse 21:2, the number from 21:5' if verse == 'Gen 21:5' else ''), at=('Gen 21:2' if verse == 'Gen 21:5' else None))
mk('Gen 21:4', 'F', [8], "M['eighth_day'] = M['born:isaac'] + 7; w.marker('Gen 21:4', M['eighth_day'], value='on the eighth day (the birth day the first): Isaac circumcised')", 'the eighth day, inclusive')
mk('Gen 41:46', 'F', [30], "M['joseph30'] = w.clock.calendar.add(year_day(w, yr(w, M['born:jacob']) + 130), -9, 'year'); M['born:joseph'] = w.clock.calendar.add(M['joseph30'], -30, 'year'); w.marker('Gen 41:46', M['joseph30'], value='Joseph a son of thirty before Pharaoh — placed by 45:6 (two years of famine) and 41:53 (seven of plenty) before 47:9', era='life:joseph'); w.clock.eras['life:joseph'].epoch = M['born:joseph']", 'Joseph placed backward from the descent')
# ---- O8 S2 FROM EDEN TO HAGAR (2026-09-08; NARRATIVE_GAPS.md section 6g) ----
# the decree of the hundred and twenty years: RETROGRADE — the flood (Noah's 600th year, 2/17 — 7:11's own expression) minus 120 years, stated before 5:32's counter (Pesachim 6b:7; Bereshit Rabbah 30:7)
mk('Gen 6:3', 'R', [120], "M['flood'] = w.clock.day_in('life:noach', 600, 2, 17); M['reprieve_decree'] = w.clock.calendar.add(M['flood'], -120, 'year'); w.marker('Gen 6:3', M['reprieve_decree'], value='and his days shall be a hundred and twenty years — the decree dated at the flood minus a hundred and twenty (Noah 480, before 5:32\\'s five hundred): RETROGRADE, Pesachim 6b:7; the reprieve\\'s timer fires on the flood (CG2)')", 'the reprieve: retrograde (the 120 parsed at 6:3)')
mk('Gen 7:4', 'F', [7, 40, 40], "M['boarding_call'] = M['flood'] - 7; w.marker('Gen 7:1', M['boarding_call'], value='for in yet seven days I will rain (7:4) — the boarding call seven days before the flood, positioned at 7:1 so the call\\'s own act falls on it (7:10 after the seven days)')", 'the boarding call: the flood minus the seven (the numbers at 7:4, the position 7:1)', at='Gen 7:1')
mk('Gen 7:12', 'F', [40, 40], "M['rain_end'] = M['flood'] + 40; w.marker('Gen 7:17', M['rain_end'], value='the rain forty days and forty nights (7:12); the flood was forty days on the earth and the ark was lifted (7:17)')", 'the forty days of rain (the numbers at 7:12, the position 7:17 — 7:13-16 stay at the flood\'s day)', at='Gen 7:17')
mk('Gen 8:6', 'F', [40], "M['window'] = M['mountains'] + 40; w.marker('Gen 8:6', M['window'], value='at the end of forty days Noah opened the window — counted from the tenth month\\'s first (8:5), the row window_count_from')", 'the window: forty days after the mountaintops')
mk('Gen 8:10', 'F', [7], "M['dove_second'] = M['window'] + 7; w.marker('Gen 8:10', M['dove_second'], value='he waited yet another seven days — the dove\\'s second sending (the first at the window\\'s day, said so)')", 'the dove\'s second sending')
mk('Gen 8:12', 'F', [7], "M['dove_third'] = M['dove_second'] + 7; w.marker('Gen 8:12', M['dove_third'], value='yet another seven days — the dove\\'s third sending, before the drying (CG4)')", 'the dove\'s third sending')
mk('Gen 16:3', 'F', [10], "M['hagar_given'] = year_day(w, yr(w, M['age:abraham:75']) + 10); w.marker('Gen 16:1', M['hagar_given'], value='at the end of ten years of Abram\\'s dwelling in the land of Canaan (16:3) — Hagar given at eighty-five (12:4\\'s seventy-five + the ten; the day modeled at the year\\'s first): CG6; POSITIONED AT 16:1, the first verse outside Genesis 15 — the ink-derived forward marker that closes the covenant\\'s stretch where the fork runs it retrograde (O9 T2)')", 'Hagar given: the ten years from the arrival — the numbers at 16:3, the position 16:1 (O9 T2: the stretch\'s close)', at='Gen 16:1')
# ---- O9 T2 (2026-09-08; CLOCK.md 12b): THE COVENANT BETWEEN THE PIECES — Genesis 15 carries no date; the row covenant_pieces_year (two readings on the local shelf) ----
mk('Gen 15:1', 'F', [], "CPY = WE.CAL_PARAMS['covenant_pieces_year']['settings']; M['covenant_pieces'] = year_day(w, yr(w, M['born:abraham']) + int(CPY[P['covenant_placement']['value']])); w.marker('Gen 15:1', M['covenant_pieces'], value='the covenant between the pieces — READING-PLACED (the row covenant_pieces_year): Bereshit Rabbah 46:2 eighty-five, the running setting, inside the page-order bound [12:4, 16:3]; the Mekhilta on Exod 12:40 seventy, the fork\\'s covenant_pieces world — earlier than the counter, RETROGRADE there, the stretch closed at 16:1; C3d the join under both')", 'the covenant: reading-placed, the year by the row (the fork runs it retrograde)', place='reading_placed')
# ---- O8 S3 FROM MAMRE TO THE HEAP (2026-09-08; NARRATIVE_GAPS.md section 7g): fourteen rows — every reading-placed date FORWARD of the counter, its teacher named ----
mk('Gen 18:10', 'F', [], "M['mamre'] = cal_day(w, yr(w, M['age:abraham:99']), 1, 15); w.marker('Gen 18:1', M['mamre'], value='the visit at Mamre — placed on Passover of Abraham\\'s ninety-ninth year (17:1, the year before 21:5\\'s hundred) (Bereshit Rabbah 48:12 on 18:6\\'s cakes: the row mamre_visit_date), joined by the ink\\'s own at this season (18:10, 18:14) and at the set time (21:2): CH0')", 'the visit: no numeral — the season phrase; the year off 17:1\'s ninety-nine (set before 18:1 on the tape), the reading-placed date at 18:1', at='Gen 18:1')
mk('Gen 19:15', 'F', [2], "M['sodom_dawn'] = M['mamre'] + 1; w.marker('Gen 19:15', M['sodom_dawn'], value='when the dawn rose (19:15; 19:1 at evening, 19:23 the sun had risen): the day after the visit')", 'the dawn: the visit plus one — nums [2] retyped 2026-09-10 (THE NUMBERS WALK 2b): the parser\'s construct rule now reads \'your TWO daughters\' (שתי בנתיך) at this verse')
mk('Gen 22:1', 'F', [], "M['binding'] = year_day(w, yr(w, M['born:isaac']) + 37); w.marker('Gen 22:1', M['binding'], value='the binding — READING-PLACED at Isaac\\'s thirty-seven, the year of Sarah\\'s death (Bereshit Rabbah 58:5: she died of that grief; 17:17 and 23:1 give the thirty-seven; the row binding_placement), the day modeled at the year\\'s first')", 'the binding: reading-placed, Isaac 37', place='reading_placed')
mk('Gen 22:4', 'F', [], "M['moriah_seen'] = M['binding'] + 2; w.marker('Gen 22:4', M['moriah_seen'], value='on the third day (22:4) — the binding\\'s day plus two, inclusive')", 'the third day, inclusive', ords=[3])
mk('Gen 25:29', 'F', [], "M['stew_day'] = M['died:abraham']; w.marker('Gen 25:29', M['stew_day'], value='the stew day — READING-PLACED on Abraham\\'s death day (Bava Batra 16b:11: that day Abraham died, the lentils the mourner\\'s meal; the row stew_day): CH2')", 'the stew day: reading-placed on the proleptic 25:7', place='reading_placed')
mk('Gen 27:1', 'F', [], "M['blessing'] = year_day(w, yr(w, M['born:jacob']) + 63); w.marker('Gen 27:1', M['blessing'], value='the blessing — READING-PLACED at Jacob\\'s sixty-three (Bereshit Rabbah 68:5; the row blessing_placement), the year of Ishmael\\'s death by the ink (16:16 + 25:17): CH3')", 'the blessing: reading-placed, Jacob 63', place='reading_placed')
mk('Gen 28:9', 'F', [], "M['mahalath'] = M['died:ishmael']; w.marker('Gen 28:9', M['mahalath'], value='Mahalath daughter of Ishmael taken — at Ishmael\\'s death (the proleptic 25:17; Megillah 17a:5: Ishmael had died and Nebaioth gave her)')", 'Mahalath: at the proleptic death (Megillah 17a:5 places it)', place='reading_placed')
mk('Gen 28:10', 'F', [], "M['departure'] = w.clock.calendar.add(M['died:ishmael'], 14, 'year'); w.marker('Gen 28:10', M['departure'], value='Jacob went out from Beersheba — READING-PLACED at Ishmael\\'s death plus fourteen years (Megillah 17a:5-6: hidden fourteen years in the house of Eber; the row hidden_years): seventy-seven at the well (17a:5)')", 'the departure: reading-placed, the fourteen hidden years — the [7] is BEERSHEBA\'s (באר שבע, the well of the seven, 21:28-31): the place-name\'s numeral the parser counts, no count of this row; nums [7] -> [] retyped 2026-09-10 (THE NUMBERS WALK 3b): from BEER-SHEBA is the name, starred by the neighbor rule', place='reading_placed')
mk('Gen 29:14', 'F', [], "M['laban_month'] = w.clock.calendar.add(M['departure'], 1, 'month'); w.marker('Gen 29:14', M['laban_month'], value='a month of days (29:14) — the departure plus one month (the journey\\'s days absorbed into the bound)')", 'the month: no numeral — the month word')
mk('Gen 29:20', 'F', [7], "M['wedding'] = w.clock.calendar.add(M['laban_month'], 7, 'year'); w.marker('Gen 29:20', M['wedding'], value='Jacob served seven years for Rachel (29:20) — the first seven\\'s end, my days are fulfilled (29:21): the wedding, Jacob eighty-four (Bereshit Rabbah 68:5): CH5')", 'the seven years')
mk('Gen 29:28', 'F', [], "M['rachel_given'] = M['wedding'] + 7; w.marker('Gen 29:28', M['rachel_given'], value='and he fulfilled her week (29:28) — the wedding plus seven days: Rachel given; CH7')", 'the week; nums [7] -> [] retyped 2026-09-10 (THE NUMBERS WALK 3b): fulfilled the WEEK of this one — the qubuts under the vet is the week, not seven')
mk('Gen 29:30', 'F', [7], "M['fourteen_end'] = w.clock.calendar.add(M['rachel_given'], 7, 'year'); w.marker('Gen 30:25', M['fourteen_end'], value='seven other years (29:30) — the second seven\\'s end, positioned at 30:25 where the ink says when Rachel had borne Joseph: CH4 (born:joseph from Pharaoh\\'s side, 41:46 + 45:6 + 47:9)')", 'the second seven, positioned at 30:25', at='Gen 30:25')
mk('Gen 31:41', 'F', [20, 14, 2, 6, 10], "M['flight'] = w.clock.calendar.add(M['fourteen_end'], 6, 'year'); w.marker('Gen 31:17', M['flight'], value='six years for your flock (31:41) — the fourteen\\'s end plus six: the flight, positioned at 31:17')", 'the six years, positioned at 31:17', at='Gen 31:17')
mk('Gen 31:22', 'F', [], "M['told'] = M['flight'] + 2; w.marker('Gen 31:22', M['told'], value='it was told to Laban on the third day (31:22) — the flight plus two, inclusive')", 'the third day, inclusive', ords=[3])
# ---- O8 S4 FROM THE FORD TO THE COFFIN (2026-09-08; NARRATIVE_GAPS.md section 8g): every reading-placed date FORWARD of the counter, its teacher named; the family's rows STAND (35:28, 41:46, 47:9, 47:28, 50:26) ----
mk('Gen 31:23', 'F', [7], "M['heap_morning'] = M['told'] + 5; w.marker('Gen 32:1', M['heap_morning'], value='the heap\\'s morning (32:1) — Laban overtook on the seventh day from the flight (31:23), the heap\\'s night, the morning after: told (the flight + 2) + 5')", 'the heap\'s morning: the seven days (31:23), positioned at 32:1', at='Gen 32:1')
mk('Gen 32:14', 'F', [], "M['jabbok_night'] = M['heap_morning'] + 1; w.marker('Gen 32:14', M['jabbok_night'], value='that night (32:14, 32:22-23) — the gift and the crossing: the heap\\'s morning plus one')", 'the night: no numeral — the night word', words=['בלילה'])
mk('Gen 32:32', 'F', [], "M['peniel_sunrise'] = M['jabbok_night'] + 1; w.marker('Gen 32:32', M['peniel_sunrise'], value='and the sun rose upon him (32:32) — the morning after the night; the meeting (33:1-16) on this day')", 'the sunrise')
mk('Gen 33:17', 'F', [], "M['sukkot'] = M['peniel_sunrise'] + 1; w.marker('Gen 33:17', M['sukkot'], value='and Jacob journeyed to Sukkot (33:17) — the day after the meeting, MODELED (said so)')", 'Sukkot: the next day, modeled')
mk('Gen 33:18', 'F', [], "M['shechem'] = w.clock.calendar.add(M['sukkot'], 18, 'month'); w.marker('Gen 33:18', M['shechem'], value='and Jacob came whole to Shechem (33:18) — READING-PLACED eighteen months after Sukkot (Megillah 17a:7: eighteen months at Sukkot; the row road_years)')", 'Shechem: reading-placed, the eighteen months', place='reading_placed')
mk('Gen 35:6', 'F', [], "M['bethel_again'] = M['shechem'] + 1; w.marker('Gen 35:6', M['bethel_again'], value='and Jacob came to Luz, that is Bethel (35:6) — the Shechem stay inside the eighteen months by the shelf\\'s own count (Megillah 17a:7: Sukkot and Bethel), 35:5\\'s journey one day, MODELED (said so); 28:15\\'s return closed here')", 'Bethel again: the shelf\'s count, the day modeled')
mk('Gen 35:16', 'F', [], "M['ephrath_road'] = w.clock.calendar.add(M['bethel_again'], 6, 'month'); w.marker('Gen 35:16', M['ephrath_road'], value='and they journeyed from Bethel (35:16) — READING-PLACED six months after the arrival (Megillah 17a:7: six months at Bethel; the row road_years): Rachel\\'s death on the road')", 'the road to Ephrath: reading-placed, the six months', place='reading_placed')
mk('Gen 35:27', 'F', [], "M['hebron'] = M['ephrath_road'] + 1; w.marker('Gen 35:27', M['hebron'], value='and Jacob came to Isaac his father at Mamre, Kiriath-arba, that is Hebron (35:27) — the road\\'s day plus one, MODELED: Jacob ninety-nine (CJ1), the two absences (CJ0)')", 'Hebron (modeled) — KIRIATH-ARBA (קרית הארבע, the city of four) carries the article and the parser does NOT count it (the bare שבע of Beersheba it does): no numeral on this row')
mk('Gen 37:2', 'F', [17], "M['age:joseph:17'] = year_day(w, yr(w, M['born:jacob']) + 108); w.marker('Gen 37:2', M['age:joseph:17'], value='Joseph seventeen (37:2) — the year off born:jacob by the chain 47:9 − 45:6\\'s nine − 41:46\\'s thirty + seventeen (born:joseph is set only at 41:46\\'s row): the row joseph_seventeen_at_the_sale; the page order (35:29 before 37:2) against the chronology (CJ2)')", 'the sale\'s year: Joseph seventeen, off born:jacob')
mk('Gen 40:12', 'F', [3, 3], "M['prison_dreams'] = year_day(w, yr(w, M['born:jacob']) + 119) - 2; w.marker('Gen 40:5', M['prison_dreams'], value='the two dreams in one night (40:5) — READING-PLACED: Joseph thirty at Jacob\\'s 121 (47:9 − 45:6\\'s nine), the birthday two years before that by 41:1, so Jacob 119; the dreams two days before the birthday (40:13, 40:19 \\'in yet three days\\', the third day inclusive)')", 'the prison dreams: the three days (40:12, 40:18), positioned at 40:5', at='Gen 40:5')
mk('Gen 40:20', 'F', [], "M['birthday'] = M['prison_dreams'] + 2; w.marker('Gen 40:20', M['birthday'], value='on the third day, Pharaoh\\'s birthday (40:20) — the dreams\\' day plus two, inclusive: the cupbearer restored, the baker hanged (CJ6)')", 'the third day, inclusive', ords=[3])
mk('Gen 41:1', 'F', [2], "M['pharaoh_dreams'] = w.clock.calendar.add(M['birthday'], 2, 'year'); w.marker('Gen 41:1', M['pharaoh_dreams'], value='at the end of two years of days (41:1) — the birthday plus two years = Joseph thirty\\'s day (41:46, S1\\'s row): the ink\\'s own arithmetic joined')", 'the two years (שנתים, the dual — Nazir 5a:5 the phrase)')
mk('Gen 41:53', 'F', [7], "M['plenty_end'] = w.clock.calendar.add(M['joseph30'], 7, 'year'); w.marker('Gen 41:53', M['plenty_end'], value='and the seven years of plenty ended (41:53) — joseph30 plus seven: the famine begins (41:54), the seven-year timer set')", 'the plenty\'s end')
mk('Gen 42:18', 'F', [], "M['custody_third'] = w.clock.day + 2; w.marker('Gen 42:18', M['custody_third'], value='and Joseph said to them on the third day (42:18) — the custody\\'s day (42:17) plus two, inclusive: the custody timer fires on this walk, before the release (CJ6)')", 'the third day of the custody, inclusive — a row 8g omitted, found at the first tape run (CJ6)', ords=[3])
mk('Gen 45:6', 'F', [2, 5], "M['famine_two'] = w.clock.calendar.add(M['plenty_end'], 2, 'year'); w.marker('Gen 45:5', M['famine_two'], value='these two years the famine (45:6) — the plenty\\'s end plus two: the recognition; = the descent\\'s year by S1\\'s construction (47:9)')", 'the famine\'s second year: the two (שנתים) and the five remaining — the numbers at 45:6, the position at Gen 45:5 where the speech\'s event begins (the tape\'s first run set the five-years timer two years early: the event\'s line sorted before the marker\'s — CJ9\'s reading)', at='Gen 45:5')
mk('Gen 46:1', 'F', [7], "M['beersheba_descent'] = M['famine_two']; w.marker('Gen 46:1', M['beersheba_descent'], value='and Israel journeyed with all that he had and came to Beersheba (46:1) — the departure in the famine\\'s second year (45:6, 45:9 \\'hurry\\')')", 'the descent\'s departure — the [7] is BEERSHEBA\'s (באר שבע): the place-name\'s numeral the parser counts, no count of this row')
mk('Gen 50:3', 'F', [40, 70], "M['embalmed'] = M['jacob_147'] + 40; w.marker('Gen 50:3', M['embalmed'], value='forty days were fulfilled for him (50:3) — the death day (47:28\\'s row, the deathbed) plus forty: the embalming\\'s end')", 'the forty (and the seventy, whose marker is 50:4\'s row)')
mk('Gen 50:4', 'F', [], "M['weeping_end'] = M['jacob_147'] + 70; w.marker('Gen 50:4', M['weeping_end'], value='and the Egyptians wept for him seventy days (50:3); when the days of weeping were past (50:4) — the death day plus seventy')", 'the seventy: the number at 50:3, the marker at 50:4 (one marker per row)')
mk('Gen 50:10', 'F', [7], "M['atad'] = M['weeping_end'] + 1; w.marker('Gen 50:10', M['atad'], value='the threshing floor of Atad (50:10) — the weeping\\'s end plus one, MODELED: the seven days\\' mourning begins')", 'Atad: the seven days')
mk('Gen 50:14', 'F', [], "M['atad_end'] = M['atad'] + 7; w.marker('Gen 50:14', M['atad_end'], value='and Joseph returned to Egypt (50:14) — Atad plus seven: the mourning\\'s end')", 'the return: Atad plus seven (one marker per row)')
# Exodus: the exodus day from the sojourn setting; the life eras of Moses and Aaron; the epoch at 12:2
# ---- O8 S1 THE EXODUS STORY (2026-09-08; NARRATIVE_GAPS.md section 4g) ----
# the birth: the exodus year from the sojourn setting; Moses born eighty years before it (7:7's number) on the seventh of Adar (the row moses_birth_date, Kiddushin 38a:5-7); the eras of Moses and Aaron
mk('Exod 7:7', 'F', [80, 83], "M['exodus_year'] = yr(w, w.clock.calendar.add(M['descent'], 430, 'year')) if P['sojourn_start']['value'] == 'descent_literal' else (yr(w, w.clock.calendar.add(M['covenant_pieces'], 430, 'year')) if P['sojourn_start']['value'] == 'covenant_pieces' else yr(w, w.clock.calendar.add(M['born:isaac'], 400, 'year'))); M['exodus'] = cal_day(w, M['exodus_year'], 1, 15); MB = WE.CAL_PARAMS['moses_birth_date']['value']; M['born:moses'] = cal_day(w, M['exodus_year'] - 80, MB['month'], MB['day']); M['born:aaron'] = w.clock.calendar.add(M['exodus'], -83, 'year'); w.marker('Exod 2:2', M['born:moses'], value='Moses born — eighty years before the exodus (7:7), on the seventh of Adar (Kiddushin 38a:5-7; the row moses_birth_date)', era='life:moses'); w.clock.set_era('life:aaron', M['born:aaron'], None)", 'the birth of Moses (the number 80 at 7:7; the day by the shelf\'s row) — positioned at 2:2; O9 T2: the running setting\'s branch reads born:isaac (text); the fork\'s covenant branch is reading-placed in its own world', at='Exod 2:2', place='text_constrained')
mk('Exod 2:2', 'F', [3], "M['ark'] = w.clock.calendar.add(M['born:moses'], 3, 'month'); w.marker('Exod 2:3', M['ark'], value='the ark in the reeds — three months after the birth (2:2); the shelf\\'s sixth of Sivan (Sotah 12b:16-17) graded beside it (CS0)')", 'the ark: the ink\'s three months from the birth', at='Exod 2:3')
mk('Exod 7:7', 'F', [80, 83], "M['speaking'] = year_day(w, M['exodus_year']); w.marker('Exod 7:7', M['speaking'], value='Moses eighty and Aaron eighty-three at the speaking — the day within the year MODELED at the first day of the exodus year (convention 18, said so): the plagues walk from here by their own stamps')", 'the speaking (the modeled placement of the undated stretch)')
mk('Exod 7:25', 'F', [7], "M['river7'] = M['speaking'] + 7; w.marker('Exod 7:25', M['river7'], value='seven days were filled after the LORD struck the river — the striking placed at the speaking (modeled), the seven the ink\\'s')", 'the river\'s seven days')
mk('Exod 8:6', 'F', [], "M['frogs_morrow'] = w.clock.day + 1; w.marker('Exod 8:6', M['frogs_morrow'], value='tomorrow — the frogs\\' removal (8:6, 8:9)')", 'the frogs\' morrow', words=['למחר'])
mk('Exod 8:19', 'F', [], "M['swarms_morrow'] = w.clock.day + 1; w.marker('Exod 8:19', M['swarms_morrow'], value='tomorrow this sign shall be — the swarms (8:19)')", 'the swarms\' morrow', words=['למחר'])
mk('Exod 9:5', 'F', [], "M['pestilence_morrow'] = w.clock.day + 1; w.marker('Exod 9:5', M['pestilence_morrow'], value='tomorrow the LORD will do this thing — the pestilence (9:5; 9:6 on the morrow)')", 'the pestilence\'s morrow', words=['מחר'])
mk('Exod 9:18', 'F', [], "M['hail_morrow'] = w.clock.day + 1; w.marker('Exod 9:18', M['hail_morrow'], value='tomorrow at this time — the hail (9:18)')", 'the hail\'s morrow', words=['מחר'])
mk('Exod 10:4', 'F', [], "M['locusts_morrow'] = w.clock.day + 1; w.marker('Exod 10:4', M['locusts_morrow'], value='tomorrow I bring locusts (10:4)')", 'the locusts\' morrow', words=['מחר'])
mk('Exod 10:22', 'F', [3], "M['darkness_end'] = w.clock.day + 3; w.marker('Exod 10:22', M['darkness_end'], value='thick darkness three days (10:22-23)')", 'the darkness\'s three days')
mk('Exod 12:3', 'F', [10], "M['lamb_taken'] = cal_day(w, M['exodus_year'], 1, 10); w.marker('Exod 12:3', M['lamb_taken'], value='on the tenth of this month — the lamb taken (12:3)')", 'the tenth')
mk('Exod 12:6', 'F', [14], "M['lamb_slaughtered'] = cal_day(w, M['exodus_year'], 1, 14); w.marker('Exod 12:6', M['lamb_slaughtered'], value='the fourteenth day of this month — the slaughter between the evenings (12:6)')", 'the fourteenth')
mk('Exod 12:29', 'F', [Fraction(1, 2)], "w.marker('Exod 12:29', M['exodus'], value='at half of the night the LORD struck every firstborn — the night belongs to the fifteenth (the day boundary is the evening): the exodus day (12:41, 12:51)')", 'the night of the fifteenth — the half read [1/2] since THE DEUTERONOMY WALK 1b (2026-09-15; rule 30 THE HALF OF A NAMED WHOLE): a fraction of the night, no day moved')
mk('Exod 14:21', 'F', [], "SD_ = WE.CAL_PARAMS['sea_split_date']['value']; M['sea'] = cal_day(w, M['exodus_year'], SD_['month'], SD_['day']); w.marker('Exod 14:21', M['sea'], value='the sea split — the twenty-first of Nisan by the shelf\\'s row (Sotah 12b:15; the ink gives the sea no date between 12:41 and 15:22)')", 'the sea by the shelf')
mk('Exod 15:22', 'F', [3], "M['shur'] = M['sea'] + 3; w.marker('Exod 15:22', M['shur'], value='three days in the wilderness of Shur without water (15:22)')", 'Shur')
mk('Exod 16:13', 'F', [], "M['manna_first'] = M['sin_wilderness'] + 1; w.marker('Exod 16:13', M['manna_first'], value='in the evening the quail, in the morning the manna — the morrow of the fifteenth (16:1); the shelf\\'s Sunday (Shabbat 87b:5) graded beside it (CS4)')", 'the manna\'s first morning', words=['ובבקר'])
mk('Exod 19:3', 'F', [], "SN = WE.CAL_PARAMS['sinai_days']['value']; M['sinai_2'] = w.clock.day_in('exodus', 1, 3, SN['second_ascent']); w.marker('Exod 19:3', M['sinai_2'], value='Moses went up — the second of Sivan by Rabbi Yose (Shabbat 86b:5; the row sinai_days)')", 'the first ascent')
mk('Exod 19:12', 'F', [], "M['sinai_bound'] = w.clock.day_in('exodus', 1, 3, WE.CAL_PARAMS['sinai_days']['value']['boundary']); w.marker('Exod 19:12', M['sinai_bound'], value='the boundary — the third of Sivan by Rabbi Yose (Shabbat 87a:1)')", 'the boundary')
mk('Exod 19:10', 'F', [], "M['sinai_sep'] = w.clock.day_in('exodus', 1, 3, WE.CAL_PARAMS['sinai_days']['value']['separation']); w.marker('Exod 19:14', M['sinai_sep'], value='sanctify them today and tomorrow — the separation on the fourth of Sivan by Rabbi Yose (Shabbat 87a:1-3: Moses added a day)')", 'the separation (19:10\'s command, 19:14\'s act)', words=['היום', 'ומחר'], at='Exod 19:14')
mk('Exod 19:16', 'F', [], "M['giving'] = w.clock.day_in('exodus', 1, 3, WE.CAL_PARAMS['sinai_days']['value']['giving']); w.marker('Exod 19:16', M['giving'], value='on the third day, when it was morning — the giving on the seventh of Sivan by Rabbi Yose (Shabbat 86b:5; = the tape\\'s ascent marker, Taanit 28b): CS3')", 'the third day', [3])
mk('Exod 12:2', 'F', [], "M['exodus_epoch'] = cal_day(w, M['exodus_year'], 1, 1); w.marker('Exod 12:2', M['exodus_epoch'], value='this month is for you the head of months', era='exodus', new_year_month=1)", 'THE EXODUS EPOCH')
mk('Exod 12:41', 'F', [430], "w.marker('Exod 12:41', M['exodus'], value='at the end of four hundred and thirty years, on that very day: the fifteenth of the month (12:6, 12:29, 12:37)')", 'the exodus day')
mk('Exod 16:1', 'F', [15], "M['sin_wilderness'] = w.clock.day_in('exodus', 1, 2, 15); w.marker('Exod 16:1', M['sin_wilderness'], value='the fifteenth of the second month after the going out')", 'the wilderness of Sin', [2])
mk('Exod 19:1', 'F', [], "M['sinai'] = w.clock.day_in('exodus', 1, 3, 1); w.marker('Exod 19:1', M['sinai'], value='the third month, on this day — the new moon by Rava (Shabbat 86b:5): a transfer, taught')", 'Sinai', [3])
mk('Exod 24:18', 'F', [40, 40], "M['ascent'] = w.clock.day_in('exodus', 1, 3, 7); w.marker('Exod 24:18', M['ascent'], value='forty days and forty nights — Moses ascended on the seventh of Sivan (Taanit 28b:8-9): a transfer, taught')", 'the ascent (Taanit 28b places it)', place='reading_placed')
mk('Exod 32:19', 'F', [], "M['breaking'] = w.clock.day_in('exodus', 1, 4, 17); w.marker('Exod 32:19', M['breaking'], value='the tablets broken — the seventeenth of Tammuz (Mishnah Taanit 4:6; Taanit 28b:9): a transfer, taught')", 'the breaking (Mishnah Taanit 4:6 places it)', place='reading_placed')
mk('Exod 32:30', 'F', [], "M['morrow'] = M['breaking'] + 1; w.marker('Exod 32:30', M['morrow'], value='and it was on the morrow — the intercession\\\'s ascent (32:31): the ink\\\'s own day-word')", 'the morrow of the breaking (O1)', words=['ממחרת'])
mk('Exod 34:28', 'F', [40, 40, 10], "M['second_tablets'] = w.clock.day_in('exodus', 1, WE.CAL_PARAMS['second_tablets_given']['value']['month'], WE.CAL_PARAMS['second_tablets_given']['value']['day']); M['second_ascent'] = M['second_tablets'] - 40; w.marker('Exod 34:4', M['second_ascent'], value='he rose early in the morning — the second ascent, forty days (34:28) before the last tablets given on Yom Kippur (Taanit 30b:8; Bava Batra 121a:6): a transfer, taught; the tradition\\\'s first of Elul not on the local shelf')", 'the second ascent dated by the shelf (O1); the number\'s verse 34:28, the position 34:2 before the ascent\'s event', at='Exod 34:2')
mk('Exod 40:17', 'F', [1], "M['erected'] = w.clock.day_in('exodus', 2, 1, 1); w.marker('Exod 40:17', M['erected'], value='the first month of the second year, the first of the month: the tabernacle erected (Shabbat 87b:6 the ten crowns)')", 'the erection', [1])
mk('Lev 8:2', 'R', [2], "M['lev8'] = M['erected'] - 7; w.marker('Lev 8:2', M['lev8'], value='the installation begins seven days before the eighth (8:33, 9:1) = the twenty-third of Adar, by Shabbat 87b:6 (first for the priesthood): RETROGRADE')", 'the installation: retrograde — nums [2] retyped 2026-09-10 (THE NUMBERS WALK 2b): the construct rule reads \'the TWO rams\' (שני האילים) at 8:2')
mk('Lev 9:1', 'F', [], "M['ninth_first'] = M['erected']; w.marker('Lev 9:1', M['ninth_first'], value='on the eighth day: the stretch ends at the erection\\'s day')", 'the eighth day', [8])
# ---- THE NUMBERS WALK 1b (2026-09-09; NUMBERS_WALK.md "Sitting 1b"): THE BOOK'S OPENING MARKER — the first of the second month of the second year, text-constrained, FORWARD from the erection; it stands BEFORE 9:5 in verse order and makes that marker RETROGRADE (Pesachim 6b:7: 'no earlier and later') ----
mk('Num 1:1', 'F', [1], "M['bamidbar'] = w.clock.day_in('exodus', 2, 2, 1); w.marker('Num 1:1', M['bamidbar'], value='and the LORD spoke to Moses in the wilderness of Sinai, in the tent of meeting, on the first of the second month in the second year of their going out of Egypt (1:1) — the census commanded; the run on the same day (1:18); the tape\\'s FORWARD marker whose successor in the text, 9:1-5, is earlier in time (Pesachim 6b:6-8)')", 'the first of the second month, year two', [2])
# ---- THE NUMBERS WALK 2b (2026-09-10; NUMBERS_WALK.md "Sitting 2b"): NASO'S FOURTEEN MARKERS, every one RETROGRADE after 1:1's (2, 2, 1) — the send-out's section placed on the erection's day by the shelf (R. Levi, Gittin 60a:17: reading-placed); 7:1 'on the day Moses finished setting up the tabernacle' = the erection's day (Exod 40:17; the day-stack of Sifrei 44:1, Shabbat 87b); the twelve day-heads by their ordinals (7:12-66) and numerals (7:72 [11] after the eleven rule, 7:78 [12]) at erected + (n - 1) — the dedication's schedule the retro-writes are checked against (CD6) ----
mk('Num 5:1', 'R', [], "M['send_out_day'] = M['erected']; w.marker('Num 5:1', M['send_out_day'], value='the sending away of the impure (5:1-4) — READING-PLACED on the day the tabernacle was erected: R. Levi\\'s eight sections said on the first of Nisan (Gittin 60a:17; the Levites\\' section 8:5-26 among them): RETROGRADE after 1:1, the teacher named')", 'the send-out\'s day: reading-placed, the erection\'s (Gittin 60a:17)', place='reading_placed')
mk('Num 7:1', 'R', [], "M['dedication_day'] = M['erected']; w.marker('Num 7:1', M['dedication_day'], value='and it was on the day Moses finished setting up the tabernacle (7:1; Exod 40:33 the finishing) — the erection\\'s day, exodus (2, 1, 1), stated after 1:1\\'s (2, 2, 1): RETROGRADE (Pesachim 6b:7); the wagons (7:2-9) and the dedication brought (7:10) dated here; the twelve days follow')", 'the dedication\'s day: the erection\'s (no numeral; the finishing verb the seat)')
for n, (v, ords) in enumerate([(12, [1]), (18, [2]), (24, [3]), (30, [4]), (36, [5]), (42, [6]), (48, [7]), (54, [8]), (60, [9]), (66, [10]), (72, None), (78, None)], 1):
    nums = [] if ords is not None else [n]
    mk('Num 7:%d' % v, 'R', nums, "M['dedication_day_%d'] = M['erected'] + %d; w.marker('Num 7:%d', M['dedication_day_%d'], value='the %s day of the dedication (7:%d) — the anointing day + %d (one prince per day, 7:11; the twelve days one continuous period, Moed Katan 9a): RETROGRADE')" % (n, n - 1, v, n, ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'][n - 1], v, n - 1), 'the dedication\'s day %d: the anointing day + %d (the ink\'s %s)' % (n, n - 1, 'ordinal' if ords is not None else 'numeral'), ords)
# ---- THE TENT sitting 2 (2026-09-09; THE_TENT.md section 2): NUMBERS' FIRST MARKER — the second year's Passover, FORWARD from the erection ----
# THE NUMBERS WALK 3b (2026-09-10; NUMBERS_WALK.md "Sitting 3b"): Beha'alotcha's four FORWARD markers — 10:11 the ink's own date; the three
# READING-PLACED by Taanit 29a:2-5 (the three days' journey, Hazeroth, Paran) — the ink's three durations run as timers between them
mk('Num 10:11', 'F', [20], "M['march'] = w.clock.day_in('exodus', 2, 2, 20); w.marker('Num 10:11', M['march'], value='in the second year, in the second month, on the twentieth of the month, the cloud was taken up (10:11) — the ink\\'s own date: the FORWARD marker after 1:1\\'s (2, 2, 1); Rosh Hashanah 3a:5 Nisan and Iyar in one year')", 'the march: the ink\'s own date, forward — THE NUMBERS WALK 3b', ords=[2])
mk('Num 11:1', 'F', [], "M['taberah'] = M['march'] + 3; w.marker('Num 11:1', M['taberah'], value='the three days\\' journey elapsed (10:33) — READING-PLACED by Taanit 29a:3 (twenty plus three: the twenty-third); the murmuring at Taberah')", 'Taberah: reading-placed, the march plus three — the three-days timer fires here (CE2)', place='reading_placed')
mk('Num 11:35', 'F', [], "M['hazeroth'] = w.clock.day_in('exodus', 2, 3, 22); w.marker('Num 11:35', M['hazeroth'], value='the arrival at Hazeroth — READING-PLACED by Taanit 29a:4 (the twenty-ninth of Sivan less the seven days shut out: the twenty-second; the month of flesh ended here on the shelf\\'s count)')", 'Hazeroth: reading-placed, the twenty-second of Sivan — the month timer fires two days after (CE3 DIVERGE expected)', place='reading_placed')
mk('Num 12:16', 'F', [], "M['paran'] = w.clock.day_in('exodus', 2, 3, 29); w.marker('Num 12:16', M['paran'], value='the journey from Hazeroth to Paran — READING-PLACED by Taanit 29a:4-5 (until the twenty-ninth of Sivan; the baraita: the spies sent that day); Seder Olam Rabbah 8:2 the twenty-eighth (the row spies_sent_day)')", 'Paran: reading-placed, the twenty-ninth of Sivan — Miriam\'s seven fire here (CE4)', place='reading_placed')
mk('Num 13:25', 'F', [40], "M['spies_return'] = w.clock.day_in('exodus', 2, 5, 9); w.marker('Num 13:25', M['spies_return'], value='and they returned from spying out the land at the end of forty days (13:25) — READING-PLACED by Taanit 29a:5 (the baraita: sent on the twenty-ninth of Sivan, returned on the Ninth of Av; the gemara: forty days minus one, thirty-nine; Abaye: Tammuz full — the row tammuz_length); Mishnah Ta\\'anit 4:6 the decree\\'s day; the forty days\\' timer fires the day after (CF2)')", 'the return: reading-placed, the Ninth of Av of year 2 — the forty days\' timer fires at (2, 5, 10), the day after (CF2); THE NUMBERS WALK 4b', place='reading_placed')
mk('Num 9:5', 'R', [14], "M['num9_pesach'] = w.clock.day_in('exodus', 2, 1, 14); w.marker('Num 9:5', M['num9_pesach'], value='and they kept the Passover in the first month, on the fourteenth day of the month (9:5) — the second year (9:1): the counter\\'s first move past the erection\\'s day; the erection\\'s morrow timers fire on this walk')", 'the second year\'s Passover: the fourteenth of the first month (the ordinal first at 9:5)', [1])
# ---- THE NUMBERS WALK 6b (2026-09-11; NUMBERS_WALK.md "Sitting 6b"): CHUKAT'S FOUR MARKERS IN THE FORTIETH YEAR — the arrival at Zin, the journey to Mount Hor, Aaron's death (33:38 read whole by the taught ordinal reader), the journey from Mount Hor after the thirty days ----
mk('Num 20:1', 'F', [], "M['zin'] = w.clock.day_in('exodus', 40, 1, 1); w.marker('Num 20:1', M['zin'], value='and the children of Israel came to the wilderness of Zin in the first month (20:1) — the month the ink\\'s own word, the year the itinerary\\'s (33:38\\'s stretch); READING-PLACED on the new moon of Nisan by Seder Olam Rabbah 9:2 (\\'it was the fortieth year, and it was the new moon of Nisan\\' — the well removed); Miriam died in the same verse: the shelf\\'s tenth of Nisan (Seder Olam 10:2) the row miriam_death_day\\'s other arm — CM5')", 'the arrival at Zin: reading-placed, the new moon of Nisan of the fortieth year (Seder Olam 9:2); the ordinal first at 20:1', [1], place='reading_placed')
mk('Num 20:22', 'F', [], "M['hor_arrival'] = w.clock.day_in('exodus', 40, 4, 1); w.marker('Num 20:22', M['hor_arrival'], value='and they journeyed from Kadesh and came to Mount Hor (20:22) — READING-PLACED by Seder Olam Rabbah 9:2 (\\'Israel stayed there three months\\': Nisan, Iyar, Sivan at Kadesh — the messengers to Edom sent in that stay); the first of Tammuz the departure')", 'the journey to Mount Hor: reading-placed, three months after the new moon (Seder Olam 9:2)', place='reading_placed')
mk('Num 20:28', 'F', [], "M['aaron_death'] = w.clock.day_in('exodus', ink_ordinals(verse_words('Num', 33, 38))[0], ink_ordinals(verse_words('Num', 33, 38))[1], ink_numbers(verse_words('Num', 33, 38))[0]); w.marker('Num 20:28', M['aaron_death'], value='and Aaron died there on the top of the mountain (20:28) — TEXT-CONSTRAINED by Num 33:38\\'s own stamp: in the fortieth year, in the fifth month, on the first of the month — the year by the taught ordinal reader (rule 20), the month and the day by the readers: (40, 5, 1); 33:39 his age 123; Seder Olam 10:2 \\'Aaron on the first of Av\\'')", 'Aaron\'s death: the ink\'s own full date on 33:38, read whole by the parser — the book\'s one full death-date', at='Num 20:28')
mk('Num 21:4', 'F', [], "M['hor_departure'] = M['aaron_death'] + ink_numbers(verse_words('Num', 20, 29))[0]; w.marker('Num 21:4', M['hor_departure'], value='and they journeyed from Mount Hor by the way of the Red Sea (21:4) — TEXT-CONSTRAINED by the ink\\'s own arithmetic: Aaron\\'s death (33:38) + the thirty days of weeping (20:29, [30] by the parser) = (40, 6, 1), the journey not before the mourning\\'s end; 14:25\\'s turn-back RUN; the thirty-eight years\\' timer (CF3, due (40, 5, 9)) and the mourning\\'s (due (40, 6, 1)) both fire on this walk')", 'the journey from Mount Hor: the death-date plus the thirty days, both the ink\'s numbers (33:38, 20:29)')
# ---- THE TENT sitting 4 (2026-09-09; THE_TENT.md section 4): NUMBERS' SECOND MARKER — the daughters' case READING-PLACED in the fortieth year; THE NUMBERS WALK 6b (2026-09-11): its day MOVED from the modeled (40, 5, 1) to the running counter after Chukat's markers (40, 6, 1) — the year Aaron died stays the reading's placement (Sifrei 133:3; Seder Olam 9:2 'standing at Arvot Moab' after the conquest), the day no longer a stand-in ----
mk('Num 27:1', 'F', [], "M['daughters'] = w.clock.day_in('exodus', 40, 6, 1); w.marker('Num 27:1', M['daughters'], value='the daughters of Zelophehad drew near — READING-PLACED in the fortieth year, the year Aaron died (Sifrei Bamidbar 133:3: Eleazar in the court\\'s roster dates the case; Seder Olam Rabbah 9:2: \\'standing at Arvot Moab\\' after Sihon and Og, the plague and the census; Bava Batra 121a:9: after the wilderness generation stopped dying, the fifteenth of Av of that year); the day the tape\\'s running counter after Chukat\\'s markers, (40, 6, 1) — THE NUMBERS WALK 6b moved it from the modeled (40, 5, 1) (THE TENT sitting 4\\'s stand-in for the year, before the fortieth year had its own markers); its own literal, not a Chukat name (THE REST drops those)')", 'the daughters: reading-placed, the fortieth year — the day the running counter after Chukat (6b), no numbers on 27:1', place='reading_placed')

# ---- THE NUMBERS WALK 8b (2026-09-11; NUMBERS_WALK.md "Sitting 8b"): THE SECOND CENSUS'S MARKER — 25:19 'and it was after the plague', READING-PLACED at the counter's own day (40, 6, 1): no day in the ink or on the shelf, the ORDER Seder Olam Rabbah 9:2's (Arvot Moab, the plague, the census, the daughters); the half-verse carries no numeral; the five census lines follow page_order ----
mk('Num 25:19', 'F', [], "M['after_the_plague'] = w.clock.day_in('exodus', 40, 6, 1); w.marker('Num 25:19', M['after_the_plague'], value='and it was after the plague (25:19) — READING-PLACED at the counter\\'s own day (40, 6, 1): no day in the ink or on the shelf; the ORDER Seder Olam Rabbah 9:2\\'s (Arvot Moab, the plague, the census, the daughters); the second census\\'s five lines follow page_order; the daughters\\' marker at 27:1 the same day')", 'after the plague: reading-placed at the counter\'s day — the order the shelf\'s, no numeral on the half-verse (THE NUMBERS WALK 8b)', place='reading_placed')

# ---- THE DEUTERONOMY WALK 1b (2026-09-15; DEUTERONOMY_WALK.md "Sitting 1b" THE DESIGN (a) THE ONE CLOCK): THE FIFTH BOOK'S FIRST MARKERS — the speech's
# date FORWARD at Deut 1:3 by the NUMBER reader [40, 11, 1] (the era the exodus's by the taught verbal analogy with Numbers 33:38's "fortieth year", Rosh
# Hashanah 2b:11 — JO.aarons_death_retold('verbal_analogy') by CALL; the ordinal reader's [40, 5] there, the number reader's here: one clock, two readers),
# placed at the tape POSITION Deut 1:1 so the speech's line wears text_constrained (as Genesis 21:5's number sits at 21:2); THREE RETROGRADE markers
# (reading_placed TYPED: the retelling's "at that time" gives no number — each day is the tape's own placement of the act the supplied line belongs beside)
# ----
mk('Deut 1:3', 'F', [40, 11, 1], "M['speech'] = w.clock.day_in('exodus', ink_numbers(verse_words('Deut', 1, 3))[0], ink_numbers(verse_words('Deut', 1, 3))[1], ink_numbers(verse_words('Deut', 1, 3))[2]); w.marker('Deut 1:1', M['speech'], value='and it came to pass in the fortieth year, in the eleventh month, on the first of the month, that Moses spoke (1:3) — the NUMBER reader [40, 11, 1] read whole; the year the exodus\\'s by the verbal analogy with 33:38\\'s fortieth year (Rosh Hashanah 2b:11 — a transfer taught, the journeys runner\\'s cell by CALL); the FORWARD marker after Num 27:1\\'s (40, 6, 1), the counter\\'s last move in the Torah\\'s fourth book crossed: thirty-six timers fire on the walk; positioned at 1:1, the book\\'s first verse')", 'the speech\'s date: the ink\'s own full date at 1:3 read by the number reader — the numbers at 1:3, the position 1:1 (the book\'s first line wears it)', at='Deut 1:1')
mk('Deut 1:6', 'R', [], "M['horeb_departure_told'] = M['march']; w.marker('Deut 1:6', M['horeb_departure_told'], value='the LORD our God spoke to us in Horeb, saying: you have dwelt long enough in this mountain; turn and take your journey (1:6-7) — the departure from Horeb TOLD ONLY HERE, dated at the day the tape gives the departure it belongs beside: Num 10:11\\'s (2, 2, 20) (the cloud taken up; Exodus 33:1 the command\\'s kin): RETROGRADE after 1:3\\'s (40, 11, 1) — Pesachim 6b:7\\'s class; the supplied line\\'s debit CLOSED at once by the prior run Num 12:16')", 'the departure from Horeb retold: reading-placed at the march\'s day (2, 2, 20) — the retelling\'s own "at that time" gives no number', place='reading_placed')
mk('Deut 1:9', 'R', [], "M['courts_founded'] = ([e['day'] for e in w.entities['israel'].ledger if e['effect'] == 'courts_established'] if 'israel' in w.entities else [w.clock.day_in('exodus', 1, 2, 16)])[0]; w.marker('Deut 1:9', M['courts_founded'], value='and I spoke to you at that time, saying: I am not able to bear you myself alone (1:9) — the judges\\' appointment and charge (1:9-18) TOLD HERE with the charge only here, dated at the day of the court\\'s founding READ OFF ISRAEL\\'S LEDGER: the courts_established entry\\'s own day (Exodus 18:25-26 — (1, 2, 16) on the tape; the bare prediction world falls back to that day): RETROGRADE; the charge\\'s line judges_charged dated here')", 'the judges charged: reading-placed at the court\'s founding day, read off the ledger by the marker\'s code (never typed on the tape; the fallback the bare world\'s alone)', place='reading_placed')
mk('Deut 2:2', 'R', [], "M['hor_departure_told'] = M['hor_departure']; w.marker('Deut 2:2', M['hor_departure_told'], value='and the LORD spoke to me, saying: you have compassed this mountain long enough; turn you northward (2:2-3) — the turn, the bars on Esau, Moab and Ammon, the Zered, the war on Sihon, the bans, Joshua\\'s encouragement and the plea TOLD HERE, dated at the departure from Mount Hor (21:4\\'s text-constrained (40, 6, 1) — the counter\\'s day for the whole stretch to the plains): RETROGRADE; the supplied debits CLOSED at once by the prior runs Num 21:10-13, 21:12, 21:24-25; the plea and the charges \\'at that time\\' after Sihon and Og (the Sifrei 26:8) inside this stretch')", 'the bypass and the plea retold: reading-placed at the departure from Mount Hor (40, 6, 1) — the stretch runs to the book\'s last line of the sitting', place='reading_placed')
# THE DEUTERONOMY WALK 2b (2026-09-16; DEUTERONOMY_WALK.md "Sitting 2b" (R3)): THE TAPE'S HOLE WRITTEN ONCE AT ITS OWN TIME — two RETROGRADE markers dating
# the two SUPPLIED Horeb lines (Exodus 20:1's ten words, 31:18's tablets — first tellings with no line on the tape): the ink's dating word "the day you
# stood before the LORD your God at Horeb" (4:10) = the giving's day (1, 3, 7) — the tape's own marker at Exod 19:16 (Rabbi Yose's seventh, the sinai_days
# row); the tablets given the fortieth day of 24:18's forty = the breaking's day (1, 4, 17) — the tape's own marker at Exod 32:19 (Taanit 28b:9: given and
# broken on one day); reading_placed TYPED (the retelling gives no number; the days the tape's own placements of the acts the lines belong beside)
mk('Deut 4:1', 'F', [], "M['chapter_4'] = M['speech']; w.marker('Deut 4:1', M['chapter_4'], value='and now, Israel, hear (4:1) — chapter 4 opens at the speech\\'s own day: the retrograde stretch of 1b\\'s Deut 2:2 marker (the bypass and the plea dated (40, 6, 1)) ENDED, the counter\\'s day (40, 11, 1) re-asserted (the stitcher\\'s placement print found the exhortation\\'s line inside the old stretch, 2026-09-16); FORWARD at the same day, Lev 9:1\\'s form')", 'chapter 4 opens: the 1b stretch ends at the speech\'s day (4:1)')
mk('Deut 4:10', 'R', [], "M['giving_told'] = M['giving']; w.marker('Deut 4:10', M['giving_told'], value='the day you stood before the LORD your God at Horeb (4:10) — the ten words declared TOLD HERE with no line on the tape (Exodus 20:1 the first telling): dated at the giving\\'s day, Exod 19:16\\'s (1, 3, 7) by Rabbi Yose (Shabbat 86b:5): RETROGRADE after 1:3\\'s (40, 11, 1) — Pesachim 6b:7\\'s class; the supplied line writes covenant_declared on Israel')", 'the ten words told: retrograde at the giving (Exod 19:16)', place='reading_placed')
mk('Deut 4:13', 'R', [10, 2], "M['tablets_told'] = M['breaking']; w.marker('Deut 4:13', M['tablets_told'], value='and he wrote them on two tablets of stone (4:13) — the tablets given TOLD HERE with no line on the tape (Exodus 31:18 the first telling): dated at the fortieth day of the ascent = the breaking\\'s day, Exod 32:19\\'s (1, 4, 17) (Taanit 28b:9 — the seventh of Sivan plus forty; given and broken on one day, 32:15): RETROGRADE; the supplied line writes tablets_delivered on Moses')", 'the tablets told: retrograde at the breaking (Exod 32:19)', place='reading_placed')
mk('Deut 4:25', 'F', [], "M['speech_resumed'] = M['speech']; w.marker('Deut 4:25', M['speech_resumed'], value='when you beget sons (4:25) — the speech resumes at its own day: the retrograde stretch of the two supplied Horeb lines ENDED, the counter\\'s own day (40, 11, 1) re-asserted (the engine\\'s stretch runs to the next marker — found at the first generator run, 2026-09-16); FORWARD at the same day, Lev 9:1\\'s form')", 'the stretch ends at the speech\'s day (4:25) — a forward marker to the counter\'s own day')
# THE DEUTERONOMY WALK 3b (2026-09-16; DEUTERONOMY_WALK.md "Sitting 3b" (L5)): THE TAPE'S SECOND HOLE WRITTEN ONCE AT ITS OWN TIME — one RETROGRADE
# marker dating the two SUPPLIED lines (the request for a mediator, Exodus 20:18-19's first telling with no line on the tape; the answer told only here):
# the ink's dating words "when you heard the voice … you came near to me" (5:23) = the giving's day (1, 3, 7) — the tape's own marker at Exod 19:16
# (Rabbi Yose's seventh, the sinai_days row); reading_placed TYPED (the retelling gives no number); a FORWARD marker at 5:32 ends the stretch (2b's lesson 1)
mk('Deut 5:23', 'R', [], "M['request_told'] = M['giving']; w.marker('Deut 5:23', M['request_told'], value='when you heard the voice out of the midst of the darkness … you came near to me, all the heads of your tribes and your elders (5:23) — the request for a mediator TOLD HERE with no line on the tape (Exodus 20:18-19 the first telling — the tape\\'s second hole; the answer 5:28-31 told only here): dated at the giving\\'s day, Exod 19:16\\'s (1, 3, 7) by Rabbi Yose (Shabbat 86b:5; Yoma 4b:3): RETROGRADE after 4:25\\'s (40, 11, 1) — Pesachim 6b:7\\'s class; the supplied lines write torah_through_moses on Israel, the charge to teach on Moses (closed by the prior run) and returned_to_tents on Israel')", 'the request told: retrograde at the giving (Exod 19:16)', place='reading_placed')
mk('Deut 5:32', 'F', [], "M['charge'] = M['speech']; w.marker('Deut 5:32', M['charge'], value='and you shall observe to do as the LORD your God commanded you (5:32) — the charge at the speech\\'s own day: the retrograde stretch of the request and the answer ENDED, the counter\\'s own day (40, 11, 1) re-asserted (a retrograde stretch runs to the next marker — 2b\\'s lesson 1); FORWARD at the same day, Lev 9:1\\'s form; the charge 5:32-33 writes nothing (the receipt a run citation of the giving, the register seat CHAPTER)')", 'the stretch ends at the charge (5:32) — a forward marker to the counter\'s own day')
# THE DEUTERONOMY WALK 7b (2026-09-19; DEUTERONOMY_WALK.md "Sitting 7b" THE LINES ON THE TAPE): AARON'S PERIL WRITTEN ONCE AT ITS OWN TIME — one RETROGRADE
# marker dating the one SUPPLIED line (9:20 — "and I prayed for Aaron also at that time": told only here, Exodus 32:21-24 and 32:35 hold no anger at Aaron and no
# prayer for him; the tape's hole): the ink's dating words "at that time" = the second forty (9:18-19: the prayer for Israel, then "also" for Aaron) = the morrow
# of the breaking, the tape's own marker at Exod 32:30 (M['morrow'] = M['breaking'] + 1, (1, 4, 18)); reading_placed TYPED (the retelling gives no number;
# Sanhedrin 102a:5 reads "at that time" as a time ordained for calamity); a FORWARD marker at 9:21 ends the stretch (2b's lesson 1; 4:25's and 5:32's form)
mk('Deut 9:20', 'R', [], "M['aaron_told'] = M['morrow']; w.marker('Deut 9:20', M['aaron_told'], value='and with Aaron the LORD was very angry, to destroy him; and I prayed for Aaron also at that time (9:20) — Aaron\\'s peril TOLD ONLY HERE with no line on the tape (Exodus 32:21-24 Aaron\\'s report, 32:35 the plague — no anger at Aaron, no prayer for him: the tape\\'s hole): dated at the second forty\\'s ascent, the morrow of the breaking, Exod 32:30\\'s (1, 4, 18) (\\'at that time\\' the second forty — 9:18-19 the prayer for Israel, then \\'also\\' for Aaron; Sanhedrin 102a:5 a time ordained for calamity): RETROGRADE after 5:32\\'s (40, 11, 1) — Pesachim 6b:7\\'s class; the supplied line writes destruction_halved on aaron (Vayikra Rabbah 10:5 — half the edict withheld)')", 'Aaron\'s peril told: retrograde at the morrow of the breaking (Exod 32:30)', place='reading_placed')
mk('Deut 9:21', 'F', [], "M['speech_resumed_9'] = M['speech']; w.marker('Deut 9:21', M['speech_resumed_9'], value='and your sin, the calf which you had made, I took and burned it with fire (9:21) — the speech resumes at its own day: the retrograde stretch of Aaron\\'s peril ENDED, the counter\\'s own day (40, 11, 1) re-asserted (a retrograde stretch runs to the next marker — 2b\\'s lesson 1); FORWARD at the same day, 4:25\\'s and 5:32\\'s form; the calf\\'s destruction a readback row, no write')", 'the stretch ends at the calf\'s destruction (9:21) — a forward marker to the counter\'s own day')
# THE DEUTERONOMY WALK 8b (2026-09-20; DEUTERONOMY_WALK.md "Sitting 8b" THE LINES ON THE TAPE): THE FORMS COMBINED — TWO RETROGRADE markers dating two acts
# TOLD ONLY HERE (the fragments in the ark at the erection's day — Exod 40:20's testimony placed, (2, 1, 1); Aaron's burial at his death — Num 20:28's
# (40, 5, 1) from 33:38's ordinals; reading_placed TYPED: the retelling gives no number, the days the tape's own placements of the acts the lines belong
# beside) and ONE FORWARD marker ending the stretch at the speech's own pivot ('and now, Israel' — 4:1's word, 10:12) before the four own-day lines
mk('Deut 10:2', 'R', [], "M['fragments_told'] = M['erected']; w.marker('Deut 10:2', M['fragments_told'], value='and you shall put them in the ark (10:2) — THE FRAGMENTS IN THE ARK TOLD ONLY HERE with no line on the tape (Exodus 34:1 has no ark clause; 40:20 places the whole tablets alone: the tape hole named at 7b): dated at the erection day, the testimony placed, Exod 40:20 (2, 1, 1) — the shelf reads the clause of both sets (Menachot 99a:12; Bava Batra 14b:6): RETROGRADE after 9:21 (40, 11, 1) — Pesachim 6b:7 class; the supplied line writes fragments_in_the_ark on the ark (the tablets and the fragments; the scroll inside or beside — Bava Batra 14a-b)')", 'the fragments in the ark told: retrograde at the erection\'s day (Exod 40:17)', place='reading_placed')
mk('Deut 10:6', 'R', [], "M['burial_told'] = M['aaron_death']; w.marker('Deut 10:6', M['burial_told'], value='and he was buried there (10:6) — AARON BURIED, TOLD ONLY HERE with no line on the tape (Numbers 20:28 the death, 20:29 the mourning, 33:38-39 the date and the age — never the burial): dated at his death, Num 20:28 (40, 5, 1) from 33:38 ordinals: RETROGRADE after 10:2 (2, 1, 1) — the second retrograde marker of the chapter; the supplied line writes buried on aaron (the status REUSED — the ninth buried); the place OPEN inside the line (Moserah in the retelling, Mount Hor on the tape — Seder Olam Rabbah 9:2 the retreat of seven stations, the parameter)')", 'Aaron\'s burial told: retrograde at his death (Num 20:28)', place='reading_placed')
mk('Deut 10:12', 'F', [], "M['speech_resumed_10'] = M['speech']; w.marker('Deut 10:12', M['speech_resumed_10'], value='and now, Israel (10:12) — the speech resumes at its own day: the retrograde stretch of the burial ENDED, the counter own day (40, 11, 1) re-asserted (a retrograde stretch runs to the next marker — 2b lesson 1); FORWARD at the same day, 4:25, 5:32 and 9:21 form; the four own-day lines follow with no marker of their own (the laws restated — STATUTE by form)')", 'the stretch ends at the pivot (10:12) — a forward marker to the counter\'s own day')

# THE DEUTERONOMY WALK 9b (2026-09-20; DEUTERONOMY_WALK.md "Sitting 9b" THE LINES ON THE TAPE): NO MARKER — chapter 11's two lines (second_paragraph_declared 11:13-21,
# blessing_and_curse_set 11:26-32) are OWN-DAY lines at the counter's (40, 11, 1), STATUTE by form, joined after the tape's last Deuteronomy 10 line by the sort (page_order);
# every act the chapter retells has a line (measured at the design) — no retrograde marker; the markers' list above 8b's exactly (172)
# THE DEUTERONOMY WALK 10b (2026-09-21; DEUTERONOMY_WALK.md "Sitting 10b" THE LINES ON THE TAPE): NO MARKER — chapter 12's FOUR lines (demolition_restated 12:1-4,
# place_chosen_declared 12:5-14, profane_slaughter_permitted 12:15-28, nations_cut_off_warned 12:29-31) are OWN-DAY lines at the counter's (40, 11, 1), STATUTE by form,
# joined after the tape's last Deuteronomy 11 line by the sort (page_order); no act told only here (the kin's lines measured at the design) — no retrograde marker; the
# markers' list above 9b's exactly (172)
# THE DEUTERONOMY WALK 11b (2026-09-21; DEUTERONOMY_WALK.md "Sitting 11b" THE LINES ON THE TAPE): NO MARKER — chapter 13's FOUR lines (word_sealed 13:1,
# prophet_test_declared 13:2-6, inciter_law_declared 13:7-12, condemned_city_law_declared 13:13-19) are OWN-DAY lines at the counter's (40, 11, 1), STATUTE by form,
# joined after the tape's last Deuteronomy 12 line by the sort (page_order); no act told only here (the kin's lines measured at the design) — no retrograde marker; the
# markers' list above 10b's exactly (172)
# THE DEUTERONOMY WALK 12b (2026-09-22; DEUTERONOMY_WALK.md "Sitting 12b" THE LINES ON THE TAPE): NO MARKER — chapter 14's FIVE lines (sons_and_mourning_declared 14:1-2,
# food_law_declared 14:3-20, carcass_and_kid_declared 14:21, second_tithe_declared 14:22-27, third_year_tithe_declared 14:28-29) are OWN-DAY lines at the counter's
# (40, 11, 1), STATUTE by form, joined after the tape's last Deuteronomy 13 line by the sort (page_order); no act told only here (the kin's lines measured at the design)
# — no retrograde marker; the markers' list above 11b's exactly (172)
# THE DEUTERONOMY WALK 13b (2026-09-23; DEUTERONOMY_WALK.md "Sitting 13b" THE LINES ON THE TAPE): NO MARKER — chapter 15's FOUR lines (release_law_declared 15:1-6,
# hand_opening_commanded 15:7-11, hebrew_slave_law_declared 15:12-18, firstling_law_declared 15:19-23) are OWN-DAY lines at the counter's (40, 11, 1), STATUTE by form,
# joined after the tape's last Deuteronomy 14 line by the sort (page_order); the chapter's one narrative verb (15:15 'and He redeemed you') a REFERENCE row on the
# tape's sent_out at Exod 12:31, never a second act — no retrograde marker; the markers' list above 12b's exactly (172)

# verify every marker's numbers against the ink NOW (the runner re-verifies at run time)
bad = []
for verse, cls, nums, ords, code, note, at, words, place in MK:
    m = FIRST.match(verse); ws = verse_words(m.group(1), int(m.group(2)), int(m.group(3)))
    got, gord = ink_numbers(ws), ink_ordinals(ws)
    if got != nums or (ords is not None and gord != ords) or (words is not None and not all(x in ws for x in words)):
        bad.append((verse, nums, got, ords, gord, ' '.join(ws)[:80]))
if bad:
    for b in bad: print('INK MISMATCH', b)
    sys.exit('the marker table disagrees with the ink parse — fix the table or the parser before stitching')
print('markers: %d, every number verified against the ink parse (F %d / P %d / R %d)' % (len(MK), sum(c == 'F' for _, c, *_ in MK), sum(c == 'P' for _, c, *_ in MK), sum(c == 'R' for _, c, *_ in MK)))

# ---- O9 T2 (2026-09-08; CLOCK.md 12b): THE PLACEMENT CLASS per marker row — COMPUTED, never recited ----
# reading_placed when the row (i) reads a third-registry row whose placement key says `places`, (ii) carries a typed shelf number
# (place='reading_placed'), or (iii) reads an M key a reading-placed row assigned (propagation, in tape order; a text row's write
# takes its key back); `refines` rows leave the class text_constrained; a typed text overrides (the exodus row: the running branch)
PLACES = {k for k, r in WE.CAL_PARAMS.items() if r.get('placement') == 'places'}
RD, WR, CPR, CALL = re.compile(r"M\['([^']+)'\]"), re.compile(r"M\['([^']+)'\]\s*="), re.compile(r"CAL_PARAMS\['(\w+)'\]"), re.compile(r"w\.marker\('([^']+)'")
reading_keys = set()
CLASS = {}   # row index in MK -> (class, reason)
for i in sorted(range(len(MK)), key=lambda j: V(MK[j][6])):
    verse, cls, nums, ords, code, note, at, words, place = MK[i]
    writes = set(WR.findall(code)); reads = set(RD.findall(code)) - writes; rows = set(CPR.findall(code))
    if place is not None:
        c, why = place, 'typed'
    elif rows & PLACES:
        c, why = 'reading_placed', 'reads the row %s' % ', '.join(sorted(rows & PLACES))
    elif reads & reading_keys:
        c, why = 'reading_placed', 'propagated from %s' % ', '.join(sorted(reads & reading_keys))
    else:
        c, why = 'text_constrained', 'the ink'
    if c == 'reading_placed':
        reading_keys |= writes
    else:
        reading_keys -= writes
    CLASS[i] = (c, why)


def with_placement(code):
    """inject placement='reading_placed' into the row's w.marker(...) call (the engine's default is text_constrained)"""
    j = code.index('w.marker(') + len('w.marker(')
    depth, q = 1, None
    while depth:
        ch = code[j]
        if q:
            if ch == '\\':
                j += 2; continue
            if ch == q:
                q = None
        elif ch in ('\'', '"'):
            q = ch
        elif ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
        j += 1
    return code[:j - 1] + ", placement='reading_placed'" + code[j - 1:]


MK = [(verse, cls, nums, ords, with_placement(code) if CLASS[i][0] == 'reading_placed' else code, note, at, words, place) for i, (verse, cls, nums, ords, code, note, at, words, place) in enumerate(MK)]
print('\nPLACEMENT CLASSES (computed; the reason per row):')
for i in sorted(range(len(MK)), key=lambda j: V(MK[j][6])):
    print('  %-11s %-9s %-16s %s' % (MK[i][6], MK[i][1], CLASS[i][0], CLASS[i][1]))
MK_CLASS = {i: CLASS[i][0] for i in CLASS}

# ---- 5. MERGE and EMIT ----
def render(e):
    parts = []
    for k, v in e.items():
        if isinstance(v, tuple) and v and v[0] == '__CLOCK__':
            parts.append('%r: w.clock.day + %d' % (k, v[1]))
        else:
            parts.append('%r: %r' % (k, v))
    return '{' + ', '.join(parts) + '}'

items = []   # (key, order, line, meta)
for i, (verse, cls, nums, ords, code, note, at, words, place) in enumerate(MK):
    ordv = '' if ords is None else ', ordinals=%r' % (ords,)
    wv = '' if words is None else ', words=%r' % (words,)
    m = CALL.search(code)
    items.append((V(at), 0, "    assert_ink(%r, %r%s%s); %s   # %s" % (verse, nums, ordv, wv, code, note), ('M', cls, MK_CLASS[i], V(m.group(1)) if m and FIRST.match(m.group(1)) else None)))
# O9 OPEN-5 (CLOCK.md 12e): the event's SLOT from the ink's day-word at its first verse (the runner's slot_of — one copy)
BOOK = {1: 'Gen', 2: 'Exod', 3: 'Lev', 4: 'Num', 5: 'Deut'}   # THE DEUTERONOMY WALK 1b (2026-09-15)
slot_of = INK['slot_of']
for i, h in enumerate(hist):
    k = h['key']
    sl = slot_of(BOOK[k[0]], k[1], k[2])
    if sl:
        h['event']['slot'] = sl
    items.append((h['key'], 1, "    w.submit(%s)   # %s [%s]" % (render(h['event']), h['runner'], h['why']), ('E', sl)))
for c in closes:
    items.append((c['key'], 2, "    w.close(%r, %r, %r%s)   # %s" % (c['args'][0], c['args'][1], c['args'][2], (', value=%r' % (c['args'][3],)) if len(c['args']) > 3 else '', c['runner']), ('C',)))
items.sort(key=lambda t: (t[0], t[1]))                       # a stable sort: the scenes' own order within a verse

# ---- O9 T2 + OPEN-5: the PREDICTED placement stamps (the engine's rule replayed on the tape's order) and the slot census ----
cur, retro_open = (None, None), False
pl_m, pl_e, sl_e = collections.Counter(), collections.Counter(), collections.Counter()
regress, last_slot, stretch_start = [], None, None
for key, order, line, meta in items:
    if meta[0] == 'M':
        _, cls, pc, callv = meta
        if cls == 'P':
            continue                                          # a proleptic marker: the counter unmoved, no class
        pl_m[pc] += 1
        cur, retro_open = (pc, callv), (cls == 'R')
        last_slot, stretch_start = None, key
    elif meta[0] == 'E':
        if retro_open:
            pl_e[cur[0]] += 1
        elif cur[0] and cur[1] is not None and key == cur[1]:
            pl_e[cur[0]] += 1
        else:
            pl_e['page_order'] += 1
        sl = meta[1]
        if sl:
            sl_e[sl] += 1
            if last_slot and WE.Calendar().crosses_day(last_slot[0], sl):
                regress.append((last_slot[1], last_slot[0], key, sl))
            last_slot = (sl, key)
PLACEMENT = {'markers': dict(pl_m), 'events': dict(pl_e)}
SLOTS = dict(sl_e)
print('\nPLACEMENT LITERAL: %r' % (PLACEMENT,))
print('SLOTS LITERAL: %r' % (SLOTS,))
print('SLOT REGRESSIONS (the ink\'s own day-crossings the tape has not marked — reported, never fixed by the engine): %d' % len(regress))
for a, sa, b, sb in regress:
    print('  %s %d:%d %s -> %s %d:%d %s' % (BOOK[a[0]], a[1], a[2], sa, BOOK[b[0]], b[1], b[2], sb))
body = ['def tape(w, M, P):', '    """THE STITCHED TAPE — generated by scratchpad/seq_stitch.py: %d markers, %d history events, %d closes in canonical verse order"""' % (len(MK), len(hist), len(closes)),
        "    assert w.clock.epoch == 'creation', 'the tape runs on the creation epoch'"]
last_ch = None
for key, order, line, meta in items:
    ch = (key[0], key[1])
    if ch != last_ch:
        body.append('    # ---- %s %d ----' % ({1: 'Gen', 2: 'Exod', 3: 'Lev', 4: 'Num', 5: 'Deut'}[key[0]], key[1])); last_ch = ch
    body.append(line)
body.append('    return M')
tape_code = '\n'.join(body) + '\n'
head, rest = SRC.split('# ==== TAPE BEGIN', 1)
mid, tail = rest.split('# ==== TAPE END ====', 1)
first_line = mid.split('\n', 1)[0]
new_src = head + '# ==== TAPE BEGIN' + first_line + '\n' + tape_code + '# ==== TAPE END ====' + tail
open(RUNNER, 'w', encoding='utf-8').write(new_src)
print('tape written into %s: %d lines' % (RUNNER, len(body)))

# ---- 6. PREDICT the markers' days on a bare world (no daemons, no events) ----
G = dict(INK); G.update({'WE': WE, 'assert_ink': lambda *a, **k: None})
w = WE.World(era='prediction', epoch='creation')
M = {}
P = {'sojourn_start': {'value': 'seed_isaac'}, 'covenant_placement': {'value': 'bereshit_rabbah_46_2'}}   # O9 T2: the running settings
for verse, cls, nums, ords, code, note, at, words, place in sorted(MK, key=lambda t: V(t[6])):     # in TAPE order (the position), as the tape runs
    exec(code, G, {'w': w, 'M': M, 'P': P})
C = w.clock.calendar
def D(d): return (C.year(d),) + C.date(d)[1:]
DAYS = collections.OrderedDict()
for k in ('born:seth', 'born:noach', 'born:shem', 'reprieve_decree', 'covenant_pieces', 'boarding_call', 'flood', 'flood_ordinal', 'rain_end', 'window', 'dove_second', 'dove_third', 'hagar_given', 'mamre', 'sodom_dawn', 'binding', 'moriah_seen', 'stew_day', 'blessing', 'mahalath', 'departure', 'laban_month', 'wedding', 'rachel_given', 'fourteen_end', 'flight', 'told', 'heap_morning', 'jabbok_night', 'peniel_sunrise', 'sukkot', 'shechem', 'bethel_again', 'ephrath_road', 'hebron', 'age:joseph:17', 'prison_dreams', 'birthday', 'pharaoh_dreams', 'custody_third', 'joseph30', 'plenty_end', 'famine_two', 'beersheba_descent', 'embalmed', 'weeping_end', 'atad', 'atad_end', 'ark_rested', 'mountains', 'dried', 'dry', 'born:arpachshad', 'born:abraham', 'born:isaac', 'eighth_day', 'born:jacob', 'born:joseph', 'descent', 'jacob_147', 'died:methuselah', 'died:terah', 'born:moses', 'ark', 'speaking', 'river7', 'darkness_end', 'lamb_taken', 'lamb_slaughtered', 'exodus_epoch', 'exodus', 'sea', 'shur', 'sin_wilderness', 'manna_first', 'sinai', 'sinai_2', 'sinai_bound', 'sinai_sep', 'giving', 'ascent', 'breaking', 'morrow', 'second_ascent', 'second_tablets', 'erected', 'lev8'):
    DAYS[k] = (M[k], D(M[k]))
print('\nPREDICTED DAYS (day, (creation year, absolute month, day of month)):')
for k, v in DAYS.items(): print('  %-18s %s' % (k, v))
print('the flood: ark_rested - flood = %d (C1, declared 150); dried - flood = %d; dry - flood = %d' % (M['ark_rested'] - M['flood'], M['dried'] - M['flood'], M['dry'] - M['flood']))
print('the exodus: creation year %d; exodus - descent = %d years; exodus - born:isaac = %d years; Shem by 5:32 %d vs by 11:10 %d' % (
    M['exodus_year'], C.year(M['exodus']) - C.year(M['descent']), C.year(M['exodus']) - C.year(M['born:isaac']), C.year(M['born:shem']), C.year(M['born:shem_by_11_10'])))
print('Sinai: ascent %s; breaking %s = ascent + %d; erected %s; lev8 %s; the exodus era at erected: %r' % (
    D(M['ascent']), D(M['breaking']), M['breaking'] - M['ascent'], D(M['erected']), D(M['lev8']), w.clock.eras['exodus'].date(M['erected'])))
print('O8 S1: Moses born %s, the ark %s (born + 3 months; the shelf\'s sixth of Sivan), the speaking %s, the plagues to %s, the lamb %s / %s, the sea %s, Shur %s, the manna %s, Sivan %s / %s / %s / %s; the weekday (1 = the first day) of the exodus %d, the fifteenth of Iyar %d, the first of Sivan %d, the giving %d' % (D(M['born:moses']), D(M['ark']), D(M['speaking']), D(M['darkness_end']), D(M['lamb_taken']), D(M['lamb_slaughtered']), D(M['sea']), D(M['shur']), D(M['manna_first']), D(M['sinai_2']), D(M['sinai_bound']), D(M['sinai_sep']), D(M['giving']), M['exodus'] % 7 + 1, M['sin_wilderness'] % 7 + 1, M['sinai'] % 7 + 1, M['giving'] % 7 + 1))
print('O8 S2: the reprieve decree %s (the flood minus 120 years — retrograde to the counter at Noah 500), the boarding call %s (the flood minus 7), the rain\'s end %s, the window %s, the dove\'s sendings %s / %s, the drying %s; Hagar given %s (Abram 85), Ishmael %s (86); the flood\'s stretch 7:11 -> 8:14 = %d days = 12 months + %d' % (D(M['reprieve_decree']), D(M['boarding_call']), D(M['rain_end']), D(M['window']), D(M['dove_second']), D(M['dove_third']), D(M['dried']), D(M['hagar_given']), D(M['born:ishmael']), M['dry'] - M['flood'], M['dry'] - C.add(M['flood'], 12, 'month')))
print('O8 S4: the heap\'s morning %s, the Jabbok night %s, the sunrise %s, Sukkot %s, Shechem %s (+18 months), Bethel again %s, the road %s (+6 months), Hebron %s (Jacob %d; Jacob\'s absence %d years), Joseph seventeen %s, the prison dreams %s, the birthday %s, Pharaoh\'s dreams %s = joseph30 %s: %s, the plenty\'s end %s, the famine\'s second %s (Joseph\'s absence %d years) = the descent %s: %s, embalmed %s, the weeping\'s end %s, Atad %s / %s; Isaac\'s death %s = the sale + %d' % (D(M['heap_morning']), D(M['jabbok_night']), D(M['peniel_sunrise']), D(M['sukkot']), D(M['shechem']), D(M['bethel_again']), D(M['ephrath_road']), D(M['hebron']), C.year(M['hebron']) - C.year(M['born:jacob']), C.year(M['hebron']) - C.year(M['departure']), D(M['age:joseph:17']), D(M['prison_dreams']), D(M['birthday']), D(M['pharaoh_dreams']), D(M['joseph30']), M['pharaoh_dreams'] == M['joseph30'], D(M['plenty_end']), D(M['famine_two']), C.year(M['famine_two']) - C.year(M['age:joseph:17']), D(M['descent']), C.year(M['famine_two']) == C.year(M['descent']), D(M['embalmed']), D(M['weeping_end']), D(M['atad']), D(M['atad_end']), D(M['died:isaac']), C.year(M['died:isaac']) - C.year(M['age:joseph:17'])))
print('DAYS LITERAL: %r' % {k: v[0] for k, v in DAYS.items()})
print('Methuselah: died %s, the flood %s: %d days before, same year %s' % (D(M['died:methuselah']), D(M['flood']), M['flood'] - M['died:methuselah'], C.year(M['died:methuselah']) == C.year(M['flood'])))
print('Sarah (17:17: born in Abraham\'s year + 10; 23:1: 127): death year %d; the purchase\'s bound years [%d, %d] (since O8 S3: from 22:4, the binding in her death year)' % (C.year(M['born:abraham']) + 10 + 127, C.year(M['moriah_seen']), C.year(M['age:isaac:40'])))

# ---- 7. THE CENSUS ----
print('\nCENSUS')
tot = collections.Counter()
for r in SPAN_ORDER:
    c = per.get(r)
    if not c: continue
    print('  %-16s scanned %3d  history %3d  case %3d  source-off %d  register-off %d' % (r, c['scanned'], c['history'], c['case'], c['source'], c['register']))
    for k in ('scanned', 'history', 'case', 'source', 'register'): tot[k] += c[k]
print('  TOTAL scanned %d; history %d (before dedup) -> %d on the tape; case %d; source-off %d; register-off %d; unregistered %d; deduped %d; re-based fields %d; closes %d' % (
    tot['scanned'], tot['history'], len(hist), tot['case'], tot['source'], tot['register'], len(off['unregistered']), len(dups), len(rebased), len(closes)))
print('  register-off:'); [print('    ', x) for x in off['register']]
print('  source-off:'); [print('    ', x) for x in off['source']]
print('  deduped:'); [print('    ', x) for x in dups]
print('  re-based:'); [print('    ', x) for x in rebased]
kinds = sorted(set(h['event']['kind'] for h in hist))
subjects = sorted(set(h['event']['subject'] for h in hist))
print('  kinds on the tape %d; subjects %d' % (len(kinds), len(subjects)))
CENSUS = (tot['scanned'], tot['history'], len(hist), tot['case'], tot['source'], tot['register'], len(dups), len(rebased), len(closes), len(MK),
          sum(c == 'F' for _, c, *_ in MK), sum(c == 'P' for _, c, *_ in MK), sum(c == 'R' for _, c, *_ in MK), len(kinds), len(subjects))
print('  CENSUS tuple (scanned, history, on tape, case, source-off, register-off, deduped, re-based, closes, markers, F, P, R, kinds, subjects): %r' % (CENSUS,))

# ---- 8. the registry's tape lines ----
reg_path = os.path.join(HERE, 'event_vocabulary.yaml')
txt = open(reg_path, encoding='utf-8').read()
SUFFIX = '; re-submitted on the sequential tape by cold_run_sequence.py'
n_add = 0
for k in kinds:
    m = re.search(r'(^  %s:\n(?:(?!^  \S).*\n)*?^    tape: ")([^"\n]*)("\n)' % re.escape(k), txt, re.M)
    if not m:
        print('  registry: no tape line found for %s' % k); continue
    line = m.group(2)
    if SUFFIX in line: continue
    if '; consumed by' in line:
        new = line.replace('; consumed by', SUFFIX + '; consumed by', 1)
    else:
        new = line + SUFFIX
    txt = txt[:m.start(2)] + new + txt[m.end(2):]; n_add += 1
open(reg_path, 'w', encoding='utf-8').write(txt)
print('  registry tape lines appended: %d (of %d kinds)' % (n_add, len(kinds)))
