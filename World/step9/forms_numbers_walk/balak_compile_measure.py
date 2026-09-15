import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 7b — THE COMPILE OF BALAK (2026-09-11; the owner: "Go" after the #131 rereads): THE MEASUREMENTS, computed
# BEFORE the design paragraph is typed (1b's order). (1) the parser's state at the portion's seats (22:1-25:19) after 6b's rules — every
# numeral verse, numbers AND ordinals; the retellings and the cross-check seats; (2) THE PLENE "THREE" censused on the whole Tanakh DB —
# every token whose consonants carry שלוש (the vav inside "three"), its points, its morph, the parser's reading; the defective שלש beside
# it by count; (3) THE APPROXIMATION PREFIX — every Torah numeral token under the prefix כ ("about"), the parser's reading at each verse
# (Exod 32:28's "about three thousands of" the known miss); (4) the calendar — the counter after Chukat's last line, the daughters' marker,
# the undated stretch (Seder Olam 9:2's order read at 6b); (5) the callees on file (the family engine's intermarriage and Isaac's
# blessing, the pre-Sinai engine's Gen 12:3, the courts (Jethro's chiefs), the sotah's zeal, Korach's plague stayed, the erection's
# everlasting priesthood, the priesthood engine's office, the sanctions' grades, the holiness engine's bestiality, the moadim's teruah,
# the well cell of chukat, bamidbar's Simeon, the exodus story's locusts); (6) the tape's subjects and the registry rows; (7) the register
# of 22-25 against the planned lines; (8) the kinds and effects on file for the names the design will use.
import sqlite3, sys, io, re, contextlib, collections, inspect, os, unicodedata
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import world_engine as WE
    import cold_run_family as FM
    import cold_run_pre_sinai as PS
    import cold_run_exodus_story as EX
    import cold_run_naso as NS
    import cold_run_korach as KR
    import cold_run_erection as ER
    import cold_run_vestments as VS
    import cold_run_priesthood as PR
    import cold_run_sanctions as SA
    import cold_run_holiness as HO
    import cold_run_holiness_b as HB
    import cold_run_moadim as MO
    import cold_run_chukat as CK
    import cold_run_bamidbar as BM
    import cold_run_pesach as PE
    import cold_run_mekoshesh as MK
    import cold_run_lev24 as L24
    import cold_run_zelophehad as ZL
    import cold_run_shelach as SH
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return unicodedata.normalize('NFC', ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF)))
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by = {}
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((plain(he), pointed(he), m))
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
NUMY = r'(אחד|אחת|שנים|שתים|שני|שתי|שלש|שלוש|ארבע|חמש|שש|שבע|שמנ|תשע|עשר|מאה|מאת|אלף|אלפ|רבע|רביע|שליש|חצי|עשרן|עשרון|עשירי|מאתים|ראשון|שלישי|שביעי|רביעי|חמישי|ששי|שמיני|תשיעי|פעמים|פעם|רגלים)'
print('==== (1) THE PARSER AT THE PORTION\'S SEATS (22:1-25:19) — every numeral verse, numbers and ordinals ====')
for c, lo, hi in ((22, 1, 41), (23, 1, 30), (24, 1, 25), (25, 1, 19)):
    for v in range(lo, hi + 1):
        n, o = N('Num', c, v), O('Num', c, v)
        numy = [(x, xp) for x, xp, _ in by[('Num', c, v)] if re.search(NUMY, x)]
        if n or o or numy:
            print('  Num %d:%d  numbers %s  ordinals %s   tokens %s' % (c, v, n, o, ' '.join('%s[%s]' % t for t in numy)))
print('-- the retellings, the cross-check seats and the exam\'s arithmetic:')
for ref in (('Exod', 32, 28), ('Num', 17, 14), ('Num', 25, 9), ('Num', 1, 23), ('Num', 26, 14), ('Num', 31, 8), ('Num', 31, 16), ('Deut', 23, 5), ('Deut', 23, 6), ('Deut', 16, 16), ('Deut', 19, 2), ('Exod', 18, 21), ('Exod', 18, 25), ('Exod', 23, 14), ('Exod', 23, 17), ('Exod', 12, 37), ('Num', 11, 21), ('Gen', 49, 9), ('Gen', 27, 29), ('Gen', 12, 3), ('Exod', 34, 15), ('Exod', 34, 16), ('Deut', 22, 24), ('Num', 22, 28), ('Num', 22, 32), ('Num', 22, 33), ('Num', 24, 10)):
    print('  %s %d:%d  numbers %s  ordinals %s   tokens %s' % (ref[0], ref[1], ref[2], N(*ref), O(*ref), ' '.join('%s[%s]' % (x, xp) for x, xp, _ in by[ref] if re.search(NUMY, x))))

print('\n==== (2) THE PLENE "THREE" — the whole Tanakh DB: every token whose consonants carry שלוש (with the vav), its points, morph, the parser\'s reading ====')
def bare_pre(x):
    for pre in ('וב', 'וכ', 'ול', 'ומ', 'ו', 'ב', 'ל', 'כ', 'ה', 'מ'):
        if x.startswith(pre) and len(x) > len(pre) + 2: return x[len(pre):], pre
    return x, ''
cnt = collections.Counter(); plene = []; defect = collections.Counter()
for (b, c, v), ws in by.items():
    for i, (x, xp, m) in enumerate(ws):
        st, pre = bare_pre(x)
        if st.startswith('שלוש'):
            plene.append((b, c, v, x, xp, m, pre, N(b, c, v) if b in T else '-'))
            cnt['torah' if b in T else 'outside'] += 1
        elif st.startswith('שלש') and not st.startswith('שלשי'):
            defect[b in T] += 1
for b, c, v, x, xp, m, pre, n in plene:
    print('  %-5s %3d:%-3d  %-12s %-16s pre %-3s morph %-10s parse %s' % (b, c, v, x, xp, pre or '-', m, n))
print('  PLENE seats: %d in the Bible (torah %d, outside %d); DEFECTIVE שלש-tokens: torah %d, outside %d' % (len(plene), cnt['torah'], cnt['outside'], defect[True], defect[False]))
print('  the plene forms by stem:', collections.Counter(bare_pre(x)[0] for _, _, _, x, *_ in plene))

print('\n==== (3) THE APPROXIMATION PREFIX — every Torah numeral token under the prefix כ ("about"), the parser\'s reading ====')
seen = set()
for (b, c, v), ws in by.items():
    if b not in T: continue
    for i, (x, xp, m) in enumerate(ws):
        if x.startswith('כ') and len(x) > 2 and re.match(r'כ(?:ה)?' + NUMY, x) and not x.startswith('כי') and not x.startswith('כל'):
            if (b, c, v) in seen: continue
            seen.add((b, c, v))
            nxt = ws[i + 1][1] if i + 1 < len(ws) else ''
            print('  %-5s %3d:%-3d  %-14s morph %-10s next %-14s parse %s   verse-tokens %s' % (b, c, v, xp, m, nxt, N(b, c, v), ' '.join(y for y, _, _ in ws if re.search(NUMY, y))))
print('  (the two known seats: Exod 32:28 "about three thousands of men" — reads 3; Exod 12:37 "about six hundred thousand" — read below)')

print('\n==== (4) THE CALENDAR — the counter after Chukat, the undated stretch ====')
w = WE.World(era='measure', epoch='exodus')
ex = w.clock.eras['exodus']
for y, m, d, why in ((40, 6, 1, "the counter after Chukat's last line (21:35 page_order at the fourth marker); the daughters' marker (27:1)"), (40, 5, 1, "Aaron's death"), (40, 11, 1, 'Deut 1:3 — Moses spoke'), (40, 12, 7, "Moses' death (the shelf's seventh of Adar)")):
    print('  (%d, %d, %d) = day %d  %s' % (y, m, d, w.clock.day_in('exodus', y, m, d), why))
src = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
for ln in src.split('\n'):
    if "w.marker('Num 27:1'" in ln: print('    27:1 marker:', ln.strip()[:200])
    if ('Num 22' in ln or 'Num 23' in ln or 'Num 24' in ln or 'Num 25' in ln) and ('w.submit' in ln or 'w.marker' in ln): print('  A LINE AT 22-25 ALREADY:', ln.strip()[:200])
print('  the tape\'s last chukat line and the first after it (by order in the file):')
lines = src.split('\n')
for i, ln in enumerate(lines):
    if "'kind': 'og_smitten'" in ln: print('   ', i + 1, ln.strip()[:120]); print('   ', i + 2, lines[i + 1].strip()[:120]); print('   ', i + 3, lines[i + 2].strip()[:160])

print('\n==== (5) THE CALLEES ON FILE ====')
def asks(mod, pat=r"(?:q|ask) == '([a-z_0-9]+)'"):
    s = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    return sorted(set(re.findall(pat, s)))
def defs(mod):
    s = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    return re.findall(r'^def ([a-z_0-9]+)\(', s, re.M)
for name, mod in (('family', FM), ('pre_sinai', PS), ('exodus_story', EX), ('naso', NS), ('korach', KR), ('erection', ER), ('vestments', VS), ('priesthood', PR), ('sanctions', SA), ('holiness', HO), ('holiness_b', HB), ('moadim', MO), ('chukat', CK), ('bamidbar', BM), ('pesach', PE), ('mekoshesh', MK), ('lev24', L24), ('zelophehad', ZL), ('shelach', SH)):
    print('  %-13s defs %s' % (name, defs(mod)[:40]))
    a = asks(mod)
    print('  %-13s asks (%d) %s' % ('', len(a), a[:100]))
def tryc(label, f):
    try:
        r = f(); print('  ', label, '->', (r['v'] if isinstance(r, dict) and 'v' in r else (r[0] if isinstance(r, tuple) else r)) if not isinstance(r, str) else r)
    except Exception as e:
        print('  ', label, 'raised', type(e).__name__, str(e)[:200])
for name, mod in (('family', FM), ('pre_sinai', PS), ('exodus_story', EX), ('korach', KR), ('erection', ER), ('holiness', HO), ('moadim', MO), ('bamidbar', BM), ('mekoshesh', MK)):
    s = open(inspect.getsourcefile(mod), encoding='utf-8').read()
    for pat in ('34:15', '34:16', '12:3', '27:29', '49:9', '49:10', '34:25', '20:3', '18:21', '18:25', '78', '17:12', '17:13', '16:21', '40:15', '18:23', '18:18', '23:14', '23:17', '1:23', '10:5', 'stoning', 'hang'):
        if pat in s: print('    %s source names %r' % (name, pat), end=';')
    print()
tryc('sanctions.grade(ervah)', lambda: SA.grade('ervah'))
tryc('sanctions.c_karet', lambda: SA.c_karet)
tryc('priesthood.family(one_hour)', lambda: PR.family('one_hour'))
tryc('priesthood.family(greatness)', lambda: PR.family('greatness'))
tryc('chukat.well_and_kings(mattanah_reading)', lambda: CK.well_and_kings({'ask': 'mattanah_reading'}, CK.DATA))
tryc('chukat.well_and_kings(land_east)', lambda: CK.well_and_kings({'ask': 'land_east'}, CK.DATA))
tryc('chukat DATA parable_tellers', lambda: CK.DATA['parable_tellers']['value'])
tryc('korach DATA keys', lambda: sorted(KR.DATA)[:60])
tryc('naso DATA keys', lambda: sorted(NS.DATA)[:60])
tryc('bamidbar TOTAL / DATA', lambda: (getattr(BM, 'TOTAL', None), sorted(getattr(BM, 'DATA', {}))[:30]))
tryc('family DATA keys', lambda: sorted(getattr(FM, 'DATA', {}))[:80])
tryc('pre_sinai DATA keys', lambda: sorted(getattr(PS, 'DATA', {}))[:80])
tryc('exodus_story DATA keys', lambda: sorted(getattr(EX, 'DATA', {}))[:80])
tryc('holiness DATA keys', lambda: sorted(getattr(HO, 'DATA', {}))[:60])
tryc('moadim DATA keys', lambda: sorted(getattr(MO, 'DATA', {}))[:60])
tryc('erection DATA keys', lambda: sorted(getattr(ER, 'DATA', {}))[:60])
tryc('mekoshesh DATA keys', lambda: sorted(getattr(MK, 'DATA', {}))[:60])
tryc('lev24 DATA keys', lambda: sorted(getattr(L24, 'DATA', {}))[:60])
print('  effects_layer NONE:', __import__('effects_layer').NONE)

print('\n==== (6) THE TAPE\'S SUBJECTS AND THE REGISTRY ROWS ====')
for s in ('balak', 'balaam', 'the-she-ass', 'moab', 'the-moabites', 'midian', 'the-midianites', 'phinehas', 'pinchas', 'zimri', 'cozbi', 'israel', 'moses', 'eleazar', 'the-angel-of-the-lord', 'the-angel', 'the-plague', 'the-elders-of-midian', 'the-judges', 'amalek', 'the-kenite', 'edom', 'the-tabernacle', 'the-daughters-of-zelophehad'):
    print('  %-28s subject lines %2d   as a token %3d' % (s, src.count("'subject': '%s'" % s), src.count("'%s'" % s)))
import yaml
reg = yaml.safe_load(open(f'{ROOT}/logic/corpus/entity_registry.yaml', encoding='utf-8'))
ids = {e['id']: e for e in reg['entities']}
for eid in ('balak', 'balaam', 'bilam', 'the_she_ass', 'moab', 'the_moabites', 'midian', 'the_midianites', 'pinchas', 'phinehas', 'zimri', 'cozbi', 'zur', 'baal_peor', 'peor', 'shittim', 'the_plague', 'amalek', 'the_kenite', 'the_angel_of_the_lord', 'the_angel', 'israel_people', 'moses', 'eleazar_son_of_aaron', 'edom', 'the_tent_of_meeting', 'the_judges_of_israel', 'the_elders_of_midian', 'the_elders_of_moab', 'agag', 'asshur', 'the_kittim', 'eber', 'sihon', 'og'):
    e = ids.get(eid)
    print('  %-24s %s' % (eid, ('kind %s; members %s; en %s' % (e.get('kind'), [m.get('token') for m in e.get('members', [])], str(e.get('en', ''))[:90])) if e else 'NO ROW'))
tok_rows = [(e['id'], m.get('token')) for e in reg['entities'] for m in e.get('members', []) if m.get('token') in ('moab', 'midian', 'the-midianites', 'pinchas', 'phinehas', 'balak', 'balaam', 'zimri', 'cozbi', 'peor', 'amalek')]
print('  token rows:', tok_rows)

print('\n==== (7) THE REGISTER OF CHAPTERS 22-25 (V.w) against the planned lines ====')
reg2 = {}
for (b, c, v), ws in by.items():
    if b == 'Num' and c in (22, 23, 24, 25):
        reg2[(c, v)] = [x for x, _, m in ws if m and m.startswith('V.w')]
LINES = [('encamped_in_the_plains_of_moab', 22, 1, 1), ('moab_feared_and_loathed', 22, 2, 4), ('balak_sent_for_balaam', 22, 5, 6), ('elders_came_with_divinations', 22, 7, 8),
         ('god_came_to_balaam_first', 22, 9, 12), ('balaam_refused_the_first', 22, 13, 14), ('balak_sent_again', 22, 15, 17), ('balaam_answered_house_of_silver', 22, 18, 19),
         ('god_came_at_night_go', 22, 20, 20), ('balaam_saddled_and_went', 22, 21, 21), ('angel_stood_as_adversary', 22, 22, 22), ('ass_saw_the_angel_thrice', 22, 23, 27),
         ('mouth_of_the_ass_opened', 22, 28, 30), ('balaams_eyes_uncovered', 22, 31, 33), ('balaam_confessed_and_sent_on', 22, 34, 35), ('balak_met_balaam_at_arnon', 22, 36, 40),
         ('balaam_brought_to_bamoth_baal', 22, 41, 41), ('seven_altars_built_first', 23, 1, 2), ('god_met_balaam_first', 23, 3, 6), ('first_parable_taken_up', 23, 7, 10),
         ('balak_protested_first', 23, 11, 12), ('taken_to_pisgah_second_stand', 23, 13, 15), ('the_lord_met_balaam_second', 23, 16, 17), ('second_parable_taken_up', 23, 18, 24),
         ('balak_protested_second', 23, 25, 26), ('taken_to_peor_third_stand', 23, 27, 30), ('spirit_of_god_upon_balaam', 24, 1, 2), ('third_parable_taken_up', 24, 3, 9),
         ('balak_clapped_and_dismissed', 24, 10, 11), ('balaam_counselled_balak', 24, 12, 14), ('fourth_parable_taken_up', 24, 15, 24), ('balaam_and_balak_parted', 24, 25, 25),
         ('people_whored_and_bowed_at_shittim', 25, 1, 2), ('israel_yoked_to_baal_peor', 25, 3, 3), ('hanging_commanded', 25, 4, 4), ('judges_commanded_to_slay', 25, 5, 5),
         ('midianite_brought_near', 25, 6, 6), ('phinehas_pierced_both', 25, 7, 8), ('plague_dead_counted', 25, 9, 9), ('covenant_of_peace_given', 25, 10, 13),
         ('slain_pair_named', 25, 14, 15), ('midian_harassment_commanded', 25, 16, 18), ('after_the_plague', 25, 19, 19)]
regv = sorted(k for k, vv in reg2.items() if vv)
print('  register verses: ch22 %d, ch23 %d, ch24 %d, ch25 %d, total %d' % (tuple(sum(1 for c, v in regv if c == k) for k in (22, 23, 24, 25)) + (len(regv),)))
for name, c, lo, hi in LINES:
    vv = [(v, reg2[(c, v)]) for v in range(lo, hi + 1) if reg2[(c, v)]]
    print('  %-38s %d:%d-%d  register verses %d  %s' % (name, c, lo, hi, len(vv), ' '.join('%d:%s' % (v, ','.join(x)) for v, x in vv)[:150]))
covered = {(c, v) for _, c, lo, hi in LINES for v in range(lo, hi + 1)}
print('  every verse of 22-25 in a line:', covered == {(c, v) for c, n in ((22, 41), (23, 30), (24, 25), (25, 19)) for v in range(1, n + 1)}, '; uncovered register verses:', [k for k in regv if k not in covered], '; lines', len(LINES))
FR = [(c, v) for (b, c, v), ws in by.items() if b == 'Num' and c in (22, 23, 24, 25) and len(ws) > 2 and ws[0][0] in ('וידבר', 'ויאמר') and ws[1][0] == 'יהוה']
print('  the frames:', sorted(FR))

print('\n==== (8) THE KINDS AND EFFECTS ON FILE — the names the design will use ====')
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev.get('events') or ev
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx.get('effects') or fx
cand_kinds = [n for n, *_ in LINES] + ['balak_case', 'balaam_case', 'oracles_case', 'peor_case', 'phinehas_case', 'midian_case', 'zealot_case', 'idolatry_case', 'blessing_case']
print('  kinds already on file among the candidates:', [k for k in cand_kinds if k in E])
cand_fx = ['encamped_at', 'feared', 'loathed', 'plea_made', 'refused', 'commanded', 'blocked', 'go_not', 'word_only', 'anger_burned', 'mark_of_anger', 'adversary_set', 'struck', 'beaten', 'mouth_opened', 'mouth_appointed', 'eyes_opened', 'uncovered', 'eyes_uncovered', 'confessed', 'sinned', 'honor_owed', 'honor_revoked',
           'offered_burnt_and_sacrifices', 'sacrifice_offered', 'altars_built', 'word_put_in_mouth', 'met', 'blessed', 'blessed_by_the_lord', 'blessed_the_people', 'cursed', 'curse_turned_to_blessing', 'parable_spoken', 'spirit_rested', 'spirit_filled', 'prophet_declared', 'counsel_given', 'counsel_accepted', 'departed', 'returned',
           'whored_after', 'idolatry_begun', 'bowed_to_gods', 'ate_of_sacrifices', 'yoked_to_baal_peor', 'plague_struck', 'plague_removed', 'plague_stayed', 'hand_stayed', 'hanged', 'put_to_death', 'stoned', 'slain', 'slain_by_sword', 'slain_by_heaven', 'death_by_heaven', 'killed', 'pierced', 'zealous', 'atoned_forgiven', 'atoned', 'covenant_of_peace', 'covenant_cut', 'covenant_promised', 'covenant_upheld', 'in_force', 'rule_installed', 'declaration_owed', 'invested_office', 'everlasting_priesthood', 'priesthood_granted', 'harass_owed', 'vengeance_owed', 'debit', 'named', 'lashes', 'exempt', 'accepted', 'liable', 'karet_cut_off', 'death_decreed', 'gathered_against', 'wept', 'weeping']
print('  effects on file among the candidates:', [f for f in cand_fx if f in F])
print('  effects NOT on file among the candidates:', [f for f in cand_fx if f not in F])
for f in ('encamped_at', 'plea_made', 'refused', 'commanded', 'mark_of_anger', 'beaten', 'mouth_appointed', 'eyes_opened', 'uncovered', 'confessed', 'honor_owed', 'offered_burnt_and_sacrifices', 'sacrifice_offered', 'blessed_by_the_lord', 'blessed_the_people', 'blessing_promised', 'blessed_by_the_priest', 'spirit_rested', 'spirit_filled', 'prophet_declared', 'counsel_accepted', 'idolatry_begun', 'plague_struck', 'plague_removed', 'hand_stayed', 'hanged', 'put_to_death', 'stoned', 'slain', 'slain_by_sword', 'slain_by_heaven', 'atoned_forgiven', 'covenant_cut', 'covenant_promised', 'covenant_upheld', 'in_force', 'rule_installed', 'invested_office', 'priesthood_removed', 'karet_cut_off', 'gathered_against', 'no_plague_at_counting', 'great_sin_charged', 'sought_to_kill', 'forgiven', 'firstborn_death_decreed', 'hamor_and_shechem_slain', 'divined_blessing', 'bowed_seven_times', 'curse_taken_upon_herself', 'blessed_by_the_sword', 'defeated', 'kings_smitten', 'destroyed', 'taken_captive'):
    if f in F: print('   %-28s %-8s :: %s' % (f, F[f].get('ledger_op', F[f].get('class', '?')), str(F[f].get('en', ''))[:170].replace('\n', ' ')))
    elif f in E: print('   %-28s (a KIND, not an effect) form %s' % (f, E[f].get('form')))
print('  kinds on file that look like this portion\'s (curse / bless / angel / ass / prophe / idol / plague / zeal / spear / hang / midian / moab / balaam / balak / oracle / parable / altar / whor / bow):')
for k in sorted(E):
    if re.search(r'curs|bless|angel|ass\b|prophe|idol|plague|zeal|spear|hang|midian|moab|balaam|balak|oracle|parable|altar|whor|bow|harlot|sacrific|counsel|priesthood|covenant', k): print('    %-36s form %-7s %s' % (k, E[k].get('form'), str(E[k].get('en', ''))[:110].replace('\n', ' ')))
print('  effects on file matching the same stems:')
for f in sorted(F):
    if re.search(r'curs|bless|angel|prophe|idol|plague|zeal|spear|hang|harass|whor|bow|sacrific|counsel|priesthood|covenant|anger|wrath|honor|mouth|eye|word|refus|confess|aton|pierc|slain|kill|death|stone|judg', f): print('    %-36s %-8s %s' % (f, F[f].get('ledger_op', '?'), str(F[f].get('en', ''))[:110].replace('\n', ' ')))
