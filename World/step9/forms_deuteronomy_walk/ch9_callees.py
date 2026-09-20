import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 7b — THE CALLEES' FACTS PRINTED BEFORE ANY ASSERT IS TYPED (2b's lesson 6): every CALL the design names, its signature, its
# source head, its asks-in-source and its result repr'd (cut), so the runner's asks copy the print; and the tape's lines the readback references, their
# kinds and first verses read off the sequence file's TAPE block. ch8_callees.py's form.
import sys, io, contextlib, subprocess, inspect, re
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_erection as ER, cold_run_exodus_story as ES, cold_run_beha as BH, cold_run_shelach as SL, cold_run_opening_speech as OS
    import cold_run_obey_horeb as OH, cold_run_covenant_at_horeb as CH, cold_run_hear_o_israel as HI, cold_run_seven_nations as SN, cold_run_shemini_day as SD, cold_run_good_land as GL
    import world_engine as WE
def sig(f): return f.__code__.co_varnames[:f.__code__.co_argcount]
def show(label, f):
    try: r = f()
    except Exception as e: r = 'RAISED %s: %s' % (type(e).__name__, str(e)[:160])
    print('%-56s %s' % (label, repr(r)[:520]))
def cells_of(M): return [n for n in dir(M) if not n.startswith('_') and callable(getattr(M, n)) and getattr(getattr(M, n), '__module__', '') == M.__name__]
def cell(M, name, asks, head_n=600):
    f = getattr(M, name, None)
    if f is None: print('==== %s.%s MISSING; cells: %s' % (M.__name__, name, cells_of(M)[:40])); return
    src = inspect.getsource(f); print('==== %s.%s sig %s (%d chars) asks-in-source %s\n%s\n' % (M.__name__, name, sig(f), len(src), sorted(set(re.findall(r"(?:ask == |^\s*if a == |\bask\b == |\bask in \()'([a-z_0-9]+)'", src, re.M))), src[:head_n]))
    for a in asks:
        if len(sig(f)) >= 2 and sig(f)[0] == 'case': show('  %s.%s({ask:%s})' % (M.__name__[9:], name, a), lambda a=a: f({'ask': a}, M.DATA)[:2])
        else: show('  %s.%s(%r)' % (M.__name__[9:], name, a), lambda a=a: f(a))
print('==== ER cells:', cells_of(ER)); print('==== ER DATA keys:', list(getattr(ER, 'DATA', {}))[:80])
cell(ER, 'ascent', ['forty', 'seventeenth_tammuz', 'sheet_taanit_4_6', 'six_seventh', 'under_mountain', 'canon_channel'])
cell(ER, 'calf', ['molten_calf', 'saru_stiff', 'seized', 'three_legged', 'vayechal', 'vow_annulled', 'oath_endures', 'relent', 'four_verbs', 'nullification_dispute', 'fourth_verb_decides', 'great_sin', 'individual_rule', 'surcharge', 'plague', 'reading_law', 'boshesh', 'confess_specify'], head_n=1200)
cell(ER, 'tablets', ['breaking_ratified', 'fragments_by_call', 'finger_and_forms']); cell(ER, 'craftsmen', ['finger'])
cell(ES, 'trials', ['ten_list', 'count_by_exodus']); cell(ES, 'sinai', ['treasure_seats']); cell(ES, 'sea', [])
cell(BH, 'taberah_and_quail', ['fire_at_edge', 'fire_sank', 'graves', 'manna_form']); cell(BH, 'march', ['three_days', 'date'])
cell(SL, 'decree', ['ability', 'egypt_will_hear', 'offer_second_seat', 'plea', 'attributes_deleted', 'exceptions', 'pardon', 'ninth_of_av_reading', 'day_for_year']); cell(SL, 'spies', ['giants', 'forty_days'])
cell(OS, 'the_spies_read_back', ['the_murmuring', 'the_presumption', 'the_asking', 'the_exceptions', 'the_carrying']); cell(OS, 'the_plea', ['the_plea', 'the_refusal'])
cell(OH, 'the_one_god', ['to_dispossess_nations', 'because_he_loved_your_fathers', 'you_were_shown']); cell(OH, 'no_image', ['consuming_fire_jealous_god']); cell(OH, 'horeb_retold', ['the_ten_words_and_the_tablets', 'the_day_you_stood']); cell(OH, 'the_exile_case', ['the_merciful_god', 'the_witnesses'])
cell(CH, 'the_voice_and_the_request', ['the_tablets_given_to_me']); cell(CH, 'the_first_tablet', ['the_first_word']); cell(CH, 'the_second_tablet', [])
cell(HI, 'the_test_and_the_right', ['you_shall_not_test'])
cell(SN, 'the_seven_nations', ['the_seven', 'the_ban'])
print('==== SD cells:', cells_of(SD)); print('==== SD DATA keys:', list(getattr(SD, 'DATA', {}))[:60])
cell(SD, 'day', ['aaron_chatat_run']); cell(SD, 'calf', []); cell(SD, 'fire', [])
cell(GL, 'the_way_of_forty_years', ['forty_years'])
for M in (ER, ES, BH, SL, OS, OH, CH, HI, SN, SD, GL):
    show('%s DATA keys' % M.__name__[9:], lambda M=M: list(getattr(M, 'DATA', {}))[:40])
for M in (OS, OH, CH, HI, SN, GL):
    show('%s.READBACK len / grades' % M.__name__[9:], lambda M=M: (len(M.READBACK), dict(getattr(M, 'RB_GRADES', {}))))
# ---- the tape's lines the readback references: kind, subject, first verse, the fields — read off the sequence file's TAPE block ----
SRC = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read().split('# ==== TAPE BEGIN', 1)[1].split('# ==== TAPE END ====', 1)[0]
KINDS = ['moses_ascended', 'calf_made', 'moses_interceded', 'tablets_broken', 'calf_destroyed', 'levites_gathered', 'tent_pitched_outside', 'attributes_proclaimed_at_sinai', 'tablets_given', 'sworn_by_himself', 'fire_of_the_lord_burned', 'named', 'quail_and_plague', 'congregation_wept', 'decree_declared', 'moses_pleaded_on_the_attributes', 'pardoned_and_decreed', 'presumed_to_go_up', 'smitten_to_hormah', 'rock_struck', 'witnesses_called']
print('==== THE TAPE\'S LINES (kind | subject | first verse | the source head | the line\'s other fields):')
import ast
for line in SRC.split('\n'):
    m = re.match(r"\s*w\.submit\((\{.*\})\)\s*#", line)
    if not m: continue
    try: e = ast.literal_eval(m.group(1))
    except Exception: continue
    if e.get('kind') in KINDS:
        cs = str(e.get('case_source', ''))
        if e['kind'] == 'named' and not cs.startswith('Exod 17:7'): continue
        print('  %-32s %-22s %-18s %-60s %s' % (e['kind'], e.get('subject'), WE.first_verse(cs), cs[:60], {k: (v if len(repr(v)) < 80 else repr(v)[:80]) for k, v in e.items() if k not in ('kind', 'subject', 'case_source')}))
print('==== THE MARKERS Exod 24:18 / 32:19 / 32:30 / 34:4 in the TAPE block:')
for line in SRC.split('\n'):
    if any(("w.marker('%s'" % v) in line for v in ('Exod 24:18', 'Exod 32:19', 'Exod 32:30', 'Exod 34:4', 'Deut 5:23', 'Deut 5:32')):
        print('  ' + line.strip()[:260])
