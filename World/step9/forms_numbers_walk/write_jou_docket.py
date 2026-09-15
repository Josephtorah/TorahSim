import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK 13b — THE COMPILE OF THE JOURNEYS (2026-09-12): THE EXAM DOCKET for Numbers 33:1-56, written from the scan's dump
# (scratchpad/jou_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a verse of the
# span; the TOPIC rows = Mishnah Zevachim 14:4-8, the four folio ranges of COMPILE_DEBT's sitting-13 box (l) read WHOLE, and Seder Olam Rabbah
# 9-10 — the union rule of 2026-09-05; Zevachim 112b-119b SIZED (265 segments, no link row) and CUT at the scan's print as the private altar's
# docket, not this chapter's — jou_docket_scan_sized.out; the CREDITED marks = addresses already verdicted in an earlier ledger, given their
# quick look here). Every address in the dump gets ONE verdict (parts A..D); the coverage is COMPUTED from the dump, never typed; the ranges'
# sizes are read from the scan's own print (jou_docket_scan.out). Append-only. write_gad_docket.py's form.
import re, os, sys, importlib.util
from collections import Counter
ROOT = _ROOT
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{ROOT}/logic/oral_triage/num_33_journeys_exam_2026-09-12.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/jou_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR, CRED = [], {}
for k, a, rest in rows:
    m = re.search(r'\{CREDITED: (.*?)\}', rest)
    if m: CRED[a.strip()] = m.group(1)
    ADDR.append((k, a.strip(), re.sub(r'\s*\{CREDITED:.*?\}', '', rest).strip()))
NL = sum(1 for k, _, _ in ADDR if k == 'LINK'); NT = len(ADDR) - NL
assert len(ADDR) == 196 and NL == 12 and len(CRED) == 139, (len(ADDR), NL, len(CRED))
V = {}
for p in 'ABCD':
    part = f'jou_docket_{p}'
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
assert len(works) == 9, len(works)
scan = open(f'{SCR}/jou_docket_scan.out', encoding='utf-8').read()
scan = scan[scan.index('THE RANGES SIZED:'):]
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) segments,\s+(\d+) link rows', scan, re.M)]   # read from the scan's print
assert len(LONG) == 4, len(LONG)
sized = open(f'{SCR}/jou_docket_scan_sized.out', encoding='utf-8').read()
ZV = re.findall(r'^  Zevachim\s+112b-119b\s+(\d+) segments,\s+(\d+) link rows', sized[sized.index('THE RANGES SIZED:'):], re.M)
assert ZV == [('265', '0')], ZV   # the cut range's size read from the sizing print
MISH = [a for k, a, _ in ADDR if k == 'TOPIC' and a.startswith('Mishnah')]
SO = [a for k, a, _ in ADDR if k == 'TOPIC' and a.startswith('Seder Olam')]
assert len(MISH) == 5 and len(SO) == 5, (MISH, SO)
assert sum(s - l for _, s, l in LONG) + len(MISH) + len(SO) == NT, (sum(s - l for _, s, l in LONG), len(MISH), len(SO), NT)   # every range read WHOLE
ncred_link = sum(1 for k, a, _ in ADDR if k == 'LINK' and a in CRED); ncred_topic = sum(1 for k, a, _ in ADDR if k == 'TOPIC' and a in CRED)
verses = Counter(h for k, _, vs in ADDR if k == 'LINK' for h in vs.split())
hdr = (f'# THE EXAM DOCKET — Numbers 33:1-56 (the journeys: the heading and the writing, the departure on the morrow of the Passover with the judgments on the gods, the forty-two stations, Aaron\'s death retold with its date and age, Arad\'s hearing, the command in the plains of Moab — the dispossession, the three objects, the lot restated, the negative arm), THE NUMBERS WALK sitting 13b, the compile (2026-09-12; the owner: "Go" after the #152 rereads, on 1b\'s order — the measurements, the design, the probes, the docket, the types, the runner; the design World/step9/NUMBERS_WALK.md "Sitting 13b").\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of Numbers 33:1-56 (the scan by script over Data/sefaria_export, commentaries excluded: {NL} rows in {len(works)} works — ' + ', '.join(f'{w} {n}' for w, n in works.most_common()) + '; the verses cited ' + ', '.join(f'{v} {n}' for v, n in verses.most_common()) + f' — the death\'s date, Arad\'s hearing and the last camp\'s extent the most), and (2) THE TOPIC-ROUTED ROWS — Mishnah Zevachim 14:4-8 (the high places\' eras — the five rows read WHOLE to decide the sense: ISRAEL\'S PRIVATE ALTARS, the erection runner\'s block, not 33:52\'s Canaanite high places), the four folio ranges of COMPILE_DEBT\'s sitting-13 box (l) read WHOLE with the link rows dropped — ' + '; '.join(f'{r} {s} segments ({l} link rows)' for r, s, l in LONG) + f' — and Seder Olam Rabbah 9-10 ({len(SO)} rows, the fortieth year\'s walk): {NT} topic rows. THE CUT, DECLARED: Zevachim 112b-119b was SIZED at the scan ({ZV[0][0]} segments, {ZV[0][1]} link rows — jou_docket_scan_sized.out) and cut from the docket as the private altar\'s own sugya (the sense the Mishnah rows decide); the design said "sized and cut at the scan\'s print". {len(CRED)} addresses already verdicted in earlier ledgers are marked CREDITED with their ledger and given a QUICK LOOK here (speed ruling (b), credit guard (1)) — {ncred_link} link rows, {ncred_topic} topic rows; Bava Batra 117a-122a whole is the second census\'s and Gad and Reuben\'s dockets\', read there and looked at here for 33:53-54\'s restatement of the land\'s gift and the lot; Seder Olam Rabbah 9:2 and 10:2 credited to the chukat and second census dockets and READ WHOLE here for the walk. Every address gets ONE verdict: LAW (a rule the runner must reproduce — the cell named: F1 the_heading_and_the_writing, F2 the_departure, F3 the_stations, F4 aarons_death_retold, F5 the_command, or the callee\'s cell by CALL), DERIVATION (a hook from the verse to a rule — a labeled move), DISPUTE (a parameter row — a DATA row named), CONTEXT, OUTSIDE (the export\'s empty or editorial row). Terse for the non-material (speed ruling (c)). The Tanchuma on the forty-two is OUTSIDE the declared spine and not opened (the box\'s own line).\n'
       f'# THE TALMUD ADDRESSING: the export\'s index 0 is folio 1a (a page = index // 2 + 1; measured 2026-09-09); the Mishnah by chapter:mishnah; Seder Olam Rabbah by chapter:segment (the export\'s text a dict under an empty key — 8b\'s fifth defect class).\n')
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
- THE FORTIETH YEAR'S WALK IN THE SHELF'S OWN ORDER (Seder Olam Rabbah 9:2, read whole): Zin in the first month, Miriam, the well gone, the messengers from Kadesh, THREE MONTHS AT KADESH, "Aaron was 123 years old when he died at Mount Hor" (33:39), the clouds gone and Arad hears (33:40 quoted with its question "what hearing did he hear?"), THE RETREAT OF SEVEN STATIONS TO MOSERAH — "did Aaron die in Moserah? did he not die at Mount Hor? rather, from where Aaron died they retreated seven stations until Moserah" — Deuteronomy 10:6's order reconciled with 33:38 by a retreat, and THE ITINERARY'S OWN COUNT AGREES: Moseroth (33:30) stands seven camps before Mount Hor (33:37) by index, the reading's measurement equal to the shelf's seven; the chukat runner's row CK.DATA['moserah'] has this row as its source and is CALLED; the three months at Kadesh are the tape's markers (40, 1, 1) and (40, 4, 1), READING-PLACED by this row at sitting 6b.
- THE ERA'S NEW YEAR FROM THE CHAPTER'S OWN DATE (Rosh Hashanah 2b:9-3a:13): the fortieth year in Av (33:38) and in Shevat (Deuteronomy 1:3) one year — the exodus count's year does not turn in Tishrei; the second year in Nisan (Exodus 40:17) and Iyar (Numbers 10:11) — not Iyar; "the third month" without "the second year" (Exodus 19:1) — not Sivan; 1 Kings 6:1's 480th year the kings' count from the exodus — THE ERA'S THREE STAMPS (Exodus 19:1, Numbers 33:38, 1 Kings 6:1: the reading's crown) are the shelf's own chain of proof, with the verbal analogy "the fortieth year" / "the fortieth year" (2b:11) TAUGHT for Deuteronomy 1:3's bare date; the engine's Calendar (the exodus era registered at Exodus 12:2 with its new year in the first month) reproduces the whole chain — (40, 5, 1) and (40, 11, 1) in one year, (2, 1, 1) and (2, 2, 20) in one year: the checkpoint's arithmetic.
- THE MORROW OF THE PASSOVER AT BOTH ENDS (Berakhot 9a:25; Kiddushin 37b:14-38a:4): redeemed at evening, LEFT BY DAY — 33:3 the proof; Joshua 5:11 the land's produce on the morrow AFTER THE OMER (the new crop's "dwelling" wherever you dwell) or after the manna's end (the other arm); THE MANNA FORTY YEARS LESS THIRTY DAYS — from the sixteenth of Iyar (THE TAPE'S MARKER at Exodus 16:13 is (1, 2, 16)) to the sixteenth of Nisan, and thirty days of the cakes taken out on the fifteenth (33:3's date) with the manna's taste: the DATA row the_morrow_of_the_passover with the shelf's two arms; Seder Olam 10:2 the same reckoning.
- MOSES' SEVENTH OF ADAR (Kiddushin 38a:5-7; Seder Olam 10:2): the death computed BACKWARD from a run's marker — the tenth of Nisan (Joshua 4:19) less thirty-three days (thirty of mourning, three of preparation) — the shelf's own retrograde marker; born and died the same day, "a hundred and twenty years old THIS DAY" (Deuteronomy 31:2) — the years of the righteous completed to the day (Exodus 23:26): THE INK'S CHECKSUM ON THE BROTHERS' AGES (Aaron 83 + 40 = 123 at 33:39; Moses 80 + 40 = 120) confirmed by the shelf's rule that the count is exact; the tape's marker at Exodus 2:2 names this row already.
- "BY THE MOUTH OF THE LORD" IS THE KISS (Bava Batra 17a:3): 33:38's phrase read as the MANNER of Aaron's death (with Deuteronomy 34:5) — the chapter's phrase in a third sense (Moses WROTE by it at 33:2, Aaron WENT UP by it at 33:38, and DIED by it on the shelf); the chukat runner's row death_by_the_kiss by CALL.
- THE COMMAND'S RUN AT THE CROSSING (Sotah 34a:5): Joshua in the Jordan — "know for what purpose you cross: to drive out the inhabitants (33:52); if not, the water will drown me and you" — the dispossession debit's first run-reading with the negative arm as its condition; THE NEGATIVE ARM ON THE SHELF (Megillah 11a:13-14): Saul's Amalek left Haman as "thorns in your eyes" (33:55) and Purim's punishment "as I thought to do to them" (33:56) — two runs past Joshua 23:13 and Judges 2:3, the DATA row negative_arm_outcome's shelf arm.
- THE FIGURED STONE AT ITS BAN (Megillah 22b:11-13): "nor shall you install any figured stone in your land to bow down upon it" (Leviticus 26:1) — bowing on a stone floor outside the Temple, with outstretched arms and legs (Ulla): 33:52's word at its ban's seat, Israel's installing and bowing banned where the Canaanites' stones are commanded destroyed; THE CELL THAT COMPILES LEVITICUS 26:1 DOES NOT EXIST (measured at this sitting) — the row filed to the compile debt "Leviticus 26:1-2's own compile" as its first exam row; the edge journeys → tochacha OWED.
- THE PRIVATE ALTAR'S ERAS ARE NOT THIS CHAPTER'S HIGH PLACES (Mishnah Zevachim 14:4-8): the tabernacle, Gilgal, Shiloh, Nob and Gibeon, Jerusalem — Israel's own altars permitted and forbidden by era (the erection runner's high_places_banned block on the land); 33:52's "their high places" the Canaanites' to demolish (Leviticus 26:30's curse in the same verb): the sense decided on the five rows, the gemara's 265 segments cut and recorded.
- THE LAST CAMP'S EXTENT (Eruvin 55b:15; Yoma 75b:14): "from Beth-jeshimoth to Abel-shittim" (33:49) three parasangs by three — Rabba bar bar Chana "I saw that place": the itinerary's one camp with two ends, measured by a witness on the shelf; the DATA row the_camps_extent.
- ARAD'S IDENTITY DISPUTED (Rosh Hashanah 3a:3): "he is Sihon, he is Arad, he is Canaan" — one person under three names, two derivations of which is the real name; Taanit 9a's Amalek in disguise the registry row's other reading: the hearer of 33:40 a DATA arm.
- THE DIRECTIONAL ENDING (Yevamot 13b:6): "Diblathaimah" (33:46) among R. Nechemya's examples of the heh that stands for the lamed — the station's name carries the ink's grammar, kept in the DATA row's Hebrew form.
- THE SHELF ON ITS OWN MANUSCRIPTS (Seder Olam Rabbah 10:2): "Aaron on the first of Av" with the export's translator noting the French manuscripts' "first of Tammuz" against the Talmud — a variant on THE MONTH 33:38 FIXES AS THE FIFTH: OBSERVED, the ink's [40, 5] the instrument; and the translator's own line that "the remaining 38 years are without record except for the list of stations (Numbers 33)" — the design's premise (the itinerary the run's only witness for the thirty-eight years) said by the export's editor.
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_jou_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {NL}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {NT}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))}; credited {len(CRED)} — the counts this script computed from the dump and the verdict lists, never typed)\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('WROTE', OUT, len(ADDR), 'rows;', dict(cnt), '; link', dict(cnt_link), '; topic', dict(cnt_topic), '; credited', len(CRED), '; long ranges', len(LONG))
