import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 6b — THE COMPILE OF CHUKAT (2026-09-11; the owner: "Go" after the #128 rereads): THE MEASUREMENTS, computed
# BEFORE the design paragraph is typed (1b's order). (1) the parser's state at the portion's seats (19:1-21:35) after 5b's rules — every
# numeral verse, numbers AND ordinals (the date-ordinals decided at the design); (2) THE DUAL "TWICE" censused on the whole Tanakh DB — every
# token whose consonants are פעמים ("times" / "twice"), its points, its morph, the parser's current reading; the singular פעם beside it;
# (3) the calendar — the exodus era's days for the fortieth year's dates (Seder Olam 9-10 read on the shelf: Miriam the first / the tenth of
# Nisan, three months at Kadesh, Aaron the first of Av, thirty days, the retreat to Moserah), the decree's due, the counter after Korach, the
# daughters' marker; (4) the callees on file (the leper's kit, the Day's finger, the sin-bull's carcass, the Passover's hyssop, the sotah's
# dust, the camps' corpse-unclean, the Levites' sprinkling, the vestments' office, the priesthood's family, the blasphemer's human soul, the
# sanctions' karet, the Lev 5 me'ilah, Shelach's turn-back / Hormah / due, Korach's staff); (5) the tape's subjects and the registry rows;
# (6) the register verses of 19-21 against the planned lines; (7) the kinds and effects on file for the names the design will use.
import sqlite3, sys, io, re, contextlib, collections, inspect, os
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import world_engine as WE
    import cold_run_metzora as MZ
    import cold_run_yoma as YM
    import cold_run_chatat as CH
    import cold_run_pesach as PS
    import cold_run_naso as NS
    import cold_run_beha as BH
    import cold_run_vestments as VS
    import cold_run_priesthood as PR
    import cold_run_lev24 as L24
    import cold_run_sanctions as SA
    import cold_run_vayikra5 as V5
    import cold_run_shelach as SH
    import cold_run_korach as KR
    import cold_run_clocks as CL
    import cold_run_zelophehad as ZL
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by = {}
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((plain(he), pointed(he), m))
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
NUMY = r'(אחד|אחת|שנים|שתים|שני|שתי|שלש|ארבע|חמש|שש|שבע|שמנ|תשע|עשר|מאה|מאת|אלף|רבע|רביע|שליש|חצי|עשרן|עשרון|עשירי|מאתים|ראשון|שלישי|שביעי|רביעי|חמישי|ששי|שמיני|תשיעי|פעמים|פעם)'
print('==== (1) THE PARSER AT THE PORTION\'S SEATS (19:1-21:35) — every numeral verse, numbers and ordinals ====')
for c, lo, hi in ((19, 1, 22), (20, 1, 29), (21, 1, 35)):
    for v in range(lo, hi + 1):
        ws = [x for x, _, _ in by[('Num', c, v)]]
        n, o = N('Num', c, v), O('Num', c, v)
        numy = [(x, xp) for x, xp, _ in by[('Num', c, v)] if re.search(NUMY, x)]
        if n or o or numy:
            print('  Num %d:%d  numbers %s  ordinals %s   tokens %s' % (c, v, n, o, ' '.join('%s[%s]' % t for t in numy)))
print('-- the retellings and the date seats:')
for ref in (('Num', 33, 38), ('Num', 33, 39), ('Deut', 2, 14), ('Deut', 34, 8), ('Deut', 3, 11), ('Num', 31, 19), ('Exod', 40, 17), ('Num', 1, 1), ('Num', 9, 1), ('Num', 10, 11), ('Num', 7, 12), ('Num', 7, 18), ('Deut', 1, 3), ('Num', 20, 1), ('Num', 19, 12), ('Num', 19, 19), ('Gen', 22, 4), ('Exod', 19, 11), ('Exod', 19, 16), ('Lev', 7, 17), ('Num', 29, 12), ('Num', 29, 32)):
    print('  %s %d:%d  numbers %s  ordinals %s   tokens %s' % (ref[0], ref[1], ref[2], N(*ref), O(*ref), ' '.join('%s[%s]' % (x, xp) for x, xp, _ in by[ref] if re.search(NUMY, x))))

print('\n==== (2) THE DUAL "TWICE" — the whole Tanakh DB: every token whose consonants are פעמים, and the singular פעם with a numeral before it ====')
def bare_pre(x):
    for pre in ('וב', 'וכ', 'ול', 'ו', 'ב', 'ל', 'כ', 'ה'):
        if x.startswith(pre): return x[len(pre):], pre
    return x, ''
SHEVA, PATACH, QAMATS, CHIRIQ, TSERE, CHOLAM, HATAF_PATACH = 'ְ', 'ַ', 'ָ', 'ִ', 'ֵ', 'ֹ', 'ֲ'
def marks_after(pt, letter_index):
    """the points on the n-th consonant of a pointed token"""
    cons = [i for i, ch in enumerate(pt) if 'א' <= ch <= 'ת']
    if letter_index >= len(cons): return ''
    s = cons[letter_index] + 1
    e = cons[letter_index + 1] if letter_index + 1 < len(cons) else len(pt)
    return ''.join(ch for ch in pt[s:e] if not ('א' <= ch <= 'ת'))
cnt = collections.Counter()
for (b, c, v), ws in by.items():
    for i, (x, xp, m) in enumerate(ws):
        st, pre = bare_pre(x)
        if st == 'פעמים':
            pe = [j for j, ch in enumerate(xp) if ch == 'פ'][0]
            # the consonant index of פ in the pointed form
            cons = [ch for ch in xp if 'א' <= ch <= 'ת']
            k = cons.index('פ')
            mk = marks_after(xp, k)
            cls = 'DUAL-twice(patach)' if PATACH in mk else ('PLURAL-times(sheva)' if SHEVA in mk else 'OTHER(%r)' % mk)
            cnt[cls] += 1
            prev = ws[i - 1][0] if i else ''
            print('  %-5s %3d:%-3d  %-14s pre %-3s  %-22s morph %-10s prev %-10s parse %s' % (b, c, v, xp, pre or '-', cls, m, prev, N(b, c, v) if b in T else '-'))
print('  classes:', dict(cnt))
print('-- the singular פעם after a numeral word (Torah):')
for (b, c, v), ws in by.items():
    if b not in T: continue
    for i, (x, xp, m) in enumerate(ws):
        st, pre = bare_pre(x)
        if st == 'פעם' and i and re.search(NUMY, ws[i - 1][0]):
            print('  %s %d:%d  %s %s  parse %s' % (b, c, v, ws[i - 1][1], xp, N(b, c, v)))

print('\n==== (3) THE CALENDAR — the fortieth year on the exodus era ====')
w = WE.World(era='measure', epoch='exodus')
ex = w.clock.eras['exodus']
for y, m, d, why in ((40, 1, 1, 'Miriam — Seder Olam 9:2 "the first of Nisan" (the well)'), (40, 1, 10, 'Miriam — Seder Olam 10:2 "the tenth of Nisan"'), (40, 1, 14, 'the Passover of the fortieth year'), (40, 4, 1, 'three months at Kadesh (Seder Olam 9:2) — the departure toward Hor'), (40, 5, 1, "Aaron's death — Num 33:38"), (40, 5, 9, "the decree's due (CF3)"), (40, 5, 15, 'the fifteenth of Av — the dying ceased (Bava Batra 121a)'), (40, 6, 1, 'the thirty days of mourning ended (20:29)'), (40, 11, 1, 'Deut 1:3 — Moses spoke')):
    dd = w.clock.day_in('exodus', y, m, d)
    print('  (%d, %d, %d) = day %d  %s   [date back: %s]' % (y, m, d, dd, why, ex.date(dd)))
d51, d61 = w.clock.day_in('exodus', 40, 5, 1), w.clock.day_in('exodus', 40, 6, 1)
print('  Av of the fortieth year: (40, 6, 1) - (40, 5, 1) = %d days; (40, 5, 1) + 30 = %s' % (d61 - d51, ex.date(d51 + 30)))
print('  the return marker (2, 5, 9) = day %d; + 38 years by the Calendar = %s (CF3\'s due %s)' % (w.clock.day_in('exodus', 2, 5, 9), ex.date(w.clock.calendar.add(w.clock.day_in('exodus', 2, 5, 9), 38, 'year')), ex.date(SH.DUE_38)))
print('  Shelach DATA deaths_ceased:', SH.DATA['deaths_ceased']['value'], '| the decree due cell:', SH.decree({'ask': 'due'}, SH.DATA)[0])
print('  the tape after Korach: the daughters\' marker at Num 27:1 = (40, 5, 1) reading-placed (the sequence runner line):')
src = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
for ln in src.split('\n'):
    if "w.marker('Num 27:1'" in ln: print('    ', ln.strip()[:600])
print('  the pending timer on the tape at 5b\'s close: carcasses_fall_in_the_wilderness due (40, 5, 9) — CF3 PENDING (the state doc #126)')

print('\n==== (4) THE CALLEES ON FILE ====')
def asks(mod, pat=r"(?:q|ask) == '([a-z_0-9]+)'"):
    s = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    return sorted(set(re.findall(pat, s)))
def defs(mod):
    s = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    return re.findall(r'^def ([a-z_0-9]+)\(', s, re.M)
for name, mod in (('metzora', MZ), ('yoma', YM), ('chatat', CH), ('pesach', PS), ('naso', NS), ('beha', BH), ('vestments', VS), ('priesthood', PR), ('lev24', L24), ('sanctions', SA), ('vayikra5', V5), ('shelach', SH), ('korach', KR), ('clocks', CL), ('zelophehad', ZL)):
    print('  %-11s defs %s' % (name, defs(mod)[:40]))
    a = asks(mod)
    print('  %-11s asks (%d) %s' % ('', len(a), a[:90]))
def tryc(label, f):
    try:
        r = f(); print('  ', label, '->', (r['v'] if isinstance(r, dict) and 'v' in r else (r[0] if isinstance(r, tuple) else r)) if not isinstance(r, str) else r)
    except Exception as e:
        print('  ', label, 'raised', type(e).__name__, str(e)[:160])
tryc('metzora.birds(kit)', lambda: MZ.birds('kit'))
tryc('metzora.birds(living_water)', lambda: MZ.birds('living_water'))
tryc('metzora.birds(vessel)', lambda: MZ.birds('vessel'))
tryc('metzora.birds(sprinkle)', lambda: MZ.birds('sprinkle'))
tryc('chatat.carcass(anointed)', lambda: CH.carcass('anointed'))
tryc('chatat.burn_site(carcass)', lambda: CH.burn_site('carcass'))
tryc('chatat.burn_site(place)', lambda: CH.burn_site('place'))
tryc('chatat.sprinklings(anointed)', lambda: CH.sprinklings('anointed'))
tryc('chatat.blood(anointed)', lambda: CH.blood('anointed'))
tryc('yoma.service_order()', lambda: YM.service_order())
tryc('pesach.paschal_procedure(hyssop)', lambda: PS.paschal_procedure({'ask': 'hyssop'}, PS.DATA if hasattr(PS, 'DATA') else {}))
tryc('pesach.paschal_procedure(blood_application)', lambda: PS.paschal_procedure({'ask': 'blood_application'}, PS.DATA if hasattr(PS, 'DATA') else {}))
tryc('naso.camp_purity(who_sent corpse_unclean)', lambda: NS.camp_purity({'ask': 'who_sent', 'who': 'corpse_unclean'}, NS.DATA))
tryc('naso.camp_purity(camps)', lambda: NS.camp_purity({'ask': 'camps'}, NS.DATA))
tryc('naso.camp_purity(warning)', lambda: NS.camp_purity({'ask': 'warning'}, NS.DATA))
tryc('naso DATA dust_order', lambda: NS.DATA['dust_order']['value'])
tryc('beha.levites_rite(purification)', lambda: BH.levites_rite({'ask': 'purification'}, BH.DATA))
tryc('vestments.office(eight)', lambda: VS.office('eight'))
tryc('priesthood.family(one_hour)', lambda: PR.family('one_hour'))
tryc('priesthood.family(greatness)', lambda: PR.family('greatness'))
tryc('priesthood.family(high_priest_dead)', lambda: PR.family('high_priest_dead'))
tryc('priesthood.family(onen)', lambda: PR.family('onen'))
tryc('lev24.talion(eye)', lambda: L24.talion('eye'))
tryc('sanctions.grade(ervah)', lambda: SA.grade('ervah'))
tryc('vayikra5.sacrilege(meilah)', lambda: V5.sacrilege({'kind': 'meilah', 'unwitting': True, 'benefit': True, 'damage': True, 'value': 4}, V5.DATA))
tryc('shelach.decree(turn_back)', lambda: SH.decree({'ask': 'turn_back'}, SH.DATA))
tryc('shelach.decree(hormah)', lambda: SH.decree({'ask': 'hormah'}, SH.DATA))
tryc('shelach.decree(due)', lambda: SH.decree({'ask': 'due'}, SH.DATA))
tryc('korach DATA staff_hidden_with', lambda: KR.DATA['staff_hidden_with']['value'])
tryc('clocks.touch(zav, direct)', lambda: CL.touch('zav', 'direct'))
tryc('sanctions karet census', lambda: SA.c_karet)
print('  vestments source: 29:29-30 named?', '29:29' in open(inspect.getsourcefile(VS), encoding='utf-8').read(), '| priesthood source 29:29:', '29:29' in open(inspect.getsourcefile(PR), encoding='utf-8').read())
print('  effects_layer NONE:', __import__('effects_layer').NONE)

print('\n==== (5) THE TAPE\'S SUBJECTS AND THE REGISTRY ROWS ====')
for s in ('miriam', 'aaron', 'eleazar', 'moses', 'israel', 'the-tabernacle', 'the-priesthood', 'edom', 'the-king-of-edom', 'arad', 'the-king-of-arad', 'the-canaanite', 'sihon', 'og', 'the-amorite', 'the-copper-serpent', 'the-serpents', 'the-well', 'moab', 'ammon', 'the-rock', 'kadesh', 'mount-hor', 'hormah', 'esau', 'jazer', 'bashan', 'the-staff', 'aarons-staff', 'the-cloud', 'the-daughters-of-zelophehad'):
    print('  %-28s subject lines %2d   as a token %3d' % (s, src.count("'subject': '%s'" % s), src.count("'%s'" % s)))
for ln in src.split('\n'):
    if ('Num 19' in ln or 'Num 20' in ln or 'Num 21' in ln) and 'w.submit' in ln: print('  A LINE AT 19-21 ALREADY:', ln.strip()[:300])
import yaml
reg = yaml.safe_load(open(f'{ROOT}/logic/corpus/entity_registry.yaml', encoding='utf-8'))
ids = {e['id']: e for e in reg['entities']}
for eid in ('miriam', 'miryam', 'aaron', 'eleazar_son_of_aaron', 'moses', 'israel_people', 'the_tent_of_meeting', 'the_priesthood', 'esau', 'the_kings_of_edom', 'edom', 'moab', 'ben_ammi', 'the_amorite', 'the_serpent', 'the_rock', 'the_staff', 'hormah', 'arad', 'sihon', 'og', 'the_copper_serpent', 'the_well', 'kadesh', 'mount_hor', 'the_cloud', 'the_daughters_of_zelophehad', 'the_canaanite', 'amalek', 'amaleq'):
    e = ids.get(eid)
    print('  %-28s %s' % (eid, ('kind %s; members %s' % (e.get('kind'), [m.get('token') for m in e.get('members', [])])) if e else 'NO ROW'))

print('\n==== (6) THE REGISTER OF CHAPTERS 19-21 (V.w) against the planned lines ====')
reg2 = {}
for (b, c, v), ws in by.items():
    if b == 'Num' and c in (19, 20, 21):
        reg2[(c, v)] = [x for x, _, m in ws if m and m.startswith('V.w')]
LINES = [('heifer_statute_given', 19, 1, 22),
         ('miriam_died_at_kadesh', 20, 1, 1), ('congregation_strove_for_water', 20, 2, 5), ('moses_and_aaron_fell_and_the_glory', 20, 6, 6), ('rock_commanded', 20, 7, 8),
         ('staff_taken_from_before_the_lord', 20, 9, 9), ('rock_struck_twice', 20, 10, 11), ('sentence_at_meribah', 20, 12, 13), ('messengers_sent_to_edom', 20, 14, 17),
         ('edom_refused', 20, 18, 18), ('israel_pleaded_the_highway', 20, 19, 19), ('edom_came_out_against', 20, 20, 21), ('journeyed_to_mount_hor', 20, 22, 22),
         ('aarons_gathering_decreed', 20, 23, 24), ('aaron_brought_up_mount_hor', 20, 25, 27), ('garments_transferred_and_aaron_died', 20, 28, 28), ('aaron_mourned_thirty_days', 20, 29, 29),
         ('arad_fought_and_took_captives', 21, 1, 1), ('israel_vowed_the_cherem', 21, 2, 2), ('canaanites_devoted_hormah_named', 21, 3, 3), ('journeyed_by_the_red_sea_way', 21, 4, 4),
         ('people_spoke_against_god_and_moses', 21, 5, 5), ('fiery_serpents_sent', 21, 6, 6), ('people_confessed_and_moses_prayed', 21, 7, 7), ('pole_commanded', 21, 8, 8),
         ('copper_serpent_made', 21, 9, 9), ('journeyed_oboth_to_arnon', 21, 10, 13), ('book_of_the_wars_cited', 21, 14, 15), ('well_given_at_beer', 21, 16, 18),
         ('journeyed_to_pisgah', 21, 19, 20), ('messengers_sent_to_sihon', 21, 21, 22), ('sihon_came_out_and_fought', 21, 23, 23), ('sihon_smitten_land_possessed', 21, 24, 25),
         ('heshbon_and_the_parable', 21, 26, 30), ('israel_dwelt_and_jazer_taken', 21, 31, 32), ('og_came_out_and_fear_not', 21, 33, 34), ('og_smitten', 21, 35, 35)]
regv = sorted(k for k, vv in reg2.items() if vv)
print('  register verses: ch19 %d, ch20 %d, ch21 %d, total %d' % (tuple(sum(1 for c, v in regv if c == k) for k in (19, 20, 21)) + (len(regv),)))
for name, c, lo, hi in LINES:
    vv = [(v, reg2[(c, v)]) for v in range(lo, hi + 1) if reg2[(c, v)]]
    print('  %-38s %d:%d-%d  register verses %d  %s' % (name, c, lo, hi, len(vv), ' '.join('%d:%s' % (v, ','.join(x)) for v, x in vv)[:150]))
covered = {(c, v) for _, c, lo, hi in LINES for v in range(lo, hi + 1)}
print('  every verse of 19-21 in a line:', covered == {(c, v) for c, n in ((19, 22), (20, 29), (21, 35)) for v in range(1, n + 1)}, '; uncovered register verses:', [k for k in regv if k not in covered], '; lines', len(LINES))
FR = [(c, v) for (b, c, v), ws in by.items() if b == 'Num' and c in (19, 20, 21) and len(ws) > 2 and ws[0][0] in ('וידבר', 'ויאמר') and ws[1][0] == 'יהוה']
print('  the frames:', sorted(FR))

print('\n==== (7) THE KINDS AND EFFECTS ON FILE — the names the design will use ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev.get('events') or ev
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx.get('effects') or fx
cand_kinds = [n for n, *_ in LINES] + ['heifer_case', 'corpse_tumah_case', 'parah_case', 'oholot_case', 'meribah_case', 'edom_case', 'succession_case', 'serpent_case', 'conquest_case', 'well_case', 'arad_case', 'sprinkling_case', 'vessel_case', 'chukat_case']
print('  kinds already on file among the candidates:', [k for k in cand_kinds if k in E])
cand_fx = ['died', 'buried', 'mourned', 'mourning_owed', 'gathered_to_his_people', 'put_to_death', 'journeyed', 'journey_halted', 'commanded', 'plea_made', 'glory_appeared', 'gathered_against', 'strove', 'tested_the_lord', 'refused', 'blocked', 'passage_refused',
           'sentence_pronounced', 'barred', 'not_to_enter', 'invested_office', 'in_force', 'office_ended', 'vow_made', 'vowed', 'devoted', 'cherem', 'plague_struck', 'atoned_forgiven', 'prayed', 'prayer_accepted', 'sign_set', 'possessed', 'smitten', 'captives_taken', 'sang', 'well_given',
           'sent_outside_the_camp', 'impure_until_evening', 'impure_seven_days', 'corpse_unclean', 'sprinkled', 'sprinkled_seven', 'karet_cut_off', 'clean', 'purified', 'ashes_kept', 'omer_kept', 'kept_for_a_sign', 'rule_installed', 'declaration_owed', 'accepted', 'disqualified', 'exempt', 'valid', 'invalid', 'unclean', 'pure',
           'named', 'place_named', 'land_possessed', 'dwelt', 'fear_not', 'assured', 'confessed', 'bitten', 'healed', 'looked_and_lived', 'made', 'object_made', 'sanctified', 'not_sanctified', 'water_given', 'waters_of_strife', 'stricken', 'struck', 'took', 'hardened', 'defeated', 'destroyed', 'city_taken', 'captured', 'settled', 'burned', 'burned_in_fire', 'washed', 'bathed', 'toucher_unclean', 'sprinkler_unclean', 'tent_unclean', 'vessel_unclean', 'vessel_clean', 'redeemed', 'pays', 'fine', 'liable', 'flogged', 'death_by_heaven', 'consumed', 'ate', 'water_lacking', 'pillar_departed', 'cloud_departed', 'departed', 'returned']
print('  effects on file among the candidates:', [f for f in cand_fx if f in F])
print('  effects NOT on file among the candidates:', [f for f in cand_fx if f not in F])
for f in ('died', 'buried', 'mourned', 'gathered_to_his_people', 'put_to_death', 'journeyed', 'journey_halted', 'sentence_pronounced', 'invested_office', 'vow_made', 'devoted', 'plague_struck', 'prayed', 'sent_outside_the_camp', 'impure_until_evening', 'impure_seven_days', 'karet_cut_off', 'purified', 'refused', 'blocked', 'possessed', 'land_possessed', 'captives_taken', 'smitten', 'struck', 'sign_set', 'made', 'named', 'sanctified', 'tested_the_lord', 'strove', 'plea_made', 'commanded', 'confessed', 'healed', 'dwelt', 'destroyed', 'sang', 'departed', 'in_force', 'rule_installed', 'atoned_forgiven'):
    if f in F: print('   %-24s %-7s :: %s' % (f, F[f].get('ledger_op', F[f].get('class', '?')), str(F[f].get('en', ''))[:150].replace('\n', ' ')))
    elif f in E: print('   %-24s (a KIND, not an effect) form %s' % (f, E[f].get('form')))
print('  kinds on file that look like this portion\'s (journey / death / war / well / serpent / vow / edom / sihon / og / miriam / aaron / heifer / corpse / unclean):')
for k in sorted(E):
    if re.search(r'journey|died|death|war|well|serpent|vow|edom|sihon|\bog\b|miriam|aaron|heifer|corpse|unclean|mourn|sprinkl|purif|hormah|arad|struck|rock|water', k): print('    %-36s form %-7s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:110].replace('\n', ' ')))
print('  effects on file matching the same stems:')
for f in sorted(F):
    if re.search(r'journey|died|death|mourn|well|serpent|vow|devot|sprinkl|purif|unclean|impure|pure|clean|corpse|tent|vessel|ashes|possess|captiv|smit|struck|refus|block|sentence|barred|enter|office|invest|prayer|pray|heal|bite|look|sign|named|sanctif|strife|water|karet|cut_off', f): print('    %-36s %-7s %s' % (f, F[f].get('ledger_op', '?'), str(F[f].get('en', ''))[:110].replace('\n', ' ')))
