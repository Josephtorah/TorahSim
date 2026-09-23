#!/usr/bin/env python3
# 13b docket D2b — THE DOCKET'S CLOSE, ITS RECORDS (write_ch15b_d2a_point.py's form + the docket's own records from the sheet): part I re-checked as a partition of
# Bekhorot 25a-28b, the census COMPUTED; the whole docket's census READ FROM THE WRITER'S PRINT (write_ch15_docket.out); then, every text built first and the caps
# asserted: MIDDOT's docket entry appended (the walk's entries at the file's tail, 12b's form), MISHNAH_TOPICS' row notes appended to the tractates read (the counts per
# tractate computed from the parts), the map's "THE DOCKET — AS RUN (D2b)" paragraph, the state doc's "#207 ADDENDUM 3", the recovery page's section-2 lines rewritten
# in place (<= 10,240), MEMORY.md's walk line (<= 17,000), the memory's deuteronomy-walk.md line appended; the D2b instruments copied to the forms folder.
import os, re, sys, ast, importlib.util, subprocess, shutil
from collections import Counter, OrderedDict
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
from ch15_docket_common import D2_UNIQUE, KIND_FIRST, long_range
from ch15_docket_crowns import crowns_d2b
DATE = '2026-09-23'; EXAM = 'deu_15_reeh_exam_2026-09-23.md'
RANGE = 'Bekhorot 25a-28b'; TARGET = [a for a in D2_UNIQUE if long_range(a) == RANGE]
ALL = OrderedDict(); VI = {}
for p in 'ABCDEFGHI':
    part = f'ch15_docket_{p}'; spec = importlib.util.spec_from_file_location(part, f'{SP}/{part}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    if p == 'I': assert m.WHOLE_STATS['corrected'] == 0
    for a, vd, n in m.ROWS:
        assert a not in ALL, ('overlap', a, p); ALL[a] = (vd, n)
        if p == 'I': VI[a] = (vd, n)
assert set(VI) == set(TARGET) and len(VI) == len(TARGET), (len(VI), len(TARGET))
def is_carried(n): return n.startswith('CREDITED (') and '; carried) — ' in n[:200]
def is_unres(n): return n.startswith('CREDITED (') and 'read whole here' in n[:400] and not is_carried(n)
N = len(VI); NL = sum(1 for a in VI if KIND_FIRST[a] == 'LINK'); NT = N - NL
cnt = Counter(vd for vd, _ in VI.values()); cl = Counter(vd for a, (vd, _) in VI.items() if KIND_FIRST[a] == 'LINK'); ct = Counter(vd for a, (vd, _) in VI.items() if KIND_FIRST[a] == 'TOPIC')
carried = sum(1 for vd, n in VI.values() if is_carried(n)); unres = sum(1 for vd, n in VI.values() if is_unres(n)); readhere = N - carried; own = N - carried - unres
LAWCELLS = Counter(mm.group(1) for vd, n in VI.values() if vd == 'LAW' and not n.startswith('CREDITED (') for mm in [re.search(r'\b(F[1-7])\b', n)] if mm)
NOUT = Counter(a.rsplit(':', 1)[0].split(' ')[1] for a, (vd, _) in VI.items() if vd == 'OUTSIDE')
unc = open(f'{SP}/ch15_docket_uncred_d2.out', encoding='utf-8').read()
um = re.search(r'\| Bekhorot 25a-28b (\d+) chunks (\d+)', unc); B_UNC, B_CH = int(um.group(1)), int(um.group(2)); bchunks = re.findall(r'B (ch15_uncred_d2b_\d+\.txt) rows (\d+)-(\d+) \((\d+) rows, (\d+) bytes\)', unc)
ur = re.search(r'\| Bekhorot (\d+) (\d+) bytes', unc); UB, UBB = int(ur.group(1)), int(ur.group(2))
assert B_UNC == own and UB == unres and len(bchunks) == B_CH, (B_UNC, own, UB, unres)
wo = open(f'{SP}/write_ch15_docket.out', encoding='utf-8').read()
wm = re.search(r'rows (\d+) link (\d+) topic (\d+) credited (\d+) \(link (\d+) topic (\d+) \) carried (\d+) unresolved_read_here (\d+) read_here (\d+) dup_dropped (\d+) (\[.*?\])', wo)
W_N, W_NL, W_NT, W_CR, W_CRL, W_CRT, W_CAR, W_UNR, W_RH, W_DUP = map(int, wm.groups()[:10]); W_DUPS = ast.literal_eval(wm.group(11))
W_VERD = ast.literal_eval(re.search(r'^verdicts (\{.*?\}) link', wo, re.M).group(1)); W_VL = ast.literal_eval(re.search(r' link (\{.*?\}) topic', wo).group(1)); W_VT = ast.literal_eval(re.search(r' topic (\{.*?\})$', wo, re.M).group(1))
W_LAW = ast.literal_eval(re.search(r'^LAW by cell (\{.*?\})$', wo, re.M).group(1)); W_OUT = ast.literal_eval(re.search(r'^OUTSIDE by work (\{.*?\})$', wo, re.M).group(1))
W_UNCITED = ast.literal_eval(re.search(r'UNCITED (\[.*?\])$', wo, re.M).group(1)); W_BYTES = int(re.search(r'^WROTE \S+ (\d+) bytes', wo, re.M).group(1))
assert W_N == len(ALL) == W_NL + W_NT and W_CAR + W_UNR == W_CR and W_RH == W_N - W_CAR, (W_N, len(ALL))
rows = [l.split('\t') for l in open(f'{SP}/ch15b_timing.tsv', encoding='utf-8').read().splitlines() if '\t13b D2b' in l]
TIM = '; '.join(f'{n} {s}s (at {t}, rc {r})' for t, n, s, r in rows)
census = (f'{N} addresses of {RANGE} (link {NL}, topic {NT}): LAW {cnt["LAW"]} / DERIVATION {cnt["DERIVATION"]} / DISPUTE {cnt["DISPUTE"]} / CONTEXT {cnt["CONTEXT"]} / OUTSIDE {cnt["OUTSIDE"]} '
          f'(the link rows {dict(sorted(cl.items()))}; the topic rows {dict(sorted(ct.items()))}); credited {carried + unres} — {carried} CARRIED, {unres} READ WHOLE HERE (the U file, now {carried * 0 + sum(1 for vd, n in ALL.values() if is_unres(n))} rows — every unresolved row of the carry); '
          f'{readhere} rows read whole in this run ({own} uncredited); LAW by cell, this docket\'s own notes {dict(sorted(LAWCELLS.items()))}; OUTSIDE by folio {dict(NOUT)}')
whole = (f'{W_N} addresses ({W_DUP} listed twice in the dump — {", ".join(W_DUPS)} — taken once; link {W_NL}, topic {W_NT}): LAW {W_VERD["LAW"]} / DERIVATION {W_VERD["DERIVATION"]} / DISPUTE {W_VERD["DISPUTE"]} / CONTEXT {W_VERD["CONTEXT"]} / OUTSIDE {W_VERD["OUTSIDE"]} '
         f'(the link rows {W_VL}; the topic rows {W_VT}); credited {W_CR} (link {W_CRL}, topic {W_CRT}) — {W_CAR} CARRIED with their ledgers\' own verdict lines, {W_UNR} READ WHOLE HERE; {W_RH} rows read whole in the three runs; '
         f'LAW by cell, this docket\'s own notes {W_LAW}; OUTSIDE by work {W_OUT}; THE ONE VERSE NO ROW CITES {["15:" + str(v) for v in W_UNCITED]} — the design\'s prediction (15:15, the memory verse) CONFIRMED BY COMPUTATION; the file {W_BYTES} bytes, lint 0')
# ---- MIDDOT's entry (12b's form — the walk's entries at the file's tail); every code checked in the file's tables before it was typed
MID = f'''
### THE DEUTERONOMY WALK 13b — THE DOCKET OF CHAPTER 15 ({DATE}, three runs; logic/oral_triage/{EXAM}, {W_N} rows — {W_CAR} carried, {W_RH} read whole here)
Every code checked in this file's tables before it was typed. I1 (the a fortiori): Kiddushin 15b:2 — Rabbi's a fortiori (the gentile's slave, redeemable by
relatives, surely freed by six years too) refuted by "by any of these" (Leviticus 25:54); Kiddushin 16a:14 — Reish Lakish's father's-death exit for the
maidservant from the signs, REFUTED at 16b:10 (the signs change her body, the death does not — the refutation's form); Bava Kamma 87b:6, Ketubot 43a:11, 58b:7 —
the equal board of 15:16 ("with you") carried to the daughter and the wife; Kiddushin 20b:20 (outside — the consecrator's field). I2 (the verbal analogy):
Kiddushin 14b:7, 20a:12, Arakhin 30a:19 — "hired worker" / "hired worker" (Leviticus 25:40, 25:53 / 15:18): the self-seller, the court's sale and the gentile's
sale one law — the acquisition by money, the redemption's lower price; the teacher who rejects it Rabbi (15a:23-15b:4); Kiddushin 17a:7 — "empty" / "empty"
(15:13 / Exodus 34:20): R. Meir's five sela; 17a:9 — the rival "empty" with the pilgrimage's (16:16) refused by "of that with which … blessed you"; 17a:10,
17a:13 — "giving" / "giving" with the gored slave's thirty (Exodus 21:32) and with the valuations' fifty (Leviticus 27:23); 17a:14 — "poverty" / "poverty"
(Leviticus 27:8 / 25:39) choosing the valuations; Kiddushin 15a:1-2 — "ear" / "ear" with the leper's right ear (Leviticus 14:14): THE DESIGN'S LABELED TRANSFER
AT ITS BAVLI SEAT; 20b:8 — "his redemption" / "his redemption" (Leviticus 25:52 / 25:26): no partial redemption; Arakhin 28b:7 — 111:1's "end" with 31:10 (the
sabbatical abrogates at its end); Arakhin 29a:18 — "well" / "well" (15:16 / Leviticus 25:50): the Hebrew slave's institution tied to the jubilee; Chullin
136b:18 — "flock" / "flock" proposed for the torn; 137a:4 — "shearing" / "shearing": the ox not shorn either; Niddah 40a:14 — "birth" / "birth" (Leviticus
22:27 / 15:19): the caesarean out; Rosh Hashanah 8b:7 — "year" / "year": the sabbatical's year from Deuteronomy's. I6 (general-particular-general): Bekhorot
37a:16-18 — "any blemish", "lameness or blindness", "any ill blemish": THE BLEMISH CLASS EXPOSED AND NOT REGENERATING (the design's I8 retyped I6 at the types —
the Bavli's own form; 37b:5 the particulars' own choice, I8's ground); Kiddushin 21b:8, 21b:6 — Rabbi's "you shall take", "the awl", "through his ear and into
the door": METAL; Kiddushin 17a:16 — "flock, threshing floor, winepress" the paradigm of the category of blessing (119:4's shape). THE AMPLIFICATION-RESTRICTION —
the rival method, no code, named: Kiddushin 21b:9 (R. Yosei son of R. Yehuda: anything but a corrosive), Bekhorot 37a:20. E28 (from the preceding): Kiddushin
15b:8 — R. Yosei HaGelili reads Leviticus 25:49's three redemptions by the verse preceding, R. Akiva by the verse following. THE JUXTAPOSITIONS — no code,
named: Kiddushin 14b:5 (the Hebrew man beside the Hebrew woman, 15:12 — the modes of acquisition), 14b:8 ("AND if a stranger" — the self-seller beside the
gentile's sale), 16a:2 ("if he takes another wife" — the maidservant beside a betrothed woman: the document), 19a:10, 19a:12 ("who did not designate her, then
he shall let her be redeemed" — the designation's timing), Bekhorot 26b:11-12 (Exodus 22:28-29 — the tending term's thirty and fifty; 26b:15 "the interpretation
of the verse was given only to the Sages"). THE DISPUTES AS PARAMETERS — named: the_severance_gift (Kiddushin 17a:5-14 — fifteen, thirty, fifty),
the_gift_feature (17a:16-17b:1; Bava Metzia 31b:9-10), the_awl_tool (Kiddushin 21b:5-11; Bekhorot 37b:10-11, 51a:15; Shevuot 4b:11), the_ear (Kiddushin
15a:1-2, 21b:7, 22b:2; Bekhorot 37b:12-13), the_three_cases (Kiddushin 14b:3-12; Bava Metzia 71a:10), the_exits_tables (Kiddushin 14b:2, 16a:10-16b:6, 17b:10,
18a:5), the_for_ever (Kiddushin 15a:17-22, 21b:4; Arakhin 29a:18; Bava Metzia 71a:14), the_awl_timing (Kiddushin 15a:4-5, 22a:3-6), the_double_hire
(Kiddushin 15a:11-12), the_release_object (Mishnah Sheviit 10:1-2; Makkot 3a:15; Shevuot 49a:2; Bava Batra 145b:2; Gittin 30a:16), the_prozbul (Gittin
36a:11-13, 37a:1; Mishnah Sheviit 10:3-4), the_release_territory (Gittin 36a:13-14; Kiddushin 38b:1, 38b:4; Tosefta Kiddushin 1:10; Arakhin 32b:15),
the_release_date (Arakhin 28b:7, 32b:18; Rosh Hashanah 8b:7; Mishnah Sheviit 10:2; Tosefta Sheviit 8:11), the_release_onset (Arakhin 32b:5, 32b:10),
the_measure_of_need (Ketubot 67b:2-15), the_needy_ranks (Bava Metzia 31b:7, 71a:3-4), the_blemish_class (Bekhorot 36b:9-16, 37a:16, 39a:15; Mishnah Bekhorot
5:3, 5:5), the_caesarean (Niddah 40a:14; Bekhorot 42a:11; Mishnah Bekhorot 2:9; Tosefta Bekhorot 3:2), the_firstlings_year (Bekhorot 26b:9, 27b:3-4; Temurah
21b:9), the_sanctify_for_value (Arakhin 29a:20; Nazir 4b:11). THE DISAGREES ROWS RESOLVED AS DATA: 15:17's maidservant against Exodus 21:7 (Kiddushin 15a:3,
15a:5, 15a:18 — she is never pierced; "likewise" reaches the gift, 17b:10-12); 15:19's "sanctify" against Leviticus 27:26 (Arakhin 29a:20; Nazir 4b:11 — for its
value, never for the altar).
'''
assert not re.search(r'[֐-׿]', MID)
# ---- MISHNAH_TOPICS row notes — the counts per tractate computed from the parts
def tract(works):
    rows = [(a, vd, n) for a, (vd, n) in ALL.items() if a.rsplit(' ', 1)[0] in works]; assert rows, works
    c = sum(1 for _, _, n in rows if is_carried(n)); return len(rows), c, len(rows) - c
NOTES = [  # (the line's prefix, the works, the spans, the point)
 ('**5. Mishnah, Seventh Year**', ['Mishnah Sheviit', 'Tosefta Sheviit'], 'Mishnah 10:1-9 and Tosefta Sheviit 8 whole', "the release's object and edges, Hillel's writ (the court's document) with its text, land condition and date, the manner 'I release it' (10:8), the oath released by the same word (Tosefta 8:8), the convert's sons (10:9 at Kiddushin 17b:18)"),
 ('**2. Mishnah, Corner of the Field**', ['Mishnah Peah'], '8:7-9', "the measure of need at Ketubot 67b:2-18 read whole — the house, the bed and the table, Hillel's horse, the loan turned gift"),
 ('**15. Mishnah, Shekels**', ['Mishnah Shekalim'], '5:6', "the chamber of the silent — the secret gift of 15:10"),
 ('**19. Mishnah, New Year**', ['Rosh Hashanah'], 'the Gemara 8b-9a whole', "the first of Tishri the sabbatical's new year, the slaves crowned till Yom Kippur, the fiftieth's arithmetic (9a:1)"),
 ('**25. Mishnah, Marriage Contracts**', ['Ketubot'], 'the Gemara 67b whole (43a:11, 58b:7 link rows)', "the measure of need and the ladder, the two who refuse, the secret givers; the board carried to the wife by a fortiori"),
 ('**29. Mishnah, Divorce Documents**', ['Gittin'], 'the Gemara 36a-37b whole (30a:16)', "Hillel's writ whole at its folio — the reason 15:9, the ground rabbinic against rabbinic, the decree arm when the jubilee is not in force, the presumption 'I had one and lost it'"),
 ('**30. Mishnah, Betrothal**', ['Mishnah Kiddushin', 'Kiddushin', 'Tosefta Kiddushin'], 'Mishnah 1:2-3, Tosefta Kiddushin 1 whole, the Gemara 14b-22b WHOLE (38b, 11b, 54b, 56b link rows)', "the three cases joined by 'hired worker', the severance gift's persons, measure and feature, the exits' tables, the pierced and the jubilee, the maidservant never pierced, the awl's tools and the upper ear, the two sayings and the board"),
 ('**32. Mishnah, Middle Gate**', ['Bava Metzia'], 'the Gemara 31b and 71a whole (30b:1, 33a:10, 47b:5 link rows)', "the doubled verbs unconditional, 'no needy among you' a precedence rule, the poor of your city first, the Hebrew slave's persons and his board"),
 ('**35. Mishnah, Lashes**', ['Makkot'], 'the Gemara 3b whole (3a:15)', "the ten-year loan's two versions, the stipulation against the release, the thirty days from 15:9's doubled name, the witnesses of the writ"),
 ('**43. Mishnah, Slaughter**', ['Mishnah Chullin'], '2:9', "the pouring place — the ground not the pit, the house not the market (15:23); Chullin 135a-137a's shearing rows in the link set"),
 ('**44. Mishnah, Firstborn**', ['Mishnah Bekhorot', 'Bekhorot', 'Tosefta Bekhorot'], 'Mishnah 1:1-2, 2:6-9, 3:3-4, 4:1-2, 5:1-6 and 6:1-12, Tosefta Bekhorot 1-2 whole, the Gemara 25a-28b, 33a-37b and 53b WHOLE', "the blemish class by general-particular-general (37a:16-19), the testimony and the expert (35b-37a), the awl's tools and the upper ear (37b:10-14), the plucking that is not shearing (25a), the shed hair (Mishnah 3:4 at 25a-26b), the tending term (26b), 'year by year' at its folio — the firstling's own year, two days across the edge, the thirty days, the exile's arm (27b-28a), the blemish shown after the slaughter (28a-b)"),
 ('**45. Mishnah, Valuations**', ['Mishnah Arakhin', 'Arakhin'], '8:7; the Gemara 32b-33a whole (28b:7, 29a:18-20, 30a:19, 30b:2 link rows)', "'you shall sanctify' for its value (29a:20), the count renewed at Ezra's return and the jubilee's condition (32b:10-18), the pierced slave's jubilee at Jeremiah's seat (33a:2-4)"),
 ('**46. Mishnah, Substitution**', ['Mishnah Temurah', 'Temurah'], '3:5 (11b:15, 17b:15, 21b:9 link rows)', "the firstling's offspring; the year passed no bar (21b:9)"),
]
MT = f'{ROOT}/logic/MISHNAH_TOPICS.md'; mt = open(MT, encoding='utf-8').read(); lines = mt.split('\n'); NOTE_TXT = {}
for pref, works, spans, point in NOTES:
    n, c, r = tract(works); idx = [i for i, l in enumerate(lines) if l.startswith(pref)]; assert len(idx) == 1, (pref, idx)
    assert "sitting 13b's docket" not in lines[idx[0]], pref
    NOTE_TXT[idx[0]] = f' — {spans} VERDICTED {DATE} (THE DEUTERONOMY WALK sitting 13b\'s docket: {n} rows — {c} carried, {r} read whole here; {point}; logic/oral_triage/{EXAM})'
for i, t in NOTE_TXT.items(): lines[i] = lines[i] + t
mt2 = '\n'.join(lines); assert not re.search(r'[֐-׿]', ''.join(NOTE_TXT.values()))
# ---- the map, the state doc, the recovery page, the memory
MAP = (f'\nTHE DOCKET — AS RUN (D2b, {DATE}; the owner\'s "Continue" at /context 276.4k after D2a\'s clean point — no compaction, his call): BEKHOROT 25a-28b WHOLE WITH ITS OWN LINK ROWS, '
       f'THE WRITER AND THE EXAM FILE. EVERY ROW READ WHOLE ({readhere} rows — the chunk files {", ".join(f"{f} rows {a}-{z} ({n} rows, {b} bytes)" for f, a, z, n, b in bchunks)} and the '
       f'unresolved file {UB} rows, {UBB} bytes; one Read page and two small prints); THE PART I on build_set over D2_UNIQUE by long_range ({N}); the U file\'s {unres} Bekhorot rows '
       f'appended (U_RUNS widened to the three runs — the U file holds every unresolved row of the carry); THE D2 CHECK on I — a PARTITION of the range, missing 0, extra 0. THE CENSUS OF '
       f'D2b (computed): {census}. THE WRITER (write_ch15_docket.py — typed on 12b\'s form, write_ch14_docket.py: the dump header asserted, the twice-listed address dropped by computation, '
       f'the parts A-I loaded and joined, the eleven ranges READ FROM THE SCAN\'S PRINT and asserted against the topic count with the {77} Mishnah and Tosefta rows, the verses cited and the '
       f'UNCITED computed, the crowns\' three paragraphs under "## The finds", the cite index, the tail\'s census) — THE EXAM FILE logic/oral_triage/{EXAM} WRITTEN ONCE: {whole}. '
       f'THE DOCKET\'S RECORDS: MIDDOT\'s entry ("### THE DEUTERONOMY WALK 13b — THE DOCKET OF CHAPTER 15" at the file\'s tail, 12b\'s form — every code checked in the tables before it '
       f'was typed, the seats read from the parts\' own notes by a print: I1, I2, I6, I8, E28, the amplification-restriction and the juxtapositions named without a code, the disputes as '
       f'parameters, the two DISAGREES rows resolved as data); MISHNAH_TOPICS\' row notes on {len(NOTES)} tractates (the counts per tractate computed from the parts); the state doc\'s #207 '
       f'addendum 3; the recovery page; the memory; COMPILE_DEBT\'s 13b box with its (o) at THE TAIL, as 12b\'s was. THE TIMING: {TIM}. THE FINDS OF BEKHOROT 25a-28b (in the exam file after '
       f'Kiddushin\'s):\n{crowns_d2b}')
assert not re.search(r'[֐-׿]', MAP) and '/Users/' not in MAP.replace('/Users/Shared', '')
STATE = (f'\n#207 ADDENDUM 3 — THE DOCKET CLOSED (2026-09-23, THE DEUTERONOMY WALK sitting 13b — THE COMPILE OF CHAPTER 15; D2b Bekhorot 25a-28b and the exam file, on the owner\'s '
         f'"Continue" at 276.4k after D2a\'s clean point (no compaction — his call, as at sitting 13\'s B1); A CLEAN COMPACTION POINT — THE DOCKET DONE, NO RUN B STEP TAKEN): THE STATE: '
         f'chapter 15 read, frozen, COMMITTED b0eaa56 (not pushed); the design in the map (RUN A); THE DOCKET DONE IN THREE RUNS — D1 the small works (548), D2a Kiddushin 14b-22b (305), '
         f'D2b Bekhorot 25a-28b ({N}: {census}); THE EXAM FILE logic/oral_triage/{EXAM}: {whole}; the parts A-I, the U file, the tools, the checks and the writer in the scratchpad AND '
         f'copied to World/step9/forms_deuteronomy_walk/; MIDDOT\'s entry, MISHNAH_TOPICS\' notes ({len(NOTES)} tractates), the map\'s "THE DOCKET — AS RUN (D2b)" paragraph written; '
         f'COMPILE_DEBT\'s 13b box (with (o) the docket) at THE TAIL as 12b\'s. THE TIMING: {TIM}. NOT COMMITTED (since b0eaa56): the commit\'s own records, the design, #207 with its '
         f'addenda and notes, the exam file, MIDDOT, MISHNAH_TOPICS, the recovery page\'s and the memory\'s lines, the forms. NOTHING MID-FLIGHT. NEXT ON HIS WORD (after a compaction: '
         f'"Reread", then "Go"): RUN B — the probes Q40-Q42 written to FAIL (patch_probes_ch15.py from patch_probes_ch14.py\'s form; the reuse literals retyped from the running world\'s '
         f'print), the types (add_types_ch15.py — the docket\'s names; the twenty-seven parameters; the twelve effects; the five kinds), the callees\' facts printed before any assert '
         f'(ch15_callees.py), the runner cold_run_release_firstborn.py in parts with the fast checker and the generated CASES, the recorder (INK_CACHE=0) and the stitcher (no marker — '
         f'the four lines on the counter\'s day), the literals DG1-DG9 from the prints, the tape to 10/10 with THE REST, checkpoint_check.py --all AFTER the tape, the records writer and '
         f'the copier WRITTEN, gates_chain.sh LAUNCHED in the background, the clean point; then THE TAIL. POST-COMPACTION REREADS: the recovery page, the map\'s "Sitting 13b — THE COMPILE '
         f'OF CHAPTER 15 … THE DESIGN" whole with its three "THE DOCKET — AS RUN" paragraphs (the newest section), MEMORY.md; then #207, its addenda 1-3 and the two NOTES; at RUN B\'s '
         f'open THE_STEPS\' compiler block, Step 2 and Step 5\'s head, the 12b RUN B forms (patch_probes_ch14.py, add_types_ch14.py, ch14_callees.py, the runner\'s parts, seq_record_ch14.py, '
         f'seq_stitch_ch14.py, patch_seq_literals_ch14.py, write_ch14b_records.py, copy_ch14b_forms.py).\n')
assert '/Users/' not in STATE.replace('/Users/Shared', '')
RP = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; rp = open(RP, encoding='utf-8').read()
H_OLD = '## 2. WHERE IT STANDS (2026-09-23, 13b D2a closed; the state doc #207 addendum 2 the newest)'
H_NEW = '## 2. WHERE IT STANDS (2026-09-23, 13b docket closed; the state doc #207 addendum 3 the newest)'
lm = re.search(r'D1 DONE \((\d+)\), D2a DONE \(Kiddushin 14b-22b, (\d+); the parts in the forms\)\.', rp); assert lm and int(lm.group(1)) + int(lm.group(2)) + N == W_N, (lm and lm.groups(), N, W_N)   # the three runs' UNIQUE counts sum to the deduplicated total
L_OLD = lm.group(0); L_NEW = f'THE DOCKET DONE ({W_N} rows, three runs; {EXAM}).'
X_OLD = '- NEXT ON HIS WORD: D2b (Bekhorot 25a-28b whole, the writer, the exam file, the records), then RUN B.'
X_NEW = '- NEXT ON HIS WORD: RUN B (the probes, the types, the runner, the tape, the chain), then THE TAIL.'
assert rp.count(H_OLD) == 1 and rp.count(L_OLD) == 1 and rp.count(X_OLD) == 1
rp2 = rp.replace(H_OLD, H_NEW).replace(L_OLD, L_NEW).replace(X_OLD, X_NEW); assert len(rp2.encode()) <= 10240, len(rp2.encode())
MP = f'{MEM}/MEMORY.md'; mem = open(MP, encoding='utf-8').read()
mm_ = re.search(r'13b: design, D1 \((\d+)\), D2a Kiddushin \((\d+)\) DONE; NEXT: D2b \(Bekhorot 25a-28b, the exam file\)', mem); assert mm_
M_OLD = mm_.group(0); M_NEW = f'13b: design + DOCKET DONE ({W_N} rows, three runs); NEXT: RUN B'
mem2 = mem.replace(M_OLD, M_NEW); assert mem2.count(M_NEW) == 1 and len(mem2.encode()) <= 17000, len(mem2.encode())
WALK = f'{MEM}/deuteronomy-walk.md'; walk_line = (f'\nSITTING 13b DOCKET CLOSED {DATE} — D2b Bekhorot 25a-28b whole ({N}; carried {carried}, read whole here {readhere}); the exam file '
                                                f'logic/oral_triage/{EXAM} ({W_N} rows: LAW {W_VERD["LAW"]} / DERIVATION {W_VERD["DERIVATION"]} / DISPUTE {W_VERD["DISPUTE"]} / CONTEXT {W_VERD["CONTEXT"]} / OUTSIDE {W_VERD["OUTSIDE"]}; '
                                                f'{W_CAR} carried, {W_RH} read whole in three runs; 15:15 the one verse no row cites — computed); MIDDOT\'s entry and MISHNAH_TOPICS\' notes written; COMPILE_DEBT\'s box at the tail. NEXT on his word: RUN B, then THE TAIL.\n')
MAPF = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; mp = open(MAPF, encoding='utf-8').read(); sec = mp[mp.rfind('\n## Sitting 13b — THE COMPILE OF CHAPTER 15'):]
assert 'THE DOCKET — AS RUN (D2a' in sec and 'THE DOCKET — AS RUN (D2b' not in sec
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; sd = open(SD, encoding='utf-8').read(); assert '#207 ADDENDUM 3' not in sd and sd.rstrip().endswith('its addenda 1-2 and the two NOTES.')
MD = f'{ROOT}/logic/MIDDOT.md'; md = open(MD, encoding='utf-8').read(); assert '13b — THE DOCKET OF CHAPTER 15' not in md and md.rstrip().endswith('(the peres and the ozniyya).') and md.endswith('\n')
# every text built and every cap asserted — now the writes
open(MAPF, 'a', encoding='utf-8').write(MAP); open(SD, 'a', encoding='utf-8').write(STATE); open(RP, 'w', encoding='utf-8').write(rp2); open(MP, 'w', encoding='utf-8').write(mem2); open(WALK, 'a', encoding='utf-8').write(walk_line)
open(MD, 'a', encoding='utf-8').write(MID); open(MT, 'w', encoding='utf-8').write(mt2)
F = f'{ROOT}/World/step9/forms_deuteronomy_walk'; copied = []
for fn in sorted(os.listdir(SP)):
    if re.match(r'(ch15_docket_(I|U|crowns)\.py|ch15_docket_d2b_check\.out|ch15_docket_U_d2b_block\.txt|write_ch15_docket\.(py|out)|write_ch15b_docket_point\.py|ch15b_timing\.tsv)$', fn):
        shutil.copy(f'{SP}/{fn}', f'{F}/{fn}'); copied.append(fn)
print('MAP +', len(MAP.encode()), 'bytes; STATE +', len(STATE.encode()), '; MIDDOT +', len(MID.encode()), '; TOPICS +', sum(len(t.encode()) for t in NOTE_TXT.values()), 'on', len(NOTE_TXT), 'lines; recovery', len(rp2.encode()), '; MEMORY.md', len(mem2.encode()), '; walk +', len(walk_line.encode()))
print('D2b CENSUS', census); print('WHOLE', whole); print('COPIED', len(copied), copied)
