import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 5b — THE COMPILE OF KORACH (2026-09-10; the owner: "Go" after the #125 rereads): THE MEASUREMENTS, computed
# BEFORE the design paragraph is typed (1b's order). (1) the parser's state at the portion's seats (16:1-18:32) after 4b's rules — every
# numeral verse, not the new class only (sitting 5's lesson); (2) THE DEFINITE NUMERAL AT THE HEAD OF A COMPOUND censused on the whole
# Tanakh DB — every article-bearing numeral word with the word after it, the vav-numeral seats apart from the vav-other seats, and the
# parser's current reading at every Torah seat; the article-numeral without a conjunction after it (the homograph class — "the fifty"
# captains, "the twelve", "the fifth [rib]", "the hundred" tower); (3) the calendar — the tape's day at the portion's position (no date in the
# ink: page_order), the morrow's timer; (4) the callees on file (bamidbar.levites, incense_shekel.shekel, pesach.firstborn, temurah.devote /
# redeem / tithe, tzav.dues_machine, naso.restitution terumah_measure, holiness_b.orlah ratio, zelophehad.inheritance_order, offerings);
# (5) the tape's subjects and the Num 16 line already on it; (6) the register verses of chapters 16-17 against the planned lines; (7) the
# event kinds and effects on file for the names the design will use (a name reused is a miss).
import sqlite3, sys, io, re, contextlib, collections, inspect
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
    import world_engine as WE
    import cold_run_bamidbar as BM
    import cold_run_incense_shekel as IS
    import cold_run_pesach as PS
    import cold_run_temurah as TM
    import cold_run_tzav as TZ
    import cold_run_naso as NS
    import cold_run_holiness_b as HB
    import cold_run_zelophehad as ZL
    import cold_run_offerings as OF
    import cold_run_priesthood as PR
    import cold_run_sanctions as SA
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
NUMY = r'(אחד|אחת|שנים|שתים|שני|שתי|שלש|ארבע|חמש|שש|שבע|שמנ|תשע|עשר|מאה|מאת|אלף|רבע|רביע|שליש|חצי|עשרן|עשרון|עשירי|מאתים)'
print('==== (1) THE PARSER AT THE PORTION\'S SEATS (16:1-18:32) — every numeral verse ====')
for c, lo, hi in ((16, 1, 35), (17, 1, 28), (18, 1, 32)):
    for v in range(lo, hi + 1):
        ws = [x for x, _, _ in by[('Num', c, v)]]
        n, o = N('Num', c, v), O('Num', c, v)
        numy = [w for w in ws if re.search(NUMY, w)]
        if n or o or numy:
            print('  Num %d:%d  numbers %s  ordinals %s   tokens %s' % (c, v, n, o, ' '.join(numy)))

print('\n==== (2) THE DEFINITE NUMERAL AT THE HEAD OF A COMPOUND — the whole Tanakh DB ====')
NUMWORDS = {'אחד', 'אחת', 'שנים', 'שתים', 'שני', 'שתי', 'שלשה', 'שלש', 'שלשת', 'ארבעה', 'ארבע', 'ארבעת', 'חמשה', 'חמש', 'חמשת', 'ששה', 'שש', 'ששת', 'שבעה', 'שבע', 'שבעת',
            'שמנה', 'שמנת', 'תשעה', 'תשע', 'תשעת', 'עשרה', 'עשר', 'עשרת', 'עשרים', 'שלשים', 'ארבעים', 'חמשים', 'ששים', 'שבעים', 'שמנים', 'תשעים', 'מאה', 'מאת', 'מאתים', 'מאות', 'אלף', 'אלפים', 'עשתי'}
def bare_num(x):
    for pre in ('ו', 'ב', 'ל', 'כ', 'מ'):
        if x.startswith(pre) and x[1:] in NUMWORDS: return x[1:]
    return x if x in NUMWORDS else None
art = collections.defaultdict(list)     # (article-numeral, next-class) -> seats
for (b, c, v), ws in by.items():
    for i, (x, xp, m) in enumerate(ws):
        if x.startswith('ה') and x[1:] in NUMWORDS and not x.startswith('וה'):
            nxt = ws[i + 1][0] if i + 1 < len(ws) else ''
            cls = 'vav-NUMERAL' if nxt.startswith('ו') and bare_num(nxt) else ('vav-other' if nxt.startswith('ו') else 'no-vav')
            art[cls].append((b, c, v, i, xp, m, ws[i - 1][0] if i else '', nxt, ws[i + 1][1] if i + 1 < len(ws) else ''))
for cls in ('vav-NUMERAL', 'vav-other', 'no-vav'):
    S = art[cls]
    print('\n-- article-numeral followed by %s: %d tokens (Torah %d)' % (cls, len(S), sum(1 for s in S if s[0] in T)))
    show = S if cls != 'no-vav' else [s for s in S if s[0] in T][:60]
    for b, c, v, i, xp, m, prev, nxt, nxtp in show:
        print('     %s %d:%d  [%s] %s [%s %s] morph %s  parse %s' % (b, c, v, prev, xp, nxt, nxtp, m, N(b, c, v) if b in T else '-'))
    if cls == 'no-vav':
        cnt = collections.Counter(s[4] for s in S if s[0] in T)
        print('     Torah forms:', cnt.most_common())
print('\n-- the 3:46 chain (the article on each part) and 16:35 side by side:')
for ref in (('Num', 3, 46), ('Num', 16, 35), ('Num', 16, 2), ('Num', 16, 17), ('Num', 31, 28), ('Num', 31, 30)):
    print('     %s %d:%d  parse %s   words %s' % (ref[0], ref[1], ref[2], N(*ref), ' '.join(w for w in CS.verse_words(*ref) if re.search(NUMY, w))))
print('-- the engine\'s article rule in the INK block:')
src = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read()
for ln in src.split('\n'):
    if 'THE ARTICLE ON A NUMERAL' in ln or "'and the N' counts only INSIDE" in ln:
        print('     ', ln.strip()[:200])

print('\n==== (3) THE CALENDAR — the tape\'s day at the portion\'s position ====')
w = WE.World(era='measure', epoch='exodus')
ex = w.clock.eras['exodus']
d9 = w.clock.day_in('exodus', 2, 5, 9)
print('  the return marker (2, 5, 9) = day', d9, '; the morrow = day', d9 + 1, ex.date(d9 + 1))
dd = w.clock.day_in('exodus', 40, 5, 1)
print('  the daughters\' marker (40, 5, 1) = day', dd, '; days between', dd - d9)
print('  Seder Olam on the shelf:', __import__('os').path.exists(f'{ROOT}/Data/sefaria_export/Seder_Olam_Rabbah'))

print('\n==== (4) THE CALLEES ON FILE ====')
for ask in ('rate', 'money', 'human_firstborn', 'age', 'means', 'owner', 'one_lamb', 'partner'):
    try:
        case = {'ask': ask}
        if ask == 'means': case['means'] = 'coins'
        if ask == 'owner': case.update({'owner': 'priest', 'animal': 'donkey'})
        if ask == 'age': case['age_days'] = 31
        r = BM.levites(case, BM.DATA)
        print('  bamidbar.levites(%s) -> %s | %s' % (ask, r[0], r[1]))
    except Exception as e:
        print('  bamidbar.levites(%s) raised %s %s' % (ask, type(e).__name__, e))
print('  incense_shekel.shekel(twenty_gerah) ->', IS.shekel('twenty_gerah')['v'])
print('  incense_shekel.shekel(sanctuary_shekel) ->', IS.shekel('sanctuary_shekel')['v'])
for k in ('human', 'donkey', 'caesarean_animal'):
    r = PS.firstborn({'kind': k}, {}); print('  pesach.firstborn(%s) -> %s | %s' % (k, r[0], r[1]))
for case in ('status', 'unspecified_destination', 'priests_devotions', 'firstborn', 'person'):
    r = TM.devote(case); print('  temurah.devote(%s) -> %s | %s' % (case, r['v'], r['fx']))
for thing in ('firstling_donkey', 'devoted', 'land_tithe', 'animal_tithe'):
    r = TM.redeem(thing); print('  temurah.redeem(%s) -> %s' % (thing, r['v']))
for case in ('procedure', 'land_tithe_status'):
    r = TM.tithe(case); print('  temurah.tithe(%s) -> %s' % (case, r['v']))
for q in ('olah_hide', 'minchah_due', 'breast_thigh', 'seizure', 'eli_violation'):
    try:
        r = TZ.dues_machine({'ask': q}, TZ.DATA if hasattr(TZ, 'DATA') else {}); print('  tzav.dues_machine(%s) -> %s | %s' % (q, r[0], r[1]))
    except Exception as e:
        print('  tzav.dues_machine(%s) raised %s %s' % (q, type(e).__name__, e))
try:
    r = NS.restitution({'ask': 'terumah_measure'}, NS.DATA); print('  naso.restitution(terumah_measure) ->', r[0], '|', r[1])
except Exception as e:
    print('  naso.restitution raised', type(e).__name__, e)
try:
    r = HB.orlah('ratio'); print('  holiness_b.orlah(ratio) ->', r['v'] if isinstance(r, dict) else r)
except Exception as e:
    print('  holiness_b.orlah raised', type(e).__name__, e)
print('  zelophehad.inheritance_order signature:', inspect.signature(ZL.inheritance_order), '| heir_of:', inspect.signature(ZL.heir_of))
try:
    r = ZL.inheritance_order({'ask': 'ladder', 'survivors': ['daughter']}, ZL.DATA); print('  zelophehad.inheritance_order(ladder, daughter) ->', r[0])
except Exception as e:
    print('  zelophehad.inheritance_order raised', type(e).__name__, e)
print('  zelophehad asks in source:', sorted(set(re.findall(r"ask == '([a-z_]+)'", open(f'{ROOT}/World/step9/cold_run_zelophehad.py', encoding='utf-8').read()))))
print('  offerings.dispatch args:', inspect.signature(OF.dispatch))
try:
    r = OF.dispatch('firstborn'); print('  offerings.dispatch(firstborn) ->', str(r)[:300])
except Exception as e:
    print('  offerings.dispatch(firstborn) raised', type(e).__name__, str(e)[:200])
print('  offerings kinds in source:', sorted(set(re.findall(r"'([a-z_]+)'", src_of := open(f'{ROOT}/World/step9/cold_run_offerings.py', encoding='utf-8').read()[:4000])))[:40])
PRS = open(f'{ROOT}/World/step9/cold_run_priesthood.py', encoding='utf-8').read()
print('  priesthood cells (def):', re.findall(r'^def ([a-z_]+)\(', PRS, re.M))
print('  priesthood asks with stranger/terumah/blemish:', sorted(set(re.findall(r"'([a-z_]*(?:stranger|zar|terumah|blemish|eat|daughter|wage)[a-z_]*)'", PRS)))[:40])
SAS = open(f'{ROOT}/World/step9/cold_run_sanctions.py', encoding='utf-8').read()
print('  sanctions death_by_heaven seats:', SAS.count('death_by_heaven'), '| sanctions.mode signature', inspect.signature(SA.mode))
print('  tzav DATA keys:', list(TZ.DATA.keys())[:30] if hasattr(TZ, 'DATA') else '(no DATA)')

print('\n==== (5) THE TAPE\'S SUBJECTS AND THE NUM 16 LINE ====')
for s in ('korach', 'dathan', 'abiram', 'on', 'the-two-hundred-fifty', 'aaron', 'eleazar', 'the-levites', 'israel', 'moses', 'the-priests', 'the-tabernacle', 'the-golden-altar', 'the-altar', 'the-ark', 'the-firstborn-of-israel', 'the-twelve-princes', 'the-princes-of-israel', 'aarons-staff', 'the-staffs', 'the-congregation'):
    print('  %-24s subject lines %2d   as a token %3d' % (s, src.count("'subject': '%s'" % s), src.count("'%s'" % s)))
for ln in src.split('\n'):
    if 'Num 16' in ln and 'w.submit' in ln: print('  THE LINE:', ln.strip()[:400])
print('  the registry rows with korach/dathan/abiram/on/eleazar/two-hundred:')
reg = open(f'{ROOT}/logic/corpus/entity_registry.yaml', encoding='utf-8').read()
for m in re.finditer(r'^  ([a-z_0-9]+):', reg, re.M):
    if re.search(r'korach|dathan|abiram|^on$|eleazar|two_hundred|250|staff|censer', m.group(1)): print('    ', m.group(1))
for tok in ("'the-two-hundred-fifty'", "the_two_hundred_fifty", "two-hundred-fifty"):
    print('   registry has %s: %s' % (tok, tok.strip("'") in reg))

print('\n==== (6) THE REGISTER OF CHAPTERS 16-17 (V.w) against the planned lines ====')
reg2 = {}
for (b, c, v), ws in by.items():
    if b == 'Num' and c in (16, 17, 18):
        reg2[(c, v)] = [x for x, _, m in ws if m and m.startswith('V.w')]
LINES = [('korach_gathered_against', 16, 1, 3), ('moses_fell_and_set_the_test', 16, 4, 7), ('levites_rebuked', 16, 8, 11), ('dathan_and_abiram_refused', 16, 12, 14),
         ('moses_burned_and_swore', 16, 15, 15), ('censers_commanded', 16, 16, 17), ('censers_offered_at_the_tent', 16, 18, 19), ('separation_commanded', 16, 20, 21),
         ('moses_and_aaron_pleaded', 16, 22, 22), ('get_up_from_the_dwelling', 16, 23, 24), ('congregation_withdrew', 16, 25, 27), ('creation_test_declared', 16, 28, 30),
         ('earth_swallowed', 16, 31, 34), ('fire_consumed_the_250', 16, 35, 35),
         ('censers_beaten_into_plates', 17, 1, 5), ('congregation_murmured_you_killed', 17, 6, 7), ('plague_begun_and_stayed', 17, 8, 15),
         ('staffs_commanded', 17, 16, 20), ('staffs_laid_and_budded', 17, 21, 24), ('aarons_staff_kept', 17, 25, 26), ('congregation_despaired', 17, 27, 28)]
regv = sorted(k for k, vv in reg2.items() if vv)
print('  register verses: ch16 %d, ch17 %d, ch18 %d, total %d' % (tuple(sum(1 for c, v in regv if c == k) for k in (16, 17, 18)) + (len(regv),)))
for name, c, lo, hi in LINES:
    vv = [(v, reg2[(c, v)]) for v in range(lo, hi + 1) if reg2[(c, v)]]
    print('  %-34s %d:%d-%d  register verses %d  %s' % (name, c, lo, hi, len(vv), ' '.join('%d:%s' % (v, ','.join(x)) for v, x in vv)[:150]))
covered = {(c, v) for _, c, lo, hi in LINES for v in range(lo, hi + 1)}
print('  every verse of 16-17 in a line:', covered == {(c, v) for c in (16, 17) for v in range(1, (36 if c == 16 else 29))}, '; uncovered register verses:', [k for k in regv if k not in covered and k[0] != 18])
print('  chapter 18 register verses (the frames):', [k for k in regv if k[0] == 18])

print('\n==== (7) THE KINDS AND EFFECTS ON FILE — the names the design will use ====')
import yaml
ev = yaml.safe_load(open(f'{ROOT}/World/step9/event_vocabulary.yaml', encoding='utf-8')); E = ev.get('events') or ev
fx = yaml.safe_load(open(f'{ROOT}/World/step9/effect_vocabulary.yaml', encoding='utf-8')); F = fx.get('effects') or fx
cand_kinds = [n for n, *_ in LINES] + ['stranger_case', 'watch_case', 'gifts_case', 'firstborn_case', 'devotion_case', 'tithe_case', 'terumah_case', 'korach_case', 'plague_case', 'staff_case']
print('  kinds already on file among the candidates:', [k for k in cand_kinds if k in E])
cand_fx = ['gathered_against', 'rebelled', 'test_set', 'commanded', 'plea_made', 'glory_appeared', 'refused', 'separated', 'swallowed_alive', 'burned_in_fire', 'put_to_death', 'death_by_heaven',
           'strange_offering_barred', 'memorial_made', 'plague_struck', 'plague_removed', 'atoned_forgiven', 'staff_budded', 'kept_for_a_sign', 'murmured', 'tested_the_lord', 'watch_owed', 'stranger_barred',
           'due_to_priest', 'consecrated', 'most_holy', 'terumah_fed', 'consecrated_firstborn', 'redeem_or_break', 'to_be_redeemed', 'pays', 'exempt', 'salted', 'covenant_upheld', 'portion_given', 'entitled', 'wage_due', 'tithe_due',
           'in_force', 'rule_installed', 'declaration_owed', 'installed', 'no_more_wrath', 'counted', 'disqualified', 'accepted', 'exempt', 'fire_from_before_the_lord', 'fell_on_face']
print('  effects on file among the candidates:', [f for f in cand_fx if f in F])
print('  effects NOT on file among the candidates:', [f for f in cand_fx if f not in F])
for f in ('put_to_death', 'death_by_heaven', 'plague_struck', 'plague_removed', 'strange_offering_barred', 'burned_in_fire', 'due_to_priest', 'terumah_fed', 'stranger_barred', 'salted', 'covenant_upheld', 'tested_the_lord', 'murmured', 'glory_appeared', 'consecrated_firstborn', 'to_be_redeemed', 'portion_given', 'separated', 'rule_installed', 'in_force'):
    if f in F: print('   %-26s %s :: %s' % (f, F[f].get('class', F[f].get('kind', '?')), str(F[f].get('en', F[f].get('desc', '')))[:140].replace('\n', ' ')))
    elif f in E: print('   %-26s (a KIND, not an effect) form %s' % (f, E[f].get('form')))
print('  kinds on file named plague_struck / plague_removed / separated / murmured / tested:', {k: E[k].get('form') for k in ('plague_struck', 'plague_removed', 'separated', 'murmured', 'tested', 'staff_swallowed', 'fire_descended', 'incense_burned', 'glory_seen', 'gifts_given', 'portion_given', 'tithe_given', 'herd_tithed', 'terumah_eaten', 'priestly_due_claimed', 'consecrated_redeemed', 'firstborn_born') if k in E})
