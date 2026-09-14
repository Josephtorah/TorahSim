#!/usr/bin/env python3
# THE NUMBERS WALK 6b — THE COMPILE OF CHUKAT (2026-09-11): THE EXAM DOCKET for Numbers 19:1-21:35, written from the scan's dump
# (scratchpad/chukat_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a
# verse of the span; the TOPIC rows = the Mishnah's rows the three reading ledgers and the debt box name BY ADDRESS plus the two Seder Olam
# segments — the union rule of 2026-09-05; the CREDITED marks = addresses already verdicted in an earlier ledger, given their quick look
# here). Every address in the dump gets ONE verdict (parts A, B, C, D, E); the coverage is COMPUTED from the dump, never typed; the long
# ranges' sizes are read from the scan's own print. Append-only once written.
import re, os, sys, importlib.util
from collections import Counter
ROOT = '<repo-old>'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{ROOT}/logic/oral_triage/num_19_21_chukat_exam_2026-09-11.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/chukat_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR, CRED = [], {}
for k, a, rest in rows:
    m = re.search(r'\{CREDITED: (.*?)\}', rest)
    if m: CRED[a.strip()] = m.group(1)
    ADDR.append((k, a.strip(), re.sub(r'\s*\{CREDITED:.*?\}', '', rest).strip()))
assert len(ADDR) == 480 and sum(1 for k, _, _ in ADDR if k == 'LINK') == 174 and len(CRED) == 60, (len(ADDR), len(CRED))
V = {}
for part in ('chukat_docket_A', 'chukat_docket_B', 'chukat_docket_C', 'chukat_docket_D', 'chukat_docket_E'):
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
scan = open(f'{SCR}/chukat_scan1.out', encoding='utf-8').read()
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) segments,\s+(\d+) link rows', scan, re.M)]   # read from the scan's print
assert len(LONG) == 43, len(LONG)
ncred_link = sum(1 for k, a, _ in ADDR if k == 'LINK' and a in CRED); ncred_topic = sum(1 for k, a, _ in ADDR if k == 'TOPIC' and a in CRED)
hdr = (f'# THE EXAM DOCKET — Numbers 19:1-21:35 (Chukat), THE NUMBERS WALK sitting 6b, the compile (2026-09-11; the owner: "Go" after the #128 rereads, on the ruling READ THEN COMPILE; the design World/step9/NUMBERS_WALK.md "Sitting 6b").\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of the span (the scan by script over Data/sefaria_export, commentaries excluded: {sum(1 for k, _, _ in ADDR if k == "LINK")} rows in {len(works)} works — ' + ', '.join(f'{w} {n}' for w, n in works.most_common()) + f'), and (2) THE TOPIC-ROUTED ROWS — the Mishnah tractates and chapters the three reading ledgers\' TESTING SHELF lines and the COMPILE_DEBT box name BY ADDRESS (Parah whole, Oholot whole, Kelim 1-2 and 9-10, Mikvaot 1-2, Keritot 1, Shevuot 1-2, Eduyot 1:14 and 6:2-3, Rosh Hashanah 3:8, Avot 5:6) with the two Seder Olam Rabbah segments the ledgers name (9:2, 10:2 — the fortieth year\'s chronology on the Midrash (the expounding books\') shelf), link-duplicates dropped: {sum(1 for k, _, _ in ADDR if k == "TOPIC")} rows. {len(CRED)} addresses ({ncred_link} link, {ncred_topic} topic) were ALREADY VERDICTED in earlier ledgers and are marked CREDITED with the ledger named — each given its QUICK LOOK here (speed ruling (b), credit guard (1)), never a blind credit. Every row carries ONE verdict: LAW (a rule the compiled function answers — the CELL named), DERIVATION (a hook from the verse to a rule), DISPUTE (a parameter row), CONTEXT, OUTSIDE.\n'
       f'# THE LONG TALMUD RANGES the ledgers name ("the tractate is the exam") enter through the link rows; their remainder is OUTSIDE DECLARED SCOPE, enumerated by count, never silently narrowed: ' + '; '.join(f'{n} ({s} segments, {l} of them link rows read here, {s - l} outside)' for n, s, l in LONG) + '.\n'
       f'# THE TALMUD ADDRESSING: the export\'s index 0 is folio 1a (a page = index // 2 + 1; measured 2026-09-09); the Mishnah by chapter:mishnah; Seder Olam Rabbah by chapter:segment of the export (its text keyed under an empty title after an empty Introduction — measured 2026-09-11).\n\n')
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
- THE HEIFER'S PARADOX ON THE ANSWER SHEET (Mishnah Parah 4:4, 8:3; Yoma 14a): everyone occupied with the heifer from the slaughter to the ashes defiles his garments, and the water that purifies the impure defiles the pure who carries it — "that which defiled you did not defile me, but you defiled me": the rite's contagion the reading measured on 19:7-10 and 19:21 is the tradition's own riddle, run as a rule.
- THE SADDUCEES' ROW (Mishnah Parah 3:7; Yoma 43b:3; Zevachim 17b:3; Yevamot 73a:1): the burning priest was DELIBERATELY DEFILED and immersed so the rite ran by a tevul yom (one who immersed that day) — "the pure one" of 19:19 read as pure only in relation to the impure — against the Sadducees' "only those on whom the sun has set": a parameter set on purpose, the record of the dispute in the act.
- WHO BURNS, WHO SLAUGHTERS (Yoma 42a-43a; Menachot 6b; Zevachim 14b, 68b; Chullin 32a): "give IT to Eleazar" — the first heifer by the deputy alone; after it the high priest (from "statute" / "statute" with the Day) or even a common priest; the slaughter by a priest (Rav — Eleazar and statute) or by a stranger while Eleazar watches (Shmuel — "before him"); the arms recorded as rows, the answer sheet (Parah 4:1) with R. Yehuda's own arm.
- THE SEVEN SPRINKLINGS INDISPENSABLE, EACH ITS OWN DIP (Menachot 27a-b; Mishnah Menachot 3:6; Parah 3:9, 4:2; Zevachim 40a): the parser's [7] at 19:4 is the count the Mishnah counts by hand — "the seventh from the sixth then a seventh: invalid; an eighth from the seventh: valid".
- THE BLOOD BURNED WITH THE FLESH (Menachot 7b:20; Zevachim 93b:14): the reading's measurement — the sin-bull's burn-list WITH THE BLOOD ADDED at 19:5 — is the Talmud's own inference: after the sprinklings the hand is wiped on the body so the remaining blood burns with it; between sprinklings the finger on the bowl's lip (Ezra 1:10's "atoning bowls").
- THE FOUR FAILURE STATES FIXED BY A FOUR-DAY INTERVAL (Kiddushin 62a:4-7; Shabbat 16b): "the third day and the seventh day" repeated at 19:12 and 19:19 — the third excludes the second, the seventh the sixth, and the third-and-EIGHTH is invalid too: a fixed interval; both sprinklings needed even for terumah — the timers' rule with its proof.
- THE PUNISHMENT SPLIT ON THE SHELF (Makkot 14b; Zevachim 33b, 43b; Shevuot 7b, 16b; Nazir 45a; Horayot 9b; Arakhin 3a:7): 19:13's "cut off" the punishment and 5:3's "they shall not defile their camp" the prohibition — the flogging and the karet; the tabernacle at 19:13 and the Temple at 19:20 the two verses the Sifrei paired — read by R. Elazar as OUTSIDE and INSIDE (the one made impure in the courtyard who lingers); the minor excluded from the karet, not the impurity; the high priest excluded (his offering is not the congregation's — Parah 12:4 "a high priest is never liable for entering").
- THE SWORD IS LIKE THE SLAIN (Pesachim 14b, 19b, 79a; Shabbat 101b): "one slain by a SWORD" at 19:16 — the reading's singular "one seat in the Bible" — is the tradition's source that a metal vessel takes the corpse's own grade: the field's first source read for its instrument.
- THE ASHES CALLED DUST FOR THE ANALOGY (Sotah 16b:15; Temurah 12b:7; Chullin 88b:8; Sotah 16a:4): "of the DUST of the burning" at 19:17 — the reading's ashes / dust pair — is R. Shimon's own note that the Torah changed its word to make the verbal analogy with the sotah's dust: the ashes ON the water as the dust on the water — the row mixing_order with naso's dust_order beside it, the order of the two rites the same by the changed word.
- THE SPRINKLER IS THE CARRIER (Yoma 14a:9; Niddah 9a:15; Mishnah Parah 12:5; Kelim 1:1-2): 19:21's "he who sprinkles shall wash his clothes" read as "he who CARRIES a sprinkling's worth" — the sprinkler clean, the carrier's grade heavier than the toucher's; the water under the measure a father by contact, above it by carrying: the Sifrei's own row (130) on the answer sheet.
- THE WELL DISAPPEARED AT MIRIAM'S DEATH (Taanit 9a:9; Seder Olam 10:2): "and Miriam died there" then "and there was no water for the congregation" — the two verses' adjacency the tradition's proof of the well by her merit; and THE TWO DAYS OF THE SAME SHELF — Seder Olam 9:2's new moon of Nisan for the arrival and the well's removal, 10:2's tenth of Nisan for her death: the row miriam_death_day with both arms, the tape's marker on the first, the checkpoint recording the nine days.
- ARAD HEARD THAT AARON DIED (Rosh Hashanah 3a:1; Taanit 9a:10; Seder Olam 9:2): "the Canaanite king of Arad heard" — what? that Aaron died and the clouds departed; 20:29's "and all the congregation SAW that Aaron was dead" the proof — the tape's order: Arad's line during the mourning, before the timer's fire; and SEDER OLAM'S RETREAT OF SEVEN STATIONS to Moserah — the reading's Deut 10:6 DIVERGE answered by the shelf: the mourning renewed at the retreat.
- THE SERPENT NEITHER KILLS NOR HEALS (Mishnah Rosh Hashanah 3:8; Rosh Hashanah 29a:7): when Israel looked upward and subjected their hearts they were healed — the answer sheet on 21:8 paired with Moses' hands at Amalek (Exod 17:11); "make YOU" — the serpent Moses' own, so the worshipped object was not an idol by right (Avodah Zarah 44a:7), and Hezekiah broke it with the Sages' agreement (Berakhot 10b:7) — the object row's run to 2 Kgs 18:4 on the shelf.
- AMMON AND MOAB PURIFIED THROUGH SIHON (Chullin 60b:13): "Heshbon was the city of Sihon who had taken all his land from Moab" — the apparently needless verse teaches Israel's title: forbidden Moab's land (Deut 2:9), Israel took it from Sihon who took it from Moab — Rav Pappa's rule; and "from his hand" = from his possession (Bava Metzia 56b) — the parable of 21:27-30 has its legal reading.
- THE STATIONS AS THE TORAH'S LADDER (Nedarim 55a:9; Eruvin 54a; Avot 6:2): Mattanah, Nahaliel, Bamoth, the valley, the wasteland's threshold — Rava's reading of the itinerary as the scholar's rise and fall: the gift-word of Mattanah (18:6-7's) the reading measured is the tradition's own hinge.
- THE ARNON'S MIRACLE FROM "THE BOOK OF THE WARS OF THE LORD" (Berakhot 54a-b): the mountains that met over the Emorites' caves, the blood seen from the well by the two lepers Et and Hev, the song that followed — the reading's unexplained citation (21:14-15) given its narrative on the shelf; Kiddushin 30b reads Vahev as love at the end.
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_chukat_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {sum(1 for k, _, _ in ADDR if k == "LINK")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {sum(1 for k, _, _ in ADDR if k == "TOPIC")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))}; credited {len(CRED)} — the counts the script\'s own Counter measured)\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('WROTE', OUT, len(ADDR), 'rows;', dict(cnt), '; link', dict(cnt_link), '; topic', dict(cnt_topic), '; credited', len(CRED), '; long ranges', len(LONG))
