#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 6 — CHAPTER 8 (2026-09-18; the owner: "Go" after 5b's commit 29c189b and THE TWO-RUN RULE, then "Reread" after the one
# compaction inside the run — the first READING sitting under THE TWO-RUN RULE, ONE run, every row whole under THE WHOLE-ROW RULE): THE RECORDS at the
# close, from the sheet World/step9/RECORD_FORMS.md in ONE call — the map's "Sitting 6 — CHAPTER 8 — AS BUILT", COMPILE_DEBT's box (owed to the compile
# 6b), MIDDOT's block (the Sifrei's rows that argue by a rule), MISHNAH_TOPICS' row notes (Blessings 6-7 and First Fruits 1 ROUTED to 6b), RESEARCH_LOG's
# entry, THE_STEPS' paragraph, THE_BRIEFING's bullet and entry, RESUME's note, the state doc's #196 addendum 1, the recovery page (rewritten whole, under
# 10 KB), the recovery addenda's section 43, the stamp row, the memory file and the index line (under 17,000 bytes). Every number parsed from a print
# named beside it (--check prints them and writes nothing); every insert on a unique anchor asserted present once; the lints before and after. Sitting 5's
# form (write_ch7_records.py) on the sheet.
import os, re, subprocess, sys, yaml, json
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/' + os.path.abspath(ROOT).replace('/', '-') + '/memory')
DATE = '2026-09-18'; LDATE = '2026-09-18'
UID = 'deu_08_manna_humility'
CHECK = '--check' in sys.argv
def rd(p): return open(p, encoding='utf-8').read()
# ---- THE NUMBERS, PARSED FROM THE PRINTS ----
truth = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py')
assert 'assert len(W["units"]) == 222' in truth and 'assert len(W["standing"]) == 2215' in truth and "8b8fff1fa28953af" in truth
CT = rd(f'{SP}/ch8_truth.out'); CB = rd(f'{SP}/ch8_bake.out'); C1 = rd(f'{SP}/ch8_fold_check1.out')
assert 'CORPUS TRUTH GREEN' in CT and 'CORPUS TRUTH GREEN' in C1 and 'wrote corpus_world.sqlite' in CB
rit = rd(f'{SP}/ch8_ritual_{UID}.out'); N_PASS = len(re.findall(r'^PASS', rit, re.M))
assert 'RITUAL COMPLETE' in rit and N_PASS == 13 and not re.search(r'^FAIL', rit, re.M), N_PASS
vt = rd(f'{SP}/ch8_vt_{UID}.out'); assert 'TEXT LAYER GREEN: 20 steps, 7 scenarios' in vt
assert '  status: frozen' in rd(f'{ROOT}/logic/units/{UID}.yaml') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json') and 'ALL_DONE' in rd(f'{SP}/ch8_chain.log')
JG = rd(f'{SP}/ch8_journal.out'); RG = rd(f'{SP}/ch8_register.out'); BW = rd(f'{SP}/ch8_build.out'); GS = rd(f'{SP}/ch8_gates_SUMMARY.txt')
assert 'GATE GREEN' in JG and 'ALL GREEN' in BW and 'THE REGISTER GATE: GREEN' in RG and 'ALL GREEN' in GS, (JG[-200:], BW[-200:], GS[-200:])
mj = re.search(r'(\d+) kinds, ([\d,]+) rows', JG); J_KINDS, J_ROWS = mj.group(1), mj.group(2)
mr = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', RG); R_DECL, R_DEBT, R_FAIL = mr.groups()
assert R_DEBT == '0' and R_FAIL == '0', mr.groups()
mc = re.search(r'(\d+) units, (\d+) facts, (\d+) demands \((\d+) open\)', CT); C_UNITS, C_FACTS, C_DEM, C_OPEN = mc.groups()
assert C_UNITS == '222', C_UNITS
HG = rd(f'{SP}/ch8_home.out'); assert 'GREEN' in HG, HG[-200:]
LED = rd(f'{ROOT}/logic/oral_triage/deu_08_ekev_{LDATE}.md')
ml = re.search(r'\*\*read: (\d+) of \1 — COMPLETE\*\* \((\d+) Onkelos verses and (\d+) Sifrei rows.*?MATERIAL (\d+) Onkelos, CONTEXT (\d+) Onkelos, MATERIAL (\d+) Sifrei outside, CONTEXT (\d+) Sifrei outside', LED, re.S)
L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_XM, L_XC = ml.groups()
assert L_ALL == '36' and L_ONK == '20' and L_SIF == '16' and LED.count('⟨MISS⟩') == 0
L_BYTES = len(LED.encode())
d_ov = yaml.safe_load(rd(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'))
OV_REF8 = len([k for k in d_ov['by_ref'] if k.startswith('Deut.8.')]); OV_REF, OV_GL = len(d_ov['by_ref']), len(d_ov['by_gloss'])
assert OV_REF8 == 20 and OV_REF == 552 and OV_GL == 466, (OV_REF8, OV_REF, OV_GL)
N_CLAIMS = len(json.load(open(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json', encoding='utf-8'))); assert N_CLAIMS == 6
VC = rd(f'{SP}/ch8_vc.out'); assert 'SUMMARY: 6 verified, 0 failed, 0 uncheckable, 0 no-check' in VC
LAB = rd(f'{SP}/ch8_labels.out'); mlab = re.search(r'CLAIM LABELS CENSUS — (\d+) claims in (\d+) manifests; labeled \1; DEBT 0', LAB); LN = f'{int(mlab.group(1)):,} claims in {mlab.group(2)} manifests'; assert 'GATE PASSED' in LAB and re.search(r'deu\s+52 claims\s+labeled\s+52\s+debt\s+0', LAB)   # the head line is the total; the 'num' row is the NUMBERS book's (the ch7 form's slip)
assert rd(f'{SP}/ch8_ink_run3.out').strip().endswith('0 failing statements') and rd(f'{SP}/ch8_ink_run2.out').strip().endswith('0 failing statements')
N_INK = len(re.findall(r'^assert ', rd(f'{SP}/ch8_ink.py'), re.M))
LL = rd(f'{SP}/ch8_large_letter.out').strip().split('\n')[-1]; assert LL.endswith('6/6'), LL
JR7 = re.search(r'12 kinds, (\d+) rows', rd(f'{ROOT}/World/step9/forms_deuteronomy_walk/gates_ch7b_journal.out')).group(1); DJ = int(J_ROWS.replace(',', '')) - int(JR7)
print('PARSED:', dict(ritual_pass=N_PASS, journal=(J_KINDS, J_ROWS, DJ), register=(R_DECL, R_DEBT, R_FAIL), corpus=(C_UNITS, C_FACTS, C_DEM, C_OPEN), ledger=(L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_XM, L_XC, L_BYTES), overrides=(OV_REF8, OV_REF, OV_GL), claims=N_CLAIMS, labels=LN, ink_asserts=N_INK, large_letters=LL))

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

STAMP = (f'| {DATE} | {UID} | DELEGATED | FULL RULE | Deuteronomy 8:1-20 derivation {LDATE} (THE DEUTERONOMY WALK sitting 6 — CHAPTER 8; the owner: "Go" after chapter 7\'s commit 29c189b and THE TWO-RUN RULE, then "Reread" after the one compaction inside the run — the first reading sitting under THE TWO-RUN RULE, ONE run, every row whole under THE WHOLE-ROW RULE; the book\'s sixth reading — chapter 8 as one draft, no portion edge inside it, the 222nd frozen unit): declared reading COMPLETE (one ledger logic/oral_triage/deu_08_ekev_{LDATE}.md, {L_ALL} sources — Onkelos 8:1-20 whole and fresh (the export\'s twenty rows the DB\'s twenty, asserted), THE SIFREI ON DEUTERONOMY SILENT ON THE CHAPTER (no piska head between 36 on 6:9 and 37 on 11:10 — the heads computed) and its SIXTEEN rows outside any piska citing chapter 8, found by the union of both files\' citations and read whole — the Ekev piskaot on 11:10-12 quoting the chapter\'s praise of the Land back at it (19:2, 37:5, 39:4, 39:6, 39:8, 40:10) and eight other piskaot quoting its sentences as proof-texts (32:10, 32:12, 32:15 the discipline; 43:7 and 318:1 satiety; 48:8 forgetting; 48:10 not by bread alone; 53:1 the end; 297:4 the first fruits; 313:15 the wilderness), five read before and REREAD WHOLE (sitting 1\'s 19:2; chapter 6\'s 32:10, 32:12, 32:15; a Genesis sitting\'s 318:1), none excluded, no interpolation; the kin\'s spine (Numbers 11:4-9, 14:33-34, 20:1-13, 21:4-9; the Mekhilta on Exodus 16-17) CREDITED BY NAME from the Numbers walk\'s ledgers with the counts computed; coverage computed by script, missing 0 extra 0; the ink facts computed from the Tanakh DB, the snapshot store and the shelf\'s bytes — {N_INK} asserts, four fell on the first typed pass (forms, not facts) and were retyped from the print, none after, 0 failing after the display patch; every quotation cut by consonants, no miss; gloss_lint 0), claims DV08-01..06 verified {N_CLAIMS}/{N_CLAIMS} (every check the word\'s longest store-piece whole — never 8:2\'s "His commandments", where the store carries the written and the read form), claim_labels_census --strict GREEN, seated as six WITNESS_READ operators at the claims\' first verses (8:1, 2, 7, 11, 15, 19), verify_text GREEN (20 steps, 7 scenarios), the ritual {N_PASS} PASS, CORPUS TRUTH GREEN ({C_UNITS} units, standing 2215 = 2209 + 6 as predicted, hash 8b8fff1fa28953af UNMOVED), build_world ALL GREEN, the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows), the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — no seat in the chapter), large_letter_probes {LL}. THE PARSER: two number verses in twenty, NO GAP — 8:2 and 8:4 "these forty years" [40]; "and you shall be satisfied" (8:10, 8:12) starred as the seven-stem homograph; "swore" no number. THE FINDS: the spine silent, the shelf not — sixteen rows from elsewhere its whole voice; THE SEVEN SPECIES at one seat (8:8 alone holds all seven in the Bible) and HONEY WITHOUT MILK; "EAT, BE SATISFIED, BLESS" the Torah\'s one command to bless; the book\'s one interrogative he on a verb (8:2) with the manna\'s own test-clause; THE KING\'S LAW\'S TOKENS at 8:13 and 8:14 (17:17, 17:20); "not by bread alone" the one seat; THE WRITTEN/READ PAIR at 8:2 (the store\'s extra token; 5:10\'s and 7:9\'s kin); the forty years as a STATE (the garment, the foot — no line on the tape); the infinitive absolute of forgetting at 8:19; "because" the heel at 8:20, the portion\'s second seat; the article + participle chain (8:14-18) answered by the boast; the two files dividing a piska differently (39:6-8); the range citations the regex cannot read; Onkelos\'s Word supplied twice, the fear supplied three times, the shoes, the counsel. Stamp delegated under the AUTO-SEAT ruling; the owner may overrule. |\n')

WALK = f'''

## Sitting 6 — CHAPTER 8 — AS BUILT ({DATE}; the design above stands as written — the one run ran as designed; every departure from the design named here)

THE RESULT: Deuteronomy 8:1-20 READ AND FROZEN as one unit — {UID}, the {C_UNITS}nd frozen unit (no portion edge inside it — Ekev runs 7:12-11:25; the
chapter the unit, per the ruling); the ledger logic/oral_triage/deu_08_ekev_{LDATE}.md ({L_ALL} sources: Onkelos {L_ONK} — MATERIAL {L_OM} / CONTEXT {L_OC}; the Sifrei's spine
0 rows — SILENT on the chapter; the outside rows {L_SIF} — MATERIAL {L_XM} / CONTEXT {L_XC}, five of them reread whole; the kin's spine credited by name in its own section — the
Numbers 11, 14, 20 and 21 ledgers' 6 / 2 / 13 / 6 rows and the Mekhilta's 8 over the ledgers, computed; {L_BYTES:,} bytes; lint 0); the manifest {UID}_claims.json
({N_CLAIMS} claims DV08-01..06, verify_claims {N_CLAIMS}/0, the labels census GREEN — {LN} labeled, debt 0); six WITNESS_READ seats at 8:1, 2, 7, 11, 15, 19, step E, seven anchor
scenarios; the ritual {N_PASS} PASS; the fold predicted and matched before and after the bake ({C_UNITS} units, standing 2215, hash 8b8fff1fa28953af; {C_FACTS} facts, {C_DEM}
demands, {C_OPEN} open); the display layer +{OV_REF8} by reference and +32 by gloss (by_ref {OV_REF}, by_gloss {OV_GL} after); the stamp row delegated (FULL RULE). No engine file
changed — the tape as at 5b's close (RUN (1307, 96, 88, 0, 12, 1602, 38, 319, the four pairs, 127), markers 167, closes 127); the sweep as at 5b.

THE DEPARTURES FROM THE DESIGN: none in substance. THE ONE RUN held — the reading sitting's first under THE TWO-RUN RULE: the rereads, the measurements, the
ink ({N_INK} asserts, four failing on the first pass and 0 on the second and third), the design, the rows whole, the ledger, the display patch, the manifest, the
seat, the chain, the fold, the gates, the records and the forms in one run of some 900k tokens with ONE compaction inside it (the state doc's #196 at 743k,
on "Get ready to compact"; the owner said "Reread" and the run resumed at the step the point named — the ledger writer — with no re-derivation). Three
small departures: (1) a middah code caught wrong before it was typed — the design's I2 at 297:4 was drafted as an analogy on "the land"; the row's own words
run the analogy on "bring" (the community's first fruits and the individual's), retyped before the manifest was written (the rule A MIDDAH CODE IS CHECKED
IN MIDDOT.md BEFORE IT IS TYPED, applied to the row's words too); (2) the gates ran as ONE chain script for the first time on a reading (ch8_gates.sh — the
manifest, the seat chain, the fold, build_world, the journal gate, the register gate, the large letters and the home gate, in the background, the summary read
once), verify_claims and the labels census run beside it; (3) the shell's grep function in the session snapshot broke mid-run (a wrapper calling a missing
binary) — /usr/bin/grep used by path; nothing of the repo touched by it.

THE GATES, COMPUTED FROM THEIR PRINTS: the ritual {N_PASS} PASS (RITUAL COMPLETE, {C_UNITS} frozen units); CORPUS TRUTH GREEN twice ({C_UNITS} units, {C_FACTS} facts, {C_DEM}
demands ({C_OPEN} open), hash 8b8fff1fa28953af — the tripwire's literals set to the prediction before the bake, matched); build_world ALL GREEN; the journal gate
GREEN ({J_KINDS} kinds, {J_ROWS} rows — {JR7} at sitting 5b, +{DJ} on the fold layer with the tape unmoved); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT},
FAILS {R_FAIL} — no seat in chapter 8); the home-path gate GREEN; the labels census GREEN ({LN} claims labeled, debt 0); large_letter_probes {LL}; the lints at their
baselines.

⚠ THE LESSONS (the run's, gathered — the numbered list the sheet asks for): (1) THE SPINE'S SILENCE IS NOT THE SHELF'S — a chapter without a section is a chapter
the shelf cites: sixteen rows from the Ekev piskaot on 11:10-12 and eight other piskaot, found by the union of both files' citations; the ledger's outside
section is the spine's whole voice. (2) A RANGE CITATION IS INVISIBLE TO THE CITATION REGEX — "(דברים ח ה-ז)" ("Deuteronomy 8:5-7") at three rows; the union found
them through the English, the Hebrew's range asserted by string; a slip this way is a row missed, never a row invented. (3) THE TWO FILES DIVIDE A PISKA'S ROWS
DIFFERENTLY — the English's 39:6 runs through the Hebrew's 39:6-8; each file's own row carries the citation, both read whole, neither counted twice. (4) A
CONSONANTAL ASSERT NEVER TYPES A POINTING — the shelf's bytes stripped to consonants before the compare; the one form that fell typed a vowel letter for a
vowel mark. (5) THE FIRST TYPED PASS FELL FOUR WAYS ON FORMS — the print first, then the assert. (6) THE CREDIT GUARD MADE FULL — five rows read before were
reread whole; the whole-row rule leaves the quick look nothing to save. (7) A READING SITTING FITS ONE RUN — the two-run rule's first reading: one compaction
inside the run, the point naming every remaining step with its script names and counts, the run resumed on "Reread" at the step named. (8) A MIDDAH CODE IS
CHECKED AGAINST THE ROW'S OWN WORDS — the code was right (I2) and the analogy's word wrong ("the land" for "bring"); the row head read again before the
manifest was typed. (9) THE KIN CREDITED BY COUNT FROM FOUR LEDGERS — the Numbers walk's ledgers hold the chapter's kin whole through Onkelos; Exodus 16-17
were read through the Mekhilta only (the shelf's default: Exodus = the Mekhilta), so the manna's and the rock's Onkelos rows exist nowhere — a note, not a
debt. (10) A READING'S GATES ARE ONE CHAIN TOO — the manifest, the seat, the ritual, the fold and the five gates in one background script with one summary;
the claims' verifier and the labels census beside it. (11) THE FOLD LAYER GROWS WITH A FREEZE WHILE THE TAPE STANDS — the journal's index +{DJ} rows on the new
unit, the header re-pinned to the unmoved hash (5's lesson held again).

THE FORMS: World/step9/forms_deuteronomy_walk/ — the one run's scripts (derive_ch8_dump0.py, ch8_dump0.py, ch8_measure1.py, ch8_ink.py, the three row files,
write_ch8_ledger.py, ch8_patch_overrides.py, write_ch8_manifest.py, seat_ch8.py, ch8_chain.sh, ch8_fold.sh, ch8_gates.sh, write_ch8_design.py,
write_ch8_records.py, copy_ch8_forms.py) and the prints (the dump, the measurement, the Onkelos dump, the outside rows, the store's glosses, the ink runs,
the manifest, the chain log, the ritual, verify_text, the claims' verifier, the labels census, the fold's checks, the gates and their summary).

NEXT on the ruling: THE COMPILE OF CHAPTER 8 (sitting 6b) in TWO RUNS — RUN A: the rereads (THE_STEPS Step 5 + the compiler block; this section; the 6b box in
COMPILE_DEBT.md), the measurements (the tape's state at Deut 7:26; the runners' cells the chapter calls — exodus_story's manna and rock lines, chukat's
serpents and Meribah, the Exodus 23 runner, obey_horeb's 4:26 cell, 7:12's heel cell, 3b's second-word cell; the blessing after the meal and the seven
species with no cell anywhere), THE DESIGN in this file before any code, the docket by the union rule (Berakhot 20b-21a, 35a-b, 41a-44a, 48b-49b; Mishnah
Berakhot 6-7; Bikkurim 1; Yoma 74b-76a; Sotah 4b-5a; Makkot 13b; Eruvin 96a; Berakhot 5a — the scan will name the rest), every row whole; RUN B: the types,
the runner (the blessing after the meal; the seven species; the manna and the humbling by the readback on the tape's lines; the forty years as a STATE — the
readback's supplied grade on a state, the design decision; the discipline; take heed lest; the heart lifted up; the exodus formula; the serpents and the rock
by CALL; the covenant established; the testimony), the tape to 10/10, the gates chain, the records, the forms, the commit message. Or THE DECALOGUE-SCHEMA
SITTING first, on the owner's word — THE INSTALL HYPOTHESIS stays on the table beside it. Then chapter 9, and on in order.
'''

DEBT = f'''
## DEUTERONOMY SITTING 6 — CHAPTER 8, Deuteronomy 8:1-20 READ AND FROZEN ({DATE}; DEUTERONOMY_WALK.md "Sitting 6" and "Sitting 6 — AS BUILT"; the ledger
## deu_08_ekev_{LDATE}.md, {L_ALL} sources; one unit {UID} FROZEN, the {C_UNITS}nd) — OWED TO THE COMPILE (sitting 6b): (a) THE BLESSING AFTER THE MEAL
## (8:10 "eat, be satisfied, bless" — the Torah's one command to bless: Berakhot 48b the grace's blessings from the verse, 20b-21a the Torah obligation, 49b and
## Mishnah Berakhot 7:2 the measure of "satisfied", 35a the blessing before as an inference; Mishnah Berakhot 6-7 whole by topic — NO CELL ANYWHERE in the
## machine, compiled at 6b for the first time); (b) THE SEVEN SPECIES (8:8 — Berakhot 41a-b the order of blessings by the verse's order and its two "land"s, 44a
## the after-blessing; Mishnah Berakhot 6:4; Bikkurim 1:3, 1:10 the first fruits (the Sifrei 297:4 by I2); Menachot 84b CREDITED at the offerings-calendar exam);
## (c) THE MANNA AND THE HUMBLING (8:2-3, 8:16 — Yoma 74b-76a "afflicted you and let you hunger", the manna's forms; the readback rows against the tape's manna
## lines by kind — Exodus 16, exodus_story by CALL); (d) THE FORTY YEARS AS A STATE (8:2, 8:4 — the garment not wearing out, the foot not swelling: a state over
## forty years with NO EARLIER LINE on the tape — the readback's SUPPLIED grade on a state, not an act: THE DESIGN DECISION of 6b); (e) THE DISCIPLINE (8:5 —
## Berakhot 5a's afflictions of love; the Sifrei 32:10-15 CREDITED here); (f) "TAKE HEED LEST" (8:11 — Makkot 13b / Eruvin 96a: "take heed, lest, do not" a
## negative command, the rule's exhibit; a cell forgetting_barred?); (g) THE HEART LIFTED UP (8:14 — Sotah 4b-5a arrogance as idolatry; 17:20 the king's law by
## CALL when chapter 17 compiles); (h) THE EXODUS FORMULA (8:14 — brought_out 12:51 by kind, the readback); (i) THE SERPENTS AND THE ROCK (8:15 — Numbers 21:6-9
## and 20:8-11, Exodus 17:6 by the tape's lines and by CALL into chukat and exodus_story); (j) "MY POWER AND THE MIGHT OF MY HAND" (8:17 — a DATA row; the Sifrei
## 48:10's "not by bread alone" reading); (k) THE COVENANT ESTABLISHED (8:18 — the oath's lines by kind, as 7:8); (l) THE TESTIMONY (8:19-20 — 4:26's line by
## kind, obey_horeb's cell by CALL; the perishing "like the nations" a DATA row; the heel's second seat 7:12's cell by CALL; "other gods" the second word's cell
## by CALL); (m) THE KING'S LAW'S TOKENS (8:13 "silver and gold shall multiply for you" against 17:17 "he shall not multiply" — the pair's CALL when chapter 17
## compiles; a note now); (n) THE DOCKET by the union rule (Berakhot 20b-21a, 35a-b, 41a-44a, 48b-49b; Mishnah Berakhot 6-7; Bikkurim 1; Yoma 74b-76a; Sotah
## 4b-5a; Makkot 13b; Eruvin 96a; Berakhot 5a — the scan will name the rest), every row whole. NOTHING ELSE IN CHAPTER 8 IS OWED TO A LATER SITTING OF ITS OWN.
'''

MIDDOT = f'''- **THE SIFREI ON DEUTERONOMY'S OWN CASE LAW ON CHAPTER 8 (Deuteronomy 8:1-20; THE DEUTERONOMY WALK sitting 6, {DATE};
  the ledger logic/oral_triage/deu_08_ekev_{LDATE}.md — THE SPINE SILENT ON THE CHAPTER, no piska head between 36 on 6:9 and 37 on
  11:10; its sixteen rows outside any piska read whole in both files, the rows that argue by a numbered rule below, each at its row):**
  · TWELVE LANDS FOR TWELVE TRIBES (39:4 on 11:11 from 8:7-10): the repeated "land" — "the land which you go in to possess", "a land of
    hills and valleys", "a land of brooks of water", "a land of wheat and barley …", "a land of olive oil and honey", "a land where you
    shall eat bread without poverty", "a land whose stones are iron" — each repetition given a tribe, twelve in all — E10 (the repeated
    expression signifies); THE INK: "a good land" twelve seats, 8:7-10 four "land" clauses in a row; the range citation 8:7-10 in the
    Hebrew's form, asserted by string.
  · WATER SAID TWICE (39:8 on 11:11 from 8:7): "from the rain of heaven it drinks WATER" — the second "water" read as irrigation water
    too, 8:7's "a land of brooks of water" the proof — E10; THE INK: "brooks of water" three seats (8:7; 10:7 Jotbathah's; Deuteronomy
    the book's two); the English's 39:6 runs through the Hebrew's 39:6-8, each file's own row read whole.
  · THE FIRST AND THE LAST (48:8 on 11:22 from 8:19): "if you SURELY keep" and "if you SURELY forget" — the doubled verb given a
    teaching: one who keeps first by first keeps the last, one who forgets first by first loses the last — E10 on the infinitive
    absolute; THE INK: 8:19's "surely forget" the lemma's one such form in the Bible.
  · THE FIRST FRUITS FROM THE SEVEN SPECIES (297:4 on 26:2 from 8:8): "BRING" said of the community's first fruits (Leviticus 23) and
    "BRING" said of the individual's (26:2) — the shared word runs the analogy: as the community's come from the seven species, so the
    individual's, 8:8 the list — I2 (the verbal analogy, "an equal decree"); Mishnah Bikkurim 1:3 the answer sheet, owed to 6b.
  · THE NAME FOR ITS SOUND (37:5 on 11:10 from 8:9): "the world" (Proverbs 8:26) is the Land of Israel because it is SPICED with
    everything — a homily on the sound of the word, no numbered rule; 8:9 "you shall not lack anything" the proof.
'''

RESEARCH = f'''
## {DATE} — DEUTERONOMY 8 READ (THE DEUTERONOMY WALK sitting 6 — CHAPTER 8, in one run under THE TWO-RUN RULE, every row whole): THE SPINE SILENT, THE SHELF NOT —
## SIXTEEN ROWS FROM ELSEWHERE; THE RANGE CITATIONS THE REGEX CANNOT READ; THE TWO FILES DIVIDE A PISKA DIFFERENTLY; THE SEVEN SPECIES AT ONE SEAT AND HONEY
## WITHOUT MILK; THE BOOK'S ONE INTERROGATIVE HE; THE KING'S LAW'S TOKENS AT 8:13; THE WRITTEN/READ PAIR AT 8:2; THE FORTY YEARS AS A STATE

THE SPINE SILENT, THE SHELF NOT. The Sifrei on Deuteronomy has no section on chapter 8 (nothing between piska 36 on 6:9 and 37 on 11:10 — chapter 7's
finding, the heads computed), but the shelf cites the chapter sixteen times from elsewhere: the Ekev piskaot on 11:10-12 quote the chapter's praise of the
Land back at it (19:2's tutor's parable on 8:7; 37:5 the Land spiced with everything on 8:9; 39:4 twelve lands for twelve tribes on 8:7-10; 39:6 and 39:8
the Land's drinking on 8:7; 40:10 the blessing in eating and satisfaction on 8:10; 297:4 the first fruits from the seven species on 8:8), and eight other
piskaot quote its sentences as proof-texts (32:10, 32:12, 32:15 the discipline of a son beside the good land; 43:7 and 318:1 rebellion out of satiety;
48:8 forgetting the first and losing the last; 48:10 "not by bread alone"; 53:1 "to do you good in your end"; 313:15 the great and terrible wilderness as
the four kingdoms). Found by the union of both files' citations — the Hebrew's book-named form fifteen on twelve rows, the English's "(Dt.8:n" twenty-six on
fifteen rows — every row read whole in both files, five of them read before at other sittings and reread whole here; none excluded, no interpolation. The
chapter's kin — the manna (Exodus 16), the rock at Horeb (17:1-7), the craving (Numbers 11:4-9), the forty years (14:33-34), Meribah (20:1-13), the serpents
(21:4-9) — were read at their own sittings and are credited by name, the counts computed from those ledgers; the Numbers kin whole through Onkelos, the
Exodus kin through the Mekhilta only (no Onkelos row of Exodus 16 or 17 exists in any ledger — the shelf's default gives Exodus the Mekhilta). {L_ALL} sources,
coverage computed; the twenty Onkelos rows whole.

THE RANGE CITATIONS THE REGEX CANNOT READ. The Hebrew export writes some citations as ranges — "(דברים ח ה-ז)" ("Deuteronomy 8:5-7") at 32:15, "8:7-10" at
39:4, "8:12-13" at 43:7 — and the citation regex reads a single verse; the union of both files found these rows through the English's citations, and the
Hebrew's range strings are asserted on the row's bytes. A slip this way is a row missed, never a row invented; the scan's blind spot is recorded for the
scanner (the range form to be read at a gate sitting).

THE TWO FILES DIVIDE A PISKA DIFFERENTLY. The English's 39:6 runs on through the Hebrew's 39:6, 39:7 and 39:8; the citation of 8:7 sits in the Hebrew's 39:8
and the English's 39:6. Both rows were read whole, each file's own row counted, neither counted twice — chapter 6's lesson (the two files compared row by
row) in its third form after the mis-cited book and the divergent row.

THE SEVEN SPECIES AT ONE SEAT AND HONEY WITHOUT MILK. 8:8 alone in the Bible holds all seven lemmas of the species for which the Land is praised — wheat,
barley, vine, fig, pomegranate, olive oil, honey (three or more together at five other seats: Numbers 20:5, Haggai 2:19, Joel 1:12, Habakkuk 3:17, Jeremiah
41:8); "milk" is absent from the chapter — the formula "flowing with milk and honey" nowhere in it. The shelf makes the verse the first fruits' list (the Sifrei
297:4, by the verbal analogy on "bring"; Mishnah Bikkurim 1:3) and the order of blessings (Berakhot 41a-b) — both owed to the compile. 8:8 is also the
chapter's one verse with no verb and neither person. Beside it 8:10 "eat, be satisfied, bless" — the Torah's ONE command to bless the LORD (the blessing
after the meal's seat; Berakhot 48b; no cell anywhere in the machine, compiled at 6b for the first time); "and you shall be satisfied" is the seven-stem
homograph the parser stars at 8:10 and 8:12, as at 6:11.

THE BOOK'S ONE INTERROGATIVE HE. 8:2 "whether you would keep His commandments or not" — the interrogative he on a verb, the book's one seat; the verse ends
with the manna's own test-clause "whether … or not", shared with Exodus 16:4 ("whether they will walk in My law or not") at the verse's end; the verse-ending
pair at seven seats over the Bible. The chapter's two number verses are 8:2 and 8:4 "these forty years" [40] — 2:7 the same phrase; the parser reads [40] at
every seat of the wilderness's forty years; no gap.

THE KING'S LAW'S TOKENS AT 8:13. "Silver and gold shall multiply for you" (8:13) and "silver and gold he shall not multiply" (17:17) share their tokens — the
blessing and the king's bar; 8:14 "and your heart be lifted up" against 17:20 "that his heart be not lifted up"; Hosea 13:6 puts the chapter's sequence
(satisfied, lifted, forgot) in the prophet's mouth. The shelf reads 8:12-14 as the rule that a people rebels only out of satiety (43:7; 318:1 — the Flood, the
Tower, Sodom, the calf, Jeshurun). 8:11 shares six tokens with 6:12 ("take heed to yourself lest you forget the LORD") — the Shema's warning said again; the
chapter's one imperative.

THE WRITTEN/READ PAIR AT 8:2. The snapshot store carries twenty-four tokens where the DB carries twenty-three: "His commandments" written without the yod
(the DB's one written-marked token in the chapter) AND read with it — the chapter's one mismatch, 5:10's and 7:9's kin (the token's five Bible seats: 5:10,
7:9, 8:2, 27:10, Numbers 15:31). Asserted as the exact difference; no claim's check uses the word (the check at 8:2 sits on "forty", before the store's extra
token).

THE FORTY YEARS AS A STATE. "Your garment did not wear out upon you, nor did your foot swell, these forty years" (8:4; 29:4 the plural garments; Nehemiah 9:21
the only other "did not swell") — a state over forty years with no line on the tape: the manna has lines (Exodus 16), the serpents and the rock have lines
(Numbers 21, 20; Exodus 17), the garment has none. The readback's grade for a state told only in the retelling is the compile's design decision (6b): a
SUPPLIED grade on a state, not an act — recorded here, not resolved.

ONKELOS ON THE CHAPTER. The Word supplied twice — 8:3 "not by bread alone is man sustained, but by everything that proceeds from the Word of the LORD" and
8:20 "accept the Word" for "hearken to the voice"; the fear supplied at the three forgettings (8:11, 8:14, 8:19 "lest you forget THE FEAR OF the LORD");
"your shoes did not go bare" for the foot that did not swell (8:4, 29:4); "teaches" for "disciplines" (8:5); "the mighty rock" for the flint (8:15);
"possessions" for wealth (8:17, 8:18, 32:15) and "He gives you COUNSEL to acquire possessions" for the power (8:18); "in exchange for" for "because" (8:20 —
7:12's); "the idols of the peoples" for other gods (8:19). THE STORE'S GLOSSES READ BACK (the display layer): 32 rows by gloss and {OV_REF8} by reference —
"the-whatness" THE MANNA, "and-mark" AND REMEMBER, "to-separation-him" ALONE, "going-forth" WHAT PROCEEDS FROM, "fail" WORE OUT, "perhaps-to-swell-up"
SWELLED, "in-indigence" IN POVERTY, "the-set" WHO GIVES, "and-mislay" AND FORGET, "burning" FIERY SERPENT, "from-cliff" FROM THE ROCK, "vigor-me" MY POWER,
"duplicate" TESTIFY, "wander-away" PERISH, "heel" BECAUSE (by reference at 8:20), "?" made "I" at 8:1 and 8:11; by_ref {OV_REF}, by_gloss {OV_GL} after.
'''

STEPS = f'''DEUTERONOMY — SITTING 6 — CHAPTER 8, Deuteronomy 8:1-20 ({DATE}, on Brian's "Go" after chapter 7's commit and the two-run rule, then "Reread" after the
one compaction; World/step9/DEUTERONOMY_WALK.md "Sitting 6" and "Sitting 6 — AS BUILT").
The chapter of the manna and the good land: remember the forty years, the humbling and the testing, "not by bread alone"; a land of brooks and of the seven
kinds of fruit; eat, be satisfied, bless; take heed lest, full and rich, you forget who brought you out; "my power and the might of my hand" answered by "He
gives you the power"; if you forget and serve other gods, you perish like the nations. The first reading sitting under the two-run rule, and it fit one run
with one stopping point inside it. The Sifrei has no section on this chapter either, but it quotes the chapter sixteen times from elsewhere — mostly from
its sections on the next chapter's praise of the Land, which quote this chapter's praise back at it — and every one of those rows was read whole, five of
them for the second time. What the reading found: one verse (8:8) is the only place in the whole Bible that names all seven kinds of fruit the Land is praised
for, and it names honey without milk; 8:10 is the Torah's one command to bless God, the seat of the grace after meals, which no cell of our machine yet
compiles; the chapter's "silver and gold shall multiply for you" uses the very words of the king's law "he shall not multiply silver and gold"; our text
store carries an extra token at 8:2 where a word is written one way and read another; and the garment that did not wear out for forty years is a state the
tape never wrote as an event — a question for the compile. The chapter is frozen as one unit, the 222nd, the world's standing facts up by six as predicted,
its hash unmoved, every gate green. Next: the commit on your word; then the compile of chapter 8 in two runs — the grace after meals, the seven kinds, the
manna, the forty years as a state, the discipline, the warnings, the testimony — or the ten-commandments schema first.

'''
BRIEF = f'''- **CHAPTER 8 READ AND FROZEN — THE MANNA AND THE GOOD LAND: THE SIFREI QUOTES THE CHAPTER SIXTEEN TIMES FROM ELSEWHERE, ONE VERSE HOLDS ALL SEVEN KINDS OF FRUIT, AND THE TORAH'S ONE COMMAND TO BLESS HAS NO CELL YET** ({DATE}, on your "Go" after chapter 7's commit and the two-run rule, then "Reread" — ONE run, every row whole; World/step9/DEUTERONOMY_WALK.md "Sitting 6"): Onkelos on all 20 verses and the Sifrei's sixteen rows from elsewhere (five reread whole) — {L_ALL} sources, coverage computed, the kin's spine credited by name from the Numbers walk; the seven kinds at one seat, honey without milk; "eat, be satisfied, bless" the one command to bless; the king's law's words at 8:13; the extra token in our store at 8:2; the forty years a state the tape never wrote; one unit frozen (the {C_UNITS}nd), {N_CLAIMS} claims verified, the ritual {N_PASS} PASS, standing facts 2215 (+6 as predicted), hash unmoved, every gate green. NEXT: the commit on your word; then the compile of chapter 8 in two runs, or the schema sitting first.
'''
BRIEF_ENTRY = f'''### {DATE} — CHAPTER 8 READ: THE MANNA, THE GOOD LAND, AND THE FIRST ONE-RUN READING

The chapter that tells the wilderness back to the people about to leave it: remember the forty years, the hunger and the manna, "not by bread alone"; the
garment that did not wear out; a father's discipline. Then the land ahead — brooks and springs, wheat and barley and vine and fig and pomegranate, olive oil
and honey, iron and copper — and the one instruction the Torah gives about a full stomach: eat, be satisfied, and bless. Then the warning: when the houses are
built and the herds and the silver multiply, do not say "my power and the might of my hand"; if you forget and serve other gods you perish like the nations.
Three things stand out. The shelf again has no section on the chapter, but it cannot leave it alone: sixteen rows elsewhere quote it, most of them from the
Sifrei's sections on the next chapter's praise of the Land, which quote this chapter's praise back at it — every row read whole, five of them for the second
time. The chapter holds two things the machine has nowhere else: 8:8 is the only verse in the Bible that names all seven kinds of fruit the Land is praised
for (and it names honey with no milk), and 8:10 is the Torah's one command to bless God, the seat of the grace after meals — no cell of ours compiles it yet;
both go to the compile. And the garment that did not wear out for forty years is a state, not an event: the tape has lines for the manna and the serpents and
the rock, none for the clothes, so the compile must decide how a retelling of a state is graded. This was the first reading under the two-run rule, and it
fit one run with one stopping point inside it. The chapter is frozen as one unit, the 222nd, every gate green.

'''
RESUME_NOTE = f'''# ⚠ THE DEUTERONOMY WALK sitting 6 ({DATE}; step9/DEUTERONOMY_WALK.md "Sitting 6" + "Sitting 6 — AS BUILT"): CHAPTER 8 READ AND FROZEN as one
# unit (the {C_UNITS}nd — {UID} 8:1-20), ONE RUN under THE TWO-RUN RULE with one compaction inside it, every row whole: THE SIFREI SILENT ON THE CHAPTER
# but SIXTEEN rows from elsewhere (the Ekev piskaot on 11:10-12 quoting the Land's praise back; five reread whole) + Onkelos whole + the kin's spine credited
# by name from the Numbers walk — {L_ALL} sources, coverage computed; the seven species at one seat (8:8) and honey without milk; "eat, be satisfied, bless" the
# Torah's one command to bless (no cell yet); the king's law's tokens at 8:13; the written/read pair at 8:2; the forty years a STATE the tape never wrote;
# the ritual {N_PASS} PASS, CORPUS TRUTH GREEN ({C_UNITS} units, standing 2215 = 2209 + 6, hash unmoved), build_world, the journal gate ({J_KINDS} kinds, {J_ROWS} rows),
# the register gate --strict (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL}) GREEN; the tape unmoved since 5b. NEXT on the ruling: the commit; then 6b — the
# compile of chapter 8 in TWO runs (the debt box (a)-(n)), or the schema sitting first.
'''
STATE = f'''
#196 ADDENDUM 1 ({DATE}, at the close of THE DEUTERONOMY WALK sitting 6 — CHAPTER 8's READING, the ONE run — A CLEAN COMPACTION POINT): THE STATE: chapter 8 read and frozen as one unit ({UID}, the {C_UNITS}nd); the corpus {C_UNITS} units, standing 2215 (2209 + 6 as predicted), hash 8b8fff1fa28953af unmoved; the tape unmoved since 5b (RUN (1307, 96, 88, 0, 12, 1602, 38, 319, the four pairs, 127), markers 167, closes 127); the ledger deu_08_ekev_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the outside rows {L_SIF}: MATERIAL {L_XM} / CONTEXT {L_XC}; {L_BYTES:,} bytes, lint 0); the manifest {N_CLAIMS} claims verified {N_CLAIMS}/0; the display layer +{OV_REF8} / +32 (by_ref {OV_REF}, by_gloss {OV_GL}). THE GATES: the ritual {N_PASS} PASS; verify_text GREEN (20 steps, 7 scenarios); CORPUS TRUTH GREEN twice; build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer since 5b); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL}); the home-path gate GREEN; the labels census GREEN ({LN}); large_letter_probes {LL}; the ink {N_INK} asserts, 0 failing on the second and third runs (the third after the display patch). THE RUN'S SHAPE: the first READING sitting under THE TWO-RUN RULE — one run, the compaction point #196 inside it at 743k ("Get ready to compact"), the owner's "Reread" after it, the run resumed at the step the point named (the ledger writer) with no re-derivation; then the display patch, the manifest (the I2 analogy at 297:4 retyped from the row's words before it was written — "bring", not "the land"), the seat, ONE GATES CHAIN in the background (ch8_gates.sh: the manifest, the seat chain, the fold, build_world, the journal gate, the register gate, the large letters, the home gate — the summary read once), verify_claims and the labels census beside it, the records (write_ch8_records.py from the sheet, one call: the map's "Sitting 6 — CHAPTER 8 — AS BUILT" with eleven lessons, COMPILE_DEBT's 6b box (a)-(n), MIDDOT's block (E10 at 39:4, 39:8, 48:8; I2 at 297:4; the name for its sound at 37:5), MISHNAH_TOPICS' two row notes (Blessings 6-7 and First Fruits 1 ROUTED to 6b), RESEARCH_LOG's entry, THE_STEPS, THE_BRIEFING (the scoreboard and an entry), RESUME, the recovery page rewritten whole (section 2 to this close; under 10,240 bytes), the addenda's §43, the stamp row, the memory (the walk note and the index line under 17,000 bytes)); the forms copied (copy_ch8_forms.py). A SESSION NOTE: the shell snapshot's `grep` function broke mid-run (a wrapper calling a missing native binary) — use /usr/bin/grep by path in this session. NOT COMMITTED: the whole sitting since 29c189b plus the two-run rule's records — the commit message drafted at <scratch>/commit_msg_ch8.txt for his word ("commit" = no push; "commit push" = both). NEXT ON THE RULING: the commit; then 6b — THE COMPILE OF CHAPTER 8 in TWO runs (RUN A the rereads, the measurements, the design in the map, the docket by the union rule, every row whole; RUN B the types, the runner, the tape to 10/10, the gates chain, the records, the forms, the commit message; the debt box (a)-(n) its list — the blessing after the meal and the seven species with no cell anywhere; the forty years as a STATE the design decision) — or the Decalogue-schema sitting first, on his word; THE INSTALL HYPOTHESIS on the table beside it. IF THIS COMPACTS HERE: reread the recovery page, the map's "Sitting 6 — CHAPTER 8 — AS BUILT" (NEXT and the lessons), MEMORY.md — nothing else unasked; THE_STEPS Step 5 + the compiler block before 6b's design.
'''
ADDENDA = f'''
## 43. ADDENDUM ({DATE}, THE DEUTERONOMY WALK sitting 6 — CHAPTER 8, Deuteronomy 8:1-20 READ AND FROZEN in ONE run under THE TWO-RUN RULE, every row whole; the owner: "Go", "Get ready to compact", "Reread"; the state doc's #196 and its addendum 1)
THE STATE: chapter 8 read and frozen as one unit ({UID}, the {C_UNITS}nd); the corpus {C_UNITS} units, standing 2215 (2209 + 6 as predicted), hash
8b8fff1fa28953af unmoved; the tape UNMOVED since 5b (RUN (1307, 96, 88, 0, 12, 1602, 38, 319, the four pairs, 127), markers 167, closes 127); the
journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL}); uncommitted since 29c189b.
WHAT THE SITTING FOUND: the Sifrei SILENT on the chapter (no piska between 36 on 6:9 and 37 on 11:10) but SIXTEEN rows from elsewhere its whole voice
— the Ekev piskaot on 11:10-12 quoting the chapter's praise of the Land back at it, eight other piskaot quoting its sentences (five rows reread whole);
the range citations the Hebrew regex cannot read, found through the English and asserted by string; the two files dividing 39:6-8 differently; the
kin's spine credited by name from the Numbers walk (Exodus 16-17 through the Mekhilta only); THE SEVEN SPECIES at one seat (8:8) and HONEY WITHOUT
MILK; "EAT, BE SATISFIED, BLESS" the Torah's one command to bless — no cell anywhere, owed to 6b; the book's one interrogative he (8:2) with the
manna's test-clause; THE KING'S LAW'S TOKENS at 8:13 and 8:14; "not by bread alone" the one seat; THE WRITTEN/READ PAIR at 8:2 (the store's extra
token); THE FORTY YEARS AS A STATE the tape never wrote (the compile's design decision); the infinitive absolute of forgetting at 8:19; "because" the
heel at 8:20; Onkelos's Word twice, the fear thrice, the shoes, the counsel.
THE TWO-RUN RULE'S FIRST READING SITTING: one run, one compaction inside it (#196), the reread three files, the run resumed at the step named; the
gates ONE chain in the background with one summary; a middah analogy retyped from the row's words before the manifest was typed.
THE FILES CHANGED: logic/oral_triage/deu_08_ekev_{LDATE}.md (new); logic/units/{UID}.yaml (draft → frozen, six operators, step E, the scenarios in
the anchor form) and logic/py_units/{UID}.py; logic/oral_audit/manifests/{UID}_claims.json (new); logic/glosses/word_gloss_overrides.yaml (+{OV_REF8} by
reference, +32 by gloss); logic/corpus/CORPUS_TRUTH.py ({C_UNITS}, 2215) and corpus_world.sqlite; the records (the map, COMPILE_DEBT, MIDDOT, MISHNAH_TOPICS,
RESEARCH_LOG, THE_STEPS, THE_BRIEFING, RESUME, the state doc, the recovery page, this file, STAMP_LEDGER, the memory); World/step9/forms_deuteronomy_walk/
(the sitting's scripts and prints); with the two-run rule's records of the same date (RECORD_FORMS, THE_STEPS, THE_BRIEFING, the map, the memory).
NEXT ON THE RULING: the commit; then the compile of chapter 8 (6b) in two runs — or the Decalogue-schema sitting first — on the owner's word.
'''
MEMPAR = f'''
SITTING 6 DONE {DATE} (the owner: "Go" after 29c189b and the two-run rule, "Get ready to compact" at 743k, "Reread"; the map's "Sitting 6" and "Sitting 6 —
AS BUILT"): CHAPTER 8 READ AND FROZEN as one unit ({UID}, the {C_UNITS}nd) — the first reading sitting under THE TWO-RUN RULE, ONE run with one compaction
inside it (#196; the run resumed at the step the point named), every row whole. The Sifrei SILENT on the chapter but SIXTEEN rows from elsewhere (the
Ekev piskaot quoting the Land's praise back; five reread whole; the range citations found through the English; 39:6-8 divided differently by the two
files); the kin's spine credited by name from the Numbers walk; the seven species at one seat (8:8) and honey without milk; "eat, be satisfied, bless"
the Torah's one command to bless — NO CELL ANYWHERE, owed to 6b; the king's law's tokens at 8:13; the written/read pair at 8:2; THE FORTY YEARS A STATE
the tape never wrote (6b's design decision). Every gate green; the corpus {C_UNITS} / 2215 / hash unmoved; the tape unmoved. ⚠ LESSONS (eleven in the map):
the spine's silence is not the shelf's; a range citation is invisible to the regex; the two files divide a piska differently; a reading fits one run; a
middah code is checked against the row's own words; a reading's gates are one chain too. OWED TO 6b (COMPILE_DEBT's box (a)-(n)): the blessing after the
meal, the seven species, the manna and the humbling, the forty years as a state, the discipline, take heed lest, the heart lifted up, the exodus formula,
the serpents and the rock, my power and my hand, the covenant established, the testimony, the king's law's tokens, the docket. NOT COMMITTED (since
29c189b; the message drafted at <scratch>/commit_msg_ch8.txt). NEXT on the ruling: the commit; then 6b in two runs, or the schema sitting, on the owner's word.
'''
MEMLINE_OLD_START = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — '
MEMLINE_NEW = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — map World/step9/DEUTERONOMY_WALK.md; chapters 1-7 COMPILED (29c189b PUSHED); SITTING 6 DONE 2026-09-18 (ch 8 FROZEN, 222 units); NEXT: commit, then 6b\n'
DESC_OLD = "COMMITTED THROUGH 29c189b (2026-09-18, on 'Commit and push'; PUSHED) — THE DEUTERONOMY WALK opened 2026-09-15 — "
DESC_NEW = "COMMITTED THROUGH 29c189b (2026-09-18; PUSHED) — SITTING 6 DONE 2026-09-18 (chapter 8 READ AND FROZEN as one unit, the 222nd; the first reading under the two-run rule; UNCOMMITTED) — THE DEUTERONOMY WALK opened 2026-09-15 — "
REC2_OLD_START = '## 2. WHERE IT STANDS'
REC2_NEW = f'''## 2. WHERE IT STANDS ({DATE}, after sitting 6; the state doc #196 addendum 1 the newest point)
- NUMBERS CLOSED. DEUTERONOMY 1:1-7:26 COMPILED AND ON THE TAPE (29c189b PUSHED); 8:1-20 READ AND FROZEN (sitting 6, one run).
- {C_UNITS} frozen units, standing 2215, hash 8b8fff1fa28953af. 62 runners, 67 daemons, 460 functions; registries 1129 kinds / 1029 effects.
- THE TAPE unmoved since 5b (RUN (1307, 96, 88, 0, 12, 1602, 38, 319, the four pairs, 127); markers 167, closes 127); the sweep 62/62; every gate
  GREEN; the register gate DECLARED {R_DECL} / DEBT 0.
- Uncommitted since 29c189b: sitting 6 whole and the two-run rule's records; the message at <scratch>/commit_msg_ch8.txt.
- NEXT ON HIS WORD: the commit; then 6b — THE COMPILE OF CHAPTER 8 in TWO runs (the debt box its list), or the schema sitting.
'''
TOPIC_BLESS = ' — 6-7 ROUTED 2026-09-18 (THE DEUTERONOMY WALK sitting 6, chapter 8\'s reading: the blessing after the meal — 8:10 "eat, be satisfied, bless", the Torah\'s one command to bless, no cell anywhere; the seven species\' order of blessings, 8:8 — owed to the compile 6b\'s docket with Berakhot 20b-21a, 35a-b, 41a-44a, 48b-49b; deu_08_ekev_2026-09-18.md)'
TOPIC_FRUITS = ' — 1 ROUTED 2026-09-18 (THE DEUTERONOMY WALK sitting 6, chapter 8\'s reading: the first fruits from the seven species for which the Land is praised — 8:8 the list, the Sifrei 297:4 by the verbal analogy on "bring"; owed to the compile 6b\'s docket, 1:3 and 1:10; deu_08_ekev_2026-09-18.md)'

LINT = f'{ROOT}/logic/solo_tools/gloss_lint.py'
def lint(path):
    out = subprocess.run([sys.executable, LINT, path], capture_output=True, text=True).stdout
    m = re.search(r'gloss_lint: (\d+) flag', out); return int(m.group(1)) if m else -1
WALKP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; RECP = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
TOPICS = f'{ROOT}/logic/MISHNAH_TOPICS.md'
TOUCH = [f'{ROOT}/logic/findings/STAMP_LEDGER.md', f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', f'{ROOT}/World/RESUME.md', f'{ROOT}/THE_STEPS.md', f'{ROOT}/THE_BRIEFING.md', f'{ROOT}/World/step9/COMPILE_DEBT.md', f'{ROOT}/RESEARCH_LOG.md', f'{ROOT}/logic/MIDDOT.md', RECP, f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md', f'{MEM}/MEMORY.md', TOPICS]
# ---- THE ANCHORS, ASSERTED PRESENT ONCE BEFORE ANY WRITE ----
A_RESUME = '# ⚠ THE DEUTERONOMY WALK sitting 5b (2026-09-18;'
A_SCORE = '## SCOREBOARD (as of 2026-09-18, latest)\n'
A_BULLET = '- **CHAPTER 7 COMPILED — THE OLD LAW SAID AGAIN FOR THE NEW PLACE, GRADED AGAINST THE CELLS THAT COMPILED IT FIRST'
A_ENTRY = '### 2026-09-18 — THE TWO-RUN RULE: A COMPILE SITTING IS TWO RUNS, A READING ONE'
A_MIDDOT = '\n## Exodus block campaign — owner\'s word "Do 3")\n'
A_REC5 = 'the newest instances: the map\'s "Sitting 5" and "Sitting 5b"'
A_REC6 = '- Deuteronomy\'s sittings: the map; the addenda §31-42 (§39 the whole-row rule). The cost cuts: §35.'
T_BLESS = '**1. Mishnah, Blessings**'; T_FRUITS = '**11. Mishnah, First Fruits**'
ANCH = [(f'{ROOT}/World/RESUME.md', A_RESUME), (f'{ROOT}/THE_STEPS.md', '\n## Step 6 — Publish\n'), (f'{ROOT}/THE_BRIEFING.md', A_SCORE), (f'{ROOT}/THE_BRIEFING.md', A_BULLET), (f'{ROOT}/THE_BRIEFING.md', A_ENTRY), (f'{ROOT}/logic/MIDDOT.md', A_MIDDOT), (RECP, REC2_OLD_START), (RECP, '\n## 3. THE STANDING LAWS'), (RECP, A_REC5), (RECP, A_REC6), (f'{MEM}/MEMORY.md', MEMLINE_OLD_START), (f'{MEM}/deuteronomy-walk.md', DESC_OLD)]
for p, a in ANCH: assert rd(p).count(a) == 1, (p, a[:40], rd(p).count(a))
tl = rd(TOPICS).split('\n'); assert sum(l.startswith(T_BLESS) for l in tl) == 1 and sum(l.startswith(T_FRUITS) for l in tl) == 1 and 'ROUTED 2026-09-18' not in rd(TOPICS)
assert '## Sitting 6 — CHAPTER 8 — AS BUILT' not in rd(WALKP) and '## Sitting 6 — CHAPTER 8, Deuteronomy 8:1-20' in rd(WALKP) and '#196 ADDENDUM 1' not in rd(TOUCH[1]) and '#196 (2026-09-18' in rd(TOUCH[1]) and '## 43. ADDENDUM' not in rd(TOUCH[9]) and '## 42. ADDENDUM' in rd(TOUCH[9]) and 'SITTING 6 DONE' not in rd(f'{MEM}/deuteronomy-walk.md') and 'DEUTERONOMY SITTING 6 — CHAPTER 8' not in rd(TOUCH[5]) and f'| {UID} |' not in rd(TOUCH[0]) and 'CASE LAW ON CHAPTER 8' not in rd(TOUCH[7])
s = rd(RECP); i = s.index(REC2_OLD_START); j = s.index('\n## 3. THE STANDING LAWS'); REC_NEW = s[:i] + REC2_NEW + s[j:]
REC_NEW = REC_NEW.replace(A_REC5, 'the newest instances: the map\'s "Sitting 6" and "Sitting 5b"').replace(A_REC6, '- Deuteronomy\'s sittings: the map; the addenda §31-43 (§39 the whole-row rule). The cost cuts: §35.')
assert len(REC_NEW.encode()) <= 10240, len(REC_NEW.encode())
m = rd(f'{MEM}/MEMORY.md'); i = m.index(MEMLINE_OLD_START); j = m.index('\n', i) + 1; MEM_NEW = m[:i] + MEMLINE_NEW + m[j:]
assert len(MEM_NEW.encode()) < 17000, len(MEM_NEW.encode())
BEFORE = {p: lint(p) for p in TOUCH}
print('lint before:', {os.path.basename(p): n for p, n in BEFORE.items()}, '| recovery page bytes', len(REC_NEW.encode()), '| MEMORY.md bytes', len(MEM_NEW.encode()))
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
row_note(TOPICS, T_FRUITS, TOPIC_FRUITS)
open(RECP, 'w', encoding='utf-8').write(REC_NEW); print('recovery page rewritten', len(REC_NEW.encode()), 'bytes')
append(TOUCH[9], ADDENDA)
append(f'{MEM}/deuteronomy-walk.md', MEMPAR)
replace_once(f'{MEM}/deuteronomy-walk.md', DESC_OLD, DESC_NEW)
open(f'{MEM}/MEMORY.md', 'w', encoding='utf-8').write(MEM_NEW); print('MEMORY.md', len(MEM_NEW.encode()), 'bytes')
AFTER = {p: lint(p) for p in TOUCH}
print('lint after: ', {os.path.basename(p): n for p, n in AFTER.items()})
assert all(AFTER[p] <= BEFORE[p] for p in TOUCH), [(os.path.basename(p), BEFORE[p], AFTER[p]) for p in TOUCH if AFTER[p] > BEFORE[p]]
assert lint(WALKP) == 0 and lint(f'{MEM}/deuteronomy-walk.md') == 0 and len(rd(RECP).encode()) <= 10240
print('records written; the lints at or under their baselines; the map and the memory file lint 0; the page under its cap')
