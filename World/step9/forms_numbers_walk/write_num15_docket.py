import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE TENT sitting 3 (2026-09-09) — THE EXAM'S DOCKET for Num 15:32-36 (cold_run_mekoshesh.py): the testing shelf routed BY
# TOPIC (logic/MISHNAH_TOPICS.md: Courts — Sanhedrin; Sabbath — Shabbat; the Tosefta beside), the rows enumerated from the
# shelf's own files, the credits found by grep over the prior dockets (the credit guards), the coverage COMPUTED. Append-only.
import json, os, re, html, glob
ROOT = _ROOT
OUT = f'{ROOT}/logic/oral_triage/num_15_mekoshesh_exam_2026-09-09.md'
assert not os.path.exists(OUT), 'docket exists — append, never overwrite'
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s)).strip()
X = f'{ROOT}/Data/sefaria_export'
ms = json.load(open(f'{X}/Mishnah_Sanhedrin/en.json'))['text']; sh = json.load(open(f'{X}/Mishnah_Shabbat/en.json'))['text']
ts = json.load(open(f'{X}/Tosefta_Sanhedrin/en.json'))['text']
assert len(ms[4]) == 5 and len(ms[5]) == 6 and len(ms[6]) == 11 and len(sh[6]) == 4, (len(ms[4]), len(ms[5]), len(ms[6]), len(sh[6]))
assert len(ts[8]) == 0, 'Tosefta Sanhedrin chapter 9 is not empty on the shelf any more'
tos_rows = [(ci + 1, i + 1) for ci, ch in enumerate(ts) for i, r in enumerate(ch) if re.search(r'\bwarn', clean(r), re.I)]
assert tos_rows == [(11, 3)], tos_rows
ROWS = ['Mishnah Sanhedrin 5:1'] + ['Mishnah Sanhedrin 6:%d' % i for i in range(1, 7)] + ['Mishnah Sanhedrin 7:1', 'Mishnah Sanhedrin 7:4', 'Mishnah Sanhedrin 7:8',
        'Mishnah Shabbat 7:1', 'Mishnah Shabbat 7:2', 'Tosefta Sanhedrin 11:3']
# the credits: a row is CREDIT when a prior docket or cases table carries it (the reading ledgers of units excluded — the E4 rule)
prior = {}
for f in sorted(glob.glob(f'{ROOT}/logic/oral_triage/*.md')) + sorted(glob.glob(f'{ROOT}/World/step9/*.py')):
    b = os.path.basename(f)
    if b.startswith(('exo_', 'lev_', 'gen_', 'num_')) and b.endswith('.md'): continue
    if b == 'cold_run_mekoshesh.py': continue          # this sitting's own runner is not a prior read
    t = open(f, encoding='utf-8').read()
    for r in ROWS:
        if re.search(re.escape(r) + r'(?!\d)', t): prior.setdefault(r, []).append(b)
credited = {r: v for r, v in prior.items()}
fresh = [r for r in ROWS if r not in credited]
assert sorted(credited) == sorted(['Mishnah Sanhedrin 6:1', 'Mishnah Sanhedrin 6:3', 'Mishnah Sanhedrin 7:1', 'Mishnah Sanhedrin 7:4', 'Mishnah Sanhedrin 7:8', 'Mishnah Shabbat 7:1', 'Mishnah Shabbat 7:2']), sorted(credited)
N = len(ROWS)

body = r'''# The wood-gatherer's exam — the testing shelf for Num 15:32-36 (2026-09-09; THE TENT sitting 3,
# World/step9/THE_TENT.md section 3; the compile cold_run_mekoshesh.py). Docket: the case-anchored rows routed BY
# TOPIC (logic/MISHNAH_TOPICS.md: Mishnah Sanhedrin — the courts, its chapters 5 (the examinations), 6 (the stoning),
# 7 (the four deaths and the stoned); Mishnah Shabbat 7 (the labors); the Tosefta beside) — the union rule of
# 2026-09-05. Every row opened; credits under the guards (a row graded at a prior docket or cases table is CREDITED
# and quick-looked against this span's cells; the per-unit reading ledgers are not graded rows). TOSEFTA SANHEDRIN
# CHAPTER 9 (the stoning's Tosefta) IS EMPTY ON THE SHELF — the export carries 0 rows there (measured: chapters 1-3,
# 5, 9-10 empty) — an honest gap of the shelf, not a credit; the Tosefta's one warning row (11:3, the rebellious son
# warned before three) is read as context. The Babylonian Talmud Sanhedrin 41a-46b, 78b, 80b and Shabbat 96b are the
# bridge, opened PER GAP at the compile and named in the cells — not docket rows. Append-only.

## Mishnah Sanhedrin 5 (the examinations — 1 of 5 rows in scope)
- Mishnah Sanhedrin 5:1 — MATERIAL (fresh). THE SEVEN EXAMINATIONS of capital witnesses (the seven-year cycle, the
  year, the month, the day of the month, the day of the week, the hour, the place; R. Yose three), then: "do you
  RECOGNIZE him? did you WARN him?" — and the particulars: whom he worshipped and how. The warning is a question the
  court puts to the witnesses — the case's own finders were the warners (Sifrei 113:1 on 15:33). →
  capital_procedure(warning)

## Mishnah Sanhedrin 6 (the stoning — 6 rows whole)
- Mishnah Sanhedrin 6:1 — MATERIAL (CREDIT: graded at the blasphemer's runner and the Emor exam — quick-looked: the
  venue cell is CALLED here). The place of stoning OUTSIDE THE COURT, "a little beyond it" — from the blasphemer's own
  verse, "bring out the curser outside the camp" (Lev 24:14); the cloth-waver and the horseman; the condemned returned
  to the court on a reason to acquit, even four or five times. → capital_procedure(venue) — CALLED L24
- Mishnah Sanhedrin 6:2 — MATERIAL (fresh). TEN CUBITS from the place: "CONFESS" — all who are executed confess; the
  confessor has a portion in the world to come — ACHAN (Joshua 7:19-25): "my son, give glory... and confess", "I have
  sinned", and "the LORD shall trouble you THIS DAY" — this day troubled, not the world to come (the Prophets' run,
  DEMONSTRATE by RUN); one who cannot confess says "let my death atone for all my sins"; R. Yehuda: the conspired-
  against says "except this sin" — the sages: then everyone would. → capital_procedure(confession)
- Mishnah Sanhedrin 6:3 — MATERIAL (CREDIT: graded at the blasphemer's runner as the recorded STRIP-DISPUTE — CALLED
  here). FOUR CUBITS from the place: stripped — a man covered in front, a woman front and back (R. Yehuda); the sages: a
  man stoned naked, a woman not. → capital_procedure(stripping) — CALLED L24
- Mishnah Sanhedrin 6:4 — MATERIAL (fresh). THE STONING HOUSE two men's heights; one witness pushes him at the hips;
  face up; turned over if on his chest; dead — enough; else the SECOND witness takes the stone and casts it on his
  chest; dead — enough; else ALL ISRAEL stone him — "the hand of the witnesses shall be first upon him to put him to
  death, and afterward the hand of all the people" (Deut 17:7). THE SIFREI'S OWN PROTOCOL (114:1) at its Mishnah seat —
  the two verses' reconciliation ("with stones" / "with a stone") is this row. THE HANGING: all the stoned are hanged —
  R. Eliezer; the sages: only the blasphemer and the idolater; a man hung facing the people, a woman facing the tree —
  R. Eliezer; the sages: a man hung, a woman not; the beam, the hands tied, hanged and immediately loosed — "you shall
  not leave his body overnight" (Deut 21:23). → capital_procedure(stoning, hanging) — the parameter row
  hanging_after_stoning (the sages running; R. Eliezer recorded — the Sifrei's arm)
- Mishnah Sanhedrin 6:5 — MATERIAL (fresh). R. Meir on "he that is hung is a CURSE of God" — the Shekhinah's "I am
  distressed about My head, My arm" — the a-fortiori to the righteous; the same-day burial a command and leaving
  overnight a prohibition (Deut 21:23), except for the dead's honor; NOT in his ancestral plot — TWO GRAVEYARDS of the
  court: one for the decapitated and strangled, one for the stoned and burned. → capital_procedure(burial) — the
  graveyards DATA
- Mishnah Sanhedrin 6:6 — MATERIAL (fresh). The flesh decomposed, the bones gathered to the ancestral plot; the
  relatives greet the judges and witnesses — "we hold no grudge"; NO MOURNING RITES (the unmourned death atones), but
  grief in the heart. → capital_procedure(burial)

## Mishnah Sanhedrin 7 (the deaths and the stoned — 3 of 11 rows in scope)
- Mishnah Sanhedrin 7:1 — CONTEXT (CREDIT: the sanctions docket). THE FOUR DEATHS in descending severity — stoning,
  burning, killing, strangling; R. Shimon: burning, stoning, strangling, killing; "this is the mitzvah of the stoned"
  closes the previous chapter. → capital_procedure(mode) — stoning the severest on the sages' order
- Mishnah Sanhedrin 7:4 — MATERIAL (CREDIT: the Acharei exam, the sanctions docket — quick-looked). THE STONED CENSUS —
  eighteen, THE SABBATH DESECRATOR among them (with the blasphemer, the idolater, the Molech-giver, the necromancer, the
  sorcerer, the parent-curser, the betrothed girl's paramour, the inciter, the subverter, the warlock, the rebellious
  son). The mode the tent's output installed, as the Mishnah's row. → the_gatherer(mode) — CALLED IS.sabbath('death_run')
- Mishnah Sanhedrin 7:8 — MATERIAL (CREDIT: the sanctions docket — quick-looked). The Sabbath desecrator stoned for a
  matter whose deliberate is KARET and whose unwitting is a SIN OFFERING — the criterion for which labors are capital
  (Shabbat 96b:16-18's hidden scroll: one of the thirty-nine is not — unnamed; every arm of the gatherer's labor is). →
  the_gatherer(labor) — the parameter row gatherers_labor

## Mishnah Shabbat 7 (the labors — 2 of 4 rows in scope)
- Mishnah Shabbat 7:1 — CONTEXT (CREDIT: the Ki Tisa exam — the great rule's tiers). One who forgets the essence of the
  Sabbath — one sin offering; who forgets the day — one per Sabbath; who knows the day and forgets the labors — one per
  primary labor. → the Sabbath engine's own cells (great_rule), not this runner's
- Mishnah Shabbat 7:2 — MATERIAL (CREDIT: the sanctuary-build docket, the Sabbath engine's data row — quick-looked).
  THE PRIMARY LABORS, FORTY LESS ONE — sowing, plowing, reaping, GATHERING SHEAVES (מְעַמֵּר, "binding"), threshing...
  DETACHING is reaping's kind, CARRYING the last (from domain to domain): the three arms of the gatherer's labor (Shabbat
  96b:15) are three of the thirty-nine. → the_gatherer(labor)

## Tosefta Sanhedrin (the chapter of the stoning EMPTY on the shelf; 1 row in scope)
- Tosefta Sanhedrin 11:3 — CONTEXT (fresh). The rebellious son WARNED BEFORE THREE — "and they shall say to the elders
  of his city": the warning before witnesses as a procedural form at another stoned case (Deut 21:19-20, OWED FORWARD);
  the gatherer's warners were his finders. → capital_procedure(warning)

## CITE INDEX — every row opened, each fully named (coverage COMPUTED by write_num15_docket.py against the shelf's own
## row counts: Mishnah Sanhedrin chapter 5 of 5 rows, chapter 6 of 6, chapter 7 of 11; Mishnah Shabbat chapter 7 of 4;
## Tosefta Sanhedrin's warning rows found by grep — 1; credits found by grep over the prior dockets and cases tables)
__CITES__
(__N__ rows: fresh __FRESH__, credited __CRED__ — __CREDLIST__.)

**read: __N__ of __N__ — COMPLETE** (the declared testing-shelf rows for the case, all opened and verdicted this
sitting; the Tosefta's stoning chapter empty on the shelf, recorded as the shelf's gap)
'''
verdicts = re.findall(r'^- (Mishnah Sanhedrin \d+:\d+|Mishnah Shabbat \d+:\d+|Tosefta Sanhedrin \d+:\d+) — (MATERIAL|CONTEXT)', body, re.M)
assert [v for v, _ in verdicts] == ROWS, ([v for v, _ in verdicts], ROWS)
credit_marks = re.findall(r'^- (Mishnah \w+ \d+:\d+|Tosefta \w+ \d+:\d+) — (?:MATERIAL|CONTEXT) \((CREDIT|fresh)', body, re.M)
assert {r for r, k in credit_marks if k == 'CREDIT'} == set(credited), ({r for r, k in credit_marks if k == 'CREDIT'} ^ set(credited))
body = (body.replace('__CITES__', '\n'.join(ROWS)).replace('__N__', str(N)).replace('__FRESH__', str(len(fresh))).replace('__CRED__', str(len(credited)))
            .replace('__CREDLIST__', '; '.join('%s in %s' % (r, ', '.join(sorted(set(v)))) for r, v in sorted(credited.items()))))
open(OUT, 'w', encoding='utf-8').write(body)
print('wrote', OUT, '| rows', N, '| fresh', len(fresh), '| credited', len(credited))
for r, v in sorted(credited.items()): print('  CREDIT', r, '<-', sorted(set(v))[:4])
