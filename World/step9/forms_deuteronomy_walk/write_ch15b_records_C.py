# ---- THE ANCHORS ----
ok = True
def need(p, a, n=1):
    global ok
    c = read(p).count(a)
    if c != n: print('ANCHOR', p.split('/')[-1], c, a[:70]); ok = False
MAP = 'World/step9/DEUTERONOMY_WALK.md'; DEBT = 'World/step9/COMPILE_DEBT.md'; MID = 'logic/MIDDOT.md'; RL = 'RESEARCH_LOG.md'; STEPS = 'THE_STEPS.md'; BRIEF = 'THE_BRIEFING.md'; LOOP = 'World/step9/THE_LOOP.md'
RES = 'World/RESUME.md'; RF = 'World/step9/RECORD_FORMS.md'; STATEDOC = 'logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; ADD = 'logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md'
REC = 'logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; WALK = f'{MEM}/deuteronomy-walk.md'; IDX = f'{MEM}/MEMORY.md'; LEDGER = 'logic/oral_triage/deu_15_reeh_2026-09-22.md'
BRIEF_ENTRY_ANCHOR = [l for l in read(BRIEF).split('\n') if l.startswith('### 2026-09-22 — CHAPTER 15 READ')]; assert len(BRIEF_ENTRY_ANCHOR) == 1, BRIEF_ENTRY_ANCHOR; BRIEF_ENTRY_ANCHOR = BRIEF_ENTRY_ANCHOR[0]
BRIEF_BULLET_ANCHOR = [l for l in read(BRIEF).split('\n') if l.startswith('- **CHAPTER 15 READ AND FROZEN')]; assert len(BRIEF_BULLET_ANCHOR) == 1, BRIEF_BULLET_ANCHOR; BRIEF_BULLET_ANCHOR = BRIEF_BULLET_ANCHOR[0]
MEM_DESC = [l for l in read(WALK).split('\n') if l.startswith('description: "')]; assert len(MEM_DESC) == 1, MEM_DESC; MEM_DESC_OLD = MEM_DESC[0]
MEM_DESC_NEW = ('description: "COMMITTED THROUGH b0eaa56 (2026-09-22, chapter 15\'s reading; NOT PUSHED — pushed through 049f55c) — SITTING 13b DONE 2026-09-23 (chapter 15 COMPILED — four laws at the chapter\'s own day, two clock data, four reuses, twenty-seven parameters; the runner %d/%d; DG1-DG9; the tape in three runs, the chain in three passes); 13b uncommitted; NEXT on his word: the commit, the push on \\"push\\", then chapter 16\'s reading (16:1-22) in two runs + the tail"' % (MX[0], MX[1]))
need(DEBT, DEBT_HDR_OLD); need(MID, MIDDOT_ANCHOR); need(STEPS, STEPS_ANCHOR); need(BRIEF, BRIEF_BULLET_ANCHOR); need(BRIEF, BRIEF_ENTRY_ANCHOR); need(BRIEF, SCORE_OLD); need(LOOP, LOOP_OLD); need(RF, FORMS_OLD)
need(WALK, MEM_DESC_OLD); need(IDX, MEM_IDX_OLD); need(MAP, L4P); assert read(MAP).index(L4E, read(MAP).index(L4P)) - read(MAP).index(L4P) < 400, 'the lesson-4 tail not within its sentence'
for a, b in REC_EDITS: need(REC, a)
assert 'Sitting 13b — THE COMPILE OF CHAPTER 15 — AS BUILT' not in read(MAP) and '#207 ADDENDUM 5' not in read(STATEDOC) and '#207 ADDENDUM 4' in read(STATEDOC) and '## CORRECTION (2026-09-23' not in read(LEDGER)
rec = read(REC)
for a, b in REC_EDITS: rec = rec.replace(a, b)
idx = read(IDX).replace(MEM_IDX_OLD, MEM_IDX_NEW)
N_ADD = next_addenda_no(read(ADD)); ADDENDA_ADD = ADDENDA_ADD_T.replace('{N}', str(N_ADD))
for t in (AS_BUILT, LESSON4_NEW, LEDGER_CORR, DEBT_BOX, MIDDOT_ENTRY, RLOG, STEPS_PARA, BRIEF_BULLET, BRIEF_ENTRY, LOOP_NEW, RESUME_HEAD, STATE_ADD, ADDENDA_ADD, MEM_PARA, MEM_DESC_NEW, rec, idx):
    assert not re.search(r'/Users/(?!Shared/)', t) and os.path.expanduser('~') not in t and ('/private' + '/tmp') not in t, 'a home or scratch path in a record'   # the guard's literal split by concatenation
for t in (AS_BUILT, LESSON4_NEW, LEDGER_CORR, DEBT_BOX, MIDDOT_ENTRY, RLOG, STEPS_PARA, BRIEF_BULLET, BRIEF_ENTRY, LOOP_NEW, RESUME_HEAD, STATE_ADD, ADDENDA_ADD, MEM_PARA, MEM_DESC_NEW):   # the NEW texts alone (the recovery page and the index carry glossed Hebrew of their own)
    assert not re.search('[\\u0590-\\u05FF]', t), 'Hebrew script in a new record — the map, the ledgers and the sheets carry none'
def lint(p):
    q = p if p.startswith('/') else f'{ROOT}/{p}'
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', q], capture_output=True, text=True); m = re.search(r'(\d+) flag', r.stdout + r.stderr); return int(m.group(1)) if m else None
FILES = (MAP, DEBT, MID, RL, STEPS, BRIEF, LOOP, RES, RF, STATEDOC, ADD, REC, WALK, IDX, LEDGER)
LINT_BEFORE = {p: lint(p) for p in FILES}
print('anchors %s; the recovery page would be %d bytes (cap 10240); MEMORY.md %d (cap 17000); the addenda section §%d; the lint before %s' % ('OK' if ok else 'BAD', len(rec.encode('utf-8')), len(idx.encode('utf-8')), N_ADD, {p.split('/')[-1]: n for p, n in LINT_BEFORE.items()}))
assert ok and len(rec.encode('utf-8')) <= 10240 and len(idx.encode('utf-8')) <= 17000
if CHECK: sys.exit(0)
m = read(MAP); i = m.index(L4P); j = m.index(L4E, i) + len(L4E); assert m.count(L4P) == 1 and RIDER not in m; W(MAP, (m[:j] + RIDER + m[j:]).rstrip('\n') + '\n' + AS_BUILT)
W(LEDGER, read(LEDGER).rstrip('\n') + '\n' + LEDGER_CORR)
W(DEBT, read(DEBT).replace(DEBT_HDR_OLD, DEBT_HDR_NEW).rstrip('\n') + '\n' + DEBT_BOX)
W(MID, read(MID).replace(MIDDOT_ANCHOR, '\n' + MIDDOT_ENTRY.rstrip('\n') + '\n' + MIDDOT_ANCHOR))
W(RL, read(RL).rstrip('\n') + '\n' + RLOG)
W(STEPS, read(STEPS).replace(STEPS_ANCHOR, '\n' + STEPS_PARA.rstrip('\n') + '\n' + STEPS_ANCHOR))
b = read(BRIEF); b = b.replace(SCORE_OLD, SCORE_NEW, 1).replace(BRIEF_BULLET_ANCHOR, BRIEF_BULLET + BRIEF_BULLET_ANCHOR, 1).replace(BRIEF_ENTRY_ANCHOR, BRIEF_ENTRY.rstrip('\n') + '\n\n' + BRIEF_ENTRY_ANCHOR, 1); W(BRIEF, b)
W(LOOP, read(LOOP).replace(LOOP_OLD, LOOP_NEW))
W(RES, RESUME_HEAD + read(RES)); W(RF, read(RF).replace(FORMS_OLD, FORMS_NEW))
W(STATEDOC, read(STATEDOC).rstrip('\n') + '\n' + STATE_ADD); W(ADD, read(ADD).rstrip('\n') + '\n' + ADDENDA_ADD); W(REC, rec)
W(WALK, read(WALK).replace(MEM_DESC_OLD, MEM_DESC_NEW).rstrip('\n') + '\n' + MEM_PARA); W(IDX, idx)
print('written: the map (+ the lesson-4 rider), the reading ledger\'s CORRECTION row, COMPILE_DEBT, MIDDOT, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP, RESUME, RECORD_FORMS, the state doc, the addenda, the recovery page, the memory note, the index')
LINT_AFTER = {p: lint(p) for p in FILES}
for p in FILES: print('  lint', p.replace(MEM, '<memory>'), LINT_BEFORE[p], '->', LINT_AFTER[p])
assert all(LINT_AFTER[p] == LINT_BEFORE[p] for p in FILES), 'a record moved the gloss lint'
