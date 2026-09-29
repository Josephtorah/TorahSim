import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (2026-09-28; LEAN): the sequence file's literals and checkpoints for chapter 32 — the import line (the live registration edge), the
# DAEMON_ORDER entry, RUN (predicted in the design: +16 events, +W writes with W READ FROM THE RUNNER'S NARRATIVE PRINT, +1 daemon fired, timers fired +0 — no clock
# word in the song, the tape's first print decides; the rest unmoved), PREVIOUS_RUN (19b's RUN EXACTLY — no declared delta), NEWEST_RUNNER, PLACEMENT and CENSUS READ FROM
# THE STITCHER'S PRINT (seq_stitch_ch32.out — the sixteen own-day lines in three forms after the tape's last Deuteronomy 31 line; NO MARKER — markers 173 UNMOVED), the
# DN1-DN5 block after DM5 + the VERDICTS entries (the D series' fourteenth name — five checkpoints, the lean block). Every replacement anchored on the exact prior text's
# head (the comment tails kept); the readback's census and writes READ from the runner's print and its part 5, never typed; the file asserted to compile after.
# patch_seq_literals_ch29.py's form WITHOUT THE MARKER. RUN FROM THE REPO ROOT.
import re, ast, subprocess, sys, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch32b_spec as S
P = ROOT + '/World/step9/cold_run_sequence.py'
s = open(P, encoding='utf-8').read()
assert 'import cold_run_song_charge_nebo' not in s, 'already patched'
def rep_head(old_head, new_head):
    """the line whose HEAD is old_head gets new_head in its place — the comment tail kept verbatim (the prior sitting's line follows the new comment)"""
    global s
    i = s.index('\n' + old_head) + 1; assert s.count('\n' + old_head) == 1, (s.count('\n' + old_head), old_head[:80])
    s = s[:i] + new_head + s[i + len(old_head):]
W = 'THE DEUTERONOMY WALK 20b (2026-09-28; LEAN)'
# 0. THE PRINTS — the placement and the census read from the stitcher's, the writes' count and the readback's census from the runner's print, the rows' writes from part 5
pr = open(SP + '/seq_stitch_ch32.out', encoding='utf-8').read()
PLACEMENT = ast.literal_eval(re.search(r'^PLACEMENT LITERAL: (.*)$', pr, re.M).group(1))
CENSUS = ast.literal_eval(re.search(r'^  CENSUS tuple .*?: (\(.*\))$', pr, re.M).group(1))
RUNF = sorted([f for f in os.listdir(SP) if re.match(r'ch32_runner_run\d+\.out$', f)])[-1]
run_out = open(SP + '/' + RUNF, encoding='utf-8').read()
NARR = ast.literal_eval(re.search(r'^THE NARRATIVE: (\(.*?\)) \(the forty-five on three ledgers', run_out, re.M).group(1)); WN = NARR[0]
RBG = ast.literal_eval(re.search(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: 52 rows — (\{.*?\});', run_out, re.M).group(1))
NPAR = int(re.search(r'the parameters (\d+) \(in the registry', run_out).group(1))
p5 = open(SP + '/ch32_part5.py', encoding='utf-8').read()
ROWS = re.findall(r"^    rb\('(Deut \d+:\d+)', \".*?\", '([A-Z]+)', .*?(?:, write='([a-z_]+)')?(?:, state=True)?(?:, pointer=\{.*?\})?\),\n", p5, re.M)
assert len(ROWS) == 52, len(ROWS)
SUP = [v for v, g, w_ in ROWS if g == 'SUPPLIED']; WRITES = [(v, w_) for v, g, w_ in ROWS if w_]
TAPE_ROWS = re.findall(r"^    rb\('(Deut \d+:\d+)', .*?tape_kind='(\w+)', tape_verse='([^']+)'", p5, re.M)
MK_PRED = {'text_constrained': 108, 'reading_placed': 50}   # the design's arithmetic: NO MARKER — 19b's placement EXACTLY; the events' classes READ FROM THE PRINT
print('PLACEMENT read:', PLACEMENT, '| markers predicted:', MK_PRED); print('CENSUS read:', CENSUS); print('the writes W read from the narrative:', WN, '| the narrative:', NARR, '| the readback census read:', RBG, '| SUPPLIED', len(SUP), SUP, '| writes', len(WRITES), '| tape rows', len(TAPE_ROWS), '| parameters', NPAR)
assert PLACEMENT['markers'] == MK_PRED, ('THE MARKERS\' PLACEMENT MOVED FROM THE DESIGN — read the stitcher\'s print', PLACEMENT['markers'], MK_PRED)
assert sum(PLACEMENT['events'].values()) == 1423 + 16, ('THE EVENTS\' PLACEMENT — the sixteen lines', PLACEMENT['events'])
assert CENSUS[2] == 1439 and CENSUS[9] == 173, ('THE CENSUS MOVED FROM THE DESIGN — read the stitcher\'s print', CENSUS)   # on the tape 1423 -> 1439 (the sixteen lines), markers 173 UNMOVED (NO MARKER); the rest READ
assert WN == 45 and NARR[7] == 0, (WN, NARR)   # the forty-five writes on three ledgers — forty-two first entries and three reuses (the design's forty-five; the print decides); NO marker
assert len(SUP) == 16 and len(WRITES) >= 16 and len(TAPE_ROWS) >= 20 and NPAR == 25, (len(SUP), len(WRITES), len(TAPE_ROWS), NPAR)
# 1. the import line — the live edge the dependency gate reads
i = s.index('import cold_run_covenant_return_charge   # THE DEUTERONOMY WALK 19b'); j = s.index('\n', i)
s = s[:j + 1] + "import cold_run_song_charge_nebo   # %s: chapter 32 (Deut 32:1-52) in ONE runner over two units — THE SONG (the witnesses called a fifth time, the Rock, the crooked generation, the nations divided, the desert and the eagle, the heights and the feast, Jeshurun fat, the hidden face the third time, the evils heaped, the enemy's boast, the joined thousand THE STATE ROW, the cup in store, I am He and the land atones) AND ITS FRAME (the song spoken with Hoshea, the charge, the summons to Nebo, Meribah); SIXTEEN own-day lines IN THREE FORMS (14 speeches, 1 act, 1 statute) ALL at Moses' last day (40, 12, 7) — NO MARKER (19b's at 31:1); the daemon law_song_charge_nebo given_at Deut 32:1, installed_by boot; 42 CALL edges all reference; DEUTERONOMY_WALK.md \"Sitting 20b\"\n" % W + s[j + 1:]
# 2. DAEMON_ORDER
i = s.index("    ('cold_run_covenant_return_charge', 'law_covenant_return_charge'),   # THE DEUTERONOMY WALK 19b"); j = s.index('\n', i)
s = s[:j + 1] + "    ('cold_run_song_charge_nebo', 'law_song_charge_nebo'),   # %s; DEUTERONOMY_WALK.md \"Sitting 20b\": chapter 32 — SIXTEEN lines in THREE FORMS (song_witnesses_called_declared 32:1, song_crooked_generation_declared 32:5, song_nations_divided_lords_portion_declared 32:7, song_found_in_the_desert_declared 32:10, song_heights_honey_rock_declared 32:13, song_jeshurun_fat_kicked_declared 32:15, song_face_hidden_foolish_nation_declared 32:19, song_evils_heaped_declared 32:23, song_enemys_boast_declared 32:26, song_one_chasing_a_thousand_declared 32:29, song_vengeance_in_store_declared 32:34, song_i_am_he_declared 32:39 — the twelve stanzas; song_spoken_by_moses_and_hoshea 32:44 (an act); set_your_heart_no_empty_matter_declared 32:46 (the statute); nebo_summons_die_as_aaron 32:48 and meribah_trespass_not_go_there_declared 32:51 (the LORD's speeches) — ALL on MOSES' LAST DAY (40, 12, 7), NO MARKER); 45 writes on three ledgers (Israel 39, Joshua 1, Moses 5 — forty-two new, three reuses)\n" % W + s[j + 1:]
# 3. RUN — the design's prediction with W read (timers fired 94 + F — F predicted 0, the tape's first print decides)
rep_head("RUN = (1423, 102, 94, 0, 12, 2003, 52, 319,   # THE DEUTERONOMY WALK 19b",
         "RUN = (1439, 102, 94, 0, 12, %d, 53, 319,   # %s: PREDICTED in DEUTERONOMY_WALK.md \"Sitting 20b\" (THE PREDICTION'S ARITHMETIC) BEFORE the run — events +16 (the sixteen own-day lines in three forms), timers set +0 (no clock word in the song), timers fired +0 (NO MARKER — the clock does not walk; the tape's first print decides), cancels 0, retro-writes 12 UNMOVED, writes +%d (READ FROM THE RUNNER'S NARRATIVE PRINT — forty-two first entries and three reuses), daemons fired +1 (law_song_charge_nebo), entities 319 UNMOVED (israel_people, yehoshua and moses on the registry already); sitting 19b's line follows:   # THE DEUTERONOMY WALK 19b" % (2003 + WN, W, WN))
rep_head("       127)   # THE DEUTERONOMY WALK 19b (2026-09-27; LEAN): 127 UNMOVED",
         "       127)   # %s: 127 UNMOVED — no close this sitting (the thirty-two statuses and the ten heaven entries have no closer, no block; the commission's debit on Moses stands OPEN to 34:1-4 — its second telling at 32:49 a status); sitting 19b's line follows:   # THE DEUTERONOMY WALK 19b (2026-09-27; LEAN): 127 UNMOVED" % W)
# 4. PREVIOUS_RUN — 19b's RUN EXACTLY, no declared delta
rep_head("PREVIOUS_RUN = (1403, 96, 88, 0, 12, 1929, 51, 319,   # THE DEUTERONOMY WALK 19b",
         "PREVIOUS_RUN = (1423, 102, 94, 0, 12, 2003, 52, 319,   # %s: sitting 19b's RUN EXACTLY, read at the design (DEUTERONOMY_WALK.md \"Sitting 20b\", THE PREDICTION'S ARITHMETIC): THE REST drops chapter 32's sixteen lines (inside the declared span [[Deut,32,1,52]]) and their daemon's writes; sitting 19b's line follows:   # THE DEUTERONOMY WALK 19b" % W)
rep_head("       127)   # THE DEUTERONOMY WALK 19b (2026-09-27; LEAN): sitting 18b's 127",
         "       127)   # %s: sitting 19b's 127 — no close this sitting, THE REST keeps 19b's; sitting 19b's line follows:   # THE DEUTERONOMY WALK 19b (2026-09-27; LEAN): sitting 18b's 127" % W)
# 5. NEWEST_RUNNER
rep_head("NEWEST_RUNNER = 'covenant_return_charge'   # THE DEUTERONOMY WALK 19b",
         "NEWEST_RUNNER = 'song_charge_nebo'   # %s: chapter 32's sixteen own-day lines in three forms (after the tape's last Deuteronomy 31 line; NO MARKER; inside the declared span [[Deut,32,1,52]]) the newest joined (was 'covenant_return_charge'); THE REST drops the newest runner's lines and its daemon's writes; sitting 19b's line follows:   # THE DEUTERONOMY WALK 19b" % W)
# 6. PLACEMENT — READ at the stitcher's print (the markers' class asserted above; the events' classes the print's)
rep_head("PLACEMENT = {'markers': {'text_constrained': 108, 'reading_placed': 50}, 'events': {'text_constrained': 110, 'page_order': 1254, 'reading_placed': 59}}   # THE DEUTERONOMY WALK 19b",
         "PLACEMENT = %r   # %s: READ at the stitcher's print (scratchpad seq_stitch_ch32.out) — NO MARKER: the markers' placement 19b's EXACTLY (text_constrained 108, reading_placed 50); the events' classes the print's (the sixteen lines at a marked day); sitting 19b's line follows:   # THE DEUTERONOMY WALK 19b" % (PLACEMENT, W))
# 7. THE VERDICTS entries — the D series' fourteenth name (five — the lean block)
old_v = "            'DM1 MATCH', 'DM2 MATCH', 'DM3 MATCH', 'DM4 MATCH', 'DM5 MATCH',   # THE DEUTERONOMY WALK 19b"
i = s.index(old_v); j = s.index('\n', i)
s = s[:j + 1] + "            'DN1 MATCH', 'DN2 MATCH', 'DN3 MATCH', 'DN4 MATCH', 'DN5 MATCH',   # %s: chapter 32's five — the D series' fourteenth name, the lean block over one chapter and two units with NO MARKER\n" % W + s[j + 1:]
# 8. CENSUS — read from the stitcher's print; the prior line found by its head (its tuple read from the file, never typed)
m = re.search(r"^CENSUS = (\(.*?\))   # THE DEUTERONOMY WALK 19b \(2026-09-27; LEAN\): READ from the stitcher's print", s, re.M); assert m, 'the CENSUS line'
OLD_CENSUS = ast.literal_eval(m.group(1)); assert OLD_CENSUS[2] == 1423 and OLD_CENSUS[9] == 173, OLD_CENSUS
s = s[:m.start()] + ("CENSUS = %r   # %s: READ from the stitcher's print (scratchpad seq_stitch_ch32.out) after chapter 32's SIXTEEN lines joined after the last Deuteronomy 31 line with NO MARKER — on the tape 1423 -> 1439 AS THE DESIGN PREDICTED, markers 173 UNMOVED, the rest the print's; sitting 19b's line follows:   # THE DEUTERONOMY WALK 19b (2026-09-27; LEAN): READ from the stitcher's print" % (CENSUS, W)) + s[m.end():]
# 9. THE DN BLOCK — five checkpoints after DM5 (the lean block; the literals from the design, the runner's print and its part 5)
OWN42 = list(S.NEW_EFFECTS); KINDS16 = list(S.KINDS)
SUBJ = {e: sub for l in S.LINES for e, _, sub in l[7]}   # each new effect's ledger
FIRSTS = tuple((l[1], sub) for l in S.LINES for _, _, sub in l[7]); assert len(FIRSTS) == 42
import yaml as _yaml; _FX = _yaml.safe_load(open(ROOT + '/World/step9/effect_vocabulary.yaml', encoding='utf-8'))['effects']; BLOCKS = [e for e in OWN42 if _FX[e]['ledger_op'] == 'block']; HEAVEN = [e for e in OWN42 if _FX[e]['ledger_op'] == 'heaven']; assert len(BLOCKS) == 0 and len(HEAVEN) == 10 and len(KINDS16) == 16
KIN62 = tuple(S.KIN_UNMOVED); KIN_EXPECTED = tuple(S.KIN_UNMOVED[k] for k in KIN62); RE3 = [(e, S.REUSE_AFTER[e]) for e in S.REUSE_BEFORE]
DN = '''    # ---- THE DEUTERONOMY WALK 20b (2026-09-28; LEAN; DEUTERONOMY_WALK.md "Sitting 20b" THE CHECKPOINTS DN1-DN5): chapter 32's sixteen own-day lines in three forms with NO MARKER — the D series' fourteenth name, the lean block over one chapter ----
    CP_KINDS = %(KINDS16)r; OWN42_CP = %(OWN42)r; SUBJ_CP = %(SUBJ)r
    ev_cp = [(i, l) for i, l in enumerate(w.log) if l[0] == 'EVENT' and l[2]['kind'] in CP_KINDS]
    i_last_d31 = max(i for i, l in enumerate(w.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 31:'))
    mk_cp = [l for l in markers if str(l[2].get('verse', '')).startswith('Deut 32:')]
    cp('DN1 THE LINES — sixteen events on the tape AFTER the tape\\'s last Deuteronomy 31 line, in the ink\\'s order (32:1, 32:5, 32:7, 32:10, 32:13, 32:15, 32:19, 32:23, 32:26, 32:29, 32:34, 32:39, 32:44, 32:46, 32:48, 32:51), no dated field; ALL on MOSES\\' LAST DAY (40, 12, 7) — 19b\\'s ONE MARKER at 31:1, NO MARKER in this chapter (32:48\\'s selfsame day THAT day): markers 173 UNMOVED, no Deuteronomy 32 marker; the lines\\' day by the exodus era\\'s date', ([k for k in CP_KINDS], True, 0, 0, [], 173, [(40, 12, 7)]), ([l[2]['kind'] for _, l in ev_cp], all(i > i_last_d31 for i, _ in ev_cp), sum(1 for _, l in ev_cp if l[2].get('dated') is not None), len(mk_cp), [l[2]['verse'] for l in mk_cp], len(markers), sorted({ex.date(l[1]) for _, l in ev_cp})))
    FV_cp = (lambda t_: '%%s %%d:%%d' %% t_ if isinstance(t_, tuple) else str(t_))
    def LGx_cp(ent): return w.entities[ent].ledger if ent in w.entities else []
    n42_cp = tuple(len([e for e in LGx_cp(SUBJ_CP[eff]) if e['effect'] == eff]) for eff in OWN42_CP); src_cp = tuple((FV_cp(WE.first_verse(str([e for e in LGx_cp(SUBJ_CP[eff]) if e['effect'] == eff][0].get('case_source', '')))), SUBJ_CP[eff]) if [e for e in LGx_cp(SUBJ_CP[eff]) if e['effect'] == eff] else None for eff in OWN42_CP)
    def _nall_cp(eff): return sum(1 for ent in w.entities.values() for e in ent.ledger if e['effect'] == eff)
    re_cp = tuple(_nall_cp(eff) for eff, _ in %(RE3)r)
    blocks_cp = sum(1 for eff in OWN42_CP for ent in w.entities.values() for e in ent.ledger if e['effect'] == eff and e.get('op') == 'block'); heaven_cp = sum(1 for eff in %(HEAVEN)r for ent in w.entities.values() for e in ent.ledger if e['effect'] == eff and e.get('op') == 'heaven'); dd_cp = yaml.safe_load(open(os.path.join(HERE, 'daemon_dispositions.yaml'), encoding='utf-8'))
    cp('DN2 THE WRITES — the forty-two NEW ONE each on their subjects with their lines\\' first verses (36 on israel_people, 1 on yehoshua — 32:44, 5 on moses — 32:48, 32:48, 32:48, 32:51, 32:51); THE THREE REUSES\\' entries after (heaven_and_earth_witness 5 — the chain\\'s fifth seat, face_hidden_and_forsaken_foretold 2 — the hidden face the third time, length_of_days_on_the_land_promised 2); no block; the ten heaven entries; law_song_charge_nebo registered, given_at Deut 32:1, installed_by boot; the sixteen cells and the table WRAPPED (seventeen)', (tuple((1, v) for v in %(FIRSTS)r), tuple(n_ for _, n_ in %(RE3)r), 0, 10, True, 'Deut 32:1', 'boot', 17), (tuple(zip(n42_cp, src_cp)), re_cp, blocks_cp, heaven_cp, 'law_song_charge_nebo' in dd_cp['daemons'], dd_cp['daemons'].get('law_song_charge_nebo', {}).get('given_at'), dd_cp['daemons'].get('law_song_charge_nebo', {}).get('installed_by'), sum(1 for v in dd_cp['functions'].get('song_charge_nebo', {}).values() if v.get('status') == 'WRAPPED')))
    RB_cp = cold_run_song_charge_nebo.READBACK; EVk_cp = [l[2] for l in events]
    found_tape_cp = sum(1 for r_ in RB_cp if r_['tape_kind'] and any(e['kind'] == r_['tape_kind'] and WE.first_verse(e.get('case_source')) == WE.first_verse(r_['tape_verse']) for e in EVk_cp))
    by_call_cp = sum(1 for r_ in RB_cp if r_['cell'] and r_['cell_found']); sup_cp = [r_ for r_ in RB_cp if r_['grade'] == 'SUPPLIED']
    cp('DN3 THE READBACK — THE FORMS ON FILE, NO NEW FORM: the_readback\\'s rows FIFTY-TWO, one per verse (the census from the runner\\'s print: %(RBGS)s), every reference row\\'s entry FOUND: %(NTAPE)d on the tape by kind and first verse (the witnesses called, the sonship, Babel\\'s scattering, Sinai\\'s covenant, the manna, the rock struck, Balaam\\'s parable, the song commanded, the inciter, the forgetting warned, the apostasy foretold, the eagle nation, the plagues scattered, the serpents, the trembling, the storehouses\\' blessing, the refuge law, Sodom\\'s fire, the Shema, the assembly and the song, the crossing charge, the hakhel, life and death, the ark entered, Abarim\\'s summons, Aaron\\'s death — THE RUN CITATION, the sentence at Meribah), the rows in the kin\\'s cells by CALL %(NCELL)d, every cell found; the SUPPLIED rows %(NSUP)d — the sixteen lines\\' first verses; THE STATE ROW at 32:30 (the joined thousand); NO pointer row (32:50 a run citation, 34:4 owed); no open row, no stretch, no retrograde row', (52, %(NTAPE)d, %(NCELL)d, %(NSUP)d, ['Deut 32:30'], [], 0, 0), (len(RB_cp), found_tape_cp, by_call_cp, len(sup_cp), [r_['verses'] for r_ in RB_cp if r_['state']], [r_['verses'] for r_ in RB_cp if r_['pointer']], sum(1 for r_ in RB_cp if r_['open']), sum(1 for r_ in RB_cp if r_['stretch'])))
    CRm = cold_run_song_charge_nebo
    cp('DN4 THE KIN AND THE REUSES — the sixty-two references\\' counts as the recon and the callees read them (barred_from_the_land 2 — Moses\\' and Aaron\\'s, gathered_to_his_people 5 — Aaron\\'s the fifth, became_the_lords_people_this_day 2, treasured_people 1, other_gods_barred 1, manna_provided 1, water_from_the_rock 2, eagle_nation_devours 1, innocent_blood_atoned 1, two_witnesses_required 1, song_spoken_to_the_assembly_to_its_end 1, atoned_forgiven 7, famine 3, no_share_in_the_world_to_come 3, enemies_flee_seven_ways 1, smitten_before_enemies_seven_ways 1 among them — no second write; the reuses MOVED by their entries); the twins diffed (32:36/Psalm 135:14 seven, 32:49/Numbers 27:12 ten, 32:46/31:12 eight, 32:47/11:9 five); THE PARSER\\'S TWO GUARDS — the false eight at 32:15 ([8] a verb) and the joined thousand at 32:30 ([1, 1002] a proverb): no count in the world; the scans\\' ground (the runner\\'s HOLE_SCAN empty at import)', (%(KINEXP)r, 7, 10, 8, 5, [8], [1, 1002], True), (tuple(_nall_cp(k) for k in %(KIN62)r), CRm.TWIN['32:36 vs Ps 135:14'], CRm.TWIN['32:49 vs Num 27:12'], CRm.TWIN['32:46 vs 31:12'], CRm.TWIN['32:47 vs 11:9'], CRm.PARSE[(32, 15)][0], CRm.PARSE[(32, 30)][0], CRm.HOLE_SCAN is None or all(v_ == [] for v_ in CRm.HOLE_SCAN.values())))
    cp('DN5 THE REST — entities 319 UNMOVED (israel_people, yehoshua and moses on the registry already), closes 127 UNMOVED, the population table 148 UNMOVED, the sixteen kinds present in three forms (14 speech, 1 act, 1 statute), markers 173 (NO MARKER — 19b\\'s at 31:1 stands); the span\\'s one range and the 42 edges on file, OWED pointers 0 in the file, the calendar UNTOUCHED (75 parameters; the_death_date_of_moses 19b\\'s, exercised by covenant_return_charge alone); the other counts 19b\\'s exactly with the sixteen lines and the daemon\\'s writes added (RUN above)', (319, 127, 148, True, (14, 1, 1), 173, 1, True, 0, 75, ['covenant_return_charge']), (len(w.entities), len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')]), len(w.tables['population']), all(k in {l[2]['kind'] for l in events} for k in CP_KINDS), tuple([yaml.safe_load(open(os.path.join(HERE, 'event_vocabulary.yaml'), encoding='utf-8'))['events'][k]['form'] for k in CP_KINDS].count(f_) for f_ in ('speech', 'act', 'statute')), len(markers), len(yaml.safe_load(open(os.path.join(HERE, 'dependency_dispositions.yaml'), encoding='utf-8'))['spans']['song_charge_nebo']), sum(1 for e in yaml.safe_load(open(os.path.join(HERE, 'dependency_dispositions.yaml'), encoding='utf-8'))['edges'] if e['from'] == 'song_charge_nebo') >= 42, sum(1 for p in yaml.safe_load(open(os.path.join(HERE, 'dependency_dispositions.yaml'), encoding='utf-8'))['pointers'] if p.get('disposition') == 'OWED'), len(WE.CAL_PARAMS), WE.CAL_PARAMS['the_death_date_of_moses']['exercised_by']))
''' % dict(KINDS16=KINDS16, OWN42=OWN42, SUBJ=SUBJ, HEAVEN=HEAVEN, FIRSTS=FIRSTS, RE3=RE3, RBGS=', '.join('%s %d' % kv for kv in RBG.items()), NTAPE=len(TAPE_ROWS), NCELL=len(re.findall(r"^    rb\('Deut \d+:\d+', .*?cell='", p5, re.M)), NSUP=len(SUP), KINEXP=KIN_EXPECTED, KIN62=KIN62)
anchor = "    print('    the story\\'s dates: Moses born %r"
assert s.count(anchor) == 1, s.count(anchor)
s = s.replace(anchor, DN + anchor)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched: import, DAEMON_ORDER, RUN (writes +%d read), PREVIOUS_RUN (no declared delta), NEWEST_RUNNER, PLACEMENT (read %r), VERDICTS DN, CENSUS (read %r), DN1-DN5 (the readback census %r, %d supplied, %d writes, %d tape rows read from the print and part 5; %d parameters); compiles' % (WN, PLACEMENT, CENSUS, RBG, len(SUP), len(WRITES), len(TAPE_ROWS), NPAR))
