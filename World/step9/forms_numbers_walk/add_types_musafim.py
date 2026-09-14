#!/usr/bin/env python3
# THE NUMBERS WALK sitting 9b — THE COMPILE OF THE OFFERINGS CALENDAR (2026-09-11; World/step9/NUMBERS_WALK.md "Sitting 9b"): THE TYPES FIRST —
# ONE new kind on the tape (the whole calendar commanded in one speech, Num 28:1-29:39), seven CASE kinds for the exam's scene, ONE new effect
# (musaf_owed — the period timer's debit; the tradition's own word), NO registry row (the daemon writes on 'the-altar' as the erection does —
# the token's two seats FILED), the 56th daemon's block (law_musafim, installed_by called_from_the_tent — law_moadim's form), the functions
# block, the dependency span and edges (the pointers after the gate's print), the installation probe's count. The `he` is the whole verse
# from the pointed DB text (cantillation stripped), the witnesses the plain consonantal verses — no anchor word typed. Idempotent
# (add_types_census2.py's form).
import re, sqlite3, yaml
ROOT = "<repo-old>"
db = sqlite3.connect(f"file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro", uri=True)
def words(book, ch, vs):
    return [r[0] for r in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx", (book, ch, vs)).fetchall()]
pv = lambda w: ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
def PV(book, ch, vs, lo=None, hi=None):
    ws = words(book, ch, vs); assert ws, (book, ch, vs)
    if lo is not None: ws = ws[lo - 1:hi]
    return ' '.join(pv(w) for w in ws)
def LV(book, ch, vs):
    return ' '.join(''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7)) for w in words(book, ch, vs))
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
N = 'Num'
def HE(ch, lo, hi, en, cap=6):
    vv = list(range(lo, min(hi, lo + cap - 1) + 1))
    s = ' · '.join(PV(N, ch, v) + ' (%s — Num %d:%d)' % (en if v == lo else 'the verse continues', ch, v) for v in vv)
    return s + (' · … (through Num %d:%d)' % (ch, hi) if hi > vv[-1] else '')
def WIT(ch, lo, hi):
    return ['Num %d:%d | %s' % (ch, v, LV(N, ch, v)) for v in range(lo, hi + 1)]
SUB = "submitted by cold_run_musafim.py [subjects: %s] (the command scene, THE NUMBERS WALK 9b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_musafim (cold_run_musafim.py) -> %s"
CASE = "submitted by cold_run_musafim.py [subjects: the exam's persons] (the wrap's scene); consumed by law_musafim (cold_run_musafim.py) -> %s"
U28 = "num_28_daily_shabbat_rosh (STEP_Nm_28_1 through STEP_Nm_28_15; claims PN28A-01 through PN28A-07); num_28_pesach_shavuot (STEP_Nm_28_16 through STEP_Nm_28_31; claims PN28B-01 through PN28B-07); num_29_fall_festivals (STEP_Nm_29_1 through STEP_Nm_29_39; claims PN29A-01 through PN29A-07)"
FIRST = "and the LORD spoke to Moses, saying: command the children of Israel and say to them: My offering, My bread for My fire offerings, My pleasing odor, you shall keep to bring near to Me in its appointed time"
KINDS = [
 ("offerings_calendar_commanded", "speech",
  "the offerings calendar commanded — ONE speech, 28:1 to 29:39 (the register's one verb; 30:1 the closer): 'command the children of Israel... My offering, My bread for My fire offerings, My pleasing odor, you shall keep to bring near to Me in its appointed time' (28:2); THE TAMID restated from Exodus 29:38-42 with its deltas (28:3-8 — 'without blemish' added, 'made at Mount Sinai', 'strong drink'); THE SABBATH's two lambs 'on its Sabbath, beside the continual' (28:9-10 — the word 'besides' twelve seats in the span); THE NEW MOON's table two bulls, one ram, seven lambs and a goat 'for a sin offering TO THE LORD' (28:11-15 — the only goat so named) with THE MASTER ROW of tenths and hin-fractions restating 15:4-10 and cited by pointer eight times; PESACH's seven days 'as these' (28:16-25), THE DAY OF FIRSTFRUITS with the same table (28:26-31 — Leviticus 23:18's set reversed: [2, 1, 7] for [7, 1, 2]); TISHRI — the day of blowing (29:1-6, the stack 'besides the burnt offering of the month and the continual'), the tenth (29:7-11, 'besides the sin offering of the atonements'), SUKKOT's declining bulls thirteen to seven = seventy with fourteen lambs and two rams each day, the water libation's three letters at 29:19, 29:31, 29:33, the eighth day [1, 1, 7] 'an assembly' (29:12-38); the closer 'these you shall make to the LORD in your appointed times, besides your vows and your freewill offerings' (29:39) — the whole read as ONE TABLE",
  HE(28, 1, 6, FIRST) + ' · … (through Num 29:39)', WIT(28, 1, 31) + WIT(29, 1, 39),
  "Num 28:1-31, 29:1-39; Onkelos Num 28:1-29:39 (Shavuot named ATZERET at 28:26; the teruah 'a day of wailing' at 29:1); Exod 29:38-42 (the tamid's first seat); Num 15:4-10 (the master row's first seat); Lev 23:1-44 (the appointed times' first seat — the shared tokens per pair); Num 10:10; Deut 16:1-17; Ezek 45:17-46:15; 2 Chr 2:3, 31:3; Ezra 3:5; Neh 10:34 (Hebrew numbering); Sifrei Bamidbar 142-152; Babylonian Talmud Menachot 44b-45b, 49a-50a, 87a-89a; Sukkah 47a-51a, 55b; Rosh Hashanah 4b-5a, 32a-34a; Shevuot 2a-2b, 9a-13a; Taanit 2b-3a; Pesachim 58a-59a, 66a, 77a; Yoma 62b-63a, 70a-70b; Arakhin 13a; Chagigah 6a-6b, 17a-18a; Beitzah 19a-20b; Berakhot 26a; Mishnah Menachot 4:2-4, 8:7, 9:2-5; Tamid 4:1; Shekalim 4:1; Taanit 4:2; Sukkah 4:9, 5:6; Shevuot 1:4-5; Zevachim 10:1; Megillah 3:5-6",
  U28, SUB % ("israel", "musaf_owed EIGHT PERIOD TIMERS on the-altar (the Calendar's keys by CALL — sabbath, month, passover_1, atzeret, rosh_hashanah, yom_kippur, sukkot_1, shemini — each due at the key's next day from the tape's counter, re-armed by the engine's period; the tables the values); the tamid's OPEN debt (tamid_owed on the-altar since Exod 40:29) READ and named, never rewritten; no marker, no entity"), ["tables", "close"]),
 ("tamid_case", "case", "the exam's rows on the continual offering (Num 28:1-8 — Mishnah Tamid 4:1; Menachot 4:4; Yoma 62b-63a; Pesachim 58a-59a, 66a, 81b; Menachot 87a-89a; Chagigah 6a-6b; Shevuot 10b-12b; Arakhin 13a): the appointed time and the Sabbath, two lambs and ben Azzai's corners, the tenth and the beaten oil, made at Sinai, the strong drink, the second lamb's pointer, the afternoon hour, the morning missed, the surplus lambs, the impurity of the deep, the priest's watches",
  HE(28, 3, 3, "and you shall say to them: this is the fire offering that you shall bring near to the LORD: yearling lambs without blemish, two a day, a continual burnt offering"), WIT(28, 3, 3), "Num 28:1-8; Exod 29:38-42; Mishnah Tamid 4:1; Menachot 4:4; Yoma 62b:1-63a:18; Pesachim 58a-59a, 66a:1-13, 81b:3; Menachot 87a-89a; Chagigah 6a:15-6b:5; Shevuot 10b:7-12b:5; Arakhin 13a:9-11; Berakhot 26a:11-17", U28, CASE % "accepted / commanded / tamid_owed / libation_owed / disqualified / exempt (the exam's persons)", ["person", "ask"]),
 ("sabbath_musaf_case", "case", "the exam's rows on the Sabbath's additional offering (Num 28:9-10 — Mishnah Tamid 7:3; Menachot 4:4; Shabbat 132b; Beitzah 19a-20b; Pesachim 66a): two lambs on its Sabbath, the override of the Sabbath by the fixed-time offerings, between the temidim, the Sabbath's musaf as the a fortiori's premise, Hillel's two hundred",
  HE(28, 10, 10, "the burnt offering of the Sabbath on its Sabbath, beside the continual burnt offering and its libation"), WIT(28, 10, 10), "Num 28:9-10; Mishnah Menachot 4:4; Shabbat 132b:1; Beitzah 19a:11, 20b:4-6; Pesachim 66a:3; Menachot 49b:5", U28, CASE % "accepted / musaf_owed / labor_barred / rest_required / exempt (the exam's persons)", ["person", "ask"]),
 ("new_moon_case", "case", "the exam's rows on the new moon's offering (Num 28:11-15 — Menachot 45a, 89a; Shevuot 2a-2b, 9a-10b; Rosh Hashanah 4b-5a; Chagigah 17b, 18a; Megillah 3:6): the table two-one-seven, the master row's tenths and hin-fractions, in its month, the goat 'to the LORD' and the sin the LORD alone knows, the availability ladder from Ezekiel, the month sanctified by its offerings, labor permitted, absent from Leviticus 23",
  HE(28, 15, 15, "and one goat of the goats for a sin offering to the LORD, beside the continual burnt offering it shall be made, and its libation"), WIT(28, 15, 15), "Num 28:11-15; Num 15:4-10; Menachot 45a:5-11, 89a:15; Shevuot 2a:8-2b:7, 9a:7-10, 9b:2-10a:17; Rosh Hashanah 5a:4; Chagigah 17b:7, 18a:6; Ezek 46:6-7; Mishnah Megillah 3:6", U28, CASE % "accepted / musaf_owed / atoned_forgiven / sanctify_day / exempt (the exam's persons)", ["person", "ask"]),
 ("pesach_shavuot_case", "case", "the exam's rows on Pesach's seven days and the day of firstfruits (Num 28:16-31 — Menachot 44b-45b, 84b, 65b-66a, 68b; Pesachim 77a; Chagigah 17a-17b; Beitzah 12a, 20b; Rosh Hashanah 4b): the dates and the food-work rule, the table 'as these', the seventh, the omer and the two loaves, the second set against Leviticus 23:18 — R. Akiva's two orders, the wilderness set, the loaves and the lambs, the seven days of redress, the day of slaughter",
  HE(28, 27, 27, "and you shall bring near a burnt offering for a pleasing odor to the LORD: two young bulls, one ram, seven yearling lambs"), WIT(28, 27, 27), "Num 28:16-31; Lev 23:5-21; Menachot 44b:1-45b:25, 84b:1-21, 65b-66a, 68b; Pesachim 77a:1-19; Chagigah 17a:3-17b:8; Beitzah 12a:4, 20b:11-14; Rosh Hashanah 4b:13-15; Mishnah Menachot 4:3, 8:7", U28, CASE % "accepted / musaf_owed / labor_barred / commanded / disqualified / exempt (the exam's persons)", ["person", "ask"]),
 ("tishri_case", "case", "the exam's rows on the day of blowing and the tenth (Num 29:1-11 — Rosh Hashanah 16a, 32a-34a; Yoma 3a, 70a-70b, 76a; Shevuot 2a-2b, 9a-10b; Arakhin 13a; Menachot 87b): the sound and the instrument, 'a day of teruah' in the count, by day not at night, the stack of Tishri's first, the tenth's afflictions, the atonements' goat and the inner goat, the rams one or two, the musaf order, sixteen lambs",
  HE(29, 1, 1, "and in the seventh month, on the first of the month, a holy convocation shall be to you; no servile work shall you do; a day of blowing shall it be to you"), WIT(29, 1, 1), "Num 29:1-11; Lev 23:23-32, 25:9; Rosh Hashanah 16a:15-17, 33b:5-34a:19; Yoma 3a:4, 70a-70b, 76a:11; Shevuot 2a:6-2b:11, 9a:2-4, 10a:14-21; Arakhin 13a:9-11; Menachot 87b:2-5; Num 10:5-10", U28, CASE % "accepted / musaf_owed / labor_barred / rest_required / atoned_forgiven / exempt (the exam's persons)", ["person", "ask"]),
 ("sukkot_case", "case", "the exam's rows on Sukkot and the eighth day (Num 29:12-38 — Sukkah 47a-51a, 55b; Taanit 2b-3a; Shabbat 103b; Menachot 87b; Zevachim 110b; Meilah 13b; Chagigah 17a; Beitzah 19b-20b; Rosh Hashanah 4b): the declining bulls and the seventy nations, the watches' division, the water libation's four sources and its measure, the eighth's head without the conjunction and its six marks, the pointer lines, the dotted tenth, the stay, the vows' deadline",
  HE(29, 13, 13, "and you shall bring near a burnt offering, a fire offering, a pleasing odor to the LORD: thirteen young bulls, two rams, fourteen yearling lambs, they shall be without blemish"), WIT(29, 13, 13), "Num 29:12-38; Lev 23:33-43; Sukkah 47a:1-51a:17, 55b:1-16; Taanit 2b:1-3a:14; Shabbat 103b:12-16; Menachot 87b:5; Zevachim 110b:1-9; Meilah 13b:8; Chagigah 17a:6-9; Beitzah 19b:8-13, 20b:5-6; Rosh Hashanah 4b:8-15; Mishnah Sukkah 4:9, 5:6", U28, CASE % "accepted / musaf_owed / libation_owed / smoked_to_the_lord / exempt (the exam's persons)", ["person", "ask"]),
 ("calendar_case", "case", "the exam's rows on the calendar as one table (Num 29:39 and the span whole — Menachot 49b, 110a; Sukkah 51a; Shevuot 12b; Berakhot 26a; Chagigah 18a; 2 Chronicles 2:3, 29:27, 5:13): 'these you shall make in your appointed times', the thirteen goats' three tiers and their vav, the sums, ben Azzai's whole-Torah census, the trumpets over the temidim and musafim, the musaf's window, the vows besides, the interchange ring, the run in the Writings",
  HE(29, 39, 39, "these you shall make to the LORD in your appointed times, besides your vows and your freewill offerings, for your burnt offerings and for your meal offerings and for your libations and for your peace offerings"), WIT(29, 39, 39), "Num 29:39; Num 28:1-29:38 whole; Menachot 49b:5, 110a:9; Sukkah 51a:12-13; Shevuot 9b:2-10a:11, 12b:3-4; Berakhot 26a:11-17; Chagigah 18a:6; 2 Chr 2:3, 5:13, 29:27; Ezra 3:5; Neh 10:34 (Hebrew numbering)", U28, CASE % "accepted / musaf_owed / commanded / exempt (the exam's persons)", ["person", "ask"]),
]
assert len(KINDS) == 8, len(KINDS)
# ---- the kinds: append INTO the `events:` mapping (before `narrative_verbs:`) ----
path = f"{ROOT}/World/step9/event_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
have = yaml.safe_load(text)['events']
out = []
for name, form, en, he, wit, ink, corpus, tape, fields in KINDS:
    if name in have: continue
    out.append(f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    form: {form}\n    witness: [{', '.join(q(w) for w in wit)}]\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    tape: {q(tape)}\n    fields: [{', '.join(q(f) for f in fields)}]\n")
if out:
    i = text.index('\nnarrative_verbs:\n')
    text = text[:i] + '\n' + ''.join(out).rstrip('\n') + text[i:]
    open(path, 'w', encoding='utf-8').write(text)
after = yaml.safe_load(open(path, encoding='utf-8'))
assert all(k[0] in after['events'] for k in KINDS)
print('kinds: %d added of %d, registry %d' % (len(out), len(KINDS), len(after['events'])))
# ---- ONE new effect: musaf_owed (the period timer's debit; the tradition's word) — appended at the effects file's end ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
fx = yaml.safe_load(text)['effects']
for e in ('tamid_owed', 'libation_owed', 'accepted', 'atoned_forgiven', 'smoked_to_the_lord', 'labor_barred', 'rest_required', 'exempt', 'disqualified', 'commanded', 'sanctify_day'):
    assert e in fx, e
if 'musaf_owed' not in fx:
    he10 = PV(N, 28, 10, 1, 8)   # the verse's first eight words from the DB: 'the burnt offering of the Sabbath on its Sabbath, beside the continual burnt offering and its libation'
    assert LV(N, 28, 10).split()[:8] == [''.join(c for c in w if not (0x0591 <= ord(c) <= 0x05C7)) for w in he10.split()], he10
    block = ('  musaf_owed:\n'
             '    en: "the additional offering owed — the PERIOD TIMER of the altar for each appointed day: \'the burnt offering of the Sabbath on its Sabbath, beside the continual burnt offering and its libation\' (Num 28:10) — the tradition\'s own word מוּסָף (\'additional\' — Mishnah Menachot 4:4, Shekalim 4:1, Tamid 7:3) for the offering BESIDES the continual; eight timers keyed to the Calendar (the Sabbath, the month, the first and seventh of Pesach, Shavuot, the day of blowing, the tenth, the first of Sukkot, the eighth), each fire OPENING the day\'s debt of its table on the altar and the offering brought CLOSING it (THE CLOSE PAIRING — the tamid_owed form, CLOCK.md section 3); the table the value"\n'
             f'    he: {q(he10 + " (the burnt offering of the Sabbath on its Sabbath, beside the continual burnt offering and its libation — Num 28:10)")}\n'
             '    ledger_op: debit   # THE NUMBERS WALK 9b (2026-09-11): the first PERIOD timer on the tape (law_moadim\'s sanctify_day carried the form with no period set before this sitting); the debit re-armed by the engine at each fire\n'
             '    ink: "Num 28:10 (\'the burnt offering of the Sabbath on its Sabbath\' a hapax; \'beside the continual burnt offering\' — the word \'besides\' twelve seats in 28:1-29:39), 28:14 (\'the burnt offering of the month in its month\'), 28:23-24, 28:31, 29:6 (the stack: \'besides the burnt offering of the month and its meal offering and the continual burnt offering\'), 29:11 (\'besides the sin offering of the atonements\'), 29:16-38 (\'besides the continual burnt offering, its meal offering and its libation\' — the pointer line on every day), 29:39 (\'these you shall make to the LORD in your appointed times, besides your vows\'); Lev 23:37-38 (the moadim\'s closer — \'each day\'s matter on its day... besides the Sabbaths of the LORD\'); Ezek 45:17, 46:4-7 (the prince\'s Sabbath and new-moon tables — the run\'s altered numbers); 2 Chr 2:3, 31:3; Ezra 3:5; Neh 10:34 (Hebrew numbering: \'the burnt offerings of the Sabbaths, of the new moons, of the appointed times\' — the run); Onkelos Num 28:10 (\'the Sabbath\'s burnt offering on its Sabbath, besides the continual burnt offering\')"\n'
             '    corpus: "num_28_daily_shabbat_rosh (STEP_Nm_28_9, 28_10, 28_14, 28_15); num_28_pesach_shavuot (STEP_Nm_28_23, 28_24, 28_31); num_29_fall_festivals (STEP_Nm_29_6, 29_11, 29_16 through 29_38, 29_39)"\n'
             '    exam: "cold_run_musafim.py; Mishnah Menachot 4:4 (the temidim and the musafim do not hold each other up), Shekalim 4:1 (bought from the chamber), Zevachim 10:1 (the frequent precedes), Tamid 7:3 (the Sabbath\'s musaf and the song), Berakhot 4:1 (the additional prayer\'s window), Arakhin 2:5 (the six lambs), Beitzah 2:4 (the festival\'s licensed slaughter — \'apart from the daily and additional offerings\'), Shevuot 1:4-5 (the musafim\'s goats)"\n')
    text = text.rstrip('\n') + '\n' + block
    open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert 'musaf_owed' in fx and fx['musaf_owed']['ledger_op'] == 'debit'
print('effects: musaf_owed %s (registry %d); reused: tamid_owed (READ), libation_owed, accepted, atoned_forgiven, smoked_to_the_lord, labor_barred, rest_required, exempt, disqualified, commanded, sanctify_day' % ('present' if 'musaf_owed' in fx else 'MISSING', len(fx)))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_musafim:' not in text:
    block = '''  law_musafim:
    file: cold_run_musafim.py
    wraps: musafim
    given_at: Num 28:1
    installed_by: called_from_the_tent   # THE NUMBERS WALK 9b (2026-09-11): a standing statute for the generations — law_moadim's form (Lev 23:1): the calendar's EIGHT PERIOD TIMERS set at the command's verse on the-altar (the token's two seats — Exod 17:15's altar and the tabernacle's — FILED for a registry sitting; the daemon writes where the erection's tamid_owed sits); the tamid's open debt READ, never rewritten
    watches:
      offerings_calendar_commanded: [musaf_owed]                      # 28:1-29:39: eight musaf_owed period timers (the Calendar's keys by CALL: sabbath, month, passover_1, atzeret, rosh_hashanah, yom_kippur, sukkot_1, shemini; the tables the values); the tamid's debt READ and named
      tamid_case: [accepted, commanded, tamid_owed, libation_owed, disqualified, exempt]   # the exam's rows on 28:1-8
      sabbath_musaf_case: [accepted, musaf_owed, labor_barred, rest_required, exempt]     # the exam's rows on 28:9-10
      new_moon_case: [accepted, musaf_owed, atoned_forgiven, sanctify_day, exempt]         # the exam's rows on 28:11-15
      pesach_shavuot_case: [accepted, musaf_owed, labor_barred, commanded, disqualified, exempt]   # the exam's rows on 28:16-31
      tishri_case: [accepted, musaf_owed, labor_barred, rest_required, atoned_forgiven, exempt]   # the exam's rows on 29:1-11
      sukkot_case: [accepted, musaf_owed, libation_owed, smoked_to_the_lord, exempt]      # the exam's rows on 29:12-38
      calendar_case: [accepted, musaf_owed, commanded, exempt]                            # the exam's rows on 29:39 and the span whole
'''
    i = text.index('  law_zelophehad:')
    text = text[:i] + block + text[i:]
if '\n  musafim:   # THE NUMBERS WALK 9b' not in text:
    fb = '''  musafim:   # THE NUMBERS WALK 9b (2026-09-11)
    the_tamid: {status: WRAPPED, by: law_musafim}
    the_sabbath: {status: WRAPPED, by: law_musafim}
    the_new_moon: {status: WRAPPED, by: law_musafim}
    pesach_shavuot: {status: WRAPPED, by: law_musafim}
    tishri: {status: WRAPPED, by: law_musafim}
    sukkot: {status: WRAPPED, by: law_musafim}
    the_calendar: {status: WRAPPED, by: law_musafim}
    the_watches: {status: WRAPPED, by: law_musafim}
'''
    i = text.index('  second_census:   # THE NUMBERS WALK 8b (2026-09-11)')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_musafim' in dd['daemons'] and 'musafim' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_musafim %s); functions blocks: %d' % (len(dd['daemons']), 'law_musafim' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + edges (the POINTERS after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  musafim:' not in text:
    a = "  second_census: [[Num, 25, 19, 19], [Num, 26, 1, 65]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  musafim:     [[Num, 28, 1, 31], [Num, 29, 1, 39]]   # THE NUMBERS WALK 9b (2026-09-11; NUMBERS_WALK.md \"Sitting 9b\"): the offerings calendar — the tamid, the Sabbath, the new moon, Pesach and the firstfruits day, Tishri, Sukkot and the eighth, the closer\n" + text[j + 1:]
    edges = '''  - {from: musafim, to: incense_shekel, disposition: CALL, link: reference, carries: procedure,
     why: "THE NUMBERS WALK 9b (2026-09-11) | 28:3-8 restates Exod 29:38-42 word for word with its deltas ('without blemish' added, 'made at Mount Sinai', 'strong drink'; 28:8 'as the meal offering of the morning' the same pointer as 29:41): cold_run_incense_shekel.tamid('two_lambs', 'plural_minimum', 'ordinals', 'clocks', 'measures', 'beaten_oil', 'three_log', 'pointer', 'olat_tamid', 'sabbath_overrides', 'sheet_4_4', 'sheet_shekalim_4_1', 'doubled_morning_order', 'initiations') CALLED — the tamid's own engine; the Sabbath token of 28:9-10 homes law_sabbath in the same file"}
  - {from: musafim, to: shelach, disposition: CALL, link: reference, carries: value,
     why: "THE NUMBERS WALK 9b (2026-09-11) | 28:12-14 'three tenths... for the bull, two tenths... for the ram, a tenth... for the lamb; their libations half a hin for the bull, a third for the ram, a quarter for the lamb' RESTATES 15:4-10's table and 28:7's quarter-hin is its lamb row: cold_run_shelach.TABLE / LOGS / RATIO / MONTH_ROW / SUKKOT_SABBATH and libations('table', 'table_seats', 'sukkot_sabbath', 'takes', 'mixing') and DATA hin_in_logs, libation_floors CALLED — the master row READ, never re-declared"}
  - {from: musafim, to: moadim, disposition: CALL, link: reference, carries: window,
     why: "THE NUMBERS WALK 9b (2026-09-11) | 28:16-29:38 are Leviticus 23's appointed times at their SECOND seat with the offerings the new column (the shared tokens per pair): cold_run_moadim.passover(), rosh_hashanah(), yom_kippur(), sukkot(), shavuot_animals(), two_loaves(), omer(), work_class and OM CALLED — the dates by the Calendar's keys, the labor class, the omer's count, Leviticus 23:18's set against 28:27's"}
  - {from: musafim, to: offerings, disposition: CALL, link: reference, carries: procedure,
     why: "THE NUMBERS WALK 9b (2026-09-11) | the bulls, rams and lambs 'for a burnt offering' and the goats 'for a sin offering' on every day of the span; 29:39's 'your peace offerings': cold_run_offerings.dispatch('olah:herd', 'olah:flock', 'outer_chatat', 'shelamim') CALLED — the rite is Leviticus 1's and 4's, not this span's question"}
  - {from: musafim, to: yoma, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 9b (2026-09-11) | 29:11 'one goat of the goats a sin offering, BESIDES THE SIN OFFERING OF THE ATONEMENTS' names the inner goat of Leviticus 16 beside the musaf's outer goat: cold_run_yoma.route() ('festival_and_new_moon_goats'), route(known_end=True) ('outer_goat_and_day') and service_order() CALLED — the tiers (Mishnah Shevuot 1:4-5) and the Day's musaf order (Yoma 70a-70b)"}
  - {from: musafim, to: minchah, disposition: CALL, link: reference, carries: value,
     why: "THE NUMBERS WALK 9b (2026-09-11) | 28:26 'on the day of the firstfruits, when you bring near a NEW MEAL OFFERING' is the omer-and-loaves day (Lev 23:16-17) and every table's 'flour mingled with oil' the meal offering's grade: cold_run_minchah.omer('source'), oil_grade() and salt('meal_offering') CALLED"}
  - {from: musafim, to: pesach, disposition: VIA, link: reference, via: moadim,
     why: "THE NUMBERS WALK 9b (2026-09-11) | 28:16 'in the first month, on the fourteenth day of the month, a Passover to the LORD' — the paschal token; its procedure and eating window are reached through cold_run_moadim.passover() (PS.paschal_procedure by the moadim runner's own call), not a second import"}
  - {from: musafim, to: calendar, disposition: VIA, link: reference, via: moadim,
     why: "THE NUMBERS WALK 9b (2026-09-11) | the three pilgrimage days (Pesach's first, the firstfruits day, Sukkot's first) — CAL.pilgrimage is the moadim runner's call; the musafim runner reads the dates through MO"}
  - {from: musafim, to: chatat, disposition: VIA, link: reference, via: yoma,
     why: "THE NUMBERS WALK 9b (2026-09-11) | the thirteen goats 'for a sin offering' — their tier logic (Lev 4's outer sin offering) is reached through cold_run_yoma.route(), the offerings engine's dispatch('outer_chatat') the rite"}
  - {from: musafim, to: pre_sinai, disposition: VIA, link: reference, via: incense_shekel,
     why: "THE NUMBERS WALK 9b (2026-09-11) | 28:9-10's Sabbath ('on the Sabbath day two lambs... on its Sabbath') — the Sabbath token homes the pre-Sinai span (Exod 16); the tabernacle's Sabbath clause (law_sabbath, Exod 31:12-17) lives in cold_run_incense_shekel, which this runner imports — the mekoshesh runner's own disposition (THE TENT sitting 3)"}
  - {from: sequence, to: musafim, disposition: CALL, link: none,
     why: "THE NUMBERS WALK 9b (2026-09-11) | the sequential run's REGISTRATION edge — ('cold_run_musafim', 'law_musafim') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license)"}
'''
    a = "  - {from: sequence, to: second_census, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
assert 'musafim' in dep['spans']
print('dependency: span + 11 edges (musafim); the pointers after the gate\'s print')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
a = "len(real) == 55 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 8b (2026-09-11): 54 -> 55, law_second_census;"
if a in text:
    text = text.replace(a, "len(real) == 56 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 9b (2026-09-11): 55 -> 56, law_musafim; 8b: 54 -> 55, law_second_census;")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 56" in open(path, encoding='utf-8').read()
print('installation_probes I5: 56')
