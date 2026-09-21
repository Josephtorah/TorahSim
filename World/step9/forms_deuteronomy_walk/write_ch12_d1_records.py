#!/usr/bin/env python3
# THE DEUTERONOMY WALK 10b — THE DOCKET D1's close (2026-09-20): the map's "THE DOCKET D1 — AS RUN" paragraph, the state doc's #201 addendum 1, the recovery
# page's section-2 lines, the memory note and the index. EVERY COUNT PARSED from the parts' check print (ch12_d1_check.out), never typed; every text built
# whole before its file is opened; the size caps asserted; the anchors asserted once. 9b's records form (write_ch11_docket_records.py), cut to a docket
# run's clean point (the ledger is written at D2's close; MIDDOT, MISHNAH_TOPICS, RESUME and COMPILE_DEBT then). Run from the repo root.
import os, re, subprocess, sys
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SCR = os.path.dirname(os.path.abspath(__file__)); MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
R = lambda p: open(p, encoding='utf-8').read()
def W(p, s): open(p, 'w', encoding='utf-8').write(s)
P = R(f'{SCR}/ch12_d1_check.out')
m = re.search(r"D1 TOTAL (\d+) (\{.*?\}) carried (\d+) unresolved read here (\d+) read here (\d+) LAW by cell \(own notes\) (\{.*?\})", P)
NR, VD, NCAR, NUNR, NRH, LAWC = int(m.group(1)), eval(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), eval(m.group(6))
parts = {p: re.search(rf"^{p} rows (\d+) (\{{.*?\}}) carried (\d+) unresolved-read-here (\d+)", P, re.M) for p in 'ABC'}
PR = {p: (int(x.group(1)), eval(x.group(2)), int(x.group(3)), int(x.group(4))) for p, x in parts.items()}
assert sum(v[0] for v in PR.values()) == NR and NRH == NR - NCAR and NUNR + NCAR == sum(v[2] + v[3] for v in PR.values()), (PR, NR, NCAR, NUNR, NRH)
C = R(f'{SCR}/ch12_credit_carry.out'); mc = re.search(r'credited (\d+) resolved (\d+) unresolved (\d+)', C); NCRED, NRES, NUNRES = map(int, mc.groups())
U = R(f'{SCR}/ch12_docket_uncred.out'); chunks = re.findall(r'(ch12_uncred_\d\d\.txt) rows (\d+)-(\d+) \((\d+) rows, (\d+) bytes\)', U)
d1chunks = [c for c in chunks if int(c[2]) <= 581]; NUNCRED_D1 = sum(int(c[3]) for c in d1chunks); assert NUNCRED_D1 + NUNR == NRH, (NUNCRED_D1, NUNR, NRH)
vd = lambda d: ', '.join(f'{k} {d.get(k, 0)}' for k in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE'))
MAPP = f'''
THE DOCKET D1 — AS RUN (2026-09-20, on "Reread then go" after the compaction at #201 — THE FIRST OF THE DOCKET'S TWO RUNS under the cost rules' ~700 clause):
the dump's rows 0-581 — the 184 LINK rows, the 26 Mishnah rows listed as topic rows (four more among the link rows), Zevachim 112b-119b (THE STATIONS), 83a-86a
(THE BONES AND THE SINEWS) and 37a (THE ONE APPLICATION) — VERDICTED in three parts on disk (ch12_docket_A.py rows 0-209, _B.py 210-464, _C.py 465-581; SPEC =
CREDITED_SPEC + OWN, build() asserting every address of the slice matched): {NR} rows — {vd(VD)} (A {vd(PR["A"][1])}; B {vd(PR["B"][1])}; C {vd(PR["C"][1])});
credited in D1 {NCAR + NUNR} — {NCAR} CARRIED with their ledgers' own verdict lines (ch12_credit_carry.py over the dump's 540 credited addresses: {NRES} resolved,
{NUNRES} unresolved by the two forms) and {NUNR} whose ledger's form carried no verdict READ WHOLE HERE (ch12_uncred_unres_D1.txt); {NUNCRED_D1} uncredited rows READ
WHOLE in {len(d1chunks)} chunk files ({", ".join(f"{c[0]} rows {c[1]}-{c[2]} ({c[3]} rows)" for c in d1chunks)}); {NRH} ROWS READ WHOLE IN THIS RUN; LAW by cell, this
docket's own notes {LAWC}; no cut, no overlay (the parts' WHOLE dicts empty, apply_whole's counts 0). THE INSTRUMENTS derived from 9b's forms by
derive_ch12_docket_tools.py with three departures asserted: the chunk cap 27,000 → 76,000 bytes (one chunk one Read — rule C; THE CAP OVERSHOT: a 76 KB chunk of
Talmud English is ~26.7k tokens against the Read page's 25k, three chunks read in two pages — THE CAP FOR D2 IS 64,000, the derive patched at D2), the
chunker flushing at the runs' boundary (row 582 = Avodah Zarah 45a:1, computed; the boundary CROSSED, not hit — the boundary row itself was credited and
skipped, the second run's chunk still spanned it), the carry's unresolved file named ch12_uncred_unres.txt (9b's _09 name would collide with a chunk this
chapter) and split by run (D1 {NUNR}, D2 {NUNRES - NUNR}). THE CROWNS SO FAR (the parts' notes; the file's finds section typed at D2): THE RECEIPT WITHOUT THE
NAME'S REFERENT IS THE ORAL LAW — Rabbi on 12:21 'as I have commanded you': the gullet and the windpipe, the majority of one sign for a bird and two for an
animal (Chullin 28a:5, 85b:16, 86a:3; Mishnah Chullin 2:1 the value) — the_rite_of_slaughter's VALUE; the_wilderness_flesh's two arms at their Bavli seats
(Chullin 16b:14 R. Yishmael's permission, 17a:2 R. Akiva's prohibition of the stabbed flesh; 17a:9 the arms on 12:22); THE LADDER against the superfluous
verse (Makkot 18a:1-2 — Rava: the repetition designates, not the a-fortiori; R. Shimon by a-fortiori; Keritot 4b:29-5a:2 lashes per type) and THE BAR'S ONSET
at the wall (Makkot 19b:15 — 12:18 read with 12:17); the blood's reward by a-fortiori (Makkot 23b:2); THE STATIONS' SIX ROWS AT THEIR FOLIO (Zevachim
112b:9-12) with the karet matrix (112b:13-15; R. Shimon's four principles 119b:10-12) and the eleven differences with their sources (112b:16-113a:2;
119b:13-20); 12:8 read as THE VOLUNTARY OFFERINGS (117b:3 — 'fitting in his eyes' the fitting offerings) and as a PROHIBITION for the premature (114a:13;
Gilgal 'outside' relative to Shiloh, 114b:3); the Gilgal row a parameter with five arms (117a:8-117b:1; the Paschal only on the great altar, 114b:7; the
appearance offering only there, 118a:11); THE ERAS' DURATIONS (118b:13-119a:2 — 39, 14, 369, 57 to the 480th year; Seder Olam 11's fourteen at its Bavli
seat, the export's chapter EMPTY); THE TWO NOUNS OF 12:9 FOUR WAYS (119a:9-13, 119b:1-5 — rest Shiloh and inheritance Jerusalem / the reverse / both Shiloh /
both Jerusalem; 'the rest of the ark' by Numbers 10:36 — the design's beha.march DATA row confirmed; 119a:4 the two nouns teach the gap for Nov and Gibeon);
the second tithe at Nov and Gibeon disputed (119a:7-8 — 'three temples'); THE PORTION OF THE PLACE (118b:6-12 — Benjamin's strip; 33:12 ahead); THE ONE
PLACEMENT AND THE ONE APPLICATION (Zevachim 36b:20-37a:7, Sanhedrin 4a:7 — 'shall be poured' R. Yishmael / R. Akiva); THE BONES AND THE SINEWS reconciled
(86a:1-4; Mishnah 9:5-7); NO BLOOD NO FLESH (104a:4 — R. Yehoshua); FLESH IN MILK from 12:25's redundant 'you shall not eat it' (Chullin 115b:1); the limb from
the living's source divided (Chullin 102b:11-12) and its scope disputed (102a:1-7; Tosefta Chullin 7:4); the blood defined by 12:23's clause (Pesachim 16b:3);
'like water' four ways at their seats (Chullin 84a:11 no covering; Pesachim 22a:8 benefit; Chullin 33a:12 susceptibility — Mishnah Makhshirin 6:4; 35b:15
the disqualified consecrated's blood); THE NAME PRONOUNCED ONLY THERE by analogy (Sotah 38a:10 — 'to put His name there'); name_erasure_barred's three
readings at their seats (Avodah Zarah 13b:3 any sacred item; Pesachim 48a:7 the lashes; Sanhedrin 113a:3, 71a:17 the mezuzah; Shabbat 120b:10 the act, not
the cause; Temurah 28b:7 the coating); THE DEMOLITION A POSITIVE COMMAND (Sanhedrin 90a:3); THE THREE COMMANDMENTS OF THE ENTRY IN ORDER (Sanhedrin 20b:8-13);
the pilgrimage's class from 'come and bring' (Chagigah 4b:2; Tosefta Chagigah 1:1); the blemished consecrated's table (Mishnah Bekhorot 2:2-3; Bekhorot 15a:5,
15a:20 the three exclusions on 12:15; 33a:1-5 the eaters and the three seats of 'the gazelle and the hart'); the court-slaughter bar (Kiddushin 57b:15-17);
THE ANSWER SHEET'S ORDER FOLLOWING THE CHAPTER'S (Rambam's Introduction 15:74-75); the export's empty row Zevachim 83a:14. THE MIDDOT (checked in MIDDOT.md
before typing): I1 at Bekhorot 33a:1, Makkot 18a:2, 23b:2, Mishnah Chullin 10:1 (refused), Zevachim 85a:5; I2 at Bekhorot 15b:8, Keritot 3b:12, Makkot 16b:15,
19b:6, Menachot 77b:4, Sanhedrin 47b:18, Sotah 38a:10, Yevamot 73b:7, 86a:5, Zevachim 83a:3, 83a:5, 86a:7, 119a:6 — and 86a:8's FREENESS rider; E28 at
Chullin 102a:11; the juxtapositions named (Bekhorot 14b:13, Chagigah 4b:2, Keritot 3b:13, Zevachim 107a:1, 60b:4, 62b:10, Pesachim 22a:8, 22b:3, 24a:12,
Yevamot 73b:2, Zevachim 84b:7, 115a:6, 116a:2) and the do-not-read readings named (Zevachim 115b:12, 115b:15, 119b:8), no code. NEXT: D2 after a compaction.
'''
STATE = f'''
#201 ADDENDUM 1 (2026-09-20, at the close of THE DOCKET D1 of THE DEUTERONOMY WALK sitting 10b — the first of the docket's two runs, on the owner's "Reread then go" after the compaction at #201 — A CLEAN COMPACTION POINT): THE STATE: D1 = the dump's rows 0-581 (the 184 link rows, the 26 Mishnah topic rows, Zevachim 112b-119b, 83a-86a, 37a) VERDICTED in three parts on disk (<scratch>/ch12_docket_A.py, _B.py, _C.py, copied to World/step9/forms_deuteronomy_walk/; SPEC = CREDITED_SPEC + OWN; build asserts every address of the slice matched; ch12_d1_check.py's print: {NR} rows — {vd(VD)}; carried {NCAR} with their ledgers' own verdict lines (ch12_credit_carry.py: 540 credited in the dump, {NRES} resolved, {NUNRES} unresolved — {NUNR} of them in D1, read whole here); {NRH} rows read whole in this run — {NUNCRED_D1} uncredited in {len(d1chunks)} chunk files at 76,000 bytes (THREE OVER THE READ PAGE'S 25k TOKENS, read in two pages each — THE CAP FOR D2 IS 64,000) and the {NUNR} unresolved in ch12_uncred_unres_D1.txt; LAW by cell, own notes {LAWC}); the instruments derived from 9b's forms by derive_ch12_docket_tools.py (three departures asserted: the chunk cap, the runs' boundary at 582 crossed not hit, the unresolved file's name and its split by run); the map's "THE DOCKET D1 — AS RUN" paragraph (the crowns so far, the middot named). THE LEDGER NOT YET WRITTEN — the writer runs at D2's close over all the parts. NOT COMMITTED (since 4af2953): RUN A's records, the design, D1's records. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT (compact before D2). NEXT ON "Go": D2 — (1) patch derive_ch12_docket_tools.py's CAP 76000 → 64000 and rerun ch12_docket_uncred.py (the chunks for rows ≥ 582 renumbered — D1's four as read stay the record; the chunk list read from the print); (2) read the D2 chunks and ch12_uncred_unres_D2.txt ({NUNRES - NUNR} rows) whole; (3) the parts D, E, F … over rows 582-1537 in the dump's order — Avodah Zarah 45a-48b (582-704; 108 of 130 credited — chapter 7's), Chullin 16b-17a, 28a, 84a-b, 102b-103a, 113a-116a (705-932), Bekhorot 15a-16a, 33a-b (933-1013), Temurah 3b-4a, 17b (1014-1062), Makkot 13a-b, 17a-19b, 23b (1063-1185), Sotah 37b-38b (1186-1233), Sanhedrin 20b, 74a-b (1234-1284), Kiddushin 36b-37a (1285-1306), Rosh Hashanah 4a-6b (1307-1396), Yevamot 47b (1397-1415), Keritot 20b-22a (1416-1491), Megillah 9b-10a (1492-1520), Pesachim 8b (1521-1537) — the boundaries computed from the dump at D2 (these from the dump's block index printed at D1); (4) the writer derived from 9b's (derive_ch12_docket_writer.py → write_ch12_docket.py: the parts 'ABCDEF…' on disk, OUT logic/oral_triage/deu_12_reeh_exam_2026-09-20.md, the verse regex Deut 12:, range(1, 32), the header ch12_docket_hdr.py and the crowns ch12_docket_crowns.py typed, the duplicate-address rule kept, LAW-by-cell over own notes, NCARRIED / UNRES from ch12_credited_rows.py; the scan's ranges from ch12_docket_scan.out's 'THE RANGES SIZED' block — assert the regex finds twenty-five); the lint; (5) the docket's records in one call (write_ch12_docket_records.py from 9b's form: the map's "THE DOCKET — AS RUN" (both runs), MIDDOT's docket entry (every code checked before typed), MISHNAH_TOPICS' row notes (Zevachim 14 and 9-10, Avodah Zarah 3, Chullin 2, 6, 8, 10, Bekhorot 2 and 9, Temurah 3, Makkot 3, Sotah 7, Kiddushin 1, Yoma 1, Makhshirin 6, Avot 2), COMPILE_DEBT's 10b box (k) noted, the state doc's addendum 2, the recovery page, RESUME, the memory, the commit message file started); (6) copy_ch12_docket_forms.py rerun; then RUN B after a compaction (the probes Q31-Q33 to FAIL first). POST-COMPACTION REREADS: the recovery page, the map's "Sitting 10b … THE DESIGN" and its "THE DOCKET D1 — AS RUN" paragraph, MEMORY.md; for D2's parts the three D1 parts' heads (the form).
'''
MEMO = f'''
THE DOCKET D1 DONE (2026-09-20, "Reread then go" after the compaction at #201): the dump's rows 0-581 verdicted in three parts (ch12_docket_A/B/C.py — {NR} rows: {vd(VD)}; {NCAR} carried, {NRH} read whole here in four 76k chunks (three read in two pages — D2's cap 64k) and the unresolved file); the ledger written at D2; the crowns in the map's "THE DOCKET D1 — AS RUN": the receipt's referent the oral law (Chullin 28a:5), the wilderness flesh's arms (16b:14, 17a:2), the ladder (Makkot 18a:1-2), the stations at their folio (Zevachim 112b:9-12), 12:9's nouns four ways (119a:9-119b:5), the durations (118b:13-119a:2), the one application (37a:4). NEXT: D2 (rows 582-1537) after a compaction; the state doc's #201 addendum 1 the newest.
'''
MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; STATEDOC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; WALK = f'{MEM}/deuteronomy-walk.md'; IDX = f'{MEM}/MEMORY.md'
REC_EDITS = [("## 2. WHERE IT STANDS (2026-09-20, sitting 10b RUN A done; the state doc #201 the newest)", "## 2. WHERE IT STANDS (2026-09-20, 10b D1 done; the state doc #201 add. 1 the newest)"),
             ('- COMMITTED 4af2953 (NOT PUSHED). 10b RUN A DONE (the design in the map; #201). NEXT ON "Go": THE DOCKET D1 (its own run), D2, RUN B.',
              f'- COMMITTED 4af2953 (NOT PUSHED). 10b A + D1 DONE ({NR} rows in parts A-C; #201 add. 1). NEXT ON "Go": D2 (rows 582-1537), then RUN B.')]
IDX_EDIT = ("10b RUN A DONE; NEXT: the docket D1", "10b A + D1 DONE; NEXT: the docket D2")
ok = True
for a, b in REC_EDITS:
    if R(REC).count(a) != 1: print('REC ANCHOR', R(REC).count(a), a[:60]); ok = False
if R(IDX).count(IDX_EDIT[0]) != 1: print('IDX ANCHOR', R(IDX).count(IDX_EDIT[0])); ok = False
assert 'THE DOCKET D1 — AS RUN' not in R(MAP) and '#201 ADDENDUM 1' not in R(STATEDOC) and 'COMPACTION POINT #201' in R(STATEDOC)
rec = R(REC)
for a, b in REC_EDITS: rec = rec.replace(a, b)
idx = R(IDX).replace(*IDX_EDIT)
print('anchors %s; the recovery page would be %d bytes (cap 10240); MEMORY.md %d (cap 17000); D1 %d rows' % ('OK' if ok else 'BAD', len(rec.encode('utf-8')), len(idx.encode('utf-8')), NR))
assert ok and len(rec.encode('utf-8')) <= 10240 and len(idx.encode('utf-8')) <= 17000
W(MAP, R(MAP).rstrip('\n') + '\n' + MAPP); W(STATEDOC, R(STATEDOC).rstrip('\n') + '\n' + STATE); W(REC, rec); W(WALK, R(WALK).rstrip('\n') + '\n' + MEMO); W(IDX, idx)
print('written: the map, the state doc, the recovery page, the memory note, the index')
for p in (MAP, STATEDOC, REC, WALK, IDX, f'{SCR}/ch12_docket_A.py', f'{SCR}/ch12_docket_B.py', f'{SCR}/ch12_docket_C.py'):
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); print('  lint', p.replace(ROOT, '<repo>').replace(MEM, '<memory>').replace(SCR, '<scratch>'), (r.stdout.strip().split('\n')[-1])[:60])
r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/scrub_home_paths.py', '--check'], capture_output=True, text=True); print('  home-path gate:', (r.stdout + r.stderr).strip().split('\n')[-1][:90])
