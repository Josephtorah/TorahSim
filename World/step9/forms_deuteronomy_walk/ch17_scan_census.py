import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 15b: THE SCAN CENSUS EXTENDED (14b's lesson 2) — every runner's ledger_scan on israel_people (its pattern and its exclusions), AND the readback
# probes' and the tape's own substring scans (readback_probes.py and cold_run_sequence.py — every `ledger_scan(` / `LG(` / effect-substring pattern read from their
# sources), replayed on the one database AS IT NOW STANDS (the chapters' lines written by the tape's first run), the survivors printed: the seats a later chapter's
# entries move. No import of the runners — the patterns read from their sources. ch16_scan_census.py's form, extended. RUN FROM THE REPO ROOT.
import os, re, glob, sqlite3, subprocess, sys
ROOT = _ROOT
DB = ROOT + '/World/journal/data/world.sqlite'
c = sqlite3.connect('file:%s?mode=ro' % DB, uri=True)
rows = c.execute("SELECT DISTINCT effect, value FROM run_ledger WHERE entity=?", ('israel_people',)).fetchall()
allrows = c.execute("SELECT DISTINCT entity, effect, value FROM run_ledger").fetchall()
NEW = {'blemished_offering_barred', 'idolater_inquiry_required', 'two_witnesses_required', 'one_witness_barred', 'witnesses_hand_first_commanded', 'high_court_at_the_place_commanded', 'sentence_binding_commanded', 'turning_from_the_word_barred', 'king_from_the_brothers_commanded', 'foreign_king_barred', 'horses_multiplying_barred', 'return_to_egypt_barred', 'wives_multiplying_barred', 'silver_and_gold_multiplying_barred', 'law_copy_commanded', 'heart_lifting_barred', 'shoulder_cheeks_maw_owed', 'first_fleece_owed', 'priests_standing_chosen', 'levite_service_at_the_place_permitted', 'equal_portions_commanded', 'abominations_learning_barred', 'passing_through_fire_barred', 'diviner_barred', 'soothsayer_barred', 'augur_barred', 'sorcerer_barred', 'charmer_barred', 'ghost_consulting_barred', 'familiar_spirit_barred', 'necromancer_barred', 'wholeness_commanded', 'prophet_like_moses_promised', 'prophet_hearkening_commanded', 'word_required_of_the_hearer', 'false_word_test_declared', 'false_prophet_fear_barred'}
present = sorted(NEW & {e for e, _ in rows})
print('israel_people rows in the one database:', len(rows), '| all distinct rows:', len(allrows), '| chapters 17-18 present:', len(present), present[:6], '...')
def compile_pat(pat):
    try: return re.compile(pat.encode().decode('unicode_escape') if '\\\\' in pat else pat, re.I)
    except Exception as ex: return None
print('==== A. THE RUNNERS\' HOLE SCANS (ledger_scan on israel_people by a WORDS pattern) ====')
trips = 0
for f in sorted(glob.glob(ROOT + '/World/step9/cold_run_*.py')):
    src = open(f, encoding='utf-8').read(); name = os.path.basename(f)[9:-3]
    for m in re.finditer(r"^(\w+) = r\"(.+?)\"\s*$", src, re.M):
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
    for m in re.finditer(r"any\(t in e\['effect'\] for t in \((.*?)\)\)", src):   # THE DEUTERONOMY WALK 15b: the tape's DE4 form — a tuple of substrings over the effect NAMES (missed by the first census; the tape's second run read it)
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
print('==== C. THE NEW ROWS\' VALUES NAMING OTHER CHAPTERS\' EFFECT NAMES (a value that spells an earlier effect\'s name trips that effect\'s substring scans) ====')
names = sorted({e for _, e, _ in allrows} - NEW)
for e, v in sorted(newvals):
    v = str(v or ''); hit = [n for n in names if len(n) > 8 and n in v]
    if hit: print(' ', e, '->', hit[:8])
print('SCAN CENSUS DONE — runner scans tripping:', trips)
