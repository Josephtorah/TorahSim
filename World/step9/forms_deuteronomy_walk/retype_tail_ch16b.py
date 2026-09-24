import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK 14b: after the chain's first pass — the state doc's #210 carries the NOTE (the first pass's two gates, the two filings, the relaunch); the tail's
# writers and the copier retyped for the two passes and the lesson's fifth seat (Q33). Plain replacements, each asserted once.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
sd = open(SD, encoding='utf-8').read()
i = sd.index('\n#210 ('); assert sd.find('\n#', i + 5) < 0 and 'NOTE (before the compaction)' not in sd
first = open(f'{SP}/ch16b_gates_SUMMARY_first.txt', encoding='utf-8').read()
t_first = re.search(r'^FAIL probes rc=1 \((\d+)s\)', first, re.M).group(1); t_tape = re.search(r'^PASS tape \((\d+)s\)', first, re.M).group(1)
NOTE = " — NOTE (2026-09-23, before the compaction; the chain's first pass read once when the harness notified): THE FIRST PASS (536 s) stopped at TWO gates — the probes (readback 42/43: Q33, chapter 12's hole probe, matched 16:5's passover_in_the_gates_barred by the substring 'in_the_gates' — the lesson's fifth seat, DD4's twin) and the dependency gate (the live registration edge sequence -> festivals_judges unfiled — 13b's precedent); the tape (%ss, 10/10), the daemon gate, the build, the journal gate and THE REGISTER GATE --strict PASSED; the five long steps skipped. FILED FROM THE PRINTS: the registration edge (patch_deps_ch16b.py; the gate green alone), Q33 retyped (patch_probe_q33_ch16.py). THE SECOND PASS RELAUNCHED FROM THE TAPE (a pass after any source change starts at the tape) — its summary <scratch>/ch16b_gates_SUMMARY.txt, its prints <scratch>/ch16b_gates/; the first pass kept as <scratch>/ch16b_gates_SUMMARY_first.txt and <scratch>/ch16b_gates_first/. THE TAIL reads the second pass's summary once." % t_tape
sd = sd.rstrip('\n') + NOTE + '\n'
open(SD, 'w', encoding='utf-8').write(sd); print('#210 NOTE appended (%d bytes)' % len(NOTE.encode()))
def edit(name, pairs):
    p = f'{SP}/{name}'; s = open(p, encoding='utf-8').read()
    for old, new in pairs:
        assert s.count(old) == 1, (name, s.count(old), old[:80]); s = s.replace(old, new)
    open(p, 'w', encoding='utf-8').write(s); print(name, 'retyped:', len(pairs))
edit('write_ch16b_records.py', [
    ("THE CHAIN ONCE — ALL GREEN in %d s (%d steps; the probes %s; %s; the positions %s; the sweep %s); the readback probes %s.", "THE CHAIN IN TWO PASSES — the first (536 s) stopped at the probes (Q33: chapter 12's hole probe matched 16:5's block — the lesson's fifth seat) and the dependency gate (the registration edge sequence -> festivals_judges unfiled — 13b's precedent), the tape, the daemon gate, the build, the journal gate and the register gate --strict passing; both filed from the prints; THE SECOND PASS from the tape ALL GREEN in %d s (%d steps; the probes %s; %s; the positions %s; the sweep %s); the readback probes %s."),
    ("(3) FOUR SCAN SEATS widened for chapter 16's entries — second_tablets' BRIBE_SCAN (at the design) and LAW_SCAN, place_name's PLACE_SCAN (found by the tape's second and third runs), and the tape's DD4 (found by the first run) — a later chapter's writes move an earlier chapter's hole scan once the tape's first run puts them in the one database;", "(3) FIVE SCAN SEATS widened for chapter 16's entries — second_tablets' BRIBE_SCAN (at the design) and LAW_SCAN, place_name's PLACE_SCAN (found by the tape's second and third runs), the tape's DD4 (found by the first run) and the probes' Q33 (found by the chain's first pass) — a later chapter's writes move an earlier chapter's hole scan once the tape's first run puts them in the one database;"),
    ("(second_tablets twice, place_name once, DD4 on the tape — four seats, three tape runs to find them one by one;", "(second_tablets twice, place_name once, DD4 on the tape, Q33 in the probes — five seats, three tape runs and a chain pass to find them one by one;"),
    ("an earlier chapter's scan of the one database moves with a later chapter's entries (four seats — the scan census the instrument); the old runners' cells take question keys;", "an earlier chapter's scan of the one database moves with a later chapter's entries (five seats — the scan census the instrument, extended to the probes' and the tape's own scans next sitting); the old runners' cells take question keys;"),
    ("NOTE210 = \" — THE TAIL (2026-09-23, after the compaction; on the owner's word): the chain's SUMMARY read once — ALL GREEN in %d s", "NOTE210 = \" — THE TAIL (2026-09-23, after the compaction; on the owner's word): the second pass's SUMMARY read once — ALL GREEN in %d s"),
    ("'the gates chain ALL GREEN once; UNCOMMITTED; NEXT the commit, then 15) — COMMITTED AND PUSHED THROUGH e824e52'", "'the gates chain ALL GREEN on its second pass; UNCOMMITTED; NEXT the commit, then 15) — COMMITTED AND PUSHED THROUGH e824e52'"),
    ("SITTING 14b DONE 2026-09-23 (the tail): the gates chain ALL GREEN in one pass (%d steps, %d s — the positions at four workers, the sweep %s);", "SITTING 14b DONE 2026-09-23 (the tail): the gates chain ALL GREEN on its second pass (%d steps, %d s — the positions at four workers, the sweep %s; the first pass stopped at Q33 and the registration edge, both filed from the prints);"),
])
edit('write_ch16b_commit_msg.py', [
    ("THE GATES CHAIN ONCE — ALL GREEN in %d s (%d steps; the positions at four workers; the sweep %s);", "THE GATES CHAIN IN TWO PASSES — the first stopped at chapter 12's hole probe Q33 (16:5's block matched by substring) and the unfiled registration edge, both filed from the prints; the second from the tape ALL GREEN in %d s (%d steps; the positions at four workers; the sweep %s);"),
    ("an earlier chapter's scan of the one database moves with a later chapter's entries (four seats; the scan census the instrument);", "an earlier chapter's scan of the one database moves with a later chapter's entries (five seats; the scan census the instrument);"),
])
edit('copy_ch16b_forms.py', [
    ("'ch16_scan_census.py', 'retype_writers_ch16b.py', 'patch_deps_ch16.py',", "'ch16_scan_census.py', 'retype_writers_ch16b.py', 'retype_point_cap_ch16b.py', 'retype_tail_ch16b.py', 'patch_deps_ch16.py', 'patch_deps_ch16b.py', 'patch_probe_q33_ch16.py',"),
    ("'ch16b_dependency_after.out', 'ch16b_gates_SUMMARY.txt',", "'ch16b_dependency_after.out', 'ch16b_dependency_after2.out', 'ch16b_gates_SUMMARY_first.txt', 'ch16b_gates_SUMMARY.txt',"),
    ("# the gates chain's own outputs (the step prints) copied under the sitting's prefix\nfor f in sorted(glob.glob(f'{SP}/ch16b_gates/*')):", "# the gates chain's own outputs (the step prints) copied under the sitting's prefix — the first pass's under gates_ch16b_first_\nfor f in sorted(glob.glob(f'{SP}/ch16b_gates_first/*')):\n    text = open(f, encoding='utf-8', errors='replace').read().replace(SP, '<scratch>').replace(ROOT, '<repo>').replace(HOME, '<home>')\n    open(f'{FD}/gates_ch16b_first_{os.path.basename(f)}', 'w', encoding='utf-8').write(text); n += 1\nfor f in sorted(glob.glob(f'{SP}/ch16b_gates/*')):"),
])
