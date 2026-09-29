import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (2026-09-28): THE SCAN CENSUS EXTENDED (14b's lesson 2; 15b's lesson 2 — the tuple-of-substrings form; 16b's B2 — the named patterns; 17b's homographs; 18b's rain lesson) — every runner's ledger_scan on israel_people (its pattern and its exclusions), AND the readback
# probes' and the tape's own substring scans (readback_probes.py and cold_run_sequence.py — every `ledger_scan(` / `LG(` / effect-substring pattern read from their
# sources), replayed on the one database AS IT NOW STANDS (the chapters' lines written by the tape's first run), the survivors printed: the seats a later chapter's
# entries move. No import of the runners — the patterns read from their sources. ch29_scan_census.py's form over the forty-two names on three ledgers. RUN FROM THE REPO ROOT.
import subprocess, os, re, glob, sqlite3, subprocess, sys
ROOT = _ROOT   # THE DEUTERONOMY WALK 16b (kept at 20b): the forms copy's portable header stripped — a scratch script's ROOT from git (the first census run resolved ROOT to the scratchpad's grandparent: 'unable to open database file')
DB = ROOT + '/World/journal/data/world.sqlite'
c = sqlite3.connect('file:%s?mode=ro' % DB, uri=True)
rows = c.execute("SELECT DISTINCT effect, value FROM run_ledger WHERE entity=?", ('israel_people',)).fetchall()
allrows = c.execute("SELECT DISTINCT entity, effect, value FROM run_ledger").fetchall()
NEW = {'fire_kindled_to_the_lowest_sheol', 'i_i_am_he_no_god_beside_me', 'the_rock_perfect_and_just_declared', 'generation_crooked_not_his_children', 'song_spoken_in_the_ears_of_the_people', 'evils_heaped_arrows_spent', 'nation_void_of_counsel', 'it_is_your_life_no_empty_matter', 'jealousy_by_no_people_foolish_nation', 'apple_of_his_eye_kept', 'trespassed_at_meribath_kadesh_not_sanctified', 'doctrine_as_rain_and_dew_likened', 'sword_whetted_vengeance_rendered', 'see_the_land_from_afar_not_go_there', 'demons_and_new_gods_sacrificed', 'nations_bounds_set_by_number_of_israel', 'one_chasing_a_thousand_rock_sold_them', 'father_who_acquired_you_requited', 'the_lord_alone_led_no_foreign_god', 'go_up_to_nebo_see_the_land_commanded', 'vengeance_laid_up_in_store_sealed', 'rock_that_begot_you_forgotten', 'hoshea_speaks_the_song_beside_moses', 'where_are_their_gods_asked', 'die_in_the_mountain_gathered_to_your_people_commanded', 'lord_judges_his_people_repents_himself', 'vine_of_sodom_gall_grapes', 'nations_sing_with_his_people_land_atones', 'feast_of_curd_milk_fat_and_wine_given', 'name_of_the_lord_proclaimed_greatness_ascribed', 'as_aaron_died_in_hor_and_was_gathered', 'set_your_heart_to_these_words_commanded', 'days_of_old_remember_commanded', 'as_an_eagle_stirring_its_nest_borne', 'jeshurun_fat_kicked_forsook_god', 'i_kill_and_make_alive_none_delivers', 'lords_portion_his_people_jacob', 'found_in_the_desert_encircled_and_kept', 'hand_lifted_to_heaven_live_forever_sworn', 'heights_of_the_land_ridden_honey_from_the_rock', 'blotting_out_stayed_by_the_enemys_boast', 'hunger_beasts_serpents_sword_terror_sent'}
present = sorted(NEW & {e for e, _ in rows})
print('israel_people rows in the one database:', len(rows), '| all distinct rows:', len(allrows), '| chapter 32 present:', len(present), present[:6], '...')
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
