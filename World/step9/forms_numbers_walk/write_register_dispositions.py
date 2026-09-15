import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE REGISTER GATE sitting (2026-09-11): the dispositions written FROM THE READING of the second run's print (register_gate_run2.out) —
# a why per non-green seat; the classes taken from the gate's own computation (never typed); verify() run before the write.
import sys, io, contextlib, collections, yaml
sys.path.insert(0, (_ROOT + '/World/step9'))
import register_census as RG
with contextlib.redirect_stdout(io.StringIO()):
    ink = RG.read_ink(); w = RG.running_world()
computed = {'counts': RG.class_counts(ink, w), 'receipts': RG.class_receipts(ink, w), 'footers': RG.class_footers(ink), 'registers': RG.class_registers(ink, w)}

SEEDING = "the backward seeding is FILED (COMPILE_DEBT.md's sitting-8b box: a register at its own marker, no roll-forward, built when a consumer calls)"
NOT_WALKED = "chapters 30-36 are NOT YET WALKED (the walk stands at chapter 28) — the seat waits for its reading and compile"
DEUT = "Deuteronomy is not on the tape (the book not read) — the seat waits for its reading and compile"
SPEC = ("THE SPEC'S COMMANDS ARE NOT DEBITS: the act is on the ledger at this verse (%s) but the command it answers is a specification the tape "
        "never wrote as a debit, so nothing closes — the command-and-receipt pair is written only where the command was itself an event "
        "(Num 1:19, 3:42, 3:51, 8:3, 8:22, 20:27); filed as a class — a debit per spec command would let these receipts close")
COUNTS = {
    'Gen 41:34': "the parser reads the verb וְחִמֵּשׁ (\"and let him take a fifth\") as FIVE — a homograph of the tithe-verb class (a verb on a numeral stem read as the numeral); not a count, not a register; filed in RESEARCH_LOG.md for the parser's next teaching",
    'Gen 46:15': "the descent roster's sub-total by mother (Leah's thirty-three) — the NAMED grain's checksum; the Joseph runner holds the four registers as ROSTERS and asserts the sub-totals (seventy('subtotals_parsed')); no row on the table — " + SEEDING,
    'Gen 46:18': "Zilpah's sixteen — the named grain's checksum, the Joseph runner's cell; no row — " + SEEDING,
    'Gen 46:22': "Rachel's fourteen — the named grain's checksum, the Joseph runner's cell; no row — " + SEEDING,
    'Gen 46:25': "Bilhah's seven — the named grain's checksum, the Joseph runner's cell; no row — " + SEEDING,
    'Gen 46:26': "the sixty-six — the ink's declared total that DIFFERS from its parts (33 + 16 + 14 + 7 = 70; DATABASE_SPECULATION.md section 4.3); the Joseph runner's CJ3b DIVERGE cell holds it; no row — " + SEEDING,
    'Gen 46:27': "the seventy with Joseph's two sons — the restated total (Exod 1:5 and Deut 10:22 repeat it); the Joseph runner's cell; no row — " + SEEDING,
    'Exod 1:5': "the seventy restated at the book's head — the Joseph runner's cell; no row — " + SEEDING,
    'Deut 10:22': "the seventy restated in Deuteronomy — " + DEUT,
    'Num 2:9': "the east camp's sum (Judah, Issachar, Zebulun = 186,400) — the Bamidbar runner computes and asserts the four camp sums from chapter 1's counts as cells (cold_run_bamidbar.py); the camps are not a table on the population table — a register the compile of 1b asserted, not seeded; no consumer",
    'Num 2:16': "the south camp's sum (151,450) — the Bamidbar runner's cell; the camps are not on the table (as 2:9)",
    'Num 2:24': "the west camp's sum (108,100) — the Bamidbar runner's cell; the camps are not on the table (as 2:9)",
    'Num 2:31': "the north camp's sum (157,600) — the Bamidbar runner's cell; the camps are not on the table (as 2:9)",
    'Num 4:36': "the service roll (thirty to fifty) — the Kohathites' 2,750, asserted by the Naso compile as a cell (cold_run_naso.py); the service roll is not on the table (the table began at 8b with the two censuses); a consumer would be the Levite service daemon — no row",
    'Num 4:40': "the Gershonites' 2,630 — the Naso compile's cell; the service roll is not on the table (as 4:36)",
    'Num 4:44': "the Merarites' 3,200 — the Naso compile's cell; the service roll is not on the table (as 4:36)",
    'Num 4:48': "the service roll's total 8,580 — the Naso compile's cell; the service roll is not on the table (as 4:36)",
    'Num 31:35': "the booty's persons (32,000) — " + NOT_WALKED,
    'Num 31:36': "the half of the sheep (337,500) — " + NOT_WALKED,
    'Num 31:40': "the persons' half (16,000) and the tribute (thirty-two souls) — " + NOT_WALKED,
    'Num 31:46': "the congregation's half of the persons (16,000) — " + NOT_WALKED,
    'Exod 38:26': "the shekel account restates the census total 603,550 (a beka a head, 'from twenty years old and upward'); the count's row is chapter 1's (as_of Num 1:17-19) — the account is the same number at an earlier page, its arithmetic the incense_shekel runner's cell; no row of its own",
    'Num 2:32': "the total restated at the camps' close; the ledger's counted status is chapter 1's (case_source Num 1:17-19) — a restatement, not a second count",
}
for v in (4, 6, 8, 11, 13, 15, 19, 21, 23, 26, 28, 30):
    COUNTS['Num 2:%d' % v] = "chapter 2 restates chapter 1's tribe count inside the camp order; the row is chapter 1's (as_of Num 1:17-19) — a restatement, not a second count"
RECEIPTS = {
    'Exod 7:6': "\"and Moses and Aaron did so, as the LORD commanded them\" — the exodus story's scene fires the plagues at their act verses (7:20 has its event); the receipt's own verse fires nothing — a scene gap of the story runner, filed",
    'Exod 7:10': "the staff become a serpent before Pharaoh — the story runner has no event at 7:10 (the sign is not on the tape); a scene gap, filed",
    'Exod 39:1': "the garments' heading (\"of the blue... they made the garments of service\") — the garment_made events fire at 39:5-31; the summary line fires none",
    'Exod 40:19': "\"he spread the tent over the tabernacle\" — the erection scene fires 'erected' at 40:17-18 and the furnishing at 40:20-33; the tent-spreading verse fires nothing — a scene gap, filed",
    'Lev 8:4': "\"and Moses did as the LORD commanded him; the congregation assembled\" — the milluim scene opens at 8:6 (the washing); the assembling fires none",
    'Lev 9:7': "the formula inside Moses' COMMAND to Aaron (\"offer... as the LORD commanded\") — a command line citing the command, not a receipt of an act",
    'Lev 10:15': "the formula inside Moses' speech on the breast and the thigh — a citation of the law, not a receipt of an act",
    'Lev 16:34': "\"and he did as the LORD commanded Moses\" — the Day of Atonement's rite is a law spec on the tape, no narrated performance: the receipt has no act to close (the tradition reads the subject as Aaron's first rite); filed",
    'Num 31:7': NOT_WALKED, 'Num 31:31': NOT_WALKED, 'Num 31:41': NOT_WALKED, 'Num 31:47': NOT_WALKED,
    'Num 36:10': "\"as the LORD commanded Moses, so did the daughters\" — the receipt the verse BEFORE the act: the Zelophehad runner's marriage fires at 36:11-12; a one-verse offset between the ink's receipt and the tape's act, declared and not moved",
    'Exod 12:28': "\"and the children of Israel went and did as the LORD commanded\" — the Passover's commands close at the act verses of the same chapter (the blood on the doorposts, the going out at 12:51); the people's 'so did they' fires no event of its own",
    'Exod 12:50': "the same receipt after the Passover statute (12:43-49) — no event at the verse; the chapter's closes are the acts'",
    'Num 2:33': "\"the Levites were not counted among the children of Israel, as the LORD commanded\" — restates 1:47-49's exemption; no event at the verse; the chapter's close is the camp order's",
    'Num 26:4': "the receipt inside the command's own line (the roll's head — the first roll's generation named); the second census's debit closes at 26:51, not here",
    'Num 27:22': "Joshua's appointment (27:15-23) is NOT COMPILED — the 8b debt line; the chapter's close is the daughters' statute (27:11)",
}
for s in ('Deut 1:19', 'Deut 4:5', 'Deut 5:12', 'Deut 5:16', 'Deut 5:32', 'Deut 10:5', 'Deut 20:17', 'Deut 34:9'): RECEIPTS[s] = DEUT
EVENT_WHY = "the event (%s) fires at this verse and writes on other lines of its scene (the garments' blocks at 39:21 and 39:26; the sons' dressing writes nothing) — the receipt has no write and no close of its own: the spec's commands are not debits (the ACT class's why)"
FOOTERS = {
    'Num 36:13': "the block Numbers 30:17-36:13 — " + NOT_WALKED + "; the stamp 'in the plains of Moab by the Jordan of Jericho' waits for its daemons",
    'Deut 1:1': "the block (Num 36:13, Deut 1:1] holds no law; " + DEUT, 'Deut 4:45': DEUT, 'Deut 12:1': DEUT, 'Deut 28:69': DEUT,
}
REGISTERS = {
    'Gen 2': "\"these are the generations of the heavens and the earth\" (2:4) — the creation register: its rows are the ops ledger's (THE_WORLD.md's schema insight — containers and contents), not the population table's; no person, no count",
    'Gen 6': "Noah's generations (6:9) — the named grain lives on the tape (the born / died markers, the life eras); the ark's kind table is FILED — " + SEEDING,
    'Gen 10': "the nations table (family, tongue, land, nation — no counts) — the counted grain keyed by family with no numbers; FILED — " + SEEDING,
    'Gen 11': "Shem to Terah (11:10-32) — the named grain with NO totals (the checksum column dropped, DATABASE_SPECULATION.md 4.3); the tape's birth markers hold the rows",
    'Gen 25': "Ishmael's generations and names (25:12-18) — a name tree with the twelve princes (25:16); no count; the named grain is the entity registry's",
    'Gen 36': "Esau's generations — the largest name tree (fifteen headers, no counts); the names the registry's where the tape wrote on them; no consumer",
    'Gen 37': "\"these are the generations of Jacob\" (37:2) — a narrative heading opening the Joseph story, not a roster",
    'Gen 46': "the descent roster — the Joseph runner's four ROSTERS (34 / 16 / 14 / 7 names) with the sub-totals as cells; FILED — " + SEEDING,
    'Exod 1': "\"these are the names\" (1:1) — the seventy restated; the Joseph runner's cell; filed with Genesis 46",
    'Exod 6': "the heads of the fathers' houses (6:14-27) — the named grain of Moses' and Aaron's line with Levi's, Kohath's and Amram's years; the persons are the registry's; no count",
    'Exod 38': "\"these are the accounts of the tabernacle\" (38:21) — the shekel account: the incense_shekel runner's cells (the beka a head; 603,550); a metals ledger, not a population register — no row",
    'Num 2': "the camps — the Bamidbar runner's four camp sums as cells; the camps are not on the table",
    'Num 4': "the service roll — the Naso compile's cells (2,750 / 2,630 / 3,200 / 8,580); no rows",
    'Num 13': "the spies' names (13:4-16) — a name list, the Shelach runner's; no count",
    'Num 34': "the land's princes by name (34:17-29) — " + NOT_WALKED,
}
decl = {}
for sec, table in (('counts', COUNTS), ('receipts', RECEIPTS), ('footers', FOOTERS), ('registers', REGISTERS)):
    decl[sec] = {}
    for seat, d in computed[sec].items():
        if d['class'] in RG.GREEN[sec]: continue
        if seat in table: why = table[seat]
        elif sec == 'receipts' and d['class'] == 'ACT': why = SPEC % ', '.join(sorted({e for _, e, _ in d['evidence']}))
        elif sec == 'receipts' and d['class'] == 'EVENT': why = EVENT_WHY % ', '.join(sorted(set(d['evidence'])))
        else: why = ''
        decl[sec][seat] = {'class': d['class'], 'why': why}
missing = [(sec, s) for sec in decl for s, x in decl[sec].items() if not x['why']]
print('declared %d; missing whys %s' % (sum(len(v) for v in decl.values()), missing))
v = RG.verify(computed, decl)
print('verify: fails %s; debt %s; declared %d' % (v['fails'], v['debt'], len(v['declared'])))
if not missing and not v['fails'] and not v['debt']:
    head = ('# register_dispositions.yaml — THE REGISTER GATE\'s dispositions (2026-09-11; THE_LOOP.md "THE REGISTER GATE — the design"). Every\n'
            '# non-green seat of the four censuses (counts / receipts / footers / registers) with its class AS THE GATE COMPUTES IT and a why typed\n'
            '# from the reading of the print. The gate verifies the class (a lie fails), refuses a declaration on a seat the world has since paid\n'
            '# (stale), and fails an undeclared seat under --strict. GREEN needs no line: counts ROW / LEDGER / MEASURE-ONLY, receipts CLOSE, footers\n'
            '# DAEMONS, registers ROWS. When a runner pays a seat, DELETE its line here (the gate will say STALE until it is gone).\n')
    with open((_ROOT + '/World/step9/register_dispositions.yaml'), 'w') as f:
        f.write(head + yaml.safe_dump(decl, allow_unicode=True, sort_keys=False, width=200))
    print('written')
