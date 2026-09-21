import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 11 — CHAPTER 13 (2026-09-21; the owner: "Go" — a reading sitting under THE COST RULES A-B-C: ONE run to the clean point #202
# after the ledger, the owner's compaction, "Reread", "Go", THE TAIL on a small context): THE RECORDS at the close, from the sheet World/step9/RECORD_FORMS.md in
# ONE call — the map's "Sitting 11 — CHAPTER 13 — AS BUILT" WITH THE TIMING TABLE computed from the scratchpad's ch13_timing.tsv, COMPILE_DEBT's box (owed to
# the compile 11b, and chapter 14's split of piska 96), MIDDOT's block (the codes censused from the ledger's own rows), MISHNAH_TOPICS' row notes (ROUTED to
# 11b), RESEARCH_LOG's entry, THE_STEPS' paragraph, THE_BRIEFING's bullet and entry, RESUME's note, the state doc's #202 addendum 1, the recovery page (section
# 2 rewritten, under 10 KB), the recovery addenda's §57, the stamp row, the memory file and the index line (under 17,000 bytes), and THE COMMIT MESSAGE.
# Every number parsed from a print named beside it (--check prints them and writes nothing); every insert on a unique anchor asserted present once; the lints
# before and after. Sitting 10's form (write_ch12_records.py).
import os, re, subprocess, sys, yaml, json, datetime, glob
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/' + os.path.abspath(ROOT).replace('/', '-') + '/memory')
DATE = '2026-09-21'; LDATE = '2026-09-21'
UID = 'deu_13_seducers'
CHECK = '--check' in sys.argv
CHAIN_NOTE = 'THE GATES CHAIN RAN ONCE, ALL GREEN ON ITS FIRST PASS (11:49:38 to 11:57:33 — 7 min 55 s: the seat, verify_text, the ritual, the fold, build_world, the journal gate, the register gate --strict, large_letter, the home gate; no demand, no retype; the summary read once) — launched in the background after the manifest (every cite index name used), verify_claims (6 verified / 0 failed) and the labels census (GATE PASSED, debt 0 — no label refused: every middah string ends in its parenthesis, asserted by the manifest writer before a byte was written) had run in the foreground and their prints were read.'
def rd(p): return open(p, encoding='utf-8').read()
# ---- THE NUMBERS, PARSED FROM THE PRINTS ----
truth = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py')
assert 'assert len(W["units"]) == 227' in truth and 'assert len(W["standing"]) == 2245' in truth and "8b8fff1fa28953af" in truth
CT = rd(f'{SP}/ch13_truth.out'); CB = rd(f'{SP}/ch13_bake.out'); C1 = rd(f'{SP}/ch13_fold_check1.out')
assert 'CORPUS TRUTH GREEN' in CT and 'CORPUS TRUTH GREEN' in C1 and 'wrote corpus_world.sqlite' in CB
rit = rd(f'{SP}/ch13_ritual_{UID}.out'); N_PASS = len(re.findall(r'^PASS', rit, re.M))
assert 'RITUAL COMPLETE' in rit and N_PASS == 13 and not re.search(r'^FAIL', rit, re.M), N_PASS
vt = rd(f'{SP}/ch13_vt_{UID}.out'); mvt = re.search(r'TEXT LAYER GREEN: (\d+) steps, (\d+) scenarios', vt); assert mvt and mvt.group(1) == '19', vt[-300:]
VT_STEPS, VT_SCEN = mvt.groups()
assert '  status: frozen' in rd(f'{ROOT}/logic/units/{UID}.yaml') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json') and 'ALL_DONE' in rd(f'{SP}/ch13_chain.log')
JG = rd(f'{SP}/ch13_journal.out'); RG = rd(f'{SP}/ch13_register.out'); BW = rd(f'{SP}/ch13_build.out'); GS = rd(f'{SP}/ch13_gates_SUMMARY.txt')
assert 'GATE GREEN' in JG and 'ALL GREEN' in BW and 'THE REGISTER GATE: GREEN' in RG and 'ALL GREEN' in GS, (JG[-200:], BW[-200:], GS[-200:])
mj = re.search(r'(\d+) kinds, ([\d,]+) rows', JG); J_KINDS, J_ROWS = mj.group(1), mj.group(2)
mr = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', RG); R_DECL, R_DEBT, R_FAIL = mr.groups()
assert R_DEBT == '0' and R_FAIL == '0', mr.groups()
mc = re.search(r'(\d+) units, (\d+) facts, (\d+) demands \((\d+) open\)', CT); C_UNITS, C_FACTS, C_DEM, C_OPEN = mc.groups()
assert C_UNITS == '227', C_UNITS
HG = rd(f'{SP}/ch13_home.out'); assert 'GREEN' in HG, HG[-200:]
LED = rd(f'{ROOT}/logic/oral_triage/deu_13_reeh_{LDATE}.md')
ml = re.search(r'\*\*read: (\d+) of \1 — COMPLETE\*\* \((\d+) Onkelos verses and (\d+) Sifrei rows.*?MATERIAL (\d+) Onkelos, CONTEXT (\d+) Onkelos, MATERIAL (\d+) Sifrei spine, CONTEXT (\d+) Sifrei spine, MATERIAL (\d+) Sifrei outside, CONTEXT (\d+) Sifrei outside', LED, re.S)
L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_SM, L_SC, L_XM, L_XC = ml.groups()
assert L_ALL == '122' and L_ONK == '19' and L_SIF == '103' and LED.count('⟨MISS⟩') == 0
L_SPINE = int(L_SM) + int(L_SC); L_OUT = int(L_XM) + int(L_XC); assert L_SPINE == 97 and L_OUT == 6, (L_SPINE, L_OUT)
L_BYTES = len(LED.encode())
N_REREAD = len(re.findall(r'^- Sifrei Devarim \d+:\d+ — [A-Z]+ \(REREAD WHOLE — read before in', LED, re.M)); N_REREAD_OUT = len(re.findall(r'^- Sifrei Devarim \d+:\d+ — [A-Z]+ \(REREAD WHOLE — first read in', LED, re.M))
assert N_REREAD == 2 and N_REREAD_OUT == 0, (N_REREAD, N_REREAD_OUT)
CODES = Counter(); BYCODE = {}
for line in re.findall(r'^- Sifrei Devarim \d+:\d+ — .*$', LED, re.M):
    name = re.match(r'- (Sifrei Devarim \d+:\d+)', line).group(1)
    for c in sorted(set(re.findall(r'\b([IE]\d{1,2}) \(', line))): CODES[c] += 1; BYCODE.setdefault(c, []).append(name.split(' ')[2])
CODE_TXT = '; '.join(f'{c} at {", ".join(BYCODE[c])}' for c in sorted(CODES, key=lambda x: (x[0], int(x[1:]))))
for c, r in (('I1', '86:3'), ('I2', '86:6'), ('I2', '90:2'), ('I2', '93:6'), ('I2', '117:3'), ('I2', '149:1'), ('I2', '190:7'), ('E30', '93:2')): assert r in BYCODE.get(c, []), (c, r, BYCODE.get(c))
assert sum(CODES.values()) == 8, dict(CODES)
d_ov = yaml.safe_load(rd(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'))
OV_REF13 = len([k for k in d_ov['by_ref'] if k.startswith('Deut.13.')]); OV_REF, OV_GL = len(d_ov['by_ref']), len(d_ov['by_gloss'])
assert OV_REF13 == 139 and OV_REF == 1122 and OV_GL == 707, (OV_REF13, OV_REF, OV_GL)
N_CLAIMS = len(json.load(open(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json', encoding='utf-8'))); assert N_CLAIMS == 6
VC = rd(f'{SP}/ch13_vc.out'); assert 'SUMMARY: 6 verified, 0 failed, 0 uncheckable, 0 no-check' in VC, VC[-300:]
LAB = rd(f'{SP}/ch13_labels.out'); mlab = re.search(r'CLAIM LABELS CENSUS — (\d+) claims in (\d+) manifests; labeled \1; DEBT 0', LAB); LN = f'{int(mlab.group(1)):,} claims in {mlab.group(2)} manifests'; assert 'GATE PASSED' in LAB and re.search(r'deu\s+82 claims', LAB), LAB[-300:]
assert all(rd(f'{SP}/ch13_ink_run{n}.out').strip().endswith('0 failing statements') for n in (1, 2, 3))
N_INK = len(re.findall(r'^assert ', rd(f'{SP}/ch13_ink.py'), re.M)); assert N_INK == 103, N_INK
LL = rd(f'{SP}/ch13_large_letter.out').strip().split('\n')[-1]; assert LL.endswith('6/6'), LL
JPREV = f'{ROOT}/World/step9/forms_deuteronomy_walk/gates_ch12b_journal.out'
JR12 = re.search(r'12 kinds, ([\d,]+) rows', rd(JPREV)).group(1); DJ = int(J_ROWS.replace(',', '')) - int(JR12.replace(',', ''))
MAN = rd(f'{SP}/ch13_manifest.out'); assert 'every CITE INDEX name used by a claim: True' in MAN
DUMP = rd(f'{SP}/ch13_dump0.out'); mdump = re.search(r'DB verses (\d+) \| export verses HE (\d+) EN (\d+)', DUMP); assert mdump and mdump.groups() == ('19', '19', '19'), DUMP[:300]
LEDW = rd(f'{SP}/write_ch13_ledger.out'); assert '122 sources' in LEDW and 'MISMARK []' in LEDW and 'FAIL []' in LEDW, LEDW[-200:]
PATCH_LINE = 'override rows written: by_ref 139 by_gloss 34 | by_ref total 1122 | by_gloss total 707'
# ---- THE TIMING TABLE, computed from the scratchpad's tsv (no 'started' row this sitting — the first step's own stamp is the start) ----
def timing():
    rows = [l.rstrip('\n').split('\t') for l in rd(f'{SP}/ch13_timing.tsv').splitlines() if l.strip()]
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
print('PARSED:', dict(ritual_pass=N_PASS, verify_text=(VT_STEPS, VT_SCEN), journal=(J_KINDS, J_ROWS, DJ, JR12), register=(R_DECL, R_DEBT, R_FAIL), corpus=(C_UNITS, C_FACTS, C_DEM, C_OPEN), ledger=(L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_SM, L_SC, L_XM, L_XC, L_BYTES, N_REREAD, N_REREAD_OUT), codes=dict(CODES), overrides=(OV_REF13, OV_REF, OV_GL), claims=N_CLAIMS, labels=LN, ink=N_INK, large_letter=LL[-3:], timing=(T_ROWS, T_MACH, T_TOTAL, T_START), chain=(CS_TXT, CS_TOTAL)))
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

STAMP = (f'| {DATE} | {UID} | DELEGATED | FULL RULE | Deuteronomy 13:1-19 derivation {LDATE} (THE DEUTERONOMY WALK sitting 11 — CHAPTER 13; the owner: "Go" — a reading sitting under THE COST RULES, one run to the clean point #202 and its tail after the compaction, every step timed, every row whole): Onkelos Deuteronomy 13 whole (19 = 19, the identity) + the Sifrei on Deuteronomy ON THE CHAPTER — piskaot 82-96 (88 without a head citation folded in on its consonants; 96:9-12 on 14:1 left for chapter 14), {L_SPINE} spine rows read whole in both files ({N_REREAD} rows read before and reread whole) + its {L_OUT} rows outside the spine read whole + the kin credited by name; the ledger deu_13_reeh_{LDATE}.md ({L_ALL} sources, coverage computed, lint 0); {N_CLAIMS} claims DV13-01..06 verified 6/0, seated as six WITNESS_READ at 13:1, 2, 7, 13, 17, 19; the ritual {N_PASS} PASS; CORPUS TRUTH GREEN ({C_UNITS} units, standing 2245, hash unmoved); the fold layer +{DJ}; the display layer +{OV_REF13} by reference, +34 by gloss; the machine\'s share of the sitting {mmss(T_MACH)} of {mmss(T_TOTAL)} | {LN}, labeled, debt 0 |\n')

WALK = f'''


## Sitting 11 — CHAPTER 13 — AS BUILT ({DATE}; the design above stands as written — the one run ran to the clean point #202 after the rows and the ledger, the owner compacted, and THE TAIL ran on "Reread" and "Go" at the step the point named; every departure from the design is named here; THE TIMING TABLE is the last section)

THE RESULT: Deuteronomy 13:1-19 READ, FROZEN and SEATED as ONE unit — deu_13_seducers (the 227th frozen unit; 19 of 19 verses in the Hebrew numbering, missing 0,
computed — the English's 12:32 the DB's 13:1; no portion edge inside it): the ledger logic/oral_triage/deu_13_reeh_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL
{L_OM} / CONTEXT {L_OC}; THE SIFREI'S SPINE piskaot 82-96 {L_SPINE} rows: MATERIAL {L_SM} / CONTEXT {L_SC}, {N_REREAD} of them read before and REREAD WHOLE (the prior reads found in the earlier
ledgers by computation — 82:5 at sitting 1, 83:4 at a Genesis sitting); the outside rows {L_OUT}: MATERIAL {L_XM} / CONTEXT {L_XC}, none read before; {L_BYTES:,} bytes, lint 0, no cut
missed — the ledger written clean on its first run), the manifest {N_CLAIMS} claims DV13-01..06 verified 6/0 (every he_contains cut from the store's own bytes; every cite index name
used by a claim — the spine's rows distributed by piska from the CITE INDEX itself, the headless 88 with the inciter's piskaot, piska 96 split at its own rows, the
six outside rows with the claims whose verses they cite), seated as six WITNESS_READ operators at 13:1, 2, 7, 13, 17, 19 with step E; the ritual {N_PASS} PASS; verify_text
GREEN ({VT_STEPS} steps, {VT_SCEN} scenarios); the fold predicted and matched (units 226 → 227, standing 2239 → 2245, the hash 8b8fff1fa28953af unmoved — CORPUS TRUTH GREEN before
and after the bake: {C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, {C_OPEN} open); build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer since
10b's chain, the tape unmoved since 10b); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — no receipt, no header, no footer in chapter 13; 13:18's
"as He swore to your fathers" the oath's AS_WHEN form, a run citation for 11b's census); large_letter_probes {LL[-3:]}; the labels census GREEN ({LN}, Deuteronomy 82);
the home-path gate GREEN; the display layer +{OV_REF13} by reference and +34 by gloss ({OV_REF} / {OV_GL} in all).

THE READING: every Onkelos row whole in the Aramaic and the English (ch13_onkelos.txt); THE SPINE ON THE CHAPTER A FIFTH TIME — fifteen piskaot 82-96, fourteen heading on
the chapter's verses and ONE WITHOUT A HEAD CITATION (88 on 13:8's "of the gods of the peoples round about you") folded in on its consonants, every row read whole in
both files (ch13_sifrei_spine.txt, split by piska for the reading — ch13_spine_p82.txt … p96.txt); PISKA 96's LAST FOUR ROWS LEFT FOR CHAPTER 14 (96:9 opens with
14:1's citation, 96:10-12 with its clauses — never read ahead; asserted on the rows' own bytes); the six outside rows whole in both files (ch13_sifrei_outside.txt —
Belial at 15:9, the inquiry at 17:4 twice, the rebellion at 19:16, the inquiry at 19:17-18 twice), none excluded; the kin (Exodus 22:19 and 32:1-8; Leviticus
20:2, 20:27, 24:14-23, 27:28-29; Numbers 12:6, 15:30-36, 21:2-3, 25:4; Deuteronomy 4:2, 5:6, 6:13-14, 7:2-26, 8:2-16, 9:26, 10:20, 11:22-28, 12:25-28) credited by
name with the counts computed from twenty ledgers; no ledger holds an Onkelos row of Genesis 22:1, Genesis 37 or Exodus 20:2, and NONE OF DEUTERONOMY 14-20 OR THE
PROPHETS (asserted — never read ahead; the idolater and the hand first at 17:2-7, the false prophet at 18:20-22, the plotting witness at 19:16-19, the exile at 28:64
wait for their own sittings).

THE DEPARTURES FROM THE DESIGN: none in substance; three in the tail's order and the instruments. (1) THE FAST STEPS RAN IN THE FOREGROUND BEFORE THE FREEZE — the
manifest, verify_claims and the labels census take seconds, so their prints were read BEFORE the chain's seat wrote a byte and the ritual froze the unit; the chain
(minutes) was then launched in the background with the records writer and the copier typed during its run and the notification the wake (sitting 10 had launched all
four as one background command — the freeze is the one step that cannot be retyped, so the look before it is worth one call). (2) THE SHELLS' DERIVE PROTECTED THE
FORM'S NAME IN EVERY SHELL by a placeholder (chapter 12's lesson 12 applied) — nothing retyped. (3) THE INK WAS GREEN ON ITS FIRST TYPED PASS — no form fell; the one
red print was the driver's launch from the scratchpad (154 "not a git repository" fails — the scratch script computes ROOT from git and the scratchpad has no root),
rerun from the repo root with PYTHONPATH the scratchpad: a launch, not a fact; the second pass added the English's three citation slips as asserts, the third ran
PATCHED. THE DESIGN'S ONE COUNT CORRECTED AT THE PRINT: three infinitive absolutes written, FOUR measured (kill, diligently, smite, devote — "diligently" is one). THE
MANIFEST WROTE FIRST TIME (every cite index name used; the six checks as designed, "you shall not add" at 13:1 among them — the store's piece six code points pointed).
THE DISPLAY PATCH held first time (twelve asserted substitutions on the chapter-12 form; the anchors sitting 10's last rows found by walking, never typed; {PATCH_LINE}).
THE MIDDAH CODES held — every code checked in MIDDOT.md before it was typed, none relabeled: the census from the ledger's rows — {CODE_TXT}. {CHAIN_NOTE}

THE GATES, COMPUTED FROM THEIR PRINTS: the ritual {N_PASS} PASS (RITUAL COMPLETE, {C_UNITS} frozen units); CORPUS TRUTH GREEN twice ({C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, {C_OPEN} open;
the hash unmoved); build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows, +{DJ}); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL});
verify_claims 6 verified / 0 failed; the labels census GREEN ({LN}); large_letter_probes {LL[-3:]}; the home-path gate GREEN; the ink {N_INK} asserts — 0 failing on
all three passes (the first typed pass green; the third after the display patch).

⚠ THE LESSONS (the run's, gathered — the numbered list the sheet asks for): (1) A PISKA'S BOUNDARY IS NOT A CHAPTER'S — 96:9-12 open with 14:1 and wait for chapter 14's
sitting: the rows decide by their own words, and chapter 14's dump must split piska 96 (96:9, 96:11 and 96:12 by their citations of 14:1, 96:10 — Amos 9:6 alone — by
the consonant rule); recorded in COMPILE_DEBT. (2) THE INK GREEN ON ITS FIRST TYPED PASS — the forms held: the generic helpers copied by content markers, the kin
recomputed inside the script, every assert typed from the prints; the one red was the launch — a scratch script computing ROOT from git runs FROM THE REPO ROOT with
PYTHONPATH the scratchpad. (3) A SUBSTRING TEST ON A CODE IS A TEST OF NOTHING — the dump's name test matched two niphal perfects by the letters "Np" inside "VNp", its
bare number check matched the seven inside "swore": the ink retypes both as prefix and engine tests. (4) THE 600k CAP WAS PASSED BY /context, NOT BY THE COUNTER —
651.7k at the clean point where the counter had shown far less (10b's lesson a second time); the rows' typing is the heavy half of a reading run: the next reading
reads the spine in two halves with the rows typed after each, or plans the clean point before the ledger. (5) THE ENGLISH'S SLIPS ASSERTED, NOT CORRECTED — three in
one chapter (117:3's "(Dt.13:4)" for 13:14, 87:3's "Ezek.24:16" for Deuteronomy 24:16, 95:6's "Josh.6:36" for 6:26) and 89:3's Leviticus 19:16 the English drops for
13:9: the Hebrew's citation decides, the English's text stands. (6) THE TWO FILES DIVIDE A PISKA'S ROWS DIFFERENTLY AGAIN (190:7-8 — the Hebrew's 190:8 the false
witness's row, the English's the probes'): chapter 8's lesson a second time; both texts read whole, the row counted once. (7) THE FORM'S NAME PROTECTED IN EVERY SHELL
— a placeholder in the chain, the fold and the gates derives before the global substitution; nothing retyped. (8) THE FAST STEPS IN THE FOREGROUND, THE SLOW CHAIN IN
THE BACKGROUND — the manifest, the verifier and the census (seconds) read before the ritual freezes a unit; the chain (minutes) launched after with its readers typed
during the run. (9) THE KIN BY COMPUTATION IS THE READING'S FIRST INSTRUMENT AGAIN — 4:2 the header's only twin (seven tokens in order); the seducers' formula at 13:3,
7, 14 each other's closest kin; 17:4 the inquiry's twin (nine of twelve); 1 Kings 13:3 the sign's one two-token kin; Joshua's Makkedah and Ai the ban's and the heap's;
Achan's valley saying 13:18 back. (10) THE PURGE FORMULA'S FIRST SEAT — "and you shall purge the evil from your midst" nine in the Bible, all in the book, 13:6 the
first: the compile's effect named from the shelf's own row (86:10 — the doer of evils removed). (11) A PROSCRIPTION FOR EVERY PRESCRIPTION — R. Eliezer son of Jacob's
rule at the header (82:2) and at the six verbs (85:3): "keep" the prohibition's verb, "do" the command's — the compile's rule that each positive cell carries its
negative. (12) THE STORE CARRIES THE KETIV — at 13:16 the written masculine and the read feminine both (329 tokens against the DB's 328), kept out of every DB check;
the shelf quotes the read form (94:2); the Prophets write the feminine, the Torah never. (13) EVERY STEP TIMED — the machine's share of the sitting {mmss(T_MACH)} of
{mmss(T_TOTAL)} wall time from {T_START} to the records; the rest the reading, the typing and one compaction: the reading is the sitting, the machine its instrument.

THE TIMING TABLE (every row appended by the scratchpad's timer as the step ran; the gap column is the time between one step's end and the next step's start — the
reading of the rows, the typing of the scripts, the owner's compaction between the clean point and the tail's rereads; the chain's inner steps from its own summary's
stamps):

{TT}

The chain's inner steps (ch13_gates_SUMMARY.txt): {CS_TXT}; the chain {mmss(CS_TOTAL)} in all. The machine's share {mmss(T_MACH)}; the sitting {mmss(T_TOTAL)} from {T_START}
to the last row above; the records writer's own row and the copier's follow in ch13_timing.tsv (copied into the forms).

THE FORMS: World/step9/forms_deuteronomy_walk/ (copy_ch13_forms.py — derive_ch13_dump0.py, ch13_dump0.py, derive_ch13_measure1.py, ch13_measure1_sections.py,
ch13_measure1.py, split_ch13_spine.py, ch13_ink_head.py, ch13_ink_body.py, ch13_ink_body_b.py, ch13_ink_body_c.py, derive_ch13_ink.py, ch13_ink.py, assert_driver.py,
the five row files, write_ch13_ledger.py, write_ch13_design.py, write_ch13_cleanpoint.py, derive_ch13_patch.py, ch13_patch_overrides.py, write_ch13_manifest.py,
seat_ch13.py, derive_ch13_shells.py, ch13_chain.sh, ch13_fold.sh, ch13_gates.sh, tstep.sh, write_ch13_records.py, copy_ch13_forms.py, the prints and ch13_timing.tsv).

NEXT on the ruling: the commit on the owner's word (this sitting stands uncommitted since 2b0c9c8 — one message at <scratch>/commit_msg_ch13.txt); then THE COMPILE OF
CHAPTER 13 (sitting 11b) in TWO RUNS + THE TAIL under the cost rules — RUN A: the rereads (THE_STEPS Step 5 + the compiler block; this section; the 11b box in
COMPILE_DEBT), the measurements (the cloud's lines on the tape for 85:1's run citation; the oath's cells for 13:18's AS_WHEN form; the calf's line for the seducers'
formula; the register's finder at 13:18; Leviticus 20's and 24's cells for the stoning; Leviticus 27's for the devoted thing; 7:26's for the devoted thing in the
house), THE DESIGN (the three cases as cells — the prophet's test with the sign's status a PARAMETER and the death's mode a PARAMETER, the inciter's hand first with
the festival's timing a PARAMETER, the condemned city's decision table with the property table; the purge formula's first seat an effect; the anger keyed to
idolatry; the mercy two-armed; the checkpoint series DE), the probes to FAIL, THE DOCKET by the union rule (Mishnah Sanhedrin 7:10, 7:6, 10:4-6, 11:1, 11:4-6, 5:1-2,
1:5, 4:1 with Sanhedrin 67a, 111b-113b, 89a-90a, 40a-41a, 88b; Tosefta Sanhedrin 11:7, 12:6, 14:1-6; Mishnah Makkot 1:4-6; Mishnah Zevachim 8:10 with Zevachim 80a-81b
and Tosefta Zevachim 8:23; Mishnah Sukkah 3:4 with Sukkah 34b; Menachot 41b-42a; Rosh Hashanah 28b; Eruvin 96a; Mishnah Avodah Zarah 3:9 with Avodah Zarah 49b-50a;
Bava Metzia 59b; Yevamot 90b; Tosefta Bava Kamma 9:30; Shabbat 151b; Avot 2:1, 3:9, 3:14; Sifrei Numbers 103, 113, 114; the Sifra on Leviticus 20 and 24 credited
from their sittings — every row whole; a docket past ~700 rows its own run); RUN B: the types, the runner, the tape to 10/10, the chain LAUNCHED; THE TAIL the
records, the forms, the message — or the Decalogue-schema sitting first, on his word.
'''

DEBT = f'''

## SITTING 11 — CHAPTER 13 ({DATE}, the reading; deu_13_seducers frozen) — OWED TO THE COMPILE 11b: (a) THE PROPHET'S TEST (13:2-6) — the sign's status a PARAMETER
## (granted true and barred anyway — R. Yose the Galilean, 84:1; a fallen prophet's standing — R. Akiva, 84:2, Hananiah son of Azzur at 189:1) with the test the
## reason either way (13:4; 8:2 and 8:16 by CALL), the death's mode a PARAMETER (stoning by the analogy of "thrusting" — 86:6, 90:2; strangling — R. Shimon, Mishnah
## Sanhedrin 11:1; Sanhedrin 89a-90a with Mishnah 11:5-6), the sign not decisive (Bava Metzia 59b) and the prophet's temporary uprooting (Yevamot 90b — 85:4's "the
## voice of His prophets"), the death's reason the a fortiori from the plotting witness (86:3 — Mishnah Makkot 1:4-6), the exemptions of duress and error (86:1-2 —
## the exam's persons), THE CLOUD a RUN CITATION (85:1 — the tape's Numbers 9-10 lines inside a law); (b) THE HEADER'S NOT-ADDING (13:1) — 4:2's cell by CALL, the
## four species and the fringes (82:4 — Mishnah Sukkah 3:4; Sukkah 34b; Menachot 41b-42a), the priests' blessing (82:5 — Rosh Hashanah 28b; Eruvin 96a; Sanhedrin
## 88b), the mixed bloods (82:3 — Mishnah Zevachim 8:10; Zevachim 80a-81b; Tosefta Zevachim 8:23): a PARAMETER with no play; R. ELIEZER SON OF JACOB'S RULE (82:2,
## 85:3 — "keep" the prohibition, "do" the command) the compile rule that each positive cell carries its negative; the light commandment as the weighty (82:1, 96:7 —
## Avot 2:1); (c) THE INCITER (13:7-12) — the concealed witnesses and the entrapment (Mishnah Sanhedrin 7:10; Sanhedrin 67a), the inclusion table (87:4-11), the two
## senses of "entice" (87:1-2), the five prohibitions each against a standing duty (89:1-5 — Leviticus 19:16, 19:18 and Exodus 23:5 by CALL), THE COURT'S RULE INVERTED
## (89:6-7 — Mishnah Sanhedrin 4:1), the hand first the enticed's own (89:8; 17:7 ahead), the stones and the stone one rite (90:1 — Leviticus 20:27 by CALL; the two
## verbs of stoning measured: Leviticus 20 and 24, Numbers 15 by CALL), THE FESTIVAL'S EXECUTION a PARAMETER of timing (91:1-2 — Mishnah Sanhedrin 11:4; Sanhedrin
## 89a; Tosefta 11:7), the fifteen utterances (91:3), the honors of an idol not capital (91:4 — Mishnah Sanhedrin 7:6); the exodus formula with redeeming (13:6, 13:11 —
## 5:6 by CALL); (d) THE CONDEMNED CITY (13:13-18) — one city at a time, two allowed, not three (92:3 — Mishnah Sanhedrin 1:5), Jerusalem excluded by "to dwell there"
## (92:5 — chapter 12's place outside the ban) and the border (93:3), the seducers' parameters (93:1-5 — adult, male, two at least, of the city, with a warning —
## Mishnah 10:4; Sifrei Numbers 113), THE SEVEN INQUIRIES AND THE PROBES (93:6-9; 149:1-2; 190:7-8 — Mishnah Sanhedrin 5:1-2; Sanhedrin 40a-41a: the two examinations'
## two rules, a decision table), "by any means" (94:1), the children (94:3 — Abba Hanan against the rule), THE PROPERTY TABLE (94:4-5, 95:1 — Mishnah Sanhedrin 10:5),
## Heaven's spoil and the consecrated (94:6, 95:4-5 — Mishnah 10:6), the heap and Jericho (95:6-7, 96:1 — Joshua 6:26, 1 Kings 16:34 the run's cases ahead), the
## devoted thing's benefit to the Salt Sea (96:2 — Mishnah Avodah Zarah 3:9; Avodah Zarah 49b-50a); Mishnah Sanhedrin 10:4-6 and Sanhedrin 111b-113b whole; Tosefta
## Sanhedrin 14:1-6; (e) THE EFFECTS — "purge the evil from your midst" THE PERSON REMOVED (86:10 — the formula's first seat of nine, all in the book), THE ANGER KEYED
## TO IDOLATRY'S PRESENCE (96:3), THE MERCY TWO-ARMED (96:4 — Tosefta Bava Kamma 9:30; Shabbat 151b), the fathers' merit (96:5 — 7b's parameter); (f) THE RUN
## CITATIONS — the cloud (85:1), THE OATH (13:18 "as He swore to your fathers", the AS_WHEN form; 19:8 ahead) for the census, the register's finder finding no receipt
## in the chapter (measured); (g) THE KIN BY CALL — Exodus 22:19 (the ban's first seat), Leviticus 27:28-29, Numbers 21:2-3 and 25:4, 7:2-26, 6:13-14, 10:20,
## 11:22-28, 12:25-28; (h) NEVER READ AHEAD — 17:2-7 (the idolater, the hand first, the inquiry's twin), 18:20-22 (the false prophet), 19:16-19 (the plotting witness),
## 24:16, 28:64 wait for their sittings — their cells by CALL when they come; (i) CHAPTER 14's SPLIT OF PISKA 96 — rows 9-12 are 14:1's (96:9, 96:11 and 96:12 by their
## citations of 14:1; 96:10 cites Amos 9:6 alone and is folded by the consonant rule): chapter 14's dump reads them, this ledger's union left them (asserted); (j) THE
## REGISTER's DATA rows — no imperative, no "if" (the three cases on "when"), the seducers' "we" the chapter's only first person plural, the four infinitive absolutes,
## the one wayyiqtol, THE KETIV AT 13:16 (the store carries both forms), the parser's [1] at 13:13, the tagger's substring slip ("Np" inside "VNp"; the bare number
## check inside "swore"); (k) THE CHECKPOINT SERIES continues (DD the fourth name — DD9 the last; the next DE1, keyed by its first word); (l) THE DOCKET by the union
## rule — the testing shelf as the design listed it (Sanhedrin's nine Mishnah rows and its folios; Makkot 1:4-6; Zevachim 8:10 and 80a-81b; Sukkah 3:4 and 34b;
## Menachot 41b-42a; Rosh Hashanah 28b; Eruvin 96a; Avodah Zarah 3:9 and 49b-50a; Bava Metzia 59b; Yevamot 90b; Tosefta Bava Kamma 9:30; Shabbat 151b; Avot 2:1, 3:9,
## 3:14; Sifrei Numbers 103, 113, 114; the Sifra on Leviticus 20 and 24 credited from their sittings) — EVERY ROW WHOLE; a docket past ~700 rows its own run; THE COST
## RULES: two runs + the tail, the chain launched at RUN B's end. NOTHING ELSE IN CHAPTER 13 IS OWED TO A LATER SITTING OF ITS OWN.
'''

MIDDOT = f'''- **THE SIFREI ON DEUTERONOMY'S OWN CASE LAW ON CHAPTER 13 (Deuteronomy 13:1-19; THE DEUTERONOMY WALK sitting 11, {DATE};
  the ledger logic/oral_triage/deu_13_reeh_{LDATE}.md — THE SPINE ON THE CHAPTER A FIFTH TIME, piskaot 82-96 (88 without a head
  citation folded in on its consonants; 96:9-12 on 14:1 left for chapter 14), {L_SPINE} rows read whole in both files, and six rows outside
  the spine; EVERY CODE CHECKED IN MIDDOT.md BEFORE IT WAS TYPED, none relabeled; the census from the ledger's own rows: {CODE_TXT}):**
  · THE A-FORTIORI FROM THE PLOTTING WITNESS (86:3 on 13:6): if one who falsifies his fellow's words is liable to death, one who
    falsifies the words of the Omnipresent how much more — I1 (checked; the row's own words קַל וָחוֹמֶר ("an a fortiori") on its bytes);
    the death's reason; the answer sheet Mishnah Makkot 1:4-6 at the compile's docket; THE INK: "for he spoke rebellion" the noun's two
    Torah seats (13:6, 19:16 — 189:1 reads each by the other).
  · THE VERBAL ANALOGY OF THRUSTING, RUN BOTH WAYS (86:6 on 13:6; 90:2 on 13:11): "thrusting" is said here and "thrusting" is said
    there — as the inciter's is by stoning, so the prophet's; and from the prophet's seat back to the inciter's — I2 (checked; גְּזֵרָה
    שָׁוָה ("a verbal analogy") at both seats); R. Shimon strangling the dissent (Mishnah Sanhedrin 11:1) — the death's mode a PARAMETER;
    THE INK: the verb ten in the book, the chapter's three (13:6, 11, 14).
  · THE VERBAL ANALOGY "DILIGENTLY, DILIGENTLY" AT THREE SEATS (93:6 on 13:15; 149:1 on 17:4; 190:7 on 19:18): the seven inquiries
    taught to every capital court from the condemned city's verse — I2 (checked at each seat); the probes from "true and certain" (93:7),
    the two examinations' two rules (93:8-9; 149:2 — Mishnah Sanhedrin 5:1-2); THE INK: "diligently" an infinitive absolute, five in the
    book, 17:4 the twin with nine of twelve tokens in order.
  · THE VERBAL ANALOGY OF BELIAL (117:3 on 15:9 from 13:14): "Belial" is said here and "Belial" is said there — as the sons of Belial
    there are idolatry, so the word of Belial here — I2 (checked); THE INK: the Torah's two seats of the word, computed; the English's
    "(Dt.13:4)" a wrong verse, the Hebrew right.
  · "SONS OF BELIAL" READ AS "WITHOUT A YOKE" (93:2 on 13:14): the word split into its parts — E30 (checked; the notarikon, a word
    read as parts); THE INK: "Belial" twenty-seven in the Bible, Naboth's witnesses the closest verse.
  · A PROSCRIPTION FOR EVERY PRESCRIPTION (82:2 on 13:1; 85:3 on 13:5): R. Eliezer son of Jacob — "keep" the prohibition's verb, "do"
    the command's, a prohibition set on every positive command in the passage — named by the rows' own words, no code typed; the
    compile's rule that each positive cell carries its negative.
  · THE INCLUSION TABLE OF THE INCITER'S KIN (87:4-11 on 13:7): the brother by the father, the mother's son, the son and the daughter of
    any kind, the betrothed and the married, the convert, and the father found in "as your own soul" — named without a code; THE INK:
    "the wife of your bosom" and "your friend as your own soul" one seat each.
  · THE COURT'S RULE INVERTED (89:6-7 on 13:10): "kill" — convicted, not brought back to acquit; "you shall kill him" — acquitted, brought
    back to convict: the doubled verb's two halves read as two rules against Mishnah Sanhedrin 4:1's ordinary procedure — named without a
    code; THE INK: "kill, you shall kill him" one seat, the infinitive absolute.
  · THE STONES AND THE STONE (90:1 on 13:11): Leviticus 20:27's singular and the chapter's plural reconciled — not dead by the first,
    dies by the second — named without a code; THE INK: two verbs of stoning in the Torah, 21:21 alone holding both.
  · THE INFINITIVE ABSOLUTE READ AS "BY ANY MEANS" (94:1 on 13:16): smite by any death, light or heavy, and by any hand; and (91:4 on
    13:12) "this" — this one by stoning and not the eight honors of an idol — the doubling and the demonstrative each read for its scope,
    named without a code; THE INK: the chapter's four infinitive absolutes.
  · THE PROPERTY TABLE (94:4-5, 95:1 on 13:16-17): the righteous' inside lost and outside saved, the wicked's lost either way — from
    "devote it", "all that is in it", "all its spoil" — Mishnah Sanhedrin 10:5's table read off three clauses, named without a code.
  · NAMED WITHOUT A CODE: the prophet's forms are Moses' (83:1); the sign disputed — true and barred, or a fallen prophet (84:1-2); the
    first verb the cloud (85:1); "purge the evil" the doer removed (86:10 — the formula's first seat); one city, not three (92:3);
    Jerusalem excluded by "to dwell there" (92:5); the three verbs three sources (92:2); "a heap forever" read by Joshua's oath (95:6);
    the anger keyed to idolatry (96:3); the mercy two-armed (96:4); the footer the header's sentence (96:7).
'''

RESEARCH = f'''

## {DATE} — DEUTERONOMY 13 READ AND FROZEN (THE DEUTERONOMY WALK sitting 11 — a reading sitting under THE COST RULES: one run to the clean point #202, the
## compaction, the tail; EVERY STEP TIMED): THE SEDUCERS' ONE FORMULA AT THREE CASES; THE HEADER'S TWIN 4:2 — THE ONLY TWO SEATS OF "NOT ADD NOR TAKE AWAY";
## "PURGE THE EVIL FROM YOUR MIDST" AT ITS FIRST SEAT OF NINE; THE INQUIRY THAT TEACHES EVERY CAPITAL COURT ITS SEVEN QUESTIONS; A PROSCRIPTION FOR EVERY
## PRESCRIPTION; THE PISKA THAT RUNS PAST THE CHAPTER; AND THE RUN THAT PASSED THE CAP BY /context
On the owner's "Go" after the reread that followed 10b's compaction ({DATE}). THE READING: Deuteronomy 13:1-19 with Onkelos whole (the export's 19 rows the DB's 19 —
the identity, asserted; the English's 12:32 the DB's 13:1, no row of the shelf citing 12:32) and THE SIFREI ON DEUTERONOMY ON THE CHAPTER A FIFTH TIME — piskaot
82-96 (fourteen heading on the chapter's verses; 88 WITHOUT A HEAD CITATION, folded in on its consonants — 13:8's "of the gods of the peoples round about you"; PISKA
96's ROWS 9-12 ON 14:1 LEFT FOR CHAPTER 14), {L_SPINE} rows read whole in both files ({N_REREAD} read before at sitting 1 and a Genesis sitting and reread whole — found by
computation), six rows outside the spine read whole (117:3 Belial at 15:9 — the English's "(Dt.13:4)" a wrong verse, the Hebrew right; 149:1-2 the inquiry at 17:4;
189:1 the rebellion at 19:16; 190:7-8 the inquiry at 19:17-18 — the two files dividing the piska differently), none excluded; the kin credited by name from twenty
ledgers (Exodus 22:19 — the ban's first seat; 32:1-8 the calf's "these are your gods"; Leviticus 20:2, 20:27, 24:14-23 the stonings; 27:28-29 the devoted thing;
Numbers 12:6, 15:30-36, 21:2-3, 25:4; Deuteronomy 4:2, 5:6, 6:13-14, 7:2-26, 8:2-16, 9:26, 10:20, 11:22-28, 12:25-28); NEVER READ AHEAD — no Onkelos row of Deuteronomy
14-20 or the Prophets in any ledger (asserted). FROZEN as ONE unit deu_13_seducers (the 227th; no portion edge inside it; standing 2245 = 2239 + 6 as predicted, hash
unmoved); the ledger deu_13_reeh_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the spine {L_SPINE}: MATERIAL {L_SM} / CONTEXT {L_SC}; the outside rows {L_OUT}:
MATERIAL {L_XM} / CONTEXT {L_XC}; coverage computed, lint 0, no cut missed, written clean on its first run); six claims DV13-01..06 verified 6/0, seated as six WITNESS_READ at
13:1, 2, 7, 13, 17, 19; the ritual {N_PASS} PASS; the fold +{DJ} on the journal; the display layer +{OV_REF13} by reference and +34 by gloss. THE FINDS: THE HEADER'S TWIN IS 4:2 —
"you shall not add to it nor take from it" the singular here and the plural there, THE ONLY TWO SEATS of the clause (seven tokens in order), the shelf reading it at
the word's grain (82:5 — the priests' blessing), the count's (82:4 — the four species, the fringes) and the rite's (82:3 — the mixed bloods); A PROSCRIPTION FOR EVERY
PRESCRIPTION — R. Eliezer son of Jacob's rule at the header and at the six verbs (82:2, 85:3); THE SEDUCER'S ONE FORMULA — "let us go (and serve) other gods which you
have not known" at 13:3, 13:7, 13:14, each the others' closest kin by computation; THE DREAM'S NOUN AND VERB in the book only at the chapter's three seats; "is
testing" the participle's one seat (Genesis 22:1 the first; the sign in the heavens and the wonder on the earth — 83:4-5); THE SIGN DISPUTED — true and barred (R. Yose
the Galilean) or a fallen prophet's, Hananiah's (R. Akiva; 189:1 his sentence) — a PARAMETER; THE FIRST VERB IS THE CLOUD (85:1 — a run citation inside a law), "His
voice obey" the voice of His prophets (85:4); THE DEATH'S MODE BY ANALOGY run both ways (86:6, 90:2; R. Shimon strangling) — a PARAMETER; its reason an a fortiori from
the plotting witness (86:3); "AND YOU SHALL PURGE THE EVIL FROM YOUR MIDST" NINE SEATS IN THE BIBLE, ALL IN THE BOOK, 13:6 THE FIRST — the doer removed (86:10);
"ENTICE" THE TORAH'S ONE TOKEN (Jezebel's and Saul's the shelf's two senses — 87:1-2); THE INCITER'S KIN AN INCLUSION TABLE with the father found in "as your own soul"
(87:4-11); "the wife of your bosom", "your friend as your own soul", "the son of your mother" one seat each; 6:14's clause SPELLED DEFECTIVE at 13:8; THE FIVE
PROHIBITIONS OF 13:9 each against a standing duty (89:1-5 — the neighbor's love, the enemy's ass, the neighbor's blood, the defense, the silence), "spare" the Torah's
two with Saul's order the third; THE COURT'S RULE INVERTED (89:6-7); THE HAND FIRST — 17:7's twin, "afterward" the Torah's two seats both this clause; TWO VERBS OF
STONING in the Torah (Deuteronomy's, Leviticus's and Numbers', 21:21 both) and the stones and the stone one rite (90:1); "ALL ISRAEL SHALL HEAR AND FEAR" the formula's
first of four with the paragogic nun — the festival's execution a PARAMETER of timing (91:1-2); THE FIFTEEN UTTERANCES (91:3) and the honors not capital (91:4);
"IN ONE OF YOUR CITIES" THE CHAPTER'S ONE NUMBER VERSE [1] given its rule — one city, not three (92:3), Jerusalem excluded by "to dwell there" THE TORAH'S ONE SEAT
(92:5), the border (93:3); SONS OF BELIAL the Torah's two (13:14, 15:9 — 117:3's analogy), Naboth's witnesses the closest verse, "without a yoke" (93:2); THE ONE
NARRATIVE VERB inside the third case; THE SEVEN INQUIRIES FROM THE CHAPTER — "diligently, diligently" at three seats (93:6; 149:1; 190:7), 17:4 the twin (nine of twelve
tokens in order), the two examinations' two rules (93:8-9 — Mishnah Sanhedrin 5:1-2); THE INFINITIVE ABSOLUTES FOUR (kill, diligently, smite, devote — "by any means",
94:1); THE KETIV AT 13:16 ("that city" — the feminine never written in the Torah, the Prophets write it; the store carrying both forms, 329 against 328; the shelf
quoting the read form); THE PROPERTY TABLE (94:4-5, 95:1) and Heaven's spoil (95:4-5); "WHOLLY TO THE LORD" 13:17 and Samuel's lamb, the word the priest's meal
offering's; "A HEAP FOREVER" Ai's and "not built again" Tyre's — JERICHO THE RUN'S CASE read by Joshua's oath (95:6-7, 96:1); the devoted thing's benefit to the Salt
Sea (96:2); "FROM THE FIERCENESS OF HIS ANGER" — Achan's valley says the words back (Joshua 7:26), the anger keyed to idolatry's presence (96:3); THE MERCY TWO-ARMED
(96:4); "AS HE SWORE TO YOUR FATHERS" (13:18) the AS_WHEN form, 19:8 its twin — a run citation for 11b's census, the register's finder finding no receipt in the
chapter; THE FOOTER THE BLESSING'S AND THE CURSE'S OPENING (28:1 fourteen tokens in order, 28:15 twelve, 15:5 eleven), "to do the right in the eyes of the LORD"
Jehoshaphat's measure, THE FOOTER THE HEADER'S SENTENCE (82:1, 96:7); THE REGISTER: singular but for the prophet's case (13:4-5 plural), the seducers' "we" the
chapter's only first person plural, NO IMPERATIVE, NO "IF" (the three cases on "when"), thirteen consecutive perfects, one wayyiqtol, no divine frame, Moses never
named, Israel once; THE PARSER: one number verse (13:13 [1]), no starred token; THE INSTRUMENT'S TWO SLIPS asserted (the tagger's "Np" substring, the bare number check
inside "swore"); ONKELOS: "the fear of" supplied at 13:5 twice and 13:11, "accept" for hearken four times, "the errors of the peoples" four times, the Memra at 13:5
and 13:19, "a fabrication" for rebellion (the two Torah seats), "the wife of your covenant", "he counsels you", "sons of wickedness", "a ruined mound", "finished" for
wholly, "He established" for swore, "well" at all five seats of "diligently", the same letters read two ways at 13:3 and 13:14. THE COST RULES: one run to the clean
point #202 after the ledger, THE RUN PAST THE CAP BY /context (651.7k where the counter had shown far less — the rows the heavy half; the next reading in two halves
or the clean point before the ledger), the owner's compaction, the tail on a small context — the patch, the manifest, the seat, the fast steps in the foreground before
the freeze, the chain in the background with the writers typed during its run; EVERY STEP TIMED — the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)} wall time from {T_START};
the table in the map's AS BUILT. THE CAUTIONS: the piska that runs past the chapter; the English's three citation slips and its dropped Leviticus at 89:3; the two
files dividing 190 differently; the driver's launch from the scratchpad. THE LESSONS (thirteen, in the map): a piska's boundary is not a chapter's; the ink green
first pass with the launch from the repo root; a substring test on a code is a test of nothing; the cap by /context; the English's slips asserted; the two files'
division; the form's name protected in every shell; the fast steps in the foreground; the kin by computation the first instrument; the purge formula's first seat;
a proscription for every prescription; the store carries the ketiv; every step timed. OWED TO 11b: the prophet's test with two parameters, the header's not-adding,
the inciter's table and the court's rule inverted, the condemned city's decision table with the seven inquiries and the property table, the effects (the purge, the
anger, the mercy), the run citations (the cloud, the oath), the kin by call, chapter 14's split of piska 96, the register's rows, the series DE, the docket.
'''

STEPS = f'''DEUTERONOMY — SITTING 11 — CHAPTER 13, Deuteronomy 13:1-19 ({DATE}, on Brian's "Go" after the reread; World/step9/DEUTERONOMY_WALK.md "Sitting 11" and "Sitting 11
— AS BUILT"; a reading sitting is one run to a clean point, then the tail after the compaction). Chapter 13 is the chapter of the seducers: first the header — all
the word that I command you, keep it, add nothing to it and take nothing from it; then three cases that open the same way. A prophet or a dreamer gives a sign, and
the sign comes true, and he says "let us go after other gods" — do not listen, the LORD is testing you; that prophet dies. Your brother, your son, your daughter,
the wife of your bosom, your friend who is as your own soul entices you in secret with the same words — do not consent, do not pity, do not shield him; your hand is
on him first, then everyone's, and he is stoned; all Israel hears and fears. You hear that men of no worth have drawn a whole city after other gods — inquire,
search, ask thoroughly, and if it is true, put the city to the sword, burn it and everything in it as a whole offering, leave it a heap forever, and keep nothing of
it, so that the LORD turns from His anger and shows you mercy. Then the footer: when you listen to His voice and do what is right in His eyes. The Sifrei has fifteen
sections on the chapter, one of them with no opening verse and placed by its own words, and one that runs past the chapter's end into the next — those four rows
were left for chapter 14; every row was read whole in both files, with six more rows from elsewhere. Laying each verse beside every verse of the Bible and counting
the shared words showed the chapter's shape: the header's "add nothing, take nothing" has exactly one twin in the Bible, the plural form in chapter 4; the seducers'
sentence is one formula said three times, each case the other cases' nearest kin; "purge the evil from your midst", which the book will say nine times, is said here
for the first time; and the verse about inquiring "thoroughly" is the source the tradition uses to teach every capital court its seven questions. The tradition also
reads the header as a rule of the whole chapter: every "keep" is a prohibition beside every "do". The chapter is frozen as one unit, the 227th, the world's standing
facts up by six as predicted, its hash unmoved, every gate green. The run stopped at a clean point after the ledger — it had already passed the 600k cap when the
context was read, a lesson for the next reading — you compacted, and the rest ran on a small context: the display patch, the claims, the seat, the gates in the
background while the records were typed. Every step was timed: the machine's own work came to {mmss(T_MACH)} in a sitting of {mmss(T_TOTAL)}; the rest was the reading and
the typing. Next: the commit on your word; then the compile of chapter 13 in two runs — the prophet's test and the inciter's hand as cells with their parameters, the
condemned city's decision table, the purge as an effect — or the ten-commandments schema first.


'''

BRIEF = f'''- **CHAPTER 13 READ AND FROZEN — THE SEDUCERS' ONE SENTENCE SAID THREE TIMES; "ADD NOTHING, TAKE NOTHING" WITH EXACTLY ONE TWIN IN THE BIBLE; "PURGE THE EVIL FROM YOUR MIDST" SAID HERE FOR THE FIRST OF NINE TIMES; THE VERSE THAT TEACHES EVERY CAPITAL COURT ITS SEVEN QUESTIONS; A SECTION THAT RUNS PAST THE CHAPTER'S END; AND THE RUN THAT PASSED THE CAP** ({DATE}; sitting 11, one run to a clean point and its tail; the ledger deu_13_reeh_{LDATE}.md — {L_ALL} sources, every row whole; the 227th unit; every gate green; the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)}).
'''
BRIEF_ENTRY = f'''### {DATE} — CHAPTER 13 READ: ONE SENTENCE THREE TIMES, THE HEADER'S ONE TWIN, THE PURGE'S FIRST SEAT, AND A SECTION THAT RUNS PAST THE CHAPTER

Chapter 13 is three cases with the same sentence in them: a prophet with a
sign, a brother in secret, a whole city drawn away — and each says "let us go
and serve other gods which you have not known." Laid beside every verse of the
Bible, each case is the other two cases' nearest kin; nothing else in the
Bible says it. The header, "add nothing to it and take nothing from it," has
exactly one twin — the plural form in chapter 4 — and the tradition reads it
three ways at once: not a word added to the priests' blessing, not a fifth
species to the four, not a fourth application of blood to the three. The
sentence "purge the evil from your midst," which the book will say nine times,
is said here for the first time, and the tradition names what it removes: the
doer. The verse that tells the court to inquire "thoroughly" about the city is
the verse from which every capital court learns its seven questions. And the
Sifrei's last section on the chapter keeps going into chapter 14 — its last
four rows open with the next chapter's words, so they were left unread for
chapter 14's sitting; a section's edge is not a chapter's. The chapter is
frozen as one unit, every gate green. The run stopped at a clean point after
the ledger; the context, when read, had already passed the 600k cap — the rows
are the heavy half of a reading, and the next one will take the spine in two
halves. Brian compacted, and the rest ran on a small context with the gates in
the background while the records were typed. Every step was timed: the
machine's own work came to {mmss(T_MACH)} in a sitting of {mmss(T_TOTAL)}.

'''

RESUME_NOTE = f'''# ⚠ THE DEUTERONOMY WALK sitting 11 ({DATE}; step9/DEUTERONOMY_WALK.md "Sitting 11" + "Sitting 11 — AS BUILT"): CHAPTER 13 READ AND FROZEN as ONE unit
# (deu_13_seducers, the 227th; standing 2245, hash unmoved) — THE SEDUCERS' ONE FORMULA AT THREE CASES (13:3, 7, 14 each other's closest kin), the header's twin 4:2
# (the only two seats of "not add nor take away"), "purge the evil from your midst" at its first seat of nine, the seven inquiries from 13:15, a proscription for
# every prescription (82:2, 85:3), the ketiv at 13:16 in the store; the ledger deu_13_reeh_{LDATE}.md ({L_ALL} sources, every row whole; piska 88 headless; piska 96's
# rows 9-12 left for chapter 14); six claims seated; the fold +{DJ} on the journal ({J_ROWS} rows); every gate green. A READING SITTING UNDER THE COST RULES, EVERY STEP
# TIMED (the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)}; the run past the cap by /context — the table in the AS BUILT). NEXT on the owner's word: the commit
# (<scratch>/commit_msg_ch13.txt); then 11b — the compile of chapter 13 (the three cases as cells with their parameters; DE the next series).
'''

STATE = f'''
#202 ADDENDUM 1 ({DATE}, at the close of THE DEUTERONOMY WALK sitting 11 — CHAPTER 13's READING: THE TAIL after the compaction at #202, on the owner's "Reread" and "Go" — A CLEAN COMPACTION POINT): THE TAIL AS RUN on a small context: the rereads (the recovery page, the map's "Sitting 11 … THE DESIGN", MEMORY.md, the state doc's #202 and its READY line); ch13_patch_overrides.py derived from the chapter-12 form by twelve asserted substitutions (derive_ch13_patch.py), the yaml +{OV_REF13} by reference and +34 by gloss ({OV_REF} / {OV_GL}); the ink rerun PATCHED (0 failing — its third pass; {N_INK} asserts, green on all three); write_ch13_manifest.py (six claims DV13-01..06 at 13:1, 2, 7, 13, 17, 19 — the spine distributed by piska from the CITE INDEX itself, the headless 88 with the inciter's piskaot, piska 96 split at its own rows, the six outside rows with the claims whose verses they cite; every he_contains cut from the store's bytes — the six checks "you shall not add" 13:1, "is testing" 13:4, "entices you" 13:7, "diligently" 13:15, "wholly" 13:17, "the right" 13:19); seat_ch13.py; ch13_chain.sh, ch13_fold.sh and ch13_gates.sh derived from chapter 12's forms with the form's name protected in every shell (derive_ch13_shells.py — lesson 12 applied, nothing retyped); THE FAST STEPS IN THE FOREGROUND — the manifest (every cite index name used), verify_claims (6/0) and the labels census ({LN}) read before the freeze; THE CHAIN LAUNCHED IN THE BACKGROUND (ch13_gates.sh — the seat, verify_text {VT_STEPS} steps / {VT_SCEN} scenarios, the ritual {N_PASS} PASS, the fold 226 → 227 / 2239 → 2245 with the hash unmoved, build_world, the journal gate {J_ROWS} rows (+{DJ} since 10b's chain), the register gate --strict DECLARED {R_DECL} / DEBT {R_DEBT} / FAILS {R_FAIL}, large_letter {LL[-3:]}, the home gate) — {CHAIN_NOTE}; the records writer and the copier typed during the chain's run, the notification the wake; THE RECORDS from the sheet in one call (write_ch13_records.py — the map's "Sitting 11 — CHAPTER 13 — AS BUILT" with thirteen lessons AND THE TIMING TABLE (computed from ch13_timing.tsv: the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)} from {T_START}; the chain's inner steps {CS_TXT}), COMPILE_DEBT's sitting-11 box (a)-(l) — 11b's docket as designed AND chapter 14's split of piska 96, MIDDOT's chapter-13 block with the codes censused from the ledger's rows ({CODE_TXT}), MISHNAH_TOPICS (eleven heads routed to 11b), RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the scoreboard bullet and an entry), World/RESUME.md, this addendum, the addenda §57, the recovery page (section 2 under its cap), the memory (the walk note and the index line under 17,000), the stamp row, THE COMMIT MESSAGE <scratch>/commit_msg_ch13.txt); the forms copied (copy_ch13_forms.py). THE TREE: + logic/units/deu_13_seducers.yaml frozen (operators, step E, the anchor scenarios), logic/py_units/deu_13_seducers.py and ALL_UNITS.py (the ritual), logic/oral_audit/manifests/deu_13_seducers_claims.json, logic/oral_triage/deu_13_reeh_{LDATE}.md, logic/glosses/word_gloss_overrides.yaml, logic/corpus/CORPUS_TRUTH.py (227 / 2245), corpus_world.sqlite, World/journal/data/world.sqlite (the fold layer, gitignored), the records, the forms. NOT COMMITTED (since 2b0c9c8): SITTING 11 — ONE message at <scratch>/commit_msg_ch13.txt for the owner's word ("Commit" = no push; "commit push" = both). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. THE MEASURE OF THE RUN: /context read 651.7k at #202 (past the 600k cap — the rows the heavy half; the lesson in the AS BUILT). NEXT ON THE RULING: the commit on his word; then CHAPTER 13's COMPILE (11b) in two runs + the tail under the cost rules (RUN A the rereads, the measurements, the design — the three cases as cells with the sign's status, the death's mode and the festival's timing as PARAMETERS, the condemned city's decision table, the purge the effect's first seat, the checkpoint series DE — and the docket by the union rule, its own run past ~700 rows; RUN B the types, the runner, the tape, the chain LAUNCHED; the tail the records) — or the Decalogue-schema sitting first; on the table: the chain's positions step at four workers, the SUPPLIED forms, the calf's day marker, the registry's homograph, the receipt's third and fourth shapes, THE INSTALL HYPOTHESIS, the eras table's merge. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 11 — CHAPTER 13 — AS BUILT" (the newest section), MEMORY.md.
'''

ADDENDA = f'''
## §57 — THE DEUTERONOMY WALK sitting 11 ({DATE}): CHAPTER 13 READ AND FROZEN — the state doc's #202 and its addendum 1; the map's "Sitting 11 — CHAPTER 13 … THE DESIGN" and "Sitting 11 — CHAPTER 13 — AS BUILT"; the owner: "Go" (a reading sitting under THE COST RULES), "Get ready to compact", "Reread" and "Go" after the compaction at #202
THE READING: Onkelos Deuteronomy 13 whole (19 = 19, the identity; the English's 12:32 the DB's 13:1); THE SIFREI ON THE CHAPTER A FIFTH TIME — piskaot 82-96, fourteen
heading on the chapter and 88 without a head citation folded in on its consonants, {L_SPINE} rows read whole in both files ({N_REREAD} read before and reread whole, found by
computation); PISKA 96's ROWS 9-12 ON 14:1 LEFT FOR CHAPTER 14 (never read ahead; asserted on the rows' bytes); six rows outside the spine by the union of both files
(117:3, 149:1-2, 189:1, 190:7-8), none excluded; the kin credited by name from twenty ledgers; the unit deu_13_seducers the 227th (standing 2245, hash unmoved); the
ledger {L_ALL} sources (Onkelos MATERIAL {L_OM} / CONTEXT {L_OC}; the spine MATERIAL {L_SM} / CONTEXT {L_SC}; the outside rows MATERIAL {L_XM} / CONTEXT {L_XC}); six claims 6/0 seated at
13:1, 2, 7, 13, 17, 19; the display layer +{OV_REF13} by reference, +34 by gloss; every gate green in one chain (ch13_gates.sh, in the background; the manifest, the verifier
and the labels census in the foreground before it). THE ONE RUN AND ITS TAIL: the measurements (the kin by computation beside the law kin named), the ink (GREEN ON ITS
FIRST TYPED PASS — the one red the driver's launch from the scratchpad), the design, the rows (three spine files, the Onkelos file, the outside file — every cut held),
the ledger (clean on its first run), the clean point #202 — /context 651.7k, PAST THE 600k CAP (the counter had shown far less; the rows the heavy half); the owner's
compaction; the tail on "Reread" and "Go" — the patch, the manifest, the seat, the shells with the form's name protected, the chain launched with the writers typed
during its run, the records, the forms, the message. EVERY STEP TIMED: the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)} from {T_START} — the table in the map's AS BUILT. THE
FINDS: THE HEADER'S TWIN 4:2 (the only two seats of "not add nor take away"), read at the word's, the count's and the rite's grain; A PROSCRIPTION FOR EVERY
PRESCRIPTION (82:2, 85:3); THE SEDUCERS' ONE FORMULA AT THREE CASES; the dream's noun and verb only at the chapter's three seats; "is testing" the participle's one
seat; THE SIGN DISPUTED — a PARAMETER; THE FIRST VERB THE CLOUD; THE DEATH'S MODE BY ANALOGY — a PARAMETER; "PURGE THE EVIL" AT ITS FIRST SEAT OF NINE; "entice" the
Torah's one token; THE INCLUSION TABLE with the father in "as your own soul"; THE FIVE PROHIBITIONS against standing duties; THE COURT'S RULE INVERTED; THE HAND FIRST
17:7's twin; TWO VERBS OF STONING; "all Israel shall hear and fear" the first of four — the festival's execution a PARAMETER; ONE CITY [1] and Jerusalem excluded by
"to dwell there"; SONS OF BELIAL the Torah's two; THE SEVEN INQUIRIES at three seats; the four infinitive absolutes; THE KETIV AT 13:16 in the store; THE PROPERTY
TABLE; "wholly", "a heap forever", "not built again" with Samuel's, Ai's and Tyre's; JERICHO the run's case; the anger keyed to idolatry; THE MERCY TWO-ARMED; "as He
swore" the AS_WHEN form; the footer the blessing's opening and the header's sentence; the register (no imperative, no "if", the seducers' "we"). THE LESSONS
(thirteen, in the map): a piska's boundary is not a chapter's; the ink green first pass; a substring test on a code; THE CAP BY /context; the English's slips asserted;
the two files' division; the form's name protected; the fast steps in the foreground; the kin by computation; the purge's first seat; a proscription for every
prescription; the store carries the ketiv; every step timed. OWED TO 11b (COMPILE_DEBT's box (a)-(l)): the prophet's test, the header's not-adding, the inciter, the
condemned city, the effects, the run citations, the kin by call, never-read-ahead's cells, chapter 14's split of piska 96, the register's rows, the series DE, the
docket. The records on the sheet; the forms in World/step9/forms_deuteronomy_walk/ (copy_ch13_forms.py).
'''

MEMPAR = f'''
SITTING 11 DONE {DATE} ("Go" after the reread; "Get ready to compact" at #202; "Reread" and "Go" after the compaction; the map's "Sitting 11" and "Sitting 11 — AS
BUILT"): CHAPTER 13 READ AND FROZEN as ONE unit deu_13_seducers (the 227th; standing 2245 = 2239 + 6 as predicted, hash unmoved; no portion edge) in ONE run to the
clean point after the ledger + THE TAIL after the compaction, every row whole — Onkelos 19 rows (the identity), THE SIFREI ON THE CHAPTER A FIFTH TIME (piskaot 82-96,
{L_SPINE} rows in both files; 88 WITHOUT A HEAD folded in on its consonants; 96:9-12 ON 14:1 LEFT FOR CHAPTER 14; {N_REREAD} reread whole, found by computation), six outside rows,
the kin credited by name from twenty ledgers; the ledger deu_13_reeh_{LDATE}.md ({L_ALL} sources, clean on its first run); six claims 6/0 seated at 13:1, 2, 7, 13, 17, 19;
every gate green; the display layer +{OV_REF13} / +34. THE FINDS: THE HEADER'S TWIN 4:2 — the only two seats of "not add nor take away", the shelf reading it at the
word's, the count's and the rite's grain (82:3-5); A PROSCRIPTION FOR EVERY PRESCRIPTION (82:2, 85:3 — 11b's rule); THE SEDUCERS' ONE FORMULA AT THREE CASES (13:3, 7,
14 each other's closest kin); THE SIGN DISPUTED and THE DEATH'S MODE BY ANALOGY — two PARAMETERS (84:1-2; 86:6, 90:2); THE FIRST VERB THE CLOUD (85:1 — a run citation
inside a law); "PURGE THE EVIL FROM YOUR MIDST" AT ITS FIRST SEAT OF NINE (86:10 — the doer removed, 11b's effect); THE INCLUSION TABLE (87:4-11); THE COURT'S RULE
INVERTED (89:6-7); THE FESTIVAL'S EXECUTION a PARAMETER (91:1-2); ONE CITY [1], Jerusalem excluded (92:3, 92:5); THE SEVEN INQUIRIES at three seats (93:6, 149:1,
190:7 — I2); THE KETIV AT 13:16 in the store (329 vs 328); THE PROPERTY TABLE; JERICHO the run's case; the anger keyed to idolatry, the mercy two-armed (96:3-4); "as
He swore" the AS_WHEN form (13:18, 19:8); the footer the blessing's opening. ⚠ LESSONS (thirteen, in the map): A PISKA'S BOUNDARY IS NOT A CHAPTER'S (chapter 14's dump
splits 96); THE INK GREEN FIRST PASS — a scratch script with ROOT from git RUNS FROM THE REPO ROOT; A SUBSTRING TEST ON A CODE IS A TEST OF NOTHING; THE CAP BY /context
(651.7k at the clean point — the rows the heavy half; the next reading in two halves or the clean point before the ledger); the English's slips asserted; the two
files' division of 190; the form's name protected in every shell; THE FAST STEPS IN THE FOREGROUND BEFORE THE FREEZE, the chain behind; the kin by computation; the
purge's first seat; the proscription rule; the store's ketiv; EVERY STEP TIMED — the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)}. OWED TO 11b: the three cases as cells
with their parameters, the condemned city's decision table, the effects, the run citations (the cloud, the oath), the kin by call, chapter 14's split of 96, the
register's rows; DD the last series (DE next). UNCOMMITTED since 2b0c9c8: sitting 11 (ONE message at <scratch>/commit_msg_ch13.txt). NEXT on the ruling: the commit;
then 11b, two runs + the tail.
'''
MEMLINE_OLD_START = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — '
MEMLINE_NEW = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — map World/step9/DEUTERONOMY_WALK.md; ch 1-12 COMPILED, PUSHED 2b0c9c8; ch 13 READ AND FROZEN (sitting 11, one run + the tail, timed; uncommitted); NEXT: the commit, then 11b\n'
DESC_OLD = "COMMITTED AND PUSHED THROUGH 2b0c9c8 (2026-09-21) — SITTING 10b DONE 2026-09-21 ("
DESC_NEW = f"COMMITTED AND PUSHED THROUGH 2b0c9c8 (2026-09-21) — SITTING 11 DONE {DATE} (chapter 13 READ AND FROZEN as one unit, the 227th — the seducers' one formula at three cases, the header's twin 4:2, the purge formula's first seat, the piska that runs past the chapter; one run + the tail under the cost rules, every step timed, the run past the cap by /context; uncommitted; 11b next) — SITTING 10b DONE 2026-09-21 ("
REC2_OLD_START = '## 2. WHERE IT STANDS'
REC2_NEW = f'''## 2. WHERE IT STANDS ({DATE}, after sitting 11; the state doc #202 addendum 1 the newest)
- NUMBERS CLOSED. DEUTERONOMY 1:1-12:31 COMPILED AND ON THE TAPE (PUSHED through 2b0c9c8); 13 READ AND FROZEN.
- {C_UNITS} frozen units, standing 2245, hash 8b8fff1fa28953af. 67 runners, 72 daemons, 491 functions; 1150 kinds / 1049 effects.
- THE TAPE at RUN (1323, 96, 88, 0, 12, 1626, 43, 319, pairs, 127), markers 172, closes 127; the sweep 66/66; every gate GREEN.
- SITTING 11 (ch 13, one run + the tail, EVERY STEP TIMED; the run past the cap by /context): the seducers' one formula at three
  cases; the header's twin 4:2; the purge's first seat; {L_ALL} sources whole; piska 96:9-12 are 14:1's (chapter 14 splits it).
- UNCOMMITTED since 2b0c9c8: sitting 11 (<scratch>/commit_msg_ch13.txt). NEXT ON HIS WORD: the commit; then 11b.

'''
A_REC6 = '- Deuteronomy\'s sittings: the map; the addenda §31-54 (§39 the whole-row rule). The cost cuts: §35, §45, §47, §53.'
A_REC6_NEW = '- Deuteronomy\'s sittings: the map; the addenda §31-57 (§39 the whole-row rule). The cost cuts: §35, §45, §47, §53.'
TOP = {
 '**34. Mishnah, Courts**': f' — 7:10, 7:6, 10:4-6, 11:1, 11:4-6, 5:1-2, 1:5, 4:1 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 11, chapter 13\'s reading: the inciter\'s concealed witnesses 13:7-12 at 87-89 (Sanhedrin 67a), the acts of honor 13:12 at 91:4, the condemned city 13:13-18 at 92-96 (Sanhedrin 111b-113b), the false prophet\'s death 13:6 at 86:6 (Sanhedrin 89a-90a), the seven inquiries 13:15 at 93:6-9 (Sanhedrin 40a-41a), one city 13:13 at 92:3, the festival\'s execution 13:12 at 91:1-2 (Sanhedrin 89a), the verdict returned 13:10 at 89:6-7; the docket at 11b)',
 '**35. Mishnah, Lashes**': f' — 1:4-6 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 11, chapter 13\'s reading: the plotting witness\'s a fortiori for the prophet\'s death 13:6 at 86:3; the docket at 11b)',
 '**41. Mishnah, Animal Offerings**': f' — 8:10 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 11, chapter 13\'s reading: the mixed bloods given in one application from "you shall not add" 13:1 at 82:3; Zevachim 80a-81b; Tosefta Zevachim 8:23; the docket at 11b)',
 '**17. Mishnah, Booth**': f' — 3:4 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 11, chapter 13\'s reading: the four species not added to 13:1 at 82:4; Sukkah 34b; the docket at 11b)',
 '**42. Mishnah, Grain Offerings**': f' — Menachot 41b-42a ROUTED {DATE} (THE DEUTERONOMY WALK sitting 11, chapter 13\'s reading: the fringes not added to 13:1 at 82:4; the docket at 11b)',
 '**19. Mishnah, New Year**': f' — Rosh Hashanah 28b ROUTED {DATE} (THE DEUTERONOMY WALK sitting 11, chapter 13\'s reading: the priests\' blessing not added to 13:1 at 82:5; Eruvin 96a, Sanhedrin 88b; the docket at 11b)',
 '**38. Mishnah, Idolatry**': f' — 3:9 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 11, chapter 13\'s reading: the devoted thing\'s benefit carried to the Salt Sea 13:18 at 96:2; Avodah Zarah 49b-50a; the docket at 11b)',
 '**32. Mishnah, Middle Gate**': f' — Bava Metzia 59b ROUTED {DATE} (THE DEUTERONOMY WALK sitting 11, chapter 13\'s reading: the prophet\'s sign not decisive 13:2-4 at 84:1-2; the docket at 11b)',
 '**24. Mishnah, Levirate Marriage**': f' — Yevamot 90b ROUTED {DATE} (THE DEUTERONOMY WALK sitting 11, chapter 13\'s reading: the prophet\'s temporary uprooting "His voice obey" 13:5 at 85:4; the docket at 11b)',
 '**31. Mishnah, First Gate**': f' — Tosefta Bava Kamma 9:30 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 11, chapter 13\'s reading: the mercy two-armed 13:18 at 96:4; Shabbat 151b; the docket at 11b)',
 '**39. Mishnah, Fathers (ethics)**': f' — 2:1, 3:9, 3:14 ROUTED {DATE} (THE DEUTERONOMY WALK sitting 11, chapter 13\'s reading: the light commandment as the weighty 13:1 and 13:19 at 82:1, 96:7; the docket at 11b)',
}

CM = f'''CHAPTER 13 READ AND FROZEN (SITTING 11 — A READING SITTING UNDER THE COST RULES: ONE RUN TO A CLEAN POINT, THE COMPACTION, THE TAIL; EVERY ROW WHOLE; EVERY STEP TIMED) — THE SEDUCERS' ONE SENTENCE SAID THREE TIMES (THE PROPHET WITH THE SIGN, THE BROTHER IN SECRET, THE CITY DRAWN AWAY — EACH CASE THE OTHERS' CLOSEST KIN), "ADD NOTHING, TAKE NOTHING" WITH EXACTLY ONE TWIN IN THE BIBLE (4:2), "PURGE THE EVIL FROM YOUR MIDST" AT ITS FIRST SEAT OF NINE, THE VERSE THAT TEACHES EVERY CAPITAL COURT ITS SEVEN QUESTIONS, A PROSCRIPTION FOR EVERY PRESCRIPTION, THE PISKA THAT RUNS PAST THE CHAPTER'S END, THE KETIV THE STORE CARRIES, AND THE RUN THAT PASSED THE CAP BY /context.

On the owner's words "Go" (the one run, after the reread that followed 10b's compaction), "Get ready to compact" (at the clean point #202), "Reread" and "Go" (the tail, after the compaction), {DATE}; World/step9/DEUTERONOMY_WALK.md "Sitting 11 — CHAPTER 13 … THE DESIGN" and "Sitting 11 — CHAPTER 13 — AS BUILT"; the state doc's #202 and its addendum 1; the addenda §57. THE READING: Deuteronomy 13:1-19 with Onkelos whole (the export's 19 rows the DB's 19 — the identity, asserted; the English's 12:32 the DB's 13:1, no row of the shelf citing 12:32) and THE SIFREI ON DEUTERONOMY ON THE CHAPTER A FIFTH TIME — piskaot 82-96, fourteen heading on the chapter's verses and ONE WITHOUT A HEAD CITATION (88 on 13:8's "of the gods of the peoples round about you") folded in on its consonants, {L_SPINE} rows READ WHOLE in both files ({N_REREAD} read before at sitting 1 and a Genesis sitting and REREAD WHOLE — the prior reads found by computation), PISKA 96's LAST FOUR ROWS LEFT FOR CHAPTER 14 (96:9 opens with 14:1's citation, 96:10-12 with its clauses — never read ahead; asserted on the rows' own bytes; chapter 14's split recorded in COMPILE_DEBT), six rows outside the spine citing the chapter read whole (Belial at 15:9 — the English's "(Dt.13:4)" a wrong verse and the Hebrew right; the inquiry at 17:4 twice; the rebellion at 19:16; the inquiry at 19:17-18 twice — the two files dividing piska 190's rows differently), none excluded, the kin credited by name with the counts computed from twenty ledgers (Exodus 22:19 the ban's first seat; 32:1-8 the calf's "these are your gods"; Leviticus 20:2, 20:27 and 24:14-23 the stonings; 27:28-29 the devoted thing; Numbers 12:6, 15:30-36, 21:2-3, 25:4; Deuteronomy 4:2, 5:6, 6:13-14, 7:2-26, 8:2-16, 9:26, 10:20, 11:22-28, 12:25-28 — no Onkelos row of Genesis 22:1, Genesis 37 or Exodus 20:2, and NONE OF DEUTERONOMY 14-20 OR THE PROPHETS in any ledger, asserted: never read ahead); frozen as ONE unit deu_13_seducers (the 227th; no portion edge inside it — Re'eh holds it whole), standing 2245 = 2239 + 6 as predicted, hash 8b8fff1fa28953af unmoved; the ledger logic/oral_triage/deu_13_reeh_{LDATE}.md ({L_ALL} sources — Onkelos {L_ONK}: MATERIAL {L_OM} / CONTEXT {L_OC}; the spine {L_SPINE}: MATERIAL {L_SM} / CONTEXT {L_SC}; the outside rows {L_OUT}: MATERIAL {L_XM} / CONTEXT {L_XC}; coverage computed, lint 0, no cut missed — written clean on its first run); six claims DV13-01..06 verified 6/0 (the spine distributed by piska from the CITE INDEX itself; piska 96 split at its own rows), the labels census green, seated as six WITNESS_READ operators at 13:1, 2, 7, 13, 17, 19 with step E; the ritual {N_PASS} PASS; the display layer +{OV_REF13} by reference and +34 by gloss under the sitting's marker. THE FINDS: THE HEADER'S TWIN IS 4:2 — "you shall not add to it nor take from it" the singular here and the plural there, THE ONLY TWO SEATS of the clause (seven tokens in order), the shelf reading it at the word's grain (82:5 — not a word of 1:11 added to the priests' blessing), the count's (82:4 — the four species and the fringes, both edges barred) and the rite's (82:3 — the mixed bloods, Mishnah Zevachim 8:10); A PROSCRIPTION FOR EVERY PRESCRIPTION — R. Eliezer son of Jacob's rule at the header and at the six verbs (82:2, 85:3 — "keep" the prohibition's verb, "do" the command's: the compile's rule that each positive cell carries its negative); THE SEDUCER'S ONE FORMULA — "let us go (and serve) other gods which you have not known" at 13:3, 13:7, 13:14, each the others' closest kin by computation ("let us go" the cohortative nine in the Torah; "other gods" forty-six in the Bible); THE DREAM'S NOUN AND VERB in the book only at the chapter's three seats; "IS TESTING" the participle's one seat (Genesis 22:1 the first; the sign in the heavens and the wonder on the earth — 83:4-5); THE SIGN DISPUTED — granted true and barred anyway (R. Yose the Galilean) or a fallen prophet's standing, Hananiah's (R. Akiva; 189:1 his sentence): a PARAMETER; THE FIRST VERB IS THE CLOUD (85:1 — the march after the cloud, a run citation of the tape's Numbers 9-10 lines inside a law), "His voice obey" the voice of His prophets (85:4); THE DEATH'S MODE BY ANALOGY run both ways (86:6, 90:2 — stoning from "thrusting"; R. Shimon strangling): a PARAMETER, its reason the a fortiori from the plotting witness (86:3); "AND YOU SHALL PURGE THE EVIL FROM YOUR MIDST" NINE SEATS IN THE BIBLE, ALL IN THE BOOK, 13:6 THE FIRST — the doer removed (86:10); "ENTICE" THE TORAH'S ONE TOKEN of eighteen (Jezebel's and Saul's the shelf's two senses — 87:1-2); THE INCITER'S KIN AN INCLUSION TABLE with the father found in "as your own soul" (87:4-11); "the wife of your bosom", "your friend as your own soul", "the son of your mother" one seat each; 6:14's clause SPELLED DEFECTIVE at 13:8; THE FIVE PROHIBITIONS OF 13:9 each against a standing duty (89:1-5 — the neighbor's love, the enemy's ass, the neighbor's blood, the defense, the silence), "spare" the Torah's two with Saul's order at 1 Samuel 15:3 the third; THE COURT'S RULE INVERTED (89:6-7 — convicted not brought back to acquit, acquitted brought back to convict); THE HAND FIRST — 17:7's "the hand of the witnesses" the twin (seven tokens in order), "afterward" the Torah's two seats both this clause; TWO VERBS OF STONING in the Torah (Deuteronomy's at 13:11, 17:5, 22:21, 22:24; Leviticus's and Numbers' at Molech's giver, the necromancer, the blasphemer, the wood-gatherer; 21:21 alone holding both) and the stones and the stone one rite (90:1); "ALL ISRAEL SHALL HEAR AND FEAR" the formula's first of four with the paragogic nun — the festival's execution a PARAMETER of timing (91:1-2); THE FIFTEEN UTTERANCES (91:3) and the honors of an idol not capital (91:4); "IN ONE OF YOUR CITIES" THE CHAPTER'S ONE NUMBER VERSE [1] given its rule — one city, not three (92:3), JERUSALEM EXCLUDED by "to dwell there" THE TORAH'S ONE SEAT (92:5), the border excluded (93:3); SONS OF BELIAL the Torah's two (13:14, 15:9 — 117:3's analogy), Naboth's witnesses the closest verse, "without a yoke" (93:2); THE ONE NARRATIVE VERB inside the third case; THE SEVEN INQUIRIES FROM THE CHAPTER — "diligently, diligently" at three seats (93:6; 149:1; 190:7), 17:4 the twin with nine of twelve tokens in order, the two examinations' two rules (93:8-9 — Mishnah Sanhedrin 5:1-2); THE INFINITIVE ABSOLUTES FOUR (kill, diligently, smite, devote — "by any means", 94:1; the design's three corrected at the print); THE KETIV AT 13:16 — "that city" with the masculine written for the feminine read, the feminine never written in the Torah and written in the Prophets, THE STORE CARRYING BOTH FORMS (329 tokens against the DB's 328), the shelf quoting the read form; THE PROPERTY TABLE (94:4-5, 95:1 — Mishnah Sanhedrin 10:5) and Heaven's spoil (95:4-5 — Mishnah 10:6); "WHOLLY TO THE LORD" 13:17 and Samuel's lamb, the word the priest's meal offering's; "A HEAP FOREVER" Ai's and "not built again" Tyre's — JERICHO THE RUN'S CASE read by Joshua's oath (95:6-7, 96:1); the devoted thing's benefit to the Salt Sea (96:2 — Mishnah Avodah Zarah 3:9); "FROM THE FIERCENESS OF HIS ANGER" — Achan's valley says the words back (Joshua 7:26), the anger keyed to idolatry's presence (96:3); THE MERCY TWO-ARMED (96:4); "AS HE SWORE TO YOUR FATHERS" (13:18) the AS_WHEN form, 19:8 its twin — a run citation for 11b's census, the register's finder finding no receipt in the chapter (measured); THE FOOTER THE BLESSING'S AND THE CURSE'S OPENING (28:1 fourteen tokens in order, 28:15 twelve, 15:5 eleven) and "to do the right in the eyes of the LORD" Jehoshaphat's measure; THE FOOTER THE HEADER'S SENTENCE (82:1, 96:7 — the light commandment as the weighty); THE REGISTER: singular but for the prophet's case (13:4-5 plural — the six verbs), the seducers' "we" the chapter's only first person plural, NO IMPERATIVE, NO "IF" (the three cases on "when"), thirteen consecutive perfects, one wayyiqtol, no divine frame, Moses never named, Israel once; THE PARSER: one number verse (13:13 [1]), no starred token; THE INSTRUMENT'S TWO SLIPS asserted as slips (the tagger's "Np" substring inside "VNp"; the bare number check inside "swore"); ONKELOS: "the fear of" supplied at 13:5 twice and at 13:11, "accept" for hearken four times, "the errors of the peoples" four times, the Memra at 13:5 and 13:19, "a fabrication" for rebellion at the two Torah seats, "the wife of your covenant", "he counsels you", "sons of wickedness", "a ruined mound", "finished" for wholly, "He established" for swore, "well" at all five seats of "diligently", the same letters read two ways at 13:3 and 13:14 — Onkelos with the tagger. EVERY GATE GREEN IN ONE CHAIN (ch13_gates.sh, in the background; the manifest, verify_claims 6/0 and the labels census in the foreground before it — the fast steps read before the freeze; the summary read once): the seat, verify_text ({VT_STEPS} steps, {VT_SCEN} scenarios), the ritual {N_PASS} PASS, CORPUS TRUTH GREEN before and after the bake ({C_UNITS} units, {C_FACTS} facts, {C_DEM} demands, hash unmoved), build_world ALL GREEN, the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — +{DJ} on the fold layer since 10b's chain, the tape unmoved), the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — no receipt, header or footer in chapter 13), large_letter_probes {LL[-3:]}, the home-path gate GREEN; the ink {N_INK} asserts — GREEN ON ITS FIRST TYPED PASS and on the second and third (the one red print the driver's launch from the scratchpad, no git root there — a launch, not a fact). THE COST RULES ON A READING SITTING: the one run to the clean point #202 after the rows and the ledger — /context read 651.7k there, PAST THE 600k CAP where the turn counter had shown far less (the rows' typing the heavy half of a reading run: the next reading takes the spine in two halves with the rows typed after each, or plans the clean point before the ledger); the owner's compaction; the tail on a small context — the display patch (twelve asserted substitutions, the anchors walked never typed), the manifest, the seat, the three shells derived with the form's name protected in every one (chapter 12's lesson 12 applied), the fast steps in the foreground before the freeze, the chain launched behind with the records writer and the copier typed during its run. EVERY STEP TIMED (the table in the map's AS BUILT, computed from ch13_timing.tsv): the machine's share {mmss(T_MACH)} of {mmss(T_TOTAL)} wall time from {T_START} to the records; the chain {mmss(CS_TOTAL)} ({CS_TXT}); the rest the reading, the typing and one compaction. THE LESSONS (thirteen, in the map's AS BUILT): a piska's boundary is not a chapter's; the ink green on its first typed pass and the launch from the repo root; a substring test on a code is a test of nothing; the 600k cap passed by /context, not by the counter; the English's slips asserted, not corrected; the two files divide a piska's rows differently again; the form's name protected in every shell; the fast steps in the foreground, the slow chain in the background; the kin by computation the reading's first instrument; the purge formula's first seat; a proscription for every prescription; the store carries the ketiv; every step timed. Also in this commit: COMPILE_DEBT's sitting-11 box (a)-(l) owed to the compile 11b (the prophet's test with the sign's status and the death's mode as parameters, the header's not-adding, the inciter's table and the court's rule inverted with the festival's timing a parameter, the condemned city's decision table with the seven inquiries and the property table, the effects — the purge, the anger, the mercy — the run citations of the cloud and the oath, the kin by call, the cells owed to never-read-ahead, CHAPTER 14's SPLIT OF PISKA 96, the register's rows, the series DE, the docket), MIDDOT's chapter-13 block (the codes censused from the ledger's rows — {CODE_TXT}), MISHNAH_TOPICS' row notes (Courts 7:10, 7:6, 10:4-6, 11:1, 11:4-6, 5:1-2, 1:5, 4:1; Lashes 1:4-6; Animal Offerings 8:10; Booth 3:4; Grain Offerings 41b-42a; New Year 28b; Idolatry 3:9; Middle Gate 59b; Levirate Marriage 90b; First Gate Tosefta 9:30; Fathers 2:1, 3:9, 3:14 — routed to 11b), RESEARCH_LOG's entry, THE_STEPS, THE_BRIEFING (the scoreboard and an entry), World/RESUME.md, the state doc's #202 with its addendum 1, the recovery page rewritten under its cap, the addenda §57, the stamp row, the memory, the forms in World/step9/forms_deuteronomy_walk/ (the one run's and the tail's scripts and prints — the derivations, the dump, the measurement, the split, the ink and its parts, the five row files, the ledger writer, the design and clean-point writers, the display patch and its derivation, the manifest, the seat, the three shells and their derivation, the timer and its table, the records, the copy).

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
A_RESUME = '# ⚠ THE DEUTERONOMY WALK sitting 10b — CHAPTER 12 COMPILED AND ON THE TAPE (2026-09-21; step9/DEUTERONOMY_WALK.md "Sitting 10b"'
A_SCORE = '## SCOREBOARD (as of 2026-09-20, latest)\n'
A_BULLET = '- **CHAPTER 12 COMPILED — THE PLACE INSTALLED WITH THE ERAS TABLE\'S OWN INK'
A_ENTRY = '### 2026-09-21 — CHAPTER 12 COMPILED: THE PLACE READS ITS OWN TABLE, THE SLAUGHTER LAW BECOMES A STATUS, AND THE RITE IS A PARAMETER'
A_MIDDOT = '\n## Exodus block campaign — owner\'s word "Do 3")\n'
ANCH = [(f'{ROOT}/World/RESUME.md', A_RESUME), (f'{ROOT}/THE_STEPS.md', '\n## Step 6 — Publish\n'), (f'{ROOT}/THE_BRIEFING.md', A_SCORE), (f'{ROOT}/THE_BRIEFING.md', A_BULLET), (f'{ROOT}/THE_BRIEFING.md', A_ENTRY), (f'{ROOT}/logic/MIDDOT.md', A_MIDDOT), (RECP, REC2_OLD_START), (RECP, '\n## 3. THE STANDING LAWS'), (RECP, A_REC6), (f'{MEM}/deuteronomy-walk.md', DESC_OLD), (f'{MEM}/MEMORY.md', MEMLINE_OLD_START)]
for p, a in ANCH: assert rd(p).count(a) == 1, (p, a[:40], rd(p).count(a))
tl = rd(TOPICS).split('\n'); assert all(sum(l.startswith(t) for l in tl) == 1 for t in TOP) and 'sitting 11, chapter 13' not in rd(TOPICS)
assert '## Sitting 11 — CHAPTER 13 — AS BUILT' not in rd(WALKP) and '## Sitting 11 — CHAPTER 13, Deuteronomy 13:1-19' in rd(WALKP) and '#202 ADDENDUM 1' not in rd(TOUCH[1]) and 'COMPACTION POINT #202' in rd(TOUCH[1]) and '## §57' not in rd(TOUCH[9]) and '## §56' in rd(TOUCH[9]) and 'SITTING 11 DONE' not in rd(f'{MEM}/deuteronomy-walk.md') and 'SITTING 11 — CHAPTER 13' not in rd(TOUCH[5]) and f'## {DATE} — DEUTERONOMY 13 READ' not in rd(TOUCH[6]) and 'CASE LAW ON CHAPTER 13' not in rd(TOUCH[7])
assert CHAIN_NOTE != 'CHAIN_NOTE_PLACEHOLDER', 'the chain note is typed from the summary before the records are written'
s = rd(RECP); i = s.index(REC2_OLD_START); j = s.index('\n## 3. THE STANDING LAWS'); REC_NEW = s[:i] + REC2_NEW + s[j:]
REC_NEW = REC_NEW.replace(A_REC6, A_REC6_NEW)
assert len(REC_NEW.encode()) <= 10240, len(REC_NEW.encode())
m = rd(f'{MEM}/MEMORY.md'); i = m.index(MEMLINE_OLD_START); j = m.index('\n', i) + 1; MEM_NEW = m[:i] + MEMLINE_NEW + m[j:]
assert len(MEM_NEW.encode()) < 17000, len(MEM_NEW.encode())
CMP = f'{SP}/commit_msg_ch13.txt'; assert not os.path.exists(CMP) or CHECK, CMP
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
