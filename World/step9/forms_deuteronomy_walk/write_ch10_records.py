import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 8 — CHAPTER 10 (2026-09-19/20; the owner: "Go" after the reread that followed 7b's compaction — a READING sitting is ONE run
# under THE TWO-RUN RULE, every row whole under THE WHOLE-ROW RULE): THE RECORDS at the close, from the sheet World/step9/RECORD_FORMS.md in ONE call — the
# map's "Sitting 8 — CHAPTER 10 — AS BUILT", COMPILE_DEBT's box (owed to the compile 8b), MIDDOT's block (the Sifrei's row that argues by a rule, the two that
# do not), MISHNAH_TOPICS' row notes (Shekels 6:1-2, Suspected Wife 7:6 and Blessings 9:5 ROUTED to 8b), RESEARCH_LOG's entry, THE_STEPS' paragraph,
# THE_BRIEFING's bullet and entry, RESUME's note, the state doc's #197 addendum 6, the recovery page (section 2 rewritten, under 10 KB), the recovery addenda's
# section 49, the stamp row, the memory file and the index line (under 17,000 bytes), and the commit message's paragraph. Every number parsed from a print named
# beside it (--check prints them and writes nothing); every insert on a unique anchor asserted present once; the lints before and after. Sitting 7's form
# (write_ch9_records.py).
import os, re, subprocess, sys, yaml, json
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/' + os.path.abspath(ROOT).replace('/', '-') + '/memory')
DATE = '2026-09-20'; LDATE = '2026-09-19'
UID = 'deu_10_second_tablets'
CHECK = '--check' in sys.argv
def rd(p): return open(p, encoding='utf-8').read()
# ---- THE NUMBERS, PARSED FROM THE PRINTS ----
truth = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py')
assert 'assert len(W["units"]) == 224' in truth and 'assert len(W["standing"]) == 2227' in truth and "8b8fff1fa28953af" in truth
CT = rd(f'{SP}/ch10_truth.out'); CB = rd(f'{SP}/ch10_bake.out'); C1 = rd(f'{SP}/ch10_fold_check1.out')
assert 'CORPUS TRUTH GREEN' in CT and 'CORPUS TRUTH GREEN' in C1 and 'wrote corpus_world.sqlite' in CB
rit = rd(f'{SP}/ch10_ritual_{UID}.out'); N_PASS = len(re.findall(r'^PASS', rit, re.M))
assert 'RITUAL COMPLETE' in rit and N_PASS == 13 and not re.search(r'^FAIL', rit, re.M), N_PASS
vt = rd(f'{SP}/ch10_vt_{UID}.out'); mvt = re.search(r'TEXT LAYER GREEN: (\d+) steps, (\d+) scenarios', vt); assert mvt and mvt.group(1) == '22', vt[-300:]
VT_STEPS, VT_SCEN = mvt.groups()
assert '  status: frozen' in rd(f'{ROOT}/logic/units/{UID}.yaml') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json') and 'ALL_DONE' in rd(f'{SP}/ch10_chain.log')
JG = rd(f'{SP}/ch10_journal.out'); RG = rd(f'{SP}/ch10_register.out'); BW = rd(f'{SP}/ch10_build.out'); GS = rd(f'{SP}/ch10_gates_SUMMARY.txt')
assert 'GATE GREEN' in JG and 'ALL GREEN' in BW and 'THE REGISTER GATE: GREEN' in RG and 'ALL GREEN' in GS, (JG[-200:], BW[-200:], GS[-200:])
mj = re.search(r'(\d+) kinds, ([\d,]+) rows', JG); J_KINDS, J_ROWS = mj.group(1), mj.group(2)
mr = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', RG); R_DECL, R_DEBT, R_FAIL = mr.groups()
assert R_DEBT == '0' and R_FAIL == '0', mr.groups()
mc = re.search(r'(\d+) units, (\d+) facts, (\d+) demands \((\d+) open\)', CT); C_UNITS, C_FACTS, C_DEM, C_OPEN = mc.groups()
assert C_UNITS == '224', C_UNITS
HG = rd(f'{SP}/ch10_home.out'); assert 'GREEN' in HG, HG[-200:]
LED = rd(f'{ROOT}/logic/oral_triage/deu_10_ekev_{LDATE}.md')
ml = re.search(r'\*\*read: (\d+) of \1 — COMPLETE\*\* \((\d+) Onkelos verses and (\d+) Sifrei rows.*?MATERIAL (\d+) Onkelos, CONTEXT (\d+) Onkelos, MATERIAL (\d+) Sifrei outside, CONTEXT (\d+) Sifrei outside', LED, re.S)
L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_XM, L_XC = ml.groups()
assert L_ALL == '25' and L_ONK == '22' and L_SIF == '3' and LED.count('⟨MISS⟩') == 0
L_BYTES = len(LED.encode())
d_ov = yaml.safe_load(rd(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'))
OV_REF10 = len([k for k in d_ov['by_ref'] if k.startswith('Deut.10.')]); OV_REF, OV_GL = len(d_ov['by_ref']), len(d_ov['by_gloss'])
assert OV_REF10 == 89 and OV_REF == 701 and OV_GL == 540, (OV_REF10, OV_REF, OV_GL)
N_CLAIMS = len(json.load(open(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json', encoding='utf-8'))); assert N_CLAIMS == 6
VC = rd(f'{SP}/ch10_vc.out'); assert 'SUMMARY: 6 verified, 0 failed, 0 uncheckable, 0 no-check' in VC
LAB = rd(f'{SP}/ch10_labels.out'); mlab = re.search(r'CLAIM LABELS CENSUS — (\d+) claims in (\d+) manifests; labeled \1; DEBT 0', LAB); LN = f'{int(mlab.group(1)):,} claims in {mlab.group(2)} manifests'; assert 'GATE PASSED' in LAB and re.search(r'deu\s+64 claims', LAB), LAB[-300:]
assert rd(f'{SP}/ch10_ink_run3.out').strip().endswith('0 failing statements') and rd(f'{SP}/ch10_ink_run2.out').strip().endswith('0 failing statements') and rd(f'{SP}/ch10_ink_run1.out').strip().startswith('8 failing statements')
N_INK = len(re.findall(r'^assert ', rd(f'{SP}/ch10_ink.py'), re.M))
LL = rd(f'{SP}/ch10_large_letter.out').strip().split('\n')[-1]; assert LL.endswith('6/6'), LL
JR9 = re.search(r'12 kinds, (\d+) rows', rd(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch9_journal.out')).group(1); DJ = int(J_ROWS.replace(',', '')) - int(JR9)
MAN = rd(f'{SP}/ch10_manifest.out'); assert 'every CITE INDEX name used by a claim: True' in MAN
DUMP = rd(f'{SP}/ch10_dump0.out'); assert 'DB verses 22 | export verses HE 22 EN 22' in DUMP and 'the union of rows (both files): 3' in DUMP
LW = rd(f'{SP}/ch10_records_ledger_line.txt') if os.path.exists(f'{SP}/ch10_records_ledger_line.txt') else ''
print('PARSED:', dict(ritual_pass=N_PASS, verify_text=(VT_STEPS, VT_SCEN), journal=(J_KINDS, J_ROWS, DJ), register=(R_DECL, R_DEBT, R_FAIL), corpus=(C_UNITS, C_FACTS, C_DEM, C_OPEN), ledger=(L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_XM, L_XC, L_BYTES), overrides=(OV_REF10, OV_REF, OV_GL), claims=N_CLAIMS, labels=LN, ink=N_INK, large_letter=LL))
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

STAMP = (f'| {DATE} | {UID} | DELEGATED | FULL RULE | Deuteronomy 10:1-22 derivation {LDATE} (THE DEUTERONOMY WALK sitting 8 — CHAPTER 10; the owner: "Go" after the reread that followed 7b\'s compaction — a reading sitting ONE run, every row whole): Onkelos Deuteronomy 10 whole (22 = 22, the identity) + the Sifrei on Deuteronomy SILENT on the chapter, its {L_SIF} rows outside any piska read whole in both files (two reread) + the kin credited by name; the ledger deu_10_ekev_{LDATE}.md ({L_ALL} sources, coverage computed, lint 0); {N_CLAIMS} claims DV10-01..06 verified 6/0, seated as six WITNESS_READ at 10:1, 5, 6, 10, 12, 17; the ritual {N_PASS} PASS; CORPUS TRUTH GREEN ({C_UNITS} units, standing 2227, hash unmoved); the fold layer +{DJ}; the display layer +{OV_REF10} by reference, +38 by gloss | {LN}, labeled, debt 0 |\n')

WALK = f'''


## Sitting 8 — CHAPTER 10 — AS BUILT ({DATE}; the design above stands as written — the one run ran as designed; every departure from it is named here)

THE RESULT: Deuteronomy 10:1-22 READ, FROZEN and SEATED as ONE unit — deu_10_second_tablets (the 224th frozen unit; 22 of 22 verses, missing 0, computed): the
ledger logic/oral_triage/deu_10_ekev_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the Sifrei\'s outside rows {L_SIF}: MATERIAL {L_XM} / CONTEXT
{L_XC}; {L_BYTES:,} bytes, lint 0, no cut missed), the manifest {N_CLAIMS} claims DV10-01..06 verified 6/0 (every he_contains cut from the store\'s own bytes; every cite
index name used by a claim), seated as six WITNESS_READ operators at 10:1, 5, 6, 10, 12, 17 with step E; the ritual {N_PASS} PASS; verify_text GREEN ({VT_STEPS} steps,
{VT_SCEN} scenarios); the fold predicted and matched (units 223 → 224, standing 2221 → 2227, the hash 8b8fff1fa28953af unmoved — CORPUS TRUTH GREEN before and after
the bake: {C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, {C_OPEN} open); build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer since
chapter 9\'s reading, the tape unmoved since 7b); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — 10:5\'s "as the LORD commanded me" and 10:22\'s
seventy the chapter\'s two listed seats, both declared NONE since the register\'s census, the dispositions 8b\'s); large_letter_probes {LL[-3:]}; the labels census GREEN
({LN}, Deuteronomy 64); the home-path gate GREEN; the display layer +{OV_REF10} by reference and +38 by gloss ({OV_REF} / {OV_GL} in all).

THE READING: every Onkelos row whole in the Aramaic and the English (ch10_onkelos.txt); every one of the three outside rows whole in both files
(ch10_sifrei_outside.txt), the two read before reread whole (32:1 from sitting 4; 311:5 from the Babel sitting); the kin (Exodus 34:1-4 and 28-29, 25:10-22, 37:1-9,
31:18; Numbers 33:30-39, 20:22-29, 3:5-13, 8:5-26, 18:20-24; Exodus 22 and 23; Leviticus 19) credited by name with the counts computed from those ledgers (the second
tablets 2, the ark 2, the furniture 2, the craftsmen 1; the journeys 10, Aaron\'s death 8, the Levites 10 and 22, the dues 5; Exodus 22 and 23 and Leviticus 19 at the
chapter\'s grain); the seventy\'s first telling (Genesis 46:27) holds its Onkelos rows in the Genesis walk\'s table-form ledgers — no row line (computed).

THE DEPARTURES FROM THE DESIGN: none in substance. THE INK\'S FIRST PASS FELL EIGHT WAYS ON FORMS (none a fact, each retyped from the print): the Numbers walk\'s later
ledgers write "Deuteronomy" whole where the earlier write "Deut"; the Genesis ledgers hold no "- Onkelos Gen 46:" row line (the table form); "and come up to Me on the
mountain" carries its vav at 10:1 and not at Exodus 24:12; "the ark of the testimony" spelled two ways in Exodus (three seats each); "your might" (6:5) beside Josiah\'s
"his might"; the heaven of heavens with the vav at 1 Kings 8:27 and the Chronicler\'s as at 10:14, without at Nehemiah 9:6 and Psalm 148:4; "seventy" forty-two seats,
not forty-three; the Bene-jaakan tokens by U, not P — FOUR of the eight the measure\'s SUM OF SEARCHES read as one search. THE LEDGER\'S FIRST WRITE fell twice on the
piece cap (two Hebrew pieces of eight tokens at 10:12 and 10:17, split); THE MIDDAH CODE E10 was typed at three outside rows on chapter 9\'s precedent and CHECKED IN
MIDDOT.md AFTER — "repeated expression": right for 311:5\'s "borders, not border", wrong for 32:1 (a distinction between two verses) and 301:4 (a proof-text for the
count), both relabeled NO CODE before the ledger stood; the lint flagged the infinitive list\'s Hebrew tokens without English (glossed) and "bene-jaakan" (glossed
"the wells of the sons of Jaakan"); THE KIN REGEXES for Exodus 22, 23 and Leviticus 19 matched no row (the ledgers\' row heads are the chapters\' own verses, not the
stranger\'s) — counted at the chapter\'s grain; THE LABELS CENSUS refused two labels ending in bare prose (its regex wants a label to END in its note) — closed; the
claims verifier takes the manifest\'s PATH, not the unit\'s name; the fold script\'s sed derivation ate its own nested heredoc twice — written by hand.

THE GATES, COMPUTED FROM THEIR PRINTS: the ritual {N_PASS} PASS (RITUAL COMPLETE, {C_UNITS} frozen units); CORPUS TRUTH GREEN twice ({C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, {C_OPEN} open;
the hash unmoved); build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows, +{DJ}); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL});
verify_claims 6 verified / 0 failed; the labels census GREEN ({LN}); large_letter_probes {LL[-3:]}; the home-path gate GREEN; the ink {N_INK} asserts — 8 failing on the first
typed pass, 0 on the second and third (the third after the display patch).

⚠ THE LESSONS (the run\'s, gathered — the numbered list the sheet asks for): (1) THE RETELLING\'S ADDITIONS ARE THE COMPILE\'S QUESTIONS — the ark inserted into God\'s
quoted word (10:1-2 against Exodus 34:1: eleven of fourteen shared, two tokens added) found by the diff, as Aaron\'s peril was at chapter 9; the fragments in the ark
the compile\'s design. (2) THE HELPERS ARE COPIED BY CONTENT MARKERS, NEVER RETYPED — derive_ch10_ink.py takes the prior ink\'s six generic blocks by their first and
last lines; the constants and the asserts alone are the sitting\'s. (3) A SUM OF SEARCHES IS NOT ONE SEARCH — where the measure prints P(a) + P(b), the ink asserts each
alone (four of the eight fell there: two spellings, a vav, a suffix). (4) THE LEDGERS\' BOOK NAMES DIFFER BY AGE — the Numbers walk\'s later ledgers write the book\'s
full name; a grep for a verse asks both forms. (5) THE GENESIS LEDGERS HAVE NO ROW LINE — a kin credit by row-count finds nothing in the table form; named as such. (6)
A MIDDAH CODE IS CHECKED BEFORE IT IS TYPED — E10 typed on a precedent and checked after cost two rows a relabel; the rule\'s order, not its outcome, was missed. (7)
THE CENSUS WANTS A LABEL TO END IN ITS NOTE — the regex\'s tail; a label\'s last clause takes its parenthesis. (8) THE HEBREW PIECE CAP IS SEVEN — a piece of eight fails
at the cut, not at the lint; split at the clause. (9) A DERIVATION THAT CROSSES A NESTED HEREDOC IS WRITTEN BY HAND — sed ate the fold script\'s tail twice. (10) THE
VERIFIER TAKES THE MANIFEST\'S PATH (chapter 6\'s lesson again). (11) THE SHELF QUOTES ONE VERSE TWO WAYS — 301:4 plene and 311:5 defective on 10:22\'s "your fathers",
the DB defective: the two rows\' bytes asserted apart. (12) THE PARSER READS THE PLURAL "FIRST" AS NO ORDINAL — the lemma five times in the chapter, one count. (13) THE
READING SITTING HELD IN ONE RUN under the two-run rule, the fifth in a row.

THE FORMS: World/step9/forms_deuteronomy_walk/ (copy_ch10_forms.py — derive_ch10_dump0.py, ch10_dump0.py, derive_ch10_measure1.py, ch10_measure1_sections.py,
ch10_measure1.py, ch10_ink_head.py, ch10_ink_body.py, derive_ch10_ink.py, ch10_ink.py, ch10_ink_diag.py, patch_ink_ch10.py, assert_driver.py, ch10_rows_onkelos_a.py,
ch10_rows_onkelos_b.py, ch10_rows_outside.py, write_ch10_ledger.py, ch10_patch_overrides.py, write_ch10_manifest.py, seat_ch10.py, write_ch10_design.py,
write_ch10_records.py, ch10_chain.sh, ch10_fold.sh, ch10_gates.sh and the prints).

NEXT on the ruling: the commit on the owner\'s word (the cache, 7b and this sitting stand uncommitted since a985fbc — one message); then THE COMPILE OF CHAPTER 10
(sitting 8b) in TWO RUNS — RUN A: the rereads (THE_STEPS Step 5 + the compiler block; this section; the 8b box in COMPILE_DEBT), the measurements (the ark\'s lines
in the furniture, erection and second-tablets runners — THE FRAGMENTS IN THE ARK; the stations\' and Aaron\'s lines in the journeys and Meribah runners; the Levites\'
in Numbers 3, 8, 18; the third forty\'s end on the clock; 6:5\'s, 6:13\'s and the stranger\'s cells for the laws\' form; the receipt seats 10:5 and 10:9 in the register),
THE DESIGN, the probes to FAIL, THE DOCKET by the union rule (Bava Batra 14a-b, Menachot 99a-b, Berakhot 8b and 33b, Menachot 43b, Yoma 69b, Berakhot 20b, Niddah
70b, Ketubot 105a-b, Bava Metzia 59b, Yevamot 47a-b, Ketubot 111b, Shevuot 35b, Temurah 3b-4a, Bava Batra 123a-b, Seder Olam 6 and 9-10 — every row whole); RUN B:
the types, the runner, the tape to 10/10, the chain, the records, the forms, the commit message — or the Decalogue-schema sitting first, on his word.
'''

DEBT = f'''

## SITTING 8 — CHAPTER 10 ({DATE}, the reading; deu_10_second_tablets frozen) — OWED TO THE COMPILE 8b: (a) THE FRAGMENTS IN THE ARK — 10:1-5 against the second
## tablets\' lines (Exodus 34:1-4, 28-29) and the ark\'s (25:10-16, 37:1-9, 40:20): the ark made BEFORE the ascent and the tablets put in it "as the LORD commanded me";
## 7b\'s owed item (i) — the shelf\'s two arks (Bava Batra 14a-b, Menachot 99a-b: the tablets and the broken tablets in one ark); the readback\'s rows — 10:2 VERBATIM
## with Exodus 34:1 (eleven of fourteen) and the ark\'s clause ADDED, 10:1 VARIANT (the spelling), 10:3 and 10:5 EXPANDED (the ark), 10:4 VARIANT; (b) THE RECEIPT SEATS
## — 10:5 "as the LORD commanded me" (the register gate lists it declared NONE — its disposition the compile\'s; 4:5 the kin) and 10:9 "as the LORD your God spoke to
## him" (by "spoke" — the finder\'s third form, 4b\'s owed item; Numbers 18:20 the word); (c) THE STATIONS AND AARON\'S DEATH — 10:6-7 against Numbers 33:30-39 (the
## order reversed: Moseroth then Bene-jaakan there, Beeroth-bene-jaakan then Moserah here) and 20:22-29 (Aaron dies at Mount Hor on the tape, dated the fortieth
## year\'s fifth month; at Moserah in the retelling): an OPEN row, the shelf\'s answer at the docket (Seder Olam 9-10; Rosh Hashanah 3a, Ta\'anit 9a); "and he was
## buried there" the Torah\'s one seat; (d) "AT THAT TIME" THE LEVITES SEPARATED (10:8) — which time: the calf\'s (Exodus 32:26-29 "fill your hand") or Numbers 8:14\'s
## line on the tape; the three offices (to carry — Numbers 4; to stand and minister — 18; to bless — 6:23-27, the blessing ledger\'s 10:8 note) by CALL; 10:9 against
## Numbers 18:20-24 and 18:1-2 (the LORD his inheritance — Onkelos\'s gifts); (e) THE THIRD FORTY\'S END (10:10 — the second ascent to 10 Tishri on 7b\'s clock: the
## third stretch row; Seder Olam 6; Ta\'anit 30b) and 10:11 against Exodus 32:34 and 33:1 (the command to go; 31:7 and Joshua 1:6 the charge repeated); (f) THE LAWS
## RESTATED — 10:12-13 and 10:20 against 6:5\'s and 6:13\'s cells (hear_o_israel by CALL; 10:20 6:13 with a FOURTH clause "and to Him you shall cleave"), 10:17-19
## against Exodus 22:20-23, 23:8-9 (the ordinances runner) and Leviticus 19:33-34 (Kedoshim) — the laws\' form on the kin, every row graded against the cell that
## compiles it; (g) "WHAT DOES THE LORD YOUR GOD ASK OF YOU" (10:12 — 6b\'s and 7b\'s owed item (vi) paid here: the demand in five infinitives; Berakhot 33b "is the
## fear of heaven a small thing?", Menachot 43b a hundred blessings from "what", Shabbat 31b, Sotah 14a); (h) THE ATTRIBUTES (10:17 — "God of gods and Lord of lords"
## Psalm 136:2-3; the great, mighty and awesome God — Yoma 69b\'s great assembly restoring what Jeremiah and Daniel dropped, Berakhot 33b\'s one who adds, Megillah
## 25a; "who lifts no face" against Numbers 6:26\'s "the LORD lift His face" — Berakhot 20b, Niddah 70b, the Sifrei on Numbers 42:2, the blessing ledger\'s three
## reconciliations; the bribe — Ketubot 105a-b, 16:19 the law\'s seat by CALL); (i) THE STRANGER (10:18-19 — "and you shall love" five in the Torah; "for you were
## strangers" at all four seats; Onkelos\'s convert and dwellers; Bava Metzia 59b the thirty-six warnings; Yevamot 47a-b); (j) THE HEART\'S FORESKIN AND THE NECK
## (10:16 — the chapter\'s one prohibition; the stiff neck 7b left as a state, now a command; 30:6 the LORD circumcises); (k) THE SEVENTY AND THE STARS (10:22 — the
## register\'s seat "souls [70]" declared NONE; the Joseph runner\'s cell by CALL; Bava Batra 123a-b Jochebed the seventieth; the shelf\'s two spellings of the quoted
## verse a DATA row; 1:10 and 28:62 the kin); (l) THE PARSER ON "FIRST" — the plural no ordinal, the singular with the article one — a DATA row; NO MEMRA in the
## chapter a DATA row; (m) THE CHECKPOINT SERIES continues (DA the open series — DA9 the last name; the next DB1, keyed by its first word); (n) THE DOCKET by the
## union rule — Bava Batra 14a-b, Menachot 99a-b, Berakhot 8b (the ark), Mishnah Shekalim 6:1-2 (the ark hidden), Berakhot 33b, Menachot 43b, Shabbat 31b, Sotah 14a
## (the demand and the ways), Yoma 69b, Megillah 25a, Berakhot 20b, Niddah 70b, Mishnah Berakhot 9:5 (the attributes), Ketubot 105a-b (the bribe), Bava Metzia 59b,
## Yevamot 47a-b (the stranger), Ketubot 111b, Shevuot 35b, Temurah 3b-4a, Sanhedrin 56a (the four clauses), Bava Batra 123a-b (the seventy), Rosh Hashanah 3a,
## Ta\'anit 9a, Seder Olam 6 and 9-10 (Aaron and the forty), Mishnah Sotah 7:6 (the blessing in the Name — 10:8) — EVERY ROW WHOLE; a docket past ~700 rows its own run.
## NOTHING ELSE IN CHAPTER 10 IS OWED TO A LATER SITTING OF ITS OWN.
'''

MIDDOT = f'''- **THE SIFREI ON DEUTERONOMY\'S OWN CASE LAW ON CHAPTER 10 (Deuteronomy 10:1-22; THE DEUTERONOMY WALK sitting 8, {DATE};
  the ledger logic/oral_triage/deu_10_ekev_{LDATE}.md — THE SPINE SILENT ON THE CHAPTER, no piska head between 36 on 6:9 and 37 on
  11:10; its three rows outside any piska read whole in both files, the one that argues by a numbered rule and the two that do not):**
  · BORDERS, NOT BORDER (311:5 on 32:8 from 10:22): "he set the borders of the peoples according to the number of the children of
    Israel" — sixty queens and eighty concubines are a hundred and forty nations against the seventy souls who went down (10:22), so
    the plural "borders" gives each nation two shares — E10 (the repeated expression signifies: the noun read for its number; the row\'s
    own form "אין כתוב כאן אלא" ("is not written here but") on its bytes; the code checked in MIDDOT.md AFTER it was typed on chapter
    9\'s precedent — the rule\'s order missed, the outcome held); THE INK: 10:22 quoted DEFECTIVE here ("your fathers" without the vav,
    as the DB writes it) and PLENE at 301:4 — the shelf\'s two spellings of one quoted verse (asserted on both rows\' bytes).
  · ACT FROM LOVE, NOT FROM FEAR (32:1 on 6:5 from 10:20): "the LORD your God you shall fear and Him you shall serve" (10:20) quoted
    as the fearer\'s seat against 6:5\'s "you shall love" — the lover\'s reward doubled; love and fear together in the All-Present alone —
    NO MIDDAH CODE (a distinction argued between two verses; the E10 typed first RELABELED before the ledger stood); THE INK: 10:20
    against 6:13 seven of eight tokens, "and to Him you shall cleave" the fourth clause; 10:12 puts fear and love in one demand.
  · WITH FEW — THE SEVENTY (301:4 on 26:5 from 10:22): the first-fruits confession\'s "with few" measured by "with seventy persons your
    fathers went down" — NO MIDDAH CODE (a proof-text read for its count; the E10 typed first RELABELED); THE INK: "with seventy
    persons" 10:22 the one seat, Exodus 1:5 the words in the other order, Genesis 46:27 "seventy" alone; the parser [70].
'''

RESEARCH = f'''

## {DATE} — DEUTERONOMY 10 READ AND FROZEN (THE DEUTERONOMY WALK sitting 8, one run): THE ARK INSERTED INTO GOD\'S QUOTED WORD; THE STATIONS REVERSED AND AARON MOVED;
## THE BOOK\'S ARK IS THE COVENANT\'S, EXODUS\'S THE TESTIMONY\'S; THREE RECEIPT FORMS IN ONE CHAPTER; THE SHEMA\'S LAW SAID AGAIN WITH A FOURTH CLAUSE; "AND YOU SHALL
## LOVE" FIVE TIMES IN THE TORAH; THE SHELF QUOTES ONE VERSE TWO WAYS
On the owner\'s "Go" after the reread that followed 7b\'s compaction (2026-09-19/20). THE READING: Deuteronomy 10:1-22 with Onkelos whole (the export\'s 22 rows the
DB\'s 22 — the identity, asserted) and the Sifrei on Deuteronomy SILENT ON THE CHAPTER (36 on 6:9, 37 on 11:10), its whole voice three rows from elsewhere found by
the union of both files\' citations and read whole (32:1 act from love — 10:20 the fearer\'s seat; 301:4 with few — the seventy quoted plene; 311:5 the hundred and
forty nations against seventy souls — E10, quoted defective); two reread whole. FROZEN as ONE unit deu_10_second_tablets (the 224th; standing 2227 = 2221 + 6 as
predicted, hash unmoved); the ledger deu_10_ekev_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the outside rows {L_SIF}: MATERIAL {L_XM} / CONTEXT
{L_XC}; coverage computed, lint 0, no cut missed); six claims DV10-01..06 verified 6/0, seated as six WITNESS_READ at 10:1, 5, 6, 10, 12, 17; the ritual {N_PASS} PASS; the
fold +{DJ} on the journal; the display layer +{OV_REF10} by reference and +38 by gloss. THE FINDS: 10:1-2 QUOTE EXODUS 34:1 word for word (six tokens, then eleven of
fourteen) and INSERT THE ARK — "come up to Me on the mountain" (Exodus 24:12\'s call, the two seats), "make for yourself an ark of wood" (one seat), "and you shall
put them in the ark" (two tokens Exodus 34 never gives); 10:3 makes the ark of acacia BEFORE the ascent; 1 Kings 8:9 reads the ark\'s contents from this telling;
THE STATIONS REVERSED — Numbers 33:30-34 Moseroth then Bene-jaakan, 10:6 Beeroth-bene-jaakan then Moserah, one token shared, and AARON\'S DEATH MOVED from Mount Hor
(33:38, dated) to Moserah; "and he was buried there" the Torah\'s one seat; "ministered as priest" the wayyiqtol at 10:6 and Numbers 3:4 alone; "separated" the hiphil
perfect at 10:8 and Numbers 16:9 alone; THE BOOK\'S ARK IS "OF THE COVENANT" (four seats, never in Exodus), EXODUS\'S "OF THE TESTIMONY" (seven, in two spellings,
never in the book); THREE RECEIPT FORMS — "as the LORD commanded me" (10:5, 4:5 — the register gate\'s seat, declared NONE), "as the LORD your God spoke to him"
(10:9 — by "spoke"), "which I swore to their fathers" (10:11 — repeated to Joshua in seven shared tokens); "at that time" twice (10:1, 10:8); THE THIRD FORTY (10:10)
the phrase\'s fifth seat in the book; THE DEMAND IN FIVE INFINITIVES (10:12-13) with the Shema\'s seven tokens inside and Micah 6:8\'s five; THE HEAVEN OF HEAVENS six
in the Bible, with the vav at Solomon\'s dedication as here; "circumcise the foreskin of your heart" the command\'s one seat and "stiffen your neck no more" the
chapter\'s one prohibition — the calf\'s adjective made a command; "God of gods and Lord of lords" Psalm 136:2-3; "who lifts no face" against Numbers 6:26; the
judge\'s bribe law (16:19, Exodus 23:8) made the Judge\'s nature; "AND YOU SHALL LOVE" FIVE IN THE TORAH (the LORD twice, the neighbor, the stranger twice) and "for you
were strangers" at all four seats; 10:20 AGAINST 6:13 SEVEN OF EIGHT — the fourth clause "and to Him you shall cleave" added; "He is your praise" one seat; THE
SEVENTY TOLD IN NEW WORDS (two tokens with Genesis 46:27, one with Exodus 1:5); THE PARSER reads the plural "first" as no ordinal and the singular "the first
writing" as [1]; NO MEMRA IN THE CHAPTER; MOSES UNNAMED from chapter 6 to 11; ONKELOS — the gifts supplied for "the LORD is his inheritance" (18:2 and Numbers
18:20 the same), the ways "that are right before Him", the foolishness of the heart, God of JUDGES and Lord of KINGS, the CONVERT loved and the DWELLERS you were,
"draw near to His fear" for cleave, "establish" for swear. THE CAUTION: the shelf quotes 10:22 two ways — 301:4 "your fathers" plene, 311:5 defective, the DB
defective (chapter 6\'s lesson in a new form). THE LESSONS (thirteen, in the map): the retelling\'s additions are the compile\'s questions; the helpers copied by
content markers; a sum of searches is not one search; the ledgers\' book names differ by age; a middah code is checked before it is typed. OWED TO 8b: the fragments
in the ark, the receipt seats, the stations\' open row, the Levites\' "at that time", the third forty\'s end, the laws restated by CALL, the demand, the attributes
against the blessing, the stranger, the seventy.
'''

STEPS = f'''DEUTERONOMY — SITTING 8 — CHAPTER 10, Deuteronomy 10:1-22 ({DATE}, on Brian\'s "Go" after the reread that followed the chapter-9 compile\'s compaction;
World/step9/DEUTERONOMY_WALK.md "Sitting 8" and "Sitting 8 — AS BUILT"; a reading sitting is one run). Chapter 10 finishes the retelling and turns to the law: the
second tablets and an ark to hold them, the stations where Aaron died and Eleazar took his place, the tribe of Levi set apart, the third forty days and the command
to go; then what the LORD asks — to fear, to walk, to love, to serve, to keep — the heavens His and the fathers chosen, the heart to be circumcised and the neck no
more stiff; the God of gods who takes no bribe and loves the stranger; fear, serve, cleave, swear; seventy souls become the stars. The reading laid each verse
beside its first telling and counted the shared words: God\'s word to hew the tablets comes back word for word from Exodus 34 — with an ark put into the middle of
it that Exodus never mentions there; the stations come back in another order, and Aaron\'s death at another station than Numbers gives; the ark is "of the
covenant" here where Exodus always says "of the testimony"; three verses carry a receipt ("as the LORD commanded me", "as He spoke to him", "which I swore");
the Shema\'s "fear, serve, swear" comes back with a fourth clause, "cleave". The Sifrei has no section on the chapter; three rows from elsewhere read it for one
clause of 10:20 and for the seventy of 10:22 — and quote that verse with two spellings. The chapter is frozen as one unit, the 224th, the world\'s standing facts
up by six as predicted, its hash unmoved, every gate green. The ink script fell eight ways on its first pass — all forms, none a fact — and held on the second.
Next: the commit on your word; then the compile of chapter 10 in two runs — the ark and the fragments in it, the receipt seats, the stations\' open row, the third
forty\'s end on the clock, the laws restated graded against their cells — or the ten-commandments schema first.


'''

BRIEF = f'''- **CHAPTER 10 READ AND FROZEN — THE ARK PUT INTO GOD\'S QUOTED WORD: MOSES RETELLS EXODUS 34 WORD FOR WORD AND ADDS AN ARK; THE STATIONS COME BACK REVERSED AND AARON DIES AT ANOTHER PLACE; THE SHEMA\'S "FEAR, SERVE, SWEAR" COMES BACK WITH "CLEAVE"; THE SIFREI QUOTES ONE VERSE TWO WAYS** ({DATE}, on your "Go"; World/step9/DEUTERONOMY_WALK.md "Sitting 8" and "Sitting 8 — AS BUILT"; the ledger deu_10_ekev_{LDATE}.md, {L_ALL} sources whole; the unit deu_10_second_tablets the 224th, standing 2227, hash unmoved; six claims 6/0; every gate green; one run, every row whole).
'''
BRIEF_ENTRY = f'''### {DATE} — CHAPTER 10 READ: THE ARK ADDED TO GOD\'S WORD, THE STATIONS REVERSED, THE FOURTH CLAUSE

Chapter 10 is the end of Moses\' retelling and the start of the law. The reading
laid each verse beside its first telling and counted shared words. God\'s command
to hew a second pair of tablets comes back from Exodus 34 word for word — eleven
words of fourteen — and between its two halves Moses puts something Exodus never
says there: "make for yourself an ark of wood … and you shall put them in the
ark". He makes the ark before he climbs; he puts the tablets in it "as the LORD
commanded me" — a receipt inside a story, which the register gate already lists
as a seat waiting for its compile. The wilderness stations come back in a
different order from the itinerary in Numbers, and Aaron dies at a different
station. The book calls the ark "of the covenant"; Exodus always calls it "of
the testimony". The Shema\'s "fear, serve, swear by His name" comes back with a
fourth clause, "cleave to Him". And the Sifrei, silent on the chapter, quotes
its last verse twice with two spellings of "your fathers". The chapter is frozen
as one unit, every gate green, in one run with every row read whole. The compile
next: the fragments in the ark, the stations\' open row, the third forty\'s end on
the clock, and the laws graded against the cells that already compile them.

'''

RESUME_NOTE = f'''# ⚠ THE DEUTERONOMY WALK sitting 8 ({DATE}; step9/DEUTERONOMY_WALK.md "Sitting 8" + "Sitting 8 — AS BUILT"): CHAPTER 10 READ AND FROZEN as ONE unit
# (deu_10_second_tablets, the 224th; standing 2227, hash unmoved) — the ark inserted into God\'s quoted word (10:1-2 against Exodus 34:1: eleven of fourteen, the ark\'s
# clause added), the stations reversed and Aaron moved (the compile\'s OPEN row), three receipt forms (10:5 the register\'s seat), 6:13 said again with "cleave"; the
# Sifrei silent, three outside rows whole; the ledger deu_10_ekev_{LDATE}.md ({L_ALL} sources); six claims seated; the fold +{DJ} on the journal ({J_ROWS} rows); every
# gate green. NEXT on the owner\'s word: the commit (the cache, 7b, this); then 8b — the compile of chapter 10 (the fragments in the ark; DA the open series).
'''

STATE = f'''
#197 ADDENDUM 6 ({DATE}, at the close of THE DEUTERONOMY WALK sitting 8 — CHAPTER 10\'s READING, the ONE run, on the owner\'s "Go" after the reread that followed 7b\'s compaction — A CLEAN COMPACTION POINT): THE STATE: chapter 10 read and frozen as one unit (deu_10_second_tablets, the 224th); the corpus {C_UNITS} units, standing 2227 (2221 + 6 as predicted), hash 8b8fff1fa28953af unmoved; the tape unmoved since 7b (RUN (1311, 96, 88, 0, 12, 1606, 40, 319, the four pairs, 127), markers 169, closes 127); the ledger deu_10_ekev_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the outside rows {L_SIF}: MATERIAL {L_XM} / CONTEXT {L_XC}; {L_BYTES:,} bytes, lint 0); the manifest 6 claims verified 6/0, seated at 10:1, 5, 6, 10, 12, 17; the display layer +{OV_REF10} / +38 ({OV_REF} / {OV_GL}). THE GATES: the ritual {N_PASS} PASS; verify_text GREEN ({VT_STEPS} steps, {VT_SCEN} scenarios); CORPUS TRUTH GREEN twice; build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer since chapter 9\'s reading); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT 0, FAILS 0 — 10:5 and 10:22 the chapter\'s listed seats, declared NONE, the dispositions 8b\'s); the home-path gate GREEN; the labels census GREEN ({LN}, Deuteronomy 64); large_letter_probes {LL[-3:]}; the ink {N_INK} asserts, 8 failing on the first typed pass (forms), 0 on the second and third. THE RUN\'S SHAPE: the reading sitting\'s one run — the rereads (the recovery page, the map\'s newest section, the memory; THE_STEPS\' compiler block, Step 2, Step 5\'s head), the dump derived by twenty-three substitutions, the measure built from chapter 9\'s helpers with the shared count on every diff line, the ink ASSEMBLED (the generic helpers copied from chapter 9\'s ink by content markers, the constants and asserts the sitting\'s), THE DESIGN in the map before a row was typed, the twenty-two Onkelos rows and the three outside rows whole, the ledger (two pieces of eight tokens split; the middah E10 relabeled at two rows after its check in MIDDOT — the rule\'s order missed; the lint\'s Hebrew-without-English on the infinitive list glossed), the patch (38 by gloss, 89 by reference), the manifest, the claims verified and the labels census (two labels closed with their notes), the seat, the chain, the fold, the gates in one chain (ch10_gates.sh), the records from the sheet in one call (write_ch10_records.py). THE FINDS: THE ARK INSERTED INTO GOD\'S QUOTED WORD (10:1-2 against Exodus 34:1 — six then eleven of fourteen, "come up to Me on the mountain" Exodus 24:12\'s, "and you shall put them in the ark" added; 10:3 the ark before the ascent; 10:5 "as the LORD commanded me" the receipt, 1 Kings 8:9 reading the ark\'s contents from it), THE STATIONS REVERSED AND AARON MOVED (10:6 against Numbers 33:30-38 — one token; the OPEN row), the book\'s ark "of the covenant" against Exodus\'s "of the testimony", "separated" and "ministered as priest" each at two Torah seats (Numbers 16:9; 3:4), three receipt forms, "at that time" twice, the third forty (10:10), the demand in five infinitives with the Shema\'s tokens and Micah 6:8\'s, the heaven of heavens with the vav at Solomon\'s dedication, the heart\'s foreskin and the neck (the chapter\'s one prohibition), "God of gods" Psalm 136:2-3 and the face not lifted against Numbers 6:26, "and you shall love" five in the Torah and "for you were strangers" at all four seats, 10:20 against 6:13 seven of eight with "cleave" added, the seventy told in new words, the parser\'s plural "first" no ordinal, no Memra in the chapter, Onkelos\'s gifts, right ways, foolishness, judges and kings, convert and dwellers; the shelf\'s two spellings of the quoted 10:22. THE RECORDS (write_ch10_records.py from the sheet): the map\'s "Sitting 8 — CHAPTER 10 — AS BUILT" (thirteen lessons), COMPILE_DEBT\'s sitting-8 box (a)-(n) owed to 8b, MIDDOT\'s chapter-10 block (E10 at 311:5; the two rows without a code, relabeled), MISHNAH_TOPICS (Shekels 6:1-2, Suspected Wife 7:6, Blessings 9:5 routed to 8b), RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the bullet and an entry; the scoreboard\'s date), RESUME, this addendum, the addenda §49, the recovery page (section 2 rewritten under its cap), the stamp row, the memory (the walk note and the index line under 17,000), the commit message\'s paragraph. THE FORMS copied (copy_ch10_forms.py). NOT COMMITTED (since a985fbc): THE VERIFIED-IMPORT CACHE, sitting 7b and this sitting 8 — ONE message at <scratch>/commit_msg_ch9b.txt covers all three for the owner\'s word ("commit" = no push; "commit push" = both). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. NEXT ON THE RULING: the commit on his word; then THE COMPILE OF CHAPTER 10 (8b) in TWO RUNS — RUN A the rereads, the measurements (the ark\'s lines in the furniture, erection and second-tablets runners — THE FRAGMENTS IN THE ARK; the stations\' and Aaron\'s lines; the Levites\'; the third forty\'s end on the clock; the laws\' cells; the receipt seats 10:5 and 10:9), the design, the probes to FAIL, the docket by the union rule (every row whole; its own run past ~700 rows); RUN B the types, the runner, the tape to 10/10, the chain, the records — or the Decalogue-schema sitting first; THE INSTALL HYPOTHESIS, THE SUPPLIED GRADE and THE SUPPLIED-WITH-A-WRITE FORM on the table. POST-COMPACTION REREADS: the recovery page, the map\'s "Sitting 8 — AS BUILT" (the newest section — the departures and the lessons), MEMORY.md.
'''

ADDENDA = f'''
## 49. ADDENDUM ({DATE}, THE DEUTERONOMY WALK sitting 8 — CHAPTER 10, Deuteronomy 10:1-22 READ AND FROZEN in ONE run under THE TWO-RUN RULE, every row whole; the owner: "Go" after the reread that followed 7b\'s compaction; the state doc\'s #197 addendum 6)
THE READING: Onkelos Deuteronomy 10 whole (22 = 22, the identity, cost 14); the Sifrei SILENT on the chapter — three rows outside any piska by the union of both files
(32:1 reread whole from sitting 4; 311:5 reread whole from the Babel sitting; 301:4 fresh); the kin credited by name (the Exodus ledgers on the second tablets, the ark
and its making, the craftsmen; the Numbers ledgers on the journeys, Aaron\'s death, the Levites and their dues; the Exodus and Leviticus ledgers on the stranger); the
unit deu_10_second_tablets the 224th (standing 2227, hash unmoved); the ledger {L_ALL} sources (Onkelos MATERIAL {L_OM} / CONTEXT {L_OC}; the outside rows MATERIAL {L_XM} /
CONTEXT {L_XC}); six claims 6/0 seated at 10:1, 5, 6, 10, 12, 17; the display layer +{OV_REF10} by reference, +38 by gloss; every gate green in one chain (ch10_gates.sh).
THE INK ASSEMBLED, not retyped: derive_ch10_ink.py copies the prior ink\'s generic helpers by content markers; eight asserts fell on the first pass (four a sum of
searches read as one), none a fact. THE FINDS: THE ARK INSERTED INTO GOD\'S QUOTED WORD (10:1-2 against Exodus 34:1 eleven of fourteen, the ark\'s clause added; 24:12\'s
call; the ark before the ascent; 10:5\'s receipt the register\'s seat; 1 Kings 8:9); THE STATIONS REVERSED AND AARON MOVED (the OPEN row); the ark of the covenant
against the ark of the testimony; three receipt forms; "at that time" twice; the third forty; the demand in five infinitives; the heaven of heavens; the heart\'s
foreskin and the one prohibition; God of gods, the face not lifted, the bribe; "and you shall love" five, "for you were strangers" four; 10:20 against 6:13 with
"cleave" added; the seventy in new words; the plural "first" no ordinal; no Memra; Onkelos\'s gifts, right ways, foolishness, judges and kings, convert and dwellers;
the shelf\'s two spellings of the quoted 10:22. THE LESSONS (thirteen, in the map): the retelling\'s additions are the compile\'s questions; the helpers copied by
content markers; a sum of searches is not one search; the ledgers\' book names differ by age; the Genesis ledgers have no row line; A MIDDAH CODE IS CHECKED BEFORE IT
IS TYPED (relearned); the census wants a label to end in its note; the piece cap is seven; a nested heredoc is written by hand; the verifier takes the path. OWED TO
8b (COMPILE_DEBT\'s box (a)-(n)): the fragments in the ark, the receipt seats, the stations\' open row, the Levites\' "at that time", the third forty\'s end, the laws
restated by CALL, the demand, the attributes against the blessing, the stranger, the seventy, the docket. The records on the sheet; the forms in
World/step9/forms_deuteronomy_walk/ (copy_ch10_forms.py).
'''

MEMPAR = f'''
SITTING 8 DONE {DATE} ("Go" after the reread that followed 7b\'s compaction; the map\'s "Sitting 8" and "Sitting 8 — AS BUILT"): CHAPTER 10 READ AND FROZEN as ONE
unit deu_10_second_tablets (the 224th; standing 2227 = 2221 + 6 as predicted, hash unmoved) in ONE run, every row whole — Onkelos 22 rows (the identity), the Sifrei
SILENT (three outside rows whole, two reread), the kin credited by name; the ledger deu_10_ekev_{LDATE}.md ({L_ALL} sources); six claims 6/0 seated at 10:1, 5, 6, 10,
12, 17; every gate green; the display layer +{OV_REF10} / +38. THE FINDS: THE ARK INSERTED INTO GOD\'S QUOTED WORD — 10:1-2 against Exodus 34:1 eleven of fourteen with
"and you shall put them in the ark" ADDED (the fragments in the ark 8b\'s design); THE STATIONS REVERSED AND AARON MOVED (10:6 against Numbers 33:30-38 — the OPEN
row); the book\'s ark "of the covenant", Exodus\'s "of the testimony"; THREE RECEIPT FORMS (10:5 "as the LORD commanded me" the register\'s seat declared NONE; 10:9 by
"spoke"; 10:11 the oath); "at that time" twice (the Levites\' time 8b\'s question); the third forty (10:10); the demand in five infinitives; 10:20 against 6:13 with
"cleave" added; "and you shall love" five in the Torah; the seventy in new words; the shelf quotes 10:22 two ways. ⚠ LESSONS (thirteen, in the map): the
retelling\'s additions are the compile\'s questions; THE HELPERS COPIED BY CONTENT MARKERS (derive_ch10_ink.py), never retyped; A SUM OF SEARCHES IS NOT ONE SEARCH;
the ledgers\' book names differ by age (grep both); the Genesis ledgers have no row line; A MIDDAH CODE IS CHECKED BEFORE IT IS TYPED — relearned (E10 typed on a
precedent, two rows relabeled); the census wants a label to end in its note; the piece cap is seven; a nested heredoc is written by hand. OWED TO 8b: the fragments
in the ark, the receipt seats 10:5 and 10:9, the stations\' open row, the Levites\' "at that time", the third forty\'s end, the laws restated by CALL (6:5, 6:13, the
ordinances, Kedoshim), the demand (10:12 — 6b\'s owed item), the attributes against Numbers 6:26, the stranger, the seventy; DA the open series. NOT COMMITTED
(since a985fbc; ONE message at <scratch>/commit_msg_ch9b.txt covers THE IMPORT CACHE, 7b and 8). NEXT on the ruling: the commit; then 8b, two runs.
'''
MEMLINE_OLD_START = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — '
MEMLINE_NEW = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — map World/step9/DEUTERONOMY_WALK.md; ch 1-9 COMPILED, 10 READ (1-8 PUSHED a985fbc; 9, the cache, 10 UNCOMMITTED); NEXT: commit, then 8b\n'
DESC_OLD = "COMMITTED THROUGH a985fbc (2026-09-19; PUSHED) — SITTING 7b DONE 2026-09-19 ("
DESC_NEW = f"COMMITTED THROUGH a985fbc (2026-09-19; PUSHED) — SITTING 8 DONE {DATE} (chapter 10 READ AND FROZEN as one unit, the 224th — the ark inserted into God's quoted word, the stations reversed and Aaron moved (the open row), three receipt forms, 6:13 said again with cleave; UNCOMMITTED) — SITTING 7b DONE 2026-09-19 ("
REC2_OLD_START = '## 2. WHERE IT STANDS'
REC2_NEW = f'''## 2. WHERE IT STANDS ({DATE}, after sitting 8; the state doc #197 addendum 6 the newest)
- NUMBERS CLOSED. DEUTERONOMY 1:1-9:29 COMPILED AND ON THE TAPE (1-7 at 29c189b, 8 at a985fbc — PUSHED; 9 at 7/7b); 10 READ (sitting 8).
- {C_UNITS} frozen units, standing 2227, hash 8b8fff1fa28953af. 64 runners, 69 daemons, 472 functions; 1135 kinds / 1032 effects.
- THE TAPE at RUN (1311, 96, 88, 0, 12, 1606, 40, 319, pairs, 127), markers 169, closes 127; the sweep 63/63; every gate GREEN; the
  register gate DECLARED {R_DECL} / DEBT 0 (10:5\'s receipt seat declared NONE — 8b\'s). The sixth form (7b) a stretch on the clock MATCH;
  the fifth form\'s SUPPLIED and the calf\'s day marker his decisions, open.
- Uncommitted since a985fbc: the cache, 7b and sitting 8; ONE message at <scratch>/commit_msg_ch9b.txt covers all three.
- NEXT ON HIS WORD: the commit; then 8b (chapter 10\'s compile, two runs: the fragments in the ark, the stations\' open row, 10:5\'s seat).
'''
TOPIC_SHEKELS = f' — 6:1-2 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 8, chapter 10\'s reading: the ark Moses made and the tablets put in it, 10:1-5 — the ark hidden and the fragments in it; Bava Batra 14a-b — the compile 8b\'s docket).'
TOPIC_SOTAH = f' — 7:6 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 8, chapter 10\'s reading: the tribe of Levi separated "to bless in His name", 10:8 — the priests\' blessing in the Name in the Temple; Numbers 6:23-27 the kin — the compile 8b\'s docket).'
TOPIC_BLESS = f' — 9:5 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 8, chapter 10\'s reading: "with all your heart and with all your soul" inside the demand of 10:12 — the Shema\'s tokens; Menachot 43b a hundred blessings from "what" — the compile 8b\'s docket).'
LINT = f'{ROOT}/logic/solo_tools/gloss_lint.py'
def lint(path):
    out = subprocess.run([sys.executable, LINT, path], capture_output=True, text=True).stdout
    m = re.search(r'gloss_lint: (\d+) flag', out); return int(m.group(1)) if m else -1
WALKP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; RECP = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
TOPICS = f'{ROOT}/logic/MISHNAH_TOPICS.md'
TOUCH = [f'{ROOT}/logic/findings/STAMP_LEDGER.md', f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', f'{ROOT}/World/RESUME.md', f'{ROOT}/THE_STEPS.md', f'{ROOT}/THE_BRIEFING.md', f'{ROOT}/World/step9/COMPILE_DEBT.md', f'{ROOT}/RESEARCH_LOG.md', f'{ROOT}/logic/MIDDOT.md', RECP, f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md', TOPICS]
# ---- THE ANCHORS, ASSERTED PRESENT ONCE BEFORE ANY WRITE ----
A_RESUME = '# ⚠ THE DEUTERONOMY WALK sitting 7b (2026-09-19; step9/DEUTERONOMY_WALK.md "Sitting 7b"'
A_SCORE = '## SCOREBOARD (as of 2026-09-19, latest)\n'; A_SCORE_NEW = f'## SCOREBOARD (as of {DATE}, latest)\n'
A_BULLET = '- **CHAPTER 9 COMPILED — THE RETELLING OF A STRETCH'
A_ENTRY = '### 2026-09-19 — The two minutes of loading became half a minute, with a proof that nothing changed'
A_MIDDOT = '\n## Exodus block campaign — owner\'s word "Do 3")\n'
A_REC5 = 'the newest instances: the map\'s "Sitting 7" and "Sitting 7b"'
A_REC6 = '- Deuteronomy\'s sittings: the map; the addenda §31-48 (§39 the whole-row rule). The cost cuts: §35, §45, §47.'
T_SHEK = '**15. Mishnah, Shekels**'; T_SOTAH = '**28. Mishnah, Suspected Wife**'; T_BLESS = '**1. Mishnah, Blessings**'
ANCH = [(f'{ROOT}/World/RESUME.md', A_RESUME), (f'{ROOT}/THE_STEPS.md', '\n## Step 6 — Publish\n'), (f'{ROOT}/THE_BRIEFING.md', A_SCORE), (f'{ROOT}/THE_BRIEFING.md', A_BULLET), (f'{ROOT}/THE_BRIEFING.md', A_ENTRY), (f'{ROOT}/logic/MIDDOT.md', A_MIDDOT), (RECP, REC2_OLD_START), (RECP, '\n## 3. THE STANDING LAWS'), (RECP, A_REC5), (RECP, A_REC6), (f'{MEM}/deuteronomy-walk.md', DESC_OLD), (f'{MEM}/MEMORY.md', MEMLINE_OLD_START)]
for p, a in ANCH: assert rd(p).count(a) == 1, (p, a[:40], rd(p).count(a))
tl = rd(TOPICS).split('\n'); assert all(sum(l.startswith(t) for l in tl) == 1 for t in (T_SHEK, T_SOTAH, T_BLESS)) and f'ROUTED {DATE}' not in rd(TOPICS)
assert '## Sitting 8 — CHAPTER 10 — AS BUILT' not in rd(WALKP) and '## Sitting 8 — CHAPTER 10, Deuteronomy 10:1-22' in rd(WALKP) and '#197 ADDENDUM 6' not in rd(TOUCH[1]) and '#197 ADDENDUM 5' in rd(TOUCH[1]) and '## 49. ADDENDUM' not in rd(TOUCH[9]) and '## 48. ADDENDUM' in rd(TOUCH[9]) and 'SITTING 8 DONE' not in rd(f'{MEM}/deuteronomy-walk.md') and 'SITTING 8 — CHAPTER 10' not in rd(TOUCH[5]) and STAMP not in rd(TOUCH[0])
s = rd(RECP); i = s.index(REC2_OLD_START); j = s.index('\n## 3. THE STANDING LAWS'); REC_NEW = s[:i] + REC2_NEW + s[j:]
REC_NEW = REC_NEW.replace(A_REC5, 'the newest instances: the map\'s "Sitting 8" and "Sitting 7b"').replace(A_REC6, '- Deuteronomy\'s sittings: the map; the addenda §31-49 (§39 the whole-row rule). The cost cuts: §35, §45, §47.')
for a, b in [("the gates (gates_chain.sh runs them all; GATES_CHAIN.md the design; sweep_stamp.json the sweep's stamp)", "the gates (gates_chain.sh; GATES_CHAIN.md; sweep_stamp.json)"), (" — a reader takes the SNAPSHOT\n  (register_census.running_world). The peer thread is never a ruling.", " — a reader takes the\n  snapshot. The peer thread is never a ruling.")]:
    assert REC_NEW.count(a) == 1, a[:50]; REC_NEW = REC_NEW.replace(a, b)   # the page trimmed under its cap (the words dropped live in the files it points to)
assert len(REC_NEW.encode()) <= 10240, len(REC_NEW.encode())
m = rd(f'{MEM}/MEMORY.md'); i = m.index(MEMLINE_OLD_START); j = m.index('\n', i) + 1; MEM_NEW = m[:i] + MEMLINE_NEW + m[j:]
assert len(MEM_NEW.encode()) < 17000, len(MEM_NEW.encode())
# the commit message's paragraph (the scratch file the owner's word commits — the cache's, 7b's and now this sitting's)
CM = f'{SP}/commit_msg_ch9b.txt'; cm = rd(CM); assert 'SITTING 8' not in cm and '\nCo-Authored-By:' in cm
head, rest = cm.split('\n', 1)
head2 = head.rstrip('.') + f' AND, THE NEXT DAY, CHAPTER 10 READ AND FROZEN (SITTING 8, ONE RUN, EVERY ROW WHOLE) — THE SECOND TABLETS AND THE ARK: GOD\'S WORD QUOTED WITH THE ARK INSERTED, THE STATIONS REVERSED AND AARON MOVED, THREE RECEIPT FORMS IN ONE CHAPTER, THE SHEMA\'S LAW SAID AGAIN WITH A FOURTH CLAUSE.'
CM_PARA = f'''
ALSO IN THIS COMMIT: SITTING 8 — CHAPTER 10 READ AND FROZEN ({DATE}, on the owner\'s "Go" after the reread that followed 7b\'s compaction; World/step9/DEUTERONOMY_WALK.md "Sitting 8" and "Sitting 8 — AS BUILT"; the state doc\'s #197 addendum 6; the addenda §49): Deuteronomy 10:1-22 with Onkelos whole (the export\'s 22 rows the DB\'s 22 — the identity, asserted) and the Sifrei on Deuteronomy SILENT ON THE CHAPTER (36 on 6:9, 37 on 11:10), its whole voice three rows from elsewhere found by the union of both files\' citations and read whole (32:1 act from love — 10:20 quoted as the fearer\'s seat; 301:4 with few — the seventy quoted plene; 311:5 a hundred and forty nations against seventy souls — E10, quoted defective), two of them read before and REREAD WHOLE; the kin credited by name from the Exodus, Numbers and Leviticus ledgers; frozen as ONE unit deu_10_second_tablets (the 224th), standing 2227 = 2221 + 6 as predicted, hash 8b8fff1fa28953af unmoved; the ledger logic/oral_triage/deu_10_ekev_{LDATE}.md ({L_ALL} sources — Onkelos 22: MATERIAL {L_OM} / CONTEXT {L_OC}; the outside rows 3: MATERIAL {L_XM} / CONTEXT {L_XC}; coverage computed, lint 0, no cut missed); six claims DV10-01..06 verified 6/0, the labels census green, seated as six WITNESS_READ operators at 10:1, 5, 6, 10, 12, 17 with step E; the ritual {N_PASS} PASS; the display layer +{OV_REF10} by reference and +38 by gloss. THE FINDS: THE ARK INSERTED INTO GOD\'S QUOTED WORD — 10:1-2 against Exodus 34:1 six tokens then eleven of fourteen, with "come up to Me on the mountain" (Exodus 24:12\'s call, the two seats) and "make for yourself an ark of wood" between the halves and "and you shall put them in the ark" at the end (two tokens Exodus 34 never gives); the ark of acacia made BEFORE the ascent (10:3); "as the LORD commanded me" (10:5 — the receipt inside the narrative, 4:5 the kin, the register gate\'s seat declared NONE) and Solomon\'s 1 Kings 8:9 reading the ark\'s contents from this telling; THE STATIONS REVERSED AND AARON MOVED — Numbers 33:30-34 Moseroth then Bene-jaakan and Aaron\'s death at Mount Hor seven stations on (dated), 10:6 Beeroth-bene-jaakan then Moserah where "Aaron died and was buried there" (one token shared; "and he was buried there" the Torah\'s one seat) — the compile\'s OPEN row; "ministered as priest" the wayyiqtol at 10:6 and Numbers 3:4 alone; "separated" the hiphil perfect at 10:8 and Numbers 16:9 alone; THE BOOK\'S ARK "OF THE COVENANT" (four seats, never in Exodus) AGAINST EXODUS\'S "OF THE TESTIMONY" (seven in two spellings, never in the book); THREE RECEIPT FORMS in one chapter (10:5, 10:9 "as the LORD your God spoke to him" by "spoke", 10:11 "which I swore" repeated to Joshua in seven shared tokens); "at that time" twice; THE THIRD FORTY (10:10, the phrase\'s fifth seat in the book); THE DEMAND IN FIVE INFINITIVES (10:12-13) with the Shema\'s seven tokens and Micah 6:8\'s five; the heaven of heavens six in the Bible, with the vav at Solomon\'s dedication as here; "circumcise the foreskin of your heart" the one seat and "stiffen your neck no more" the chapter\'s one prohibition; "God of gods and Lord of lords" Psalm 136:2-3, "who lifts no face" against Numbers 6:26, the judge\'s bribe law made the Judge\'s nature; "AND YOU SHALL LOVE" FIVE IN THE TORAH and "for you were strangers" at all four seats; 10:20 AGAINST 6:13 SEVEN OF EIGHT with "and to Him you shall cleave" added; "He is your praise" one seat; the seventy told in new words; the parser\'s plural "first" no ordinal; NO MEMRA in the chapter; Moses unnamed from chapter 6 to 11; Onkelos\'s gifts for the inheritance, the ways right before Him, the foolishness of the heart, God of judges and Lord of kings, the convert and the dwellers, "draw near to His fear", "establish" for swear; THE SHELF QUOTES ONE VERSE TWO WAYS (301:4 plene, 311:5 defective). THE INK ASSEMBLED, NOT RETYPED: the generic helpers copied from chapter 9\'s ink by content markers (derive_ch10_ink.py); eight asserts fell on the first pass, none a fact (four a sum of searches read as one). EVERY GATE GREEN IN ONE CHAIN (ch10_gates.sh): the seat, verify_text ({VT_STEPS} steps), the ritual {N_PASS} PASS, CORPUS TRUTH GREEN before and after the bake ({C_UNITS} units, {C_FACTS} facts, {C_DEM} demands), build_world ALL GREEN, the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer), the register gate --strict GREEN (DECLARED {R_DECL}, DEBT 0, FAILS 0), large_letter_probes {LL[-3:]}, the home-path gate GREEN; verify_claims 6/0 and the labels census GREEN beside the chain. THE LESSONS (thirteen, in the map\'s AS BUILT): the retelling\'s additions are the compile\'s questions; the helpers copied by content markers; a sum of searches is not one search; the ledgers\' book names differ by age; the Genesis ledgers have no row line; a middah code is checked BEFORE it is typed (relearned — E10 typed on a precedent, two rows relabeled); the census wants a label to end in its note; the piece cap is seven; a nested heredoc is written by hand; the verifier takes the path; the shelf quotes one verse two ways; the parser reads the plural "first" as no ordinal; the reading sitting held in one run. Also in this commit: COMPILE_DEBT\'s sitting-8 box (a)-(n) owed to the compile 8b (the fragments in the ark, the receipt seats, the stations\' open row, the Levites\' "at that time", the third forty\'s end, the laws restated by CALL, the demand, the attributes, the stranger, the heart and the neck, the seventy, the parser\'s DATA rows, the series, the docket), MIDDOT\'s chapter-10 block, MISHNAH_TOPICS\' row notes (Shekels 6:1-2, Suspected Wife 7:6, Blessings 9:5 routed to 8b), RESEARCH_LOG\'s entry, THE_STEPS, THE_BRIEFING (the scoreboard and an entry), World/RESUME.md, the state doc\'s #197 addendum 6, the recovery page rewritten, the addenda §49, the stamp row, the display overrides, the forms in World/step9/forms_deuteronomy_walk/ (copy_ch10_forms.py). NEXT on the owner\'s word: THE COMPILE OF CHAPTER 10 (8b) in two runs — or the Decalogue-schema sitting first.
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
replace_once(TOUCH[4], A_SCORE, A_SCORE_NEW)
insert_before(TOUCH[4], A_BULLET, BRIEF)
insert_before(TOUCH[4], A_ENTRY, BRIEF_ENTRY)
append(TOUCH[5], DEBT)
append(TOUCH[6], RESEARCH)
insert_before(TOUCH[7], A_MIDDOT, MIDDOT)
row_note(TOPICS, T_SHEK, TOPIC_SHEKELS)
row_note(TOPICS, T_SOTAH, TOPIC_SOTAH)
row_note(TOPICS, T_BLESS, TOPIC_BLESS)
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
