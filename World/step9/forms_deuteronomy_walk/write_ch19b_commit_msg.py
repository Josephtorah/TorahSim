import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16b (LEAN): the commit message built from the prints — sittings 15, 15b (chapters 17-18 read and compiled), 16 (chapters 19-21 read) and 16b
# (chapters 19-21 compiled) in the lean form, together (uncommitted since f730559) — for the owner's word. The earlier sittings' own messages (commit_msg_ch17b.txt for
# 15/15b, commit_msg_ch19.txt for 16) folded in whole with their trailers stripped; the trailers once at the end. write_ch17b_commit_msg.py's form. RUN FROM THE REPO ROOT after the records.
import os, re, subprocess, ast, glob
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name):
    g = re.search(pat, text, re.M); assert g, (name, pat); return g.group(1)
def RL(pat, text, name):
    g = re.findall(pat, text, re.M); assert g, (name, pat); return g[-1]
TRAIL = 'Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01MiJCE3AxFHu3jksQa2GG21\n'
def strip_trailers(m):
    m = m.replace(TRAIL, '').rstrip('\n')
    assert 'Co-Authored-By' not in m and 'Claude-Session' not in m, 'the trailers stripped'
    return m
summ = rd(f'{SP}/ch19b_gates_SUMMARY.txt'); assert 'ALL GREEN' in summ, 'the chain not green — the tail files its demands first'
STEPS = re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ, re.M); CHAIN_S = sum(int(t) for _, _, t in STEPS)
SWEEP = R(r'(\d+/\d+) runners green', rd(f'{SP}/ch19b_gates/sweep.out'), 'the sweep')
run = rd(sorted(glob.glob(f'{SP}/ch19_runner_run*.out'))[-1]); MATRIX = RL(r'^MATRIX: (\d+/\d+)', run, 'the runner'); W = ast.literal_eval(R(r'^THE NARRATIVE: (\(.*?\)) \(the forty-five', run, 'the narrative'))[0]
NPAR = int(R(r'the parameters (\d+) \(in the registry', run, 'the parameters')); RBG = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: 64 rows — (\{.*?\});', run, 'the readback')
tapes = sorted(glob.glob(f'{SP}/ch19_tape_run*.out')); tape = rd(tapes[-1]); NRUN = len(tapes)
TAPE_CP = R(r'(\d+/\d+) checkpoints?', tape, 'the tape') if re.search(r'\d+/\d+ checkpoints?', tape) else R(r'checkpoints[^\n]*?(\d+/\d+)', tape, 'the tape')
seq = rd(f'{ROOT}/World/step9/cold_run_sequence.py'); RUN = R(r"^RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),", seq, 'RUN')
CASES = int(R(r'^CASES generated: (\d+)', rd(f'{SP}/ch19_cases_gen.out'), 'the cases'))
dep = rd(sorted(glob.glob(f'{SP}/ch19b_dependency_after*.out'))[-1]); NDEP = R(r'dispositions on file: (\d+ edges, \d+ pointers)', dep, 'the dispositions')
tim = [l.split('\t') for l in rd(f'{SP}/ch19b_timing.tsv').strip().split('\n') if l.split('\t')[1].startswith('16b')]; MACHINE_S = sum(int(t[2]) for t in tim)
PROBES = re.findall(r'^  (\w+): (\d+/\d+)$', rd(f'{SP}/ch19b_gates/probes.out'), re.M) if os.path.exists(f'{SP}/ch19b_gates/probes.out') else []
_reg = rd(f'{SP}/ch19b_gates/register.out'); REG = (re.search(r'(DECLARED \d+[^\n]*)', _reg, re.M) or re.search(r'(THE REGISTER GATE: GREEN)', _reg)).group(1)   # the register's own line form (the records writer's form; the first regex read a head the print does not carry)
EXAM = rd(f'{ROOT}/logic/oral_triage/deu_19_21_shoftim_ki_teitzei_exam_2026-09-25.md'); NROWS = len(re.findall(r'^- Mishnah [A-Za-z ]+ \d+:\d+ — LAW\.', EXAM, re.M))
m17 = strip_trailers(rd(f'{SP}/commit_msg_ch17b.txt')); m19 = strip_trailers(rd(f'{SP}/commit_msg_ch19.txt'))
HEAD = '''CHAPTERS 19-21 COMPILED IN THE LEAN FORM (SITTING 16b — THE LEAN PASS'S SIXTH SITTING AND ITS THIRD COMPILE, THE FIRST OVER THREE CHAPTERS: ONE RUNNER AND ONE DAEMON OVER THREE UNITS, THIRTEEN OWN-DAY LINES, THE TWENTY-EIGHT MISHNAH ROWS THE LEDGER CITES AT LEAST TWICE AS THE CASES, NO DOCKET, THE CHAIN ONCE — THE FULL PROCESS OWED) — THE THREE CITIES IN THE MIDST AND NONE ADMITTING UNTIL ALL SIX, THE WAY PREPARED AND THE BORDER IN THREE, THE MANSLAYER'S WORD FROM MAKKOT 2:8 IN THE SPINE'S OWN HEBREW, THE HATER'S CLOCK THE GORING OX'S, THE FOREST WHERE BOTH MAY ENTER, THE AVENGER BEYOND THE BOUNDARY EXEMPT BY BOTH ARMS, THE INNOCENT BLOOD PURGED AS PERSONS, ONE WITNESS FOR ANY INIQUITY BUILT FROM 17:6, THE WOMAN NOT A WITNESS BY 'TWO' 'TWO', THE INQUIRY WELL AT THREE VERSES, AS HE PLOTTED AND NOT AS HE DID, EYE IN EYE AS MONEY BY LEVITICUS 24:20'S OPERATOR, FEAR NOT PAID FROM 7:18, THE PRIEST ANOINTED FOR WAR AND THE FOUR TERRORS, WHO RETURNS AND WHO DOES NOT, THE FEARFUL THREE WAYS, THE GUARDS WITH IRON MALLETS, THE PEACE CALL WITH SIHON'S MESSENGERS THE TAPE'S OWN ACT, TRIBUTE AND SERVITUDE BOTH, MIDIAN'S STRICTER SENTENCE PAID TO ITS CHAPTER, THE BAN ON THE SIX NAMED WITH THE RECEIPT 20:17 BEHIND, THE TREE THAT IS NOT LIKE A MAN, THE HEIFER THAT CEASED WITH THE MURDERERS, A BLEMISH NO BAR, THE HOLY SPIRIT'S ANSWER A HEAVEN ENTRY, THE CAPTIVE'S NAILS AFTER R. AKIVA, THE RELEASE A DIVORCE, THE DOUBLE IN THE FATHER'S HELD PROPERTY WITH JACOB'S PORTION AND REUBEN'S STRENGTH THE TAPE'S OWN SEATS, THE STIPULATION AGAINST THE TORAH VOID, THE REBELLIOUS SON JUDGED BY HIS END WITH A TARTEMAR OF MEAT, AND THE HANGED RELEASED AT ONCE WITH THE CURSE THE REVILER'S; AND BENEATH IT SITTINGS 15, 15b AND 16 (CHAPTERS 17-18 READ AND COMPILED, CHAPTERS 19-21 READ) — ALL UNCOMMITTED SINCE f730559.

On the owner's words "Reread and go" (RUN A, after the compaction at #214) and "Reread and go" (RUN B, after the compaction at #215 — no commit word said, the compile opened on the uncommitted tree), 2026-09-25; World/step9/DEUTERONOMY_WALK.md "Sitting 16b — THE COMPILE OF CHAPTERS 19-21 … LEAN" (the design and the AS BUILT); the state doc's #215, #216. RUN A: the recon over three chapters, the twenty-eight Mishnah rows COMPUTED from the reading's ledger (cited at least twice; 56 distinct citations) and read whole, the design (67 KB, lint 0), the callees' facts from twenty-three runners (106 facts, 2 fails read — the asks needing a case field asked otherwise), the probe Q45 to FAIL (44/45), the lean exam file (%d rows, lint 0), the types (13 kinds, 45 effects, the daemon law_refuge_war_family the 78th, the span three ranges, 23 CALL edges all reference, I5 78). RUN B: the tape tools and the shells derived from 15b's forms; cold_run_refuge_war_family.py the 73rd runner in five parts (part 1 derived — the helpers from the chapter 17-18 runner, the ink blocks from the reading's own instrument, the callees' facts typed from the print; parts 2-5 typed — nine cells and the readback's sixty-four rows, %d parameters and 83 DATA rows, the daemon with literal writes, thirteen lines, the narrative); %d cases generated from the cells' own asks; %s on the first graded run (%d writes on Israel, every one its first entry; the readback %s); the tape %s on run %d (RUN (%s, the four pairs, 127); DJ1-DJ5 the D series' tenth name); the scan census extended over the forty-five names; the dependency gate's demands read before the chain and filed at the tail (%s on file); THE GATES CHAIN ONE PASS ALL GREEN in %d s over %d steps (the probes %s; the register gate --strict %s; the sweep %s); %d timed steps, %d machine seconds. THE RECEIPT 20:17 dispositioned at the tail from the register gate's print — 7:1-5's line nations_devoted BEHIND, a run citation.

''' % (NROWS, NPAR, CASES, MATRIX, W, RBG, TAPE_CP, NRUN, RUN, NDEP, CHAIN_S, len(STEPS), PROBES, REG[:60], SWEEP, len(tim), MACHINE_S)
MSG = HEAD + '---- SITTING 16 (CHAPTERS 19-21 READ AND FROZEN, LEAN) — its own message as written at its close ----\n\n' + m19 + '\n\n---- SITTINGS 15 AND 15b (CHAPTERS 17-18 READ, FROZEN AND COMPILED, LEAN) — their own message as written at their close ----\n\n' + m17 + '\n\n' + TRAIL
assert not re.search(r'[֐-׿]', MSG) and MSG.endswith(TRAIL) and MSG.count('Co-Authored-By') == 1
open(f'{SP}/commit_msg_ch19b.txt', 'w', encoding='utf-8').write(MSG)
print('commit_msg_ch19b.txt %d bytes (16b head %d; 16 folded %d; 15/15b folded %d)' % (len(MSG.encode()), len(HEAD.encode()), len(m19.encode()), len(m17.encode())))
