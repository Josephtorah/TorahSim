# -*- coding: utf-8 -*-
"""Authored content for lev_04 (4:1-35). DB evidence: lev04_prestage_full.txt
(regenerable: python3 logic/solo_tools/prestage.py Lev 4:1-4:35) + targeted
queries logged in the derivation session 2026-08-07 (probe wave, block 2)."""

UID = "lev_04_inadvertence_case_tree"
BOOK = "Lev"
SPAN = (4, 1, 4, 35)
EXTRA_SUBS = {
    # All seven et-* pronoun tokens in-span are the OBJECT-MARKER (853),
    # DB-checked per token (4:5,12,14,21,24 et-o; 4:33 et-ה global otah;
    # 4:35 et-m). Two bare 854 'et' tokens exist (4:6 idx12, 4:17
    # idx10, before the veil-phrase) — suffixless, no key needed.
    "et-o": "oto", "et-m": "otam",
}


META = [
    ("id", "lev_04_inadvertence_case_tree"),
    ("title_en", '"The inadvertence tree: four ranked cases, zero statutes (4:1-35) - the casuistic probe"'),
    ("title_he", "נֶפֶשׁ כִּי־תֶחֱטָא בִשְׁגָגָה"),
    ("title_he_translit", "nefesh ki-techeta vi-shegaga"),
    ("title_he_en", "\"'A soul, when it sins in inadvertence'\""),
    ("book_he", "וַיִּקְרָא"),
    ("book_he_translit", "Va-yiqra"),
    ("book_en", "Leviticus"),
    ("refs", "4:1-35"),
    ("unit_span_planned", "4:1-35"),
]

DRAFT_NOTE = """
DRAFT 2026-08-07 · SOLO ERA unit #15 · PROBE WAVE BLOCK 2 (owner order
2026-08-07: "probe wave lets do it"; block 2 = the casuistic genre).
Span: 4:1-35, whole chapter: 35 verses · 542 tokens
(SNAPSHOT-verified). SNAPSHOT + debut_map. Conventions unchanged;
split at etnachta - 34 of 35 verses carry one; the single verse
without one is 4:1, THE FRAME VERSE (tifcha idx1 fallback): the
frame-signature now holds THREE law units running (13:1, 19:1, 4:1 -
each unit's only narrative verse is its only unbracketed verse). No
ketiv in span. Onkelos BUFFER PENDING.

THE PROBE QUESTION AND ITS ANSWER. Block 2 asks whether a
casuistic decision tree - four agent-ranked branches with graded
outcomes and sub-branches - encodes in the machine's existing
vocabulary. ANSWER: ZERO new operators. The whole chapter is
lev_13's CASE/HANDLER machine at full scale: 6 CASEs (the 4:2
intake + four rank-branches + the 4:32 lamb-alternative) and 27
HANDLERs (the weqatal procedure chains), under ONE queue card
(4:2's daber, the relay imperative, YHWH to Moses - never narrated
in-span: again exactly ONE wayyiqtol in the chapter, 4:1's
va-yedaber [VERIFIED: morph scan]). STATUTES 0 - the register
lev_19 filled fifty-six times never fires: this chapter commands
nothing standing; it installs procedures that wait for sins. The
three law units now hold mirror profiles: lev_13 = 1 case + 6
handlers (procedure); lev_19 = 56 statutes + 4 cases + 8 handlers
(apodictic); lev_04 = 6 cases + 27 handlers + 0 statutes
(casuistic). REGISTRY 0 [VERIFIED: zero qara-lemma tokens]. TESTS
0 [VERIFIED: zero tov-adjective tokens]. Volitive census: 1
imperative, 0 jussives, 0 cohortatives - quieter than lev_19's
five; only lev_13's frame ran fully volitive-silent (zero, its
whole span) [fence: reviewer census].

THE TREE (the letter's own branch grammar): intake 4:2 - nefesh ki
techeta vi-shegaga ("a SOUL, WHEN it sins in INADVERTENCE") - then
four ranked branches whose openers the letter grades by particle:
4:3 IM ha-kohen ha-mashiach ("IF the anointed priest"), 4:13 VE-IM
kal adat yisrael ("AND IF the whole congregation"), 4:22 ASHER
nasi yecheta ("WHEN a leader sins" - the ONLY branch opened by the
relative asher [VERIFIED: idx0 morph HTr; the token map's five
livestock-branch openers are im / ve-im / asher / ve-im / ve-im]),
4:27 VE-IM nefesh achat me-am ha-aretz ("and if one soul of the
people of the land"), with sub-branches: O hoda ("OR it is made
known", 4:23/4:28 - the knowledge-trigger re-entering the tree)
and VE-IM keves (4:32, the lamb alternative). The outcomes grade
with rank: bull (priest, congregation) / male goat (leader) /
female goat or ewe (commoner); blood INSIDE the tent (veil x7,
incense-altar horns) for the two bull-cases, blood OUTSIDE (the
burnt-offering altar's horns) for leader and commoner; the
unblemished-adjective grades in gender with the victim - tamim
twice, temima twice [VERIFIED: 8549 toks 10-13/47].

CROWN 1 - THE DOOR AND THE SIN (Gen 4:7 -> Lev 4:4): the noun
chatat ("sin / sin-offering", 2403) and the noun petach ("door /
entrance", 6607) BOTH debut in Gen 4:7 - and as ADJACENT TOKENS:
la-petach chatat rovetz, "at the DOOR SIN crouches" (idx7-8,
consecutive; the chatat there rides homograph-letter 2403 b,
leveled by the debut map) [VERIFIED: both careers tok1 = Gen 4:7;
adjacency by idx]. In this chapter the sin-offering is BROUGHT TO
THE DOOR: ve-hevi et ha-par el PETACH ohel moed (4:4; petach toks
36-38/75 in-span) - the pair born crouching together at Cain's
door meet again at the tent's: the sin that lay at the opening is
carried to the opening.

CROWN 2 - THE DECEPTION'S INSTRUMENTS (Gen 37:31 -> the chatat
kit): the dip-verb taval (2881) has ten Torah tokens and its
DEBUT is Gen 37:31 - va-yishchatu SEIR IZIM va-yitblu et
ha-kutonet BA-DAM: the brothers slaughter a GOAT OF THE GOATS
and DIP Joseph's coat IN THE BLOOD. One deception verse holds
FOUR of this chapter's instruments [VERIFIED: token scan]: the
slaughter-verb shachat, the exact animal-phrase seir izim (4:23's
leader's victim), the dip-verb (4:6/4:17's ve-taval, toks 3-4/10),
and dam the blood. The kit that faked a death for a father
becomes the kit that clears a sin before God - and the span's
shachat debut-line runs deeper: the slaughter-verb's OWN tok1 is
Gen 22:10, Abraham's hand at the Akedah [VERIFIED: 7819 careers],
and the horn-noun qeren's tok1 is Gen 22:13 - the ram caught BY
ITS HORNS [VERIFIED: 7161]: the verb raised over the son and the
horns that held his substitute both land here as altar furniture
(qarnot x5, toks 12-16/21; shachat x7 in-span, toks 14-20/47).

CROWN 3 - THE FORGIVE-VERB'S PRAYER DEBUT: salach ("forgive",
5545) enters the Torah at Exod 34:9 - Moses' golden-calf plea,
VE-SALACHTA la-avonenu ("and FORGIVE our iniquity") - and its
next four tokens are THIS CHAPTER'S four machine-pardons:
ve-nislach (niphal weqatal, "and it shall be FORGIVEN") at 4:20,
4:26, 4:31, 4:35 [VERIFIED: toks 2-5/20]: the verb asked once in
prayer becomes a procedure's guaranteed last line. Its partner
kipper ("atone", 3722, toks 13-16/79 in-span) debuted at Gen
6:14 - ve-khafarta... ba-kofer, Noah PITCHING the ark with
pitch: the atone-root's first act is sealing a hull against the
flood. And THE FIRST BRANCH HAS NO PARDON [the unit's letter
headline]: the anointed priest's own bull (4:3-12) runs the
deepest blood-rite in the chapter and ends at the ash-heap with
NO ve-khiper and NO ve-nislach clause [VERIFIED: zero
3722/5545 tokens in 4:3-12] - congregation, leader, and
commoner (twice) each get the atoned-and-forgiven refrain; the
priest's own case alone ends unforgiven-in-text, mid-procedure,
like a case the letter leaves at the heap.

CROWN 4 - THE LAW CALLS ITS OWN SUBROUTINES: the chapter defines
procedures BY REFERENCE eight times - ka-asher yuram mi-shor
zevach ha-shelamim (4:10, "AS IT IS LIFTED from the ox of the
well-being sacrifice" - calling Lev 3's fat-rite); ka-asher asa
le-far ha-chatat ken yaase lo (4:20, branch 2 defined by branch
1's bull); ka-asher saraf et ha-par ha-rishon (4:21 - "as he
burned THE FIRST BULL": the law numbering its own precedent,
rishon tok 22/55); bi-meqom asher yishchat et ha-ola (4:24,
4:33 - the burnt-offering's slaughter-place as an address);
ke-chelev zevach ha-shelamim (4:26); ka-asher husar / yusar
(4:31, 4:35 - hophal: "as it IS REMOVED"). Cross-reference
census: 5 ka-asher + 2 bi-meqom-asher + 1 ke-chelev = 8 calls
[VERIFIED: token map; 4:29's compressed bi-meqom ha-ola repeats
the same pointer WITHOUT asher - the same address, counted apart
from the eight] - the casuistic genre's machine signature:
branches that invoke earlier branches instead of repeating them.

CROWN 5 - MASHIACH DEBUTS AS THE SINNING PRIEST: ha-mashiach
("the ANOINTED", 4899) enters the Torah at 4:3 and has FOUR
tokens, every one of them ha-kohen ha-mashiach - 4:3, 4:5, 4:16,
6:15 [VERIFIED: full census] - three in this chapter: the word's
whole Torah career is the anointed priest INSIDE sin-offering
law, and its debut-verse makes him the sinner: im ha-kohen
ha-mashiach yecheta LE-ASHMAT HA-AM ("if the anointed priest
sins TO THE GUILT OF THE PEOPLE" - ashmah, 819, debuting in the
same clause, 1/4): the Torah's first "mashiach" is a priest
whose sin indebts his people.

CROWN 6 - THE INADVERTENCE VOCABULARY IS BORN: shegaga
("inadvertence", 7684) DEBUTS at 4:2 and fires three times
in-span (1-3/15; the noun's career runs to Num 35's
manslayer-cities); its verb shagag (7686, 1/3) debuts at 4:13's
yishgu; alam ("be hidden", 5956, 1/10) debuts at 4:13's
ve-nelam davar ("and a thing be HIDDEN from the eyes of the
assembly"); asham the guilt-VERB (816, 1/13) debuts at 4:13's
ve-ashemu and fires at 4:22/4:27 - the whole legal grammar of
unwitting guilt (inadvertent / hidden / become-guilty) is
minted inside this one chapter, plus shefekh ("pouring-place",
8211) whose ENTIRE two-token career sits in ONE VERSE (4:12 x2
- the ash-heap named twice and never again) and seirat
("she-goat of", 8166, 1/2 with 5:6).

CROWN 7 - THE FINGER'S CAREER: etzba ("finger", 676) fires five
times in-span (toks 4-8/18, one per blood-rite) - its tok1 is
Exod 8:15, the magicians' ETZBA ELOHIM ("this is the FINGER of
God"), and its Torah career closes at Deut 9:10 with the tablets
written BE-ETZBA ELOHIM: God's finger (plague), the priest's
finger (blood, x5 here), God's finger (writing). And the
pour-verb shafakh (8210, toks 6-10/22, five yishpokh
base-pourings) debuted at Gen 9:6 - shofekh dam ha-adam, the
bloodshed ban: the verb of murder's definition is the verb of
the altar's disposal line.

CROWN 8 - ONLY THE COMMONER'S GOAT PLEASES: recha nichocha
("pleasing aroma", 7381/5207) - the phrase born on NOAH's altar
(Gen 8:21, both nouns' tok1) - appears in this chapter EXACTLY
ONCE, at 4:31, the common person's she-goat [VERIFIED: in-span
census]: not the anointed priest's bull, not the congregation's,
not the leader's goat - the one smoke called soothing is the
lowest-ranked sinner's.

MACHINE SHAPE (the wall): SPECS depth 1 OPEN (the relay card,
never narrated); CASES 6; HANDLERS 27; STATUTES 0; REGISTRY 0;
TESTS 0; 33 standing facts. The kipper+nislach refrain runs 4x;
the semikha hand-leaning runs 5x (5564 toks 9-13/23 - its tok1
is Gen 27:37's semakhtiv, Isaac SUSTAINING Jacob in the
blessing; its Torah career ends at Deut 34:9, Moses' hands on
Joshua); the blood-noun fires 15 in-span tokens; the chatat-noun
20 (toks 14-33/142 - the sin-offering's densest chapter).
"""

STEPS = [
 dict(ref=(4,1), op="THE_FRAME",
  en="And the LORD spoke to Moses, saying:",
  tl_en="the LORD spoke to Moses",
  tr_en="saying - the quote opener",
  ops=[
   dict(op="EVENT",
    expr="speak(e1) ∧ Agent(e1, YHWH)",
    frag=("va-yedaber",5), prose="""
THE THIRD FRAME. va-yedaber YHWH el moshe le-mor ("and the LORD
spoke to Moses, saying") - the span's only wayyiqtol
('and-then-he-did' narrative form) [VERIFIED: morph scan, 1 in
542 tokens] and its only etnachta-less verse [VERIFIED: mark
census]: the frame-signature's third consecutive law unit
(13:1, 19:1, 4:1). Moses alone on the distribution list
(contrast 13:1's Moses-and-Aaron)."""),
   dict(op="NOTE_PRESUPPOSED",
    expr="moshe are READ without prior install (standalone machine; the Exodus narrative's person - cross-unit chaining is Stage E)",
    frag=("el",2), prose="""
Flag, not fix - the addressee is an import (lev_13/lev_19
precedent)."""),
  ],
  comment="One narrative verb; thirty-four verses of installed procedure follow."),

 dict(ref=(4,2), op="THE_RELAY_AND_THE_INTAKE",
  en="Speak to the sons of Israel, saying: a soul, when it sins in inadvertence from any of the commandments of the LORD which shall not be done, and does from one of them -",
  tl_en="speak to the sons of Israel",
  tr_en="a soul that sins in inadvertence, and does from one of them",
  ops=[
   dict(op="DECLARE",
    expr="DECLARE(YHWH, LET(daber_el_bene_yisrael(moshe)))",
    frag=("daber",5), prose="""
THE SECOND RELAY CARD [MACHINE SHAPE]. daber el bene yisrael
le-mor ("SPEAK to the sons of Israel, saying") - the span's
single volitive (Vpv2ms) [VERIFIED: census - 1 imperative, 0
jussives, 0 cohortatives], a true narrative-present demand:
PUSH. The address here is plain bene yisrael - NOT lev_19's
kal adat bene yisrael (that whole-congregation daber remains
unique to the holiness chapter). And as in lev_19, no verse
narrates Moses speaking: the card holds OPEN under the whole
tree. PUSH LET(daber_el_bene_yisrael(moshe)). Depth 1."""),
   dict(op="CASE",
    expr="CASE(nefesh, techeta_vi_shegaga_mi_kol_mitzvot) ROUTE(ve_asa_me_achat_me_hena)",
    frag=("nefesh",13), prose="""
THE INTAKE - INADVERTENCE IS BORN [CROWN 6]. nefesh ki
techeta VI-SHEGAGA ("a SOUL, WHEN it sins in INADVERTENCE") -
the ki re-types (lev_13's law, third exercise), and the
trigger-noun shegaga DEBUTS here (7684, 1/15; its career runs
to Num 35's manslayer cities): the tree's whole jurisdiction
is the unwitting act - mi-kol mitzvot YHWH asher lo teasena
("from any of the LORD's commandments which shall not be
done") ve-asa me-achat me-hena ("and does from ONE of them").
The formula re-fires at each branch-head (4:13, 4:22, 4:27 -
mitzvot toks 6-9/66). CASES 1."""),
  ],
  comment="One card pushed, and the tree's root case installed in the same verse."),

 dict(ref=(4,3), op="BRANCH_ONE_THE_ANOINTED",
  en="If the anointed priest sins to the guilt of the people, he shall offer for his sin which he has sinned a bull, a son of the herd, unblemished, to the LORD for a sin-offering.",
  tl_en="if the anointed priest sins to the guilt of the people",
  tr_en="he offers an unblemished bull to the LORD for a sin-offering",
  ops=[
   dict(op="CASE",
    expr="CASE(ha_kohen_ha_mashiach, im_yecheta_le_ashmat_ha_am) ROUTE(par_ben_baqar_tamim_le_chatat)",
    frag=("im",6), prose="""
MASHIACH DEBUTS AS THE SINNER [CROWN 5]. im ha-kohen
HA-MASHIACH yecheta ("IF the ANOINTED priest sins") - the
im-branch: the word mashiach enters the Torah in this clause
(4899, 1/4; all four tokens are ha-kohen ha-mashiach - 4:3,
4:5, 4:16, 6:15 [VERIFIED: full census]) and its debut names
him sinning - LE-ASHMAT HA-AM ("to the GUILT of the people";
ashmah 819 debuting in the same clause, 1/4): the head's sin
indebts the body. Routing: par ben baqar tamim le-chatat -
the highest tariff (a herd-bull), unblemished (tamim, 8549
tok 10/47). CASES 2."""),
  ],
  comment="The first branch: the highest office, the highest victim, the people's guilt."),

 dict(ref=(4,4), op="TO_THE_DOOR",
  en="And he shall bring the bull to the entrance of the tent of meeting before the LORD, and lean his hand on the bull's head, and slaughter the bull before the LORD.",
  tl_en="bring the bull to the tent's entrance before the LORD",
  tr_en="lean the hand, slaughter the bull before the LORD",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(par_ha_chatat) THEN(hevi_el_petach_ohel_moed ∧ samakh_yado_al_rosh ∧ shachat_li_fene_YHWH)",
    frag=("ve-hevi",9), prose="""
THE SIN COMES TO THE DOOR [CROWN 1]. ve-hevi et ha-par el
PETACH ohel moed ("and he shall bring the bull to the DOOR of
the tent of meeting") - petach and chatat, the pair born as
ADJACENT tokens at Gen 4:7 (la-petach chatat rovetz, "at the
door sin crouches" - both careers' tok1, idx7-8 consecutive
[VERIFIED]), meet again: the sin-offering carried to the
opening where sin first crouched. ve-samakh et yado al rosh
ha-par ("and LEAN his hand on the bull's head") - semikha
(5564, tok 9/23; tok1 = Gen 27:37's semakhtiv, Isaac
sustaining Jacob inside the stolen blessing; the career ends
at Deut 34:9, Moses' hands on Joshua). ve-shachat ("and
slaughter") - the Akedah's verb (7819 tok1 = Gen 22:10,
Abraham's li-shechot) [CROWN 2]. HANDLERS 1."""),
  ],
  comment="Bring, lean, slaughter: the skeleton every branch will repeat."),

 dict(ref=(4,5), op="BLOOD_ENTERS",
  en="And the anointed priest shall take of the bull's blood and bring it into the tent of meeting.",
  tl_en="the anointed priest takes of the bull's blood",
  tr_en="and brings it into the tent of meeting",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(dam_ha_par) THEN(laqach_ha_mashiach ∧ hevi_oto_el_ohel_moed)",
    frag=("ve-laqach",10), prose="""
THE BLOOD GOES INSIDE. ve-laqach ha-kohen ha-mashiach mi-dam
ha-par ve-hevi oto el ohel moed - the rank-grading's key move
[THE TREE]: for the two bull-cases (priest, congregation) the
blood ENTERS the tent; for leader and commoner it will stay
at the outer altar. The blood-noun dam opens its fifteen
in-span tokens (1818, toks 49-63/166 - Abel's crying deme
tok1 behind it). HANDLERS 2."""),
  ],
  comment="Rank measured in blood-depth: the anointed's blood goes deepest."),

 dict(ref=(4,6), op="SEVEN_BEFORE_THE_VEIL",
  en="And the priest shall dip his finger in the blood and sprinkle of the blood seven times before the LORD, before the veil of the sanctuary.",
  tl_en="dip the finger in the blood",
  tr_en="sprinkle seven times before the veil of the sanctuary",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(ba_dam) THEN(taval_etzbao ∧ hiza_sheva_peamim_et_pene_parokhet_ha_qodesh)",
    frag=("ve-taval",16), prose="""
THE DIP-VERB'S REDEMPTION [CROWN 2]. ve-TAVAL ha-kohen et
ETZBAO ba-dam ("and the priest shall DIP his FINGER in the
blood") - taval's debut is Gen 37:31, the brothers dipping
Joseph's coat in goat's blood (toks 3-4/10 are this chapter's
two): the deception's dip becomes the rite's. etzba the
finger (676, tok 4/18; tok1 = Exod 8:15's etzba elohim, the
magicians' cry; the career closes at Deut 9:10, the tablets
written by God's finger) [CROWN 7]. ve-hiza sheva peamim
("sprinkle SEVEN times") et pene parokhet ha-qodesh ("before
the VEIL of the sanctuary") - parokhet tok 16/24: the
innermost address any blood reaches in this chapter.
HANDLERS 3."""),
  ],
  comment="Seven sprinklings at the veil: the tree's deepest penetration."),

 dict(ref=(4,7), op="HORNS_AND_BASE",
  en="And the priest shall put of the blood on the horns of the altar of fragrant incense before the LORD in the tent of meeting; and all the bull's blood he shall pour out at the base of the altar of burnt-offering which is at the entrance of the tent of meeting.",
  tl_en="blood on the horns of the incense altar before the LORD",
  tr_en="all the rest poured at the burnt-offering altar's base at the entrance",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(min_ha_dam) THEN(natan_al_qarnot_mizbach_ha_qetoret ∧ yishpokh_el_yesod_mizbach_ha_ola)",
    frag=("ve-natan",14), prose="""
THE AKEDAH'S HORNS [CROWN 2]. ve-natan... al QARNOT mizbach
qetoret ha-samim ("on the HORNS of the altar of fragrant
incense") - qeren's tok1 is Gen 22:13, the ram caught by its
horns; here the horns receive the substitute's blood (7161
tok 12/21; qetoret tok 20/45, the inner altar's only in-span
token). ve-et kal dam ha-par YISHPOKH el YESOD ("and ALL the
bull's blood he shall POUR at the BASE") - shafakh, Gen 9:6's
bloodshed-verb (8210, tok 6/22), domesticated to the
disposal line; yesod (3247, tok 2/9 - five of its nine Torah
tokens are this chapter's five base-pourings). HANDLERS 4."""),
  ],
  comment="Two altars, one verse: fragrant horns and a base that swallows the rest."),

 dict(ref=(4,8), op="THE_FAT_LIFTED",
  en="And all the fat of the sin-offering bull he shall lift from it: the fat that covers the entrails, and all the fat that is on the entrails,",
  tl_en="all the fat of the sin-offering bull lifted from it",
  tr_en="the covering fat and all the fat on the entrails",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(chelev_par_ha_chatat) THEN(yarim_et_ha_chelev_ha_mekhase)",
    frag=("ve-et",7), prose="""
THE LIFT. ve-et kal chelev par ha-chatat YARIM mimenu ("and
all the FAT of the sin-offering bull he shall LIFT from it")
- chelev opens its eleven in-span tokens (2459, toks 21-31/65;
tok1 = Gen 4:4, Abel's u-me-chelvehen - the fat-portions of
the first accepted offering); rum the lift-verb (7311, toks
16-18/46). HANDLERS 5."""),
  ],
  comment="Abel's fat-word begins its densest chapter."),

 dict(ref=(4,9), op="KIDNEYS_AND_LOBE",
  en="and the two kidneys and the fat that is on them, which is on the flanks, and the lobe on the liver - with the kidneys he shall remove it -",
  tl_en="the two kidneys and their fat on the flanks",
  tr_en="the liver's lobe removed with the kidneys",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(shete_ha_kelayot_ve_ha_yoteret_al_ha_kaved) THEN(yesirena)",
    frag=("ve-et",17), prose="""
THE ANATOMY LIST. shete ha-kelayot ("the two KIDNEYS", 3629
tok 9-10/17)... ve-ha-yoteret al ha-kaved ("and the LOBE on
the LIVER" - yoteret 3508 tok 6/11, kaved 3516 tok 6/11:
both nouns' careers are pure sacrificial anatomy, debuting
in Exod 29's ordination) al ha-kelayot YESIRENA ("with the
kidneys he shall REMOVE it" - sur, 5493 tok 30/55). The
kesalim flank-noun rides tok 4/5 of an all-Leviticus career
(3689). HANDLERS 6."""),
  ],
  comment="The offering's inner map, part by part."),

 dict(ref=(4,10), op="THE_FIRST_SUBROUTINE",
  en="as it is lifted from the ox of the sacrifice of well-being - and the priest shall burn them on the altar of burnt-offering.",
  tl_en="as it is lifted from the well-being sacrifice's ox",
  tr_en="the priest burns them on the burnt-offering altar",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(ka_asher_yuram_mi_shor_zevach_ha_shelamim) THEN(hiqtiram_al_mizbach_ha_ola)",
    frag=("ka-asher",10), prose="""
THE LAW CALLS LEV 3 [CROWN 4]. ka-asher YURAM mi-shor zevach
ha-shelamim ("AS IT IS LIFTED from the ox of the well-being
sacrifice" - hophal: the passive of an already-written rite):
the first of the chapter's EIGHT cross-procedure calls - the
fat-rite is not restated, it is INVOKED from the shelamim
chapter (zevach toks 16-19/72, shelamim toks 9-12/54 - four
citations each, one per branch). ve-hiqtiram ("and BURN
them", 6999 tok 20/44). HANDLERS 7."""),
  ],
  comment="The chapter's signature move: procedure by reference, not repetition."),

 dict(ref=(4,11), op="THE_CARCASS_LIST",
  en="And the bull's hide and all its flesh, with its head and with its legs, and its entrails and its dung -",
  tl_en="the hide and all the flesh, head and legs",
  tr_en="the entrails and the dung",
  ops=[
   dict(op="NOTE_ZERO_EVENTS",
    expr="the verse is a bare object-list with no verb and no event - the carry-out verb waits in 4:12",
    frag=("ve-et",12), prose="""
A VERSE WITH NO VERB. or ha-par ("the bull's HIDE" - or, Gen
3:21's skin-noun, 5785 tok 20/80) ve-et kal besaro ("and all
its FLESH" - Gen 2:21's basar)... keraav (Exod 12:9's
Passover legs-word, 3767 tok 5/8), u-firsho ("and its DUNG"
- peresh, 6569 tok 2/5, all five tokens carcass-law): the
whole animal enumerated with ZERO verbs - the letter stacks
the object and holds its breath; the machine records no
event. HANDLERS still 7."""),
  ],
  comment="The sentence inhales through a verse-long list; 4:12 exhales it."),

 dict(ref=(4,12), op="OUTSIDE_THE_CAMP",
  en="he shall carry out the whole bull outside the camp to a clean place, to the pouring-place of the ashes, and burn it on wood in fire; on the pouring-place of the ashes it shall be burned.",
  tl_en="the whole bull carried outside the camp to a clean place",
  tr_en="burned on wood in fire at the ash-pouring-place",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(kol_ha_par) THEN(hotzi_el_mi_chutz_la_machane_el_maqom_tahor ∧ saraf_al_shefekh_ha_deshen)",
    frag=("ve-hotzi",22), prose="""
THE ASH-HEAP NAMED TWICE AND NEVER AGAIN [CROWN 6]. ve-hotzi
et kal ha-par el MI-CHUTZ LA-MACHANE ("carry out the WHOLE
bull OUTSIDE THE CAMP") el maqom TAHOR ("to a CLEAN place" -
the pure-adjective on a dump: 2889 tok 35/69) el SHEFEKH
ha-deshen ("to the POURING-PLACE of the ashes") - shefekh's
entire two-token Torah career sits in this ONE verse (8211,
1-2/2 [VERIFIED]); deshen toks 2-3/5. ve-saraf... al etzim
ba-esh ("burn it on wood in fire"). And NO PARDON CLOSES THE
BRANCH [CROWN 3]: the anointed's procedure ends here at the
heap - zero kipper, zero nislach in 4:3-12 [VERIFIED] - the
only branch of the four the letter leaves unforgiven-in-text.
HANDLERS 8."""),
  ],
  comment="The deepest blood, the whole bull burned, and no forgiveness spoken."),

 dict(ref=(4,13), op="BRANCH_TWO_THE_CONGREGATION",
  en="And if the whole congregation of Israel errs, and a thing is hidden from the eyes of the assembly, and they do one of all the commandments of the LORD which shall not be done, and become guilty -",
  tl_en="if the whole congregation errs and a thing is hidden from the assembly's eyes",
  tr_en="they do one of the forbidden commandments and become guilty",
  ops=[
   dict(op="CASE",
    expr="CASE(kal_adat_yisrael, yishgu_ve_nelam_davar) ROUTE(ve_ashemu)",
    frag=("ve-im",9), prose="""
THE HIDDEN THING [CROWN 6]. ve-im kal adat yisrael YISHGU
("and if the whole congregation of Israel ERRS" - shagag the
err-verb debuting, 7686 1/3) VE-NELAM davar me-ene ha-qahal
("and a thing be HIDDEN from the EYES of the assembly" - alam
the hide-verb debuting, 5956 1/10: corporate sin defined as a
blind spot) ve-ashemu ("and they become GUILTY" - asham the
guilt-verb's Torah DEBUT, 816 1/13). A whole legal ontology -
err, hidden, guilty - is minted in one verse. qahal toks
7-9/34. CASES 3."""),
  ],
  comment="The body politic can sin without seeing; the tree has a branch for that."),

 dict(ref=(4,14), op="THE_SIN_BECOMES_KNOWN",
  en="and the sin which they sinned against it becomes known - then the assembly shall offer a bull, a son of the herd, for a sin-offering, and bring it before the tent of meeting.",
  tl_en="the sin they sinned becomes known",
  tr_en="the assembly offers a herd-bull and brings it before the tent",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(ve_noda_ha_chatat) THEN(hiqrivu_ha_qahal_par ∧ heviu_oto_li_fene_ohel_moed)",
    frag=("ve-noda",16), prose="""
KNOWLEDGE RE-ENTERS THE TREE. ve-NODA ha-chatat ("and the sin
becomes KNOWN" - yada in niphal weqatal, 3045 tok 103/174):
the tree's re-entry trigger - hiddenness (4:13) resolved by
knowledge fires the procedure, exactly as hoda will fire the
leader's and commoner's branches (4:23, 4:28: the know-verb's
three in-span tokens ARE the tree's three triggers). HANDLERS
9."""),
  ],
  comment="What was hidden from the eyes returns as knowledge, and the machinery wakes."),

 dict(ref=(4,15), op="THE_ELDERS_HANDS",
  en="And the elders of the congregation shall lean their hands on the bull's head before the LORD, and one shall slaughter the bull before the LORD.",
  tl_en="the elders lean their hands on the bull's head before the LORD",
  tr_en="the bull slaughtered before the LORD",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(par_ha_qahal) THEN(samkhu_ziqne_ha_eda_yedehem ∧ shachat_li_fene_YHWH)",
    frag=("ve-samkhu",10), prose="""
REPRESENTATIVE HANDS. ve-samkhu ZIQNE ha-eda et YEDEHEM ("and
the ELDERS of the congregation shall lean their HANDS") - the
only plural semikha in the chapter (5564 tok 10/23): a body
too large to touch the victim delegates its hands to its
elders (ziqne, 2205 tok 22/54); the congregation's dual
yedehem against every other branch's singular yado. HANDLERS
10."""),
  ],
  comment="The congregation's hands are its elders'."),

 dict(ref=(4,16), op="THE_ANOINTED_CARRIES_AGAIN",
  en="And the anointed priest shall bring of the bull's blood into the tent of meeting.",
  tl_en="the anointed priest brings of the bull's blood",
  tr_en="into the tent of meeting",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(dam_ha_par) THEN(hevi_ha_mashiach_el_ohel_moed)",
    frag=("ve-hevi",8), prose="""
THE SINNER OF BRANCH ONE OFFICIATES BRANCH TWO. ve-hevi
ha-kohen HA-MASHIACH mi-dam ha-par ("and the ANOINTED priest
shall bring of the bull's blood") - mashiach's third in-span
token (3/4): the officer whose own case ran unpardoned
carries the congregation's blood inside. Blood-depth grades
identically for the two bull-cases [THE TREE]. HANDLERS
11."""),
  ],
  comment="Same officer, same depth: the congregation ranks with its priest."),

 dict(ref=(4,17), op="SEVEN_AGAIN",
  en="And the priest shall dip his finger from the blood and sprinkle seven times before the LORD, before the veil.",
  tl_en="dip the finger from the blood",
  tr_en="sprinkle seven times before the LORD, before the veil",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(min_ha_dam) THEN(taval_etzbao ∧ hiza_sheva_peamim_et_pene_ha_parokhet)",
    frag=("ve-taval",13), prose="""
THE VEIL'S SECOND SEVEN. ve-taval... ve-hiza sheva peamim...
et pene HA-PAROKHET ("before the VEIL", here bare, without
4:6's ha-qodesh genitive - parokhet tok 17/24): the dip-verb's
fourth token (taval 4/10) - and between its Gen 37:31
deception-debut and this pair sits tok2: Exod 12:22's
u-tevaltem BA-DAM, the PASSOVER hyssop dipped in doorpost
blood; the career runs on through Lev 14's cleansing-dips
and Num 19:18's hyssop to Deut 33:24's oil-dipped foot
[VERIFIED: full 2881 census].
sheva peamim - the pair of sevens (7651 toks 82-83/185, 6471
toks 20-21/39: the chapter's only two). HANDLERS 12."""),
  ],
  comment="Branch two replays branch one's innermost rite."),

 dict(ref=(4,18), op="HORNS_AND_BASE_AGAIN",
  en="And of the blood he shall put on the horns of the altar which is before the LORD, which is in the tent of meeting; and all the blood he shall pour out at the base of the altar of burnt-offering which is at the entrance of the tent of meeting.",
  tl_en="blood on the horns of the altar before the LORD in the tent",
  tr_en="all the rest poured at the burnt-offering altar's base",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(u_min_ha_dam) THEN(yiten_al_qarnot_ha_mizbecha ∧ yishpokh_el_yesod_mizbach_ha_ola)",
    frag=("u-min",12), prose="""
THE INNER ALTAR UNNAMED. u-min ha-dam YITEN al qarnot
ha-mizbecha asher li-fene YHWH ("on the horns of THE ALTAR
that is before the LORD" - branch one named it the incense
altar; branch two calls it only 'the altar before the LORD':
the second telling compresses, the subroutine habit in
miniature). yishpokh el yesod - base-pouring 2 of 5.
HANDLERS 13."""),
  ],
  comment="Compression on the retell: the altar keeps its place, loses its name."),

 dict(ref=(4,19), op="ALL_ITS_FAT",
  en="And all its fat he shall lift from it and burn on the altar.",
  tl_en="all its fat lifted from it",
  tr_en="and burned on the altar",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(kol_chelbo) THEN(yarim_mimenu ∧ hiqtir_ha_mizbecha)",
    frag=("ve-et",7), prose="""
THE FAT-RITE IN SEVEN TOKENS. ve-et kal chelbo yarim mimenu
ve-hiqtir ha-mizbecha - branch one's three verses of anatomy
(4:8-10) compress to one line: the second bull's fat-rite is
already law, so the letter spends seven tokens where it spent
forty-five (4:8-10's 18+17+10) [VERIFIED: token counts]
(ha-mizbecha with the directional he-vowel - "to the
altar"). HANDLERS 14."""),
  ],
  comment="Forty-five tokens the first time, seven the second: precedent compresses."),

 dict(ref=(4,20), op="AS_THE_FIRST_AND_FORGIVEN",
  en="And he shall do to the bull as he did to the sin-offering bull - so shall he do to it; and the priest shall atone for them, and it shall be forgiven them.",
  tl_en="do to this bull as to the sin-offering bull",
  tr_en="the priest atones for them and they are forgiven",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(ka_asher_asa_le_far_ha_chatat) THEN(ken_yaase_lo ∧ kiper_ha_kohen ∧ nislach_lahem)",
    frag=("ve-asa",14), prose="""
BRANCH TWO CALLS BRANCH ONE - AND GETS THE PARDON [CROWNS 3,
4]. ve-asa la-par KA-ASHER ASA le-far ha-chatat ken yaase lo
("and he shall do to the bull AS HE DID to the sin-offering
bull - so shall he do to it"): the law defines a procedure by
citing its own previous branch - the chapter's clearest
subroutine call. Then the refrain the first branch never got:
ve-KHIPER alehem ha-kohen ve-NISLACH lahem ("and the priest
shall ATONE for them and it shall be FORGIVEN them") - kipper
tok 13/79, nislach tok 2/20: the forgive-verb's first token
since Moses' Exod 34:9 plea, granted first to the many.
HANDLERS 15."""),
  ],
  comment="Do as was done - and, for the first time in the chapter, be forgiven."),

 dict(ref=(4,21), op="THE_FIRST_BULL_CITED",
  en="And he shall carry the bull outside the camp and burn it as he burned the first bull: it is the sin-offering of the assembly.",
  tl_en="the bull carried outside the camp",
  tr_en="burned as the first bull was burned: the assembly's sin-offering",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(ka_asher_saraf_et_ha_par_ha_rishon) THEN(hotzi_ve_saraf_mi_chutz_la_machane)",
    frag=("ve-hotzi",16), prose="""
THE LAW NUMBERS ITS OWN PRECEDENT [CROWN 4]. ve-saraf oto
ka-asher saraf et ha-par HA-RISHON ("and burn it as he burned
THE FIRST bull" - rishon, 7223 tok 22/55): the letter itself
counts its bulls - branch one becomes citable precedent
inside its own chapter. Classification clause (the lev_13
hu-class): chatat ha-qahal HU ("it IS the assembly's
sin-offering"). HANDLERS 16."""),
  ],
  comment="'The first bull': the chapter cites itself by ordinal."),

 dict(ref=(4,22), op="BRANCH_THREE_THE_LEADER",
  en="When a leader sins, and does one of all the commandments of the LORD his God which shall not be done, in inadvertence, and becomes guilty -",
  tl_en="when a leader sins",
  tr_en="one of the forbidden commandments, in inadvertence, and becomes guilty",
  ops=[
   dict(op="CASE",
    expr="CASE(nasi, asher_yecheta_bi_shegaga) ROUTE(ve_ashem)",
    frag=("asher",3), prose="""
THE ASHER BRANCH [THE TREE]. ASHER nasi yecheta ("WHEN a
LEADER sins") - of the five livestock-branch openers (im /
ve-im / asher / ve-im / ve-im) only the nasi's rides the
relative pronoun asher [VERIFIED: idx0 HTr]: the letter
grades even its conditionals - the priest gets IF, the
leader gets WHEN. nasi (5387, tok 9/71: toks 1-8 are
Ishmael's twelve princes (17:20, 25:16), Abraham's Machpelah
title (23:6), Shechem's CHAMOR (34:2 - frozen gen_57's
demander was the Torah's fourth nasi), Exod 22:27's curse-ban
on the office, and the Exodus chieftains [VERIFIED: census]).
And
his formula alone adds ELOHAV: mitzvot YHWH ELOHAV ("the
commandments of the LORD his GOD" - 4:2/13/27 say only
YHWH): rank binds the leader by his personal God-clause.
CASES 4."""),
  ],
  comment="The leader's branch: opened by WHEN, bound to 'his God'."),

 dict(ref=(4,23), op="THE_KNOWLEDGE_TRIGGER",
  en="or his sin which he sinned is made known to him - then he shall bring his offering: a goat of the goats, a male, unblemished.",
  tl_en="or his sin is made known to him",
  tr_en="he brings a male goat, unblemished",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(o_hoda_elav_chatato) THEN(hevi_qarbano_seir_izim_zakhar_tamim)",
    frag=("o",7), prose="""
THE DECEPTION'S ANIMAL [CROWN 2]. o HODA elav chatato ("OR
his sin is MADE KNOWN to him" - hoda, hophal, the know-verb's
second in-span trigger, 3045 tok 104/174): the o-sub-branch.
ve-hevi et qarbano SEIR IZIM zakhar tamim ("a GOAT OF THE
GOATS, male, unblemished") - the exact animal-phrase of Gen
37:31, where the brothers slaughtered a seir izim to dip
Joseph's coat: the deception's victim becomes the leader's
tariff (8163 tok 4/51; qarban toks 22-24/78). HANDLERS 17."""),
  ],
  comment="Told of his sin, the leader brings the deception's own animal."),

 dict(ref=(4,24), op="AT_THE_OLAH_PLACE",
  en="And he shall lean his hand on the goat's head and slaughter it in the place where one slaughters the burnt-offering before the LORD: it is a sin-offering.",
  tl_en="lean the hand on the goat's head",
  tr_en="slaughtered at the burnt-offering's place before the LORD: a sin-offering",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(seir_ha_chatat) THEN(samakh_yado ∧ shachat_bi_meqom_asher_yishchat_et_ha_ola)",
    frag=("ve-samakh",14), prose="""
AN ADDRESS BY REFERENCE [CROWN 4]. ve-shachat oto BI-MEQOM
ASHER yishchat et ha-ola ("slaughter it IN THE PLACE WHERE
one slaughters the burnt-offering"): the third subroutine
call - not a place-name but a pointer into the olah's law
(Lev 1:11's north side). Classification: chatat HU. The
blood, from here down, will never enter the tent [THE TREE].
HANDLERS 18."""),
  ],
  comment="The leader's geography is a pointer; his blood stays outside."),

 dict(ref=(4,25), op="OUTER_HORNS",
  en="And the priest shall take of the sin-offering's blood with his finger and put it on the horns of the altar of burnt-offering; and its blood he shall pour out at the base of the altar of burnt-offering.",
  tl_en="the sin-offering's blood taken with the finger",
  tr_en="on the burnt-offering altar's horns; the rest at its base",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(mi_dam_ha_chatat) THEN(natan_be_etzbao_al_qarnot_mizbach_ha_ola ∧ yishpokh_el_yesod)",
    frag=("ve-laqach",17), prose="""
THE BLOOD STAYS OUT. ve-natan al qarnot mizbach HA-OLA ("on
the horns of the BURNT-OFFERING altar") - branch one put
blood on the incense altar's horns INSIDE; the leader's
blood reaches only the courtyard altar: rank measured in
meters. No sevenfold sprinkling, no veil. etzba tok 6/18;
base-pouring 3 of 5. HANDLERS 19."""),
  ],
  comment="Same gestures, outer address: the tree's grading made spatial."),

 dict(ref=(4,26), op="LEADER_FORGIVEN",
  en="And all its fat he shall burn on the altar like the fat of the sacrifice of well-being; and the priest shall atone for him from his sin, and he shall be forgiven.",
  tl_en="all the fat burned like the well-being sacrifice's fat",
  tr_en="the priest atones for him from his sin and he is forgiven",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(kol_chelbo_ke_chelev_zevach_ha_shelamim) THEN(yaqtir ∧ kiper ∧ nislach_lo)",
    frag=("ve-et",14), prose="""
PARDON TWO. ke-chelev zevach ha-shelamim ("LIKE the fat of
the well-being sacrifice") - the fourth cross-call [CROWN 4];
ve-khiper alav ha-kohen ME-chatato ("and the priest shall
atone for him FROM his sin") ve-nislach LO ("and HE shall be
forgiven" - singular now; 4:20 forgave a plural them): the
refrain conjugates per branch. kipper 14/79, nislach 3/20.
HANDLERS 20."""),
  ],
  comment="The leader is forgiven in the singular."),

 dict(ref=(4,27), op="BRANCH_FOUR_THE_COMMONER",
  en="And if one soul of the people of the land sins in inadvertence, by doing one of the commandments of the LORD which shall not be done, and becomes guilty -",
  tl_en="if one soul of the people of the land sins in inadvertence",
  tr_en="doing one forbidden commandment, and becomes guilty",
  ops=[
   dict(op="CASE",
    expr="CASE(nefesh_me_am_ha_aretz, techeta_vi_shegaga) ROUTE(ve_ashem)",
    frag=("ve-im",7), prose="""
THE PEOPLE OF THE LAND. ve-im NEFESH ACHAT me-AM HA-ARETZ
("and if ONE SOUL of the PEOPLE OF THE LAND") - the intake's
nefesh (4:2) returns as the fourth branch's subject: the
commoner is the root case's own noun, one soul among the
land's people (am toks 209-210/445 in-span pair: 4:3's
ha-am whom the priest's sin guilts, 4:27's am ha-aretz who
sin one at a time). The formula's third refrain (mitzvot
tok 9/66); ve-ashem (816, 3/13). CASES 5."""),
  ],
  comment="The tree descends to one soul of the land."),

 dict(ref=(4,28), op="THE_SHE_GOAT",
  en="or his sin which he sinned is made known to him - then he shall bring his offering: a she-goat of the goats, unblemished, a female, for his sin which he sinned.",
  tl_en="or his sin is made known to him",
  tr_en="he brings an unblemished female she-goat for his sin",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(o_hoda_elav_chatato) THEN(hevi_qarbano_seirat_izim_temima_neqeva)",
    frag=("o",12), prose="""
THE TARIFF GRADES DOWN AND FEMININE. o hoda elav (the
know-trigger's third firing, 3045 tok 105/174) - ve-hevi
qarbano SEIRAT izim TEMIMA NEQEVA ("a SHE-GOAT of the goats,
unblemished, FEMALE") - seirat debuts (8166, 1/2; its only
other token is Lev 5:6's same tariff); the
unblemished-adjective turns feminine with the victim
(temima, 8549 tok 12/47); neqeva (5347 tok 9/21 - Gen
1:27's creation-word as a tariff line). HANDLERS 21."""),
  ],
  comment="One rank down, the victim turns female."),

 dict(ref=(4,29), op="LEAN_AND_SLAUGHTER",
  en="And he shall lean his hand on the sin-offering's head and slaughter the sin-offering in the place of the burnt-offering.",
  tl_en="lean the hand on the sin-offering's head",
  tr_en="slaughter it in the burnt-offering's place",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(ha_chatat) THEN(samakh_yado ∧ shachat_bi_meqom_ha_ola)",
    frag=("ve-samakh",11), prose="""
THE VICTIM BECOMES ITS OFFICE. ve-samakh... al rosh
HA-CHATAT ve-shachat et HA-CHATAT ("on the head of THE
SIN-OFFERING... slaughter THE SIN-OFFERING") - branches one
to three said bull and goat; the commoner's verses call the
animal by its function alone (chatat toks 27-28/142, the
noun twice in one verse): the tree's leaf-level names the
role, not the beast. Semikha 4 of 5. HANDLERS 22."""),
  ],
  comment="At the tree's bottom the animal is just 'the sin-offering'."),

 dict(ref=(4,30), op="FINGER_HORNS_BASE",
  en="And the priest shall take of its blood with his finger and put it on the horns of the altar of burnt-offering; and all its blood he shall pour out at the base of the altar.",
  tl_en="its blood taken with the priest's finger",
  tr_en="on the burnt-offering altar's horns; all the rest at the base",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(mi_damah) THEN(natan_be_etzbao_al_qarnot_mizbach_ha_ola ∧ yishpokh_el_yesod_ha_mizbecha)",
    frag=("ve-laqach",16), prose="""
HER BLOOD. ve-laqach ha-kohen mi-DAMAH ("of HER blood" - the
feminine suffix tracking the she-goat, dama-h toks 60-61/166)
be-etzbao (finger 7/18) al qarnot mizbach ha-ola - outer
horns again; base-pouring 4 of 5. HANDLERS 23."""),
  ],
  comment="The rite runs unchanged; only the pronoun turned feminine."),

 dict(ref=(4,31), op="THE_PLEASING_AROMA",
  en="And all its fat he shall remove, as fat is removed from the sacrifice of well-being, and the priest shall burn it on the altar for a pleasing aroma to the LORD; and the priest shall atone for him, and he shall be forgiven.",
  tl_en="all the fat removed as from the well-being sacrifice",
  tr_en="burned for a pleasing aroma; the priest atones and he is forgiven",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(kol_chelbah_ka_asher_husar_me_al_zevach_ha_shelamim) THEN(hiqtir_le_recha_nichocha ∧ kiper ∧ nislach_lo)",
    frag=("ve-et",21), prose="""
ONLY THE COMMONER'S GOAT PLEASES [CROWN 8]. ka-asher HUSAR
chelev me-al zevach ha-shelamim ("as fat IS REMOVED from the
well-being sacrifice" - hophal cross-call five [CROWN 4];
sur toks 31-32/55 in one verse, active-then-passive) -
ve-hiqtir ha-kohen ha-mizbecha LE-RECHA NICHOCHA la-YHWH
("for a PLEASING AROMA to the LORD"): the phrase born on
Noah's altar (Gen 8:21, both nouns' tok1) fires ONCE in this
chapter [VERIFIED] - not for the priest's bull or the
leader's goat but here, the common soul's she-goat. Pardon
three: kipper 15/79, nislach 4/20. HANDLERS 24."""),
  ],
  comment="Of the four victims, the letter smells only the lowest one."),

 dict(ref=(4,32), op="THE_LAMB_ALTERNATIVE",
  en="And if he brings a lamb as his offering for a sin-offering, an unblemished female shall he bring.",
  tl_en="if he brings a lamb as his sin-offering",
  tr_en="an unblemished female shall he bring",
  ops=[
   dict(op="CASE",
    expr="CASE(keves, ve_im_yavi_le_chatat) ROUTE(neqeva_temima_yeviena)",
    frag=("ve-im",8), prose="""
THE TREE'S LAST FORK. ve-im KEVES yavi qarbano le-chatat
("and if a LAMB he brings as his offering") - the only
branch keyed to the VICTIM's species rather than the
sinner's rank (keves, 3532 tok 7/87): within the commoner's
case, goat or lamb - the letter's ve-im runs one level
deeper than the agent-classes. neqeva temima yeviena ("an
unblemished female shall he BRING-HER" - Vhi3ms with the 3fs
suffix: the she-lamb carried inside the verb). CASES 6."""),
  ],
  comment="One fork below rank: the commoner alone gets a choice of species."),

 dict(ref=(4,33), op="LEAN_AND_SLAUGHTER_HER",
  en="And he shall lean his hand on the sin-offering's head and slaughter it for a sin-offering in the place where one slaughters the burnt-offering.",
  tl_en="lean the hand on the sin-offering's head",
  tr_en="slaughter it where the burnt-offering is slaughtered",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(ha_chatat) THEN(samakh_yado ∧ shachat_otah_le_chatat_bi_meqom_asher_yishchat_et_ha_ola)",
    frag=("ve-samakh",14), prose="""
THE POINTER AGAIN. ve-shachat otah le-chatat BI-MEQOM ASHER
yishchat et ha-ola - the place-by-reference re-cited
verbatim-class from 4:24 (cross-call six [CROWN 4]); the
fifth and last semikha (5564 tok 13/23); shachat's seventh
in-span token closes the span's slaughter-census (7819 toks
14-20/47). HANDLERS 25."""),
  ],
  comment="The last hand leans; the last knife falls at the referenced place."),

 dict(ref=(4,34), op="THE_LAST_BLOOD",
  en="And the priest shall take of the sin-offering's blood with his finger and put it on the horns of the altar of burnt-offering; and all its blood he shall pour out at the base of the altar.",
  tl_en="the sin-offering's blood taken with the finger",
  tr_en="on the burnt-offering altar's horns; all the rest at the base",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(mi_dam_ha_chatat) THEN(natan_be_etzbao_al_qarnot ∧ yishpokh_kal_damah_el_yesod)",
    frag=("ve-laqach",17), prose="""
BASE-POURING FIVE OF FIVE. ve-laqach... be-etzbao (the
finger's fifth and last in-span token, 676 tok 8/18) ve-et
kal damah yishpokh el yesod ha-mizbecha - yesod tok 6/9 and
shafakh tok 10/22: the pour-at-the-base line has now run
once per victim, five for five. HANDLERS 26."""),
  ],
  comment="Every victim's blood ends at the same base."),

 dict(ref=(4,35), op="THE_WALL_FOURTH_PARDON",
  en="And all its fat he shall remove, as the lamb's fat is removed from the sacrifice of well-being, and the priest shall burn them on the altar upon the fire-offerings of the LORD; and the priest shall atone for him, for his sin which he sinned, and he shall be forgiven.",
  tl_en="all the fat removed as the well-being lamb's fat",
  tr_en="burned on the LORD's fire-offerings; atoned, and he is forgiven",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(kol_chelbah_ka_asher_yusar_chelev_ha_kesev) THEN(hiqtir_al_ishe_YHWH ∧ kiper ∧ nislach_lo)",
    frag=("ve-et",26), prose="""
THE WALL [MACHINE SHAPE]. ka-asher YUSAR chelev HA-KESEV
mi-zevach ha-shelamim ("as the LAMB's fat is removed from
the well-being sacrifice" - the eighth and last cross-call
[CROWN 4]; kesev 3775 tok 7/13) - ve-hiqtir... al ISHE YHWH
("upon the FIRE-OFFERINGS of the LORD", 801 tok 20/63) -
ve-khiper alav ha-kohen al chatato asher chata ve-NISLACH lo:
pardon four (kipper 16/79, nislach 5/20 - the forgive-verb's
Exod 34:9 debut plus these four = its first five tokens).
UNIT END: SPECS depth 1 OPEN (the relay card - Moses'
speaking never narrated); CASES 6; HANDLERS 27; STATUTES 0;
REGISTRY 0 [VERIFIED: zero qara-lemma tokens]; TESTS 0
[VERIFIED: zero tov-adjective tokens]. The casuistic probe's
answer: a four-rank tree with sub-branches, graded blood,
graded gender, and eight self-citations - encoded with ZERO
new operators. HANDLERS 27."""),
  ],
  comment="Four branches, four pardons, one branch left at the ash-heap, one card still open."),
]

# ---------------------------------------------------------------------------

def _s(id, ref, frag, title, given, expect, occ=1):
    d = dict(id=id, ref=ref, frag=frag, title=title, given=given, expect=expect)
    d["occ"] = occ
    return d

DB = "LET(daber_el_bene_yisrael(moshe)) pushed and OPEN;"
NTN = "no test, no name."

SCENS = [
 _s("S1", (4,1), ("va-yedaber",5),
    "after STEP_Lv_4_1 — the frame: one narrative verb",
    "The LORD spoke to Moses, saying.",
    ["SPECS empty;", NTN]),
 _s("S2", (4,2), ("nefesh",4),
    "after STEP_Lv_4_2 — the relay card pushed; the intake case installed",
    "Speak to the sons of Israel: a soul that sins in inadvertence.",
    [DB, "Facts case-shegaga HOLD;", "STATUTES 0 standing;", NTN]),
 _s("S3", (4,3), ("im",6),
    "after STEP_Lv_4_3 — branch one: the anointed priest",
    "If the anointed priest sins to the guilt of the people.",
    [DB, "Facts case-mashiach HOLD;", NTN]),
 _s("S4", (4,4), ("ve-hevi",9),
    "after STEP_Lv_4_4 — the sin-offering brought to the door",
    "Bring the bull to the tent's entrance; lean; slaughter.",
    [DB, "Facts handler-petach HOLD;", NTN]),
 _s("S5", (4,5), ("ve-laqach",10),
    "after STEP_Lv_4_5 — the blood enters the tent",
    "The anointed priest brings the blood into the tent.",
    [DB, "Facts handler-laqach HOLD;", NTN]),
 _s("S6", (4,6), ("ve-taval",5),
    "after STEP_Lv_4_6 — seven times before the veil",
    "Dip the finger; sprinkle seven times before the veil.",
    [DB, "Facts handler-parokhet HOLD;", NTN]),
 _s("S7", (4,7), ("ve-natan",9),
    "after STEP_Lv_4_7 — incense horns and olah base",
    "Blood on the incense altar's horns; the rest at the base.",
    [DB, "Facts handler-qetoret HOLD;", NTN]),
 _s("S8", (4,8), ("ve-et",7),
    "after STEP_Lv_4_8 — the fat lifted",
    "All the sin-offering bull's fat lifted from it.",
    [DB, "Facts handler-mekhase HOLD;", NTN]),
 _s("S9", (4,9), ("ve-et",9),
    "after STEP_Lv_4_9 — kidneys and lobe",
    "The two kidneys and the lobe on the liver removed.",
    [DB, "Facts handler-yesirena HOLD;", NTN]),
 _s("S10", (4,10), ("ka-asher",5),
    "after STEP_Lv_4_10 — the first subroutine call",
    "As it is lifted from the well-being ox; burned on the altar.",
    [DB, "Facts handler-yuram HOLD;", NTN]),
 _s("S11", (4,11), ("ve-et",12),
    "after STEP_Lv_4_11 — the verbless carcass list",
    "The hide, flesh, head, legs, entrails, dung.",
    [DB, "Facts handler-yuram HOLD;", NTN]),
 _s("S12", (4,12), ("ve-hotzi",10),
    "after STEP_Lv_4_12 — outside the camp; no pardon closes branch one",
    "The whole bull burned at the ash-pouring-place.",
    [DB, "Facts handler-shefekh HOLD;", NTN]),
 _s("S13", (4,13), ("ve-im",9),
    "after STEP_Lv_4_13 — branch two: the congregation's hidden thing",
    "If the whole congregation errs and it is hidden.",
    [DB, "Facts case-nelam HOLD;", NTN]),
 _s("S14", (4,14), ("ve-noda",6),
    "after STEP_Lv_4_14 — the sin becomes known",
    "The sin becomes known; the assembly offers a bull.",
    [DB, "Facts handler-noda HOLD;", NTN]),
 _s("S15", (4,15), ("ve-samkhu",10),
    "after STEP_Lv_4_15 — the elders' hands",
    "The elders lean their hands; the bull is slaughtered.",
    [DB, "Facts handler-ziqne HOLD;", NTN]),
 _s("S16", (4,16), ("ve-hevi",8),
    "after STEP_Lv_4_16 — the anointed carries the blood in",
    "The anointed priest brings the blood into the tent.",
    [DB, "Facts handler-mashiach HOLD;", NTN]),
 _s("S17", (4,17), ("ve-taval",7),
    "after STEP_Lv_4_17 — the veil's second seven",
    "Dip and sprinkle seven times before the veil.",
    [DB, "Facts handler-ha_parokhet HOLD;", NTN]),
 _s("S18", (4,18), ("u-min",12),
    "after STEP_Lv_4_18 — horns and base again",
    "Blood on the altar before the LORD; the rest at the base.",
    [DB, "Facts handler-yiten HOLD;", NTN]),
 _s("S19", (4,19), ("ve-et",7),
    "after STEP_Lv_4_19 — the fat-rite compressed",
    "All its fat lifted and burned on the altar.",
    [DB, "Facts handler-hiqtir_ha_mizbecha HOLD;", NTN]),
 _s("S20", (4,20), ("ve-asa",9),
    "after STEP_Lv_4_20 — branch two calls branch one; the first pardon",
    "Do as with the first bull; atoned, and forgiven.",
    [DB, "Facts handler-nislach_lahem HOLD;", NTN]),
 _s("S21", (4,21), ("ve-hotzi",13),
    "after STEP_Lv_4_21 — 'the first bull' cited; the assembly's chatat",
    "Burned as the first bull; it is the assembly's sin-offering.",
    [DB, "Facts handler-ha_rishon HOLD;", NTN]),
 _s("S22", (4,22), ("asher",3),
    "after STEP_Lv_4_22 — branch three: the leader, opened by asher",
    "When a leader sins - the commandments of the LORD his God.",
    [DB, "Facts case-nasi HOLD;", NTN]),
 _s("S23", (4,23), ("o",7),
    "after STEP_Lv_4_23 — made known: the male goat",
    "Or his sin is made known: a male goat, unblemished.",
    [DB, "Facts handler-seir HOLD;", NTN]),
 _s("S24", (4,24), ("ve-samakh",14),
    "after STEP_Lv_4_24 — slaughtered at the olah's place",
    "Lean; slaughter where the burnt-offering is slaughtered.",
    [DB, "Facts handler-bi_meqom HOLD;", NTN]),
 _s("S25", (4,25), ("ve-laqach",10),
    "after STEP_Lv_4_25 — the outer horns",
    "Blood on the burnt-offering altar's horns; the rest at its base.",
    [DB, "Facts handler-qarnot HOLD;", NTN]),
 _s("S26", (4,26), ("ve-et",14),
    "after STEP_Lv_4_26 — the leader forgiven, singular",
    "Fat like the well-being sacrifice; atoned, forgiven.",
    [DB, "Facts handler-nislach_lo HOLD;", NTN]),
 _s("S27", (4,27), ("ve-im",7),
    "after STEP_Lv_4_27 — branch four: one soul of the land",
    "If one soul of the people of the land sins.",
    [DB, "Facts case-am_ha_aretz HOLD;", NTN]),
 _s("S28", (4,28), ("o",12),
    "after STEP_Lv_4_28 — the she-goat, unblemished, female",
    "Or made known: a female she-goat for his sin.",
    [DB, "Facts handler-temima HOLD;", NTN]),
 _s("S29", (4,29), ("ve-samakh",11),
    "after STEP_Lv_4_29 — the animal called by its office",
    "Lean on the sin-offering's head; slaughter the sin-offering.",
    [DB, "Facts handler-shachat HOLD;", NTN]),
 _s("S30", (4,30), ("ve-laqach",16),
    "after STEP_Lv_4_30 — her blood at horns and base",
    "Her blood on the horns; all the rest at the base.",
    [DB, "Facts handler-damah HOLD;", NTN]),
 _s("S31", (4,31), ("ve-et",21),
    "after STEP_Lv_4_31 — the one pleasing aroma; pardon three",
    "Burned for a pleasing aroma; atoned, and forgiven.",
    [DB, "Facts handler-nichocha HOLD;", NTN]),
 _s("S32", (4,32), ("ve-im",8),
    "after STEP_Lv_4_32 — the lamb fork",
    "If he brings a lamb: an unblemished female.",
    [DB, "Facts case-keves HOLD;", NTN]),
 _s("S33", (4,33), ("ve-samakh",14),
    "after STEP_Lv_4_33 — the last leaning at the referenced place",
    "Lean; slaughter it where the burnt-offering is slaughtered.",
    [DB, "Facts handler-le_chatat HOLD;", NTN]),
 _s("S34", (4,34), ("ve-laqach",17),
    "after STEP_Lv_4_34 — base-pouring five of five",
    "Blood on the horns; all her blood at the base.",
    [DB, "Facts handler-yesod HOLD;", NTN]),
 _s("S35", (4,35), ("ve-et",26),
    "after STEP_Lv_4_35 — the wall: four pardons, zero statutes, one open card",
    "The lamb's fat burned; atoned, and he is forgiven.",
    [DB, "Facts handler-ishe HOLD;", "STATUTES 0 standing;", NTN]),
]
