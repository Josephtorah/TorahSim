#!/usr/bin/env python3
# THE NUMBERS WALK 11b — THE COMPILE OF MIDIAN (2026-09-12): THE EXAM DOCKET for Numbers 31:1-54, written from the scan's dump
# (scratchpad/midian_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a verse of the
# span; the TOPIC rows = Mishnah Avodah Zarah chapter 5 WHOLE, the single mishnayot (Kelim 11:1, 15:1; Oholot 1:2-3; Terumot 4:3), the Jerusalem
# Talmud Terumot 4:3's halakhah and the seventeen folio ranges of the reading ledger's TESTING SHELF line read WHOLE — the union rule of
# 2026-09-05; the CREDITED marks = addresses already verdicted in an earlier ledger, given their quick look here). Every address in the dump gets
# ONE verdict (parts A..G); the coverage is COMPUTED from the dump, never typed; the ranges' sizes are read from the scan's own print
# (midian_docket_scan.out). Append-only. write_vows_docket.py's form.
import re, os, sys, importlib.util
from collections import Counter
ROOT = '<repo-old>'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{ROOT}/logic/oral_triage/num_31_midian_exam_2026-09-12.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/midian_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR, CRED = [], {}
for k, a, rest in rows:
    m = re.search(r'\{CREDITED: (.*?)\}', rest)
    if m: CRED[a.strip()] = m.group(1)
    ADDR.append((k, a.strip(), re.sub(r'\s*\{CREDITED:.*?\}', '', rest).strip()))
NL = sum(1 for k, _, _ in ADDR if k == 'LINK'); NT = len(ADDR) - NL
assert len(ADDR) == 451 and NL == 40 and len(CRED) == 106, (len(ADDR), NL, len(CRED))
V = {}
for p in 'ABCDEFG':
    part = f'midian_docket_{p}'
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
assert len(works) == 19, len(works)
scan = open(f'{SCR}/midian_docket_scan.out', encoding='utf-8').read()
scan = scan[scan.index('THE RANGES SIZED:'):]
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) segments,\s+(\d+) link rows', scan, re.M)]   # read from the scan's print
assert len(LONG) == 17, len(LONG)
MISH = [a for k, a, _ in ADDR if k == 'TOPIC' and a.startswith('Mishnah')]
JT = [a for k, a, _ in ADDR if k == 'TOPIC' and a.startswith('Jerusalem Talmud')]
assert sum(s - l for _, s, l in LONG) + len(MISH) + len(JT) == NT, (sum(s - l for _, s, l in LONG), len(MISH), len(JT), NT)   # every range read WHOLE: the topic rows = the ranges' non-link segments + the Mishnah rows + the Jerusalem Talmud's segments
ncred_link = sum(1 for k, a, _ in ADDR if k == 'LINK' and a in CRED); ncred_topic = sum(1 for k, a, _ in ADDR if k == 'TOPIC' and a in CRED)
hdr = (f'# THE EXAM DOCKET — Numbers 31:1-54 (Midian: the vengeance and the muster, the war and the kings and Balaam, the captives and the spoil, Moses\' wrath and the sentence, the purification of the warriors, Eleazar\'s statute of the vessels, the division of the prey with the tribute and the Levites\' share, the officers\' gold), THE NUMBERS WALK sitting 11b, the compile (2026-09-12; the owner: "Go" after the #145 rereads, on 1b\'s order — the measurements, the design, the probes, the docket, the types, the runner; the design World/step9/NUMBERS_WALK.md "Sitting 11b").\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of Numbers 31:1-54 (the scan by script over Data/sefaria_export, commentaries excluded: {NL} rows in {len(works)} works — ' + ', '.join(f'{w} {n}' for w, n in works.most_common()) + f'), and (2) THE TOPIC-ROUTED ROWS — Mishnah Avodah Zarah chapter 5 WHOLE (5:12 the vessels of Midian; {len(MISH)} mishnayot in all with Kelim 11:1 and 15:1, Oholot 1:2-3 and Terumot 4:3 beyond the links), the Jerusalem Talmud Terumot 4:3\'s halakhah ({len(JT)} segments — "one of fifty" at Num 31:30) and the seventeen folio ranges of the reading ledger\'s TESTING SHELF line (logic/oral_triage/num_31_midian_2026-09-12.md) and COMPILE_DEBT\'s sitting-11 box, read WHOLE with the link rows dropped: ' + '; '.join(f'{r} {s} segments ({l} link rows)' for r, s, l in LONG) + f' — {NT} topic rows. {len(CRED)} addresses already verdicted in earlier ledgers are marked CREDITED with their ledger and given a QUICK LOOK here (speed ruling (b), credit guard (1)) — {ncred_link} link rows, {ncred_topic} topic rows. Every address gets ONE verdict: LAW (a rule the runner must reproduce — the cell named: F1 the_vengeance, F2 the_war, F3 the_sentence, F4 the_purification, F5 the_vessels, F6 the_division, F7 the_gold, or the callee\'s cell by CALL), DERIVATION (a hook from the verse to a rule — a labeled move), DISPUTE (a parameter row — a DATA row named), CONTEXT, OUTSIDE (the shelf\'s colophon and rows outside the span\'s question). Terse for the non-material (speed ruling (c)).\n'
       f'# THE TALMUD ADDRESSING: the export\'s index 0 is folio 1a (a page = index // 2 + 1; measured 2026-09-09); the Mishnah by chapter:mishnah; the Jerusalem Talmud by chapter:halakhah:segment.\n')
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
- THE KASHERING RULE'S WHOLE SUGYA AT THE VESSELS OF MIDIAN: Rava reads IMMERSION out of "and it shall be pure" (31:23) — every purged and whitened vessel immersed in forty se'ah (Avodah Zarah 75b:7); Bar Kappara reads "NEVERTHELESS" as the particle that EXCLUDES the third and seventh day's sprinkling, and "the water of niddah" as the water a menstruant immerses in, not the heifer's (75b:8-11) — the reading's four-seat phrase split by the shelf; the immersion's scope the passage's own: METAL utensils (75b:14), PURCHASED as the captured were, not borrowed (75b:13), even new (75b:12), glass as metal and the glazed by its final state (75b:15); THE BARAITA'S TABLE BY USE — unused, cold, hot, fire, immersion on every row (75b:17) beside the Mishnah's whiten / boil / immerse / polish (5:12 = 75b:6); the Torah's own rule only a pot used THAT DAY (75b:21-76a:1; Pesachim 44b:15); the spit whitened against the sacrificial spit purged — Rav Sheshet's forbidden-absorbed against permitted-turned-forbidden (76a:4-16); the measures — until the outer layer sheds, a kettle in a kettle (76a:17); AS IT ABSORBS SO IT EMITS (76b:1; Pesachim 30b:6); the knife polished and thrust ten times (76b:2), white-hot for Passover (Pesachim 30b:5); earthenware never purged — "the Torah testified" (Pesachim 30b:8): the ink's fire / water at 31:23 is the trunk, the Mishnah's four modes its branches by use — the DATA rows kashering_modes and immersion_source.
- THE TASTE AS THE SUBSTANCE, AND THE NOVELTY: R. Akiva derives the principle from the vessels of Midian — mere absorbed taste, and the vessels forbidden until purged (Nazir 37b:1; Pesachim 44b:13); THE RABBIS REFUSE THE DERIVATION — the purging of gentiles' vessels is itself a NOVELTY, forbidding a taste that taints (Pesachim 44b:14, 44b:16); R. Meir's detriment principle grounded on the same verses (Avodah Zarah 67b:6): the chapter's statute is the tradition's laboratory for one of its widest rules.
- THE TWO LISTS ARE A TAUGHT TRANSFER: the verbal analogy "garment and leather" between Leviticus 11:32 and Numbers 31:20 (Shabbat 64a:7-8, 64a:15; Bava Kamma 25b:6) — the spun and woven from the sack (64a:3), the goat-work's reach to reins, tails, horns and hooves and not to birds' bones (64a:4, 64a:9; Chullin 25b:4), the analogy run BOTH WAYS (64a:8 — the Sifrei 157:8's two-way identity at its Talmud seat) and its FREE-WORD condition argued (64a:16-19): the edge midian → shemini carries `link: transfer` with these teachers, the Sifrei's freed word the exposition's ground.
- THE SWORD LIKE THE SLAIN AT THREE SEATS: the metal sword takes the corpse's grade (Nazir 53b:11; Pesachim 14b:1, 14b:5 — metal the one substance where the corpse's and the creeping animal's impurity differ; Chullin 3a:1 the knife); the SEVEN DAYS a Torah floor for what a corpse defiles, from 31:24's "wash your garments on the seventh day" (Bava Kamma 25b:13); the vessel's toucher until evening (Nazir 54b:6; Oholot 1:2-3): CK's sword_like_slain row READ, the warriors' metal and the six metals its seat.
- THE GENTILE'S CORPSE AND THE MIDIAN WAR: no tent (Yevamot 61a:1) but touch and carrying — the war's purification the proof even for R. Shimon ben Yochai (61a:5); "NOT ONE MAN OF US IS MISSING" read by the Rabbis as the casualty count (no Jew fell — the corpses gentile) and by R. Shimon as a moral count (61a:4): the F7 count and the F4 purification meet on one verse.
- THE SENTENCE'S CASE KINDS RUN BY AGE: "every woman that has known man" = FIT FOR INTERCOURSE, the line at three years (Yevamot 60b:9-10 — Rav Huna's contradiction resolved); THE FRONTPLATE TEST — the girls passed before it, the sallow face (60b:11); Jabesh-gilead's four hundred by the barrel of wine, the frontplate "for acceptance, not calamity" for Israel (60b:12-13 — the RUN_CITATION Judges 21 at its seat); the convert under three fit for the priesthood — R. Shimon ben Yochai from 31:18 with Phinehas present (60b:6; Kiddushin 78a:19), THE HALAKHA as him (60b:14) against the Rabbis' "as slaves and maidservants" (60b:7), the reason "virgins of the seed of the house of Israel" — a hymen formed as a Jew (Kiddushin 78a:21): the DATA rows known_a_man_test, frontplate_test, proselyte_age.
- WE DO NOT PUNISH BY INFERENCE — THE RULE ABOUT RULES AT ITS SEATS: the baraita on the sister of both parents (Makkot 5b:11-12), no prohibition by inference either (5b:14), not lashes (5b:15), not exile (5b:16); the Abaye / Rava fork on the father's brother (Sanhedrin 54a:17): the Sifrei 157:6's reading of 31:17's doubled "kill" carried as the DATA row punish_by_inference with the shelf's two arms; MIDDOT's case law.
- ANGER BEGETS ERROR: Moses' wrath (31:14) and the statute in Eleazar's mouth (31:21) — the law hidden from Moses by his anger (Pesachim 66b:7); the prophet's prophecy (Elisha, 66b:8), Eliab lowered (66b:9), the haughty (66b:6); ELEAZAR LOWERED FOR RULING BEFORE HIS TEACHER — "commanded to my father's brother, not to me" (Eruvin 63a:24): the priest's relay read by the shelf as a fault, the installed_by class's own witness; "WHOEVER REPORTS A SAYING IN THE NAME OF ITS SAYER" (Megillah 15a:20) — the Sifrei 157:9's closing rule at its seat, the export's dropped attribution the reading's finding.
- THE RATES ON THE SHELF: the Midian teruma NOT one of ten and NOT for all generations — refused as a source (Menachot 77b:20 — the division's rates a one-time instruction, the daemon's class witnessed); one in five hundred asked as a measure for the ash removal (Yoma 24a:5); THE LEVITES' FIFTIETH IS THE TERUMAH'S AVERAGE — R. Levi: "from the half of the children of Israel take one part in fifty" (Num 31:30), "all you take elsewhere shall be like this" (Jerusalem Talmud Terumot 4:3:2; Mishnah Terumot 4:3's one fiftieth) — a transfer taught, the reading's "one of fifty" on the local shelf after all; the Torah's own measure of terumah NONE (4:3:8): the parser's Fraction(1, 50) the shelf's number.
- THE OFFICERS' GOLD: "the LORD's offering" is not "an offering TO the LORD" — the gold to the tent, never the altar (Temurah 13a:14; 6b:15, 13a:11); the ATONEMENT for the eyes' thoughts of transgression — Moses' exchange with the officers on "not one of us is missing" (Shabbat 64a:22, 64a:23-64b:2; the school of R. Yishmael) beside the ink's ransom-words (Exodus 30:15-16 — the DATA row atonement_reading with both arms); the five ornaments named — agil the breast-mold, kumaz the womb-mold, its Aramaic "what leads to folly" (64a:20-21; Berakhot 24a:15); the ornaments as VESSELS for impurity — "all vessels with which labor is done" (31:51 — Shabbat 60a:3, 63b:6, 63b:19).
- 31:6 WORD BY WORD: "them" the Sanhedrin, Phinehas THE PRIEST ANOINTED FOR WAR, the holy vessels the ark and the tablets, the trumpets the shofarot (Sotah 43a:1); PHINEHAS THE AVENGER OF JOSEPH — "the Midianites sold him" (Genesis 37:36) and "the daughters of Putiel" — Joseph AND Jethro, both (43a:2-3): the Sifrei 157:4's proof text and the export's inserted Jethro answered by the shelf itself (the DATA row phinehas_lineage); the priest anointed for war's speech on Deuteronomy 20 (43a:9 — the forward span's).
- BALAAM'S DEATH ON THE SHELF: to collect his fee for the twenty-four thousand (Sanhedrin 106a:16); ALL FOUR COURT MODES in him (106b:1 — BK's row's two settings); thirty-three years old "when Phinehas the highwayman killed him" — the heretic's notebook (106b:2, the hand the ink never names); the counsel in Egypt his second cause (106a:4; Sotah 11a:13); "let me die the death of the righteous" his own sign (105a:12); Joshua 13:22's "diviner" — first a prophet (106a:17); MIDIAN JOINED MOAB — the two dogs and the wolf (105a:13), the elders of Midian left (105a:14); MOAB SPARED — Moses' own a-fortiori from "harass the Midianites" refused by Deuteronomy 2:9 (Bava Kamma 38a:16): the Balak runner's cells by CALL, every one.
- THE INK'S WORDS ON THE SHELF'S PAGES: "the half [mechetzat] of the congregation" (31:43) read for the mishna's partition (Bava Batra 2b:3, 3a:2); "nefesh adam" — the captives distinguished from the beasts (31:40 — Keritot 6b:21; Yevamot 61a:2); "arm [hechaletzu]" as removal from one's place (31:3 — Yevamot 102b:9); "afterward you shall be gathered" (31:2) among the scribes' ornamentations (Nedarim 37b:8); "every thing" — even a sounding vessel (31:23 — Shabbat 58b:5, 63b:11); "immersion in fire" (Sanhedrin 39a:15).
- THE SHELF'S OWN GAPS: the tractate's colophon a segment (Avodah Zarah 76b:5 — OUTSIDE); the Jerusalem Talmud recension's scribal confusions of thirty / fifty / sixty read as the shelf's own, not adjudicated (4:3:3).
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_midian_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {NL}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {NT}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))}; credited {len(CRED)} — the counts this script computed from the dump and the verdict lists, never typed)\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('WROTE', OUT, len(ADDR), 'rows;', dict(cnt), '; link', dict(cnt_link), '; topic', dict(cnt_topic), '; credited', len(CRED), '; long ranges', len(LONG), '; mishnah topic rows', len(MISH), '; jt rows', len(JT))
