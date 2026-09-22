import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 12 — CHAPTER 14 (2026-09-21; the owner: "Go" after 11b's tail — a reading sitting under THE COST RULES A-B-C: ONE run to the clean
# point #204 after the rows (the cap passed by /context a second time — the NOTE), the owner's compaction, "Reread", "Go", THE TAIL on a small context): THE RECORDS
# at the close, from the sheet World/step9/RECORD_FORMS.md in ONE call — the map's "Sitting 12 — CHAPTER 14 — AS BUILT" WITH THE TIMING TABLE computed from the
# scratchpad's ch14_timing.tsv, COMPILE_DEBT's box (owed to the compile 12b), MIDDOT's block (the codes censused from the ledger's own rows), MISHNAH_TOPICS' row
# notes (ROUTED to 12b), RESEARCH_LOG's entry, THE_STEPS' paragraph, THE_BRIEFING's bullet and entry, RESUME's note, the state doc's #204 addendum 1, the recovery
# page (section 2 rewritten, under 10 KB), the recovery addenda's §59, the stamp row, the memory file and the index line (under 17,000 bytes), and THE COMMIT
# MESSAGE (chapter 14's, carrying chapter 13's compile message beneath it — both uncommitted since fb797a1). Every number parsed from a print named beside it
# (--check prints them and writes nothing); every insert on a unique anchor asserted present once; the lints before and after. Sitting 11's form
# (write_ch13_records.py). RUN FROM THE REPO ROOT.
import os, re, subprocess, sys, yaml, json, datetime, glob
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/' + os.path.abspath(ROOT).replace('/', '-') + '/memory')
DATE = '2026-09-21'; LDATE = '2026-09-21'
UID = 'deu_14_food_tithe'
CHECK = '--check' in sys.argv
CHAIN_NOTE = 'THE GATES CHAIN RAN ONCE, ALL GREEN ON ITS FIRST PASS (18:57:52 to 19:06:01 — 8 min 9 s: the seat (seven operators on seven steps, the scenarios in the anchor form), verify_text (29 steps, 7 scenarios), the ritual (13 PASS), the fold (228 / 2252 / the hash unmoved — 1,809 facts, 341 demands, 191 open), build_world, the journal gate (9,788 rows, +16 on the fold layer), the register gate --strict (DECLARED 98, no demand — the register step 4 min 39 s of the chain), large_letter 6/6, the home gate; no demand, no retype; the summary read once) — launched in the background after the manifest (every cite index name used), verify_claims (7 verified / 0 failed) and the labels census (GATE PASSED, debt 0 — 3,312 claims in 231 manifests) had run in the foreground and their prints were read; the records writer and the copier typed during its 489 seconds, the notification the wake.'
def rd(p): return open(p, encoding='utf-8').read()
# ---- THE NUMBERS, PARSED FROM THE PRINTS ----
truth = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py')
assert 'assert len(W["units"]) == 228' in truth and 'assert len(W["standing"]) == 2252' in truth and "8b8fff1fa28953af" in truth
CT = rd(f'{SP}/ch14_truth.out'); CB = rd(f'{SP}/ch14_bake.out'); C1 = rd(f'{SP}/ch14_fold_check1.out')
assert 'CORPUS TRUTH GREEN' in CT and 'CORPUS TRUTH GREEN' in C1 and 'wrote corpus_world.sqlite' in CB
rit = rd(f'{SP}/ch14_ritual_{UID}.out'); N_PASS = len(re.findall(r'^PASS', rit, re.M))
assert 'RITUAL COMPLETE' in rit and N_PASS >= 1 and not re.search(r'^FAIL', rit, re.M), N_PASS
vt = rd(f'{SP}/ch14_vt_{UID}.out'); mvt = re.search(r'TEXT LAYER GREEN: (\d+) steps, (\d+) scenarios', vt); assert mvt and mvt.group(1) == '29', vt[-300:]
VT_STEPS, VT_SCEN = mvt.groups()
assert '  status: frozen' in rd(f'{ROOT}/logic/units/{UID}.yaml') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json') and 'ALL_DONE' in rd(f'{SP}/ch14_chain.log')
JG = rd(f'{SP}/ch14_journal.out'); RG = rd(f'{SP}/ch14_register.out'); BW = rd(f'{SP}/ch14_build.out'); GS = rd(f'{SP}/ch14_gates_SUMMARY.txt')
assert 'GATE GREEN' in JG and 'ALL GREEN' in BW and 'THE REGISTER GATE: GREEN' in RG and 'ALL GREEN' in GS, (JG[-200:], BW[-200:], GS[-200:])
mj = re.search(r'(\d+) kinds, ([\d,]+) rows', JG); J_KINDS, J_ROWS = mj.group(1), mj.group(2)
mr = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', RG); R_DECL, R_DEBT, R_FAIL = mr.groups()
assert R_DEBT == '0' and R_FAIL == '0' and R_DECL == '98', mr.groups()
mc = re.search(r'(\d+) units, (\d+) facts, (\d+) demands \((\d+) open\)', CT); C_UNITS, C_FACTS, C_DEM, C_OPEN = mc.groups()
assert C_UNITS == '228', C_UNITS
HG = rd(f'{SP}/ch14_home.out'); assert 'GREEN' in HG, HG[-200:]
LED = rd(f'{ROOT}/logic/oral_triage/deu_14_reeh_{LDATE}.md')
ml = re.search(r'\*\*read: (\d+) of \1 — COMPLETE\*\* \((\d+) Onkelos verses and (\d+) Sifrei rows.*?MATERIAL (\d+) Onkelos, CONTEXT (\d+) Onkelos, MATERIAL (\d+) Sifrei spine, CONTEXT (\d+) Sifrei spine, MATERIAL (\d+) Sifrei outside, CONTEXT (\d+) Sifrei outside', LED, re.S)
L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_SM, L_SC, L_XM, L_XC = ml.groups()
assert L_ALL == '143' and L_ONK == '29' and L_SIF == '114' and LED.count('⟨MISS⟩') == 0
L_SPINE = int(L_SM) + int(L_SC); L_OUT = int(L_XM) + int(L_XC); assert L_SPINE == 111 and L_OUT == 3, (L_SPINE, L_OUT)
L_BYTES = len(LED.encode())
SEC_SPINE = LED.split('## Sifrei Devarim rows citing chapter 14')[0]; SEC_OUT = LED.split('## Sifrei Devarim rows citing chapter 14')[1].split('## Onkelos')[0]
N_REREAD = len(re.findall(r'^- Sifrei Devarim \d+:\d+ — [A-Z]+ \(REREAD WHOLE — read before in', SEC_SPINE, re.M)); N_REREAD_OUT = len(re.findall(r'^- Sifrei Devarim \d+:\d+ — [A-Z]+ \(REREAD WHOLE — read before in', SEC_OUT, re.M))
assert N_REREAD == 2 and N_REREAD_OUT == 1, (N_REREAD, N_REREAD_OUT)
CODES = Counter(); BYCODE = {}
for line in re.findall(r'^- Sifrei Devarim \d+:\d+ — .*$', LED, re.M):
    name = re.match(r'- (Sifrei Devarim \d+:\d+)', line).group(1)
    for c in sorted(set(re.findall(r'\b([IE]\d{1,2}) \(', line))): CODES[c] += 1; BYCODE.setdefault(c, []).append(name.split(' ')[2])
CODE_TXT = '; '.join(f'{c} at {", ".join(BYCODE[c])}' for c in sorted(CODES, key=lambda x: (x[0], int(x[1:]))))
print('CODES BY ROW:', CODE_TXT, '| the sum', sum(CODES.values()))
for c, r in (('I1', '101:10'), ('I1', '76:7'), ('I1', '106:3'), ('I1', '106:4'), ('I1', '107:4'), ('I1', '107:7'), ('I2', '96:12'), ('I2', '99:2'), ('I2', '103:3'), ('I2', '103:4'), ('I2', '107:16'), ('I2', '109:2'), ('I3', '103:8'), ('I3', '228:5'), ('I3', '105:8'), ('I3', '107:11'), ('I3', '110:1'), ('I3', '110:2')): assert r in BYCODE.get(c, []), (c, r, BYCODE.get(c))
assert dict(CODES) == {'I1': 6, 'I2': 6, 'I3': 6}, dict(CODES)
d_ov = yaml.safe_load(rd(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'))
OV_REF14 = len([k for k in d_ov['by_ref'] if k.startswith('Deut.14.')]); OV_REF, OV_GL = len(d_ov['by_ref']), len(d_ov['by_gloss'])
assert OV_REF14 == 131 and OV_REF == 1253 and OV_GL == 756, (OV_REF14, OV_REF, OV_GL)
N_CLAIMS = len(json.load(open(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json', encoding='utf-8'))); assert N_CLAIMS == 7
VC = rd(f'{SP}/ch14_vc.out'); assert 'SUMMARY: 7 verified, 0 failed, 0 uncheckable, 0 no-check' in VC, VC[-300:]
LAB = rd(f'{SP}/ch14_labels.out'); mlab = re.search(r'CLAIM LABELS CENSUS — (\d+) claims in (\d+) manifests; labeled \1; DEBT 0', LAB); LN = f'{int(mlab.group(1)):,} claims in {mlab.group(2)} manifests'; assert 'GATE PASSED' in LAB and re.search(r'deu\s+89 claims', LAB), LAB[-300:]
INKF = {n: int(re.search(r'(\d+) failing statements', rd(f'{SP}/ch14_ink_run{n}.out')).group(1)) for n in (1, 2, 3, 4, 5, 6)}
assert INKF == {1: 27, 2: 2, 3: 0, 4: 0, 5: 2, 6: 0}, INKF
N_INK = len(re.findall(r'^assert ', rd(f'{SP}/ch14_ink.py'), re.M)); assert N_INK == 106, N_INK
LL = rd(f'{SP}/ch14_large_letter.out').strip().split('\n')[-1]; assert LL.endswith('6/6'), LL
JPREV = f'{ROOT}/World/step9/forms_deuteronomy_walk/gates_ch13b_journal.out'
JR13 = re.search(r'12 kinds, ([\d,]+) rows', rd(JPREV)).group(1); DJ = int(J_ROWS.replace(',', '')) - int(JR13.replace(',', ''))
MAN = rd(f'{SP}/ch14_manifest.out'); assert 'every CITE INDEX name used by a claim: True' in MAN
DUMP = rd(f'{SP}/ch14_dump0.out'); mdump = re.search(r'DB verses (\d+) \| export verses HE (\d+) EN (\d+)', DUMP); assert mdump and mdump.groups() == ('29', '29', '29'), DUMP[:300]
LEDW = rd(f'{SP}/write_ch14_ledger.out'); assert '143 sources' in LEDW and 'MISMARK []' in LEDW and 'FAIL []' in LEDW, LEDW[-200:]
PATCH_LINE = rd(f'{SP}/ch14_patch.out').strip().split('\n')[-1]; assert PATCH_LINE == 'override rows written: by_ref 131 by_gloss 49 | by_ref total 1253 | by_gloss total 756', PATCH_LINE
# ---- THE TIMING TABLE, computed from the scratchpad's tsv (the first step's own stamp is the start) ----
def timing():
    rows = [l.rstrip('\n').split('\t') for l in rd(f'{SP}/ch14_timing.tsv').splitlines() if l.strip()]
    day = datetime.datetime(2026, 9, 21)
    def at(hms): h, m, s = map(int, hms.split(':')); return int(day.replace(hour=h, minute=m, second=s).timestamp())
    t0 = at(rows[0][0])
    out = ['| step | began | ran | the gap before it (reading, typing, the owner\'s compaction) |', '|---|---|---|---|']
    prev_end, mach = t0, 0
    for hms, name, secs, rc in rows:
        b = at(hms); gap = b - prev_end; mach += int(secs); prev_end = b + int(secs)
        out.append(f'| {name} | {hms} | {secs} s{" (rc " + rc + ")" if rc != "0" else ""} | {gap // 60} min {gap % 60} s |')
    total = prev_end - t0
    return '\n'.join(out), mach, total, rows[0][0], len(rows)
TT, T_MACH, T_TOTAL, T_START, T_ROWS = timing()
def chain_steps():
    st = re.findall(r'^=== (\w+) (\d\d):(\d\d):(\d\d)', GS, re.M); end = re.search(r'^ALL GREEN (\d\d):(\d\d):(\d\d)', GS, re.M)
    pts = [(n, int(h) * 3600 + int(m) * 60 + int(s)) for n, h, m, s in st] + [('ALL GREEN', int(end.group(1)) * 3600 + int(end.group(2)) * 60 + int(end.group(3)))]
    return '; '.join(f'{pts[i][0]} {pts[i + 1][1] - pts[i][1]} s' for i in range(len(pts) - 1)), pts[-1][1] - pts[0][1]
CS_TXT, CS_TOTAL = chain_steps()
def mmss(x): return f'{x // 60} min {x % 60} s'
print('PARSED:', dict(ritual_pass=N_PASS, verify_text=(VT_STEPS, VT_SCEN), journal=(J_KINDS, J_ROWS, DJ, JR13), register=(R_DECL, R_DEBT, R_FAIL), corpus=(C_UNITS, C_FACTS, C_DEM, C_OPEN), ledger=(L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_SM, L_SC, L_XM, L_XC, L_BYTES, N_REREAD, N_REREAD_OUT), codes=dict(CODES), overrides=(OV_REF14, OV_REF, OV_GL), claims=N_CLAIMS, labels=LN, ink=(N_INK, INKF), large_letter=LL[-3:], timing=(T_ROWS, T_MACH, T_TOTAL, T_START), chain=(CS_TXT, CS_TOTAL)))
print(TT)
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

STAMP = (f'| {DATE} | {UID} | DELEGATED | FULL RULE | Deuteronomy 14:1-29 derivation {LDATE} (THE DEUTERONOMY WALK sitting 12 — CHAPTER 14; the owner: "Go" after 11b\'s tail — a reading sitting under THE COST RULES, one run to the clean point #204 after the rows and its tail after the compaction, every step timed, every row whole): Onkelos Deuteronomy 14 whole (29 = 29, the identity) + the Sifrei on Deuteronomy ON THE CHAPTER — piska 96\'s rows 9-12 and piskaot 97-110 (the heads not in verse order), {L_SPINE} spine rows read whole in both files ({N_REREAD} rows read before and reread whole) + its {L_OUT} rows outside the spine read whole ({N_REREAD_OUT} reread whole) + the kin credited by name; the ledger deu_14_reeh_{LDATE}.md ({L_ALL} sources, coverage computed, lint 0); {N_CLAIMS} claims DV14-01..07 verified 7/0, seated as seven WITNESS_READ at 14:1, 3, 9, 21, 22, 24, 28; the ritual {N_PASS} PASS; CORPUS TRUTH GREEN ({C_UNITS} units, standing 2252, hash unmoved); the fold layer +{DJ}; the display layer +{OV_REF14} by reference, +49 by gloss; the machine\'s share of the sitting {mmss(T_MACH)} of {mmss(T_TOTAL)} | {LN}, labeled, debt 0 |\n')

WALK = f'''


## Sitting 12 — CHAPTER 14 — AS BUILT ({DATE}; the design above stands as written but for the clean point's place — the one run ran through ALL the rows to the clean point #204 (the design had said "between the halves if the counter nears the cap": the counter stood near 470k and /context read 657.8k — the cap passed a second time), the owner compacted, and THE TAIL ran on "Reread" and "Go" with the ledger its first step; every departure from the design is named here; THE TIMING TABLE is the last section)

THE RESULT: Deuteronomy 14:1-29 READ, FROZEN and SEATED as ONE unit — deu_14_food_tithe (the 228th frozen unit; 29 of 29 verses, missing 0, computed — the
export's chapter 14 the DB's, the identity; no portion edge inside it): the ledger logic/oral_triage/deu_14_reeh_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} /
CONTEXT {L_OC}; THE SIFREI'S SPINE piska 96's tail and piskaot 97-110, {L_SPINE} rows: MATERIAL {L_SM} / CONTEXT {L_SC}, {N_REREAD} of them read before and REREAD WHOLE (the prior reads
found in the earlier ledgers by computation — 104:8 at chapter 6's sitting, 106:5 at chapter 12's); the outside rows {L_OUT}: MATERIAL {L_XM} / CONTEXT {L_XC}, 76:7 read before at
chapter 12's sitting and REREAD WHOLE; {L_BYTES:,} bytes, lint 0, no cut missed — the ledger written clean on its first run), the manifest {N_CLAIMS} claims DV14-01..07
verified 7/0 (every he_contains cut from the store's own bytes — the seven words' pieces MEASURED in the store before they were typed, the floor four code points;
every cite index name used by a claim — the spine's rows distributed by piska from the CITE INDEX itself, 96's tail with the children and the cuts, the three
outside rows with the claims whose verses they cite), seated as seven WITNESS_READ operators at 14:1, 3, 9, 21, 22, 24, 28 with step E; the ritual {N_PASS} PASS;
verify_text GREEN ({VT_STEPS} steps, {VT_SCEN} scenarios); the fold predicted and matched (units 227 → 228, standing 2245 → 2252, the hash 8b8fff1fa28953af unmoved —
CORPUS TRUTH GREEN before and after the bake: {C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, {C_OPEN} open); build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows —
+{DJ} on the fold layer since 11b's chain, the tape unmoved since 11b); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — no receipt, no header,
no footer in chapter 14; 14:4's "this is the beast" a list's header, not a register's; the number verses 14:6 and 14:28 no count lines — as the design predicted);
large_letter_probes {LL[-3:]}; the labels census GREEN ({LN}, Deuteronomy 89); the home-path gate GREEN; the display layer +{OV_REF14} by reference and +49 by gloss
({OV_REF} / {OV_GL} in all).

THE READING: every Onkelos row whole in the Aramaic and the English (ch14_onkelos.txt); THE SPINE ON THE CHAPTER A SIXTH TIME — fourteen piskaot 97-110 heading on
the chapter's verses NOT IN VERSE ORDER (98 on 14:6 before 99 on 14:3 and 100 on 14:4; three piskaot on 14:6) AND PISKA 96'S TAIL (rows 9-12 on 14:1, left by
chapter 13's sitting — 96:9, 96:11 and 96:12 by their citations, 96:10 by its consonants with Amos 9:6 alone in its brackets: chapter 13's lesson 1 closed), every
row read whole in both files (ch14_sifrei_spine.txt, split by piska for the reading — ch14_spine_p96.txt (rows 9-12) … p110.txt); the three outside rows whole in
both files (ch14_sifrei_outside.txt — flesh in milk at 12:23, reread whole from chapter 12; the bird's nest at 22:7; the LORD's portion at 32:9), none excluded;
the kin (Leviticus 11 THE TWIN CHAPTER in two ledgers, 17:15, 19:10, 19:27-28, 20:26, 21:5, 22:8, 23:22, 27:30-33; Exodus 22:30, 23:19; Numbers 18:20-32;
Deuteronomy 7:6, 10:9, 10:18, 12:5-26) credited by name with the counts computed from fourteen ledgers; no ledger holds an Onkelos row of Genesis 7, 14 or 28, of
Exodus 19, 23:10-11 or 34:26, and NONE OF DEUTERONOMY 15-26 OR THE PROPHETS (asserted — never read ahead; the release at 15:1, the firstling at 15:19-23, the
rejoicing with the four at 16:11-14, the blemished offering at 17:1, the Levite at 18:1, the bird's nest at 22:6-7, the gleanings at 24:19-21, the tithe confession
at 26:12-14, the rejoicing at 27:7, the assembly at 31:10 wait for their own sittings).

THE DEPARTURES FROM THE DESIGN: one in the run's shape, four in the tail's instruments. (1) THE CLEAN POINT AFTER ALL THE ROWS, NOT BETWEEN THE HALVES — the design
had made the halfway point conditional on the counter, and the counter is not /context: 657.8k where the estimate stood near 470k (the #204 NOTE; the rule for the
next reading below). (2) THE LEDGER IN THE TAIL — written after the compaction from the five row files on disk, clean on its first run (143 sources, no MISMARK, no
cut missed). (3) THE INK'S PATCH BLOCK (body C) WRITTEN BEFORE THE LEDGER — the ledger reads the patch's prediction (49 by gloss, 131 by reference) from the ink's
own lists, as chapter 13's did; the fourth pass green. (4) THE FIFTH PASS FELL ON ONE ASSERT OF THE INSTRUMENT'S OWN MAKING — the count of the chapter's glosses
"already" in the overrides grew by this sitting's forty-nine once the patch ran; the two counting asserts made patch-aware (the store's "already" = the chapter's
glosses in the overrides minus this sitting's), the sixth pass green: A COUNTING ASSERT ON THE OVERRIDES MUST KNOW WHETHER THE PATCH HAS RUN. (5) THE MANIFEST'S
CHECK WORDS PROBED IN THE STORE FIRST — the store splits a word into pieces and the check is the longest piece whole with a floor of four code points: "three"
(three letters) and the design's "you shall not cut yourselves" (one piece, fourteen code points pointed) measured before the seven words were typed — 14:1
"cut yourselves", 14:6 "parts", 14:11 "bird", 14:21 "a kid", 14:22 "you shall tithe", 14:25 "bind up", 14:28 "at the end of"; the manifest wrote first time. THE
SHELLS' DERIVE PROTECTED THE FORM'S NAME (chapter 12's lesson 12; chapter 13's forms the source — nothing retyped). THE DISPLAY PATCH held first time (twelve
asserted substitutions on the chapter-13 form with its portable header stripped; the anchors sitting 11's last rows found by walking, never typed; {PATCH_LINE}).
THE MIDDAH CODES held — every code checked in MIDDOT.md before it was typed, none relabeled: the census from the ledger's rows — {CODE_TXT}; "the verse compares"
(the juxtaposition) named at 106:4-5 by the shelf's own word, no code. {CHAIN_NOTE}

THE GATES, COMPUTED FROM THEIR PRINTS: the ritual {N_PASS} PASS (RITUAL COMPLETE, {C_UNITS} frozen units); CORPUS TRUTH GREEN twice ({C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, {C_OPEN} open;
the hash unmoved); build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows, +{DJ}); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL});
verify_claims 7 verified / 0 failed; the labels census GREEN ({LN}); large_letter_probes {LL[-3:]}; the home-path gate GREEN; the ink {N_INK} asserts — the six passes
{INKF[1]} / {INKF[2]} / {INKF[3]} / {INKF[4]} / {INKF[5]} / {INKF[6]} failing (the first the instrument's shapes and three lists from memory, the second two facts from the print's tuple,
the third green, the fourth green with the patch's block, the fifth the "already" count, the sixth green PATCHED).

⚠ THE LESSONS (the run's, gathered — the numbered list the sheet asks for): (1) THE 600k CAP WAS PASSED A SECOND TIME BY /context, NOT BY THE COUNTER — 657.8k at
the clean point after the rows where the run's own estimate stood near 470k, the estimate 170k short (sitting 11's lesson 4 repeated, its remedy not taken far
enough): A READING OF A CHAPTER THIS SIZE IS TWO RUNS + THE TAIL, like a compile — the measurements, the ink and the design one run to a clean point; the rows and
the ledger a second; the tail the third; the clean point after the first half of the rows UNCONDITIONALLY, never on the counter's word (the #204 NOTE; the cost
rules' memory amended). (2) THE INSTRUMENT'S SHAPE, NOT THE FACT — twenty-seven asserts fell on the ink's first typed pass and not one was a fact: the word table's
pairs where the measure held five-tuples, the Aramaic helper's string where the measure returned tokens, the book-alone name the measure's, and three lists typed
from memory against the print (the antelope's letters Ezekiel 40's cells, the ra'ah's the verb "see", the desire clause's vav); two on the second (the ra'ah's two
homograph seats, the sojourner's rendering at 28:43 misassigned from the print's tuple): the ink is retyped from the print, never from the hand. (3) A COUNTING
ASSERT ON THE OVERRIDES MUST KNOW WHETHER THE PATCH HAS RUN — the fifth pass's one fail. (4) A PISKA'S TAIL FOLDED IN — 96:9-12 read here by citation and by
consonants, chapter 13's lesson 1 closed: the two files' union left 96:10 (it cites nothing) and the consonant rule fetched it. (5) THE HEADS OUT OF VERSE ORDER —
the shelf's order is the argument's, not the verse's (98 on the signs before 99 on the abomination and 100 on the list): the reading goes by position, the claims by
the CITE INDEX's distribution, and no assert may assume the heads climb. (6) THE TWIN CHAPTER DIFFED VERSE BY VERSE IS THE READING'S OWN INSTRUMENT — 14:6 is 11:3
with "two", 14:15 is 11:16 to the letter, 14:7 folds 11:4-6's three into one, 14:9 twelve of 11:9's twelve with the seas and the rivers dropped, the vocabulary
changed ("abomination" and "unclean" for "detestable"), the locusts absent, the ra'ah's resh for the da'ah's dalet — and the shelf names the two added names as
the whole gain of the restatement (98:6): the ink and the shelf agree on what the chapter adds and differ on what it drops. (7) THE PERMITTED BIRDS HAVE NO SIGN
IN THE INK — the exam's four signs come from the answer sheet inside the spine (103:8 — Mishnah Chullin 3:6 in the row's own Hebrew): the compile's parameter
the_birds_signs is DATA, the code/data separation law's own case. (8) ONE NOUN, TWO PERSONS IN ONE CHAPTER — the sojourner who eats the carcass (14:21, the
resident alien — 104:2, Onkelos "uncircumcised") and the sojourner who eats the poor man's tithe (14:29, the convert — 110:2, Onkelos "the convert"): a parameter
for 12b's cell, the shelf and the translation agreeing. (9) THE KIN BY COMPUTATION AGAIN — 14:2 is 7:6 (eighteen of nineteen), 14:24 holds 12:21's clause (twelve
in order), 14:29 has 24:19's clause (seven), 14:5's one kin in the Bible Solomon's table, 14:28's Samaria's fall, 14:29's own closest 14:27. (10) THE CUT'S ONE
MISS THE EXPORT'S OWN SPELLING — "casually" without the aleph at 105:16, retyped from the export: the cut reads the shelf's bytes, never the dictionary's. (11)
THE MANIFEST'S CHECK WORDS PROBED FIRST — the store's pieces measured before the seven words were typed (the floor four code points). (12) THE FAST STEPS IN THE
FOREGROUND, THE CHAIN BEHIND — sitting 11's lesson 8 held: the manifest, the verifier and the census read before the ritual froze the unit; the chain launched
with the records writer and the copier typed during its run. (13) EVERY STEP TIMED — the machine's share of the sitting {mmss(T_MACH)} of {mmss(T_TOTAL)} wall time
from {T_START} to the records; the rest the reading, the typing and one compaction: the reading is the sitting, the machine its instrument.

THE TIMING TABLE (every row appended by the scratchpad's timer as the step ran; the gap column is the time between one step's end and the next step's start — the
reading of the rows, the typing of the scripts, the owner's compaction between the clean point and the tail's rereads; the chain's inner steps from its own summary's
stamps):

{TT}

The chain's inner steps (ch14_gates_SUMMARY.txt): {CS_TXT}; the chain {mmss(CS_TOTAL)} in all. The machine's share {mmss(T_MACH)}; the sitting {mmss(T_TOTAL)} from {T_START}
to the last row above; the records writer's own row and the copier's follow in ch14_timing.tsv (copied into the forms).

THE FORMS: World/step9/forms_deuteronomy_walk/ (copy_ch14_forms.py — derive_ch14_dump0.py, ch14_dump0.py, derive_ch14_measure1.py, ch14_measure1_sections.py,
ch14_measure1.py, split_ch14_spine.py, ch14_ink_head.py, ch14_ink_body.py, ch14_ink_body_b.py, ch14_ink_body_c.py, derive_ch14_ink.py, ch14_ink.py, assert_driver.py,
the five row files, write_ch14_ledger.py, write_ch14_design.py, write_ch14_cleanpoint.py, derive_ch14_patch.py, ch14_patch_overrides.py, write_ch14_manifest.py,
seat_ch14.py, derive_ch14_shells.py, ch14_chain.sh, ch14_fold.sh, ch14_gates.sh, tstep.sh, write_ch14_records.py, copy_ch14_forms.py, the prints, the split
piskaot and ch14_timing.tsv).

NEXT on the ruling: the commit on the owner's word (chapter 13's compile and chapter 14 stand uncommitted since fb797a1 — ONE message at <scratch>/commit_msg_ch14.txt
carries both); then THE COMPILE OF CHAPTER 14 (sitting 12b) in TWO RUNS + THE TAIL under the cost rules — RUN A: the rereads (THE_STEPS Step 5 + the compiler
block; this section; the 12b box in COMPILE_DEBT), the measurements (Leviticus 11's cells for the beasts', the fish's and the birds' signs; Exodus 23:19's cell for
the kid; Leviticus 17:15's and 22:8's for the carcass; Numbers 18's and Leviticus 27's for the tithes; chapter 12's place cells and eras table; 10:9's and 12:12's for
the Levite; the register's finder at 14:4, 14:6, 14:28), THE DESIGN (the food laws as cells — the two signs with the four exceptions as the written exception set,
the water's two, the birds' twenty-one with the_birds_signs a PARAMETER from the answer sheet, the carcass table with R. Judah's dissent a PARAMETER, the kid's
three readings; the second tithe as a status with the wall, the House and the year its conditions, the money's form two arms, the far place by CALL to chapter 12's
cell, the rejoicing a peace offering; the third year's tithe with the removal's date a CLOCK DATUM and the four at the gate with the sojourner two persons; the
checkpoint series DF), the probes to FAIL, THE DOCKET by the union rule (Mishnah Chullin 3:6-7, 8:1-4, 4:4, 1:7 with Chullin 59a-66b, 80a, 113a-116b, 72b-73a,
68a-69a, 77a; Mishnah Makkot 3:5-6 with Makkot 20a-21a; Yevamot 13b-14a, 47b, 86a-b; Kiddushin 36a, 54b; Mishnah Maaser Sheni 1-5 with its folios; Mishnah
Maasrot 1:1, 1:3, 2:4, 4:5-6; Rosh Hashanah 12a-13a; Bekhorot 34a-35a, 53b; Mishnah Temurah 6:1; Mishnah Eduyot 3:2; Pesachim 21b, 50b-51a; Bava Metzia 88a;
Mishnah Zevachim 5:8; Mishnah Peah 8:5-9 with Tosefta Peah 4:2, 4:11; Tosefta Kilayim 1:9; Tosefta Sanhedrin 3:5-6; Avot 3:9, 3:14; the Sifra on Leviticus 11, 19 and
27 credited from their sittings — every row whole; a docket past ~700 rows its own run); RUN B: the types, the runner, the tape to 10/10, the chain LAUNCHED; THE
TAIL the records, the forms, the message — or the Decalogue-schema sitting first, on his word.
'''

DEBT = f'''

## SITTING 12 — CHAPTER 14 ({DATE}, the reading; deu_14_food_tithe frozen) — OWED TO THE COMPILE 12b: (a) THE CUTS AND THE BALDNESS (14:1) — the mourner's cut and
## no factions (96:10-11; Yevamot 13b-14a), the baldness by the analogy run both ways with the priests' 21:5 (96:12 — I2; Mishnah Makkot 3:5-6; Makkot 20a-21a):
## the count of lashes and "for the dead" the conditions; the sonship's two arms (96:9 — Kiddushin 36a); (b) THE SIGNS OF THE BEASTS (14:6-8) — the three signs
## from the three clauses (98:1), THE FOUR NAMED THE EXCEPTION SET AND THE SIGN THE CLASS (101:10 — I1; Chullin 59a, 60b, 66b; Mishnah Chullin 3:6-7), the cleft
## one a creature (98:2 — Chullin 60b), the license by the names for the altar's disqualified (101:1-9 — Mishnah Temurah 6:1), the afterbirth (101:7 — Chullin
## 68a-69a, 77a); Leviticus 11:3-8 by CALL — THE TWIN CHAPTER'S CELLS; (c) THE WATER (14:9-10) — fins and scales, Leviticus 11:9-12 by CALL (Chullin 66a-b); (d)
## THE BIRDS (14:11-20) — THE PERMITTED BIRDS HAVE NO SIGN IN THE INK: the_birds_signs a PARAMETER FROM THE ANSWER SHEET (103:8 — I3; Mishnah Chullin 3:6 in the
## row's Hebrew; Chullin 59a, 61a-65a), the lexicon rule "bird" = clean (98:3; 228:5 — I3), the list carried by its head (103:3-4 — I2), the counting rule (100:2,
## 103:7), the locusts in the frames (103:10 — Chullin 65a-66a; Leviticus 11:21-22 by CALL), the ra'ah and the dayyah (98:5-6 — Chullin 63b); (e) THE CARCASS
## (14:21) — THE FOUR-CELL TABLE of the two verbs over the two persons against R. Judah's "as written" (104:5-6 — Pesachim 21b): A PARAMETER WITH TWO ARMS; the
## torn from "any" (104:1 — Chullin 72b-73a; Mishnah Chullin 4:4), the resident alien (104:2), the custom's bar (104:7 — Pesachim 50b-51a); Leviticus 17:15, 22:8
## and Exodus 22:30 by CALL; (f) THE KID'S THREE READINGS (14:21) — the three covenants (104:8), R. Akiva's three exclusions (104:9 — Mishnah Chullin 8:4; Chullin
## 113a-116b), the fowl out by "its mother's milk" (104:10), the eating at 12:24's clause (76:7 — I1; Chullin 115b): the cooking, the eating, the benefit — three
## laws from one verse said three times; Exodus 23:19 by CALL, 34:26 through its spine; (g) THE SECOND TITHE (14:22-27) — NAMED THE SECOND by the shelf (105:2;
## Numbers 18 the first by CALL), THE LIABILITIES from the verse's clauses (105:1-19 — Mishnah Maasrot 1:1, 1:3, 2:4, 4:5-6; Rosh Hashanah 12b; Bekhorot 53b; Bava
## Metzia 88a; Leviticus 27:30 and Numbers 18:27 by CALL), THREE STATUSES for the eating — the wall of Jerusalem (106:3 — I1; Mishnah Zevachim 5:8), the House
## standing (106:4 — the juxtaposition; Tosefta Sanhedrin 3:6), the year passed no bar (106:5), the firstling from outside the Land not brought (106:2 — Tosefta
## Sanhedrin 3:5; 15:19-23 ahead by CALL when it comes), the study (106:6); THE FAR PLACE — of place not time, any distance, the rich too (107:1-3 — Mishnah Maaser
## Sheni 1:1?; 12:21's clause by CALL to chapter 12's cell), THE MONEY'S FORM TWO ARMS (107:4 — I1; Mishnah Eduyot 3:2), the possession (107:5 — Mishnah Maaser
## Sheni 1:2), Shiloh and the eternal House (107:6 — the eras table by CALL), THREE MONEYS THE LAW'S TABLE (107:7 — Mishnah Maaser Sheni 3:10), the class from the
## four named (107:8-11 — I3; Mishnah Maaser Sheni 1:5, 1:7, 2:1), the containers (107:12-15 — Mishnah Maaser Sheni 1:3; Mishnah Chullin 1:7), THE REJOICING A
## PEACE OFFERING (107:16 — I2 with 27:7 ahead), THE LEVITE'S LADDER OF FOUR (108:1 — a status with four sources; 10:9, 12:12 and Numbers 18:20-24 by CALL); (h)
## THE THIRD YEAR (14:28-29) — THE REMOVAL'S DATE A CLOCK DATUM: the eve of the last festival day of Passover of the fourth and the seventh year (109:1-3 — I2 with
## 31:10 ahead; 26:12 ahead; Mishnah Maaser Sheni 5:6), the seventh year exempt (109:4 — Exodus 23:10-11 through its spine; 15:1 ahead), ONE TITHE NOT TWO — the
## poor man's replaces the second (109:5, 109:10-11 — Numbers 18:21 by CALL), the vegetables' year (109:8 — Rosh Hashanah 12a-13a), the gifts exempt (109:12 —
## Leviticus 19:9-10, 23:22 by CALL), THE FOUR IN WANT AND SONS OF THE COVENANT (110:1-2 — I3; Mishnah Peah 8:5-9; Yevamot 47b, 86a-b), THE SOJOURNER TWO PERSONS
## (14:21 the resident alien, 14:29 the convert — a PARAMETER of the noun), the measure half a kav (110:3 — Tosefta Peah 4:2), the Land (110:4); (i) THE EFFECTS —
## "a holy people" the ground of the cutting's bar and the custom's bar (97:1, 104:7), the sonship (96:9), "learn to fear" the tithe's effect (106:6), the blessing
## on the work of the hand (14:29); (j) THE PLACE FORMULA at its fourth and fifth seats — 12b reads chapter 12's cells by CALL (the Shekhinah's nine seats in
## Onkelos measured); (k) THE KIN BY CALL — Leviticus 11 whole, 17:15, 19:10, 19:27-28, 20:26, 21:5, 22:8, 23:22, 27:30-33; Exodus 22:30, 23:19; Numbers 18:20-32;
## 7:6, 10:9, 10:18, 12:5-26; (l) NEVER READ AHEAD — 15:1, 15:19-23, 16:11-14, 17:1, 18:1, 22:6-7, 23:21, 24:17-21, 26:12-14, 27:7, 31:10, 32:9 wait for their
## sittings — their cells by CALL when they come; (m) THE REGISTER's DATA rows — the chapter split in two (the food laws plural, the tithe singular, 14:21 both),
## no imperative, no "if" (the one case on "and when" at 14:24), no first person, no narrative verb, the two number verses [2] and [3], the starred tithe tokens,
## no written/read pair; (n) THE CHECKPOINT SERIES continues (DE the fifth name — DE9 the last; the next DF1, keyed by its first word); (o) THE DOCKET by the union
## rule — the testing shelf as the design and the AS BUILT list it (Mishnah Chullin 3:6-7, 8:1-4, 4:4, 1:7 and Chullin 59a-66b, 80a, 113a-116b, 72b-73a, 68a-69a,
## 77a; Mishnah Makkot 3:5-6 and Makkot 20a-21a; Yevamot 13b-14a, 47b, 86a-b; Kiddushin 36a, 54b; Mishnah Maaser Sheni 1-5 with Kiddushin 54b; Mishnah Maasrot
## 1:1, 1:3, 2:4, 4:5-6; Rosh Hashanah 12a-13a; Bekhorot 34a-35a, 53b; Mishnah Temurah 6:1; Mishnah Eduyot 3:2; Pesachim 21b, 50b-51a; Bava Metzia 88a; Mishnah
## Zevachim 5:8; Mishnah Peah 8:5-9 with Tosefta Peah 4:2, 4:11; Tosefta Kilayim 1:9; Tosefta Sanhedrin 3:5-6; Avot 3:9, 3:14; the Sifra on Leviticus 11, 19 and 27
## credited from their sittings) — EVERY ROW WHOLE; a docket past ~700 rows its own run; THE COST RULES: two runs + the tail, the chain launched at RUN B's end;
## A READING IS TWO RUNS + THE TAIL from now (the #204 NOTE). NOTHING ELSE IN CHAPTER 14 IS OWED TO A LATER SITTING OF ITS OWN.
'''

MIDDOT = f'''- **THE SIFREI ON DEUTERONOMY'S OWN CASE LAW ON CHAPTER 14 (Deuteronomy 14:1-29; THE DEUTERONOMY WALK sitting 12, {DATE};
  the ledger logic/oral_triage/deu_14_reeh_{LDATE}.md — THE SPINE ON THE CHAPTER A SIXTH TIME, piska 96's tail (rows 9-12 on 14:1) and
  piskaot 97-110 with the heads not in verse order, {L_SPINE} rows read whole in both files, and three rows outside the spine; EVERY CODE
  CHECKED IN MIDDOT.md BEFORE IT WAS TYPED, none relabeled; the census from the ledger's own rows: {CODE_TXT}):**
  · THE A-FORTIORI FROM THE FOUR TO THE REST (101:10 on 14:7-8): if the camel, the hare, the rock-badger and the swine, which have signs
    of cleanness, are under a prohibition, the rest, which have none, how much more — I1 (checked; the row's own words קַל וָחוֹמֶר ("an
    a fortiori") on its bytes): THE WRITTEN LIST THE EXCEPTION SET, THE SIGN THE CLASS — the compile's rule for the beasts' cell; the
    answer sheet Mishnah Chullin 3:6-7 and Chullin 66b at 12b's docket.
  · THE A-FORTIORI REFUTED, THEN THE VERSE (76:7 on 12:24 for 14:21; 106:3 and 106:4 on 14:23; 107:4 and 107:7 on 14:25-26): flesh in milk
    from the carcass, refuted by mixed seeds; the wall from the firstling, refuted by the firstling's narrow time; the House standing from
    the firstling, twice refuted — the first-fruits prove and are refuted; the money from consecrated property, refuted by its movables;
    the second money from the tithe, overridden by THE COUNT OF THE WORD (three "money" tokens at 14:25-26 — the ink's count the law's
    table) — I1 (checked at each seat): the shelf's pattern that a reasoning proposes and the verse decides.
  · THE VERBAL ANALOGY OF BALDNESS, RUN BOTH WAYS (96:12 on 14:1): "baldness" is said here and "baldness" is said there (Leviticus 21:5)
    — the priests' verse gives Israel the whole head and the count, Israel's verse gives the priests "for the dead" — I2 (checked; גְּזֵרָה
    שָׁוָה ("a verbal analogy") on its bytes); THE INK: the Torah's two seats of the word, computed.
  · THE VERBAL ANALOGIES OF THE LIST (99:2 on 14:3; 103:3 on 14:12; 103:4 on 14:13): "abomination" here and at 17:1 — the disqualified
    consecrated; "eagle" here and at Leviticus 11:13 — the whole list under "do not feed" and "do not eat"; "ayyah" here and there — the
    ra'ah a kind of ayyah — I2 (checked at each seat): the list carried by its head from the twin chapter.
  · THE VERBAL ANALOGIES OF THE TITHE (107:16 on 14:26; 109:2 on 14:28): "rejoicing" here and at 27:7 — peace offerings, then the verse's
    own pair "eat and rejoice" limits it; "end" here and at 31:10 — a pilgrimage festival, then 26:12's "finished" picks Passover — I2
    (checked at both seats; 27:7 and 31:10 never read ahead, recorded from their seats): THE REMOVAL'S DATE COMPUTED FROM TWO VERSES.
  · THE PARADIGM OF THE BIRD (98:3, 228:5 on 14:11): wherever "bird" is said, Scripture speaks of a clean one — applied at the bird's nest
    (22:7) — I3 (checked; the row's own words בִּנְיַן אָב ("a paradigm") on its bytes); THE PARADIGM OF THE EAGLE (103:8 on 14:12): no crop,
    no extra toe, no peelable gizzard, seizes and eats — THE PERMITTED BIRDS HAVE NO SIGN IN THE INK, the signs the answer sheet's
    (Mishnah Chullin 3:6 in the row's Hebrew) — I3 (checked): the code/data separation law's own case inside the spine.
  · THE PARADIGMS OF THE TITHE (105:8 on 14:22; 107:11 on 14:26; 110:1 and 110:2 on 14:29): the paradigm from grain — rice, millet, poppy
    and sesame — OVERRIDDEN by the doubled verb; the four named as the father of the class — fruit from fruit and of the earth, water and
    salt out; the poor's want from Leviticus 19:10 and the covenant's sons from the Levite — I3 (checked at each seat): THE SOJOURNER OF
    14:29 THE CONVERT against 14:21's resident alien, one noun two persons.
  · "THE VERSE COMPARES" (106:4-5 on 14:23): the firstling's eating compared to the second tithe's — only while the House stands; the
    firstling past its year still fit — the juxtaposition, named by the shelf's own word (מַקִּישׁ — "compares") without a code.
  · THE COUNTING RULE (100:2 on 14:4; 103:7 on 14:15-17): everywhere Scripture specifies the fewer — the unclean beasts by name because
    fewer, the unclean birds by name because fewer, the clean by a frame — named without a code.
  · THE TWO VERBS OVER THE TWO PERSONS (104:5 on 14:21): give and sell crossed over the sojourner and the foreigner into a four-cell
    table, against R. Judah's "the words as they are written" (104:6) — named without a code; a PARAMETER with two arms at 12b.
  · THE THREE SEATS THREE WAYS (104:8-10 on 14:21): the kid's verse said three times — the three covenants; the wild beast, the fowl and
    the unclean beast excluded; the fowl out by "its mother's milk" — and the eating at 12:24 (76:7): one verse, three laws — named
    without a code.
  · NAMED WITHOUT A CODE: the sonship two-armed (96:9); no factions from the letters (96:10); "sanctify yourself" at both seats of "a holy
    people" (97:1, 104:7); each one beloved, not above the fathers (97:4-5); the three signs from the three clauses (98:1); the cleft one
    a creature (98:2); why the names were repeated (98:6); the license by the names (101:1-9); "was Moses a hunter" (102:1); the second
    tithe named (105:2); the liabilities from the clauses (105:1-19); the way's distance of place (107:1-3); Shiloh and the eternal House
    (107:6); the Levite's ladder of four (108:1); one tithe not two (109:5, 109:10-11); the measure half a kav (110:3); who chose whom (312:1).
'''

RESEARCH = f'''

## {DATE} — DEUTERONOMY 14 READ AND FROZEN (THE DEUTERONOMY WALK sitting 12 — a reading sitting under THE COST RULES: one run to the clean point #204 after the
## rows, the compaction, the tail; EVERY STEP TIMED): THE TWIN CHAPTER DIFFED VERSE BY VERSE; THE PERMITTED BIRDS WITHOUT A SIGN IN THE INK; THE KID'S THIRD SEAT
## THREE WAYS; THE SECOND TITHE'S THREE STATUSES; THE REMOVAL'S DATE COMPUTED FROM TWO VERSES; ONE NOUN TWO PERSONS; AND THE CAP PASSED BY /context A SECOND TIME
On the owner's "Go" after 11b's tail ({DATE}). THE READING: Deuteronomy 14:1-29 with Onkelos whole (the export's 29 rows the DB's 29 — the identity, asserted) and
THE SIFREI ON DEUTERONOMY ON THE CHAPTER A SIXTH TIME — piska 96's rows 9-12 on 14:1 (left by chapter 13's sitting; 96:10 folded in on its consonants, Amos 9:6
alone in its brackets) and fourteen piskaot 97-110 whose heads are NOT IN VERSE ORDER (98 on 14:6 before 99 on 14:3 and 100 on 14:4; three piskaot on 14:6),
{L_SPINE} rows read whole in both files ({N_REREAD} read before — the kid's three covenants at chapter 6, the firstling's year at chapter 12 — and reread whole, found by
computation), three rows outside the spine read whole (76:7 flesh in milk at 12:23, reread whole from chapter 12; 228:5 the bird's nest at 22:7; 312:1 the LORD's
portion at 32:9), none excluded; the kin credited by name from fourteen ledgers (Leviticus 11 the twin chapter, 17:15, 19:10, 19:27-28, 20:26, 21:5, 22:8, 23:22,
27:30-33; Exodus 22:30, 23:19; Numbers 18:20-32; Deuteronomy 7:6, 10:9, 10:18, 12:5-26); NEVER READ AHEAD — no Onkelos row of Deuteronomy 15-26 or the Prophets in
any ledger (asserted). FROZEN as ONE unit deu_14_food_tithe (the 228th; no portion edge inside it; standing 2252 = 2245 + 7 as predicted, hash unmoved); the
ledger deu_14_reeh_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the spine {L_SPINE}: MATERIAL {L_SM} / CONTEXT {L_SC}; the outside rows {L_OUT}: MATERIAL
{L_XM} / CONTEXT {L_XC}; coverage computed, lint 0, no cut missed, written clean on its first run); seven claims DV14-01..07 verified 7/0, seated as seven WITNESS_READ at
14:1, 3, 9, 21, 22, 24, 28; the ritual {N_PASS} PASS; the fold +{DJ} on the journal; the display layer +{OV_REF14} by reference and +49 by gloss (the beasts' and the birds'
names, the hoof, the carcass, the strong drink, "unclean" for forty-eight tokens). THE FINDS: THE TWIN CHAPTER DIFFED — 14:6 is Leviticus 11:3 with "two hoofs"
(the number verse [2]), 14:15 is 11:16 to the letter, 14:7 folds 11:4-6's three into one, 14:9 twelve of 11:9's twelve with the seas and the rivers dropped, the
vocabulary changed ("abomination" and "unclean" for "detestable"), the locusts absent, the ra'ah's resh for the da'ah's dalet — and the shelf's reason for the
restatement the two added names (98:6); THE THREE SIGNS FROM THE THREE CLAUSES (98:1), THE CLEFT ONE A CREATURE (98:2), THE FOUR NAMED THE EXCEPTION SET AND THE
SIGN THE CLASS (101:10 — I1), "WAS MOSES A HUNTER" (102:1); THE PERMITTED BIRDS HAVE NO SIGN IN THE INK — the signs the answer sheet's from the eagle as the
father (103:8 — I3, Mishnah Chullin 3:6 inside the spine); THE LEXICON RULE "bird" = clean at the bird's nest (98:3, 228:5); THE LIST CARRIED BY ITS HEAD (103:3-4
— I2); SCRIPTURE SPECIFIES THE FEWER (100:2, 103:7); THE LOCUSTS IN THE FRAMES (103:10); "A HOLY PEOPLE" three in the Bible and 14:2 is 7:6 with one word
dropped, "sanctify yourself" at both seats (97:1, 104:7); THE SONSHIP TWO-ARMED (96:9); THE CUTTING READ THREE WAYS with the baldness by analogy both ways (96:10-12
— I2); THE CARCASS GIVEN NOT CAST — no clause shared with its three kin, the four-cell table against R. Judah's "as written" (104:5-6); THE KID'S THIRD AND LAST
SEAT THREE WAYS (104:8-10) with the eating at 12:24 (76:7 — I1); "TITHE, YOU SHALL TITHE" the doubling's one seat with the tithe's liabilities from the verse's
clauses (105) and the second tithe NAMED (105:2); THE FIRSTLING AND THE SECOND TITHE ONE VERSE — the wall, the House standing, the year passed (106:2-5: three
statuses; I1 refuted, "the verse compares"); THE WAY OF PLACE NOT TIME (107:1-3); THE MONEY'S FORM TWO ARMS (107:4 — I1); THREE MONEYS FROM THE INK'S COUNT (107:7);
the class from the four named (107:8-11 — I3); THE REJOICING A PEACE OFFERING (107:16 — I2); SHILOH AND THE ETERNAL HOUSE (107:6); THE LEVITE'S LADDER OF FOUR
(108:1); THE REMOVAL'S DATE COMPUTED — Passover's last day of the fourth and the seventh year (109:1-3 — I2); ONE TITHE NOT TWO (109:5, 109:10-11); THE FOUR IN
WANT AND SONS OF THE COVENANT — the sojourner of 14:29 the convert against 14:21's resident alien (110:1-2 — I3); THE REGISTER SPLIT IN TWO (the food laws plural,
the tithe singular, 14:21 both), no "if", no imperative, no first person, Moses' voice alone; THE PARSER: two number verses ([2] at 14:6, [3] at 14:28) and the
starred tithe tokens; THE STORE = THE DB (no written/read pair); ONKELOS: incisions, beloved, what is removed, the seven wild in Aramaic names, the daughter of
the wing, FLESH WITH MILK for the kid (the law not the verse), the uncircumcised sojourner and the convert, the Shekhinah at the place's two seats, new wine and
old. THE COST RULES: one run to the clean point #204 after ALL the rows, THE CAP PASSED BY /context A SECOND TIME (657.8k where the estimate stood near 470k — the
#204 NOTE: A READING OF THIS SIZE IS TWO RUNS + THE TAIL, the clean point after the first half of the rows unconditionally), the owner's compaction, the tail on a
small context — the ledger, the patch, the manifest, the seat, the fast steps in the foreground before the freeze, the chain in the background with the writers
typed during its run; EVERY STEP TIMED — the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)} wall time from {T_START}; the table in the map's AS BUILT. THE CAUTIONS: the
ink's twenty-seven first-pass fails all the instrument's; the "already" count grown by the patch itself; the cut's one miss the export's spelling; the heads out
of verse order. THE LESSONS (thirteen, in the map): the cap by /context a second time and the two-runs rule; the instrument's shape not the fact; the counting
assert patch-aware; the piska's tail folded in; the heads out of order; the twin chapter diffed; the birds' signs data; one noun two persons; the kin by
computation; the cut's miss the export's; the checks probed first; the fast steps in the foreground; every step timed. OWED TO 12b: the cuts and the baldness, the
beasts' signs with the four the exception set, the water, the birds' signs a parameter, the carcass table, the kid's three readings, the second tithe's three
statuses with the money's two arms and the rejoicing, the third year's date and the four with the sojourner two persons, the effects, the place formula by call,
the kin by call, never-read-ahead's cells, the register's rows, the series DF, the docket.
'''

STEPS = f'''DEUTERONOMY — SITTING 12 — CHAPTER 14, Deuteronomy 14:1-29 ({DATE}, on Brian's "Go" after chapter 13's compile; World/step9/DEUTERONOMY_WALK.md "Sitting 12" and
"Sitting 12 — AS BUILT"; a reading sitting of a chapter this size is now two runs to two clean points, then the tail). Chapter 14 is the food laws and the tithe.
You are children of the LORD — do not cut yourselves or shave a bald patch for the dead, for you are a holy people. Eat no abomination: these are the animals you
may eat, the ox, the sheep, the goat and seven wild kinds — anything that parts the hoof in two and chews the cud — but not the camel, the hare, the rock-badger,
which chew and do not part, nor the swine, which parts and does not chew. From the water, what has fins and scales. Every clean bird, but not these twenty-one.
No carcass — give it to the sojourner in your gates or sell it to a foreigner; and do not boil a kid in its mother's milk. Tithe your produce every year and eat
it before the LORD at the place He chooses; if the place is too far, turn it into money, tie the money in your hand, go there and spend it on whatever you like
— oxen, sheep, wine, strong drink — and rejoice with your household, and do not forget the Levite. Every third year bring the whole tithe out and leave it in your
gates for the Levite, the sojourner, the orphan and the widow. Most of it is Leviticus 11 said again, so the two chapters were laid side by side verse by verse:
this one adds "two" to the hoof, names ten animals Leviticus does not, folds three animals into one verse, spells one bird with a different letter, drops the
locusts and the seas, and says "abomination" and "unclean" where Leviticus says "detestable" — and the tradition itself says the restatement exists for the two
names it adds. The tradition then supplies what the text does not have: the signs of a clean bird come from the answer sheet, not from the verse; the kid's verse,
said three times in the Torah, is read as three laws (do not cook, do not eat, do not benefit); the sojourner who may eat the carcass and the sojourner who eats
the poor man's tithe are two different people under one word; the second tithe may be eaten only inside Jerusalem's wall, only while the Temple stands, and from
one year into the next; "tie the money" is read two ways — a thing that can be bundled or a thing with a stamp on it; and the day the old tithes must be cleared
out is computed from two other verses to be the eve of the last day of Passover in the fourth and the seventh year. The Sifrei has fourteen sections on the
chapter, not in verse order, plus the four rows of chapter 13's last section that had spilled over; every row was read whole in both languages, with three rows
from elsewhere. The chapter is frozen as one unit, the 228th, the world's standing facts up by seven as predicted, its hash unmoved, every gate green. The run
stopped after all the rows — the context, when you read it, had passed the 600k cap a second time where my own count said far less, so from now a reading of a
chapter this size takes its first clean point after half the rows, no matter what the count says. You compacted, and the rest ran on a small context: the ledger,
the display fixes, the claims, the seat, the gates in the background while the records were typed. Every step was timed: the machine's own work came to
{mmss(T_MACH)} in a sitting of {mmss(T_TOTAL)}; the rest was the reading and the typing. Next: the commit on your word (chapter 13's compile and chapter 14 together);
then the compile of chapter 14 in two runs — the food laws as cells with the birds' signs a parameter, the carcass table, the second tithe as a status with its
three conditions, the removal's date on the clock — or the ten-commandments schema first.


'''

BRIEF = f'''- **CHAPTER 14 READ AND FROZEN — THE TWIN CHAPTER LAID BESIDE LEVITICUS 11 VERSE BY VERSE; THE CLEAN BIRDS HAVE NO SIGN IN THE TEXT, THE TRADITION SUPPLIES IT; THE KID'S VERSE READ AS THREE LAWS; THE SECOND TITHE'S THREE CONDITIONS; THE DAY THE TITHES ARE CLEARED COMPUTED FROM TWO OTHER VERSES; ONE WORD, TWO SOJOURNERS; AND THE CAP PASSED A SECOND TIME — A READING IS TWO RUNS NOW** ({DATE}; sitting 12, one run to a clean point and its tail; the ledger deu_14_reeh_{LDATE}.md — {L_ALL} sources, every row whole; the 228th unit; every gate green; the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)}).
'''
BRIEF_ENTRY = f'''### {DATE} — CHAPTER 14 READ: LEVITICUS 11 SAID AGAIN WITH TWO NAMES ADDED, THE BIRDS' SIGNS FROM THE ANSWER SHEET, AND THE TITHE'S CALENDAR

Chapter 14 restates Leviticus 11's food laws and adds the tithe. Laid side by
side verse by verse, the restatement adds one word to the hoof ("two"), names
ten animals the older chapter does not, folds three animals into one verse,
spells one bird with a different letter, drops the locusts and the seas, and
changes the vocabulary — and the tradition says outright that the chapter was
repeated for the two names it adds. What the text leaves open, the tradition
fills: the signs of a clean bird are not in any verse — they come from the
answer sheet, so in the machine they will be a parameter, not code. The
prohibition on cooking a kid in its mother's milk, said three times in the
Torah, is read as three laws. The sojourner who may eat the carcass and the
sojourner who eats the third-year tithe turn out to be two different people
under one word, and Onkelos writes them differently. The second tithe may be
eaten only inside Jerusalem's wall, only while the Temple stands, and from one
year into the next; and the day the old tithes must be cleared out is computed
from two other verses. The chapter is frozen as one unit, every gate green.
The run stopped after all the rows — the context, when read, had passed the
600k cap a second time where my own count said far less; from now a reading
of a chapter this size takes its first clean point after half the rows, no
matter what the count says. Brian compacted, and the rest ran on a small
context with the gates in the background while the records were typed. Every
step was timed: the machine's own work came to {mmss(T_MACH)} in a sitting of
{mmss(T_TOTAL)}.

'''

RESUME_NOTE = f'''# ⚠ THE DEUTERONOMY WALK sitting 12 ({DATE}; step9/DEUTERONOMY_WALK.md "Sitting 12" + "Sitting 12 — AS BUILT"): CHAPTER 14 READ AND FROZEN as ONE unit
# (deu_14_food_tithe, the 228th; standing 2252, hash unmoved) — THE TWIN CHAPTER DIFFED VERSE BY VERSE (14:6 = 11:3 + "two", 14:15 = 11:16, the ra'ah's resh), THE
# PERMITTED BIRDS WITHOUT A SIGN IN THE INK (103:8 — the answer sheet's parameter), the kid's third seat three ways (104:8-10; 76:7), the second tithe's three
# statuses (106:2-5), the money's two arms (107:4), the removal's date computed (109:1-3), the sojourner two persons (104:2, 110:2); the ledger deu_14_reeh_{LDATE}.md
# ({L_ALL} sources, every row whole; piska 96's tail folded in; the heads not in verse order); seven claims seated; the fold +{DJ} on the journal ({J_ROWS} rows); every gate
# green. A READING SITTING UNDER THE COST RULES, EVERY STEP TIMED (the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)}; THE CAP PASSED BY /context A SECOND TIME — a
# reading of this size is TWO RUNS + THE TAIL from now). NEXT on the owner's word: the commit (<scratch>/commit_msg_ch14.txt — chapter 13's compile and chapter 14
# together, uncommitted since fb797a1); then 12b — the compile of chapter 14 (the food laws as cells, the birds' signs a parameter, the second tithe a status; DF the next series).
'''

STATE = f'''
#204 ADDENDUM 1 ({DATE}, at the close of THE DEUTERONOMY WALK sitting 12 — CHAPTER 14's READING: THE TAIL after the compaction at #204, on the owner's "Reread" and "Go" — A CLEAN COMPACTION POINT): THE TAIL AS RUN on a small context: the rereads (the recovery page, the map's "Sitting 12 … THE DESIGN", MEMORY.md, the state doc's #204 and its NOTE; THE_STEPS' compiler block, Step 2's head and Step 5's head before the ledger); THE INK'S BODY C (the display patch predicted from the G print — 49 by gloss, 131 by reference; the fourth pass green); write_ch14_ledger.py derived from the forms' write_ch13_ledger.py (the five row files; the prior reads marked REREAD WHOLE — 104:8, 106:5 and the outside 76:7; coverage computed: the Sifrei 111 + 3, Onkelos 29, the kin's credits by name from the ink's counts) — the ledger clean on its first run ({L_ALL} sources, {L_BYTES:,} bytes, lint 0); ch14_patch_overrides.py derived from the forms' ch13_patch_overrides.py by twelve asserted substitutions with its portable header stripped (derive_ch14_patch.py), the yaml +{OV_REF14} by reference and +49 by gloss ({OV_REF} / {OV_GL}); the ink rerun PATCHED — the fifth pass fell on ONE assert of the instrument's own making (the chapter's glosses "already" in the overrides grew by this sitting's forty-nine once the patch ran; the two counting asserts made patch-aware), the sixth pass green ({N_INK} asserts); write_ch14_manifest.py (seven claims DV14-01..07 at 14:1, 3, 9, 21, 22, 24, 28 — the spine distributed by piska from the CITE INDEX itself, 96's tail with the first claim, the three outside rows with the claims whose verses they cite; every he_contains cut from the store's bytes, the seven words' pieces MEASURED first — "cut yourselves" 14:1, "parts" 14:6, "bird" 14:11, "a kid" 14:21, "you shall tithe" 14:22, "bind up" 14:25, "at the end of" 14:28); seat_ch14.py; ch14_chain.sh, ch14_fold.sh and ch14_gates.sh derived from chapter 13's forms with the form's name protected in every shell (derive_ch14_shells.py); THE FAST STEPS IN THE FOREGROUND — the manifest (every cite index name used), verify_claims (7/0) and the labels census ({LN}) read before the freeze; THE CHAIN LAUNCHED IN THE BACKGROUND (ch14_gates.sh — the seat, verify_text {VT_STEPS} steps / {VT_SCEN} scenarios, the ritual {N_PASS} PASS, the fold 227 → 228 / 2245 → 2252 with the hash unmoved, build_world, the journal gate {J_ROWS} rows (+{DJ} since 11b's chain), the register gate --strict DECLARED {R_DECL} / DEBT {R_DEBT} / FAILS {R_FAIL}, large_letter {LL[-3:]}, the home gate) — {CHAIN_NOTE}; the records writer and the copier typed during the chain's run, the notification the wake; THE RECORDS from the sheet in one call (write_ch14_records.py — the map's "Sitting 12 — CHAPTER 14 — AS BUILT" with thirteen lessons AND THE TIMING TABLE (computed from ch14_timing.tsv: the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)} from {T_START}; the chain's inner steps {CS_TXT}), COMPILE_DEBT's sitting-12 box (a)-(o) owed to 12b, MIDDOT's chapter-14 block with the codes censused from the ledger's rows ({CODE_TXT}), MISHNAH_TOPICS (seventeen heads routed to 12b), RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the scoreboard bullet and an entry), World/RESUME.md, this addendum, the addenda §59, the recovery page (section 2 under its cap; the sitting shapes' newest instances), the memory (the walk note and the index line under 17,000), the stamp row, THE COMMIT MESSAGE <scratch>/commit_msg_ch14.txt — chapter 14's with chapter 13's compile message beneath it); the forms copied (copy_ch14_forms.py). THE TREE: + logic/units/deu_14_food_tithe.yaml frozen (operators, step E, the anchor scenarios), logic/py_units/deu_14_food_tithe.py and ALL_UNITS.py (the ritual), logic/oral_audit/manifests/deu_14_food_tithe_claims.json, logic/oral_triage/deu_14_reeh_{LDATE}.md, logic/glosses/word_gloss_overrides.yaml, logic/corpus/CORPUS_TRUTH.py (228 / 2252), corpus_world.sqlite, World/journal/data/world.sqlite (the fold layer, gitignored), the records, the forms. NOT COMMITTED (since fb797a1): the docket and 11b (chapter 13's compile) and SITTING 12 — ONE message at <scratch>/commit_msg_ch14.txt carries both (chapter 13's message beneath chapter 14's) for the owner's word ("Commit" = no push; "commit push" = both). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. THE MEASURE OF THE RUN: /context read 657.8k at #204 (past the 600k cap a second time — the NOTE's rule: A READING OF A CHAPTER THIS SIZE IS TWO RUNS + THE TAIL, the clean point after the first half of the rows unconditionally; the cost rules' memory amended). NEXT ON THE RULING: the commit on his word; then CHAPTER 14's COMPILE (12b) in two runs + the tail under the cost rules (RUN A the rereads, the measurements, the design — the food laws as cells with the four exceptions the written exception set, the_birds_signs a PARAMETER from the answer sheet, the carcass table's two arms, the kid's three readings, the second tithe a STATUS with the wall, the House and the year, the money's form two arms, the far place by CALL, the removal's date a CLOCK DATUM, the sojourner two persons, the checkpoint series DF — and the docket by the union rule, its own run past ~700 rows; RUN B the types, the runner, the tape, the chain LAUNCHED; the tail the records) — or the Decalogue-schema sitting first; on the table: the chain's positions step at four workers as the standing form, the SUPPLIED forms, the calf's day marker, the registry's homographs, the receipt's third and fourth shapes, THE INSTALL HYPOTHESIS, the eras table's merge, the fast checker's cells' dry-run. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 12 — CHAPTER 14 — AS BUILT" (the newest section), MEMORY.md.
'''

ADDENDA = f'''
## §59 — THE DEUTERONOMY WALK sitting 12 ({DATE}): CHAPTER 14 READ AND FROZEN — the state doc's #204, its NOTE and its addendum 1; the map's "Sitting 12 — CHAPTER 14 … THE DESIGN" and "Sitting 12 — CHAPTER 14 — AS BUILT"; the owner: "Go" (a reading sitting under THE COST RULES), "/context" and "Ready to compact" at #204, "Reread" and "Go" after the compaction
THE READING: Onkelos Deuteronomy 14 whole (29 = 29, the identity); THE SIFREI ON THE CHAPTER A SIXTH TIME — piska 96's tail (rows 9-12 on 14:1, left by chapter
13's sitting; 96:10 folded in on its consonants) and piskaot 97-110 with the heads NOT IN VERSE ORDER, {L_SPINE} rows read whole in both files ({N_REREAD} read before and
reread whole, found by computation); three rows outside the spine by the union of both files (76:7 reread whole from chapter 12; 228:5; 312:1), none excluded; the
kin credited by name from fourteen ledgers (Leviticus 11 the twin chapter at its head); the unit deu_14_food_tithe the 228th (standing 2252, hash unmoved); the
ledger {L_ALL} sources (Onkelos MATERIAL {L_OM} / CONTEXT {L_OC}; the spine MATERIAL {L_SM} / CONTEXT {L_SC}; the outside rows MATERIAL {L_XM} / CONTEXT {L_XC}); seven claims 7/0
seated at 14:1, 3, 9, 21, 22, 24, 28; the display layer +{OV_REF14} by reference, +49 by gloss; every gate green in one chain (ch14_gates.sh, in the background; the
manifest, the verifier and the labels census in the foreground before it). THE ONE RUN AND ITS TAIL: the measurements (the kin by computation beside the law kin
named and THE TWIN CHAPTER DIFFED), the ink (27 fell on the first typed pass — every one the instrument's shape or a list from memory; 2 on the second; 0 on the
third), the design, the rows in five files (every cut held but one — the export's spelling, retyped), THE CLEAN POINT #204 AFTER ALL THE ROWS — /context 657.8k,
PAST THE 600k CAP A SECOND TIME where the estimate stood near 470k (the NOTE: a reading of this size is TWO RUNS + THE TAIL, the clean point after the first half
of the rows unconditionally); the owner's compaction; the tail on "Reread" and "Go" — the ledger (clean first run), the patch, the ink's fifth pass on the
"already" count and the sixth green, the manifest with its checks probed first, the seat, the shells with the form's name protected, the chain launched with the
writers typed during its run, the records, the forms, the message. EVERY STEP TIMED: the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)} from {T_START} — the table in the
map's AS BUILT. THE FINDS: THE TWIN CHAPTER DIFFED VERSE BY VERSE (14:6 = 11:3 + "two", 14:15 = 11:16, 14:7 folds three, the ra'ah's resh, the locusts and the seas
dropped, the vocabulary changed; the shelf's reason the two added names); THE THREE SIGNS FROM THREE CLAUSES; THE FOUR THE EXCEPTION SET (I1); "WAS MOSES A
HUNTER"; THE PERMITTED BIRDS WITHOUT A SIGN IN THE INK — the answer sheet's parameter (I3); THE LEXICON RULE at the bird's nest; THE LIST CARRIED BY ITS HEAD
(I2); SCRIPTURE SPECIFIES THE FEWER; THE LOCUSTS IN THE FRAMES; "A HOLY PEOPLE" three in the Bible, 14:2 = 7:6; THE SONSHIP TWO-ARMED; THE CUTTING THREE WAYS
with the baldness by analogy both ways (I2); THE CARCASS GIVEN NOT CAST with the four-cell table and R. Judah's dissent; THE KID'S THIRD SEAT THREE WAYS and the
eating at 12:24 (I1); THE TITHE'S LIABILITIES and the second tithe named; THE WALL, THE HOUSE, THE YEAR (three statuses); THE WAY OF PLACE; THE MONEY'S TWO ARMS
(I1); THREE MONEYS FROM THE COUNT; the class from the four named (I3); THE REJOICING A PEACE OFFERING (I2); SHILOH AND THE HOUSE; THE LEVITE'S LADDER; THE
REMOVAL'S DATE COMPUTED (I2); ONE TITHE NOT TWO; THE FOUR IN WANT, SONS OF THE COVENANT — ONE NOUN TWO PERSONS (I3); the register split in two; the parser's [2]
and [3] with the starred tithe tokens; Onkelos's flesh with milk. THE LESSONS (thirteen, in the map): the cap by /context a second time and the two-runs rule; the
instrument's shape not the fact; the counting assert patch-aware; the piska's tail folded in; the heads out of order; the twin chapter diffed; the birds' signs
data; one noun two persons; the kin by computation; the cut's miss the export's; the checks probed first; the fast steps in the foreground; every step timed.
OWED TO 12b (COMPILE_DEBT's box (a)-(o)): the cuts, the beasts' signs, the water, the birds' signs, the carcass table, the kid's three readings, the second tithe's
statuses and the money's arms, the third year's date and the four, the effects, the place formula by call, the kin by call, never-read-ahead's cells, the
register's rows, the series DF, the docket. The records on the sheet; the forms in World/step9/forms_deuteronomy_walk/ (copy_ch14_forms.py).
'''

MEMPAR = f'''
SITTING 12 DONE {DATE} ("Go" after 11b's tail; "/context" and "Ready to compact" at #204; "Reread" and "Go" after the compaction; the map's "Sitting 12" and
"Sitting 12 — AS BUILT"): CHAPTER 14 READ AND FROZEN as ONE unit deu_14_food_tithe (the 228th; standing 2252 = 2245 + 7 as predicted, hash unmoved; no portion edge)
in ONE run to the clean point after ALL the rows + THE TAIL after the compaction, every row whole — Onkelos 29 rows (the identity), THE SIFREI ON THE CHAPTER A
SIXTH TIME (piska 96's tail 9-12 on 14:1 folded in — chapter 13's lesson closed; piskaot 97-110 with THE HEADS NOT IN VERSE ORDER; {L_SPINE} rows in both files; {N_REREAD}
reread whole, found by computation), three outside rows (76:7 reread whole), the kin credited by name from fourteen ledgers; the ledger deu_14_reeh_{LDATE}.md
({L_ALL} sources, clean on its first run); seven claims 7/0 seated at 14:1, 3, 9, 21, 22, 24, 28; every gate green; the display layer +{OV_REF14} / +49. THE FINDS: THE
TWIN CHAPTER DIFFED VERSE BY VERSE (14:6 = Leviticus 11:3 + "two"; 14:15 = 11:16; 14:7 folds 11:4-6; the ra'ah's resh; the locusts, the seas dropped; "abomination"
and "unclean" for "detestable"; the shelf's reason the two added names — 98:6); THE FOUR NAMED THE EXCEPTION SET, THE SIGN THE CLASS (101:10 — I1, 12b's rule);
THE PERMITTED BIRDS HAVE NO SIGN IN THE INK — the_birds_signs a PARAMETER from the answer sheet (103:8 — I3; Mishnah Chullin 3:6 inside the spine: the code/data
law's case); THE CARCASS TABLE with R. Judah's dissent (104:5-6 — two arms); THE KID'S THIRD SEAT THREE WAYS (104:8-10; 76:7 the eating at 12:24 — I1); THE
SECOND TITHE NAMED (105:2) with THREE STATUSES — the wall, the House, the year (106:3-5); THE MONEY'S FORM TWO ARMS (107:4 — I1); THREE MONEYS FROM THE INK'S
COUNT (107:7); THE REMOVAL'S DATE COMPUTED FROM TWO VERSES — Passover's last day, years 4 and 7 (109:1-3 — I2, a clock datum); ONE TITHE NOT TWO (109:5); ONE NOUN
TWO PERSONS — the sojourner at 14:21 (the resident alien) and 14:29 (the convert), Onkelos writing both (104:2, 110:2 — I3); "a holy people" three in the Bible,
14:2 = 7:6; the register split (the food laws plural, the tithe singular, 14:21 both); the parser's [2] and [3], the starred tithe tokens. ⚠ LESSONS (thirteen,
in the map): THE CAP PASSED BY /context A SECOND TIME (657.8k where the estimate stood near 470k) — A READING OF A CHAPTER THIS SIZE IS TWO RUNS + THE TAIL, the
clean point after the FIRST HALF of the rows UNCONDITIONALLY (the #204 NOTE; cost-rules memory amended); THE INSTRUMENT'S SHAPE NOT THE FACT (27 first-pass
fails, none a fact — retype from the print); A COUNTING ASSERT ON THE OVERRIDES MUST KNOW WHETHER THE PATCH HAS RUN; the piska's tail folded in; the heads out of
verse order; the twin chapter diffed; the birds' signs data; one noun two persons; the kin by computation; the cut's miss the export's spelling; the manifest's
checks probed in the store first; the fast steps in the foreground; EVERY STEP TIMED — the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)}. OWED TO 12b: the food laws
as cells with the exception set and the birds' parameter, the carcass table, the kid's three readings, the second tithe a status with three conditions and the
money's arms, the removal's clock datum, the sojourner parameter, the kin by call; DE the last series (DF next). UNCOMMITTED since fb797a1 (NOT PUSHED): 13's
compile and 14 (ONE message at <scratch>/commit_msg_ch14.txt carries both). NEXT on the ruling: the commit; then 12b, two runs + the tail.
'''
MEMLINE_OLD_START = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — '
MEMLINE_NEW = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — map World/step9/DEUTERONOMY_WALK.md; ch 1-13 COMPILED (PUSHED through 2b0c9c8); 14 READ AND FROZEN (sitting 12; A READING IS TWO RUNS + THE TAIL now); 13b + 14 uncommitted; NEXT: the commit, then 12b\n'
DESC_OLD = "COMMITTED THROUGH fb797a1 (2026-09-21; NOT PUSHED — pushed through 2b0c9c8) — SITTING 11b DONE 2026-09-21 ("
DESC_NEW = f"COMMITTED THROUGH fb797a1 (2026-09-21; NOT PUSHED — pushed through 2b0c9c8) — SITTING 12 DONE {DATE} (chapter 14 READ AND FROZEN as one unit, the 228th — the twin chapter diffed verse by verse, the permitted birds without a sign in the ink, the kid's third seat three ways, the second tithe's three statuses, the removal's date computed, the sojourner two persons; the cap passed by /context a second time — A READING IS TWO RUNS + THE TAIL from now; 13b and 14 UNCOMMITTED) — SITTING 11b DONE 2026-09-21 ("
REC2_OLD_START = '## 2. WHERE IT STANDS'
REC2_NEW = f'''## 2. WHERE IT STANDS ({DATE}, after sitting 12; the state doc #204 addendum 1 the newest)
- NUMBERS CLOSED. DEUTERONOMY 1:1-13:19 COMPILED AND ON THE TAPE (PUSHED through 2b0c9c8); 14 READ AND FROZEN.
- {C_UNITS} frozen units, standing 2252, hash 8b8fff1fa28953af. 68 runners, 73 daemons, 498 functions; 1155 kinds / 1056 effects.
- THE TAPE at RUN (1327, 96, 88, 0, 12, 1634, 44, 319, pairs, 127), markers 172, closes 127; the sweep 67/67; every gate GREEN.
- SITTING 12 (ch 14; TIMED; THE CAP PASSED BY /context A SECOND TIME — A READING IS TWO RUNS + THE TAIL NOW): the twin chapter
  diffed; the birds' signs the answer sheet's; {L_ALL} sources whole; 7 claims seated.
- UNCOMMITTED since fb797a1 (NOT PUSHED): 13's compile and 14 (<scratch>/commit_msg_ch14.txt carries both). NEXT ON HIS
  WORD: the commit; then 12b.

'''
A_REC5 = 'the newest instances: the map\'s "Sitting 11b" and "Sitting 11")'
A_REC5_NEW = 'the newest instances: the map\'s "Sitting 12" and "Sitting 11b")'
A_REC6 = '- Deuteronomy\'s sittings: the map; the addenda §31-57 (§39 the whole-row rule). The cost cuts: §35, §45, §47, §53.'
A_REC6_NEW = '- Deuteronomy\'s sittings: the map; the addenda §31-59 (§39 the whole-row rule). The cost cuts: §35, §45, §47, §53.'
TOP = {
 '**43. Mishnah, Slaughter**': f' — 3:6-7, 8:1-4, 4:4, 1:7 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: the signs of the beasts, the cleft one and the four exceptions 14:6-8 at 98:1-2, 101:10, 102:1 (Chullin 59a-60b, 66b), the fish 14:9-10 (Chullin 66a-b), THE BIRDS\' SIGNS FROM THE ANSWER SHEET 14:11-20 at 103:8 (Chullin 59a, 61a-65a) with the ra\'ah 14:13 at 98:5-6 (63b) and the locusts at 103:10 (65a-66a), flesh in milk 14:21 at 104:8-10 and 76:7 (Chullin 113a-116b), the carcass and the torn 14:21 at 104:1 (Chullin 72b-73a), the afterbirth 14:6 at 101:7 (68a-69a, 77a), grape-skin wine 14:26 at 107:15; the docket at 12b)',
 '**35. Mishnah, Lashes**': f' — 3:5-6 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: the cuts and the baldness 14:1 at 96:10-12 — the counts of lashes, "for the dead", "between your eyes"; Makkot 20a-21a; the docket at 12b)',
 '**8. Mishnah, Second Tithe**': f' — 1:1-7, 2:1, 3:10, 5:6 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: the far place and the money 14:24-26 at 107:1-15 — the money\'s form (Eduyot 3:2), the possession, the three moneys, the class from the four named, the condiments, the containers; the removal\'s date 14:28 at 109:3; Kiddushin 54b; the docket at 12b)',
 '**7. Mishnah, Tithes**': f' — 1:1, 1:3, 2:4, 4:5-6 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: the tithe\'s liabilities 14:22-23 at 105:5-18 — the edible, the onset, the casual eating, the vegetables and the pulses; the docket at 12b)',
 '**2. Mishnah, Corner of the Field**': f' — 8:5-9 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: the poor man\'s tithe and the measure of the gift 14:28-29 at 110:1-5 — half a kav of wheat, a kav of barley (Tosefta Peah 4:2, 4:11); the sons of Hanan at 105:19 (Jerusalem Talmud Peah 1:6); the docket at 12b)',
 '**30. Mishnah, Betrothal**': f' — Kiddushin 36a, 54b ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: the sonship conditional or not 14:1 at 96:9 (36a); the second tithe\'s money (54b); the docket at 12b)',
 '**24. Mishnah, Levirate Marriage**': f' — Yevamot 13b-14a, 47b, 86a-b ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: no factions 14:1 at 96:10 (13b-14a); the sojourner a son of the covenant 14:29 at 110:2 (47b); the Levite\'s tithe and Ezra\'s penalty 14:27-29 at 108:1, 109:10-11 (86a-b); the docket at 12b)',
 '**19. Mishnah, New Year**': f' — Rosh Hashanah 12a-13a ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: "year by year" — not from one year for its fellow 14:22 at 105:1; the vegetables\' year 14:28 at 109:8; Bekhorot 53b; the docket at 12b)',
 '**44. Mishnah, Firstborn**': f' — Bekhorot 34a-35a, 53b ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: the maimed firstling an abomination 14:3 at 99:1 (34a-35a); the cattle tithe year by year 14:22 at 105:3 (53b); the docket at 12b)',
 '**46. Mishnah, Substitution**': f' — 6:1 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: the altar\'s disqualified still food 14:4-6 at 101:1-2 — the Mishnah cited in the row\'s own Hebrew; the docket at 12b)',
 '**37. Mishnah, Testimonies**': f' — 3:2 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: "bind up the money" two ways — R. Ishmael\'s bound thing, R. Akiva\'s figured coin 14:25 at 107:4; the docket at 12b)',
 '**14. Mishnah, Passover**': f' — Pesachim 21b, 50b-51a ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: the carcass\'s two verbs over the two persons and R. Judah\'s "as written" 14:21 at 104:5-6 (21b); the custom\'s bar from "a holy people" 14:21 at 104:7 (50b-51a); the docket at 12b)',
 '**32. Mishnah, Middle Gate**': f' — Bava Metzia 88a ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: the seller and the buyer — the sons of Hanan\'s shops 14:22-23 at 105:19; the docket at 12b)',
 '**41. Mishnah, Animal Offerings**': f' — 5:8 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: the second tithe within the wall as the firstling 14:23 at 106:3; Tosefta Sanhedrin 3:5-6 at 106:2, 106:4; the docket at 12b)',
 '**4. Mishnah, Mixtures**': f' — Tosefta Kilayim 1:9 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: the antelope the wild ox 14:5 at 100:3; Chullin 80a for the seven wild; the docket at 12b)',
 '**39. Mishnah, Fathers (ethics)**': f' — 3:9, 3:14 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: the children of the LORD 14:1 at 96:9 (3:14); one band at 96:10 (3:9); the docket at 12b)',
 '**38. Mishnah, Idolatry**': f' — 2:6? ROUTED {DATE} (THE DEUTERONOMY WALK sitting 12, chapter 14\'s reading: the carcass sold to the foreigner 14:21 at 104:3-5 — the row\'s own question mark; the docket at 12b)',
}

M13B = rd(f'{SP}/commit_msg_ch13b.txt')
TRAIL = 'Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01MiJCE3AxFHu3jksQa2GG21\n'
assert M13B.endswith('\n' + TRAIL) or M13B.endswith(TRAIL), M13B[-200:]
M13B_BODY = M13B[:M13B.rindex('Co-Authored-By:')].rstrip('\n')
CM = f'''CHAPTER 14 READ AND FROZEN (SITTING 12 — A READING SITTING UNDER THE COST RULES: ONE RUN TO A CLEAN POINT AFTER ALL THE ROWS, THE COMPACTION, THE TAIL; EVERY ROW WHOLE; EVERY STEP TIMED) — THE TWIN CHAPTER LAID BESIDE LEVITICUS 11 VERSE BY VERSE (14:6 IS 11:3 WITH "TWO HOOFS", 14:15 IS 11:16 TO THE LETTER, 14:7 FOLDS THREE VERSES INTO ONE, THE RA'AH'S RESH FOR THE DA'AH'S DALET, THE LOCUSTS AND THE SEAS DROPPED, "ABOMINATION" AND "UNCLEAN" FOR "DETESTABLE" — AND THE SHELF'S REASON FOR THE RESTATEMENT THE TWO NAMES IT ADDS), THE FOUR NAMED THE EXCEPTION SET AND THE SIGN THE CLASS, THE PERMITTED BIRDS WITHOUT A SIGN IN THE INK (THE ANSWER SHEET'S PARAMETER INSIDE THE SPINE), THE KID'S THIRD AND LAST SEAT READ THREE WAYS, THE CARCASS GIVEN NOT CAST WITH R. JUDAH'S DISSENT, THE SECOND TITHE NAMED WITH THREE STATUSES (THE WALL, THE HOUSE, THE YEAR), THE MONEY'S FORM TWO ARMS, THE REMOVAL'S DATE COMPUTED FROM TWO VERSES, ONE NOUN TWO SOJOURNERS, THE HEADS OF THE SPINE OUT OF VERSE ORDER, AND THE CAP PASSED BY /context A SECOND TIME — A READING OF THIS SIZE IS TWO RUNS + THE TAIL FROM NOW; AND, BENEATH IT, CHAPTER 13 COMPILED AND ON THE TAPE (SITTING 11b) — BOTH UNCOMMITTED SINCE fb797a1.

On the owner's words "Go" (the one run, after 11b's tail), "/context" and "Ready to compact" (at the clean point #204 — 657.8k), "Reread" and "Go" (the tail, after the compaction), {DATE}; World/step9/DEUTERONOMY_WALK.md "Sitting 12 — CHAPTER 14 … THE DESIGN" and "Sitting 12 — CHAPTER 14 — AS BUILT"; the state doc's #204, its NOTE and its addendum 1; the addenda §59. THE READING: Deuteronomy 14:1-29 with Onkelos whole (the export's 29 rows the DB's 29 — the identity, asserted) and THE SIFREI ON DEUTERONOMY ON THE CHAPTER A SIXTH TIME — piska 96's rows 9-12 on 14:1 (left by chapter 13's sitting; 96:10 folded in on its consonants with Amos 9:6 alone in its brackets — chapter 13's lesson 1 closed) and fourteen piskaot 97-110 whose heads are NOT IN VERSE ORDER (98 on 14:6 before 99 on 14:3 and 100 on 14:4; three piskaot on 14:6), {L_SPINE} rows READ WHOLE in both files ({N_REREAD} read before — the kid's three covenants at chapter 6, the firstling's year at chapter 12 — and REREAD WHOLE, found by computation), three rows outside the spine citing the chapter read whole (76:7 flesh in milk at 12:23, reread whole from chapter 12; 228:5 the bird's nest at 22:7; 312:1 the LORD's portion at 32:9), none excluded, the kin credited by name with the counts computed from fourteen ledgers (Leviticus 11 THE TWIN CHAPTER in two ledgers, 17:15, 19:10, 19:27-28, 20:26, 21:5, 22:8, 23:22, 27:30-33; Exodus 22:30, 23:19; Numbers 18:20-32; Deuteronomy 7:6, 10:9, 10:18, 12:5-26 — no Onkelos row of Genesis 7, 14 or 28, of Exodus 19, 23:10-11 or 34:26, and NONE OF DEUTERONOMY 15-26 OR THE PROPHETS in any ledger, asserted: never read ahead); frozen as ONE unit deu_14_food_tithe (the 228th; no portion edge inside it — Re'eh holds it whole), standing 2252 = 2245 + 7 as predicted, hash 8b8fff1fa28953af unmoved; the ledger logic/oral_triage/deu_14_reeh_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the spine {L_SPINE}: MATERIAL {L_SM} / CONTEXT {L_SC}; the outside rows {L_OUT}: MATERIAL {L_XM} / CONTEXT {L_XC}; coverage computed, lint 0, no cut missed — written clean on its first run, in the tail); seven claims DV14-01..07 verified 7/0 (the spine distributed by piska from the CITE INDEX itself; the seven check words' pieces measured in the store before they were typed), the labels census green, seated as seven WITNESS_READ operators at 14:1, 3, 9, 21, 22, 24, 28 with step E; the ritual {N_PASS} PASS; the display layer +{OV_REF14} by reference and +49 by gloss under the sitting's marker (the beasts' and the birds' names, "hoof" for "claw", "carcass" for "flabby-thing", "unclean" for forty-eight tokens of "foul-in-a-religious-sense", "the-cormorant" for "the-bird-of-prey", "the-little-owl" for "the-cup", "portion" for "smoothness", "and-bind-up" for "and-cramp"). THE FINDS: THE TWIN CHAPTER DIFFED VERSE BY VERSE — the ink's own instrument beside the shelf's reason (98:6 — repeated for the cleft one and the dayyah); THE THREE SIGNS FROM THE VERSE'S THREE CLAUSES (98:1) and THE CLEFT ONE A CREATURE (98:2 — ONE seat in the Bible); THE FOUR NAMED FROM SCRIPTURE AND THE REST BY A FORTIORI (101:10 — the written list the exception set, the sign the class: the compile's rule for the beasts' cell); "WAS MOSES A HUNTER OR AN ARCHER?" (102:1); THE LICENSE BY THE NAMES for the altar's disqualified (101:1-9 — Mishnah Temurah 6:1 in the row's Hebrew); THE PERMITTED BIRDS HAVE NO SIGN IN THE INK — the signs built from the eagle as the father on the answer sheet inside the spine (103:8 — Mishnah Chullin 3:6: the compile's parameter the_birds_signs is DATA, the code/data separation law's own case); THE LEXICON RULE "bird" = clean wherever said, applied at the bird's nest (98:3, 228:5); THE LIST CARRIED BY ITS HEAD — "eagle" here and there, two prohibitions on each name (103:3-4); SCRIPTURE SPECIFIES THE FEWER (100:2, 103:7); THE LOCUSTS IN THE FRAMES where the ink names none (103:10); "A HOLY PEOPLE" THREE IN THE BIBLE and 14:2 IS 7:6 with one word dropped — "sanctify yourself" at both seats, the custom's bar at the second (97:1, 104:7); THE SONSHIP TWO-ARMED (96:9); "YOU SHALL NOT CUT YOURSELVES" READ THREE WAYS — the mourner's cut with Carmel the run's case, no factions from the letters, the baldness by an analogy run both ways with the priests' verse (96:10-12); THE CARCASS GIVEN TO THE SOJOURNER, NOT CAST TO THE DOG — no clause shared with its three kin; the two verbs crossed over the two persons into a four-cell table against R. Judah's "the words as they are written" (104:5-6 — a PARAMETER with two arms); THE SOJOURNER OF THE GATES THE RESIDENT ALIEN (104:2 — Onkelos "uncircumcised"); THE KID'S THIRD AND LAST SEAT THREE WAYS — the three covenants, R. Akiva's three exclusions, the fowl out by "its mother's milk" (104:8-10) — and the eating seated at 12:24's clause by a refuted a fortiori (76:7): one verse said three times, three laws; "TITHE, YOU SHALL TITHE" the doubling's one seat — THE STARRED TITHE TOKENS the parser marks and reads no number; THE TITHE'S LIABILITIES FROM THE VERSE'S OWN CLAUSES (105:1-19) and THE CHAPTER'S TITHE NAMED THE SECOND (105:2); THE FIRSTLING AND THE SECOND TITHE ONE VERSE — the place, THE WALL OF JERUSALEM, THE HOUSE STANDING, THE YEAR PASSED (106:2-5: three statuses for the compile's cell; two a fortiori refuted, then "the verse compares"); THE TITHE A SCHOOL (106:6); THE WAY'S DISTANCE OF PLACE NOT TIME, any distance, the rich too (107:1-3); THE MONEY'S FORM TWO ARMS — R. Ishmael's bound thing, R. Akiva's figured coin (107:4 — Mishnah Eduyot 3:2); THREE MONEYS THE LAW'S TABLE FROM THE INK'S COUNT (107:7); the class from the four named — fruit from fruit and of the earth (107:8-11); THE REJOICING A PEACE OFFERING (107:16); SHILOH AND THE ETERNAL HOUSE (107:6 — chapter 12's eras table by CALL); THE LEVITE'S LADDER OF FOUR (108:1); THE REMOVAL'S DATE COMPUTED FROM TWO VERSES — "end, end" with 31:10 and 26:12's "finished": the eve of the last festival day of Passover of the fourth and the seventh year (109:1-3 — a clock datum); ONE TITHE NOT TWO — the poor man's replaces the second, the first does not move (109:5, 109:10-11); THE FOUR IN WANT AND SONS OF THE COVENANT — THE SOJOURNER OF 14:29 THE CONVERT AGAINST 14:21'S RESIDENT ALIEN, ONE NOUN TWO PERSONS, Onkelos writing both (110:1-2); the measure half a kav (110:3); THE REGISTER SPLIT IN TWO (the food laws plural, the tithe singular, 14:21 both; no "if", no imperative, no first person, no narrative verb, no "saying" — Moses' voice alone, Moses, Israel and Egypt never named); THE PARSER: two number verses ([2] "two hoofs", [3] "three years") and the starred tithe tokens at 14:22, 23, 28; THE STORE = THE DB (351 = 351, no written/read pair); ONKELOS: "you shall not make incisions", "beloved" for "treasured", "what is removed" for "abomination", the seven wild in Aramaic names, "the daughter of the wing" for the ra'ah, "YOU SHALL NOT EAT FLESH WITH MILK" (the law, not the verse), "the uncircumcised sojourner" and "the convert", the Shekhinah at the place's two seats, "new wine and old", no Memra. EVERY GATE GREEN IN ONE CHAIN (ch14_gates.sh, in the background; the manifest, verify_claims 7/0 and the labels census in the foreground before it; the summary read once): the seat, verify_text ({VT_STEPS} steps, {VT_SCEN} scenarios), the ritual {N_PASS} PASS, CORPUS TRUTH GREEN before and after the bake ({C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, hash unmoved), build_world ALL GREEN, the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer since 11b's chain, the tape unmoved), the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — no receipt, header or footer in chapter 14), large_letter_probes {LL[-3:]}, the home-path gate GREEN; the ink {N_INK} asserts in six passes ({INKF[1]} / {INKF[2]} / {INKF[3]} / {INKF[4]} / {INKF[5]} / {INKF[6]} failing — the first the instrument's shapes and three lists from memory, none a fact; the fifth the "already" count grown by the patch itself; the sixth green PATCHED). THE COST RULES ON A READING SITTING: the one run to the clean point #204 after ALL the rows — /context read 657.8k there, PAST THE 600k CAP A SECOND TIME where the run's own estimate stood near 470k (the #204 NOTE: A READING OF A CHAPTER THIS SIZE IS TWO RUNS + THE TAIL — the measurements, the ink and the design one run; the rows and the ledger a second; the tail the third; the clean point after the first half of the rows UNCONDITIONALLY); the owner's compaction; the tail on a small context — the ledger, the display patch (twelve asserted substitutions on the chapter-13 form), the manifest, the seat, the three shells derived with the form's name protected, the fast steps in the foreground before the freeze, the chain launched behind with the records writer and the copier typed during its run. EVERY STEP TIMED (the table in the map's AS BUILT, computed from ch14_timing.tsv): the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)} wall time from {T_START} to the records; the chain {mmss(CS_TOTAL)} ({CS_TXT}); the rest the reading, the typing and one compaction. THE LESSONS (thirteen, in the map's AS BUILT): the cap by /context a second time and the two-runs rule for a reading; the instrument's shape, not the fact; a counting assert on the overrides must know whether the patch has run; a piska's tail folded in; the heads out of verse order; the twin chapter diffed verse by verse; the birds' signs are data; one noun, two persons; the kin by computation again; the cut's one miss the export's own spelling; the manifest's check words probed first; the fast steps in the foreground, the chain behind; every step timed. Also in this commit: COMPILE_DEBT's sitting-12 box (a)-(o) owed to the compile 12b, MIDDOT's chapter-14 block (the codes censused from the ledger's rows — {CODE_TXT}), MISHNAH_TOPICS' row notes (Slaughter 3:6-7, 8:1-4, 4:4, 1:7; Lashes 3:5-6; Second Tithe 1:1-7, 2:1, 3:10, 5:6; Tithes 1:1, 1:3, 2:4, 4:5-6; Corner of the Field 8:5-9; Betrothal 36a, 54b; Levirate Marriage 13b-14a, 47b, 86a-b; New Year 12a-13a; Firstborn 34a-35a, 53b; Substitution 6:1; Testimonies 3:2; Passover 21b, 50b-51a; Middle Gate 88a; Animal Offerings 5:8; Mixtures Tosefta 1:9; Fathers 3:9, 3:14; Idolatry 2:6? — routed to 12b), RESEARCH_LOG's entry, THE_STEPS, THE_BRIEFING (the scoreboard and an entry), World/RESUME.md, the state doc's #204 with its NOTE and its addendum 1, the recovery page rewritten under its cap, the addenda §59, the stamp row, the memory (the cost rules amended — a reading is two runs + the tail), the forms in World/step9/forms_deuteronomy_walk/ (the one run's and the tail's scripts and prints — the derivations, the dump, the measurement, the split, the ink and its three parts, the five row files, the ledger writer, the design and clean-point writers, the display patch and its derivation, the manifest, the seat, the three shells and their derivation, the timer and its table, the records, the copy).

{M13B_BODY}

{TRAIL}'''

LINT = f'{ROOT}/logic/solo_tools/gloss_lint.py'
def lint(path):
    out = subprocess.run([sys.executable, LINT, path], capture_output=True, text=True).stdout
    m = re.search(r'gloss_lint: (\d+) flag', out); return int(m.group(1)) if m else -1
WALKP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; RECP = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
TOPICS = f'{ROOT}/logic/MISHNAH_TOPICS.md'
TOUCH = [f'{ROOT}/logic/findings/STAMP_LEDGER.md', f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', f'{ROOT}/World/RESUME.md', f'{ROOT}/THE_STEPS.md', f'{ROOT}/THE_BRIEFING.md', f'{ROOT}/World/step9/COMPILE_DEBT.md', f'{ROOT}/RESEARCH_LOG.md', f'{ROOT}/logic/MIDDOT.md', RECP, f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md', TOPICS]
# ---- THE ANCHORS, ASSERTED PRESENT ONCE BEFORE ANY WRITE ----
A_RESUME = '# ⚠ THE DEUTERONOMY WALK sitting 11b — CHAPTER 13 COMPILED AND ON THE TAPE (2026-09-21; step9/DEUTERONOMY_WALK.md "Sitting 11b"'
A_SCORE = '## SCOREBOARD (as of 2026-09-20, latest)\n'
A_BULLET = '- **CHAPTER 13 COMPILED — THE SEDUCERS\' ONE SENTENCE SAID THREE TIMES COMPILED AS FOUR LAWS AT THE CHAPTER\'S OWN DAY'
A_ENTRY = '### 2026-09-21 — CHAPTER 13 COMPILED: FOUR LAWS AT ONE DAY, THREE OF THEM REUSING WHAT THE MACHINE HELD, AND THE DISPUTES AS PARAMETERS'
A_MIDDOT = '\n## Exodus block campaign — owner\'s word "Do 3")\n'
ANCH = [(f'{ROOT}/World/RESUME.md', A_RESUME), (f'{ROOT}/THE_STEPS.md', '\n## Step 6 — Publish\n'), (f'{ROOT}/THE_BRIEFING.md', A_SCORE), (f'{ROOT}/THE_BRIEFING.md', A_BULLET), (f'{ROOT}/THE_BRIEFING.md', A_ENTRY), (f'{ROOT}/logic/MIDDOT.md', A_MIDDOT), (RECP, REC2_OLD_START), (RECP, '\n## 3. THE STANDING LAWS'), (RECP, A_REC5), (RECP, A_REC6), (f'{MEM}/deuteronomy-walk.md', DESC_OLD), (f'{MEM}/MEMORY.md', MEMLINE_OLD_START)]
for p, a in ANCH: assert rd(p).count(a) == 1, (p, a[:40], rd(p).count(a))
tl = rd(TOPICS).split('\n'); assert all(sum(l.startswith(t) for l in tl) == 1 for t in TOP) and 'sitting 12, chapter 14' not in rd(TOPICS)
assert '## Sitting 12 — CHAPTER 14 — AS BUILT' not in rd(WALKP) and '## Sitting 12 — CHAPTER 14, Deuteronomy 14:1-29' in rd(WALKP) and '#204 ADDENDUM 1' not in rd(TOUCH[1]) and '#204 (' in rd(TOUCH[1]) and '#204 — NOTE' in rd(TOUCH[1]) and '## §59' not in rd(TOUCH[9]) and '## §58' in rd(TOUCH[9]) and 'SITTING 12 DONE' not in rd(f'{MEM}/deuteronomy-walk.md') and 'SITTING 12 — CHAPTER 14' not in rd(TOUCH[5]) and f'## {DATE} — DEUTERONOMY 14 READ' not in rd(TOUCH[6]) and 'CASE LAW ON CHAPTER 14' not in rd(TOUCH[7]) and 'DEUTERONOMY — SITTING 12 — CHAPTER 14' not in rd(TOUCH[3])
s = rd(RECP); i = s.index(REC2_OLD_START); j = s.index('\n## 3. THE STANDING LAWS'); REC_NEW = s[:i] + REC2_NEW + s[j:]
REC_NEW = REC_NEW.replace(A_REC5, A_REC5_NEW).replace(A_REC6, A_REC6_NEW)
assert len(REC_NEW.encode()) <= 10240, len(REC_NEW.encode())
m = rd(f'{MEM}/MEMORY.md'); i = m.index(MEMLINE_OLD_START); j = m.index('\n', i) + 1; MEM_NEW = m[:i] + MEMLINE_NEW + m[j:]
assert len(MEM_NEW.encode()) < 17000, len(MEM_NEW.encode())
CMP = f'{SP}/commit_msg_ch14.txt'; assert not os.path.exists(CMP) or CHECK, CMP
for t in (WALK, DEBT, MIDDOT, RESEARCH, STEPS, BRIEF, BRIEF_ENTRY, RESUME_NOTE, STATE, ADDENDA, MEMPAR, CM, REC_NEW, MEM_NEW) + tuple(TOP.values()):
    assert SP not in t and os.path.expanduser('~') not in t, 'a scratch or home path in a record'
BEFORE = {p: lint(p) for p in TOUCH}
print('lint before:', {os.path.basename(p): n for p, n in BEFORE.items()}, '| recovery page bytes', len(REC_NEW.encode()), '| MEMORY.md bytes', len(MEM_NEW.encode()), '| commit message bytes', len(CM.encode()))
if CHECK: print('CHECK ONLY — nothing written'); sys.exit(0)
assert CHAIN_NOTE != 'CHAIN_NOTE_PLACEHOLDER', 'the chain note is typed from the summary before the records are written'
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
for t, note in TOP.items(): row_note(TOPICS, t, note)
open(RECP, 'w', encoding='utf-8').write(REC_NEW); print('recovery page rewritten', len(REC_NEW.encode()), 'bytes')
append(TOUCH[9], ADDENDA)
append(f'{MEM}/deuteronomy-walk.md', MEMPAR)
replace_once(f'{MEM}/deuteronomy-walk.md', DESC_OLD, DESC_NEW)
open(f'{MEM}/MEMORY.md', 'w', encoding='utf-8').write(MEM_NEW); print('MEMORY.md', len(MEM_NEW.encode()), 'bytes')
open(CMP, 'w', encoding='utf-8').write(CM); print('the commit message written', len(CM.encode()), 'bytes')
AFTER = {p: lint(p) for p in TOUCH}
print('lint after: ', {os.path.basename(p): n for p, n in AFTER.items()})
assert all(AFTER[p] <= BEFORE[p] for p in TOUCH), [(os.path.basename(p), BEFORE[p], AFTER[p]) for p in TOUCH if AFTER[p] > BEFORE[p]]
assert lint(WALKP) == 0 and lint(f'{MEM}/deuteronomy-walk.md') == 0 and len(rd(RECP).encode()) <= 10240
print('records written; the lints at or under their baselines; the map and the memory file lint 0; the page under its cap')
