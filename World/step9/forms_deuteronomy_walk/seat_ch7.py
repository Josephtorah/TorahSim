#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 5 — CHAPTER 7 (2026-09-18, run 3): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch7.py <uid>.
# Sitting 4's form (seat_ch6.py).
import subprocess
import json, re, sys, yaml
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
DATE = '2026-09-17'
UID = sys.argv[1]
SPEC = {
 'deu_07_nations_cherem': (7, 1, 26, [('DV07-01', 1, 'the_seven_nations_and_the_ban', 'utterly_destroy_no_covenant_no_favor_no_marriage_altars_torn_down'), ('DV07-02', 6, 'the_holy_people', 'chosen_for_love_and_the_oath_not_for_number'), ('DV07-03', 9, 'the_faithful_god', 'covenant_and_kindness_to_a_thousand_generations_the_hater_repaid'), ('DV07-04', 12, 'because_you_hear', 'love_blessing_fruit_no_barrenness_no_disease_consume_no_pity'), ('DV07-05', 17, 'do_not_fear', 'remember_pharaoh_the_hornet_little_by_little_their_name_destroyed'), ('DV07-06', 25, 'the_images_and_the_devoted_thing', 'silver_and_gold_not_coveted_no_abomination_into_your_house')], 'the seven nations and the ban (7:1-26); the portion\'s edge at 7:12 inside it'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 5, chapter 7"
    comment: >
      The book's fifth reading, at the chapter's grain (chapter 7 as one
      draft — {WHAT}), run 2 of four under the four-run rule and every row
      whole under the whole-row rule: Onkelos Deuteronomy {CH}:{LO}-{HI} whole
      and fresh (the export's twenty-six rows the DB's twenty-six — the
      identity, asserted); THE SIFREI ON DEUTERONOMY SILENT ON THE CHAPTER
      (no piska head between 36 on 6:9 and 37 on 11:10) — its three rows
      outside any piska citing chapter 7 read whole in both files (37:1 the
      translator's own interpolation, marked; 50:4 the count; 61:7 the
      renaming), the kin's spine (Exodus 23:20-33, 34:11-16, Numbers
      33:50-56) credited by name from the Exodus and Numbers ledgers. Ledger
      deu_07_vaetchanan_ekev_{DATE}.md, coverage computed by script, the ink
      facts computed from the Tanakh DB and the snapshot store (every fact
      an assert — seven fell on the first typed pass, forms not facts,
      retyped from the print), the engine's numeral parser measured on
      every verse (two number verses — "seven nations" [7] with the verse's
      seven gentilic tokens as its own witness, "a thousand generations"
      [1000]; the oath's noun starred; no gap), the store's extra read-form
      token at 7:9 asserted as the chapter's one written/read pair and kept
      out of every check, every quotation cut by consonants (no miss).
      Seated as claims {ids[0]}..{ids[-1][-2:]}:
      {'; '.join(TITLES[i].lower() for i in ids)}. The compile (the ban with
      chapter 20; no covenant, no favor, no marriage; the altars and the
      Asherim; the chosen people; the faithful God and the hater repaid;
      because you hear; the blessings; no pity and no serving; do not fear;
      little by little by a call into Exodus 23; the idols' silver and gold
      with the tenth word's cell; the abomination into the house) follows
      in its own sitting (World/step9/DEUTERONOMY_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_07_vaetchanan_ekev_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
