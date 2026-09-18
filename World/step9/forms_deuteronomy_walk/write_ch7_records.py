#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 5 — CHAPTER 7 (2026-09-17/18; the owner: "Go" after 4b's commit, then "go for run 2", "run 3 go", "4 go" for runs 2-4 —
# the second READING sitting under THE FOUR-RUN RULE, every row whole under THE WHOLE-ROW RULE): THE RECORDS at the close, from the sheet
# World/step9/RECORD_FORMS.md in ONE call — the map's "Sitting 5 — CHAPTER 7 — AS BUILT", COMPILE_DEBT's box (owed to the compile 5b), MIDDOT's block
# (the Sifrei's two rows that argue by a rule), RESEARCH_LOG's entry, THE_STEPS' paragraph, THE_BRIEFING's bullet and entry, RESUME's note, the state
# doc's #194 addendum 3, the recovery page (rewritten whole, under 10 KB), the recovery addenda's section 41, the stamp row, the memory file and the
# index line (under 17,000 bytes). Every number parsed from a print named beside it (--check prints them and writes nothing); every insert on a
# unique anchor asserted present once; the lints before and after. Sitting 4's form (write_ch6_records.py) on the sheet.
import os, re, subprocess, sys, yaml, json
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/' + os.path.abspath(ROOT).replace('/', '-') + '/memory')
DATE = '2026-09-18'; LDATE = '2026-09-17'
UID = 'deu_07_nations_cherem'
CHECK = '--check' in sys.argv
def rd(p): return open(p, encoding='utf-8').read()
# ---- THE NUMBERS, PARSED FROM THE PRINTS ----
truth = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py')
assert 'assert len(W["units"]) == 221' in truth and 'assert len(W["standing"]) == 2209' in truth and "8b8fff1fa28953af" in truth
CT = rd(f'{SP}/ch7_truth.out'); CB = rd(f'{SP}/ch7_bake.out'); C1 = rd(f'{SP}/ch7_fold_check1.out')
assert 'CORPUS TRUTH GREEN' in CT and 'CORPUS TRUTH GREEN' in C1 and 'wrote corpus_world.sqlite' in CB
rit = rd(f'{SP}/ch7_ritual_{UID}.out'); N_PASS = len(re.findall(r'^PASS', rit, re.M))
assert 'RITUAL COMPLETE' in rit and N_PASS == 13 and not re.search(r'^FAIL', rit, re.M), N_PASS
vt = rd(f'{SP}/ch7_vt_{UID}.out'); assert 'TEXT LAYER GREEN: 26 steps, 7 scenarios' in vt
assert '  status: frozen' in rd(f'{ROOT}/logic/units/{UID}.yaml') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json') and 'ALL_DONE' in rd(f'{SP}/ch7_chain.log')
JG = rd(f'{SP}/ch7_journal.out'); RG = rd(f'{SP}/ch7_register.out'); BW = rd(f'{SP}/ch7_build.out')
assert 'GATE GREEN' in JG and 'ALL GREEN' in BW and 'THE REGISTER GATE: GREEN' in RG, (JG[-200:], BW[-200:])
mj = re.search(r'(\d+) kinds, ([\d,]+) rows', JG); J_KINDS, J_ROWS = mj.group(1), mj.group(2)
mr = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', RG); R_DECL, R_DEBT, R_FAIL = mr.groups()
assert R_DEBT == '0' and R_FAIL == '0', mr.groups()
mc = re.search(r'(\d+) units, (\d+) facts, (\d+) demands \((\d+) open\)', CT); C_UNITS, C_FACTS, C_DEM, C_OPEN = mc.groups()
assert C_UNITS == '221', C_UNITS
HG = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/scrub_home_paths.py', '--check'], capture_output=True, text=True).stdout
assert 'GREEN' in HG, HG[-200:]
LED = rd(f'{ROOT}/logic/oral_triage/deu_07_vaetchanan_ekev_{LDATE}.md')
ml = re.search(r'\*\*read: (\d+) of \1 — COMPLETE\*\* \((\d+) Onkelos verses and (\d+) Sifrei rows.*?MATERIAL (\d+) Onkelos, CONTEXT (\d+) Onkelos, MATERIAL (\d+) Sifrei outside, CONTEXT (\d+) Sifrei outside', LED, re.S)
L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_XM, L_XC = ml.groups()
assert L_ALL == '29' and L_ONK == '26' and L_SIF == '3' and LED.count('⟨MISS⟩') == 0
L_BYTES = len(LED.encode())
d_ov = yaml.safe_load(rd(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'))
OV_REF7 = len([k for k in d_ov['by_ref'] if k.startswith('Deut.7.')]); OV_REF, OV_GL = len(d_ov['by_ref']), len(d_ov['by_gloss'])
assert OV_REF7 == 36 and OV_REF == 532 and OV_GL == 434, (OV_REF7, OV_REF, OV_GL)
N_CLAIMS = len(json.load(open(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json', encoding='utf-8'))); assert N_CLAIMS == 6
VC = rd(f'{SP}/ch7_vc.out'); assert 'SUMMARY: 6 verified, 0 failed, 0 uncheckable, 0 no-check' in VC
LAB = rd(f'{SP}/ch7_labels.out'); LN = re.search(r'num\s+(\d+) claims\s+labeled\s+\1\s+debt\s+0', LAB).group(1); assert 'GATE PASSED' in LAB
assert rd(f'{SP}/ch7_ink_run3.out').strip().endswith('0 failing statements') and rd(f'{SP}/ch7_ink_run2.out').strip().endswith('0 failing statements')
N_INK = len(re.findall(r'^assert ', rd(f'{SP}/ch7_ink.py'), re.M))
LL = subprocess.run([sys.executable, f'{ROOT}/World/step9/large_letter_probes.py'], capture_output=True, text=True).stdout.strip().split('\n')[-1]
assert LL.endswith('6/6'), LL
JR6 = re.search(r'12 kinds, (\d+) rows', rd(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch6_journal.out')).group(1); DJ = int(J_ROWS.replace(',', '')) - int(JR6)
print('PARSED:', dict(ritual_pass=N_PASS, journal=(J_KINDS, J_ROWS, DJ), register=(R_DECL, R_DEBT, R_FAIL), corpus=(C_UNITS, C_FACTS, C_DEM, C_OPEN), ledger=(L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_XM, L_XC, L_BYTES), overrides=(OV_REF7, OV_REF, OV_GL), claims=N_CLAIMS, labels=LN, ink_asserts=N_INK, large_letters=LL))

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

STAMP = (f'| {DATE} | {UID} | DELEGATED | FULL RULE | Deuteronomy 7:1-26 derivation {LDATE} (THE DEUTERONOMY WALK sitting 5 — CHAPTER 7; the owner: "Go" after chapter 6\'s commit, then "go for run 2", "run 3 go", "4 go" for the runs — the second reading sitting under THE FOUR-RUN RULE, every row whole under THE WHOLE-ROW RULE; the book\'s fifth reading — chapter 7 as one draft with the portion\'s edge at 7:12 inside it, the 221st frozen unit): declared reading COMPLETE (one ledger logic/oral_triage/deu_07_vaetchanan_ekev_{LDATE}.md, {L_ALL} sources — Onkelos 7:1-26 whole and fresh (the export\'s twenty-six rows the DB\'s twenty-six, asserted), THE SIFREI ON DEUTERONOMY SILENT ON THE CHAPTER (no piska head between 36 on 6:9 and 37 on 11:10 — the heads computed) and its THREE rows outside any piska citing chapter 7, found by the scan of the whole export in both files and read whole (37:1 on 11:10 — the English\'s own "(Dt.7:12)" an INTERPOLATION, read and marked; 50:4 on 11:23 — 7:1\'s count, even one of the seven greater than all Israel; 61:7 on 12:3 — 7:26\'s doubled verbs the rule of renaming the shrines for the worse), none excluded; the kin\'s spine (Exodus 23:20-33, 34:11-16, Numbers 33:50-56) CREDITED BY NAME from the Exodus and Numbers ledgers with the counts computed; coverage computed by script, missing 0 extra 0; the ink facts computed from the Tanakh DB, the snapshot store and the shelf\'s bytes — {N_INK} asserts, seven fell on the first typed pass (forms, not facts) and were retyped from the print, none after; every quotation cut by consonants, no miss; gloss_lint 0), claims DV07-01..06 verified {N_CLAIMS}/{N_CLAIMS} (every check the word\'s longest store-piece whole — never 7:9\'s "His commandments", where the store carries the written and the read form), claim_labels_census --strict GREEN, seated as six WITNESS_READ operators at the claims\' first verses (7:1, 6, 9, 12, 17, 25), verify_text GREEN (26 steps, 7 scenarios), the ritual {N_PASS} PASS, CORPUS TRUTH GREEN ({C_UNITS} units, standing 2209 = 2203 + 6 as predicted, hash 8b8fff1fa28953af UNMOVED), build_world ALL GREEN, the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows), the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — no seat in the chapter). THE PARSER: two number verses in twenty-six, NO GAP — 7:1 "seven nations" [7] WITH THE VERSE\'S OWN WITNESS (seven gentilic tokens beside the numeral), 7:9 "to a thousand generations" [1000]; "the oath" (7:8) starred as the seven-stem homograph, "swore" no number. THE FINDS: the spine silent on the chapter, its whole voice three rows from elsewhere; 7:1 alone counts its list — SEVEN WHERE EXODUS HAD SIX (the Girgashite); both directions of marriage barred where Exodus 34:16 barred one; four objects where 34:13 had three; THE WRITTEN/READ PAIR at 7:9 (the store\'s extra token; 5:10\'s kin); "to a thousand generations" [1000] against the ten words\' bare plural; Onkelos\'s SUPPLIED DOCTRINE at 7:10 (twelve tokens made twenty-two — the wicked paid in this world); "because" the noun heel at 7:12, the portion Ekev named by it; THE FLOCK\'S "YOUNG" TAGGED A NAME in the DB\'s morph at four seats (the goddess\'s homograph); the hornet\'s three seats (the promise, the retelling, the receipt); little by little at 7:22 and Exodus 23:30 alone; "YOU SHALL NOT COVET" (7:25) the tenth word\'s verb on the idols\' silver and gold. Stamp delegated under the AUTO-SEAT ruling; the owner may overrule. |\n')

WALK = f'''

## Sitting 5 — CHAPTER 7 — AS BUILT ({DATE}; the design above stands as written — the four runs ran as designed, the RUN 2 and RUN 3 paragraphs their record; every departure from the design named here)

THE RESULT: Deuteronomy 7:1-26 READ AND FROZEN as one unit — {UID}, the {C_UNITS}st frozen unit (the portion's edge at 7:12 inside it — the chapter the unit, per the
ruling); the ledger logic/oral_triage/deu_07_vaetchanan_ekev_{LDATE}.md ({L_ALL} sources: Onkelos {L_ONK} — MATERIAL {L_OM} / CONTEXT {L_OC}; the Sifrei's spine 0 rows — SILENT on the
chapter; the outside rows {L_SIF} — MATERIAL {L_XM} / CONTEXT {L_XC}, 37:1 an interpolation; the kin's spine credited by name in its own section; {L_BYTES:,} bytes; lint 0); the
manifest {UID}_claims.json ({N_CLAIMS} claims DV07-01..06, verify_claims {N_CLAIMS}/0, the labels census GREEN — {LN} labeled, debt 0); six WITNESS_READ seats at 7:1, 6, 9,
12, 17, 25, step E, seven anchor scenarios; the ritual {N_PASS} PASS; the fold predicted and matched before and after the bake ({C_UNITS} units, standing 2209, hash
8b8fff1fa28953af; {C_FACTS} facts, {C_DEM} demands, {C_OPEN} open); the display layer +{OV_REF7} by reference and +49 by gloss (by_ref {OV_REF}, by_gloss {OV_GL} after); the stamp row
delegated (FULL RULE). No engine file changed — the tape as at 4b's close (RUN (1304, 96, 88, 0, 12, 1595, 37, 319, the four pairs, 127), markers 167, closes 127);
the sweep as at 4b.

THE DEPARTURES FROM THE DESIGN: none in substance. THE FOUR RUNS held their edges — run 1 the rereads, the measurements, the ink ({N_INK} asserts, seven failing
on the first pass and 0 on the second) and the design (#194, the compaction); run 2 the rows whole and the ledger (#194 addendum 1); run 3 the display layer, the
manifest, the seat, the chain, the fold and the gates (#194 addendum 2); run 4 the records (#194 addendum 3) — the owner compacted after run 1 only and said
"reread", "go for run 2", "run 3 go", "4 go". Three small departures: the run-3 record named THE_WORLD among run 4's records, but a reading's sheet has no
THE_WORLD row (the compile's) — not written; the recovery page's cap tripped twice by a few bytes (run 3, run 4) and the lines were shortened, nothing else
touched; THE INSTALL HYPOTHESIS was recorded ON THE TABLE at run 1 on the owner's "yes record it" — the map's tail section, not this sitting's work, no engine
change. The design's OWED TO THE COMPILE list stands as the 5b box below (COMPILE_DEBT).

THE GATES, COMPUTED FROM THEIR PRINTS: the ritual {N_PASS} PASS (RITUAL COMPLETE, {C_UNITS} frozen units); CORPUS TRUTH GREEN twice ({C_UNITS} units, {C_FACTS} facts, {C_DEM}
demands ({C_OPEN} open), hash 8b8fff1fa28953af — the tripwire's literals set to the prediction before the bake, matched); build_world ALL GREEN; the journal gate
GREEN ({J_KINDS} kinds, {J_ROWS} rows — {JR6} at sitting 4b, +{DJ} on the fold layer with the tape unmoved); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT},
FAILS {R_FAIL} — no seat in chapter 7); the home-path gate GREEN; the labels census GREEN ({LN} claims labeled, debt 0); large_letter_probes {LL}; the lints at their
baselines.

⚠ THE LESSONS (the three runs', gathered — the numbered list the sheet asks for): (1) A CHAPTER WITHOUT A SPINE READS ITS KIN'S SPINE BY CREDIT — the Exodus 23
and 34 ledgers and the Numbers 33 ledger hold the angel's clauses, the renewed covenant and the dispossession; the credit is by name, with the counts computed
from those ledgers, never a source of this one. (2) THE TRANSLATOR'S PARENTHESIS AGAIN — 37:1's "(Dt.7:12)" names the portion's opening the Sifrei skips; read and
marked, never counted. (3) A NUMBER VERSE CAN CARRY ITS OWN WITNESS — 7:1's seven gentilic tokens beside "seven": the count checkable from the ink alone, and the
shelf reads the count (50:4). (4) THE WRITTEN/READ PAIR IS THE STORE'S EXTRA TOKEN — the store carries both forms, the DB the written one marked; the mismatch
census names the seat; no check on that word. (5) THE FIRST TYPED PASS FELL SEVEN WAYS ON FORMS — a token's variants summed short, a count typed from memory, a
gloss already rewritten at chapter 6: the print first, then the assert. (6) A DERIVATION BY ASSERTED SUBSTITUTIONS — the dump script from the prior chapter's by
twenty-two named replacements, each asserted present; the forms copy keeps its git-root line, so the header check is conditional. (7) A PORTION'S EDGE INSIDE A
CHAPTER — 7:12 opens the next portion; the chapter is the unit per the ruling; the token split recorded. (8) A CHAPTER WITHOUT A SPINE HAS A LEDGER WITHOUT A
SPINE SECTION — the form drops the spine's loop, the credits dict and the divergence check whole; the coverage line says "0 rows" with the heads computed. (9) THE
OUTSIDE ROWS ARE THE SPINE'S WHOLE VOICE — 50:4 the count, 61:7 the renaming, both by E10. (10) A SINGULAR AND A PLURAL "THAN YOU" — a census by spelling splits
what the shelf joins by sense; the row names the seat. (11) THE FORMS HELD FIRST TIME — five run-3 scripts derived by name changes alone, none retyped: a
reading's run 3 is a form, not a design. (12) THE FOLD LAYER GROWS WITH A FREEZE WHILE THE TAPE STANDS — the journal's index +{DJ} rows on the new unit, the
header re-pinned to the unmoved hash. (13) THE FOUR-RUN RULE HELD ON A SECOND READING SITTING — one compaction, the reread three files, each checkpoint naming
the next run's first step; the recovery page's cap is a tripwire, not a target.

THE FORMS: World/step9/forms_deuteronomy_walk/ — the four runs' scripts (derive_ch7_dump0.py, ch7_dump0.py, ch7_measure1.py, ch7_ink.py, the three row files,
write_ch7_ledger.py, ch7_patch_overrides.py, write_ch7_manifest.py, seat_ch7.py, ch7_chain.sh, ch7_fold.sh, write_ch7_design.py, write_ch7_run2.py,
write_ch7_run3.py, write_ch7_records.py, copy_ch7_forms.py) and the prints (the dump, the measurement, the Onkelos dump, the outside rows, the store's glosses,
the ink runs, the chain log, the ritual, verify_text, the claims' verifier, the labels census, the fold's checks, the gates).

NEXT on the ruling: THE COMPILE OF CHAPTER 7 (sitting 5b) in four runs — (1) the rereads (THE_STEPS Step 5 + the compiler block; this section; the 5b box in
COMPILE_DEBT.md), the measurements (the tape's state at Deut 6:19; the runners' cells the chapter calls — the Exodus 23 runner's clauses for the hornet and
little by little, 3b's coveting cell for 7:25, the second word's cell for 7:4 and 7:16; the erection docket's Mishnah Avodah Zarah rows credited) and THE DESIGN
in this file before any code; (2) the docket by the union rule (Avodah Zarah 20a, 36b, 42a-54b whole; Kiddushin 68b; Yevamot 23a; Sotah 35b-36a; Chullin 89a;
Makkot 22a; Mishnah Avodah Zarah 1-4; Mishnah Kiddushin 3:12), every row whole; (3) the runner (the ban with chapter 20's cell owed; no covenant, no favor, no
marriage; the altars and the Asherim; the chosen people; the faithful God and the hater repaid; because you hear and the blessings; no pity, no serving; do not
fear; little by little by CALL; the idols' silver and gold with the tenth word's cell by CALL; the abomination into the house; the run citations as the
readback's reference rows), the stitch, the tape to 10/10; (4) the gates chain, the records, the forms. Or THE DECALOGUE-SCHEMA SITTING first, on the owner's
word — THE INSTALL HYPOTHESIS stays on the table beside it. Then chapter 8, and on in order.
'''

DEBT = f'''
## DEUTERONOMY SITTING 5 — CHAPTER 7, Deuteronomy 7:1-26 READ AND FROZEN ({DATE}; DEUTERONOMY_WALK.md "Sitting 5" and "Sitting 5 — AS BUILT"; the ledger
## deu_07_vaetchanan_ekev_{LDATE}.md, {L_ALL} sources; one unit {UID} FROZEN, the {C_UNITS}st) — OWED TO THE COMPILE (sitting 5b): (a) THE BAN (7:2 "you shall
## utterly destroy them" with 20:16-18 — the seven nations' cell; the Sifrei's war sections at chapter 20 unread — the cell's ink here, the war chapter's CALL when
## it compiles); (b) NO COVENANT AND NO FAVOR (7:2 — Avodah Zarah 20a's readings of "show them no favor": no settlement, no gift, no praise; Exodus 23:32 and 34:12,
## 15 the kin by CALL into the Exodus 23 and 34 runners); (c) NO MARRIAGE, BOTH DIRECTIONS (7:3-4 — "for he will turn your son": the child of a gentile mother follows
## her, Kiddushin 68b; Mishnah Kiddushin 3:12 CREDITED at the erection docket; Yevamot 23a; Avodah Zarah 36b; 7:4's "other gods" a CALL into 3b's second-word cell);
## (d) THE ALTARS, THE PILLARS, THE ASHERIM, THE IMAGES (7:5 with 12:3 — Mishnah Avodah Zarah 3:5-10 CREDITED; Avodah Zarah 45b-48b; the Sifrei 61:7's renaming for
## the worse with Tosefta Avodah Zarah 6:4); (e) THE CHOSEN PEOPLE (7:6-8 — Chullin 89a "not because you were more … but because you humble yourselves"; Exodus 19:5-6
## the kin); (f) THE FAITHFUL GOD AND THE HATER REPAID (7:9-10 — Onkelos's doctrine of the wicked paid in this world; "to a thousand generations" against the ten
## words' "to thousands" — 3b's cell by CALL; the fathers' iniquity visited there, the hater repaid to his face here); (g) "BECAUSE YOU HEAR" AND THE BLESSINGS
## (7:12-15 — the fruit, the increase and the young, no barrenness, the diseases of Egypt — Exodus 15:26, 23:25-26 the kin; 28:4, 11, 18, 51, 60 the blessings' and
## the curses' seats ahead); (h) NO PITY AND NO SERVING (7:16 — Exodus 23:33 "a snare" the kin by CALL; "your eye shall not pity" the book's five seats); (i) DO NOT
## FEAR (7:17-21 — Sotah 36a's hornet on the Jordan's bank; the run citations "did to Pharaoh" 7:18 and the trials, signs, wonders 7:19 as the readback's reference
## rows against the tape's plague and sea lines); (j) LITTLE BY LITTLE (7:22 — Exodus 23:29-30 the first telling, by CALL into the Exodus 23 runner; "the beasts of
## the field" the reason kept whole); (k) THE KINGS AND THE NAME (7:23-24 — "destroy their name from under heaven" beside Amalek's 25:19 ahead; Joshua 1:5's receipt);
## (l) THE IDOLS' SILVER AND GOLD (7:25 — Mishnah Avodah Zarah 3:5 CREDITED at the erection docket, 4:4-5 the nullification; Avodah Zarah 44b-52a; "you shall not
## covet" THE TENTH WORD'S VERB — 3b's coveting cell by CALL; Achan's Joshua 7:21 the run's case); (m) THE ABOMINATION INTO THE HOUSE (7:26 — Makkot 22a the lashes;
## Mishnah Avodah Zarah 3:3; "devoted like it" — the devoted thing's lemma, not the ban's); (n) THE RUN CITATIONS — "swore to your fathers" (7:8, 12, 13), the oath's
## tape entries as at chapter 6's (i); the hornet (7:20 ← Exodus 23:28, → Joshua 24:12); (o) THE DOCKET by the union rule (Avodah Zarah 20a, 36b, 42a-54b; Kiddushin
## 68b; Yevamot 23a; Sotah 35b-36a; Chullin 89a; Makkot 22a; Mishnah Avodah Zarah 1-4; Mishnah Kiddushin 3:12 — the scan will name the rest), every row whole;
## (p) THE FLOCK'S "YOUNG" TAGGED A NAME in the DB's morph at its four seats (7:13, 28:4, 18, 51) — a note for the DB, no cell (the gloss rewritten; the parser
## unaffected). NOTHING ELSE IN CHAPTER 7 IS OWED TO A LATER SITTING OF ITS OWN.
'''

MIDDOT = f'''- **THE SIFREI ON DEUTERONOMY'S OWN CASE LAW ON CHAPTER 7 (Deuteronomy 7:1-26; THE DEUTERONOMY WALK sitting 5, {DATE};
  the ledger logic/oral_triage/deu_07_vaetchanan_ekev_{LDATE}.md — THE SPINE SILENT ON THE CHAPTER, no piska head between 36 on 6:9
  and 37 on 11:10; its three rows outside any piska read whole in both files, the two that argue by a numbered rule below, each at its row):**
  · THE COUNT READ FROM THE REPETITION (50:4 on 11:23 from 7:1): 11:23's "greater and mightier than you" (the plural) beside 7:1's
    "seven nations greater and mightier than you" (the singular) — the second "than you" read as a teaching: EACH ONE of the seven
    greater than all Israel, Amos 2:9's Amorite the proof — E10 (the repeated expression signifies); THE INK: "seven nations" one seat,
    the verse's seven gentilic tokens the numeral's own witness; the singular phrase three seats, the plural one.
  · THE SHRINES RENAMED FOR THE WORSE (61:7 on 12:3 from 7:26): "and you shall destroy their name" beside 12:2's "you shall utterly
    destroy" — a DISPUTE: R. Eliezer the Asherah uprooted, R. Akiva the redundancy given a teaching (E10), the shrines RENAMED; 7:26's
    doubled verbs "utterly detest, utterly abhor" fix the direction — a name for the worse, never for the better (Tosefta Avodah Zarah
    6:4: "the Face of God" made "Dog-Face"); THE INK: the two infinitive absolutes one seat; the detesting verb Leviticus 11's.
  · THE INTERPOLATION (37:1 on 11:10): no rule — the English's own "(Dt.7:12)" with its note that the Sifrei does not expound the verse;
    the Hebrew cites 11:10 alone; read and marked, chapter 6's 104:8 the form.
'''

RESEARCH = f'''
## {DATE} — DEUTERONOMY 7 READ (THE DEUTERONOMY WALK sitting 5 — CHAPTER 7, in four runs, every row whole): THE SPINE SILENT ON THE CHAPTER; 7:1 COUNTS ITS OWN
## LIST — SEVEN WHERE EXODUS HAD SIX; THE OATH'S NOUN STARRED; THE WRITTEN/READ PAIR AT 7:9; ONKELOS'S SUPPLIED DOCTRINE AT 7:10; THE FLOCK'S YOUNG TAGGED A NAME;
## "YOU SHALL NOT COVET" ON THE IDOLS' SILVER AND GOLD

THE SPINE SILENT ON THE CHAPTER. The Sifrei on Deuteronomy has no section between piska 36 on 6:9 and piska 37 on 11:10 — chapters 7, 8, 9, 10 and 11:1-9 are
not expounded by position (the heads computed from the Hebrew's first rows; chapter 4 the earlier case). Its whole voice on chapter 7 is three rows from
elsewhere, found by the union of both files' citations: 37:1 (the English translator's own "(Dt.7:12)" for the portion's opening, with his note that the verse
is not expounded — an interpolation, read and marked), 50:4 on 11:23 (even one of the seven nations greater than all Israel — 7:1's count read), 61:7 on 12:3
(7:26's doubled verbs the rule of renaming the shrines for the worse). The chapter's kin — the angel's clauses (Exodus 23:20-33), the renewed covenant (34:11-16),
the dispossession (Numbers 33:50-56) — were read by position at the Exodus and Numbers sittings and are credited by name, the counts computed from those ledgers.
{L_ALL} sources, coverage computed; the twenty-six Onkelos rows whole.

7:1 COUNTS ITS OWN LIST. The engine's parser reads "seven nations" as [7], and the verse carries its own witness: seven gentilic tokens beside the numeral
(the Hittite, the Girgashite, the Amorite, the Canaanite, the Perizzite, the Hivite, the Jebusite — the morphology's Ng tag). Over the Bible the seven-name
lists are three (7:1; Joshua 3:10, 24:11) and the six-name lists eleven (Exodus 3:8, 3:17, 23:23, 33:2, 34:11; 20:17; Joshua 9:1, 11:3, 12:8; Judges 3:5;
Nehemiah 9:8) — none of them counts; 7:1 alone does. The seventh is the Girgashite, absent from every Exodus list and from 20:17 (seven seats: Genesis 10:16,
15:21; 7:1; Joshua's two; Nehemiah 9:8; 1 Chronicles 1:14). The same re-declaration runs through the chapter's kin: both directions of marriage barred where
Exodus 34:16 barred one (no token shared); four objects to destroy where 34:13 had three (the images added); "you shall not covet" moved to the idols' silver
and gold. Beside it the second number verse, 7:9 "to a thousand generations" [1000] — the ten words' "to thousands" (Exodus 20:6, 5:10, 34:7) the bare plural,
no number; Onkelos makes 7:9 the plural too ("to thousands of generations" — 5:10 and 7:9 alone).

THE OATH'S NOUN STARRED. "The oath which He swore to your fathers" (7:8): the parser stars the noun as the seven-stem homograph and reads the verb "swore" as no
number — the noun's ten Torah seats (Genesis 26:3; Exodus 22:10 "the oath of the LORD"; Leviticus 5:4; Numbers 5:21, 30:3, 11, 14; Genesis 24:8); Onkelos makes
noun and verb both the covenant's word ("the covenant which He established"). No gap: the chapter's two numbers are the two the parser reads.

THE WRITTEN/READ PAIR AT 7:9. The snapshot store carries seventeen tokens where the DB carries sixteen: "His commandments" written without the yod (the DB's
one written-marked token in the chapter, of 1,268 over the Bible) AND read with it — the chapter's one mismatch, the same written form as 5:10's (there the read
form is Exodus 20:6's "MY commandments"). Asserted as the exact difference; no claim's check uses the word (the check at 7:9 sits on "the faithful", before the
store's extra token). Chapter 6's large letters were the store's other kind of difference (a dropped letter); this is an added token — the mismatch census
names both.

ONKELOS'S SUPPLIED DOCTRINE AT 7:10. "And repays those who hate Him to their face, to destroy them; He will not delay with him who hates Him" — twelve tokens —
becomes twenty-two in the Aramaic: "He repays those who hate Him THE GOOD THAT THEY DO BEFORE HIM IN THEIR LIFETIME, to destroy them; He does not delay THE
GOOD DEED of those who hate Him …" — the wicked paid for their good in this world so as to be destroyed in the next; six bracketed supplements in the English
(the chapter's seventeen over ten verses). The row's length computed; the doctrine the compile's cell (5b). The chapter's other renderings: "beloved" for
treasured (7:6, 14:2, 26:18), "desired" for set His love, "in exchange for" for "because" (7:12 — the noun "heel" read as a conjunction at five seats, the
portion Ekev named by it), "the miracles" for the trials (4:34, 7:19, 16:1), "His Shekhinah is among you" (6:15, 7:21 — the pair), "a thing distanced" for the
abomination (7:25, 24:4, 27:15), "detest … keep far" (7:26).

THE FLOCK'S YOUNG TAGGED A NAME. "The increase of your cattle and the young of your flock" (7:13; 28:4, 18, 51 the other seats): the DB's morphology tags the
flock's word a proper name (Np) at all four seats — the goddess's homograph (the same consonants as the name at Judges 2:13 and 1 Samuel 7:3); the store's
gloss is the goddess too. A note for the DB, recorded and not resolved: the display layer rewrites the gloss ("and-the-young-of"), the parser is unaffected
(no number on the word), and no cell reads the tag.

"YOU SHALL NOT COVET" ON THE IDOLS' SILVER AND GOLD. 7:25 and Exodus 20:17 are the two seats of the phrase in this form (5:21 "and you shall not covet"); the
tenth word's verb moved from the neighbor's house to the images' silver and gold, with "and take it for yourself" — Achan's "I coveted them and took them"
(Joshua 7:21) the run's own case, Zechariah 6:11 the other "silver and gold … take". The compile's cell calls 3b's coveting cell (5b's box (l)); Mishnah
Avodah Zarah 3:5 on this verse was graded at the Exodus 34 sitting and is credited.

THE STORE'S GLOSSES READ BACK (the display layer): 49 rows by gloss and {OV_REF7} by reference — "seclude" BAN, "try" CHOOSE, "wealth" TREASURE,
"the-something-sworn" THE OATH, "the-build-up" THE FAITHFUL, "fetus" THE INCREASE OF, the goddess's name AND THE YOUNG OF, "the-wasp" THE HORNET, "the-testing"
THE TRIALS, "physical--a-net" DEVOTED, "be-filthy" DETEST, "something-disgusting" ABOMINATION, "heel" BECAUSE (by reference at 7:12), "?" made "I" at 7:11,
"strength" GOD and "nose" ANGER; by_ref {OV_REF}, by_gloss {OV_GL} after.
'''

STEPS = f'''DEUTERONOMY — SITTING 5 — CHAPTER 7, Deuteronomy 7:1-26 ({DATE}, on Brian's "Go" after chapter 6's commit, then "go for run 2", "run 3 go" and "4 go" for
the runs; World/step9/DEUTERONOMY_WALK.md "Sitting 5" and "Sitting 5 — AS BUILT").
The chapter of the seven nations. The Sifrei has no section here — nothing between the Shema's last verse and 11:10 — so the shelf's whole voice on the chapter
is three rows quoted from elsewhere, one of them the translator's own aside about where the next portion begins; the chapter's kin in Exodus 23 and 34 and
Numbers 33 had been read at their own sittings and are credited by name. The sitting ran as four runs with a stopping point after each, every row read whole.
What the reading found: the verse that names the seven nations also counts them, and our parser reads the count with the verse's own seven names as its
witness — seven where Exodus had six; the chapter re-says the old code for the new place in several ways (both directions of marriage barred, four things to
destroy instead of three, "you shall not covet" aimed at the idols' silver and gold); our text store carries one extra token at 7:9 where a word is written one
way and read another; Onkelos doubles 7:10 into a teaching about the wicked being paid in this world; and our word table tags "the young of your flock" as a
goddess's name — a note for the table, not for the code. The chapter is frozen as one unit, the 221st, the world's standing facts up by six as predicted, its
hash unmoved, every gate green. Next: the commit on your word; then the compile of chapter 7 in four runs — the ban, no covenant, no marriage, the altars, the
chosen people, the blessings, do not fear, little by little, the idols' silver and gold — or the ten-commandments schema first.

'''
BRIEF = f'''- **CHAPTER 7 READ AND FROZEN — THE SEVEN NATIONS: THE SIFREI IS SILENT ON THE CHAPTER, THE VERSE COUNTS ITS OWN LIST, AND THE OLD CODE IS SAID AGAIN FOR THE NEW PLACE** ({DATE}, on your "Go" and the runs' "go for run 2", "run 3 go", "4 go" — four runs, every row whole; World/step9/DEUTERONOMY_WALK.md "Sitting 5"): Onkelos on all 26 verses and the Sifrei's three rows from elsewhere — {L_ALL} sources, coverage computed, the kin's spine credited by name; "seven nations" counted by the verse's own seven names, seven where Exodus had six; both directions of marriage, four objects, "you shall not covet" on the idols' silver and gold; one extra token in our store at 7:9 (written one way, read another); Onkelos's doctrine at 7:10; the flock's young tagged a goddess's name in our word table; one unit frozen (the {C_UNITS}st), {N_CLAIMS} claims verified, the ritual {N_PASS} PASS, standing facts 2209 (+6 as predicted), hash unmoved, every gate green. NEXT: the commit on your word; then the compile of chapter 7 in four runs, or the schema sitting first.
'''
BRIEF_ENTRY = f'''### {DATE} — CHAPTER 7 READ: THE SEVEN NATIONS, AND A CHAPTER THE SHELF DOES NOT EXPOUND

The chapter that names the seven nations and gives the rules for the land they hold: destroy them, no treaty, no marriage either way, tear down their altars;
you were chosen for love and for the oath, not for size; keep the covenant and it will go well; do not fear them; burn their images and do not covet the silver
and gold on them. Two things stand out. The first is the shelf: the Sifrei, which had six sections on the Shema, has none at all here — nothing between the end
of chapter 6 and the middle of chapter 11 — so what the tradition says about this chapter by position is three rows quoted from other places, and one of those
is the translator's own note about where the next weekly portion starts. The chapter's real kin — the angel's promise in Exodus 23, the renewed covenant in
Exodus 34, the order to dispossess in Numbers 33 — had been read at their own sittings, so they are credited by name with the counts taken from those ledgers.
The second is what the chapter does to that kin: it says the old code again for the new place. The Exodus lists have six nations; this one has seven and
counts them, and our parser reads the count with the seven names as its witness. Exodus barred taking their daughters; this bars both directions. Exodus named
three things to destroy; this names four. The tenth commandment's verb, "you shall not covet", is aimed here at the silver and gold on the idols. That pattern
is part of what we have on the table as the "install" reading of Deuteronomy — recorded, not ruled. Two small finds for the machine: our text store carries an
extra token at 7:9 where the word is written one way and read another, and our word table tags "the young of your flock" as a goddess's name — both noted, not
acted on. The chapter is frozen as one unit, the 221st, every gate green.

'''
RESUME_NOTE = f'''# ⚠ THE DEUTERONOMY WALK sitting 5 ({DATE}; step9/DEUTERONOMY_WALK.md "Sitting 5" + "Sitting 5 — AS BUILT"): CHAPTER 7 READ AND FROZEN as one
# unit (the {C_UNITS}st — {UID} 7:1-26, the portion's edge at 7:12 inside it), FOUR RUNS with a clean point after each, every row whole: THE SIFREI
# SILENT ON THE CHAPTER (three rows from elsewhere, one an interpolation) + Onkelos whole + the kin's spine credited by name — {L_ALL} sources, coverage
# computed; 7:1 counts its own list (seven where Exodus had six); the oath's noun starred; the written/read pair at 7:9; Onkelos's supplied doctrine at
# 7:10; the flock's young tagged a name; "you shall not covet" on the idols' silver and gold; the ritual {N_PASS} PASS, CORPUS TRUTH GREEN ({C_UNITS} units,
# standing 2209 = 2203 + 6, hash unmoved), build_world, the journal gate ({J_KINDS} kinds, {J_ROWS} rows), the register gate --strict (DECLARED {R_DECL}, DEBT {R_DEBT},
# FAILS {R_FAIL}) GREEN; the tape unmoved since 4b. THE INSTALL HYPOTHESIS on the table (the map's tail). NEXT on the ruling: the commit; then 5b — the compile of
# chapter 7 in four runs, or the schema sitting first.
'''
STATE = f'''
#194 ADDENDUM 3 ({DATE}, at the close of THE DEUTERONOMY WALK sitting 5 — CHAPTER 7's READING, RUN 4 of four — A CLEAN COMPACTION POINT): THE STATE: chapter 7 read and frozen as one unit ({UID}, the {C_UNITS}st); the corpus {C_UNITS} units, standing 2209 (2203 + 6 as predicted), hash 8b8fff1fa28953af unmoved; the tape unmoved since 4b (RUN (1304, 96, 88, 0, 12, 1595, 37, 319, the four pairs, 127), markers 167, closes 127); the ledger deu_07_vaetchanan_ekev_{LDATE}.md ({L_ALL} sources, {L_BYTES:,} bytes, lint 0); the manifest {N_CLAIMS} claims verified; the display layer +{OV_REF7} / +49 (by_ref {OV_REF}, by_gloss {OV_GL}). THE GATES: the ritual {N_PASS} PASS; CORPUS TRUTH GREEN twice; build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL}); the home-path gate GREEN; the labels census GREEN ({LN}); large_letter_probes {LL}. THE RECORDS (write_ch7_records.py from the sheet, one call): the map's "Sitting 5 — CHAPTER 7 — AS BUILT" (thirteen lessons gathered from the three runs), COMPILE_DEBT's 5b box (a)-(p), MIDDOT's block (the Sifrei's two rows by E10 and the interpolation), RESEARCH_LOG's entry, THE_STEPS, THE_BRIEFING (the scoreboard and an entry), RESUME, the recovery page rewritten whole (section 2 to this close; under 10,240 bytes), the addenda's §41, the stamp row, the memory (the walk note and the index line under 17,000 bytes); the forms copied (copy_ch7_forms.py). THE FOUR-RUN RULE'S SECOND READING SITTING: run 1 closed at #194 (the compaction), run 2 at addendum 1, run 3 at addendum 2, run 4 here — the owner compacted once and said "reread", "go for run 2", "run 3 go", "4 go"; every run's checkpoint named the next run's first step. ALSO IN THE TREE: the design thread's ARCHITECTURE/THE_BOOKS_AS_A_PROGRAM.md (new) and README.md section, on the owner's word (its message of this date) — not this thread's work; ARCHITECTURE rides the commit. NOT COMMITTED: the whole sitting since 64a8362 — the commit message drafted at <scratch>/commit_msg_ch7.txt for his word ("commit" = no push; "commit push" = both). NEXT ON THE RULING: the commit; then 5b — THE COMPILE OF CHAPTER 7 in four runs (the design first, in the map; the debt box (a)-(p) its list; the run citations as the readback's reference rows) — or the Decalogue-schema sitting first, on his word; THE INSTALL HYPOTHESIS on the table beside it. IF THIS COMPACTS HERE: reread the recovery page, the map's "Sitting 5 — CHAPTER 7 — AS BUILT" (NEXT and the lessons) and "THE INSTALL HYPOTHESIS", MEMORY.md — nothing else unasked; THE_STEPS Step 5 + the compiler block before 5b's design.
'''
ADDENDA = f'''
## 41. ADDENDUM ({DATE}, THE DEUTERONOMY WALK sitting 5 — CHAPTER 7, Deuteronomy 7:1-26 READ AND FROZEN in four runs, every row whole; the owner: "Go", "go for run 2", "run 3 go", "4 go"; the state doc's #194 and its addenda 1-3)
THE STATE: chapter 7 read and frozen as one unit ({UID}, the {C_UNITS}st); the corpus {C_UNITS} units, standing 2209 (2203 + 6 as predicted), hash
8b8fff1fa28953af unmoved; the tape UNMOVED since 4b (RUN (1304, 96, 88, 0, 12, 1595, 37, 319, the four pairs, 127), markers 167, closes 127); the
journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL}); uncommitted since 64a8362.
WHAT THE SITTING FOUND: the Sifrei SILENT on the chapter (no piska between 36 on 6:9 and 37 on 11:10) — three rows from elsewhere its whole voice, 37:1 the
translator's interpolation; the kin's spine credited by name with the counts computed; 7:1 COUNTS ITS OWN LIST — the parser's [7] with seven gentilic tokens
as the witness, SEVEN WHERE EXODUS HAD SIX (the Girgashite); both directions of marriage, four objects, "you shall not covet" on the idols' silver and gold —
the old code re-said for the new place (THE INSTALL HYPOTHESIS on the table, the map's tail); the oath's noun starred; THE WRITTEN/READ PAIR at 7:9 (the
store's extra token, 5:10's kin); "to a thousand generations" [1000] against the ten words' bare plural; Onkelos's SUPPLIED DOCTRINE at 7:10; "because" the
heel at 7:12, the portion's edge inside the chapter; THE FLOCK'S YOUNG TAGGED A NAME in the morph; the hornet's three seats; little by little's two.
THE FOUR-RUN RULE'S SECOND READING SITTING: the runs' edges held; the reread after the one compaction three files; the forms of run 3 held first time.
THE FILES CHANGED: logic/oral_triage/deu_07_vaetchanan_ekev_{LDATE}.md (new); logic/units/{UID}.yaml (draft → frozen, six operators, step E, the
scenarios in the anchor form) and logic/py_units/{UID}.py; logic/oral_audit/manifests/{UID}_claims.json (new); logic/glosses/word_gloss_overrides.yaml
(+{OV_REF7} by reference, +49 by gloss); logic/corpus/CORPUS_TRUTH.py ({C_UNITS}, 2209) and corpus_world.sqlite; the records (the map, COMPILE_DEBT, MIDDOT, RESEARCH_LOG,
THE_STEPS, THE_BRIEFING, RESUME, the state doc, the recovery page, this file, STAMP_LEDGER, the memory); World/step9/forms_deuteronomy_walk/ (the sitting's
scripts and prints); ARCHITECTURE/DEUTERONOMY_SO_FAR.md + epub (the tutorial on the owner's word, run 1); the design thread's ARCHITECTURE files (its own).
NEXT ON THE RULING: the commit; then the compile of chapter 7 (5b) in four runs — or the Decalogue-schema sitting first — on the owner's word.
'''
MEMPAR = f'''
SITTING 5 DONE {DATE} (the owner: "Go", "go for run 2", "run 3 go", "4 go"; the map's "Sitting 5" and "Sitting 5 — AS BUILT"): CHAPTER 7 READ AND FROZEN as one
unit ({UID}, the {C_UNITS}st) — the second reading sitting under THE FOUR-RUN RULE, every row whole (four clean points: #194, its addenda 1-3; the owner
compacted once). The Sifrei SILENT on the chapter (three rows from elsewhere, 37:1 an interpolation); the kin's spine credited by name; 7:1 counts its own
list — seven where Exodus had six; both directions of marriage, four objects, "you shall not covet" on the idols' silver and gold (the install hypothesis's
seventh exhibit, on the table); the oath's noun starred; the written/read pair at 7:9; Onkelos's supplied doctrine at 7:10; the flock's young tagged a name
in the morph. Every gate green; the corpus {C_UNITS} / 2209 / hash unmoved; the tape unmoved. ⚠ LESSONS (thirteen in the map): a chapter without a spine reads
its kin's by credit and has a ledger without a spine section; a number verse can carry its own witness; the written/read pair is the store's extra token;
the forms held first time — a reading's run 3 is a form; the fold layer grows with a freeze while the tape stands. OWED TO 5b (COMPILE_DEBT's box (a)-(p)):
the ban, no covenant and no favor, no marriage, the altars and the Asherim, the chosen people, the faithful God and the hater repaid, because you hear and
the blessings, no pity and no serving, do not fear, little by little by CALL, the idols' silver and gold with the tenth word's cell, the abomination into the
house, the run citations, the docket. NOT COMMITTED (since 64a8362; the message drafted at <scratch>/commit_msg_ch7.txt). NEXT on the ruling: the commit;
then 5b in four runs, or the schema sitting, on the owner's word.
'''
MEMLINE_OLD_START = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — '
MEMLINE_NEW = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — map World/step9/DEUTERONOMY_WALK.md; chapters 1-6 COMPILED (64a8362 PUSHED); SITTING 5 DONE 2026-09-18 (ch 7 FROZEN, 221 units); the INSTALL hypothesis ON THE TABLE; NEXT: commit, then 5b\n'
DESC_OLD = 'SITTING 5 (chapter 7) RUNS 1-3 DONE 2026-09-18'
DESC_NEW = 'SITTING 5 DONE 2026-09-18 (chapter 7 READ AND FROZEN as one unit, the 221st; the Sifrei silent on the chapter; uncommitted)'
REC2_OLD_START = '## 2. WHERE IT STANDS'
REC2_NEW = f'''## 2. WHERE IT STANDS ({DATE}; the state doc #194 addendum 3)
- NUMBERS CLOSED. DEUTERONOMY 1:1-6:25 READ, FROZEN, COMPILED AND ON THE TAPE (64a8362 PUSHED); 7:1-26 READ AND FROZEN (sitting 5, four runs).
- {C_UNITS} frozen units, standing 2209, hash 8b8fff1fa28953af. 61 runners, 66 daemons, 454 functions; registries 1125 kinds / 1025 effects.
- THE TAPE unmoved since 4b (RUN (1304, 96, 88, 0, 12, 1595, 37, 319, the four pairs, 127); markers 167, closes 127); the sweep 61/61; every gate GREEN;
  the register gate DECLARED {R_DECL} / DEBT 0.
- CHAPTER 7'S FINDS: the Sifrei SILENT (three rows from elsewhere); 7:1 counts its list — seven where Exodus had six; the written/read pair at 7:9.
- Uncommitted since 64a8362: sitting 5 whole, the tutorial, the design thread's files; the message at <scratch>/commit_msg_ch7.txt.
- NEXT ON HIS WORD: the commit; then 5b — THE COMPILE OF CHAPTER 7 in four runs (the debt box; the design first), or the schema sitting.
'''

LINT = f'{ROOT}/logic/solo_tools/gloss_lint.py'
def lint(path):
    out = subprocess.run([sys.executable, LINT, path], capture_output=True, text=True).stdout
    m = re.search(r'gloss_lint: (\d+) flag', out); return int(m.group(1)) if m else -1
WALKP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; RECP = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
TOUCH = [f'{ROOT}/logic/findings/STAMP_LEDGER.md', f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', f'{ROOT}/World/RESUME.md', f'{ROOT}/THE_STEPS.md', f'{ROOT}/THE_BRIEFING.md', f'{ROOT}/World/step9/COMPILE_DEBT.md', f'{ROOT}/RESEARCH_LOG.md', f'{ROOT}/logic/MIDDOT.md', RECP, f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md', f'{MEM}/MEMORY.md']
# ---- THE ANCHORS, ASSERTED PRESENT ONCE BEFORE ANY WRITE ----
A_RESUME = '# ⚠ THE DEUTERONOMY WALK sitting 4b (2026-09-17;'
A_SCORE = '## SCOREBOARD (as of 2026-09-17, latest)\n'
A_BULLET = '- **CHAPTER 6 COMPILED — THE SHEMA\'S LAW GIVEN AT ITS OWN DAY FOR THE FIRST TIME, THE READBACK\'S THIRD FORM'
A_ENTRY = '### 2026-09-17 — CHAPTER 6 COMPILED: THE SHEMA GIVEN AT ITS OWN DAY, AND THE READBACK\'S THIRD FORM'
A_MIDDOT = '\n## Exodus block campaign — owner\'s word "Do 3")\n'
A_REC5 = 'the newest instances: the map\'s "Sitting 4" and "Sitting 4b"'
A_REC6 = '- Deuteronomy\'s sittings: the map; the addenda §31-40 (§39 the whole-row rule). The cost cuts: §35.'
ANCH = [(f'{ROOT}/World/RESUME.md', A_RESUME), (f'{ROOT}/THE_STEPS.md', '\n## Step 6 — Publish\n'), (f'{ROOT}/THE_BRIEFING.md', A_SCORE), (f'{ROOT}/THE_BRIEFING.md', A_BULLET), (f'{ROOT}/THE_BRIEFING.md', A_ENTRY), (f'{ROOT}/logic/MIDDOT.md', A_MIDDOT), (RECP, REC2_OLD_START), (RECP, '\n## 3. THE STANDING LAWS'), (RECP, A_REC5), (RECP, A_REC6), (f'{MEM}/MEMORY.md', MEMLINE_OLD_START), (f'{MEM}/deuteronomy-walk.md', DESC_OLD)]
for p, a in ANCH: assert rd(p).count(a) == 1, (p, a[:40], rd(p).count(a))
assert '## Sitting 5 — CHAPTER 7 — AS BUILT' not in rd(WALKP) and 'RUN 3 — AS RUN (2026-09-18' in rd(WALKP) and '#194 ADDENDUM 3' not in rd(TOUCH[1]) and '#194 ADDENDUM 2' in rd(TOUCH[1]) and '## 41. ADDENDUM' not in rd(TOUCH[9]) and 'SITTING 5 DONE' not in rd(f'{MEM}/deuteronomy-walk.md') and 'DEUTERONOMY SITTING 5 — CHAPTER 7' not in rd(TOUCH[5]) and f'| {UID} |' not in rd(TOUCH[0])
s = rd(RECP); i = s.index(REC2_OLD_START); j = s.index('\n## 3. THE STANDING LAWS'); REC_NEW = s[:i] + REC2_NEW + s[j:]
REC_NEW = REC_NEW.replace(A_REC5, 'the newest instances: the map\'s "Sitting 5" and "Sitting 4b"').replace(A_REC6, '- Deuteronomy\'s sittings: the map; the addenda §31-41 (§39 the whole-row rule). The cost cuts: §35.')
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
replace_once(TOUCH[4], A_SCORE, f'## SCOREBOARD (as of {DATE}, latest)\n')
insert_before(TOUCH[4], A_BULLET, BRIEF)
insert_before(TOUCH[4], A_ENTRY, BRIEF_ENTRY)
append(TOUCH[5], DEBT)
append(TOUCH[6], RESEARCH)
insert_before(TOUCH[7], A_MIDDOT, MIDDOT)
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
