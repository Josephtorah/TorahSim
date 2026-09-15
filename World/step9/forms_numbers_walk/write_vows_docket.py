import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK 10b — THE COMPILE OF THE VOWS (2026-09-12): THE EXAM DOCKET for Numbers 30:1-17, written from the scan's dump
# (scratchpad/vows_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a verse of the
# span; the TOPIC rows = Mishnah Nedarim chapters 9-11 WHOLE and the twelve folio ranges of the reading ledger's TESTING SHELF line read WHOLE —
# the union rule of 2026-09-05; the CREDITED marks = addresses already verdicted in an earlier ledger, given their quick look here). Every address
# in the dump gets ONE verdict (parts A..M); the coverage is COMPUTED from the dump, never typed; the ranges' sizes are read from the scan's own
# print (vows_docket_scan.out). Append-only. write_musafim_docket.py's form.
import re, os, sys, importlib.util
from collections import Counter
ROOT = _ROOT
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{ROOT}/logic/oral_triage/num_30_vows_exam_2026-09-12.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/vows_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR, CRED = [], {}
for k, a, rest in rows:
    m = re.search(r'\{CREDITED: (.*?)\}', rest)
    if m: CRED[a.strip()] = m.group(1)
    ADDR.append((k, a.strip(), re.sub(r'\s*\{CREDITED:.*?\}', '', rest).strip()))
NL = sum(1 for k, _, _ in ADDR if k == 'LINK'); NT = len(ADDR) - NL
assert len(ADDR) == 1047 and NL == 90 and len(CRED) == 82, (len(ADDR), NL, len(CRED))
V = {}
for p in 'ABCDEFGHIJKLM':
    part = f'vows_docket_{p}'
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
assert len(works) == 16, len(works)
scan = open(f'{SCR}/vows_docket_scan.out', encoding='utf-8').read()
scan = scan[scan.index('THE RANGES SIZED:'):]
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) segments,\s+(\d+) link rows', scan, re.M)]   # read from the scan's print
assert len(LONG) == 12, len(LONG)
MISH = [a for k, a, _ in ADDR if k == 'TOPIC' and a.startswith('Mishnah')]
assert sum(s - l for _, s, l in LONG) + len(MISH) == NT, (sum(s - l for _, s, l in LONG), len(MISH), NT)   # every range read WHOLE: the topic rows = the ranges' non-link segments + the Mishnah rows
ncred_link = sum(1 for k, a, _ in ADDR if k == 'LINK' and a in CRED); ncred_topic = sum(1 for k, a, _ in ADDR if k == 'TOPIC' and a in CRED)
hdr = (f'# THE EXAM DOCKET — Numbers 30:1-17 (the vows: a man\'s vow and oath, the daughter in her father\'s house, the betrothed, the widow and the divorcee, the married woman, the affliction oath, the statutes), THE NUMBERS WALK sitting 10b, the compile (2026-09-12; the owner: "Go" after the #142 rereads, on 1b\'s order — the measurements, the design, the probes, the docket, the types, the runner; the design World/step9/NUMBERS_WALK.md "Sitting 10b").\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of Numbers 30:1-17 (the scan by script over Data/sefaria_export, commentaries excluded: {NL} rows in {len(works)} works — ' + ', '.join(f'{w} {n}' for w, n in works.most_common()) + f'), and (2) THE TOPIC-ROUTED ROWS — Mishnah Nedarim chapters 9, 10 and 11 WHOLE (the release by a sage; the father, the betrothed, the married, the day; which vows he annuls — {len(MISH)} mishnayot beyond the links) and the twelve folio ranges of the reading ledger\'s TESTING SHELF line (logic/oral_triage/num_30_vows_2026-09-12.md) and COMPILE_DEBT\'s sitting-10 box (h), read WHOLE with the link rows dropped: ' + '; '.join(f'{r} {s} segments ({l} link rows)' for r, s, l in LONG) + f' — {NT} topic rows. {len(CRED)} addresses already verdicted in earlier ledgers are marked CREDITED with their ledger and given a QUICK LOOK here (speed ruling (b), credit guard (1)) — {ncred_link} link rows, {ncred_topic} topic rows. Every address gets ONE verdict: LAW (a rule the runner must reproduce — the cell named: F1 the_man, F2 the_daughter, F3 the_betrothed, F4 the_widow, F5 the_wife, F6 the_affliction_oath, F7 the_statutes, or the callee\'s cell by CALL), DERIVATION (a hook from the verse to a rule — a labeled move), DISPUTE (a parameter row — a DATA row named), CONTEXT, OUTSIDE (the shelf\'s empty segments and rows outside the span\'s question). Terse for the non-material (speed ruling (c)).\n'
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
- THE FOOTER IS THE LAW'S ENGINE ON THE TALMUD'S PAGE TOO: the school of R. Yishmael derives the betrothed maiden's JOINT annulment from 30:17 "between a man and his wife, between a father and his daughter" (Nedarim 68a:1) where Rabba derives it from 30:7-9 (67a:5) — the Sifrei 156:3's likening at both seats; and 30:17's "between a man and his wife" supplies THE FILTER's second class — vows that touch the marriage even without affliction (68a:2, 79b:2); Ketubot and Kiddushin take "in her youth, in her father's house" for the father's rights beyond vows (Ketubot 40b:4, 46b:6; Kiddushin 3b:7).
- THE DOUBLED VERBS READ AS LAW: "be, she SHALL BE to a husband" (30:7) = TWO BETROTHALS — the betrothed dies and the authority reverts to the father (Nedarim 70a:8, 70b:1); "confirm IT ... annul IT" (30:14) — R. Akiva hears a mem inside the suffix ("confirm PART of it", yakim mimmennu, 87b:1: the revocalization class of M-16), R. Yishmael answers "is it written with a mem?", and THE RABBIS a third arm: what he annulled he annulled, what he confirmed he confirmed, no more (87b:2) — the reading's five doubled verbs at their exam seats.
- THE DEADLINE RULED ON THE PAGE: the whole day till dark (the first tanna from "on the day that he hears", 30:13) against THE PAIR's twenty-four hours from "from day to day" (30:15) — R. Yehoshua b. Levi: THE HALAKHA (the ruling) IS NOT AS THAT PAIR (Nedarim 76b:4-8; the Sifrei 156:1's R. Shimon ben Yochai = the pair); each arm reads BOTH clauses (76b:6-7: the night inside the day / not a week); the Sabbath's annulment hangs on the arm (77a:3-4; Shabbat 157a:9-11); R. Chanina's "silence to vex annuls ten days later" REFUTED THREE TIMES (79a:5, 79a:7, 79a:9) — the timer fires at nightfall whatever the intent; "superfluous verses are written about silence" (79a:6).
- EACH OFFICE ITS OWN VERB: "this is the thing" (30:2) — the sage DISSOLVES and does not annul, the husband ANNULS and does not dissolve (77b:9-78a:1); a sage who said "annulled" or a husband who said "dissolved" HAS SAID NOTHING (77b:8); the dissolution of vows FLIES IN THE AIR (Mishnah Chagigah 1:8 at 10a:4) and Shmuel's one unrefuted ground is the chapter's own clause "he shall not profane his word" — he cannot, others can (10a:9, 10a:13: "one spicy pepper"); "the heads of the tribes" = a single expert, and three laymen by the verbal analogy or by ben Azzai (78a:3, 78b:2-3).
- THE STATE MACHINE'S ASYMMETRY WRITTEN ON THE SHELF: SILENCE CONFIRMS, silence does not annul; confirmed in the heart — confirmed, annulled in the heart — NOT annulled (Nedarim 79a:1; Beit Hillel: the heart annuls too, 77b:7); confirmed, never annulled; annulled, never confirmed; a sage dissolves a CONFIRMATION but not an annulment (69a:4, 79a:3); "confirmed and annulled at once" — nothing (69b:3); "what came to confirmation came to annulment" (75a:6, 76b:1); THE CONFIRMING WORDS are an act ("you did well", 77b:5).
- THE TWO REACHES: affliction vows annulled for himself AND FOR OTHERS; between-them vows for himself only — a divorce or a second husband revives them; "I am removed from the Jews" the test case (79b:3-5, 82a:1, 84a:2); the whole eleventh chapter R. YOSEI'S (82a:2, 82b:1; Shmuel rules as the Rabbis); Rava's two afflictions — Yom Kippur's felt now, the vows' what LEADS to affliction (80b:6); the affliction oath of 30:14 is Shevuot's "oath to harm himself" (27a:6).
- THE HEARING IS THE TRIGGER: the deaf excluded (73a:4); annulment WITHOUT hearing left UNRESOLVED (73a:1 — the machine keeps the ink's trigger and records the open); the advance annulment a conditional whose trigger is the hearing (72b:4-7); the MISTAKEN annulment void when the report was specified (86b:5, 87a:3-4; Mishnah 11:5) — and WITHIN THE TIME OF A SHORT PHRASE the act is still open, except the blasphemer, the idolater, the betrother and the divorcer (87a:5-8).
- THE AGES ON THE ANSWER SHEET: the girl of eleven and a day EXAMINED, twelve and a day valid; the boy twelve / thirteen (Mishnah Niddah 5:6 at 45b:2-4); no self-report moves the ends (45b:9); hairs during the time are as before (46a:3, 46a:12); the minor of the examined year who consecrated and ate is FLOGGED (46a:22); Rebbi against R. Shimon b. Elazar on the sexes' order (45b:10); 6:2's "man" includes thirteen and a day without clear utterance (46a:2) — the Sifrei 153:3's identity at its seat.
- THE VOW AND THE OATH ON ONE PAGE: vows take effect on a MITZVA, oaths on the INTANGIBLE (Nedarim 13b:4; Shevuot 25a:11-12); the vow leans on a VOWED thing, never a Torah-forbidden one (14a:5; 13a:2; the firstborn disputed, 12b:8-13a:7); konamot forbid ANY AMOUNT (Shevuot 22a:2, 22a:9); the oath needs THE LIPS (26b:9) and the willing heart's donation stands apart (26b:15-16); a vow on a limb binds (13b:3-5); "he shall not profane his word" covers the custom-vow by rabbinic law (15a:8, 81b:9).
- THE DELAY BAN'S CLOCKS: three festivals / in their order / one / two / by Sukkot (Rosh Hashanah 4a:13-14, 4b:2-10 — the musafim runner's vow_deadline row confirmed with a fifth setting, "two"); the POSITIVE mitzva at the first festival, the prohibition at the third (6a:16); CHARITY at once (6a:14); "the sin in you, not in your offering" and "not in your wife" (5b:5, 6a:3); Deuteronomy 23:24's clauses — a positive mitzva, a prohibition, the court's warrant (6a:5); the vow's DEBIT persists past its animal, the gift's does not (6a:12); the count restarts at a replacement's consecration (5b:11).
- THE MESSENGER AT FIVE SEATS: R. Yoshiyah's doubled "her husband" against R. Yonatan's "a man's agent is as himself" (Bava Metzia 96a:20; Nazir 12b:3; Nedarim 72b:8-10) — the Sifrei 153:6's pair; the principle's own sources (Kiddushin 41b:5 from the Passover's "the whole assembly shall slaughter it"; 42a:8 the court's STEWARD from "take one prince", Num 34:18 — the caretaker's office at its root).
- THE AUTHORITY TABLE'S EDGES: the levirate widow (R. Eliezer / R. Yehoshua / R. Akiva — Mishnah 10:6, 74a-75a); the sustained betrothed (10:5, 73b:5: "every woman vows on her husband's consent"); the two deaths and the reversion (68a:5-69a:2 — Beit Hillel: the annulment WEAKENS, never severs); the same-day divorce and remarriage (11:9, 89a:1); DIVORCE AS SILENCE OR CONFIRMATION unresolved (71b:2-72a:8); the nine young women of R. Yehuda against the Rabbis' THREE — the mature, the orphan, the orphan in her father's lifetime (89b:2).
- THE NAZIRITE'S INDIVISIBILITY: her naziriteship annulled WHOLE — no partial naziriteship (83a:3-6); the annulled vow leaves no lashes, the intent alone needs forgiveness (83a:1; Kiddushin 81b:5; Nazir 23a:3); "he shall not profane" and "you shall not delay" both on the nazirite (3a:7); the husband annuls her "and I" but not his own (Nazir 20b:4).
- RULES ABOUT RULES, LOGGED FOR MIDDOT: THE METHOD FORK with its lineages — R. Yishmael from R. Nechunya b. HaKana (generalization and detail), R. Akiva from Nachum of Gam Zo (amplification and restriction) — run on Leviticus 5:4 (Shevuot 26a:6-9); the identical-form preference (Yoma 76a:1); "grasped many, grasped nothing" (Rosh Hashanah 4b:15); two verses as one teach nothing outward (Shevuot 26b:18); the profane not from the sacred (26b:20); R. Yoshiyah's strict conjunction against R. Yonatan's inclusive (Shevuot 27a:15-16); the Sifrei's reversed induction answered on the page by the Talmud's own "I will reverse it" (Shevuot 26a:11).
- THE SHELF'S OWN GAPS: three EMPTY segments in the export (Nedarim 66b:9, 79a:10, 13b:6) — verdicted empty; a commentary-class work (the Rambam's introduction) caught by the scan and verdicted CONTEXT.
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_vows_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {NL}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {NT}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))}; credited {len(CRED)} — the counts this script computed from the dump and the verdict lists, never typed)\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('WROTE', OUT, len(ADDR), 'rows;', dict(cnt), '; link', dict(cnt_link), '; topic', dict(cnt_topic), '; credited', len(CRED), '; long ranges', len(LONG), '; mishnah topic rows', len(MISH))
