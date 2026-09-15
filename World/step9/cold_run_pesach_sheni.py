import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# NUM 9:1-14 — THE SECOND PASSOVER (THE TENT sitting 2, 2026-09-09; World/step9/THE_TENT.md section 2).
# The first Numbers span compiled, and the second CASE-BORN law: the run halts on the unclean men (9:8
# "stand, and I will hear"), and the tent's output (9:9-14) is the statute itself — installed on the tent
# in the case's name (rule_installed) and running forward from the next event. Five motions of the
# deliverable rule, the wrap the sixth; every cell cites its source; every token probed (zero-report law);
# effects on every cell (the effects law). Reading ledger: logic/oral_triage/num_09_pesach_cloud_2026-09-09.md
# (the Sifrei on Numbers 64-71 + Onkelos); the exam's docket: num_09_pesach_sheni_exam_2026-09-09.md.
# A CORRECTION on the record: the map said this code was "already in the Passover engine's cells" — a
# grep found none; the Passover engine compiles Exod 12-13 alone and this runner CALLS it (the edge).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
# Every expected value this runner grades against must be a LITERAL typed from the answer sheet; the parser
# checks the source before anything runs, and the count below is the tripwire — it fails loudly the day the
# table changes.
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 26, ('the guard counted %d expectations, the tripwire holds 26' % GUARDED)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, contextlib
import effects_layer as FX
import world_engine as WE
import cold_run_pesach as PS                     # THE EDGE (dependency_dispositions.yaml: pesach_sheni -> pesach CALL, reference, procedure)

db = sqlite3.connect((_ROOT + '/Data/tanakh.sqlite'))

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def verse_text(ch, vs):
    rows = db.execute("""SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num'
        AND v.chapter=? AND v.verse=? ORDER BY w.idx""", (ch, vs)).fetchall()
    return ' '.join(strip(h) for (h,) in rows)

# ---- zero-report probes: the span's load-bearing tokens ---------------------------------------------------
PROBES = [
    ('במועדו', 9, 2,  'in its appointed time — the first Passover\'s date word'),
    ('טמאים',  9, 6,  'unclean — the case'),
    ('עמדו',   9, 8,  'stand — the halt'),
    ('ואשמעה', 9, 8,  'and I will hear'),
    ('רחקה',   9, 10, 'distant — the dotted heh\'s word'),
    ('לדרתיכם', 9, 10, 'to your generations'),
    ('השני',   9, 11, 'the second [month]'),
    ('מצות',   9, 11, 'unleavened bread'),
    ('ומררים', 9, 11, 'and bitter herbs'),
    ('ישאירו', 9, 12, 'they shall (not) leave over'),
    ('ישברו',  9, 12, 'they shall (not) break — the bone'),
    ('חקת',    9, 12, 'the statute of — the scope clause'),
    ('טהור',   9, 13, 'clean — the karet clause\'s subject'),
    ('וחדל',   9, 13, 'and refrained'),
    ('ונכרתה', 9, 13, 'and shall be cut off — karet'),
    ('גר',     9, 14, 'a proselyte'),
    ('אחת',    9, 14, 'one [statute]'),
]
for tok, ch, vs, note in PROBES:
    if tok not in verse_text(ch, vs).split():
        sys.exit('ZERO-REPORT LAW: probe %r (%s) failed at Num %d:%d — refusing to run' % (tok, note, ch, vs))
print('probes: all %d token probes fired  [zero-report law satisfied]\n' % len(PROBES))

P = []  # the provenance trail of the case being run
def ink(ref, note):  P.append(('INK',  'Num %s — %s' % (ref, note)))
def move(src, note): P.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P.append(('DATA', note))

def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P)


# ===== THE DATA CHANNEL — the two parameter rows the ink leaves open (motion 2's recorded settings) =========
DATA = {
    'distant_way': {
        'value': 'modiim',
        'settings': {
            'modiim': "from Modi'im and beyond, and its radius around Jerusalem (fifteen mil — Ulla, Pesachim 93b:11) — R. Akiva (Mishnah Pesachim 9:2; Sifrei Bamidbar 69:1 'the sages measured')",
            'city_entrance': "outside the place of its EATING — from Jerusalem's entrance outward, by the tithe's 'distant way' (Deut 14:24) — R. Eliezer in the Sifrei (69:1); Pesachim 94b:10-11 the tannaim on R. Eliezer",
            'court_threshold': "from the threshold of the court and beyond — R. Eliezer in the Mishnah (9:2; R. Yose's dotted heh), R. Yehuda in the Sifrei (69:1: outside the place of its fitness)"},
        'source': "the ink says 'a distant way' (9:10) and no measure — the distance is a DATUM; the dotted heh (9:10) qualifies it (Sifrei 69:2, Mishnah 9:2)"},
    'second_passover_nature': {
        'value': 'independent_festival',
        'settings': {
            'independent_festival': "the second Passover is a festival of its own — anyone who did not keep the first is obligated in it, and the karet clause reaches both (Rebbi: Sifrei Bamidbar 70:1, Pesachim 93a:7, 93a:9)",
            'redress': "the second is the first's redress (tashlumin) — one obligated in the first who did not keep it may keep it then; the karet is the first's alone (R. Natan: Sifrei 70:1, Pesachim 93a:7, 93a:10)",
            'repair': "the second REPAIRS the first — kept, it removes the first's karet; not kept, the first's karet stands (R. Chananya b. Akavya: Pesachim 93a:7, 93a:11)"},
        'source': "the ink writes 'shall be cut off' and 'his sin he shall bear' in one verse (9:13) — the three readings of the 'because' (Pesachim 93a:12-93b:6); the Tosefta's printed attribution (8:2-3) inverts two names — recorded in the docket ledger"},
}


# ===== F1: THE SECOND PASSOVER (Num 9:10-13) ================================================================
def second_passover(case, data):
    del P[:]
    ask = case['ask']
    nature = data['second_passover_nature']['value']
    if ask == 'who_keeps':
        r = case['reason']
        ink('9:10', '"any man who is UNCLEAN BY A CORPSE (טמא לנפש), or ON A DISTANT WAY (בדרך רחקה), of you or of your '
                    'generations, shall keep a Passover to the LORD" — the two named cases')
        ink('9:11', '"in the SECOND month, on the fourteenth day, between the evenings they shall keep it" — the date')
        if case.get('minor'):
            ink('9:13', '"his sin shall he bear, THAT MAN (האיש ההוא)" — a man, not a minor')
            move('Sifrei Bamidbar 70:1', '"that man" — a man and not a minor; the woman included from "that soul"')
            return out('exempt (a man, not a minor)', ['exempt'])
        if r in ('unclean_by_corpse', 'distant_way'):
            return out('keeps the second Passover', ['second_passover_due'])
        if r == 'other_impurity':
            move('Sifrei Bamidbar 69:1', 'BINYAN AV from the two — the corpse-unclean is not like the distant nor the distant like '
                 'the corpse-unclean; what they share: one who did not keep the first keeps the second — so ALL who could not; '
                 'Tosefta Pesachim 8:1\'s roster (zavim, zavot, menstruants, lepers)')
            return out('keeps the second Passover', ['second_passover_due'])
        if r in ('forced', 'unwitting'):
            move('Sifrei Bamidbar 69:1 + Mishnah Pesachim 9:1', '"all who could not keep the first keep the second" — the forced '
                 'and the unwitting are the Mishnah\'s own second clause')
            return out('keeps the second Passover', ['second_passover_due'])
        if r == 'deliberate':
            move('Pesachim 92b:8 (Rav Nachman on Mishnah 9:1: "and did not keep" includes the deliberate) + Tosefta Pesachim 8:1 '
                 '("the deliberate" on the roster)', 'the deliberate too keeps the second — the karet question is separate')
            return out('keeps the second Passover', ['second_passover_due'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'karet':
        f, s = case['first'], case['second']       # each: 'kept' | 'deliberate' | 'unwitting' | 'unclean_or_distant'
        ink('9:13', '"and the man who is CLEAN and was NOT on a way and REFRAINED (וחדל) from keeping the Passover — that soul '
                    'shall be CUT OFF (ונכרתה) from its people; for the offering of the LORD he did not bring in its appointed '
                    'time, his sin shall he bear"')
        if f == 'unclean_or_distant' and s != 'kept':
            move('Mishnah Pesachim 9:1 (the last clause)', 'the unclean and the distant were named to teach: THESE are exempt '
                 'from karet [when the second is missed]; the others liable — the answer sheet\'s row (Rebbi\'s baraita, '
                 'Pesachim 93a:7, would reach the deliberate second; the Mishnah\'s row grades)')
            return out('exempt from karet', ['exempt'])
        if f == 'deliberate' and s == 'deliberate':
            move('Pesachim 93b:7', 'deliberate on both — ALL agree: karet')
            return out('karet', ['karet_cut_off'])
        if f == 'unwitting' and s == 'unwitting':
            move('Pesachim 93b:7', 'unwitting on both — ALL agree: exempt')
            return out('exempt from karet', ['exempt'])
        if f == 'deliberate' and s == 'unwitting':
            dat('the row second_passover_nature = %s' % nature)
            move('Pesachim 93b:8', 'deliberate first, unwitting second — Rebbi and R. Natan: liable (the first\'s own karet); '
                 'R. Chananya b. Akavya: exempt (the second, though missed unwittingly, could still repair? — no: he holds the '
                 'first\'s karet stands only when the second is not kept, and here it was not kept — the Gemara reads him '
                 'exempt because the missing was unwitting)')
            return out('karet' if nature in ('independent_festival', 'redress') else 'exempt from karet',
                       ['karet_cut_off'] if nature in ('independent_festival', 'redress') else ['exempt'])
        if f == 'unwitting' and s == 'deliberate':
            dat('the row second_passover_nature = %s' % nature)
            move('Pesachim 93b:9', 'unwitting first, deliberate second — Rebbi: liable (the second a festival of its own); '
                 'R. Natan and R. Chananya b. Akavya: exempt (the second is the first\'s redress or repair — no karet of its own)')
            return out('karet' if nature == 'independent_festival' else 'exempt from karet',
                       ['karet_cut_off'] if nature == 'independent_festival' else ['exempt'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'distance':
        dat('the row distant_way = %s: %s' % (data['distant_way']['value'], data['distant_way']['settings'][data['distant_way']['value']]))
        ink('9:10', '"on a distant way" — no measure in the ink; the heh dotted (Sifrei 69:2, Mishnah 9:2)')
        return out("from Modi'im and beyond (fifteen mil)" if data['distant_way']['value'] == 'modiim' else data['distant_way']['value'], ['exempt'])
    if ask == 'sabbath_override':
        ink('9:13', '"for the offering of the LORD he did not bring IN ITS APPOINTED TIME (במעדו)" — the second\'s appointed time')
        move('Sifrei Bamidbar 70:1 (+ 65:1 on the first)', '"in its appointed time" — the second Passover overrides the Sabbath; '
             'Mishnah Pesachim 9:3: both override the Sabbath; Tosefta 8:4')
        return out('overrides the Sabbath', ['exempt'])
    if ask == 'impurity_override':
        ink('9:10', '"any man who is unclean by a corpse... shall keep a Passover" — the second exists FOR the unclean')
        move('Sifrei Bamidbar 70:1', '"its whole reason is his being unclean at the first — shall he come and keep it in impurity?"; '
             'Tosefta Pesachim 8:3; Pesachim 95b:5 (the first tanna, the anonymous Mishnah voice, against R. Yehuda)')
        return out('does not override impurity', ['barred_from_it'])
    if ask == 'congregation':
        ink('9:6', '"and there were MEN (אנשים) who were unclean" — individuals')
        move('Sifrei Bamidbar 70:1', '"they shall keep it" — individuals keep the second, the congregation never (from "there were '
             'men"; R. Natan from "the man who is clean"); Mishnah Pesachim 9:4: the majority unclean offers the FIRST in impurity')
        return out('the congregation offers the first in impurity; no second Passover', ['exempt'])
    if ask == 'scope':
        item = case['item']
        ink('9:11', '"with unleavened bread and bitter herbs they shall eat it"')
        ink('9:12', '"they shall not leave of it until morning, and a bone they shall not break in it; according to ALL THE '
                    'STATUTE OF THE PASSOVER (ככל חקת הפסח) they shall keep it"')
        if item == 'leaven_in_house':
            move('Sifrei Bamidbar 69:2', '"a bone" was in the general and LEFT IT to teach on the general (the eighth middah): "all '
                 'the statute" = the mitzvot ON ITS BODY — not the seven days\' matzah, not the leaven; Pesachim 95a:14 ("it '
                 'shall not be seen / found" excluded); Mishnah 9:3: leaven and matzah with him in the house')
            return out('permitted', ['exempt'])
        if item == 'hallel_at_eating':
            move('Pesachim 95b:2 (R. Yochanan in R. Shimon b. Yehotzadak\'s name: "the song of a night sanctified as a festival", '
                 'Isa 30:29)', 'the second Passover\'s night is no festival — no hallel at the eating; hallel at the making '
                 'stands (95b:3); Mishnah 9:3')
            return out('not required', ['exempt'])
        if item == 'bone':
            v, e, pr = PS.paschal_procedure({'ask': 'break_bone', 'lamb_valid': case.get('lamb_valid', True)}, {})   # THE CALL
            P.append(('MOVE', 'CALLED cold_run_pesach.paschal_procedure(break_bone) -> %s [%s]' % (v, '; '.join(x[1][:50] for x in pr))))
            return out(v, e)
        if item == 'leftover':
            v, e, pr = PS.paschal_procedure({'ask': 'leftover'}, {})                                                    # THE CALL
            P.append(('MOVE', 'CALLED cold_run_pesach.paschal_procedure(leftover) -> %s' % v))
            return out(v + ' (of the second month)', e)
        if item == 'roasted':
            v, e, pr = PS.paschal_procedure({'ask': 'preparation'}, {})                                                 # THE CALL
            P.append(('MOVE', 'CALLED cold_run_pesach.paschal_procedure(preparation) -> %s; Tosefta Pesachim 8:4 "not raw nor boiled" at both' % v))
            return out(v, e)
        return out('no verdict in span', [FX.NONE])
    if ask == 'the_case':
        ink('9:6', '"and there were men who were unclean by a human corpse and could not keep the Passover ON THAT DAY, and they '
                   'came near before Moses and before Aaron"')
        ink('9:7', '"we are unclean by a human corpse — why should we be HELD BACK (נגרע) from bringing the offering of the LORD '
                   'in its appointed time among the children of Israel?"')
        ink('9:8', '"stand, and I will hear what the LORD will command concerning you" — the HALT')
        ink('9:10-11', '"any man who is unclean by a corpse... shall keep a Passover to the LORD in the second month" — the OUTPUT')
        return out('held back from the first; the second Passover in the second month', ['second_passover_due'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE PROSELYTE (Num 9:14) ==========================================================================
def proselyte(case, data):
    del P[:]
    ink('9:14', '"and if a proselyte (גר) sojourns with you and keeps a Passover to the LORD — according to the statute of the '
                'Passover and its ordinance so shall he do; ONE STATUTE (חקה אחת) shall be for you, for the proselyte and for '
                'the native of the land"')
    if case['converted'] == 'before_the_first':
        v, e, pr = PS.access_filter({'kind': 'convert'}, {})                                                             # THE CALL
        P.append(('MOVE', 'CALLED cold_run_pesach.access_filter(convert) -> %s [Exod 12:48-49 "one law"]' % v))
        move('Sifrei Bamidbar 71:1', '"as the native on the fourteenth, so the proselyte" — not as soon as he converts')
        return out('keeps the first on the fourteenth, as the native', e)
    if case['converted'] == 'between_the_passovers':
        nature = data['second_passover_nature']['value']
        dat('the row second_passover_nature = %s' % nature)
        move('Tosefta Pesachim 8:2 + Pesachim 93a:8-10', 'Rebbi: he keeps the second (a festival of its own); R. Natan: no — never '
             'obligated in the first (the second its redress); Sifrei 71:1\'s R. Shimon b. Elazar excludes him')
        if nature == 'independent_festival':
            return out('keeps the second Passover', ['second_passover_due'])
        return out('exempt (never obligated in the first)', ['exempt'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP (THE TENT sitting 2, 2026-09-09) — the daemon, the scene, the narrative ------------------------
def law_pesach_sheni(event, world):
    """Num 9:1-14 (cold_run_pesach_sheni.py F1-F2). CASE-BORN: installed by the tent's output (statute_declared)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'passover_kept':
        return [E_('passover_in_its_time', event['subject'], value=event.get('date', 'the fourteenth of the first month'), law='F1 [INK 9:5 "and they kept the Passover in the first month on the fourteenth day" — the second year\'s Passover; Sifrei 67:1: the only one of the forty years]')]
    if k == 'unclean_at_the_passover':
        due = WE.due_of_passover_sheni(world)                                          # the fourteenth of the second month through the Calendar (the row passover_sheni)
        return [E_('second_passover_due', p, cp='HEAVEN', due=due, value=event.get('reason', 'unclean_by_corpse'), law='F1 [INK 9:10-11 "any man who is unclean by a corpse... shall keep a Passover to the LORD in the second month" — decided at the case, before the halt (the boot setting); the due the Calendar\'s]') for p in event['persons']]
    if k == 'missed_the_first_passover':
        p = event['person']
        if event.get('minor'):
            v, e, _ = second_passover({'ask': 'who_keeps', 'reason': event['reason'], 'minor': True}, DATA)
            return [E_('exempt', p, value='a_man_not_a_minor', law='F1 [INK 9:13 "that MAN"; Sifrei 70:1]')]
        if event.get('kept_second') is None:                                            # the eligibility row: who keeps the second
            v, e, _ = second_passover({'ask': 'who_keeps', 'reason': event['reason']}, DATA)
            return [E_('second_passover_due', p, cp='HEAVEN', due=WE.due_of_passover_sheni(world), value=event['reason'], law='F1 [%s]' % v)]
        v, e, _ = second_passover({'ask': 'karet', 'first': event['first'], 'second': event['second']}, DATA)   # the karet row
        if e == ['karet_cut_off']:
            return [E_('karet_cut_off', p, cp='HEAVEN', value='%s/%s' % (event['first'], event['second']), law='F1 [INK 9:13; Pesachim 93b:7-9 under the row second_passover_nature — %s]' % v)]
        return [E_('exempt', p, value='%s/%s' % (event['first'], event['second']), law='F1 [Mishnah Pesachim 9:1 / Pesachim 93b:7-9 — %s]' % v)]
    if k == 'converted_between_the_passovers':
        v, e, _ = proselyte({'ask': 'proselyte', 'converted': 'between_the_passovers'}, DATA)
        if e == ['second_passover_due']:
            return [E_('second_passover_due', event['person'], cp='HEAVEN', due=WE.due_of_passover_sheni(world), value='converted_between', law='F2 [Tosefta Pesachim 8:2 Rebbi — %s]' % v)]
        return [E_('exempt', event['person'], value='converted_between', law='F2 [Tosefta Pesachim 8:2 R. Natan — %s]' % v)]
    if k == 'second_passover_kept':
        out_ = []
        if event.get('leaven_in_house'):
            out_.append(E_('exempt', event['person'], value='leaven_with_him_at_the_second', law='F1 [INK 9:12 "all the statute" bounded to the body — Sifrei 69:2; Mishnah 9:3]'))
        if event.get('bone_broken'):
            v, e, _ = second_passover({'ask': 'scope', 'item': 'bone', 'lamb_valid': event.get('lamb_valid', True)}, DATA)
            out_.append(E_('lashes', event['person'], law='F1 [INK 9:12 "a bone they shall not break"; CALLED PS.paschal_procedure(break_bone) -> %s]' % v) if e == ['lashes']
                        else E_('exempt', event['person'], value='the_disqualified_lambs_bone', law='F1 [CALLED PS.paschal_procedure(break_bone) -> %s]' % v))
        if event.get('left_over'):
            out_.append(E_('burn_remainder', event['lamb'], due=world.clock.day + 2, law='F1 [INK 9:12 "they shall not leave of it until morning"; CALLED PS.paschal_procedure(leftover): the burn on the sixteenth — of the second month]'))
        return out_
    return []


def scene():
    """THE SCENE — the recorded rows replayed on the world engine (the exodus epoch: the Calendar's second month)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 9:10-14: Mishnah Pesachim 9:1-4 and Tosefta Pesachim 8 on the engine (the exodus epoch; the second month the Calendar\'s)', epoch='exodus')
        w.laws = [law_pesach_sheni]
        w.advance(w.clock.next('passover'))                                             # the fourteenth of the first month
        for p, r in (('the-unclean', 'unclean_by_corpse'), ('the-distant', 'distant_way'), ('the-zav', 'other_impurity'), ('the-forced', 'forced'), ('the-unwitting', 'unwitting'), ('the-deliberate', 'deliberate')):
            w.submit({'kind': 'missed_the_first_passover', 'subject': p, 'person': p, 'reason': r, 'kept_second': None, 'case_source': 'Mishnah Pesachim 9:1; Tosefta Pesachim 8:1 — who keeps the second'})
        w.submit({'kind': 'missed_the_first_passover', 'subject': 'the-minor', 'person': 'the-minor', 'reason': 'deliberate', 'kept_second': None, 'minor': True, 'case_source': 'Sifrei Bamidbar 70:1 — "that man": not a minor'})
        for p, f, s in (('the-refrainer', 'deliberate', 'deliberate'), ('the-unclean-who-missed-both', 'unclean_or_distant', 'deliberate'), ('the-unwitting-both', 'unwitting', 'unwitting'),
                        ('the-deliberate-then-unwitting', 'deliberate', 'unwitting'), ('the-unwitting-then-deliberate', 'unwitting', 'deliberate')):
            w.submit({'kind': 'missed_the_first_passover', 'subject': p, 'person': p, 'reason': f, 'kept_second': False, 'first': f, 'second': s, 'case_source': 'Mishnah Pesachim 9:1 (the karet clause); Pesachim 93b:7-9 (the table)'})
        w.submit({'kind': 'converted_between_the_passovers', 'subject': 'the-convert-between', 'person': 'the-convert-between', 'converted': 'between_the_passovers', 'case_source': 'Tosefta Pesachim 8:2 — Rebbi against R. Natan'})
        w.advance(w.clock.next('passover_sheni'))                                       # the fourteenth of the second month: the dues FIRE
        w.submit({'kind': 'second_passover_kept', 'subject': 'the-keeper', 'person': 'the-keeper', 'leaven_in_house': True, 'bone_broken': True, 'left_over': True, 'lamb': 'the-second-lamb', 'case_source': 'Mishnah Pesachim 9:3 — the difference table; Num 9:11-12'})
        w.advance(w.clock.day + 2)                                                       # the sixteenth: the leftover's burn timer FIRES
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return (n('the-unclean', 'second_passover_due'), n('the-distant', 'second_passover_due'), n('the-zav', 'second_passover_due'), n('the-forced', 'second_passover_due'),
            n('the-unwitting', 'second_passover_due'), n('the-deliberate', 'second_passover_due'), n('the-minor', 'exempt'),
            n('the-refrainer', 'karet_cut_off'), n('the-unclean-who-missed-both', 'exempt'), n('the-unwitting-both', 'exempt'),
            n('the-deliberate-then-unwitting', 'karet_cut_off'), n('the-unwitting-then-deliberate', 'karet_cut_off'),
            n('the-convert-between', 'second_passover_due'), n('the-keeper', 'exempt'), n('the-keeper', 'lashes'), n('the-second-lamb', 'burn_remainder'),
            tset, fired, w.clock.eras['exodus'].date(w.clock.day)[1:]), w
SCENE, _W = scene()


def narrative():
    """THE TENT sitting 2 (2026-09-09; THE_TENT.md section 2): the chapter's own case AS HISTORY — Num 9:5-14's four lines in the
    text's order on a world with the library's tent daemon registered first (the Passover kept, the case, the halt, the output);
    recorded by the sequential run's recorder and stitched onto the tape. Not a graded cell: the tuple below is a tripwire typed
    from THE_TENT.md's design; the sequence world's RUN tuple grades the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 9:5-14: the unclean men at the Passover on the tape — the keeping, the case, the halt, the output (the exodus epoch)', epoch='exodus')
        w.laws = [WE.law_tent, law_pesach_sheni]
        w.advance(w.clock.day_in('exodus', 2, 1, 14))                                   # the fourteenth of the first month of the second year (9:5)
        w.submit({'kind': 'passover_kept', 'subject': 'israel', 'date': 'the fourteenth of the first month of the second year', 'case_source': 'Num 9:5 — and they kept the Passover in the first month, on the fourteenth day of the month, between the evenings, in the wilderness of Sinai'})
        w.submit({'kind': 'unclean_at_the_passover', 'subject': 'the-unclean-men', 'persons': ['the-unclean-men'], 'reason': 'unclean_by_corpse', 'day_of_month': 14, 'case_source': 'Num 9:6-7 — and there were men who were unclean by a human corpse and could not keep the Passover on that day; and they came near before Moses and before Aaron: why should we be held back?'})
        w.submit({'kind': 'stood_to_hear', 'subject': 'the-unclean-men', 'persons': ['the-unclean-men'], 'case_of': 'Num 9:6', 'uncertainty': 'the_mode', 'case_source': 'Num 9:8 — and Moses said to them: stand, and I will hear what the LORD will command concerning you (Sifrei Bamidbar 68:1: I have not heard; R. Chidka: whether the blood is sprinkled for them)'})
        w.submit({'kind': 'statute_declared', 'subject': 'the-unclean-men', 'persons': ['the-unclean-men'], 'installs': 'law_pesach_sheni', 'case_source': 'Num 9:9-14 — and the LORD spoke to Moses saying: speak to the children of Israel saying: any man who is unclean by a corpse or on a distant way... shall keep a Passover to the LORD in the second month; one statute shall be for you'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: [e.get('open') for e in w.entity(eid).ledger if e['effect'] == eff]
    owed = [e for e in w.entity('the-court').ledger if e['effect'] == 'declaration_owed']
    pend = [t for _, t in w.timers if t['effect'] == 'second_passover_due' and t['subject'] == 'the-unclean-men']
    return (n('israel', 'passover_in_its_time'), len(pend), n('the-unclean-men', 'second_passover_due'), n('the-unclean-men', 'waits_for_the_word'), is_open('the-unclean-men', 'waits_for_the_word'),
            len(owed), owed[0].get('open') if owed else None, (owed[0].get('covered_by') or None) if owed else None, n('the-tabernacle', 'rule_installed'),
            w.clock.eras['exodus'].date(pend[0]['due'])[1:] if pend else None), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (1, 1, 0, 1, [False], 1, False, ['law_pesach_sheni'], 1, (2, 14))   # THE_TENT.md section 2: the Passover kept on the people; the men's due a PENDING timer (the code decides before the halt), no ledger line; the wait written and CLOSED by the output; the docket owed then closed, covered by law_pesach_sheni; the rule installed; the due the fourteenth of the second month
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE TENT: the second Passover narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the Mishnah's and the Tosefta's rows.
# =====================================================================
CASES = [
    # F1 — who keeps the second
    ('Mishnah Pesachim 9:1 — unclean by a corpse at the first',
     lambda: second_passover({'ask': 'who_keeps', 'reason': 'unclean_by_corpse'}, DATA), 'keeps the second Passover'),
    ('Mishnah Pesachim 9:1 — on a distant way at the first',
     lambda: second_passover({'ask': 'who_keeps', 'reason': 'distant_way'}, DATA), 'keeps the second Passover'),
    ('Tosefta Pesachim 8:1 — the zav (another impurity): the Sifrei\'s binyan av',
     lambda: second_passover({'ask': 'who_keeps', 'reason': 'other_impurity'}, DATA), 'keeps the second Passover'),
    ('Mishnah Pesachim 9:1 — prevented by force',
     lambda: second_passover({'ask': 'who_keeps', 'reason': 'forced'}, DATA), 'keeps the second Passover'),
    ('Mishnah Pesachim 9:1 — the unwitting',
     lambda: second_passover({'ask': 'who_keeps', 'reason': 'unwitting'}, DATA), 'keeps the second Passover'),
    ('Tosefta Pesachim 8:1 — the deliberate (Rav Nachman, Pesachim 92b:8)',
     lambda: second_passover({'ask': 'who_keeps', 'reason': 'deliberate'}, DATA), 'keeps the second Passover'),
    ('Sifrei Bamidbar 70:1 / Tosefta 8:6 — "that man": a minor',
     lambda: second_passover({'ask': 'who_keeps', 'reason': 'deliberate', 'minor': True}, DATA), 'exempt (a man, not a minor)'),
    # F1 — the karet clause
    ('Num 9:13 — clean and near, refrained from both (Pesachim 93b:7)',
     lambda: second_passover({'ask': 'karet', 'first': 'deliberate', 'second': 'deliberate'}, DATA), 'karet'),
    ('Mishnah Pesachim 9:1 (the last clause) — unclean at the first, missed the second: exempt',
     lambda: second_passover({'ask': 'karet', 'first': 'unclean_or_distant', 'second': 'deliberate'}, DATA), 'exempt from karet'),
    ('Pesachim 93b:7 — unwitting on both',
     lambda: second_passover({'ask': 'karet', 'first': 'unwitting', 'second': 'unwitting'}, DATA), 'exempt from karet'),
    ('Pesachim 93b:8 — deliberate first, unwitting second (Rebbi and R. Natan liable; R. Chananya exempt)',
     lambda: second_passover({'ask': 'karet', 'first': 'deliberate', 'second': 'unwitting'}, DATA), 'karet'),
    ('Pesachim 93b:9 — unwitting first, deliberate second (Rebbi liable; R. Natan and R. Chananya exempt)',
     lambda: second_passover({'ask': 'karet', 'first': 'unwitting', 'second': 'deliberate'}, DATA), 'karet'),
    # F1 — the parameters and the overrides
    ('Mishnah Pesachim 9:2 — the distance: R. Akiva\'s Modi\'im (the running setting; R. Eliezer\'s threshold recorded)',
     lambda: second_passover({'ask': 'distance'}, DATA), "from Modi'im and beyond (fifteen mil)"),
    ('Mishnah Pesachim 9:3 / Tosefta 8:4 — the second overrides the Sabbath',
     lambda: second_passover({'ask': 'sabbath_override'}, DATA), 'overrides the Sabbath'),
    ('Tosefta Pesachim 8:3 — the second does not override impurity (Pesachim 95b:5)',
     lambda: second_passover({'ask': 'impurity_override'}, DATA), 'does not override impurity'),
    ('Mishnah Pesachim 9:4 / Sifrei 70:1 — the congregation unclean: the first in impurity, no second',
     lambda: second_passover({'ask': 'congregation'}, DATA), 'the congregation offers the first in impurity; no second Passover'),
    # F1 — the scope (the difference table)
    ('Mishnah Pesachim 9:3 — leaven with him in the house at the second',
     lambda: second_passover({'ask': 'scope', 'item': 'leaven_in_house'}, DATA), 'permitted'),
    ('Mishnah Pesachim 9:3 — no hallel at the eating at the second',
     lambda: second_passover({'ask': 'scope', 'item': 'hallel_at_eating'}, DATA), 'not required'),
    ('Num 9:12 — the bone at the second: the Passover engine called',
     lambda: second_passover({'ask': 'scope', 'item': 'bone'}, DATA), 'lashes'),
    ('Num 9:12 — the leftover at the second: the Passover engine called',
     lambda: second_passover({'ask': 'scope', 'item': 'leftover'}, DATA), 'burn on the 16th (of the second month)'),
    ('Tosefta Pesachim 8:4 — roasted at the second: the Passover engine called',
     lambda: second_passover({'ask': 'scope', 'item': 'roasted'}, DATA), 'roasted only'),
    # F2 — the proselyte
    ('Sifrei Bamidbar 71:1 — converted before the first: as the native on the fourteenth (the access filter called)',
     lambda: proselyte({'ask': 'proselyte', 'converted': 'before_the_first'}, DATA), 'keeps the first on the fourteenth, as the native'),
    ('Tosefta Pesachim 8:2 — converted between the Passovers: Rebbi (the running setting; R. Natan recorded)',
     lambda: proselyte({'ask': 'proselyte', 'converted': 'between_the_passovers'}, DATA), 'keeps the second Passover'),
    # THE CASE
    ('Num 9:6-11 — the chapter\'s own case: the unclean men on the fourteenth',
     lambda: second_passover({'ask': 'the_case'}, DATA), 'held back from the first; the second Passover in the second month'),
    # THE WRAP: the scene on the world engine
    ('THE SCENE on the world engine — the wrap: six who keep the second (their dues set at the first Passover and FIRED on the Calendar\'s fourteenth of the second month), the minor exempt, three karet and two exempt on the karet table, the between-Passovers convert\'s due (Rebbi), the keeper\'s leaven permitted, his bone lashed, his leftover burned on the sixteenth of the second month',
     lambda: (SCENE, [FX.NONE], [('INK', 'Num 9:10-14 — the recorded rows replayed: Mishnah Pesachim 9:1-4, Tosefta Pesachim 8:1-6, Pesachim 93b:7-9')]),
     (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 8, (2, 16))),
    ('THE NARRATIVE on the world engine — the tape\'s four lines with the tent daemon first (the tripwire typed from THE_TENT.md section 2)',
     lambda: (NARRATIVE, [FX.NONE], [('INK', 'Num 9:5-14 — the Passover kept, the case, the halt, the output')]),
     (1, 1, 0, 1, [False], 1, False, ['law_pesach_sheni'], 1, (2, 14))),
]

if __name__ == '__main__':
    ok = 0
    frac = {'INK': 0, 'MOVE': 0, 'DATA': 0}
    used_effects = []
    print()
    for label, fn, want in CASES:
        got, effects, prov = fn()
        hit = got == want
        ok += hit
        kinds = [k for k, _ in prov]
        cls = 'INK' if all(k == 'INK' for k in kinds) else ('MOVE' if 'MOVE' in kinds else 'DATA')
        frac[cls] += 1
        print('%s  [%s]  %s' % ('PASS' if hit else 'MISS', cls, label))
        if not hit:
            print('      expected: %s' % (want,))
            print('      got     : %s' % (got,))
        used_effects += effects
        for line in FX.render(effects):
            print('        ->%s' % line)
    print()
    print('WATCH COVERAGE (the wrap):')
    _W.print_coverage()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, len(CASES)))
    tot = len(CASES)
    print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%) · data %d/%d (%.0f%%)' %
          (frac['INK'], tot, 100.0 * frac['INK'] / tot, frac['MOVE'], tot, 100.0 * frac['MOVE'] / tot, frac['DATA'], tot, 100.0 * frac['DATA'] / tot))
    ops = FX.summarize(used_effects)
    print('LEDGER OPS this span writes:', ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
    print('THE PARAMETER ROWS: distant_way = %s; second_passover_nature = %s (the other settings recorded in DATA)' % (DATA['distant_way']['value'], DATA['second_passover_nature']['value']))
    if ok == len(CASES):
        print('\nTHE SECOND PASSOVER COMPILES — the first Numbers span, the second case-born law: the run halted on the unclean men and the tent\'s statute installed it.')
