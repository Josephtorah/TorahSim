#!/usr/bin/env python3
# O8 S4 (2026-09-08; NARRATIVE_GAPS.md section 8e) — the one registry: the scene tokens joined to existing entities as members
# scoped [step9-scenes]; the stretch's new entities appended as text at the file's tail. Idempotent. A JOIN target that does not
# exist is reported (never silently created): the design names the existing ids. Convention 21: a scene's tokens are its own —
# no generic noun another runner submits or writes on.
import re, yaml, sys
ROOT = '<repo-old>'
path = ROOT + '/logic/corpus/entity_registry.yaml'
txt = open(path, encoding='utf-8').read()
d = yaml.safe_load(txt)
ids = {e['id'] for e in d['entities']}
tokens = {m['token'] for e in d['entities'] for m in (e.get('members') or []) if 'step9-scenes' in (m.get('units') or [])}
NOTE = '   # O8 S4 (2026-09-08): the step-9 scene token (cold_run_joseph.py), resolved at the engine'
# ---- members joining EXISTING entities: entity id -> the scene token (only where the token is not yet a scene member) ----
JOIN = {'jacob': 'jacob', 'esau': 'esau', 'joseph': 'joseph', 'judah': 'judah', 'reuben': 'reuben', 'simeon': 'simeon', 'levi': 'levi', 'dinah': 'dinah', 'rachel': 'rachel', 'leah': 'leah',
        'bilhah': 'bilhah', 'zilpah': 'zilpah', 'isaac': 'isaac', 'rebekah': 'rebekah', 'god': 'god', 'israel_people': 'israel', 'egypt_people': 'egypt_people', 'the_land_of_canaan': 'the-land-of-canaan', 'beer_sheva_place': 'beersheba', 'the_place_luz_bethel': 'the-place', 'the_pillar_of_bethel': 'the_pillar_of_bethel'}
missing = [eid for eid in JOIN if eid not in ids]
print('JOIN targets missing from the registry (to be NEW):', missing)
added_members = 0
for eid, tok in JOIN.items():
    if eid not in ids or tok in tokens: continue
    m = re.search(r'^  - id: %s\n((?:(?!^  - id: ).*\n)*)' % re.escape(eid), txt, re.M)
    assert m, eid
    body = m.group(1)
    fm = re.search(r'^    members: \[(.*)\]\n', body, re.M)
    if fm:
        items = re.findall(r'\{[^}]*\}', fm.group(1))
        new_body = body[:fm.start()] + '    members:\n' + ''.join('      - %s\n' % it for it in items) + '      - {token: %s, units: [step9-scenes]}%s\n' % (tok, NOTE) + body[fm.end():]
    else:
        bm = re.search(r'^    members:\n((?:      - .*\n)+)', body, re.M)
        if bm:
            new_body = body[:bm.end()] + '      - {token: %s, units: [step9-scenes]}%s\n' % (tok, NOTE) + body[bm.end():]
        else:
            new_body = body + '    members:\n      - {token: %s, units: [step9-scenes]}%s\n' % (tok, NOTE)
    txt = txt[:m.start(1)] + new_body + txt[m.end(1):]
    added_members += 1
# ---- NEW entities (id, en, kind, [tokens], note) ----
NEW = [
 ('benjamin', "Benjamin, Rachel's second son, born on the way to Ephrath; Ben-oni by his mother (Gen 35:18)", 'person', ['benjamin'], None),
 ('deborah_the_nurse', "Deborah, Rebekah's nurse, died and buried below Bethel under the oak (Gen 35:8; 24:59)", 'person', ['deborah'], "Bereshit Rabbah 81:5 reads Rebekah's own death under the oak of weeping — recorded, no fold."),
 ('hamor', 'Hamor the Hivite, father of Shechem (Gen 33:19, 34:2-26)', 'person', ['hamor'], None),
 ('shechem_son_of_hamor', 'Shechem son of Hamor, prince of the land (Gen 34:2-26)', 'person', ['shechem'], None),
 ('the_men_of_shechem', 'the men of the city of Shechem, circumcised by the condition and slain on the third day (Gen 34:20-25)', 'collective', ['the-men-of-shechem'], None),
 ('the_city_of_shechem', 'the city of Shechem, plundered (Gen 33:18, 34:27-29)', 'place', ['the-city-of-shechem'], None),
 ('the_field_at_shechem', 'the portion of the field Jacob bought from the sons of Hamor for a hundred kesitah (Gen 33:19; Josh 24:32)', 'object', ['the-field-at-shechem'], None),
 ('the_altar_of_el_elohe_israel', 'the altar Jacob set up at Shechem and named (Gen 33:20) — a second altar at Shechem beside Abram\'s (12:7)', 'object', ['the-altar-of-el-elohe-israel'], None),
 ('the_altar_at_bethel_again', 'the altar Jacob built at Bethel on his return, the place named El-Bethel (Gen 35:1-7)', 'object', ['the-altar-at-bethel-again'], None),
 ('the_house_of_jacob', "Jacob's house and all who were with him (Gen 35:2-6, 46:27, 47:12)", 'collective', ['the-house-of-jacob'], None),
 ('the_cities_around_shechem', 'the cities around, on whom a terror of God fell (Gen 35:5)', 'collective', ['the-cities'], None),
 ('the_grave_of_rachel', "Rachel's grave on the way to Ephrath, with its pillar to this day (Gen 35:19-20; 48:7)", 'place', ['the-grave-of-rachel'], None),
 ('the_midwife', "the midwife at Rachel's hard birth (Gen 35:17)", 'person', ['the-midwife'], None),
 ('simeon_and_levi', "Simeon and Levi, Dinah's brothers, each with his sword (Gen 34:25-31; 49:5-7 the family engine's testament)", 'collective', ['simeon-and-levi'], None),
 ('the_maids_and_their_children', "Bilhah and Zilpah with their children, first in the order of the meeting (Gen 33:2, 33:6)", 'collective', ['the-maids-and-their-children'], None),
 ('esaus_wives', "Esau's wives of the Edom ledger: Adah daughter of Elon, Oholibamah daughter of Anah, Basemath daughter of Ishmael (Gen 36:2-3)", 'collective', ['adah-wife-of-esau', 'oholibamah', 'basemath-bat-ishmael'], "UNCERTAIN against 26:34 (Basemath daughter of Elon, Judith daughter of Beeri) and 28:9 (Mahalath daughter of Ishmael): the ink's two Basemaths and the Ishmaelite wife's two names — recorded, no fold."),
 ('the_chiefs_of_esau', "the chiefs of the sons of Esau (Gen 36:15-19) and the chiefs by their places (36:40-43): Teman, Omar, Zepho, Kenaz, Korah, Gatam, Amalek; Nahath, Zerah, Shammah, Mizzah; Jeush, Jalam, Korah; Timna, Alvah, Jetheth, Oholibamah, Elah, Pinon, Kenaz, Teman, Mibzar, Magdiel, Iram", 'collective', ['the-chiefs-of-esau'], None),
 ('the_sons_of_seir', 'the sons of Seir the Horite, the dwellers of the land, and their chiefs (Gen 36:20-30): Lotan, Shobal, Zibeon, Anah, Dishon, Ezer, Dishan', 'collective', ['the-sons-of-seir'], 'Bava Batra 115b:4 on the two Anahs (36:20, 36:24) — recorded, the ink\'s knot kept.'),
 ('the_kings_of_edom', 'the eight kings who reigned in Edom before a king reigned for the sons of Israel (Gen 36:31-39): Bela, Jobab, Husham, Hadad son of Bedad, Samlah, Shaul of Rehoboth, Baal-hanan, Hadar', 'collective', ['the-kings-of-edom', 'bela', 'jobab', 'husham', 'hadad-ben-bedad', 'samlah', 'shaul-of-rehoboth', 'baal-hanan', 'hadar'], None),
 ('eliphaz', "Eliphaz, Esau's firstborn by Adah (Gen 36:4, 36:10-12, 36:15-16)", 'person', ['eliphaz'], None),
 ('reuel', "Reuel, Esau's son by Basemath (Gen 36:4, 36:10, 36:13, 36:17)", 'person', ['reuel'], None),
 ('amalek', "Amalek, son of Eliphaz by Timna the concubine (Gen 36:12, 36:16) — the exodus story's amaleq is the people", 'person', ['amalek-son-of-eliphaz'], None),
 ('timna', "Timna, concubine of Eliphaz, sister of Lotan (Gen 36:12, 36:22) — Sanhedrin 99b:7-8: the rejected proselyte", 'person', ['timna'], None),
 ('the_coat_of_stripes', "Joseph's coat of stripes, stripped, dipped in blood, recognized (Gen 37:3, 37:23, 37:31-33)", 'object', ['the-coat-of-stripes'], None),
 ('the_pit', 'the empty pit in the wilderness, no water in it (Gen 37:20-29)', 'place', ['the-pit'], None),
 ('the_ishmaelites', 'the caravan of Ishmaelites from Gilead who bought Joseph and brought him to Egypt (Gen 37:25-28, 39:1)', 'collective', ['the-ishmaelites'], None),
 ('the_midianites', 'the Midianite men, merchants, who passed by (Gen 37:28)', 'collective', ['the-midianites'], None),
 ('the_medanites', 'the Medanites who sold Joseph to Potiphar (Gen 37:36)', 'collective', ['the-medanites'], None),
 ('the_sellers_of_joseph', "the sellers of Joseph at 37:28 — 'and they drew and lifted Joseph out of the pit, and sold Joseph': the ink's grammar leaves the subject between the brothers and the Midianites; Joseph's own word at 45:4 names the brothers", 'collective', ['the-sellers-of-joseph'], "UNCERTAIN in the verse's grammar, certain in Joseph's mouth (45:4-5) — the ledger's counterparty follows Joseph's word."),
 ('the_man_at_shechem', 'the man who found Joseph wandering in the field and sent him to Dothan (Gen 37:15-17)', 'person', ['the-man-at-shechem'], 'Bereshit Rabbah 84:14: three angels — recorded, no fold.'),
 ('the_two_officers', "Pharaoh's two officers in custody, the chief cupbearer and the chief baker (Gen 40:1-23, 41:9-13)", 'collective', ['the-two-officers'], None),
 ('potiphar', "Potiphar, Pharaoh's officer, the chief of the slaughterers, an Egyptian man (Gen 37:36, 39:1-20)", 'person', ['potiphar'], None),
 ('potiphars_wife', "Potiphar's wife, who lifted her eyes to Joseph (Gen 39:7-19)", 'person', ['potiphars-wife'], None),
 ('the_house_of_potiphar', "Potiphar's house, blessed for Joseph's sake (Gen 39:2-6, 39:14)", 'collective', ['the-house-of-potiphar'], None),
 ('the_prison_keeper', 'the chief of the prison-house (Gen 39:21-23)', 'person', ['the-prison-keeper'], None),
 ('the_cupbearer', "the chief of the cupbearers of the king of Egypt (Gen 40:1-23, 41:9-13)", 'person', ['the-chief-cupbearer'], None),
 ('the_baker', 'the chief of the bakers of the king of Egypt, hanged (Gen 40:1-22)', 'person', ['the-chief-baker'], 'The bare token the-baker is another runner\'s (convention 21) — the scene token carries the title.'),
 ('paro_joseph_era', "Pharaoh of Joseph's days, who dreamed, raised Joseph and welcomed Jacob (Gen 40:1-47:10, 50:4-6)", 'person', ['pharaoh-of-joseph'], None),
 ('the_magicians', 'the magicians of Egypt and its wise men, who could not interpret (Gen 41:8, 41:24)', 'collective', ['the-magicians'], None),
 ('asenath', 'Asenath, daughter of Poti-phera priest of On, wife of Joseph, mother of Manasseh and Ephraim (Gen 41:45, 41:50, 46:20)', 'person', ['asenath'], None),
 ('poti_phera', 'Poti-phera priest of On, father of Asenath (Gen 41:45, 41:50, 46:20)', 'person', ['poti-phera'], 'Sotah 13b:12: the same as Potiphar, renamed — recorded, no fold.'),
 ('the_steward', "the one over Joseph's house, who ran the meal and planted the cup (Gen 43:16-24, 44:1-12)", 'person', ['the-steward'], None),
 ('the_interpreter', 'the interpreter between Joseph and his brothers (Gen 42:23)', 'person', ['the-interpreter'], 'Bereshit Rabbah 91:8: Manasseh — recorded, no fold.'),
 ('the_silver_cup', "Joseph's silver cup, planted in Benjamin's bag (Gen 44:2-17)", 'object', ['the-silver-cup'], None),
 ('the_lands', 'all the lands, all the earth, that came to Egypt to buy (Gen 41:54-57)', 'collective', ['the-lands'], None),
 ('the_land_of_egypt', 'the land of Egypt of the plenty and the famine (Gen 41:29-57, 47:13-26)', 'place', ['the-land-of-egypt'], None),
 ('the_ground_of_egypt', "the ground of Egypt, bought for Pharaoh, under the statute of the fifth (Gen 47:19-26)", 'object', ['the-ground-of-egypt'], None),
 ('the_priests_of_egypt', 'the priests of Egypt, whose ground was not bought (Gen 47:22, 47:26)', 'collective', ['the-priests-of-egypt'], None),
 ('goshen', 'the land of Goshen (Gen 45:10, 46:28-34, 47:1-6, 47:27)', 'place', ['goshen'], None),
 ('rameses', 'the land of Rameses, the best of the land (Gen 47:11)', 'place', ['rameses'], None),
 ('the_wagons', "the wagons Pharaoh commanded and Joseph sent, that revived Jacob's spirit (Gen 45:19-27, 46:5)", 'object', ['the-wagons'], None),
 ('the_threshing_floor_of_atad', 'the threshing floor of Atad beyond the Jordan, named Abel-mizraim (Gen 50:10-11)', 'place', ['the-threshing-floor-of-atad'], None),
 ('the_sons_of_machir', "the sons of Machir son of Manasseh, born on Joseph's knees (Gen 50:23)", 'collective', ['the-sons-of-machir'], None),
 ('the_physicians', "Joseph's servants the physicians, who embalmed Israel (Gen 50:2)", 'collective', ['the-physicians'], None),
 ('the_camp_of_god', 'the camp of God — the angels who met Jacob at Mahanaim (Gen 32:2-3)', 'collective', ['the-camp-of-god'], None),
 ('the_terebinth_at_shechem', 'the terebinth by Shechem under which Jacob hid the foreign gods (Gen 35:4)', 'place', ['the-terebinth-at-shechem'], None),
]
out, n = [], 0
for eid, en, kind, toks, note in NEW:
    if eid in ids: continue
    mem = ''.join('      - {token: %s, units: [step9-scenes]}\n' % t for t in toks)
    block = '  - id: %s\n    en: "%s"\n    kind: %s\n    members:\n%s' % (eid, en.replace('"', '\\"'), kind, mem)
    if note: block += '    note: "%s"\n' % note.replace('"', '\\"')
    out.append(block); n += 1
if out:
    if not txt.endswith('\n'): txt += '\n'
    txt += "\n  # ---- O8 S4 FROM THE FORD TO THE COFFIN (2026-09-08; NARRATIVE_GAPS.md section 8e): the stretch's persons, collectives, objects and places (the scene tokens [step9-scenes]) ----\n" + ''.join(out)
# convention 21's guard: no NEW token may be a subject or a write target of another runner (a generic noun)
import glob, os
gen = set()
for f in glob.glob(ROOT + '/World/step9/cold_run_*.py'):
    if os.path.basename(f) in ('cold_run_joseph.py', 'cold_run_sequence.py'): continue
    s = open(f, encoding='utf-8').read()
    gen |= set(re.findall(r"'subject': '([a-z_\-]+)'", s)) | set(re.findall(r"E_\('[a-z_]+', '([a-z_\-]+)'", s))
clash = sorted(t for _, _, _, toks, _ in NEW for t in toks if t in gen)
if clash:
    print('CONVENTION 21 CLASH — a new scene token is another runner\'s subject or write target:', clash); sys.exit(1)
if '--dry' in sys.argv:
    print('DRY: members to join %d; entities to append %d; no token clash' % (added_members, n)); sys.exit(0)
open(path, 'w', encoding='utf-8').write(txt)
after = yaml.safe_load(open(path, encoding='utf-8'))
print('registry: members joined %d; entities appended %d (%d -> %d)' % (added_members, n, len(ids), len(after['entities'])))
