#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 6 — CHAPTER 8 (2026-09-18, the one run): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch8.py <uid>.
# Sitting 5's form (seat_ch7.py).
import subprocess
import json, re, sys, yaml
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
DATE = '2026-09-18'
UID = sys.argv[1]
SPEC = {
 'deu_08_manna_humility': (8, 1, 20, [('DV08-01', 1, 'the_frame', 'all_the_commandment_that_you_may_live_and_possess_the_land'), ('DV08-02', 2, 'the_way_of_forty_years', 'the_humbling_the_manna_not_by_bread_alone_the_discipline_of_a_son'), ('DV08-03', 7, 'the_good_land', 'brooks_and_deeps_the_seven_species_iron_and_copper_eat_be_satisfied_bless'), ('DV08-04', 11, 'take_heed_lest_you_forget', 'the_houses_the_herds_the_silver_and_gold_the_heart_lifted_up'), ('DV08-05', 15, 'the_chain_and_the_covenant', 'who_led_you_who_fed_you_my_power_and_my_hand_the_covenant_established'), ('DV08-06', 19, 'the_testimony', 'if_you_forget_and_serve_other_gods_you_shall_surely_perish_like_the_nations')], 'the way of forty years and the good land (8:1-20)'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 6, chapter 8"
    comment: >
      The book's sixth reading, at the chapter's grain (chapter 8 as one
      draft — {WHAT}), ONE run under the two-run rule and every row whole
      under the whole-row rule: Onkelos Deuteronomy {CH}:{LO}-{HI} whole and
      fresh (the export's twenty rows the DB's twenty — the identity,
      asserted); THE SIFREI ON DEUTERONOMY SILENT ON THE CHAPTER (no piska
      head between 36 on 6:9 and 37 on 11:10) — its sixteen rows outside
      any piska citing chapter 8 read whole in both files (the Ekev piskaot
      on 11:10-12 quoting the Land's praise back at it; five read before
      and reread whole), the kin's spine (Numbers 11:4-9, 14:33-34,
      20:1-13, 21:4-9; the Mekhilta on Exodus 16-17) credited by name from
      the Numbers and Exodus ledgers. Ledger deu_08_ekev_{DATE}.md, coverage
      computed by script, the ink facts computed from the Tanakh DB and the
      snapshot store (every fact an assert — four fell on the first typed
      pass, forms not facts, retyped from the print), the engine's numeral
      parser measured on every verse (two number verses — "these forty
      years" [40] at 8:2 and 8:4; the sated verb starred at 8:10 and 8:12;
      no gap), the store's extra read-form token at 8:2 asserted as the
      chapter's one written/read pair and kept out of every check, every
      quotation cut by consonants (no miss). Seated as claims
      {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the blessing after the meal; the seven species; the
      manna and the humbling; the forty years as a state; the discipline;
      take heed lest; the heart lifted up; the exodus formula; the serpents
      and the rock; my power and the might of my hand; the covenant
      established; the testimony) follows in its own sitting
      (World/step9/DEUTERONOMY_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_08_ekev_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
