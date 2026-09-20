import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 8b — THE CALLEES' FACTS PRINTED BEFORE ANY ASSERT IS TYPED (2b's lesson 6; 7b's form): every CALL the design names, its signature,
# its asks-in-source and EVERY ask's result repr'd (cut) — the older runners' cells take q, the Deuteronomy runners' take (case, data): the print settles
# each form; and the tape's lines the readback references, their kinds, subjects and first verses read off the sequence file's TAPE block, with the
# markers the two retrograde lines and the stretch row use. ch9_callees.py's form.
import sys, io, contextlib, subprocess, inspect, re
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_erection as ER, cold_run_sanctuary_build as SB, cold_run_covenant_at_horeb as CH, cold_run_obey_horeb as OH, cold_run_not_righteousness as NR
    import cold_run_journeys as JO, cold_run_chukat as CK, cold_run_bamidbar as BM, cold_run_beha as BH, cold_run_korach as KR, cold_run_naso as NS, cold_run_joseph as JS
    import cold_run_opening_speech as OS, cold_run_hear_o_israel as HI, cold_run_good_land as GL, cold_run_seven_nations as SN, cold_run_ordinances as OR, cold_run_holiness_b as HB
    import world_engine as WE
def sig(f): return f.__code__.co_varnames[:f.__code__.co_argcount]
def show(label, f, cut=360):
    try: r = f()
    except Exception as e: r = 'RAISED %s: %s' % (type(e).__name__, str(e)[:160])
    print('%-64s %s' % (label, repr(r)[:cut]))
def cells_of(M): return [n for n in dir(M) if not n.startswith('_') and callable(getattr(M, n)) and getattr(getattr(M, n), '__module__', '') == M.__name__]
def asks_in(src): return sorted(set(re.findall(r"(?:ask == |^\s*if a == |\bask\b == |\bask in \(|\bq == |\bq in \()'([a-z_0-9]+)'", src, re.M)))
def cell(M, name, asks=None, head_n=400, cut=360):
    f = getattr(M, name, None)
    if f is None: print('==== %s.%s MISSING; cells: %s' % (M.__name__, name, cells_of(M)[:40])); return
    src = inspect.getsource(f); found = asks_in(src)
    print('==== %s.%s sig %s (%d chars) asks-in-source %s\n%s\n' % (M.__name__, name, sig(f), len(src), found, src[:head_n].replace('\n', '\n    ')))
    for a in (asks if asks is not None else found):
        if len(sig(f)) >= 2 and sig(f)[0] == 'case': show('  %s.%s({ask:%s})' % (M.__name__[9:], name, a), lambda a=a: f({'ask': a}, M.DATA)[:2], cut)
        else: show('  %s.%s(%r)' % (M.__name__[9:], name, a), lambda a=a: f(a), cut)
cell(ER, 'tablets', ['fragments_by_call', 'breaking_ratified', 'finger_and_forms']); cell(ER, 'ascent', ['forty', 'seventeenth_tammuz'])
cell(SB, 'ark'); cell(CH, 'the_voice_and_the_request', ['the_tablets_given_to_me'])
cell(OH, 'the_one_god', ['because_he_loved_your_fathers', 'you_were_shown', 'to_dispossess_nations']); cell(OH, 'the_exhortation'); cell(OH, 'horeb_retold', ['the_ten_words_and_the_tablets'])
cell(NR, 'the_calf_retold', ['written_with_the_finger', 'the_fragments_in_the_ark', 'the_breaking_in_my_own_words']); cell(NR, 'the_forty_days', ['forty_days_forty_nights', 'the_second_forty', 'i_sat_on_the_mount']); cell(NR, 'the_intercession', ['the_lord_hearkened'])
cell(JO, 'the_stations'); cell(JO, 'aarons_death_retold'); cell(CK, 'edom_and_hor'); cell(BM, 'kohath'); cell(BM, 'levites'); cell(BH, 'march'); cell(BH, 'levites_rite')
cell(KR, 'the_watch'); cell(KR, 'the_tithe'); cell(NS, 'blessing'); cell(JS, 'seventy'); cell(JS, 'the_seventy')
print('==== OS cells:', cells_of(OS))
for n in cells_of(OS):
    src = inspect.getsource(getattr(OS, n))
    if 'ככוכבי' in src or 'stars' in src or "1:10" in src: cell(OS, n)
cell(HI, 'the_header'); cell(HI, 'the_creed'); cell(HI, 'the_gift_and_the_warning'); cell(GL, 'the_way_of_forty_years')
cell(SN, 'the_holy_people'); cell(SN, 'the_faithful_god'); cell(SN, 'do_not_fear'); cell(OR, 'courts'); cell(OR, 'stranger'); cell(HB, 'convert_measures')
for M in (ER, SB, CH, OH, NR, JO, CK, BM, BH, KR, NS, JS, OS, HI, GL, SN, OR, HB):
    show('%s DATA keys' % M.__name__[9:], lambda M=M: list(getattr(M, 'DATA', {}))[:48], 900)
show('JO.DATA the_deuteronomy_order', lambda: JO.DATA.get('the_deuteronomy_order'), 900); show('CK.DATA moserah', lambda: CK.DATA.get('moserah'), 900); show('NS.DATA face_lifted', lambda: NS.DATA.get('face_lifted'), 900)
for M in (OS, OH, CH, HI, SN, GL, NR):
    show('%s.READBACK len / grades' % M.__name__[9:], lambda M=M: (len(M.READBACK), dict(getattr(M, 'RB_GRADES', {}))))
# ---- the tape's lines the readback references: kind, subject, first verse, the fields — read off the sequence file's TAPE block ----
SRC = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read().split('# ==== TAPE BEGIN', 1)[1].split('# ==== TAPE END ====', 1)[0]
KINDS = ['moses_ascended', 'vessel_made', 'testimony_placed', 'tablets_given', 'levites_gathered', 'levites_given', 'levites_purified_and_given', 'portion_declared', 'journeyed_to_mount_hor', 'garments_transferred_and_aaron_died', 'aaron_mourned_thirty_days', 'sworn_by_himself', 'shema_declared', 'levites_rebuked', 'moses_interceded', 'prayed_for_aaron', 'nations_devoted', 'hearing_blessed']
print('==== THE TAPE\'S LINES (kind | subject | first verse | the source head | the line\'s other fields):')
import ast
for line in SRC.split('\n'):
    m = re.match(r"\s*w\.submit\((\{.*\})\)\s*#", line)
    if not m: continue
    try: e = ast.literal_eval(m.group(1))
    except Exception: continue
    if e.get('kind') in KINDS:
        cs = str(e.get('case_source', ''))
        if e['kind'] == 'vessel_made' and 'ark' not in cs and e.get('vessel') != 'ark': continue
        print('  %-36s %-22s %-18s %-60s %s' % (e['kind'], e.get('subject'), WE.first_verse(cs), cs[:60], {k: (v if len(repr(v)) < 90 else repr(v)[:90]) for k, v in e.items() if k not in ('kind', 'subject', 'case_source')}))
print('==== THE MARKERS Exod 34:4 / 34:28 / 40:17 / Num 20:22 / 20:28 / Deut 9:20 / 9:21 in the TAPE block:')
for line in SRC.split('\n'):
    if any(("w.marker('%s'" % v) in line for v in ('Exod 34:4', 'Exod 34:28', 'Exod 40:17', 'Num 20:22', 'Num 20:28', 'Deut 9:20', 'Deut 9:21')):
        print('  ' + line.strip()[:300])
print('==== the tape\'s last Deuteronomy 9 lines and markers (the new lines go after them):')
tail = [l for l in SRC.split('\n') if 'Deut 9:' in l[:120] and ('w.submit' in l or 'w.marker' in l)]
for l in tail[-3:]: print('  ' + l.strip()[:200])
