import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 18b (2026-09-26): THE SCAN CENSUS EXTENDED (14b's lesson 2; 15b's lesson 2 — the tuple-of-substrings form; 16b's B2 — the named patterns; 17b's homographs) — every runner's ledger_scan on israel_people (its pattern and its exclusions), AND the readback
# probes' and the tape's own substring scans (readback_probes.py and cold_run_sequence.py — every `ledger_scan(` / `LG(` / effect-substring pattern read from their
# sources), replayed on the one database AS IT NOW STANDS (the chapters' lines written by the tape's first run), the survivors printed: the seats a later chapter's
# entries move. No import of the runners — the patterns read from their sources. ch22_scan_census.py's form over the ninety-one names. RUN FROM THE REPO ROOT.
import subprocess, os, re, glob, sqlite3, subprocess, sys
ROOT = _ROOT   # THE DEUTERONOMY WALK 16b (kept at 18b): the forms copy's portable header stripped — a scratch script's ROOT from git (the first census run resolved ROOT to the scratchpad's grandparent: 'unable to open database file')
DB = ROOT + '/World/journal/data/world.sqlite'
c = sqlite3.connect('file:%s?mode=ro' % DB, uri=True)
rows = c.execute("SELECT DISTINCT effect, value FROM run_ledger WHERE entity=?", ('israel_people',)).fetchall()
allrows = c.execute("SELECT DISTINCT entity, effect, value FROM run_ledger").fetchall()
NEW = {'seed_vines_olives_lost', 'sore_boils_sole_to_crown', 'sons_flesh_eaten_in_siege', 'tithe_for_the_dead_barred', 'consumption_fever_inflammation_sent', 'curses_for_not_hearkening', 'first_fruits_declaration_commanded', 'blessed_in_city_and_field', 'sword_blight_mildew_sent', 'blessed_basket_and_trough', 'life_hanging_in_doubt', 'scattered_among_all_peoples', 'eagle_nation_devours', 'carcass_food_for_birds', 'tithe_removal_commanded', 'ebal_offerings_commanded', 'exiled_with_king_to_serve_wood_and_stone', 'tithe_in_mourning_barred', 'six_tribes_on_ebal_for_the_curse', 'boil_of_egypt_hemorrhoids_scab_itch', 'fathers_wife_lier_cursed', 'peoples_fear_israel', 'high_above_all_nations_promised', 'beast_lier_cursed', 'tithe_confession_commanded', 'wife_house_vineyard_taken', 'lend_not_borrow', 'iron_on_altar_barred', 'mother_in_law_lier_cursed', 'few_in_number_left', 'levites_loud_voice_commanded', 'parent_dishonorer_cursed', 'bribe_for_blood_taker_cursed', 'stranger_head_israel_tail', 'plagues_made_wonderful', 'secret_smiter_cursed', 'madness_blindness_astonishment', 'first_fruits_basket_commanded', 'enemies_flee_seven_ways', 'law_non_upholder_cursed', 'storehouses_blessed', 'great_stones_commanded', 'amen_answered_commanded', 'blessed_coming_in_and_going_out', 'astonishment_proverb_byword', 'diseases_of_egypt_returned', 'first_fruits_set_before_altar_commanded', 'turning_aside_barred', 'established_holy_people', 'returned_to_egypt_in_ships', 'judgment_perverter_cursed', 'became_the_lords_people_this_day', 'covenant_words_in_moab_declared', 'curse_confusion_rebuke_sent', 'lord_declared_israel_treasure_people', 'hearken_and_do_commanded', 'holy_people_promised', 'landmark_mover_cursed', 'enemies_served_in_want', 'fruit_eaten_by_unknown_nation', 'rain_turned_to_dust', 'sold_and_none_buys', 'cursed_coming_in_and_going_out', 'blind_misleader_cursed', 'pestilence_cleaving', 'cursed_fruit_of_womb_ground_beast', 'heavens_brass_earth_iron', 'law_written_very_plainly_commanded', 'stones_plastered_written_commanded', 'sister_lier_cursed', 'first_fruits_recital_commanded', 'blessed_fruit_of_womb_ground_beast', 'iron_yoke_on_neck', 'cursed_basket_and_trough', 'serving_wood_and_stone_among_nations', 'sons_daughters_given_to_another_people', 'siege_in_all_gates_walls_fall', 'ox_ass_flock_taken', 'image_maker_cursed', 'sons_daughters_into_captivity', 'israel_declared_the_lord_god', 'whole_stones_altar_commanded', 'six_tribes_on_gerizim_to_bless', 'statutes_this_day_commanded', 'curses_pursue_until_destroyed', 'heavens_good_treasure_opened', 'trembling_heart_no_rest', 'cursed_in_city_and_field', 'smitten_before_enemies_seven_ways', 'tithe_in_uncleanness_barred', 'head_not_tail'}
present = sorted(NEW & {e for e, _ in rows})
print('israel_people rows in the one database:', len(rows), '| all distinct rows:', len(allrows), '| chapters 26-28 present:', len(present), present[:6], '...')
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
