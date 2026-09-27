import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 17b (2026-09-26): THE CALLEES' FACTS, third pass — the family, joseph, exodus_story, balak, primeval and naso cells (the asks typed from the keys
# print), the mishpatim runners' module-level tables named, the tape's lines at Numbers 15 and Leviticus 19; every value by repr. RUN FROM THE REPO ROOT.
import os, sys, io, re, contextlib, subprocess, inspect
ROOT = _ROOT; sys.path.insert(0, ROOT + '/World/step9')
def load(name):
    with contextlib.redirect_stdout(io.StringIO()):
        return __import__('cold_run_' + name)
M = {}
def show(label, fn):
    try:
        v = fn(); print('FACT %s = %r' % (label, v))
    except Exception as ex:
        print('FAIL %s: %s: %s' % (label, type(ex).__name__, str(ex)[:200]))
def fmt(c): return (c.get('v'), c.get('p'), c.get('fx'), str(c.get('why', ''))[:300]) if isinstance(c, dict) and 'v' in c else (str(c)[:500] if not isinstance(c, dict) else {kk: str(t)[:200] for kk, t in c.items()})
def q(n, name, keys):
    if n not in M: M[n] = load(n)
    fn = getattr(M[n], name)
    for k in keys: show('%s.%s(%s)' % (n, name, k), lambda k=k: fmt(fn(k)))
def c(n, name, asks, **fields):
    if n not in M: M[n] = load(n)
    fn = getattr(M[n], name); D = getattr(M[n], 'DATA', {})
    for a in asks: show('%s.%s(%s%s)' % (n, name, a, (', ' + str(fields)) if fields else ''), lambda a=a: (lambda v: v[:2] if isinstance(v, (list, tuple)) else fmt(v))(fn(dict(ask=a, **fields), D)))
q('family', 'commission', ['naar_ketiv', 'girl_vs_maiden', 'virgin_two_predicates', 'bride_price_by_call', 'wife_taken_sinai_seat', 'marriage_formula', 'bride_year', 'days_or_ten', 'father_takes_for_the_son', 'her_consent', 'their_consent', 'handover_domain', 'gifts_two_moments', 'sivlonot'])
q('family', 'inheritance', ['kahal_by_credit', 'firstborn_by_call', 'kind', 'inheritance_order_owed', 'zelophehad_three'])
q('joseph', 'dinah', ['outrage_phrase', 'mohar_unbounded', 'mohar_by_call', 'seducer_sheet', 'three_verbs', 'silence_kept'])
q('exodus_story', 'amalek', ['hands', 'weakened_seat', 'blotting', 'jethro_heard'])
q('primeval', 'hagar', ['affliction_reading', 'as_a_wife', 'first_union', 'wrong_with_words']); q('primeval', 'separation', ['muzzled', 'lewdness'])
c('balak', 'the_call', ['curse_roots', 'blessing_formula', 'word_formula', 'restrictors', 'cursing_barred', 'house_of_silver', 'honor_promised', 'embassies', 'prophet_then_diviner', 'balaam_name', 'midian_joined'])
c('naso', 'camp_purity', ['ladder'], who='leper'); c('naso', 'camp_purity', ['ladder'], who='zav'); c('naso', 'camp_purity', ['ladder'], who='corpse_unclean'); c('naso', 'camp_purity', ['who_is_sent'], what='seed_emitter'); c('naso', 'camp_purity', ['who_is_sent'], what='night_chance')
c('beha', 'miriam', ['who_declared', 'grade', 'halt', 'humble', 'foolish', 'admonition_days'])
c('mekoshesh', 'capital_procedure', ['stoning'], died_at='the stoning house'); 
for nm in ('mishpatim', 'mishpatim_2', 'mishpatim_3', 'negaim', 'metzora', 'hear_o_israel'):
    m = load(nm); M[nm] = m
    ups = [n for n in dir(m) if n.isupper() and not n.startswith('_')]
    print('MODULE', nm, 'upper names:', ups[:40])
    for n in ups:
        v = getattr(m, n)
        if isinstance(v, (list, tuple, dict)) and len(v) and len(str(v)) < 40000:
            s = str(v); hits = [k for k in ('seduc', 'virgin', 'betroth', 'kidnap', 'steal', 'soul', 'wrestl', 'strive', 'hurt', 'fifty', 'dowry', 'mohar', 'lepros', 'priest', 'tzitzit', 'fringe', 'tassel') if k in s.lower()]
            if hits: print('  TABLE %s.%s: %s | %d items | hits %s | head: %s' % (nm, n, type(v).__name__, len(v), hits, s[:600]))
print('DEFS negaim:', [(f, str(inspect.signature(getattr(M['negaim'], f)))) for f in ('days', 'house_machine', 'standing_verdict', 'scene') if hasattr(M['negaim'], f)])
show('negaim.standing_verdict source head', lambda: re.sub(r'\s+', ' ', inspect.getsource(M['negaim'].standing_verdict)[:900]))
show('mishpatim_2 source: the seducer cells', lambda: [re.sub(r'\s+', ' ', l)[:220] for l in inspect.getsource(M['mishpatim_2']).split('\n') if re.search(r'seduc|virgin|betroth|mohar|fifty|22:15|22:16', l)][:24])
show('mishpatim source: the kidnapper and the wrestlers', lambda: [re.sub(r'\s+', ' ', l)[:220] for l in inspect.getsource(M['mishpatim']).split('\n') if re.search(r'kidnap|steal.*soul|21:16|21:22|strive|wrestl|hurt', l)][:24])
show('hear_o_israel source: the fringes', lambda: [re.sub(r'\s+', ' ', l)[:220] for l in inspect.getsource(M['hear_o_israel']).split('\n') if re.search(r'tzitzit|fringe|tassel|15:3[7-9]|15:4[01]', l)][:16])
print('==== THE TAPE\'S LINES AT NUMBERS 15, LEVITICUS 19 AND THE PURGE SEATS ====')
seq = open(ROOT + '/World/step9/cold_run_sequence.py', encoding='utf-8').read()
subs = re.findall(r"^\s+w\.submit\(\{'kind': '(\w+)'.*?'case_source': (?:'([^']*)'|\"([^\"]*)\")", seq, re.M)
for pref in ('Num 15:', 'Lev 19:', 'Lev 18:', 'Lev 20:', 'Lev 21:', 'Lev 25:', 'Exod 21:', 'Exod 22:', 'Exod 23:', 'Deut 13:', 'Deut 17:', 'Deut 18:', 'Deut 19:', 'Deut 15:', 'Deut 5:', 'Deut 16:', 'Lev 13:', 'Lev 14:'):
    hits = [(k, (a or b)[:34]) for k, a, b in subs if (a or b).startswith(pref)]
    print(' TAPE %-9s %d %s' % (pref, len(hits), hits[:16]))
print('CALLEES3 DONE')
