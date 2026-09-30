import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 22 — CHAPTER 34, THE DEATH OF MOSES (LEAN, 2026-09-30): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch34.py <uid>.
# Sitting 21's form (seat_ch33.py) over one unit; the CITE INDEX regex widened for the Tosefta's one row. RUN FROM THE REPO ROOT.
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-30'
UID = sys.argv[1]
SPEC = {
 'deu_34_moses_death': (34, 1, 12, [('DV34-01', 1, 'and_moses_went_up_to_nebo_the_lord_showed_him_all_the_land', 'and_moses_went_up_from_the_plains_of_moab_to_mount_nebo_the_top_of_pisgah_and_the_lord_showed_him_all_the_land_gilead_to_dan_naphtali_ephraim_and_manasseh_judah_to_the_hinder_sea_the_south_the_plain_of_jericho_to_zoar'), ('DV34-02', 4, 'this_is_the_land_i_swore_you_shall_not_cross_over_there', 'this_is_the_land_which_i_swore_to_abraham_isaac_and_jacob_to_your_seed_i_will_give_it_i_have_caused_you_to_see_it_but_you_shall_not_cross_over_there'), ('DV34-03', 5, 'moses_the_servant_of_the_lord_died_there_he_buried_him_no_man_knows_his_grave', 'moses_the_servant_of_the_lord_died_there_in_the_land_of_moab_by_the_mouth_of_the_lord_he_buried_him_in_the_valley_over_against_beth_peor_and_no_man_knows_his_grave_to_this_day'), ('DV34-04', 7, 'a_hundred_and_twenty_years_his_eye_not_dim_israel_wept_thirty_days', 'moses_a_hundred_and_twenty_years_old_when_he_died_his_eye_not_dim_nor_his_force_abated_the_children_of_israel_wept_for_moses_thirty_days_and_the_days_of_weeping_were_ended'), ('DV34-05', 9, 'joshua_full_of_the_spirit_of_wisdom_israel_hearkened_to_him', 'joshua_the_son_of_nun_full_of_the_spirit_of_wisdom_for_moses_had_laid_his_hands_upon_him_and_the_children_of_israel_hearkened_to_him_and_did_as_the_lord_commanded_moses'), ('DV34-06', 10, 'no_prophet_like_moses_the_signs_the_mighty_hand_the_great_terror', 'there_has_not_arisen_a_prophet_since_in_israel_like_moses_whom_the_lord_knew_face_to_face_in_all_the_signs_and_wonders_in_egypt_and_all_the_mighty_hand_and_the_great_terror_which_moses_wrought_in_the_sight_of_all_israel')],
  'and Moses went up from the plains of Moab to Mount Nebo and the LORD showed him all the land — Gilead to Dan, Naphtali, Ephraim and Manasseh, Judah to the hinder sea, the south and the plain of Jericho to Zoar; this is the land which I swore to Abraham, Isaac and Jacob — I have caused you to see it, but you shall not cross over there; Moses the servant of the LORD died there by the mouth of the LORD, He buried him in the valley over against Beth-peor and no man knows his grave; a hundred and twenty years old, his eye not dim, Israel wept thirty days; Joshua full of the spirit of wisdom, Israel hearkened to him; no prophet arose like Moses, whom the LORD knew face to face — the signs and wonders in Egypt, the mighty hand and the great terror in the sight of all Israel'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 22, chapter 34, THE DEATH OF MOSES, LEAN"
    comment: >
      The book's twenty-second reading and its LAST, at the chapter's grain
      (chapter {CH} verses {LO}-{HI} as one draft — {WHAT}; the portion Vezot
      Habrachah runs 33:1-34:12 — chapter 34 the unit, CHAPTER NUMBERS, the
      book's last chapter; one chapter read at one sitting in one run under
      the cost rules' cap, one unit, one ledger), THE SEVENTEENTH SITTING OF
      THE LEAN PASS (ruled 2026-09-23) and its ninth reading, THE SPINE IN
      FORCE AT ITS LAST PISKA: every row whole under the whole-row rule:
      Onkelos Deuteronomy {CH}:{LO}-{HI} whole and fresh (the export's rows
      the DB's — the identity, asserted); THE SIFREI ON DEUTERONOMY IN FORCE
      — piska 357 on 34:1-12 (44 rows read whole in both files; the
      export's last piska, its last row on the tablets broken "in the sight
      of all Israel"; four rows read before over four ledgers REREAD WHOLE
      and marked by computation; the rows seated at the verse each cites in
      the Hebrew — THE SEAT RULE BY ROW — one citing row per verse 34:1-11,
      34:12's words at the last two rows); two rows outside the spine
      citing the chapter read whole (both reread whole from chapters 29-31
      and the song — the angel of death refused, the two denials); THE
      TESTING SHELF'S ONE ROW read whole by sitting 21b's leaving (Tosefta
      Sotah 4:4 — Moses merited Joseph's bones, the four mil from Reuben's
      portion to Gad's); the kin (Genesis 12, 13, 15, 50; Exodus 24, 33;
      Numbers 11, 12, 20, 27, 33; Deuteronomy 3, 18, 31-33) credited by
      name from the earlier ledgers. Ledger deu_34_moses_death_{DATE}.md,
      coverage computed by script (59 sources over the chapter: 12 Onkelos
      + 44 spine + 2 outside + 1 Tosefta), the ink facts computed from the
      Tanakh DB and the snapshot store (67 asserts over four passes: two
      fell on the first pass of block a — Moab's four seats, the two-letter
      "el" the preposition; one on block b's first — the Torah's
      twenty-fifth Aramaic seat past the measure's cut; none on the
      fourth), the engine's numeral parser measured on every verse (TWO
      NUMBERS counted — 120 at 34:7, 31:2's number on the marker's day, and
      30 at 34:8, Aaron's thirty days: a guard owed the compile), the store
      the DB at every verse, every quotation cut by consonants (zero misses
      on 59 rows in the rows check after one retype). Seated as claims
      {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The Mishnah and Tosefta rows the spine and the translator name (Nazir
      1:3 the thirty days at 357:37; Sotah 1:9 the bones at Tosefta Sotah
      4:4; Avot 1:1 the chain at Onkelos 34:9; Sanhedrin 10:1 the
      resurrection at 357:18) are the compile's cases (22b); THE THREE
      GIFTS' DAEMON at 34:5, the register's receipt at 34:9 and the thirty
      days on the counter the compile's matters; the full process (the
      docket whole, the full records) OWED to this chapter under the lean
      pass (World/step9/COMPILE_DEBT.md's lean-pass box).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_34_moses_death_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
ci = set(re.findall(r'^(Onkelos Deut \d+:\d+|Sifrei Devarim \d+:\d+|Tosefta Sotah \d+:\d+)$', led, re.M))
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
