import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 9 — CHAPTER 11 (2026-09-20, the one run): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch11.py <uid>.
# Sitting 8's form (seat_ch10.py).
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-20'
UID = sys.argv[1]
SPEC = {
 'deu_11_bless_curse_set': (11, 1, 32, [('DV11-01', 1, 'the_discipline_your_children_have_not_seen', 'love_the_lord_keep_his_charge_egypt_the_sea_the_wilderness_dathan_and_abiram_your_eyes_have_seen'), ('DV11-02', 8, 'the_land_watered_by_heaven', 'keep_all_the_commandment_milk_and_honey_not_like_egypt_the_rain_of_heaven_the_eyes_of_the_lord_always'), ('DV11-03', 13, 'the_second_paragraph', 'if_you_hearken_the_rain_in_its_season_lest_the_heavens_shut_the_frontlets_the_sons_the_doorposts_the_days_of_heaven'), ('DV11-04', 22, 'the_borders_and_the_dread', 'keep_and_cleave_the_nations_dispossessed_every_place_your_foot_treads_no_man_shall_stand_as_he_spoke'), ('DV11-06', 25, 'the_retelling_and_the_laws_on_the_tape', 'the_discipline_retold_the_rain_conditional_a_new_cell_the_frontlets_by_call_the_borders_the_receipt_gerizim_and_ebal_owed_to_the_compile'), ('DV11-05', 26, 'the_blessing_and_the_curse_gerizim_and_ebal', 'see_a_blessing_and_a_curse_gerizim_and_ebal_opposite_gilgal_the_terebinths_of_moreh_possess_it_and_dwell_in_it')],
  'the discipline your children have not seen, the land watered by heaven, the second paragraph of the Shema with the rain conditional and the frontlets, the borders and the dread, the blessing and the curse set on Gerizim and Ebal'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 9, chapter 11"
    comment: >
      The book's ninth reading, at the chapter's grain (chapter 11 as one
      draft — {WHAT}; the portion edge Ekev / Re'eh at 11:25-26 inside it),
      ONE run under the two-run rule and every row whole under the
      whole-row rule: Onkelos Deuteronomy {CH}:{LO}-{HI} whole and fresh (the
      export's thirty-two rows the DB's thirty-two — the identity,
      asserted); THE SIFREI ON DEUTERONOMY ON THE CHAPTER for the first
      time since chapter 6 — piskaot 37-58 heading on 11:10-32 (piska 45
      without a head citation, the spine's by its opening words), one
      hundred and seventy-one rows read whole in both files (forty-one
      prior reads of thirty-seven rows found in the earlier ledgers by
      computation and reread whole), seven rows outside the spine citing
      the chapter read whole (the frontlets' four compartments and the
      doorposts' two plurals from chapter 6's piskaot, the sages at the
      border, the song's heavens shut; 234:6 excluded — the English's slip
      for 22:12), the kin's spine (Numbers 16 on Dathan and Abiram, 6:4-9,
      8:7-10, Exodus 23:27-31, Leviticus 26:3-5 and 19-20; the sea and the
      frontlets through the Mekhilta) credited by name from the earlier
      ledgers. Ledger deu_11_ekev_reeh_{DATE}.md, coverage computed by
      script (210 sources), the ink facts computed from the Tanakh DB and
      the snapshot store (166 asserts — ten fell on the first typed pass,
      forms not facts, retyped from the print), the engine's numeral parser
      measured on every verse (no number verse, no ordinal; "swore" no
      number; one starred token at 11:15; no gap), no written/read pair in
      the chapter, every quotation cut by consonants (no miss). Seated as
      claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the readback's rows of the discipline against Exodus 14
      and Numbers 16; the rain conditional a new cell with Leviticus 26 by
      CALL; the frontlets and the doorposts by 6:8-9's cell; the borders
      by Numbers 34; the receipt at 11:25 pointed at Exodus 23:27; Gerizim
      and Ebal by chapter 27's ceremony) follows in its own sitting
      (World/step9/DEUTERONOMY_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_11_ekev_reeh_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
