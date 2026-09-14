#!/usr/bin/env python3
# THE NUMBERS WALK 12b — THE COMPILE OF GAD AND REUBEN (2026-09-12): THE EXAM DOCKET for Numbers 32:1-42, written from the scan's dump
# (scratchpad/gad_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a verse of the
# span; the TOPIC rows = Mishnah Kiddushin 3:4 and Mishnah Shekalim 3:2 (both link rows themselves) and the ten folio ranges of COMPILE_DEBT's
# sitting-12 box (n) read WHOLE — the union rule of 2026-09-05; the CREDITED marks = addresses already verdicted in an earlier ledger, given
# their quick look here). Every address in the dump gets ONE verdict (parts A..E); the coverage is COMPUTED from the dump, never typed; the
# ranges' sizes are read from the scan's own print (gad_docket_scan.out). Append-only. write_midian_docket.py's form.
import re, os, sys, importlib.util
from collections import Counter
ROOT = '<repo-old>'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{ROOT}/logic/oral_triage/num_32_gad_reuben_exam_2026-09-12.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/gad_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR, CRED = [], {}
for k, a, rest in rows:
    m = re.search(r'\{CREDITED: (.*?)\}', rest)
    if m: CRED[a.strip()] = m.group(1)
    ADDR.append((k, a.strip(), re.sub(r'\s*\{CREDITED:.*?\}', '', rest).strip()))
NL = sum(1 for k, _, _ in ADDR if k == 'LINK'); NT = len(ADDR) - NL
assert len(ADDR) == 319 and NL == 15 and len(CRED) == 156, (len(ADDR), NL, len(CRED))
V = {}
for p in 'ABCDE':
    part = f'gad_docket_{p}'
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
assert len(works) == 10, len(works)
scan = open(f'{SCR}/gad_docket_scan.out', encoding='utf-8').read()
scan = scan[scan.index('THE RANGES SIZED:'):]
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) segments,\s+(\d+) link rows', scan, re.M)]   # read from the scan's print
assert len(LONG) == 10, len(LONG)
MISH = [a for k, a, _ in ADDR if k == 'TOPIC' and a.startswith('Mishnah')]
assert MISH == [], MISH   # both single mishnayot are link rows themselves (the scan's print: "already a link row")
assert sum(s - l for _, s, l in LONG) == NT, (sum(s - l for _, s, l in LONG), NT)   # every range read WHOLE: the topic rows = the ranges' non-link segments
ncred_link = sum(1 for k, a, _ in ADDR if k == 'LINK' and a in CRED); ncred_topic = sum(1 for k, a, _ in ADDR if k == 'TOPIC' and a in CRED)
hdr = (f'# THE EXAM DOCKET — Numbers 32:1-42 (Gad and Reuben: the request, Moses\' rebuke and the oath retold, the offer, the doubled condition and the utterance rule, the acceptance and the commission charged, the grant east of the Jordan, the cities built and renamed, Machir, Jair and Nobah), THE NUMBERS WALK sitting 12b, the compile (2026-09-12; the owner: "Go" after the #149 rereads, on 1b\'s order — the measurements, the design, the probes, the docket, the types, the runner; the design World/step9/NUMBERS_WALK.md "Sitting 12b").\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of Numbers 32:1-42 (the scan by script over Data/sefaria_export, commentaries excluded: {NL} rows in {len(works)} works — ' + ', '.join(f'{w} {n}' for w, n in works.most_common()) + f'; the verses most cited 32:30 and 32:22 five each, 32:29 four — the doubled condition and the clearance), and (2) THE TOPIC-ROUTED ROWS — Mishnah Kiddushin 3:4 (the doubled condition\'s exemplar) and Mishnah Shekalim 3:2 (the clearance), both link rows themselves, and the ten folio ranges of COMPILE_DEBT\'s sitting-12 box (n) — the doubled condition\'s sugyot (Kiddushin 61a-62a, Bava Metzia 94a, Gittin 75a-b, Nedarim 11a, Shevuot 36a), the clearance\'s (Yoma 38a, Pesachim 13a), the division of the land (Bava Batra 117a-122a), the spies and Caleb\'s Hebron (Sotah 34b-35a) and Sanhedrin 111a — read WHOLE with the link rows dropped: ' + '; '.join(f'{r} {s} segments ({l} link rows)' for r, s, l in LONG) + f' — {NT} topic rows. {len(CRED)} addresses already verdicted in earlier ledgers are marked CREDITED with their ledger and given a QUICK LOOK here (speed ruling (b), credit guard (1)) — {ncred_link} link rows, {ncred_topic} topic rows; Bava Batra 117a-122a whole is the second census\'s docket\'s, read there on 2026-09-11 and looked at here for this chapter\'s rows (Jair and Machir the wilderness\' survivors; Manasseh\'s ten parts beside Gilead and Bashan; Joshua and Caleb outside the lot). Every address gets ONE verdict: LAW (a rule the runner must reproduce — the cell named: F1 the_request, F2 the_rebuke, F3 the_offer, F4 the_condition, F5 the_acceptance_and_the_charge, F6 the_grant, F7 the_cities, F8 machir_jair_nobah, or the callee\'s cell by CALL), DERIVATION (a hook from the verse to a rule — a labeled move), DISPUTE (a parameter row — a DATA row named), CONTEXT, OUTSIDE (the export\'s empty segment). Terse for the non-material (speed ruling (c)). The Tanchuma on the cattle before the children is OUTSIDE the declared spine and not opened (the box\'s own line).\n'
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
- THE CHAPTER IS THE SOURCE OF THE WHOLE LAW OF CONDITIONS: "from where do we learn the laws of all conditions? from the condition of the sons of Gad and Reuben" — Rava (Gittin 75a:11), Rav Adda bar Ahava (75a:14), Rava again (75b:6); the exemplar's LIMBS read off the chapter's verses one by one — DOUBLED (R. Meir, Mishnah Kiddushin 3:4 = 61a:9, the proof 32:29 then 32:30), THE CONDITION BEFORE THE ACTION (Gittin 75a:12 — "and you shall give them the land of Gilead" after the "if"; Bava Metzia 94a:3, Abba Chalafta in R. Meir's name 94a:7), THE POSITIVE BEFORE THE NEGATIVE (Gittin 75b:6 — 32:29 before 32:30), THE CONDITION'S MATTER AND THE ACT'S MATTER DISTINCT (Gittin 75a:14 — to fight, to receive Gilead: a FIFTH feature the shelf reads off the same verses), A CONDITION THAT CAN BE FULFILLED (Bava Metzia 94a:3, 94a:11-14 — R. Yehuda ben Teima against the Rabbis, THE HALAKHA as him; Kiddushin 62a:12's "anything in one's power"): the DATA row the_conditions_four_limbs carries five lines with their tannaim and their verses; "ON CONDITION" IS "FROM NOW" (Rav Huna in Rav's name, Gittin 75b:2) — the act takes effect at once under the condition: THE GRANT'S TIMING at 32:33 (the transfer written at the grant, the debit open beside it) is the shelf's own form.
- THE DOUBLING DISPUTED AND SCOPED: R. Meir's rule against R. Chanina ben Gamliel's "the doubling was needed there for its own sake" (Mishnah Kiddushin 3:4, 61a:10), R. Meir's hook the superfluous "in the land of Canaan" (61a:11-61b:1), R. Chanina's parable of the father's three sons (61b:3-4) and the two positions dated against each other (61b:5-8); THE RULE'S COROLLARY — R. Meir does not infer the unstated arm (Nedarim 11a:2; Shevuot 36a:25), IN MONETARY MATTERS ONLY or everywhere (Shevuot 36a:27 against 36a:29 — the sotah's "hinnaki" written and "chinnaki" read, Kiddushin 62a:2-3): the DATA row doubled_condition's arms and its scope arm; THE EXEMPLAR'S KIN censused on the shelf — Cain's IF (Genesis 4:7, 61b:9), Eliezer's oath (24:41, 61b:10-12), the blessings and the curses (Leviticus 26, 61b:13), Isaiah 1:19-20 (61b:14), the sotah (62a:2-3), the heifer's third and seventh day (Numbers 19:12, 62a:4-5), and the flood's doubled "no, no" as an oath (Shevuot 36a:14): the doubling a FORM the tradition reads across the books, this chapter its name.
- THE NEGATIVE ARM'S TWO READINGS: "they shall receive a possession among you in the land of Canaan" (32:30) — Gilead shared or Canaan only; without the doubling no portion anywhere, or Gilead anyway (Kiddushin 61b:2, 61b:5-8): the DATA row negative_arm_outcome; the ink's own second outcome "know your sin which will find you" (32:23) not read by any row of the docket — the ink's arm alone.
- THE CLEARANCE'S THREE SEATS: the treasury's clerk enters with no cuffed garment, shoe, sandal, phylacteries or amulet — "a person must appear justified before people as before the Omnipresent" (Mishnah Shekalim 3:2); the House of Garmu's coarse bread and the House of Avtinas's unperfumed brides — beyond reproach AND beyond suspicion (Yoma 38a:9, 38a:12 — the perfumers STIPULATE with a bride from elsewhere: a condition on a marriage at the rule's own seat); the charity collectors who sell to others and change money with others (Pesachim 13a:13-14): 32:22's "clear before the LORD and before Israel" the rule's one verse at every seat — the effect clear_before_the_lord_and_israel written on the exam's three persons, the DATA row the_clearance.
- THE STIPULATION'S VERB: "and every armed man of you will pass over [ve'avar] the Jordan" (32:21) read of the FUTURE — the perfect with the conjunction in a condition; "the land subdued... and you return afterward" (32:22) fixes it (Sotah 3a:8-9, against the sotah's past "ve'avar"): the condition's clauses a sequence — arm, cross, subdue, return.
- THE OATH RETOLD ON THE SHELF: two of six hundred thousand entered — Caleb and Joshua (Rav Simai, Sanhedrin 111a:6); the decree not on Levi (Rav Hamnuna, Bava Batra 121b:8) nor on those under twenty or over sixty (Rav Acha bar Yaakov, 121b:11); the deaths ceased on the fifteenth of Av and God's speech resumed (Bava Batra 121a:9-121b:1 with Deuteronomy 2:16-17); Joshua and Caleb took the spies' portions (117b:2, 118b:3) and their own not by lot but by the LORD's word — Timnath-serah, Hebron (122a:12); CALEB'S HEBRON — he went alone to the fathers' graves (Sotah 34b:7), "another spirit" a change over time where Joshua opposed from the outset (34b:8); "send YOU" at Moses' discretion (34b:3) — and MOSES' OWN "WHEN I SENT THEM" (32:8) the retelling's first person; Joshua "a severed head, no children" (35a:4) — the shelf's reason nothing is owed him in the ink; slow to anger at the spies' sin (Sanhedrin 111a:12-13): the shelach runner's cells by CALL at every one.
- JAIR AND MACHIR SURVIVED THE WILDERNESS: "Jair son of Manasseh and Machir son of Manasseh were born in Jacob's days and did not die until Israel entered the land" — the baraita on "about thirty-six men" at Ai (Joshua 7:5; R. Yehuda literally, R. Nechemya: Jair alone, the majority of the Sanhedrin — Bava Batra 121b:9-10), Jair already old at the decree (121b:11): THE CHAPTER'S TWO CONQUERORS (32:39-41) on the shelf as the exodus generation's survivors, Machir's sons "born on Joseph's knees" (Genesis 50:23 — the registry's collective, written on again here): the DATA row jair_and_machir_survived; Jair's fall at Ai a RUN_CITATION.
- HALF MANASSEH'S EAST ON THE SHELF: "ten parts fell to Manasseh, BESIDE the land of Gilead and Bashan beyond the Jordan" (Joshua 17:5-6 at Bava Batra 118b:8) — the shelf's own line between the tribe's ten parts in Canaan and its east (32:33, 32:39-42); ERETZ YISRAEL HELD BEFORE ASSIGNMENT (Rabba, 119a:1, 119a:5 — the possession's standing the grant's word "a holding" carries); the exodus generation BEQUEATH AND DO NOT INHERIT (119b:3-4 — Exodus 6:8's "heritage", the song's "bring THEM in"); ELEAZAR WITH THE URIM, JOSHUA AND ALL ISRAEL BEFORE HIM at the lottery (122a:4) — 32:28's commission at its run.
- MOSES' GRAVE: in Reuben's portion — Nebo is Reuben's, "the children of Reuben built... Nebo" (32:37-38; Sotah 13b:20), and ONKELOS'S "NEBO, THE BURIAL PLACE OF MOSES" at 32:3 is the same reading in the translation's own words (the reading's find, now with its Talmud seat); the Sifrei 106:1's Gad (Deuteronomy 33:21) the other arm — the DATA row moses_grave.
- THE SHELF'S ASSUMPTION AGAINST THE STORE: "even a verse comprised entirely of names identical in Hebrew and Aramaic — Ataroth and Dibon..." (Berakhot 8b:1 on 32:3) — where the local Onkelos renders the nine by ARAMAIC names (the reading's ledger row at 32:3): the Talmud's premise about the Targum of this verse is not the store's Targum — a RESEARCH_LOG finding.
- THE SHELF'S OWN GAP: an EMPTY segment at Bava Metzia 94a:15 (OUTSIDE — the export's blank row, owed its verdict).
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_gad_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {NL}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {NT}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))}; credited {len(CRED)} — the counts this script computed from the dump and the verdict lists, never typed)\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('WROTE', OUT, len(ADDR), 'rows;', dict(cnt), '; link', dict(cnt_link), '; topic', dict(cnt_topic), '; credited', len(CRED), '; long ranges', len(LONG))
