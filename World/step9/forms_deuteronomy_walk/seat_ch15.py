import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13 — CHAPTER 15 (2026-09-22, two runs and the tail): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch15.py <uid>.
# Sitting 12's form (seat_ch14.py). RUN FROM THE REPO ROOT.
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-22'
UID = sys.argv[1]
SPEC = {
 'deu_15_release_firstborn': (15, 1, 23, [('DV15-01', 1, 'the_release', 'at_the_end_of_seven_years_you_shall_make_a_release_every_creditor_shall_release_the_loan_of_his_hand_the_foreigner_you_may_exact_your_hand_shall_release'), ('DV15-02', 4, 'the_needy_and_the_blessing', 'there_shall_be_no_needy_among_you_for_the_lord_will_surely_bless_you_if_you_hearken_you_shall_lend_to_many_nations_and_not_borrow_rule_and_not_be_ruled'), ('DV15-03', 7, 'the_hand_opened', 'if_there_be_a_needy_one_of_your_brothers_do_not_harden_your_heart_nor_shut_your_hand_open_you_shall_open_lend_him_sufficient_for_his_need_beware_lest_the_year_of_release_draws_near_give_you_shall_give_the_needy_shall_never_cease'), ('DV15-04', 12, 'the_hebrew_slave', 'if_your_brother_a_hebrew_man_or_woman_be_sold_to_you_six_years_and_in_the_seventh_free_not_empty_furnish_you_shall_furnish_him_remember_that_you_were_a_slave_in_egypt'), ('DV15-05', 16, 'the_awl_and_the_double_hire', 'if_he_says_i_will_not_go_out_the_awl_through_his_ear_into_the_door_a_servant_for_ever_likewise_to_your_maidservant_double_the_hire_of_a_hireling'), ('DV15-06', 19, 'the_firstling', 'every_firstling_male_of_herd_and_flock_you_shall_sanctify_no_work_no_shearing_eat_it_before_the_lord_year_by_year_at_the_place'), ('DV15-07', 21, 'the_blemish_and_the_blood', 'if_it_has_a_blemish_lame_or_blind_you_shall_not_sacrifice_it_eat_it_within_your_gates_the_unclean_and_the_clean_alike_only_its_blood_pour_on_the_ground_as_water')],
  'the release of debts at the end of seven years with the foreigner exacted, the needy who shall not be and shall never cease with the blessing on hearkening, the hand opened and the base thought barred, the Hebrew slave freed in the seventh year and furnished from the flock, the floor and the press, the awl through the ear into the door and the double hire, the firstling sanctified and eaten year by year at the place, the blemished eaten in the gates and the blood poured as water'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 13, chapter 15"
    comment: >
      The book's thirteenth reading, at the chapter's grain (chapter 15 as one
      draft — {WHAT}; no portion edge inside it — Re'eh holds it whole),
      TWO runs to two clean compaction points and the tail under the cost
      rules, every row whole under the whole-row rule: Onkelos
      Deuteronomy {CH}:{LO}-{HI} whole and fresh (the export's twenty-three rows
      the DB's twenty-three — the identity, asserted); THE SIFREI ON
      DEUTERONOMY ON THE CHAPTER — sixteen piskaot 111-126 heading on the
      chapter's verses in verse order, no tail folded in (110's rows chapter
      14's, 126's stopping before 16:1): ninety-nine rows read whole in both
      files (two prior reads of two rows found in the earlier ledgers by
      computation and reread whole — the base thought at chapter 13, the wife
      by "for him" at Genesis 2), ten rows outside the spine citing the
      chapter read whole (six reread whole from chapters 11, 12 and 14 — the
      release after the conquest, the permanent blemish and the one dish, the
      firstling's year, the end at Booths; the blemishes at 17:1, the
      hireling's cry at 24:15 and Moses' righteousness at 33:21 fresh; none
      excluded), the kin (Leviticus 25's sabbatical, poor brother and sold
      brother; Leviticus 22:17-27 and 21:16-23; Leviticus 27:26 and Numbers
      18:15-18; Deuteronomy 12:6, 15-18, 22-24, 14:28-29 and 5:15) credited
      by name from the earlier ledgers. Ledger deu_15_reeh_{DATE}.md,
      coverage computed by script (132 sources), the ink facts computed from
      the Tanakh DB and the snapshot store (3 asserts fell on the first typed
      pass, every one the instrument's shape; green on the second), the
      engine's numeral parser measured on every verse (four number verses —
      15:1 "seven years" [7], 15:7 "one of your gates" [1], 15:12 and 15:18
      "six years" [6]; one ordinal — 15:9 "the seventh" [7]; no gap), the
      store the DB at every verse (no written/read pair), every quotation cut
      by consonants (nine misses retyped from the export's own spellings).
      Seated as claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the release as an effect on the debts with its onset and
      territory parameters and the prozbul's procedure from the answer sheet;
      the ranks of the poor a precedence parameter; the Hebrew slave's three
      cases, his exits and the gift; the awl's rite by day with the judges;
      the firstling's year of two days and the blemish's classes; the blood's
      clauses by call to chapter 12's cells) follows in its own sitting
      (World/step9/DEUTERONOMY_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_15_reeh_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
