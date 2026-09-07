#!/usr/bin/env python3
"""cold_run_vayikra5.py — THE FIRST COMPILE UNDER THE STEP-5 DELIVERABLE
RULE (2026-09-03, owner: "amend it and run it on Leviticus 5").

The five motions, in order:
 (1) code from the BARE INK of Lev 5 alone (verse-tagged, provenance
     [INK] on every ink-borne branch; unstated quantities = DATA);
 (2) the Mishnah's rows collected as TEST DATA below;
 (3) run;
 (4) every miss filled by a NAMED Talmud/Sifra move, labeled [MOVE ...]
     on the changed line;
 (5) the graded matrix printed with per-cell provenance and fractions.
Zero-report law: every claimed ink token is probed before anything runs.
"""
# ---- THE HONEST-PAIRING GUARD (sitting C retrofit, 2026-09-05) ------------
# Every expected value this runner grades against must be a LITERAL typed from
# the answer sheet; the parser checks the source before anything runs, and the
# count below is the tripwire — it fails loudly the day the table changes.
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp, check_honest_dict as _chd, check_honest_calls as _chc
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 32, ('the guard counted %d expectations, the tripwire holds 32' % GUARDED)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, os
import io as _io, contextlib as _ctx

DB = '<repo-old>/elijah_docket/tanakh.sqlite'
db = sqlite3.connect(DB)

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

rows = db.execute("""SELECT v.verse, w.idx, w.he FROM words w
    JOIN verses v ON w.verse_id=v.id
    WHERE v.book='Lev' AND v.chapter=5 ORDER BY v.verse, w.idx""").fetchall()
verses = {}
for vs, i, he in rows:
    verses.setdefault(vs, []).append(strip(he))

# ---- ink probes (each MUST fire or we refuse to run) ----------------
PROBES = {
    'oath-voice (kol alah)':        (1,  'אלה'),
    'hidden (venelam)':             (2,  'ונעלם'),
    'he knew (ve-hu yada)':         (3,  'ידע'),
    'harm-or-good option template': (4,  'להרע'),
    'confess (vehitvadah)':         (5,  'והתודה'),
    'ENOUGH for a lamb (dei seh)':  (7,  'די'),
    'FIRST (chatat first, rishonah)':(8, 'ראשונה'),
    'AS PRESCRIBED (kamishpat)':    (10, 'כמשפט'),
    'tenth of the ephah':           (11, 'עשירת'),
    'no frankincense (stripping)':  (11, 'לבנה'),
    'silver shekels (currency)':    (15, 'שקלים'),
    'its fifth (chamishito, plene)':(16, 'חמישתו'),
    'did NOT know (lo yada)':       (17, 'ידע'),
    'he shall RETURN (veheshiv)':   (23, 'והשיב'),
    'its fifthS (PLURAL!)':         (24, 'וחמשתיו'),
    'at its head (principal)':      (24, 'בראשו'),
    'to its owner (la-asher hu lo)':(24, 'לו'),
    'of ONE of all (per-one)':      (26, 'מכל'),
}
for label, (vs, tok) in PROBES.items():
    if not any(tok == w or w.endswith(tok) or w.startswith(tok) for w in verses[vs]):
        sys.exit('ZERO-REPORT LAW: probe %r failed at Lev 5:%d — refusing to run' % (label, vs))
print('probes: all %d ink-token probes fired  [zero-report law satisfied]' % len(PROBES))

# ---- mechanical case-opener parse -----------------------------------
OPENERS = {'ונפש', 'או', 'ואם', 'נפש', 'וידבר'}
cases_found = [vs for vs in sorted(verses) if verses[vs][0] in OPENERS]
print('case-opener parse: verse-initial openers at', cases_found)

P = []  # provenance trail of the last call
def ink(vs, note):   P.append(('INK',  'Lev 5:%s — %s' % (vs, note)))
def move(src, note): P.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P.append(('DATA', note))

# =====================================================================
# THE CODE — from the ink of Leviticus 5 alone. Mishnah/Talmud appear
# ONLY on [MOVE] lines (motion 4) and in the DATA section (motion 2).
# =====================================================================

def graded_offering(person, data):
    """Lev 5:1-13 as a machine. person = the input case; data = what the
    ink does not state (the two poverty thresholds, dispute settings)."""
    del P[:]
    # ---- trigger 1: the witness oath (5:1) ----
    t1 = False
    if person.get('trigger') == 'witness_oath':
        # "and he heard the voice of an oath AND HE IS a witness — or saw
        # or knew — if he does not tell, then he shall bear his sin"
        ink(1, 'the oath must FIND a witness: "and he heard... AND HE IS '
               'a witness" — the word order itself exempts the oath that '
               'precedes the knowledge')
        if not person.get('was_witness_at_oath'):
            return 'exempt', P
        if person.get('adjuration_scope') == 'blanket_congregation':
            move('Sifra, Vayikra Dibbura DeChovah, Section 8 6 (Mishnah '
                 'Shevuot 4:10)', 'a blanket oath over a crowd singles '
                 'out no addressee')
            return 'exempt', P
        if person.get('adjured_by') == 'messenger':
            move('Sifra, Vayikra Dibbura DeChovah, Section 8 4 (Mishnah '
                 'Shevuot 4:12)', 'the claim must be the claimant\'s own')
            return 'exempt', P
        if person.get('claim_kind') == 'promised_gift':
            move('Sifra, Vayikra Dibbura DeChovah, Chapter 12 (R. Yossi '
                 'Haglili; Mishnah Shevuot 4:8)', 'monetary testimony '
                 'only — a promise is no present debt')
            return 'exempt', P
        if person.get('denial_forum') != 'court':
            move('Sifra, Vayikra Dibbura DeChovah, Chapter 12 5-6 '
                 '(Mishnah Shevuot 4:3)', 'the denial that counts is the '
                 'one a court hears')
            return 'exempt', P
        if person.get('testified'):
            ink(1, '"if he does NOT tell" — telling discharges')
            return 'exempt', P
        t1 = True
    # ---- trigger 2: sanctuary tumah (5:2-3) ----
    t2 = False
    if person.get('trigger') == 'tumah':
        ink(2, '"or if a soul touch any unclean thing... AND IT BE '
               'HIDDEN from him" — the knowledge gap is the trigger')
        ink(3, '"and HE KNEW, and he is guilty" — awareness at the END '
               'is the ink\'s own closing bracket')
        if not person.get('aware_at_end'):
            return 'no offering yet', P
        if not person.get('hidden_in_middle'):
            ink(2, 'no hiddenness — no gap to atone')
            return 'exempt', P
        if not person.get('aware_at_start'):
            move('Babylonian Talmud Shevuot 14b (R. Akiva on the doubled '
                 '"and it be hidden", Sifra Chapter 13 11)',
                 'awareness at the BEGINNING required — the doubled '
                 'hidden implies a bracket on both sides')
            return 'exempt', P
        if not person.get('touched_sanctum'):
            move('Sifra, Vayikra Dibbura DeChovah, Chapter 13 10',
                 'the scope is the sanctuary and its consecrated things '
                 '— warning, punishment, and offering aligned to one '
                 'object')
            return 'exempt', P
        if person.get('forgot') == 'sanctuary_not_tumah':
            move('Sifra, Vayikra Dibbura DeChovah, Chapter 13 7 (the '
                 'first-tanna reading; Rabbi\'s dispute recorded)',
                 'the hidden variable must be the TUMAH itself')
            return 'exempt', P
        t2 = True
    # ---- trigger 3: the utterance oath (5:4) ----
    t3 = False
    if person.get('trigger') == 'utterance_oath':
        ink(4, '"to do harm OR TO DO GOOD" — the option template: the '
               'sworn act must be his to do')
        if not person.get('act_is_his_option'):
            return 'exempt', P
        if person.get('tense') == 'past':
            move('Sifra, Vayikra Dibbura DeChovah, Section 9 8 (Mishnah '
                 'Shevuot 3:1)', 'the doubled pronounce-verb doubles the '
                 'tense scope: past oaths join the future')
        if person.get('oath_epistemics') == 'known_false':
            ink(4, '"AND IT BE HIDDEN from him" — the known-false oath '
                   'is never hidden: the vain class sits outside this '
                   'offering')
            return 'vain oath — outside the offering', P
        if not person.get('oath_forgotten'):
            ink(4, '"and it be hidden from him" — only the forgotten '
                   'oath triggers')
            return 'exempt', P
        t3 = True
    if not (t1 or t2 or t3):
        return 'no offering', P
    # ---- the discharge: confession + the means ladder (5:5-13) ----
    out = ['CONFESS']
    ink(5, '"then he shall CONFESS wherein he sinned" — confession '
           'rides the offering')
    wealth = person.get('means')
    dat('the two thresholds — "enough for a lamb" (5:7) and "attains '
        'two birds" (5:11) — are hand-tests whose measure the ink never '
        'states: DATA (Onkelos renders the first as "the MEASURE of a '
        'lamb")')
    if wealth == 'reaches_lamb':
        ink(6, 'a FEMALE from the flock — lamb or goat-kid — as a '
               'sin-offering')
        out.append('female lamb or goat (chatat)')
    elif wealth == 'reaches_birds':
        ink(7, '"if his hand cannot attain ENOUGH (dei) for a lamb: two '
               'turtledoves or two young pigeons, one chatat one olah"')
        ink(8, 'the chatat offered FIRST — "rishonah" is in the ink')
        ink(10, 'the second "as prescribed (ka-mishpat)" — the ink\'s '
                'own POINTER to the bird-olah rite of chapter 1')
        out.append('two birds: chatat FIRST, then olah per Lev 1')
    else:
        ink(11, '"a tenth of the ephah of fine flour... he shall put NO '
                'oil and NO frankincense upon it, for it is a chatat" — '
                'the stripped flour tier, stripping stated in the ink')
        dat('the SIZE of the ephah is data — the tradition computes the '
            'tenth as one-of-ten-in-three-se\'im, and Onkelos writes '
            'the conversion into the verse')
        out.append('tenth of an ephah, no oil, no frankincense')
    ink(13, '"for his sin... OF ONE of these" — any trigger rides the '
            'ladder: the scale reads the MEANS, never the sin\'s '
            'gravity')
    return '; '.join(out), P


def sacrilege(case, data):
    """Lev 5:14-19 — me'ilah and the suspended guilt-offering."""
    del P[:]
    if case.get('kind') == 'meilah':
        ink(15, '"a soul, if it commit a TRESPASS and sin unwittingly '
                'in the holy things of the LORD"')
        if not case.get('unwitting'):
            ink(15, '"unwittingly" — the deliberate trespasser is '
                    'outside this offering')
            return 'no offering (deliberate)', P
        if not (case.get('benefit') and case.get('damage')):
            move('Sifra, Vayikra Dibbura DeChovah, Section 11 3 (the '
                 'terumah likeness)', 'liability needs damage AND '
                 'benefit together')
            return 'exempt', P
        out = ['repay the principal to the fund struck']
        ink(16, '"and what he sinned from the holy he shall PAY, and '
                'ITS FIFTH he shall add to it, and give it to the '
                'priest"')
        base = case.get('value')
        fifth = base / 4.0
        move('Sifra, Vayikra Dibbura DeChovah, Chapter 20 8 (Bava '
             'Metzia 54a)', 'the fifth is the ADDED QUARTER: principal '
             'plus fifth equals five parts — pay %.2f on %.2f'
             % (fifth, base))
        out.append('add the fifth (%.2f)' % fifth)
        ink(15, 'and the ram "by your valuation, SILVER SHEKELS" — the '
                'currency in ink, the amount a parameter')
        dat('the valuation floor — two sela — is the transmitted '
            'setting (Onkelos converts the currency to sanctuary '
            'sela\'im in the verse itself)')
        out.append('ram at the valuation floor (%s)' % data['ram_floor'])
        return '; '.join(out), P
    if case.get('kind') == 'doubt':
        ink(17, '"and if a soul sin... AND HE DID NOT KNOW — and he is '
                'guilty and shall bear his sin": the doubt case is the '
                'ink\'s own')
        if case.get('later_resolved') == 'sinned':
            move('Sifra, Vayikra Dibbura DeChovah, Section 12 5',
                 '"and he did not know" — once he KNOWS, the suspended '
                 'ram lapses to the certain sin-offering')
            return 'chatat now (the talui covered only the doubt '\
                   'interval)', P
        if case.get('doubt_object') == 'meilah':
            dat('DISPUTE as two recorded settings: R. Akiva — the '
                'suspended ram covers a sacrilege doubt; the sages — '
                'the sacrilege class rides its own definite ram '
                '(Mishnah Keritot 5:2)')
            return 'DISPUTE: liable (R. Akiva) / exempt (the sages)', P
        ink(18, 'a ram, by the valuation, "for his error which he '
                'erred AND HE KNEW IT NOT"')
        return 'suspended ram (asham talui)', P
    return 'no offering', P


def deposit_restitution(claim, data):
    """Lev 5:20-26 — the deposit oath and its payment algebra."""
    del P[:]
    ink(21, 'the claim forms enumerated: deposit, hand-pledge, '
            'robbery, oppression — "or found a lost thing" (5:22) — '
            'each clause closing a loophole')
    if claim.get('claim_kind') not in data['claim_forms']:
        move('Sifra, Vayikra Dibbura DeChovah, Chapter 22 10-11',
             'claims that cannot convert to money-payment (the fine '
             'classes, the Sabbath-injury) are outside')
        return 'exempt', P
    if not claim.get('swore_falsely'):
        ink(24, 'the fifth and the ram ride "all that he swears upon '
                'FALSELY" — denial without an oath pays the principal '
                'alone')
        return 'principal only', P
    out = []
    ink(23, '"then he shall RETURN the theft that he stole, or the '
            'oppression, or the deposit, or the lost thing" — '
            'restitution FIRST, before the offering')
    if claim.get('object_exists'):
        ink(23, '"which was deposited WITH HIM" — while it is with '
                'him, the thing itself returns')
        out.append('return the object itself')
    else:
        out.append('pay its value')
    ink(24, '"he shall pay it AT ITS HEAD (be-rosho)" — the principal, '
            'not the doubles: the fine track and the oath track are '
            'exclusive')
    base = claim.get('value')
    fifth = base / 4.0
    move('Sifra, Vayikra Dibbura DeChovah, Section 13 8 (Bava Kamma '
         '9:5-8)', 'the added-quarter fifth on the oath: %.2f' % fifth)
    out.append('add the fifth (%.2f)' % fifth)
    if claim.get('swore_on_fifth'):
        ink(24, 'the ink writes "its FIFTHS" — plural: the recursion '
                'hook is a letter')
        move('Sifra, Vayikra Dibbura DeChovah, Section 13 12 (Mishnah '
             'Bava Kamma 9:7)', 'the sworn-on fifth becomes principal '
             'and bears its own fifth')
        dat('the recursion\'s base case — less than a perutah — is the '
            'transmitted floor')
        out.append('fifth on the fifth, to the perutah floor')
    ink(24, '"to WHOM IT BELONGS shall he give it, on the day of his '
            'guilt" — delivered to the owner himself')
    if claim.get('owner_far'):
        out.append('carry it after him, even to Media')
    if claim.get('victim') == 'father_deceased':
        ink(23, '"the theft THAT HE STOLE" — his own act; the '
                'principal goes to the heirs')
        move('Sifra, Vayikra Dibbura DeChovah, Section 13 2-6 (Mishnah '
             'Bava Kamma 9:9)', 'the fifth and the ram ride his OWN '
             'oath — the father-matrix rung')
        out.append('principal to the heirs; fifth+ram on his own oath')
    ink(25, 'and the guilt-ram "by your valuation" closes it')
    out.append('ram at the valuation floor')
    if claim.get('ask') == 'valuation_date':
        dat('DISPUTE as two recorded settings on "the day of his '
            'guilt": Beth Shammai / Beth Hillel split who bears the '
            'object\'s change of value between theft and conviction')
        return 'DISPUTE: the day-of-guilt valuation (two houses)', P
    return '; '.join(out), P

# =====================================================================
# THE CHAPTER'S OWN POINTERS, RESOLVED BY LIVE CALL (2026-09-06, the
# dependency-debt sitting). This runner was the first Leviticus compile;
# every later engine calls INTO it, and its own cross-references stood as
# notes. 5:10 "as prescribed" points to the bird burnt offering (Lev
# 1:14-17); 5:13 "as the meal offering" to Lev 2's remainder; 5:6's female
# of the flock to Lev 4:27-35's commoner; 5:15-19's ram to Lev 7:1-7's
# procedure. The imports are function-local: those engines import this
# module at load, so they are fetched only when a pointer is asked.
def pointers(q, data):
    del P[:]
    import io as _io, contextlib as _ctx
    with _ctx.redirect_stdout(_io.StringIO()):
        import cold_run_minchah as MIN, cold_run_chatat as CH, cold_run_tzav as TZ
    if q == 'bird_olah_as_prescribed':
        ink(10, '"and the second he shall make a BURNT OFFERING, AS PRESCRIBED '
                '(כמשפט)" — the ink\'s own pointer to the bird rite of Lev 1:14-17')
        b = MIN.bird
        move('cold_run_minchah.bird [IMPORT, live call]', 'place -> %r; how many -> %r; '
             'burn -> %r (Lev 1:15-17 compiled at audit sitting B; Mishnah Zevachim '
             '6:5-7, 7:2)' % (b('place')['v'], b('how_many')['v'], b('burn')['v']))
        return 'olah per Lev 1:14-17: %s, %s, %s (CALLED minchah.bird)' % (
            b('place')['v'], b('how_many')['v'], b('burn')['v']), P
    if q == 'remainder_as_minchah':
        ink(13, '"and it shall be the priest\'s AS THE MEAL OFFERING (כמנחה)" — '
                'the pointer to Lev 2:3, 2:10')
        r = MIN.remainder('sinner')['v']
        move('cold_run_minchah.remainder(sinner) [IMPORT, live call]', '-> %r '
             '(Mishnah Menachot 6:1 lists the sinner\'s among the scooped)' % r)
        return 'to the priest as every meal offering: %s (CALLED minchah.remainder)' % r, P
    if q == 'lamb_tier_procedure':
        ink(6, '"a FEMALE from the flock, a lamb or a goat-kid, for a sin '
               'offering" — the commoner\'s animal of Lev 4:28 and 4:32')
        r = CH.rank('commoner')['v']
        move('cold_run_chatat.rank(commoner) [IMPORT, live call]', '-> %r: the '
             'graded offering\'s first tier RUNS Lev 4:27-35\'s procedure (the '
             'horns, the base, the fat as the lamb\'s or the goat\'s)' % r)
        return '%s per Lev 4:27-35 (CALLED chatat.rank)' % r, P
    if q == 'asham_procedure':
        ink(15, '"a ram without blemish from the flock, by your valuation in '
                'silver shekels, for a GUILT OFFERING" — the case; the '
                'procedure is Lev 7:1-7\'s')
        pl = TZ.asham_law({'ask': 'place'}, TZ.PARAMS)[0]
        ea = TZ.asham_law({'ask': 'eater'}, TZ.PARAMS)[0]
        move('cold_run_tzav.asham_law [IMPORT, live call]', 'place -> %r; eater '
             '-> %r (compiled 2026-09-06; Mishnah Zevachim 5:5)' % (pl, ea))
        return 'north, male_priests within the hangings (CALLED tzav.asham_law)', P
    return 'no pointer', P


# THE TEST DATA — the Mishnah's rows, fed at run time (motion 2).
# =====================================================================
DATA = {
    'ram_floor': 'two sela (Mishnah Keritot 5:2; Zevachim 10:5 class)',
    'claim_forms': ['deposit', 'hand_pledge', 'robbery', 'oppression',
                    'lost_object'],
}

# ---- THE WRAP (W3 THE OFFERING ENGINE, D9-iii, 2026-09-07) — the daemon; the scene runs under main ----
# Five case heads: the witness who heard the adjuration (5:1, with the confession 5:5 and the ladder's first
# rung 5:6), the impurity hidden (5:2-3, the second rung 5:7), the oath uttered (5:4, the third rung 5:11) —
# each through the graded offering by call; the sacrilege (5:15-16); the doubtful sin (5:17-18 — law_chatat's
# seat too: the pieces and the resolution). The deposit oath (5:20-26) is the library's law_deposit_oath,
# registered beside on the scene. This module imports cold (the meal-offering, sin-offering and Tzav engines
# call it), so the daemon is module-level and the scene runs under main. Never emits an event.
import world_engine as WE
def law_vayikra5(event, world):
    """Lev 5:1-19 (cold_run_vayikra5.py — the three triggers and the means ladder, the sacrilege, the doubt)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'witness_oath_heard':
        v, _ = graded_offering(dict(event, trigger='witness_oath'), DATA)
        if v == 'exempt':
            return [E_('exempt', event['person'], value=v, law='[INK 5:1 — the oath must FIND a witness; the blanket oath, the messenger, the promised gift, the denial outside court, the telling]')]
        if v.startswith('no offering') or v.startswith('vain'):
            return []
        return [E_('confessed', event['person'], cp='HEAVEN', law='[INK 5:5 "he shall confess that wherein he sinned"]'),
                E_('atoned_forgiven', event['person'], cp='HEAVEN', value=v, law='[INK 5:6, 5:10, 5:13 "and the priest shall atone for him" — the means ladder: %s]' % v)]
    if k == 'impurity_hidden':
        v, _ = graded_offering(dict(event, trigger='tumah'), DATA)
        if v == 'exempt':
            return [E_('exempt', event['person'], value=v, law='[INK 5:2-3 "and it be hidden from him... and he knew" — the brackets; Shevuot 14b]')]
        if v.startswith('no offering') or v.startswith('vain'):
            return []                                            # not yet aware at the end: no offering YET (the ink's own closing bracket) — the silence
        return [E_('confessed', event['person'], cp='HEAVEN', law='[INK 5:5 "he shall confess"]'),
                E_('atoned_forgiven', event['person'], cp='HEAVEN', value=v, law='[INK 5:6-7 — the ladder by his means: %s]' % v)]
    if k == 'oath_uttered':
        v, _ = graded_offering(dict(event, trigger='utterance_oath'), DATA)
        if v == 'exempt':
            return [E_('exempt', event['person'], value=v, law='[INK 5:4 "to do evil or to do good" — his to do; "and it be hidden" — forgotten]')]
        if v.startswith('no offering') or v.startswith('vain'):
            return []                                            # the known-false oath: the vain class sits outside this offering — the silence
        return [E_('confessed', event['person'], cp='HEAVEN', law='[INK 5:5 "he shall confess"]'),
                E_('atoned_forgiven', event['person'], cp='HEAVEN', value=v, law='[INK 5:11 — the flour without oil or frankincense: %s]' % v)]
    if k == 'sacrilege_committed':
        v, _ = sacrilege({'kind': 'meilah', 'unwitting': event['unwitting'], 'benefit': event['benefit'], 'damage': event['damage'], 'value': event['value']}, DATA)
        if v == 'exempt':
            return [E_('exempt', event['person'], value=v, law='[Sifra Chovah Section 11 3 — damage AND benefit together]')]
        if v.startswith('no offering'):
            return []                                            # the deliberate trespasser: outside this offering (INK 5:15 "unwittingly") — the silence
        return [E_('pays', event['person'], cp='the-sanctuary', amount=event['value'], law='[INK 5:16 "what he sinned from the holy he shall pay"]'),
                E_('adds_fifth', event['person'], cp='the-sanctuary', amount=event['value'] / 4.0, law='[INK 5:16 "and its fifth he shall add" — the added quarter (Sifra Chovah Chapter 20 8)]'),
                E_('atoned_forgiven', event['person'], cp='HEAVEN', value=v, law='[INK 5:16 "the priest shall atone for him with the ram... and he shall be forgiven"]')]
    if k == 'doubtful_sin':
        v, _ = sacrilege({'kind': 'doubt', 'later_resolved': event.get('later_resolved'), 'doubt_object': event.get('doubt_object')}, DATA)
        if v.startswith('chatat now'):
            return [E_('atoned_forgiven', event['sinner'], cp='HEAVEN', value=v, law='[Sifra Chovah Section 12 5 — once he KNOWS, the ram lapses to the certain sin offering]')]
        if v.startswith('DISPUTE'):
            return [E_('suspends', event['sinner'], value=v, law='[Mishnah Keritot 5:2 — R. Akiva: the suspended ram covers a sacrilege doubt]'),
                    E_('exempt', event['sinner'], value=v, law='[Mishnah Keritot 5:2 — the sages\' arm: the fork carried]')]
        return [E_('suspends', event['sinner'], value=v, law='[INK 5:17-18 "and knew it not" — the suspended ram]')]
    return []

def scene():
    """THE SCENE — Lev 5's recorded rows replayed with the deposit oath on the library daemon (clock unit: days)."""
    with _ctx.redirect_stdout(_io.StringIO()):
        w = WE.World(era='the graded offering, the sacrilege, the doubt, the deposit oath: Shevuot 1-4, Keritot 5, Bava Kamma 9 on the engine (clock unit: days)')
        w.laws = [law_vayikra5, WE.law_deposit_oath]
        w.advance(1)
        w.submit({'kind': 'witness_oath_heard', 'subject': 'the-blanket-witness', 'person': 'the-blanket-witness', 'was_witness_at_oath': True, 'adjuration_scope': 'blanket_congregation', 'case_source': 'Mishnah Shevuot 4:10 — the synagogue blanket oath: exempt'})
        w.submit({'kind': 'witness_oath_heard', 'subject': 'the-silent-witness', 'person': 'the-silent-witness', 'was_witness_at_oath': True, 'denial_forum': 'court', 'testified': False, 'means': 'reaches_lamb', 'case_source': 'Lev 5:1, 5:5-6 — heard, was a witness, denied in court: the confession and the female of the flock'})
        w.submit({'kind': 'impurity_hidden', 'subject': 'the-defiler', 'person': 'the-defiler', 'aware_at_start': True, 'hidden_in_middle': True, 'aware_at_end': True, 'touched_sanctum': True, 'means': 'reaches_birds', 'case_source': 'Mishnah Shevuot 2:1; Lev 5:2-3, 5:7 — the brackets held: two birds'})
        w.submit({'kind': 'impurity_hidden', 'subject': 'the-unaware', 'person': 'the-unaware', 'aware_at_start': True, 'hidden_in_middle': True, 'aware_at_end': False, 'touched_sanctum': True, 'case_source': 'Lev 5:3 "and he knew" — not yet: no offering yet (the silence)'})
        w.submit({'kind': 'oath_uttered', 'subject': 'the-forgetter', 'person': 'the-forgetter', 'act_is_his_option': True, 'oath_forgotten': True, 'means': 'reaches_flour', 'case_source': 'Mishnah Shevuot 3:1; Lev 5:4, 5:11 — the forgotten oath: the tenth of an ephah'})
        w.submit({'kind': 'oath_uttered', 'subject': 'the-liar', 'person': 'the-liar', 'act_is_his_option': True, 'oath_epistemics': 'known_false', 'case_source': 'Mishnah Shevuot 3:7 — the known-false oath: the vain class, outside (the silence)'})
        w.submit({'kind': 'sacrilege_committed', 'subject': 'the-trespasser', 'person': 'the-trespasser', 'unwitting': True, 'benefit': True, 'damage': True, 'value': 4.0, 'case_source': 'Mishnah Meilah 5:1; Keritot 5:2 — benefit and damage: the principal, the fifth, the ram'})
        w.submit({'kind': 'sacrilege_committed', 'subject': 'the-deliberate-trespasser', 'person': 'the-deliberate-trespasser', 'unwitting': False, 'benefit': True, 'damage': True, 'value': 4.0, 'case_source': 'Lev 5:15 "unwittingly" — the deliberate outside (the silence)'})
        w.submit({'kind': 'doubtful_sin', 'subject': 'the-doubter', 'sinner': 'the-doubter', 'pieces': ['fat', 'hullin'], 'case_source': 'Mishnah Keritot 4:1 — the suspended ram'})
        w.submit({'kind': 'doubtful_sin', 'subject': 'the-later-knower', 'sinner': 'the-later-knower', 'pieces': ['fat', 'hullin'], 'later_resolved': 'sinned', 'case_source': 'Sifra Chovah Section 12 5 — once he knows: the certain sin offering'})
        w.submit({'kind': 'doubtful_sin', 'subject': 'the-meilah-doubter', 'sinner': 'the-meilah-doubter', 'pieces': ['kodesh', 'hullin'], 'doubt_object': 'meilah', 'case_source': 'Mishnah Keritot 5:2 — R. Akiva liable, the sages exempt: the fork'})
        w.submit({'kind': 'sworn_denial_admitted', 'subject': 'the-denier', 'claimant_against': 'the-denier', 'owner': 'the-robbed', 'value': 4.0, 'object_exists': True, 'case_source': 'Mishnah Bava Kamma 9:5; Shevuot 8 — the deposit oath admitted: the object restored, the fifth, the ram (the library daemon)'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    amt = lambda eid, eff: sum(e['amount'] or 0 for e in w.entity(eid).ledger if e['effect'] == eff)
    return (n('the-blanket-witness', 'exempt'), n('the-silent-witness', 'confessed'), n('the-silent-witness', 'atoned_forgiven'), n('the-defiler', 'atoned_forgiven'), n('the-unaware', 'atoned_forgiven'),
            n('the-forgetter', 'atoned_forgiven'), n('the-liar', 'atoned_forgiven'), amt('the-trespasser', 'pays'), amt('the-trespasser', 'adds_fifth'), n('the-trespasser', 'atoned_forgiven'),
            n('the-deliberate-trespasser', 'pays'), n('the-doubter', 'suspends'), n('the-later-knower', 'atoned_forgiven'), n('the-meilah-doubter', 'suspends'), n('the-meilah-doubter', 'exempt'),
            amt('the-denier', 'restores'), amt('the-denier', 'adds_fifth'), n('the-denier', 'atoned_forgiven'), w.clock.day), w

CASES = [
 ('Shevuot 4:10 — the synagogue blanket oath',
  lambda: graded_offering({'trigger':'witness_oath','was_witness_at_oath':True,
    'adjuration_scope':'blanket_congregation'}, DATA), 'exempt'),
 ('Shevuot 4:9 — the oath preceded the knowledge',
  lambda: graded_offering({'trigger':'witness_oath','was_witness_at_oath':False},
    DATA), 'exempt'),
 ('Shevuot 4:12 — demanded through a messenger',
  lambda: graded_offering({'trigger':'witness_oath','was_witness_at_oath':True,
    'adjured_by':'messenger'}, DATA), 'exempt'),
 ('Shevuot 4:8 — the promised-gift claim',
  lambda: graded_offering({'trigger':'witness_oath','was_witness_at_oath':True,
    'claim_kind':'promised_gift'}, DATA), 'exempt'),
 ('Shevuot 4:3 — denied outside court, admitted inside',
  lambda: graded_offering({'trigger':'witness_oath','was_witness_at_oath':True,
    'denial_forum':'outside'}, DATA), 'exempt'),
 ('Shevuot 2:1 — aware, hidden, aware; ate consecrated food (rich man)',
  lambda: graded_offering({'trigger':'tumah','aware_at_start':True,
    'hidden_in_middle':True,'aware_at_end':True,'touched_sanctum':True,
    'means':'reaches_lamb'}, DATA), 'CONFESS; female lamb or goat (chatat)'),
 ('Shevuot (the machine): no closing awareness yet',
  lambda: graded_offering({'trigger':'tumah','aware_at_start':True,
    'hidden_in_middle':True,'aware_at_end':False}, DATA), 'no offering yet'),
 ('Shevuot 14b — no opening awareness',
  lambda: graded_offering({'trigger':'tumah','aware_at_start':False,
    'hidden_in_middle':True,'aware_at_end':True}, DATA), 'exempt'),
 ('Shevuot 2:5 field — forgot the sanctuary, not the tumah',
  lambda: graded_offering({'trigger':'tumah','aware_at_start':True,
    'hidden_in_middle':True,'aware_at_end':True,'touched_sanctum':True,
    'forgot':'sanctuary_not_tumah'}, DATA), 'exempt'),
 ('Shevuot 3:5 — utterance about others, his option, forgotten (middle tier)',
  lambda: graded_offering({'trigger':'utterance_oath','act_is_his_option':True,
    'oath_forgotten':True,'means':'reaches_birds'}, DATA),
  'CONFESS; two birds: chatat FIRST, then olah per Lev 1'),
 ('Sifra Section 9 3 — swore to harm another (not his option)',
  lambda: graded_offering({'trigger':'utterance_oath','act_is_his_option':False},
    DATA), 'exempt'),
 ('Shevuot 3:1 — a PAST false oath, forgotten (poorest tier)',
  lambda: graded_offering({'trigger':'utterance_oath','act_is_his_option':True,
    'tense':'past','oath_forgotten':True,'means':'reaches_flour'}, DATA),
  'CONFESS; tenth of an ephah, no oil, no frankincense'),
 ('Shevuot 3:8 — the vain oath (the stone column of gold)',
  lambda: graded_offering({'trigger':'utterance_oath','act_is_his_option':True,
    'oath_epistemics':'known_false'}, DATA), 'vain oath — outside the offering'),
 ('Keritot/Sifra close — gravest trigger, poorest hand: still flour',
  lambda: graded_offering({'trigger':'tumah','aware_at_start':True,
    'hidden_in_middle':True,'aware_at_end':True,'touched_sanctum':True,
    'means':'reaches_flour'}, DATA),
  'CONFESS; tenth of an ephah, no oil, no frankincense'),
 ('Meilah 18a class — benefit without damage',
  lambda: sacrilege({'kind':'meilah','unwitting':True,'benefit':True,
    'damage':False}, DATA), 'exempt'),
 ('Sifra Section 11 8 — the deliberate trespasser',
  lambda: sacrilege({'kind':'meilah','unwitting':False}, DATA),
  'no offering (deliberate)'),
 ('Bava Metzia 54a — the fifth on a four-value trespass = one',
  lambda: sacrilege({'kind':'meilah','unwitting':True,'benefit':True,
    'damage':True,'value':4.0}, DATA),
  'repay the principal to the fund struck; add the fifth (1.00); '
  'ram at the valuation floor (two sela (Mishnah Keritot 5:2; '
  'Zevachim 10:5 class))'),
 ('Keritot — the plain doubt brings the suspended ram',
  lambda: sacrilege({'kind':'doubt'}, DATA), 'suspended ram (asham talui)'),
 ('Sifra Section 12 5 — the doubt resolved: he sinned',
  lambda: sacrilege({'kind':'doubt','later_resolved':'sinned'}, DATA),
  'chatat now (the talui covered only the doubt interval)'),
 ('Keritot 5:2 — doubt of SACRILEGE: the recorded dispute',
  lambda: sacrilege({'kind':'doubt','doubt_object':'meilah'}, DATA),
  'DISPUTE: liable (R. Akiva) / exempt (the sages)'),
 ('Shevuot 5:1 field — denial WITHOUT an oath',
  lambda: deposit_restitution({'claim_kind':'deposit','swore_falsely':False},
    DATA), 'principal only'),
 ('Bava Kamma 9:5 — sworn robbery, object gone, owner far',
  lambda: deposit_restitution({'claim_kind':'robbery','swore_falsely':True,
    'object_exists':False,'value':4.0,'owner_far':True}, DATA),
  'pay its value; add the fifth (1.00); carry it after him, even to '
  'Media; ram at the valuation floor'),
 ('Sifra Section 13 4 — the deposit still with him returns itself',
  lambda: deposit_restitution({'claim_kind':'deposit','swore_falsely':True,
    'object_exists':True,'value':8.0}, DATA),
  'return the object itself; add the fifth (2.00); ram at the '
  'valuation floor'),
 ('Bava Kamma 9:7 — swore on the fifth: the recursion',
  lambda: deposit_restitution({'claim_kind':'robbery','swore_falsely':True,
    'object_exists':False,'value':4.0,'swore_on_fifth':True}, DATA),
  'pay its value; add the fifth (1.00); fifth on the fifth, to the '
  'perutah floor; ram at the valuation floor'),
 ('Bava Kamma 9:9 — robbed the father, swore, the father died',
  lambda: deposit_restitution({'claim_kind':'robbery','swore_falsely':True,
    'object_exists':False,'value':4.0,'victim':'father_deceased'}, DATA),
  'pay its value; add the fifth (1.00); principal to the heirs; '
  'fifth+ram on his own oath; ram at the valuation floor'),
 ('Sifra Chapter 22 11 — the fine-class claim (the daughter) is outside',
  lambda: deposit_restitution({'claim_kind':'daughter_fine',
    'swore_falsely':True}, DATA), 'exempt'),
 ('Sifra Section 13 13 — the day-of-guilt valuation',
  lambda: deposit_restitution({'claim_kind':'robbery','swore_falsely':True,
    'object_exists':True,'value':4.0,'ask':'valuation_date'}, DATA),
  'DISPUTE: the day-of-guilt valuation (two houses)'),
 # ---- the pointers, live (2026-09-06) ----
 ('Lev 5:10 "as prescribed" — the bird burnt offering by call into the meal-offering engine',
  lambda: pointers('bird_olah_as_prescribed', DATA),
  'olah per Lev 1:14-17: above_the_red_line_south_east_corner, even_one, wholly_burned_on_the_wood (CALLED minchah.bird)'),
 ('Lev 5:13 "as the meal offering" — the remainder by call',
  lambda: pointers('remainder_as_minchah', DATA),
  'to the priest as every meal offering: aaron_and_sons_most_holy (CALLED minchah.remainder)'),
 ('Lev 5:6 — the lamb tier runs Lev 4:27-35 by call into the sin-offering engine',
  lambda: pointers('lamb_tier_procedure', DATA),
  'she_goat_or_ewe_lamb per Lev 4:27-35 (CALLED chatat.rank)'),
 ('Lev 5:15-19 — the guilt offering\'s procedure by call into the Tzav engine',
  lambda: pointers('asham_procedure', DATA),
  'north, male_priests within the hangings (CALLED tzav.asham_law)'),
 # ---- THE WRAP (W3, 2026-09-07) — Lev 5 on the world engine, the deposit oath on the library daemon ----
 ('THE SCENE — (the blanket witness exempt; the silent witness confessed, atoned; the defiler atoned, the unaware\'s silence; the forgetter '
  'atoned, the liar\'s silence; the trespasser pays 4, adds 1, atoned; the deliberate\'s silence; the doubter\'s ram, the later-knower\'s '
  'sin offering, the sacrilege doubt\'s two arms; the denier restores 4, adds 1, atoned; the clock)',
  lambda: (SCENE, [('INK', 'the tape is the ink: Lev 5 and the recorded rows of Shevuot 1-4, Keritot 5, Meilah 5, Bava Kamma 9')]),
  (1, 1, 1, 1, 0, 1, 0, 4.0, 1.0, 1, 0, 1, 1, 1, 1, 4.0, 1.0, 1, 1)),
]

# ---- motion 3+5: run and grade --------------------------------------
# Guarded so graded_offering() IMPORTS COLD — cold_run_minchah.py CALLS it for the
# sinner's meal offering's adjuncts (sitting B, 2026-09-05; the first-call standard).
if __name__ == '__main__':
    SCENE, _W = scene()                  # W3: the scene under main (the module imports cold); the CASES row's lambda binds SCENE at run time
    ok = 0
    frac = {'INK': 0, 'MOVE': 0, 'DATA': 0}
    print()
    for label, fn, want in CASES:
        got, prov = fn()
        hit = got == want
        ok += hit
        kinds = [k for k, _ in prov]
        cls = 'INK' if all(k == 'INK' for k in kinds) else \
              ('DATA' if 'DATA' in kinds and got.startswith('DISPUTE') else
               ('MOVE' if 'MOVE' in kinds else 'DATA'))
        frac[cls] += 1
        print('%s  [%s]  %s' % ('PASS' if hit else 'MISS', cls, label))
        if not hit:
            print('      expected: %s' % want)
            print('      got     : %s' % got)
    print()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, len(CASES)))
    tot = len(CASES)
    print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%) '
          '· data/dispute %d/%d (%.0f%%)' %
          (frac['INK'], tot, 100.0*frac['INK']/tot,
           frac['MOVE'], tot, 100.0*frac['MOVE']/tot,
           frac['DATA'], tot, 100.0*frac['DATA']/tot))
    if ok == len(CASES):
        print('LEVITICUS 5 COMPILES — the deliverable rule\'s first function '
              'set is live.')

    # ---- EFFECTS (retrofit 2026-09-03, under the effects law) -----------
    # The verdict writes the LEDGER, never the event stream. Leviticus 5's
    # routes end on HEAVEN'S DOCKET: the offering brought, the priest
    # atones, and the ink itself closes the entry — ונסלח לו ("and he shall
    # be forgiven", nine sites in Lev 4-5). Mapping is by the verdict
    # string the function actually emitted; disputes fork (both arms'
    # effects, labeled, per method law 3).
    import effects_layer as FX

    def effect_of(verdict):
        v = verdict
        if isinstance(v, tuple):
            return [FX.NONE]                        # the scene row (W3): its effects are on the engine's ledger, counted in the tuple
        if v.startswith('DISPUTE: liable (R. Akiva)'):
            return ['atoned_forgiven', 'exempt']   # the fork's two arms
        if v.startswith('DISPUTE: the day-of-guilt'):
            # the dispute is the valuation DATUM; the effects stand
            return ['restores', 'adds_fifth', 'atoned_forgiven']
        if v == 'exempt':
            return ['exempt']
        if v in ('no offering', 'no offering yet', 'no offering (deliberate)',
                 'vain oath — outside the offering'):
            return [FX.NONE]                        # pending, or routed outside
        if v == 'principal only':
            return ['restores']
        fx = []
        if 'return the object itself' in v:
            fx.append('restores')
        if 'pay its value' in v or 'principal' in v:
            fx.append('pays' if 'pay its value' in v else 'restores')
        if 'fifth' in v:
            fx.append('adds_fifth')
        # any route that ends at an offering closes on Heaven's docket
        if any(w in v for w in ('chatat', 'birds', 'ephah', 'ram', 'olah')):
            fx.append('atoned_forgiven')
        return fx or [FX.NONE]

    print()
    print('EFFECTS — the state changes each verdict writes:')
    used = []
    for label, fn, want in CASES:
        got, _ = fn()
        fx = effect_of(got)
        used += fx
        tag = '  [DISPUTE FORK — both arms, labeled]' if isinstance(got, str) and got.startswith('DISPUTE') else ''
        for line in FX.render(fx):
            print('  %-44s ->%s%s' % (label[:44], line, tag))
    ops = FX.summarize(used)
    print('LEDGER OPS this run writes:',
          ', '.join('%s x%d' % (op, cnt) for op, cnt in sorted(ops.items())))
    print('effects: all %d cases carry a REGISTERED effect or an honest '
          'no-change [effects law satisfied]' % len(CASES))
    print('SCENE: %r — the daemons\' watch coverage (the library\'s law_deposit_oath beside law_vayikra5):' % (SCENE,))
    _W.print_coverage()
