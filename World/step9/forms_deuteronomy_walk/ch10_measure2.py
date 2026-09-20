#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 8b — THE COMPILE OF CHAPTER 10: THE SECOND MEASUREMENT on the running world's snapshot (after ch10_compile_recon.py) —
# (1) the log's rows the chapter retells, with the clock's day and its date; (2) THE THIRD FORTY on the clock; (3) the ledger entries on the ark, the
# Levites, Aaron, Eleazar, Israel (the laws restated), the judge/stranger ids; (4) the receipt finder on chapter 10; (5) the kin's DATA rows whole
# (chukat's moserah, journeys' stations, erection's fragments, joseph's seventy, hear_o_israel's creed and duties, ordinances' stranger and bribe).
import sys, io, re, contextlib, inspect, collections, subprocess, importlib
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS, world_engine as WE, register_census as RC
    w = RC.running_world()
    MODS = {n: importlib.import_module('cold_run_' + n) for n in ('chukat', 'journeys', 'erection', 'joseph', 'hear_o_israel', 'ordinances', 'holiness_b', 'korach', 'naso', 'sanctuary_build', 'bamidbar', 'beha', 'obey_horeb', 'not_righteousness', 'covenant_at_horeb', 'opening_speech', 'exodus_story')}
def D(day):
    try: return w.clock.date_in('exodus', day)
    except Exception as e: return 'date_in raised %r' % e
print('==== (0) THE ROW SHAPES ====')
seen = set()
for row in w.log:
    if not isinstance(row, (list, tuple)): continue
    if row[0] in seen: continue
    seen.add(row[0]); print('  %s: %s' % (row[0], str(row)[:500]))
print('  clock.date_in signature: %s; day_in: %s' % (inspect.signature(w.clock.date_in), inspect.signature(w.clock.day_in)))
print('  w attrs: %s' % [a for a in dir(w) if not a.startswith('_')][:60])
print('\n==== (1) THE LOG ROWS THE CHAPTER RETELLS (tag, day, date, kind, subject, source) ====')
KIN = r'^(?:Exod (?:1:[1-7]|22:2[0-3]|23:[89]|24:12|25:(?:1\d|2[0-2])|31:18|32:(?:2[6-9]|34)|33:1|34:(?:[1-4]|2[89])|37:[1-9]|40:(?:3|2[01]))|Lev 19:3[34]|Num (?:3:(?:[5-9]|1[0-3]|4\d|5[01])|4:\d+|6:2[2-7]|8:(?:[5-9]|1\d|2[0-6])|18:(?:[12]|2[0-4])|20:2[2-9]|33:3\d)|Gen 46:2[67]|Deut (?:4:13|6:|10:))\b'
def src_of(ev):
    if isinstance(ev, dict): return str(ev.get('case_source') or ev.get('source') or ev.get('verse') or ev.get('at') or '')
    return str(ev)
n = 0
for row in w.log:
    if not isinstance(row, (list, tuple)) or len(row) < 3: continue
    tag, day, ev = row[0], row[1], row[2]
    s = src_of(ev)
    if re.search(KIN, s):
        k = ev.get('kind', ev.get('effect', ev.get('value', '?'))) if isinstance(ev, dict) else '?'
        sub = ev.get('subject', '') if isinstance(ev, dict) else ''
        print('  %-7s day %-7s %-16s %-36s %-24s %s' % (tag, day, str(D(day)), str(k)[:36], str(sub)[:24], s[:90]))
        n += 1
print('  rows: %d' % n)
print('\n==== (2) THE THIRD FORTY ON THE CLOCK ====')
cp = WE.CAL_PARAMS['second_tablets_given']['value']
d_tab = w.clock.day_in('exodus', 1, cp['month'], cp['day'])
mk = {}
for row in w.log:
    if isinstance(row, (list, tuple)) and row[0] == 'MARKER':
        s = src_of(row[2]); mk[s] = row[1]
for v in ('Exod 24:18', 'Exod 32:19', 'Exod 32:30', 'Exod 34:4', 'Exod 40:17', 'Num 20:22', 'Num 20:28', 'Deut 4:13', 'Deut 9:20', 'Deut 9:21', 'Deut 1:1'):
    print('  marker %-11s day %s  %s' % (v, mk.get(v), D(mk[v]) if v in mk else '-'))
print('  second_tablets_given param: %s -> day %s = %s; the third forty: %s - %s = %s days' % (cp, d_tab, D(d_tab), d_tab, mk.get('Exod 34:4'), d_tab - mk['Exod 34:4'] if 'Exod 34:4' in mk else '?'))
print('  the first two forties: %s, %s' % (mk['Exod 32:19'] - mk['Exod 24:18'], mk['Exod 34:4'] - mk['Exod 32:30']))
print('  a MARKER row whole (Exod 34:4): %s' % [str(r)[:700] for r in w.log if isinstance(r, (list, tuple)) and r[0] == 'MARKER' and src_of(r[2]) == 'Exod 34:4'])
print('  the moses_ascended lines (day, date, fields): %s' % [(r[1], D(r[1]), {k: str(v)[:60] for k, v in r[2].items()}) for r in w.log if isinstance(r, (list, tuple)) and r[0] == 'EVENT' and isinstance(r[2], dict) and r[2].get('kind') == 'moses_ascended'])
print('  the counter (the tape\'s end): day %s = %s' % (w.clock.day, D(w.clock.day)))
print('  Aaron\'s death: the line\'s day vs the marker: %s' % [(r[1], D(r[1]), r[2].get('date')) for r in w.log if isinstance(r, (list, tuple)) and r[0] == 'EVENT' and isinstance(r[2], dict) and r[2].get('kind') == 'garments_transferred_and_aaron_died'])
print('\n==== (3) THE LEDGER ENTRIES on the ark, the Levites, Aaron, Eleazar, Levi; Israel\'s entries touching the restated laws; the ids naming stranger/judge/orphan/widow ====')
ent = getattr(w, 'entities', {})
print('  entities type %s, %d; a sample key: %s' % (type(ent).__name__, len(ent), list(ent)[:3] if hasattr(ent, '__iter__') else '?'))
def entries(eid):
    e = ent.get(eid) if isinstance(ent, dict) else None
    if e is None: return None
    for a in ('ledger', 'entries', 'effects', 'status'):
        if hasattr(e, a): return getattr(e, a)
    if isinstance(e, dict): return e.get('ledger', e)
    return e
for eid in ('the_ark', 'the-ark', 'the_levites', 'the-levites', 'levi', 'aaron', 'eleazar_son_of_aaron', 'the_priesthood'):
    L = entries(eid)
    if L is None: print('  %s: no entity' % eid); continue
    try:
        rows = list(L.items()) if isinstance(L, dict) else list(L)
    except Exception as e:
        rows = [str(L)[:300]]
    print('  %s: %d entries: %s' % (eid, len(rows), [str(r)[:140] for r in rows][:40]))
w_rows = [r for r in w.log if isinstance(r, (list, tuple)) and r[0] in ('WRITE', 'RETRO-WRITE', 'CLOSE')]
print('  a WRITE row whole: %s' % str(w_rows[0])[:500])
def wr(pat, subj=None):
    out = []
    for r in w_rows:
        s = str(r[2])
        if subj and (isinstance(r[2], dict) and str(r[2].get('subject', r[2].get('on', ''))) != subj): continue
        if re.search(pat, s): out.append((r[0], r[1], str(D(r[1])), s[:170]))
    return out
for pat in ('tablets_delivered', 'fragments|broken_tablets', 'given_to_aaron|tithe_granted|inheritance_barred|terumah_of_the_tithe|levites_portion|separated|set_apart', 'blessed_by_the_priests|blessed_the_people|name_put', 'shema_commanded|test_barred|fear|serve|cleave|swear|love', 'stranger|bribe|orphan|widow', 'circumcis|foreskin|stiff|neck', 'seventy|stars', 'garments_inherited|buried|died|death'):
    rows = wr(pat)
    print('  WRITES matching %-70r: %d  %s' % (pat, len(rows), rows[:12]))
ids = sorted(k for k in (ent.keys() if isinstance(ent, dict) else []) if re.search(r'stranger|judge|orphan|widow|convert|ger\b|the_ark|tablet|levite|levi\b|aaron|eleazar|priest', str(k)))
print('  ids: %s' % ids)
print('\n==== (4) THE RECEIPT FINDER on chapter 10 ====')
ink = RC.read_ink()
for fn in ('receipts', 'footers', 'count_lines', 'register_headers'):
    try:
        r = getattr(RC, fn)(ink)
        rows = [x for x in (r.items() if isinstance(r, dict) else r) if 'Deut 10' in str(x) or "('Deut', 10" in str(x)]
        print('  %s: type %s; Deut 10 rows: %s' % (fn, type(r).__name__, [str(x)[:220] for x in rows][:12]))
    except Exception as e: print('  %s raised %r' % (fn, e))
print('  the receipt regex/forms in register_census.receipts: %s' % inspect.getsource(RC.receipts)[:1500])
print('\n==== (5) THE KIN\'S DATA ROWS WHOLE ====')
CH, JO, ER, JS, HI, OR, HB, KO, NA, SB, BA, BE, NR = (MODS[n] for n in ('chukat', 'journeys', 'erection', 'joseph', 'hear_o_israel', 'ordinances', 'holiness_b', 'korach', 'naso', 'sanctuary_build', 'bamidbar', 'beha', 'not_righteousness'))
for mod, keys in ((CH, ['moserah', 'death_dates', 'seder_olam_walk', 'two_mount_hors', 'succession', 'thirty_days', 'aaron_age']), (JO, None), (NR, ['the_readback'])):
    dd = getattr(mod, 'DATA', {})
    ks = keys or [k for k in dd if re.search(r'station|moser|jaakan|aaron|hor|order|deut', k)]
    for k in ks:
        if k in dd: print('  %s.DATA[%r]: %s' % (mod.__name__[9:], k, str(dd[k])[:900]))
        else: print('  %s.DATA has no %r (keys: %s)' % (mod.__name__[9:], k, sorted(dd)[:40]))
for mod, fn in ((CH, 'edom_and_hor'), (JO, 'the_stations'), (JO, 'aarons_death_retold'), (ER, 'tablets'), (JS, 'the_seventy'), (JS, 'seventy'), (HI, 'the_creed'), (HI, 'the_four_duties'), (OR, 'stranger'), (OR, 'courts'), (HB, 'convert_measures'), (KO, 'the_tithe'), (NA, 'blessing'), (SB, 'ark'), (BA, 'levites'), (BE, 'levites_rite'), (NR, 'rb'), (NR, 'the_forty_days')):
    f = getattr(mod, fn, None)
    if f is None: print('  %s.%s: MISSING' % (mod.__name__[9:], fn)); continue
    s = inspect.getsource(f)
    print('  -- %s.%s(%s): %d lines; head: %s' % (mod.__name__[9:], fn, inspect.signature(f), s.count('\n'), s.split('\n')[0][:160]))
    for l in s.split('\n'):
        if re.search(r"if q == |q in \(|'moserah'|'fragments_by_call'|'both_in_the_ark'|'seventy'|'creed'|'might'|'fear'|'serve'|'swear'|'cleave'|'bribe'|'stranger'|'love'|Deut 10|10:\d|Menachot 99|Bava Batra 14|Bava Batra 123|Num 33|33:3|Seder Olam|Rosh Hashanah 3a|Ta'?anit 9a|retreat|seven stations", l):
            print('       %s' % l.strip()[:300])
