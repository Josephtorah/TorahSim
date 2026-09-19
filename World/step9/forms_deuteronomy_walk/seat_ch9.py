import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 7 — CHAPTER 9 (2026-09-19, the one run): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch9.py <uid>.
# Sitting 6's form (seat_ch8.py).
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-19'
UID = sys.argv[1]
SPEC = {
 'deu_09_not_righteousness': (9, 1, 29, [('DV09-01', 1, 'not_for_your_righteousness', 'the_nations_greater_the_consuming_fire_the_word_sworn_the_stiff_neck'), ('DV09-02', 7, 'the_calf_retold', 'the_first_forty_days_the_tablets_of_the_covenant_the_finger_of_God_let_me_alone'), ('DV09-06', 12, 'the_retelling_on_the_tape', 'the_calf_the_forty_days_the_tablets_the_provocations_the_prayer_owed_to_the_compile'), ('DV09-03', 15, 'the_breaking', 'the_second_forty_days_aarons_peril_the_calfs_dust'), ('DV09-04', 22, 'the_four_provocations', 'taberah_massah_kibroth_hattaavah_kadesh_barnea'), ('DV09-05', 25, 'the_intercession', 'your_people_and_your_inheritance_remember_your_servants_lest_the_land_say')], 'not for your righteousness, the calf retold in Moses\' first person, the four provocations, the intercession'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 7, chapter 9"
    comment: >
      The book's seventh reading, at the chapter's grain (chapter 9 as one
      draft — {WHAT}), ONE run under the two-run rule and every row whole
      under the whole-row rule: Onkelos Deuteronomy {CH}:{LO}-{HI} whole and
      fresh (the export's twenty-nine rows the DB's twenty-nine — the
      identity, asserted); THE SIFREI ON DEUTERONOMY SILENT ON THE CHAPTER
      (no piska head between 36 on 6:9 and 37 on 11:10) — its seven rows
      outside any piska citing chapter 9 read whole in both files (the
      prayer's ten names, the door opened, the forty days as suffering,
      the hyperbole rule, the harsh words, the breaking among the wonders;
      four read before and reread whole), the kin's spine (Exodus 24:12-18,
      31:18, 32, 34:1-4 and 28; Numbers 11:1-3, 31-35, 13-14, 20:24)
      credited by name from the Exodus and Numbers ledgers. Ledger
      deu_09_ekev_{DATE}.md, coverage computed by script, the ink facts
      computed from the Tanakh DB and the snapshot store (every fact an
      assert — eighteen fell on the first typed pass, forms not facts,
      retyped from the print), the engine's numeral parser measured on
      every verse (seven number verses — the forty days and nights [40, 40]
      at 9:9, 11, 18, 25, the two tablets [2] and the two hands; "swore"
      no number; no gap), no written/read pair in the chapter, every
      quotation cut by consonants (no miss). Seated as claims
      {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the readback's rows of the calf against Exodus 32, 24,
      31 and 34; Aaron's peril told only here; the three forties and their
      dates; the four provocations; the intercession's second telling;
      the stiff neck as a state; a new checkpoint series) follows in its
      own sitting (World/step9/DEUTERONOMY_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_09_ekev_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
