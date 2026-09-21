#!/usr/bin/env python3
# THE DEUTERONOMY WALK 10b — THE DOCKET D2a's close (2026-09-20): the map's "THE DOCKET D2a — AS RUN" paragraph, the state doc's #201 addendum 2, the
# recovery page's section-2 lines, the memory note and the index. EVERY COUNT PARSED from the part's check print (ch12_d2_check.out), never typed; every
# text built whole before its file is opened; the caps and the anchors asserted. write_ch12_d1_records.py's form. Run from the repo root.
import os, re, subprocess, sys
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SCR = os.path.dirname(os.path.abspath(__file__)); MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
R = lambda p: open(p, encoding='utf-8').read()
def W(p, s): open(p, 'w', encoding='utf-8').write(s)
P = R(f'{SCR}/ch12_d2_check.out')
m = re.search(r"^D TOTAL (\d+) (\{.*?\}) carried (\d+) unresolved read here (\d+) read here (\d+) LAW by cell \(own notes\) (\{.*?\})", P, re.M)
NR, VD, NCAR, NUNR, NRH, LAWC = int(m.group(1)), eval(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), eval(m.group(6))
assert NRH == NR - NCAR, (NRH, NR, NCAR)
P1 = R(f'{SCR}/ch12_d1_check.out'); m1 = re.search(r"D1 TOTAL (\d+) (\{.*?\}) carried (\d+) unresolved read here (\d+) read here (\d+)", P1); NR1, VD1, NCAR1, NUNR1, NRH1 = int(m1.group(1)), eval(m1.group(2)), int(m1.group(3)), int(m1.group(4)), int(m1.group(5))
U = R(f'{SCR}/ch12_docket_uncred.out'); chunks = re.findall(r'(ch12_uncred_\d\d\.txt) rows (\d+)-(\d+) \((\d+) rows, (\d+) bytes\)', U)
d2a = [c for c in chunks if 582 <= int(c[1]) and int(c[2]) <= 932]; NUNCRED = sum(int(c[3]) for c in d2a); assert NUNCRED + NUNR == NRH, (NUNCRED, NUNR, NRH)
d2b = [c for c in chunks if int(c[1]) >= 933]
S = R(f'{SCR}/ch12_unres_split.py'); 
vd = lambda d: ', '.join(f'{k} {d.get(k, 0)}' for k in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE'))
TOTV = {k: VD.get(k, 0) + VD1.get(k, 0) for k in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE')}
MAPP = f'''
THE DOCKET D2a — AS RUN (2026-09-20, in D1's window — the room under the 600k cap after D1 took D2's first half; the docket now THREE runs): the dump's rows
582-932 — Avodah Zarah 45a-48b (108 of 130 carried from chapter 7's docket), Chullin 16b-17a, 28a, 84a-b, 102b-103a and 113a-116a — VERDICTED in one part
on disk (ch12_docket_D.py; SPEC = CREDITED_SPEC + OWN, build() asserting the slice matched — no unmatched address on the first check): {NR} rows — {vd(VD)};
{NCAR} CARRIED with their ledgers' own verdict lines and {NUNR} whose ledger's form carried no verdict READ WHOLE HERE (ch12_uncred_unres_D2a.txt — the carry's
unresolved split by run, ch12_unres_split.py); {NUNCRED} uncredited rows READ WHOLE in {len(d2a)} chunk files ({", ".join(f"{c[0]} rows {c[1]}-{c[2]} ({c[3]} rows)" for c in d2a)}; the
chunker's boundaries {{582, 933}} — Bekhorot 15a:1 the first D2b row, computed); {NRH} ROWS READ WHOLE IN THIS RUN; LAW by cell, this docket's own notes
{LAWC}; no cut, no overlay. WITH D1: {NR1 + NR} rows verdicted ({vd(TOTV)}; {NCAR1 + NCAR} carried, {NRH1 + NRH} read whole). THE CROWNS OF D2a (the part's notes; the
file's finds section typed at D2b): THE WILDERNESS FLESH'S ARMS NARRATED — R. Yishmael's: the flesh of desire forbidden in the wilderness, eaten only as an
offering, released at the entry (Chullin 16b:15) with THE DISTANCE ITS GROUND (16b:17 — near the Tabernacle they ate from God's table; 12:21's 'too far');
R. Akiva's: stabbing permitted, the rite required at the entry (17a:3-4 — the two values named: 'the flesh of desire never forbidden' / 'the flesh of
stabbing never permitted'); THE EXILE'S STATE — the release persists ('one may always slaughter', 16b:16; 17a:3), a third state for the parameter; the wild
animal outside the ban (17a:10 — 12:22's gazelle); THE BIRD'S SLAUGHTER — by Torah law (Rabbi from 12:21 'as I have commanded you' — in part A) or by the
scribes (R. Elazar HaKappar from 12:22's comparison, 28a:4); WHICH SIGN FOR A BIRD a parameter (28a:6 — either / the gullet; 28a:13 the pinching refutes Rav
Adda), THE UNCERTAINTY RULE (28a:8 — 'any uncertainty in slaughter, invalid'), the interruption and the deficiency rules (28a:11-12), everyone, always,
anything that cuts (17a:16 — no fear of the appearance of worship on a roof or a ship); THE CIVILITY at its seat (84a:18-21 — meat as if trapped; 12:21's
'OF your cattle' the partitive 'some, not all', one's own not the market's; R. Elazar ben Azaria's ladder of means; 84a:24 a son not accustomed to meat and
wine; 84b:4 below one's means for oneself, above them for wife and children); 'LIKE WATER' BOUNDED — no covering for the domestic animal (84a:10-11) but no
immersion in blood (84a:12-16 — Leviticus 11:36's three waters exclude it: a fifth reading refused); THE LIMB FROM THE LIVING'S MEASURE — a whole live
creature any amount (Chullin 102b:1; 102b:2-3 Rabbi against R. Elazar son of R. Shimon on 'stands to be divided into limbs'), THE LASHES' COUNT from the two
verses' division (102b:13; 103a:1) and THE STACKING RULE (103a:4-17 — a prohibition upon a prohibition; the limb's Noahide breadth the ground, 103a:6;
Leviticus 7:24 the teacher, 103a:16); THE BLOOD BAN'S KITCHEN RULE (113a:10-14 — salted and rinsed; the perforated vessel; the neck not broken before the
soul departs); FLESH IN MILK AT ITS FOLIO — Mishnah Chullin 8:4 (113a:18-19 — the three 'kid's; R. Yosei HaGelili's bird from 'its mother's milk'),
Shmuel's six rules on the three mentions (113b:5-8 — THE CHAPTER'S BLOOD NOT MEAT for the milk law; Tosefta 8:3 at 114a:4), 'kid' any domestic animal
from Genesis 38:20 and 27:16 (113a:20-113b:3 — the run's own verses; two verses as one), the cow, the sister and the mother's own milk by a-fortiori with the
verse still needed (114a:8-114b:8 — I1's refutation form, I3's common element), THE EATING BAN'S SOURCES (Rav Ashi from 14:3's 'abominable', 114b:9; Reish
Lakish from the Paschal's 'boiled in any way', 115a:10; Isi ben Yehuda's 'sacred' / 'sacred' with Exodus 22:30, 115b:7; the three verses' three jobs —
R. Yishmael's school, 115b:6) and THE BENEFIT BAN'S (R. Abbahu's 'you shall not eat' rule, 114b:10 — the chapter's four 'you shall not eat' clauses under it,
the blood's benefit the specified exception; Rabbi's 'kadosh' / 'kadesh' analogy, 115b:4; R. Eliezer's school from the carcass sold, 115b:5; R. Shimon's
arm that benefit is permitted, 116a:7-8), and THE CROWN OF 12:25 — RABBI'S REDUNDANT 'YOU SHALL NOT EAT IT' DEFENDED BY THE CHAPTER'S OWN CONTEXT: 'a
matter derived from its context' (I12) — the adjacent verses the redeemed consecrated, two types, so a prohibition of two types (115b:2); THE REFUTATION
RULES (115b:13-116a:2 — a verbal analogy not refuted by reasoning; a common-element analogy refuted only from its sources' details); THE WILD ANIMAL AND
THE BIRD IN MILK the arms (116a:12-14 — bird in milk eaten in R. Yosei HaGelili's locale); Mishnah Avodah Zarah 3:6 at its folio (47a:21 — the fallen wall
withdrawn four cubits) and the revoked asherah's lulav (47a:4-12 — unresolved). THE MIDDOT (checked in MIDDOT.md before typing): I1 at Chullin 84b:6,
102b:2, 114a:9, 114a:13, 114b:1, 115a:4, 115b:8; I2 at 115b:4, 115b:7, 116a:7 — and 115b:13's rider (no refutation by reasoning); I3 at 114a:15-17,
115b:16, 116a:1-2 (the common element and its refutation rule); I12 at 115b:2 (the context — the thirteen principles named by the row itself); E28 at
113a:19, 115b:5; the juxtapositions named (28a:4, 84a:5, 84a:7, 115a:6) and the do-not-read reading (115a:5), no code. NEXT: D2b after a compaction —
rows 933-1537 in {len(d2b)} chunk files ({", ".join(f"{c[0]} rows {c[1]}-{c[2]} ({c[3]} rows)" for c in d2b)}; two of them over the Read page — two pages each) and ch12_uncred_unres_D2b.txt (30 rows); then the writer over the parts, the records, the forms.
'''
STATE = f'''
#201 ADDENDUM 2 (2026-09-20, at the close of THE DOCKET D2a of THE DEUTERONOMY WALK sitting 10b — the second of the docket's runs, taken in D1's window for the room under the 600k cap — A CLEAN COMPACTION POINT): THE STATE: D2a = the dump's rows 582-932 (Avodah Zarah 45a-48b, Chullin 16b-17a, 28a, 84a-b, 102b-103a, 113a-116a) VERDICTED in one part on disk (<scratch>/ch12_docket_D.py, copied to World/step9/forms_deuteronomy_walk/; build asserts the slice matched — no unmatched address on its first check; ch12_d2_check.py's print: {NR} rows — {vd(VD)}; carried {NCAR}, {NUNR} unresolved read whole here; {NRH} rows read whole in this run in {len(d2a)} chunk files and ch12_uncred_unres_D2a.txt; LAW by cell, own notes {LAWC}); WITH D1: {NR1 + NR} of the dump's 1,538 rows verdicted in parts A-D ({vd(TOTV)}), {NCAR1 + NCAR} carried, {NRH1 + NRH} read whole; the chunker's boundaries {{582, 933}} (the derive patched: SPLIT_AT crossed, not hit); the unresolved rows split by run (ch12_unres_split.py — D1 68, D2a 19, D2b 30); the map's "THE DOCKET D2a — AS RUN" paragraph (the crowns, the middot named). THE LEDGER NOT YET WRITTEN — the writer runs at D2b's close over parts A-G. NOT COMMITTED (since 4af2953): RUN A's records, the design, D1's and D2a's records. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT (compact before D2b). NEXT ON "Go": D2b — (1) read the chunks {", ".join(c[0] for c in d2b)} (rows 933-1537; the two 76k chunks in two Read pages each — offset/limit) and ch12_uncred_unres_D2b.txt (30 rows) whole; (2) the parts E (rows 933-1185: Bekhorot 15a-16a, 33a-b — Mishnah Bekhorot 2:2-3 and 9:3's Gemara, the blemished consecrated and the tithe's partners; Temurah 3b-4a (29 of 29 carried), 17b — the substitute; Makkot 13a-b (35 of 35 carried), 17a-19b, 23b — outside the wall, the ladder, the blood's reward), F (rows 1186-1396: Sotah 37b-38b — the Name as written; Sanhedrin 20b — the three commandments, 74a-b — the persecution (25 of 33 carried); Kiddushin 36b-37a (24 of 24 carried) — the land-bound; Rosh Hashanah 4a-6b (76 of 93 carried) — do not delay), G (rows 1397-1537: Yevamot 47b (19 of 19 carried), Keritot 20b-22a — the blood's classes (71 to read), Megillah 9b-10a — the sanctity after Jerusalem, Pesachim 8b (17 of 17 carried)) — the boundaries from the dump's block index (Bekhorot 15a:1 933, Temurah 3b:1 1014, Makkot 13a:1 1063, Sotah 37b:1 1186, Sanhedrin 20b:1 1234, Kiddushin 36b:1 1285, Rosh Hashanah 4a:1 1307, Yevamot 47b:1 1397, Keritot 20b:1 1416, Megillah 9b:1 1492, Pesachim 8b:1 1521), ch12_d2_check.py EFG; (3) derive_ch12_docket_writer.py → write_ch12_docket.py (9b's form: the parts 'ABCDEFG', OUT logic/oral_triage/deu_12_reeh_exam_2026-09-20.md, 'Deut 12:' and range(1, 32), the header ch12_docket_hdr.py and the crowns ch12_docket_crowns.py typed from the three AS RUN paragraphs, the duplicate-address rule kept, the ranges from ch12_docket_scan.out's 'THE RANGES SIZED' block — assert twenty-five); the lint; (4) write_ch12_docket_records.py (9b's form: the map's "THE DOCKET — AS RUN" summing the three runs, MIDDOT's docket entry (every code checked before typed), MISHNAH_TOPICS' row notes, COMPILE_DEBT's 10b box (k) noted, the state doc's addendum 3, the recovery page, RESUME, the memory, the commit message file started); (5) copy_ch12_docket_forms.py; then RUN B after a compaction. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 10b … THE DESIGN" and its "THE DOCKET D1 — AS RUN" and "THE DOCKET D2a — AS RUN" paragraphs, MEMORY.md; for D2b's parts the head of ch12_docket_D.py (the form).
'''
MEMO = f'''
THE DOCKET D2a DONE (2026-09-20, in D1's window): rows 582-932 in ch12_docket_D.py — {NR} rows ({vd(VD)}; {NCAR} carried, {NRH} read whole here); with D1 {NR1 + NR} of 1,538 verdicted; the crowns in the map's "THE DOCKET D2a — AS RUN": the wilderness flesh's arms narrated with the distance their ground (Chullin 16b:15-17a:4), the exile a third state (16b:16), which sign for a bird (28a:6), the civility's partitive 'of' (84a:20), the limb's measure and the stacking rule (102b:1-103a:17), flesh in milk at its folio and Rabbi's 12:25 defended by the context — I12 (115b:2). NEXT: D2b (rows 933-1537) after a compaction; the state doc's #201 addendum 2 the newest.
'''
MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; STATEDOC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; WALK = f'{MEM}/deuteronomy-walk.md'; IDX = f'{MEM}/MEMORY.md'
REC_EDITS = [("## 2. WHERE IT STANDS (2026-09-20, 10b D1 done; the state doc #201 add. 1 the newest)", "## 2. WHERE IT STANDS (2026-09-20, 10b D2a done; the state doc #201 add. 2 the newest)"),
             (f'- COMMITTED 4af2953 (NOT PUSHED). 10b A + D1 DONE ({NR1} rows in parts A-C; #201 add. 1). NEXT ON "Go": D2 (rows 582-1537), then RUN B.',
              f'- COMMITTED 4af2953 (NOT PUSHED). 10b A + D1 + D2a DONE ({NR1 + NR} rows in parts A-D; #201 add. 2). NEXT ON "Go": D2b (rows 933-1537), then RUN B.')]
IDX_EDIT = ("10b A + D1 DONE; NEXT: the docket D2", "10b A + D1 + D2a DONE; NEXT: the docket D2b")
ok = True
for a, b in REC_EDITS:
    if R(REC).count(a) != 1: print('REC ANCHOR', R(REC).count(a), a[:60]); ok = False
if R(IDX).count(IDX_EDIT[0]) != 1: print('IDX ANCHOR', R(IDX).count(IDX_EDIT[0])); ok = False
assert 'THE DOCKET D2a — AS RUN' not in R(MAP) and '#201 ADDENDUM 2' not in R(STATEDOC) and '#201 ADDENDUM 1' in R(STATEDOC)
rec = R(REC)
for a, b in REC_EDITS: rec = rec.replace(a, b)
idx = R(IDX).replace(*IDX_EDIT)
print('anchors %s; the recovery page would be %d bytes (cap 10240); MEMORY.md %d (cap 17000); D2a %d rows, with D1 %d' % ('OK' if ok else 'BAD', len(rec.encode('utf-8')), len(idx.encode('utf-8')), NR, NR1 + NR))
assert ok and len(rec.encode('utf-8')) <= 10240 and len(idx.encode('utf-8')) <= 17000
W(MAP, R(MAP).rstrip('\n') + '\n' + MAPP); W(STATEDOC, R(STATEDOC).rstrip('\n') + '\n' + STATE); W(REC, rec); W(WALK, R(WALK).rstrip('\n') + '\n' + MEMO); W(IDX, idx)
print('written: the map, the state doc, the recovery page, the memory note, the index')
for p in (MAP, STATEDOC, REC, WALK, IDX, f'{SCR}/ch12_docket_D.py'):
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); print('  lint', p.replace(ROOT, '<repo>').replace(MEM, '<memory>').replace(SCR, '<scratch>'), (r.stdout.strip().split('\n')[-1])[:60])
r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/scrub_home_paths.py', '--check'], capture_output=True, text=True); print('  home-path gate:', (r.stdout + r.stderr).strip().split('\n')[-1][:90])
