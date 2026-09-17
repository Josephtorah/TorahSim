import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 3b — THE COMPILE OF CHAPTER 5 (2026-09-16): THE EXAM DOCKET for Deuteronomy 5:1-33, written from the scan's dump
# (scratchpad/ch5_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a verse of the
# chapter — by TWO numberings, the row's quoted words fixing the DB verse; the TOPIC rows = the three Mishnah rows and the ten folio ranges of the
# design's item (j) read WHOLE — the union rule of 2026-09-05, the second word's rows added by the design; the CREDITED marks = addresses already
# verdicted in an earlier ledger, given their quick look here). Every address in the dump gets ONE verdict (parts A..D on disk); the coverage is
# COMPUTED from the dump, never typed; the ranges' sizes are read from the scan's own print (ch5_docket_scan.out). Append-only. write_ch4_docket.py's form.
import re, os, sys, importlib.util, subprocess
from collections import Counter
ROOT = _ROOT
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{ROOT}/logic/oral_triage/deu_05_vaetchanan_exam_2026-09-16.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/ch5_docket_dump.txt', encoding='utf-8').read()
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
    part = f'ch5_docket_{p}'
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
scan = open(f'{SCR}/ch5_docket_scan.out', encoding='utf-8').read()
scan = scan[scan.index('THE RANGES SIZED:'):]
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) segments,\s+(\d+) link rows', scan, re.M)]   # read from the scan's print
assert len(LONG) == 10, len(LONG)
MISH = [a for k, a, _ in ADDR if k == 'TOPIC' and not re.search(r'\d+[ab]:\d+$', a)]   # the Mishnah rows
assert len(MISH) == 3, MISH   # Shevuot 3:8-9 and Sanhedrin 7:6 — the scan's print
assert sum(s - l for _, s, l in LONG) + len(MISH) == NT, (sum(s - l for _, s, l in LONG), len(MISH), NT)   # every range read WHOLE
ncred_link = sum(1 for k, a, _ in ADDR if k == 'LINK' and a in CRED); ncred_topic = sum(1 for k, a, _ in ADDR if k == 'TOPIC' and a in CRED)
verses = Counter(h for k, _, vs in ADDR if k == 'LINK' for h in re.findall(r'Deut 5:\d+', vs))
LAWCELLS = Counter(m.group(1) for vd, note in V.values() if vd == 'LAW' for m in [re.search(r'\b(F[1-7])\b', note)] if m)
hdr = (f'# THE EXAM DOCKET — Deuteronomy 5:1-33 (the covenant at Horeb retold; THE SECOND COPY OF THE TEN WORDS — the laws\' readback, code against code; the second and the tenth words compiled here; the voice and the tablets; the people\'s request for a mediator and the LORD\'s answer — return to your tents, stand here with me), THE DEUTERONOMY WALK sitting 3b (2026-09-16; World/step9/DEUTERONOMY_WALK.md "Sitting 3b"; the runner cold_run_covenant_at_horeb.py, the daemon law_covenant_at_horeb).\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of Deuteronomy 5 (the scan ch5_docket_scan.py: {NL} rows in {len(works)} works; THE CITATIONS FOLLOW TWO NUMBERINGS — the export\'s thirty-verse division and a second one a verse lower around the short words — so each verdict names the DB verse BY THE ROW\'S QUOTED WORDS; the DB verses cited most, through the alignment, {", ".join(f"{v} {n}" for v, n in verses.most_common(7))}), and (2) THE TOPIC ROWS by address (the reading ledger\'s TESTING paragraph, COMPILE_DEBT\'s sitting-3 box (j), and the design\'s (b) — the second word\'s own answer sheet): the Mishnah rows {", ".join(MISH)} and the folio ranges read WHOLE — {"; ".join(f"{n} ({s} segments, {l} of them link rows)" for n, s, l in LONG)} = {NT} topic rows. EVERY ADDRESS ONE VERDICT: LAW (the cell of cold_run_covenant_at_horeb.py named — F1 the_assembly_called, F2 the_second_word, F3 the_first_tablet, F4 the_second_tablet, F5 the_tenth_word, F6 the_voice_and_the_request, F7 the_answer_and_the_charge — or the callee\'s cell by CALL), DERIVATION, DISPUTE, CONTEXT, OUTSIDE; {len(CRED)} addresses CREDITED from earlier ledgers (link {ncred_link}, topic {ncred_topic}) with their quick look. The rows are the answer sheet\'s: the Mishnah GRADES, the Talmud TEACHES per gap; nothing here is code.\n'
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
- THE FIRST TWO WORDS FROM THE ALMIGHTY'S MOUTH (Makkot 24a:1): 611 the mitzvot Moses taught, and two — "I am the LORD your God", "you shall have no other gods" (5:6-7) — heard directly: the tradition's own reading of the request for a mediator (5:5 "I stood between the LORD and you"; 5:27 "you speak to us … and we will hear"): F6 the_request (the write torah_through_moses), the DATA row the_mediator.
- REMEMBER AND KEEP IN ONE UTTERANCE (Shevuot 20b:9; Rosh Hashanah 27a:2, 27a:6; Berakhot 20b:10; Shabbat 33b:8): the fourth word's first diff (5:12 KEEP for REMEMBER) is the tradition's exhibit of one utterance saying two words — the vain and the false oath "one" by the same rule (the decalogue runner's own ask vain_and_false_utterance); women obligated in kiddush because whoever is in "keep" is in "remember" (Rava): F3 keep_and_remember; the Sifrei 233:1's exhibit at its Talmud seats (the schema question's).
- THE RECEIPT INSIDE THE CODE READ AS MARAH (Sanhedrin 56b:16; Shabbat 87b:1): "as the LORD your God commanded you" (5:12, 5:16) — Rav Yehuda: commanded at Marah (Exodus 15:25 — the Sabbath and honoring parents among the statutes there): the teacher's referent of the receipt beside the ink's plain one (the first giving, 20:8, 20:12); the register seats' pointers name both: F3 the_receipt_5_12, F4 the_receipt_5_16, the DATA row the_receipts.
- THE OX AND THE ASS EVERY ANIMAL (Bava Kamma 54b:13 with 54b:9-11, 54b:25, 67b:6; Bava Metzia 89a:1): R. Yosei in R. Yishmael's name — the second copy's "your ox and your ass" inside "all your cattle" (5:14) teaches that wherever "ox and ass" are written every animal is meant — the readback row 5:14 EXPANDED read by the tradition itself as a teaching; the servants' rest "like you" the analogy's limit (54b:28): F3 the_ox_and_the_ass, the_servants_rest.
- THE SERVANT'S REST AND THE STRANGER'S TWO KINDS (Yevamot 48b:5-6): "that your servant and maidservant may rest like you" (5:14) the circumcised slave; "your stranger within your gates" the righteous convert — Exodus 23:12's the uncircumcised slave and the resident alien: F3 the_servants_rest.
- "GOOD" NOT IN THE FIRST TABLETS (Bava Kamma 55a:1; Chullin 110b:3, 142a:3; Kiddushin 39b:7, 40a:5): the fifth word's expansion "and that it may go well with you" (5:16) has its own Talmud row — why here and not at Sinai (the answer named in the next segment: the first tablets were to be broken); a mitzva whose reward is stated beside it — the court does not enforce it (Rami bar Tamrei), the reward after the resurrection (R. Yaakov) or in this world (Rava): F4 the_reward_clause, the DATA row.
- THE HONOR DEFINED AT ITS KIN'S SEAT (Kiddushin 30b:16-31b:14): what is fear (his place, his seat, his words, his side) and what is honor (feed, dress, bring in and out — 31b:14); the three equations (honor with wealth, fear with fear, cursing with cursing — 30b:18-20); the three partners (30b:21); the father first in "honor", the mother first in "fear" (30b:22-31a:1); the woman's duty under her husband (30b:16-17); the father first when both ask (31a:4-5); how far — Dama ben Netina (31a:8-13); the manner (31a:14); in life and in death (31b:10-13): the fifth word compiled at Leviticus 19:3's cell — holiness.frame by CALL: F4 the_fifth_word, the DATA row the_honor_by_call.
- THE THEFT OF PERSONS BY THE CONTEXT (Sanhedrin 86a:15-17 with 86a:1-14): "you shall not steal" (20:15 / 5:19) speaks of persons — a matter learned from its context (murder, adultery: capital); Leviticus 19:11's of property by its context; the abduction's arms — the one already found in his hand (the father, the teachers), the half-slave (R. Yehuda / the Rabbis): the decalogue runner's own move at its Talmud seat: F4 the_eighth_word (decalogue.theft_commandment by CALL).
- THE COVETER WHO PAYS (Bava Metzia 5b:19-20): Rav Acha of Difti — taking by force or deceit violates "you shall not covet" (20:17 / 5:21) EVEN WITH PAYMENT; most people read it as taking without payment, so the bailee who pays is not disqualified: the tenth word's answer sheet, compiled here: F5 the_tenth_word, the_coveter_who_pays.
- THE FOUR SERVICES AND THE BOWER'S MODE (Mishnah Sanhedrin 7:6; Sanhedrin 60b:1-19): the idolater stoned — the worshipper in its way, the slaughterer, the incense-burner, the libation-pourer, the bower even not in its way (the Temple's rites emptied to the Name — "except to the LORD alone", Exodus 22:19); the hugger and kisser a prohibition without death; bowing's death by the juxtaposition of 17:3 to 17:5 and its prohibition from 34:14 ("you shall bow to no other god" — not the second word's "to them"); Rava bar Rav Chanan's "any honorable service" the disputed arm: the second word's answer sheet, compiled here: F2 the_second_word, bow_and_serve, the DATA row the_second_word.
- THE VISITING CLAUSE REVOKED (Makkot 24a:30): "he visits the transgression of the fathers upon the sons" (Exodus 34:7 — 5:9's clause) revoked by Ezekiel 18:4 — beside Berakhot 7a's "when they hold their fathers' deeds": the DATA row the_visiting's two arms.
- "WE WILL DO" BEFORE "WE WILL HEAR" (Shabbat 88a:7-9 with 88a:5): R. Simai's two crowns, the calf's removal; the angels' secret (R. Elazar); the heretic's "impulsive nation"; the mountain overturned like a tub and the caveat: the TURNED row 5:27 ("we will hear and do") against 24:7's order: F6 hear_and_do.
- RETURN TO YOUR TENTS (Beitzah 5a:7-5b:3; Shabbat 87a:4; Yevamot 62a:2; Moed Katan 7b:5, 15b:13; Sanhedrin 59b:3-4; Avodah Zarah 5a:7): the separation of Exodus 19:15 released by 5:30 — a matter forbidden by a count needs a count to permit (Rav Yosef); "his tent" his wife; procreation repeated at Sinai; Moses' own separation agreed by "and you, stand here with me": F7 return_to_your_tents (the write returned_to_tents), stand_here_with_me.
- STAND HERE WITH ME (Megillah 21a:14): the Torah read standing from 5:31; "with me" — He too stood: F7 stand_here_with_me (the Sifrei 357:40's kin).
- DID NOT CEASE (Sanhedrin 17a:9-13; Sotah 10b:12): "a great voice, and it did not cease" (5:22) — Eldad and Medad who did not stop; Judah who did not cease: the DATA note "added no more" / "did not cease" (Onkelos): F6 added_no_more.
- THE TEN AS ONE VOICE AND ONE READING (Kiddushin 31a:6-7; Berakhot 12a:4-8): the nations conceded the first words when the fifth was said — "the words of Your mouth"; the priests read the ten daily in the Temple, the provinces sought it and it was abolished for the heretics' grievance: the ten words a unit on the shelf — the DATA row the_readback's setting (the schema question's second exhibit).
- THE SECOND COPY'S OWN STATUS (Sotah 37b:3 with 37b:1-6): R. Akiva — generals and details said at Sinai, repeated at the Tent, and reiterated a third time by Moses in the plains of Moab; R. Yishmael — the generals at Sinai only; the covenants counted forty-eight per mitzva, times 603,550 guarantors ("with us, we who are all here alive this day", 5:3): the readback's teacher — the DATA row the_readback's setting 'the_third_telling'; F1 the_covenant_at_horeb.
- THE DAY AND THE VOICE HEARD BY ALL (Yoma 4b:1-8): the sixth or the seventh of Sivan (the sinai_days row's two settings — the retrograde marker at 5:23 dated on R. Yosei's seventh); "He called to Moses" — all Israel standing and listening, at the Tent Moses alone (Numbers 7:89): F1 face_in_face, the DATA row the_face_in_face.
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_ch5_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {NL}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {NT}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))}; credited {len(CRED)} — the counts this script computed from the dump and the verdict lists, never typed).\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('WROTE', OUT, os.path.getsize(OUT), 'bytes')
print('rows', len(ADDR), 'link', NL, 'topic', NT, 'credited', len(CRED), '(link', ncred_link, 'topic', ncred_topic, ')')
print('verdicts', dict(sorted(cnt.items())), 'link', dict(sorted(cnt_link.items())), 'topic', dict(sorted(cnt_topic.items())))
print('LAW by cell', dict(sorted(LAWCELLS.items())))
print('ranges', [(n, s, l) for n, s, l in LONG]); print('mishnah rows', len(MISH))
