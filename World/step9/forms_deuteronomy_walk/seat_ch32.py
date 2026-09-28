import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 20 — CHAPTER 32, THE SONG (LEAN, 2026-09-27/28): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch32.py <uid>.
# Sitting 19's form (seat_ch29.py) over two units. RUN FROM THE REPO ROOT.
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-27'
UID = sys.argv[1]
SPEC = {
 'deu_32_haazinu': (32, 1, 43, [('DV32-01', 1, 'give_ear_o_heavens_the_rock_whose_work_is_perfect', 'give_ear_o_heavens_and_hear_o_earth_my_doctrine_as_the_rain_i_proclaim_the_name_ascribe_greatness_the_rock_his_work_is_perfect_a_god_of_faithfulness_just_and_right'), ('DV32-02', 5, 'the_crooked_generation_and_the_father_who_made_them', 'they_dealt_corruptly_not_his_children_a_perverse_and_crooked_generation_do_you_thus_requite_the_lord_is_he_not_your_father_who_bought_you_made_you_and_established_you'), ('DV32-03', 7, 'remember_the_days_of_old_the_nations_divided', 'remember_the_days_of_old_ask_your_father_the_most_high_gave_the_nations_their_inheritance_by_the_number_of_the_children_of_israel_the_lords_portion_is_his_people'), ('DV32-04', 10, 'found_in_the_desert_the_apple_of_his_eye_the_eagle', 'he_found_him_in_a_desert_land_kept_him_as_the_apple_of_his_eye_as_an_eagle_bears_her_young_on_her_pinions_the_lord_alone_led_him_no_strange_god_with_him'), ('DV32-05', 13, 'the_heights_of_the_land_honey_from_the_rock', 'he_made_him_ride_on_the_high_places_honey_from_the_crag_and_oil_from_the_flinty_rock_curd_and_milk_the_fat_of_lambs_and_rams_of_bashan_the_kidney_fat_of_wheat_the_blood_of_the_grape'), ('DV32-06', 15, 'jeshurun_grew_fat_and_kicked', 'jeshurun_grew_fat_and_kicked_forsook_the_god_who_made_him_moved_him_to_jealousy_with_strange_gods_sacrificed_to_demons_gods_they_knew_not_forgot_the_rock_that_begot_him'), ('DV32-07', 19, 'the_lord_saw_and_spurned_i_will_hide_my_face', 'the_lord_saw_and_spurned_i_will_hide_my_face_and_see_their_end_a_perverse_generation_i_will_provoke_them_with_a_foolish_nation_a_fire_burns_to_the_depths_of_sheol'), ('DV32-08', 23, 'evils_heaped_the_sword_without_and_terror_within', 'i_will_heap_evils_and_spend_my_arrows_hunger_the_fiery_bolt_the_teeth_of_beasts_the_venom_of_crawlers_the_sword_without_and_terror_within_the_young_man_and_the_maiden'), ('DV32-09', 26, 'i_would_have_scattered_them_but_for_the_enemys_boast', 'i_said_i_would_scatter_them_were_it_not_for_the_enemys_provocation_lest_they_say_our_hand_is_high_a_nation_void_of_counsel'), ('DV32-10', 29, 'had_they_been_wise_one_chasing_a_thousand', 'had_they_been_wise_how_should_one_chase_a_thousand_except_their_rock_had_sold_them_their_rock_is_not_as_our_rock_our_enemies_are_judges_the_vine_of_sodom_the_venom_of_asps'), ('DV32-11', 34, 'laid_up_in_store_vengeance_is_mine', 'laid_up_in_store_sealed_in_my_treasuries_vengeance_is_mine_and_recompense_the_lord_will_judge_his_people_when_their_power_is_gone_where_are_their_gods_who_ate_the_fat_of_their_sacrifices'), ('DV32-12', 39, 'see_now_that_i_i_am_he_sing_o_nations', 'see_now_that_i_i_am_he_i_kill_and_make_alive_i_lift_my_hand_to_heaven_my_glittering_sword_vengeance_on_my_adversaries_sing_o_nations_the_blood_of_his_servants_avenged_his_land_atones')],
  'give ear, O heavens — the witnesses called, the rain and the dew, the Name proclaimed, the Rock whose work is perfect; the crooked generation and the Father who made them; remember the days of old — the nations divided by the number of Israel, the LORD\'s portion His people; found in the desert, the apple of His eye, the eagle, the LORD alone; the heights of the land, honey from the rock, the blood of the grape; Jeshurun grew fat and kicked — the God who made him forsaken, demons and new gods; the LORD saw and spurned — I will hide My face, a foolish nation, the fire to Sheol; evils heaped — hunger, beasts, the serpent, the sword without and terror within; I would have blotted them out but for the enemy\'s boast — a nation void of counsel; had they been wise — one chasing a thousand, the Rock that sold them, the vine of Sodom; laid up in store — vengeance is Mine, the LORD will judge His people, where are their gods; see now that I, I am He — I kill and make alive, the hand lifted, the sword whetted, the blood avenged — sing, O nations'),
 'deu_32_song_aftermath': (32, 44, 52, [('DV32A-01', 44, 'moses_and_hoshea_speak_the_song', 'moses_came_and_spoke_all_the_words_of_this_song_in_the_ears_of_the_people_he_and_hoshea_son_of_nun_and_finished_speaking_to_all_israel'), ('DV32A-02', 46, 'set_your_heart_it_is_your_life', 'set_your_heart_to_all_these_words_command_your_children_to_do_all_the_words_of_this_law_it_is_no_empty_thing_it_is_your_life_you_shall_prolong_days_on_the_land'), ('DV32A-03', 48, 'the_selfsame_day_go_up_to_nebo_and_die_as_aaron_died', 'the_selfsame_day_go_up_to_mount_nebo_in_the_abarim_see_the_land_of_canaan_and_die_in_the_mountain_and_be_gathered_to_your_people_as_aaron_died_on_hor'), ('DV32A-04', 51, 'meribath_kadesh_you_shall_see_the_land_and_not_go_there', 'because_you_trespassed_at_meribath_kadesh_and_did_not_sanctify_me_you_shall_see_the_land_before_you_but_you_shall_not_go_there')],
  'Moses and Hoshea son of Nun speak the song in the ears of the people; set your heart to all these words — it is your life, no empty matter; the selfsame day — go up to Nebo in the Abarim, see the land and die as Aaron died on Hor; because you broke faith at Meribath-kadesh — you shall see the land from afar and not go there'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 20, chapter 32, THE SONG, LEAN"
    comment: >
      The book's twentieth reading, at the chapter's grain (chapter {CH}
      verses {LO}-{HI} as one draft — {WHAT}; no portion edge inside the
      chapter — Haazinu is 32:1-52 whole, Vezot Habrachah opens at 33:1;
      the chapter the unit, CHAPTER NUMBERS; one chapter read at one sitting
      in four runs under the cost rules' cap by the split's byte plan, two
      units, one ledger), THE THIRTEENTH SITTING OF THE LEAN PASS (ruled
      2026-09-23), its seventh reading and THE FIRST WITH THE SPINE IN FORCE
      since chapter 26: every row whole under the whole-row rule: Onkelos
      Deuteronomy {CH}:{LO}-{HI} whole and fresh (the export's rows the DB's
      — the identity, asserted); THE SIFREI ON DEUTERONOMY IN FORCE —
      thirty-six piskaot 306-341 on 32:1-52 (249 rows read whole in both
      files, the export's longest piska 306 on 32:1 with thirty-seven rows;
      every head present, 328's misprinted in the Hebrew marker — 32:35 for
      32:38's words, the row seated by its words; thirty rows read before
      over twenty-four ledgers REREAD WHOLE and marked by computation); eleven
      rows outside the spine citing the chapter read whole (eight reread
      whole from chapters 1-3, 4, 8, 9, 11, sitting 19 and the Genesis ledger
      of the covenant's bow; three fresh from the blessing's and the death's
      piskaot, the piskaot not opened — READ THEN COMPILE PER PORTION), the
      kin (Genesis 4, 6, 7, 11, 12, 15; Exodus 32; Leviticus 13, 26; Numbers
      13, 14, 17, 19, 20, 23, 25, 27, 28, 35; Deuteronomy 4, 6, 8, 9, 11,
      29-31) credited by name from the earlier ledgers. Ledger
      deu_32_haazinu_{DATE}.md, coverage computed by script (312 sources
      over the chapter: 52 Onkelos + 249 spine + 11 outside), the ink facts
      computed from the Tanakh DB and the snapshot store (39 asserts: 1 fell
      on the first typed pass — 328's marker sits in the Hebrew row itself;
      0 on the second and third), the engine's numeral parser measured on
      every verse (32:15's FALSE EIGHT "you grew fat" and 32:30's JOINED
      THOUSAND [1, 1002] — the spine reads the one as a verb and the other
      as four numbers: the compile's two guards), the store the DB at every
      verse but 32:13 (the qere), every quotation cut by consonants (zero
      misses on 312 rows in the whole-spine check's first run). Seated as
      claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The Mishnah rows the spine names (Chagigah 1:8 at 317:3 and 335:1;
      Peah 1:1 inside 336:1-2; Sotah 9:9; Sanhedrin 3:5 the enemy's
      disqualification; Berakhot 1:1 the Shema's clock; Avot 5:1) are the
      compile's cases (20b); the full process (the docket whole, the full
      records) OWED to this chapter under the lean pass
      (World/step9/COMPILE_DEBT.md's lean-pass box).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_32_haazinu_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
