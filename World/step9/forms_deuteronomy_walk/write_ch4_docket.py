import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 2b — THE COMPILE OF CHAPTER 4 (2026-09-16): THE EXAM DOCKET for Deuteronomy 4:1-49, written from the scan's dump
# (scratchpad/ch4_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a verse of the
# chapter; the TOPIC rows = the ten Mishnah rows and the nine folio ranges of the design's item (k) read WHOLE — the union rule of 2026-09-05; the
# CREDITED marks = addresses already verdicted in an earlier ledger, given their quick look here). Every address in the dump gets ONE verdict (parts
# A..D on disk); the coverage is COMPUTED from the dump, never typed; the ranges' sizes are read from the scan's own print (ch4_docket_scan.out).
# Append-only. write_deu_docket.py's form.
import re, os, sys, importlib.util, subprocess
from collections import Counter
ROOT = _ROOT
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{ROOT}/logic/oral_triage/deu_04_vaetchanan_exam_2026-09-16.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/ch4_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR, CRED = [], {}
for k, a, rest in rows:
    m = re.search(r'\{CREDITED: (.*?)\}', rest)
    if m: CRED[a.strip()] = m.group(1)
    ADDR.append((k, a.strip(), re.sub(r'\s*\{CREDITED:.*?\}', '', rest).strip()))
NL = sum(1 for k, _, _ in ADDR if k == 'LINK'); NT = len(ADDR) - NL
hdr_line = dump.split('\n', 1)[0]
assert hdr_line == 'ROWS %d LINK %d TOPIC %d CREDITED %d' % (len(ADDR), NL, NT, len(CRED)), (hdr_line, len(ADDR), NL, NT, len(CRED))
V = {}
for p in 'ABCD':
    part = f'ch4_docket_{p}'
    spec = importlib.util.spec_from_file_location(part, f'{SCR}/{part}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for addr, verdict, note in m.ROWS:
        assert addr not in V, ('duplicate verdict', addr)
        assert verdict in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE'), (addr, verdict)
        V[addr] = (verdict, note)
missing = [a for _, a, _ in ADDR if a not in V]; extra = [a for a in V if a not in {x[1] for x in ADDR}]
if missing or extra:
    print('MISSING', len(missing), missing); print('EXTRA', len(extra), extra); sys.exit(1)
cnt = Counter(vd for vd, _ in V.values())
cnt_link = Counter(V[a][0] for k, a, _ in ADDR if k == 'LINK'); cnt_topic = Counter(V[a][0] for k, a, _ in ADDR if k == 'TOPIC')
works = Counter(a.rsplit(' ', 1)[0] for k, a, _ in ADDR if k == 'LINK')
scan = open(f'{SCR}/ch4_docket_scan.out', encoding='utf-8').read()
scan = scan[scan.index('THE RANGES SIZED:'):]
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) segments,\s+(\d+) link rows', scan, re.M)]   # read from the scan's print
assert len(LONG) == 9, len(LONG)
MISH = [a for k, a, _ in ADDR if k == 'TOPIC' and not re.search(r'\d+[ab]:\d+$', a)]   # the Mishnah rows
assert len(MISH) == 10, len(MISH)   # eleven named in the design, one of them (Mishnah Makkot 2:4) already a LINK row — the scan's print
assert sum(s - l for _, s, l in LONG) + len(MISH) == NT, (sum(s - l for _, s, l in LONG), len(MISH), NT)   # every range read WHOLE
ncred_link = sum(1 for k, a, _ in ADDR if k == 'LINK' and a in CRED); ncred_topic = sum(1 for k, a, _ in ADDR if k == 'TOPIC' and a in CRED)
verses = Counter(h for k, _, vs in ADDR if k == 'LINK' for h in vs.split())
LAWCELLS = Counter(m.group(1) for vd, note in V.values() if vd == 'LAW' for m in [re.search(r'\b(F[1-6])\b', note)] if m)
hdr = (f'# THE EXAM DOCKET — Deuteronomy 4:1-49 (the exhortation with the one law — add nothing, diminish nothing; Horeb retold with the ten words and the tablets; the no-image list and the host apportioned; the one case — the exile and the return with heaven and earth as witnesses; the one God, the nation from a nation, the creed; the three cities Moses set apart and the second frame), THE DEUTERONOMY WALK sitting 2b (2026-09-16; World/step9/DEUTERONOMY_WALK.md "Sitting 2b"; the runner cold_run_obey_horeb.py, the daemon law_obey_horeb).\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of Deuteronomy 4:1-49 (the scan ch4_docket_scan.py: {NL} rows in {len(works)} works; the verses cited most {", ".join(f"{v} {n}" for v, n in verses.most_common(7))}), and (2) THE TOPIC ROWS by address (the reading ledger\'s TESTING paragraph, COMPILE_DEBT\'s sitting-2 box (k)): the Mishnah rows {", ".join(MISH)} and the folio ranges read WHOLE — {"; ".join(f"{n} ({s} segments, {l} of them link rows)" for n, s, l in LONG)} = {NT} topic rows. EVERY ADDRESS ONE VERDICT: LAW (the cell of cold_run_obey_horeb.py named — F1 the_exhortation, F2 horeb_retold, F3 no_image, F4 the_exile_case, F5 the_one_god, F6 the_cities_and_the_frame — or the callee\'s cell by CALL), DERIVATION, DISPUTE, CONTEXT, OUTSIDE; {len(CRED)} addresses CREDITED from earlier ledgers (link {ncred_link}, topic {ncred_topic}) with their quick look. The rows are the answer sheet\'s: the Mishnah GRADES, the Talmud TEACHES per gap; nothing here is code.\n'
       f'# THE TALMUD ADDRESSING: the export\'s index 0 is folio 1a (a page = index // 2 + 1; measured 2026-09-09); the Mishnah by chapter:mishnah.\n')
body = ''
last = None
for k, a, vs in ADDR:
    work = a.rsplit(' ', 1)[0]
    if work != last:
        body += f'\n## {work}\n'; last = work
    vd, note = V[a]
    body += f'- {a} [{k}{(" — " + vs) if vs else ""}{(" — CREDITED: " + CRED[a]) if a in CRED else ""}] — {vd}. {note}\n'
crowns = '''
## The finds (this docket's crowns)
- BAL TOSIF'S TWO PARAMETERS (Rosh Hashanah 28b:8-24; Eruvin 95b:19-96a:5): "you shall not add" (4:2) is transgressed IN THE MITZVA'S TIME without intent and OUT OF ITS TIME only with intent (Rava's final setting, 28b:24) — the sleeper in the sukkah on the eighth day, the second pair of tefillin on the Sabbath (a time for tefillin or not — the tannaim), the priest who adds a blessing (the whole day his time, another congregation may come, 28b:13); "do not diminish" its pair on one act — R. Eliezer's four sprinklings against R. Yehoshua's one (28b:15-18): adding an ACT, diminishing an OMISSION: F1 add_nothing / diminish_nothing, the DATA row the_law_bal_tosif.
- THE ADDITION THAT SPOILS (Sanhedrin 88b:14-89a:2): the rebellious elder is liable only where the essence is Torah, the explanation the scribes', and an addition SPOILS the mitzva — the fifth compartment of the tefillin made as one (five made) against a fifth placed beside (stands alone); the lulav's added species by the binding, the fringes' added thread by the upper knot: the third parameter of the law's cell (the Sifrei 82:5's fifth species and fifth fringe at their Talmud seat).
- THE GRANDSONS INCLUDED, THE DAUGHTERS EXCLUDED (Kiddushin 30a:3-8): "make them known to your sons and to your sons' sons" (4:9) against "teach them to your sons" (11:19) — the grandfather's duty (Zevulun ben Dan taught by his father's father — Bible alone in the extent), the daughters excluded by "your sons"; the juxtaposition to 4:10's "the day you stood at Horeb": as if received from Sinai (R. Yehoshua ben Levi); the same juxtaposition's second teaching — Torah studied in awe as Sinai was (Berakhot 22a:4; Moed Katan 15a:18): F2 take_heed_lest_you_forget, the DATA row the_teach_your_sons.
- THE FORGETTER'S PROHIBITION (Menachot 99b:3; Avot 3:8; Shevuot 36a:20): "only take heed to yourself and keep your soul diligently lest you forget" (4:9) — a prohibition (R. Avin: "take heed", "lest", "do not"), two of them, three with "keep your soul"; the forgetter as if guilty of death, unless it was too hard for him; the self-curser's warning at the same clause: F2 take_heed_lest_you_forget.
- THE FREE TEACHING (Bekhorot 29a:7-8; Nedarim 37a:2, 38a:5): "as the LORD my God commanded me" (4:5) — as I learned for free, you learned for free: the judge who takes wages, the teacher of Bible; Rav Chisda's objection from 4:14 ("commanded me to teach you") resolved — the Torah commanded to Moses, the teaching his own; THE RECEIPT'S OWN READING at its exam seat: F1 taught_as_commanded (the register seat Deut 4:5 ACT — the teaching's run) and F2 commanded_to_teach.
- THE IMAGES FOR STUDY (Mishnah Rosh Hashanah 2:8; Rosh Hashanah 24a:18-24b:13; Mishnah Avodah Zarah 3:1-3): Rabban Gamliel's forms of the moon — "you shall not make with Me" (Exodus 20:20) beside 20:4's "any likeness of what is in heaven above": the baraita's parameter table (the sun, moon, stars, constellations; the ministering angels; the mountains, hills, seas, rivers; a tiny worm — worship, not making); the reproducible attendants; the human face by "not Me"; others made them; in pieces; to teach himself ("you shall not learn TO DO", 18:9) — THE SECOND WORD'S ROWS, WAITING FOR THEIR ENGINE: F3 the_image_list (4:16-19's forms at their Sinai seat; the edge to the decalogue OWED — no cell compiles the image law; chapter 5's sitting).
- THE HOST ALLOTTED (Avodah Zarah 55a:9-10; Megillah 9b:1; the Sifrei 148:8): "which the LORD your God has allotted to all the peoples" (4:19) — Rav: He let them slip into their delusion to drive them from the world; Reish Lakish: the one who comes to defile himself is given the opening; the Septuagint's "to give light" added for Ptolemy; Onkelos "prepared": F3 the_host_apportioned, a DATA note — no link of our own.
- CORRUPTION IS IDOLATRY (Chullin 23a:3; Avodah Zarah 23b:9; Bekhorot 57a:12; Temurah 28b:17; Sanhedrin 57a:1): the school of R. Yishmael's lexicon — "lest you deal corruptly and make you a graven image" (4:16) the idolatry seat, the flood's "corrupted its way" the licentiousness seat; the birds of 4:17 ("any winged bird" — kosher or not, the grasshoppers): F3 the_image_list's word.
- THE CONSUMING FIRE AND THE CLEAVING (Ketubot 111b:6-8; Sanhedrin 64a:11, 90b:13; Sotah 14a:3; Avodah Zarah 54b:18-55a:3; Nedarim 62b:3): "you who cleave to the LORD are alive" (4:4) against "a consuming fire" (4:24) — the Sifrei 49:2's objection at its Talmud seats: cleave to the scholars (marry a daughter to one, do business for one, benefit one); Peor's cord against the dates lightly touching; even on the day all are dead; walk after His attributes; the philosopher's and Agrippas's questions — jealousy at the worshipper, not the idol: F1 the_cleaving, F3 consuming_fire_jealous_god.
- THE LIMITS OF INQUIRY AND ADAM'S HEIGHT (Chagigah 11b:21-24, 12a:2; Tosefta Chagigah 2:3; Sanhedrin 38b:7): "ask now of the days past" (4:32) in the singular — one may inquire of creation, not two; "from one end of heaven to the other" — within the world's bounds, not above, below, before, after; Adam's span from one end to the other, diminished after the sin: F5 the_former_days, the DATA row the_inquiry_limits.
- NONE ELSE — EVEN SORCERY; THE KINGSHIP VERSES (Chullin 7b:14; Sanhedrin 67b:7; Rosh Hashanah 32b:17; Tosefta Rosh Hashanah 2:11; Gittin 57b:17): "there is none else beside Him" (4:35) — R. Chanina: even sorcery; 4:35 and 4:39 verses of kingship (R. Yosei) or not (R. Yehuda); the seventh son's creed: F5 you_were_shown, know_this_day, the DATA row the_creed.
- THE EXILE HASTENED (Gittin 88a:15-17; Sanhedrin 38a:6; Megillah 31b:2): "and you have grown old in the land" (4:25) — the word's letters eight hundred and fifty-two, the exile hastened by two years (Ulla's righteousness); after grandchildren a matter is old (Rav Huna); seven dynasties from the seven verbs (R. Ammi); the Ninth of Av's reading 4:25-40: F4 the_case_head, the DATA row the_exile_case — "in the end of days" a prophecy, no timer.
- GOD SO NEAR (Sanhedrin 38b:15; Rosh Hashanah 18a:10; Yevamot 105a:17; Berakhot 6a:24; Megillah 11a:9): "God near" (4:7) plural against "whenever we call upon Him" singular — the heretics' verse and its own answer (the reading's find at its seat); a community's sealed sentence torn up; the tefillin's compartments; Esther's introductions: F1 god_so_near.
- THE EASTERN CITIES HOME (Makkot 9b:18-10a:16; Mishnah Makkot 2:4-8; Gittin 12a:11; Sotah 49a:4; Avodah Zarah 58b:8): the two rows of vines — Hebron against Bezer, Shechem against Ramoth, Kadesh against Golan; Gilead's murderers; Reuben first; "a mitzva that came my way" — Moses knowing the three would admit no one until Joshua's three: THE DEBIT LEFT OPEN on the answer sheet's own row (Mishnah Makkot 2:4); "and live" (4:42) — the teacher exiled with his school, the slave's surplus, the quarreling scholars; Bezer not Bozrah: F6 then_moses_set_apart, not_until_all_six, the_manslayer_defined, the_three_names.
- THE SECOND FRAME'S WORD (Yoma 72b:14; Avodah Zarah 2b:6; Menachot 53b:4; Makkot 10a:11): "this is the Torah which Moses SET" (4:44) — a drug of life or death (the sin read as the samekh); "this" is nothing but Torah (the Sifrei 323:1); Torah provides refuge — 4:43's cities juxtaposed to 4:44: F6 the_second_frame, NO WRITE (R6).
- THE INSTRUMENTS AND THE HAGGADAH (Mishnah Pesachim 10:4; Berakhot 6a:24; Megillah 11a:9; the Sifrei 301:21): "a nation from the midst of a nation, by trials, signs, wonders, war, a mighty hand, an outstretched arm, great terrors" (4:34) — the exposition from "a wandering Aramean" (26:5-8) that the Mishnah orders; the arm plene here, defective there: F5 the_nation_from_a_nation, the DATA row the_instruments.
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_ch4_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {NL}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {NT}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))}; credited {len(CRED)} — the counts this script computed from the dump and the verdict lists, never typed).\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('WROTE', OUT, os.path.getsize(OUT), 'bytes')
print('rows', len(ADDR), 'link', NL, 'topic', NT, 'credited', len(CRED), '(link', ncred_link, 'topic', ncred_topic, ')')
print('verdicts', dict(sorted(cnt.items())), 'link', dict(sorted(cnt_link.items())), 'topic', dict(sorted(cnt_topic.items())))
print('LAW by cell', dict(sorted(LAWCELLS.items())))
print('ranges', [(n, s, l) for n, s, l in LONG]); print('mishnah rows', len(MISH))
