import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 11 — CHAPTER 13 (2026-09-21, the one run and its tail): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch13.py <uid>.
# Sitting 10's form (seat_ch12.py).
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-21'
UID = sys.argv[1]
SPEC = {
 'deu_13_seducers': (13, 1, 19, [('DV13-01', 1, 'the_header', 'all_the_word_that_i_command_you_keep_to_do_you_shall_not_add_to_it_nor_take_away_from_it'), ('DV13-02', 2, 'the_prophet_and_the_test', 'a_prophet_or_a_dreamer_of_a_dream_a_sign_or_a_wonder_let_us_go_after_other_gods_the_lord_is_testing_you_the_six_verbs_that_prophet_put_to_death_rebellion_purge_the_evil'), ('DV13-03', 7, 'the_inciter', 'your_brother_your_son_your_daughter_the_wife_of_your_bosom_your_friend_entices_you_in_secret_the_gods_of_the_peoples_round_about_not_consent_your_eye_shall_not_pity_your_hand_first_stone_him_all_israel_shall_hear_and_fear'), ('DV13-04', 13, 'the_city_heard_of_the_inquiry_and_the_sword', 'in_one_of_your_cities_sons_of_belial_have_drawn_away_its_inhabitants_inquire_and_search_and_ask_diligently_true_and_certain_smite_with_the_edge_of_the_sword_devote_it_and_its_cattle'), ('DV13-05', 17, 'the_whole_offering_the_heap_and_the_mercy', 'gather_its_spoil_into_its_street_burn_it_wholly_to_the_lord_a_heap_forever_not_built_again_nothing_of_the_devoted_thing_shall_cleave_to_your_hand_the_fierceness_of_his_anger_mercy_multiply_you_as_he_swore'), ('DV13-06', 19, 'the_footer', 'when_you_hearken_to_the_voice_of_the_lord_your_god_to_keep_all_his_commandments_to_do_the_right_in_the_eyes_of_the_lord')],
  'the header (all the word — nothing added nor taken away), the prophet and the test, the inciter, the city heard of with the inquiry and the sword, the whole offering with the heap and the mercy, the footer'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 11, chapter 13"
    comment: >
      The book's eleventh reading, at the chapter's grain (chapter 13 as one
      draft — {WHAT}; no portion edge inside it — Re'eh holds it whole),
      ONE run and its tail under the cost rules and every row whole under
      the whole-row rule: Onkelos Deuteronomy {CH}:{LO}-{HI} whole and fresh (the
      export's nineteen rows the DB's nineteen — the identity, asserted;
      the English's 12:32 the DB's 13:1); THE SIFREI ON DEUTERONOMY ON THE
      CHAPTER — piskaot 82-96, fourteen heading on the chapter's verses and
      one without a head citation (88) folded in on its consonants,
      ninety-seven rows read whole in both files (piska 96's last four rows
      are 14:1's and wait for chapter 14's sitting — never read ahead; two
      prior reads of two rows found in the earlier ledgers by computation
      and reread whole), six rows outside the spine citing the chapter read
      whole (Belial at 15:9, the inquiry at 17:4, the rebellion at 19:16,
      the inquiry at 19:17-18; none excluded), the kin (Exodus 22:19 and
      32:1-8; Leviticus 20:2, 20:27, 24:14-23, 27:28-29; Numbers 15:30-36,
      21:2-3, 25:4; Deuteronomy 4:2, 5:6, 6:13-14, 7:2-26, 8:2-16, 10:20,
      11:22-28, 12:25-28) credited by name from the earlier ledgers. Ledger
      deu_13_reeh_{DATE}.md, coverage computed by script (122 sources), the
      ink facts computed from the Tanakh DB and the snapshot store (green on
      the first typed pass), the engine's numeral parser measured on every
      verse (one number verse, 13:13 "in one of your cities" [1]; no
      starred token; no gap), the written/read pair at 13:16 ("that city"
      — the store carries both forms, the chapter's one ketiv), every
      quotation cut by consonants (no miss).
      Seated as claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the prophet's test and the inciter's hand as cells; the
      condemned city's decision table; the ban's status; the purge formula's
      first seat; the seducers' one formula at three cases) follows in its
      own sitting (World/step9/DEUTERONOMY_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_13_reeh_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
