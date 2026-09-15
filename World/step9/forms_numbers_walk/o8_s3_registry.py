import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# O8 S3 (2026-09-08; NARRATIVE_GAPS.md section 7e) — the one registry: the scene tokens joined to existing entities as members
# scoped [step9-scenes]; the stretch's new entities appended as text at the file's tail. Idempotent. A JOIN target that does not
# exist is reported (never silently created): the design names the existing ids.
import re, yaml, sys
ROOT = _ROOT
path = ROOT + '/logic/corpus/entity_registry.yaml'
txt = open(path, encoding='utf-8').read()
d = yaml.safe_load(txt)
ids = {e['id'] for e in d['entities']}
tokens = {m['token'] for e in d['entities'] for m in (e.get('members') or []) if 'step9-scenes' in (m.get('units') or [])}
NOTE = '   # O8 S3 (2026-09-08): the step-9 scene token (cold_run_mamre.py), resolved at the engine'
# ---- members joining EXISTING entities: entity id -> the scene token ----
JOIN = {'isaac': 'isaac', 'rebekah': 'rebekah', 'jacob': 'jacob', 'esau': 'esau', 'laban': 'laban', 'leah': 'leah', 'rachel': 'rachel', 'lot': 'lot', 'ishmael': 'ishmael', 'hagar': 'hagar',
        'three_visitors': 'the-three-men', 'two_angels_sodom': 'the-two-angels', 'the_men_of_sodom': 'the-men-of-sodom', 'avimelekh_abraham_era': 'abimelech', 'avimelekh_isaac_era': 'abimelech-of-isaac',
        'fikhol_isaac_era': 'phicol', 'reuben': 'reuben', 'simeon': 'simeon', 'levi': 'levi', 'judah': 'judah', 'dan_son': 'dan', 'naphtali': 'naphtali', 'gad': 'gad', 'asher': 'asher',
        'issachar': 'issachar', 'zebulun': 'zebulun', 'dinah': 'dinah', 'joseph': 'joseph', 'beer_sheva_place': 'beersheba', 'rachel_and_leah': 'rachel_and_leah', 'abrahams_serving_lad': 'the-lad',
        'nahor_son_of_terah': 'nahor', 'milcah': 'milcah', 'the_land_of_canaan': 'the-land-of-canaan'}   # the scene uses the S2 token; the bare 'the-land' is the erection's subject (fixed 2026-09-08 after the RUN reading)
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
 ('lots_wife', "Lot's wife, who looked back and became a pillar of salt (Gen 19:26)", 'person', ['lots-wife'], None),
 ('the_two_daughters_of_lot', "Lot's two daughters (Gen 19:8, 19:30-38)", 'collective', ['the-two-daughters'], None),
 ('the_firstborn_daughter_of_lot', "Lot's firstborn daughter, the mother of Moab (Gen 19:31-37)", 'person', ['ha-bekhirah'], None),
 ('moab', 'Moab, son of the firstborn daughter, father of the Moabites (Gen 19:37)', 'person', ['moab'], None),
 ('ben_ammi', 'Ben-ammi, son of the younger daughter, father of the children of Ammon (Gen 19:38)', 'person', ['ben-ammi'], None),
 ('ahuzzath', "Ahuzzath, Abimelech's friend (Gen 26:26)", 'person', ['ahuzzath', 'the-friend'], None),
 ('keturah', "Keturah, Abraham's wife after Sarah (Gen 25:1-4)", 'person', ['keturah'], 'Bereshit Rabbah 61:4: Rav says she is Hagar — recorded, no fold.'),
 ('the_philistines', 'the Philistines of Gerar who envied Isaac and stopped the wells (Gen 26:14-15, 26:18)', 'collective', ['the-philistines'], None),
 ('the_heap', 'the heap of stones Jacob and his kin made, named Jegar-sahadutha and Galeed (Gen 31:46-48)', 'object', ['the-heap'], None),
 ('the_pillar_of_gilead', 'the stone Jacob raised as a pillar at the heap (Gen 31:45, 31:51-52)', 'object', ['the_pillar_of_gilead'], None),
 ('the_place_luz_bethel', 'the place where Jacob lodged, Luz, named Bethel (Gen 28:11, 28:19)', 'place', ['the-place'], None),
 ('the_wells_of_isaac', "the wells Isaac's servants dug in the wadi of Gerar: Esek, Sitnah, Rehoboth (Gen 26:19-22)", 'object', ['esek', 'sitnah', 'rehoboth'], None),
 ('the_servants_of_isaac', "Isaac's servants who dug the wells (Gen 26:19, 26:25, 26:32)", 'collective', ['the-servants-of-isaac'], None),
 ('the_herdsmen_of_gerar', "the herdsmen of Gerar who quarreled with Isaac's herdsmen (Gen 26:20)", 'collective', ['the-herdsmen-of-gerar'], None),
 ('isaac_and_abimelech', "Isaac and Abimelech's party, who swore each to his brother (Gen 26:28-31)", 'collective', ['isaac_and_abimelech'], None),
 ('the_two_lads', "Abraham's two lads left with the donkey (Gen 22:3, 22:5, 22:19)", 'collective', ['the-two-lads'], None),
 ('bethuel', "Bethuel son of Nahor, father of Rebekah and Laban (Gen 22:22-23, 28:2, 28:5)", 'person', ['bethuel'], None),
 ('judith', 'Judith daughter of Beeri the Hittite, wife of Esau (Gen 26:34)', 'person', ['judith'], None),
 ('basemath', 'Basemath daughter of Elon the Hittite, wife of Esau (Gen 26:34)', 'person', ['basemath'], None),
 ('beeri', 'Beeri the Hittite (Gen 26:34)', 'person', ['beeri'], None), ('elon', 'Elon the Hittite (Gen 26:34)', 'person', ['elon'], None),
 ('zoar', 'Zoar, the little city spared (Gen 19:20-23, 13:10)', 'place', ['zoar'], None),
 ('sodom', 'Sodom (Gen 13:10-13, 18:20-19:29)', 'place', ['sodom'], None), ('gerar', 'Gerar, the city of Abimelech (Gen 20:1, 26:1-17)', 'place', ['gerar'], None),
 ('bilhah', "Bilhah, Rachel's maid, given to Jacob as a wife (Gen 29:29, 30:3-8)", 'person', ['bilhah'], None),
 ('zilpah', "Zilpah, Leah's maid, given to Jacob as a wife (Gen 29:24, 30:9-13)", 'person', ['zilpah'], None),
 ('mahalath', 'Mahalath daughter of Ishmael, sister of Nebaioth, wife of Esau (Gen 28:9)', 'person', ['mahalath'], None),
 ('the_ram', 'the ram caught in the thicket, offered in place of Isaac (Gen 22:13)', 'creature', ['the-ram-at-moriah'], None)   # not the bare 'the-ram' (Lev 9's),
 ('the_house_of_abimelech', "Abimelech's house — his wife and his maidservants, healed (Gen 20:17-18); his servants who feared (20:8)", 'collective', ['the_house_of_abimelech'], None),
 ('the_people_of_gerar', 'all the people of Gerar under the touch ban (Gen 26:11)', 'collective', ['the-people-of-gerar'], None),
 ('the_wells_of_abraham', "the wells Abraham's servants dug, stopped by the Philistines and redug by Isaac (Gen 26:15, 26:18)", 'object', ['the-wells-of-abraham'], None),
 ('the_sons_of_the_concubines', "the sons of Abraham's concubines, sent eastward with gifts (Gen 25:6)", 'collective', ['the-sons-of-the-concubines'], None),
 ('lot_and_his_house', 'Lot, his wife and his two daughters, led out of Sodom (Gen 19:16-17)', 'collective', ['lot_and_his_house'], None),
 ('the_cities_of_the_plain', 'Sodom, Gomorrah and the cities of the plain, overthrown (Gen 19:24-25)', 'place', ['the-cities-of-the-plain'], None),
 ('the_pillar_of_bethel', 'the stone Jacob set as a pillar and anointed at Bethel (Gen 28:18, 31:13, 35:14)', 'object', ['the_pillar_of_bethel'], None),
 ('the_heap_and_pillar', 'the heap and the pillar of Gilead as one witness (Gen 31:51-52)', 'object', ['the_heap_and_pillar'], None),
 ('the_well_of_haran', 'the well in the field with the great stone on its mouth (Gen 29:2-10)', 'place', ['the-well-of-haran'], None),
 ('the_flock', "Laban's flock under Jacob's hand, bearing striped, speckled and spotted (Gen 30:31-43, 31:8)", 'collective', ['the-flock'], None),
 ('jacob_and_his_kin', 'Jacob and his kinsmen who ate bread and lodged on the mountain (Gen 31:46, 31:54)', 'collective', ['jacob_and_his_kin'], None),
 ('isaac_and_rebekah', 'Isaac and Rebekah together, to whom Esau\'s wives were a bitterness of spirit (Gen 26:35)', 'collective', ['isaac_and_rebekah'], None),
 ('the_sons_of_nahor', 'the eight sons of Nahor by Milcah and the four by Reumah (Gen 22:20-24): Uz, Buz, Kemuel, Chesed, Hazo, Pildash, Jidlaph, Bethuel; Tebah, Gaham, Tahash, Maacah', 'collective', ['the-sons-of-nahor', 'uz', 'buz', 'kemuel', 'chesed', 'hazo', 'pildash', 'jidlaph', 'tebah', 'gaham', 'tahash', 'maacah'], None),
 ('reumah', "Reumah, Nahor's concubine (Gen 22:24)", 'person', ['reumah'], None),
 ('the_sons_of_keturah', "Keturah's six sons and their lines (Gen 25:2-4): Zimran, Jokshan, Medan, Midian, Ishbak, Shuah; Sheba and Dedan; the Asshurim, Letushim and Leummim; Ephah, Epher, Hanoch, Abida, Eldaah", 'collective', ['the-sons-of-keturah', 'zimran', 'jokshan', 'medan', 'midian', 'ishbak', 'shuah', 'sheba', 'dedan', 'ephah', 'epher', 'hanoch', 'abida', 'eldaah', 'the-asshurim', 'the-letushim', 'the-leummim'], None),
 ('the_sons_of_ishmael', "Ishmael's twelve princes (Gen 25:13-16): Nebaioth, Kedar, Adbeel, Mibsam, Mishma, Dumah, Massa, Hadad, Tema, Jetur, Naphish, Kedemah", 'collective', ['the-sons-of-ishmael', 'nebaioth', 'kedar', 'adbeel', 'mibsam', 'mishma', 'dumah', 'massa', 'hadad', 'tema', 'jetur', 'naphish', 'kedemah'], None),
 ('the_younger_daughter', "Lot's younger daughter, the mother of Ben-ammi (Gen 19:34-38)", 'person', ['the-younger-daughter'], None),
 ('the_thief_of_the_teraphim', "the one with whom Laban's gods would be found (Gen 31:32) — the machine knows her from 31:19 (Rachel), Jacob does not; the entry is written on Rachel by the narrator's knowledge", 'person', ['the-thief-of-the-teraphim'], "UNCERTAIN in Jacob's mouth, certain in the narrator's — the ledger follows the narrator (31:19); Bereshit Rabbah 74:4, 74:9 read the curse to 35:19."),
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
    txt += "\n  # ---- O8 S3 FROM MAMRE TO THE HEAP (2026-09-08; NARRATIVE_GAPS.md section 7e): the stretch's persons, collectives, objects and places (the scene tokens [step9-scenes]) ----\n" + ''.join(out)
if '--dry' in sys.argv:
    print('DRY: members to join %d; entities to append %d' % (added_members, n)); sys.exit(0)
open(path, 'w', encoding='utf-8').write(txt)
after = yaml.safe_load(open(path, encoding='utf-8'))
print('registry: members joined %d; entities appended %d (%d -> %d)' % (added_members, n, len(ids), len(after['entities'])))
