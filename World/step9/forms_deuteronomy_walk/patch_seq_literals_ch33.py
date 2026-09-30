import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 21b (2026-09-29; LEAN): the sequence file's literals and checkpoints for chapter 33 — the import line (the live registration edge), the
# DAEMON_ORDER entry, RUN (predicted in the design: +11 events, +W writes with W READ FROM THE RUNNER'S NARRATIVE PRINT, +1 daemon fired, timers fired +0 — no clock
# word in the blessing, the tape's first print decides; the rest unmoved), PREVIOUS_RUN (20b's RUN EXACTLY — no declared delta), NEWEST_RUNNER, PLACEMENT and CENSUS READ FROM
# THE STITCHER'S PRINT (seq_stitch_ch33.out — the eleven own-day lines in two forms after the tape's last Deuteronomy 32 line; NO MARKER — markers 173 UNMOVED), the
# DO1-DO5 block after DN5 + the VERDICTS entries (the D series' fifteenth name — five checkpoints, the lean block). Every replacement anchored on the exact prior text's
# head (the comment tails kept); the readback's census and writes READ from the runner's print and its part 5, never typed; the twin literals READ from the runner's print;
# the file asserted to compile after. patch_seq_literals_ch32.py's form WITHOUT THE MARKER AND WITHOUT A REUSE. RUN FROM THE REPO ROOT.
import re, ast, subprocess, sys, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch33b_spec as S
P = ROOT + '/World/step9/cold_run_sequence.py'
s = open(P, encoding='utf-8').read()
assert 'import cold_run_blessing_of_moses' not in s, 'already patched'
def rep_head(old_head, new_head):
    """the line whose HEAD is old_head gets new_head in its place — the comment tail kept verbatim (the prior sitting's line follows the new comment)"""
    global s
    i = s.index('\n' + old_head) + 1; assert s.count('\n' + old_head) == 1, (s.count('\n' + old_head), old_head[:80])
    s = s[:i] + new_head + s[i + len(old_head):]
W = 'THE DEUTERONOMY WALK 21b (2026-09-29; LEAN)'
# 0. THE PRINTS — the placement and the census read from the stitcher's, the writes' count and the readback's census from the runner's print, the rows' writes from part 5
pr = open(SP + '/seq_stitch_ch33.out', encoding='utf-8').read()
PLACEMENT = ast.literal_eval(re.search(r'^PLACEMENT LITERAL: (.*)$', pr, re.M).group(1))
CENSUS = ast.literal_eval(re.search(r'^  CENSUS tuple .*?: (\(.*\))$', pr, re.M).group(1))
RUNF = sorted([f for f in os.listdir(SP) if re.match(r'ch33_runner_run\d+\.out$', f)])[-1]
run_out = open(SP + '/' + RUNF, encoding='utf-8').read()
NARR = ast.literal_eval(re.search(r'^THE NARRATIVE: (\(.*?\)) \(the twenty-eight on twelve ledgers', run_out, re.M).group(1)); WN = NARR[0]
RBG = ast.literal_eval(re.search(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: 29 rows — (\{.*?\});', run_out, re.M).group(1))
NPAR = int(re.search(r'the parameters (\d+) \(in the registry', run_out).group(1))
TWIN = ast.literal_eval(re.findall(r'^THE TWINS DIFFED \(printed before they are asserted\): (\{.*\})$', run_out, re.M)[-1])   # the runner's own print — the last (the callees' prints precede it)
p5 = open(SP + '/ch33_part5.py', encoding='utf-8').read()
ROWS = re.findall(r"^    rb\('(Deut \d+:\d+)', \".*?\", '([A-Z]+)', .*?(?:, write='([a-z_]+)')?(?:, state=True)?(?:, pointer=\{.*?\})?\),\n", p5, re.M)
assert len(ROWS) == 29, len(ROWS)
SUP = [v for v, g, w_ in ROWS if g == 'SUPPLIED']; WRITES = [(v, w_) for v, g, w_ in ROWS if w_]
TAPE_ROWS = re.findall(r"^    rb\('(Deut \d+:\d+)', .*?tape_kind='(\w+)', tape_verse='([^']+)'", p5, re.M)
NCELL = len(re.findall(r"^    rb\('Deut \d+:\d+', .*?cell='", p5, re.M))
MK_PRED = {'text_constrained': 108, 'reading_placed': 50}   # the design's arithmetic: NO MARKER — 20b's placement EXACTLY; the events' classes READ FROM THE PRINT
print('PLACEMENT read:', PLACEMENT, '| markers predicted:', MK_PRED); print('CENSUS read:', CENSUS); print('the writes W read from the narrative:', WN, '| the narrative:', NARR, '| the readback census read:', RBG, '| SUPPLIED', len(SUP), SUP, '| writes', len(WRITES), '| tape rows', len(TAPE_ROWS), '| cells', NCELL, '| parameters', NPAR, '| the twins', {k: TWIN[k] for k in ('33:16 vs Gen 49:26', '33:1 vs 4:44', '33:13 vs Gen 49:25', '33:1 vs Josh 14:6')})
assert PLACEMENT['markers'] == MK_PRED, ('THE MARKERS\' PLACEMENT MOVED FROM THE DESIGN — read the stitcher\'s print', PLACEMENT['markers'], MK_PRED)
assert sum(PLACEMENT['events'].values()) == 1439 + 11, ('THE EVENTS\' PLACEMENT — the eleven lines', PLACEMENT['events'])
assert CENSUS[2] == 1450 and CENSUS[9] == 173, ('THE CENSUS MOVED FROM THE DESIGN — read the stitcher\'s print', CENSUS)   # on the tape 1439 -> 1450 (the eleven lines), markers 173 UNMOVED (NO MARKER); the rest READ
assert WN == 28 and NARR[7] == 0, (WN, NARR)   # the twenty-eight writes on twelve ledgers — twenty-eight first entries, no reuse (the design's twenty-eight; the print decides); NO marker
assert len(SUP) == 11 and len(WRITES) >= 11 and len(TAPE_ROWS) >= 8 and NPAR == 16 and NCELL == 29, (len(SUP), len(WRITES), len(TAPE_ROWS), NPAR, NCELL)
# 1. the import line — the live edge the dependency gate reads
i = s.index('import cold_run_song_charge_nebo   # THE DEUTERONOMY WALK 20b'); j = s.index('\n', i)
s = s[:j + 1] + "import cold_run_blessing_of_moses   # %s: chapter 33 (Deut 33:1-29) in ONE runner over one unit — THE BLESSING (the man of God and the theophany, the law the inheritance and the king in Jeshurun, Reuben and Judah, Levi, Benjamin, Joseph, Zebulun and Issachar, Gad — the lioness and the lawgiver's portion (Moses' grave FORWARD to 34:6), Dan, Naphtali and Asher, the rider of the heaven, Israel dwelling alone); ELEVEN own-day lines IN TWO FORMS (1 act, 10 speeches) ALL at Moses' last day (40, 12, 7) — NO MARKER (19b's at 31:1); the daemon law_blessing_of_moses given_at Deut 33:1, installed_by boot; 39 CALL edges all reference; THE TWO POINTER ROWS 33:5 and 33:28 (20b's owed pointers PAID); DEUTERONOMY_WALK.md \"Sitting 21b\"\n" % W + s[j + 1:]
# 2. DAEMON_ORDER
i = s.index("    ('cold_run_song_charge_nebo', 'law_song_charge_nebo'),   # THE DEUTERONOMY WALK 20b"); j = s.index('\n', i)
s = s[:j + 1] + "    ('cold_run_blessing_of_moses', 'law_blessing_of_moses'),   # %s; DEUTERONOMY_WALK.md \"Sitting 21b\": chapter 33 — ELEVEN lines in TWO FORMS (moses_blessed_israel_before_his_death 33:1 the act; blessing_prologue_law_and_king_declared 33:3, blessing_reuben_and_judah_declared 33:6, blessing_levi_declared 33:8, blessing_benjamin_declared 33:12, blessing_joseph_declared 33:13, blessing_zebulun_and_issachar_declared 33:18, blessing_gad_declared 33:20, blessing_dan_naphtali_asher_declared 33:22, blessing_rider_of_the_heaven_declared 33:26, blessing_israel_dwells_alone_declared 33:28 — the speeches) — ALL on MOSES' LAST DAY (40, 12, 7), NO MARKER); 28 writes on twelve ledgers (Israel 10, reuben 1, judah 1, levi 4, benjamin 1, joseph 3, zebulun 1, issachar 1, gad 2, dan_son 1, naphtali 1, asher 2 — twenty-eight new, no reuse)\n" % W + s[j + 1:]
# 3. RUN — the design's prediction with W read (timers fired 94 + F — F predicted 0, the tape's first print decides)
rep_head("RUN = (1439, 102, 94, 0, 12, 2048, 53, 319,   # THE DEUTERONOMY WALK 20b",
         "RUN = (1450, 102, 94, 0, 12, %d, 54, 319,   # %s: PREDICTED in DEUTERONOMY_WALK.md \"Sitting 21b\" (THE PREDICTION'S ARITHMETIC) BEFORE the run — events +11 (the eleven own-day lines in two forms), timers set +0 (no clock word in the blessing), timers fired +0 (NO MARKER — the clock does not walk; the tape's first print decides), cancels 0, retro-writes 12 UNMOVED, writes +%d (READ FROM THE RUNNER'S NARRATIVE PRINT — twenty-eight first entries on twelve ledgers, no reuse), daemons fired +1 (law_blessing_of_moses), entities 319 UNMOVED (israel_people and the tribes' fathers on the registry already — dan_son Dan's); sitting 20b's line follows:   # THE DEUTERONOMY WALK 20b" % (2048 + WN, W, WN))
rep_head("       127)   # THE DEUTERONOMY WALK 20b (2026-09-28; LEAN): 127 UNMOVED",
         "       127)   # %s: 127 UNMOVED — no close this sitting (the twenty-eight statuses have no closer, no block, no heaven entry; the commission's debit on Moses stands OPEN to 34:1-4); sitting 20b's line follows:   # THE DEUTERONOMY WALK 20b (2026-09-28; LEAN): 127 UNMOVED" % W)
# 4. PREVIOUS_RUN — 20b's RUN EXACTLY, no declared delta
rep_head("PREVIOUS_RUN = (1423, 102, 94, 0, 12, 2003, 52, 319,   # THE DEUTERONOMY WALK 20b",
         "PREVIOUS_RUN = (1439, 102, 94, 0, 12, 2048, 53, 319,   # %s: sitting 20b's RUN EXACTLY, read at the design (DEUTERONOMY_WALK.md \"Sitting 21b\", THE PREDICTION'S ARITHMETIC): THE REST drops chapter 33's eleven lines (inside the declared span [[Deut,33,1,29]]) and their daemon's writes; sitting 20b's line follows:   # THE DEUTERONOMY WALK 20b" % W)
rep_head("       127)   # THE DEUTERONOMY WALK 20b (2026-09-28; LEAN): sitting 19b's 127",
         "       127)   # %s: sitting 20b's 127 — no close this sitting, THE REST keeps 20b's; sitting 20b's line follows:   # THE DEUTERONOMY WALK 20b (2026-09-28; LEAN): sitting 19b's 127" % W)
# 5. NEWEST_RUNNER
rep_head("NEWEST_RUNNER = 'song_charge_nebo'   # THE DEUTERONOMY WALK 20b",
         "NEWEST_RUNNER = 'blessing_of_moses'   # %s: chapter 33's eleven own-day lines in two forms (after the tape's last Deuteronomy 32 line; NO MARKER; inside the declared span [[Deut,33,1,29]]) the newest joined (was 'song_charge_nebo'); THE REST drops the newest runner's lines and its daemon's writes; sitting 20b's line follows:   # THE DEUTERONOMY WALK 20b" % W)
# 6. PLACEMENT — READ at the stitcher's print (the markers' class asserted above; the events' classes the print's)
rep_head("PLACEMENT = {'markers': {'text_constrained': 108, 'reading_placed': 50}, 'events': {'text_constrained': 110, 'page_order': 1270, 'reading_placed': 59}}   # THE DEUTERONOMY WALK 20b",
         "PLACEMENT = %r   # %s: READ at the stitcher's print (scratchpad seq_stitch_ch33.out) — NO MARKER: the markers' placement 20b's EXACTLY (text_constrained 108, reading_placed 50); the events' classes the print's (the eleven lines at a marked day); sitting 20b's line follows:   # THE DEUTERONOMY WALK 20b" % (PLACEMENT, W))
# 7. THE VERDICTS entries — the D series' fifteenth name (five — the lean block)
old_v = "            'DN1 MATCH', 'DN2 MATCH', 'DN3 MATCH', 'DN4 MATCH', 'DN5 MATCH',   # THE DEUTERONOMY WALK 20b"
i = s.index(old_v); j = s.index('\n', i)
s = s[:j + 1] + "            'DO1 MATCH', 'DO2 MATCH', 'DO3 MATCH', 'DO4 MATCH', 'DO5 MATCH',   # %s: chapter 33's five — the D series' fifteenth name, the lean block over one chapter and one unit with NO MARKER and NO REUSE\n" % W + s[j + 1:]
# 8. CENSUS — read from the stitcher's print; the prior line found by its head (its tuple read from the file, never typed)
m = re.search(r"^CENSUS = (\(.*?\))   # THE DEUTERONOMY WALK 20b \(2026-09-28; LEAN\): READ from the stitcher's print", s, re.M); assert m, 'the CENSUS line'
OLD_CENSUS = ast.literal_eval(m.group(1)); assert OLD_CENSUS[2] == 1439 and OLD_CENSUS[9] == 173, OLD_CENSUS
s = s[:m.start()] + ("CENSUS = %r   # %s: READ from the stitcher's print (scratchpad seq_stitch_ch33.out) after chapter 33's ELEVEN lines joined after the last Deuteronomy 32 line with NO MARKER — on the tape 1439 -> 1450 AS THE DESIGN PREDICTED, markers 173 UNMOVED, the rest the print's; sitting 20b's line follows:   # THE DEUTERONOMY WALK 20b (2026-09-28; LEAN): READ from the stitcher's print" % (CENSUS, W)) + s[m.end():]
# 9. THE DO BLOCK — five checkpoints after DN5 (the lean block; the literals from the design, the runner's print and its part 5)
OWN28 = list(S.NEW_EFFECTS); KINDS11 = list(S.KINDS)
SUBJ = {e: sub for l in S.LINES for e, _, sub in l[7]}   # each new effect's ledger
FIRSTS = tuple((l[1], sub) for l in S.LINES for _, _, sub in l[7]); assert len(FIRSTS) == 28
import yaml as _yaml; _FX = _yaml.safe_load(open(ROOT + '/World/step9/effect_vocabulary.yaml', encoding='utf-8'))['effects']; BLOCKS = [e for e in OWN28 if _FX[e]['ledger_op'] == 'block']; HEAVEN = [e for e in OWN28 if _FX[e]['ledger_op'] == 'heaven']; assert len(BLOCKS) == 0 and len(HEAVEN) == 0 and len(KINDS11) == 11
KIN47 = tuple(S.KIN_UNMOVED); KIN_EXPECTED = tuple(S.KIN_UNMOVED[k] for k in KIN47); assert S.REUSES == []
TW = (TWIN['33:16 vs Gen 49:26'], TWIN['33:1 vs 4:44'], TWIN['33:13 vs Gen 49:25'], TWIN['33:1 vs Josh 14:6'])
DO = '''    # ---- THE DEUTERONOMY WALK 21b (2026-09-29; LEAN; DEUTERONOMY_WALK.md "Sitting 21b" THE CHECKPOINTS DO1-DO5): chapter 33's eleven own-day lines in two forms with NO MARKER and NO REUSE — the D series' fifteenth name, the lean block over one chapter ----
    CP_KINDS = %(KINDS11)r; OWN28_CP = %(OWN28)r; SUBJ_CP = %(SUBJ)r
    ev_cp = [(i, l) for i, l in enumerate(w.log) if l[0] == 'EVENT' and l[2]['kind'] in CP_KINDS]
    i_last_d32 = max(i for i, l in enumerate(w.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 32:'))
    mk_cp = [l for l in markers if str(l[2].get('verse', '')).startswith('Deut 33:')]
    cp('DO1 THE LINES — eleven events on the tape AFTER the tape\\'s last Deuteronomy 32 line, in the ink\\'s order (33:1, 33:3, 33:6, 33:8, 33:12, 33:13, 33:18, 33:20, 33:22, 33:26, 33:28), no dated field; ALL on MOSES\\' LAST DAY (40, 12, 7) — 19b\\'s ONE MARKER at 31:1, NO MARKER in this chapter (33:1\\'s before his death THAT day): markers 173 UNMOVED, no Deuteronomy 33 marker; the lines\\' day by the exodus era\\'s date', ([k for k in CP_KINDS], True, 0, 0, [], 173, [(40, 12, 7)]), ([l[2]['kind'] for _, l in ev_cp], all(i > i_last_d32 for i, _ in ev_cp), sum(1 for _, l in ev_cp if l[2].get('dated') is not None), len(mk_cp), [l[2]['verse'] for l in mk_cp], len(markers), sorted({ex.date(l[1]) for _, l in ev_cp})))
    FV_cp = (lambda t_: '%%s %%d:%%d' %% t_ if isinstance(t_, tuple) else str(t_))
    def LGx_cp(ent): return w.entities[ent].ledger if ent in w.entities else []
    n28_cp = tuple(len([e for e in LGx_cp(SUBJ_CP[eff]) if e['effect'] == eff]) for eff in OWN28_CP); src_cp = tuple((FV_cp(WE.first_verse(str([e for e in LGx_cp(SUBJ_CP[eff]) if e['effect'] == eff][0].get('case_source', '')))), SUBJ_CP[eff]) if [e for e in LGx_cp(SUBJ_CP[eff]) if e['effect'] == eff] else None for eff in OWN28_CP)
    def _nall_cp(eff): return sum(1 for ent in w.entities.values() for e in ent.ledger if e['effect'] == eff)
    blocks_cp = sum(1 for eff in OWN28_CP for ent in w.entities.values() for e in ent.ledger if e['effect'] == eff and e.get('op') == 'block'); heaven_cp = sum(1 for eff in OWN28_CP for ent in w.entities.values() for e in ent.ledger if e['effect'] == eff and e.get('op') == 'heaven'); dd_cp = yaml.safe_load(open(os.path.join(HERE, 'daemon_dispositions.yaml'), encoding='utf-8'))
    cp('DO2 THE WRITES — the twenty-eight NEW ONE each on their subjects with their lines\\' first verses (10 on israel_people — 33:1, 33:1, 33:1, 33:3, 33:3, 33:3, 33:26, 33:26, 33:28, 33:28; reuben 33:6, judah 33:6, levi 33:8 four, benjamin 33:12, joseph 33:13 three, zebulun 33:18, issachar 33:18, gad 33:20 two, dan_son 33:22, naphtali 33:22, asher 33:22 two — the sons\\' own ledgers); NO reuse; no block; no heaven entry; law_blessing_of_moses registered, given_at Deut 33:1, installed_by boot; the eleven cells and the table WRAPPED (twelve)', (tuple((1, v) for v in %(FIRSTS)r), 0, 0, True, 'Deut 33:1', 'boot', 12), (tuple(zip(n28_cp, src_cp)), blocks_cp, heaven_cp, 'law_blessing_of_moses' in dd_cp['daemons'], dd_cp['daemons'].get('law_blessing_of_moses', {}).get('given_at'), dd_cp['daemons'].get('law_blessing_of_moses', {}).get('installed_by'), sum(1 for v in dd_cp['functions'].get('blessing_of_moses', {}).values() if v.get('status') == 'WRAPPED')))
    RB_cp = cold_run_blessing_of_moses.READBACK; EVk_cp = [l[2] for l in events]
    found_tape_cp = sum(1 for r_ in RB_cp if r_['tape_kind'] and any(e['kind'] == r_['tape_kind'] and WE.first_verse(e.get('case_source')) == WE.first_verse(r_['tape_verse']) for e in EVk_cp))
    by_call_cp = sum(1 for r_ in RB_cp if r_['cell'] and r_['cell_found']); sup_cp = [r_ for r_ in RB_cp if r_['grade'] == 'SUPPLIED']
    cp('DO3 THE READBACK — THE FORMS ON FILE, NO NEW FORM: the_readback\\'s rows TWENTY-NINE, one per verse (the census from the runner\\'s print: %(RBGS)s), every reference row\\'s entry FOUND: %(NTAPE)d on the tape by kind and first verse (Sinai\\'s descent, the law written and delivered, the testament twice, the sentence at Meribah, the calf\\'s sword, the bush, the crossed hands, the poor law, the young men\\'s offering, Isaac\\'s blessing), the rows in the kin\\'s cells by CALL %(NCELL)d, every cell found; the SUPPLIED rows %(NSUP)d — the eleven lines\\' first verses; NO STATE ROW; THE TWO POINTER ROWS 33:5 and 33:28 (20b\\'s owed pointers PAID, grade R); no open row, no stretch, no retrograde row; 33:21 and 33:29 FORWARD', (29, %(NTAPE)d, %(NCELL)d, %(NSUP)d, [], ['Deut 33:5', 'Deut 33:28'], 0, 0), (len(RB_cp), found_tape_cp, by_call_cp, len(sup_cp), [r_['verses'] for r_ in RB_cp if r_['state']], [r_['verses'] for r_ in RB_cp if r_['pointer']], sum(1 for r_ in RB_cp if r_['open']), sum(1 for r_ in RB_cp if r_['stretch'])))
    CRm = cold_run_blessing_of_moses
    cp('DO4 THE KIN AND THE READBACK\\'S GROUND — the forty-seven references\\' counts as the recon and the callees read them (barred_from_the_land 2 — Moses\\' and Aaron\\'s, gathered_to_his_people 5, counted 22, hand_opening_commanded 1, blessed_with_dew_and_fat 1, shield_promised 1, slain_by_sword 2, heaven_and_earth_witness 5, high_places_banned 3, kings_smitten 3, land_possessed 6 among them — no second write, NO REUSE); the twins diffed (33:16/Genesis 49:26, 33:1/4:44, 33:13/Genesis 49:25, 33:1/Joshua 14:6 — read from the runner\\'s print); THE PARSER\\'S FALSE SEVEN at 33:23 — no number, one mark: no count in the world; the scans\\' ground (the runner\\'s HOLE_SCAN empty at import)', (%(KINEXP)r, %(TW)r, [], 1, True), (tuple(_nall_cp(k) for k in %(KIN47)r), (CRm.TWIN['33:16 vs Gen 49:26'], CRm.TWIN['33:1 vs 4:44'], CRm.TWIN['33:13 vs Gen 49:25'], CRm.TWIN['33:1 vs Josh 14:6']), CRm.PARSE[(33, 23)][0], len(CRm.PARSE[(33, 23)][2]), CRm.HOLE_SCAN is None or all(v_ == [] for v_ in CRm.HOLE_SCAN.values())))
    cp('DO5 THE REST — entities 319 UNMOVED (israel_people and the tribes\\' fathers on the registry already, dan_son Dan\\'s), closes 127 UNMOVED, the population table 148 UNMOVED, the eleven kinds present in two forms (10 speech, 1 act), markers 173 (NO MARKER — 19b\\'s at 31:1 stands); the span\\'s one range and the 39 edges on file, OWED pointers 0 in the file, the calendar UNTOUCHED (75 parameters; the_death_date_of_moses 19b\\'s, exercised by covenant_return_charge alone); the other counts 20b\\'s exactly with the eleven lines and the daemon\\'s writes added (RUN above)', (319, 127, 148, True, (10, 1), 173, 1, True, 0, 75, ['covenant_return_charge']), (len(w.entities), len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')]), len(w.tables['population']), all(k in {l[2]['kind'] for l in events} for k in CP_KINDS), tuple([yaml.safe_load(open(os.path.join(HERE, 'event_vocabulary.yaml'), encoding='utf-8'))['events'][k]['form'] for k in CP_KINDS].count(f_) for f_ in ('speech', 'act')), len(markers), len(yaml.safe_load(open(os.path.join(HERE, 'dependency_dispositions.yaml'), encoding='utf-8'))['spans']['blessing_of_moses']), sum(1 for e in yaml.safe_load(open(os.path.join(HERE, 'dependency_dispositions.yaml'), encoding='utf-8'))['edges'] if e['from'] == 'blessing_of_moses') >= 39, sum(1 for p in yaml.safe_load(open(os.path.join(HERE, 'dependency_dispositions.yaml'), encoding='utf-8'))['pointers'] if p.get('disposition') == 'OWED'), len(WE.CAL_PARAMS), WE.CAL_PARAMS['the_death_date_of_moses']['exercised_by']))
''' % dict(KINDS11=KINDS11, OWN28=OWN28, SUBJ=SUBJ, FIRSTS=FIRSTS, RBGS=', '.join('%s %d' % kv for kv in RBG.items()), NTAPE=len(TAPE_ROWS), NCELL=NCELL, NSUP=len(SUP), KINEXP=KIN_EXPECTED, KIN47=KIN47, TW=TW)
anchor = "    print('    the story\\'s dates: Moses born %r"
assert s.count(anchor) == 1, s.count(anchor)
s = s.replace(anchor, DO + anchor)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched: import, DAEMON_ORDER, RUN (writes +%d read), PREVIOUS_RUN (no declared delta), NEWEST_RUNNER, PLACEMENT (read %r), VERDICTS DO, CENSUS (read %r), DO1-DO5 (the readback census %r, %d supplied, %d writes, %d tape rows, %d cells read from the print and part 5; %d parameters; the twins %r); compiles' % (WN, PLACEMENT, CENSUS, RBG, len(SUP), len(WRITES), len(TAPE_ROWS), NCELL, NPAR, TW))
