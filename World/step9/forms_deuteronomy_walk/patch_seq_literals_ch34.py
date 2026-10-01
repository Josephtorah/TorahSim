import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22b (2026-09-30; LEAN): the sequence file's literals and checkpoints for chapter 34 — the import line (the live registration edge), the
# DAEMON_ORDER entry, RUN (predicted in the design: +6 events, +W writes with W READ FROM THE RUNNER'S NARRATIVE PRINT, +1 daemon fired, timers set +0 and fired +0 — the
# thirty days a duration, the thirty days' row written without a due; the tape's first print decides), PREVIOUS_RUN (21b's RUN EXACTLY — no declared delta), NEWEST_RUNNER, PLACEMENT and
# CENSUS READ FROM THE STITCHER'S PRINT (seq_stitch_ch34.out — the six own-day lines in two forms after the tape's last Deuteronomy 33 line; NO MARKER — markers 173 UNMOVED), the
# DP1-DP5 block after DO5 + the VERDICTS entries (the D series' sixteenth name — five checkpoints, the lean block). Every replacement anchored on the exact prior text's
# head (the comment tails kept); the readback's census and writes READ from the runner's print and its part 5, never typed; the twin literals READ from the runner's print; the
# receipt's class READ from the register file AFTER patch_register_ch34.py retyped it from the gate's print; the file asserted to compile after. patch_seq_literals_ch33.py's form
# WITH THREE REUSES AND WITHOUT A MARKER. RUN FROM THE REPO ROOT.
import re, ast, subprocess, sys, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch34b_spec as S
P = ROOT + '/World/step9/cold_run_sequence.py'
s = open(P, encoding='utf-8').read()
REG_ONLY = '--registration' in sys.argv   # THE SPLIT (22b's find): the sequence file's import asserts DAEMON_ORDER against daemon_dispositions.yaml — the register gate, the probes and every reader importing it need the import line and the DAEMON_ORDER entry BEFORE the stitcher; the rest of the literals after the stitcher's print
REGISTERED = 'import cold_run_moses_death' in s
assert not (REG_ONLY and REGISTERED), 'the registration already patched'
assert REG_ONLY or REGISTERED, 'the registration first (--registration), the literals after the stitcher'
def rep_head(old_head, new_head):
    """the line whose HEAD is old_head gets new_head in its place — the comment tail kept verbatim (the prior sitting's line follows the new comment)"""
    global s
    i = s.index('\n' + old_head) + 1; assert s.count('\n' + old_head) == 1, (s.count('\n' + old_head), old_head[:80])
    s = s[:i] + new_head + s[i + len(old_head):]
W = 'THE DEUTERONOMY WALK 22b (2026-09-30; LEAN)'
if REG_ONLY:
    # 1. the import line — the live edge the dependency gate reads
    i = s.index('import cold_run_blessing_of_moses   # THE DEUTERONOMY WALK 21b'); j = s.index('\n', i)
    s = s[:j + 1] + "import cold_run_moses_death   # %s: chapter 34 (Deut 34:1-12) in ONE runner over one unit — THE DEATH OF MOSES, THE BOOK'S LAST (the ascent and the land shown, the oath and the denial, the death and the burial, the years and the thirty days, Joshua and the receipt, the prophet, the signs and the terror); SIX own-day lines IN TWO FORMS (5 acts, 1 speech of the LORD) ALL at Moses' last day (40, 12, 7) — NO MARKER (19b's at 31:1; the thirty days a DURATION, the counter unmoved); the daemon law_moses_death given_at Deut 34:1, installed_by boot; 20 CALL edges all reference; THE THREE POINTER ROWS 34:4, 34:5, 34:6 (the song's two and the blessing's owed pointers PAID); THREE REUSES at their own forward seats; THE RECEIPT 34:9 re-declared from the gate's print; DEUTERONOMY_WALK.md \"Sitting 22b\"\n" % W + s[j + 1:]
    # 2. DAEMON_ORDER
    i = s.index("    ('cold_run_blessing_of_moses', 'law_blessing_of_moses'),   # THE DEUTERONOMY WALK 21b"); j = s.index('\n', i)
    s = s[:j + 1] + "    ('cold_run_moses_death', 'law_moses_death'),   # %s; DEUTERONOMY_WALK.md \"Sitting 22b\": chapter 34 — SIX lines in TWO FORMS (moses_went_up_to_nebo_and_saw_the_land 34:1, moses_died_and_was_buried 34:5, moses_hundred_and_twenty_israel_wept_thirty_days 34:7, joshua_full_of_the_spirit_israel_hearkened 34:9, no_prophet_like_moses_declared 34:10 — the acts; oath_land_shown_not_crossed_declared 34:4 — the LORD's speech) — ALL on MOSES' LAST DAY (40, 12, 7), NO MARKER; 15 writes on three ledgers (moses 8, israel_people 6, yehoshua 1 — twelve new statuses, three reuses: the denial a heaven entry, the gathering a status, the thirty days' timer row written without a due) — THE BOOK'S LAST DAEMON\n" % W + s[j + 1:]
    open(P, 'w', encoding='utf-8').write(s)
    import py_compile; py_compile.compile(P, doraise=True)
    print('patched (--registration): the import line and the DAEMON_ORDER entry — the live registration edge and the daemon order the sequence file asserts at import; the rest of the literals after the stitcher'); sys.exit(0)
# 0. THE PRINTS — the placement and the census read from the stitcher's, the writes' count and the readback's census from the runner's print, the rows' writes from part 5, the receipt's class from the register file
pr = open(SP + '/seq_stitch_ch34.out', encoding='utf-8').read()
PLACEMENT = ast.literal_eval(re.search(r'^PLACEMENT LITERAL: (.*)$', pr, re.M).group(1))
CENSUS = ast.literal_eval(re.search(r'^  CENSUS tuple .*?: (\(.*\))$', pr, re.M).group(1))
RUNF = sorted([f for f in os.listdir(SP) if re.match(r'ch34_runner_run\d+\.out$', f)])[-1]
run_out = open(SP + '/' + RUNF, encoding='utf-8').read()
NARR = ast.literal_eval(re.search(r'^THE NARRATIVE: (\(.*?\)) \(the twelve on three ledgers', run_out, re.M).group(1)); WN = NARR[0]
RBG = ast.literal_eval(re.search(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: 12 rows — (\{.*?\});', run_out, re.M).group(1))
NPAR = int(re.search(r'the parameters (\d+) \(in the registry', run_out).group(1))
TWIN = ast.literal_eval(re.findall(r'^THE TWINS DIFFED \(printed before they are asserted\): (\{.*\})$', run_out, re.M)[-1])   # the runner's own print — the last (the callees' prints precede it)
p5 = open(SP + '/ch34_part5.py', encoding='utf-8').read()
ROWS = re.findall(r"^    rb\('(Deut \d+:\d+)', \".*?\", '([A-Z]+)', .*?(?:, write='([a-z_]+)')?(?:, state=True)?(?:, pointer=\{.*?\})?\),\n", p5, re.M)
assert len(ROWS) == 12, len(ROWS)
SUP = [v for v, g, w_ in ROWS if g == 'SUPPLIED']; WRITES = [(v, w_) for v, g, w_ in ROWS if w_]
TAPE_ROWS = re.findall(r"^    rb\('(Deut \d+:\d+)', .*?tape_kind='(\w+)', tape_verse='([^']+)'", p5, re.M)
NCELL = len(re.findall(r"^    rb\('Deut \d+:\d+', .*?cell='", p5, re.M))
import yaml as _yaml
_RG = _yaml.safe_load(open(ROOT + '/World/step9/register_dispositions.yaml', encoding='utf-8')); RCLASS = _RG['receipts']['Deut 34:9']['class']
assert 'THE DEUTERONOMY WALK 22b' in _RG['receipts']['Deut 34:9']['why'], 'the receipt at 34:9 RE-DECLARED first (patch_register_ch34.py from the gate\'s print — the class AS THE GATE HOLDS IT, the stale why removed)'
MK_PRED = {'text_constrained': 108, 'reading_placed': 50}   # the design's arithmetic: NO MARKER — 21b's placement EXACTLY; the events' classes READ FROM THE PRINT
print('PLACEMENT read:', PLACEMENT, '| markers predicted:', MK_PRED); print('CENSUS read:', CENSUS); print('the writes W read from the narrative:', WN, '| the narrative:', NARR, '| the readback census read:', RBG, '| SUPPLIED', len(SUP), SUP, '| writes', len(WRITES), '| tape rows', len(TAPE_ROWS), '| cells', NCELL, '| parameters', NPAR, '| the receipt\'s class', RCLASS, '| the twins', {k: TWIN[k] for k in ('34:4 vs Exod 33:1', '34:1 vs 32:49', '34:9 vs Num 27:23', '34:7 vs 31:2')})
assert PLACEMENT['markers'] == MK_PRED, ('THE MARKERS\' PLACEMENT MOVED FROM THE DESIGN — read the stitcher\'s print', PLACEMENT['markers'], MK_PRED)
assert sum(PLACEMENT['events'].values()) == 1450 + 6, ('THE EVENTS\' PLACEMENT — the six lines', PLACEMENT['events'])
assert CENSUS[2] == 1456 and CENSUS[9] == 173, ('THE CENSUS MOVED FROM THE DESIGN — read the stitcher\'s print', CENSUS)   # on the tape 1450 -> 1456 (the six lines), markers 173 UNMOVED (NO MARKER); the rest READ
assert WN == 15 and NARR[7] == 0 and NARR[1] == 0, (WN, NARR)   # the fifteen writes on three ledgers — twelve new, three reuses (the design's fifteen; the print decides); NO marker; NO timer (the thirty days' row without a due)
assert len(SUP) == 6 and len(WRITES) >= 6 and len(TAPE_ROWS) >= 8 and NPAR == 9 and NCELL == 12, (len(SUP), len(WRITES), len(TAPE_ROWS), NPAR, NCELL)
# 3. RUN — the design's prediction with W read (timers set 102 + 0, fired 94 + 0 — the thirty days a duration; the tape's first print decides)
rep_head("RUN = (1450, 102, 94, 0, 12, 2076, 54, 319,   # THE DEUTERONOMY WALK 21b",
         "RUN = (1456, 102, 94, 0, 12, %d, 55, 319,   # %s: PREDICTED in DEUTERONOMY_WALK.md \"Sitting 22b\" (THE PREDICTION'S ARITHMETIC) BEFORE the run — events +6 (the six own-day lines in two forms), timers set +0 (the thirty days' row REUSED WITHOUT A DUE — a duration, no timer), timers fired +0 (NO MARKER — the clock does not walk; the tape's first print decides), cancels 0, retro-writes 12 UNMOVED, writes +%d (READ FROM THE RUNNER'S NARRATIVE PRINT — twelve new statuses and three reuses on three ledgers), daemons fired +1 (law_moses_death — THE BOOK'S LAST), entities 319 UNMOVED (moses, israel_people and yehoshua on the registry already; the LORD's speech makes no entity); sitting 21b's line follows:   # THE DEUTERONOMY WALK 21b" % (2076 + WN, W, WN))
rep_head("       127)   # THE DEUTERONOMY WALK 21b (2026-09-29; LEAN): 127 UNMOVED",
         "       127)   # %s: 127 UNMOVED — no close this sitting (the twelve statuses have no closer; the receipt at 34:9 a run citation, the register gate's class decides; the heaven entry reused at 34:4 stands open as 32:52's did); sitting 21b's line follows:   # THE DEUTERONOMY WALK 21b (2026-09-29; LEAN): 127 UNMOVED" % W)
# 4. PREVIOUS_RUN — 21b's RUN EXACTLY, no declared delta
rep_head("PREVIOUS_RUN = (1439, 102, 94, 0, 12, 2048, 53, 319,   # THE DEUTERONOMY WALK 21b",
         "PREVIOUS_RUN = (1450, 102, 94, 0, 12, 2076, 54, 319,   # %s: sitting 21b's RUN EXACTLY, read at the design (DEUTERONOMY_WALK.md \"Sitting 22b\", THE PREDICTION'S ARITHMETIC): THE REST drops chapter 34's six lines (inside the declared span [[Deut,34,1,12]]) and their daemon's writes; sitting 21b's line follows:   # THE DEUTERONOMY WALK 21b" % W)
rep_head("       127)   # THE DEUTERONOMY WALK 21b (2026-09-29; LEAN): sitting 20b's 127",
         "       127)   # %s: sitting 21b's 127 — no close this sitting, THE REST keeps 21b's; sitting 21b's line follows:   # THE DEUTERONOMY WALK 21b (2026-09-29; LEAN): sitting 20b's 127" % W)
# 5. NEWEST_RUNNER
rep_head("NEWEST_RUNNER = 'blessing_of_moses'   # THE DEUTERONOMY WALK 21b",
         "NEWEST_RUNNER = 'moses_death'   # %s: chapter 34's six own-day lines in two forms (after the tape's last Deuteronomy 33 line; NO MARKER; inside the declared span [[Deut,34,1,12]]) the newest joined (was 'blessing_of_moses') — THE BOOK'S LAST; THE REST drops the newest runner's lines and its daemon's writes; sitting 21b's line follows:   # THE DEUTERONOMY WALK 21b" % W)
# 6. PLACEMENT — READ at the stitcher's print (the markers' class asserted above; the events' classes the print's)
rep_head("PLACEMENT = {'markers': {'text_constrained': 108, 'reading_placed': 50}, 'events': {'text_constrained': 110, 'page_order': 1281, 'reading_placed': 59}}   # THE DEUTERONOMY WALK 21b",
         "PLACEMENT = %r   # %s: READ at the stitcher's print (scratchpad seq_stitch_ch34.out) — NO MARKER: the markers' placement 21b's EXACTLY (text_constrained 108, reading_placed 50); the events' classes the print's (the six lines at a marked day); sitting 21b's line follows:   # THE DEUTERONOMY WALK 21b" % (PLACEMENT, W))
# 7. THE VERDICTS entries — the D series' sixteenth name (five — the lean block)
old_v = "            'DO1 MATCH', 'DO2 MATCH', 'DO3 MATCH', 'DO4 MATCH', 'DO5 MATCH',   # THE DEUTERONOMY WALK 21b"
i = s.index(old_v); j = s.index('\n', i)
s = s[:j + 1] + "            'DP1 MATCH', 'DP2 MATCH', 'DP3 MATCH', 'DP4 MATCH', 'DP5 MATCH',   # %s: chapter 34's five — the D series' sixteenth name, the lean block over one chapter and one unit with NO MARKER and THREE REUSES — THE BOOK'S LAST\n" % W + s[j + 1:]
# 8. CENSUS — read from the stitcher's print; the prior line found by its head (its tuple read from the file, never typed)
m = re.search(r"^CENSUS = (\(.*?\))   # THE DEUTERONOMY WALK 21b \(2026-09-29; LEAN\): READ from the stitcher's print", s, re.M); assert m, 'the CENSUS line'
OLD_CENSUS = ast.literal_eval(m.group(1)); assert OLD_CENSUS[2] == 1450 and OLD_CENSUS[9] == 173, OLD_CENSUS
s = s[:m.start()] + ("CENSUS = %r   # %s: READ from the stitcher's print (scratchpad seq_stitch_ch34.out) after chapter 34's SIX lines joined after the last Deuteronomy 33 line with NO MARKER — on the tape 1450 -> 1456 AS THE DESIGN PREDICTED, markers 173 UNMOVED, the rest the print's; sitting 21b's line follows:   # THE DEUTERONOMY WALK 21b (2026-09-29; LEAN): READ from the stitcher's print" % (CENSUS, W)) + s[m.end():]
# 9. THE DP BLOCK — five checkpoints after DO5 (the lean block; the literals from the design, the runner's print, its part 5 and the register file)
OWN12 = list(S.NEW_EFFECTS); KINDS6 = list(S.KINDS)
SUBJ = {e: sub for l in S.LINES for e, _, sub in l[7]}   # each new effect's ledger
FIRSTS = tuple((l[1], sub) for l in S.LINES for _, _, sub in l[7]); assert len(FIRSTS) == 12
REUSES = tuple((e, S.REUSE_AFTER[e]) for e, _, _, _ in S.REUSES); assert len(REUSES) == 3
_FX = _yaml.safe_load(open(ROOT + '/World/step9/effect_vocabulary.yaml', encoding='utf-8'))['effects']; BLOCKS = [e for e in OWN12 if _FX[e]['ledger_op'] == 'block']; HEAVEN = [e for e in OWN12 if _FX[e]['ledger_op'] == 'heaven']; assert len(BLOCKS) == 0 and len(HEAVEN) == 0 and len(KINDS6) == 6
KIN24 = tuple(S.KIN); KIN_AFTER = tuple(S.KIN_AFTER[k] for k in KIN24)
TW = (TWIN['34:4 vs Exod 33:1'], TWIN['34:1 vs 32:49'], TWIN['34:9 vs Num 27:23'], TWIN['34:7 vs 31:2'])
DP = '''    # ---- THE DEUTERONOMY WALK 22b (2026-09-30; LEAN; DEUTERONOMY_WALK.md "Sitting 22b" THE CHECKPOINTS DP1-DP5): chapter 34's six own-day lines in two forms with NO MARKER and THREE REUSES — the D series' sixteenth name, the lean block over one chapter, THE BOOK'S LAST ----
    CP_KINDS = %(KINDS6)r; OWN12_CP = %(OWN12)r; SUBJ_CP = %(SUBJ)r; REUSES_CP = %(REUSES)r
    ev_cp = [(i, l) for i, l in enumerate(w.log) if l[0] == 'EVENT' and l[2]['kind'] in CP_KINDS]
    i_last_d33 = max(i for i, l in enumerate(w.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 33:'))
    mk_cp = [l for l in markers if str(l[2].get('verse', '')).startswith('Deut 34:')]
    cp('DP1 THE LINES — six events on the tape AFTER the tape\\'s last Deuteronomy 33 line, in the ink\\'s order (34:1, 34:4, 34:5, 34:7, 34:9, 34:10), no dated field; ALL on MOSES\\' LAST DAY (40, 12, 7) — 19b\\'s ONE MARKER at 31:1, NO MARKER in this chapter (the death THAT day; the thirty days a DURATION): markers 173 UNMOVED, no Deuteronomy 34 marker; the lines\\' day by the exodus era\\'s date', ([k for k in CP_KINDS], True, 0, 0, [], 173, [(40, 12, 7)]), ([l[2]['kind'] for _, l in ev_cp], all(i > i_last_d33 for i, _ in ev_cp), sum(1 for _, l in ev_cp if l[2].get('dated') is not None), len(mk_cp), [l[2]['verse'] for l in mk_cp], len(markers), sorted({ex.date(l[1]) for _, l in ev_cp})))
    FV_cp = (lambda t_: '%%s %%d:%%d' %% t_ if isinstance(t_, tuple) else str(t_))
    def LGx_cp(ent): return w.entities[ent].ledger if ent in w.entities else []
    n12_cp = tuple(len([e for e in LGx_cp(SUBJ_CP[eff]) if e['effect'] == eff]) for eff in OWN12_CP); src_cp = tuple((FV_cp(WE.first_verse(str([e for e in LGx_cp(SUBJ_CP[eff]) if e['effect'] == eff][0].get('case_source', '')))), SUBJ_CP[eff]) if [e for e in LGx_cp(SUBJ_CP[eff]) if e['effect'] == eff] else None for eff in OWN12_CP)
    def _nall_cp(eff): return sum(1 for ent in w.entities.values() for e in ent.ledger if e['effect'] == eff)
    blocks_cp = sum(1 for eff in OWN12_CP for ent in w.entities.values() for e in ent.ledger if e['effect'] == eff and e.get('op') == 'block'); heaven_cp = sum(1 for eff in OWN12_CP for ent in w.entities.values() for e in ent.ledger if e['effect'] == eff and e.get('op') == 'heaven'); dd_cp = yaml.safe_load(open(os.path.join(HERE, 'daemon_dispositions.yaml'), encoding='utf-8'))
    timer_cp = [e for e in LGx_cp('israel_people') if e['effect'] == 'mourned_thirty_days' and str(e.get('case_source', '')).startswith('Deut 34:')]
    cp('DP2 THE WRITES — the twelve NEW ONE each on their subjects with their lines\\' first verses (moses 34:1, 34:1, 34:4, 34:5, 34:5, 34:7; israel_people 34:5, 34:7, 34:9, 34:10, 34:10; yehoshua 34:9); THE THREE REUSES at their own forward seats — their counts on the tape AFTER (the denial 2, the gathering 6, the thirty days 2); the thirty days\\' row at 34:8 written WITHOUT A DUE (no timer — the design\\'s duration); no block; no heaven entry among the twelve; law_moses_death registered, given_at Deut 34:1, installed_by boot; the six cells and the table WRAPPED (seven)', (tuple((1, v) for v in %(FIRSTS)r), tuple(n_ for _, n_ in REUSES_CP), (1, None), 0, 0, True, 'Deut 34:1', 'boot', 7), (tuple(zip(n12_cp, src_cp)), tuple(_nall_cp(e_) for e_, _ in REUSES_CP), (len(timer_cp), timer_cp[0].get('due') if timer_cp else 'absent'), blocks_cp, heaven_cp, 'law_moses_death' in dd_cp['daemons'], dd_cp['daemons'].get('law_moses_death', {}).get('given_at'), dd_cp['daemons'].get('law_moses_death', {}).get('installed_by'), sum(1 for v in dd_cp['functions'].get('moses_death', {}).values() if v.get('status') == 'WRAPPED')))
    CRm = cold_run_moses_death
    cp('DP3 THE KIN — the twenty-four references\\' counts AFTER the run as the spec predicted (KIN_AFTER: the three reuses moved by one — see_the_land_from_afar_not_go_there 2, gathered_to_his_people 6, mourned_thirty_days 2; the rest UNMOVED — barred_from_the_land 2, invested_office 6, buried 9, wept 12 among them); the twins diffed (34:4/Exodus 33:1, 34:1/32:49, 34:9/Numbers 27:23, 34:7/31:2 — read from the runner\\'s print); THE PARSER\\'S TWO NUMBERS 120 at 34:7 and 30 at 34:8 — DATA rows, no count in the world; the scans\\' ground (the runner\\'s HOLE_SCAN empty at import)', (%(KINAFT)r, %(TW)r, [120], [30], True), (tuple(_nall_cp(k) for k in %(KIN24)r), (CRm.TWIN['34:4 vs Exod 33:1'], CRm.TWIN['34:1 vs 32:49'], CRm.TWIN['34:9 vs Num 27:23'], CRm.TWIN['34:7 vs 31:2']), CRm.PARSE[(34, 7)][0], CRm.PARSE[(34, 8)][0], CRm.HOLE_SCAN is None or all(v_ == [] for v_ in CRm.HOLE_SCAN.values())))
    RB_cp = cold_run_moses_death.READBACK; EVk_cp = [l[2] for l in events]
    found_tape_cp = sum(1 for r_ in RB_cp if r_['tape_kind'] and any(e['kind'] == r_['tape_kind'] and WE.first_verse(e.get('case_source')) == WE.first_verse(r_['tape_verse']) for e in EVk_cp))
    by_call_cp = sum(1 for r_ in RB_cp if r_['cell'] and r_['cell_found']); sup_cp = [r_ for r_ in RB_cp if r_['grade'] == 'SUPPLIED']
    rg_cp = yaml.safe_load(open(os.path.join(HERE, 'register_dispositions.yaml'), encoding='utf-8'))
    cp('DP4 THE READBACK — THE FORMS ON FILE, NO NEW FORM: the_readback\\'s rows TWELVE, one per verse (the census from the runner\\'s print: %(RBGS)s), every reference row\\'s entry FOUND: %(NTAPE)d on the tape by kind and first verse (the summons, Aaron\\'s death and his thirty days, the marker\\'s line, the commission, the prophet\\'s law, the signs, the tablets broken), the rows in the kin\\'s cells by CALL %(NCELL)d, every cell found; the SUPPLIED rows %(NSUP)d — the six lines\\' first verses; NO STATE ROW; THE THREE POINTER ROWS 34:4, 34:5, 34:6 (the song\\'s two and the blessing\\'s one PAID, grade R); no open row, no stretch; THE RECEIPT 34:9 RE-DECLARED — the register file\\'s class %(RCLASS)s AS THE GATE HOLDS IT (its print after the registration; the stale why removed)', (12, %(NTAPE)d, %(NCELL)d, %(NSUP)d, [], ['Deut 34:4', 'Deut 34:5', 'Deut 34:6'], 0, 0, %(RCLASS)r), (len(RB_cp), found_tape_cp, by_call_cp, len(sup_cp), [r_['verses'] for r_ in RB_cp if r_['state']], [r_['verses'] for r_ in RB_cp if r_['pointer']], sum(1 for r_ in RB_cp if r_['open']), sum(1 for r_ in RB_cp if r_['stretch']), rg_cp['receipts']['Deut 34:9']['class']))
    cp('DP5 THE REST — entities 319 UNMOVED (moses, israel_people and yehoshua on the registry already; the LORD\\'s speech makes no entity), closes 127 UNMOVED, the population table 148 UNMOVED, the six kinds present in two forms (1 speech, 5 act), markers 173 (NO MARKER — 19b\\'s at 31:1 stands); the span\\'s one range and the 20 edges on file, OWED pointers 0 in the file, the calendar UNTOUCHED (75 parameters; the_death_date_of_moses 19b\\'s, exercised by covenant_return_charge alone); the other counts 21b\\'s exactly with the six lines and the daemon\\'s writes added (RUN above) — THE BOOK\\'S EDGE', (319, 127, 148, True, (1, 5), 173, 1, True, 0, 75, ['covenant_return_charge']), (len(w.entities), len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')]), len(w.tables['population']), all(k in {l[2]['kind'] for l in events} for k in CP_KINDS), tuple([yaml.safe_load(open(os.path.join(HERE, 'event_vocabulary.yaml'), encoding='utf-8'))['events'][k]['form'] for k in CP_KINDS].count(f_) for f_ in ('speech', 'act')), len(markers), len(yaml.safe_load(open(os.path.join(HERE, 'dependency_dispositions.yaml'), encoding='utf-8'))['spans']['moses_death']), sum(1 for e in yaml.safe_load(open(os.path.join(HERE, 'dependency_dispositions.yaml'), encoding='utf-8'))['edges'] if e['from'] == 'moses_death') >= 20, sum(1 for p in yaml.safe_load(open(os.path.join(HERE, 'dependency_dispositions.yaml'), encoding='utf-8'))['pointers'] if p.get('disposition') == 'OWED'), len(WE.CAL_PARAMS), WE.CAL_PARAMS['the_death_date_of_moses']['exercised_by']))
''' % dict(KINDS6=KINDS6, OWN12=OWN12, SUBJ=SUBJ, REUSES=REUSES, FIRSTS=FIRSTS, RBGS=', '.join('%s %d' % kv for kv in RBG.items()), NTAPE=len(TAPE_ROWS), NCELL=NCELL, NSUP=len(SUP), KINAFT=KIN_AFTER, KIN24=KIN24, TW=TW, RCLASS=RCLASS)
anchor = "    print('    the story\\'s dates: Moses born %r"
assert s.count(anchor) == 1, s.count(anchor)
s = s.replace(anchor, DP + anchor)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched: RUN (writes +%d read), PREVIOUS_RUN (no declared delta), NEWEST_RUNNER, PLACEMENT (read %r), VERDICTS DP, CENSUS (read %r), DP1-DP5 (the readback census %r, %d supplied, %d writes, %d tape rows, %d cells read from the print and part 5; %d parameters; the receipt\'s class %s; the twins %r); compiles' % (WN, PLACEMENT, CENSUS, RBG, len(SUP), len(WRITES), len(TAPE_ROWS), NCELL, NPAR, RCLASS, TW))
