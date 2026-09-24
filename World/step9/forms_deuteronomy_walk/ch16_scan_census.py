import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b: THE SCAN CENSUS — every runner's ledger_scan on israel_people (its pattern and its exclusions) replayed on the one database AS IT NOW
# STANDS (chapter 16's lines written by the tape's first run), the survivors printed: the seats a later chapter's entries move (the third tape run stopped at
# place_name's). No import of the runners — the patterns read from their sources. RUN FROM THE REPO ROOT.
import os, re, glob, sqlite3, subprocess
ROOT = _ROOT
DB = ROOT + '/World/journal/data/world.sqlite'
c = sqlite3.connect('file:%s?mode=ro' % DB, uri=True)
rows = c.execute("SELECT DISTINCT effect, value FROM run_ledger WHERE entity=?", ('israel_people',)).fetchall()
NEW = {'passover_at_the_place_commanded', 'passover_in_the_gates_barred', 'leaven_with_the_passover_barred', 'flesh_till_morning_barred', 'seventh_day_assembly_commanded', 'weeks_at_the_place_commanded', 'booths_at_the_place_commanded', 'three_pilgrimages_commanded', 'empty_appearance_barred', 'judges_and_officers_commanded', 'judgment_wresting_barred', 'person_respecting_barred', 'justice_pursuit_commanded', 'asherah_beside_the_altar_barred', 'pillar_barred', 'bribe_barred'}
print('israel_people rows in the one database:', len(rows), '| chapter 16 present:', sorted(NEW & {e for e, _ in rows}))
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
        try: rx = re.compile(pat.encode().decode('unicode_escape') if '\\\\' in pat else pat, re.I)
        except Exception as ex: print(' ', name, var, 'PATTERN ERROR', ex); continue
        hits = sorted({e for e, v in rows if rx.search('%s %s' % (e, v if v is not None else ''))})
        surv = [e for e in hits if e not in excl_names]
        flag = 'TRIPS' if surv else 'ok'
        print(' %-6s %-18s %-14s hits %d, excluded %d, survivors %s' % (flag, name, var, len(hits), len(excl_names), surv))
