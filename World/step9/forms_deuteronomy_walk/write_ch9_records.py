import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 7 — CHAPTER 9 (2026-09-19; the owner: "Let's keep run as it is and do another section" after THE GATES CUT — a READING
# sitting is ONE run under THE TWO-RUN RULE, every row whole under THE WHOLE-ROW RULE): THE RECORDS at the close, from the sheet World/step9/RECORD_FORMS.md
# in ONE call — the map's "Sitting 7 — CHAPTER 9 — AS BUILT", COMPILE_DEBT's box (owed to the compile 7b), MIDDOT's block (the Sifrei's rows that argue by a
# rule), MISHNAH_TOPICS' row notes (Fasts 4:6 and Idolatry 3:3 ROUTED to 7b), RESEARCH_LOG's entry, THE_STEPS' paragraph, THE_BRIEFING's bullet and entry,
# RESUME's note, the state doc's #197 addendum 1, the recovery page (section 2 rewritten, under 10 KB), the recovery addenda's section 46, the stamp row, the
# memory file and the index line (under 17,000 bytes), and the commit message's paragraph. Every number parsed from a print named beside it (--check prints
# them and writes nothing); every insert on a unique anchor asserted present once; the lints before and after. Sitting 6's form (write_ch8_records.py).
import os, re, subprocess, sys, yaml, json
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/' + os.path.abspath(ROOT).replace('/', '-') + '/memory')
DATE = '2026-09-19'; LDATE = '2026-09-19'
UID = 'deu_09_not_righteousness'
CHECK = '--check' in sys.argv
def rd(p): return open(p, encoding='utf-8').read()
# ---- THE NUMBERS, PARSED FROM THE PRINTS ----
truth = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py')
assert 'assert len(W["units"]) == 223' in truth and 'assert len(W["standing"]) == 2221' in truth and "8b8fff1fa28953af" in truth
CT = rd(f'{SP}/ch9_truth.out'); CB = rd(f'{SP}/ch9_bake.out'); C1 = rd(f'{SP}/ch9_fold_check1.out')
assert 'CORPUS TRUTH GREEN' in CT and 'CORPUS TRUTH GREEN' in C1 and 'wrote corpus_world.sqlite' in CB
rit = rd(f'{SP}/ch9_ritual_{UID}.out'); N_PASS = len(re.findall(r'^PASS', rit, re.M))
assert 'RITUAL COMPLETE' in rit and N_PASS == 13 and not re.search(r'^FAIL', rit, re.M), N_PASS
vt = rd(f'{SP}/ch9_vt_{UID}.out'); mvt = re.search(r'TEXT LAYER GREEN: (\d+) steps, (\d+) scenarios', vt); assert mvt and mvt.group(1) == '29', vt[-300:]
VT_STEPS, VT_SCEN = mvt.groups()
assert '  status: frozen' in rd(f'{ROOT}/logic/units/{UID}.yaml') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json') and 'ALL_DONE' in rd(f'{SP}/ch9_chain.log')
JG = rd(f'{SP}/ch9_journal.out'); RG = rd(f'{SP}/ch9_register.out'); BW = rd(f'{SP}/ch9_build.out'); GS = rd(f'{SP}/ch9_gates_SUMMARY.txt')
assert 'GATE GREEN' in JG and 'ALL GREEN' in BW and 'THE REGISTER GATE: GREEN' in RG and 'ALL GREEN' in GS, (JG[-200:], BW[-200:], GS[-200:])
mj = re.search(r'(\d+) kinds, ([\d,]+) rows', JG); J_KINDS, J_ROWS = mj.group(1), mj.group(2)
mr = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', RG); R_DECL, R_DEBT, R_FAIL = mr.groups()
assert R_DEBT == '0' and R_FAIL == '0', mr.groups()
mc = re.search(r'(\d+) units, (\d+) facts, (\d+) demands \((\d+) open\)', CT); C_UNITS, C_FACTS, C_DEM, C_OPEN = mc.groups()
assert C_UNITS == '223', C_UNITS
HG = rd(f'{SP}/ch9_home.out'); assert 'GREEN' in HG, HG[-200:]
LED = rd(f'{ROOT}/logic/oral_triage/deu_09_ekev_{LDATE}.md')
ml = re.search(r'\*\*read: (\d+) of \1 — COMPLETE\*\* \((\d+) Onkelos verses and (\d+) Sifrei rows.*?MATERIAL (\d+) Onkelos, CONTEXT (\d+) Onkelos, MATERIAL (\d+) Sifrei outside, CONTEXT (\d+) Sifrei outside', LED, re.S)
L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_XM, L_XC = ml.groups()
assert L_ALL == '36' and L_ONK == '29' and L_SIF == '7' and LED.count('⟨MISS⟩') == 0
L_BYTES = len(LED.encode())
d_ov = yaml.safe_load(rd(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'))
OV_REF9 = len([k for k in d_ov['by_ref'] if k.startswith('Deut.9.')]); OV_REF, OV_GL = len(d_ov['by_ref']), len(d_ov['by_gloss'])
assert OV_REF9 == 60 and OV_REF == 612 and OV_GL == 502, (OV_REF9, OV_REF, OV_GL)
N_CLAIMS = len(json.load(open(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json', encoding='utf-8'))); assert N_CLAIMS == 6
VC = rd(f'{SP}/ch9_vc.out'); assert 'SUMMARY: 6 verified, 0 failed, 0 uncheckable, 0 no-check' in VC
LAB = rd(f'{SP}/ch9_labels.out'); mlab = re.search(r'CLAIM LABELS CENSUS — (\d+) claims in (\d+) manifests; labeled \1; DEBT 0', LAB); LN = f'{int(mlab.group(1)):,} claims in {mlab.group(2)} manifests'; assert 'GATE PASSED' in LAB and re.search(r'deu\s+58 claims', LAB), LAB[-300:]
assert rd(f'{SP}/ch9_ink_run3.out').strip().endswith('0 failing statements') and rd(f'{SP}/ch9_ink_run2.out').strip().endswith('0 failing statements') and rd(f'{SP}/ch9_ink_run1.out').strip().startswith('18 failing statements')
N_INK = len(re.findall(r'^assert ', rd(f'{SP}/ch9_ink.py'), re.M))
LL = rd(f'{SP}/ch9_large_letter.out').strip().split('\n')[-1]; assert LL.endswith('6/6'), LL
JR8 = re.search(r'12 kinds, (\d+) rows', rd(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch8_journal.out')).group(1); DJ = int(J_ROWS.replace(',', '')) - int(JR8)
MAN = rd(f'{SP}/ch9_manifest.out'); assert 'every CITE INDEX name used by a claim: True' in MAN
DUMP = rd(f'{SP}/ch9_dump0.out'); assert 'DB verses 29 | export verses HE 29 EN 29' in DUMP and 'the union of rows (both files): 7' in DUMP
print('PARSED:', dict(ritual_pass=N_PASS, verify_text=(VT_STEPS, VT_SCEN), journal=(J_KINDS, J_ROWS, DJ), register=(R_DECL, R_DEBT, R_FAIL), corpus=(C_UNITS, C_FACTS, C_DEM, C_OPEN), ledger=(L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_XM, L_XC, L_BYTES), overrides=(OV_REF9, OV_REF, OV_GL), claims=N_CLAIMS, labels=LN, ink_asserts=N_INK))
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

STAMP = (f'| {DATE} | {UID} | DELEGATED | FULL RULE | Deuteronomy 9:1-29 derivation {LDATE} (THE DEUTERONOMY WALK sitting 7 — CHAPTER 9; the owner: "Let\'s keep run as it is and do another section" after THE GATES CUT — a reading sitting ONE run, every row whole): Onkelos Deuteronomy 9 whole (29 = 29, the identity) + the Sifrei on Deuteronomy SILENT on the chapter, its {L_SIF} rows outside any piska read whole in both files (four reread) + the kin credited by name; the ledger deu_09_ekev_{LDATE}.md ({L_ALL} sources, coverage computed, lint 0); {N_CLAIMS} claims DV09-01..06 verified 6/0, seated as six WITNESS_READ at 9:1, 7, 12, 15, 22, 25; the ritual {N_PASS} PASS; CORPUS TRUTH GREEN ({C_UNITS} units, standing 2221, hash unmoved); the fold layer +{DJ}; the display layer +{OV_REF9} by reference, +36 by gloss | {LN}, labeled, debt 0 |\n')

WALK = f'''


## Sitting 7 — CHAPTER 9 — AS BUILT ({DATE}; the design above stands as written — the one run ran as designed; every departure from it is named here)

THE RESULT: Deuteronomy 9:1-29 READ, FROZEN and SEATED as ONE unit — deu_09_not_righteousness (the 223rd frozen unit; 29 of 29 verses, missing 0, computed): the
ledger logic/oral_triage/deu_09_ekev_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the Sifrei\'s outside rows {L_SIF}: MATERIAL {L_XM} / CONTEXT
{L_XC}; {L_BYTES:,} bytes, lint 0, no cut missed), the manifest {N_CLAIMS} claims DV09-01..06 verified 6/0 (every he_contains cut from the store\'s own bytes; every cite
index name used by a claim), seated as six WITNESS_READ operators at 9:1, 7, 12, 15, 22, 25 with step E; the ritual {N_PASS} PASS; verify_text GREEN ({VT_STEPS} steps,
{VT_SCEN} scenarios); the fold predicted and matched (units 222 → 223, standing 2215 → 2221, the hash 8b8fff1fa28953af unmoved — CORPUS TRUTH GREEN before and after
the bake: {C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, {C_OPEN} open); build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer since
chapter 8\'s reading, the tape unmoved); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — no receipt form in the chapter); large_letter_probes {LL[-3:]};
the labels census GREEN ({LN}, Deuteronomy 58); the home-path gate GREEN; the display layer +{OV_REF9} by reference and +36 by gloss ({OV_REF} / {OV_GL} in all).

THE READING: every Onkelos row whole in the Aramaic and the English (ch9_onkelos.txt); every one of the seven outside rows whole in both files (ch9_sifrei_outside.txt),
the four read at sitting 1 reread whole; the kin (Exodus 24:12-18, 31:18, 32, 34:1-4 and 28; Numbers 11:1-3 and 31-35, 13-14, 20:24) credited by name with the counts
computed from those ledgers (the calf 8, the ascent 2, the second tablets 1, the craftsmen 1; Taberah and Kibroth 8, the spies 33, the rejection 45, Meribah 1);
Massah\'s first telling (Exodus 17:1-7) holds no Onkelos row in any ledger — read through the Mekhilta at its sitting (computed).

THE DEPARTURES FROM THE DESIGN: none in substance. THE INK\'S FIRST PASS FELL EIGHTEEN WAYS ON FORMS (thirteen retyped from the print, none a fact): the shelf\'s own
spellings of "hyperbole" (הביי, "hyperbole") and "light and heavy" (וחמר, "and heavy") on its bytes; the Name\'s count thirty-four (typed thirty-three); a
single shared token where the summary had written none (9:17 against Exodus 32:19 one, 9:19 against 32:14 one, 9:20 against 32:21 one, 9:28 against 32:12 two);
"fortified" plene at 1:28 against defective at 9:1 (the phrase census split by the spelling); "who passes over" with the article at 9:3 alone; three phrase
searches typed as one where the shelf has two forms (the uprightness of heart, Kibroth\'s two spellings, "rebelled against the mouth"). THE SEAT SCRIPT\'S SPEC fell
once on a form (the fifth element, the draft\'s description, dropped in the derivation — the chain stopped at the seat, the draft untouched; retyped, rerun).

THE GATES, COMPUTED FROM THEIR PRINTS: the ritual {N_PASS} PASS (RITUAL COMPLETE, {C_UNITS} frozen units); CORPUS TRUTH GREEN twice ({C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, {C_OPEN} open;
the hash unmoved); build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows, +{DJ}); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL});
verify_claims 6 verified / 0 failed; the labels census GREEN ({LN}); large_letter_probes {LL[-3:]}; the home-path gate GREEN; the ink {N_INK} asserts — 18 failing on the first
typed pass, 0 on the second and third (the third after the display patch).

⚠ THE LESSONS (the run\'s, gathered — the numbered list the sheet asks for): (1) A RETELLING OF NARRATIVE HAS ITS CLOSEST ROW WHERE GOD SPEAKS — 9:13 eleven of thirteen
tokens with Exodus 32:9, Moses\' own acts retold in his own words (9:17 one token with 32:19). (2) AN ACT TOLD ONLY IN THE RETELLING — Aaron\'s peril and the prayer for
him (9:20) — is the compile\'s retrograde question, found at the reading by the diff. (3) THE SHELF\'S BYTES SPELL THEIR OWN WORDS — "hyperbole" and "light and heavy"
as the export writes them, never as typed from memory. (4) A SUMMARIZER THAT COUNTS RUNS MISSES SINGLE TOKENS — the kin summary wrote "nothing shared" where one
token is; the ink\'s counter is the measure, retyped from the print. (5) A SPELLING SPLITS A CENSUS — 1:28\'s plene "fortified" against 9:1\'s defective; the phrase
found at one seat until both spellings were asked. (6) THREE VOICES ON ONE PRONOUN — the second person singular is Israel\'s, then God\'s to Moses, then Moses\' to
God; the morphology counts them one. (7) THE ENGLISH SIFREI MIS-CITES AGAIN — 306:25\'s "Ex.36:28" for 34:28 (chapter 6\'s lesson a second time); the Hebrew right,
the row kept. (8) A DERIVED SCRIPT\'S TUPLE IS RETYPED WHOLE — the seat spec\'s fifth element dropped; the chain stopped at the first step and touched nothing.
(9) THE KIN\'S CREDITS ARE COUNTED, NOT TYPED — the eight ledgers\' counts computed by kinrows; a kin without an Onkelos row (Massah) named as such. (10) THE
READING SITTING HELD IN ONE RUN under the two-run rule, the fourth in a row.

THE FORMS: World/step9/forms_deuteronomy_walk/ (copy_ch9_forms.py — derive_ch9_dump0.py, ch9_dump0.py, derive_ch9_measure1.py, ch9_measure1_sections.py,
ch9_measure1.py, ch9_ink.py, ch9_ink_diag.py, ch9_rows_onkelos_a.py, ch9_rows_onkelos_b.py, ch9_rows_outside.py, write_ch9_ledger.py, ch9_patch_overrides.py,
write_ch9_manifest.py, seat_ch9.py, write_ch9_design.py, write_ch9_records.py, ch9_chain.sh, ch9_fold.sh, ch9_gates.sh and the prints).

NEXT on the ruling: the commit on the owner\'s word (chapter 8, the gates cut and this sitting stand uncommitted since 29c189b); then THE COMPILE OF CHAPTER 9
(sitting 7b) in TWO RUNS — RUN A: the rereads (THE_STEPS Step 5 + the compiler block; this section; the 7b box in COMPILE_DEBT), the measurements (the calf\'s
lines in the kitisa, ascent, second-tablets and craftsmen runners; the four provocations\' lines; the checkpoint prefix space — A NEW SERIES, the probes\' regexes
measured before a name is typed), THE DESIGN, the probes to FAIL, THE DOCKET by the union rule (Berakhot 32a, Shabbat 87a-89a, Ta\'anit 4:6 and 28b, Avodah Zarah
43b-44a, Menachot 99a-b, Bava Batra 14b, Sanhedrin 102a, Beitzah 25b, Shabbat 55a — every row whole); RUN B: the types, the runner, the tape to 10/10, the chain,
the records, the forms, the commit message — or the Decalogue-schema sitting first, on his word.
'''

DEBT = f'''

## SITTING 7 — CHAPTER 9 ({DATE}, the reading; deu_09_not_righteousness frozen) — OWED TO THE COMPILE 7b: (a) THE READBACK\'S ROWS OF THE CALF — 9:8-21 and 9:25-29
## against the kitisa runner\'s lines (the calf made, God\'s word to go down, the offer, the prayer, the tablets broken, the calf burned), the ascent\'s (Exodus
## 24:12-18), the second tablets\' (34:1-4, 28) and the craftsmen\'s (31:18): 9:13 VERBATIM (eleven of thirteen tokens with Exodus 32:9), 9:12 VARIANT, 9:9 and 9:18
## VARIANT (the forty days), 9:21 VARIANT (the calf ground), 9:17 EXPANDED in Moses\' own words, 9:19 TURNED (the relenting as "hearkened"); (b) AARON\'S PERIL (9:20)
## — an act told ONLY in the retelling: the LORD\'s anger at Aaron and Moses\' prayer for him — the RETROGRADE WRITE at Exodus 32\'s own day, the design question
## (the milluim and investiture ledgers read his re-acceptance from this verse); (c) THE STATE "stiff-necked" (9:6, 9:13) — Exodus 32:9\'s line measured: a status on
## Israel or nothing on the tape; the six Bible seats all the calf\'s; (d) THE THREE FORTIES — the tradition\'s three ascents (Exodus 24:18; 32:30-34:9; 34:28) against
## the tape\'s lines and DATES: Ta\'anit 4:6 the tablets broken on the seventeenth of Tammuz (THE ANSWER SHEET\'S DATE for 9:17), Ta\'anit 28b and Shabbat 87a-88a the
## forty-day arithmetic from 7 Sivan to 10 Tishri — the clock\'s test; the Sifrei 14:1 and 306:25 read 9:9 with 34:28; (e) THE FOUR PROVOCATIONS (9:22-23) — run
## citations of Numbers 11:1-3, Exodus 17:1-7, Numbers 11:31-34 and 13-14, out of the tape\'s order; (f) THE INTERCESSION\'S SECOND TELLING (9:26-29) against Exodus
## 32:11-13 and Numbers 14:13-19 — the same argument twice on the tape (Israel/Jacob, the Egyptians/the land, the mountains/the wilderness); Solomon (1 Kings 8:51)
## and Nehemiah (1:10) quoting THIS telling — the run, outside the Torah; (g) THE OFFER\'S THREE FORMS (Exodus 32:10, Numbers 14:12, 9:14) a DATA row; (h) THE THREE
## SPELLINGS OF "TABLETS" and the Bible\'s three "tablets of the covenant" a DATA row; (i) THE CHECKPOINT PREFIX SPACE — 7b OPENS A NEW SERIES (CU the last two-letter
## prefix): the probes\' 'C[A-Z]' regexes (the recon\'s finder, checkpoint_positions.py, checkpoint_probes.py, cold_run_sequence\'s VERDICTS list) MEASURED at the
## design before a name is typed; (j) THE DOCKET by the union rule — Berakhot 32a and 7a (the prayer), Shabbat 87a-89a (the breaking approved; the forty days),
## Menachot 99a-b and Bava Batra 14b (the broken tablets in the ark), Ta\'anit 4:6 and 28b, Avodah Zarah 43b-44a with Mishnah Avodah Zarah 3:3 (the calf\'s
## destruction the idol\'s), Sanhedrin 102a and Vayikra Rabbah 10:5 (Aaron), Beitzah 25b (the stiff neck), Shabbat 55a (the merit of the fathers), Devarim Rabbah 2:1
## (the ten names of prayer) — EVERY ROW WHOLE; a docket past ~700 rows its own run. NOTHING ELSE IN CHAPTER 9 IS OWED TO A LATER SITTING OF ITS OWN.
'''

MIDDOT = f'''- **THE SIFREI ON DEUTERONOMY\'S OWN CASE LAW ON CHAPTER 9 (Deuteronomy 9:1-29; THE DEUTERONOMY WALK sitting 7, {DATE};
  the ledger logic/oral_triage/deu_09_ekev_{LDATE}.md — THE SPINE SILENT ON THE CHAPTER, no piska head between 36 on 6:9 and 37 on
  11:10; its seven rows outside any piska read whole in both files, the rows that argue by a numbered rule below, each at its row):**
  · THE ONE FOR THE MANY, THE MANY FOR THE ONE (27:2 on 3:24 from 9:14): "let Me alone and I will destroy them" — the door God opened
    for Moses to stand and pray; the prayer of one for the many heard, so the prayer of the many for one all the more — I1 (qal
    wa-chomer, the a-fortiori; the row\'s own words "קל וחמר" ("light and heavy") on its bytes); THE INK: "let Me alone" the Bible\'s one
    seat of the form (Exodus 32:10\'s "let Me be" another verb); Onkelos supplies the prayer in the clause ("leave your prayer from
    before Me") at both tellings; 9:19\'s "the LORD hearkened to me" the prayer heard.
  · BEFORE YOUR EYES, BEFORE THE EYES OF ALL ISRAEL (357:44 on 34:12 from 9:17): "it is said there: and I broke them BEFORE YOUR EYES;
    and here it says: which Moses did BEFORE THE EYES OF ALL ISRAEL" — the breaking of the tablets counted among Moses\' wonders by the
    shared phrase — I2 (gezerah shavah, the verbal analogy; the row\'s own form "נאמר להלן … וכאן הוא אומר" ("it is said there … and
    here it says")); THE INK: "before your eyes" 1:30, 9:17, 29:1 in the book; 9:17 shares one token with Exodus 32:19 — the breaking
    retold in Moses\' own words; 34:12 the book\'s last verse.
  · THE SCRIPTURES SPEAK IN HYPERBOLE (25:4 on 1:28 from 9:1): "cities great and fortified to the heavens" — Rabban Shimon ben Gamliel\'s
    rule that Scripture exaggerates, 9:1 the proof, and the promise to Abraham of the stars and the dust the exception — a rule of
    reading, not a numbered middah (E10 the nearest label: the expression read for what it signifies); THE INK: the phrase\'s two seats
    spelled plene there and defective here; Onkelos "to the height of heaven" at both.
  · THE TEN NAMES OF PRAYER (26:7 on 3:23 from 9:25-26): "falling" (9:25) and "prayer" (9:26) two of the ten, "imploring" (Exodus 32:11)
    the same prayer\'s first telling — E10 (the words\' seats gathered); THE INK: "fell down before the LORD" the hithpael\'s two Torah
    seats both this chapter\'s; "I prayed" 9:20, 9:26 among the Torah\'s eight.
  · THE FORTY DAYS AS SUFFERING (14:1 on 1:14 and 306:25 on 32:2 from 9:9): "I stayed on the mountain forty days and forty nights"
    read beside Exodus 34:28 as the price Moses paid for the Torah — E10; THE INK: the phrase\'s nine Bible seats, four in the chapter;
    the English\'s "Ex.36:28" at 306:25 a slip for the Hebrew\'s 34:28 (asserted on both files\' bytes).
  · THE HARSH WORDS FIRST (342:1 on 33:1 from 9:7-8): "at Horeb you provoked the LORD", "you have been rebellious" among the hard words
    before the blessing — a reading of order, no rule (the range citation "9:7-8" in the Hebrew\'s form, found through the English).
'''

RESEARCH = f'''

## {DATE} — DEUTERONOMY 9 READ AND FROZEN (THE DEUTERONOMY WALK sitting 7, one run): THE CALF RETOLD IN MOSES\' FIRST PERSON — GOD\'S WORD VERBATIM, MOSES\' ACTS
## IN HIS OWN WORDS, AARON\'S PERIL TOLD ONLY HERE; STIFF-NECKED SIX SEATS ALL THE CALF\'S; THREE SPELLINGS OF "TABLETS"; THE FORTY DAYS FOUR TIMES; THE PRAYER\'S SECOND
## TELLING QUOTED BY SOLOMON AND NEHEMIAH
On the owner\'s "Let\'s keep run as it is and do another section" after THE GATES CUT. THE READING: Deuteronomy 9:1-29 with Onkelos whole (the export\'s 29 rows the DB\'s
29 — the identity, asserted) and the Sifrei on Deuteronomy SILENT ON THE CHAPTER (36 on 6:9, 37 on 11:10 — chapters 7-10 without a section), its whole voice
seven rows from elsewhere found by the union of both files\' citations and read whole (14:1 and 306:25 the forty days as suffering, with Exodus 34:28; 25:4 the
hyperbole rule; 26:7 the ten names of prayer; 27:2 the door opened — I1; 342:1 the harsh words, the Hebrew\'s range form; 357:44 the breaking among the wonders —
I2); four reread whole from sitting 1. FROZEN as ONE unit deu_09_not_righteousness (the 223rd; standing 2221 = 2215 + 6 as predicted, hash unmoved); the ledger
deu_09_ekev_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the outside rows {L_SIF}: MATERIAL {L_XM} / CONTEXT {L_XC}; coverage computed, lint 0, no cut
missed); six claims DV09-01..06 verified 6/0, seated as six WITNESS_READ at 9:1, 7, 12, 15, 22, 25; the ritual {N_PASS} PASS; the fold +{DJ} on the journal; the display
layer +{OV_REF9} by reference and +36 by gloss. THE FINDS: 9:13 shares ELEVEN OF THIRTEEN tokens with Exodus 32:9 — God\'s word quoted whole but for "to me, saying"; 9:17
shares ONE with 32:19 — the breaking retold in Moses\' own words ("before your eyes" for "beneath the mountain"); AARON\'S PERIL (9:20 — the anger, "to destroy him",
the prayer for him) has no telling in Exodus 32 — an act told only in the retelling, the compile\'s retrograde question; STIFF-NECKED six seats in the Bible, all
the calf\'s (Exodus 32:9, 33:3, 33:5, 34:9; 9:6, 9:13) and "stubbornness" (9:27) the noun\'s one seat; "TABLETS" in THREE SPELLINGS (plene 9:9-10 and 10:1 alone;
defective 9:11, 9:15, Exodus\'s form; the second plene 9:11 with 4:13 and 1 Kings 8:9) — two inside one verse — and "the tablets of the covenant" the Bible\'s three
seats all here; THE FORTY DAYS FOUR TIMES of the phrase\'s nine Bible seats, 9:25 alone with the article; THE OFFER\'S THREE FORMS (Exodus 32:10, Numbers 14:12,
9:14); "to do what is evil in the eyes of the LORD" (9:18) the Kings\' formula at its ONE Torah seat, "and I looked, and behold" (9:16) the vision formula\'s one;
THE PRAYER\'S SECOND TELLING — Israel/Jacob, the Egyptians/the land, the mountains/the wilderness — quoted by Solomon (1 Kings 8:51) and Nehemiah (1:10) from THIS
telling; THE NATIONS\' TAUNT IN FOUR FORMS; "because the LORD was not able" at two seats spelled two ways; THREE VOICES ON ONE PRONOUN (Israel\'s "you", God\'s to
Moses, Moses\' to God) and Moses never named; the register switching inside 9:7; ONKELOS — the Memra a consuming fire (4:24 the kin), merit for righteousness,
the reverential "before" at eleven seats, the prayer supplied at "let Me alone" and "hearkened", the file for the grinding, TWO ARAMAIC WORDS FOR FIRE (the calf
burned in the burnings\' fire, the mountain in the theophany\'s), the three place names translated, Rekem Geah, the double Name; JOSIAH\'S KIDRON the kin of the calf\'s
dust (2 Kings 23:6, 12). THE CAUTION: the English Sifrei mis-cites 306:25\'s Exodus verse ("Ex.36:28" for 34:28) — chapter 6\'s lesson again; the Hebrew right, the
row kept. THE LESSONS (ten, in the map): the shelf\'s bytes spell their own words; a summarizer counting runs misses single tokens; a spelling splits a census; a
derived tuple is retyped whole. OWED TO 7b: the readback\'s rows of the calf, Aaron\'s retrograde write, the state of the stiff neck, the three forties and their
dates (Ta\'anit 4:6), the four provocations, the intercession\'s second telling, a new checkpoint series.
'''

STEPS = f'''DEUTERONOMY — SITTING 7 — CHAPTER 9, Deuteronomy 9:1-29 ({DATE}, on Brian\'s "Let\'s keep run as it is and do another section" after the gates cut;
World/step9/DEUTERONOMY_WALK.md "Sitting 7" and "Sitting 7 — AS BUILT"; a reading sitting is one run). Chapter 9 is Moses telling the calf again in his own
voice — not for your righteousness, the forty days, the tablets written with God\'s finger, God\'s word to go down, the tablets broken before your eyes, forty days
more of prayer, Aaron\'s danger, the calf ground to dust, the four places of provoking, and the prayer that God should not destroy His people. The reading measured
each verse against its first telling: where God speaks, the retelling is word for word (9:13 with Exodus 32:9, eleven tokens of thirteen); where Moses acts, he
tells it in his own words (9:17 shares one token with Exodus 32:19); one thing has no first telling at all — the LORD\'s anger at Aaron and Moses\' prayer for him
(9:20) — and that is a question for the compile: an act told only here is written once at its own time. The Sifrei has no section on the chapter; its seven rows
from elsewhere read the chapter for its prayer, its forty days, its hyperbole, its harsh words and the breaking of the tablets among Moses\' wonders. The chapter
is frozen as one unit, the 223rd, the world\'s standing facts up by six as predicted, its hash unmoved, every gate green. The ink script fell eighteen ways on its
first pass — all forms (the shelf\'s own spellings, a count of one token), none a fact — and held on the second. Next: the commit on your word; then the compile of
chapter 9 in two runs — the calf\'s retelling graded against the tape, Aaron\'s retrograde write, the stiff neck as a state, the three forties and the answer sheet\'s
date for the breaking, a new checkpoint series — or the ten-commandments schema first.


'''

BRIEF = f'''- **CHAPTER 9 READ AND FROZEN — THE CALF RETOLD: GOD\'S WORD COMES BACK VERBATIM, MOSES\' ACTS COME BACK IN HIS OWN WORDS, AND AARON\'S DANGER IS TOLD NOWHERE ELSE; STIFF-NECKED SIX TIMES IN THE BIBLE, ALL FOR THE CALF; THE PRAYER SOLOMON AND NEHEMIAH QUOTE IS THIS ONE** ({DATE}, on your "Let\'s keep run as it is and do another section"; World/step9/DEUTERONOMY_WALK.md "Sitting 7" and "Sitting 7 — AS BUILT"; the ledger deu_09_ekev_{LDATE}.md, {L_ALL} sources whole; the unit deu_09_not_righteousness the 223rd, standing 2221, hash unmoved; six claims 6/0; every gate green; one run, every row whole).
'''
BRIEF_ENTRY = f'''### {DATE} — CHAPTER 9 READ: THE CALF TOLD TWICE, AND WHAT THE SECOND TELLING ADDS

Chapter 9 is Moses retelling the golden calf. The reading laid every verse
beside its first telling in Exodus and counted the shared words. The pattern
is clean: where God speaks, the retelling is word for word (God\'s "I have
seen this people, a stiff-necked people" comes back eleven words of
thirteen); where Moses acts, he retells it in his own words (his breaking of
the tablets shares one word with Exodus). And one thing has no first telling
at all: the LORD\'s anger at Aaron and Moses\' prayer for him (9:20). That is
the compile\'s question next sitting — an act told only in the retelling is
written once, at its own day. Other things the counting found: "stiff-necked"
occurs six times in the Bible and every one is about the calf; the word for
"tablets" is spelled three ways in this chapter, two of them inside one
verse; the forty days and nights appear four times here out of nine in the
whole Bible; and when Solomon and Nehemiah later pray "Your people and Your
inheritance … Your great power", they quote Moses\' prayer as chapter 9 tells
it, not as Exodus does. The Sifrei has no section on the chapter; seven rows
from elsewhere read it for its prayer, its forty days and its hyperbole.
The chapter is frozen as one unit, every gate green, in one run with every
row read whole.

'''

RESUME_NOTE = f'''# ⚠ THE DEUTERONOMY WALK sitting 7 ({DATE}; step9/DEUTERONOMY_WALK.md "Sitting 7" + "Sitting 7 — AS BUILT"): CHAPTER 9 READ AND FROZEN as ONE unit
# (deu_09_not_righteousness, the 223rd; standing 2221, hash unmoved) — the calf retold: 9:13 verbatim with Exodus 32:9, 9:17 in Moses\' own words, Aaron\'s peril
# (9:20) told only here (the compile\'s retrograde question); the Sifrei silent, seven outside rows whole; the ledger deu_09_ekev_{LDATE}.md ({L_ALL} sources); six claims
# seated; the fold +{DJ} on the journal ({J_ROWS} rows); every gate green. NEXT on the owner\'s word: the commit; then 7b — the compile of chapter 9 (a new checkpoint series).
'''

STATE = f'''
#197 ADDENDUM 1 ({DATE}, at the close of THE DEUTERONOMY WALK sitting 7 — CHAPTER 9\'s READING, the ONE run, on the owner\'s "Let\'s keep run as it is and do another section" — A CLEAN COMPACTION POINT): THE STATE: chapter 9 read and frozen as one unit (deu_09_not_righteousness, the 223rd); the corpus {C_UNITS} units, standing 2221 (2215 + 6 as predicted), hash 8b8fff1fa28953af unmoved; the tape unmoved since 6b (RUN (1310, 96, 88, 0, 12, 1605, 39, 319, the four pairs, 127), markers 167, closes 127); the ledger deu_09_ekev_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the outside rows {L_SIF}: MATERIAL {L_XM} / CONTEXT {L_XC}; {L_BYTES:,} bytes, lint 0); the manifest {N_CLAIMS} claims verified 6/0, seated at 9:1, 7, 12, 15, 22, 25; the display layer +{OV_REF9} / +36 ({OV_REF} / {OV_GL}). THE GATES: the ritual {N_PASS} PASS; verify_text GREEN ({VT_STEPS} steps, {VT_SCEN} scenarios); CORPUS TRUTH GREEN twice; build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer since chapter 8\'s reading); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL}); the home-path gate GREEN; the labels census GREEN ({LN}, Deuteronomy 58); large_letter_probes {LL[-3:]}; the ink {N_INK} asserts, 18 failing on the first typed pass (forms), 0 on the second and third. THE RUN\'S SHAPE: the reading sitting\'s one run — the rereads (the recovery page, the map\'s newest section, the memory; THE_STEPS Step 2, Step 5\'s head, the compiler block), the dump derived by twenty-three substitutions, the measure built from chapter 8\'s helpers, the ink, THE DESIGN in the map before a row was typed, the twenty-nine Onkelos rows and the seven outside rows whole, the ledger, the patch, the manifest, the seat (the spec\'s fifth element dropped in the derivation — the chain stopped at the seat, the draft untouched, retyped), the chain, the fold, the gates in one chain (ch9_gates.sh), the records from the sheet in one call (write_ch9_records.py). THE FINDS: 9:13 eleven of thirteen tokens with Exodus 32:9 (God\'s word verbatim), 9:17 one with 32:19 (Moses\' own words), AARON\'S PERIL TOLD ONLY HERE (9:20 — the retrograde question for 7b), stiff-necked six seats all the calf\'s, "tablets" in three spellings (two in 9:11) and "the tablets of the covenant" the Bible\'s three seats here, the forty days four times (9:25 with the article), the offer\'s three forms, the Kings\' formula at its one Torah seat (9:18), the prayer\'s second telling quoted by Solomon and Nehemiah, the taunt\'s four forms, three voices on one pronoun, Onkelos\'s two fires and the prayer supplied, the English Sifrei\'s "Ex.36:28" slip. THE RECORDS (write_ch9_records.py from the sheet): the map\'s "Sitting 7 — CHAPTER 9 — AS BUILT" (ten lessons), COMPILE_DEBT\'s sitting-7 box (a)-(j) owed to 7b, MIDDOT\'s chapter-9 block (I1 at 27:2, I2 at 357:44 — both checked in MIDDOT.md before typing), MISHNAH_TOPICS (Fasts 4:6 and Idolatry 3:3 routed to 7b), RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the bullet and an entry), RESUME, this addendum, the addenda §46, the recovery page (section 2 rewritten under its cap), the stamp row, the memory (the walk note and the index line under 17,000), the commit message\'s paragraph. THE FORMS copied (copy_ch9_forms.py). NOT COMMITTED (since 29c189b): sitting 6, the two-run rule, 6b, the gates cut, and sitting 7 — the message at <scratch>/commit_msg_ch8.txt covers them all for the owner\'s word ("commit" = no push; "commit push" = both). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. NEXT ON THE RULING: the commit on his word; then THE COMPILE OF CHAPTER 9 (7b) in TWO RUNS — RUN A the rereads, the measurements (the calf\'s lines in four runners; the checkpoint prefix space — A NEW SERIES, the 'C[A-Z]' regexes measured first), the design, the probes to FAIL, the docket by the union rule (every row whole; its own run past ~700 rows); RUN B the types, the runner, the tape to 10/10, the chain, the records — or the Decalogue-schema sitting first; THE INSTALL HYPOTHESIS and THE SUPPLIED GRADE on the table. POST-COMPACTION REREADS: the recovery page, the map\'s "Sitting 7 — AS BUILT" (the newest section — the departures and the lessons), MEMORY.md.
'''

ADDENDA = f'''
## 46. ADDENDUM ({DATE}, THE DEUTERONOMY WALK sitting 7 — CHAPTER 9, Deuteronomy 9:1-29 READ AND FROZEN in ONE run under THE TWO-RUN RULE, every row whole; the owner: "Let\'s keep run as it is and do another section"; the state doc\'s #197 addendum 1)
THE READING: Onkelos Deuteronomy 9 whole (29 = 29, the identity, cost 37); the Sifrei SILENT on the chapter — seven rows outside any piska by the union of both files
(14:1, 25:4, 26:7, 27:2 reread whole from sitting 1; 306:25, 342:1, 357:44 fresh; 342:1 the Hebrew\'s range form "9:7-8" found through the English); the kin credited by
name (the Exodus ledgers on the calf, the ascent, the second tablets, the craftsmen; the Numbers ledgers on Taberah, Kibroth, the spies, Meribah); the unit
deu_09_not_righteousness the 223rd (standing 2221, hash unmoved); the ledger {L_ALL} sources (Onkelos MATERIAL {L_OM} / CONTEXT {L_OC}; the outside rows MATERIAL {L_XM} / CONTEXT {L_XC});
six claims 6/0 seated at 9:1, 7, 12, 15, 22, 25; the display layer +{OV_REF9} by reference, +36 by gloss; every gate green in one chain (ch9_gates.sh — the chain stopped
once at the seat, the spec\'s fifth element dropped in the derivation, retyped and rerun). THE FINDS: 9:13 eleven of thirteen tokens with Exodus 32:9; 9:17 one with
32:19; AARON\'S PERIL told only here (9:20 — the retrograde question); stiff-necked six seats all the calf\'s; "tablets" in three spellings; the forty days four times;
the offer\'s three forms; the Kings\' formula\'s one Torah seat (9:18); the prayer\'s second telling quoted by Solomon and Nehemiah; the taunt\'s four forms; three voices
on one pronoun; Onkelos\'s two fires, the names translated, the prayer supplied; the English Sifrei\'s "Ex.36:28" slip. THE LESSONS (ten, in the map): the shelf\'s
bytes spell their own words; a summarizer counting runs misses single tokens; a spelling splits a census; a derived tuple is retyped whole; the kin\'s credits are
counted. OWED TO 7b (COMPILE_DEBT\'s box): the readback\'s rows of the calf, Aaron\'s retrograde write, the stiff neck as a state, the three forties and Ta\'anit 4:6\'s
date, the four provocations, the intercession\'s second telling, a NEW checkpoint series, the docket. The records on the sheet; the forms in
World/step9/forms_deuteronomy_walk/ (copy_ch9_forms.py).
'''

MEMPAR = f'''
SITTING 7 DONE {DATE} ("Let\'s keep run as it is and do another section" after THE GATES CUT; the map\'s "Sitting 7" and "Sitting 7 — AS BUILT"): CHAPTER 9 READ AND FROZEN
as ONE unit deu_09_not_righteousness (the 223rd; standing 2221 = 2215 + 6 as predicted, hash unmoved) in ONE run, every row whole — Onkelos 29 rows (the identity),
the Sifrei SILENT (seven outside rows whole, four reread from sitting 1), the kin credited by name; the ledger deu_09_ekev_{LDATE}.md ({L_ALL} sources); six claims 6/0
seated at 9:1, 7, 12, 15, 22, 25; every gate green; the display layer +{OV_REF9} / +36. THE FINDS: the calf retold — 9:13 VERBATIM with Exodus 32:9 (eleven of thirteen
tokens), 9:17 in Moses\' own words (one token with 32:19), AARON\'S PERIL (9:20) TOLD ONLY HERE — the compile\'s retrograde question; stiff-necked six Bible seats all
the calf\'s; "tablets" in three spellings (two in 9:11), "the tablets of the covenant" the Bible\'s three seats all here; the forty days four times; the offer\'s three
forms; the Kings\' formula at its one Torah seat (9:18); the prayer\'s second telling quoted by Solomon and Nehemiah; Onkelos\'s two words for fire, the three names
translated, the prayer supplied. ⚠ LESSONS (ten, in the map): the shelf\'s bytes spell their own words (הביי "hyperbole", וחמר "and heavy"); a summarizer counting runs
misses single tokens — the ink\'s counter is the measure; a spelling splits a census; a derived tuple is retyped whole (the seat spec\'s fifth element — the chain
stopped at its first step, nothing touched). OWED TO 7b: the readback\'s rows of the calf, Aaron\'s retrograde write, the stiff neck as a state, the three forties and
Ta\'anit 4:6\'s date, the four provocations, the intercession\'s second telling, A NEW CHECKPOINT SERIES (CU the last two-letter prefix — the probes\' regexes measured
first), the docket by the union rule. NOT COMMITTED (since 29c189b; the message at <scratch>/commit_msg_ch8.txt covers sitting 6, the two-run rule, 6b, the gates
cut and sitting 7). NEXT on the ruling: the commit; then 7b — or the schema sitting.
'''
MEMLINE_OLD_START = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — '
MEMLINE_NEW = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — map World/step9/DEUTERONOMY_WALK.md; ch 1-8 COMPILED, ch 9 READ (1-7 PUSHED 29c189b; the rest + the gates cut UNCOMMITTED); NEXT: commit, then 7b (a NEW checkpoint series)\n'
DESC_OLD = "COMMITTED THROUGH 29c189b (2026-09-18; PUSHED) — SITTING 6b DONE 2026-09-19 ("
DESC_NEW = f"COMMITTED THROUGH 29c189b (2026-09-18; PUSHED) — SITTING 7 DONE {DATE} (chapter 9 READ AND FROZEN as one unit, the 223rd — the calf retold, Aaron's peril told only here, the retrograde question for 7b; UNCOMMITTED) — SITTING 6b DONE 2026-09-19 ("
REC2_OLD_START = '## 2. WHERE IT STANDS'
REC2_NEW = f'''## 2. WHERE IT STANDS ({DATE}, after sitting 7 and THE GATES CUT; the state doc #197 addendum 1 the newest)
- NUMBERS CLOSED. DEUTERONOMY 1-8 COMPILED AND ON THE TAPE (1-7 at 29c189b PUSHED; 8 at sittings 6/6b); 9 READ (sitting 7).
- {C_UNITS} frozen units, standing 2221, hash 8b8fff1fa28953af. 63 runners, 68 daemons, 466 functions; 1133 kinds / 1031 effects.
- THE TAPE at RUN (1310, 96, 88, 0, 12, 1605, 39, 319, pairs, 127), markers 167, closes 127; the sweep 63/63; every gate GREEN; the
  register gate DECLARED {R_DECL} / DEBT 0. The readback's FIFTH form (6b): a STATE graded SUPPLIED, no write — his decision open.
- Uncommitted since 29c189b: sitting 6, the two-run rule, 6b, THE GATES CUT, sitting 7; the message at <scratch>/commit_msg_ch8.txt.
- NEXT ON HIS WORD: the commit; then 7b (chapter 9's compile, two runs: the calf's readback rows, Aaron's retrograde write, a NEW
  checkpoint series — CU the last prefix).
'''
TOPIC_FASTS = f' — 4:6 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 7, chapter 9\'s reading: the tablets broken on the seventeenth of Tammuz — THE ANSWER SHEET\'S DATE for 9:17; the three forties\' arithmetic at 28b — the compile 7b\'s docket).'
TOPIC_IDOL = f' — 3:3 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 7, chapter 9\'s reading: the calf burned, ground fine as dust and thrown into the brook, 9:21 — the idol\'s destruction by R. Yose\'s "grind and scatter"; Avodah Zarah 43b-44a — the compile 7b\'s docket).'
LINT = f'{ROOT}/logic/solo_tools/gloss_lint.py'
def lint(path):
    out = subprocess.run([sys.executable, LINT, path], capture_output=True, text=True).stdout
    m = re.search(r'gloss_lint: (\d+) flag', out); return int(m.group(1)) if m else -1
WALKP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; RECP = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
TOPICS = f'{ROOT}/logic/MISHNAH_TOPICS.md'
TOUCH = [f'{ROOT}/logic/findings/STAMP_LEDGER.md', f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', f'{ROOT}/World/RESUME.md', f'{ROOT}/THE_STEPS.md', f'{ROOT}/THE_BRIEFING.md', f'{ROOT}/World/step9/COMPILE_DEBT.md', f'{ROOT}/RESEARCH_LOG.md', f'{ROOT}/logic/MIDDOT.md', RECP, f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md', TOPICS]
# ---- THE ANCHORS, ASSERTED PRESENT ONCE BEFORE ANY WRITE ----
A_RESUME = '# ⚠ THE GATES CUT (2026-09-19; step9/GATES_CHAIN.md'
A_SCORE = '## SCOREBOARD (as of 2026-09-19, latest)\n'
A_BULLET = '- **THE GATES CHAIN CUT FROM NINETY MINUTES TO'
A_ENTRY = '### 2026-09-19 — The test bench got fast without getting looser'
A_MIDDOT = '\n## Exodus block campaign — owner\'s word "Do 3")\n'
A_REC5 = 'the newest instances: the map\'s "Sitting 6" and "Sitting 6b"'
A_REC6 = '- Deuteronomy\'s sittings: the map; the addenda §31-44 (§39 the whole-row rule). The cost cuts: §35, §45.'
T_FASTS = '**20. Mishnah, Fasts**'; T_IDOL = '**38. Mishnah, Idolatry**'
ANCH = [(f'{ROOT}/World/RESUME.md', A_RESUME), (f'{ROOT}/THE_STEPS.md', '\n## Step 6 — Publish\n'), (f'{ROOT}/THE_BRIEFING.md', A_SCORE), (f'{ROOT}/THE_BRIEFING.md', A_BULLET), (f'{ROOT}/THE_BRIEFING.md', A_ENTRY), (f'{ROOT}/logic/MIDDOT.md', A_MIDDOT), (RECP, REC2_OLD_START), (RECP, '\n## 3. THE STANDING LAWS'), (RECP, A_REC5), (RECP, A_REC6), (f'{MEM}/deuteronomy-walk.md', DESC_OLD), (f'{MEM}/MEMORY.md', MEMLINE_OLD_START)]
for p, a in ANCH: assert rd(p).count(a) == 1, (p, a[:40], rd(p).count(a))
tl = rd(TOPICS).split('\n'); assert sum(l.startswith(T_FASTS) for l in tl) == 1 and sum(l.startswith(T_IDOL) for l in tl) == 1 and f'ROUTED {DATE}' not in rd(TOPICS)
assert '## Sitting 7 — CHAPTER 9 — AS BUILT' not in rd(WALKP) and '## Sitting 7 — CHAPTER 9, Deuteronomy 9:1-29' in rd(WALKP) and '#197 ADDENDUM 1' not in rd(TOUCH[1]) and '#197 (2026-09-19' in rd(TOUCH[1]) and '## 46. ADDENDUM' not in rd(TOUCH[9]) and '## 45. ADDENDUM' in rd(TOUCH[9]) and 'SITTING 7 DONE' not in rd(f'{MEM}/deuteronomy-walk.md') and 'SITTING 7 — CHAPTER 9' not in rd(TOUCH[5]) and STAMP not in rd(TOUCH[0])
s = rd(RECP); i = s.index(REC2_OLD_START); j = s.index('\n## 3. THE STANDING LAWS'); REC_NEW = s[:i] + REC2_NEW + s[j:]
REC_NEW = REC_NEW.replace(A_REC5, 'the newest instances: the map\'s "Sitting 7" and "Sitting 6b"').replace(A_REC6, '- Deuteronomy\'s sittings: the map; the addenda §31-46 (§39 the whole-row rule). The cost cuts: §35, §45.')
for a, b in [("forms_deuteronomy_walk/ (the walk's scripts and prints — derive the\nnewest sitting's form by sed)", "forms_deuteronomy_walk/ (the walk's forms — derive by sed)"), ("- THE_STEPS Step 2, Step 5 and the compiler-law block: before a READING sitting's ledger is written.", "- THE_STEPS Step 2, Step 5, the compiler block: before a reading's ledger."), ("He compacts after each RUN; a clean point is announced at every run's end.", "A clean point is announced at every run's end.")]:
    assert REC_NEW.count(a) == 1, a[:50]; REC_NEW = REC_NEW.replace(a, b)   # the page trimmed under its cap (the words dropped live in the files it points to)
assert len(REC_NEW.encode()) <= 10240, len(REC_NEW.encode())
m = rd(f'{MEM}/MEMORY.md'); i = m.index(MEMLINE_OLD_START); j = m.index('\n', i) + 1; MEM_NEW = m[:i] + MEMLINE_NEW + m[j:]
assert len(MEM_NEW.encode()) < 17000, len(MEM_NEW.encode())
# the commit message's paragraph (the scratch file the owner's word commits)
CM = f'{SP}/commit_msg_ch8.txt'; cm = rd(CM); assert 'SITTING 7' not in cm and '\nCo-Authored-By:' in cm
head, rest = cm.split('\n', 1)
head2 = head.rstrip('.') + f' AND, THE SAME DAY, CHAPTER 9 READ AND FROZEN (SITTING 7, ONE RUN, EVERY ROW WHOLE) — THE CALF RETOLD: GOD\'S WORD VERBATIM, MOSES\' ACTS IN HIS OWN WORDS, AARON\'S PERIL TOLD NOWHERE ELSE.'
CM_PARA = f'''
ALSO IN THIS COMMIT: SITTING 7 — CHAPTER 9 READ AND FROZEN ({DATE}, on the owner\'s "Let\'s keep run as it is and do another section"; World/step9/DEUTERONOMY_WALK.md "Sitting 7" and "Sitting 7 — AS BUILT"; the state doc\'s #197 addendum 1; the addenda §46): Deuteronomy 9:1-29 with Onkelos whole (the export\'s 29 rows the DB\'s 29 — the identity, asserted) and the Sifrei on Deuteronomy SILENT ON THE CHAPTER (36 on 6:9, 37 on 11:10), its whole voice seven rows from elsewhere found by the union of both files\' citations and read whole (14:1 and 306:25 the forty days as Moses\' suffering, with Exodus 34:28; 25:4 the hyperbole rule; 26:7 the ten names of prayer; 27:2 the door opened, the a-fortiori; 342:1 the harsh words, the Hebrew\'s range form; 357:44 the breaking among the wonders, the verbal analogy), four reread whole from sitting 1; frozen as ONE unit deu_09_not_righteousness (the 223rd; standing 2221 = 2215 + 6 as predicted, hash 8b8fff1fa28953af unmoved); the ledger logic/oral_triage/deu_09_ekev_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the outside rows {L_SIF}: MATERIAL {L_XM} / CONTEXT {L_XC}; coverage computed, lint 0, no cut missed); six claims DV09-01..06 verified 6/0, seated as six WITNESS_READ operators at 9:1, 7, 12, 15, 22, 25 with step E; the ritual {N_PASS} PASS; the display layer +{OV_REF9} by reference and +36 by gloss. THE FINDS: THE CALF RETOLD — 9:13 shares ELEVEN OF THIRTEEN tokens with Exodus 32:9 (God\'s word quoted whole but for "to me, saying"), 9:17 shares ONE with 32:19 (the breaking in Moses\' own words — "before your eyes" for "beneath the mountain"), AARON\'S PERIL (9:20 — the LORD\'s anger at him, "to destroy him", Moses\' prayer for him) has no telling in Exodus 32 — an act told only in the retelling, the compile\'s retrograde question; STIFF-NECKED six seats in the Bible, all the calf\'s, and "stubbornness" the noun\'s one seat; "TABLETS" IN THREE SPELLINGS (two inside 9:11) and "the tablets of the covenant" the Bible\'s three seats all here; THE FORTY DAYS FOUR TIMES (9:25 alone with the article); THE OFFER\'S THREE FORMS; the Kings\' formula "to do what is evil in the eyes of the LORD" at its ONE Torah seat (9:18); THE PRAYER\'S SECOND TELLING (Israel/Jacob, the Egyptians/the land, the mountains/the wilderness) quoted by Solomon (1 Kings 8:51) and Nehemiah (1:10) from THIS telling; the nations\' taunt in four forms; three voices on one pronoun and Moses never named; ONKELOS — the Memra a consuming fire, merit for righteousness, the prayer supplied at "let Me alone" and "hearkened to me", the file for the grinding, two Aramaic words for fire, the three place names translated, Rekem Geah; the English Sifrei mis-cites 306:25\'s Exodus verse ("Ex.36:28" for 34:28) — chapter 6\'s lesson again. EVERY GATE GREEN: verify_claims 6/0, the labels census ({LN}, debt 0), verify_text ({VT_STEPS} steps, {VT_SCEN} scenarios), the ritual {N_PASS} PASS, CORPUS TRUTH GREEN before and after the bake ({C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, hash unmoved), build_world ALL GREEN, the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer, the tape unmoved), the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL}), large_letter_probes 6/6, the home-path gate GREEN; the ink {N_INK} asserts, eighteen failing on the first typed pass (forms, not facts) and 0 on the second and third. THE LESSONS (ten, in the map): the shelf\'s bytes spell their own words; a summarizer counting runs misses single tokens; a spelling splits a census; three voices on one pronoun; the English export mis-citing again; a derived tuple retyped whole (the seat spec\'s fifth element — the chain stopped at its first step, nothing touched); the kin\'s credits counted; the reading sitting held in one run. Also in this commit: COMPILE_DEBT\'s sitting-7 box (a)-(j) owed to 7b (the readback\'s rows of the calf, Aaron\'s retrograde write, the stiff neck as a state, the three forties and Ta\'anit 4:6\'s date, the four provocations, the intercession\'s second telling, a NEW checkpoint series, the docket), MIDDOT\'s chapter-9 block (I1 at 27:2, I2 at 357:44), MISHNAH_TOPICS (Fasts 4:6 and Idolatry 3:3 routed), RESEARCH_LOG\'s entry, THE_STEPS, THE_BRIEFING (the scoreboard and an entry), World/RESUME.md, the recovery page rewritten under its cap, the stamp row, the forms in World/step9/forms_deuteronomy_walk/. NEXT on the owner\'s word: THE COMPILE OF CHAPTER 9 (7b) in two runs — or the Decalogue-schema sitting first.
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
row_note(TOPICS, T_FASTS, TOPIC_FASTS)
row_note(TOPICS, T_IDOL, TOPIC_IDOL)
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
