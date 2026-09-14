#!/usr/bin/env python3
# THE NUMBERS WALK sitting 15 — THE REFUGE CITIES (2026-09-13): SEAT the claims of the manifest into the draft unit as WITNESS_READ operators
# (sitting 9's rhythm: one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names),
# append derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last)
# before the ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is
# the manifest's own claim_en, so the operator and the claim cannot drift apart. Usage: seat_ref.py num_35_refuge_cities
import json, re, sys, yaml
ROOT = '<repo-old>'
DATE = '2026-09-13'
UID = sys.argv[1]
SPEC = {
 'num_35_refuge_cities': (35, 1, 34, [('MS35A-01', 1, 'the_levite_cities_and_their_measure', 'forty_eight_from_the_wall_a_thousand_and_two_thousand'), ('MS35A-02', 9, 'the_refuge_law_when_you_cross', 'six_cities_for_the_unwitting_slayer'), ('MS35A-03', 16, 'the_murderer_by_iron_stone_wood_hatred_enmity', 'the_avenger_of_blood_puts_him_to_death'), ('MS35A-04', 22, 'the_unwitting_suddenly_without_enmity', 'the_congregation_judges_between_smiter_and_avenger'), ('MS35A-05', 25, 'the_term_until_the_high_priests_death', 'outside_the_border_the_avenger_has_no_blood'), ('MS35A-06', 29, 'a_statute_of_judgment_by_witnesses', 'one_witness_shall_not_testify'), ('MS35A-07', 31, 'no_ransom_for_the_murderer_or_the_fugitive', 'the_goring_oxs_ransom_the_contrast'), ('MS35A-08', 33, 'the_land_polluted_by_blood_atoned_by_blood', 'in_whose_midst_i_dwell'), ('MS35A-09', 5, 'the_parser_the_frames_the_register', 'the_bare_dual_thousand_unread'), ('MS35A-10', 9, 'the_sifrei_returns_and_its_duplicated_block', 'the_rows_defects_and_moves'), ('MS35A-11', 14, 'the_twin_specs_on_the_tokens', 'joshua_twenty_quotes_the_spec'), ('MS35A-12', 19, 'onkelos_supplies_the_court_the_dual_the_presence', 'one_word_for_refuge_one_for_the_killer'), ('MS35A-13', 34, 'the_chapters_closes_and_the_books', 'the_inclusio_with_five_three_and_the_colophon'), ('MS35A-14', 12, 'the_stores_glosses_read_back', 'one_hundred_and_fifty_two_override_rows')],
   'the refuge cities (35:1-34)'),
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
    name_en: "Numbers {CH}:{LO}-{HI} derivation {DATE} — THE NUMBERS WALK sitting 15, the refuge cities"
    comment: >
      The walk's fifteenth reading, at the parashah grain (the portion Masei's
      third chapter as one draft — {WHAT}; the next unit, 36:1-13, frozen at
      THE TENT — the walk's last reading in Numbers): Onkelos Numbers
      {CH}:{LO}-{HI} whole and fresh; THE SIFREI ON NUMBERS RETURNS at 35:9 —
      piskaot 159-161 found BY POSITION (the export's last three; sixteen rows
      at the English file's grain, each read in both files; the Hebrew file's
      four extra rows at 160 are 161:1-4 duplicated — a defect class new to
      the walk; the rows' own defects read to their verses), two rows of
      another piska citing the chapter credited with a quick look. Ledger
      {UID}_{DATE}.md, coverage computed by script, the ink facts computed
      from the Tanakh DB and the snapshot store (every fact an assert — five
      fell on the first typed pass, each retyped from the leg print, none on
      the second), the engine's numeral parser measured on every verse (seven
      number verses read; ONE GAP — 35:5's bare dual "two thousand" four times
      unread, the class named for the compile), every quotation cut by
      consonants (no cut miss; the lint 18 → 0 inside the writing step).
      Seated as claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the bare dual taught to the parser; the Levite cities and
      the refuge cities as the law's tables; the murderer and the manslayer
      as one root's four agents; the high priest's death as a timer keyed to
      the office; the ransom refused twice and the land's atonement; the
      register gate with nothing to pay) follows in its own sitting
      (World/step9/NUMBERS_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/{UID}_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
ci = set(re.findall(r'^(Onkelos Num \d+:\d+|Sifrei Bamidbar \d+:\d+)$', led, re.M))
assert len(claims) == len(SEATS) == 14 and set(claims) == {s[0] for s in SEATS}, (sorted(claims), SEATS)
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
