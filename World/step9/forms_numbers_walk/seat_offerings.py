#!/usr/bin/env python3
# THE NUMBERS WALK sitting 9 — THE OFFERINGS CALENDAR (2026-09-11): SEAT the claims of one manifest into its draft unit as WITNESS_READ operators
# (sitting 8's rhythm, seat_census.py: one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the
# ledger's own names), append derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six
# verses + its last) before the ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded
# after. The prose is the manifest's own claim_en, so the operator and the claim cannot drift apart. Usage: seat_offerings.py <uid>
import json, re, sys, yaml
ROOT = '<repo-old>'
DATE = '2026-09-11'
UID = sys.argv[1]
SPEC = {
 'num_28_daily_shabbat_rosh': (28, 1, 15, [('PN28A-01', 1, 'the_lord_spoke_command', 'my_offering_my_bread_in_its_appointed_time'), ('PN28A-02', 3, 'two_per_day', 'the_one_lamb_the_second_lamb_exodus_29_restated'), ('PN28A-03', 5, 'the_tenth_of_the_ephah', 'wheat_beaten_oil_three_seahs'), ('PN28A-04', 6, 'made_at_mount_sinai', 'strong_drink_the_morning_meal_offering_the_name_on_every_offering'), ('PN28A-05', 9, 'the_sabbaths_two_lambs', 'on_its_sabbath_the_service_overrides'), ('PN28A-06', 11, 'the_new_moons_register', 'the_master_table_the_hins_marks_in_its_month'), ('PN28A-07', 15, 'the_goat_to_the_lord', 'the_grave_of_the_deep')],
   'the tamid, the Sabbath and the new moon (28:1-15)'),
 'num_28_pesach_shavuot': (28, 16, 31, [('PN28B-01', 16, 'pesach_the_fourteenth', 'leviticus_23_at_its_second_seat_the_five_grains'), ('PN28B-02', 19, 'the_festival_table', 'one_and_seven_read_eight_the_accent_gap'), ('PN28B-03', 20, 'the_meal_offering_and_the_goat', 'besides_the_stack'), ('PN28B-04', 24, 'as_these_each_day', 'pesach_constant_sukkot_declining'), ('PN28B-05', 26, 'the_day_of_the_firstfruits', 'in_your_weeks_onkelos_atzeret'), ('PN28B-06', 27, 'shavuots_second_table', 'leviticus_23_18_reversed_the_bar'), ('PN28B-07', 31, 'unblemished_and_their_libations', 'the_libations_likened')],
   'Pesach and the day of the firstfruits (28:16-31)'),
 'num_29_fall_festivals': (29, 1, 39, [('PN29A-01', 1, 'the_day_of_blowing', 'the_tishri_table_the_three_layer_stack'), ('PN29A-02', 7, 'the_tenth_day', 'the_plene_tenth_silent_afflict_any_work_the_sin_offering_of_the_atonements'), ('PN29A-03', 12, 'the_fifteenth_day', 'thirteen_bulls_the_table_multiplied'), ('PN29A-04', 16, 'the_seven_days', 'seventy_bulls_the_pointer_line_seven_times'), ('PN29A-05', 19, 'the_water_libation', 'three_letters_verified'), ('PN29A-06', 35, 'the_eighth_day', 'assembly_on_two_festivals_a_festival_of_its_own'), ('PN29A-07', 39, 'the_calendars_footer', 'besides_your_vows_and_moses_said')],
   'the seventh month (29:1-39)'),
}
CH, LO, HI, SEATS, WHAT = SPEC[UID]
claims = {c['id']: c for c in json.load(open(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json', encoding='utf-8'))}
TITLES = {cid: c['claim_en'].split('. ')[0].rstrip('.') for cid, c in claims.items()}

def wrap(prose, indent=10):
    lines, cur = [], ''
    for w in prose.split(' '):
        if len(cur) + len(w) + 1 > 78 - indent and cur: lines.append(cur); cur = w
        else: cur = (cur + ' ' + w) if cur else w
    lines.append(cur)
    return '\n'.join(' ' * indent + l for l in lines)
def q(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

def STEP_E(ids):
    return f'''
  - step: E
    name_en: "Numbers {CH}:{LO}-{HI} derivation {DATE} — THE NUMBERS WALK sitting 9, the offerings calendar"
    comment: >
      The walk's ninth reading, at the parashah grain (the portion Pinchas's
      remainder 28:1-29:39 read in one pass as three drafts — {WHAT}; the
      portion's last verse 30:1 opens the next draft and is read with it;
      chapter 27 frozen at THE TENT and skipped): Onkelos Numbers {CH}:{LO}-{HI}
      whole and fresh; the Sifrei on Numbers piskaot found BY POSITION (eleven
      on the two chapters, twenty-three rows; no piska on 29:1-11 or 29:13-34,
      computed on every head; the rows' own defects read to their verses —
      RESEARCH_LOG.md). Ledger {UID}_{DATE}.md, coverage computed by script, the
      ink facts computed from the Tanakh DB and the snapshot store (every fact
      an assert — four fell on the first typed pass, each an index or a count),
      every number by the engine's own numeral parser (fifty-four number verses
      in the two chapters, right at every one but 28:19 — the etnachta on "one"
      before "and seven"; and the plene "tenth" of 29:7 silent — two gaps named
      for the compile), every quotation cut by consonants in glossed pieces,
      the formulaic rows built from the tokens. Seated as claims
      {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the calendar as one table with the master row cited by
      pointer; the two parser gaps taught; the water libation's letters as a
      checked row; the seventy bulls; the stacks on the tamid; Leviticus 23 by
      CALL) follows in its own sitting (World/step9/NUMBERS_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/{UID}_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
ci = set(re.findall(r'^(Sifrei Bamidbar \d+:\d+|Onkelos Num \d+:\d+)$', led, re.M))
assert len(claims) == len(SEATS) == 7 and set(claims) == {s[0] for s in SEATS}, (sorted(claims), SEATS)
txt = open(unit, encoding='utf-8').read()
assert 'operators:' not in txt, 'the draft already carries operators'
by_step = {}
for cid, step, anchor, name in SEATS:
    assert LO <= step <= HI and re.fullmatch(r'[\w-]+', anchor) and re.fullmatch(r'[\w-]+', name), (cid, step, anchor, name)
    cites = claims[cid]['source'].split('; ')
    for c in cites: assert c in ci, (cid, c)
    prose = f"{TITLES[cid]} [claim {cid}]. {claims[cid]['claim_en']}"
    by_step.setdefault(step, []).append((anchor, name, cites, prose))
for step, ops in by_step.items():
    sid = f'  - id: STEP_Nm_{CH}_{step}\n'
    i = txt.index(sid)
    j = txt.index('    comment: >\n', i)
    nxt = txt.find(f'\n  - id: STEP_Nm_{CH}_', i + 1)
    assert nxt == -1 or j < nxt, step
    block = '    operators:\n'
    for anchor, name, cites, prose in ops:
        block += ('      - op: WITNESS_READ\n'
                  f'        expr_en: "WITNESS-READ({anchor}, {name})"\n'
                  '        en: >\n' + wrap(prose) + '\n'
                  '        cites: [' + ', '.join(q(c) for c in cites) + ']\n'
                  '        confidence: witnessed\n')
    txt = txt[:j] + block + txt[j:]
k = txt.index('\nboot_steps:\n')
txt = txt[:k] + STEP_E([s[0] for s in SEATS]) + txt[k:]
a = txt.index('\nscenarios:\n'); b = txt.index('\nbinary_trees:', a)
scen = '\nscenarios:\n'
firsts = list(range(LO, min(LO + 6, HI + 1)))
for n, v in enumerate(firsts, 1):
    scen += f'  - id: S{n}\n    title_en: "after STEP_Nm_{CH}_{v} — Num {CH}:{v}"\n    expect_en: "no test, no name."\n'
scen += f'  - id: S_last\n    title_en: "after STEP_Nm_{CH}_{HI} — Num {CH}:{HI}"\n    expect_en: "no test, no name."\n'
txt = txt[:a] + scen + txt[b:]
open(unit, 'w', encoding='utf-8').write(txt)
d = yaml.safe_load(open(unit, encoding='utf-8'))
ops = [(s['id'], o) for s in d['boot_steps'] for o in s.get('operators', [])]
assert len(ops) == len(SEATS) and all(o['op'] == 'WITNESS_READ' for _, o in ops), len(ops)
assert d['derivation_log'][-1]['step'] == 'E' and len(d['boot_steps']) == HI - LO + 1
assert [s['id'] for s in d['scenarios']] == [f'S{n}' for n in range(1, len(firsts) + 1)] + ['S_last'] and all(s['expect_en'] == 'no test, no name.' for s in d['scenarios'])
print(f'{UID}: seated {len(ops)} operators on {len(by_step)} steps {sorted(by_step)}; scenarios {len(d["scenarios"])} in the anchor form')
