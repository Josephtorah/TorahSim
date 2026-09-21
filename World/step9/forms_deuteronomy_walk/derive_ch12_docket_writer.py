#!/usr/bin/env python3
# 10b docket — write_ch12_docket.py DERIVED from the 9b form (write_ch11_docket.py in the forms folder) by asserted line-based substitutions (9b's own
# derive form): the machinery copied whole; the chapter, the file names, the seven parts, the verse regex, the header (ch12_docket_hdr.py) and the crowns
# (ch12_docket_crowns.py) typed; the duplicate-address rule, the LAW-by-cell and the carried counts over THIS docket's own notes kept from 9b. RUN FROM THE
# REPO ROOT.
import subprocess, os, re
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/write_ch11_docket.py', encoding='utf-8').read()
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
rep_block("# THE DEUTERONOMY WALK 9b — THE COMPILE OF CHAPTER 11", "every row read WHOLE.", [
"# THE DEUTERONOMY WALK 10b — THE COMPILE OF CHAPTER 12 (2026-09-20/21; the docket THREE RUNS under THE COST RULES' ~700 clause — D1 on \"Reread then go\",",
"# D2a in D1's window, D2b on \"Continue\" after the compaction): THE EXAM DOCKET for Deuteronomy 12:1-31, written from the scan's dump",
"# (scratchpad/ch12_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a verse of the chapter —",
"# the export's chapter 12 the DB's thirty-one verses; the TOPIC rows = the thirty Mishnah rows and the twenty-five folio ranges of the 10b design's exam,",
"# read WHOLE; the CREDITED marks = addresses already verdicted in an earlier ledger — CARRIED here with that ledger's own verdict line by",
"# ch12_credit_carry.py, or read whole here where the ledger's form carried no verdict). Every address in the dump gets ONE verdict (parts A..G on disk,",
"# each a SPEC over the dump's own addresses); the coverage is COMPUTED from the dump, never typed; the ranges' sizes are read from the scan's own print",
"# (ch12_docket_scan.out). Append-only. 9b's form (write_ch11_docket.py, derived by asserted line-based substitutions — derive_ch12_docket_writer.py):",
"# every row read WHOLE."])
rep_line("OUT = f'{ROOT}/logic/oral_triage/deu_11_ekev_reeh_exam_2026-09-20.md'", "OUT = f'{ROOT}/logic/oral_triage/deu_12_reeh_exam_2026-09-20.md'")
sub_in_line("dump = open(f'{SCR}/ch11_docket_dump.txt'", 'ch11_docket_dump', 'ch12_docket_dump')
sub_in_line("for p in 'ABC':", "'ABC'", "'ABCDEFG'")
sub_in_line("    part = f'ch11_docket_{p}'", 'ch11_docket_', 'ch12_docket_')
sub_in_line("scan = open(f'{SCR}/ch11_docket_scan.out'", 'ch11_docket_scan', 'ch12_docket_scan')
sub_in_line("verses = Counter(h for k, _, vs in ADDR if k == 'LINK' for h in re.findall(r'Deut 11:\\d+', vs))", "Deut 11:", "Deut 12:")
sub_in_line("UNCITED = [v for v in range(1, 33) if f'Deut 11:{v}' not in verses]", "range(1, 33) if f'Deut 11:{v}'", "range(1, 32) if f'Deut 12:{v}'")
sub_in_line("from ch11_credited_rows import UNRESOLVED as UNRES", "ch11_credited_rows", "ch12_credited_rows")
i = find_line("LONG = [(f'{w.replace(\"_\", \" \")} {a}-{z}', int(s), int(l))"); lines.insert(i + 1, "assert len(LONG) == 25, ('the design names twenty-five folio ranges', len(LONG), LONG)")
# the header block and the crowns block typed for chapter 12
i = find_line("hdr = (f'''# THE EXAM DOCKET"); j = [k for k in range(i + 1, len(lines)) if lines[k].rstrip() == "''')"][0]
lines[i:j + 1] = [l for l in open(f'{SP}/ch12_docket_hdr.py', encoding='utf-8').read().rstrip('\n').split('\n')]
i = find_line("crowns = '''"); j = [k for k in range(i + 1, len(lines)) if lines[k].rstrip() == "'''"][0]
lines[i:j + 1] = [l for l in open(f'{SP}/ch12_docket_crowns.py', encoding='utf-8').read().rstrip('\n').split('\n')]
sub_in_line("cite = '\\n## CITE INDEX", 'write_ch11_docket.py', 'write_ch12_docket.py')
sub_in_line("        f'the topic windows {NT}:", 'the Mishnah and Tosefta rows', 'the Mishnah rows')
out = '\n'.join(lines)
bad = [l[:90] for l in out.split('\n') if ('ch11' in l and 'write_ch11_docket.py' not in l) or 'Deut 11' in l or 'Tosefta Sotah' in l or 'blessing_and_curse' in l or 'the_discipline_retold' in l]
assert not bad, bad
open(f'{SP}/write_ch12_docket.py', 'w', encoding='utf-8').write(out)
print('written', f'{SP}/write_ch12_docket.py', len(out), 'bytes')
