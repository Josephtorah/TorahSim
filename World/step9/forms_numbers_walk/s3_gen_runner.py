import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# O8 S3 — the generator of cold_run_mamre.py's MECHANICAL parts from the hand-model's own scene (o8_s3_scene.json) and the
# registries: the probes (every kind's witnesses in the span), the answer sheet and the shelf rows, the daemon's branches
# (one `if k == ...` per watched kind, the writes the model fixed per event), the scene's submits and closes in the model's
# order, the slots. The cells and the tests are the hand's (s3_cells_A/B.py, s3_tests.py); the generator splices them in.
import json, yaml, re
S = '<scratch>/'
D = (_ROOT + '/World/step9/')
J = json.load(open(S + 'o8_s3_scene.json', encoding='utf-8'))
EV = yaml.safe_load(open(D + 'event_vocabulary.yaml', encoding='utf-8'))['events']
FX = yaml.safe_load(open(D + 'effect_vocabulary.yaml', encoding='utf-8'))['effects']
SCENE = J['scene']; SLOTS = [tuple(x) for x in J['slots']]; PRED = tuple(J['pred']); CLOSES = J['closes']; NOT_HERE = J['not_here']
SPAN = {18, 19, 20, 22, 25, 26, 27, 28, 29, 30, 31}
kinds = list(dict.fromkeys(k for k, *_ in SCENE))
# ---- the probes: every kind's witnesses inside the span, plus the rosters' names ----
probes = []
for k in kinds:
    for w in EV[k]['witness']:
        m = re.match(r'Gen (\d+):(\d+) \| (.+)$', w)
        if m and int(m.group(1)) in SPAN: probes.append((int(m.group(1)), int(m.group(2)), m.group(3)))
ROSTERS = [(25, 13, 'נבית'), (25, 13, 'קדר'), (25, 13, 'אדבאל'), (25, 13, 'מבשם'), (25, 14, 'משמע'), (25, 14, 'דומה'), (25, 14, 'משא'), (25, 15, 'חדד'), (25, 15, 'תימא'), (25, 15, 'יטור'), (25, 15, 'נפיש'), (25, 15, 'קדמה'),
           (22, 21, 'עוץ'), (22, 21, 'בוז'), (22, 21, 'קמואל'), (22, 22, 'כשד'), (22, 22, 'חזו'), (22, 22, 'פלדש'), (22, 22, 'ידלף'), (22, 22, 'בתואל'), (22, 24, 'טבח'), (22, 24, 'גחם'), (22, 24, 'תחש'), (22, 24, 'מעכה'),
           (25, 2, 'זמרן'), (25, 2, 'יקשן'), (25, 2, 'מדן'), (25, 2, 'מדין'), (25, 2, 'ישבק'), (25, 2, 'שוח')]
import sqlite3
_db = sqlite3.connect(('file:' + _ROOT + '/Data/tanakh.sqlite?mode=ro'), uri=True)
def _toks(ch, vs):
    return [re.sub(r'[\u0591-\u05C7/]', '', h) for (h,) in _db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Gen' AND v.chapter=? AND v.verse=? ORDER BY w.idx", (ch, vs))]
_res = []
for ch, vs, name in ROSTERS:   # the roster names as the verse writes them (a conjunction prefix where the ink joins them)
    ws = _toks(ch, vs)
    form = name if name in ws else ('ו' + name if ('ו' + name) in ws else None)
    assert form, ('ROSTER NAME NOT IN VERSE', ch, vs, name, ws)
    _res.append((ch, vs, form))
probes += [p for p in _res if p not in probes]
probes = list(dict.fromkeys(probes))
# ---- the daemon's branches from the model's writes ----
by_kind = {}
for k, s, f, ws, d in SCENE:
    by_kind.setdefault(k, []).append((f.get('case_source'), s, [tuple(x) for x in ws]))
VALUE = {'name_given': "value=event.get('name')", 'righteous_count_pleaded': "value=event.get('counts')", 'twelve_princes': "value=event.get('names')", 'hundredfold_found': "value=event.get('measure')",
         'thousand_silver_covering': "value=event.get('amount')", 'wages_changed_ten_times': "value=10", 'twenty_years_served': "value=20", 'supplanted_twice': "value=event.get('times')",
         'pursued_seven_days': "value=event.get('days')", 'told_on_the_third_day': "value=event.get('ordinal')", 'place_seen_on_the_third_day': "value=event.get('ordinal')", 'vow_of_bethel': "value={'conditions': event.get('conditions'), 'commitments': event.get('commitments')}",
         'flock_removed': "value=event.get('days')", 'month_dwelt': "value=event.get('months')", 'births_told': "value=event.get('count')", 'begotten': "cp=subj", 'wife_taken': "cp=event.get('husband')",
         'maid_given': "value=event.get('maid')", 'speckled_wage_agreed': "cp='jacob'", 'seven_years_owed': "cp='laban'", 'second_seven_owed': "cp='laban'", 'night_hired_for_mandrakes': "cp='rachel'",
         'teraphim_stolen': "cp='laban'", 'livestock_rescued': "cp='laban'", 'bread_and_lentils_given': "cp='jacob'", 'led_out_of_sodom': "cp='the-two-angels'", 'taken_by_the_king': "cp='abimelech'",
         'restored_with_gifts': "cp='abimelech'", 'all_given_to_isaac': "cp='abraham'", 'gifts_given': "cp='abraham'", 'sent_out': "cp=event.get('by')", 'birthright_transferred': "cp=event.get('from')",
         'covenant_between_men': "cp=event.get('with')", 'presented_as_sister': "cp=event.get('by')", 'decree_issued': "value=event.get('decree')", 'oath_sworn': "value=event.get('by')", 'encamped_at': "value=event.get('to') or event.get('at') or 'the place'"}
TIMER = {'return_at_the_season': "due=_years(world, day, event.get('years', 1))", 'seven_years_service': "due=_years(world, day, 7)", 'second_seven_service': "due=_years(world, day, 7)", 'week_of_the_feast': "due=day + 7"}
def ecall(ent, eff):
    args = ["'%s'" % eff, ("subj" if ent == '__subj__' else "'%s'" % ent)]
    if eff in VALUE: args.append(VALUE[eff])
    if eff in TIMER: args.append(TIMER[eff])
    return 'E_(%s)' % ', '.join(args)
branches = []
for k in kinds:
    rows = by_kind[k]
    patterns = set()
    for cs, s, ws in rows:
        patterns.add(tuple(('__subj__' if ent == s else ent, eff) for ent, eff in ws))
    if len(patterns) == 1:
        pat = list(patterns)[0]
        branches.append("    if k == '%s': return [%s]" % (k, ', '.join(ecall(ent, eff) for ent, eff in pat)))
    else:
        tbl = {}
        for cs, s, ws in rows: tbl[(cs, s)] = [('__subj__' if ent == s else ent, eff) for ent, eff in ws]
        lines = ["    if k == '%s':" % k, "        T = {"]
        for (cs, s), ws in tbl.items():
            lines.append("            (%r, %r): lambda: [%s]," % (cs, s, ', '.join(ecall(ent, eff) for ent, eff in ws)))
        lines.append("        }")
        lines.append("        return T.get((src, subj), lambda: [])()   # the model's own table per (verse, subject); an unlisted pairing writes nothing")
        branches.append('\n'.join(lines))
DAEMON = '''
# ---- (6) THE WRAP: the daemon over the cells — consumes the stretch's acts, writes the ledger, never emits an event ----
def _years(world, day, n):
    return world.clock.calendar.add(day, n, 'year') if world.clock.epoch else day + 365 * n

def E_(effect, subject, cp=None, value=None, due=None):
    return {'effect': effect, 'subject': subject, 'counterparty': cp, 'amount': None, 'due': due, 'value': value}

def law_mamre(event, world):
    """FROM MAMRE TO THE HEAP's daemon (the forty-second): the acts and speeches of Genesis 18-20, 22, 25-31 to the ledger.
    One branch per watched kind — the writes per event are the hand-model's own table (scratchpad o8_s3_predict.py, printed
    before this file was typed). The daemon answers ITS SPAN ONLY (convention 14 both ways): a shared kind at another seat
    is another daemon's. One close on another engine's event: son_promised_at_the_season on the pre-Sinai engine's born isaac
    at Gen 21:2 — the ink's own fulfillment ('at the set time of which God had spoken')."""
    k, subj, src = event['kind'], event.get('subject'), event.get('case_source', '')
    day = event.get('day', world.clock.day)
    s = WE.seat(src)
    if k == 'born' and subj == 'isaac' and s == ('Gen', 21):
        world.close('sarah', 'son_promised_at_the_season', 'Gen 21:2 — and Sarah conceived and bore Abraham a son, at the set time of which God had spoken (the pre-Sinai engine\\'s birth; the promise of 18:10 kept)')
        return []
    if not (s is not None and s[0] == 'Gen' and s[1] in (18, 19, 20, 22, 25, 26, 27, 28, 29, 30, 31)): return []
''' + '\n'.join(branches) + '''
    return []
'''
# ---- the scene ----
sc = ["def scene():", '    """THE SCENE — the stretch\'s acts on a bare world in the text\'s order (scene days; the tape carries the ink\'s markers); the events and their', '    days the hand-model\'s (scratchpad o8_s3_predict.py) — typed from its print"""', "    closes = [0]",
      "    def close(eid, eff, note, value=None):", "        closes[0] += bool(w.close(eid, eff, note, value=value))",
      "    with contextlib.redirect_stdout(io.StringIO()):",
      "        w = WE.World(era='FROM MAMRE TO THE HEAP — Genesis 18-20, 22, 25-31 (clock unit: days; the tape\\'s own order)')",
      "        w.laws = [law_mamre, PS_.law_pre_sinai]   # the covenant\\'s own run on every male birth (Gen 17:12) — the pre-Sinai daemon beside the story\\'s, as S1"]
# the closes: after which event (by kind, subject, case_source) — the model's CLOSES and NOT_HERE placed at their verses
AFTER = {('sodom', 'spared_for_the_ten'): ('overturned', 'the-cities-of-the-plain'), ('sodom', 'outcry_to_be_seen'): ('overturned', 'the-cities-of-the-plain'), ('lot', 'evacuation_owed'): ('led_out', 'lot_and_his_house'),
         ('abimelech', 'return_owed'): ('restored', 'abraham'), ('abimelech', 'death_decreed_over_the_woman'): ('healed', 'the_house_of_abimelech'), ('abraham', 'offering_of_the_son_owed'): ('called_from_heaven', 'abraham'),
         ('abraham', 'tried'): ('called_from_heaven', 'abraham'), ('esau', 'hunt_owed'): ('delicacies_brought', 'esau'), ('jacob', 'flight_owed'): ('journeyed', 'jacob:Gen 28:10'), ('jacob', 'seven_years_owed'): ('wife_demanded', 'jacob'),
         ('jacob', 'wife_from_paddan_owed'): ('married', 'rachel'), ('jacob', 'second_seven_owed'): ('release_demanded', 'jacob'), ('jacob', 'with_you_promised'): ('account_given', 'jacob:Gen 31:5-13'), ('laban', 'speech_restrained'): ('charges_laid', 'laban'),
         ('abraham', 'buried_in_peace'): ('died', 'abraham'), ('hagar', 'seed_multiplied'): ('princes_counted', 'ishmael')}
notes = {tuple(c[:2]): c[2] for c in CLOSES + NOT_HERE}
placed = set()
last_day = None
for i, (k, s, f, ws, d) in enumerate(SCENE):
    if d != last_day:
        sc.append("        w.advance(%d)" % d); last_day = d
    fields = ', '.join("%r: %r" % (kk, vv) for kk, vv in f.items() if kk != 'case_source')
    sc.append("        w.submit({'kind': %r, 'subject': %r%s, 'case_source': %r})" % (k, s, (', ' + fields) if fields else '', f['case_source']))
    for (eid, eff), (ak, asub) in AFTER.items():
        sub, _, cs_req = asub.partition(':')
        if (eid, eff) in placed or ak != k or sub != s or (cs_req and f['case_source'] != cs_req): continue
        if (eid, eff) in [tuple(c[:2]) for c in CLOSES] and ak == 'called_from_heaven' and f.get('time') != 'the first': continue
        sc.append("        close(%r, %r, %r)" % (eid, eff, notes[(eid, eff)])); placed.add((eid, eff))
assert placed == set(notes), (set(notes) - placed)
sc += ["    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])",
       "    open_total = sum(len(ent.open_entries()) for ent in w.entities.values())",
       "    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])",
       "    return tuple(n(eid, eff) for eid, eff in SLOTS) + (open_total, tset, fired, closes[0], w.clock.day), w",
       "SCENE, _W = scene()", "SCENE_EVENTS = %r" % [(k, s) for k, s, *_ in SCENE], "_SCENE_NAMED = [e for e in SCENE_EVENTS if e[0] == 'named']", ""]
OUT = {'PROBES': probes, 'DAEMON': DAEMON, 'SCENE_CODE': '\n'.join(sc), 'SLOTS': SLOTS, 'PRED': PRED}
json.dump(OUT, open(S + 'o8_s3_gen.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('generated: probes %d, kinds %d (tables %d), scene lines %d, slots %d' % (len(probes), len(kinds), sum(1 for b in branches if 'T = {' in b), len(sc), len(SLOTS)))
