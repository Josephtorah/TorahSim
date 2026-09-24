import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b (2026-09-23): THE LEAN RECON for the compile of chapter 16 — what the tape, the registries, the dispositions, the probes and the
# running world say BEFORE a line is typed (13b's recon cut to the lean form: no docket scan; the kin's cells found by a STATIC scan of every runner's defs
# for the kin verses' refs, no import). Every number printed, never typed. RUN FROM THE REPO ROOT.
import os, re, sys, subprocess, io, contextlib, collections, glob
ROOT = _ROOT
sys.path.insert(0, ROOT + '/World/step9')
import yaml
S9 = ROOT + '/World/step9'
print('==== A. THE TAPE (cold_run_sequence.py) ====')
seq = open(S9 + '/cold_run_sequence.py', encoding='utf-8').read(); L = seq.split('\n')
for i, l in enumerate(L, 1):
    if re.match(r'^(RUN|PREVIOUS_RUN|NEWEST_RUNNER|PLACEMENT) = ', l): print('%d: %s' % (i, l[:170]))
    if re.match(r'^\s+\d+\)\s+#', l): print('%d: %s' % (i, l[:120]))
print('import lines:', sum(1 for l in L if l.startswith('import cold_run_')), '| DAEMON_ORDER tuples:', len(re.findall(r"^\s+\('cold_run_\w+', 'law_\w+'\)", seq, re.M)))
cps = re.findall(r"cp\('([A-Z]{2}\d+) ", seq); print('checkpoints:', len(cps), '| the D series in use:', sorted({c[:2] for c in cps if c[0] == 'D'}), '| last:', cps[-1])
vl = [l for l in L if "'DG9 MATCH'" in l]; print('VERDICTS DG line:', [l[:160] for l in vl])
m = re.search(r"^CENSUS_EXPECTED = .*$", seq, re.M); print('CENSUS_EXPECTED:', m.group(0)[:200] if m else '(no such line)')
print('lines naming Deut 16:', [(i, l[:120]) for i, l in enumerate(L, 1) if 'Deut 16' in l][:12])
print('==== B. THE DISPOSITIONS ====')
dep = yaml.safe_load(open(S9 + '/dependency_dispositions.yaml', encoding='utf-8'))
print('edges', len(dep['edges']), '| pointers', len(dep.get('pointers', [])), '| spans', len(dep['spans']))
print('edges/pointers naming Deut 16 or festivals_judges:', [e for e in dep['edges'] if 'festivals_judges' in str(e) or 'Deut 16' in str(e)][:5], [p for p in dep.get('pointers', []) if 'Deut 16' in str(p) or 'festivals_judges' in str(p)][:5])
print('a span example:', dep['spans'].get('release_firstborn') if isinstance(dep['spans'], dict) else dep['spans'][-1])
print('an edge example (release_firstborn -> seducers):', [e for e in dep['edges'] if e.get('from') == 'release_firstborn' and e.get('to') == 'seducers'])
print('a pointer example (release_firstborn):', [p for p in dep.get('pointers', []) if 'release_firstborn' in str(p)][:2])
dd = yaml.safe_load(open(S9 + '/daemon_dispositions.yaml', encoding='utf-8'))
print('daemons', len(dd['daemons']), '| functions (runners)', len(dd['functions']), '| law_release_firstborn:', dd['daemons'].get('law_release_firstborn'))
print('functions release_firstborn:', dd['functions'].get('release_firstborn'))
rg = yaml.safe_load(open(S9 + '/register_dispositions.yaml', encoding='utf-8'))
print('register keys:', list(rg.keys()), '| seats naming Deut 16:', [k for sec in rg.values() if isinstance(sec, dict) for k in sec if 'Deut 16' in str(k)])
print('==== C. THE PROBES ====')
ip = open(S9 + '/installation_probes.py', encoding='utf-8').read().split('\n')
print('I5 lines:', [(i, l[:200]) for i, l in enumerate(ip, 1) if re.search(r"'I5|I5 ", l)][:4])
rp = open(S9 + '/readback_probes.py', encoding='utf-8').read().split('\n')
print('readback defs:', [l[:40] for l in rp if re.match(r'^def q\d+', l)][-3:], '| PROBES list lines:', [(i, l[:200]) for i, l in enumerate(rp, 1) if re.match(r'^(PROBES|    \(q4|SUITE|def main|if __name__)', l)][:8])
print('==== D. THE REGISTRIES ====')
fx = yaml.safe_load(open(S9 + '/effect_vocabulary.yaml', encoding='utf-8'))['effects']; ev = yaml.safe_load(open(S9 + '/event_vocabulary.yaml', encoding='utf-8'))['events']
NEW_E = ['passover_at_the_place_commanded', 'passover_in_the_gates_barred', 'leaven_with_the_passover_barred', 'flesh_till_morning_barred', 'seventh_day_assembly_commanded', 'weeks_at_the_place_commanded', 'booths_at_the_place_commanded', 'three_pilgrimages_commanded', 'empty_appearance_barred', 'judges_and_officers_commanded', 'judgment_wresting_barred', 'person_respecting_barred', 'justice_pursuit_commanded', 'asherah_beside_the_altar_barred', 'pillar_barred']
NEW_K = ['passover_at_the_place_declared', 'weeks_and_booths_declared', 'three_pilgrimages_declared', 'judges_in_every_gate_commanded', 'asherah_and_pillar_barred']
print('effects', len(fx), '| kinds', len(ev), '| the fifteen new effects present before:', [e for e in NEW_E if e in fx], '| the five kinds present before:', [k for k in NEW_K if k in ev])
print('near names (effects containing passover|pilgrim|judges|justice|asherah|pillar|booth|weeks):', [e for e in fx if re.search(r'passover|pilgrim|judges|justice|asherah|pillar|booth|weeks', e)])
for e in ('bribe_barred', 'appearance_owed', 'appearance_gift_owed', 'judgment_perverted', 'courts_established', 'judges_charged', 'rejoicing_before_the_lord_commanded', 'place_chosen_required', 'burn_remainder', 'counts_omer', 'dwells_in_booths', 'passover_in_its_time'):
    print(' E', e, fx[e])
print('a statute kind row (second_tithe_declared):', ev.get('second_tithe_declared'))
print('==== E. THE CALENDAR ====')
cal = yaml.safe_load(open(S9 + '/calendar_parameters.yaml', encoding='utf-8'))
for k in ('festival_dates', 'omer_day', 'intercalated_month', 'intercalation_grounds', 'intercalation_threshold_days', 'between_the_evenings_from', 'night_start', 'day_boundary', 'twilight_doubt', 'the_removal_date'):
    print(' C', k, '=', cal['parameters'].get(k))
print('==== F. THE KIN\'S CELLS BY STATIC SCAN (every runner\'s defs; the refs they name among the kin verses) ====')
KIN = re.compile(r'\b(Deut 16:\d+|Exod 12:(?:[1-9]|1\d|20)\b|Exod 13:(?:[3-9]|10)\b|Exod 23:(?:[1-9]|1[4-9])\b|Exod 34:(?:13|1[8-9]|2[0-6])\b|Lev 23:\d+|Num 28:\d+|Num 29:\d+|Exod 18:(?:1[3-9]|2[0-6])\b|Lev 19:15|Lev 26:1\b|Deut 1:(?:9|1[0-8])\b|Deut 7:5|Deut 12:3|Exod 20:2[1-3]|2 Chr 8:13|Deut 5:15)')
for f in sorted(glob.glob(S9 + '/cold_run_*.py')):
    src = open(f, encoding='utf-8').read(); name = os.path.basename(f)[9:-3]
    if name == 'sequence': continue
    for m in re.finditer(r'^def ([a-z_0-9]+)\(.*?(?=^def |\Z)', src, re.S | re.M):
        refs = sorted(set(KIN.findall(m.group(0))))
        if refs:
            asks = re.findall(r"if ask == '([a-z_0-9]+)':", m.group(0))
            print(' %s.%s: refs %s | asks %d %s' % (name, m.group(1), refs[:14], len(asks), asks[:24]))
print('==== G. THE RUNNING WORLD (the snapshot) ====')
try:
    import register_census as R
    with contextlib.redirect_stdout(io.StringIO()):
        w = R.running_world()
    def nall(eff): return [(ent.name if hasattr(ent, 'name') else k, e.get('op')) for k, ent in w.entities.items() for e in ent.ledger if e['effect'] == eff]
    for eff in ('bribe_barred', 'appearance_owed', 'appearance_gift_owed', 'judgment_perverted', 'courts_established', 'judges_charged', 'rejoicing_before_the_lord_commanded', 'place_chosen_required', 'burn_remainder', 'counts_omer', 'dwells_in_booths', 'passover_in_its_time', 'pillar_raised', 'pillar_anointed', 'pillar_leads', 'matzot_made', 'high_places_banned', 'name_erasure_barred', 'holy_things_in_the_gates_barred') + tuple(NEW_E):
        print(' W', eff, len(nall(eff)), nall(eff)[:6])
    isr = w.entities['israel'].ledger if 'israel' in w.entities else []
    print(' israel ledger entries', len(isr), '| open debits', len([e for e in isr if e.get('op') == 'debit' and not e.get('closed_by')]), '| blocks', len([e for e in isr if e.get('op') == 'block']))
    print(' entities', len(w.entities), '| closes', len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')]), '| markers', len([l for l in w.log if l[0] == 'MARKER']), '| events', len([l for l in w.log if l[0] == 'EVENT']), '| the day', w.clock.eras['exodus'].date(w.clock.day), '| population rows', len(w.tables['population']))
    last = [l[2] for l in w.log if l[0] == 'EVENT'][-6:]; print(' the tape\'s last six events:', [(e['kind'], str(e.get('case_source', ''))[:12]) for e in last])
except Exception as ex:
    import traceback; traceback.print_exc(); print(' THE SNAPSHOT FAILED:', repr(ex))
print('RECON DONE')
