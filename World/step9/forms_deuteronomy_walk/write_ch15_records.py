import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13 — CHAPTER 15 (2026-09-22; the owner: "Go" after 12b's commit — a reading sitting under THE COST RULES A-B-C in TWO RUNS + THE
# TAIL (the #204 NOTE's shape): RUN A the measurements, the ink and the design to the clean point #206; RUN B1 the first half of the rows to addendum 1 (taken
# unconditionally); RUN B2 the second half and the ledger to addendum 2 — B1 and B2 in ONE context on the owner's /context reading of 260k at B1's clean point;
# the compaction; "Reread", "Go", THE TAIL on a small context): THE RECORDS at the close, from the sheet World/step9/RECORD_FORMS.md in ONE call — the map's
# "Sitting 13 — CHAPTER 15 — AS BUILT" WITH THE TIMING TABLE computed from the scratchpad's ch15_timing.tsv, COMPILE_DEBT's box (owed to the compile 13b),
# MIDDOT's block (the codes censused from the ledger's own rows), MISHNAH_TOPICS' row notes (ROUTED to 13b), RESEARCH_LOG's entry, THE_STEPS' paragraph,
# THE_BRIEFING's bullet and entry, RESUME's note, the state doc's #206 addendum 3, the recovery page (section 2 rewritten, under 10 KB), the recovery addenda's
# §61, the stamp row, the memory file and the index line (under 17,000 bytes), and THE COMMIT MESSAGE (chapter 15's alone — chapters 1-14 pushed through
# 049f55c). Every number parsed from a print named beside it (--check prints them and writes nothing); every insert on a unique anchor asserted present once;
# the lints before and after. Sitting 12's form (write_ch14_records.py). RUN FROM THE REPO ROOT.
import os, re, subprocess, sys, yaml, json, datetime, glob
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/' + os.path.abspath(ROOT).replace('/', '-') + '/memory')
DATE = '2026-09-22'; LDATE = '2026-09-22'
UID = 'deu_15_release_firstborn'
CHECK = '--check' in sys.argv
CHAIN_NOTE = 'THE GATES CHAIN RAN ONCE, ALL GREEN ON ITS FIRST PASS (20:53:26 to 21:01:52 — 8 min 26 s: the seat (seven operators on seven steps, the scenarios in the anchor form), verify_text (23 steps, 7 scenarios), the ritual, the fold (229 / 2259 / the hash unmoved — 1,809 facts, 341 demands, 191 open), build_world, the journal gate, the register gate --strict (DECLARED 98, no demand — the register step 4 min 55 s of the chain), large_letter 6/6, the home gate; no demand, no retype; the summary read once) — launched in the background after the manifest (every cite index name used), verify_claims (7 verified / 0 failed) and the labels census (GATE PASSED, debt 0 — 3,319 claims in 232 manifests) had run in the foreground and their prints were read; the records writer and the copier typed in four parts during its 506 seconds, the notification the wake.'
def rd(p): return open(p, encoding='utf-8').read()
# ---- THE NUMBERS, PARSED FROM THE PRINTS ----
truth = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py')
assert 'assert len(W["units"]) == 229' in truth and 'assert len(W["standing"]) == 2259' in truth and "8b8fff1fa28953af" in truth
CT = rd(f'{SP}/ch15_truth.out'); CB = rd(f'{SP}/ch15_bake.out'); C1 = rd(f'{SP}/ch15_fold_check1.out')
assert 'CORPUS TRUTH GREEN' in CT and 'CORPUS TRUTH GREEN' in C1 and 'wrote corpus_world.sqlite' in CB
rit = rd(f'{SP}/ch15_ritual_{UID}.out'); N_PASS = len(re.findall(r'^PASS', rit, re.M))
assert 'RITUAL COMPLETE' in rit and N_PASS >= 1 and not re.search(r'^FAIL', rit, re.M), N_PASS
vt = rd(f'{SP}/ch15_vt_{UID}.out'); mvt = re.search(r'TEXT LAYER GREEN: (\d+) steps, (\d+) scenarios', vt); assert mvt and mvt.group(1) == '23', vt[-300:]
VT_STEPS, VT_SCEN = mvt.groups()
assert '  status: frozen' in rd(f'{ROOT}/logic/units/{UID}.yaml') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json') and 'ALL_DONE' in rd(f'{SP}/ch15_chain.log')
JG = rd(f'{SP}/ch15_journal.out'); RG = rd(f'{SP}/ch15_register.out'); BW = rd(f'{SP}/ch15_build.out'); GS = rd(f'{SP}/ch15_gates_SUMMARY.txt')
assert 'GATE GREEN' in JG and 'ALL GREEN' in BW and 'THE REGISTER GATE: GREEN' in RG and 'ALL GREEN' in GS, (JG[-200:], BW[-200:], GS[-200:])
mj = re.search(r'(\d+) kinds, ([\d,]+) rows', JG); J_KINDS, J_ROWS = mj.group(1), mj.group(2)
mr = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', RG); R_DECL, R_DEBT, R_FAIL = mr.groups()
assert R_DEBT == '0' and R_FAIL == '0' and R_DECL == '98', mr.groups()
mc = re.search(r'(\d+) units, (\d+) facts, (\d+) demands \((\d+) open\)', CT); C_UNITS, C_FACTS, C_DEM, C_OPEN = mc.groups()
assert C_UNITS == '229', C_UNITS
HG = rd(f'{SP}/ch15_home.out'); assert 'GREEN' in HG, HG[-200:]
LED = rd(f'{ROOT}/logic/oral_triage/deu_15_reeh_{LDATE}.md')
ml = re.search(r'\*\*read: (\d+) of \1 — COMPLETE\*\* \((\d+) Onkelos verses and (\d+) Sifrei rows.*?MATERIAL (\d+) Onkelos, CONTEXT (\d+) Onkelos, MATERIAL (\d+) Sifrei spine, CONTEXT (\d+) Sifrei spine, MATERIAL (\d+) Sifrei outside, CONTEXT (\d+) Sifrei outside', LED, re.S)
L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_SM, L_SC, L_XM, L_XC = ml.groups()
assert L_ALL == '132' and L_ONK == '23' and L_SIF == '109' and LED.count('⟨MISS⟩') == 0
L_SPINE = int(L_SM) + int(L_SC); L_OUT = int(L_XM) + int(L_XC); assert L_SPINE == 99 and L_OUT == 10, (L_SPINE, L_OUT)
L_BYTES = len(LED.encode())
SEC_SPINE = LED.split('## Sifrei Devarim rows citing chapter 15')[0]; SEC_OUT = LED.split('## Sifrei Devarim rows citing chapter 15')[1].split('## Onkelos')[0]
N_REREAD = len(re.findall(r'^- Sifrei Devarim \d+:\d+ — [A-Z]+ \(REREAD WHOLE — read before in', SEC_SPINE, re.M)); N_REREAD_OUT = len(re.findall(r'^- Sifrei Devarim \d+:\d+ — [A-Z]+ \(REREAD WHOLE — read before in', SEC_OUT, re.M))
assert N_REREAD == 2 and N_REREAD_OUT == 6, (N_REREAD, N_REREAD_OUT)
CODES = Counter(); BYCODE = {}
for line in re.findall(r'^- Sifrei Devarim \d+:\d+ — .*$', LED, re.M):
    name = re.match(r'- (Sifrei Devarim \d+:\d+)', line).group(1)
    for c in sorted(set(re.findall(r'\b([IE]\d{1,2}) \(', line))): CODES[c] += 1; BYCODE.setdefault(c, []).append(name.split(' ')[2])
CODE_TXT = '; '.join(f'{c} at {", ".join(BYCODE[c])}' for c in sorted(CODES, key=lambda x: (x[0], int(x[1:]))))
print('CODES BY ROW:', CODE_TXT, '| the sum', sum(CODES.values()))
for c, r in (('I2', '111:1'), ('I2', '111:7'), ('I2', '117:3'), ('I2', '122:6'), ('I2', '122:8'), ('I2', '71:6'), ('I3', '111:3'), ('I1', '112:3'), ('I1', '112:4'), ('I1', '124:3'), ('I1', '124:6'), ('I1', '71:6'), ('E30', '117:1'), ('I6', '119:4'), ('I8', '126:1')): assert r in BYCODE.get(c, []), (c, r, BYCODE.get(c))
assert dict(CODES) == {'I1': 5, 'I2': 6, 'I3': 1, 'I6': 1, 'I8': 1, 'E30': 1}, dict(CODES)   # the census typed from its own print (the tail's foreground call)
N_I13 = len(re.findall(r"I13's question", LED)); assert N_I13 >= 2, N_I13   # 114:1 and 118:1 name I13's question without a code — the third verse absent
d_ov = yaml.safe_load(rd(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'))
OV_REF15 = len([k for k in d_ov['by_ref'] if k.startswith('Deut.15.')]); OV_REF, OV_GL = len(d_ov['by_ref']), len(d_ov['by_gloss'])
assert OV_REF15 == 168 and OV_REF == 1421 and OV_GL == 800, (OV_REF15, OV_REF, OV_GL)   # the patch's own print
N_CLAIMS = len(json.load(open(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json', encoding='utf-8'))); assert N_CLAIMS == 7
VC = rd(f'{SP}/ch15_vc.out'); assert 'SUMMARY: 7 verified, 0 failed, 0 uncheckable, 0 no-check' in VC, VC[-300:]
LAB = rd(f'{SP}/ch15_labels.out'); mlab = re.search(r'CLAIM LABELS CENSUS — (\d+) claims in (\d+) manifests; labeled \1; DEBT 0', LAB); LN = f'{int(mlab.group(1)):,} claims in {mlab.group(2)} manifests'; assert 'GATE PASSED' in LAB and re.search(r'deu\s+96 claims', LAB), LAB[-300:]
INKF = {n: int(re.search(r'(\d+) failing statements', rd(f'{SP}/ch15_ink_run{n}.out')).group(1)) for n in (1, 2, 3, 4)}
assert INKF == {1: 3, 2: 0, 3: 0, 4: 0}, INKF
N_INK = len(re.findall(r'^assert ', rd(f'{SP}/ch15_ink.py'), re.M)); assert N_INK == 128, N_INK   # the count from the tail's grep print
LL = rd(f'{SP}/ch15_large_letter.out').strip().split('\n')[-1]; assert LL.endswith('6/6'), LL
JPREV = f'{ROOT}/World/step9/forms_deuteronomy_walk/gates_ch14b_journal.out'
JR14 = re.search(r'12 kinds, ([\d,]+) rows', rd(JPREV)).group(1); DJ = int(J_ROWS.replace(',', '')) - int(JR14.replace(',', ''))
MAN = rd(f'{SP}/ch15_manifest.out'); assert 'every CITE INDEX name used by a claim: True' in MAN
DUMP = rd(f'{SP}/ch15_dump0.out'); mdump = re.search(r'DB verses (\d+) \| export verses HE (\d+) EN (\d+)', DUMP); assert mdump and mdump.groups() == ('23', '23', '23'), DUMP[:300]
LEDW = rd(f'{SP}/write_ch15_ledger3.out'); assert '132 sources' in LEDW and 'MISMARK []' in LEDW and 'FAIL []' in LEDW, LEDW[-200:]
PATCH_LINE = rd(f'{SP}/ch15_patch.out').strip().split('\n')[-1]; assert PATCH_LINE == 'override rows written: by_ref 168 by_gloss 44 | by_ref total 1421 | by_gloss total 800', PATCH_LINE
PROBE = rd(f'{SP}/ch15_manifest_probe.out') if os.path.exists(f'{SP}/ch15_manifest_probe.out') else ''
# ---- THE TIMING TABLE, computed from the scratchpad's tsv (the first step's own stamp is the start) ----
def timing():
    rows = [l.rstrip('\n').split('\t') for l in rd(f'{SP}/ch15_timing.tsv').splitlines() if l.strip()]
    day = datetime.datetime(2026, 9, 22)
    def at(hms): h, m, s = map(int, hms.split(':')); return int(day.replace(hour=h, minute=m, second=s).timestamp())
    t0 = at(rows[0][0])
    out = ['| step | began | ran | the gap before it (reading, typing, the owner\'s compactions) |', '|---|---|---|---|']
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
print('PARSED:', dict(ritual_pass=N_PASS, verify_text=(VT_STEPS, VT_SCEN), journal=(J_KINDS, J_ROWS, DJ, JR14), register=(R_DECL, R_DEBT, R_FAIL), corpus=(C_UNITS, C_FACTS, C_DEM, C_OPEN), ledger=(L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_SM, L_SC, L_XM, L_XC, L_BYTES, N_REREAD, N_REREAD_OUT), codes=dict(CODES), overrides=(OV_REF15, OV_REF, OV_GL), claims=N_CLAIMS, labels=LN, ink=(N_INK, INKF), large_letter=LL[-3:], timing=(T_ROWS, T_MACH, T_TOTAL, T_START), chain=(CS_TXT, CS_TOTAL)))
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

STAMP = (f'| {DATE} | {UID} | DELEGATED | FULL RULE | Deuteronomy 15:1-23 derivation {LDATE} (THE DEUTERONOMY WALK sitting 13 — CHAPTER 15; the owner: "Go" after 12b\'s commit — a reading sitting under THE COST RULES in TWO RUNS + THE TAIL: the measurements, the ink and the design to #206; the rows in two halves to #206 addenda 1-2 with the ledger; the tail after the compaction; every step timed, every row whole): Onkelos Deuteronomy 15 whole (23 = 23, the identity) + the Sifrei on Deuteronomy ON THE CHAPTER — sixteen piskaot 111-126 in verse order, no tail folded in, {L_SPINE} spine rows read whole in both files ({N_REREAD} rows read before and reread whole) + its {L_OUT} rows outside the spine read whole ({N_REREAD_OUT} reread whole) + the kin credited by name from ten ledgers; the ledger deu_15_reeh_{LDATE}.md ({L_ALL} sources, coverage computed, lint 0); {N_CLAIMS} claims DV15-01..07 verified 7/0, seated as seven WITNESS_READ at 15:1, 4, 7, 12, 16, 19, 21; the ritual {N_PASS} PASS; CORPUS TRUTH GREEN ({C_UNITS} units, standing 2259, hash unmoved); the fold layer +{DJ}; the display layer +{OV_REF15} by reference, +44 by gloss; the machine\'s share of the sitting {mmss(T_MACH)} of {mmss(T_TOTAL)} | {LN}, labeled, debt 0 |\n')

WALK = f'''


## Sitting 13 — CHAPTER 15 — AS BUILT ({DATE}; the design above stands as written but for one thing — RUN B1 and RUN B2 ran in ONE context: at B1's clean point the owner read /context at 260k and said "Go" without compacting, his call; the clean point itself was taken unconditionally as the design ruled; RUN A ended at 517k by his reading (under the 600k cap); the owner compacted after A and after B2, and THE TAIL ran on "Reread" and "Go"; every departure from the design is named here; THE TIMING TABLE is the last section)

THE RESULT: Deuteronomy 15:1-23 READ, FROZEN and SEATED as ONE unit — deu_15_release_firstborn (the 229th frozen unit; 23 of 23 verses, missing 0, computed — the
export's chapter 15 the DB's, the identity; no portion edge inside it): the ledger logic/oral_triage/deu_15_reeh_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} /
CONTEXT {L_OC}; THE SIFREI'S SPINE piskaot 111-126, {L_SPINE} rows: MATERIAL {L_SM} / CONTEXT {L_SC}, {N_REREAD} of them read before and REREAD WHOLE (the prior reads found in the
earlier ledgers by computation — 117:3 at chapter 13's sitting, 116:18 at the Genesis 2 sitting); the outside rows {L_OUT}: MATERIAL {L_XM} / CONTEXT {L_XC}, {N_REREAD_OUT} of them read
before and REREAD WHOLE — 41:3 from chapter 11, 71:6-8 from chapter 12, 106:5 from chapters 12 and 14 (its third read), 109:3 from chapter 14; 147:3-4, 279:4 and
355:9 fresh; {L_BYTES:,} bytes, lint 0, no cut missed — the writer fell twice on its own asserts before it wrote: the Name's bare count and the homograph of Moses'
name), the manifest {N_CLAIMS} claims DV15-01..07 verified 7/0 (every he_contains cut from the store's own bytes — the seven words' pieces PROBED in the store before
they were typed, every one over the floor of four code points; every cite index name used by a claim — the spine's rows distributed by piska from the CITE
INDEX itself, piskaot 116 and 118 split at the rows where they turn to the next verse, the ten outside rows with the claims whose verses they cite), seated as
seven WITNESS_READ operators at 15:1, 4, 7, 12, 16, 19, 21 with step E; the ritual {N_PASS} PASS; verify_text GREEN ({VT_STEPS} steps, {VT_SCEN} scenarios); the fold predicted
and matched (units 228 → 229, standing 2252 → 2259, the hash 8b8fff1fa28953af unmoved — CORPUS TRUTH GREEN before and after the bake: {C_UNITS} units, {C_FACTS} facts,
{C_DEM} demands, {C_OPEN} open); build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer since 12b's chain, the tape unmoved since
12b); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — no receipt, no header, no footer in chapter 15: 15:6's "as He spoke to you" not a
receipt by the finder's forms, 15:2's "this is the manner" not a register header, the four number verses no count lines — as the design predicted);
large_letter_probes {LL[-3:]}; the labels census GREEN ({LN}, Deuteronomy 96); the home-path gate GREEN; the display layer +{OV_REF15} by reference and +44 by
gloss ({OV_REF} / {OV_GL} in all).

THE READING: every Onkelos row whole in the Aramaic and the English (ch15_onkelos.txt); THE SPINE ON THE CHAPTER A SEVENTH TIME — sixteen piskaot 111-126 heading
on the chapter's verses IN VERSE ORDER (chapter 14's were not), seven verses without a head (7, 8, 10, 12, 14, 22, 23), NO TAIL FOLDED IN (110's rows all on
14:29 and read at chapter 14; 126's rows stop before 16:1's words — both ends checked on the consonants), every row read whole in both files
(ch15_sifrei_spine.txt, split by piska for the reading — ch15_spine_p111.txt … p126.txt); the ten outside rows whole in both files (ch15_sifrei_outside.txt —
the release after the conquest at 11:13, the permanent blemish and the one dish at 12:15, the firstling's year at 14:23, "the end" at 14:28, the blemishes at
17:1, the hireling's cry at 24:15, Moses' righteousness at 33:20), none excluded; the kin (Leviticus 25's sabbatical, poor brother and sold brother in three
ledgers; Leviticus 22:17-27 and 21:16-23; Leviticus 27:26; Numbers 18:15-18; Deuteronomy 12:6, 15-18, 22-24; 14:28-29; 5:15) credited by name with the counts
computed from ten ledgers; no ledger holds an Onkelos row of Exodus 21:2-11, 23:10-11, 22:24-26, 22:29, 13:2-16 or 34:19-20, of Genesis 4:4, and NONE OF
DEUTERONOMY 16-34 OR THE PROPHETS (asserted — never read ahead; 16:5's gates, 16:12's slave remembered, 17:1's blemish, 17:18's copy, 23:17's escaped slave,
23:20-21's interest, 24:10-15's pledge and the hireling's cry, 24:18-22's sojourner, 26:12-19, 28:1-12's blessing and its lending, 29:12, 31:10's release-year
assembly wait for their own sittings; Jeremiah 34 the run's case, never a row).

THE DEPARTURES FROM THE DESIGN: none in the shape of the runs, seven in the instruments. (1) RUN B1 AND RUN B2 IN ONE CONTEXT — at B1's clean point (#206 addendum
1, taken unconditionally as the design ruled) the owner read /context at 260k and said "Go" without compacting: the clean point is the design's, the compaction
his. (2) THE LEDGER WRITER FELL TWICE ON ITS OWN ASSERTS — the design's text said "the Name thirteen bare" where the writer's print read 12 (the assert retyped
from the print — a count in the design's prose is not the ink), and "Moses, Israel never named" fell on 15:2's מַשֵּׁה ("the loan" of his hand), the same letters
as Moses (lemma 4874 against Moses' 4872 at 1:1 — retyped by lemma and recorded in the register paragraph). (3) NINE CUT MISSES on the rows' first checks — EIGHT
THE EXPORT'S DEFECTIVE SPELLINGS UNDER ITS VOWELS (כלם "all of them", אפלו "even", תכבש "you will conquer", מצוה "commanded" — the full-spelling habit typed where
the print's letters differ) and one a vav from the word before (125:1); every one retyped from the print, the second checks green. (4) THE ARAMAIC PIECES ON
15:4, 7 AND 11 CUT BESIDE "NEEDY" — the export writes its kaf as a presentation-form letter the cutter does not fold; the ink's seat counter reads through NFKC
and finds the five seats (15:4, 7, 9, 11; 24:14); chapter 14's Aramaic counts stand as measured, a note for 13b. (5) THE SHELLS' DERIVE FELL ONCE ON ITS OWN
COUNT — the unit named once in the chain, not twice; retyped from the assert's print. (6) verify_claims CALLED WITH THE UNIT'S NAME where it takes the manifest's
path — the argument retyped from its own error. (7) THE INK'S THIRD PASS CARRIED THE PATCH BLOCK AS BODY D (the design's plan), the fourth pass PATCHED green —
the counting asserts patch-aware from the start (chapter 14's lesson 3 held). THE DISPLAY PATCH held first time (twelve asserted substitutions on the chapter-14
form with its portable header stripped; the two counts read from the ink's third-pass print; the anchors sitting 12's last rows found by walking, never typed;
{PATCH_LINE}). THE MIDDAH CODES held — every code checked in MIDDOT.md before it was typed, none relabeled: the census from the ledger's rows — {CODE_TXT}; I13's
question named at 114:1 and 118:1 without its third verse (the two verses upheld by a condition), no code. {CHAIN_NOTE}

THE GATES, COMPUTED FROM THEIR PRINTS: the ritual {N_PASS} PASS (RITUAL COMPLETE, {C_UNITS} frozen units); CORPUS TRUTH GREEN twice ({C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, {C_OPEN} open;
the hash unmoved); build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows, +{DJ}); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL});
verify_claims 7 verified / 0 failed; the labels census GREEN ({LN}); large_letter_probes {LL[-3:]}; the home-path gate GREEN; the ink {N_INK} asserts — the four passes
{INKF[1]} / {INKF[2]} / {INKF[3]} / {INKF[4]} failing (the first the instrument's shapes — a ledger's whole-row count for its Onkelos-row count, a verse range one verse too wide, the
firstling's short form without its preposition; the second green; the third green with the patch block; the fourth green PATCHED).

⚠ THE LESSONS (the runs', gathered — the numbered list the sheet asks for): (1) THE POINTED EXPORT SPELLS DEFECTIVELY UNDER ITS VOWELS — a cut's consonants are typed
from the print's letters, never from the full-spelling habit: eight misses of nine were this one shape, and SP_ caught every one. (2) A COUNT IN THE DESIGN'S
PROSE IS NOT THE INK — "thirteen bare" was a slip of the summary; the assert is retyped from the writer's own print, and the design's number corrected here: the
Name 12 bare and 3 with "to". (3) A NAME'S LETTERS ARE NOT THE NAME — 15:2's "the loan" wears Moses' letters; "never named" is asserted by lemma, and the
registry's homographs gain a pair. (4) THE ARAMAIC EXPORT CARRIES PRESENTATION-FORM LETTERS — a substring count misses them unless folded through NFKC; the
seat counter folds, the piece cutter does not (the pieces are typed around such a word); chapter 14's Aramaic counts owe a re-measure at 13b. (5) THE CLEAN POINT IS
UNCONDITIONAL, THE COMPACTION IS HIS — B1's clean point was taken at 63 rows as the design ruled; on his /context reading (260k) he ran B2 in the same context and
the reading ended near 450k by the run's own estimate: the rule stands, the owner reads the counter. (6) THE RECEIPT'S REFERENT CAN POINT FORWARD — 116:1
answers "as He spoke to you" with 28:3, a verse the book has not yet spoken; for the compile a labeled HYPOTHESIS until 28:3's sitting (the receipt's third shape
after the Name's and the back-pointer's). (7) THE MISHNAH INSIDE THE SPINE — five times the Sifrei cites the answer sheet by name (Sheviit 10:8, 10:2, 10:3-4;
Shekalim 5:6; Kiddushin 1:2): the compile rules cite the answer sheet, and HILLEL'S PROZBUL is a procedure the verse leaves open — a parameter, not code. (8) TWO
VERSES UPHELD BY A CONDITION, NOT A THIRD VERSE — 15:4 against 15:11 at 114:1 and 118:1: I13's question without its third verse; the compile's state variable.
(9) THE TWO FILES DISAGREE (124:6's closing verse read opposite ways) AND TWO SPINES DISAGREE (123:1's night service against the Mekhilta) — disputes for the exam,
never resolved by the ink. (10) R. ISHMAEL'S THREE PLACES WHERE THE HALAKHA CIRCUMVENTS SCRIPTURE (122:1 — the blood's dust, the divorce's writ, the awl) — the
code/data separation law's hardest case, inside the spine. (11) THE KIN BY COMPUTATION AGAIN — Jeremiah 34:14 is 15:12's closest kin in the whole Bible (seven of
fifteen in order), closer than Exodus 21:2; 15:14 has no kin above two tokens; 15:15's closest is 24:18. (12) EVERY STEP TIMED — the machine's share of the sitting
{mmss(T_MACH)} of {mmss(T_TOTAL)} wall time from {T_START} to the records; the rest the reading, the typing and two compactions: the reading is the sitting, the
machine its instrument.

THE TIMING TABLE (every row appended by the scratchpad's timer as the step ran; the gap column is the time between one step's end and the next step's start — the
reading of the rows, the typing of the scripts, the owner's compactions between the clean points and the rereads; the chain's inner steps from its own summary's
stamps):

{TT}

The chain's inner steps (ch15_gates_SUMMARY.txt): {CS_TXT}; the chain {mmss(CS_TOTAL)} in all. The machine's share {mmss(T_MACH)}; the sitting {mmss(T_TOTAL)} from {T_START}
to the last row above; the records writer's own row and the copier's follow in ch15_timing.tsv (copied into the forms).

THE FORMS: World/step9/forms_deuteronomy_walk/ (copy_ch15_forms.py — derive_ch15_dump0.py, ch15_dump0.py, derive_ch15_measure1.py, ch15_measure1_sections_a.py
and _b.py, ch15_measure1.py, split_ch15_spine.py, ch15_ink_head.py, ch15_ink_body.py, _b.py, _c.py, _d.py, derive_ch15_ink.py, ch15_ink.py, assert_driver.py, the
eight row files and their two import checks, write_ch15_ledger.py, write_ch15_design.py, the three clean-point writers, derive_ch15_patch.py,
ch15_patch_overrides.py, ch15_manifest_probe.py, write_ch15_manifest.py, seat_ch15.py, derive_ch15_shells.py, ch15_chain.sh, ch15_fold.sh, ch15_gates.sh, tstep.sh,
write_ch15_records.py, copy_ch15_forms.py, the prints, the split piskaot and ch15_timing.tsv).

NEXT on the ruling: the commit on the owner's word (chapter 15 stands uncommitted since 049f55c — the message at <scratch>/commit_msg_ch15.txt); then THE COMPILE
OF CHAPTER 15 (sitting 13b) in TWO RUNS + THE TAIL under the cost rules — RUN A: the rereads (THE_STEPS Step 5 + the compiler block; this section; the 13b box in
COMPILE_DEBT), the measurements (Leviticus 25's cells for the sabbatical and the sold brother; Exodus 21's slave cell through its spine; the firstling's cells from
Numbers 18 and Leviticus 27; chapter 12's blood and place cells; the running world's sabbatical count for the release's year; the register's finder at 15:2 and
15:6; chapter 14's Aramaic counts re-measured through NFKC), THE DESIGN (the release as an EFFECT on the debts at the year's end with its onset and territory
PARAMETERS and the prozbul a PARAMETER from the answer sheet; the needy's ranks a PRECEDENCE PARAMETER; the hand opened as a status with the pledge dispute two
arms and the measure of need a bound; the Hebrew slave's three cases with the exits' two tables and the gift's feature a dispute; the awl's rite by day with the
judges and the upper right ear, "for ever" the master's lifetime; the double hire the night's service; the firstling's year of two days a CLOCK DATUM, "sanctify"
for its value; the blemish's class visible and permanent with 17:1 by CALL when it comes; the blood by CALL to chapter 12's cells with the olive and the warning;
the checkpoint series DG), the probes to FAIL, THE DOCKET by the union rule (Mishnah Sheviit 10:1-9 with Gittin 36a-37b and Arakhin 32b-33a; Makkot 3b; Rosh
Hashanah 8b-9a; Mishnah Kiddushin 1:2-3 with Kiddushin 14b-22b; Bava Metzia 31b and 71a; Mishnah Peah 8:7-9 with Ketubot 67b; Mishnah Bekhorot 1:1-2, 2:6-9,
3:3-4, 4:1-2, 5:1-6, 6:1-12 with Bekhorot 25a-28b, 26b-27b, 33a-37b, 53b; Mishnah Temurah 3:5; Mishnah Arakhin 8:7; Mishnah Shekalim 5:6; Mishnah Chullin 2:9; the
Sifra on Leviticus 25 credited from its sitting — every row whole; a docket past ~700 rows its own run); RUN B: the types, the runner, the tape to 10/10, the chain
LAUNCHED; THE TAIL the records, the forms, the message — or the Decalogue-schema sitting first, on his word.
'''

DEBT = f'''

## SITTING 13 — CHAPTER 15 ({DATE}, the reading; deu_15_release_firstborn frozen) — OWED TO THE COMPILE 13b: (a) THE RELEASE (15:1-3) — "end" at the year's end
## by the analogy with 31:10 (111:1 — I2; 109:3's Booths for the tithe's end), THE ONE CALENDAR — seven years for the whole world, never for each debtor (111:3-8
## — I2 named in the Hebrew; Rosh Hashanah 8b-9a): the release-year A DATE PARAMETER read from the world's count (THE RUNNING WORLD'S SABBATICAL COUNT the
## measurement owed), the onset after the conquest and the territory in and outside the Land (111:9-11, 112:11, 41:3 — TWO PARAMETERS; Gittin 36a-b the release by
## decree when the jubilee is not; Arakhin 32b-33a), the manner the word said (112:1 — Mishnah Sheviit 10:8), the object loans only and standing debts (112:5-7;
## Sheviit 10:1-2), the two years' powers (112:2-4 — I1; Leviticus 25:13 by CALL), the exaction a prohibition (112:8), the neighbor and the brother two exclusions
## (112:9-10), the foreigner a positive command (113:1), THE PLEDGE-LOAN NOT RELEASED (113:2 — Sheviit 10:2) and HILLEL'S PROZBUL — "your hand" and not the
## court's, the procedure the verse leaves open: A PARAMETER FROM THE ANSWER SHEET (113:3 — Sheviit 10:3-4; Gittin 36a-37b), the witnesses (Makkot 3b); Exodus
## 23:10-11 through its spine, Leviticus 25:1-7 by CALL; (b) THE NEEDY AND THE BLESSING (15:4-6) — THE TWO VERSES UPHELD BY A CONDITION (114:1, 118:1 — I13's
## question without its third verse): a state variable with the blessing's arm and the default, the blessing only in the Land (114:2), the reward clause (114:3),
## THE WORDS OF THE SCRIBES (115:1 — the oral law named), the light as the weighty (115:2), THE RECEIPT'S REFERENT FORWARD — 28:3 a labeled HYPOTHESIS until its
## sitting (116:1), lend not borrow, rule not be ruled (116:2-3 — Judges 1:7 the run's case); (c) THE HAND OPENED (15:7-11) — THE RANKS OF THE POOR a PRECEDENCE
## PARAMETER (116:4-8; Bava Metzia 71a), the heart's state before the hand's (116:10-11), open and give a hundred times (116:12, 117:6), the gift dressed as a loan
## (116:13), THE PLEDGE A DISPUTE — R. Judah and the sages, two arms (116:14; Bava Metzia 31b), THE MEASURE OF NEED — not to enrich, even a horse and a slave, the
## wife (116:15-18 — Mishnah Peah 8:7-9; Ketubot 67b), "base" without a yoke and idolatry by the analogy with 13:14 (117:1-3 — E30, I2; 13:14's cell by CALL),
## beware and lest two prohibitions (117:2), the cry a hastener and the sin unconditional (117:5; 279:4 at 24:15 by CALL when it comes), the secret gift (117:7 —
## Mishnah Shekalim 5:6), the four grades of the giver (117:8), the three measures (118:3); 14:28-29's four at the gate by CALL; (d) THE HEBREW SLAVE (15:12-15)
## — THE THREE CASES, each twin law its own (118:4 — Exodus 21:2 and Leviticus 25:39 by CALL; Mishnah Kiddushin 1:2-3; Kiddushin 14b-22b), the man's and the
## woman's exits TWO TABLES (118:5 — Mishnah Kiddushin 1:2), the son not the heir, the fugitive and the sick (118:6-7), THE GIFT — the three sendings, not the
## heirs, only what resembles the particular with the feature a dispute (119:1-4 — I6; Kiddushin 17a), the measure four opinions (119:5 — a dispute), Egypt the
## model (120:1), BY DAY THEY PIERCE (120:2 — a time datum); 5:15 by CALL; (e) THE AWL (15:16-17) — two sayings and two times (121:1-2), the love mutual and the
## house (121:3), illness bars (121:4; Kiddushin 22a-b), any tool or metal A DISPUTE (122:1), the judges present (122:3), the upper right ear by the analogy with
## the leper's (122:5-6 — I2; Leviticus 14:14 by CALL), through into the door (122:7), "FOR EVER" THE MASTER'S LIFETIME — the son not the daughter, the pierced no
## heir (122:8 — I2), "likewise" the gift not the awl (122:9); R. ISHMAEL'S THREE CIRCUMVENTIONS a DATA row (122:1); (f) THE DOUBLE HIRE (15:18) — the night's
## service against the Mekhilta (123:1 — A DISPUTE OF TWO SPINES; Kiddushin 15a), the blessing beside every money loss (123:3 — a rule of the book's form); (g)
## THE FIRSTLING (15:19-20) — its year and the blemished (124:1), the caesarean out (124:2 — Mishnah Bekhorot 2:9), the consecrated by the refuted a fortiori
## (124:3 — I1), "SANCTIFY" FOR ITS VALUE, NEVER FOR THE ALTAR (124:4 — Mishnah Arakhin 8:7; Leviticus 27:26 by CALL), "your" two ways (124:5 — a dispute), the
## two bars crossed and THE TWO FILES OPPOSITE (124:6 — a dispute), "YEAR BY YEAR" TWO DAYS ACROSS THE YEAR'S EDGE (125:1 — a CLOCK DATUM; Bekhorot 26b-27b), the
## year passed no bar (106:5); the shearing and the work (Bekhorot 25a-28b); Numbers 18:15-18 by CALL; (h) THE BLEMISH AND THE BLOOD (15:21-23) — the class
## visible and permanent (126:1 — I8; 147:3-4 at 17:1 by CALL when it comes; Bekhorot 33a-37b; Leviticus 22:17-27 and 21:16-23 by CALL), the permanent blemish
## lent to all the consecrated (71:6 — I2), one dish and the heave-offering apart (71:7-8), drinking is eating (126:2), THE WITNESSES' WARNING gating the penalty
## (126:3), THE OLIVE a quantity (126:4), the ground not the pit, the house not the market (126:5 — Mishnah Chullin 2:9), the neck and the seeds (126:6); chapter
## 12's blood and place cells by CALL, Keritot 20b-22a credited from chapter 12's docket; (i) THE EFFECTS — the release on the debts and the exaction's
## transgression, the blessing on the work of the hand (15:10, 15:18), the sin of the cry (15:9), the gift's status (15:14), the slave's status for ever (15:17);
## (j) THE KIN BY CALL — Exodus 21:2-11 and 23:10-11 through their spines; Leviticus 25 whole; 22:17-27, 21:16-23, 27:26; Numbers 18:15-18; 5:15, 12:6-24,
## 14:28-29; (k) NEVER READ AHEAD — 16:5, 16:12-13, 17:1, 17:18, 21:3, 23:17-22, 24:14-22, 26:12-19, 28:1-12, 29:12, 31:10 wait for their sittings — their cells
## by CALL when they come; (l) THE REGISTER's DATA rows — SINGULAR END TO END, 15:2 addressing no one, one imperative, eight infinitive absolutes, THE ONE
## NARRATIVE VERB (15:15 "redeemed you" — the T1 row), the four number verses and the ordinal, the homograph of Moses' name at 15:2, no written/read pair; (m)
## THE AS-MEASURED NOTE — chapter 14's Aramaic counts re-measured through NFKC; (n) THE CHECKPOINT SERIES continues (DF the sixth name — DF9 the last; the next
## DG1, keyed by its first word); (o) THE DOCKET by the union rule — the testing shelf as the design and the AS BUILT list it (Mishnah Sheviit 10:1-9 with Gittin
## 36a-37b and Arakhin 32b-33a; Makkot 3b; Rosh Hashanah 8b-9a; Mishnah Kiddushin 1:2-3 with Kiddushin 14b-22b; Bava Metzia 31b, 71a; Mishnah Peah 8:7-9 with
## Ketubot 67b; Mishnah Bekhorot 1:1-2, 2:6-9, 3:3-4, 4:1-2, 5:1-6, 6:1-12 with Bekhorot 25a-28b, 26b-27b, 33a-37b, 53b; Mishnah Temurah 3:5; Mishnah Arakhin
## 8:7; Mishnah Shekalim 5:6; Mishnah Chullin 2:9; the Sifra on Leviticus 25 credited from its sitting) — EVERY ROW WHOLE; a docket past ~700 rows its own run;
## THE COST RULES: two runs + the tail, the chain launched at RUN B's end. NOTHING ELSE IN CHAPTER 15 IS OWED TO A LATER SITTING OF ITS OWN.
'''

MIDDOT = f'''- **THE SIFREI ON DEUTERONOMY'S OWN CASE LAW ON CHAPTER 15 (Deuteronomy 15:1-23; THE DEUTERONOMY WALK sitting 13, {DATE};
  the ledger logic/oral_triage/deu_15_reeh_{LDATE}.md — THE SPINE ON THE CHAPTER A SEVENTH TIME, sixteen piskaot 111-126 with the heads in
  verse order and no tail folded in, {L_SPINE} rows read whole in both files, and ten rows outside the spine; EVERY CODE CHECKED IN
  MIDDOT.md BEFORE IT WAS TYPED, none relabeled; the census from the ledger's own rows: {CODE_TXT}):**
  · THE VERBAL ANALOGY NAMED IN THE HEBREW (111:7 on 15:1): two paradigms deadlocked — the land's release (seven years for the whole
    world) against the Hebrew slave (seven for each one), each with a feature the other lacks (the jubilee, the territory) — and the
    deadlock broken by the row's own words ״שֶׁבַע שָׁנִים״ ״שֶׁבַע שָׁנִים״ לִגְזֵרָה שָׁוָה ("seven years, seven years, for an analogy") — I2
    (checked): THE ONE CALENDAR, the release-year the world's, never the debtor's; R. Yose the Galilean's "draws near" the second proof
    (111:8, 117:4); the paradigm's own name at 111:3 (I3, checked — the reasoning from the land's release before the analogy decides).
  · "END" HERE AND "END" THERE (111:1 on 15:1; 109:3 on 14:28): נֶאֱמַר כָּאן ״קֵץ״ וְנֶאֱמַר לְהַלָּן ("end is said here and end is said there")
    — the release at the year's end by 31:10's assembly; the tithe's end at Booths by the same word, then 26:12's "finished" picks Passover
    — I2 (checked at both seats; 109:3 REREAD WHOLE from chapter 14).
  · "BASE" HERE AND "BASE" THERE (117:3 on 15:9): the base thought is idolatry by 13:14's sons of Belial — I2 (checked; REREAD WHOLE from
    chapter 13); and "BASE" CUT INTO TWO WORDS (117:1): בְלִיַּעַל בְּלִי עוֹל ("base — without a yoke"): whoever withholds mercy throws off the
    yoke of Heaven — E30 (checked; the row's own division of the word).
  · "HIS EAR" HERE AND "HIS EAR" THERE (122:6 on 15:17): the right ear by the leper's (Leviticus 14:14), in its upper part by the priest not
    blemished (122:5) — I2 (checked); "FOR EVER" HERE AND THERE (122:8 on 15:17): the master's lifetime by Exodus 21:6 — the son not the
    daughter, the pierced one neither — I2 (checked; the row names the analogy on the word); "YOUR GATES" HERE AND THERE (71:6 on 12:15 for
    15:22): the permanent blemish lent to all the consecrated after the a fortiori from the firstling is refuted — I2 and I1 (checked;
    REREAD WHOLE from chapter 12).
  · THE TWO YEARS' POWERS (112:3 and 112:4 on 15:2): if the release, which frees no slave, releases a loan, the jubilee which frees slaves
    should release a loan — cancelled by "this is the manner of the release"; if the jubilee, which releases no loan, frees slaves, the
    seventh year should free slaves — cancelled by "in this year of jubilee" (Leviticus 25:13) — I1 (checked at both seats): two verses'
    "this" the fence around two a fortiori arguments.
  · THE A-FORTIORI REFUTED, THEN THE VERSE (124:3 on 15:19; 124:6 on 15:19): the work and the shearing of all the consecrated from the
    firstling's, refuted, then "every firstling"; the ox's shearing and the flock's work crossed by four arguments — I1 (checked; 124:6
    THE TWO FILES READ THE CLOSING VERSE OPPOSITE WAYS — a dispute of the two files for the exam).
  · THE GENERAL, THE PARTICULAR AND THE GENERAL (119:4 on 15:14): "furnish, you shall furnish" — everything; "from your flock, your floor and
    your press" — only what resembles the particular: fit for a blessing, or bearing young, a dispute on the feature — I6 (checked; the
    row's shape, not its name).
  · THE PARTICULARS THAT TEACH THE CLASS (126:1 on 15:21; 147:3-4 on 17:1): as the lame and the blind are blemishes visible and permanent,
    so every blemish visible and permanent — I8 (checked; the row's own words); and "YOU SHALL SANCTIFY" AGAINST "NO MAN SHALL SANCTIFY"
    (124:4 on 15:19) — for its value, never for the altar, the firstling singled out to teach the consecrated (Mishnah Arakhin 8:7) — I8's
    shape, named without a code; the release's object narrowed by "the loan of his hand" to standing debts (112:5-7) — I8's shape.
  · TWO VERSES UPHELD BY A CONDITION, NOT A THIRD VERSE (114:1 on 15:4; 118:1 on 15:11): "there shall be no needy" and "the needy shall
    never cease" — when you do the will of the Place the needy are among others, when you do not, among you — I13's question ("how are
    these two verses upheld") answered without its third verse; named without a code: the compile's state variable.
  · NAMED WITHOUT A CODE: the two releases bound (111:2); the onset not in the wilderness, the territory in and outside the Land (111:9-11,
    112:11); the manner the word said (112:1 — Mishnah Sheviit 10:8); the pledge-loan and HILLEL'S PROZBUL (113:2-3 — Sheviit 10:2-4);
    the words of the scribes (115:1); the receipt's referent forward (116:1 — 28:3); the ranks of the poor (116:4-8); the loan for the
    ashamed and the pledge dispute (116:13-14); the measure of need (116:15-18); the cry a hastener (117:5; 279:4); the four grades of the
    giver (117:8); the three measures (118:3); the three twin laws each given a case (118:4); the two exit tables (118:5 — Mishnah
    Kiddushin 1:2); the son not the heir (118:6); Egypt the model (120:1); by day they pierce (120:2); the slave who stays (121:1-4); the
    awl any tool or metal and R. Ishmael's three circumventions (122:1); the judges (122:3); "likewise" the gift not the awl (122:9); the
    double hire the night's service (123:1); the blessing beside the money loss (123:3); the caesarean (124:2); "year by year" two days
    (125:1); the year passed no bar (106:5); drinking is eating, the warning, the olive, the ground, the neck, the seeds (126:2-6); one dish
    and the heave-offering (71:7-8); Moses' one alms (355:9).
'''

RESEARCH = f'''

## {DATE} — DEUTERONOMY 15 READ AND FROZEN (THE DEUTERONOMY WALK sitting 13 — a reading sitting under THE COST RULES in TWO RUNS + THE TAIL: the measurements,
## the ink and the design to #206; the rows in two halves to #206 addenda 1-2 with the ledger — B1 and B2 in one context on the owner's reading; the compaction;
## the tail; EVERY STEP TIMED): THE ONE CALENDAR; THE TWO VERSES UPHELD BY A CONDITION; THE MISHNAH INSIDE THE SPINE FIVE TIMES WITH HILLEL'S PROZBUL; THE
## RECEIPT'S REFERENT POINTING FORWARD; THE LOAN THAT WEARS MOSES' NAME; THE EXPORT'S DEFECTIVE SPELLINGS; AND THE PRESENTATION-FORM LETTERS OF THE ARAMAIC
On the owner's "Go" after 12b's commit ({DATE}). THE READING: Deuteronomy 15:1-23 with Onkelos whole (the export's 23 rows the DB's 23 — the identity, asserted) and
THE SIFREI ON DEUTERONOMY ON THE CHAPTER A SEVENTH TIME — sixteen piskaot 111-126 whose heads climb in verse order (seven verses without a head), no tail folded in
(both ends checked on the consonants), {L_SPINE} rows read whole in both files ({N_REREAD} read before — the base thought at chapter 13, the wife by "for him" at Genesis 2 —
and reread whole, found by computation), ten rows outside the spine by the union of both files' citations read whole ({N_REREAD_OUT} reread whole — 41:3 from chapter 11,
71:6-8 from chapter 12, 106:5 from chapters 12 and 14 for its third read, 109:3 from chapter 14; 147:3-4, 279:4, 355:9 fresh), none excluded; the kin credited by
name from ten ledgers (Leviticus 25 in three, 22:17-27, 21:16-23, 27:26; Numbers 18:15-18; Deuteronomy 12:6-24, 14:28-29, 5:15); NEVER READ AHEAD — no Onkelos row of
Deuteronomy 16-34 or the Prophets in any ledger (asserted; Jeremiah 34 the run's case). FROZEN as ONE unit deu_15_release_firstborn (the 229th; no portion edge
inside it; standing 2259 = 2252 + 7 as predicted, hash unmoved); the ledger deu_15_reeh_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the spine
{L_SPINE}: MATERIAL {L_SM} / CONTEXT {L_SC}; the outside rows {L_OUT}: MATERIAL {L_XM} / CONTEXT {L_XC}; coverage computed, lint 0, no cut missed); seven claims DV15-01..07 verified 7/0,
seated as seven WITNESS_READ at 15:1, 4, 7, 12, 16, 19, 21; the ritual {N_PASS} PASS; the fold +{DJ} on the journal; the display layer +{OV_REF15} by reference and +44 by gloss
("release" for "remission", "the-loan-of" for "debt", "the-foreigner" for "the-strange", "needy" for "destitute", "shut", "free", "empty", "and-into-the-door",
"a-hireling", "blemish" for "stain", "saying" for "to-say"). THE FINDS: THE ONE CALENDAR — two paradigms deadlocked by two features and broken by the analogy
named in the Hebrew, "seven years, seven years" (111:3-7 — I2), R. Yose the Galilean's "draws near" the second proof (111:8, 117:4): the release-year the
world's, never the debtor's; "END" AT THE YEAR'S END with 31:10 and at Booths with 14:28 (111:1, 109:3 — I2); THE TWO RELEASES BOUND (111:2); THE ONSET AND THE
TERRITORY TWO PARAMETERS (111:9-11, 112:11, 41:3); THE MISHNAH INSIDE THE SPINE FIVE TIMES — the creditor's word "I release it" (112:1 — Sheviit 10:8), the
pledge-loan (113:2 — Sheviit 10:2), HILLEL'S PROZBUL WITH ITS TEXT, ordained because the people transgressed 15:9 (113:3 — Sheviit 10:3-4: the law's foreseen
failure repaired by a procedure the verse leaves open), the chamber of the silent (117:7 — Shekalim 5:6), the two exit tables (118:5 — Kiddushin 1:2); THE TWO
YEARS' POWERS fenced by two verses' "this" (112:3-4 — I1); THE OBJECT loans only and standing debts (112:5-7); THE TWO VERSES 15:4 AND 15:11 UPHELD BY A CONDITION,
NOT A THIRD VERSE (114:1, 118:1 — I13's question); THE WORDS OF THE SCRIBES (115:1); THE RECEIPT'S REFERENT SUPPLIED BY THE SHELF AND POINTING FORWARD — 28:3 at
116:1, a HYPOTHESIS until its sitting; THE RANKS OF THE POOR (116:4-8); THE MEASURE OF NEED — a horse, a slave, a wife (116:15-18); "BASE" WITHOUT A YOKE (117:1 —
E30) AND IDOLATRY (117:3 — I2); THE CRY NEITHER COMMANDED NOR FORBIDDEN (117:5; 279:4); THE FOUR GRADES OF THE GIVER (117:8); THE THREE TWIN LAWS EACH GIVEN A CASE
(118:4); THE GIFT — only what resembles the particular, a dispute (119:4 — I6); EGYPT THE MODEL (120:1); BY DAY THEY PIERCE (120:2); THE AWL any tool or metal and
R. ISHMAEL'S THREE CIRCUMVENTIONS (122:1); THE UPPER RIGHT EAR (122:5-6 — I2); "FOR EVER" THE MASTER'S LIFETIME (122:8 — I2); "LIKEWISE" THE GIFT NOT THE AWL
(122:9); THE DOUBLE HIRE THE NIGHT'S SERVICE AGAINST THE MEKHILTA (123:1); "SANCTIFY" FOR ITS VALUE, NEVER FOR THE ALTAR (124:4 — Arakhin 8:7); THE TWO FILES
OPPOSITE AT 124:6; "YEAR BY YEAR" TWO DAYS ACROSS THE YEAR'S EDGE (125:1); LAME AND BLIND THE PARTICULARS THAT TEACH THE CLASS (126:1 — I8; 147:3-4); THE BLOOD —
drinking is eating, the warning, the olive, the ground not the pit, the sectarians, the neck, the seeds (126:2-6); MOSES' ONE ALMS (355:9); THE REGISTER SINGULAR
FROM END TO END with 15:2 addressing no one, one imperative, eight infinitive absolutes, one narrative verb, the Name 12 bare and 3 with "to"; THE HOMOGRAPH —
15:2's מַשֵּׁה ("the loan") wears Moses' letters, asserted by lemma; THE PARSER'S four number verses and one ordinal; THE STORE = THE DB; ONKELOS — the master of the
claim, a son of the nations, the Memra thrice, a son of Israel or a daughter of Israel, set apart, the people of your house, a serving servant, two for one, as
the flesh of, no Shekhinah at the place. THE COST RULES: RUN A to #206 (517k by his reading), RUN B1 to addendum 1 (the clean point taken unconditionally), RUN B2
to addendum 2 in the same context on his 260k reading, the compaction, the tail on a small context with the chain in the background and the writers typed
during its run; EVERY STEP TIMED — the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)} wall time from {T_START}; the table in the map's AS BUILT. THE CAUTIONS: the
ink's three first-pass fails all the instrument's; the ledger writer's two fails its own (the design's count, the homograph); nine cut misses — eight the export's
defective spellings; the Aramaic's presentation-form letters. THE LESSONS (twelve, in the map): the defective spellings; a count in the prose is not the ink; a
name's letters are not the name; the presentation-form letters; the clean point unconditional, the compaction his; the receipt's forward pointer; the Mishnah
inside the spine; two verses upheld by a condition; the two files and the two spines disagree; the three circumventions; the kin by computation; every step
timed. OWED TO 13b: the release as an effect with its parameters and the prozbul from the answer sheet, the needy's precedence, the hand opened with the pledge
dispute and the measure of need, the Hebrew slave's three cases and the gift, the awl's rite, the double hire, the firstling's year of two days, the blemish's
class, the blood by call, the effects, the kin by call, never-read-ahead's cells, the register's rows, the series DG, the docket.
'''

STEPS = f'''DEUTERONOMY — SITTING 13 — CHAPTER 15, Deuteronomy 15:1-23 ({DATE}, on Brian's "Go" after chapter 14's compile; World/step9/DEUTERONOMY_WALK.md "Sitting 13" and
"Sitting 13 — AS BUILT"; the reading took two runs to two clean points and a tail, as the rule now says). Chapter 15 is the seventh-year release, the poor, the
Hebrew slave and the firstling. Every seventh year, every lender lets go of what he lent to his brother — but not to the foreigner. There will be no poor among
you, says one verse; the poor will never cease, says another eight verses later. Do not harden your heart or shut your hand: open it, lend him enough for his
need, and do not let the thought "the seventh year is near" make you refuse — if he cries to the LORD it is a sin in you; give, and the LORD will bless you. A
Hebrew man or woman sold to you serves six years and goes free in the seventh, and you do not send him away empty — load him from your flock, your floor and
your press, because you were a slave in Egypt. If he wants to stay, you take an awl and put it through his ear into the door and he serves for good; and it
should not seem hard to you, because he served double a hired man's worth. Every firstborn male of your herd and flock is holy: no work, no shearing; eat it
before the LORD every year at the place He chooses — unless it has a blemish, lame or blind, in which case you eat it at home like any deer, pouring the blood
out like water. The tradition does most of its work on the calendar and the poor. It settles that the seventh year is one year for the whole world, not seven
years counted from each loan, by an argument the text itself names as an analogy; it takes the two verses about the poor and makes them a condition — when you
do God's will the poor are among the other nations, when you do not they are among you; it ranks the poor (your own brother first, your own town first, the
beggar who goes door to door owed nothing from the fund); it reads "enough for his need" as even a horse and a servant if that is what he had; and it records
Hillel's workaround, the prozbul, by which a lender hands his debts to the court so the seventh year does not cancel them — written right into the commentary
because people had stopped lending. On the slave, it reads the three versions of the law (Exodus, Leviticus, here) as three cases, and decides that "do
likewise to your maidservant" reaches the parting gift but not the awl. On the firstling it settles that "year by year" means the animal may be eaten across the
year's edge, on two days. Two things surprised the machine: the commentary answers "as He spoke to you" with a verse from chapter 28 that has not been spoken
yet, so the machine files it as a guess until we get there; and the word for "the loan" in verse 2 has exactly the letters of Moses' name, so "Moses is never
named in this chapter" had to be checked by the dictionary entry and not by the letters. Every row of the commentary on the chapter was read whole in both
languages — ninety-nine rows in sixteen sections, plus ten rows from elsewhere. The chapter is frozen as one unit, the 229th, the world's standing facts up by
seven as predicted, its hash unmoved, every gate green. The two-run rule held: the first run stopped after the measurements and the design, the second after half
the rows; you read the counter at 260k and said go on, so the rest of the rows and the ledger ran in the same window; you compacted, and the tail ran on a small
context — the display fixes, the claims, the seat, the gates in the background while the records were typed. Every step was timed: the machine's own work came
to {mmss(T_MACH)} in a sitting of {mmss(T_TOTAL)}; the rest was the reading and the typing. Next: the commit on your word; then the compile of chapter 15 in two
runs — the release as an effect on the debts with the prozbul a parameter from the answer sheet, the poor's ranking a parameter, the slave's cases, the awl's rite,
the firstling's two-day year on the clock — or the ten-commandments schema first, on your word.


'''

BRIEF = f'''- **CHAPTER 15 READ AND FROZEN — THE SEVENTH-YEAR RELEASE ON ONE CALENDAR FOR THE WHOLE WORLD (THE TEXT'S OWN ANALOGY); "THERE SHALL BE NO POOR" AND "THE POOR WILL NEVER CEASE" MADE A CONDITION; HILLEL'S PROZBUL WRITTEN INTO THE COMMENTARY; A PROMISE ANSWERED BY A VERSE NOT YET SPOKEN; THE LOAN THAT WEARS MOSES' NAME; THE HEBREW SLAVE'S THREE CASES, THE AWL, THE FIRSTLING'S TWO-DAY YEAR; AND TWO RUNS + THE TAIL AS RULED** ({DATE}; sitting 13; the ledger deu_15_reeh_{LDATE}.md — {L_ALL} sources, every row whole; the 229th unit; every gate green; the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)}).
'''
BRIEF_ENTRY = f'''### {DATE} — CHAPTER 15 READ: ONE CALENDAR FOR THE RELEASE, THE POOR AS A CONDITION, HILLEL'S WORKAROUND IN THE COMMENTARY, AND A LOAN THAT SPELLS "MOSES"

Chapter 15 cancels debts every seventh year, tells you to open your hand to
the poor, frees the Hebrew slave in the seventh year with a parting gift, and
gives the firstborn of the herd to the LORD. The tradition's biggest move is
on the calendar: the seventh year is one year for everyone, not a private
count from each loan — and the commentary settles it by an argument the text
names as an analogy, "seven years, seven years". Its second move is on a
contradiction the chapter carries openly: "there shall be no poor among you"
and, eight verses later, "the poor will never cease" — read as a condition,
not a contradiction. It ranks the poor, sets the measure of need by what the
man once had, and writes Hillel's prozbul into the commentary itself: a way
to hand debts to the court so the release does not cancel them, invented
because people had stopped lending — the law's own foreseen failure and its
repair, both on the page. Two things the machine could not have known: the
commentary answers "as He spoke to you" with a verse from chapter 28 that
has not been read yet (filed as a guess until we get there), and the word for
"the loan" in verse 2 has the letters of Moses' name, so "Moses is never
named" had to be checked against the dictionary entry rather than the
letters. Every row was read whole in both languages. The chapter is frozen
as one unit, every gate green. The two-run rule you set after chapter 14
held: a clean point after the measurements and another after half the rows;
you read the counter and let the second half run in the same window; then
the compaction and a short tail with the gates in the background. Every step
was timed: the machine's own work came to {mmss(T_MACH)} in a sitting of
{mmss(T_TOTAL)}.

'''

RESUME_NOTE = f'''# ⚠ THE DEUTERONOMY WALK sitting 13 ({DATE}; step9/DEUTERONOMY_WALK.md "Sitting 13" + "Sitting 13 — AS BUILT"): CHAPTER 15 READ AND FROZEN as ONE unit
# (deu_15_release_firstborn, the 229th; standing 2259, hash unmoved) — THE ONE CALENDAR by the analogy named in the Hebrew (111:3-8), THE TWO VERSES 15:4 and 15:11
# UPHELD BY A CONDITION (114:1, 118:1), THE MISHNAH INSIDE THE SPINE FIVE TIMES with HILLEL'S PROZBUL (113:3), THE RECEIPT'S REFERENT POINTING FORWARD to 28:3 (116:1 —
# a HYPOTHESIS), the ranks of the poor (116:4-8), the three twin laws each a case (118:4), the awl's rite (122), the double hire against the Mekhilta (123:1),
# "sanctify" for its value (124:4), "year by year" two days (125:1), the blemish's class (126:1), THE LOAN THAT WEARS MOSES' NAME (15:2, by lemma); the ledger
# deu_15_reeh_{LDATE}.md ({L_ALL} sources, every row whole; the heads in verse order, no tail folded in); seven claims seated; the fold +{DJ} on the journal ({J_ROWS} rows);
# every gate green; the display layer +{OV_REF15} / +44. TWO RUNS + THE TAIL AS RULED (B1 and B2 in one context on his 260k reading), EVERY STEP TIMED (the machine's
# share {mmss(T_MACH)} of {mmss(T_TOTAL)}). NEXT on the owner's word: the commit (<scratch>/commit_msg_ch15.txt — chapter 15 alone, uncommitted since 049f55c); then 13b —
# the compile of chapter 15 (the release an effect with the prozbul a parameter, the poor's ranks, the slave's cases, the awl, the firstling's two-day year; DG the next series).
'''

STATE = f'''
#206 — ADDENDUM 3 ({DATE}, at the close of THE DEUTERONOMY WALK sitting 13 — CHAPTER 15's READING: THE TAIL after the compaction at #206 addendum 2, on the owner's "Reread" and "Go" — A CLEAN COMPACTION POINT): THE TAIL AS RUN on a small context: the rereads (the recovery page, the map's "Sitting 13 … THE DESIGN", MEMORY.md, the state doc's #206 with its NOTE, addenda 1-2 and the addendum-2 NOTE; the forms' tail scripts read whole — ch14_patch_overrides.py and its derive, write_ch14_manifest.py, seat_ch14.py, the three shells, copy_ch14_forms.py, write_ch14_records.py in pages; the ledger's rows in brief and its ink and crowns paragraphs); THE INK'S BODY D (the display patch predicted from the G print — {OV_REF15} by reference, 44 by gloss, the counts PRINTED by the third pass and typed into the patch script from the print; the third pass green, {N_INK} asserts); ch15_patch_overrides.py derived from the forms' ch14_patch_overrides.py by twelve asserted substitutions with its portable header stripped (derive_ch15_patch.py), the yaml +{OV_REF15} by reference and +44 by gloss ({OV_REF} / {OV_GL}); the ink rerun PATCHED — the fourth pass green (the counting asserts patch-aware from the start); THE MANIFEST'S CHECK WORDS PROBED IN THE STORE FIRST (ch15_manifest_probe.py — "a release" 15:1, "needy" 15:4, "you shall open" 15:8, "the Hebrew" 15:12, "the awl" 15:17, "the firstling" 15:19, "a blemish" 15:21: every piece over the floor); write_ch15_manifest.py (seven claims DV15-01..07 at 15:1, 4, 7, 12, 16, 19, 21 — the spine distributed by piska from the CITE INDEX itself, 116 and 118 split at their turning rows, the ten outside rows with the claims whose verses they cite; every cite index name used); seat_ch15.py; ch15_chain.sh, ch15_fold.sh and ch15_gates.sh derived from sitting 12's forms with the form's name protected (derive_ch15_shells.py — its own count fell once: the unit named once in the chain); THE FAST STEPS IN THE FOREGROUND — the manifest, verify_claims (7/0 — called first with the unit's name where it takes the manifest's path, retyped) and the labels census ({LN}) read before the freeze; THE CHAIN LAUNCHED IN THE BACKGROUND (ch15_gates.sh — the seat, verify_text {VT_STEPS} steps / {VT_SCEN} scenarios, the ritual {N_PASS} PASS, the fold 228 → 229 / 2252 → 2259 with the hash unmoved, build_world, the journal gate {J_ROWS} rows (+{DJ} since 12b's chain), the register gate --strict DECLARED {R_DECL} / DEBT {R_DEBT} / FAILS {R_FAIL}, large_letter {LL[-3:]}, the home gate) — {CHAIN_NOTE}; the records writer and the copier typed during the chain's run, the notification the wake; THE RECORDS from the sheet in one call (write_ch15_records.py — the map's "Sitting 13 — CHAPTER 15 — AS BUILT" with twelve lessons AND THE TIMING TABLE (computed from ch15_timing.tsv: the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)} from {T_START}; the chain's inner steps {CS_TXT}), COMPILE_DEBT's sitting-13 box (a)-(o) owed to 13b, MIDDOT's chapter-15 block with the codes censused from the ledger's rows ({CODE_TXT}), MISHNAH_TOPICS (thirteen heads routed to 13b), RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the scoreboard bullet and an entry), World/RESUME.md, this addendum, the addenda §61, the recovery page (section 2 under its cap; the sitting shapes' newest instances), the memory (the walk note and the index line under 17,000), the stamp row, THE COMMIT MESSAGE <scratch>/commit_msg_ch15.txt — chapter 15's alone); the forms copied (copy_ch15_forms.py). THE TREE: + logic/units/deu_15_release_firstborn.yaml frozen (operators, step E, the anchor scenarios), logic/py_units/deu_15_release_firstborn.py and ALL_UNITS.py (the ritual), logic/oral_audit/manifests/deu_15_release_firstborn_claims.json, logic/oral_triage/deu_15_reeh_{LDATE}.md, logic/glosses/word_gloss_overrides.yaml, logic/corpus/CORPUS_TRUTH.py (229 / 2259), corpus_world.sqlite, World/journal/data/world.sqlite (the fold layer, gitignored), the records, the forms. NOT COMMITTED (since 049f55c): SITTING 13 — the message at <scratch>/commit_msg_ch15.txt for the owner's word ("Commit" = no push; "commit push" = both). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. THE MEASURE OF THE RUNS: RUN A 517k by his /context reading (under the 600k cap; the estimate 130k short), RUN B1's clean point at 260k by his reading — he ran B2 in the same context (the reading's end near 450k by the run's own estimate), the tail on a small context: THE TWO-RUNS-AND-A-TAIL SHAPE FITS A CHAPTER OF THIS SIZE WITH ROOM. NEXT ON THE RULING: the commit on his word; then CHAPTER 15's COMPILE (13b) in two runs + the tail under the cost rules (RUN A the rereads, the measurements — Leviticus 25's cells, Exodus 21's slave cell through its spine, the firstling's cells, chapter 12's blood and place cells, the running world's sabbatical count, the register's finder at 15:2 and 15:6, chapter 14's Aramaic counts re-measured through NFKC — and the design: the release an EFFECT on the debts with its onset and territory PARAMETERS and the prozbul a PARAMETER from the answer sheet, the needy's ranks a PRECEDENCE PARAMETER, the hand opened a status with the pledge dispute two arms, the Hebrew slave's three cases with the exits' two tables and the gift's feature a dispute, the awl's rite by day with the judges and the ear, the double hire, the firstling's two-day year a CLOCK DATUM and "sanctify" for its value, the blemish's class with 17:1 by CALL when it comes, the blood by CALL to chapter 12's cells, the checkpoint series DG — and the docket by the union rule, its own run past ~700 rows; RUN B the types, the runner, the tape, the chain LAUNCHED; the tail the records) — or the Decalogue-schema sitting first; on the table: the chain's positions step at four workers as the standing form, the SUPPLIED forms, the calf's day marker, the registry's homographs (now with 15:2's loan and Moses), the receipt's third and fourth shapes (the forward pointer 15:6 → 28:3 a new shape), THE INSTALL HYPOTHESIS, the eras table's merge, the fast checker's cells' dry-run. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 13 — CHAPTER 15 — AS BUILT" (the newest section), MEMORY.md.
'''

ADDENDA = f'''
## §61 — THE DEUTERONOMY WALK sitting 13 ({DATE}): CHAPTER 15 READ AND FROZEN — the state doc's #206, its NOTE, its addenda 1-3 and the addendum-2 NOTE; the map's "Sitting 13 — CHAPTER 15 … THE DESIGN" and "Sitting 13 — CHAPTER 15 — AS BUILT"; the owner: "Go" (RUN A), "Get ready to compact" and "/context" (517k) at #206, "Reread" and "Go" (RUN B1), "/context" (260k) and "Go" (RUN B2 in the same context), "Get ready to compact" at addendum 2, "Reread" and "Go" (the tail)
THE READING: Onkelos Deuteronomy 15 whole (23 = 23, the identity); THE SIFREI ON THE CHAPTER A SEVENTH TIME — sixteen piskaot 111-126 with the heads IN VERSE
ORDER and no tail folded in, {L_SPINE} rows read whole in both files ({N_REREAD} read before and reread whole, found by computation); ten rows outside the spine by the union
of both files' citations ({N_REREAD_OUT} reread whole; 147:3-4, 279:4, 355:9 fresh), none excluded; the kin credited by name from ten ledgers (Leviticus 25 in three at the
head); the unit deu_15_release_firstborn the 229th (standing 2259, hash unmoved); the ledger {L_ALL} sources (Onkelos MATERIAL {L_OM} / CONTEXT {L_OC}; the spine MATERIAL {L_SM} /
CONTEXT {L_SC}; the outside rows MATERIAL {L_XM} / CONTEXT {L_XC}); seven claims 7/0 seated at 15:1, 4, 7, 12, 16, 19, 21; the display layer +{OV_REF15} by reference, +44 by gloss;
every gate green in one chain (ch15_gates.sh, in the background; the manifest, the verifier and the labels census in the foreground before it). THE RUNS: RUN A —
the measurements (the kin by computation beside the law kin named, the twin laws diffed verse by verse), the ink (3 fell on the first typed pass — every one the
instrument's shape; 0 on the second), the design, THE CLEAN POINT #206 (517k by his reading, under the cap); RUN B1 — the first half of the rows (63, piskaot
111-118; Onkelos 15:1-11; four outside rows), the import check (8 cut misses, all the export's defective spellings, retyped), THE CLEAN POINT ADDENDUM 1 TAKEN
UNCONDITIONALLY; RUN B2 in the same context on his 260k reading — the second half (36, piskaot 119-126; Onkelos 15:12-23; six outside rows), the import check over
all eight files (1 miss, a vav from the word before), the ledger (the writer fell twice on its own asserts — the Name's bare count and the homograph of Moses'
name), lint 0, THE CLEAN POINT ADDENDUM 2; the compaction; THE TAIL — the ink's body D (the patch predicted, the counts printed then typed), the patch, the fourth
pass PATCHED, the manifest with its checks probed first, the seat, the shells with the form's name protected, the fast steps in the foreground, the chain launched
with the writers typed during its run, the records, the forms, the message. EVERY STEP TIMED: the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)} from {T_START} — the table
in the map's AS BUILT. THE FINDS: THE ONE CALENDAR by the analogy named in the Hebrew (I2) with R. Yose the Galilean's "draws near"; "END" AT THE YEAR'S END and at
Booths (I2); THE TWO RELEASES BOUND; THE ONSET AND THE TERRITORY TWO PARAMETERS; THE MISHNAH INSIDE THE SPINE FIVE TIMES — the manner the word said, the pledge-loan,
HILLEL'S PROZBUL WITH ITS TEXT, the chamber of the silent, the two exit tables; THE TWO YEARS' POWERS fenced by two "this" (I1); THE OBJECT loans only; THE TWO
VERSES UPHELD BY A CONDITION, NOT A THIRD VERSE (I13's question); THE WORDS OF THE SCRIBES; THE RECEIPT'S REFERENT FORWARD — 28:3 a HYPOTHESIS; THE RANKS OF THE
POOR; THE MEASURE OF NEED; "BASE" WITHOUT A YOKE (E30) AND IDOLATRY (I2); THE CRY NEITHER COMMANDED NOR FORBIDDEN; THE FOUR GRADES OF THE GIVER; THE THREE TWIN
LAWS EACH A CASE; THE GIFT'S FEATURE A DISPUTE (I6); EGYPT THE MODEL; BY DAY THEY PIERCE; THE AWL ANY TOOL OR METAL AND THE THREE CIRCUMVENTIONS; THE UPPER RIGHT EAR
(I2); "FOR EVER" THE MASTER'S LIFETIME (I2); "LIKEWISE" THE GIFT NOT THE AWL; THE DOUBLE HIRE AGAINST THE MEKHILTA; "SANCTIFY" FOR ITS VALUE; THE TWO FILES OPPOSITE;
"YEAR BY YEAR" TWO DAYS; LAME AND BLIND THE CLASS (I8); THE BLOOD'S SIX ROWS; MOSES' ONE ALMS; the register singular end to end; the homograph of Moses' name; the
parser's four number verses and one ordinal; Onkelos's a son of Israel, the Memra thrice, no Shekhinah at the place. THE LESSONS (twelve, in the map): the
defective spellings; a count in the prose is not the ink; a name's letters are not the name; the presentation-form letters; the clean point unconditional, the
compaction his; the receipt's forward pointer; the Mishnah inside the spine; two verses upheld by a condition; the two files and the two spines disagree; the
three circumventions; the kin by computation; every step timed. OWED TO 13b (COMPILE_DEBT's box (a)-(o)): the release, the needy and the blessing, the hand
opened, the Hebrew slave, the awl, the double hire, the firstling, the blemish and the blood, the effects, the kin by call, never-read-ahead's cells, the
register's rows, the as-measured note, the series DG, the docket. The records on the sheet; the forms in World/step9/forms_deuteronomy_walk/ (copy_ch15_forms.py).
'''

MEMPAR = f'''
SITTING 13 DONE {DATE} ("Go" after 12b's commit; "Get ready to compact" and "/context" 517k at #206; "Reread"/"Go" for B1; "/context" 260k and "Go" for B2 in the same
context; "Get ready to compact" at #206 add. 2; "Reread" and "Go" after the compaction; the map's "Sitting 13" and "Sitting 13 — AS BUILT"): CHAPTER 15 READ AND
FROZEN as ONE unit deu_15_release_firstborn (the 229th; standing 2259 = 2252 + 7 as predicted, hash unmoved; no portion edge) in TWO RUNS + THE TAIL as ruled —
Onkelos 23 rows (the identity), THE SIFREI ON THE CHAPTER A SEVENTH TIME (sixteen piskaot 111-126, THE HEADS IN VERSE ORDER, no tail folded in; {L_SPINE} rows in both
files; {N_REREAD} reread whole, found by computation), ten outside rows ({N_REREAD_OUT} reread whole), the kin credited by name from ten ledgers; the ledger deu_15_reeh_{LDATE}.md
({L_ALL} sources; the writer fell twice on its own asserts); seven claims 7/0 seated at 15:1, 4, 7, 12, 16, 19, 21; every gate green; the display layer +{OV_REF15} / +44. THE
FINDS: THE ONE CALENDAR — seven years for the whole world, never for each debtor, by the analogy the row names in the Hebrew (111:3-7 — I2; 111:8's "draws near");
"END" AT THE YEAR'S END (111:1 — I2 with 31:10); THE MISHNAH INSIDE THE SPINE FIVE TIMES — Sheviit 10:8 (112:1), 10:2 (113:2), 10:3-4 HILLEL'S PROZBUL with its text
(113:3), Shekalim 5:6 (117:7), Kiddushin 1:2 (118:5): the answer sheet cited by the compile rules; THE TWO VERSES 15:4 AND 15:11 UPHELD BY A CONDITION, NOT A THIRD
VERSE (114:1, 118:1 — I13's question); THE RECEIPT'S REFERENT SUPPLIED BY THE SHELF AND POINTING FORWARD — 28:3 at 116:1 (a HYPOTHESIS until its sitting; the
receipt's third shape); THE WORDS OF THE SCRIBES (115:1); THE RANKS OF THE POOR a precedence parameter (116:4-8); THE MEASURE OF NEED (116:15-18); "BASE" WITHOUT A
YOKE (117:1 — E30) and idolatry (117:3 — I2); THE CRY NEITHER COMMANDED NOR FORBIDDEN (117:5 = 279:4); THE FOUR GRADES OF THE GIVER (117:8); THE THREE TWIN LAWS EACH
GIVEN A CASE (118:4); THE GIFT'S FEATURE A DISPUTE (119:4 — I6); BY DAY THEY PIERCE (120:2); R. ISHMAEL'S THREE CIRCUMVENTIONS (122:1); "FOR EVER" THE MASTER'S
LIFETIME (122:8 — I2); "LIKEWISE" THE GIFT NOT THE AWL (122:9); THE DOUBLE HIRE AGAINST THE MEKHILTA (123:1); "SANCTIFY" FOR ITS VALUE (124:4 — Arakhin 8:7); THE TWO
FILES OPPOSITE (124:6); "YEAR BY YEAR" TWO DAYS (125:1); LAME AND BLIND THE CLASS (126:1 — I8); THE REGISTER SINGULAR END TO END, 15:2 addressing no one; THE HOMOGRAPH
— 15:2's "the loan" wears Moses' letters (by lemma 4874 vs 4872). ⚠ LESSONS (twelve, in the map): THE EXPORT SPELLS DEFECTIVELY UNDER ITS VOWELS (eight cut misses
of nine — the consonants from the print's letters); A COUNT IN THE DESIGN'S PROSE IS NOT THE INK (13 → 12 from the print); A NAME'S LETTERS ARE NOT THE NAME (assert
by lemma); THE ARAMAIC'S PRESENTATION-FORM LETTERS (NFKC; chapter 14's counts owe a re-measure); THE CLEAN POINT UNCONDITIONAL, THE COMPACTION HIS (B1 and B2 in one
context at 260k); the receipt's forward pointer; the Mishnah inside the spine; two verses upheld by a condition; the two files and the two spines disagree; the
three circumventions; the kin by computation (Jeremiah 34:14 the closest kin of 15:12); EVERY STEP TIMED — the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)}. OWED TO
13b: the release an effect with the prozbul a parameter from the answer sheet, the poor's ranks, the hand opened with the pledge dispute, the slave's three cases
and the gift, the awl's rite, the double hire, the firstling's two-day year a clock datum, the blemish's class, the blood by call; DG the next series. UNCOMMITTED
since 049f55c (NOT PUSHED): 15 (the message at <scratch>/commit_msg_ch15.txt). NEXT on the ruling: the commit; then 13b, two runs + the tail.
'''
MEMLINE_OLD_START = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — '
MEMLINE_NEW = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — map World/step9/DEUTERONOMY_WALK.md; ch 1-14 COMPILED AND PUSHED through 049f55c; 15 READ AND FROZEN (sitting 13 — two runs + the tail; 132/132; the 229th unit); UNCOMMITTED; NEXT: the commit, then 13b\n'
DESC_OLD = 'description: "COMMITTED AND PUSHED THROUGH 049f55c (2026-09-22 — 13b, 14 and 12b in one message) — SITTING 12b DONE 2026-09-22 ('
DESC_NEW = f'description: "COMMITTED AND PUSHED THROUGH 049f55c (2026-09-22 — 13b, 14 and 12b in one message) — SITTING 13 DONE {DATE} (chapter 15 READ AND FROZEN as one unit, the 229th — the one calendar, the two verses upheld by a condition, the prozbul inside the spine, the receipt pointing forward, the loan that wears Moses\' name; two runs + the tail as ruled; UNCOMMITTED; NEXT on his word: the commit, then 13b) — SITTING 12b DONE 2026-09-22 ('
REC2_OLD_START = '## 2. WHERE IT STANDS'
REC2_NEW = f'''## 2. WHERE IT STANDS ({DATE}, after sitting 13; the state doc #206 addendum 3 the newest)
- NUMBERS CLOSED. DEUTERONOMY 1:1-14:29 ON THE TAPE (PUSHED through 049f55c); 15 READ AND FROZEN (UNCOMMITTED).
- {C_UNITS} frozen units, standing 2259, hash 8b8fff1fa28953af. 69 runners, 74 daemons; 1161 kinds / 1061 effects.
- THE TAPE at RUN (1332, 96, 88, 0, 12, 1641, 45, 319, pairs, 127), markers 172, closes 127; 10/10 (DF1-DF9); the sweep 68/68; every gate GREEN.
- SITTING 13 (ch 15; TWO RUNS + THE TAIL as ruled; TIMED): the one calendar; the two verses upheld by a condition; the prozbul
  inside the spine; the receipt pointing forward; {L_ALL} sources whole; 7 claims seated; +{OV_REF15} / +44.
- UNCOMMITTED since 049f55c: 15 (<scratch>/commit_msg_ch15.txt). NEXT ON HIS WORD: the commit; then 13b.

'''
A_REC5 = 'the newest instances: the map\'s "Sitting 12b" and "Sitting 12")'
A_REC5_NEW = 'the newest instances: the map\'s "Sitting 13" and "Sitting 12b")'
A_REC6 = '- Deuteronomy\'s sittings: the map; the addenda §31-59 (§39 the whole-row rule). The cost cuts: §35, §45, §47, §53.'
A_REC6_NEW = '- Deuteronomy\'s sittings: the map; the addenda §31-61 (§39 the whole-row rule). The cost cuts: §35, §45, §47, §53.'
TOP = {
 '**5. Mishnah, Seventh Year**': f' — 10:1-9 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 13, chapter 15\'s reading: the release of debts 15:1-3 at 111-113 — the manner the word said (10:8 at 112:1), the pledge-loan (10:2 at 113:2), HILLEL\'S PROZBUL with its text (10:3-4 at 113:3), the standing debt and the shop\'s credit (10:1 at 112:5-7); Gittin 36a-37b, Arakhin 32b-33a; the docket at 13b)',
 '**29. Mishnah, Divorce Documents**': f' — Gittin 36a-37b ROUTED {DATE} (THE DEUTERONOMY WALK sitting 13, chapter 15\'s reading: the prozbul, and the release by decree when the jubilee is not 15:1-3 at 113:3, 111:9-11; the docket at 13b)',
 '**45. Mishnah, Valuations**': f' — 8:7 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 13, chapter 15\'s reading: "you shall sanctify" against Leviticus 27:26\'s "no man shall sanctify" — for its value, never for the altar 15:19 at 124:4; Arakhin 32b-33a the jubilee\'s link; the docket at 13b)',
 '**35. Mishnah, Lashes**': f' — Makkot 3b ROUTED {DATE} (THE DEUTERONOMY WALK sitting 13, chapter 15\'s reading: the witnesses in the release 15:1-2; the warning of witnesses from "only" 15:23 at 126:3; the docket at 13b)',
 '**19. Mishnah, New Year**': f' — Rosh Hashanah 8b-9a ROUTED {DATE} (THE DEUTERONOMY WALK sitting 13, chapter 15\'s reading: "the year of release" and the year\'s start — the one calendar 15:1, 15:9 at 111:3-8, 117:4; the docket at 13b)',
 '**30. Mishnah, Betrothal**': f' — 1:2-3 with Kiddushin 14b-22b ROUTED {DATE} (THE DEUTERONOMY WALK sitting 13, chapter 15\'s reading: the Hebrew slave and the Hebrew woman — the three cases and the exits\' two tables 15:12 at 118:4-5 (1:2 in the row\'s own Hebrew), the gift and its feature 15:14 at 119:4 (17a), the double hire 15:18 at 123:1 (15a), the awl and the ear 15:16-17 at 121-122 (22a-b); the docket at 13b)',
 '**32. Mishnah, Middle Gate**': f' — Bava Metzia 31b, 71a ROUTED {DATE} (THE DEUTERONOMY WALK sitting 13, chapter 15\'s reading: the doubled words "lend, you shall lend", "give, you shall give", "furnish, you shall furnish" 15:8, 10, 14 at 116:12-13, 117:6, 119:2 (31b); the poor of your city first 15:7 at 116:4-8 (71a); the docket at 13b)',
 '**2. Mishnah, Corner of the Field**': f' — 8:7-9 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 13, chapter 15\'s reading: "sufficient for his need" — not to enrich him, even a horse and a slave 15:8 at 116:15-17; Ketubot 67b; the docket at 13b)',
 '**25. Mishnah, Marriage Contracts**': f' — Ketubot 67b ROUTED {DATE} (THE DEUTERONOMY WALK sitting 13, chapter 15\'s reading: the poor man\'s former standard — Hillel\'s horse and the litra of meat 15:8 at 116:16-17; the docket at 13b)',
 '**44. Mishnah, Firstborn**': f' — 1:1-2, 2:6-9, 3:3-4, 4:1-2, 5:1-6, 6:1-12 with Bekhorot 25a-28b, 26b-27b, 33a-37b, 53b ROUTED {DATE} (THE DEUTERONOMY WALK sitting 13, chapter 15\'s reading: the firstling\'s year of two days 15:20 at 125:1 and 106:5, the caesarean 15:19 at 124:2 (2:9), the shearing and the work at 124:5-6, the blemish\'s class visible and permanent 15:21 at 126:1 and 147:3-4; the docket at 13b)',
 '**46. Mishnah, Substitution**': f' — 3:5 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 13, chapter 15\'s reading: the firstling\'s offspring 15:19 at 124:1-3; the docket at 13b)',
 '**15. Mishnah, Shekels**': f' — 5:6 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 13, chapter 15\'s reading: the chamber of the silent — the secret gift 15:10 at 117:7, the Mishnah in the row\'s own Hebrew; the docket at 13b)',
 '**43. Mishnah, Slaughter**': f' — 2:9 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 13, chapter 15\'s reading: the blood poured on the ground, not into a pit — in the house beside a hole, not in the market lest he imitate the sectarians 15:23 at 126:5; the docket at 13b)',
}

TRAIL = 'Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01MiJCE3AxFHu3jksQa2GG21\n'
CM = f'''CHAPTER 15 READ AND FROZEN (SITTING 13 — A READING SITTING UNDER THE COST RULES IN TWO RUNS + THE TAIL AS RULED: THE MEASUREMENTS, THE INK AND THE DESIGN TO ONE CLEAN POINT, THE ROWS IN TWO HALVES TO TWO MORE WITH THE LEDGER, THE COMPACTION, THE TAIL; EVERY ROW WHOLE; EVERY STEP TIMED) — THE SEVENTH-YEAR RELEASE ON ONE CALENDAR FOR THE WHOLE WORLD BY THE ANALOGY THE ROW NAMES IN THE HEBREW, "THERE SHALL BE NO NEEDY" AND "THE NEEDY SHALL NEVER CEASE" UPHELD BY A CONDITION AND NOT A THIRD VERSE, THE MISHNAH INSIDE THE SPINE FIVE TIMES WITH HILLEL'S PROZBUL AND ITS TEXT, THE RECEIPT'S REFERENT SUPPLIED BY THE SHELF AND POINTING FORWARD TO A VERSE NOT YET SPOKEN, THE RANKS OF THE POOR AND THE MEASURE OF NEED, THE THREE TWIN LAWS EACH GIVEN A CASE, THE AWL WITHOUT JUDGES OR DOORPOST AND R. ISHMAEL'S THREE CIRCUMVENTIONS, "SANCTIFY" FOR ITS VALUE AND NEVER FOR THE ALTAR, "YEAR BY YEAR" TWO DAYS ACROSS THE YEAR'S EDGE, LAME AND BLIND THE PARTICULARS THAT TEACH THE CLASS, THE LOAN THAT WEARS MOSES' NAME, THE EXPORT'S DEFECTIVE SPELLINGS AND THE ARAMAIC'S PRESENTATION-FORM LETTERS — UNCOMMITTED SINCE 049f55c.

On the owner's words "Go" (RUN A, after 12b's commit), "Get ready to compact" and "/context" (517k) at #206, "Reread" and "Go" (RUN B1), "/context" (260k) and "Go" (RUN B2 in the same context — his call), "Get ready to compact" at #206 addendum 2, "Reread" and "Go" (the tail, after the compaction), {DATE}; World/step9/DEUTERONOMY_WALK.md "Sitting 13 — CHAPTER 15 … THE DESIGN" and "Sitting 13 — CHAPTER 15 — AS BUILT"; the state doc's #206, its NOTE, its addenda 1-3 and the addendum-2 NOTE; the addenda §61. THE READING: Deuteronomy 15:1-23 with Onkelos whole (the export's 23 rows the DB's 23 — the identity, asserted) and THE SIFREI ON DEUTERONOMY ON THE CHAPTER A SEVENTH TIME — sixteen piskaot 111-126 whose heads climb IN VERSE ORDER (seven verses without a head), NO TAIL FOLDED IN (both ends checked on the consonants), {L_SPINE} rows READ WHOLE in both files ({N_REREAD} read before — the base thought at chapter 13, the wife by "for him" at Genesis 2 — and REREAD WHOLE, found by computation), ten rows outside the spine by the union of both files' citations read whole ({N_REREAD_OUT} reread whole — the release after the conquest from chapter 11, the permanent blemish and the one dish from chapter 12, the firstling's year from chapters 12 and 14 for its third read, "the end" from chapter 14; the blemishes at 17:1, the hireling's cry at 24:15 and Moses' righteousness at 33:21 fresh), none excluded, the kin credited by name with the counts computed from ten ledgers (Leviticus 25's sabbatical, poor brother and sold brother in three, 22:17-27, 21:16-23, 27:26; Numbers 18:15-18; Deuteronomy 12:6-24, 14:28-29, 5:15 — no Onkelos row of Exodus 21:2-11, 23:10-11, 22:24-26, 22:29, 13:2-16 or 34:19-20, of Genesis 4:4, and NONE OF DEUTERONOMY 16-34 OR THE PROPHETS in any ledger, asserted: never read ahead; Jeremiah 34 the run's case); frozen as ONE unit deu_15_release_firstborn (the 229th; no portion edge inside it — Re'eh holds it whole), standing 2259 = 2252 + 7 as predicted, hash 8b8fff1fa28953af unmoved; the ledger logic/oral_triage/deu_15_reeh_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the spine {L_SPINE}: MATERIAL {L_SM} / CONTEXT {L_SC}; the outside rows {L_OUT}: MATERIAL {L_XM} / CONTEXT {L_XC}; coverage computed, lint 0, no cut missed — the writer fell twice on its own asserts before it wrote: the design's "thirteen bare" against the print's 12, and "Moses never named" against 15:2's loan that wears his letters, retyped by lemma); seven claims DV15-01..07 verified 7/0 (the spine distributed by piska from the CITE INDEX itself, piskaot 116 and 118 split at their turning rows; the seven check words' pieces PROBED in the store before they were typed), the labels census green ({LN}), seated as seven WITNESS_READ operators at 15:1, 4, 7, 12, 16, 19, 21 with step E; the ritual {N_PASS} PASS; the display layer +{OV_REF15} by reference and +44 by gloss under the sitting's marker ("release" for "remission", "the-loan-of" for "debt", "the-foreigner" for "the-strange", "needy" for "destitute", "shut" for "draw-together", "free" for "exempt", "empty" for "emptily", "and-into-the-door", "a-hireling" for "man-at-wages", "blemish" for "stain", "saying" for "to-say", "his-brother", "your-heart"; the three "?" of Moses' "I" by reference). THE FINDS: THE ONE CALENDAR — two paradigms (the land's release, the Hebrew slave) deadlocked by two features (the jubilee, the territory) and broken by "SEVEN YEARS, SEVEN YEARS, FOR AN ANALOGY" named in the row's own Hebrew (111:3-7), R. Yose the Galilean's "draws near" the second proof (111:8, 117:4): the release-year the world's, never the debtor's; "END" AT THE YEAR'S END with 31:10 (111:1) and at Booths with 14:28 where the tithe's end falls at Passover (109:3); THE TWO RELEASES BOUND (111:2); THE ONSET AND THE TERRITORY TWO PARAMETERS — not in the wilderness, "to the LORD" both in the Land and outside it (111:9-11, 112:11, 41:3); THE MISHNAH INSIDE THE SPINE FIVE TIMES — the creditor's word "I release it" (112:1 — Sheviit 10:8), the pledge-loan not released (113:2 — Sheviit 10:2), HILLEL'S PROZBUL WITH ITS TEXT, "your hand" and not the court's, ordained when the people refrained from lending and transgressed 15:9 (113:3 — Sheviit 10:3-4: the law's foreseen failure repaired by a procedure the verse leaves open — a parameter from the answer sheet), the chamber of the silent (117:7 — Shekalim 5:6), the man's and the woman's exits two tables (118:5 — Kiddushin 1:2); THE TWO YEARS' POWERS fenced by two verses' "this" (112:3-4); THE OBJECT loans only and standing debts (112:5-7); THE TWO VERSES 15:4 AND 15:11 UPHELD BY A CONDITION, NOT A THIRD VERSE — when you do the will of the Place the needy are among others (114:1, 118:1); THE WORDS OF THE SCRIBES named (115:1); THE RECEIPT'S REFERENT SUPPLIED BY THE SHELF AND POINTING FORWARD — "and what did He speak to you? Blessed shall you be in the city", 28:3 at 116:1 (a labeled HYPOTHESIS until its sitting; 11:25's pointed back to Exodus 23:27); THE RANKS OF THE POOR — the hungrier, the father's brother, the city, the Land, the door-to-door beggar owed nothing from the fund (116:4-8); THE MEASURE OF NEED — not to enrich him, even a horse and a slave, Hillel's horse, the litra of meat, the wife by "for him" (116:15-18); the gift dressed as a loan and THE PLEDGE A DISPUTE (116:13-14); "BASE" SPLIT INTO "WITHOUT A YOKE" (117:1) and read as idolatry with 13:14 (117:3); THE CRY NEITHER COMMANDED NOR FORBIDDEN, THE SIN UNCONDITIONAL, THE CRY A HASTENER (117:5 — 279:4 at 24:15 word for word); THE FOUR GRADES OF THE GIVER (117:8); THE THREE NOUNS THREE MEASURES (118:3); THE THREE TWIN LAWS EACH GIVEN A CASE — the buyer, the self-seller, THE COURT'S SALE (118:4); THE GIFT — the three sendings, not the heirs, only what resembles the particular with the feature a dispute (119:1-4), Egypt the model (120:1), BY DAY THEY PIERCE (120:2); THE SLAVE WHO STAYS — two sayings, two times, the love mutual, illness bars (121); THE AWL — any tool or metal a dispute, and R. ISHMAEL'S THREE PLACES WHERE THE HALAKHA CIRCUMVENTS SCRIPTURE (122:1), the judges present (122:3), the upper right ear (122:5-6), "FOR EVER" THE MASTER'S LIFETIME — the son not the daughter, the pierced no heir (122:8), "LIKEWISE" THE GIFT NOT THE AWL (122:9); THE DOUBLE HIRE THE NIGHT'S SERVICE AGAINST THE MEKHILTA (123:1 — a dispute of two spines); the blessing beside every money loss (123:3); THE FIRSTLING — its year and the blemished, the caesarean out, all the consecrated (124:1-3), "YOU SHALL SANCTIFY" AGAINST "NO MAN SHALL SANCTIFY" UPHELD BY DIVIDING THE SPHERES (124:4 — Arakhin 8:7), "your" two ways (124:5), THE TWO FILES READING THE CLOSING VERSE OPPOSITE WAYS (124:6), "YEAR BY YEAR" TWO DAYS ACROSS THE YEAR'S EDGE (125:1), the year passed no bar (106:5); LAME AND BLIND THE PARTICULARS THAT TEACH THE CLASS — visible and permanent (126:1; 147:3-4 at 17:1), the permanent blemish lent to all the consecrated (71:6), one dish and the heave-offering apart (71:7-8); THE BLOOD — drinking is eating, "only" the witnesses' warning and the olive, the ground not the pit, the house not the market lest he imitate the sectarians, pouring from the neck, the seeds made susceptible (126:2-6); MOSES' ONE ALMS THE LAW OF ALMS (355:9); THE REGISTER SINGULAR FROM END TO END — 15:2 addressing no one, one imperative, eight infinitive absolutes, one narrative verb ("redeemed you"), the Name 12 bare and 3 with "to", Egypt the one other name, and THE HOMOGRAPH — 15:2's "the loan" wears Moses' letters (lemma 4874 against 4872); THE PARSER: four number verses ([7] "seven years", [1] "one of your gates", [6] "six years" twice) and one ordinal ([7] "the seventh"); THE STORE = THE DB (354 = 354, no written/read pair); ONKELOS: "the master of the claim" for the creditor, "a son of the nations" for the foreigner, "receive the Memra" thrice, "in wickedness" for base, "guilt" for sin, "A SON OF ISRAEL OR A DAUGHTER OF ISRAEL" for the Hebrew man and woman, "a son of freedom", "set apart" for furnish, "the people of your house", "a serving servant", "two for one", "as the flesh of the gazelle", no Shekhinah at the place. EVERY GATE GREEN IN ONE CHAIN (ch15_gates.sh, in the background; the manifest, verify_claims 7/0 and the labels census in the foreground before it; the summary read once): the seat, verify_text ({VT_STEPS} steps, {VT_SCEN} scenarios), the ritual {N_PASS} PASS, CORPUS TRUTH GREEN before and after the bake ({C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, hash unmoved), build_world ALL GREEN, the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer since 12b's chain, the tape unmoved), the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — no receipt, header or footer in chapter 15), large_letter_probes {LL[-3:]}, the home-path gate GREEN; the ink {N_INK} asserts in four passes ({INKF[1]} / {INKF[2]} / {INKF[3]} / {INKF[4]} failing — the first the instrument's shapes, none a fact; the third with the patch block; the fourth PATCHED). THE COST RULES ON A READING SITTING: TWO RUNS + THE TAIL as the #204 NOTE ruled — RUN A to #206 (517k by his reading, under the cap), RUN B1 to addendum 1 with THE CLEAN POINT TAKEN UNCONDITIONALLY after the first half of the rows, RUN B2 in the same context on his 260k reading (the reading's end near 450k by the run's own estimate), the compaction, the tail on a small context — the ink's body D with the counts printed then typed, the display patch (twelve asserted substitutions on the chapter-14 form), the manifest with its checks probed first, the seat, the three shells derived with the form's name protected, the fast steps in the foreground, the chain launched behind with the records writer and the copier typed during its run. EVERY STEP TIMED (the table in the map's AS BUILT, computed from ch15_timing.tsv): the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)} wall time from {T_START} to the records; the chain {mmss(CS_TOTAL)} ({CS_TXT}); the rest the reading, the typing and two compactions. THE LESSONS (twelve, in the map's AS BUILT): the export spells defectively under its vowels; a count in the design's prose is not the ink; a name's letters are not the name; the Aramaic's presentation-form letters; the clean point unconditional, the compaction his; the receipt's referent can point forward; the Mishnah inside the spine; two verses upheld by a condition; the two files and the two spines disagree; R. Ishmael's three circumventions; the kin by computation again; every step timed. Also in this commit: COMPILE_DEBT's sitting-13 box (a)-(o) owed to the compile 13b, MIDDOT's chapter-15 block (the codes censused from the ledger's rows — {CODE_TXT}), MISHNAH_TOPICS' row notes (Seventh Year 10:1-9; Divorce Documents 36a-37b; Valuations 8:7; Lashes 3b; New Year 8b-9a; Betrothal 1:2-3 with 14b-22b; Middle Gate 31b, 71a; Corner of the Field 8:7-9; Marriage Contracts 67b; Firstborn 1:1-2, 2:6-9, 3:3-4, 4:1-2, 5:1-6, 6:1-12 with its folios; Substitution 3:5; Shekels 5:6; Slaughter 2:9 — routed to 13b), RESEARCH_LOG's entry, THE_STEPS, THE_BRIEFING (the scoreboard and an entry), World/RESUME.md, the state doc's #206 with its NOTE, addenda 1-3 and the addendum-2 NOTE, the recovery page rewritten under its cap, the addenda §61, the stamp row, the memory, the forms in World/step9/forms_deuteronomy_walk/ (the two runs' and the tail's scripts and prints — the derivations, the dump, the measurement in three files, the split, the ink and its four parts, the eight row files and their two checks, the ledger writer, the design and the three clean-point writers, the display patch and its derivation, the probe, the manifest, the seat, the three shells and their derivation, the timer and its table, the records, the copy).

{TRAIL}'''

LINT = f'{ROOT}/logic/solo_tools/gloss_lint.py'
def lint(path):
    out = subprocess.run([sys.executable, LINT, path], capture_output=True, text=True).stdout
    m = re.search(r'gloss_lint: (\d+) flag', out); return int(m.group(1)) if m else -1
WALKP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; RECP = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
TOPICS = f'{ROOT}/logic/MISHNAH_TOPICS.md'
TOUCH = [f'{ROOT}/logic/findings/STAMP_LEDGER.md', f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', f'{ROOT}/World/RESUME.md', f'{ROOT}/THE_STEPS.md', f'{ROOT}/THE_BRIEFING.md', f'{ROOT}/World/step9/COMPILE_DEBT.md', f'{ROOT}/RESEARCH_LOG.md', f'{ROOT}/logic/MIDDOT.md', RECP, f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md', TOPICS]
# ---- THE ANCHORS, ASSERTED PRESENT ONCE BEFORE ANY WRITE ----
A_RESUME = '# ⚠ THE DEUTERONOMY WALK sitting 12b — CHAPTER 14 COMPILED AND ON THE TAPE (2026-09-22; step9/DEUTERONOMY_WALK.md "Sitting 12b"'
A_SCORE = '## SCOREBOARD (as of 2026-09-20, latest)\n'; A_SCORE_NEW = f'## SCOREBOARD (as of {DATE}, latest)\n'
A_BULLET = '- **CHAPTER 14 COMPILED — THE FOOD LAWS AND THE TITHES AS FIVE LAWS AT THE CHAPTER\'S OWN DAY OVER THE TWIN CHAPTER\'S CELLS BY CALL'
A_ENTRY = '### 2026-09-22 — CHAPTER 14 COMPILED: FIVE LAWS AT ONE DAY OVER A TWIN ALREADY IN THE MACHINE, AND THE DISPUTES AS PARAMETERS'
A_MIDDOT = '\n## Exodus block campaign — owner\'s word "Do 3")\n'
ANCH = [(f'{ROOT}/World/RESUME.md', A_RESUME), (f'{ROOT}/THE_STEPS.md', '\n## Step 6 — Publish\n'), (f'{ROOT}/THE_BRIEFING.md', A_SCORE), (f'{ROOT}/THE_BRIEFING.md', A_BULLET), (f'{ROOT}/THE_BRIEFING.md', A_ENTRY), (f'{ROOT}/logic/MIDDOT.md', A_MIDDOT), (RECP, REC2_OLD_START), (RECP, '\n## 3. THE STANDING LAWS'), (RECP, A_REC5), (RECP, A_REC6), (f'{MEM}/deuteronomy-walk.md', DESC_OLD), (f'{MEM}/MEMORY.md', MEMLINE_OLD_START)]
for p, a in ANCH: assert rd(p).count(a) == 1, (p, a[:40], rd(p).count(a))
tl = rd(TOPICS).split('\n'); assert all(sum(l.startswith(t) for l in tl) == 1 for t in TOP) and 'sitting 13, chapter 15' not in rd(TOPICS)
assert '## Sitting 13 — CHAPTER 15 — AS BUILT' not in rd(WALKP) and '## Sitting 13 — CHAPTER 15, Deuteronomy 15:1-23' in rd(WALKP) and '#206 — ADDENDUM 3' not in rd(TOUCH[1]) and '#206 — ADDENDUM 2' in rd(TOUCH[1]) and '#206 ADDENDUM 2 — NOTE' in rd(TOUCH[1]) and '## §61' not in rd(TOUCH[9]) and '## §60' in rd(TOUCH[9]) and 'SITTING 13 DONE' not in rd(f'{MEM}/deuteronomy-walk.md') and 'SITTING 13 — CHAPTER 15' not in rd(TOUCH[5]) and f'## {DATE} — DEUTERONOMY 15 READ' not in rd(TOUCH[6]) and 'CASE LAW ON CHAPTER 15' not in rd(TOUCH[7]) and 'DEUTERONOMY — SITTING 13 — CHAPTER 15' not in rd(TOUCH[3])
s = rd(RECP); i = s.index(REC2_OLD_START); j = s.index('\n## 3. THE STANDING LAWS'); REC_NEW = s[:i] + REC2_NEW + s[j:]
REC_NEW = REC_NEW.replace(A_REC5, A_REC5_NEW).replace(A_REC6, A_REC6_NEW)
assert len(REC_NEW.encode()) <= 10240, len(REC_NEW.encode())
m = rd(f'{MEM}/MEMORY.md'); i = m.index(MEMLINE_OLD_START); j = m.index('\n', i) + 1; MEM_NEW = m[:i] + MEMLINE_NEW + m[j:]
assert len(MEM_NEW.encode()) < 17000, len(MEM_NEW.encode())
CMP = f'{SP}/commit_msg_ch15.txt'; assert not os.path.exists(CMP) or CHECK, CMP
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
replace_once(TOUCH[4], A_SCORE, A_SCORE_NEW)
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
