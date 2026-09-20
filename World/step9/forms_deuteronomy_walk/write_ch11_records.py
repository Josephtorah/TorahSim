import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 9 — CHAPTER 11 (2026-09-20; the owner: "Go" after the reread that followed 8b's compaction, "Continue" after the clean point #198 —
# a READING sitting is ONE run under THE TWO-RUN RULE, every row whole under THE WHOLE-ROW RULE): THE RECORDS at the close, from the sheet World/step9/RECORD_FORMS.md
# in ONE call — the map's "Sitting 9 — CHAPTER 11 — AS BUILT", COMPILE_DEBT's box (owed to the compile 9b), MIDDOT's block (the Sifrei's rows that argue by a rule —
# the codes censused from the ledger's own rows), MISHNAH_TOPICS' row notes (ROUTED to 9b), RESEARCH_LOG's entry, THE_STEPS' paragraph, THE_BRIEFING's bullet and
# entry, RESUME's note, the state doc's #198 addendum 1, the recovery page (section 2 rewritten, under 10 KB), the recovery addenda's section 51, the stamp row, the
# memory file and the index line (under 17,000 bytes), and the commit message's paragraph. Every number parsed from a print named beside it (--check prints them and
# writes nothing); every insert on a unique anchor asserted present once; the lints before and after. Sitting 8's form (write_ch10_records.py).
import os, re, subprocess, sys, yaml, json
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/' + os.path.abspath(ROOT).replace('/', '-') + '/memory')
DATE = '2026-09-20'; LDATE = '2026-09-20'
UID = 'deu_11_bless_curse_set'
CHECK = '--check' in sys.argv
CHAIN_NOTE = 'THE GATES CHAIN RAN ONCE, ALL GREEN ON ITS FIRST PASS (12:11 to 12:19 — the seat, verify_text, the ritual, the fold, build_world, the journal gate, the register gate --strict, large_letter, the home gate; no demand, no retype; the summary read once). THE LABELS CENSUS REFUSED TWO LABELS ENDING IN BARE PROSE (DV11-02, DV11-05 — chapter 10\'s lesson 7 repeated: the label\'s last clause takes its parenthesis) — closed by the two tails patched in the form and in the file, the verifier and the census rerun green.'
def rd(p): return open(p, encoding='utf-8').read()
# ---- THE NUMBERS, PARSED FROM THE PRINTS ----
truth = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py')
assert 'assert len(W["units"]) == 225' in truth and 'assert len(W["standing"]) == 2233' in truth and "8b8fff1fa28953af" in truth
CT = rd(f'{SP}/ch11_truth.out'); CB = rd(f'{SP}/ch11_bake.out'); C1 = rd(f'{SP}/ch11_fold_check1.out')
assert 'CORPUS TRUTH GREEN' in CT and 'CORPUS TRUTH GREEN' in C1 and 'wrote corpus_world.sqlite' in CB
rit = rd(f'{SP}/ch11_ritual_{UID}.out'); N_PASS = len(re.findall(r'^PASS', rit, re.M))
assert 'RITUAL COMPLETE' in rit and N_PASS == 13 and not re.search(r'^FAIL', rit, re.M), N_PASS
vt = rd(f'{SP}/ch11_vt_{UID}.out'); mvt = re.search(r'TEXT LAYER GREEN: (\d+) steps, (\d+) scenarios', vt); assert mvt and mvt.group(1) == '32', vt[-300:]
VT_STEPS, VT_SCEN = mvt.groups()
assert '  status: frozen' in rd(f'{ROOT}/logic/units/{UID}.yaml') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json') and 'ALL_DONE' in rd(f'{SP}/ch11_chain.log')
JG = rd(f'{SP}/ch11_journal.out'); RG = rd(f'{SP}/ch11_register.out'); BW = rd(f'{SP}/ch11_build.out'); GS = rd(f'{SP}/ch11_gates_SUMMARY.txt')
assert 'GATE GREEN' in JG and 'ALL GREEN' in BW and 'THE REGISTER GATE: GREEN' in RG and 'ALL GREEN' in GS, (JG[-200:], BW[-200:], GS[-200:])
mj = re.search(r'(\d+) kinds, ([\d,]+) rows', JG); J_KINDS, J_ROWS = mj.group(1), mj.group(2)
mr = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', RG); R_DECL, R_DEBT, R_FAIL = mr.groups()
assert R_DEBT == '0' and R_FAIL == '0', mr.groups()
mc = re.search(r'(\d+) units, (\d+) facts, (\d+) demands \((\d+) open\)', CT); C_UNITS, C_FACTS, C_DEM, C_OPEN = mc.groups()
assert C_UNITS == '225', C_UNITS
HG = rd(f'{SP}/ch11_home.out'); assert 'GREEN' in HG, HG[-200:]
LED = rd(f'{ROOT}/logic/oral_triage/deu_11_ekev_reeh_{LDATE}.md')
ml = re.search(r'\*\*read: (\d+) of \1 — COMPLETE\*\* \((\d+) Onkelos verses and (\d+) Sifrei rows.*?MATERIAL (\d+) Onkelos, CONTEXT (\d+) Onkelos, MATERIAL (\d+) Sifrei spine, CONTEXT (\d+) Sifrei spine, MATERIAL (\d+) Sifrei outside, CONTEXT (\d+) Sifrei outside', LED, re.S)
L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_SM, L_SC, L_XM, L_XC = ml.groups()
assert L_ALL == '210' and L_ONK == '32' and L_SIF == '178' and LED.count('⟨MISS⟩') == 0
L_BYTES = len(LED.encode())
N_REREAD = len(re.findall(r'^- Sifrei Devarim \d+:\d+ — [A-Z]+ \(REREAD WHOLE — read before in', LED, re.M)); N_REREAD_OUT = len(re.findall(r'^- Sifrei Devarim \d+:\d+ — [A-Z]+ \(REREAD WHOLE — first read in', LED, re.M))
assert N_REREAD == 37 and N_REREAD_OUT == 2, (N_REREAD, N_REREAD_OUT)
ROWS = re.findall(r'^- (Sifrei Devarim \d+:\d+) — [A-Z]+.*$', LED, re.M)
CODES = Counter(); BYCODE = {}
for line in re.findall(r'^- Sifrei Devarim \d+:\d+ — .*$', LED, re.M):
    name = re.match(r'- (Sifrei Devarim \d+:\d+)', line).group(1)
    for c in sorted(set(re.findall(r'\b([IE]\d{1,2}) \(', line))): CODES[c] += 1; BYCODE.setdefault(c, []).append(name.split(' ')[2])
CODE_TXT = '; '.join(f'{c} at {", ".join(BYCODE[c])}' for c in sorted(CODES, key=lambda x: (x[0], int(x[1:]))))
d_ov = yaml.safe_load(rd(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'))
OV_REF11 = len([k for k in d_ov['by_ref'] if k.startswith('Deut.11.')]); OV_REF, OV_GL = len(d_ov['by_ref']), len(d_ov['by_gloss'])
assert OV_REF11 == 158 and OV_REF == 859 and OV_GL == 604, (OV_REF11, OV_REF, OV_GL)
N_CLAIMS = len(json.load(open(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json', encoding='utf-8'))); assert N_CLAIMS == 6
VC = rd(f'{SP}/ch11_vc.out'); assert 'SUMMARY: 6 verified, 0 failed, 0 uncheckable, 0 no-check' in VC
LAB = rd(f'{SP}/ch11_labels.out'); mlab = re.search(r'CLAIM LABELS CENSUS — (\d+) claims in (\d+) manifests; labeled \1; DEBT 0', LAB); LN = f'{int(mlab.group(1)):,} claims in {mlab.group(2)} manifests'; assert 'GATE PASSED' in LAB and re.search(r'deu\s+70 claims', LAB), LAB[-300:]
assert rd(f'{SP}/ch11_ink_run3.out').strip().endswith('0 failing statements') and rd(f'{SP}/ch11_ink_run2.out').strip().endswith('0 failing statements') and rd(f'{SP}/ch11_ink_run1.out').strip().startswith('10 failing statements')
N_INK = len(re.findall(r'^assert ', rd(f'{SP}/ch11_ink.py'), re.M))
LL = rd(f'{SP}/ch11_large_letter.out').strip().split('\n')[-1]; assert LL.endswith('6/6'), LL
JR10 = re.search(r'12 kinds, (\d+) rows', rd(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch10_journal.out')).group(1); DJ = int(J_ROWS.replace(',', '')) - int(JR10)
MAN = rd(f'{SP}/ch11_manifest.out'); assert 'every CITE INDEX name used by a claim: True' in MAN
DUMP = rd(f'{SP}/ch11_dump0.out'); mdump = re.search(r'DB verses (\d+) \| export verses HE (\d+) EN (\d+)', DUMP); assert mdump and mdump.groups() == ('32', '32', '32'), DUMP[:300]
print('PARSED:', dict(ritual_pass=N_PASS, verify_text=(VT_STEPS, VT_SCEN), journal=(J_KINDS, J_ROWS, DJ), register=(R_DECL, R_DEBT, R_FAIL), corpus=(C_UNITS, C_FACTS, C_DEM, C_OPEN), ledger=(L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_SM, L_SC, L_XM, L_XC, L_BYTES, N_REREAD, N_REREAD_OUT), codes=dict(CODES), overrides=(OV_REF11, OV_REF, OV_GL), claims=N_CLAIMS, labels=LN, ink=N_INK, large_letter=LL[-3:]))
print('CODES BY ROW:', CODE_TXT)
def append(path, text):
    s = rd(path); assert text not in s
    with open(path, 'a', encoding='utf-8') as f: f.write(text)
    print('appended %d bytes -> %s' % (len(text.encode()), path))
def insert_before(path, anchor, text):
    s = rd(path); assert s.count(anchor) == 1, (path, anchor[:40], s.count(anchor))
    open(path, 'w', encoding='utf-8').write(s.replace(anchor, text + anchor)); print('inserted %d bytes before %r -> %s' % (len(text.encode()), anchor[:30], path))
def replace_once(path, a, b):
    s = rd(path); assert s.count(a) == 1, (path, a[:40], s.count(a))
    open(path, 'w', encoding='utf-8').write(s.replace(a, b)); print('replaced %r -> %s' % (a[:30], path))
def row_note(path, line_start, note):
    lines = rd(path).split('\n'); hits = [i for i, l in enumerate(lines) if l.startswith(line_start)]
    assert len(hits) == 1 and note not in lines[hits[0]], (line_start, len(hits))
    lines[hits[0]] += note; open(path, 'w', encoding='utf-8').write('\n'.join(lines)); print('row note %d bytes -> %s (%s)' % (len(note.encode()), path, line_start[:30]))

STAMP = (f'| {DATE} | {UID} | DELEGATED | FULL RULE | Deuteronomy 11:1-32 derivation {LDATE} (THE DEUTERONOMY WALK sitting 9 — CHAPTER 11; the owner: "Go" after the reread that followed 8b\'s compaction, "Continue" after the clean point #198 — a reading sitting ONE run, every row whole): Onkelos Deuteronomy 11 whole (32 = 32, the identity) + the Sifrei on Deuteronomy ON THE CHAPTER — piskaot 37-58, {L_SM and int(L_SM) + int(L_SC)} spine rows read whole in both files ({N_REREAD} rows read before and reread whole) + its {L_XM} rows outside the spine read whole ({N_REREAD_OUT} reread) + the kin credited by name; the ledger deu_11_ekev_reeh_{LDATE}.md ({L_ALL} sources, coverage computed, lint 0); {N_CLAIMS} claims DV11-01..06 verified 6/0, seated as six WITNESS_READ at 11:1, 8, 13, 22, 25, 26; the ritual {N_PASS} PASS; CORPUS TRUTH GREEN ({C_UNITS} units, standing 2233, hash unmoved); the fold layer +{DJ}; the display layer +{OV_REF11} by reference, +64 by gloss | {LN}, labeled, debt 0 |\n')

WALK = f'''


## Sitting 9 — CHAPTER 11 — AS BUILT ({DATE}; the design above stands as written — the one run ran as designed with a clean compaction point inside it (#198, after the rows and the ledger; the owner: "Continue"); every departure from it is named here)

THE RESULT: Deuteronomy 11:1-32 READ, FROZEN and SEATED as ONE unit — deu_11_bless_curse_set (the 225th frozen unit; 32 of 32 verses, missing 0, computed; the
portion edge Ekev / Re\'eh at 11:25-26 INSIDE it — the chapter the unit): the ledger logic/oral_triage/deu_11_ekev_reeh_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}:
MATERIAL {L_OM} / CONTEXT {L_OC}; THE SIFREI\'S SPINE piskaot 37-58 {int(L_SM) + int(L_SC)} rows: MATERIAL {L_SM} / CONTEXT {L_SC}, {N_REREAD} of them read before and REREAD WHOLE (the prior reads
found in the earlier ledgers by computation — 41 reads of 37 rows: 23 at the Deuteronomy sittings, 18 at the Genesis sittings); the outside rows {L_XM}: MATERIAL {L_XM} /
CONTEXT {L_XC}, {N_REREAD_OUT} reread; {L_BYTES:,} bytes, lint 0, no cut missed), the manifest {N_CLAIMS} claims DV11-01..06 verified 6/0 (every he_contains cut from the store\'s own bytes;
every cite index name used by a claim — the spine\'s rows distributed by piska from the CITE INDEX itself), seated as six WITNESS_READ operators at 11:1, 8, 13,
22, 25, 26 with step E; the ritual {N_PASS} PASS; verify_text GREEN ({VT_STEPS} steps, {VT_SCEN} scenarios); the fold predicted and matched (units 224 → 225, standing 2227 → 2233,
the hash 8b8fff1fa28953af unmoved — CORPUS TRUTH GREEN before and after the bake: {C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, {C_OPEN} open); build_world ALL GREEN; the
journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer since chapter 10\'s reading, the tape unmoved since 8b); the register gate --strict GREEN (DECLARED
{R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — no seat in the chapter in the finder\'s forms: 11:25\'s "as He spoke to you" is by "spoke", the third form owed since 4b, measured here);
large_letter_probes {LL[-3:]}; the labels census GREEN ({LN}, Deuteronomy 70); the home-path gate GREEN; the display layer +{OV_REF11} by reference and +64 by gloss ({OV_REF} / {OV_GL} in all).

THE READING: every Onkelos row whole in the Aramaic and the English (ch11_onkelos.txt); THE SPINE ON THE CHAPTER for the first time since chapter 6 — twenty-two
piskaot heading on 11:10-32 (37-38 on 11:10, 39 on 11:11, 40 on 11:12, 41 on 11:13, 42 on 11:14, 43 on 11:15, 44 on 11:18, 45 WITHOUT A HEAD CITATION — its one row
opening with 11:18\'s words, the spine\'s by the consonants, 46 on 11:19, 47 on 11:21, 48-49 on 11:22, 50 on 11:23, 51 on 11:24, 52 on 11:25, 53-54 on 11:26, 55 on 11:29,
56 on 11:30, 57 on 11:31, 58 on 11:32; 36 on 6:9 before, 59 on 12:1 after), every row read whole in both files (ch11_sifrei_spine.txt, 315 KB, split by piska for the
reading); the seven outside rows whole in both files (ch11_sifrei_outside.txt — the frontlets\' four compartments 35:4 and the doorposts\' two plurals 36:3 from
chapter 6\'s piskaot, reread; the sages at the border 80:4-5; the song\'s heavens shut 306:4, 306:6, 306:9), 234:6 EXCLUDED (the English\'s "(Dt.11:12)" for 22:12\'s
garment — the Hebrew cites nothing); the kin (Numbers 16 on Dathan and Abiram, 6:4-9, 8:7-10, Exodus 23:27-31, Leviticus 26:3-5 and 19-20) credited by name with the
counts computed from those ledgers (35, 6, 4, 3, 5); the sea and the frontlets read through the Mekhilta at the Exodus block (38 rows across the ledgers) — no ledger
holds an Onkelos row of Exodus 13-15 (asserted).

THE DEPARTURES FROM THE DESIGN: none in substance. THE INK\'S FIRST PASS FELL TEN WAYS ON FORMS (none a fact, each retyped from the diag print): the Proverbs range
citation "(משלי כה כא-כב)" ("Proverbs 25:21-22") invisible to the citation regex at 45:1; the colon inside 37:3\'s opening; chapter 12\'s verse count 31, not 32; the
hiphil filter catching two infinitives (4:38, 7:17); "which I set before you today" sorting 11:26, 11:32, 4:8; the Aramaic offset of 11:19 against 6:7 (the sixth word
against the fourth); the override counts 64 / 158 / 36. THE LEDGER WRITER\'S FIRST RUN fell on TWO TYPED SUMS (956 and 959 were not the dicts\' sums — printed, the
literals dropped); the lint flagged ONE TRANSLITERATION ("qal wa-chomer" — glossed "(a-fortiori)"); THE PROSE\'S OWN REREAD MARK checked against the computed list
differed at two rows — 51:1 had claimed a prior read at chapters 1-3 that no ledger holds (corrected to fresh) and 41:17 carried the mark in lower case (the check
made case-blind); the ledger rewritten by its own script under DEU_REWRITE before the point, uncommitted. THE MIDDAH CODES held — every code checked in MIDDOT.md
before it was typed, none relabeled (chapter 10\'s lesson kept): the census from the ledger\'s rows — {CODE_TXT}. {CHAIN_NOTE}

THE GATES, COMPUTED FROM THEIR PRINTS: the ritual {N_PASS} PASS (RITUAL COMPLETE, {C_UNITS} frozen units); CORPUS TRUTH GREEN twice ({C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, {C_OPEN} open;
the hash unmoved); build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows, +{DJ}); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL});
verify_claims 6 verified / 0 failed; the labels census GREEN ({LN}); large_letter_probes {LL[-3:]}; the home-path gate GREEN; the ink {N_INK} asserts — 10 failing on the
first typed pass, 0 on the second and third (the third after the display patch).

⚠ THE LESSONS (the run\'s, gathered — the numbered list the sheet asks for): (1) THE SPINE RETURNS AT THE LAND\'S PRAISE, NOT THE PARAGRAPH\'S HEAD — the Sifrei opens
its exposition at 11:10 and not at 11:13 (or 11:1): four chapters of silence end on the Land, and the reading sees it only by computing the heads. (2) A PISKA\'S
MEMBERSHIP IS DECIDED ON THE CONSONANTS — 45 has no head citation; its row opens with 11:18\'s words: the heads are a first sort, the words the second. (3) THE TWO
FILES DIVIDE A PISKA DIFFERENTLY (chapter 8\'s lesson again, at 37): each file\'s own row read whole and counted once. (4) THE FIRST TYPED PASS FELL TEN WAYS ON FORMS
— a range citation, a colon, a verse count, a morphology filter, a sort, an offset, three counts — none a fact; the diag print retypes them all at once. (5) A TYPED
SUM IS PRINTED BEFORE IT IS ASSERTED — the writer\'s two sums were remembered, not read. (6) THE PROSE\'S OWN MARK IS CHECKED AGAINST THE COMPUTED LIST — a "read
before" in the prose is a claim; the ledgers decide it (one corrected, one case-blind). (7) A TRANSLITERATION IS GLOSSED LIKE THE SCRIPT — the lint reads "qal
wa-chomer" as Hebrew. (8) THE PRIOR READS ARE FOUND BY COMPUTATION, NOT MEMORY — forty-one reads of thirty-seven rows across twenty ledgers, none typed. (9) THE
MANIFEST TAKES THE SPINE FROM THE CITE INDEX — every piska\'s rows listed from the ledger itself, so "every name used" holds by construction. (10) THE POINT FALLS WHERE
THE DESIGN PUT IT — the rows and the ledger are the heavy half of a reading with a spine; a clean point inside the run, resumed on "Continue" at the step named (#198).
(11) A MIDDAH CODE CHECKED BEFORE IT IS TYPED IS NOT RELABELED — the rule\'s order held this time, no row moved. (12) THE RECEIPT BY "SPOKE" IS THE FINDER\'S THIRD
FORM — 11:25\'s "as He spoke to you" listed nowhere by the gate; the shelf names its callee (52:4 — Exodus 23:27): measured at the reading, dispositioned at 9b. (13)
THE READING SITTING HELD IN ONE RUN under the two-run rule, the sixth in a row — the first with a spine on the chapter since the rule.

THE FORMS: World/step9/forms_deuteronomy_walk/ (copy_ch11_forms.py — derive_ch11_dump0.py, ch11_dump0.py, derive_ch11_measure1.py, ch11_measure1_sections.py,
ch11_measure1.py, ch11_ink_head.py, ch11_ink_body.py, derive_ch11_ink.py, ch11_ink.py, ch11_ink_diag.py, patch_ink_ch11.py, assert_driver.py, the eight row files,
write_ch11_ledger.py, derive_ch11_patch.py, ch11_patch_overrides.py, write_ch11_manifest.py, seat_ch11.py, write_ch11_design.py, write_ch11_records.py,
ch11_chain.sh, ch11_fold.sh, ch11_gates.sh and the prints).

NEXT on the ruling: the commit on the owner\'s word (the cache, 7b, 8, 8b and this sitting stand uncommitted since a985fbc — one message); then THE COMPILE OF
CHAPTER 11 (sitting 9b) in TWO RUNS — RUN A: the rereads (THE_STEPS Step 5 + the compiler block; this section; the 9b box in COMPILE_DEBT), the measurements (the
sea\'s and Dathan and Abiram\'s lines on the tape for the retelling rows; 6:8-9\'s cell for the frontlets and the doorposts; Leviticus 26\'s cell for the rain; Exodus
23:27-31\'s for the dread and the borders; Numbers 34\'s for the borders; the receipt at 11:25 in the register; chapter 27\'s ceremony ahead), THE DESIGN (the rain
conditional a NEW cell; the checkpoint series DC), the probes to FAIL, THE DOCKET by the union rule (Mishnah Berakhot 2:2 and Berakhot 13a-16a on the paragraphs\'
order; Menachot 34a-37b and Kiddushin 29a-b credited from 4b; Kiddushin 36b-37a the land-bound; Ta\'anit 2a-3a and 7a-10a the rain; Rosh Hashanah 16a-17b the year
judged; Gittin 8a and Mishnah Sheviit 6:1 the borders; Sotah 32a-37b and Mishnah Sotah 7:2-5 the ceremony; Sotah 33b-34a Gerizim and Ebal; Ketubot 110b-111a the
dwelling; Sanhedrin 90b the resurrection; Kiddushin 40b the study and the deed — every row whole; a docket past ~700 rows its own run); RUN B: the types, the
runner, the tape to 10/10, the chain, the records, the forms, the commit message — or the Decalogue-schema sitting first, on his word.
'''

DEBT = f'''

## SITTING 9 — CHAPTER 11 ({DATE}, the reading; deu_11_bless_curse_set frozen) — OWED TO THE COMPILE 9b: (a) THE RAIN CONDITIONAL (11:13-17) — NO CELL ANYWHERE IN
## THE MACHINE: a NEW cell with Leviticus 26:3-5 and 19-20 by CALL (the rains in their season, the heavens as iron), 28:12 the treasure and 11:17 the shut heavens the
## pair the shelf reads (40:12; 306:4, 306:6, 306:9 — "shut" defined by the wombs, Genesis 16:2 and 20:18), the year judged at its head and the rain\'s measure moved by
## the deeds (40:5-14; Rosh Hashanah 16a-17b; Mishnah Rosh Hashanah 1:2), the mention and the request of rain (Ta\'anit 2a-3a; Mishnah Ta\'anit 1:1-3; Berakhot 33a) —
## the effect a STATUS on the land and a BLOCK on the heavens; (b) THE FRONTLETS, THE TEACHING AND THE DOORPOSTS SAID AGAIN IN THE PLURAL (11:18-20) — 6:8-9\'s cell
## (hear_o_israel) by CALL: the four compartments over THE SPELLINGS\' OPEN ROW (35:4; 6:8 defective, 11:18 and Exodus 13:16 with the first vav — measured on the
## pointed tokens; Menachot 34b, Sanhedrin 4b), the doorposts\' two plurals (36:3; Menachot 34a), "teach" the piel against 5:1\'s qal, sons not daughters (46:1;
## Kiddushin 29b), the second paragraph\'s place after the first (Mishnah Berakhot 2:2; Berakhot 13a); (c) THE BORDERS (11:24) — Numbers 34 by CALL; the returners\'
## two lines (51:2 — Mishnah Sheviit 6:1 quoted inside the Sifrei; Gittin 8a; the Tosefta Sheviit 4:11 the baraita of the borders, 51:3\'s thirty-five names) a
## PARAMETER; the conquest abroad after the Land (51:1 — David\'s Aram the counter-case; the verbal analogy "shall be" with Numbers 34:6); (d) THE DREAD AND THE
## RECEIPT (11:25) — "as He spoke to you" pointed at Exodus 23:27 by 52:4 (the terror sent before; the escort runner\'s cell): a RUN_CITATION pointer with its why —
## THE FINDER\'S THIRD FORM (4b\'s owed item) measured here at a seat the register gate lists nowhere ("as He spoke" sixteen in the book); the dread on the near and
## the fear on the far (52:2 — Rahab\'s Red Sea, Joshua 2:10; Jericho the particular); the pilgrimage guarded (52:4; Exodus 34:24 by CALL; Pesachim 8b); (e) THE
## DISPOSSESSION (11:23) — "little by little" Exodus 23:29-30 by CALL (chapter 7\'s find), the sin the pace (50:2); "than you" plural against 4:38 and 9:1 (50:4);
## (f) THE BLESSING AND THE CURSE SET (11:26-28) — the choice commanded (30:19 by CALL ahead; 53:1\'s crossroads), the blessing if / the curse if not (54:1), idolatry
## the whole Torah\'s denial (54:4; Sotah 37a; the Sifrei on Numbers 111) — a STATUS on Israel: the set before them; (g) GERIZIM AND EBAL (11:29-30) — chapter 27\'s
## ceremony by CALL (27:12-13; Mishnah Sotah 7:2-5; Sotah 32a-37b; the Tosefta Sotah 8:10): a blessing precedes a curse, the curses liken the blessings (55:2); the
## mountains\' place (56:3 — Genesis 12:6 by the analogy; R. Eliezer\'s five readings; Sotah 33b-34a; the Samaritan "Shechem" a variant reading — a DATA row); GILGAL the
## Torah\'s one seat, Joshua 4:19-20 and 8:30-35 the run; (h) THE RETELLING ROWS (11:2-7) — the readback\'s reference rows against the tape\'s lines: the signs in
## Egypt, the sea (Exodus 14 — 11:4 against 14:31 three tokens), the wilderness (chapter 8\'s state row), Dathan and Abiram (Numbers 16:31-33\'s line; Korah unnamed;
## "every living thing" the flood\'s word; 16:14 their own milk and honey) — the generation that saw (11:7 — Joshua 24:31, Judges 2:7 the run); (i) THE STUDY AND
## THE DEED (41:12-14 — the study first, the deed the greater; Kiddushin 40b) and THE DUTIES OF THE BODY AGAINST THE LAND-BOUND (44:1 — Kiddushin 36b-37a; Mishnah
## Kiddushin 1:9) DATA rows; the exile\'s cause (43:34) and the dwelling weighed against all (80:4-5; Ketubot 110b-111a) DATA rows; (j) THE RESURRECTION FROM "TO THEM"
## (47:2 — Sanhedrin 90b) and the three ages (47:1-2) DATA rows; the sixty ascents by gematria (47:4 — E29) a DATA row; (k) THE PARSER — no number verse in the
## chapter, one starred token (11:15 "and you shall be satisfied"), "swore" twice no number — a DATA row; the Memra at 11:1, the export\'s parenthesis at 11:8, the
## tefillin at 11:18 DATA rows; MOSES UNNAMED chapters 6-14 a DATA row; (l) THE LAND\'S ONE GARDEN (11:10 — Genesis 13:10 Lot\'s clause) and the one spelling quoted
## plene by the Sifrei (11:12; 40:8-10) DATA rows for the census; (m) THE CHECKPOINT SERIES continues (DB the open series — DB9 the last name; the next DC1, keyed by
## its first word); (n) THE DOCKET by the union rule — Mishnah Berakhot 2:2, Berakhot 13a-16a (the paragraphs\' order); Menachot 34a-37b and Kiddushin 29a-30b
## CREDITED from 4b\'s docket (every row read whole there); Kiddushin 36b-37a (the land-bound); Kiddushin 40b (study and deed); Ta\'anit 2a-3a, 7a-10a (the rain);
## Mishnah Ta\'anit 1:1-3; Rosh Hashanah 16a-17b, Mishnah Rosh Hashanah 1:2 (the year judged); Berakhot 33a (the mention of rain); Gittin 8a, Mishnah Sheviit 6:1 (the
## borders); Pesachim 8b (the pilgrimage guarded); Sotah 32a-37b, Mishnah Sotah 7:2-5 (the ceremony), Sotah 33b-34a (the mountains); Ketubot 110b-111a (the dwelling);
## Sanhedrin 90b (the resurrection); Sotah 37a (idolatry); Sukkah 52a CREDITED from 8b (the inclination) — EVERY ROW WHOLE; a docket past ~700 rows its own run.
## NOTHING ELSE IN CHAPTER 11 IS OWED TO A LATER SITTING OF ITS OWN.
'''

MIDDOT = f'''- **THE SIFREI ON DEUTERONOMY\'S OWN CASE LAW ON CHAPTER 11 (Deuteronomy 11:1-32; THE DEUTERONOMY WALK sitting 9, {DATE};
  the ledger logic/oral_triage/deu_11_ekev_reeh_{LDATE}.md — THE SPINE ON THE CHAPTER for the first time since chapter 6, piskaot
  37-58, {int(L_SM) + int(L_SC)} rows read whole in both files, and seven rows outside the spine; EVERY CODE CHECKED IN MIDDOT.md BEFORE IT WAS TYPED,
  none relabeled; the census from the ledger\'s own rows: {CODE_TXT}):**
  · THE COMMON GROUND OF TWO (44:1 on 11:18): tefillin and the study of Torah are not alike, but both are duties of the body not bound
    to the land — so every duty of the body binds in the Land and abroad, and the land-bound only in the Land (orlah and mixed kinds
    the exceptions; the new grain R. Eliezer\'s) — I3 (binyan av from two verses; the row\'s own words "מבנין אב שבין שניהם" ("from
    the common ground of the two") on its bytes); THE INK: 11:18\'s two commands the row\'s two cases — the compile\'s partition.
  · EXTENSION AFTER EXTENSION RESTRICTS (36:3 on 6:9 from 11:20): "doorposts" twice, the plural read down to ONE doorpost — E3; THE
    INK: 6:9 מזוזת ("doorposts") with one vav, 11:20 מזוזות ("doorposts") with two — the two plurals the shelf counts, measured at
    their seats.
  · THE VERBAL ANALOGY "SHALL BE" (51:2 on 11:24): "to the sea shall be your border" against "the Great Sea and its border shall be
    your sea border" (Numbers 34:6) — what lies opposite in the sea is the Land\'s — I2; the Hebrew carries it at 51:2, the English at
    51:1 (the two files\' division); THE MISHNAH QUOTED BY NAME INSIDE THE SIFREI (Sheviit 6:1 — the answer sheet inside the spine).
  · THE VERBAL ANALOGY "TEREBINTH OF MOREH" (56:3 on 11:30): 11:30\'s Moreh is Genesis 12:6\'s — Shechem — I2; R. Eliezer\'s five
    readings against it (the Jordan\'s bank, the sunset, the Hivites, the hills, Gilgal unseen); the Samaritan "Shechem" named a forgery
    that changes nothing — a variant reading witnessed inside the spine; THE INK: Gilgal the Torah\'s one seat, "the terebinths of
    Moreh" one (Genesis 12:6 singular, plene).
  · THE A-FORTIORI FROM NAAMAN\'S EARTH (52:4 on 11:25): if Naaman feared to take two mules\' burden of earth without leave, how would a
    man take goods and cattle — the Land guarded at the pilgrimage (Exodus 34:24) — I1 (qal wa-chomer (a-fortiori)); and THE RECEIPT
    NAMED: "as He spoke to you" — "and where did He speak? \\"I will send My terror before you\\" (Exodus 23:27)" — the teacher pointing
    11:25\'s receipt at its callee (the compile\'s RUN_CITATION with its why; the finder\'s third form).
  · THE REPEATED EXPRESSION READ FOR ITS NUMBER (50:4 on 11:23): "than you" said again after 7:1 — one of the seven peoples greater than
    all Israel (Amos 2:9\'s Amorite) — E10; THE INK: "than you" plural here, singular at 4:38 and 9:1. (52:2: "the dread of you" and "the
    fear of you" two nouns read apart — the near and the far — E10; Rahab\'s "the waters of the Red Sea" the ink\'s find, Joshua 2:10.)
  · THE EXTENSION BY "ALL" (48:10 on 11:22; 50:2 on 11:23): "the commandment, the commandment, all the commandment" — midrash, laws and
    lore; "all these nations" — their helpers included after "these" restricts — E1 (ribui); "too" the second extension (48:10, gam).
  · THE GEMATRIA OF THE ASCENTS (47:4 on 11:21): "a song for the ascents" — thirty ascents by the preposition\'s letter-value, sixty by
    the plural — E29 (checked; the English\'s note the computation).
  · THE PARABLES (E26): the king\'s dressing on the wound — words of Torah a potion against the inclination (45:1, the piska without a
    head; Genesis 4:7 "if you do well, it is lifted"); the king\'s bird given to the servant (48:2 — "it is no empty thing for you: it is
    your life"); the two brothers and the denar (48:3 — the disciple who lays by); the crossroads and the two paths (53:1 — Re\'eh\'s
    opening); the feast and the fine portion (53:2); the two stewards (306:4 — 28:12 and 11:17 the pair from the song).
  · NAMED WITHOUT A CODE: the affirmation implying its negation (46:1 — "from the yes the no"); the likening of the curses to the
    blessings (55:2 — the Levites, the voice, the tongue, the Amen); the definition by another seat (306:6 — "opening" by Leah\'s womb,
    "shutting" by Abimelech\'s); the particular that leaves the general (52:2 — Jericho, Saul, Pharaoh\'s daughter); the four terms of the
    frame assigned to the four kinds of the oral shelf (58:1 — Mishnah, deed, expositions, laws).
'''

RESEARCH = f'''

## {DATE} — DEUTERONOMY 11 READ AND FROZEN (THE DEUTERONOMY WALK sitting 9, one run with a clean point inside it): THE SPINE RETURNS — TWENTY-TWO SECTIONS OF THE
## SIFREI ON ONE CHAPTER, OPENING AT THE LAND\'S PRAISE; THE RAIN CONDITIONAL HAS NO CELL; THE FRONTLETS\' THREE SPELLINGS MEASURED AT THEIR SEATS; JOSHUA SAYS THE
## CHAPTER\'S SENTENCES AT SEVEN SEATS; THE MISHNAH QUOTED BY NAME INSIDE THE SIFREI; THE RECEIPT BY "SPOKE" POINTED AT EXODUS 23:27 BY THE TEACHER
On the owner\'s "Go" after the reread that followed 8b\'s compaction and "Continue" after the clean point #198 ({DATE}). THE READING: Deuteronomy 11:1-32 with Onkelos
whole (the export\'s 32 rows the DB\'s 32 — the identity, asserted) and THE SIFREI ON DEUTERONOMY ON THE CHAPTER for the first time since chapter 6 — piskaot 37-58
heading on 11:10-32 (45 without a head citation, the spine\'s by its opening words; 36 on 6:9 before, 59 on 12:1 after), {int(L_SM) + int(L_SC)} rows read whole in both files
({N_REREAD} read before at twenty earlier sittings and reread whole — found by computation), seven rows outside the spine read whole (234:6 excluded — the English\'s
slip for 22:12), the kin credited by name (Numbers 16; 6:4-9; 8:7-10; Exodus 23:27-31; Leviticus 26). FROZEN as ONE unit deu_11_bless_curse_set (the 225th; the
portion edge Ekev / Re\'eh inside it; standing 2233 = 2227 + 6 as predicted, hash unmoved); the ledger deu_11_ekev_reeh_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}:
MATERIAL {L_OM} / CONTEXT {L_OC}; the spine {int(L_SM) + int(L_SC)}: MATERIAL {L_SM} / CONTEXT {L_SC}; the outside rows {L_XM}: MATERIAL {L_XM}; coverage computed, lint 0, no cut missed); six claims
DV11-01..06 verified 6/0, seated as six WITNESS_READ at 11:1, 8, 13, 22, 25, 26; the ritual {N_PASS} PASS; the fold +{DJ} on the journal; the display layer +{OV_REF11} by
reference and +64 by gloss. THE FINDS: THE SPINE OPENS AT 11:10, the Land\'s praise, not at the paragraph\'s head — Egypt watered by the foot against the Land drinking
by heaven\'s rain (37-39), the rain\'s measure fixed at the year\'s head and moved by the deeds (40); "garden" fifteen in the Torah, 11:10 THE ONLY SEAT OUTSIDE GENESIS,
"like the land of Egypt" Lot\'s clause (Genesis 13:10) and 11:10 alone; "from the beginning of the year" spelled without the aleph THE BIBLE\'S ONE SEAT — QUOTED PLENE
BY THE SIFREI; "the discipline of the LORD" the Torah\'s one seat of the noun; "made flow" the hiphil\'s one Bible seat; "the waters of the Red Sea" 11:4 and Rahab\'s
Joshua 2:10 (the Sifrei 52:2 quotes her); DATHAN AND ABIRAM WITHOUT KORAH — eight seats each, never apart; "every living thing" the flood\'s word (Genesis 7:4, 7:23,
11:6); Numbers 16:14 "a land flowing with milk and honey" IN THEIR OWN MOUTHS of Egypt; "every great deed of the LORD" Joshua 24:31 and Judges 2:7 — JOSHUA SAYS THE
CHAPTER\'S SENTENCES AT SEVEN SEATS (1:3-5 the borders and no man standing, 1:11 the crossing, 5:6 the oath, 22:5 the charge whole with twelve tokens, 23:16 the curse
whole with eleven, 24:31; Rahab\'s 2:10); "My commandments" at 11:13 INSIDE MOSES\' SPEECH (5:29 the other seat, inside God\'s word); the two infinitive absolutes
"hearken, hearken" and "keep, keep" the shelf pairs (48:1); THE RAIN CONDITIONAL (11:13-17) HAS NO CELL ANYWHERE IN THE MACHINE — 28:12 and 11:17 the pair the song\'s
rows read (306:4, 306:6, 306:9), "and He shut the heavens" defined by the wombs (Genesis 16:2, 20:18) with the ink agreeing on the verb\'s Torah seats; THE FRONTLETS\'
THREE SPELLINGS MEASURED — 6:8 defective, 11:18 and Exodus 13:16 with the first vav — the shelf\'s four compartments (35:4) need a defective 11:18 the DB does not
write (4b\'s open row carried with its measurement); the doorposts 6:9 one vav / 11:20 two (36:3); "teach" the piel at 11:19 against 5:1\'s qal; "as the days of the
heavens above the earth" one seat — the resurrection from "to them" (47:2); "than you" plural against the singular 4:38, 9:1 (50:4); "the river, the river Euphrates"
one; "AS HE SPOKE TO YOU" (11:25) — the receipt by "spoke", sixteen in the book against the finder\'s "commanded" forms: THE TEACHER POINTS IT AT EXODUS 23:27 (52:4 —
"and where did He speak?"); THE MISHNAH QUOTED BY NAME INSIDE THE SIFREI (Sheviit 6:1 at 51:2) and the baraita of the borders (51:3 — thirty-five Aramaic names);
Re\'eh opens at 11:26 inside the chapter — "See" the singular imperative, seven in the book; "a blessing and a curse" one seat; Gerizim four, Ebal eight (three a man);
GILGAL THE TORAH\'S ONE SEAT; "the terebinths of Moreh" one — 56:3\'s analogy against R. Eliezer\'s five readings, the Samaritan "Shechem" a forgery that changes
nothing; "possess it and dwell in it" one — the sages at the border (80:4-5); the four terms of the frame the four kinds of the oral shelf (58:1); MOSES UNNAMED
chapters 6-14; NO NUMBER VERSE in the chapter; ONKELOS — the Word at 11:1, "teaching" for discipline, the export\'s parenthesis at 11:8, "demands it, always", "accept,
accept", "shut" one row, tefillin at 11:18, "teach" against 6:7\'s "repeat", "the blessers and the cursers", "the plains of Moreh". THE CAUTIONS: the two files divide
piska 37 differently (chapter 8\'s lesson again); the ledger writer\'s two typed sums; the prose\'s own mark against the computed list. THE LESSONS (thirteen, in the
map): the spine returns at the Land\'s praise; a piska\'s membership on the consonants; a typed sum printed first; the prose\'s mark checked; a transliteration glossed;
the prior reads by computation; the manifest\'s spine from the cite index; the point where the design put it; the receipt by "spoke" the finder\'s third form. OWED TO
9b: the rain conditional a NEW cell (Leviticus 26 by CALL), the frontlets and the doorposts by 6:8-9\'s cell, the borders by Numbers 34 with the returners\' lines, the
receipt\'s pointer at 11:25, the dispossession little by little, the blessing and the curse set, Gerizim and Ebal by chapter 27\'s ceremony, Gilgal, the retelling
rows, the study/deed clock, the land-bound partition, the docket.
'''

STEPS = f'''DEUTERONOMY — SITTING 9 — CHAPTER 11, Deuteronomy 11:1-32 ({DATE}, on Brian\'s "Go" after the reread that followed the chapter-10 compile\'s compaction and
"Continue" after a clean point inside the run; World/step9/DEUTERONOMY_WALK.md "Sitting 9" and "Sitting 9 — AS BUILT"; a reading sitting is one run). Chapter 11 is
the end of the long charge and the hinge to the laws: love the LORD and keep His charge; the discipline your children have not seen — Egypt, the sea, the wilderness,
Dathan and Abiram swallowed; keep all the commandment and prolong your days on a land not like Egypt, a land that drinks the rain of heaven and that the LORD\'s eyes
are on all year; if you hearken, the rain in its season — if you turn aside, the heavens shut; the words on the heart, the hand, the eyes, the sons and the
doorposts, said again to all of you; keep and cleave, and every place your foot treads is yours, from the wilderness to the river to the sea, and no man will stand
before you; see, a blessing and a curse — the blessing on Mount Gerizim and the curse on Mount Ebal, across the Jordan by Gilgal; you are crossing to possess and
dwell, so keep the statutes set before you today. For the first time since chapter 6 the Sifrei has sections on the chapter — twenty-two of them, from the Land\'s
praise at 11:10 to the last verse, every row read whole in both files, with seven more rows from elsewhere; forty-one earlier reads of thirty-seven rows were found
in the older ledgers by computation and reread. The reading laid each verse beside its kin and counted the shared words: Joshua says this chapter\'s sentences back
at seven places; the rain clause has no code anywhere in the machine yet; the frontlets are spelled three ways at their three seats and the tradition\'s count of four
needs a spelling the text does not have; the Sifrei quotes a Mishnah by name inside its own text for the borders; and where Moses says "as He spoke to you", the
teacher names the place — Exodus 23:27. The chapter is frozen as one unit, the 225th, the world\'s standing facts up by six as predicted, its hash unmoved, every gate
green. The ink script fell ten ways on its first pass — all forms, none a fact — and held on the second. Next: the commit on your word; then the compile of chapter
11 in two runs — the rain clause as a new cell, the frontlets and the doorposts by call, the borders, the receipt\'s pointer, the blessing and the curse set, Gerizim
and Ebal by chapter 27\'s ceremony — or the ten-commandments schema first.


'''

BRIEF = f'''- **CHAPTER 11 READ AND FROZEN — THE SIFREI COMES BACK ONTO THE PAGE: TWENTY-TWO SECTIONS ON ONE CHAPTER, OPENING AT THE LAND\'S PRAISE; THE RAIN CLAUSE HAS NO CODE IN THE MACHINE; THE FRONTLETS ARE SPELLED THREE WAYS AND THE TRADITION\'S COUNT NEEDS A FOURTH; JOSHUA SAYS THE CHAPTER\'S SENTENCES BACK AT SEVEN PLACES; A MISHNAH QUOTED BY NAME INSIDE THE SIFREI; "AS HE SPOKE TO YOU" POINTED AT EXODUS 23 BY THE TEACHER** ({DATE}; sitting 9, one run with a clean point inside it; the ledger deu_11_ekev_reeh_{LDATE}.md — {L_ALL} sources, every row whole; the 225th unit; every gate green).
'''
BRIEF_ENTRY = f'''### {DATE} — CHAPTER 11 READ: THE SPINE RETURNS, THE RAIN CLAUSE WITHOUT A CELL, THE FRONTLETS\' THREE SPELLINGS

Chapter 11 closes the long charge and opens the laws: the discipline your
children have not seen, the land that drinks the rain of heaven, the rain if
you hearken and the shut heavens if you turn, the words on hand and eyes and
doorposts said again to all of you, the borders and the dread, and a blessing
and a curse set on two mountains across the Jordan. For four chapters the
Sifrei on Deuteronomy had no section at all; here it has twenty-two, and it
opens them not at the chapter\'s head but at the Land\'s praise. Every row was
read whole in both files — one hundred and seventy-one on the chapter and seven
from elsewhere — and forty-one earlier readings of thirty-seven of them were
found in the older ledgers by computation, not memory. The reading laid each
verse beside its kin and counted the shared words: Joshua says this chapter\'s
sentences back at seven places, Rahab among them. The rain clause has no code
anywhere in the machine yet — the compile\'s first job. The frontlets are
spelled three ways at their three seats, and the tradition\'s four compartments
need a spelling the text does not have — measured now, carried to the compile
with its measurement. The Sifrei quotes a Mishnah by name inside its own text
for the borders, and where Moses says "as He spoke to you", the teacher names
the place: Exodus 23:27. The chapter is frozen as one unit, every gate green,
in one run with a clean compaction point inside it.

'''

RESUME_NOTE = f'''# ⚠ THE DEUTERONOMY WALK sitting 9 ({DATE}; step9/DEUTERONOMY_WALK.md "Sitting 9" + "Sitting 9 — AS BUILT"): CHAPTER 11 READ AND FROZEN as ONE unit
# (deu_11_bless_curse_set, the 225th; standing 2233, hash unmoved) — THE SPINE ON THE CHAPTER for the first time since chapter 6 (piskaot 37-58, {int(L_SM) + int(L_SC)} rows whole in
# both files; seven outside), the rain conditional (11:13-17) with NO CELL in the machine, the frontlets\' three spellings measured (4b\'s open row carried), 11:25\'s
# receipt by "spoke" pointed at Exodus 23:27 by the shelf (the finder\'s third form), Joshua saying the chapter\'s sentences at seven seats; the ledger
# deu_11_ekev_reeh_{LDATE}.md ({L_ALL} sources); six claims seated; the fold +{DJ} on the journal ({J_ROWS} rows); every gate green. NEXT on the owner\'s word: the
# commit (the cache, 7b, 8, 8b, this); then 9b — the compile of chapter 11 (the rain cell; DB the open series).
'''

STATE = f'''
#198 ADDENDUM 1 ({DATE}, at the close of THE DEUTERONOMY WALK sitting 9 — CHAPTER 11\'s READING, the ONE run, resumed on the owner\'s "Continue" at the step #198 named — A CLEAN COMPACTION POINT): THE SECOND HALF AS RUN: ch11_patch_overrides.py derived from the chapter-10 form by fourteen asserted substitutions (derive_ch11_patch.py; its final check loosened once to the import name — the form\'s own name stays in the comment), the yaml +{OV_REF11} by reference and +64 by gloss ({OV_REF} / {OV_GL}); the ink rerun PATCHED (0 failing); the manifest write_ch11_manifest.py (six claims DV11-01..06; THE SPINE DISTRIBUTED BY PISKA FROM THE CITE INDEX ITSELF — sifp(); every name used by construction; every he_contains cut from the store\'s bytes); the chain ch11_gates.sh (the seat, verify_text {VT_STEPS} steps / {VT_SCEN} scenarios, the ritual {N_PASS} PASS, the fold 224 → 225 / 2227 → 2233 with the hash unmoved, build_world, the journal gate {J_ROWS} rows (+{DJ}), the register gate --strict DECLARED {R_DECL} / DEBT {R_DEBT} / FAILS {R_FAIL}, large_letter {LL[-3:]}, the home gate) — {CHAIN_NOTE}; verify_claims 6/0 and the labels census ({LN}) beside it; THE RECORDS from the sheet in one call (write_ch11_records.py — the map\'s "Sitting 9 — CHAPTER 11 — AS BUILT" with thirteen lessons, COMPILE_DEBT\'s sitting-9 box (a)-(n), MIDDOT\'s chapter-11 block with the codes censused from the ledger\'s rows ({CODE_TXT}), MISHNAH_TOPICS (six heads routed to 9b), RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the scoreboard bullet and an entry), World/RESUME.md, this addendum, the addenda §51, the recovery page (section 2 under its cap), the memory (the walk note and the index line under 17,000), the stamp row, the commit message\'s paragraph); the forms copied (copy_ch11_forms.py). THE TREE: + logic/units/deu_11_bless_curse_set.yaml frozen (operators, step E, the anchor scenarios), logic/py_units/deu_11_bless_curse_set.py and ALL_UNITS.py (the ritual), logic/oral_audit/manifests/deu_11_bless_curse_set_claims.json, logic/oral_triage/deu_11_ekev_reeh_{LDATE}.md, logic/glosses/word_gloss_overrides.yaml, logic/corpus/CORPUS_TRUTH.py (225 / 2233), corpus_world.sqlite, World/journal/data/world.sqlite (the fold layer, gitignored), the records, the forms. NOT COMMITTED (since a985fbc): THE VERIFIED-IMPORT CACHE, 7b, 8, 8b and now 9 — ONE message at <scratch>/commit_msg_ch9b.txt covers all for the owner\'s word ("Commit" = no push; "commit push" = both). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. NEXT ON THE RULING: the commit on his word; then CHAPTER 11\'s COMPILE (9b) in two runs (RUN A the rereads, the measurements, the design — the rain conditional a NEW cell, the checkpoint series DC — and the docket by the union rule; RUN B the types, the runner, the tape, the chain, the records) — or the Decalogue-schema sitting first; THE INSTALL HYPOTHESIS and the owner\'s open decisions (the SUPPLIED forms, the calf\'s day marker, the registry\'s homograph) on the table. POST-COMPACTION REREADS: the recovery page, the map\'s "Sitting 9 — CHAPTER 11 — AS BUILT" (the newest section), MEMORY.md.
'''

ADDENDA = f'''
## 51. ADDENDUM ({DATE}, THE DEUTERONOMY WALK sitting 9 — CHAPTER 11, Deuteronomy 11:1-32 READ AND FROZEN in ONE run under THE TWO-RUN RULE with a clean compaction point inside it (#198), every row whole; the owner: "Go" after the reread that followed 8b\'s compaction, "Continue" after the point; the state doc\'s #198 and its addendum 1; the map\'s "Sitting 9 — CHAPTER 11 … THE DESIGN" and "Sitting 9 — CHAPTER 11 — AS BUILT")
THE READING: Onkelos Deuteronomy 11 whole (32 = 32, the identity, cost 18); THE SIFREI ON THE CHAPTER for the first time since chapter 6 — piskaot 37-58 heading on
11:10-32 (45 without a head citation, the spine\'s by its opening words), {int(L_SM) + int(L_SC)} rows read whole in both files ({N_REREAD} read before at twenty earlier sittings and reread
whole, found by computation); seven rows outside the spine by the union of both files (35:4, 36:3 reread from sitting 4; 80:4, 80:5; 306:4, 306:6, 306:9 — the ibid.
form found through the English); 234:6 excluded; the kin credited by name (Numbers 16 — 35 rows; 6:4-9 — 6; 8:7-10 — 4; Exodus 23:27-31 — 3; Leviticus 26 — 5; the
Mekhilta\'s 38 on the sea and the frontlets); the unit deu_11_bless_curse_set the 225th (standing 2233, hash unmoved; the portion edge inside it); the ledger {L_ALL}
sources (Onkelos MATERIAL {L_OM} / CONTEXT {L_OC}; the spine MATERIAL {L_SM} / CONTEXT {L_SC}; the outside rows MATERIAL {L_XM}); six claims 6/0 seated at 11:1, 8, 13, 22, 25, 26; the
display layer +{OV_REF11} by reference, +64 by gloss; every gate green in one chain (ch11_gates.sh). THE INK ASSEMBLED by derive_ch11_ink.py (the helpers by content
markers); ten asserts fell on the first pass (a range citation, a colon, a verse count, a morphology filter, a sort, an offset, three counts), none a fact. THE
FINDS: THE SPINE OPENS AT THE LAND\'S PRAISE (11:10), not the paragraph\'s head; the one garden outside Genesis and Lot\'s clause; the one spelling (11:12) quoted plene;
the discipline\'s noun, the hiphil "made flow", Rahab\'s Red Sea; Dathan and Abiram without Korah, "every living thing" the flood\'s word, 16:14 their own milk and
honey; JOSHUA AT SEVEN SEATS; "My commandments" inside Moses\' speech; the two doubled infinitives paired by 48:1; THE RAIN CONDITIONAL WITH NO CELL — 28:12 and 11:17
the pair, "shut" by the wombs; THE FRONTLETS\' THREE SPELLINGS and the doorposts\' two plurals measured (4b\'s open row carried); "teach" piel against qal; the
resurrection from "to them"; "than you" plural; Joshua 1:3-5 the borders\' receipt; "AS HE SPOKE TO YOU" pointed at Exodus 23:27 by 52:4 (the finder\'s third form);
the Mishnah quoted by name inside the Sifrei (Sheviit 6:1) and the baraita of the borders; Re\'eh inside the chapter, "See" seven; Gerizim four, Ebal eight; Gilgal
the Torah\'s one; Moreh\'s analogy against R. Eliezer\'s five readings and the Samaritan variant; the sages at the border; the four terms of the frame; Moses unnamed
6-14; no number verse. THE LESSONS (thirteen, in the map): the spine returns at the Land\'s praise; a piska\'s membership on the consonants; the two files divide a
piska differently; the first pass fell ten ways on forms; A TYPED SUM IS PRINTED FIRST; THE PROSE\'S MARK IS CHECKED AGAINST THE COMPUTED LIST; a transliteration is
glossed; the prior reads by computation; the manifest\'s spine from the cite index; the point where the design put it; a code checked first is not relabeled; the
receipt by "spoke"; the sixth reading in one run. OWED TO 9b (COMPILE_DEBT\'s box (a)-(n)): the rain cell, the frontlets and the doorposts by CALL, the borders, the
receipt\'s pointer, the dispossession, the blessing and the curse set, Gerizim and Ebal by chapter 27, the retelling rows, the study/deed clock, the land-bound
partition, the resurrection row, the parser\'s DATA rows, the series DC, the docket. The records on the sheet; the forms in World/step9/forms_deuteronomy_walk/
(copy_ch11_forms.py).
'''

MEMPAR = f'''
SITTING 9 DONE {DATE} ("Go" after the reread that followed 8b\'s compaction; "Continue" after the clean point #198 inside the run; the map\'s "Sitting 9" and
"Sitting 9 — AS BUILT"): CHAPTER 11 READ AND FROZEN as ONE unit deu_11_bless_curse_set (the 225th; standing 2233 = 2227 + 6 as predicted, hash unmoved; the
portion edge inside it) in ONE run, every row whole — Onkelos 32 rows (the identity), THE SIFREI ON THE CHAPTER for the first time since chapter 6 (piskaot 37-58,
{int(L_SM) + int(L_SC)} rows in both files; {N_REREAD} reread whole, found by computation; 45 without a head), seven outside rows (two reread), the kin credited by name; the ledger
deu_11_ekev_reeh_{LDATE}.md ({L_ALL} sources); six claims 6/0 seated at 11:1, 8, 13, 22, 25, 26; every gate green; the display layer +{OV_REF11} / +64. THE FINDS: THE
SPINE OPENS AT THE LAND\'S PRAISE (11:10); THE RAIN CONDITIONAL (11:13-17) HAS NO CELL — 9b\'s first job (Leviticus 26 by CALL; 28:12 and 11:17 the pair); THE
FRONTLETS\' THREE SPELLINGS measured (6:8 defective, 11:18 and Exodus 13:16 plene — the four compartments need a defective 11:18; 4b\'s open row carried); "AS HE
SPOKE TO YOU" (11:25) pointed at Exodus 23:27 by the Sifrei 52:4 — the finder\'s third form; JOSHUA SAYS THE CHAPTER AT SEVEN SEATS; the Mishnah (Sheviit 6:1) quoted
by name inside the Sifrei; Dathan and Abiram without Korah; the one garden outside Genesis; Gilgal the Torah\'s one; Moses unnamed 6-14; no number verse. ⚠ LESSONS
(thirteen, in the map): the spine returns where it wants (compute the heads); a piska\'s membership on the consonants; A TYPED SUM IS PRINTED BEFORE IT IS ASSERTED;
THE PROSE\'S OWN "READ BEFORE" IS CHECKED AGAINST THE COMPUTED LIST; a transliteration is glossed like the script; THE PRIOR READS BY COMPUTATION (41 of 37 rows); the
manifest\'s spine from the cite index (sifp); a clean point inside a reading run, resumed on "Continue"; a code checked first is not relabeled. OWED TO 9b: the rain
cell, the frontlets/doorposts by 6:8-9\'s cell, the borders (Numbers 34; the returners\' lines a PARAMETER), the receipt\'s pointer, little by little, the blessing
and the curse set, Gerizim and Ebal by chapter 27\'s ceremony, Gilgal, the retelling rows, the study/deed clock, the land-bound partition; DB the open series
(DC next). NOT COMMITTED (since a985fbc; ONE message at <scratch>/commit_msg_ch9b.txt covers THE IMPORT CACHE, 7b, 8, 8b and 9). NEXT on the ruling: the commit;
then 9b, two runs.
'''
MEMLINE_OLD_START = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — '
MEMLINE_NEW = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — map World/step9/DEUTERONOMY_WALK.md; ch 1-10 COMPILED, 11 READ (1-8 PUSHED a985fbc; 9-11 + the cache UNCOMMITTED); NEXT: commit, then 9b\n'
DESC_OLD = "COMMITTED THROUGH a985fbc (2026-09-19; PUSHED) — SITTING 8b DONE 2026-09-20 ("
DESC_NEW = f"COMMITTED THROUGH a985fbc (2026-09-19; PUSHED) — SITTING 9 DONE {DATE} (chapter 11 READ AND FROZEN as one unit, the 225th — the Sifrei back on the chapter with twenty-two sections, the rain conditional with no cell, the frontlets' three spellings measured, 11:25's receipt pointed at Exodus 23:27 by the teacher, Joshua at seven seats; 9b next) — SITTING 8b DONE 2026-09-20 ("
REC2_OLD_START = '## 2. WHERE IT STANDS'
REC2_NEW = f'''## 2. WHERE IT STANDS ({DATE}, after sitting 9; the state doc #198 addendum 1 the newest)
- NUMBERS CLOSED. DEUTERONOMY 1:1-10:22 COMPILED AND ON THE TAPE (1-7 at 29c189b, 8 at a985fbc — PUSHED; 9 at 7/7b, 10 at 8/8b); 11 READ.
- {C_UNITS} frozen units, standing 2233, hash 8b8fff1fa28953af. 65 runners, 70 daemons, 478 functions; 1142 kinds / 1037 effects.
- THE TAPE at RUN (1317, 96, 88, 0, 12, 1613, 41, 319, pairs, 127), markers 172, closes 127; the sweep 64/64; every gate GREEN.
- SITTING 9 (chapter 11 read, one run): THE SPINE BACK ON THE CHAPTER — twenty-two Sifrei sections on 11:10-32, {L_ALL} sources whole; the
  rain conditional (11:13-17) has NO CELL; the frontlets\' three spellings measured; 11:25\'s receipt pointed at Exodus 23:27 by the shelf.
- Uncommitted since a985fbc: the cache, 7b, 8, 8b, 9; ONE message at <scratch>/commit_msg_ch9b.txt covers all, on his word.
- NEXT ON HIS WORD: the commit; then 9b (two runs: the rain cell with Leviticus 26, the frontlets by CALL, the borders, the ceremony).

'''
TOPIC_BLESS = f' — 2:2 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 9, chapter 11\'s reading: the second paragraph of the Shema, 11:13-21 — its place after the first, the yoke of the kingdom before the yoke of the commandments; Berakhot 13a; the docket at 9b)'
TOPIC_SHEVIIT = f' — 6:1 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 9, chapter 11\'s reading: the borders of the Land by the returners from Babylon and from Egypt, 11:24 — QUOTED BY NAME INSIDE THE SIFREI at 51:2; Gittin 8a; the docket at 9b)'
TOPIC_SOTAH = f' — 7:2-5 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 9, chapter 11\'s reading: the blessing on Mount Gerizim and the curse on Mount Ebal, 11:29-30 — the ceremony\'s form at 55:2, the mountains\' place at 56:3; Sotah 32a-37b; the docket at 9b)'
TOPIC_KIDD = f' — 1:7, 1:9 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 9, chapter 11\'s reading: "your sons and not your daughters" 11:19 at 46:1 and the duties of the body against the land-bound 11:18 at 44:1; Kiddushin 29b, 36b-37a; the docket at 9b)'
TOPIC_MENACH = f' — 3:7 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 9, chapter 11\'s reading: the frontlets\' four compartments over the three spellings, 11:18 at 35:4 — 6:8 defective, 11:18 and Exodus 13:16 plene, measured; Menachot 34b; the docket at 9b)'
TOPIC_RH = f' — 1:2 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 9, chapter 11\'s reading: "from the beginning of the year to the end of the year" 11:12 at 40:5-14 — the rain\'s measure fixed at the year\'s head and moved by the deeds; Rosh Hashanah 16a-17b; the docket at 9b)'
T_BLESS = '**1. Mishnah, Blessings**'; T_SHEVIIT = '**5. Mishnah, Seventh Year**'; T_SOTAH = '**28. Mishnah, Suspected Wife**'; T_KIDD = '**30. Mishnah, Betrothal**'; T_MENACH = '**42. Mishnah, Grain Offerings**'; T_RH = '**19. Mishnah, New Year**'

LINT = f'{ROOT}/logic/solo_tools/gloss_lint.py'
def lint(path):
    out = subprocess.run([sys.executable, LINT, path], capture_output=True, text=True).stdout
    m = re.search(r'gloss_lint: (\d+) flag', out); return int(m.group(1)) if m else -1
WALKP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; RECP = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
TOPICS = f'{ROOT}/logic/MISHNAH_TOPICS.md'
TOUCH = [f'{ROOT}/logic/findings/STAMP_LEDGER.md', f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', f'{ROOT}/World/RESUME.md', f'{ROOT}/THE_STEPS.md', f'{ROOT}/THE_BRIEFING.md', f'{ROOT}/World/step9/COMPILE_DEBT.md', f'{ROOT}/RESEARCH_LOG.md', f'{ROOT}/logic/MIDDOT.md', RECP, f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md', TOPICS]
# ---- THE ANCHORS, ASSERTED PRESENT ONCE BEFORE ANY WRITE ----
A_RESUME = '# ⚠ THE DEUTERONOMY WALK sitting 8b (2026-09-20; step9/DEUTERONOMY_WALK.md "Sitting 8b"'
A_SCORE = '## SCOREBOARD (as of 2026-09-20, latest)\n'
A_BULLET = '- **CHAPTER 10 COMPILED — THE FORMS COMBINE'
A_ENTRY = '### 2026-09-20 — CHAPTER 10 COMPILED: TWO ACTS WRITTEN INTO THE PAST'
A_MIDDOT = '\n## Exodus block campaign — owner\'s word "Do 3")\n'
A_REC5 = 'the newest instances: the map\'s "Sitting 8" and "Sitting 8b"'
A_REC6 = '- Deuteronomy\'s sittings: the map; the addenda §31-50 (§39 the whole-row rule). The cost cuts: §35, §45, §47.'
ANCH = [(f'{ROOT}/World/RESUME.md', A_RESUME), (f'{ROOT}/THE_STEPS.md', '\n## Step 6 — Publish\n'), (f'{ROOT}/THE_BRIEFING.md', A_SCORE), (f'{ROOT}/THE_BRIEFING.md', A_BULLET), (f'{ROOT}/THE_BRIEFING.md', A_ENTRY), (f'{ROOT}/logic/MIDDOT.md', A_MIDDOT), (RECP, REC2_OLD_START), (RECP, '\n## 3. THE STANDING LAWS'), (RECP, A_REC5), (RECP, A_REC6), (f'{MEM}/deuteronomy-walk.md', DESC_OLD), (f'{MEM}/MEMORY.md', MEMLINE_OLD_START)]
for p, a in ANCH: assert rd(p).count(a) == 1, (p, a[:40], rd(p).count(a))
tl = rd(TOPICS).split('\n'); assert all(sum(l.startswith(t) for l in tl) == 1 for t in (T_BLESS, T_SHEVIIT, T_SOTAH, T_KIDD, T_MENACH, T_RH)) and f'sitting 9, chapter 11' not in rd(TOPICS)
assert '## Sitting 9 — CHAPTER 11 — AS BUILT' not in rd(WALKP) and '## Sitting 9 — CHAPTER 11, Deuteronomy 11:1-32' in rd(WALKP) and '#198 ADDENDUM 1' not in rd(TOUCH[1]) and 'COMPACTION POINT #198' in rd(TOUCH[1]) and '## 51. ADDENDUM' not in rd(TOUCH[9]) and '## 50. ADDENDUM' in rd(TOUCH[9]) and 'SITTING 9 DONE' not in rd(f'{MEM}/deuteronomy-walk.md') and 'SITTING 9 — CHAPTER 11' not in rd(TOUCH[5]) and f'## {DATE} — DEUTERONOMY 11 READ' not in rd(TOUCH[6]) and 'CASE LAW ON CHAPTER 11' not in rd(TOUCH[7])
assert CHAIN_NOTE != 'CHAIN_NOTE_PLACEHOLDER', 'the chain note is typed from the summary before the records are written'
s = rd(RECP); i = s.index(REC2_OLD_START); j = s.index('\n## 3. THE STANDING LAWS'); REC_NEW = s[:i] + REC2_NEW + s[j:]
REC_NEW = REC_NEW.replace(A_REC5, 'the newest instances: the map\'s "Sitting 9" and "Sitting 8b"').replace(A_REC6, '- Deuteronomy\'s sittings: the map; the addenda §31-51 (§39 the whole-row rule). The cost cuts: §35, §45, §47.')
assert len(REC_NEW.encode()) <= 10240, len(REC_NEW.encode())
m = rd(f'{MEM}/MEMORY.md'); i = m.index(MEMLINE_OLD_START); j = m.index('\n', i) + 1; MEM_NEW = m[:i] + MEMLINE_NEW + m[j:]
assert len(MEM_NEW.encode()) < 17000, len(MEM_NEW.encode())
# the commit message's paragraph (the scratch file the owner's word commits — the cache's, 7b's, 8's, 8b's and now this sitting's)
CM = f'{SP}/commit_msg_ch9b.txt'; cm = rd(CM); assert 'SITTING 9 ' not in cm and 'CHAPTER 11 READ' not in cm and '\nCo-Authored-By:' in cm
head, rest = cm.split('\n', 1)
head2 = head.rstrip('.') + f' AND CHAPTER 11 READ AND FROZEN (SITTING 9, ONE RUN, EVERY ROW WHOLE) — THE SPINE RETURNS: TWENTY-TWO SECTIONS OF THE SIFREI ON ONE CHAPTER, THE RAIN CONDITIONAL WITH NO CELL, THE FRONTLETS\' THREE SPELLINGS MEASURED, THE RECEIPT BY "SPOKE" POINTED AT EXODUS 23:27 BY THE TEACHER, AND JOSHUA SAYING THE CHAPTER\'S SENTENCES AT SEVEN SEATS.'
CM_PARA = f'''
ALSO IN THIS COMMIT: SITTING 9 — CHAPTER 11 READ AND FROZEN ({DATE}, on the owner\'s "Go" after the reread that followed 8b\'s compaction and "Continue" after the clean compaction point #198 inside the run; World/step9/DEUTERONOMY_WALK.md "Sitting 9 — CHAPTER 11 … THE DESIGN" and "Sitting 9 — CHAPTER 11 — AS BUILT"; the state doc\'s #198 and its addendum 1; the addenda §51): Deuteronomy 11:1-32 with Onkelos whole (the export\'s 32 rows the DB\'s 32 — the identity, asserted) and THE SIFREI ON DEUTERONOMY ON THE CHAPTER for the first time since chapter 6 — TWENTY-TWO PISKAOT 37-58 heading on 11:10-32 (the heads computed; 45 WITHOUT A HEAD CITATION, the spine\'s by its opening words; 36 on 6:9 before, 59 on 12:1 after), {int(L_SM) + int(L_SC)} rows READ WHOLE in both files ({N_REREAD} read before at twenty earlier sittings and REREAD WHOLE — the prior reads found in the ledgers by computation, 41 reads of 37 rows), seven rows outside the spine citing the chapter read whole (the frontlets\' four compartments and the doorposts\' two plurals from chapter 6\'s piskaot, the sages at the border, the song\'s heavens shut — the ibid. form found through the English; 234:6 EXCLUDED, the English\'s slip for 22:12\'s garment), the kin credited by name with the counts computed (the Korah ledger 35 rows on Dathan and Abiram; chapter 6\'s 6 on the Shema; chapter 8\'s 4 on the good land; Exodus 23\'s 3 on the dread and the borders; Leviticus 26\'s 5 on the rains; the Mekhilta\'s 38 on the sea and the frontlets — no ledger holding an Onkelos row of Exodus 13-15, asserted); frozen as ONE unit deu_11_bless_curse_set (the 225th; THE PORTION EDGE Ekev / Re\'eh at 11:25-26 INSIDE IT — the chapter the unit, per the ruling CHAPTER NUMBERS), standing 2233 = 2227 + 6 as predicted, hash 8b8fff1fa28953af unmoved; the ledger logic/oral_triage/deu_11_ekev_reeh_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the spine {int(L_SM) + int(L_SC)}: MATERIAL {L_SM} / CONTEXT {L_SC}; the outside rows {L_XM}: MATERIAL {L_XM}; coverage computed, lint 0, no cut missed); six claims DV11-01..06 verified 6/0 (the spine distributed by piska from the CITE INDEX itself), the labels census green, seated as six WITNESS_READ operators at 11:1, 8, 13, 22, 25, 26 with step E; the ritual {N_PASS} PASS; the display layer +{OV_REF11} by reference and +64 by gloss under the sitting\'s marker. THE FINDS: THE SPINE OPENS AT THE LAND\'S PRAISE (11:10), not at the paragraph\'s head — Egypt watered by the foot against the Land drinking by heaven\'s rain (37-39), the rain\'s measure fixed at the year\'s head and moved by the deeds (40); "garden" fifteen in the Torah and 11:10 THE ONLY SEAT OUTSIDE GENESIS, "like the land of Egypt" Lot\'s clause and 11:10 alone; "from the beginning of the year" spelled without the aleph THE BIBLE\'S ONE SEAT, QUOTED PLENE BY THE SIFREI; "the discipline of the LORD" the Torah\'s one seat of the noun; "made flow" the hiphil\'s one Bible seat; "the waters of the Red Sea" 11:4 and Rahab\'s Joshua 2:10 — the Sifrei quotes her; DATHAN AND ABIRAM WITHOUT KORAH (eight seats each, never apart), "every living thing" the flood\'s word (Genesis 7:4, 7:23, 11:6), Numbers 16:14\'s "a land flowing with milk and honey" IN THEIR OWN MOUTHS of Egypt; JOSHUA SAYS THE CHAPTER\'S SENTENCES AT SEVEN SEATS (1:3-5, 1:11, 5:6, 22:5 twelve tokens, 23:16 eleven, 24:31; Rahab\'s 2:10) — the install\'s receipts in the run; "My commandments" at 11:13 INSIDE MOSES\' SPEECH (5:29 the other seat, inside God\'s word); the two infinitive absolutes "hearken, hearken" and "keep, keep" paired by the shelf; THE RAIN CONDITIONAL (11:13-17) HAS NO CELL ANYWHERE IN THE MACHINE — 28:12 and 11:17 the pair the song\'s rows read, "and He shut the heavens" defined by the wombs with the ink agreeing on the verb\'s seats; THE FRONTLETS\' THREE SPELLINGS MEASURED AT THEIR SEATS — 6:8 defective, 11:18 and Exodus 13:16 with the first vav — the shelf\'s four compartments need a defective 11:18 the DB does not write (4b\'s open row carried with its measurement); the doorposts 6:9 one vav / 11:20 two; "teach" the piel at 11:19 against 5:1\'s qal; "as the days of the heavens above the earth" one seat, the resurrection read from "to them"; "than you" plural against the singular 4:38 and 9:1; THE RECEIPT BY "SPOKE" — 11:25\'s "as He spoke to you", sixteen in the book against the finder\'s "commanded" forms, POINTED AT EXODUS 23:27 BY THE TEACHER (52:4 — "and where did He speak?"): the finder\'s third form measured at a seat the register gate lists nowhere; THE MISHNAH QUOTED BY NAME INSIDE THE SIFREI (Sheviit 6:1 at 51:2 — the answer sheet inside the spine) and the baraita of the borders (51:3, thirty-five Aramaic names); Re\'eh opening at 11:26 inside the chapter, "See" the singular imperative seven in the book, "a blessing and a curse" one seat; Gerizim four seats, Ebal eight (three a man); GILGAL THE TORAH\'S ONE SEAT; "the terebinths of Moreh" one — the analogy with Genesis 12:6 against R. Eliezer\'s five readings, the Samaritan "Shechem" named a forgery that changes nothing (a variant reading witnessed inside the spine); "possess it and dwell in it" one seat — the sages at the border (80:4-5); the four terms of the frame the four kinds of the oral shelf (58:1); Moses unnamed chapters 6-14; NO NUMBER VERSE in the chapter (one starred token, "swore" twice no number); Onkelos\'s Word at 11:1, "teaching" for discipline, the export\'s parenthesis at 11:8, "demands it, always", "accept, accept", "shut" one row, tefillin at 11:18, "teach" against 6:7\'s "repeat", "the blessers and the cursers", "the plains of Moreh". EVERY GATE GREEN IN ONE CHAIN (ch11_gates.sh): the manifest (every CITE INDEX name used), the seat, verify_text ({VT_STEPS} steps, {VT_SCEN} scenarios), the ritual {N_PASS} PASS, CORPUS TRUTH GREEN before and after the bake ({C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, hash unmoved), build_world ALL GREEN, the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer, the tape unmoved since 8b), the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — no seat in the chapter in the finder\'s forms), large_letter_probes {LL[-3:]}, the home-path gate GREEN; verify_claims 6/0 and the labels census GREEN beside the chain; the ink {N_INK} asserts — 0 failing on its second and third runs (ten forms fell on the first). THE LESSONS (thirteen, in the map\'s AS BUILT): the spine returns at the Land\'s praise; a piska\'s membership on the consonants; the two files divide a piska differently; the first typed pass fell ten ways on forms; a typed sum is printed before it is asserted; the prose\'s own mark is checked against the computed list; a transliteration is glossed like the script; the prior reads by computation; the manifest\'s spine from the cite index; the point where the design put it; a code checked first is not relabeled; the receipt by "spoke" the finder\'s third form; the sixth reading in one run. Also in this commit: COMPILE_DEBT\'s sitting-9 box (a)-(n) owed to the compile 9b (the rain conditional a NEW cell with Leviticus 26 by CALL, the frontlets and the doorposts by 6:8-9\'s cell over the spellings\' open row, the borders by Numbers 34 with the returners\' lines, the receipt\'s pointer at 11:25, the dispossession little by little, the blessing and the curse set, Gerizim and Ebal by chapter 27\'s ceremony, Gilgal and Moreh, the retelling rows, the study/deed clock, the land-bound partition, the resurrection row, the parser\'s DATA rows, the series DC, the docket), MIDDOT\'s chapter-11 block (the codes censused from the ledger\'s rows — {CODE_TXT}), MISHNAH_TOPICS\' row notes (Blessings 2:2, Seventh Year 6:1, New Year 1:2, Suspected Wife 7:2-5, Betrothal 1:7 and 1:9, Grain Offerings 3:7 routed to 9b), RESEARCH_LOG\'s entry, THE_STEPS, THE_BRIEFING (the scoreboard and an entry), World/RESUME.md, the state doc\'s #198 with its addendum 1, the recovery page rewritten under its cap, the addenda §51, the stamp row, the forms in World/step9/forms_deuteronomy_walk/ (the one run\'s scripts and prints — the derivation, the dump, the measurement, the ink and its parts, the eight row files, the ledger writer, the display patch and its derivation, the manifest, the seat, the chain, the fold, the gates chain, the design, the records, the copy).
'''
k = rest.index('\nCo-Authored-By:'); CM_NEW = head2 + '\n' + rest[:k].rstrip('\n') + '\n' + CM_PARA + rest[k:]
BEFORE = {p: lint(p) for p in TOUCH}
print('lint before:', {os.path.basename(p): n for p, n in BEFORE.items()}, '| recovery page bytes', len(REC_NEW.encode()), '| MEMORY.md bytes', len(MEM_NEW.encode()), '| commit message bytes', len(CM_NEW.encode()))
if CHECK: print('CHECK ONLY — nothing written'); sys.exit(0)
# ---- THE WRITES ----
append(TOUCH[0], STAMP)
append(WALKP, WALK)
append(TOUCH[1], STATE)
insert_before(TOUCH[2], A_RESUME, RESUME_NOTE)
insert_before(TOUCH[3], '\n## Step 6 — Publish\n', STEPS)
insert_before(TOUCH[4], A_BULLET, BRIEF)
insert_before(TOUCH[4], A_ENTRY, BRIEF_ENTRY)
append(TOUCH[5], DEBT)
append(TOUCH[6], RESEARCH)
insert_before(TOUCH[7], A_MIDDOT, MIDDOT)
row_note(TOPICS, T_BLESS, TOPIC_BLESS)
row_note(TOPICS, T_SHEVIIT, TOPIC_SHEVIIT)
row_note(TOPICS, T_RH, TOPIC_RH)
row_note(TOPICS, T_SOTAH, TOPIC_SOTAH)
row_note(TOPICS, T_KIDD, TOPIC_KIDD)
row_note(TOPICS, T_MENACH, TOPIC_MENACH)
open(RECP, 'w', encoding='utf-8').write(REC_NEW); print('recovery page rewritten', len(REC_NEW.encode()), 'bytes')
append(TOUCH[9], ADDENDA)
append(f'{MEM}/deuteronomy-walk.md', MEMPAR)
replace_once(f'{MEM}/deuteronomy-walk.md', DESC_OLD, DESC_NEW)
open(f'{MEM}/MEMORY.md', 'w', encoding='utf-8').write(MEM_NEW); print('MEMORY.md', len(MEM_NEW.encode()), 'bytes')
open(CM, 'w', encoding='utf-8').write(CM_NEW); print('the commit message extended', len(CM_NEW.encode()), 'bytes')
AFTER = {p: lint(p) for p in TOUCH}
print('lint after: ', {os.path.basename(p): n for p, n in AFTER.items()})
assert all(AFTER[p] <= BEFORE[p] for p in TOUCH), [(os.path.basename(p), BEFORE[p], AFTER[p]) for p in TOUCH if AFTER[p] > BEFORE[p]]
assert lint(WALKP) == 0 and lint(f'{MEM}/deuteronomy-walk.md') == 0 and len(rd(RECP).encode()) <= 10240
print('records written; the lints at or under their baselines; the map and the memory file lint 0; the page under its cap')
