#!/usr/bin/env python3
# THE DEUTERONOMY WALK 13b THE TAIL (2026-09-23): the chain story built from the passes' prints (the first and fourth summaries kept aside, the fifth live, the
# positions run, the sweep) and the timing rows for the five passes appended (each pass's seconds the sum of its summary's step seconds; the second pass's and the
# third's from their prints as read — the files overwritten by the passes after them). RUN AFTER THE FIFTH PASS, FROM THE REPO ROOT.
import os, re, sys, subprocess, datetime
SP = os.path.dirname(os.path.abspath(__file__)); G = f'{SP}/gates_ch15b'
def rd(p): return open(p if p.startswith('/') else f'{SP}/{p}', encoding='utf-8', errors='ignore').read()
def secs(summ): return sum(int(s) for s in re.findall(r'\((\d+)s\)', summ))
def steps(summ): return re.findall(r'^(PASS|FAIL) (\w+)', summ, re.M)
s1 = rd('ch15b_chain_summary_first.txt'); s4 = rd('ch15b_chain_summary_fourth.txt'); s5 = rd(f'{G}/SUMMARY.txt')
assert 'FAIL probes' in s1 and 'FAIL dependency' in s1 and s1.count('PASS ') == 5, s1
assert 'GATES CHAIN DONE — ALL GREEN' in s4 and s4.count('PASS ') == 7, s4
assert 'GATES CHAIN DONE — ALL GREEN' in s5 and [n for _, n in steps(s5)] == ['checkpoint', 'stamp', 'sweep', 'unmoved'], s5
rb1 = rd('ch15b_chain_readback_first.out'); assert 'readback_probes: 41/42' in rb1 and 'FAIL Q17' in rb1
d1 = rd('ch15b_chain_dependency_first.out'); DEM = [l.strip()[5:] for l in d1.splitlines() if l.startswith('  FAIL ')]; assert len(DEM) == 5
t3 = rd('ch15b_chain_tape_third.out'); assert '9/10 checkpoints' in t3 and 'CHECKPOINT DG7 ' in t3
po = rd(f'{G}/positions.out'); PO = re.search(r'THE FALLS: (\d+) checkpoints over (\d+) pauses in (\d+) s \((\d+) workers\); at pause 0 \(before any line\) (\d+); the last fall at pause (\d+) \((.*?)\)', po); assert PO, po[-400:]
sw = rd(f'{G}/sweep.out'); SW_P = len(re.findall(r'^PASS +cold_run_\w+\.py', sw, flags=re.M)); SW_F = len(re.findall(r'^FAIL +cold_run_\w+\.py', sw, flags=re.M)); assert SW_F == 0 and SW_P >= 69, (SW_P, SW_F)
ck = rd(f'{G}/checkpoint.out'); CK = re.findall(r'(\d+)/7', ck); assert CK and CK[-1] == '7', CK
sec = {n: int(x) for n, x in re.findall(r'^(?:PASS|FAIL) (\w+)[^\n]*?\((\d+)s\)', s5, re.M)}
t1 = secs(s1); t4 = secs(s4); t5 = secs(s5); t2 = 398 + 4 + 2 + 61 + 33 + 16; t3s = 32
story = (f"THE GATES CHAIN FIVE PASSES — (1) the first pass ({t1} s, LAUNCHED at RUN B's end, its summary read once when the harness notified) stopped at TWO gates: the probes (readback 41/42 — Q17, chapter 7's probe, "
         "counting blessings_for_hearing ONE at its tenth seat against the tape's TWO: the design's grep had listed the line CUT AT 200 CHARACTERS with the name past the cut, CU5's twin) and the dependency gate with FIVE demands "
         "(release_firstborn -> family at 15:4 [inheritance]; -> pesach at 15:19, 15:21 [firstborn, pesach]; -> mishpatim dispositioned CALL with no live import edge — the F1 TABLE read; the live registration edge sequence -> release_firstborn unfiled; "
         "the pointer Deut 15:6 AS_WHEN 'as He spoke to you' undispositioned); the tape, the daemon gate, the build, the journal gate and THE REGISTER GATE --strict PASSED; the five long steps skipped; (2) THE SIX DEMANDS FILED FROM THE PRINTS "
         "(patch_tail_ch15b.py: Q17's tenth seat 1 -> 2 with its why; family FALSE with the gift formula's seats COMPUTED by lemma on the Tanakh database — 4:21, 4:38, 12:9, 15:4, 19:10, 19:14, 20:16, 21:23, 24:4, 25:19, 26:1, 29:7; pesach VIA korach "
         "(korach imports pesach — verified at its line 31) with 'lame' named as the Passover's consonantal homograph; mishpatim CALL -> PARAMETER, carries value, the runner's import comment amended; the registration edge, link none; the pointer OWED, "
         "link hypothesis, its why's prefix 10b's 'THE RECEIPT'S THIRD AND FOURTH SHAPES' line already in COMPILE_DEBT.md); the dependency gate alone GREEN in 2 s; (3) the second pass --from probes ({t2} s; its summary overwritten by the third — the "
         "seconds as read) REFUSED BY THE READERS: the runner's source had changed after the last tape run (the comment), the saved world's digest no longer matched, and the readback and register probes each ran the world THEMSELVES under the live "
         "session's source name — the one removed the .live journal at its seal, the other found it gone (FileNotFoundError), the register probe's audit index_equal False, the journal gate's run 9/10 — the rule 'never a second stepper under the live "
         "name' broken by the skip itself: A PASS AFTER ANY SOURCE CHANGE STARTS AT THE TAPE; (4) the third pass from the tape ({t3s} s to the tape's verdict, then KILLED) — the tape 9/10, DG7 DIVERGE: the checkpoint counts the CALL edges from "
         "release_firstborn on file, twenty-one at the tape's first run and TWENTY after the tail's own filing (mishpatim's PARAMETER) — RETYPED FROM THE YAML'S OWN COUNT (patch_tape_dg7_ch15.py: reference 18, transfer 2, one pointer); (5) the fourth "
         f"pass from the tape ({t4} s) ALL GREEN through the register gate — the tape, the probe suites (readback 42/42, census 224/224, installation 6/6, register 7/7), the daemon gate, the dependency gate, the build, the journal gate, THE REGISTER "
         f"GATE --strict; (6) THE POSITIONS TABLE BY FOUR WORKERS outside the chain (the step's own command; the eight-worker step skipped — 12b's precedent): {PO.group(1)} checkpoints over {PO.group(2)} pauses in {PO.group(3)} s, {PO.group(5)} at pause 0, "
         f"the last fall at pause {PO.group(6)} ({PO.group(7)}) — DG1-DG9 in the table; (7) the fifth pass --from checkpoint ({t5} s) ALL GREEN: checkpoint {CK[-1]}/7, the journal stamped, the sweep {SW_P}/{SW_P} in {sec.get('sweep', '?')} s, the journal UNMOVED. "
         "THE LESSONS OF THE CHAIN: a pass after any source change starts at the tape (the readers' snapshot is keyed by the sources' digest); a filing at the tail moves the checkpoint that counts the file (DG7) — the tape reruns after the filing; "
         "the chain's failures arrive after the clean point and the NOTE beneath an addendum carries them.")
assert '\n' not in story
open(f'{SP}/ch15b_chain_story.txt', 'w', encoding='utf-8').write(story + '\n')
rows = [('13b T the gates chain, first pass (tape, probes FAIL, daemon, dependency FAIL, build, journal, register; five skipped)', t1, 1),
        ('13b T the gates chain, second pass (--from probes: the readers ran the world under the live name — refused; from the print, the file overwritten)', t2, 1),
        ('13b T the gates chain, third pass (from the tape: DG7 DIVERGE after the filing; killed)', t3s, 1),
        ('13b T the gates chain, fourth pass (from the tape: ALL GREEN through the register gate)', t4, 0),
        ('13b T the gates chain, fifth pass (--from checkpoint: checkpoint, stamp, sweep, unmoved — ALL GREEN)', t5, 0)]
with open(f'{SP}/ch15b_timing.tsv', 'a', encoding='utf-8') as f:
    for name, s, rc in rows: f.write('%s\t%s\t%d\t%d\n' % (datetime.datetime.now().strftime('%H:%M:%S'), name, s, rc))
print('the chain story written:', len(story), 'bytes; the passes', (t1, t2, t3s, t4, t5), '; positions', PO.groups()[:3], '; sweep', SW_P, '; checkpoint', CK[-1])
