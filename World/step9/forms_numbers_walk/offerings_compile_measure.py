#!/usr/bin/env python3
# THE NUMBERS WALK sitting 9b — THE COMPILE OF THE OFFERINGS CALENDAR, Numbers 28:1-29:39 (2026-09-11; the owner: "Ok go" after the #138
# rereads): THE MEASUREMENTS, computed BEFORE the design paragraph is typed (1b's order). (1) the parser at every numeral verse of 28-29 after
# 8b's rules and at the cross-check seats (the tamid Exod 29:38-42, Lev 23's dates and Shavuot's table, the libation table Num 15:4-10, the
# tenth-day seats, the fifth-verb); (2) GAP 23 measured on the whole Tanakh — a unit numeral followed by 'and' + a unit numeral, with the accent
# class on the first; (3) GAP 24 — every 'עשור' token with its points; (4) THE FIFTH-VERB and the 'armed' homograph on the five-stem; (5) the tape's
# state — the counter, the altar's tamid entries, the period timers, the markers; (6) the kinds and effects on file; (7) the callees live; (8) the
# engine's literals; (9) the register of 28-29; (10) the calendar's own tokens (besides, according to the ordinance, these you shall do).
import sqlite3, sys, io, re, contextlib, collections, inspect, os
ROOT = '<repo-old>'
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import world_engine as WE
    import cold_run_moadim as MO
    import cold_run_shelach as SH
    import cold_run_incense_shekel as IS
    import cold_run_erection as ER
    import cold_run_offerings as OFF
    import cold_run_yoma as YO
    import cold_run_calendar as CAL
    import cold_run_pesach as PS
    import cold_run_minchah as MIN
    import cold_run_chatat as CH
    import cold_run_bamidbar as BM
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
db = sqlite3.connect(f'file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by = collections.OrderedDict()
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((he, m))
def words(b, c, v): return [plain(x) for x, _ in by[(b, c, v)]]
TORAH = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
NUMY = r'(אחד|אחת|שנים|שתים|שני|שתי|שלש|שלוש|ארבע|חמש|שש|שבע|שמנ|תשע|עשר|עשור|מאה|מאת|אלף|אלפ|מאתים|ראשון|שלישי|שביעי|רביעי|חמישי|ששי|שמיני|תשיעי|עשירי|רבע|רביע|שליש|חצי|מחצית)'

print('==== (1) THE PARSER AT THE CALENDAR\'S SEATS (Num 28:1-29:39) after 8b\'s rules — every verse with a numeral token ====')
for ch, hi in ((28, 31), (29, 39)):
    for v in range(1, hi + 1):
        n, o = N('Num', ch, v), O('Num', ch, v)
        numy = [x for x in words('Num', ch, v) if re.search(NUMY, x)]
        if n or o or numy:
            print('  Num %d:%-3d numbers %-28s ordinals %-8s tokens %s' % (ch, v, [str(x) for x in n], o, ' '.join(numy)))
print('-- the cross-check seats:')
for ref in (('Exod', 29, 38), ('Exod', 29, 39), ('Exod', 29, 40), ('Exod', 29, 41), ('Exod', 29, 42), ('Lev', 23, 5), ('Lev', 23, 6), ('Lev', 23, 8), ('Lev', 23, 12), ('Lev', 23, 13), ('Lev', 23, 16), ('Lev', 23, 17), ('Lev', 23, 18), ('Lev', 23, 19), ('Lev', 23, 24), ('Lev', 23, 27), ('Lev', 23, 32), ('Lev', 23, 34), ('Lev', 23, 36), ('Lev', 23, 39), ('Num', 15, 4), ('Num', 15, 5), ('Num', 15, 6), ('Num', 15, 7), ('Num', 15, 9), ('Num', 15, 10), ('Num', 15, 11), ('Lev', 16, 29), ('Lev', 25, 9), ('Exod', 12, 3), ('Exod', 30, 10), ('Gen', 41, 34), ('Exod', 13, 18), ('Num', 7, 87), ('Num', 7, 88), ('Num', 10, 10), ('Lev', 4, 14), ('Lev', 9, 3), ('Ezra', 3, 5), ('Neh', 10, 34), ('Ezek', 45, 17), ('Ezek', 46, 4), ('Ezek', 46, 6), ('2Chr', 31, 3), ('1Chr', 23, 31)):
    b = ref[0]
    print('  %s %d:%d  numbers %s  ordinals %s   tokens %s' % (b, ref[1], ref[2], [str(x) for x in N(*ref)] if b in TORAH else '(outside the parser\'s books)', O(*ref) if b in TORAH else '-', ' '.join(x for x in words(*ref) if re.search(NUMY, x)) if ref in by else 'NO VERSE'))

print('\n==== (2) GAP 23 — A UNIT NUMERAL FOLLOWED BY "AND" + A UNIT NUMERAL, the whole Tanakh, with the accent class on the first ====')
UNIT9 = {k for k, val in CS.UNITS.items() if 1 <= val <= 9 and not re.search(r'[#^~%@|*]', k)}
PRE = ('וה', 'וב', 'ול', 'וכ', 'ו', 'ב', 'ל', 'כ', 'ה', '')
def core_unit(bare):
    for p in PRE:
        if bare.startswith(p) and bare[len(p):] in UNIT9:
            return p, bare[len(p):]
    return None, None
def accent_class(raw):
    if '־' in raw: return 'MAQQEF'
    if any(c in CS._DISJ for c in raw): return 'DISJ:' + ','.join('%04X' % ord(c) for c in raw if c in CS._DISJ)
    if any(c in CS._CONJ for c in raw): return 'CONJ:' + ','.join('%04X' % ord(c) for c in raw if c in CS._CONJ)
    return 'NONE'
seats = []
for key, ws in by.items():
    for i in range(len(ws) - 1):
        b1 = plain(ws[i][0]); b2 = plain(ws[i + 1][0])
        p1, u1 = core_unit(b1)
        if u1 is None or p1 in ('ו', 'וה', 'וב', 'ול', 'וכ'):
            continue
        if b2.startswith('ו') and not b2.startswith('וה') and b2[1:] in UNIT9:
            seats.append((key, i, b1, b2, accent_class(ws[i][0]), accent_class(ws[i + 1][0])))
print('  seats: %d' % len(seats))
for (b, c, v), i, b1, b2, a1, a2 in seats:
    par = [str(x) for x in N(b, c, v)] if b in TORAH else '-'
    print('  %-5s %3d:%-3d  %s %s   accent on the first %-12s on the second %-12s   the parser now %s   | %s' % (b, c, v, b1, b2, a1, a2, par, ' '.join(words(b, c, v))[:110]))
print('-- ONE followed by "and" + ANY numeral word (the tens, the hundreds included):')
seats1 = []
for key, ws in by.items():
    for i in range(len(ws) - 1):
        b1 = plain(ws[i][0]); b2 = plain(ws[i + 1][0])
        if b1.lstrip('ובלכה') in ('אחד', 'אחת') and b2.startswith('ו') and CS._bare(b2[1:]) is not None:
            seats1.append((key, b1, b2, accent_class(ws[i][0])))
for (b, c, v), b1, b2, a1 in seats1:
    print('  %-5s %3d:%-3d  %s %s  accent on one %-14s the parser now %s' % (b, c, v, b1, b2, a1, [str(x) for x in N(b, c, v)] if b in TORAH else '-'))

print('\n==== (3) GAP 24 — EVERY "עשור" TOKEN (the tenth-day noun, plene), the whole Tanakh, with its points ====')
for (b, c, v), ws in by.items():
    for he, m in ws:
        bare = plain(he)
        if bare.lstrip('ובלכהמ') == 'עשור':
            print('  %-5s %3d:%-3d  %s  pointed %s  morph %s  the parser now %s   | %s' % (b, c, v, bare, pointed(he), m, [str(x) for x in N(b, c, v)] if b in TORAH else '-', ' '.join(words(b, c, v))[:100]))
print('-- the defective tenth-day noun עשר with a qamats (Exod 12:3\'s form) — the four books:')
for (b, c, v), ws in by.items():
    if b not in TORAH: continue
    for he, m in ws:
        bare = plain(he)
        if bare.lstrip('ובלכהמ') == 'עשר':
            st = pointed(he)[pointed(he).rfind('ע'):]
            if 'ָ' in st[:3]:
                print('  %-5s %3d:%-3d  %s  pointed %s  morph %s  the parser now %s' % (b, c, v, bare, pointed(he), m, [str(x) for x in N(b, c, v)]))

print('\n==== (4) THE FIVE-STEM\'S HOMOGRAPHS — the fifth-verb (a hiriq under the chet) and "armed" (a qubuts under the mem), the whole Tanakh ====')
for (b, c, v), ws in by.items():
    for he, m in ws:
        bare = plain(he)
        core = bare.lstrip('ובלכהמ')
        if core in ('חמש', 'חמשים', 'חמשה', 'חמשת'):
            st = pointed(he)[pointed(he).rfind('ח'):]
            vowel_chet = ''.join('%04X' % ord(x) for x in st[1:3] if 'ְ' <= x <= 'ּ')
            mem_i = st.find('מ')
            vowel_mem = ''.join('%04X' % ord(x) for x in st[mem_i + 1:mem_i + 3] if 'ְ' <= x <= 'ּ') if mem_i >= 0 else ''
            hiriq_chet = '05B4' in vowel_chet
            qubuts_mem = '05BB' in vowel_mem
            if hiriq_chet or qubuts_mem or (m and 'V' in m.split('/')[-1][:2]):
                print('  %-5s %3d:%-3d  %s  pointed %s  morph %s  chet %s mem %s  the parser now %s   | %s' % (b, c, v, bare, pointed(he), m, vowel_chet, vowel_mem, [str(x) for x in N(b, c, v)] if b in TORAH else '-', ' '.join(words(b, c, v))[:90]))

print('\n==== (5) THE TAPE\'S STATE — the counter, the altar, the period timers, the markers (the running world) ====')
w = None
try:
    import register_census as RG
    with contextlib.redirect_stdout(io.StringIO()):
        w = RG.running_world()
    print('  the running world built by register_census.running_world()')
except Exception as e:
    print('  register_census.running_world raised %s: %s' % (type(e).__name__, str(e)[:200]))
if w is not None:
    ex = w.clock.eras['exodus']
    print('  the counter: day %d = %s (exodus era); entities %d; log lines %d' % (w.clock.day, ex.date(w.clock.day), len(w.entities), len(w.log)))
    alt = w.entities.get('the-altar')
    if alt:
        te = [e for e in alt.ledger if e['effect'] == 'tamid_owed']
        print('  the-altar: ledger %d; tamid_owed entries %d — open %s; the first %s; the last %s' % (len(alt.ledger), len(te), [e.get('open') for e in te], {k: te[0].get(k) for k in ('day', 'due', 'value', 'case_source', 'source_law')} if te else None, {k: te[-1].get(k) for k in ('day', 'due', 'value', 'case_source', 'closed_by')} if te else None))
        print('  the-altar effects: %s' % dict(collections.Counter(e['effect'] for e in alt.ledger)))
    else:
        print('  NO the-altar entity; altar-like ids: %s' % [k for k in w.entities if 'altar' in k])
    tim = getattr(w, 'timers', None)
    print('  w.timers type %s len %s' % (type(tim).__name__, len(tim) if tim is not None and hasattr(tim, '__len__') else '?'))
    if tim:
        sample = tim[0] if isinstance(tim, list) else next(iter(tim.items()))
        print('  a timer sample: %s' % (str(sample)[:300],))
        per = [t for t in (tim if isinstance(tim, list) else tim.values()) if isinstance(t, dict) and t.get('period')]
        print('  timers carrying a PERIOD: %d — %s' % (len(per), [(t.get('subject'), t.get('effect'), t.get('period'), t.get('due')) for t in per][:20]))
        pend = [t for t in (tim if isinstance(tim, list) else tim.values()) if isinstance(t, dict) and not t.get('fired') and not t.get('cancelled')]
        print('  pending timers: %d — %s' % (len(pend), [(t.get('subject'), t.get('effect'), t.get('due'), ex.date(t['due']) if t.get('due') else None) for t in pend][:30]))
    tset = [l for l in w.log if l[0] == 'TIMER-SET']; tfire = [l for l in w.log if l[0] == 'TIMER-FIRE']
    print('  TIMER-SET %d, TIMER-FIRE %d; the fires by effect: %s' % (len(tset), len(tfire), dict(collections.Counter(l[2].get('effect') for l in tfire))))
    print('  the set timers by effect: %s' % dict(collections.Counter(l[2].get('effect') for l in tset)))
    per_set = [l[2] for l in tset if l[2].get('period')]
    print('  TIMER-SET with a period: %d — %s' % (len(per_set), [(t.get('subject'), t.get('effect'), t.get('period')) for t in per_set][:20]))
    sd = [(eid, e.get('value'), e.get('due'), e.get('period')) for eid, ent in w.entities.items() for e in ent.ledger if e['effect'] == 'sanctify_day']
    print('  sanctify_day entries on the running world: %d — %s' % (len(sd), sd[:10]))
    mk = [l for l in w.log if l[0] == 'MARKER']
    print('  markers %d; the last three: %s' % (len(mk), [(l[2].get('verse'), ex.date(l[1]), l[2].get('placement')) for l in mk[-3:]]))
    isr = w.entities.get('israel_people')
    print('  israel_people effects: %s' % dict(collections.Counter(e['effect'] for e in isr.ledger).most_common(30)) if isr else '  no israel_people')
    for eid in ('the-altar', 'the-tabernacle', 'the-priesthood', 'aaron-and-sons', 'the-golden-altar', 'the-table', 'the-lampstand'):
        ent = w.entities.get(eid)
        print('  %-18s %s' % (eid, ('ledger %d, open %d' % (len(ent.ledger), sum(1 for e in ent.ledger if e.get('open')))) if ent else 'NO ENTITY'))
    print('  the clock keys: ', end='')
    for k in ('sabbath', 'passover', 'passover_1', 'passover_7', 'omer', 'atzeret', 'rosh_hashanah', 'yom_kippur', 'sukkot_1', 'shemini', 'new_moon', 'month', 'week', 'passover_sheni'):
        try:
            d = w.clock.next(k); print('%s -> %s; ' % (k, ex.date(d)), end='')
        except BaseException as e:   # the Calendar refuses an unknown key with SystemExit — a probe harness catches BaseException (the clock sitting's lesson)
            print('%s -> %s; ' % (k, type(e).__name__), end='')
    print()
    try:
        cal = getattr(w.clock, 'calendar', None) or getattr(w.clock, 'cal', None)
        print('  Clock attrs: %s' % [a for a in dir(w.clock) if not a.startswith('_')][:40])
        print('  Calendar attrs: %s' % ([a for a in dir(cal) if not a.startswith('_')][:40] if cal else 'NO calendar attr'))
        if cal:
            print('  Calendar.day_of(1, 1, 7) = %d; festivals %s' % (cal.day_of(1, 1, 7), getattr(cal, 'festivals', None)))
    except Exception as e:
        print('  Calendar probe raised %s: %s' % (type(e).__name__, e))
    # the entity that holds the tamid's debt (the erection daemon writes on the token 'the-altar', re-homed by the registry)
    holders = [(eid, [(e.get('open'), e.get('due'), e.get('day'), str(e.get('case_source', ''))[:60], e.get('closed_by')) for e in ent.ledger if e['effect'] == 'tamid_owed']) for eid, ent in w.entities.items() if any(e['effect'] == 'tamid_owed' for e in ent.ledger)]
    print('  tamid_owed holders: %s' % holders)
    for eff in ('bread_set_weekly', 'lamp_arranged', 'incense_continual', 'accepted'):
        hs = [(eid, len([e for e in ent.ledger if e['effect'] == eff]), [e.get('open') for e in ent.ledger if e['effect'] == eff][:4]) for eid, ent in w.entities.items() if any(e['effect'] == eff for e in ent.ledger)]
        print('  %s holders: %s' % (eff, hs[:8]))
    print('  the registry map for the tokens: %s' % {t: (RG.CS.registry_map().get(t) if hasattr(RG, 'CS') else None) for t in ('the-altar', 'the-tabernacle', 'the-priesthood', 'israel', 'the-court')})
    try:
        reg_map = CS.registry_map()
        print('  registry_map: %s' % {t: reg_map.get(t) for t in ('the-altar', 'the-tabernacle', 'the-priesthood', 'israel', 'the-court', 'the-golden-altar', 'the-table', 'the-lampstand', 'aaron-and-sons')})
    except Exception as e:
        print('  registry_map raised %s' % e)
    open_alt = [(eid, e['effect'], e.get('value'), e.get('due')) for eid, ent in w.entities.items() if 'altar' in eid for e in ent.ledger if e.get('open')]
    print('  open entries on altar entities: %s' % open_alt[:20])
print('-- the five-stem noun "a fifth" (a holam under the chet) — every seat:')
for (b, c, v), ws in by.items():
    for he, m in ws:
        bare = plain(he)
        if bare.lstrip('ובלכהמ') == 'חמש':
            st = pointed(he)[pointed(he).rfind('ח'):]
            if 'ֹ' in st[:3]:
                print('  %-5s %3d:%-3d  %s  pointed %s  morph %s  the parser now %s   | %s' % (b, c, v, bare, pointed(he), m, [str(x) for x in N(b, c, v)] if b in TORAH else '-', ' '.join(words(b, c, v))[:90]))

print('\n==== (6) THE KINDS AND EFFECTS ON FILE — the names the design will use ====')
import yaml
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev['events']
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx['effects']
cand_kinds = ['offerings_calendar_commanded', 'tamid_offered', 'tamid_case', 'musaf_offered', 'sabbath_offering_case', 'new_moon_case', 'holy_convocation_proclaimed', 'paschal_offered', 'omer_brought', 'two_loaves_brought', 'booths_dwelt', 'four_species_taken', 'yom_kippur_kept', 'offering_slaughtered', 'libation_brought', 'libations_case', 'water_libation_case', 'calendar_case', 'festival_offering_case', 'shofar_blown', 'offering_calendar_case']
print('  kinds on file among the candidates:', [k for k in cand_kinds if k in E])
print('  kinds NOT on file:', [k for k in cand_kinds if k not in E])
cand_fx = ['tamid_owed', 'musaf_owed', 'additional_owed', 'sanctify_day', 'rest_required', 'labor_barred', 'smoked_to_the_lord', 'accepted', 'libation_owed', 'commanded', 'atoned_forgiven', 'appearance_owed', 'due_to_priest', 'most_holy', 'counts_omer', 'dwells_in_booths', 'takes_four_species', 'karet_cut_off', 'disqualified', 'exempt', 'water_libation_owed', 'wine_libation_owed', 'sin_offering_owed', 'goat_owed', 'offering_owed', 'in_force', 'rule_installed', 'salted', 'pleasing_odor', 'burn_remainder', 'eating_window', 'shofar_sounded', 'teruah_sounded', 'wailed', 'afflicted', 'vow_owed', 'tithe_owed']
print('  effects on file among the candidates:', [f for f in cand_fx if f in F])
print('  effects NOT on file:', [f for f in cand_fx if f not in F])
for f in sorted(F):
    if re.search(r'owed$|offer|libation|tamid|sanctify|smoke|odor|goat|festival|sabbath|moon|blow|shofar|afflict', f):
        print('   %-32s %-8s %s' % (f, F[f].get('ledger_op'), str(F[f].get('en', ''))[:110].replace('\n', ' ')))
print('  kinds on file matching offer/tamid/sabbath/moon/festival/libation/case:')
for k in sorted(E):
    if re.search(r'offer|tamid|sabbath|moon|festival|libation|convocation|paschal|omer|loaves|booths|species|kippur|blow|shofar', k):
        print('    %-36s form %-7s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:100].replace('\n', ' ')))
print('  the case-form kinds of the Numbers walk (the naming precedent):', [k for k in E if E[k].get('form') == 'case' and re.search(r'census|naso|beha|shelach|korach|chukat|balak|libation|spies|heifer', k)])

print('\n==== (7) THE CALLEES ON FILE, live ====')
def tryc(label, f):
    try:
        r = f(); print('  ', label, '->', (r['v'] if isinstance(r, dict) and 'v' in r else (r[0] if isinstance(r, tuple) else r)) if not isinstance(r, str) else r)
    except Exception as e:
        print('  ', label, 'raised', type(e).__name__, str(e)[:200])
for q in ('two_lambs', 'plural_minimum', 'ordinals', 'clocks', 'measures', 'beaten_oil', 'three_log', 'pointer', 'olat_tamid', 'sabbath_overrides', 'sheet_4_4', 'sheet_shekalim_4_1', 'doubled_morning_order', 'initiations'):
    tryc('IS.tamid(%s)' % q, lambda q=q: IS.tamid(q))
tryc('SH.TABLE', lambda: {k: tuple(str(x) for x in v) for k, v in SH.TABLE.items()})
tryc('SH.LOGS', lambda: SH.LOGS); tryc('SH.RATIO', lambda: {k: str(v) for k, v in SH.RATIO.items()})
tryc('SH.MONTH_ROW / TAMID_ROW / DAILY_ROW / OMER_ROW / SUKKOT_SABBATH', lambda: ([str(x) for x in SH.MONTH_ROW], [str(x) for x in SH.TAMID_ROW], [str(x) for x in SH.DAILY_ROW], [str(x) for x in SH.OMER_ROW], SH.SUKKOT_SABBATH))
tryc('SH.libations(table)', lambda: SH.libations({'ask': 'table'}, SH.DATA))
tryc('SH.libations(table_seats)', lambda: SH.libations({'ask': 'table_seats'}, SH.DATA))
tryc('SH.libations(sukkot_sabbath)', lambda: SH.libations({'ask': 'sukkot_sabbath'}, SH.DATA))
tryc('SH.libations(takes festival_goat)', lambda: SH.libations({'ask': 'takes', 'offering': 'festival_goat'}, SH.DATA))
tryc('SH.libations(takes olah)', lambda: SH.libations({'ask': 'takes', 'offering': 'olah'}, SH.DATA))
tryc('SH DATA keys', lambda: sorted(SH.DATA))
tryc('MO.work_class(sabbath)', lambda: MO.work_class('sabbath')); tryc('MO.work_class(passover_1)', lambda: MO.work_class('passover_1')); tryc('MO.work_class(yom_kippur)', lambda: MO.work_class('yom_kippur'))
tryc('MO.passover()', lambda: {k: v['v'] for k, v in MO.passover().items()})
tryc('MO.rosh_hashanah()', lambda: {k: v['v'] for k, v in MO.rosh_hashanah().items()})
tryc('MO.yom_kippur()', lambda: {k: v['v'] for k, v in MO.yom_kippur().items()})
tryc('MO.sukkot()', lambda: {k: v['v'] for k, v in MO.sukkot().items()})
tryc('MO.shavuot_animals()', lambda: {k: v['v'] for k, v in MO.shavuot_animals().items()})
tryc('MO.two_loaves()', lambda: {k: v['v'] for k, v in MO.two_loaves().items()})
tryc('MO.omer()', lambda: {k: v['v'] for k, v in MO.omer().items()})
tryc('MO.OM keys', lambda: sorted(MO.OM) if hasattr(MO, 'OM') else 'no OM')
tryc('OFF.dispatch(olah:flock)', lambda: {k: v['v'] for k, v in OFF.dispatch('olah:flock').items()})
tryc('OFF.dispatch(olah:herd)', lambda: {k: v['v'] for k, v in OFF.dispatch('olah:herd').items()})
tryc('OFF.dispatch(outer_chatat)', lambda: {k: v['v'] for k, v in OFF.dispatch('outer_chatat').items()})
tryc('OFF.dispatch(inner_chatat_yk)', lambda: {k: v['v'] for k, v in OFF.dispatch('inner_chatat_yk').items()})
tryc('YO.route() default', lambda: YO.route()); tryc('YO.route(known_end)', lambda: YO.route(known_end=True))
tryc('YO.route(sin_class other)', lambda: YO.route(sin_class='other'))
tryc('YO.service_order()', lambda: YO.service_order())
tryc('CAL.pilgrimage(able_male)', lambda: CAL.pilgrimage({'kind': 'able_male'}, CAL.DATA)); tryc('CAL DATA keys', lambda: sorted(CAL.DATA))
tryc('PS.paschal_procedure(eating_time)', lambda: PS.paschal_procedure({'ask': 'eating_time'}, PS.DATA))
tryc('MIN.omer(source)', lambda: MIN.omer('source')); tryc('MIN.oil_grade()', lambda: MIN.oil_grade()); tryc('MIN.salt(meal_offering)', lambda: MIN.salt('meal_offering'))
tryc('CH DATA keys', lambda: sorted(CH.DATA)[:40])
tryc('BM.DATA keys', lambda: sorted(BM.DATA)[:40])
tryc('IS.sabbath(q) defs', lambda: [n for n in dir(IS) if not n.startswith('_') and callable(getattr(IS, n))][:60])
def defs(mod):
    s = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    return re.findall(r'^def ([a-z_0-9]+)\(', s, re.M)
for name, mod in (('moadim', MO), ('shelach', SH), ('incense_shekel', IS), ('erection', ER), ('offerings', OFF), ('yoma', YO), ('calendar', CAL), ('pesach', PS), ('minchah', MIN), ('chatat', CH)):
    print('  %-14s defs %s' % (name, defs(mod)[:40]))
for name, mod in (('moadim', MO), ('shelach', SH), ('incense_shekel', IS), ('erection', ER), ('offerings', OFF), ('yoma', YO), ('calendar', CAL), ('pesach', PS), ('minchah', MIN), ('chatat', CH)):
    s = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    print('  %-14s imports %s' % (name, sorted(set(re.findall(r'^\s*import (cold_run_\w+)', s, re.M)))))
# the erection daemon's tamid branch
src_er = open(inspect.getsourcefile(ER), encoding='utf-8').read()
i = src_er.find("if k == 'tamid_offered'")
print('  ER law_erection tamid branch:\n' + '\n'.join('    ' + l for l in src_er[i:i + 700].split('\n')[:8]))

print('\n==== (8) THE ENGINE\'S LITERALS ====')
print('  DAEMON_ORDER length %d, last %s' % (len(CS.DAEMON_ORDER), CS.DAEMON_ORDER[-1]))
print('  RUN %s\n  PREVIOUS_RUN %s\n  NEWEST_RUNNER %s\n  CENSUS %s\n  PLACEMENT %s\n  SLOTS %s' % (CS.RUN, CS.PREVIOUS_RUN, CS.NEWEST_RUNNER, CS.CENSUS, CS.PLACEMENT, CS.SLOTS))
print('  installation_probes I5 expects: %s' % re.findall(r'len\(real\) == (\d+)', open(f'{ROOT}/World/step9/installation_probes.py', encoding='utf-8').read()))
reg = yaml.safe_load(open(f'{ROOT}/logic/corpus/entity_registry.yaml', encoding='utf-8'))
print('  registry entities %d; the-altar / the-tabernacle rows: %s' % (len(reg['entities']), [(e['id'], e.get('kind')) for e in reg['entities'] if e['id'] in ('the_altar', 'the_olah_altar', 'the_tent_of_meeting', 'the_priesthood', 'the_altar_of_burnt_offering')]))
print('  registry ids containing altar:', [e['id'] for e in reg['entities'] if 'altar' in e['id']])
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
print('  daemons %d; the Numbers walk daemons\' installed_by: %s' % (len(dd['daemons']), {k: (v.get('given_at'), v.get('installed_by')) for k, v in dd['daemons'].items() if k in ('law_census', 'law_naso', 'law_beha', 'law_shelach', 'law_korach', 'law_chukat', 'law_balak', 'law_second_census', 'law_moadim', 'law_offerings', 'law_pesach_sheni', 'law_investiture', 'law_erection')}))
dep = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8'))
print('  spans %d; edges %d; pointers %d' % (len(dep['spans']), len(dep['edges']), len(dep['pointers'])))
print('  pointers at Num 28-29 already: %s' % [p for p in dep['pointers'] if str(p.get('verse', '')).startswith(('Num 28', 'Num 29'))])
print('  edges to/from moadim: %s' % [(e['from'], e['to'], e['disposition']) for e in dep['edges'] if 'moadim' in (e['from'], e['to'])])

print('\n==== (9) THE REGISTER OF 28-29 (V.w) and the frames ====')
for ch, hi in ((28, 31), (29, 39)):
    reg2 = {v: [plain(x) for x, m in by[('Num', ch, v)] if m and re.search(r'(^|/)V[A-Za-z]w', m)] for v in range(1, hi + 1)}
    regv = [v for v in reg2 if reg2[v]]
    print('  Num %d register verses %d: %s' % (ch, len(regv), ' '.join('%d:%s' % (v, ','.join(reg2[v])) for v in regv)))
    FR = [v for v in range(1, hi + 1) if len(words('Num', ch, v)) > 2 and words('Num', ch, v)[0] in ('וידבר', 'ויאמר') and words('Num', ch, v)[1] == 'יהוה']
    print('  Num %d frames: %s' % (ch, FR))
print('  Num 30:1 words: %s' % ' '.join(words('Num', 30, 1)))

print('\n==== (10) THE CALENDAR\'S OWN TOKENS ====')
for tok, label in (('מלבד', 'besides'), ('כמשפט', 'according to the ordinance'), ('כמשפטם', 'according to their ordinance'), ('במספרם', 'by their number'), ('התמיד', 'the continual'), ('לשבתו', 'on its Sabbath'), ('בשבתו', 'on its Sabbath'), ('בחדשו', 'in its month'), ('כאלה', 'as these'), ('אלה', 'these'), ('תמימם', 'without blemish'), ('לחטאת', 'for a sin offering'), ('חטאת', 'a sin offering'), ('ליהוה', 'to the LORD'), ('הכפרים', 'the atonements'), ('עצרת', 'assembly'), ('תרועה', 'blowing'), ('ונסכיהם', 'and their libations'), ('ונסכיה', 'and its libations'), ('בעשור', 'on the tenth'), ('לכפר', 'to atone')):
    seats = [(ch, v) for ch, hi in ((28, 31), (29, 39)) for v in range(1, hi + 1) if tok in words('Num', ch, v)]
    print('  %-10s %-30s %2d seats: %s' % (tok, label, len(seats), ' '.join('%d:%d' % s for s in seats)))
# the "besides the continual burnt offering" phrase: על עלת התמיד seats
seats = []
for ch, hi in ((28, 31), (29, 39)):
    for v in range(1, hi + 1):
        ws = words('Num', ch, v)
        for i in range(len(ws) - 2):
            if ws[i] == 'על' and ws[i + 1] == 'עלת' and ws[i + 2] == 'התמיד':
                seats.append('%d:%d' % (ch, v))
print('  "on the continual burnt offering" (על עלת התמיד): %d seats: %s' % (len(seats), ' '.join(seats)))
seats = [(ch, v) for ch, hi in ((28, 31), (29, 39)) for v in range(1, hi + 1) if 'מלבד' in words('Num', ch, v) and 'עלת' in words('Num', ch, v)]
print('  "besides the burnt offering of..." (מלבד עלת): %d seats: %s' % (len(seats), ' '.join('%d:%d' % s for s in seats)))
# Sukkot's bulls by the parser per day (29:13-34) and the sum; the goats; the rams; the lambs
bulls = []
for v in (13, 17, 20, 23, 26, 29, 32):
    n = N('Num', 29, v); bulls.append(n)
print('  Sukkot day-heads 29:13,17,20,23,26,29,32 by the parser: %s' % ([[str(x) for x in n] for n in bulls],))
print('  29:35-36 (the eighth day): %s %s' % ([str(x) for x in N('Num', 29, 35)], [str(x) for x in N('Num', 29, 36)]))
print('  28:11 (the new moon): %s; 28:19: %s; 28:27: %s; 29:2: %s; 29:8: %s' % ([str(x) for x in N('Num', 28, 11)], [str(x) for x in N('Num', 28, 19)], [str(x) for x in N('Num', 28, 27)], [str(x) for x in N('Num', 29, 2)], [str(x) for x in N('Num', 29, 8)]))
print('  Lev 23:18 (Shavuot\'s table there): %s; Lev 23:19: %s' % ([str(x) for x in N('Lev', 23, 18)], [str(x) for x in N('Lev', 23, 19)]))
print('  the words of 29:39: %s' % ' '.join(words('Num', 29, 39)))
print('  the words of 28:2: %s' % ' '.join(words('Num', 28, 2)))
print('  the words of 28:6: %s' % ' '.join(words('Num', 28, 6)))
print('  the words of 29:19: %s' % ' '.join(words('Num', 29, 19)))
print('  the words of 29:31: %s' % ' '.join(words('Num', 29, 31)))
print('  the words of 29:33: %s' % ' '.join(words('Num', 29, 33)))
