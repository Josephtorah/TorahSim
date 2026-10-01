import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22b (2026-09-30): THE LEAN EXAM FILE — the Mishnah rows the reading's ledger cites (every distinct citation with a paragraph, computed by the citation regex;
# Avot from the export's folder Pirkei_Avot) and the Tosefta's one row the reading read whole (Tosefta Sotah 4:4), each read WHOLE from the export (Hebrew and English), each a case
# of a cell with its verdict a PARAMETER or a DATA row; the ONE row the regex misread EXCLUDED (the Mishnah's Sotah 4:4 read for the Tosefta's — read whole and excluded); the four
# folios the ledger names OWED (Bava Batra 15a, Menachot 30a, Shabbat 87a, Sotah 13b — cited never read); coverage COMPUTED from the export's rows; the Hebrew opening CUT from the
# export's own bytes (the first four words), its English beside it. ls done before the write (the file asserted absent). write_ch33_exam.py's form, lean. RUN FROM THE REPO ROOT.
import json, os, re, html, subprocess, collections, sys
ROOT = _ROOT
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ch34b_spec as S
OUT = ROOT + '/logic/oral_triage/deu_34_moses_death_exam_2026-09-30.md'
assert not os.path.exists(OUT) or os.environ.get('DEU_REWRITE') == '1', OUT
LED = open(ROOT + '/logic/oral_triage/deu_34_moses_death_2026-09-30.md', encoding='utf-8').read()
def clean(s): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', html.unescape(s))).strip()
GLOSS = [('Torah', 'Torah (the law)'), ('Shema', 'Shema (the creed\'s recitation)'), ('halakhot', 'halakhot (the laws)'), ('halakha', 'halakha (the law)'), ('mitzvot', 'mitzvot (the commandments)'), ('mitzva', 'mitzva (a commandment)'), ('Shechinah', 'Shechinah (the Presence)'), ('Shekhinah', 'Shekhinah (the Presence)'),
         ('epikoros', 'epikoros (a scoffer)'), ('Gemara', 'Gemara (the Talmud\'s discussion)'), ('mishna', 'mishna (the row)'), ('Sanhedrin', 'Sanhedrin (the high court)'), ('nazirite', 'nazirite (the vowed abstainer)'), ('naziriteship', 'naziriteship (the vow\'s term)'), ('nazir', 'nazir (the vowed abstainer)'), ('mil', 'mil (a Roman mile)'), ('Eretz Yisrael', 'Eretz Yisrael (the land of Israel)'), ('Eretz Israel', 'Eretz Israel (the land of Israel)'),
         ('sotah', 'sotah (the suspected wife)'), ('Sotah', 'Sotah (the suspected wife)'), ('Yavne', 'Yavne (the sages\' seat after the Temple)'), ('Sheol', 'Sheol (the grave)'), ('Gehenna', 'Gehenna (the place of punishment)'), ('Gehinnom', 'Gehinnom (the place of punishment)'), ('Kohen', 'Kohen (a priest)'), ('korban', 'korban (an offering)'), ('kohanim', 'kohanim (the priests)')]
def gloss(en):
    for a, b in GLOSS:
        if re.search(r'\b' + re.escape(a) + r'\b', en) and b not in en: en = re.sub(r'\b' + re.escape(a) + r'\b', b, en, count=1)
    return en
def folder(tr): return f'{ROOT}/Data/sefaria_export/' + (('Tosefta_' + tr[8:].replace(' ', '_')) if tr.startswith('Tosefta ') else ('Pirkei_Avot' if tr == 'Avot' else 'Mishnah_' + tr.replace(' ', '_')))
def row(tr, c, p):
    d = folder(tr); he = json.load(open(f'{d}/he.json', encoding='utf-8')); en = json.load(open(f'{d}/en.json', encoding='utf-8'))
    g = lambda x: (x['text'] if isinstance(x, dict) and 'text' in x else x)
    return clean(g(he)[c - 1][p - 1]), clean(g(en)[c - 1][p - 1])
TR = r'(Tosefta Sotah|Sotah|Sanhedrin|Nazir|Avot|Bava Batra|Menachot|Shabbat|Kiddushin)'
cites = collections.Counter(re.findall(TR + r' (\d+):(\d+)\b', LED))
DIST = sorted((t, int(c), int(p)) for (t, c, p) in cites)
assert set(DIST) == set(S.MISHNAH) | set(S.TOSEFTA) | set(S.MISHNAH_EXCLUDED), (DIST, S.MISHNAH, S.TOSEFTA, S.MISHNAH_EXCLUDED)
CASE = {('Avot', 1, 1): ("THE PARAMETER the_chain_of_transmission — 'Moses received the Torah from Sinai and handed it to Joshua': Onkelos 34:9 'and the children of Israel RECEIVED from him' the translator's own verb for 'hearkened'; F5 the_children_of_israel_hearkened_to_him_and_did_as_the_lord_commanded_moses", 'F5'),
        ('Nazir', 1, 3): ("THE PARAMETER the_nazirites_term — an unspecified naziriteship is thirty days: 357:37 reads it from 34:8's 'days' by the verbal analogy with Numbers 6:4's 'the days' (I2); naso's DATA nazir_default_days (30) the callee's row by CALL — the last chapter supplies a datum to the sixth of Numbers; F4 the_children_of_israel_wept_for_moses_in_the_plains_of_moab_thirty_days", 'F4'),
        ('Sanhedrin', 10, 1): ("THE PARAMETER the_world_to_come_share — all Israel has a share in the world to come; 357:18's 'the hinder sea' read 'the last day' (the world to its end and the resurrection) and 357:41's face shown at death — the dead see; F1 the_lord_showed_him_all_the_land_gilead_to_dan_naphtali_ephraim_and_manasseh_judah_to_the_hinder_sea, F6 there_arose_not_a_prophet_since_in_israel_like_moses_whom_the_lord_knew_face_to_face", 'F1'),
        ('Sotah', 1, 7): ("THE PARAMETER measure_for_measure — with the measure a man measures it is measured to him: the Tosefta's row (4:4) opens on it — Moses merited Joseph's bones, the Place attended Moses; F3 he_buried_him_in_the_valley_in_the_land_of_moab_over_against_beth_peor", 'F3'),
        ('Sotah', 1, 9): ("THE PARAMETERS joseph_bones_merited and the_burial_by_the_place — Joseph merited to bury his father, Moses merited Joseph's bones, none greater than Moses so the Place Himself attended him (34:6 'and He buried him'); joseph's bones_oath and exodus_story by CALL; F3 he_buried_him_in_the_valley_in_the_land_of_moab_over_against_beth_peor", 'F3'),
        ('Tosefta Sotah', 4, 4): ("THE PARAMETER the_four_mil — the body borne four mil on the Shekhinah's wings from Reuben's field to Gad's (357:31 — died in Reuben's inheritance, buried in Gad's field; 355:6 and Onkelos 33:21 at the blessing): THE POINTER 33:21 -> 34:6 PAID; gad_reuben's DATA moses_grave by CALL; F3 he_buried_him_in_the_valley_in_the_land_of_moab_over_against_beth_peor", 'F3')}
lines = ["# Deuteronomy 34:1-12 — THE LEAN EXAM (THE DEUTERONOMY WALK 22b, 2026-09-30): the Mishnah rows the reading's ledger cites and the Tosefta's one row, read whole at the design",
         "", "THE LEAN FORM (owner-ruled 2026-09-23): no docket, no Talmud segment read; the rows the reading's ledger cites are the compile's cases — every distinct citation with a paragraph COMPUTED from the ledger",
         f"(logic/oral_triage/deu_34_moses_death_2026-09-30.md) by the citation regex: {len(DIST)} — {', '.join(f'{t} {c}:{p}' for t, c, p in DIST)}; the ONE the regex misread (the Mishnah's Sotah 4:4 read for the Tosefta's) read whole and EXCLUDED;",
         "the folios the ledger names OWED, cited never read: " + '; '.join(S.TALMUD_OWED) + ". Each row a case of a cell (the runner cold_run_moses_death.py) with its verdict a PARAMETER or a DATA row — the answer sheet's, never the code's.", ""]
tot = 0; nrow = 0
for t, c, p in DIST:
    he, en = row(t, c, p); tot += len(he) + len(en)
    seats = len(re.findall(re.escape(f'{t} {c}:{p}') + r'\b', LED))
    four = ' '.join(w.strip('.:,;') for w in he.split()[:4]); eng = gloss(re.sub('([' + chr(0x5d0) + '-' + chr(0x5ea) + chr(0x5b0) + '-' + chr(0x5c7) + ']+)', lambda m: m.group(1) + " (the export's own Hebrew word)", en))   # the lint's window stops at a period — the cut's punctuation dropped; a Hebrew run inside the English glossed on the spot
    if (t, c, p) in S.MISHNAH_EXCLUDED:
        lines.append(f"- Mishnah {t} {c}:{p} — EXCLUDED. The regex's misread: the ledger's '{t} {c}:{p}' names the TOSEFTA's row (Tosefta {t} {c}:{p} — the testing shelf's one row) at its {seats} seats; the Mishnah's own row read whole and excluded — HE: {four} ({eng[:70]}) EN: {eng}")
        continue
    nrow += 1; case, cell = CASE[(t, c, p)]
    name = ('Tosefta ' if t.startswith('Tosefta ') else 'Mishnah ') + (t[8:] if t.startswith('Tosefta ') else t) + f' {c}:{p}'
    lines.append(f"- {name} — LAW. Cited at {seats} seats of the ledger. {case} ({cell}). HE: {four} ({eng[:70]}) EN: {eng}")
lines += ["", f"**read: {nrow} of {nrow} rows — COMPLETE** ({len(DIST)} distinct citations; {nrow} rows the cases, {len(S.MISHNAH_EXCLUDED)} excluded; {tot} characters read whole)", ""]
txt = '\n'.join(lines)
open(OUT, 'w', encoding='utf-8').write(txt)
r = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', OUT], capture_output=True, text=True)
print('THE LEAN EXAM WRITTEN:', OUT, len(txt.encode()), 'bytes;', nrow, 'rows,', len(S.MISHNAH_EXCLUDED), 'excluded,', tot, 'chars;', r.stdout.strip().split('\n')[-1])
