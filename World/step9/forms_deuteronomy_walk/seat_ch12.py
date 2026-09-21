import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12 (2026-09-20, the one run and its tail): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch12.py <uid>.
# Sitting 9's form (seat_ch11.py).
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-20'
UID = sys.argv[1]
SPEC = {
 'deu_12_place_name': (12, 1, 31, [('DV12-01', 1, 'the_header_and_the_demolition', 'these_are_the_statutes_and_the_judgments_destroy_you_shall_destroy_the_places_under_every_leafy_tree_not_so_to_the_lord'), ('DV12-02', 5, 'the_place_chosen', 'the_place_which_the_lord_will_choose_his_dwelling_you_shall_seek_the_offerings_brought_there_the_rest_and_the_inheritance_the_levite'), ('DV12-03', 13, 'the_burnt_offerings_only_there', 'take_heed_lest_in_every_place_you_see_in_one_of_your_tribes_all_that_i_command_you'), ('DV12-04', 15, 'the_profane_slaughter_the_blood_and_the_gates', 'slaughter_and_eat_flesh_as_the_gazelle_the_blood_like_water_you_may_not_eat_within_your_gates_the_household_the_levite_not_forsaken'), ('DV12-05', 20, 'the_border_enlarged_and_the_altar', 'as_he_has_spoken_let_me_eat_flesh_as_i_have_commanded_you_be_steadfast_the_blood_is_the_life_the_altar_observe_and_hear'), ('DV12-06', 29, 'the_nations_cut_off_and_the_abomination', 'when_the_lord_cuts_off_the_nations_lest_you_be_ensnared_how_did_they_serve_not_so_to_the_lord_the_children_burned')],
  'the header and the demolition, the place the LORD will choose with the offerings brought there and the rest and the inheritance, the burnt offerings only there, the profane slaughter with the blood poured like water and the gates, the border enlarged with the slaughter as commanded and the altar, the nations cut off and the abomination'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 10, chapter 12"
    comment: >
      The book's tenth reading, at the chapter's grain (chapter 12 as one
      draft — {WHAT}; no portion edge inside it — Re'eh holds it whole),
      ONE run and its tail under the cost rules and every row whole under
      the whole-row rule: Onkelos Deuteronomy {CH}:{LO}-{HI} whole and fresh (the
      export's thirty-one rows the DB's thirty-one — the identity,
      asserted; the English's 12:32 the DB's 13:1); THE SIFREI ON
      DEUTERONOMY ON THE CHAPTER — piskaot 59-81, twenty heading on the
      chapter's verses and three without a head citation (68, 73, 74)
      folded in on their consonants, one hundred and fifty-nine rows read
      whole in both files (five prior reads of four rows found in the
      earlier ledgers by computation and reread whole), seven rows outside
      the spine citing the chapter read whole (the rest as the Land, the
      firstling and the second tithe, the rejoicing, the Asherah not
      planted, the order of offerings, build anywhere, the blood's reward;
      none excluded), the kin's spine (Leviticus 17:1-16, Numbers 18:8-32,
      7:5 and 7:25-26, Leviticus 20:2-5 and 18:21, Numbers 33:52, Exodus
      23:24; Exodus 20:21 through the Mekhilta) credited by name from the
      earlier ledgers. Ledger deu_12_reeh_{DATE}.md, coverage computed by
      script (197 sources), the ink facts computed from the Tanakh DB and
      the snapshot store (121 asserts — five fell on the first typed pass,
      forms not facts, retyped from the print), the engine's numeral parser
      measured on every verse (one number verse, 12:14 "in one of" [1]; one
      starred token, 12:17's tithe; no ordinal; no gap), no written/read
      pair in the chapter, every quotation cut by consonants (no miss).
      Seated as claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the place a variable the run assigns — the stations of
      the high places; the slaughter law changed by a place; the receipt
      without the Name at 12:21; the demolition's decision tables; the
      blood four ways; the ladder of a fortiori on 12:17) follows in its
      own sitting (World/step9/DEUTERONOMY_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_12_reeh_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
