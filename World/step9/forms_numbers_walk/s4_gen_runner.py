#!/usr/bin/env python3
# O8 S4 — the generator of cold_run_joseph.py's MECHANICAL parts from the hand-model's own scene (o8_s4_scene.json) and the
# registries: the probes (every kind's witnesses in the span, the rosters' names as the verses write them), the daemon's
# branches (one `if k == ...` per watched kind, the writes the model fixed per event), the scene's submits and closes in the
# model's order, the slots. The cells and the tests are the hand's (s4_cells_A/B.py, s4_tests.py); the assembler splices them in.
import json, yaml, re, sqlite3
S = '<scratch>/'
D = '<repo-old>/World/step9/'
J = json.load(open(S + 'o8_s4_scene.json', encoding='utf-8'))
EV = yaml.safe_load(open(D + 'event_vocabulary.yaml', encoding='utf-8'))['events']
FX = yaml.safe_load(open(D + 'effect_vocabulary.yaml', encoding='utf-8'))['effects']
SCENE = J['scene']; SLOTS = [tuple(x) for x in J['slots']]; PRED = tuple(J['pred']); CLOSES = J['closes']; NOT_HERE = J['not_here']
SPAN = {32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 50}
kinds = list(dict.fromkeys(k for k, *_ in SCENE))
# ---- the probes: every kind's witnesses inside the span, plus the rosters' names ----
probes = []
for k in kinds:
    for w in EV[k]['witness']:
        m = re.match(r'Gen (\d+):(\d+) \| (.+)$', w)
        if m and int(m.group(1)) in SPAN: probes.append((int(m.group(1)), int(m.group(2)), m.group(3)))
# the rosters: the seventy by register (46:8-25; the verse's own spelling where the roster's differs), the twelve (35:23-26), the eight kings (36:32-39)
ROSTERS = {
    'leah': [(46, 9, 'ראובן'), (46, 9, 'חנוך'), (46, 9, 'פלוא'), (46, 9, 'חצרן|חצרון'), (46, 9, 'כרמי'), (46, 10, 'שמעון'), (46, 10, 'ימואל'), (46, 10, 'ימין'), (46, 10, 'אהד'), (46, 10, 'יכין'), (46, 10, 'צחר'), (46, 10, 'שאול'),
             (46, 11, 'לוי'), (46, 11, 'גרשון'), (46, 11, 'קהת'), (46, 11, 'מררי'), (46, 12, 'יהודה'), (46, 12, 'ער'), (46, 12, 'אונן'), (46, 12, 'שלה'), (46, 12, 'פרץ'), (46, 12, 'זרח'), (46, 12, 'חצרן|חצרון'), (46, 12, 'חמול'),
             (46, 13, 'יששכר'), (46, 13, 'תולע'), (46, 13, 'פוה'), (46, 13, 'יוב'), (46, 13, 'שמרן|שמרון'), (46, 14, 'זבלון|זבולן'), (46, 14, 'סרד'), (46, 14, 'אלון'), (46, 14, 'יחלאל'), (46, 15, 'דינה')],
    'zilpah': [(46, 16, 'גד'), (46, 16, 'צפיון'), (46, 16, 'חגי'), (46, 16, 'שוני'), (46, 16, 'אצבן'), (46, 16, 'ערי'), (46, 16, 'ארודי'), (46, 16, 'אראלי'), (46, 17, 'אשר'), (46, 17, 'ימנה'), (46, 17, 'ישוה'), (46, 17, 'ישוי'), (46, 17, 'בריעה'), (46, 17, 'שרח'), (46, 17, 'חבר'), (46, 17, 'מלכיאל')],
    'rachel': [(46, 19, 'יוסף'), (46, 19, 'בנימן'), (46, 20, 'מנשה'), (46, 20, 'אפרים'), (46, 21, 'בלע'), (46, 21, 'בכר'), (46, 21, 'אשבל'), (46, 21, 'גרא'), (46, 21, 'נעמן'), (46, 21, 'אחי'), (46, 21, 'ראש'), (46, 21, 'מפים'), (46, 21, 'חפים'), (46, 21, 'ארד')],
    'bilhah': [(46, 23, 'דן'), (46, 23, 'חשים'), (46, 24, 'נפתלי'), (46, 24, 'יחצאל'), (46, 24, 'גוני'), (46, 24, 'יצר'), (46, 24, 'שלם')],
    'twelve': [(35, 23, 'ראובן'), (35, 23, 'שמעון'), (35, 23, 'לוי'), (35, 23, 'יהודה'), (35, 23, 'יששכר'), (35, 23, 'זבלון|זבולן'), (35, 24, 'יוסף'), (35, 24, 'בנימן'), (35, 25, 'דן'), (35, 25, 'נפתלי'), (35, 26, 'גד'), (35, 26, 'אשר')],
    'kings': [(36, 32, 'בלע'), (36, 33, 'יובב'), (36, 34, 'חשם'), (36, 35, 'הדד'), (36, 36, 'שמלה'), (36, 37, 'שאול'), (36, 38, 'בעל חנן'), (36, 39, 'הדר')],
}
_db = sqlite3.connect('file:<repo-old>/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
def _toks(ch, vs):
    return [re.sub(r'[֑-ׇ/]', '', h) for (h,) in _db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Gen' AND v.chapter=? AND v.verse=? ORDER BY w.idx", (ch, vs))]
RES = {}
for reg, L in ROSTERS.items():
    out = []
    for ch, vs, name in L:   # the roster names as the verse writes them (a conjunction prefix where the ink joins them; a plene spelling where the roster's is short)
        ws = _toks(ch, vs); form = None
        for alt in name.split('|'):
            parts = alt.split()
            for cand in (parts, ['ו' + parts[0]] + parts[1:]):
                if any(ws[i:i + len(cand)] == cand for i in range(len(ws) - len(cand) + 1)): form = ' '.join(cand); break
            if form: break
        assert form, ('ROSTER NAME NOT IN VERSE', reg, ch, vs, name, ws)
        out.append((ch, vs, form))
    RES[reg] = out
    probes += [p for p in out if p not in probes]
probes = list(dict.fromkeys(probes))
# ---- the daemon's branches from the model's writes ----
by_kind = {}
for k, s, f, ws, d in SCENE:
    by_kind.setdefault(k, []).append((f.get('case_source'), s, [tuple(x) for x in ws]))
VALUE = {'name_given': "value=event.get('name')", 'begotten': "cp=subj", 'wife_taken': "cp=event.get('husband')", 'asenath_given': "cp=event.get('by')",
         'sold_into_egypt': "cp=subj, amount=event.get('price')", 'sold_to_potiphar': "cp=subj", 'bought_by_potiphar': "cp='potiphar'",
         'gift_sent_ahead': "cp='jacob', value=event.get('head_count')", 'blessing_returned': "cp='jacob'", 'field_acquired': "cp=subj, amount=event.get('price')",
         'ground_of_egypt_acquired': "cp='egypt_people', amount=event.get('price')", 'ring_given': "cp=event.get('by')", 'set_over_egypt': "cp=event.get('by')",
         'gift_presented': "cp=subj", 'wagons_given': "cp='joseph'", 'gifts_given': "cp=event.get('by')", 'three_hundred_silver': "cp=event.get('by'), amount=event.get('amount')",
         'ten_donkeys_sent': "cp=event.get('by')", 'sent_out': "cp=event.get('by')", 'holding_given': "cp=subj", 'silver_gathered_to_pharaoh': "cp='egypt_people'",
         'livestock_to_pharaoh': "cp='egypt_people'", 'seed_given': "cp=subj", 'surety_undertaken': "cp=event.get('to')",
         'souls_counted': "value={'registers': event.get('registers'), 'all': event.get('all'), 'from_the_loins': event.get('from_the_loins')}",
         'twelve_sons_listed': "value=event.get('count')", 'reigned_in_edom': "value=event.get('king') or event.get('successor')", 'bowed_seven_times': "value=event.get('times')",
         'five_hands': "value=event.get('hands')", 'years_confessed': "value=event.get('years')", 'concubine_lain_with': "value=event.get('reading')",
         'encamped_at': "value=event.get('to')", 'famine': "value=event.get('years')", 'dwelt_in_egypt': "value=event.get('years')", 'thirty_at_the_standing': "value=event.get('age')",
         'fifth_to_pharaoh': "value=event.get('statute')", 'interpretation_given': "value=event.get('days')", 'one_dream': "value=event.get('years')",
         'five_presented': "value=event.get('count')", 'ten_went_down': "value=event.get('count')", 'chiefs_by_places_listed': "value=event.get('count')",
         'horites_listed': "value=event.get('count')", 'sons_of_esau_listed': "value=event.get('count')", 'cup_found': "value=event.get('found_with')",
         'esau_approaching': "value=event.get('report')", 'mohar_offered_unbounded': "value=event.get('mohar')",
         'buried': "value=event.get('where') or event.get('by')", 'kissed_and_wept': "value='dotted'", 'hanged': "cp='pharaoh-of-joseph'", 'restored_to_the_cup': "cp='pharaoh-of-joseph'",
         'in_custody': "cp=event.get('by')", 'held_in_custody': "cp=event.get('by')", 'imprisoned': "cp=event.get('by')", 'in_the_pit': "cp=subj",
         'sacrifice_offered': "value=event.get('to')", 'libation_poured': "value=event.get('libation')", 'pillar_anointed': "value=event.get('oil')",
         'double_silver_taken': "value=event.get('silver')", 'peace_given': "cp=subj", 'comforted': "cp=subj", 'forgiven': "cp=subj"}
TIMER = {'head_lifted_up_due': "due=day + 2", 'head_lifted_off_due': "due=day + 2", 'custody_three_days': "due=day + 2",   # the third day INCLUSIVE (the tape's convention at 22:4, 31:22: 'on the third day' = the day + 2) — the model's 738 was the exclusive reading, corrected at the tape's design (8n)
         'plenty_seven_years': "due=_years(world, day, 7)", 'famine_seven_years': "due=_years(world, day, 7)", 'five_years_of_famine_left': "due=_years(world, day, 5)",
         'embalming_forty_days': "due=day + 40", 'egypt_wept_seventy': "due=day + 70", 'seven_days_mourning': "due=day + 7"}
for e in list(VALUE) + list(TIMER): assert e in FX, ('VALUE/TIMER names an unregistered effect', e)
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
BUP = [ent for k, s, f, ws, d in SCENE for ent, eff in ws if eff == 'brought_up_promised'][0]
BIC = [ent for k, s, f, ws, d in SCENE for ent, eff in ws if eff == 'burial_in_canaan_sworn'][0]
DAEMON = '''
# ---- (6) THE WRAP: the daemon over the cells — consumes the stretch's acts, writes the ledger, never emits an event ----
def _years(world, day, n):
    return world.clock.calendar.add(day, n, 'year') if world.clock.epoch else day + 365 * n

def E_(effect, subject, cp=None, value=None, due=None, amount=None):
    return {'effect': effect, 'subject': subject, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value}

def law_joseph(event, world):
    """FROM THE FORD TO THE COFFIN's daemon (the forty-third): the acts and speeches of Genesis 32-37, 39-47, 50 to the ledger.
    One branch per watched kind — the writes per event are the hand-model's own table (scratchpad o8_s4_predict.py, printed
    before this file was typed). The daemon answers ITS SPAN ONLY (convention 14 both ways): a shared kind at another seat
    is another daemon's — the family's renaming (32:29), sinew (32:33) and burial (50:12-13) are excluded by the seat, as
    are Genesis 38, 48, 49. Four closes on other engines' events, by seat (CJ7): brought_up_promised (46:4) and
    burial_in_canaan_sworn (47:31) on the family's `buried` at Gen 50:13; visitation_promised (50:24) on the exodus story's
    `believed` at Exod 4:31; bones_oath (50:25) on its `bones_taken` at Exod 13:19 — the ink's own receipts."""
    k, subj, src = event['kind'], event.get('subject'), event.get('case_source', '')
    day = event.get('day', world.clock.day)
    s = WE.seat(src)
    if k == 'buried' and subj == 'jacob' and s == ('Gen', 50):
        world.close(%r, 'brought_up_promised', 'Gen 50:13 — and his sons carried him to the land of Canaan and buried him (the family engine\\'s burial; 46:4 "I will bring you up" kept)')
        world.close(%r, 'burial_in_canaan_sworn', 'Gen 50:13 — buried in the cave of the field of Machpelah (the oath of 47:31 kept by the family engine\\'s burial)')
        return []
    if k == 'believed' and s == ('Exod', 4):
        world.close('israel_people', 'visitation_promised', 'Exod 4:31 — and the people believed, and they heard that the LORD had visited the children of Israel (50:24\\'s "God will surely visit you" received)')
        return []
    if k == 'bones_taken' and s == ('Exod', 13):
        world.close('israel_people', 'bones_oath', 'Exod 13:19 — and Moses took the bones of Joseph with him, for he had surely sworn the children of Israel (50:25\\'s oath kept)')
        return []
    if not (s is not None and s[0] == 'Gen' and s[1] in (32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 50)): return []
''' % (BUP, BIC) + '\n'.join(branches) + '''
    return []
'''
# ---- the scene ----
sc = ["def scene():", '    """THE SCENE — the stretch\'s acts on a bare world in the text\'s order (scene days; the tape carries the ink\'s markers); the events and their', '    days the hand-model\'s (scratchpad o8_s4_predict.py) — typed from its print"""', "    closes = [0]",
      "    def close(eid, eff, note, value=None):", "        closes[0] += bool(w.close(eid, eff, note, value=value))",
      "    with contextlib.redirect_stdout(io.StringIO()):",
      "        w = WE.World(era='FROM THE FORD TO THE COFFIN — Genesis 32-37, 39-47, 50 (clock unit: days; the tape\\'s own order)')",
      "        w.laws = [law_joseph, PS_.law_pre_sinai]   # the covenant\\'s own run on every male birth (Gen 17:12) — the pre-Sinai daemon beside the story\\'s, as S1 and S3"]
# the closes: after which event (by kind, subject[, case_source]) — the model's CLOSES and NOT_HERE placed at their verses
AFTER = {('the-house-of-jacob', 'foreign_gods_removal_owed'): ('gods_hidden', 'jacob'), ('jacob', 'ascent_to_bethel_owed'): ('journeyed', 'jacob:Gen 35:6'), ('jacob', 'return_promised'): ('journeyed', 'jacob:Gen 35:6'),
         ('jacob', 'altar_owed'): ('altar_erected', 'the-altar-at-bethel-again'), ('jacob', 'vow_of_bethel'): ('altar_erected', 'the-altar-at-bethel-again'), ('joseph', 'in_the_pit'): ('sold', 'the-sellers-of-joseph'),
         ('the-chief-cupbearer', 'in_custody'): ('restored', 'the-chief-cupbearer'), ('the-chief-baker', 'in_custody'): ('hanged', 'the-chief-baker'), ('simeon', 'held_in_custody'): ('peace_given', 'the-steward'),
         ('judah', 'surety_undertaken'): ('journeyed', 'the-sons:Gen 45:25'), ('the-house-of-jacob', 'goshen_promised'): ('settled', 'joseph'), ('the-sons', 'good_of_egypt_promised'): ('settled', 'joseph'),
         ('jacob', 'sustenance_promised'): ('sustained', 'joseph:Gen 47:12'), ('jacob', 'josephs_hand_on_the_eyes'): ('fell_on_the_neck', 'joseph:Gen 50:1')}
notes = {tuple(c[:2]): c[2] for c in CLOSES + NOT_HERE}
assert set(AFTER) == set(notes), (set(AFTER) ^ set(notes))
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
        sc.append("        close(%r, %r, %r)" % (eid, eff, notes[(eid, eff)])); placed.add((eid, eff))
assert placed == set(notes), (set(notes) - placed)
sc += ["    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])",
       "    open_total = sum(len(ent.open_entries()) for ent in w.entities.values())",
       "    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])",
       "    return tuple(n(eid, eff) for eid, eff in SLOTS) + (open_total, tset, fired, closes[0], w.clock.day), w",
       "SCENE, _W = scene()", "SCENE_EVENTS = %r" % [(k, s) for k, s, *_ in SCENE], "_SCENE_NAMED = [e for e in SCENE_EVENTS if e[0] == 'named']", ""]
OUT = {'PROBES': probes, 'DAEMON': DAEMON, 'SCENE_CODE': '\n'.join(sc), 'SLOTS': SLOTS, 'PRED': PRED, 'ROSTERS': RES}
json.dump(OUT, open(S + 'o8_s4_gen.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('generated: probes %d (rosters %d names), kinds %d (tables %d), scene lines %d, slots %d; closes by seat on %r / %r' % (len(probes), sum(len(v) for v in RES.values()), len(kinds), sum(1 for b in branches if 'T = {' in b), len(sc), len(SLOTS), BUP, BIC))
