import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 12 — CHAPTER 14 (2026-09-21, the one run and its tail): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch14.py <uid>.
# Sitting 11's form (seat_ch13.py). RUN FROM THE REPO ROOT.
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-21'
UID = sys.argv[1]
SPEC = {
 'deu_14_food_tithe': (14, 1, 29, [('DV14-01', 1, 'the_children_and_the_cuts', 'you_are_children_of_the_lord_you_shall_not_cut_yourselves_nor_make_a_baldness_between_your_eyes_for_the_dead_a_holy_people_chosen_to_be_his_treasured_people'), ('DV14-02', 3, 'the_abomination_and_the_beasts', 'you_shall_not_eat_any_abomination_the_ox_the_sheep_the_goat_and_the_seven_wild_every_beast_that_parts_the_hoof_cleft_into_two_and_chews_the_cud_the_camel_the_hare_the_rock_badger_and_the_swine'), ('DV14-03', 9, 'the_water_and_the_birds', 'fins_and_scales_you_shall_eat_every_clean_bird_the_twenty_one_names_you_shall_not_every_swarming_thing_of_the_fowl_unclean_every_clean_fowl'), ('DV14-04', 21, 'the_carcass_and_the_kid', 'you_shall_not_eat_any_carcass_give_it_to_the_sojourner_within_your_gates_or_sell_it_to_a_foreigner_a_holy_people_you_shall_not_boil_a_kid_in_its_mothers_milk'), ('DV14-05', 22, 'the_tithe_at_the_place', 'tithe_you_shall_tithe_year_by_year_and_eat_before_the_lord_in_the_place_the_tithe_of_grain_wine_and_oil_and_the_firstlings_that_you_may_learn_to_fear_all_the_days'), ('DV14-06', 24, 'the_way_the_money_and_the_levite', 'when_the_way_is_too_long_and_the_place_too_far_turn_it_into_money_bind_the_money_in_your_hand_spend_it_on_whatever_your_soul_desires_eat_and_rejoice_you_and_your_household_the_levite_you_shall_not_forsake'), ('DV14-07', 28, 'the_third_year', 'at_the_end_of_three_years_bring_out_all_the_tithe_of_that_year_and_lay_it_up_within_your_gates_the_levite_the_sojourner_the_fatherless_and_the_widow_shall_eat_and_be_satisfied_that_the_lord_may_bless_you')],
  'the children of the LORD and the cuts for the dead, the abomination and the beasts with their two signs, the water and the birds, the carcass given to the sojourner and the kid in its mother\'s milk, the tithe eaten at the place, the way too long with the money and the Levite, the third year\'s tithe for the four at the gate'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 12, chapter 14"
    comment: >
      The book's twelfth reading, at the chapter's grain (chapter 14 as one
      draft — {WHAT}; no portion edge inside it — Re'eh holds it whole),
      ONE run to a clean compaction point after the rows and its tail under
      the cost rules, every row whole under the whole-row rule: Onkelos
      Deuteronomy {CH}:{LO}-{HI} whole and fresh (the export's twenty-nine rows
      the DB's twenty-nine — the identity, asserted); THE SIFREI ON
      DEUTERONOMY ON THE CHAPTER — fourteen piskaot 97-110 heading on the
      chapter's verses, not in verse order (98 on 14:6 before 99 on 14:3 and
      100 on 14:4; three piskaot on 14:6), and piska 96's rows 9-12 on 14:1
      left by chapter 13's sitting (96:10 folded in on its consonants):
      one hundred and eleven rows read whole in both files (two prior reads
      of two rows found in the earlier ledgers by computation and reread
      whole — the kid's three covenants at chapter 6, the firstling's year
      at chapter 12), three rows outside the spine citing the chapter read
      whole (flesh in milk at 12:23, reread whole from chapter 12; the bird's
      nest at 22:7; the LORD's portion at 32:9; none excluded), the kin
      (Leviticus 11 the twin chapter, 17:15, 19:10, 19:27-28, 20:26, 21:5,
      22:8, 23:22, 27:30-33; Exodus 22:30, 23:19; Numbers 18:20-32;
      Deuteronomy 7:6, 10:9, 10:18, 12:5-26) credited by name from the
      earlier ledgers. Ledger deu_14_reeh_{DATE}.md, coverage computed by
      script (143 sources), the ink facts computed from the Tanakh DB and
      the snapshot store (27 asserts fell on the first typed pass, every one
      the instrument's shape or a list typed from memory; green on the
      third), the engine's numeral parser measured on every verse (two
      number verses — 14:6 "two hoofs" [2], 14:28 "three years" [3]; the
      tithe's starred tokens at 14:22, 23, 28 marked and no number read; no
      gap), the store the DB at every verse (no written/read pair), every
      quotation cut by consonants (one miss retyped from the export).
      Seated as claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the beasts' and the birds' signs as cells with the birds'
      signs a parameter from the answer sheet; the carcass table with R.
      Judah's dissent; the kid's three readings; the second tithe's wall,
      House and year statuses; the money's form two arms; the removal's date
      a clock datum; the sojourner two persons; the tithe's liabilities)
      follows in its own sitting (World/step9/DEUTERONOMY_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_14_reeh_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
