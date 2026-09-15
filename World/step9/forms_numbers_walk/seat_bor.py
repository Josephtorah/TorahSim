import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 14 — THE BORDERS (2026-09-12): SEAT the claims of the manifest into the draft unit as WITNESS_READ operators (sitting
# 9's rhythm: one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. Usage: seat_bor.py num_34_borders
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-12'
UID = sys.argv[1]
SPEC = {
 'num_34_borders': (34, 1, 29, [('MS34A-01', 1, 'this_is_the_land_that_shall_fall_to_you', 'the_one_command_without_expense'), ('MS34A-02', 3, 'the_south_side_from_zin_to_the_brook_of_egypt', 'judahs_border_is_the_lands_the_spies_walked_it'), ('MS34A-03', 6, 'the_west_border_the_great_sea', 'the_sea_as_the_direction'), ('MS34A-04', 7, 'the_north_border_marked_out_to_lebo_hamath', 'the_borders_own_verb_the_second_mount_hor'), ('MS34A-05', 11, 'the_east_border_down_to_the_salt_sea', 'the_blotting_verb_and_the_shoulder'), ('MS34A-06', 13, 'moses_commands_the_nine_and_a_half', 'one_tribe_noun_the_six_words_joshua_quotes'), ('MS34A-07', 16, 'eleazar_joshua_and_one_prince_from_a_tribe', 'the_distributive_doubling'), ('MS34A-08', 19, 'the_ten_princes_caleb_first', 'the_two_survivors_and_an_order_matching_no_other'), ('MS34A-09', 29, 'these_are_they_whom_the_lord_commanded', 'the_intensive_stem_that_runs_in_joshua'), ('MS34A-10', 13, 'the_parser_and_the_frames', 'three_numbers_read_twenty_verbs'), ('MS34A-11', 5, 'the_promised_extents_against_the_borders', 'no_river_no_euphrates'), ('MS34A-12', 2, 'onkelos_splits_and_merges', 'the_west_from_the_sea_the_brook_from_the_inheritance'), ('MS34A-13', 3, 'the_stores_glosses_read_back', 'fifty_nine_override_rows')],
   'the borders (34:1-29)'),
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
    name_en: "Numbers {CH}:{LO}-{HI} derivation {DATE} — THE NUMBERS WALK sitting 14, the borders"
    comment: >
      The walk's fourteenth reading, at the parashah grain (the portion Masei's
      second chapter as one draft — {WHAT}; the next draft opens at 35:1):
      Onkelos Numbers {CH}:{LO}-{HI} whole and fresh; the Sifrei on Numbers
      found BY POSITION to have NO piska on the chapter (158 on 31:22 is
      followed by 159 on 35:9 — the shelf silent from 31:25 to 35:8), the whole
      export scanned in both files for a row citing the chapter in four forms
      (the English "Bamidbar" and "Ibid.", the Hebrew chapter mark with the
      gershayim and the Hebrew "ibid."): one row of another chapter cites 34:2
      (1:2 — the one "command" that entails no expense), credited with a quick
      look (read whole at sitting 2). Ledger {UID}_{DATE}.md, coverage computed
      by script, the ink facts computed from the Tanakh DB and the snapshot
      store (every fact an assert — eighteen fell on the first typed pass, each
      retyped from the leg print, one on the second), the engine's numeral
      parser measured on every verse (three number verses, every one read; no
      gap), every quotation cut by consonants in glossed pieces (no cut miss;
      the lint clean on the first write). Seated as claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the four sides as a data row of named points against
      Joshua 15 and Ezekiel 47; the commission's daemon — the dividers by name,
      the register gate's Num 34 headers seat paid; the nine and a half by
      CALL into the second census's lot and the Gad runner's grant; the
      distributive doubling; Joshua 14:2's receipt outside the Torah) follows
      in its own sitting (World/step9/NUMBERS_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/{UID}_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
ci = set(re.findall(r'^(Onkelos Num \d+:\d+)$', led, re.M))
assert len(claims) == len(SEATS) == 13 and set(claims) == {s[0] for s in SEATS}, (sorted(claims), SEATS)
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
