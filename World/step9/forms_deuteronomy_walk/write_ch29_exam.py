import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27): THE LEAN EXAM FILE — the Mishnah rows the reading's ledger cites (EVERY distinct citation — three rows: Sotah 7:8, Berakhot 9:2,
# Avot 1:6) and the Tosefta's rows the translator's parallels name (Tosefta Sotah 11:2, 11:3, 11:4 and Ketubot 5:8 — the cited 11:7 read whole and EXCLUDED as a case: not
# the parallel), read WHOLE from the export (Hebrew and English) at the design, each a case of a cell with its verdict a PARAMETER or a DATA row; NO Talmud segment read
# (the folios the rows name OWED to the docket, listed); coverage COMPUTED from the export's rows, never recited; the citing rows of the ledger COMPUTED per row; the
# Hebrew opening CUT from the export's own bytes (the first four words), its English typed beside it; the row's Hebrew whole stays in the prints, the English whole here (the lint: a Hebrew run is glossed within ninety characters). ls done before the write. write_ch26_exam.py's form over three chapters.
# RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
import json, os, re, html, subprocess, collections, sys
ROOT = _ROOT
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ch29b_spec as S
OUT = ROOT + '/logic/oral_triage/deu_29_31_nitzavim_vayelech_exam_2026-09-27.md'
assert not os.path.exists(OUT) or os.environ.get('DEU_REWRITE') == '1', OUT
LED = open(ROOT + '/logic/oral_triage/deu_29_31_nitzavim_vayelech_2026-09-27.md', encoding='utf-8').read()
def clean(s): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', html.unescape(s))).strip()
GLOSS = [('Sukkot', 'Sukkot (the feast of booths)'), ('Torah scroll', 'Torah (the law) scroll'), ('Torah', 'Torah (the law)'), ('Sabbatical Year', 'Sabbatical Year (the release year)'), ('Yom Kippur', 'Yom Kippur (the Day of Atonement)'), ('Adar', 'Adar (the twelfth month)'), ('Nissan', 'Nissan (the first month)'), ('Iyar', 'Iyar (the second month)'), ('Omer', 'Omer (the barley sheaf)'), ('Gilgal', 'Gilgal (the first camp in the land)'), ('matzah', 'matzah (unleavened bread)'), ('Hakhamim', 'Hakhamim (the sages)'), ('yevam', 'yevam (the levirate brother)'), ('levir', 'levir (the dead brother\'s brother)'), ('dinars', 'dinars (gold coins)'), ('Akko', 'Akko (the northern port)'), ('Rambam', 'Rambam (Maimonides)'), ('Gemara', 'Gemara (the Talmud\'s discussion)'), ('zikin and zeva’ot', 'zikin and zeva’ot (comets and earthquakes)'), ('Agrippa', 'Agrippa (the king)')]
def gloss(en):
    en = en.replace('(עד בואם)', 'עד בואם "until they came"')   # the translation's bare Hebrew in parentheses glossed in place (the lint's lesson)
    for a, b in GLOSS:
        if a in en and b not in en: en = en.replace(a, b, 1)
    return en
def folder(tr): return f'{ROOT}/Data/sefaria_export/' + (('Tosefta_' + tr[8:].replace(' ', '_')) if tr.startswith('Tosefta ') else ('Pirkei_Avot' if tr == 'Avot' else 'Mishnah_' + tr.replace(' ', '_')))
def row(tr, c, p):
    d = folder(tr); he = json.load(open(f'{d}/he.json', encoding='utf-8')); en = json.load(open(f'{d}/en.json', encoding='utf-8'))
    g = lambda x: (x['text'] if isinstance(x, dict) and 'text' in x else x)
    return clean(g(he)[c - 1][p - 1]), gloss(clean(g(en)[c - 1][p - 1]))
TR = r'(Tosefta Sotah|Tosefta Ketubot|Makkot|Sotah|Sanhedrin|Bava Batra|Bekhorot|Yevamot|Kiddushin|Shevuot|Chullin|Zevachim|Sukkah|Berakhot|Pesachim|Menachot|Temurah|Arakhin|Bava Metzia|Peah|Ketubot|Gittin|Shabbat|Eruvin|Yoma|Rosh Hashanah|Megillah|Chagigah|Eduyot|Bikkurim|Terumot|Maaser Sheni|Avot|Shekalim)'
cites = collections.Counter(re.findall(TR + r' (\d+):(\d+)\b', LED))
ALL = sorted([(t, int(c), int(p)) for (t, c, p), n in cites.items()])
CITED_TOSEFTA = [(t, c, p) for t, c, p in ALL if t.startswith('Tosefta')]
assert set(t for t in ALL if not t[0].startswith('Tosefta')) == set(S.MISHNAH), (ALL, S.MISHNAH)
assert set(CITED_TOSEFTA) <= set(S.TOSEFTA), (CITED_TOSEFTA, S.TOSEFTA)
CHONLY = sorted(set(re.findall(TR + r' (\d+)(?![:\d])', LED)))
def where(tr, c, p):
    ids = []
    for line in LED.split('\n'):
        if re.search(r'\b%s %d:%d\b' % (re.escape(tr), c, p), line) or (tr.startswith('Tosefta') and re.search(r'\b%s %d\b(?!:)' % (re.escape(tr), c), line)):
            g = re.match(r'- (Sifrei Devarim \d+:\d+|Onkelos Deut \d+:\d+)', line)
            ids.append(g.group(1).replace('Sifrei Devarim ', '') if g else (line[:40] + '…'))
    return ids
def cut4(he):
    w = re.sub(r'[\.,:;!?"()׳״–\-\[\]]', ' ', he).split(); return ' '.join(w[:4])
ROWS = [
 ('Sotah', 7, 8, '31:10-13', "F11 the_law_written_and_the_hakhel — THE KING'S READING: the night after the first festival day of booths in the eighth year at the end of the seventh (the_hakhel_time — THE CALENDAR PARAMETER), the wooden platform in the court (the_hakhels_place), the scroll from the attendant to the head to the deputy to the high priest to the king (the_hakhels_reader), Agrippas standing and weeping at 17:15 with Israel's 'you are our brother' (157:10's Sifrei row — the Mishnah NAMED IN THE HEBREW ROW), the portions from 1:1 to the Shema, the Shema, 'if you hearken', 'you shall tithe', 'when you have finished tithing', the king's portion, the blessings and the curses (the_hakhels_portions — every one A LINE ON THE TAPE: the hakhel reads the tape), the eight blessings with the festivals' for the forgiveness of iniquity (the_hakhels_blessings)", 'how is the portion of the king read'),
 ('Berakhot', 9, 2, '31:14', "F12 the_tent_and_the_commission — THE BLESSING ON BAD TIDINGS: 'blessed be the true Judge' (304:1's R. Shimon ben Yochai at 'your days approach to die' — the death announced blessed as the Judge's verdict); rain and good tidings 'who is good and does good'; R. Judah's great sea both arms on the line (the_blessing_on_bad_tidings a PARAMETER)", 'on comets and on earthquakes and on lightning'),
 ('Avot', 1, 6, '31:14', "F12 the_tent_and_the_commission — ACQUIRE A COMPANION: Joshua ben Perachya's three — a teacher, a companion, the scale of merit; 305:1's 'a companion is acquired only with great difficulty' the Sifrei's use (the_companion a DATA row; the_interpreter the parameter — Joshua to teach in Moses' lifetime)", 'Joshua ben Perachya and Nittai the Arbelite received from them'),
 ('Tosefta Sotah', 11, 3, '31:2', "F10 the_charge_and_the_crossing — THE SEVENTH OF ADAR: 'this day' teaches the years completed to the day; the death date computed BACKWARD from Joshua 4:19's tenth of Nisan through the thirty days (34:8) and the three days (Joshua 1:11) — the_death_date_of_moses THE CALENDAR PARAMETER and THE MARKER'S DAY (40, 12, 7); 2:3's Sifrei row the reading's; 'the number of your days I will complete' (Exodus 23:26) the row's own proof", 'and from where that on the seventh of Adar Moses was born'),
 ('Tosefta Sotah', 11, 4, '31:15', "F12 the_tent_and_the_commission — THE THREE GIFTS AND THEIR THREE MERITS: the well by Miriam, the pillar of cloud by Aaron, the manna by Moses; Miriam died — the well ceased and returned by Moses' and Aaron's merit; Aaron died — the cloud ceased and returned by Moses' merit; Moses died — all three ceased (305:4's row; the_three_gifts_and_their_merits a PARAMETER — the daemon shape owed to the death's sitting: the cloud stands at the door at 31:15, its last standing); the hornet stopped at the Jordan", 'R. Yosei son of R. Judah says: when Israel went out of Egypt'),
 ('Tosefta Sotah', 11, 2, '31:15', "F12 the_tent_and_the_commission — THE MANNA AFTER MOSES' DEATH: the manna gathered on the day Moses died eaten until the sixteenth of Nisan, thirty-nine days, until the omer at Gilgal (Joshua 5:12); the forty years counted with the cakes brought from Egypt (Exodus 16:35); R. Elazar ben Azariah's parable of the hot and the cold water — a DATA row beside the three gifts (the manna the tape's line by CALL)", 'as long as Moses was alive the manna came down'),
 ('Tosefta Ketubot', 5, 8, '31:14-23', "F13 the_apostasy_foretold — NAKDIMON'S DAUGHTER gathering barley beneath the horses' hooves at Akko, five hundred gold dinars a day her perfume fund while she waited for the levir (305:3's story on the Sifrei's row — Rabban Yochanan ben Zakkai's; the Tosefta's R. Elazar bar Tzadok): THE CONDITIONAL RULE OF THE NATIONS — when Israel does His will no nation rules them, when not He hands them to a lowly nation — a DATA row the_subjection_condition (28:43-48's arm by CALL; 305:3 CONTEXT at the reading)", 'the surplus of food is his and the surplus of worn clothes is hers'),
]
EXCL = [('Tosefta Sotah', 11, 7, "cited by 2:3's row as the parallel for Moses' hundred and twenty to the day — READ WHOLE (Rachel's tomb at Zelzah, Saul at Gibeah and Ramah, the feet in Jerusalem's gates, Geba to Rimmon) and found NOT THE PARALLEL: the translator's paragraph number differs from the export's — 11:3 the true parallel, read and taken as the case above; EXCLUDED as a case", 'similarly you say: when you go from me today')]
assert set((t, c, p) for t, c, p, *_ in ROWS) | set((t, c, p) for t, c, p, *_ in EXCL) == set(S.MISHNAH) | set(S.TOSEFTA), 'the rows and the spec disagree'
WHERE = {(t, c, p): where(t, c, p) for t, c, p, *_ in ROWS + EXCL}
body = []; tot = 0
for t, c, p, verses, note, en_open in ROWS:
    he, en = row(t, c, p); tot += len(he) + len(en); heb4 = cut4(he)
    body.append(f'- {"Mishnah " if not t.startswith("Tosefta") else ""}{t} {c}:{p} — LAW. On {verses}. {heb4} "{en_open}" — {note}. THE ROW WHOLE IN ENGLISH ({len(he)} Hebrew characters read whole at the design, the print ch29_exam_rows.out and its neighbours\' print holding them): {en} — cited by the ledger\'s rows: {WHERE[(t, c, p)] or ["(the tractate named without the paragraph — the parallel located at the design)"]}. Read whole at the design.')
for t, c, p, note, en_open in EXCL:
    he, en = row(t, c, p); tot += len(he) + len(en); heb4 = cut4(he)
    body.append(f'- {t} {c}:{p} — EXCLUDED. {heb4} "{en_open}" — {note}. THE ROW WHOLE IN ENGLISH ({len(he)} Hebrew characters read whole at the design): {en} — cited by the ledger\'s rows: {WHERE[(t, c, p)]}. Read whole at the design.')
NR = len(ROWS); NX = len(EXCL)
head = (f'# THE LEAN EXAM — Deuteronomy 29:1-31:30 (the covenant in Moab and its oath with those not here, the individual\'s curse and the land\'s desolation, the hidden and the revealed; the return and the gathering, the heart circumcised, the commandment near, life and death; the charge and the crossing, the law written and THE HAKHEL — the king\'s reading at the release year\'s booths, the Tent and the commission, the apostasy foretold, the song as a witness, the book beside the ark) — THE DEUTERONOMY WALK sitting 19b, THE LEAN PASS (2026-09-27; DEUTERONOMY_WALK.md "Sitting 19b — THE COMPILE OF CHAPTERS 29-31 … LEAN" THE FORM)\n'
        f'# DECLARED (THE LEAN PASS, owner-ruled 2026-09-23 — DEUTERONOMY_WALK.md "THE LEAN PASS"; the state doc\'s #208): NO DOCKET at this sitting — the testing shelf\'s cases are THE MISHNAH ROWS THE READING\'S LEDGER CITES (logic/oral_triage/deu_29_31_nitzavim_vayelech_2026-09-27.md — the rows\' citations counted by the regex: {len(ALL)} distinct citations with a paragraph ({len(S.MISHNAH)} Mishnah rows — Sotah 7:8 CITED IN THE SPINE\'S OWN HEBREW at 157:10 by its marker, Berakhot 9:2 and Avot 1:6 the translator\'s parallels at 304:1 and 305:1 — and {len(CITED_TOSEFTA)} Tosefta paragraph cited: {CITED_TOSEFTA}) AND THE TOSEFTA\'S ROWS THE PARALLELS NAME BY CHAPTER ({CHONLY} the chapter-only citations — Tosefta Sotah 11 and Ketubot 5 the Tosefta\'s, the rest Talmud folios OWED): {NR} rows read WHOLE from the export (Data/sefaria_export/Mishnah_<tractate>, Pirkei_Avot, Tosefta_<tractate> — he.json and en.json, chapter:paragraph), Hebrew and English, at the design (the whole-row rule, owner-ruled 2026-09-17; ch29_exam_rows.py printed the cited four whole, the Tosefta\'s neighbours located and printed whole beside them), each a case of a cell of cold_run_{S.RUNNER}.py with its verdict a PARAMETER or a DATA row (the code/data separation law: the Mishnah\'s rows and the Tosefta\'s never in the source); {NX} row read whole and EXCLUDED as a case (Tosefta Sotah 11:7 — the cited paragraph is not the parallel the translator meant; the export\'s 11:3 is); THE TALMUD FOLIOS THE ROWS NAME ({"; ".join(S.TALMUD_OWED)}) OWED to the docket, none read; NO Talmud segment read. THE DOCKET WHOLE OWED (COMPILE_DEBT\'s lean-pass box).\n'
        f'# COVERAGE (computed from the export\'s rows): **read: {NR + NX} of {NR + NX} — COMPLETE** ({NR} cases, {NX} excluded; {tot} characters read whole).\n\n')
text = head + '\n'.join(body) + '\n'
os.makedirs(os.path.dirname(OUT), exist_ok=True)
assert os.path.expanduser('~') not in text
open(OUT, 'w', encoding='utf-8').write(text)
lint = subprocess.run([sys.executable, ROOT + '/logic/solo_tools/gloss_lint.py', OUT], capture_output=True, text=True)
print(f'THE LEAN EXAM WRITTEN: {OUT} — {len(text.encode())} bytes; {NR} rows + {NX} excluded; {tot} characters read whole; the distinct citations {ALL}; chapter-only {CHONLY}; lint: {(lint.stdout + lint.stderr).strip().split(chr(10))[-1]}')
if lint.returncode: print((lint.stdout + lint.stderr).strip()[-1500:])
