#!/usr/bin/env python3
# THE NUMBERS WALK 15b — THE COMPILE OF THE REFUGE CITIES (2026-09-13): THE EXAM DOCKET for Numbers 35:1-34, written from the scan's dump
# (scratchpad/ref_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a verse of the
# span; the TOPIC rows = the twenty-two Mishnah rows and the thirteen folio ranges of COMPILE_DEBT's sitting-15 box (k) read WHOLE — the union rule
# of 2026-09-05; the CREDITED marks = addresses already verdicted in an earlier ledger, given their quick look here). Every address in the dump
# gets ONE verdict (parts A..H on disk); the coverage is COMPUTED from the dump, never typed; the ranges' sizes are read from the scan's own print
# (ref_docket_scan.out). Append-only. write_bor_docket.py's form.
import re, os, sys, importlib.util
from collections import Counter
ROOT = '<repo-old>'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{ROOT}/logic/oral_triage/num_35_refuge_cities_exam_2026-09-13.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/ref_docket_dump.txt', encoding='utf-8').read()
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
for p in 'ABCDEFGH':
    part = f'ref_docket_{p}'
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
scan = open(f'{SCR}/ref_docket_scan.out', encoding='utf-8').read()
scan = scan[scan.index('THE RANGES SIZED:'):]
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) segments,\s+(\d+) link rows', scan, re.M)]   # read from the scan's print
assert len(LONG) == 13, len(LONG)
MISH = [a for k, a, _ in ADDR if k == 'TOPIC' and a.startswith('Mishnah')]
assert len(MISH) == 19, len(MISH)   # twenty-two named, three of them (Makkot 2:4, 2:6, 2:7) already LINK rows — the scan's print
assert sum(s - l for _, s, l in LONG) + len(MISH) == NT, (sum(s - l for _, s, l in LONG), len(MISH), NT)   # every range read WHOLE
ncred_link = sum(1 for k, a, _ in ADDR if k == 'LINK' and a in CRED); ncred_topic = sum(1 for k, a, _ in ADDR if k == 'TOPIC' and a in CRED)
verses = Counter(h for k, _, vs in ADDR if k == 'LINK' for h in vs.split())
hdr = (f'# THE EXAM DOCKET — Numbers 35:1-34 (the refuge cities: the Levite cities and their measures, the six cities of refuge, the murderer and the manslayer, the term until the high priest\'s death, the border, the witnesses, the ransom refused, the land polluted by blood and atoned by the shedder\'s, "in whose midst I dwell"), THE NUMBERS WALK sitting 15b, 2026-09-13\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of Numbers 35:1-34 (the scan ref_docket_scan.py: {NL} rows in {len(works)} works; the verses cited most {", ".join(f"{v} {n}" for v, n in verses.most_common(6))}), and (2) THE TOPIC-ROUTED ROWS — the twenty-two Mishnah rows of COMPILE_DEBT\'s sitting-15 box (k) (Makkot 2:1-8, Sanhedrin 1:4, 9:1-2, 3:4, Bava Kamma 4:5, Eruvin 4:3, 5:1-5, Sotah 9:7, Arakhin 9:8, Shevuot 4:1) and the thirteen folio ranges read WHOLE ({"; ".join(f"{n} {s} segments, {l} of them link rows" for n, s, l in LONG)}). Every address ONE verdict: LAW (names the cell of cold_run_refuge.py — F1 the_levite_cities, F2 the_refuge_law, F3 the_murderer, F4 the_manslayer, F5 the_statute — or the callee\'s cell by CALL), DERIVATION (a hook from the verse to a rule), DISPUTE (a parameter row — a DATA row named), CONTEXT, OUTSIDE. CREDITED rows ({len(CRED)} — {ncred_link} link, {ncred_topic} topic) were verdicted in an earlier ledger and get their quick look here (the credit guards of 2026-08-25). Coverage COMPUTED by write_ref_docket.py against the scan\'s dump: {len(ADDR)} addresses, every one verdicted — missing 0, extra 0.\n'
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
- THE SABBATH LIMIT IS THIS CHAPTER'S MEASURE (Eruvin 51a:8; Mishnah Sotah 5:3 / Sotah 27b:8-10; Mishnah Arakhin 9:8): Rav Chisda's chain of verbal analogies runs from "let no man go out of his place" (Exodus 16:29) through the manslayer's flight and border (35:26-27) to "you shall measure from OUTSIDE the city two thousand cubits" (35:5) — the two thousand of the Sabbath are the Levite city's; R. Akiva on his day reconciles 35:4's thousand and 35:5's two thousand as the open land and the Sabbath limit; R. Eliezer son of R. Yosei HaGelili as the open land and the fields and vineyards; the Mishnah in Arakhin as a thousand and a thousand — THREE SETTINGS ON TWO VERSES, the DATA row the_measures.
- THE COURT OF TWENTY-THREE FROM THE CONGREGATION-TOKENS (Mishnah Sanhedrin 1:6; Sanhedrin 2a:14-2b:1; 17a:17): "the congregation shall judge" ten, "the congregation shall deliver" ten (a congregation ten by the spies' ten, 14:27), a majority of two to convict (Exodus 23:2) and one for the odd number — twenty-three: the Sifrei 160:8's "ten and ten and three" in the Mishnah's own arithmetic; and the deliverance verb read three more ways — the court must seek exoneration (Pesachim 12a:2; Rosh Hashanah 26a:2; Sanhedrin 69a:12), a Sanhedrin that saw the killing may not judge it (Makkot 12a:12).
- THE IRON NEEDS NO MEASURE (Sanhedrin 76b:12-13): Shmuel — "in hand" written at the stone and the wood (35:17-18) and not at the iron (35:16) because iron of any size kills; Rebbi's baraita — "revealed and known before Him who spoke and the world came to be that an iron instrument of any size kills, therefore the Torah gave it no measure"; the Gemara — only when he STABBED, a struck blow with iron needs the measure too: the size clause a PARAMETER with the shelf's own exemption and its edge.
- THE DOWNWARD MOTION (Makkot 7b:2; Mishnah Makkot 2:1; 7b:6-16): Shmuel from "and he dropped it on him and he died" (35:23) — exile only for a downward motion; the roller, the barrel, the ladder; the butcher's four baraitot resolved by the stroke's stages; the rung displaced; "and if suddenly" read word by word — the corner, the enemy, the shove, the downward-for-upward, the stone thrown aside: the manslayer's whole table on 35:22-23's tokens.
- THE TERM'S REASON AND ITS THREE PRIESTS (Makkot 11a:12-14; 11b:9-13; Mishnah Makkot 2:6-7; Horayot 3:4): "the death of the high priest" three times (35:25; 35:28 twice) = the anointed, the many-garmented, the relieved (R. Yehuda: the war-anointed from 35:32's bare "the priest"); the high priest's death ATONES because the office bore the generation — they should have pleaded and did not (Rava); the second high priest's death because he should have pleaded for the verdict; the priesthood found void — died or voided (R. Ami / R. Yitzchak Nappacha); the exile's dwelling, death and burial "there" (11b:7); the bones carried (11b:12): the term an EVENT-keyed close, the shelf's rows the DATA.
- THE AVENGER AFTER THE COURT, AND HIS HAND (Makkot 12a:8-11; 10b:7-15; Sanhedrin 45b:11-13): R. Eliezer — "until he stands before the congregation for judgment" (35:12) written against 35:27's avenger: only after conviction (Onkelos' clause at 19 and 21 the same); R. Yosei HaGelili a mitzva / R. Akiva a license outside the border, and any other man; Rav — the avenger who kills before conviction is liable; the court appoints an avenger where there is none ("when he meets him", 45b:13); the murderer and the avenger "two verses that come as one" (45b:12); Rav Huna's avenger on the way exempt (Deuteronomy 19:6 read both ways).
- NO RANSOM, AND WHY THE OX HAS ONE (Ketubot 37b:3-14; Bava Kamma 83b:9-19; 40a:5-12; 41a:2-5; Sanhedrin 15b:4-5): 35:31 refuses money for the murderer's death and 35:32 for the fugitive's exile — one for the intentional, one for the unwitting; R. Yishmael son of R. Yochanan ben Beroka — those executed at HEAVEN'S hand give money and are atoned (the ox's owner, Exodus 21:29-30), those executed by man never ("dedicated of men shall not be redeemed"); and from "no ransom for the LIFE of a murderer" — ransom IS taken for limbs: the talion's money; the stewards pay damages but no ransom (an atonement); the partners' ox's ransom unresolved.
- THE LAND'S ATONEMENT AND THE HEIFER (Arakhin 16a:22; Zevachim 88b:13; Keritot 26a:17; Mishnah Sotah 9:7 / Sotah 47b:2; Ketubot 37b:5-7; Yoma 23a:11-16; Shabbat 33a:4): the killer known — no atonement for the community until he dies (35:33), or where the court cannot execute (no forewarning); the heifer broken and then the killer found — he dies, not by the calf's blood; the beheaded are beheaded FROM THE NECK like the heifer (Deuteronomy 21:9) but not with the cleaver ("love your neighbor as yourself"); the priest stabbed on the ramp and R. Tzadok's "whose heifer?"; bloodshed destroys the Temple and drives the Presence out — 35:33-34 read whole.
- THE INCLUSIO'S TWO READINGS (Shabbat 33a:4; Yoma 85a:14; Shevuot 7b:7; Megillah 29a:4): "in whose midst I dwell" (35:34) — the Presence departs for bloodshed (Shabbat), yet R. Yishmael reads it at the burglar's seat to permit saving a life on the Sabbath (Yoma), bloodshed an impurity the goat does not atone (Shevuot), and R. Shimon ben Yochai's Presence that GOES WITH ISRAEL into every exile and RETURNS with them (Megillah) — the land's Presence against the people's.
- THE RULE ABOUT RULES A THIRD TIME (Makkot 5b:15-16; Bava Kamma 86b:21-22; Sanhedrin 33b:8-9): "we do not punish by inference" — for the lashed by "wicked" / "wicked" (35:31; Deuteronomy 25:2), for the exiled by "murderer" / "murderer" (35:21; 35:11): the Sifrei's rule (157:6, 160:3) at its Talmud seats, the chapter's own two halves joined by its one root.
- THE LEVITE CITIES' OWN SPECIFICATIONS (Makkot 10a:5-8; 10b:16-17; Arakhin 33b:19-24; 13a:2-3; 12b:9): intermediate towns with water, markets and people; no weapons sold, no nets, no ropes; not a city of manslayers, not without elders (Joshua 20:4); Hebron Caleb's suburbs and the priests' city; Kedesh two; walled cities fallen to the Levites by lot; the rent to the Levite landlords disputed on 35:6 and 35:11; a Levite exiled from district to district.
- THE ONE WITNESS FOR ACQUITTAL (Sanhedrin 33b:15; Mishnah Shevuot 4:1; Sanhedrin 27b:9-13; 29a:6): "one witness shall not testify against a person to die" (35:30) — R. Yosei son of R. Yehuda: he may answer to acquit; bar Chama acquitted when one witness fell; the kin and the haters disqualified (Mishnah Sanhedrin 3:4-5) — "not his enemy" testifies, "nor sought his harm" judges (35:23): the Sifrei 160:8's juxtaposition at its Mishnah seats.
- THE APPOINTMENT'S RUN OUTSIDE THE TORAH (Makkot 11a:1-6; 9b:18-19; 10a:14-16): Joshua 20:1-2's harsh speech — the cities a Torah mitzva, or Joshua delayed; "Joshua wrote these words in the book of the Torah of God" — the refuge portion of Joshua as Torah-written (R. Nechemya); the six as two rows of vines; Reuben first for Joseph's rescue; Moses' three that could not receive until Joshua's — "a mitzva that came my way": THE DEBIT OPEN BY DESIGN read on the shelf.
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_ref_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {NL}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {NT}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))}; credited {len(CRED)} — the counts this script computed from the dump and the verdict lists, never typed).\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('WROTE', OUT, len(ADDR), 'rows;', dict(cnt), '; link', dict(cnt_link), '; topic', dict(cnt_topic), '; credited', len(CRED), '; long ranges', len(LONG))
