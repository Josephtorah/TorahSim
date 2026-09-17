#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 4 — CHAPTER 6 (2026-09-17, run 3): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch6.py <uid>.
# Sitting 3's form (seat_ch5.py).
import subprocess
import json, re, sys, yaml
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
DATE = '2026-09-17'
UID = sys.argv[1]
SPEC = {
 'deu_06_shema': (6, 1, 25, [('DV06-01', 1, 'the_header', 'this_is_the_commandment_to_teach_you_hear_o_israel'), ('DV06-02', 4, 'the_creed_and_the_love', 'the_lord_is_one_with_all_your_heart_soul_and_might'), ('DV06-03', 6, 'the_words_four_duties', 'on_the_heart_taught_bound_written'), ('DV06-04', 10, 'the_gift_and_the_warning', 'cities_you_did_not_build_lest_you_forget_fear_serve_swear'), ('DV06-05', 16, 'massah_keep_the_right_and_the_good', 'you_shall_not_test_as_at_massah'), ('DV06-06', 20, 'the_sons_question_and_the_answer', 'we_were_slaves_to_pharaoh_as_he_commanded_us')], 'the Shema and its frame (6:1-25)'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 4, chapter 6"
    comment: >
      The book's fourth reading, at the chapter's grain (chapter 6 as one
      draft — {WHAT}), run 2 of four under the four-run rule: Onkelos
      Deuteronomy {CH}:{LO}-{HI} whole and fresh (the export's twenty-five
      rows the DB's twenty-five — the identity, asserted); THE SIFREI ON
      DEUTERONOMY'S PISKAOT 31-36 ON THE CHAPTER (the heads 6:4, 6:5, 6:6,
      6:7, 6:8, 6:9 — one per verse of the Shema; 6:1-3 and 6:10-25
      without a piska) — 67 rows read whole in both files, 64 fresh and 3
      credited from Genesis sittings with a quick look; eight rows outside
      the spine citing chapter 6 found by the scan of both files (one
      excluded — the English's slip for Numbers 6:27). Ledger
      deu_06_vaetchanan_{DATE}.md, coverage computed by script, the ink
      facts computed from the Tanakh DB and the snapshot store (every fact
      an assert — six fell on the first typed pass, forms not facts,
      retyped from the print), the engine's numeral parser measured on
      every verse (one number verse — the creed's "one" read as the
      numeral; no gap), the store's two dropped large letters at 6:4
      asserted as the exact miss and kept out of every check, every
      quotation cut by consonants (one miss on the first run, retyped).
      Two finds: the export's two files diverge at Sifrei 36:10; the
      shelf's count of four compartments reads 11:18 "frontlets" defective
      where the ink spells it plene. Seated as claims
      {ids[0]}..{ids[-1][-2:]}:
      {'; '.join(TITLES[i].lower() for i in ids)}. The compile (the four
      duties as law cells — the recitation, the tefillin with the
      spellings' open row, the mezuzah; fear-serve-swear; the test; the
      right and the good; the son's answer as the readback's third form;
      the receipt without the name at 6:25) follows in its own sitting
      (World/step9/DEUTERONOMY_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_06_vaetchanan_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
