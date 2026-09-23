#!/usr/bin/env python3
# 13b — the range-trim measure's NOTE on #207 addendum 1 (the owner: "If you think it is safe to make that change then yes" — the measure ran, the judgment: NOT SAFE, NOT ADOPTED);
# the three runs' counts READ FROM THEIR PRINTS, never typed; the measure script and its prints copied to the forms; a line inside the memory's talmud-rows-whole.md.
import os, re, subprocess, sys, shutil
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip(); SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
env = dict(os.environ, PYTHONPATH=SP); outs = {}
for tag, args in (('broad2', ['2']), ('narrow2', ['2', 'narrow']), ('narrow3', ['3', 'narrow'])):
    o = subprocess.run([sys.executable, f'{SP}/ch15_range_trim_measure.py'] + args, capture_output=True, text=True, env=env, cwd=ROOT).stdout
    open(f'{SP}/ch15_range_trim_measure_{tag}.out', 'w', encoding='utf-8').write(o)
    m = re.search(r'MARGIN (\d+) ranges (\d+) rows in ranges (\d+) trimmed (\d+) UNSAFE \(LAW/DERIVATION/DISPUTE in a trim\) (\d+) (\[.*?\])\n', o)
    k = re.search(r'\(\'Kiddushin\', \'14b\', \'22b\', (\d+), \'D2\', (\d+), (\d+),', o); b = re.search(r'\(\'Bekhorot\', \'25a\', \'28b\', (\d+), \'D2\', (\d+), (\d+),', o)
    d1 = re.search(r'D1 OUTSIDE rows (\d+) of them in a trimmed end (\d+) inside the window \(untouched\) (\d+)', o)
    outs[tag] = dict(margin=int(m.group(1)), ranges=int(m.group(2)), rows=int(m.group(3)), trimmed=int(m.group(4)), unsafe=int(m.group(5)), which=m.group(6),
                     kidd=(int(k.group(2)) + int(k.group(3))) if k else 0, bekh=(int(b.group(2)) + int(b.group(3))) if b else 0, out_all=int(d1.group(1)), out_trim=int(d1.group(2)))
B, N2, N3 = outs['broad2'], outs['narrow2'], outs['narrow3']
NOTE = (f"\n#207 ADDENDUM 1 — NOTE (2026-09-23, on the owner's question \"How much more do we have for ch 15? Why is it taking so long\" and his conditional word \"If you think it is "
        f"safe to make that change then yes\" on the whole-row rule's off-topic tails): THE RANGE-TRIM MEASURE (ch15_range_trim_measure.py — a declared folio range's TWO ENDS trimmed "
        f"to the stretch bearing the chapter's terms, a margin of segments kept; over D1's verdicted ranges THE SAFETY TEST: a LAW / DERIVATION / DISPUTE row in a trim = unsafe; "
        f"over D2's unread ranges the saving): a BROAD term list ({B['ranges']} ranges, {B['rows']} rows in them) trims {B['trimmed']} rows — the off-topic tails share the chapter's words "
        f"(the Canaanite slave still says 'slave', the jubilee's houses still say 'redeem'); the chapter's STRICT term list at margin 2 trims {N2['trimmed']} rows and catches "
        f"{N2['unsafe']} verdicted DERIVATION rows in the trims {N2['which']}, at margin 3 trims {N3['trimmed']} and catches {N3['unsafe']} {N3['which']}; of D1's {N2['out_all']} OUTSIDE rows only "
        f"{N2['out_trim']} sit in a trimmed end (margin 2) — the rest sit INSIDE the windows, where a keyword cannot cut them; for D2 the strict trim would drop {N2['kidd']} rows of "
        f"Kiddushin 14b-22b's tail and {N2['bekh']} of Bekhorot 25a-28b, of 426. THE JUDGMENT: NOT SAFE (the Gemara's argument runs past its last keyword — two derivation rows on "
        f"the interest's 'from him' and one on the walled cities' sanctity would have been dropped unread) AND NOT WORTH IT (under one row in sixteen); THE CHANGE IS NOT ADOPTED — "
        f"the whole-row rule stands as ruled 2026-09-17. WHERE THE TIME GOES: the on-topic middle of the ranges, read whole and verdicted row by row (D1: {N2['rows']} range rows "
        f"of 548; the typing of the verdicts the largest single cost), plus the fixed records at every run's clean point. THE LEVER THAT IS SAFE AND NEEDS NO RULING: at the DESIGN "
        f"step, declare a range at the SEGMENT grain from the link rows' positions and the shelf's mishnah bounds (the sugya's first and last rows read whole to fix the boundary) "
        f"instead of by whole folios — from chapter 16's design on; chapter 15's ranges stand as declared. NOTHING MOVED at D1's clean point; NEXT ON HIS WORD: D2.\n")
assert '/Users/' not in NOTE.replace('/Users/Shared', '') and not re.search(r'[֐-׿]', NOTE)
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; sd = open(SD, encoding='utf-8').read(); assert '#207 ADDENDUM 1 — NOTE' not in sd and '#207 ADDENDUM 1 — THE DOCKET D1' in sd
open(SD, 'a', encoding='utf-8').write(NOTE)
MF = f'{MEM}/talmud-rows-whole.md'; mf = open(MF, encoding='utf-8').read(); assert 'RANGE-TRIM MEASURE' not in mf
open(MF, 'a', encoding='utf-8').write(f"\n\n**2026-09-23 — THE RANGE-TRIM MEASURE (the owner: \"If you think it is safe to make that change then yes\"):** trimming a declared range's off-topic ENDS by the chapter's terms was measured over chapter 15's D1 (the state doc's #207 addendum 1 NOTE): a broad term list trims nothing, a strict list trims {N2['trimmed']} of {N2['rows']} range rows and drops {N2['unsafe']} DERIVATION rows unread — NOT SAFE, NOT ADOPTED; the rule stands. The safe lever is at the design step: declare ranges at the segment grain from the link rows and the mishnah's bounds, not by whole folios (from chapter 16 on).\n")
F = f'{ROOT}/World/step9/forms_deuteronomy_walk'
for fn in ['ch15_range_trim_measure.py', 'ch15_range_trim_measure_broad2.out', 'ch15_range_trim_measure_narrow2.out', 'ch15_range_trim_measure_narrow3.out', 'write_ch15b_trim_note.py']: shutil.copy(f'{SP}/{fn}', f'{F}/{fn}')
print('NOTE +', len(NOTE.encode()), 'bytes; state doc', os.path.getsize(SD), '; memory file', os.path.getsize(MF)); print(outs)
