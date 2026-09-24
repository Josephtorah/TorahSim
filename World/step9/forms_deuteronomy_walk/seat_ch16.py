import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 14 — CHAPTER 16 (LEAN, 2026-09-23): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch15.py <uid>.
# Sitting 13's form (seat_ch15.py). RUN FROM THE REPO ROOT.
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-23'
UID = sys.argv[1]
SPEC = {
 'deu_16_festivals_judges': (16, 1, 22, [('DV16-01', 1, 'the_month_of_aviv_and_the_passover', 'observe_the_month_of_aviv_and_keep_the_passover_for_by_night_he_brought_you_out_sacrifice_it_flock_and_herd_at_the_place_where_his_name_dwells'), ('DV16-02', 3, 'the_leaven_and_the_bread_of_affliction', 'eat_no_leaven_with_it_seven_days_unleavened_bread_of_affliction_for_in_haste_you_went_out_no_leaven_seen_in_your_border_none_of_the_flesh_left_until_morning'), ('DV16-03', 5, 'the_place_the_evening_and_the_seventh_day', 'not_within_your_gates_but_at_the_place_at_evening_at_sunset_the_season_of_your_going_out_cook_and_eat_and_turn_in_the_morning_six_days_and_a_solemn_assembly_on_the_seventh'), ('DV16-04', 9, 'the_weeks_from_the_sickle_and_the_feast_of_weeks', 'count_seven_weeks_from_the_sickle_on_the_standing_grain_keep_the_feast_of_weeks_with_the_measure_of_your_hand_rejoice_with_your_household_and_remember_the_slave'), ('DV16-05', 13, 'the_feast_of_booths', 'keep_the_feast_of_booths_seven_days_when_you_gather_in_rejoice_in_your_feast_seven_days_at_the_place_and_be_altogether_joyful'), ('DV16-06', 16, 'the_three_pilgrimages_and_the_gift_of_the_hand', 'three_times_a_year_all_your_males_shall_appear_at_the_three_feasts_and_none_empty_each_man_as_his_hand_gives'), ('DV16-07', 18, 'the_judges_and_officers', 'judges_and_officers_in_all_your_gates_tribe_by_tribe_righteous_judgment_no_wresting_no_respecting_of_persons_no_bribe_justice_justice_pursue_and_live_and_inherit'), ('DV16-08', 21, 'the_asherah_and_the_pillar', 'plant_no_asherah_of_any_tree_beside_the_altar_and_set_up_no_pillar_which_the_lord_your_god_hates')],
  'the month of Aviv observed and the Passover kept by night, sacrificed of flock and herd at the place; the leaven barred and the bread of affliction eaten seven days in haste\'s memory, no leaven seen in the border and none of the flesh kept to morning; the Passover not in the gates but at the place at evening, cooked and eaten there, the morning\'s return, six days and the seventh\'s assembly; the weeks counted from the sickle and the feast of weeks with the hand\'s measure, the household rejoicing and the slave remembered; the feast of booths seven days at the gathering, altogether joyful; the three pilgrimages of every male, none empty, each as his hand gives; the judges and officers in every gate tribe by tribe, the three prohibitions and the bribe, justice pursued for the land; the asherah and the pillar barred beside the altar'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 14, chapter 16, LEAN"
    comment: >
      The book's fourteenth reading, at the chapter's grain (chapter 16 as one
      draft — {WHAT}; a portion edge inside it — Re'eh ends at 16:17 and
      Shoftim opens at 16:18; the chapter the unit), THE FIRST SITTING OF THE
      LEAN PASS (ruled 2026-09-23): one reading window under the cost rules,
      every row whole under the whole-row rule: Onkelos Deuteronomy
      {CH}:{LO}-{HI} whole and fresh (the export's twenty-two rows the DB's
      twenty-two — the identity, asserted); THE SIFREI ON DEUTERONOMY ON THE
      CHAPTER — twenty piskaot 127-146 in verse order (nineteen heads in the
      chapter and 135 headless on 16:8, folded in by position; no tail folded
      in): one hundred and eleven rows read whole in both files (two prior
      reads found in chapter 12's ledger by computation and reread whole —
      the rejoicing by analogy, the asherah's a fortiori), three rows outside
      the spine citing the chapter read whole (52:4 and 147:2 reread whole
      from chapters 11 and 12 — the guard of the land, the order of
      offerings; 281:1 fresh — the sojourner's judgment), the kin (Leviticus
      23; Numbers 9, 28, 29; Exodus 23 and 34; Leviticus 19:15 and 26:1;
      Deuteronomy 1:16-17, 5:15, 7:5, 12, 15:15) credited by name from the
      earlier ledgers. Ledger deu_16_reeh_shoftim_{DATE}.md, coverage computed
      by script (136 sources), the ink facts computed from the Tanakh DB and
      the snapshot store (2 asserts fell on the first typed pass, both the
      instrument's shape; green on the second), the engine's numeral parser
      measured on every verse (eight number verses, two ordinals, one
      starred token; no gap), the store the DB at every verse, every
      quotation cut by consonants (three misses retyped from the print).
      Seated as claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The Mishnah rows the spine cites are the compile's cases (14b); the
      full process (the docket whole, the full records) OWED to this chapter
      under the lean pass (World/step9/COMPILE_DEBT.md's lean-pass box).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_16_reeh_shoftim_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
ci = set(re.findall(r'^(Onkelos Deut \d+:\d+|Sifrei Devarim \d+:\d+)$', led, re.M))
assert len(claims) == len(SEATS) and set(claims) == {s[0] for s in SEATS}, (sorted(claims), SEATS)
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
    sid = f'  - id: STEP_Dt_{CH}_{step}\n'
    i = txt.index(sid)
    j = txt.index('    comment: >\n', i)
    nxt = txt.find(f'\n  - id: STEP_Dt_{CH}_', i + 1)
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
    scen += f'  - id: S{n}\n    title_en: "after STEP_Dt_{CH}_{v} — Deut {CH}:{v}"\n    expect_en: "no test, no name."\n'
scen += f'  - id: S_last\n    title_en: "after STEP_Dt_{CH}_{HI} — Deut {CH}:{HI}"\n    expect_en: "no test, no name."\n'
txt = txt[:a] + scen + txt[b:]
open(unit, 'w', encoding='utf-8').write(txt)
d = yaml.safe_load(open(unit, encoding='utf-8'))
ops = [(s['id'], o) for s in d['boot_steps'] for o in s.get('operators', [])]
assert len(ops) == len(SEATS) and all(o['op'] == 'WITNESS_READ' for _, o in ops), len(ops)
assert d['derivation_log'][-1]['step'] == 'E' and len(d['boot_steps']) == HI - LO + 1
assert [s['id'] for s in d['scenarios']] == [f'S{n}' for n in range(1, len(firsts) + 1)] + ['S_last'] and all(s['expect_en'] == 'no test, no name.' for s in d['scenarios'])
print(f'{UID}: seated {len(ops)} operators on {len(by_step)} steps {sorted(by_step)}; scenarios {len(d["scenarios"])} in the anchor form')
