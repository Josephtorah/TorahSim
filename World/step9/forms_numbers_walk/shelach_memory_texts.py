import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
_MEMORY = _os.path.expanduser('~/.claude/projects/' + _os.path.abspath(_ROOT).replace('/', '-') + '/memory')   # THE PORTABLE REPO (2026-09-15): the memory folder as Claude Code names it, from the root
# THE NUMBERS WALK 4b — the records' final appends, run after the sweep prints (SWEEPLINE replaced by the sweep's own line).
import re, sys, os
SCR = os.path.dirname(os.path.abspath(__file__))
SWEEP = sys.argv[1]   # e.g. "run_cold_all 46/46 runners green, 5,299 graded cells (5,127 + Shelach's 172)"
def rep(p, a, b):
    s = open(p, encoding='utf-8').read(); assert s.count(a) == 1, (p, a[:70], s.count(a)); s = s.replace(a, b); open(p, 'w', encoding='utf-8').write(s)
def app(p, t):
    s = open(p, encoding='utf-8').read()
    if not s.endswith('\n'): s += '\n'
    open(p, 'w', encoding='utf-8').write(s + t)
R = _ROOT
# ---- NUMBERS_WALK.md: the sweep paragraph at the as-built's end ----
app(f'{R}/World/step9/NUMBERS_WALK.md', """
THE JOURNAL GATE AND THE SWEEP (the last two gates of the order): world_journal.py --gate GREEN — the running world's ledger 1,344 =
1,332 writes + 12 retro-writes, timers 49 = 49 set (48 fired, 1 pending — the thirty-eight years), its clock 152 = the markers; "the
replay is the audit". %s. Sitting 4b CLOSED (the state doc's #124). Numbers 1:1-15:31 is read, frozen, compiled and on the tape
(chapter 9 and 15:32-41 by THE TENT); the walk resumes at 16:1 on the ruling's form — read, then compile: chapter 16, Korach's reading.
""" % SWEEP)
# ---- THE_STEPS.md: the fourth compile paragraph in ## THE NUMBERS WALK ----
para = open(f'{SCR}/shelach_steps_para.txt', encoding='utf-8').read().replace('SWEEPLINE', 'Every gate and the sweep green (%s).' % SWEEP)
rep(f'{R}/THE_STEPS.md', "the Bible at that goat. Next: Shelach's compile (4b), then chapter 16.\n", "the Bible at that goat. Next: Shelach's compile (4b), then chapter 16.\n" + para)
# ---- THE_BRIEFING.md: the scoreboard bullet atop the list + the entry newest-first ----
entry = open(f'{SCR}/shelach_briefing_entry.txt', encoding='utf-8').read().replace('SWEEPLINE', 'Every gate green; %s.' % SWEEP)
rep(f'{R}/THE_BRIEFING.md', "## ENTRIES (newest first)\n\n", "## ENTRIES (newest first)\n\n" + entry)
bullet = ("- **SHELACH COMPILED — SITTING 4b DONE: THE PARSER READS FRACTIONS, UNIT NOUNS AND \"THE ONE\", THE LIBATION TABLE IS COMPUTED FROM THE INK, AND THE GEMARA'S \"FORTY DAYS MINUS ONE\" LANDS ON THE TAPE** (2026-09-10, on your \"Go\"; World/step9/NUMBERS_WALK.md \"Sitting 4b\"). "
          "The exam docket 313 rows (141 laws); thirty-four parser probes written to fail, then the fraction before a measure noun, the unit noun as one and the definite one taught — the corpus-wide diff read at a hundred and ten verses and three more false readings found by their vowels (the third generation as thirty, Sheshai as the sixth, the tithe verb as ten); "
          "cold_run_shelach.py 172 of 172 on the first graded run, the table computed from 15:4-10 and asserted at Exodus 29:40 and Numbers 28, the census set and the idolatry column called from earlier engines; the tape's seventeen lines and the Ninth of Av marker, the forty-day timer firing one day late (the inclusive count, open with Abaye's arm), the thirty-eight years pending at (40, 5, 9); "
          "the run tuple matched on the second run after the first caught a reused kind name and the timer rule; %s. Numbers 1:1-15:31 is read, frozen, compiled and on the tape. Next: chapter 16, Korach's reading.\n" % SWEEP)
rep(f'{R}/THE_BRIEFING.md', "## SCOREBOARD (as of 2026-09-10, latest)\n\n", "## SCOREBOARD (as of 2026-09-10, latest)\n\n" + bullet)
# ---- World/RESUME.md ----
app(f'{R}/World/RESUME.md', "SITTING 4b DONE 2026-09-10 (THE COMPILE OF SHELACH 13:1-15:31; NUMBERS_WALK.md \"Sitting 4b\" design + as-built): the docket 313 rows; the parser's fraction / unit noun / definite one taught with thirty-four probes to FAIL and three more homographs off the diff; cold_run_shelach.py 172/172 first graded run, law_shelach the 51st daemon, four engines CALLED; the tape's seventeen lines and the 13:25 marker (2, 5, 9), the forty days FIRED at (2, 5, 10) (CF2 DIVERGE, OPEN), the thirty-eight years PENDING (40, 5, 9); RUN (1136, 49, 48, 0, 12, 1332, 22, 284, four pairs, 101) matched on the second run; THE REST exact; 10/10; the journal gate GREEN; %s. NUMBERS 1:1-15:31 ON THE TAPE. Next: chapter 16 (Korach's reading), then its compile.\n" % SWEEP)
# ---- the state doc ----
state = open(f'{SCR}/shelach_state_entry.txt', encoding='utf-8').read().replace('SWEEPLINE', SWEEP)
app(f'{R}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', state)
# ---- memory: the ruling file, the lessons head, the index line ----
MEM = _MEMORY
rep(f'{MEM}/numbers-in-order-ruling.md', "THEN chapter 16 (Korach's reading) — never the next\nreading first.\nRelated:",
    "THEN chapter 16 (Korach's reading) — never the next\nreading first.\nSITTING 4b DONE 2026-09-10 — THE COMPILE OF SHELACH (NUMBERS_WALK.md \"Sitting 4b\" design + as-built; COMPILE_DEBT's sitting-4 line PAID): the docket\n313 rows (141 LAW); the parser taught THE FRACTION before a measure noun, THE UNIT NOUN AS ONE (the tenth, the cubit by its points, the hin) and\nTHE DEFINITE ONE (34 probes to FAIL, 110/110; the diff 110 verses read — three more homographs: the third generation as thirty, Sheshai as the\nsixth, the tithe verb as ten); cold_run_shelach.py 172/172 first graded run, law_shelach the 51st, the libation table COMPUTED from 15:4-10 and\nasserted at Exod 29:40 / Num 28, bamidbar / chatat / offerings / minchah CALLED; the tape's seventeen lines + the 13:25 marker (2, 5, 9); the forty\ndays FIRED at (2, 5, 10) — CF2 DIVERGE (the inclusive count; tammuz_length's Abaye arm), the thirty-eight years PENDING (40, 5, 9) — CF3; RUN\n(1136, 49, 48, 0, 12, 1332, 22, 284, four pairs, 101) matched on the second run (the first caught the REUSED KIND report_given and CS7's\nunscoped count); THE REST exact; 10/10; the journal gate GREEN; %s. NUMBERS 1:1-15:31 READ, FROZEN, COMPILED AND ON THE TAPE.\nNEXT: CHAPTER 16 — Korach's reading (16:1-18:32; the Sifrei silent on 16-17, piska 116 at 18:1; chapter 18 pays the challah's terumah pointer), then\nits compile (5b) — never the next reading first.\nRelated:" % SWEEP)
rep(f'{MEM}/numbers-in-order-ruling.md', "SITTING 4 SHELACH 13:1-15:31 READ AND FROZEN 2026-09-10 (190 units; the Sifrei silent on 13-14; the fraction class); NEXT the compile of Shelach (4b), then chapter 16\"",
    "SITTING 4 SHELACH 13:1-15:31 READ AND FROZEN 2026-09-10 (190 units; the Sifrei silent on 13-14; the fraction class); SITTING 4b DONE 2026-09-10 (the compile: the fraction / unit noun / definite one taught, 172/172, the Ninth of Av on the tape); NEXT chapter 16, Korach's reading\"")
les = ("⚠ THE NUMBERS WALK sitting 4b — THE COMPILE OF SHELACH (2026-09-10): A KIND'S NAME IS CHECKED AGAINST THE REGISTRY BEFORE IT IS TYPED — the types script printed \"23 of 24 added\" and the hand did not read it; report_given was the Joseph story's kind, and THE REST (the tape minus the newest runner) came back one write heavy: the branch seat-guarded, both registry rows annotated (the shared-kind lesson's sixth instance, at the naming step). A TIMER'S SETTING IS NOT A LEDGER WRITE — its entry lands at the FIRE; a PENDING timer has no entry (the narrative's prediction counts effects less timers plus fires; the RUN tuple's writes likewise). AN EDGE IS A CALL EXPRESSION, NOT AN ATTRIBUTE (BM.TOTAL left the bamidbar edge dead in the dependency gate). THE STITCHER'S MARKERS ARE ITS OWN TABLE — a scene's w.marker never reaches the tape; the mk row is typed with its numbers and verified. THE OLD CHECKPOINT KEEPS ITS VERSES, AGAIN (CS7 scoped to Exodus when Shelach's tenth trial landed; CF6 counts the whole). A FRACTION READS ONLY BEFORE A MEASURE NOUN — Exod 12:29's \"half of the night\" (the exodus marker) is the tripwire. THE UNIT NOUN'S HOMOGRAPHS ARE TOLD BY THE POINTS (the cubit's patach-and-dagesh against the maidservant's qamats and the mappiq of \"her mother\"); the class beyond the tenth, the cubit and the hin NAMED AND LEFT. THE DEFINITE ONE CLOSES ITS PHRASE BUT JOINS A CONJOINED NUMERAL (\"the one and twentieth\", Exod 12:18 — read off the diff). THE ORDINAL READER HAS HOMOGRAPHS (Sheshai). THE PREFIXED FORM, AGAIN (Joshua's eighth seat, Hoshea at Deut 32:44, Nehemiah's dough-word). A COUNT NAMES ITS UNIT — distinct words or tokens (the attributes' eleven against seventeen). A YAML NOTE IS VALIDATED BEFORE THE GATES CHAIN STARTS. THE DOCKET'S VERDICT ROWS GLOSS EVERY HEBREW-DERIVED WORD, HYPHENATED COMPOUNDS TOO (\"karet-class\", \"tanna\").\n")
p = f'{MEM}/step9-exam-era.md'
s = open(p, encoding='utf-8').read()
a = "## STANDING LESSONS AND WATCHES (moved verbatim from the MEMORY.md index line on 2026-09-07 to keep the index under its size limit; the W4/W3/W2/W1/D9/G/E lesson tail as it stood)\n"
assert s.count(a) == 1; s = s.replace(a, a + les); open(p, 'w', encoding='utf-8').write(s)
# ---- MEMORY.md index line ----
p = f'{MEM}/MEMORY.md'
s = open(p, encoding='utf-8').read()
a = "13:1-15:31 READ AND FROZEN (4, 2026-09-10: the Sifrei SILENT on 13-14; 121 sources; 30 claims; 190 units, standing 1959; THE FRACTION a parser class) — UNCOMMITTED since 0a98276. NEXT: sitting 4b SHELACH'S COMPILE (the ninth-of-Av marker, the forty-day / forty-year timers, the libation table, the fraction), then chapter 16."
assert s.count(a) == 1, s.count(a)
s = s.replace(a, "13:1-15:31 READ, FROZEN AND COMPILED (4 + 4b, 2026-09-10: the Sifrei SILENT on 13-14; 190 units, standing 1959; the parser reads the FRACTION before a measure noun, the UNIT NOUN as one, THE DEFINITE ONE — 110/110, the diff's three more homographs; cold_run_shelach.py 172/172, law_shelach the 51st; the Ninth of Av marker, the forty days FIRED a day late (CF2 OPEN), the thirty-eight years PENDING; RUN (1136, 49, 48, 0, 12, 1332, 22, 284, four pairs, 101); the shared kind report_given caught by THE REST) — UNCOMMITTED since 0a98276. NEXT: chapter 16, KORACH'S READING (16:1-18:32; then its compile 5b).")
open(p, 'w', encoding='utf-8').write(s)
print('records appended; MEMORY.md bytes', os.path.getsize(p))
