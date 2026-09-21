import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12 (2026-09-20; the owner: "Monitor how long each step takes and report when the chapter is done" — the first sitting
# under THE COST RULES A-B-C: ONE run to the clean point #200 after the ledger, the owner's compaction, "Reread", THE TAIL on a small context): THE RECORDS at the
# close, from the sheet World/step9/RECORD_FORMS.md in ONE call — the map's "Sitting 10 — CHAPTER 12 — AS BUILT" WITH THE TIMING TABLE computed from the
# scratchpad's ch12_timing.tsv, COMPILE_DEBT's box (owed to the compile 10b), MIDDOT's block (the codes censused from the ledger's own rows), MISHNAH_TOPICS' row
# notes (ROUTED to 10b), RESEARCH_LOG's entry, THE_STEPS' paragraph, THE_BRIEFING's bullet and entry, RESUME's note, the state doc's #200 addendum 1, the recovery
# page (section 2 rewritten, under 10 KB), the recovery addenda's §54, the stamp row, the memory file and the index line (under 17,000 bytes), and THE COMMIT
# MESSAGE (a new file — the cost audit's records and this sitting ride one commit). Every number parsed from a print named beside it (--check prints them and
# writes nothing); every insert on a unique anchor asserted present once; the lints before and after. Sitting 9's form (write_ch11_records.py).
import os, re, subprocess, sys, yaml, json, datetime
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/' + os.path.abspath(ROOT).replace('/', '-') + '/memory')
DATE = '2026-09-20'; LDATE = '2026-09-20'
UID = 'deu_12_place_name'
CHECK = '--check' in sys.argv
CHAIN_NOTE = 'THE GATES CHAIN RAN ONCE, ALL GREEN ON ITS FIRST PASS (19:19:18 to 19:26:57 — 7 min 39 s: the seat, verify_text, the ritual, the fold, build_world, the journal gate, the register gate --strict, large_letter, the home gate; no demand, no retype; the summary read once) — launched in one background command behind the manifest, verify_claims (6 verified / 0 failed) and the labels census (GATE PASSED, debt 0 — no label refused: every middah string ends in its parenthesis, chapter 10\'s lesson 7 kept, asserted by the manifest writer before a byte was written).'
def rd(p): return open(p, encoding='utf-8').read()
# ---- THE NUMBERS, PARSED FROM THE PRINTS ----
truth = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py')
assert 'assert len(W["units"]) == 226' in truth and 'assert len(W["standing"]) == 2239' in truth and "8b8fff1fa28953af" in truth
CT = rd(f'{SP}/ch12_truth.out'); CB = rd(f'{SP}/ch12_bake.out'); C1 = rd(f'{SP}/ch12_fold_check1.out')
assert 'CORPUS TRUTH GREEN' in CT and 'CORPUS TRUTH GREEN' in C1 and 'wrote corpus_world.sqlite' in CB
rit = rd(f'{SP}/ch12_ritual_{UID}.out'); N_PASS = len(re.findall(r'^PASS', rit, re.M))
assert 'RITUAL COMPLETE' in rit and N_PASS == 13 and not re.search(r'^FAIL', rit, re.M), N_PASS
vt = rd(f'{SP}/ch12_vt_{UID}.out'); mvt = re.search(r'TEXT LAYER GREEN: (\d+) steps, (\d+) scenarios', vt); assert mvt and mvt.group(1) == '31', vt[-300:]
VT_STEPS, VT_SCEN = mvt.groups()
assert '  status: frozen' in rd(f'{ROOT}/logic/units/{UID}.yaml') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json') and 'ALL_DONE' in rd(f'{SP}/ch12_chain.log')
JG = rd(f'{SP}/ch12_journal.out'); RG = rd(f'{SP}/ch12_register.out'); BW = rd(f'{SP}/ch12_build.out'); GS = rd(f'{SP}/ch12_gates_SUMMARY.txt')
assert 'GATE GREEN' in JG and 'ALL GREEN' in BW and 'THE REGISTER GATE: GREEN' in RG and 'ALL GREEN' in GS, (JG[-200:], BW[-200:], GS[-200:])
mj = re.search(r'(\d+) kinds, ([\d,]+) rows', JG); J_KINDS, J_ROWS = mj.group(1), mj.group(2)
mr = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', RG); R_DECL, R_DEBT, R_FAIL = mr.groups()
assert R_DEBT == '0' and R_FAIL == '0', mr.groups()
mc = re.search(r'(\d+) units, (\d+) facts, (\d+) demands \((\d+) open\)', CT); C_UNITS, C_FACTS, C_DEM, C_OPEN = mc.groups()
assert C_UNITS == '226', C_UNITS
HG = rd(f'{SP}/ch12_home.out'); assert 'GREEN' in HG, HG[-200:]
LED = rd(f'{ROOT}/logic/oral_triage/deu_12_reeh_{LDATE}.md')
ml = re.search(r'\*\*read: (\d+) of \1 — COMPLETE\*\* \((\d+) Onkelos verses and (\d+) Sifrei rows.*?MATERIAL (\d+) Onkelos, CONTEXT (\d+) Onkelos, MATERIAL (\d+) Sifrei spine, CONTEXT (\d+) Sifrei spine, MATERIAL (\d+) Sifrei outside, CONTEXT (\d+) Sifrei outside', LED, re.S)
L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_SM, L_SC, L_XM, L_XC = ml.groups()
assert L_ALL == '197' and L_ONK == '31' and L_SIF == '166' and LED.count('⟨MISS⟩') == 0
L_SPINE = int(L_SM) + int(L_SC); L_OUT = int(L_XM) + int(L_XC); assert L_SPINE == 159 and L_OUT == 7, (L_SPINE, L_OUT)
L_BYTES = len(LED.encode())
N_REREAD = len(re.findall(r'^- Sifrei Devarim \d+:\d+ — [A-Z]+ \(REREAD WHOLE — read before in', LED, re.M)); N_REREAD_OUT = len(re.findall(r'^- Sifrei Devarim \d+:\d+ — [A-Z]+ \(REREAD WHOLE — first read in', LED, re.M))
assert N_REREAD == 4 and N_REREAD_OUT == 1, (N_REREAD, N_REREAD_OUT)
CODES = Counter(); BYCODE = {}
for line in re.findall(r'^- Sifrei Devarim \d+:\d+ — .*$', LED, re.M):
    name = re.match(r'- (Sifrei Devarim \d+:\d+)', line).group(1)
    for c in sorted(set(re.findall(r'\b([IE]\d{1,2}) \(', line))): CODES[c] += 1; BYCODE.setdefault(c, []).append(name.split(' ')[2])
CODE_TXT = '; '.join(f'{c} at {", ".join(BYCODE[c])}' for c in sorted(CODES, key=lambda x: (x[0], int(x[1:]))))
for c, r in (('I1', '145:3'), ('I1', '286:16'), ('I2', '138:1')): assert r in BYCODE.get(c, []), (c, r, BYCODE.get(c))
d_ov = yaml.safe_load(rd(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'))
OV_REF12 = len([k for k in d_ov['by_ref'] if k.startswith('Deut.12.')]); OV_REF, OV_GL = len(d_ov['by_ref']), len(d_ov['by_gloss'])
assert OV_REF12 == 124 and OV_REF == 983 and OV_GL == 673, (OV_REF12, OV_REF, OV_GL)
N_CLAIMS = len(json.load(open(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json', encoding='utf-8'))); assert N_CLAIMS == 6
VC = rd(f'{SP}/ch12_vc.out'); assert 'SUMMARY: 6 verified, 0 failed, 0 uncheckable, 0 no-check' in VC, VC[-300:]
LAB = rd(f'{SP}/ch12_labels.out'); mlab = re.search(r'CLAIM LABELS CENSUS — (\d+) claims in (\d+) manifests; labeled \1; DEBT 0', LAB); LN = f'{int(mlab.group(1)):,} claims in {mlab.group(2)} manifests'; assert 'GATE PASSED' in LAB and re.search(r'deu\s+76 claims', LAB), LAB[-300:]
assert rd(f'{SP}/ch12_ink_run3.out').strip().endswith('0 failing statements') and rd(f'{SP}/ch12_ink_run2.out').strip().endswith('0 failing statements') and rd(f'{SP}/ch12_ink_run1.out').strip().startswith('5 failing statements')
N_INK = len(re.findall(r'^assert ', rd(f'{SP}/ch12_ink.py'), re.M)); assert N_INK == 121, N_INK
LL = rd(f'{SP}/ch12_large_letter.out').strip().split('\n')[-1]; assert LL.endswith('6/6'), LL
JR11 = re.search(r'12 kinds, ([\d,]+) rows', rd(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch11_journal.out')).group(1); DJ = int(J_ROWS.replace(',', '')) - int(JR11.replace(',', ''))
MAN = rd(f'{SP}/ch12_manifest.out'); assert 'every CITE INDEX name used by a claim: True' in MAN
DUMP = rd(f'{SP}/ch12_dump0.out'); mdump = re.search(r'DB verses (\d+) \| export verses HE (\d+) EN (\d+)', DUMP); assert mdump and mdump.groups() == ('31', '31', '31'), DUMP[:300]
LEDW = rd(f'{SP}/write_ch12_ledger.out'); assert '197 sources' in LEDW and 'MISMARK []' in LEDW and 'FAIL []' in LEDW, LEDW[-200:]   # retyped from the print (the writer ends its line with MISMARK [] | FAIL [])
# ---- THE TIMING TABLE, computed from the scratchpad's tsv (the owner's ask) ----
def timing():
    rows = [l.rstrip('\n').split('\t') for l in rd(f'{SP}/ch12_timing.tsv').splitlines() if l.strip()]
    assert rows[0][0] == 'started', rows[0]
    t0 = int(rows[0][2]); day = datetime.datetime.fromtimestamp(t0)
    out = ['| step | began | ran | the gap before it (reading, typing, the owner\'s compaction) |', '|---|---|---|---|']
    prev_end, mach = t0, 0
    for hms, name, secs, rc in rows[1:]:
        h, m, s = map(int, hms.split(':')); b = int(day.replace(hour=h, minute=m, second=s).timestamp())
        gap = b - prev_end; mach += int(secs); prev_end = b + int(secs)
        out.append(f'| {name} | {hms} | {secs} s{" (rc " + rc + ")" if rc != "0" else ""} | {gap // 60} min {gap % 60} s |')
    total = prev_end - t0
    return '\n'.join(out), mach, total, rows[0][1], len(rows) - 1
TT, T_MACH, T_TOTAL, T_START, T_ROWS = timing()
def chain_steps():
    st = re.findall(r'^=== (\w+) (\d\d):(\d\d):(\d\d)', GS, re.M); end = re.search(r'^ALL GREEN (\d\d):(\d\d):(\d\d)', GS, re.M)
    pts = [(n, int(h) * 3600 + int(m) * 60 + int(s)) for n, h, m, s in st] + [('ALL GREEN', int(end.group(1)) * 3600 + int(end.group(2)) * 60 + int(end.group(3)))]
    return '; '.join(f'{pts[i][0]} {pts[i + 1][1] - pts[i][1]} s' for i in range(len(pts) - 1)), pts[-1][1] - pts[0][1]
CS_TXT, CS_TOTAL = chain_steps()
def mmss(x): return f'{x // 60} min {x % 60} s'
print('PARSED:', dict(ritual_pass=N_PASS, verify_text=(VT_STEPS, VT_SCEN), journal=(J_KINDS, J_ROWS, DJ), register=(R_DECL, R_DEBT, R_FAIL), corpus=(C_UNITS, C_FACTS, C_DEM, C_OPEN), ledger=(L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_SM, L_SC, L_XM, L_XC, L_BYTES, N_REREAD, N_REREAD_OUT), codes=dict(CODES), overrides=(OV_REF12, OV_REF, OV_GL), claims=N_CLAIMS, labels=LN, ink=N_INK, large_letter=LL[-3:], timing=(T_ROWS, T_MACH, T_TOTAL, T_START), chain=(CS_TXT, CS_TOTAL)))
print('CODES BY ROW:', CODE_TXT)
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

STAMP = (f'| {DATE} | {UID} | DELEGATED | FULL RULE | Deuteronomy 12:1-31 derivation {LDATE} (THE DEUTERONOMY WALK sitting 10 — CHAPTER 12; the owner: "Monitor how long each step takes and report when the chapter is done" — the first sitting under THE COST RULES, one run to the clean point #200 and its tail after the compaction, every step timed, every row whole): Onkelos Deuteronomy 12 whole (31 = 31, the identity) + the Sifrei on Deuteronomy ON THE CHAPTER — piskaot 59-81 (three without a head citation folded in on their consonants), {L_SPINE} spine rows read whole in both files ({N_REREAD} rows read before and reread whole) + its {L_OUT} rows outside the spine read whole ({N_REREAD_OUT} reread) + the kin credited by name; the ledger deu_12_reeh_{LDATE}.md ({L_ALL} sources, coverage computed, lint 0); {N_CLAIMS} claims DV12-01..06 verified 6/0, seated as six WITNESS_READ at 12:1, 5, 13, 15, 20, 29; the ritual {N_PASS} PASS; CORPUS TRUTH GREEN ({C_UNITS} units, standing 2239, hash unmoved); the fold layer +{DJ}; the display layer +{OV_REF12} by reference, +69 by gloss; the machine\'s share of the sitting {mmss(T_MACH)} of {mmss(T_TOTAL)} | {LN}, labeled, debt 0 |\n')

WALK = f'''


## Sitting 10 — CHAPTER 12 — AS BUILT ({DATE}; the design above stands as written — the one run ran to the clean point #200 after the rows and the ledger, the owner compacted, and THE TAIL ran on "Reread" at the step the point named; every departure from the design is named here; THE TIMING TABLE the owner asked for is the last section)

THE RESULT: Deuteronomy 12:1-31 READ, FROZEN and SEATED as ONE unit — deu_12_place_name (the 226th frozen unit; 31 of 31 verses in the Hebrew numbering, missing 0,
computed — the English's 12:32 the DB's 13:1; no portion edge inside it): the ledger logic/oral_triage/deu_12_reeh_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL
{L_OM} / CONTEXT {L_OC}; THE SIFREI'S SPINE piskaot 59-81 {L_SPINE} rows: MATERIAL {L_SM} / CONTEXT {L_SC}, {N_REREAD} of them read before and REREAD WHOLE (the prior reads found in the earlier
ledgers by computation — 61:7 at chapter 7, 80:4-5 at chapter 11, 75:2 at two Genesis sittings); the outside rows {L_OUT}: MATERIAL {L_XM} / CONTEXT {L_XC}, {N_REREAD_OUT} reread (2:2 from
sitting 1); {L_BYTES:,} bytes, lint 0, no cut missed), the manifest {N_CLAIMS} claims DV12-01..06 verified 6/0 (every he_contains cut from the store's own bytes; every cite index
name used by a claim — the spine's rows distributed by piska from the CITE INDEX itself, the headless 68, 73, 74 with the piskaot they were folded into, the seven
outside rows with the claims whose verses they cite), seated as six WITNESS_READ operators at 12:1, 5, 13, 15, 20, 29 with step E; the ritual {N_PASS} PASS; verify_text
GREEN ({VT_STEPS} steps, {VT_SCEN} scenarios); the fold predicted and matched (units 225 → 226, standing 2233 → 2239, the hash 8b8fff1fa28953af unmoved — CORPUS TRUTH GREEN before
and after the bake: {C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, {C_OPEN} open); build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer since
chapter 11's reading, the tape unmoved since 9b); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — the header at 12:1 the declared EMPTY seat; 12:21's
"as I have commanded you" listed nowhere: the receipt without the Name, the finder's fourth seat); large_letter_probes {LL[-3:]}; the labels census GREEN ({LN},
Deuteronomy 76); the home-path gate GREEN; the display layer +{OV_REF12} by reference and +69 by gloss ({OV_REF} / {OV_GL} in all).

THE READING: every Onkelos row whole in the Aramaic and the English (ch12_onkelos.txt); THE SPINE ON THE CHAPTER AGAIN — twenty-three piskaot 59-81, twenty heading on
the chapter's verses and THREE WITHOUT A HEAD CITATION (68 on 12:11's "your burnt offerings", 73 on 12:17's "your herd and your flock", 74 on 12:17's "your vows")
folded in on their consonants, every row read whole in both files (ch12_sifrei_spine.txt, split by piska for the reading — ch12_spine_p59.txt … p81.txt); the seven
outside rows whole in both files (ch12_sifrei_outside.txt — the rest as the Land 2:2, the firstling and the second tithe 106:5, the rejoicing 138:1, the Asherah not
planted 145:3, the order of offerings 147:2, build anywhere 179:2, the blood's reward 286:16), none excluded; the kin (Leviticus 17:1-16, Numbers 18:8-32, 7:5 and
7:25-26, Leviticus 20:2-5 and 18:21, Numbers 33:52, Exodus 23:24) credited by name with the counts computed from those ledgers (16, 25, 3, 4, 1, 1, 1), the altar in
every place (Exodus 20:21) through the Mekhilta alone (two rows) — no ledger holds an Onkelos row of Exodus 20:21, of Genesis 9:4, of Exodus 34:13 or 34:24, and
NONE OF DEUTERONOMY 13-16 (asserted — never read ahead; the tithe, the firstling and the feasts wait for their own sittings).

THE DEPARTURES FROM THE DESIGN: none in substance; three in the tail's order and forms. (1) THE CHAIN WAS LAUNCHED AS SOON AS ITS INPUTS EXISTED — the manifest, the
verifier, the labels census and the gates chain as one background command right after the manifest, the seat and the three shells were written; the records writer
and the copier were typed DURING the chain's run and the notification was the wake (the design had the writers first, then the launch: the order of RUN B's end,
where the owner compacts after the launch; the tail has no compaction after it, so the wait overlapped the typing and nothing idled on any context). (2) THE
SHELLS' DERIVE REPLACED THE FORM'S OWN NAME — the global ch11 → ch12 substitution ran over the gates script's comment "sitting 9's form ch11_gates.sh" and turned it
into ch12's; retyped once by sed; the chain and fold derives protect the form's name with a placeholder, the gates derive did not (lesson 12). (3) THE INK'S FIRST
PASS FELL FIVE WAYS ON FORMS (none a fact, each retyped from the diag print): the English's unopened "Dt.13:29)" at 179:2, 138:1's head citation counted by the
citation regex, the "how?" gloss caught by a '?' substring test, the computed kin asserted before its computation, the by-gloss count sixty-nine; 0 on the second
pass and on the third after the display patch. THE LEDGER WRITER'S FIRST RUN fell on FOURTEEN CUTS — the Name token inside 67:2-3's cuts, Jerusalem's defective
spelling (68:6, 74:3), "partition" without its yod (71:12, 72:8), "common" with its vav (75:6-10), 81:5's cut moved — every miss listed at once by the FAIL print,
retyped from the rows' own bytes, the second run clean. THE DISPLAY PATCH held first time (fourteen asserted substitutions on the chapter-11 form; the anchors
sitting 9's last rows found by walking, never typed). THE MIDDAH CODES held — every code checked in MIDDOT.md before it was typed, none relabeled: the census from
the ledger's rows — {CODE_TXT}. {CHAIN_NOTE}

THE GATES, COMPUTED FROM THEIR PRINTS: the ritual {N_PASS} PASS (RITUAL COMPLETE, {C_UNITS} frozen units); CORPUS TRUTH GREEN twice ({C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, {C_OPEN} open;
the hash unmoved); build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows, +{DJ}); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL});
verify_claims 6 verified / 0 failed; the labels census GREEN ({LN}); large_letter_probes {LL[-3:]}; the home-path gate GREEN; the ink {N_INK} asserts — 5 failing on the
first typed pass, 0 on the second and third (the third after the display patch).

⚠ THE LESSONS (the run's, gathered — the numbered list the sheet asks for): (1) THE KIN IS FOUND BY COMPUTATION — every verse of the chapter against every verse of
the Bible by shared distinct tokens, the closest re-scored in order, beside the law kin named: 12:18's closest kin is 16:11 (thirteen tokens in order) and 12:19 has
none — the design's kin list is a prediction the print corrects. (2) THREE PISKAOT WITHOUT A HEAD — the heads are the first sort, the words the second (chapter 11's
lesson 2 three times over); the union of citations finds 137 spine rows and the count of rows is the shelf's, not the regex's. (3) THE ENGLISH'S OWN SLIP IS
ASSERTED, NOT CORRECTED — 179:2's "(Dt.13:29)" for 12:29 and its unopened parenthesis: the Hebrew's citation decides, the English's text stands as it is. (4) THE
FIRST TYPED PASS FELL FIVE WAYS ON FORMS — a parenthesis, a head citation, a substring test, an order of statements, a count — none a fact; the diag print retypes
them all at once. (5) A CUT IS TYPED FROM THE ROW'S OWN BYTES — fourteen cuts fell on spellings the eye supplies (the Name, the yod, the vav, Jerusalem's defective
form); the FAIL print lists every miss at once and the second run is clean. (6) THE RECEIPT WITHOUT THE NAME HAS A FOURTH SEAT — 12:21 "as I have commanded you"
(Exodus 23:15 its one kin): the finder's third form owed since 4b and 6b; the shelf makes the seat the oral law's (75:6, 75:15) — measured at the reading,
dispositioned at 10b. (7) THE PLACE IS INSTALLED, NOT NAMED — "will choose" twenty-three seats in the book and none before chapter 12; the shelf makes the place a
variable with five stations (Mishnah Zevachim 14): the compile's parameter, the run's assignment. (8) A LAW CHANGED BY A PLACE — the slaughter law's release said in
new words (one token in order with Leviticus 17:3-5), the tape's entry the switch (R. Ishmael against R. Akiva, 75:3-4): the compile's question. (9) THE HEADER'S
TWIN IS THE FOLD'S FOOTER — 12:1 and Leviticus 26:46 alone: the laws' frame reopened where the Leviticus fold closed. (10) THE 400k CAP'S CLEAN POINT FELL AFTER THE
LEDGER — the rows and the ledger are the heavy half; the tail on a small context did the patch, the manifest, the seat, the chain, the records: THE COST RULES HELD
ON THEIR FIRST SITTING, the timing table the measure. (11) THE CHAIN IS LAUNCHED WHEN ITS INPUTS EXIST — the writers typed during its run, the notification the wake;
nothing waited on any context. (12) A GLOBAL SUBSTITUTION RUNS AFTER THE NAMED ONES AND THE FORM'S NAME IS PROTECTED — the gates shell's comment lost its form's
name to the ch11 → ch12 replace; a placeholder guards it. (13) EVERY STEP TIMED — the machine's share of the sitting {mmss(T_MACH)} of {mmss(T_TOTAL)} wall time from
{T_START} to the records; the rest the reading, the typing and one compaction: the reading is the sitting, the machine its instrument.

THE TIMING TABLE (the owner's ask — "Monitor how long each step takes and report when the chapter is done"; every row appended by the scratchpad's timer as the
step ran; the gap column is the time between one step's end and the next step's start — the reading of the rows, the typing of the scripts, the owner's compaction
between the ledger's second run and the tail's rereads; the chain's inner steps from its own summary's stamps):

{TT}

The chain's inner steps (ch12_gates_SUMMARY.txt): {CS_TXT}; the chain {mmss(CS_TOTAL)} in all. The machine's share {mmss(T_MACH)}; the sitting {mmss(T_TOTAL)} from {T_START}
to the last row above; the records writer's own row and the copier's follow in ch12_timing.tsv (copied into the forms).

THE FORMS: World/step9/forms_deuteronomy_walk/ (copy_ch12_forms.py — derive_ch12_dump0.py, ch12_dump0.py, derive_ch12_measure1.py, ch12_measure1_sections.py,
ch12_measure1.py, split_ch12_spine.py, ch12_ink_head.py, ch12_ink_body.py, ch12_ink_body_b.py, ch12_ink_body_c.py, derive_ch12_ink.py, ch12_ink.py, ch12_ink_diag.py,
patch_ink_ch12.py, assert_driver.py, the nine row files and patch_rows_ch12.py, write_ch12_ledger.py, write_ch12_design.py, write_ch12_cleanpoint.py, derive_ch12_patch.py,
ch12_patch_overrides.py, write_ch12_manifest.py, seat_ch12.py, derive_ch12_shells.py, ch12_chain.sh, ch12_fold.sh, ch12_gates.sh, tstep.sh, write_ch12_records.py,
copy_ch12_forms.py, the prints and ch12_timing.tsv).

NEXT on the ruling: the commit on the owner's word (the cost audit's records and this sitting stand uncommitted since bb62e90 — one message at
<scratch>/commit_msg_ch12.txt); then THE COMPILE OF CHAPTER 12 (sitting 10b) in TWO RUNS + THE TAIL under the cost rules — RUN A: the rereads (THE_STEPS Step 5 + the
compiler block; this section; the 10b box in COMPILE_DEBT), the measurements (the place's stations on the tape — the Tabernacle's erection, Gilgal, Shiloh, Nob and
Gibeon ahead; Leviticus 17's cell for the slaughter's switch; the register's finder at 12:21; the demolition's cells at 7:5 and Exodus 34:13; the blood's cells at
Leviticus 17:11-13), THE DESIGN (the place a PARAMETER the run assigns; the slaughter law's release a cell switched by the entry; the checkpoint series DD), the
probes to FAIL, THE DOCKET by the union rule (Mishnah Zevachim 14:4-8 and Zevachim 112b-119b the stations; Mishnah Avodah Zarah 3:5, 3:7 and Avodah Zarah 45a-48b;
Chullin 16b-17a, 28a, 84a-b, 102b-103a, 113a-116a with Mishnah Chullin 2:9, 6:1, 8:1-4, 10:1; Mishnah Bekhorot 2:2-3, 9:3 with Bekhorot 15a-16a, 33a-b; Mishnah Temurah
3:5 with Temurah 3b-4a, 17b; Mishnah Makkot 3:3, 3:15 with Makkot 13a-b, 17a-19b, 23b; Mishnah Sotah 7:6 with Sotah 37b-38b; Sanhedrin 20b; Mishnah Zevachim 9:5-6 with
Zevachim 83a-86a and 37a; Tosefta Zevachim 4:1; Mishnah Kiddushin 1:9 with Kiddushin 36b-37a; Rosh Hashanah 4a-6b; Mishnah Yoma 1:1; Tosefta Sheqalim 2:1; Avot 2:1;
Pesachim 8b; Tosefta Menachot 9:2; Sanhedrin 74a-b; Yevamot 47b, Keritot 20b-22a; Makhshirin 6:4; Seder Olam 11 — every row whole; a docket past ~700 rows its own
run); RUN B: the types, the runner, the tape to 10/10, the chain LAUNCHED; THE TAIL the records, the forms, the message — or the Decalogue-schema sitting first, on
his word.
'''

DEBT = f'''

## SITTING 10 — CHAPTER 12 ({DATE}, the reading; deu_12_place_name frozen) — OWED TO THE COMPILE 10b: (a) THE PLACE WHICH THE LORD WILL CHOOSE (12:5, 11, 14, 18, 21, 26)
## — INSTALLED HERE ("will choose" twenty-three seats in the book, none before chapter 12): a PARAMETER the run assigns — the shelf's five stations (the Tabernacle,
## Gilgal, Shiloh, Nob and Gibeon, Jerusalem — 65:1-2, 66:1-2; Mishnah Zevachim 14:4-8; Zevachim 112b-119b), the procedure (seek and find, then the prophet confirms —
## 62:1; David and Gad the run's citation), the two verses reconciled (62:2-3, 70:4 — the money from all, the ground from one), the Name pronounced only there (62:4 —
## Mishnah Sotah 7:6; Sotah 37b-38b); the effect a STATUS on the place; 12:8's "every man what is right in his eyes" the run's witness (Judges 17:6, 21:25) that the
## place was not yet chosen; the three commandments of the entry ordered (67:1-3 — Sanhedrin 20b; 12:10's "rest" 2 Samuel 7:1's); (b) THE DEMOLITION SAID IN NEW
## WORDS (12:2-3) — 7:5's and Exodus 34:13's cells by CALL (two tokens in order with 7:5, three with 34:13; five verbs where 7:5 had four), the decision tables (the
## three Asherim, the three houses — 61:5-6; Mishnah Avodah Zarah 3:5, 3:7; Avodah Zarah 45a-48b), the renaming for the worse (61:7 — R. Eliezer against R. Akiva),
## "from that place" the Land the duty's scope (61:6), "even ten times" (60:1); Numbers 33:52 and Exodus 23:24 by CALL; 145:3's a fortiori to 16:21 ahead; (c) THE
## HEADER (12:1) — the register's declared EMPTY seat, its twin Leviticus 26:46 (the fold's footer): the four nouns as exposition, law, learning and deed (59:1-4) and
## the land-bound rule (59:5 — Mishnah Kiddushin 1:9; Kiddushin 36b-37a) DATA rows; "you shall not do so to the LORD" plural 12:4 and singular 12:31 the pair (61:8;
## 81:5 the wrong altar's liability — Zevachim's rite); (d) THE SLAUGHTER LAW RELEASED (12:15, 20-22) — Leviticus 17:3-5's cell by CALL and A LAW CHANGED BY A PLACE:
## R. Ishmael's repeal on entering the Land against R. Akiva's no repeal (75:3-4 — Chullin 16b-17a): the tape's entry the switch, the design's question; "as He has
## spoken to you" (12:20) the AS_WHEN pointer with two teachers (75:2 — Genesis 15:19-20 or Ezekiel 48); "AS I HAVE COMMANDED YOU" (12:21) — THE RECEIPT WITHOUT THE
## NAME (Exodus 23:15 its one kin), the register's finder BLIND to it (measured): a RUN_CITATION pointer with its why — THE FINDER'S THIRD FORM owed since 4b and 6b,
## 12:21 its fourth seat; the shelf's seat of the oral law of slaughter (75:6, 75:15 — Mishnah Chullin 2:1; Chullin 28a) and the partitive's civility (75:5 — Chullin
## 84a-b) DATA rows; "as the gazelle and the hart" the comparison that teaches and is taught (75:15; 71:7-8) — the wild animal's slaughter, the bird's by the scribes;
## the unclean and the clean together (75:11), the blemished consecrated redeemed (71:1-6 — Mishnah Bekhorot 2:2-3; Bekhorot 15a-16a), the tithe's joint owners (71:9-10
## — Chullin 10:1); (e) THE BLOOD FOUR WAYS (12:16, 23-25, 27) — Leviticus 17:11-13's cell by CALL: "like water" no vessel, permitted for benefit, susceptibility, no
## covering (71:14 — Mishnah Chullin 6:1; Makhshirin 6:4), one prohibition not two (71:13), "the blood is the life" 17:11's clause turned, "be steadfast" the word said
## to Joshua — Israel steeped in blood (76:1), the lightest commandment the measure of all (76:2, 76:9, 286:16 — Mishnah Makkot 3:15; Makkot 23b), the limb from the
## living (76:5 — Chullin 102b-103a) and flesh in milk (76:7-8 — Mishnah Chullin 8:1-4; Chullin 113a-116a) by refuted a fortiori arguments — the effects BLOCKS on the
## eater; "shall be poured" the sin offering's verb at 12:27 — no blood no flesh (78:1-2 — Tosefta Zevachim 4:1), the one application (78:7-8 — Zevachim 37a), the bones
## and the sinews (78:4-5 — Mishnah Zevachim 9:5-6; Zevachim 83a-86a); the persecution (76:3 — Sanhedrin 74a-b) and the blood's classes (Yevamot 47b; Keritot 20b-22a)
## DATA rows; (f) THE OFFERINGS ONLY THERE (12:6, 11, 13-14, 17, 26) — the three lists compared (68:6 Shiloh's and Jerusalem's; "the choice of your vows" added at
## 12:11), the burnt offerings in every place you see a PROHIBITION (70:1) with a prophet's word the exception (70:3), the rest of the offerings included (70:5-6),
## THE LADDER OF A FORTIORI on 12:17's five items (72:9-11, 73:1, 74:1 — Mishnah Makkot 3:3; Makkot 13a-b, 17a-19b; 106:5, 147:2 — Mishnah Zevachim 10:1-2) a decision
## table of prohibitions, "you may not" read "not permitted" (72:1), "do not delay" (63:5 — Rosh Hashanah 4a-6b), the substitute (77:5-6, 78:9-10 — Mishnah Temurah 3:5;
## Temurah 3b-4a, 17b), from abroad (77:1), "the heave offering of your hand" the first fruits (63:9; Tosefta Menachot 9:2 at 68:4), the tithe STARRED by the parser
## (12:17; 14:23, 14:28, 26:12 ahead) — Numbers 18:8-32's cell by CALL; (g) THE TABLE AND THE HOUSEHOLD (12:7, 12, 18-19) — "before the LORD" within the partition (64:1;
## 67:4's two partitions), the rejoicing peace offerings (64:2; 138:1 — I2 with 27:7), "your households" his wife (64:4 — Mishnah Yoma 1:1), 5:14's household said
## again (69:3, 74:4 — the dearer first; 16:11, 14 ahead), the Levite's ladder (69:4, 74:5) and THE LEVITE'S VERSE ALONE (12:19 — even in sabbaticals and jubilees, not in
## the exile: 74:8-9; Pesachim 8b the pilgrimage) — the Levite's support a STATUS; Numbers 18:20's "no portion" by CALL; (h) THE NATIONS CUT OFF AND THE ABOMINATION
## (12:29-31) — 19:1 the twin (build anywhere — 80:3, 179:2), the sages at the border (80:4-5 — Ketubot 110b-111a credited from 9b), "lest you be ensnared" the root
## not 7:25's (a DATA row), "how did these nations serve" the seeker's one "saying", "so" for the service and the thing served (81:5), the parents from "even" (81:6 —
## R. Akiva's witness), THE KING-WORD'S HOMOGRAPH (Molech's consonants "to the king" — the census's slip at 7:8 and 11:3; 12:31 names no Molech: Leviticus 18:21 and
## 20:2-5 by CALL); (i) THE REGISTER'S SWITCH AT THE CHAPTER'S MIDDLE (plural 2-12, singular 13-31; the one plural verb at 12:16; the paragogic nun six, all in the
## plural half; no wayyiqtol; no divine frame) and THE PARSER (12:14's [1]; the starred tithe; the gazelle's two lemmas; the Kings' formula at 12:2; "leafy" the
## Torah's one) DATA rows for the census; Moses unnamed chapters 6-14 a DATA row; (j) THE CHECKPOINT SERIES continues (DC the open series — DC9 the last name; the
## next DD1, keyed by its first word); (k) THE DOCKET by the union rule — the testing shelf as the design listed it (Zevachim 14 and 112b-119b; Avodah Zarah 3 and
## 45a-48b; Chullin's eight stretches with its Mishnah; Bekhorot; Temurah; Makkot 3 and its folios; Sotah 7:6 and 37b-38b; Sanhedrin 20b and 74a-b; Zevachim 9 and 83a-86a,
## 37a; Tosefta Zevachim 4:1; Kiddushin 1:9 and 36b-37a; Rosh Hashanah 4a-6b; Yoma 1:1; Tosefta Sheqalim 2:1; Avot 2:1; Pesachim 8b; Tosefta Menachot 9:2; Yevamot 47b;
## Keritot 20b-22a; Makhshirin 6:4; Seder Olam 11; the Sifra on Leviticus 17 credited from its sitting) — EVERY ROW WHOLE; a docket past ~700 rows its own run; THE COST
## RULES: two runs + the tail, the chain launched at RUN B's end. NOTHING ELSE IN CHAPTER 12 IS OWED TO A LATER SITTING OF ITS OWN.
'''

MIDDOT = f'''- **THE SIFREI ON DEUTERONOMY'S OWN CASE LAW ON CHAPTER 12 (Deuteronomy 12:1-31; THE DEUTERONOMY WALK sitting 10, {DATE};
  the ledger logic/oral_triage/deu_12_reeh_{LDATE}.md — THE SPINE ON THE CHAPTER AGAIN, piskaot 59-81 (three without a head
  citation folded in on their consonants), {L_SPINE} rows read whole in both files, and seven rows outside the spine; EVERY CODE CHECKED
  IN MIDDOT.md BEFORE IT WAS TYPED, none relabeled; the census from the ledger's own rows: {CODE_TXT}):**
  · THE LADDER OF A FORTIORI (72:9-11, 73:1, 74:1 on 12:17): the five items of "you may not eat within your gates" assigned by
    elimination — each item's plain reading shown redundant by an a fortiori from the item before (the first fruits before the
    declaration, the thank and peace offerings before the throwing, the firstborn by a non-priest, the sin and guilt outside the
    curtains, the burnt offering anywhere), one method five times over — I1 (qal wa-chomer (a-fortiori)) as a DECISION TABLE of
    prohibitions; THE INK: 12:17's list against 12:6's and 12:11's item by item, the tithe starred by the parser; the answer sheet
    Mishnah Makkot 3:3 at the compile's docket.
  · THE A-FORTIORI FROM THE BURNING TO THE PLANTING (145:3 on 16:21 from 12:3): "their Asherim you shall burn in fire" — a fortiori
    that one not plant one; so "you shall not plant" is assigned to maintaining — I1 (checked; the row's own words קַל וָחוֹמֶר
    ("an a fortiori") on its bytes); the method of the ladder at a single seat.
  · THE A-FORTIORI FROM THE BLOOD (286:16 on 25:1 from 12:23; 76:2, 76:9 on 12:23): if one who abstains from blood, from which a
    man's soul recoils, receives a reward, how much more one who abstains from robbery and forbidden unions, which the soul craves —
    I1 (checked); Mishnah Makkot 3:15's argument with the reward's generations (79:2's phrase); THE INK: "be steadfast" the word said
    to Joshua (1:38, 31:7, 31:23) said to the eater.
  · THE REFUTED A-FORTIORI ARGUMENTS (76:5 and 76:7-8 on 12:23-24): the limb from the living and flesh in milk argued from the blood's
    clauses and refuted, the verse itself then cited — I1 (checked) in its refuted form; THE INK: "the life with the flesh" one seat,
    "you shall not eat it" 12:24-25 the pair.
  · THE VERBAL ANALOGY OF THE REJOICING (138:1 on 16:11 from 12:7; 64:2 on 12:7): "and you shall rejoice" here and at 27:7 — peace
    offerings — I2 (checked; the English adds "(Dt.12:7)" to the Hebrew's 27:7); THE INK: "and you shall rejoice" 12:7, 12:12, 12:18
    and the feasts' 16:11, 16:14 — 12:18 sharing thirteen tokens in order with 16:11.
  · THE TWO VERSES RECONCILED (62:2-3, 70:4 on 12:5 and 12:14): "from all your tribes" against "in one of your tribes" — the money
    from all, the ground from one; Shiloh and Jerusalem — named by the rows' own words, no code typed; THE INK: each phrase one seat,
    12:14 the chapter's one number verse [1].
  · THE DOUBLED VERB READ FOR ITS NUMBER (60:1 on 12:2): "destroy, you shall destroy" — even ten times — the infinitive absolute
    read as repetition, named without a code; THE INK: the doubling is "perish, you shall perish" (4:26, 8:19, 30:18) in the piel.
  · THE COMPARISON THAT TEACHES AND IS TAUGHT (75:15 on 12:22; 71:7-8 on 12:15): "as the gazelle and the hart are eaten" — the wild
    animal's slaughter taught by it, the bird's by the scribes (named by the row's own words; E12-E25's scope moves carry no fixed
    number for it — used by name, no code); THE INK: the gazelle's consonants "the beauty" elsewhere (2 Samuel 1:19) — the DB's two
    lemmas.
  · THE RESTRICTIVE PARTICLES (71:1, 71:5, 71:11, 75:14, 76:2, 77:9 on "only" and "but"): "only" four times and "but" once in the
    chapter, each read as a restriction of the clause before it — named without a code; THE INK: "only" twenty in the book, "but"
    (12:22) the chapter's one.
  · NAMED WITHOUT A CODE: the prohibition from "take heed to yourself lest" three times (70:1, 74:6-7, 81:1); "so" for the service and
    for the thing served (81:5); the parents from "even" (81:6 — R. Akiva's witness); the header's four nouns as exposition, law,
    learning and deed (59:1-4); the stations of the high places as a history (65:1-2, 66:1-2 — Mishnah Zevachim 14); the callee of
    "as He has spoken" disputed (75:2 — Genesis 15 or Ezekiel 48); the oral law's seat at "as I have commanded you" (75:6, 75:15);
    "like water" four ways (71:14).
'''

RESEARCH = f'''

## {DATE} — DEUTERONOMY 12 READ AND FROZEN (THE DEUTERONOMY WALK sitting 10 — the first sitting under THE COST RULES: one run to the clean point, the compaction,
## the tail; EVERY STEP TIMED on the owner's word): THE PLACE THE LORD WILL CHOOSE INSTALLED HERE — NO SEAT BEFORE CHAPTER 12; THE HEADER'S TWIN IS THE FOLD'S FOOTER;
## THE SLAUGHTER LAW RELEASED IN NEW WORDS — A LAW CHANGED BY A PLACE; "AS I HAVE COMMANDED YOU" THE RECEIPT WITHOUT THE NAME, THE FINDER'S FOURTH SEAT; THE LADDER OF
## A FORTIORI ON FIVE ITEMS; THE KIN FOUND BY COMPUTATION
On the owner's "Monitor how long each step takes and report when the chapter is done" ({DATE}). THE READING: Deuteronomy 12:1-31 with Onkelos whole (the export's
31 rows the DB's 31 — the identity, asserted; the English's 12:32 the DB's 13:1) and THE SIFREI ON DEUTERONOMY ON THE CHAPTER AGAIN — piskaot 59-81 (twenty heading
on the chapter's verses; 68, 73, 74 WITHOUT A HEAD CITATION, folded in on their consonants — 12:11's "your burnt offerings", 12:17's "your herd and your flock" and
"your vows"), {L_SPINE} rows read whole in both files ({N_REREAD} read before at chapter 7, chapter 11 and two Genesis sittings and reread whole — found by computation), seven
rows outside the spine read whole (2:2 the rest as the Land; 106:5; 138:1; 145:3; 147:2; 179:2 — the English's "(Dt.13:29)" a wrong chapter, the Hebrew right;
286:16), none excluded; the kin credited by name (Leviticus 17:1-16 — 16 rows; Numbers 18:8-32 — 25; 7:5, 7:25-26 — 3; Leviticus 20:2-5 — 4; 18:21 — 1; Numbers
33:52 — 1; Exodus 23:24 — 1; Exodus 20:21 through the Mekhilta's two rows); NEVER READ AHEAD — no Onkelos row of Deuteronomy 13-16 in any ledger (asserted). FROZEN as
ONE unit deu_12_place_name (the 226th; no portion edge inside it; standing 2239 = 2233 + 6 as predicted, hash unmoved); the ledger deu_12_reeh_{LDATE}.md ({L_ALL}
sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the spine {L_SPINE}: MATERIAL {L_SM} / CONTEXT {L_SC}; the outside rows {L_OUT}: MATERIAL {L_XM} / CONTEXT {L_XC}; coverage computed,
lint 0, no cut missed); six claims DV12-01..06 verified 6/0, seated as six WITNESS_READ at 12:1, 5, 13, 15, 20, 29; the ritual {N_PASS} PASS; the fold +{DJ} on the
journal; the display layer +{OV_REF12} by reference and +69 by gloss. THE FINDS: THE PLACE WHICH THE LORD WILL CHOOSE INSTALLED HERE — "will choose" twenty-three seats
in the book and NONE BEFORE CHAPTER 12 (ten with the article, seven with "in the place"); "to put His name there" and "to make His name dwell there" the two forms,
"HIS DWELLING" (12:5) one seat in the Bible — Onkelos "the house of His Shekhinah" (12:5 and 32:40 alone); "seek" His dwelling (12:5) and "inquire" after their gods
(12:30) ONE VERB FOR TWO SEEKINGS; the shelf's five stations (the Tabernacle, Gilgal, Shiloh, Nob and Gibeon, Jerusalem — 65-66, Mishnah Zevachim 14) and "every man
what is right in his eyes" Judges' refrain (17:6, 21:25) the run's own witness; THE HEADER'S TWIN IS THE FOLD'S FOOTER — "these are the statutes and the judgments"
12:1 and Leviticus 26:46 alone (59:1-4 the four nouns; 59:5 the land-bound rule); THE VERB OF ISRAEL'S PERISHING TURNED ON THE SHRINES — "destroy, you shall destroy"
(12:2) is 4:26's, 8:19's and 30:18's "perish, you shall perish" in the piel; "UNDER EVERY LEAFY TREE" THE KINGS' FORMULA (ten seats, 12:2 the Torah's one; "leafy" the
Torah's one); THE DEMOLITION SAID IN NEW WORDS — 12:3 two tokens in order with 7:5, three with Exodus 34:13, 12:2 none; five verbs where 7:5 had four, the fifth the
renaming (61:7); "you shall not do so to the LORD" plural 12:4 and singular 12:31; THE SEVEN OFFERINGS listed three times with the list changing (68:6 Shiloh's and
Jerusalem's); THE SABBATH'S HOUSEHOLD (5:14) at 12:18 and the feasts (12:18 — 16:11 thirteen tokens in order, THE KIN FOUND BY COMPUTATION); "take heed to yourself
lest" THREE TIMES in one chapter (nine in the Bible), each a prohibition on the shelf; "only" four and "but" one; THE SLAUGHTER LAW SAID IN NEW WORDS — Leviticus
17:3-5 one token in order with 12:15, the release named by the shelf (75:3 R. Ishmael; R. Akiva no repeal) — A LAW CHANGED BY A PLACE; THE GAZELLE'S HOMOGRAPH ("the
beauty" — the DB's two lemmas; the store's "splendor"); "on the earth you shall pour it like water" — Leviticus 17:13's dust nowhere (71:14 four ways); "YOU MAY NOT"
read "not permitted" (72:1; Onkelos "no permission"); THE LADDER OF A FORTIORI on 12:17's five items (72:9-11, 73:1, 74:1); THE LEVITE'S VERSE ALONE (12:19 — no verse
of the Bible shares two non-stop tokens with it); "AS HE HAS SPOKEN TO YOU" (12:20) the AS_WHEN form with two teachers on the callee (75:2); "AS I HAVE COMMANDED
YOU" (12:21) — THE RECEIPT WITHOUT THE NAME, Exodus 23:15 its one kin, the register's finder BLIND to it (measured) — the oral law's seat on the shelf (75:6, 75:15;
Mishnah Chullin 2:1): the finder's third form owed since 4b and 6b, its fourth seat; "BE STEADFAST" (12:23) the word said to Joshua said to the eater; "THE BLOOD IS
THE LIFE" Leviticus 17:11's clause turned; "SHALL BE POURED" the sin offering's verb at 12:27; "the good and the right" 6:18's pair (79:5 Heaven's eyes and men's);
"LEST YOU BE ENSNARED" (12:30) another root than 7:25's snare, the Torah's one niphal of each; "abomination of the LORD" eight in the book; THE CHILDREN BURNED
(Jeremiah 7:31 six tokens) and NO MOLECH NAMED — the king-word's homograph (the census's slip at 7:8 and 11:3); THE DB'S 13:1 IS THE ENGLISH'S 12:32; THE REGISTER
SWITCHES AT THE CHAPTER'S MIDDLE (plural 2-12, singular 13-31, the one plural verb at 12:16; the paragogic nun six, all in the plural half; no wayyiqtol; no divine
frame; Moses unnamed 6-14); THE PARSER: one number verse (12:14 [1]) and the tithe starred (12:17 — the ten-word's homograph at every tithe seat of the book); the
store = the DB (520 tokens, 2,051 letters, no written/read pair); ONKELOS: the Shekhinah for the Name, "their errors" for their gods, "before the LORD" for "to the
LORD", "the separation of your hand", the tithe SUPPLIED at 12:26, "as the FLESH of the gazelle" supplied at 12:22, "keep and RECEIVE" at 12:28, "the house of rest"
at 12:9. THE COST RULES ON THEIR FIRST SITTING: one run to the clean point after the ledger (#200), the owner's compaction, the tail on a small context — the patch,
the manifest, the seat, the chain launched as soon as its inputs existed with the writers typed during its run; EVERY STEP TIMED — the machine's share {mmss(T_MACH)} of
{mmss(T_TOTAL)} wall time from {T_START}; the table in the map's AS BUILT. THE CAUTIONS: the English's unopened "Dt.13:29)"; three piskaot without a head; fourteen cuts
fell on spellings the eye supplies; the gates shell's comment lost its form's name to a global replace. THE LESSONS (thirteen, in the map): the kin by computation;
the heads the first sort and the words the second; the English's slip asserted; the first pass fell five ways on forms; a cut from the row's own bytes; the receipt's
fourth seat; the place installed not named; a law changed by a place; the header the fold's footer; the clean point after the ledger; the chain launched when its
inputs exist; the form's name protected; every step timed. OWED TO 10b: the place a PARAMETER with five stations, the demolition's cells by CALL, the header's DATA
rows, the slaughter's switch by the entry, the receipt's pointer at 12:21, the blood's cells, the offerings' ladder, the table and the household, the nations cut off,
the register's switch, the series DD, the docket.
'''

STEPS = f'''DEUTERONOMY — SITTING 10 — CHAPTER 12, Deuteronomy 12:1-31 ({DATE}, on Brian's "Monitor how long each step takes and report when the chapter is done" — the first
sitting under the cost rules; World/step9/DEUTERONOMY_WALK.md "Sitting 10" and "Sitting 10 — AS BUILT"; a reading sitting is one run to a clean point, then the
tail after the compaction). Chapter 12 opens the laws themselves: tear down every place where the nations served their gods — on the high mountains, on the hills,
under every leafy tree — and do not do so to the LORD; instead, the place which the LORD will choose to put His name there is where the offerings go and where you
eat and rejoice with your household and the Levite; not as we do here today, every man what is right in his eyes, for you have not yet come to the rest; burnt
offerings only there — but flesh you may slaughter and eat in all your gates, the unclean and the clean alike, as the gazelle and the hart, only not the blood, which
you pour on the earth like water; the tithe, the firstlings and the vows not in your gates but before the LORD; when your border is enlarged and the place is far,
slaughter as I have commanded you and eat; be steadfast about the blood, for the blood is the life; take your holy things to the place and pour the blood on the altar;
and when the nations are cut off, do not be ensnared into asking how they served their gods — they burned their sons and daughters. The Sifrei has twenty-three
sections on the chapter, three of them with no opening verse and placed by their own words; every row was read whole in both files, with seven more rows from
elsewhere. The reading laid each verse beside every verse of the Bible and counted the shared words, a new form: the phrase "the place which the LORD will choose"
has no seat anywhere before this chapter — the chapter installs it, and the tradition gives it five stations; the chapter's opening line has one twin in the Bible,
the last line of the Leviticus laws; the permission to slaughter and eat flesh anywhere is a change of the older law that the tradition says came with the entry
into the Land; and where Moses says "as I have commanded you", nothing in the written text was ever commanded — the tradition places the rules of slaughter there,
and the machine's finder cannot see the sentence because it carries no Name. The chapter is frozen as one unit, the 226th, the world's standing facts up by six as
predicted, its hash unmoved, every gate green. The run stopped at a clean point after the ledger, you compacted, and the rest ran on a small context — the display
patch, the claims, the seat, the gates in the background while the records were typed. Every step was timed: the machine's own work came to {mmss(T_MACH)} in a sitting
of {mmss(T_TOTAL)}; the rest was the reading and the typing. Next: the commit on your word; then the compile of chapter 12 in two runs — the place as a parameter, the
slaughter's switch, the receipt's pointer — or the ten-commandments schema first.


'''

BRIEF = f'''- **CHAPTER 12 READ AND FROZEN — "THE PLACE WHICH THE LORD WILL CHOOSE" IS INSTALLED HERE, WITH NO SEAT BEFORE IT; THE CHAPTER'S FIRST LINE HAS ONE TWIN, THE LAST LINE OF THE LEVITICUS LAWS; THE PERMISSION TO EAT FLESH ANYWHERE IS AN OLD LAW CHANGED BY A PLACE; "AS I HAVE COMMANDED YOU" POINTS AT A COMMAND THE WRITTEN TEXT NEVER GIVES; AND THE FIRST SITTING UNDER THE COST RULES, EVERY STEP TIMED** ({DATE}; sitting 10, one run to a clean point and its tail; the ledger deu_12_reeh_{LDATE}.md — {L_ALL} sources, every row whole; the 226th unit; every gate green; the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)}).
'''
BRIEF_ENTRY = f'''### {DATE} — CHAPTER 12 READ: THE PLACE INSTALLED, A LAW CHANGED BY A PLACE, A COMMAND THE TEXT NEVER GIVES, AND EVERY STEP TIMED

Chapter 12 is where the laws begin: destroy the nations' shrines, bring the
offerings only to the place the LORD will choose, eat and rejoice there with
your household and the Levite, but slaughter and eat flesh in any gate you
like — only not the blood. Three things stood out when each verse was laid
beside every verse of the Bible and the shared words counted. The phrase "the
place which the LORD will choose" has no seat anywhere before this chapter;
the chapter installs it, and the tradition gives the variable five values in
turn — the Tabernacle, Gilgal, Shiloh, Nob and Gibeon, Jerusalem. The
permission to eat flesh anywhere shares one word with the older law that sent
every slaughter to the tent's door; the tradition says the change came with
the entry into the Land, which makes it a law switched by a place — a question
for the compile. And where Moses says "as I have commanded you" about the
slaughter, nothing in the written text was ever commanded; the tradition puts
the rules of slaughter there, and the machine's receipt-finder cannot see the
sentence because it carries no Name — the fourth such seat. The Sifrei has
twenty-three sections on the chapter, three of them with no opening verse and
placed by their own words; every row was read whole. The chapter is frozen as
one unit, every gate green. This was the first sitting under the cost rules:
the run stopped at a clean point after the ledger, Brian compacted, and the
rest ran on a small context with the gates in the background while the records
were typed. Every step was timed, as he asked: the machine's own work came to
{mmss(T_MACH)} in a sitting of {mmss(T_TOTAL)}; the rest was the reading and the typing.

'''

RESUME_NOTE = f'''# ⚠ THE DEUTERONOMY WALK sitting 10 ({DATE}; step9/DEUTERONOMY_WALK.md "Sitting 10" + "Sitting 10 — AS BUILT"): CHAPTER 12 READ AND FROZEN as ONE unit
# (deu_12_place_name, the 226th; standing 2239, hash unmoved) — THE PLACE WHICH THE LORD WILL CHOOSE INSTALLED HERE (no seat before chapter 12; five stations on the
# shelf), the header's twin Leviticus 26:46, the slaughter law released in new words (a law changed by a place), 12:21's "as I have commanded you" the receipt without
# the Name (the finder's fourth seat), the ladder of a fortiori on 12:17, the kin found by computation; the ledger deu_12_reeh_{LDATE}.md ({L_ALL} sources, every row
# whole; three headless piskaot folded in); six claims seated; the fold +{DJ} on the journal ({J_ROWS} rows); every gate green. THE FIRST SITTING UNDER THE COST RULES,
# EVERY STEP TIMED (the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)}; the table in the AS BUILT). NEXT on the owner's word: the commit (the cost audit and this sitting —
# <scratch>/commit_msg_ch12.txt); then 10b — the compile of chapter 12 (the place a parameter; DD the next series).
'''

STATE = f'''
#200 ADDENDUM 1 ({DATE}, at the close of THE DEUTERONOMY WALK sitting 10 — CHAPTER 12's READING: THE TAIL after the compaction at #200, on the owner's "Reread" — A CLEAN COMPACTION POINT): THE TAIL AS RUN on a small context: the rereads (the recovery page, the map's "Sitting 10 … THE DESIGN", MEMORY.md — 32 s); ch12_patch_overrides.py derived from the chapter-11 form by fourteen asserted substitutions (derive_ch12_patch.py), the yaml +{OV_REF12} by reference and +69 by gloss ({OV_REF} / {OV_GL}); the ink rerun PATCHED (0 failing — its third pass); the manifest write_ch12_manifest.py (six claims DV12-01..06 at 12:1, 5, 13, 15, 20, 29 — the spine distributed by piska from the CITE INDEX itself, the headless piskaot with their neighbours, the seven outside rows with the claims whose verses they cite; every he_contains cut from the store's bytes — the six checks "you shall destroy" 12:2, "His dwelling" 12:5, "in one of" 12:14, "as the gazelle" 12:15, "I have commanded you" 12:21, "be ensnared" 12:30); seat_ch12.py; ch12_chain.sh, ch12_fold.sh and ch12_gates.sh derived from chapter 11's forms (derive_ch12_shells.py — the gates comment retyped once, lesson 12); THE CHAIN LAUNCHED IN THE BACKGROUND AS ONE COMMAND — the manifest, verify_claims (6/0), the labels census ({LN}), then ch12_gates.sh (the seat, verify_text {VT_STEPS} steps / {VT_SCEN} scenarios, the ritual {N_PASS} PASS, the fold 225 → 226 / 2233 → 2239 with the hash unmoved, build_world, the journal gate {J_ROWS} rows (+{DJ}), the register gate --strict DECLARED {R_DECL} / DEBT {R_DEBT} / FAILS {R_FAIL}, large_letter {LL[-3:]}, the home gate) — {CHAIN_NOTE}; the records writer and the copier typed during the chain's run, the notification the wake; THE RECORDS from the sheet in one call (write_ch12_records.py — the map's "Sitting 10 — CHAPTER 12 — AS BUILT" with thirteen lessons AND THE TIMING TABLE the owner asked for (computed from ch12_timing.tsv: the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)} from {T_START}; the chain's inner steps {CS_TXT}), COMPILE_DEBT's sitting-10 box (a)-(k), MIDDOT's chapter-12 block with the codes censused from the ledger's rows ({CODE_TXT}), MISHNAH_TOPICS (ten heads routed to 10b), RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the scoreboard bullet and an entry), World/RESUME.md, this addendum, the addenda §54, the recovery page (section 2 under its cap), the memory (the walk note and the index line under 17,000), the stamp row, THE COMMIT MESSAGE <scratch>/commit_msg_ch12.txt — the cost audit's records and this sitting in one); the forms copied (copy_ch12_forms.py). THE TREE: + logic/units/deu_12_place_name.yaml frozen (operators, step E, the anchor scenarios), logic/py_units/deu_12_place_name.py and ALL_UNITS.py (the ritual), logic/oral_audit/manifests/deu_12_place_name_claims.json, logic/oral_triage/deu_12_reeh_{LDATE}.md, logic/glosses/word_gloss_overrides.yaml, logic/corpus/CORPUS_TRUTH.py (226 / 2239), corpus_world.sqlite, World/journal/data/world.sqlite (the fold layer, gitignored), the records, the forms. NOT COMMITTED (since bb62e90): THE COST AUDIT's records (COST_AUDIT_2026-09-20.md, its five forms and the rules writer, the record edits of #199 addendum 4) and SITTING 10 — ONE message at <scratch>/commit_msg_ch12.txt for the owner's word ("Commit" = no push; "commit push" = both). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. NEXT ON THE RULING: the commit on his word; then CHAPTER 12's COMPILE (10b) in two runs + the tail under the cost rules (RUN A the rereads, the measurements, the design — the place a PARAMETER with five stations, the slaughter's switch by the entry, the receipt's pointer at 12:21, the checkpoint series DD — and the docket by the union rule, its own run past ~700 rows; RUN B the types, the runner, the tape, the chain LAUNCHED; the tail the records) — or the Decalogue-schema sitting first; THE INSTALL HYPOTHESIS and the owner's open decisions (the SUPPLIED forms, the calf's day marker, the registry's homograph, the receipt's third and fourth shapes, options D and F of the cost audit) on the table. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 10 — CHAPTER 12 — AS BUILT" (the newest section), MEMORY.md.
'''

ADDENDA = f'''
## §54 — THE DEUTERONOMY WALK sitting 10 ({DATE}): CHAPTER 12 READ AND FROZEN — the state doc's #200 and its addendum 1; the map's "Sitting 10 — CHAPTER 12 … THE DESIGN" and "Sitting 10 — CHAPTER 12 — AS BUILT"; the owner: "Monitor how long each step takes and report when the chapter is done" (the first sitting under THE COST RULES A-B-C), "Reread" after the compaction at #200
THE READING: Onkelos Deuteronomy 12 whole (31 = 31, the identity; the English's 12:32 the DB's 13:1); THE SIFREI ON THE CHAPTER AGAIN — piskaot 59-81, twenty heading
on the chapter and three without a head citation (68, 73, 74) folded in on their consonants, {L_SPINE} rows read whole in both files ({N_REREAD} read before and reread whole,
found by computation); seven rows outside the spine by the union of both files (2:2 reread from sitting 1; 106:5, 138:1, 145:3, 147:2, 179:2, 286:16), none excluded;
the kin credited by name (Leviticus 17 — 16 rows; Numbers 18 — 25; chapter 7 — 3; Leviticus 20 — 4; 18:21 — 1; Numbers 33:52 — 1; Exodus 23:24 — 1; the Mekhilta's 2 on
Exodus 20:21); the unit deu_12_place_name the 226th (standing 2239, hash unmoved); the ledger {L_ALL} sources (Onkelos MATERIAL {L_OM} / CONTEXT {L_OC}; the spine MATERIAL
{L_SM} / CONTEXT {L_SC}; the outside rows MATERIAL {L_XM} / CONTEXT {L_XC}); six claims 6/0 seated at 12:1, 5, 13, 15, 20, 29; the display layer +{OV_REF12} by reference, +69 by
gloss; every gate green in one chain (ch12_gates.sh, launched in the background as one command with the manifest, the verifier and the labels census). THE ONE RUN
AND ITS TAIL: the measurements (THE KIN FOUND BY COMPUTATION for the first time), the ink (five forms fell on the first pass, none a fact), the design, the rows, the
ledger (fourteen cuts retyped from the FAIL print), the clean point #200 at the 400k cap; the owner's compaction; the tail on "Reread" — the patch, the manifest, the
seat, the chain launched as soon as its inputs existed with the writers typed during its run, the records, the forms, the message. EVERY STEP TIMED (the owner's ask):
the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)} from {T_START} — the table in the map's AS BUILT. THE FINDS: THE PLACE WHICH THE LORD WILL CHOOSE INSTALLED HERE (no seat
before; five stations on the shelf); THE HEADER'S TWIN THE FOLD'S FOOTER (Leviticus 26:46); the verb of Israel's perishing turned on the shrines; the Kings' formula
"under every leafy tree"; the demolition said in new words (five verbs); "His dwelling" one seat and the Shekhinah; one verb for two seekings; the seven offerings
listed three times; the Sabbath's household at the table; the slaughter law released in new words — A LAW CHANGED BY A PLACE (75:3-4); the gazelle's homograph; the
blood four ways; the ladder of a fortiori on 12:17; the Levite's verse alone; "as He has spoken" with two teachers on the callee; "AS I HAVE COMMANDED YOU" THE RECEIPT
WITHOUT THE NAME — the finder's fourth seat, the oral law's seat on the shelf; "be steadfast" Joshua's word; the snare's root not 7:25's; no Molech named; the
register's switch at the middle; the parser's [1] and the starred tithe. THE LESSONS (thirteen, in the map): the kin by computation; the heads then the words; the
English's slip asserted; five forms; a cut from the bytes; the receipt's fourth seat; the place installed; a law changed by a place; the header the footer; the clean
point after the ledger; the chain when its inputs exist; the form's name protected; every step timed. OWED TO 10b (COMPILE_DEBT's box (a)-(k)): the place a PARAMETER,
the demolition's cells, the header's rows, the slaughter's switch, the receipt's pointer, the blood's cells, the offerings' ladder, the table, the nations cut off, the
register's rows, the series DD, the docket. The records on the sheet; the forms in World/step9/forms_deuteronomy_walk/ (copy_ch12_forms.py).
'''

MEMPAR = f'''
SITTING 10 DONE {DATE} ("Monitor how long each step takes and report when the chapter is done" — the first sitting under THE COST RULES; "Reread" after the
compaction at #200; the map's "Sitting 10" and "Sitting 10 — AS BUILT"): CHAPTER 12 READ AND FROZEN as ONE unit deu_12_place_name (the 226th; standing 2239 = 2233 + 6
as predicted, hash unmoved; no portion edge) in ONE run to the clean point after the ledger + THE TAIL after the compaction, every row whole — Onkelos 31 rows (the
identity), THE SIFREI ON THE CHAPTER AGAIN (piskaot 59-81, {L_SPINE} rows in both files; 68, 73, 74 WITHOUT A HEAD folded in on their consonants; {N_REREAD} reread whole, found
by computation), seven outside rows (one reread), the kin credited by name; the ledger deu_12_reeh_{LDATE}.md ({L_ALL} sources); six claims 6/0 seated at 12:1, 5, 13,
15, 20, 29; every gate green; the display layer +{OV_REF12} / +69. THE FINDS: THE PLACE WHICH THE LORD WILL CHOOSE INSTALLED HERE — "will choose" none before chapter 12;
the shelf's five stations (Mishnah Zevachim 14) — 10b's parameter; THE HEADER'S TWIN IS THE FOLD'S FOOTER (12:1 = Leviticus 26:46); THE SLAUGHTER LAW RELEASED IN NEW
WORDS (one token with Leviticus 17:3-5) — A LAW CHANGED BY A PLACE (R. Ishmael v. R. Akiva, 75:3-4) — 10b's question; "AS I HAVE COMMANDED YOU" (12:21) THE RECEIPT
WITHOUT THE NAME (Exodus 23:15 its one kin), the finder BLIND — its fourth seat; the oral law's seat on the shelf (75:6, 75:15); THE LADDER OF A FORTIORI on 12:17's five
items; THE KIN FOUND BY COMPUTATION (12:18 — 16:11 thirteen tokens; 12:19 no kin); "destroy, you shall destroy" = "perish, you shall perish" in the piel; "under every
leafy tree" the Kings' formula; "His dwelling" one seat; the gazelle's homograph; the snare's root not 7:25's; no Molech named; the DB's 13:1 the English's 12:32.
⚠ LESSONS (thirteen, in the map): THE KIN BY COMPUTATION (the design's list a prediction); the heads the first sort, the words the second; the English's slip
asserted not corrected; five forms on the first pass; A CUT FROM THE ROW'S OWN BYTES (fourteen fell on the Name, a yod, a vav, a defective Jerusalem); the receipt's
fourth seat; the place installed not named; a law changed by a place; THE CLEAN POINT AFTER THE LEDGER (the 400k cap held); THE CHAIN LAUNCHED WHEN ITS INPUTS EXIST,
the writers typed during its run; a global replace after the named ones with the form's name protected; EVERY STEP TIMED — the machine's share {mmss(T_MACH)} of
{mmss(T_TOTAL)}. OWED TO 10b: the place a PARAMETER with five stations, the demolition by CALL (7:5, Exodus 34:13), the slaughter's switch by the entry (Leviticus 17:3-5),
the receipt's pointer at 12:21, the blood's cells (Leviticus 17:11-13), the offerings' ladder, the table and the household, the nations cut off, the register's rows;
DC the open series (DD next). UNCOMMITTED since bb62e90: the cost audit's records and sitting 10 (ONE message at <scratch>/commit_msg_ch12.txt). NEXT on the ruling: the
commit; then 10b, two runs + the tail.
'''
MEMLINE_OLD_START = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — '
MEMLINE_NEW = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — map World/step9/DEUTERONOMY_WALK.md; ch 1-11 COMPILED, PUSHED bb62e90; ch 12 READ AND FROZEN (sitting 10, every step timed; uncommitted with the cost audit); NEXT: the commit, then 10b\n'
DESC_OLD = "COMMITTED AND PUSHED THROUGH bb62e90 (2026-09-20) — SITTING 9b DONE 2026-09-20 ("
DESC_NEW = f"COMMITTED AND PUSHED THROUGH bb62e90 (2026-09-20) — SITTING 10 DONE {DATE} (chapter 12 READ AND FROZEN as one unit, the 226th — the place the LORD will choose installed here, 12:21's receipt without the Name the finder's fourth seat, the slaughter law released in new words; the first sitting under the cost rules, every step timed; uncommitted with the cost audit; 10b next) — SITTING 9b DONE 2026-09-20 ("
REC2_OLD_START = '## 2. WHERE IT STANDS'
REC2_NEW = f'''## 2. WHERE IT STANDS ({DATE}, after sitting 10; the state doc #200 addendum 1 the newest)
- NUMBERS CLOSED. DEUTERONOMY 1:1-11:32 COMPILED AND ON THE TAPE (PUSHED through bb62e90); 12 READ AND FROZEN.
- {C_UNITS} frozen units, standing 2239, hash 8b8fff1fa28953af. 66 runners, 71 daemons, 484 functions; 1145 kinds / 1042 effects.
- THE TAPE at RUN (1319, 96, 88, 0, 12, 1618, 42, 319, pairs, 127), markers 172, closes 127; the sweep 65/65; every gate GREEN.
- SITTING 10 (ch 12; EVERY STEP TIMED, the table in the AS BUILT): the place INSTALLED here; 12:21's receipt without the Name; the
  slaughter law released in new words; {L_ALL} sources whole.
- UNCOMMITTED since bb62e90: the cost audit + sitting 10 (<scratch>/commit_msg_ch12.txt). NEXT ON HIS WORD: the commit; then 10b.

'''
A_REC6 = '- Deuteronomy\'s sittings: the map; the addenda §31-51 (§39 the whole-row rule). The cost cuts: §35, §45, §47.'
A_REC6_NEW = '- Deuteronomy\'s sittings: the map; the addenda §31-54 (§39 the whole-row rule). The cost cuts: §35, §45, §47, §53.'
TOP = {
 '**41. Mishnah, Animal Offerings**': f' — 14:4-8, 9:5-6, 10:1-2 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 10, chapter 12\'s reading: the stations of the high places 12:8-11 at 65:1-2, 66:1-2; the bones and the sinews 12:27 at 78:4-5; the order of offerings at 147:2; Zevachim 112b-119b, 83a-86a, 37a; the docket at 10b)',
 '**38. Mishnah, Idolatry**': f' — 3:5, 3:7 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 10, chapter 12\'s reading: the mountains not their gods 12:2 at 60:4, the three Asherim and the three houses 12:3 at 61:5-6; Avodah Zarah 45a-48b; the docket at 10b)',
 '**43. Mishnah, Slaughter**': f' — 2:1, 2:9, 6:1, 8:1-4, 10:1 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 10, chapter 12\'s reading: the rite of slaughter at "as I have commanded you" 12:21 (75:6, 75:15), the blood like water 12:16 (71:14), flesh in milk 12:23-24 (76:7-8), the gifts 12:15 (71:9-10), the flesh of desire 12:20 (75:3-4); Chullin 16b-17a, 28a, 84a-b, 102b-103a, 113a-116a; the docket at 10b)',
 '**44. Mishnah, Firstborn**': f' — 2:2-3, 9:3 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 10, chapter 12\'s reading: the blemished consecrated redeemed 12:15 at 71:1-6, the tithe\'s joint owners at 77:7-8; Bekhorot 15a-16a, 33a-b; the docket at 10b)',
 '**46. Mishnah, Substitution**': f' — 3:5 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 10, chapter 12\'s reading: the substitute of the holy things 12:26 at 77:5-6, 78:9-10; Temurah 3b-4a, 17b; the docket at 10b)',
 '**35. Mishnah, Lashes**': f' — 3:3, 3:15 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 10, chapter 12\'s reading: the tithe and the firstling outside the wall 12:17 — the ladder of a fortiori at 72:9-11, 73:1, 74:1; the blood\'s reward 12:23 at 76:2, 76:9, 286:16; Makkot 13a-b, 17a-19b, 23b; the docket at 10b)',
 '**28. Mishnah, Suspected Wife**': f' — 7:6 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 10, chapter 12\'s reading: the Name pronounced as written only in the chosen place 12:5 at 62:4; Sotah 37b-38b; the docket at 10b)',
 '**30. Mishnah, Betrothal**': f' — 1:9 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 10, chapter 12\'s reading: the land-bound rule from the header\'s two clauses 12:1 at 59:5; Kiddushin 36b-37a; the docket at 10b)',
 '**16. Mishnah, Day of Atonement**': f' — 1:1 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 10, chapter 12\'s reading: "your households" his wife 12:7 at 64:4; the docket at 10b)',
 '**59. Mishnah, Enabling Liquids**': f' — 6:4 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 10, chapter 12\'s reading: the blood poured like water prepares seeds for uncleanness 12:16 at 71:14; the docket at 10b)',
}

CM = f'''THE COST AUDIT AND THE THREE RULES — THE BILL SPLIT THREE WAYS FROM THE TRANSCRIPTS (CACHE WRITES 45%, CACHE READS 37%, OUTPUT 17%), A THIRD OF NINE DAYS' BILL IN 169 RE-WRITES OF THE WHOLE CONTEXT AFTER WAITS LONGER THAN THE CACHE'S FIVE MINUTES, AND THREE RULES RULED (THE CACHE LAW, THE 400k CAP, FEWER CALLS); AND CHAPTER 12 READ AND FROZEN (SITTING 10 — THE FIRST SITTING UNDER THE RULES: ONE RUN TO A CLEAN POINT, THE COMPACTION, THE TAIL; EVERY STEP TIMED; EVERY ROW WHOLE) — "THE PLACE WHICH THE LORD WILL CHOOSE" INSTALLED HERE WITH NO SEAT BEFORE IT, THE HEADER'S TWIN THE FOLD'S FOOTER, THE SLAUGHTER LAW RELEASED IN NEW WORDS AS A LAW CHANGED BY A PLACE, "AS I HAVE COMMANDED YOU" THE RECEIPT WITHOUT THE NAME AT ITS FOURTH SEAT, THE LADDER OF A FORTIORI ON FIVE ITEMS, AND THE KIN FOUND BY COMPUTATION.

THE COST AUDIT (2026-09-20, after 9b's push, on the owner's "Do a complete audit of our process" and his word "Let's go to 400 a b and c"; World/step9/COST_AUDIT_2026-09-20.md with its five forms and the rules writer in World/step9/forms_deuteronomy_walk/; the map's "THE COST AUDIT AND THE THREE RULES"; the state doc's #199 addendum 4; the addenda §53; THE_BRIEFING's entry; THE_STEPS; RECORD_FORMS; GATES_CHAIN.md; the recovery page; the memory): the bill measured from the transcripts, one usage per API call — cache writes 45%, cache reads 37%, output 17%; under the writes 169 calls that re-wrote the whole context from nothing, 126 of them after a wait of five to sixty minutes (the gates chain, the sweep, the positions table, a pause) — the prompt cache dies at five minutes and every longer wait writes the pile again, a third of nine days' bill and growing with the program; under the reads a third of the calls past 600k carrying 57% of the reads; the typing a sixth, the paperwork under a twentieth. "One book at a time" set aside (it trims the paperwork and widens a slip to ten chapters). THREE RULES: A THE CACHE LAW — every long job launched in the background at the end of its run with its readers written, the clean point announced before the wait, the owner compacts, the tail on a small context reads the summary; before any break the clean point and the compaction first; B THE 400k CAP — a run ends at the clean point nearest 400k, never past 450k; C FEWER CALLS — one call per pipeline step, reads batched, batching never skipping. A compile sitting two runs + the tail; a reading sitting one run + its tail. Projected: the same work at about a third of the price.

SITTING 10 — CHAPTER 12 READ AND FROZEN ({DATE}, on the owner's "Monitor how long each step takes and report when the chapter is done" and "Reread" after the compaction at the clean point #200; World/step9/DEUTERONOMY_WALK.md "Sitting 10 — CHAPTER 12 … THE DESIGN" and "Sitting 10 — CHAPTER 12 — AS BUILT"; the state doc's #200 and its addendum 1; the addenda §54): Deuteronomy 12:1-31 with Onkelos whole (the export's 31 rows the DB's 31 — the identity, asserted; the English's 12:32 the DB's 13:1) and THE SIFREI ON DEUTERONOMY ON THE CHAPTER AGAIN — piskaot 59-81, twenty heading on the chapter's verses and THREE WITHOUT A HEAD CITATION (68 on 12:11's "your burnt offerings", 73 on 12:17's "your herd and your flock", 74 on 12:17's "your vows") folded in on their consonants, {L_SPINE} rows READ WHOLE in both files ({N_REREAD} read before at chapter 7, chapter 11 and two Genesis sittings and REREAD WHOLE — the prior reads found by computation), seven rows outside the spine citing the chapter read whole (the rest as the Land, the firstling and the second tithe, the rejoicing, the Asherah not planted, the order of offerings, build anywhere — the English's "(Dt.13:29)" a wrong chapter and the Hebrew right, the blood's reward), none excluded, the kin credited by name with the counts computed (Leviticus 17:1-16 sixteen rows; Numbers 18:8-32 twenty-five; 7:5 and 7:25-26 three; Leviticus 20:2-5 four; 18:21 one; Numbers 33:52 one; Exodus 23:24 one; Exodus 20:21 through the Mekhilta's two rows — no Onkelos row of it, of Genesis 9:4, of Exodus 34:13 or 34:24, and NONE OF DEUTERONOMY 13-16 in any ledger, asserted: never read ahead); frozen as ONE unit deu_12_place_name (the 226th; no portion edge inside it — Re'eh holds it whole), standing 2239 = 2233 + 6 as predicted, hash 8b8fff1fa28953af unmoved; the ledger logic/oral_triage/deu_12_reeh_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the spine {L_SPINE}: MATERIAL {L_SM} / CONTEXT {L_SC}; the outside rows {L_OUT}: MATERIAL {L_XM} / CONTEXT {L_XC}; coverage computed, lint 0, no cut missed); six claims DV12-01..06 verified 6/0 (the spine distributed by piska from the CITE INDEX itself), the labels census green, seated as six WITNESS_READ operators at 12:1, 5, 13, 15, 20, 29 with step E; the ritual {N_PASS} PASS; the display layer +{OV_REF12} by reference and +69 by gloss under the sitting's marker. THE FINDS: "THE PLACE WHICH THE LORD WILL CHOOSE" INSTALLED HERE — "will choose" twenty-three seats in the book and NONE BEFORE CHAPTER 12 (ten with the article, seven with "in the place"), "to put His name there" and "to make His name dwell there" the two forms, "HIS DWELLING" (12:5) one seat in the Bible — Onkelos "the house of His Shekhinah" (12:5 and 32:40 alone), "seek" His dwelling and "inquire" after their gods ONE VERB FOR TWO SEEKINGS, the shelf's five stations (the Tabernacle, Gilgal, Shiloh, Nob and Gibeon, Jerusalem — Mishnah Zevachim 14) and "every man what is right in his eyes" Judges' refrain the run's own witness; THE HEADER'S TWIN IS THE FOLD'S FOOTER — "these are the statutes and the judgments" 12:1 and Leviticus 26:46 alone; THE VERB OF ISRAEL'S PERISHING TURNED ON THE SHRINES — "destroy, you shall destroy" is "perish, you shall perish" (4:26, 8:19, 30:18) in the piel; "UNDER EVERY LEAFY TREE" THE KINGS' FORMULA for the high places (ten seats, 12:2 the Torah's one); THE DEMOLITION SAID IN NEW WORDS — 12:3 two tokens in order with 7:5, three with Exodus 34:13, 12:2 none; five verbs where 7:5 had four, the fifth the renaming for the worse (61:7); the seven offerings listed three times with the list changing (Shiloh's and Jerusalem's — 68:6); THE SABBATH'S HOUSEHOLD (5:14) at 12:18 and the feasts — 12:18 sharing thirteen tokens in order with 16:11, THE KIN FOUND BY COMPUTATION (every verse against every verse of the Bible, a new form); "take heed to yourself lest" three times in one chapter, each a prohibition on the shelf; THE SLAUGHTER LAW SAID IN NEW WORDS — Leviticus 17:3-5 one token in order with 12:15, the release named by the shelf (75:3 R. Ishmael, R. Akiva no repeal) — A LAW CHANGED BY A PLACE, the compile's question; THE GAZELLE'S HOMOGRAPH ("the beauty" — the DB's two lemmas); "on the earth you shall pour it like water" with Leviticus 17:13's dust nowhere (71:14 four ways); "you may not" read "not permitted"; THE LADDER OF A FORTIORI on 12:17's five items (72:9-11, 73:1, 74:1 — one method five times, a decision table of prohibitions); THE LEVITE'S VERSE ALONE (12:19); "as He has spoken to you" (12:20) with two teachers on the callee (75:2); "AS I HAVE COMMANDED YOU" (12:21) — THE RECEIPT WITHOUT THE NAME, Exodus 23:15 its one kin, the register's finder BLIND to it (measured) — the oral law's seat on the shelf (the rite of slaughter, the gullet and the windpipe — 75:6, 75:15; Mishnah Chullin 2:1): the finder's third form owed since 4b and 6b, its fourth seat; "BE STEADFAST" the word said to Joshua said to the eater; "THE BLOOD IS THE LIFE" Leviticus 17:11's clause turned; "SHALL BE POURED" the sin offering's verb at 12:27; "LEST YOU BE ENSNARED" another root than 7:25's; "abomination of the LORD" eight in the book; THE CHILDREN BURNED and NO MOLECH NAMED (the king-word's homograph, the census's slip); the register's switch at the chapter's middle (plural 2-12, singular 13-31, the one plural verb at 12:16, six paragogic nuns all in the plural half, no wayyiqtol, no divine frame); the parser's one number verse (12:14 [1]) and the starred tithe; Onkelos's Shekhinah, "their errors", "before the LORD", the tithe supplied at 12:26, the flesh supplied at 12:22, "keep and receive". EVERY GATE GREEN IN ONE CHAIN (ch12_gates.sh, launched in the background as one command with the manifest, verify_claims 6/0 and the labels census, the summary read once): the seat, verify_text ({VT_STEPS} steps, {VT_SCEN} scenarios), the ritual {N_PASS} PASS, CORPUS TRUTH GREEN before and after the bake ({C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, hash unmoved), build_world ALL GREEN, the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer, the tape unmoved since 9b), the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — the header at 12:1 the declared EMPTY seat; 12:21 listed nowhere), large_letter_probes {LL[-3:]}, the home-path gate GREEN; the ink {N_INK} asserts — 0 failing on its second and third runs (five forms fell on the first). THE COST RULES ON THEIR FIRST SITTING: the one run to the clean point #200 after the rows and the ledger (the 400k cap), the owner's compaction, the tail on a small context — the patch, the manifest, the seat, the chain launched as soon as its inputs existed with the records writer and the copier typed during its run. EVERY STEP TIMED (the owner's ask; the table in the map's AS BUILT, computed from ch12_timing.tsv): the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)} wall time from {T_START} to the records; the chain {mmss(CS_TOTAL)} ({CS_TXT}); the rest the reading, the typing and one compaction. THE LESSONS (thirteen, in the map's AS BUILT): the kin by computation; the heads the first sort and the words the second; the English's slip asserted, not corrected; the first typed pass fell five ways on forms; a cut is typed from the row's own bytes; the receipt's fourth seat; the place installed, not named; a law changed by a place; the header the fold's footer; the clean point after the ledger; the chain launched when its inputs exist; a global replace after the named ones with the form's name protected; every step timed. Also in this commit: COMPILE_DEBT's sitting-10 box (a)-(k) owed to the compile 10b (the place a PARAMETER with five stations, the demolition by CALL, the header's rows, the slaughter's switch by the entry, the receipt's pointer at 12:21, the blood's cells, the offerings' ladder, the table and the household, the nations cut off, the register's rows, the series DD, the docket), MIDDOT's chapter-12 block (the codes censused from the ledger's rows — {CODE_TXT}), MISHNAH_TOPICS' row notes (Animal Offerings 14:4-8, 9:5-6, 10:1-2; Idolatry 3:5, 3:7; Slaughter 2:1, 2:9, 6:1, 8:1-4, 10:1; Firstborn 2:2-3, 9:3; Substitution 3:5; Lashes 3:3, 3:15; Suspected Wife 7:6; Betrothal 1:9; Day of Atonement 1:1; Enabling Liquids 6:4 — routed to 10b), RESEARCH_LOG's entry, THE_STEPS, THE_BRIEFING (the scoreboard and an entry), World/RESUME.md, the state doc's #200 with its addendum 1, the recovery page rewritten under its cap, the addenda §54, the stamp row, the forms in World/step9/forms_deuteronomy_walk/ (the one run's and the tail's scripts and prints — the derivations, the dump, the measurement, the split, the ink and its parts, the nine row files and their patch, the ledger writer, the design and clean-point writers, the display patch and its derivation, the manifest, the seat, the three shells and their derivation, the timer and its table, the records, the copy).

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01MiJCE3AxFHu3jksQa2GG21
'''

LINT = f'{ROOT}/logic/solo_tools/gloss_lint.py'
def lint(path):
    out = subprocess.run([sys.executable, LINT, path], capture_output=True, text=True).stdout
    m = re.search(r'gloss_lint: (\d+) flag', out); return int(m.group(1)) if m else -1
WALKP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; RECP = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
TOPICS = f'{ROOT}/logic/MISHNAH_TOPICS.md'
TOUCH = [f'{ROOT}/logic/findings/STAMP_LEDGER.md', f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', f'{ROOT}/World/RESUME.md', f'{ROOT}/THE_STEPS.md', f'{ROOT}/THE_BRIEFING.md', f'{ROOT}/World/step9/COMPILE_DEBT.md', f'{ROOT}/RESEARCH_LOG.md', f'{ROOT}/logic/MIDDOT.md', RECP, f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md', TOPICS]
# ---- THE ANCHORS, ASSERTED PRESENT ONCE BEFORE ANY WRITE ----
A_RESUME = '# ⚠ THE DEUTERONOMY WALK sitting 9b — CHAPTER 11 COMPILED AND ON THE TAPE (2026-09-20; step9/DEUTERONOMY_WALK.md "Sitting 9b"'
A_SCORE = '## SCOREBOARD (as of 2026-09-20, latest)\n'
A_BULLET = '- **CHAPTER 11 COMPILED — THE RAIN CONDITIONAL GETS ITS CELL'
A_ENTRY = '### 2026-09-20 — THE COST AUDIT: WHERE A CHAPTER\'S PRICE GOES, AND THREE RULES'
A_MIDDOT = '\n## Exodus block campaign — owner\'s word "Do 3")\n'
ANCH = [(f'{ROOT}/World/RESUME.md', A_RESUME), (f'{ROOT}/THE_STEPS.md', '\n## Step 6 — Publish\n'), (f'{ROOT}/THE_BRIEFING.md', A_SCORE), (f'{ROOT}/THE_BRIEFING.md', A_BULLET), (f'{ROOT}/THE_BRIEFING.md', A_ENTRY), (f'{ROOT}/logic/MIDDOT.md', A_MIDDOT), (RECP, REC2_OLD_START), (RECP, '\n## 3. THE STANDING LAWS'), (RECP, A_REC6), (f'{MEM}/deuteronomy-walk.md', DESC_OLD), (f'{MEM}/MEMORY.md', MEMLINE_OLD_START)]
for p, a in ANCH: assert rd(p).count(a) == 1, (p, a[:40], rd(p).count(a))
tl = rd(TOPICS).split('\n'); assert all(sum(l.startswith(t) for l in tl) == 1 for t in TOP) and 'sitting 10, chapter 12' not in rd(TOPICS)
assert '## Sitting 10 — CHAPTER 12 — AS BUILT' not in rd(WALKP) and '## Sitting 10 — CHAPTER 12, Deuteronomy 12:1-31' in rd(WALKP) and '#200 ADDENDUM 1' not in rd(TOUCH[1]) and 'COMPACTION POINT #200' in rd(TOUCH[1]) and '## §54' not in rd(TOUCH[9]) and '## §53' in rd(TOUCH[9]) and 'SITTING 10 DONE' not in rd(f'{MEM}/deuteronomy-walk.md') and 'SITTING 10 — CHAPTER 12' not in rd(TOUCH[5]) and f'## {DATE} — DEUTERONOMY 12 READ' not in rd(TOUCH[6]) and 'CASE LAW ON CHAPTER 12' not in rd(TOUCH[7])
assert CHAIN_NOTE != 'CHAIN_NOTE_PLACEHOLDER', 'the chain note is typed from the summary before the records are written'
s = rd(RECP); i = s.index(REC2_OLD_START); j = s.index('\n## 3. THE STANDING LAWS'); REC_NEW = s[:i] + REC2_NEW + s[j:]
REC_NEW = REC_NEW.replace(A_REC6, A_REC6_NEW)
assert len(REC_NEW.encode()) <= 10240, len(REC_NEW.encode())
m = rd(f'{MEM}/MEMORY.md'); i = m.index(MEMLINE_OLD_START); j = m.index('\n', i) + 1; MEM_NEW = m[:i] + MEMLINE_NEW + m[j:]
assert len(MEM_NEW.encode()) < 17000, len(MEM_NEW.encode())
CMP = f'{SP}/commit_msg_ch12.txt'; assert not os.path.exists(CMP) or CHECK, CMP
for t in (WALK, DEBT, MIDDOT, RESEARCH, STEPS, BRIEF, BRIEF_ENTRY, RESUME_NOTE, STATE, ADDENDA, MEMPAR, CM, REC_NEW, MEM_NEW) + tuple(TOP.values()):
    assert SP not in t and os.path.expanduser('~') not in t, 'a scratch or home path in a record'
BEFORE = {p: lint(p) for p in TOUCH}
print('lint before:', {os.path.basename(p): n for p, n in BEFORE.items()}, '| recovery page bytes', len(REC_NEW.encode()), '| MEMORY.md bytes', len(MEM_NEW.encode()), '| commit message bytes', len(CM.encode()))
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
