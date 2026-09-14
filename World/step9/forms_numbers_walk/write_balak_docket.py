#!/usr/bin/env python3
# THE NUMBERS WALK 7b — THE COMPILE OF BALAK (2026-09-11): THE EXAM DOCKET for Numbers 22:1-25:19, written from the scan's dump
# (scratchpad/balak_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a
# verse of the span; the TOPIC rows = the Mishnah's rows the four reading ledgers and the debt box name BY ADDRESS, Sanhedrin 105a-106b
# whole, and the Jerusalem Talmud's two halakhot — the union rule of 2026-09-05; the CREDITED marks = addresses already verdicted in an
# earlier ledger, given their quick look here). Every address in the dump gets ONE verdict (parts A, B, C, D); the coverage is COMPUTED
# from the dump, never typed; the long ranges' sizes are read from the scan's own print. Append-only once written.
import re, os, sys, importlib.util
from collections import Counter
ROOT = '<repo-old>'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{ROOT}/logic/oral_triage/num_22_25_balak_exam_2026-09-11.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/balak_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR, CRED = [], {}
for k, a, rest in rows:
    m = re.search(r'\{CREDITED: (.*?)\}', rest)
    if m: CRED[a.strip()] = m.group(1)
    ADDR.append((k, a.strip(), re.sub(r'\s*\{CREDITED:.*?\}', '', rest).strip()))
assert len(ADDR) == 199 and sum(1 for k, _, _ in ADDR if k == 'LINK') == 88 and len(CRED) == 20, (len(ADDR), len(CRED))
V = {}
for part in ('balak_docket_A', 'balak_docket_B', 'balak_docket_C', 'balak_docket_D'):
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
scan = open(f'{SCR}/balak_scan1.out', encoding='utf-8').read()
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) segments,\s+(\d+) link rows', scan, re.M)]   # read from the scan's print
assert len(LONG) == 24, len(LONG)
ncred_link = sum(1 for k, a, _ in ADDR if k == 'LINK' and a in CRED); ncred_topic = sum(1 for k, a, _ in ADDR if k == 'TOPIC' and a in CRED)
ntopic = Counter(a.rsplit(' ', 1)[0].replace(' 105a', '').replace(' 105b', '').replace(' 106a', '').replace(' 106b', '') for k, a, _ in ADDR if k == 'TOPIC')
hdr = (f'# THE EXAM DOCKET — Numbers 22:1-25:19 (Balak), THE NUMBERS WALK sitting 7b, the compile (2026-09-11; the owner: "Go" after the #131 rereads, on the ruling READ THEN COMPILE; the design World/step9/NUMBERS_WALK.md "Sitting 7b").\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of the span (the scan by script over Data/sefaria_export, commentaries excluded: {sum(1 for k, _, _ in ADDR if k == "LINK")} rows in {len(works)} works — ' + ', '.join(f'{w} {n}' for w, n in works.most_common()) + '), and (2) THE TOPIC-ROUTED ROWS — the rows the four reading ledgers\' TESTING SHELF lines and the COMPILE_DEBT box name BY ADDRESS: Mishnah Sanhedrin 7:6 (baring to Peor), 9:6 (the zealots — THE ANSWER SHEET), 10:1-2 (Balaam\'s share); Pirkei Avot 5:6 (the mouth of the ass), 5:19 (Balaam\'s disciples); SANHEDRIN 105a-106b WHOLE — the Balaam sugya (the Talmud\'s case discussion): 76 segments in the range, 22 of them link rows, the other 54 here by address; and the JERUSALEM TALMUD\'s Taanit 4:5 (R. Akiva\'s star — 24 segments) and Sanhedrin 10:2 (Balaam\'s share, the Peor story, the judges\' arithmetic — 27 segments), every segment of each halakhah (the law-section): {sum(1 for k, _, _ in ADDR if k == "TOPIC")} rows, link-duplicates dropped. {len(CRED)} addresses ({ncred_link} link, {ncred_topic} topic) were ALREADY VERDICTED in earlier ledgers and are marked CREDITED with the ledger named — each given its QUICK LOOK here (speed ruling (b), credit guard (1)), never a blind credit. Every row carries ONE verdict: LAW (a rule the compiled function answers — the CELL named), DERIVATION (a hook from the verse to a rule), DISPUTE (a parameter row), CONTEXT, OUTSIDE. The Sifrei on Numbers piska 131 (the reading shelf) was read at sitting 7, not here.\n'
       f'# THE LONG TALMUD RANGES the ledgers name ("the tractate is the exam") enter through the link rows or whole by address; their remainder is OUTSIDE DECLARED SCOPE, enumerated by count, never silently narrowed: ' + '; '.join(f'{n} ({s} segments, {l} of them link rows read here, {s - l} {"read whole by address" if n.startswith("Sanhedrin 105a") else "outside"})' for n, s, l in LONG) + '.\n'
       f'# THE TALMUD ADDRESSING: the export\'s index 0 is folio 1a (a page = index // 2 + 1; measured 2026-09-09); the Mishnah by chapter:mishnah; the Jerusalem Talmud by chapter:halakhah:segment of the export (the translator\'s footnotes run inline in the text — read around them; measured 2026-09-11).\n')
body = ''
last = None
for k, a, vs in ADDR:
    work = a.rsplit(' ', 1)[0] if not a.startswith('Jerusalem') else ' '.join(a.split()[:3])
    if work != last:
        body += f'\n## {work}\n'; last = work
    vd, note = V[a]
    body += f'- {a} [{k}{(" — " + vs) if vs else ""}{(" — CREDITED: " + CRED[a]) if a in CRED else ""}] — {vd}. {note}\n'
crowns = '''
## The finds (this docket's crowns)
- THE ZEALOTS' RULE ON THE ANSWER SHEET AND ITS FOUR LIMITS (Mishnah Sanhedrin 9:6; Sanhedrin 82a:10-12; Avodah Zarah 36b:9): "one who cohabits with an Aramean woman — zealots strike him" — no court death written, the zealous may; DURING THE ACT ONLY (separated, the zealot is a murderer), the pursued may kill the zealot in self-defense (a pursuer), the rule NOT TAUGHT to one who asks (Moses forgot it, the Sanhedrin wept, the zealot remembered), a law to Moses from Sinai and not a decree — the deed at 25:7-8 the rule's installing act, the reward at 25:10-13 its ratification: the tape's second seat of THE TENT's form, with no halt and no docket.
- THE JUDGES' ARITHMETIC ON TWO SHELVES (Sanhedrin 35a:2; the Jerusalem Talmud Sanhedrin 10:2:17): "take the heads and hang them" = install the heads as JUDGES and let them execute by day — Onkelos's court at the reading is the Jerusalem Talmud's rule; the judges 78,600 = 600 + 6,000 + 12,000 + 60,000 of Exod 18:21's tiers, each executing two = 157,200 — the exodus engine's cell by CALL and the multiplication computed.
- THE MOMENT OF ANGER (Berakhot 7a:8-13; Avodah Zarah 4b:4-5; Sanhedrin 105b:5-10): "and knows the knowledge of the Most High" = the one moment of God's daily anger — one 58,888th of an hour, in the first three hours when the kings crown themselves to the sun and the rooster's crest whitens — and "how shall I curse whom God has not cursed" = no anger all Balaam's days (Micah 6:5 the retelling's own witness).
- PHINEHAS NOT A PRIEST UNTIL THE DEED (Zevachim 101b:10; Kiddushin 66b:10-13; Ketubot 13b:16; Yevamot 100b:8): "the covenant of an everlasting priesthood" written only after Zimri — the priesthood engine's addressees row (the sons of Aaron bound) gains its named exception; the covenant's "shalom" read "whole" for the blemished priest (Rav Nachman: the vav severed by tradition — a letter's shape the DB's bytes cannot carry), "his seed after him" the attribution rule (the shetuki), the unfit seed's service valid after the fact.
- THE DATING DATUM ON THREE SHELVES (Sanhedrin 106a:10; the Jerusalem Talmud Sanhedrin 10:2:15; the Sifrei 131:2 at the reading): the jug of Ammonite wine "not yet forbidden" at Peor — the decree on gentile wine (Avodah Zarah 36b) is LATER than the sin: a law's installation dated by the shelf against the tape.
- THE LID'S WORD ON THE SHELF (Sanhedrin 64a:11): "attached to Baal-peor" = a cord-bound cover [tzamid patil] — 19:15's lid, the reading's crown, is the Talmud's own simile for the yoking; against "you who cleave to the LORD" like two dates.
- THE TENTS' DOORS (Bava Batra 60a:5): "he saw Israel dwelling by its tribes" — the entrances not aligned: the privacy rule's source in Balaam's sight of chapter 2's camp.
- THE CURSES TURNED, A TABLE (Sanhedrin 105b:17-19; Taanit 20a:15; Sanhedrin 105b:20-106a:2): each clause of 24:5-7 the curse he intended; all reverted but the synagogues — Deut 23:6's singular "curse"; and the cedar-blessing worse than Ahijah's reed-curse.
- THE FORTY-TWO OFFERINGS' REWARD (Sanhedrin 105b:12; Nazir 23b; Horayot 10b): the parser's 7, 7, 7 at three stands = twenty-one altars, forty-two beasts — Ruth from Balak; and the intention table: Tamar for a mitzvah against Zimri for a transgression (24,000).
- THE SHEMA'S CANDIDATE (Berakhot 12b:15-16): Balak's portion nearly fixed in the Shema for 24:9's "he lay down... who shall rouse him" — the reading's Judah-blessing crown the Sages' reason.
- THE BLOOD OF THE SLAIN AS A LIQUID (Chullin 35b; Keritot 22a; Niddah 19b, 55b): 23:24's clause the source that blood after death renders food susceptible — the oracle's poetry a purity rule's proof-text.
- THE STAR APPLIED AND REFUSED (the Jerusalem Talmud Taanit 4:5:13): R. Akiva's "Koziba out of Jacob — this is King Messiah" against R. Yochanan ben Torta — Onkelos's KING and MESSIAH at the reading, the application on the Jerusalem shelf.
- THE DIVINER'S TITLES IN ORDER (Sanhedrin 106a:16-17, 106b:1; the Jerusalem Talmud 10:2:18): first a prophet, at the end a diviner (Josh 13:22); at Midian to collect his wages for the 24,000; slain with all four modes (Rav); "on their slain" four ways.
- THE NINTH OF AV'S SECOND COMPUTATION (the Jerusalem Talmud Taanit 4:5:8): 10:11 + three days + the month + Miriam's seven + the forty = the ninth of the fifth month by the translator's 29/30/29 — beside Taanit 29a's, recorded for Shelach's CF2.
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_balak_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {sum(1 for k, _, _ in ADDR if k == "LINK")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {sum(1 for k, _, _ in ADDR if k == "TOPIC")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))}; credited {len(CRED)} — the counts this script computed from the dump and the verdict lists, never typed)\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('WROTE', OUT, len(ADDR), 'rows;', dict(cnt), '; link', dict(cnt_link), '; topic', dict(cnt_topic), '; credited', len(CRED), '; long ranges', len(LONG))
