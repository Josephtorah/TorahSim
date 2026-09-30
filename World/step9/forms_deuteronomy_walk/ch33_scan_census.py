import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 21b (2026-09-29): THE SCAN CENSUS EXTENDED (14b's lesson 2; 15b's lesson 2 — the tuple-of-substrings form; 16b's B2 — the named patterns; 17b's homographs; 18b's rain lesson) — every runner's ledger_scan on israel_people (its pattern and its exclusions), AND the readback
# probes' and the tape's own substring scans (readback_probes.py and cold_run_sequence.py — every `ledger_scan(` / `LG(` / effect-substring pattern read from their
# sources), replayed on the one database AS IT NOW STANDS (the chapters' lines written by the tape's first run), the survivors printed: the seats a later chapter's
# entries move. No import of the runners — the patterns read from their sources. ch32_scan_census.py's form over the twenty-eight names on twelve ledgers. RUN FROM THE REPO ROOT.
import subprocess, os, re, glob, sqlite3, subprocess, sys
ROOT = _ROOT   # THE DEUTERONOMY WALK 16b (kept at 21b): the forms copy's portable header stripped — a scratch script's ROOT from git (the first census run resolved ROOT to the scratchpad's grandparent: 'unable to open database file')
DB = ROOT + '/World/journal/data/world.sqlite'
c = sqlite3.connect('file:%s?mode=ro' % DB, uri=True)
rows = c.execute("SELECT DISTINCT effect, value FROM run_ledger WHERE entity=?", ('israel_people',)).fetchall()
allrows = c.execute("SELECT DISTINCT entity, effect, value FROM run_ledger").fetchall()
NEW = {'naphtali_sated_with_favor_sea_and_south_blessed', 'law_commanded_the_inheritance_of_jacob_declared', 'levi_father_and_mother_unseen_covenant_kept', 'gad_came_with_the_heads_righteousness_of_the_lord_executed', 'iron_and_brass_bars_strength_as_your_days_blessed', 'eternal_god_dwelling_everlasting_arms_enemy_driven_out_declared', 'joseph_firstling_ox_horns_ephraim_myriads_manasseh_thousands', 'joseph_land_blessed_with_the_precious_things', 'happy_are_you_israel_shield_and_sword_high_places_trodden_declared', 'asher_blessed_above_sons_foot_dipped_in_oil', 'blessing_given_before_moses_death', 'benjamin_beloved_dwells_in_safety_between_his_shoulders_blessed', 'gad_enlarged_lioness_first_part_lawgivers_portion_blessed', 'king_in_jeshurun_when_the_heads_gathered_declared', 'the_lord_came_from_sinai_seir_paran_declared', 'none_like_the_god_of_jeshurun_rider_of_the_heaven_declared', 'joseph_the_bush_dweller_favor_on_the_crown_separate_from_his_brethren', 'peoples_called_to_the_mountain_sacrifices_of_righteousness', 'israel_dwells_in_safety_alone_fountain_of_jacob_declared', 'levi_thummim_and_urim_proved_at_massah_blessed', 'fiery_law_from_his_right_hand_declared', 'dan_lions_whelp_leaps_from_bashan_blessed', 'levi_teaches_jacob_incense_and_whole_offering', 'judahs_voice_heard_brought_to_his_people_blessed', 'reuben_to_live_and_not_die_blessed', 'levi_substance_blessed_loins_of_his_foes_smitten', 'zebulun_going_out_issachar_in_tents_blessed', 'lover_of_the_peoples_holy_ones_in_his_hand_declared'}
present = sorted(NEW & {e for e, _ in rows})
print('israel_people rows in the one database:', len(rows), '| all distinct rows:', len(allrows), '| chapter 33 present:', len(present), present[:6], '...')
def compile_pat(pat):
    try: return re.compile(pat.encode().decode('unicode_escape') if '\\\\' in pat else pat, re.I)
    except Exception as ex: return None
print('==== A. THE RUNNERS\' HOLE SCANS (ledger_scan on israel_people by a WORDS pattern) ====')
trips = 0
for f in sorted(glob.glob(ROOT + '/World/step9/cold_run_*.py')):
    src = open(f, encoding='utf-8').read(); name = os.path.basename(f)[9:-3]
    for m in re.finditer(r"(\w+) = r\"(.+?)\"", src):   # THE DEUTERONOMY WALK 16b: several patterns on one line read (second_tablets' LAW_WORDS shared its line with two others — the anchored form read the first alone; the tape's second run fell at its assert)
        var, pat = m.group(1), m.group(2)
        if not var.endswith('WORDS'): continue
        use = re.search(r"ledger_scan\('israel_people', %s\)" % var, src)
        if not use: continue
        stmt = src[src.rfind('\n', 0, use.start()) + 1: src.find('\n', use.end())]
        excl = re.findall(r"if e not in \((.*?)\)\]", stmt)
        excl_names = set(re.findall(r"'([a-z_0-9]+)'", excl[0])) if excl else set()
        rx = compile_pat(pat)
        if rx is None: print(' ', name, var, 'PATTERN ERROR'); continue
        hits = sorted({e for e, v in rows if rx.search('%s %s' % (e, v if v is not None else ''))})
        surv = [e for e in hits if e not in excl_names]
        flag = 'TRIPS' if surv else 'ok'; trips += bool(surv)
        print(' %-6s %-18s %-14s hits %d, excluded %d, survivors %s' % (flag, name, var, len(hits), len(excl_names), surv))
print('==== B. THE PROBES\' AND THE TAPE\'S SUBSTRING SCANS (every quoted pattern handed to a ledger/effect scan in readback_probes.py, census_probes.py, register_census.py and cold_run_sequence.py; the values of the new rows searched for each) ====')
def scans_in(path):
    src = open(path, encoding='utf-8').read(); out = []
    for m in re.finditer(r"(?:ledger_scan|LG|effect_scan|nall|L)\(\s*(?:'([a-z_\-]+)'\s*,\s*)?(?:r)?'([^']+)'", src):
        out.append((m.group(1), m.group(2), src.count('\n', 0, m.start()) + 1))
    for m in re.finditer(r"re\.search\(\s*r?'([^']+)'\s*,\s*(?:'%s %s' % \()?(?:e|v|str\(v\)|val)", src):
        out.append((None, m.group(1), src.count('\n', 0, m.start()) + 1))
    for m in re.finditer(r"'([a-z_]+)' in (?:str\()?(?:v|val|e\[.value.\]|e\.get\(.value.\))", src):
        out.append((None, m.group(1), src.count('\n', 0, m.start()) + 1))
    for m in re.finditer(r"any\(t in e\['effect'\] for t in \((.*?)\)\)", src):   # THE DEUTERONOMY WALK 15b (kept at 16b): the tape's DE4 form — a tuple of substrings over the effect NAMES (missed by the first census; the tape's second run read it)
        for t in re.findall(r"'([a-z_]+)'", m.group(1)): out.append(('name', t, src.count('\n', 0, m.start()) + 1))
    return out
newvals = [(e, v) for e, v in rows if e in NEW]
for fn in ('readback_probes.py', 'census_probes.py', 'register_census.py', 'cold_run_sequence.py', 'checkpoint_check.py'):
    p = ROOT + '/World/step9/' + fn
    if not os.path.exists(p): print(' (no file)', fn); continue
    found = scans_in(p); shown = 0
    for ent, pat, line in found:
        if len(pat) < 4 or pat in NEW: continue
        rx = compile_pat(pat) if any(ch in pat for ch in '^$\\|()[]') else None
        hitn = [e for e, v in newvals if (rx.search('%s %s' % (e, v or '')) if rx else ((pat in e) if ent == 'name' else (pat in e or pat in str(v or ''))))]
        hita = [(ent_, e) for ent_, e, v in allrows if e in NEW and (rx.search('%s %s' % (e, v or '')) if rx else (pat in e or pat in str(v or '')))] if not hitn else []
        if hitn or hita:
            shown += 1; print(' TRIPS? %-22s line %-5d entity %-14s pattern %-40r -> new rows matched %s' % (fn, line, ent, pat[:40], sorted(set(hitn))[:6] or sorted(set(hita))[:6]))
    print(' %s: %d scan seats read, %d name a new row' % (fn, len(found), shown))
print('==== B2. THE TAPE\'S NAMED-PATTERN SCANS (re.search(cold_run_X.NAME_WORDS, …) in cold_run_sequence.py — the pattern read from the runner\'s own source; a THIRD form the census had not covered: THE DEUTERONOMY WALK 16b, read at the tape\'s first run 9/10 — CU7 and DA6) ====')
seqsrc = open(ROOT + '/World/step9/cold_run_sequence.py', encoding='utf-8').read()
named = re.findall(r"re\.search\(cold_run_(\w+)\.(\w+), '%s %s' % \(e\['effect'\], e\.get\('value', ''\)\)", seqsrc)
seen = set(); shown2 = 0
for runner, var in named:
    if (runner, var) in seen: continue
    seen.add((runner, var))
    rsrc = open(ROOT + '/World/step9/cold_run_%s.py' % runner, encoding='utf-8').read()
    m = re.search(r"^%s = r?\"(.+?)\"\s*(?:#.*)?$" % var, rsrc, re.M) or re.search(r"^%s = r?'(.+?)'\s*(?:#.*)?$" % var, rsrc, re.M)
    if not m: print(' ', runner, var, 'PATTERN NOT FOUND in the runner\'s source'); continue
    rx = compile_pat(m.group(1))
    if rx is None: print(' ', runner, var, 'PATTERN ERROR'); continue
    line = seqsrc.count('\n', 0, seqsrc.find('cold_run_%s.%s' % (runner, var))) + 1
    hitn = sorted({e for e, v in newvals if rx.search('%s %s' % (e, v if v is not None else ''))})
    print(' %-6s cold_run_sequence.py line %-5d %-22s %-14s pattern %-50r -> new rows matched %s' % ('TRIPS' if hitn else 'ok', line, runner, var, m.group(1)[:50], hitn))
    shown2 += bool(hitn)
print(' named-pattern seats read %d, %d name a new row' % (len(seen), shown2))
print('==== C. THE NEW ROWS\' VALUES NAMING OTHER CHAPTERS\' EFFECT NAMES (a value that spells an earlier effect\'s name trips that effect\'s substring scans) ====')
names = sorted({e for _, e, _ in allrows} - NEW)
for e, v in sorted(newvals):
    v = str(v or ''); hit = [n for n in names if len(n) > 8 and n in v]
    if hit: print(' ', e, '->', hit[:8])
print('SCAN CENSUS DONE — runner scans tripping:', trips)
