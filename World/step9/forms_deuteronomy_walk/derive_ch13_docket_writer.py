#!/usr/bin/env python3
# 11b docket — write_ch13_docket.py DERIVED from the 10b form (write_ch12_docket.py in the forms folder) by asserted line-based substitutions (10b's own
# derive form): the machinery copied whole; the chapter, the file names, the four parts, the verse regex and range, the fourteen ranges ASSERTED, the header
# (ch13_docket_hdr.py) and the crowns (ch13_docket_crowns.py) typed; the duplicate-address rule, the LAW-by-cell and the carried counts kept. RUN FROM THE
# REPO ROOT.
import subprocess, os, re
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/write_ch12_docket.py', encoding='utf-8').read()
lines = src.split('\n')
def find_line(prefix):
    idx = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    assert len(idx) == 1, ('prefix not unique/absent', prefix[:60], idx); return idx[0]
def rep_line(prefix, new): lines[find_line(prefix)] = new
def rep_block(prefix_first, suffix_last, new, skip_first=False):
    i = find_line(prefix_first); js = [k for k in range(i + (1 if skip_first else 0), len(lines)) if lines[k].rstrip().endswith(suffix_last)]
    assert js, ('suffix absent', suffix_last[:60]); lines[i:js[0] + 1] = new
def sub_in_line(prefix, old, new, n=1):
    i = find_line(prefix); assert lines[i].count(old) == n, (prefix[:40], old, lines[i].count(old)); lines[i] = lines[i].replace(old, new)
rep_block("# THE DEUTERONOMY WALK 10b — THE COMPILE OF CHAPTER 12", "every row read WHOLE.", [
"# THE DEUTERONOMY WALK 11b — THE COMPILE OF CHAPTER 13 (2026-09-21; the docket ONE RUN under THE COST RULES' ~700 clause, on the owner's \"Run\" after the",
"# compaction at #203): THE EXAM DOCKET for Deuteronomy 13:1-19, written from the scan's dump (scratchpad/ch13_docket_dump.txt: the LINK rows = every",
"# Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a verse of the chapter — the English numbering's 12:32 folded to 13:1; the TOPIC",
"# rows = the twenty-two Mishnah rows, the fourteen folio ranges and the twelve whole-chapter rows of the 11b design's exam, read WHOLE; the CREDITED marks =",
"# addresses already verdicted in an earlier ledger — CARRIED here with that ledger's own verdict line by ch13_credit_carry.py, or read whole here where the",
"# ledger's form carried no verdict — the shared file ch13_docket_U.py). Every address in the dump gets ONE verdict (parts A..D on disk, each a SPEC over the",
"# dump's own addresses); the coverage is COMPUTED from the dump, never typed; the ranges' sizes are read from the scan's own print (ch13_docket_scan.out).",
"# Append-only. 10b's form (write_ch12_docket.py, derived by asserted line-based substitutions — derive_ch13_docket_writer.py): every row read WHOLE."])
rep_line("OUT = f'{ROOT}/logic/oral_triage/deu_12_reeh_exam_2026-09-20.md'", "OUT = f'{ROOT}/logic/oral_triage/deu_13_reeh_exam_2026-09-21.md'")
sub_in_line("dump = open(f'{SCR}/ch12_docket_dump.txt'", 'ch12_docket_dump', 'ch13_docket_dump')
sub_in_line("for p in 'ABCDEFG':", "'ABCDEFG'", "'ABCD'")
sub_in_line("    part = f'ch12_docket_{p}'", 'ch12_docket_', 'ch13_docket_')
sub_in_line("scan = open(f'{SCR}/ch12_docket_scan.out'", 'ch12_docket_scan', 'ch13_docket_scan')
sub_in_line("verses = Counter(h for k, _, vs in ADDR if k == 'LINK' for h in re.findall(r'Deut 12:\\d+', vs))", "Deut 12:", "Deut 13:")
sub_in_line("UNCITED = [v for v in range(1, 32) if f'Deut 12:{v}' not in verses]", "range(1, 32) if f'Deut 12:{v}'", "range(1, 20) if f'Deut 13:{v}'")
sub_in_line("from ch12_credited_rows import UNRESOLVED as UNRES", "ch12_credited_rows", "ch13_credited_rows")
sub_in_line("assert len(LONG) == 25, ('the design names twenty-five folio ranges', len(LONG), LONG)", "25, ('the design names twenty-five", "14, ('the design names fourteen")
# the header block and the crowns block typed for chapter 13
i = find_line("hdr = (f'''# THE EXAM DOCKET"); j = [k for k in range(i + 1, len(lines)) if lines[k].rstrip() == "''')"][0]
lines[i:j + 1] = [l for l in open(f'{SP}/ch13_docket_hdr.py', encoding='utf-8').read().rstrip('\n').split('\n')]
i = find_line("crowns = '''"); j = [k for k in range(i + 1, len(lines)) if lines[k].rstrip() == "'''"][0]
lines[i:j + 1] = [l for l in open(f'{SP}/ch13_docket_crowns.py', encoding='utf-8').read().rstrip('\n').split('\n')]
sub_in_line("cite = '\\n## CITE INDEX", 'write_ch12_docket.py', 'write_ch13_docket.py')
out = '\n'.join(lines)
bad = [l[:90] for l in out.split('\n') if ('ch12' in l and 'write_ch12_docket.py' not in l) or 'Deut 12' in l or 'place_name' in l or 'three runs' in l or 'the_header_and_the_demolition' in l]
assert not bad, bad
open(f'{SP}/write_ch13_docket.py', 'w', encoding='utf-8').write(out)
print('written', f'{SP}/write_ch13_docket.py', len(out), 'bytes')
