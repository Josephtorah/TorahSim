#!/usr/bin/env python3
# 9b docket — write_ch11_docket.py DERIVED from the 8b form (write_ch10_docket.py in the forms folder) by asserted line-based substitutions (this sitting's
# form): the machinery copied whole; the chapter, the file names, the verse regex, the header's DECLARED text, the crowns and the tail typed; LAW-by-cell
# counted over THIS docket's own notes only (a carried note names its own docket's cells).
import subprocess, os, re
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/write_ch10_docket.py', encoding='utf-8').read()
lines = src.split('\n')
if lines[0].startswith('import os as _os'): lines = lines[2:]
def find_line(prefix):
    idx = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    assert len(idx) == 1, ('prefix not unique/absent', prefix[:60], idx); return idx[0]
def rep_line(prefix, new): lines[find_line(prefix)] = new
def rep_block(prefix_first, suffix_last, new, skip_first=False):
    i = find_line(prefix_first); js = [k for k in range(i + (1 if skip_first else 0), len(lines)) if lines[k].rstrip().endswith(suffix_last)]
    assert js, ('suffix absent', suffix_last[:60]); lines[i:js[0] + 1] = new
def sub_in_line(prefix, old, new, n=1):
    i = find_line(prefix); assert lines[i].count(old) == n, (prefix[:40], old, lines[i].count(old)); lines[i] = lines[i].replace(old, new)
if any(l.startswith('ROOT = _ROOT') for l in lines): rep_line('ROOT = _ROOT', "ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()   # RUN FROM THE REPO ROOT")
rep_block("# THE DEUTERONOMY WALK 8b — THE COMPILE OF CHAPTER 10", "every row read WHOLE from the start.", [
"# THE DEUTERONOMY WALK 9b — THE COMPILE OF CHAPTER 11 (2026-09-20; the docket its own run under THE TWO-RUN RULE, on the owner's \"Go\" after the compaction):",
"# THE EXAM DOCKET for Deuteronomy 11:1-32, written from the scan's dump (scratchpad/ch11_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah /",
"# Tosefta segment on the local shelf citing a verse of the chapter — the export's chapter 11 the DB's thirty-two verses; the TOPIC rows = the Mishnah rows,",
"# the fifteen folio ranges of the 9b box's item (n), Tosefta Sotah 8 and Tosefta Sheviit 4, read WHOLE; the CREDITED marks = addresses already verdicted in an",
"# earlier ledger — CARRIED here with that ledger's own verdict line by ch11_credit_carry.py, or read whole here where the ledger's form carried no verdict).",
"# Every address in the dump gets ONE verdict (parts A..C on disk, each a SPEC over the dump's own addresses); the coverage is COMPUTED from the dump, never",
"# typed; the ranges' sizes are read from the scan's own print (ch11_docket_scan.out). Append-only. 8b's form (write_ch10_docket.py, derived by asserted",
"# line-based substitutions — derive_ch11_docket_writer.py): every row read WHOLE."])
rep_line("OUT = f'{ROOT}/logic/oral_triage/deu_10_ekev_exam_2026-09-20.md'", "OUT = f'{ROOT}/logic/oral_triage/deu_11_ekev_reeh_exam_2026-09-20.md'")
sub_in_line("dump = open(f'{SCR}/ch10_docket_dump.txt'", 'ch10_docket_dump', 'ch11_docket_dump')
sub_in_line("    part = f'ch10_docket_{p}'", 'ch10_docket_', 'ch11_docket_')
sub_in_line("scan = open(f'{SCR}/ch10_docket_scan.out'", 'ch10_docket_scan', 'ch11_docket_scan')
sub_in_line("verses = Counter(h for k, _, vs in ADDR if k == 'LINK' for h in re.findall(r'Deut 10:\\d+', vs))", "Deut 10:", "Deut 11:")
sub_in_line("UNCITED = [v for v in range(1, 23) if f'Deut 10:{v}' not in verses]", "range(1, 23) if f'Deut 10:{v}'", "range(1, 33) if f'Deut 11:{v}'")
rep_line("LAWCELLS = Counter(m.group(1) for vd, note in V.values() if vd == 'LAW' for m in [re.search(r'\\b(F[1-6])\\b', note)] if m)",
         "LAWCELLS = Counter(m.group(1) for vd, note in V.values() if vd == 'LAW' and not note.startswith('CREDITED (') for m in [re.search(r'\\b(F[1-6])\\b', note)] if m)   # this docket's own notes; a carried note names its own docket's cells\nNCARRIED = sum(1 for vd, note in V.values() if note.startswith('CREDITED (') and '; carried) — ' in note[:200]); NREADHERE = len(ADDR) - NCARRIED")
sub_in_line("NWHOLE = sum(1 for vd, note in V.values() if '[whole:' in note)", "if '[whole:' in note)", "if '[whole:' in note and '; carried) — ' not in note[:200])")   # a carried note may hold its own docket's [whole:] mark
sub_in_line("NWHOLE = sum(1 for vd, note in V.values()", "assert NWHOLE == TOT['corrected'] == 0, (NWHOLE, TOT)", "assert NWHOLE == TOT['corrected'] == 0, (NWHOLE, TOT); assert NCARRIED == len(CRED) - len(UNRES), (NCARRIED, len(CRED), len(UNRES))")
i = find_line("assert hdr_line == 'ROWS %d LINK %d TOPIC %d CREDITED %d'")
lines.insert(i + 1, "_seen = set(); _dedup = []\nfor _k, _a, _vs in ADDR:\n    if _a in _seen: continue\n    _seen.add(_a); _dedup.append((_k, _a, _vs))\nNDUP = len(ADDR) - len(_dedup); ADDR = _dedup; NT = len(ADDR) - NL   # an address listed twice in the dump (a link row inside a chapter read whole) is taken once — computed")
rep_line("        assert addr not in V, ('duplicate verdict', addr)", "        if addr in V: assert V[addr] == (verdict, note), ('duplicate verdict differs', addr); continue")
sub_in_line("TOT = {k: sum(s[k] for s in STATS) for k in STATS[0]}", "assert TOT['rows'] == len(ADDR), TOT", "assert TOT['rows'] == len(ADDR) + NDUP, (TOT, len(ADDR), NDUP)")
# the header block, the crowns block and the tail typed for chapter 11
i = find_line("hdr = (f'# THE EXAM DOCKET"); j = [k for k in range(i, len(lines)) if lines[k].rstrip().endswith("UNCITED by any row: {UNCITED}.\\n')")][0]
lines[i:j + 1] = [l for l in open(f'{SP}/ch11_docket_hdr.py', encoding='utf-8').read().rstrip('\n').split('\n')]
i = find_line("crowns = '''"); j = [k for k in range(i + 1, len(lines)) if lines[k].rstrip() == "'''"][0]
lines[i:j + 1] = [l for l in open(f'{SP}/ch11_docket_crowns.py', encoding='utf-8').read().rstrip('\n').split('\n')]
sub_in_line("cite = '\\n## CITE INDEX", 'write_ch10_docket.py', 'write_ch11_docket.py')
rep_block("tail = (f'\\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE**", "OUTSIDE by work: {dict(NOUT)}.)\\n')", [
"tail = (f'\\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {NL}: {\", \".join(f\"{k} {n}\" for k, n in sorted(cnt_link.items()))}; '",
"        f'the topic windows {NT}: {\", \".join(f\"{k} {n}\" for k, n in sorted(cnt_topic.items()))}; all rows: {\", \".join(f\"{k} {n}\" for k, n in sorted(cnt.items()))}; credited {len(CRED)} — {NCARRIED} carried with their ledgers\\' own verdict lines and {len(UNRES)} read whole here; {NREADHERE} rows read whole in this run — the counts this script computed from the dump and the verdict lists, never typed; corrections {TOT[\"corrected\"]}; the ranges: {\"; \".join(f\"{n} {s} rows ({l} link)\" for n, s, l in LONG)}; the Mishnah and Tosefta rows {len(MISH)}; OUTSIDE by work: {dict(NOUT)}.)\\n')"])
# UNRES read from the carry's file
i = find_line("V = {}; STATS = []"); lines.insert(i, "from ch11_credited_rows import UNRESOLVED as UNRES   # the credited rows the carry could not resolve (read whole here)")
sub_in_line("print('rows', len(ADDR), 'link', NL, 'topic', NT, 'credited', len(CRED), '(link', ncred_link, 'topic', ncred_topic, ')')", "'topic', ncred_topic, ')')", "'topic', ncred_topic, ')', 'carried', NCARRIED, 'unresolved_read_here', len(UNRES), 'read_here', NREADHERE, 'dup_dropped', NDUP)")
out = '\n'.join(lines)
bad = [l[:90] for l in out.split('\n') if ('ch10' in l and 'write_ch10_docket.py' not in l) or 'Deut 10' in l or 'Shekalim' in l or 'Seder Olam' in l or 'second_tablets' in l]
assert not bad, bad
open(f'{SP}/write_ch11_docket.py', 'w', encoding='utf-8').write(out)
print('written', f'{SP}/write_ch11_docket.py', len(out), 'bytes')
