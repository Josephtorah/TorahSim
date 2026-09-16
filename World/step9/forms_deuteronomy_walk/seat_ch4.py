import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 2 — CHAPTER 4 (2026-09-16): SEAT the claims of the two manifests into the two draft units as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch4.py <uid>.
# Sitting 1's form (seat_deu.py).
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-16'
UID = sys.argv[1]
SPEC = {
 'deu_04_obey_horeb': (4, 1, 40, [('DV04A-01', 1, 'the_exhortation', 'hear_the_statutes_add_nothing_take_nothing'), ('DV04A-02', 9, 'horeb_retold', 'a_voice_of_words_and_no_form'), ('DV04A-03', 15, 'no_image', 'the_form_of_any_figure_the_host_apportioned'), ('DV04A-04', 25, 'the_exile_and_the_return', 'heaven_and_earth_witness_seek_and_find'), ('DV04A-05', 32, 'the_one_god', 'you_were_shown_the_lord_is_god_none_else')], 'the exhortation, Horeb retold, no image, the exile and the return, the one God (4:1-40)'),
 'deu_04_refuge_east': (4, 41, 49, [('DV04B-01', 41, 'the_three_cities', 'then_moses_set_apart_bezer_ramoth_golan'), ('DV04B-02', 44, 'the_frame', 'this_is_the_torah_the_testimonies_moses_spoke')], 'the three cities and the frame (4:41-49)'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 2, chapter 4"
    comment: >
      The book's second reading, at the chapter's grain (chapter 4 as two
      drafts — this unit {WHAT}): Onkelos Deuteronomy {CH}:{LO}-{HI} whole and
      fresh; THE SIFREI ON DEUTERONOMY has NO PISKA on the chapter (30 on
      3:29, 31 on 6:4) — its eight rows citing chapter 4 found by the scan
      of the whole export in both files, six read fresh (48:2, 49:2, 148:8,
      301:21, 306:1, 323:1), two credited from sitting 1 (30:2, 37:9).
      Ledger deu_04_vaetchanan_{DATE}.md (one ledger for the two drafts),
      coverage computed by script, the ink facts computed from the Tanakh DB
      and the snapshot store (every fact an assert — six fell on the first
      typed pass, retyped from the leg print, none on the second), the
      engine's numeral parser measured on every verse (four number verses
      read, no gap), every quotation cut by consonants (no cut miss; the
      lint 0). Seated as claims {ids[0]}..{ids[-1][-2:]}:
      {'; '.join(TITLES[i].lower() for i in ids)}. The compile (the
      chapter's one law and one case; the three cities closing the refuge
      runner's debit; the receipt at 4:5 paying the register's seat; the
      retellings of Horeb, Baal-peor, the bar and the two kings through the
      readback's first form) follows in its own sitting
      (World/step9/DEUTERONOMY_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_04_vaetchanan_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
