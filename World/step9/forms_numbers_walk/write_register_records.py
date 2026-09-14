#!/usr/bin/env python3
# THE REGISTER GATE sitting (2026-09-11): the appends — THE_LOOP.md's as-built, COMPILE_DEBT.md's box, RESEARCH_LOG.md's entry, the state doc's
# #137, World/RESUME.md's line. THE_BRIEFING, THE_STEPS and the memory files are edited by the Edit tool beside this script.
import os
ROOT = '<repo-old>'
def append(path, text):
    assert os.path.exists(path), path
    with open(path, 'a') as f: f.write(text)
    print('appended %d bytes -> %s' % (len(text.encode()), path))

LOOP = '''
## As built — THE REGISTER GATE (2026-09-11; the owner: "Ok go" on the recommendation's item 2; the design above written first, the probes
## to FAIL 0/6 before the code, then 6/6; the gate GREEN under --strict with 104 declared seats)

THE FILES: World/step9/register_census.py (the gate — read_ink / running_world / count_lines / receipts / footers / register_headers, the four
class_* functions, verify, gate; --strict / --emit / --no-index), register_probes.py (R1-R6), register_dispositions.yaml (the 104 whys),
REGISTER_INDEX.md (written each run). Nothing built into the engine: no table, no row, no column, no daemon.

THE FIRST RUN READ (non-strict, --emit): 118 debt seats, 0 fails — and the reading found the finder's own faults before the world's: ten count
lines UNPAIRED because the run-finder matched number-word stems inside PROPER NAMES and ORDINALS (Issachar's שש "six" inside יששכר "Issachar",
ושנים "and second" at Num 2:16, ושני "and the years of" at Exod 6:16, השבעי "the seventh" at Exod 12:15) — the token census's homograph lesson at a
third seat. THE FIX: the finder now runs on THE PARSER'S OWN TOKENS (cold_run_sequence.verse_words, aligned one-to-one with the DB's words), whose
markers decide — a STAR is a homograph the points refused (not a numeral), a percent sign a fraction, an at sign the unit noun as one, the hash /
caret / tilde forms their own keys in UNITS — and two rules of the ink joined the unit rule: THE DUALS carry their unit inside the token
("two years" שנתים, "two days", "two cubits", "twice") and are measures; and ONE IS NEVER A CHECKSUM ("one soul", "one man for his father's house",
"on the first of the month" — a register's total is never one). Second run: no UNPAIRED line; 104 debt seats — counts NONE 21 / ELSEWHERE 14
(41 MEASURE-ONLY, 29 ROW, 3 LEDGER green), receipts NONE 21 / ACT 18 / EVENT 5 / CHAPTER 5 (9 CLOSE green), footers EMPTY 5 (4 DAEMONS), registers
NONE 15 (3 ROWS). Every why typed from the reading of the print (scratchpad write_register_dispositions.py — the classes taken from the gate's
computation, never typed; verify() clean before the write); the strict run GREEN; the probes 6/6.

WHAT THE GATE FOUND ON THE WORLD (the ledger's honest state, now declared, not fixed by hand):
- THE SPEC'S COMMANDS ARE NOT DEBITS — 18 receipts whose act is on the ledger at the verse (the veil hung, the bread set, the lamps, the incense,
  the tamid, the washing, the garments' blocks, the milluim's blood, the eighth day's acceptance, the omer jar, the tablets, Aaron's staff) with
  NOTHING CLOSED, because the command each answers is a specification (Exodus 25-31, Leviticus 8's instructions) the tape never wrote as a
  debit; plus 5 receipts whose event fires and writes nothing at the verse. The command-and-receipt pair closes only where the command was
  itself an EVENT (Num 1:19, 3:42, 3:51, 8:3, 8:22, 20:27, and the tent's cases 24:23, 15:36, 27:11) — nine CLOSE. Filed as a debt CLASS
  (COMPILE_DEBT.md): a debit per spec command would let these receipts close.
- THE STORY'S SCENE GAPS — receipts with no event at the verse: Exod 7:6, 7:10 (the staff-serpent), 39:1 (the garments' heading), 40:19 (the tent
  spread), Lev 8:4 (the assembly); Lev 16:34's "and he did as the LORD commanded" with no narrated rite; Num 36:10's receipt ONE VERSE BEFORE the
  act (the marriage fires at 36:11-12 — declared, not moved).
- THE RECEIPT INSIDE A COMMAND — Lev 9:7, 10:15, Num 26:4: the formula quoted inside a command or a speech, not a receipt of an act.
- THE REGISTERS THE TABLE DOES NOT HOLD: the camps (Num 2 — the Bamidbar runner's four sums as cells), the service roll (Num 4 — Naso's cells),
  the shekel account (Exod 38 — a metals ledger), Genesis 46's four sub-totals and the 66 / 70 (the Joseph runner's ROSTERS and CJ3b), the
  spies' and the princes' name lists; Genesis' eight name trees (the named grain on the tape and in the entity registry); chapters 30-36 and
  Deuteronomy not yet walked. Each a declared seat; the seeding stays FILED.
- THE PARSER'S NEXT HOMOGRAPH — Gen 41:34 וְחִמֵּשׁ ("and let him take a fifth") read as FIVE: the tithe-verb class (a verb on a numeral stem);
  filed for the parser's next teaching (RESEARCH_LOG.md).

THE LAW OF THE DISPOSITIONS IN FORCE: a declared class that differs from the computed one FAILS (a lie); a declaration on a seat the world has
since paid FAILS (stale — delete the line when a runner pays the seat); an undeclared non-green seat is debt, FAIL under --strict. The gate
runs at every compile sitting's gates step (THE_STEPS' compile checklist), not in run_cold_all.py.
'''

DEBT = '''
## THE REGISTER GATE SITTING (2026-09-11, after the discussion step; THE_LOOP.md "THE REGISTER GATE — the design" + "As built"; the owner: "Ok go"):
## register_census.py GREEN under --strict (104 declared seats), register_probes.py 0/6 -> 6/6. THE DEBT CLASSES THE GATE SURFACED (each seat declared
## in register_dispositions.yaml — DELETE a seat's line when a runner pays it, the gate says STALE until it is gone): (a) THE SPEC'S COMMANDS ARE NOT
## DEBITS — 18 ACT + 5 EVENT receipts (Exod 16:34, 34:4, 39:5-43, 40:21-32, Lev 8:9-29, 9:10, Num 17:26; Exod 7:20) whose act is on the ledger with
## nothing closed: a debit per spec command (the sanctuary spec Exod 25-31, the milluim's instructions Lev 8, the jar, the tablets, the staff) would
## let them close — a wrap item for the sanctuary / milluim / story runners; (b) THE STORY'S SCENE GAPS — Exod 7:6, 7:10, 39:1, 40:19, Lev 8:4 fire no
## event at the receipt's verse; Lev 16:34's rite unnarrated; Num 36:10's receipt one verse before the act (declared, not moved); (c) THE REGISTERS
## WITHOUT ROWS — the camps (Num 2), the service roll (Num 4), the shekel account (Exod 38), Genesis 46 / Exod 1 (the seventy), the name trees of
## Genesis: each a register at its own marker under the seeding's design, built only when a consumer calls; (d) THE PARSER'S FIFTH-VERB HOMOGRAPH —
## Gen 41:34 "take a fifth" read as five (the tithe-verb class): teach at the next parser sitting with a probe; (e) 27:15-23 (Joshua) uncompiled
## — the 8b line stands; (f) chapters 30-36 and Deuteronomy: the walk's own future (Num 31's booty counts, 34's princes, 36:13's Moab block, the
## eight Deuteronomy receipts and four footers).
'''

RESEARCH = '''
## 2026-09-11 — THE REGISTER GATE'S FIRST RUN: THE FINDER'S OWN HOMOGRAPHS, THE PARSER'S STAR AS THE SIGNAL, ONE IS NEVER A CHECKSUM, THE FIFTH-VERB
## READ AS FIVE, AND THE RECEIPTS' CENSUS ON THE LEDGER (THE_LOOP.md "THE REGISTER GATE")

1. THE FINDER'S OWN HOMOGRAPHS. The first run-finder matched number-word stems by regex on the DB's consonantal words and paired the runs to the
   parser's values; ten count lines came back UNPAIRED because the stems live inside PROPER NAMES and ORDINALS — יששכר ("Issachar") holds שש
   ("six"), וּשְׁנִים ("and second", Num 2:16) and וּשְׁנֵי ("and the years of", Exod 6:16) hold שני, הַשְּׁבִיעִי ("the seventh", Exod 12:15) holds שבע. The
   token census's lesson (a roll of names is a field of homographs) at a third seat, on our own instrument.
2. THE PARSER'S STAR IS THE SIGNAL. cold_run_sequence.verse_words returns one token per DB word and MARKS its decisions: a star on a word the points
   refused as a numeral (ושנים*, ושני*, השבע*), a hash on a suffixed numeral (שני# for שניהם "the two of them"), a caret on the construct two, a
   tilde on a dual, a percent on a fraction, an at sign on the unit noun as one, a bar on the disjunctive. The gate's finder now reads those
   marks instead of guessing: no UNPAIRED line remains on 108 count lines. Measured: the tokens align one-to-one with the DB's words at every
   count line (a mismatch falls to UNPAIRED, never silent).
3. ONE IS NEVER A CHECKSUM. Eleven count lines carry the numeral one beside "soul" or "the number" — "one soul" (Lev 4:27, 5:4, 5:17, Num 15:27,
   35:30), "one man for his father's house" (Num 1:44), "on the first of the month" (Num 1:18), "one of the commandments" (Num 15:12) — the law's
   individual or a date, never a register's total. The rule joined the unit rule (a numeral followed by year / day / month / gerah / talent /
   shekel / city / man is a measure) and the duals (the unit inside the token: שנתים "two years"). 41 of the 108 lines are measure-only.
4. THE FIFTH-VERB READ AS FIVE. Gen 41:34 וְחִמֵּשׁ אֶת־אֶרֶץ מִצְרַיִם ("and let him take a fifth of the land of Egypt") — the parser returns 5: a verb on
   the numeral stem, the tithe-verb's class (עַשֵּׂר "tithe" read as ten, taught at 4b). Filed for the parser's next teaching with its probe; the
   gate carries the seat declared.
5. THE COUNT-NOUN VARIES. The ink's checksum lines say "the counted" (פְּקֻדֵיהֶם — Num 1, 2, 26), "the number" (בְּמִסְפַּר — Num 3:28's 8,600, 3:43's
   22,273), "souls" (נֶפֶשׁ — Genesis 46's five totals, Exod 1:5, Num 31's persons), or NOTHING (Simeon's bare footer at 26:14: "these are the
   families of the Simeonites, 22,200"). A gate anchored on one noun would miss a tribe; the union of the three nouns and the footer form reads
   all 108.
6. THE RECEIPTS' CENSUS ON THE LEDGER. Fifty-eight "as the LORD commanded" lines: nine close a ledger entry at the verse (every one where the
   command was itself an event or a tent case); eighteen have the ACT on the ledger with nothing closed — the command a specification the tape
   never wrote as a debit; five fire an event that writes nothing at the verse; five have a close in the chapter, not at the verse; twenty-one
   have nothing (five story-scene gaps, one unnarrated rite, three formulas quoted inside commands, twelve in unwalked chapters). The ink's
   command-and-receipt pair is a ledger form the machine writes only where the command was an event: a debt class, now declared.
'''

STATE = '''
═══ COMPACTION POINT #137 (2026-09-11 — written at the close of THE REGISTER GATE SITTING; THE GATE GREEN UNDER --strict, THE PROBES 6/6; NOTHING BUILT INTO THE ENGINE; NEXT CHAPTER 28) ═══
STATE: the engine as #134 — 201 frozen units, standing 2075, hash 8b8fff1fa28953af UNMOVED; 50 runners, 55 daemons, the sweep 50/50 at 5,788 (unmoved — no runner changed); RUN (1244, 52, 52, 0, 12, 1469, 26, 302, the four pairs, 114). NEW FILES: World/step9/register_census.py (the gate), register_probes.py (R1-R6, 0/6 -> 6/6), register_dispositions.yaml (104 declared seats), REGISTER_INDEX.md (gate-written). Nothing committed since a42f518.
THE SITTING (the owner: "Ok go" on item 2; THE_LOOP.md "THE REGISTER GATE — the design" written after the measurements and before the probes; "As built" after): the gate reads FOUR censuses off the Tanakh DB — A the count lines (a count-noun "the counted" / "the number" / "souls" or a register footer with a numeral; THE UNIT RULE classes each numeral: a unit noun within two tokens after it, a dual with the unit inside, or ONE = a measure; the rest counts → ROW / LEDGER / ELSEWHERE / NONE), B the receipts "as the LORD commanded" (58 → CLOSE / ACT / EVENT / CHAPTER / NONE), C the footers "these are the statutes / commandments / judgments / words / testimonies" (9: 7 FOOTER + 2 HEADER by the verb; the block by the neighbours; the stamp sinai / moab / jordan; DAEMONS / EMPTY by the daemons' given_at), D the registers (the 68 "these are + generations / names / sons / families / the counted" headers in 18 chapters → ROWS / NONE) — and checks the population table, the ledger and daemon_dispositions.yaml's given_at. THE DISPOSITIONS' LAW: a lie FAILS, a stale declaration FAILS, an undeclared non-green seat is debt (FAIL under --strict); --emit prints stubs, the why typed from the reading. THE FIRST RUN READ: 118 debt, 0 fails, TEN UNPAIRED lines — the finder's own homographs (number-word stems inside Issachar, "and second", "the seventh") → the finder rewritten on THE PARSER'S OWN TOKENS (verse_words' marks: the star = a refused homograph, hash / caret / tilde / percent / at) + THE DUALS + ONE IS NEVER A CHECKSUM; the second run 104 debt, no UNPAIRED; the whys written (scratchpad write_register_dispositions.py; verify clean); --strict GREEN; probes 6/6; gloss_lint 0 on every new file. COVERAGE: counts 108 (ROW 29, LEDGER 3, MEASURE-ONLY 41, ELSEWHERE 14, NONE 21); receipts 58 (CLOSE 9, ACT 18, EVENT 5, CHAPTER 5, NONE 21); footers 9 (DAEMONS 4, EMPTY 5); registers 18 (ROWS 3, NONE 15).
THE FINDINGS (RESEARCH_LOG.md's entry; COMPILE_DEBT.md's box): THE SPEC'S COMMANDS ARE NOT DEBITS (18 ACT + 5 EVENT receipts — the act on the ledger, nothing closed; the pair closes only where the command was an event: nine CLOSE) — a debt class; the story's scene gaps (Exod 7:6, 7:10, 39:1, 40:19, Lev 8:4), Lev 16:34's unnarrated rite, Num 36:10's receipt one verse before the act; the formula inside a command (Lev 9:7, 10:15, Num 26:4); the registers without rows (the camps, the service roll, the shekel account, Genesis 46 / Exod 1, the name trees) — the seeding FILED unchanged; THE FIFTH-VERB HOMOGRAPH (Gen 41:34 read as five — the parser's next teaching); the count-noun varies (Simeon's bare footer).
THE RECORDS: THE_LOOP.md (design + as-built); COMPILE_DEBT.md's register-gate box; RESEARCH_LOG.md's six-finding entry; THE_STEPS' compile checklist (the register gate's line at the gates step); THE_BRIEFING's scoreboard bullet and entry; World/RESUME.md; memory (numbers-in-order-ruling.md NEXT, MEMORY.md's bullet, step9-exam-era.md's lessons head). LAST COMMIT a42f518; UNCOMMITTED: sitting 8's, 8b's, the discussion step's and this sitting's paths — commit only on "commit push".
NEXT on the ruling: CHAPTER 28 — the reading (the portion opening at 28:1: the daily and festival offerings; the Sifrei's piskaot by position; the parser measured on the chapter's own numbers; the draft's grain at both ends; chapter 27 FROZEN at THE TENT and skipped), THEN its compile (28b) on 1b's order with the register gate at the gates step — never the next reading first.
POST-COMPACTION REREADS (mandatory, first sitting): numbers-in-order-ruling.md + this entry + NUMBERS_WALK.md "Sitting 8" (the reading's form) + "Sitting 8b — AS BUILT" (the compile's form) + THE_STEPS Step 2 + Step 5 + the compiler block; memory's STANDING LESSONS head. WATCHES: as #136's + THE REGISTER GATE RUNS AT EVERY COMPILE SITTING (--strict; a paid seat's line DELETED, else STALE) + THE PARSER'S STAR IS THE HOMOGRAPH SIGNAL (never a stem regex on names) + ONE IS NEVER A CHECKSUM + THE SPEC'S COMMANDS ARE NOT DEBITS (a class, declared — never a close faked) + THE FIFTH-VERB HOMOGRAPH OWED TO THE PARSER.
'''

RESUME = '''THE REGISTER GATE SITTING DONE 2026-09-11 (the owner: "Ok go" on the recommendation's item 2; THE_LOOP.md "THE REGISTER GATE — the design" + "As built"): World/step9/register_census.py reads the ink's own formulas off the Tanakh DB — 108 count lines (the unit rule, the duals, one never a checksum), 58 receipts "as the LORD commanded", 9 law-block footers and headers, 68 register headers in 18 chapters — and checks the population table, the ledger and the installation registry; probes 0/6 -> 6/6; the first run read (the finder's own homographs fixed by the parser's marks); 104 seats declared with a why (register_dispositions.yaml — a lie or a stale line fails); GREEN under --strict; nothing built into the engine. The debt classes surfaced: the spec's commands are not debits (18 + 5 receipts), the story's scene gaps, the registers without rows, the fifth-verb homograph. NEXT: CHAPTER 28 — the reading, then its compile with the gate at the gates step.
'''

append(f'{ROOT}/World/step9/THE_LOOP.md', LOOP)
append(f'{ROOT}/World/step9/COMPILE_DEBT.md', DEBT)
append(f'{ROOT}/RESEARCH_LOG.md', RESEARCH)
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', STATE)
append('<world-link>/RESUME.md', RESUME)
