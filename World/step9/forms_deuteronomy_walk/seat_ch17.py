import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 15 — CHAPTERS 17-18 (LEAN, 2026-09-24): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch15.py <uid>.
# Sitting 14's form (seat_ch16.py) over two units. RUN FROM THE REPO ROOT.
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-24'
UID = sys.argv[1]
SPEC = {
 'deu_17_courts_king': (17, 1, 20, [('DV17-01', 1, 'the_blemished_offering', 'no_ox_or_sheep_with_a_blemish_any_evil_thing_for_it_is_an_abomination'), ('DV17-02', 2, 'the_idolater_in_the_gate', 'the_man_or_woman_who_serves_other_gods_inquired_well_stoned_at_the_gate_by_two_witnesses_or_three_the_witnesses_hand_first_the_evil_purged'), ('DV17-03', 8, 'the_high_court_at_the_place', 'the_hard_case_brought_up_to_the_priests_the_levites_and_the_judge_the_sentence_not_turned_from_the_rebel_dies_and_the_people_hear_and_fear'), ('DV17-04', 14, 'the_king', 'a_king_chosen_from_among_your_brothers_no_foreigner_no_horses_wives_or_gold_his_copy_of_the_law_read_all_his_days_his_heart_not_lifted')],
  'the blemished offering an abomination; the idolater in the gate inquired, stoned by two witnesses or three with the witnesses\' hand first and the evil purged; the hard case brought up to the high court at the place, its sentence not turned from and the rebel put to death; the king chosen from among the brothers with his three limits and his copy of the law'),
 'deu_18_levi_prophet': (18, 1, 22, [('DV18-01', 1, 'the_priests_portion_and_dues', 'no_portion_with_israel_the_fire_offerings_the_shoulder_cheeks_and_maw_the_firsts_of_grain_wine_oil_and_fleece_standing_to_minister'), ('DV18-02', 6, 'the_levite_from_the_gates', 'the_levite_who_comes_with_all_his_souls_desire_to_the_place_ministers_and_eats_portion_as_portion_besides_the_fathers_sales'), ('DV18-03', 9, 'the_diviners_barred', 'none_who_passes_through_the_fire_no_diviner_soothsayer_omen_reader_sorcerer_charmer_ghost_asker_or_necromancer_be_whole_with_the_lord'), ('DV18-04', 15, 'the_prophet_like_moses', 'a_prophet_from_among_the_brothers_as_asked_at_horeb_my_words_in_his_mouth_the_presumptuous_prophet_dies_the_word_tested_by_its_coming')],
  'the priests\' portion the fire offerings and their dues the shoulder, the cheeks and the maw and the firsts; the Levite from the gates ministering at the place portion as portion; the diviners\' nine barred and Israel whole with the LORD; the prophet like Moses raised as asked at Horeb, the false prophet dying and the word tested by its coming'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 15, chapters 17-18, LEAN"
    comment: >
      The book's fifteenth reading, at the chapter's grain (chapter {CH} as one
      draft — {WHAT}; no portion edge inside it — Shoftim 16:18-21:9 holds
      the two chapters whole; two chapters read at one sitting, two units,
      one ledger), THE THIRD SITTING OF THE LEAN PASS (ruled 2026-09-23):
      one reading window under the cost rules, every row whole under the
      whole-row rule: Onkelos Deuteronomy {CH}:{LO}-{HI} whole and fresh (the
      export's rows the DB's — the identity, asserted); THE SIFREI ON
      DEUTERONOMY ON THE TWO CHAPTERS — thirty-two piskaot 147-178 in verse
      order (sixteen heads in each chapter, none headless, no tail folded
      in): one hundred and eighty-one rows read whole in both files (seven
      prior reads found in the earlier ledgers by computation and reread
      whole — the order of offerings, the blemish's class, the host of
      heaven apportioned, the seven investigations, the calf cut in two),
      eleven rows outside the spine citing the chapters read whole (six
      reread whole from chapters 11-14; five fresh — the witnesses male, the
      blemished priest's blessing, the dog's price, the Temple's height
      twice), the kin (Leviticus 7, 19, 20, 22; Numbers 18, 22, 23, 35;
      Exodus 22; Deuteronomy 1, 4, 5, 10, 12, 13, 14, 15) credited by name
      from the earlier ledgers. Ledger deu_17_18_shoftim_{DATE}.md, coverage
      computed by script (234 sources over the two chapters), the ink facts
      computed from the Tanakh DB and the snapshot store (1 assert fell on
      the first typed pass — a fact the print corrected; green on the
      second), the engine's numeral parser measured on every verse (two
      number verses in chapter 17, none in 18; no ordinal; "from one" at
      18:6 unread behind its prefix), the store the DB at every verse, every
      quotation cut by consonants (four misses retyped from the print at
      once). Seated as claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The Mishnah rows the spine cites are the compile's cases (15b); the
      full process (the docket whole, the full records) OWED to these
      chapters under the lean pass (World/step9/COMPILE_DEBT.md's lean-pass box).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_17_18_shoftim_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
