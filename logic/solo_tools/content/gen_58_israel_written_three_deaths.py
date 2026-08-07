# -*- coding: utf-8 -*-
"""Authored content for gen_58 (35:1-29). DB evidence: gen58_prestage_full.txt
(regenerable: python3 logic/solo_tools/prestage.py Gen 35:1-35:29) + targeted
queries logged in the derivation session 2026-08-07."""

UID = "gen_58_israel_written_three_deaths"
BOOK = "Gen"
SPAN = (35, 1, 35, 29)
EXTRA_SUBS = {
    # 35:3's et-y is the object-marker (853): "the El who answered ME".
    "et-y": "oti",
    # NOTE: "et-o" stays RAW throughout this unit — the span mixes the
    # object-marker (oto: 35:9 blessed-him, 35:29 buried-him) with the
    # with-preposition (ito: 35:13,14,15 spoke-WITH-him); a single subs
    # key cannot carry both readings (im-o/bi-y class; subs.py NOTE).
}


META = [
    ("id", "gen_58_israel_written_three_deaths"),
    ("title_en", '"Bethel again: Israel written, three deaths on the road (35:1-29)"'),
    ("title_he", "וַיִּקְרָא אֶת־שְׁמוֹ יִשְׂרָאֵל"),
    ("title_he_translit", "va-yiqra et-shemo yisrael"),
    ("title_he_en", "\"'And He called his name Israel'\""),
    ("book_he", "בְּרֵאשִׁית"),
    ("book_he_translit", "Be-reshit"),
    ("book_en", "Genesis"),
    ("refs", "35:1-29"),
    ("unit_span_planned", "35:1-29"),
]

DRAFT_NOTE = """
DRAFT 2026-08-07 · SOLO ERA unit #12 (Claude coordinator+deriver;
external fresh-context adversarial review before freeze per standing
law). Span: 35:1-29, whole chapter: 29 verses · 378 tokens
(SNAPSHOT-verified). SNAPSHOT + debut_map. bar C. Conventions: step
he: = plain (no accents/meteg; maqqef ־ per snapshot); tree halves =
accents kept, slashes stripped; split at etnachta — 26 of 29 verses
carry one; the three without (35:15, 35:24, 35:25) split at the
prestage fallback (tifcha idx9; zaqef qatan idx1; zaqef qatan idx3 —
the strongest-disjunctive rule). No ketiv in span. Onkelos BUFFER
PENDING.

UNIT SHAPE — NINE pushes, ZERO pops: a SECOND nine-open wall, back to
back with gen_57's — the corpus's two largest all-open walls now sit
in consecutive units, and they are OPPOSITES: gen_57's nine died
refused and unperformed; gen_58's nine die OBEYED — every commanded
thing happens, and not one commanded VERB ever returns as narrated
deed. The obedience chapter never repeats a single commanded root in narration
of the demandee's compliance; the one commanded root that does
narrate (alah, 35:13) has GOD, not the demandee, as its subject.
The letter answers every imperative in a different verb:
arise/go-up → they JOURNEY and Jacob COMES (nasa 35:5, bo 35:6);
dwell (yashav) → Israel ABIDES (shakhan, 35:22 — the near-synonym,
other root); make an altar (asa) → he BUILDS it (bana, 35:7); remove
the gods (sur) → they are GIVEN and HIDDEN (natan + taman, 35:4);
purify / change garments → never narrated at all; be-fruitful-and-
multiply → horizon; fear-not → Rachel dies. Under the standing
letter-law (gen_45 Excerpt B: performance in another root never
pops; gen_54's liqtu→va-yiqchu; gen_57's shama+mul compliance) all
nine cards stand OPEN at the wall over a chapter of visible
obedience — the mismatch family gains its COMPLIANCE class.

THE NINE, in queue order:
(1-3) 35:1 — God's command-chain to Jacob, split per the standing
bundling rules: LET(qum_ale(yaaqov, bet_el)) — the arise-aux rides
the travel-verb (gen_47's qum-chains; gen_56's nisa-ve-nelekha
travel-pair class); LET(shev_sham(yaaqov, bet_el)) — the
dwell-obligation; LET(ase_sham_mizbeach(yaaqov, la_el_ha_nire)) —
the altar-task (distinct obligations = distinct cards, gen_57's
settlement-triple class). The go-up card's root alah performs
in-span ONCE in narration — at 35:13, with GOD as subject, ascending
FROM Jacob: the demanded verb's only narrated token is the wrong
performer in the opposite direction. The altar-card's asa is
answered by va-YIVEN (bana, 35:7) — the thing made, the verb
swapped. The dwell-card's yashav never recurs (3427 in-span: the
imperative only); 35:22's bi-shekon is shakhan, the other
abide-root.
(4-6) 35:2 — Jacob's purge-triple on his house: LET(hasiru(bet_
yaaqov, et_elohe_ha_nekhar)) — answered at 35:4 by va-yitnu (GIVE)
and va-yitmon (HIDE): two other roots do the removing, sur never
returns; LET(hitaharu(bet_yaaqov)) — THE PURIFY-VERB'S TORAH DEBUT
[CROWN 2], never performed in-span; LET(hachalifu(bet_yaaqov,
simlotekhem)) — the garment-change, never narrated (simla's next
token is 37:34 — Jacob TEARING his garments over Joseph).
(7) 35:3 — CMD-US?(naquma_ve_naale(bet_yaaqov, bet_el)) — Jacob's
1cp cohortative pair (ve-naquma ve-naale, HC/Vqh1cp ×2), one card
per gen_56's nisa-ve-nelekha travel-pair precedent, TIR-033's
?-guard; the group then JOURNEYS (va-yisu, nasa) — other root,
card open.
(8) 35:11 — LET(pere_u_reve(yisrael)) — THE ONLY SINGULAR
BE-FRUITFUL-AND-MULTIPLY IN THE TORAH [VERIFIED: full morph census
of 6509 + 7235 — each root has exactly ONE Vqv2ms token, both in
this verse]: the pair spoken to sea-creatures, humanity, and Noah
as plural blessing (1:22, 1:28, 9:1, 9:7) arrives ONCE as a
singular command — to the man just named Israel; one card (the
fixed merism, gen_56's pair class). Horizon: 47:27's va-yifru
va-yirbu (Israel-the-people, in Goshen).
(9) 35:17 — LET-NOT(tiri(rachel)) — the midwife's fear-not: al +
true jussive (HVqj2fs), gen_54's LET-NOT class; the fear-verb never
returns in-span; the next verse is her death. OPEN.
The volitive census (12: 9 imperatives + 2 cohortatives + 1
jussive) is fully accounted: nine cards, every volitive token
inside a pushed card (two arise-auxes absorbed into their travel
cards; the fruit-multiply merism one card), ZERO fenced.

CROWN 1 — THE DECREE AND THE FORMULA IN ONE VERSE (35:10): va-yomer
lo Elohim shimkha yaaqov — then the DECREE grammar: lo yiqare
shimkha od yaaqov ki im yisrael yihye shemekha (negated imperfect +
nominal clause — 17:5/15's and 32:29's exact class, which WRITES
NOTHING, gen_33's law) — and then, same verse: VA-YIQRA et shemo
yisrael — the narrative formula, which WRITES. The registry takes
name(yaaqov) := yisrael three chapters after 32:29's decree
withheld it — decree and formula side by side in one verse, and
only the formula moves the machine [thesis specimen]. THE
COUNTERSIGN: the narrator's FIRST use of Israel for the man is
35:21 va-yisa yisrael (3478 tok7/587) — AFTER the write, never
before it [VERIFIED: toks 1-6 = two decrees' speech, the
people-law, the altar-title, the jurisdiction, the formula's own
object]; and the narrator still writes yaaqov EIGHT more times
in-span after the write (toks 132-139 — the last is 35:29's own
burial-verse ve-yaaqov) — the census shows a
formula-write beginning a usage and retiring nothing: last-write-
wins, not erasure (the inverse of 17:5's avram-dies-instantly
letter-proof, extending gen_55's care 13).

CROWN 2 — THE PURITY-PAIR BORN IN CONSECUTIVE CHAPTERS: tamei
("defile", 2930) entered the Torah at 34:5 — ON DINAH (gen_57
CROWN 4); taher ("purify", 2891) enters at 35:2 — in Jacob's purge
command, ONE CHAPTER LATER [VERIFIED: debut_map — tok1/54; toks
2+ = Lev 11:32 onward]. The codebook's defining verb-pair debuts
back to back, defilement in the outrage chapter, purification in
the response — and both careers run straight to Leviticus (tamei
114 tokens, taher 54: the codebook's verb-pair, born in these two
family chapters).

CROWN 3 — LAST-WRITE-WINS, TWICE: (a) 35:7 va-yiqra la-maqom EL
BET-EL (write) → 35:15 va-yiqra yaaqov et shem ha-maqom... BET-EL
(write): the same place-key written twice by the same namer, the
El-prefixed name reduced to the plain one — registry ends bet_el;
(b) 35:18 va-tiqra shemo BEN-ONI ("son of my sorrow" — the dying
mother's formula write) → ve-aviv qara lo VINYAMIN ("son of the
right hand" — the father's overwrite, gen_54's 31:47 qara-lo write
class): registry ends binyamin — the machine's last-write-wins law
enacting the story's own grief: her name for him exists in the
ledger one write deep, and the Torah never uses it again
[binyamin 1144 toks 2-31 all Binyamin; ben-oni 1126 tok1/1 HAPAX].

CROWN 4 — THE CULT KIT SEEDED AT BETHEL (35:14): nesekh
("libation", 5262 tok1/41 DEBUT — the drink-offering noun is born
on Jacob's pillar; toks 2+ = the tamid and festival libations,
Exod 29:40 onward); va-yitzoq ("poured", 3332 tok2/19 — tok1 =
28:18, the SAME MAN pouring oil on the SAME PILLAR: the pour-verb's
first two tokens are Jacob's two Bethel anointings, twenty years
apart; career → the anointing of Aaron, Exod 29:7, Lev 8:12);
shemen ("oil", 8081 tok2/106 — same pair: 28:18 then here; tok3
opens the Mishkan's oil, Exod 25:6); matzeva ("pillar", 4676 toks
8-9/16 — career ends BANNED: Lev 26:1, Deut 16:22 "you shall not
set up a pillar, which YHWH hates" — the stone Jacob raises twice
becomes the stone the law forbids); matzevet (4678 toks 1-2/2 —
WHOLE CAREER IN-SPAN: the Bethel stone and Rachel's grave-stone,
both Jacob's, one unit).

CROWN 5 — GOD-GOES-UP, EXACTLY TWICE: va-yaal (me-al...) Elohim —
the God-ascends formula occurs exactly TWICE in the Torah
[VERIFIED: full 5927 census against adjacent Elohim]: 17:22 (up
from ABRAHAM — closing the chapter of the Abram→Abraham and
Sarai→Sarah DECREES, which wrote nothing) and 35:13 (up from
JACOB — closing the theophany whose formula WROTE Israel): the two
renaming theophanies, and only they, end with God ascending — one
sealed a decree the registry refused, the other a write it took.

CROWN 6 — BETHLEHEM EXISTS ONLY AT RACHEL'S GRAVE: bet lachem
(1035/1035+ toks 1/2 + 1/2) — Bethlehem's ONLY two Torah token-
pairs are 35:19 (hiv bet lachem — her burial verse) and 48:7
(Jacob's deathbed RETELLING of this very death). So too kivrat
ha-aretz ("a stretch of land", 3530 1/2 + 48:7) and efrata (672
toks 1-2 here, 3-4 = 48:7): the death-scene's entire rare
vocabulary recurs nowhere but in the dying Jacob's own retelling
of it — event and memory, and nothing between.

CARE-POINTS (ordinals from debut_map via prestage unless tagged):
(1) 35:1 THE COMMAND-CHAIN [cards 1-3]: qum ale vet-el (6965
tok39/145; 5927 tok17/201; 1008 tok7/13) — God's Bethel-order;
ve-shev sham (3427 tok50/199); va-ase sham mizbecha (6213
tok115/860; 4196 tok11/198); la-el ha-nire elekha (410 tok12/50;
7200 tok88/396 — "the El who APPEARED to you", nifal participle)
BE-VARCHAKHA mi-pene esav achikha — GOD NAMES THE FLIGHT: berach
(1272 tok8/14) — gen_53's filed arm lands: "when you FLED from
Esau your brother" — the flee-verb Jacob never performed in
gen_47's span (he went; he never fled) is now the verb God uses
for that journey, and 35:7's narrator echoes it (be-varcho, tok9)
— the flight named twice in the chapter that ends it.
(2) 35:2 THE PURGE-TRIPLE [cards 4-6; CROWN 2]: hasiru et elohe
ha-nekhar (5493 tok6/55; 5236 tok3/8 — the foreign-noun nekhar:
career → Exod 12:43's ben-nekhar Passover exclusion, Deut 31:16's
elohe nekhar covenant-breach — the phrase's future is apostasy
law); ve-hitaharu (2891 tok1/54 DEBUT); ve-hachalifu simlotekhem
(2498 tok3/5 — the change-verb of Laban's wage-switches 31:7,41
now aimed at garments; 8071 simla tok2/19 — next token 37:34,
Jacob TEARS the garments he here orders changed).
(3) 35:3 THE COHORTATIVE PAIR [card 7]: ve-naquma ve-naale bet-el
(HC/Vqh1cp ×2) — TIR-033 CMD-US?; la-el ha-one oti be-yom tzarati
(6030 tok14/48 — "who ANSWERED me"; 6869 tzara tok1/5 DEBUT — the
distress-noun born in Jacob's testimony; toks 2-3 = 42:21, the
brothers' confession over Joseph: "we saw the DISTRESS of his
soul... therefore this DISTRESS has come" — the word debuts in
the father's rescue-story and returns in the sons' guilt);
va-yehi imadi ba-derekh (5978 tok12/19 — the with-me formula of
28:20's vow: the vow's own word quoted back as fulfilled).
(4) 35:4 THE HANDOVER [cards 4-6's other-root answers]: va-yitnu
el yaaqov (5414 tok94/647) — THE GIVE-VERB'S FIRST NARRATED
PERFORMANCE SINCE THE GEN_57 NEGOTIATION THAT NEVER GAVE: eight
give-tokens haggled over a daughter and gave nothing; token 94
hands over gods and earrings; ve-et ha-nezamim asher be-aznehem
(5141 tok4/7) — THE EARRING'S LEDGER: toks 1-3 = the bride-ring
on Rebekah (24:22,30,47), tok4 = buried under the terebinth, toks
5-6 = Exod 32:2-3 — THE GOLDEN CALF'S RINGS ("break off the
rings in your ears") — tok7 = Exod 35:22, the Mishkan freewill
offering: bride-gift, buried idol-freight, calf, sanctuary — the
one ornament walks the whole ledger of devotion; va-yitmon (2934
tok1/3 DEBUT) — the hide-verb's three tokens: Jacob hides the
gods, Moses hides the Egyptian (Exod 2:12), the sand's hidden
treasures (Deut 33:19); tachat ha-ela (424 tok1/1 HAPAX — the
terebinth appears once; with 35:8's oak the chapter holds TWO
tree-hapaxes [see (8)]).
(5) 35:5 THE UN-PURSUIT: va-yisu — the etnachta stands on the
verse's FIRST TOKEN: 35:5 is one of the corpus's TWELVE
first-word splits [gen_57 CROWN 2d's census] — and the LAST unit
held another (34:31): two of the twelve in consecutive units;
chitat Elohim (2847 tok1/1 HAPAX) — the God-terror, said once
ever, answering 34:30's fear; ve-lo RADFU (7291 tok4/25) — the
pursue-verb: tok3 was LABAN'S pursuit (31:23); tok4 is the
pursuit that does NOT happen — negated; career → Pharaoh's
pursuit (Exod 14 ×4, 15:9) and the covenant-curse pursuits
(Lev 26 ×7, blessing-side and curse-side): Jacob's feared
gathering (34:30 ve-neesfu) is
answered by a hapax terror and a negated verb.
(6) 35:6-7 ARRIVAL AND ALTAR [cards 1-3 held open]: va-yavo
yaaqov luzah (935 tok123/619; 3870 luz tok2/3) — he COMES (bo);
the commanded alah never narrates for him; va-YIVEN sham
mizbecha (1129 tok16/41) — he BUILDS the altar he was told to
MAKE (bana for asa — the other-root answer); WRITE #1: va-yiqra
la-maqom EL BET-EL (7121 tok83/193) — the place named with El
riding the name (33:20's el-elohe-yisrael altar-title class,
now on a maqom); ki sham NIGLU elav ha-Elohim (1540 tok2/33) —
the reveal-verb: tok1 = 9:21, Noah UNCOVERED in his tent
(va-yitgal); tok2 = the Elohim REVEALED at Bethel; career → Lev
18-20's uncover-nakedness cluster — shame, theophany, then the
forbidden uncoverings; the verb is PLURAL (niglu, HVNp3cp) with
ha-Elohim — morph letter-fact, filed as observation only.
(7) 35:8 THE NURSE NAMED AT DEATH [WRITE #2]: va-tamat devora
(1683 tok1/1 HAPAX; 4191 tok41/303) — Rebekah's nurse traveled
anonymous since 24:59 (meniqtah, 3243 tok2 — "her nurse", no
name) and receives her name IN HER DEATH-VERSE — the Torah's
only devora; mi-tachat le-vet-el tachat ha-alon (437 tok1/1
HAPAX — the oak, once ever); WRITE #2: va-yiqra shemo ALON
BAKHUT ("Oak of Weeping", 439+/439 both 1/1 HAPAX) — a hapax
person under a hapax tree with a hapax name; and rivqa (7259
tok29/30) — Rebekah's LAST living-narrative token: the Torah
never narrates her death; her nurse's death stands where hers
never will (tok30 = 49:31, the grave-list retell).
(8) 35:9-10 THE WRITE [CROWN 1; WRITE #3]: va-yera Elohim el
yaaqov OD ("again", 5750 tok29/95 — the second Bethel
theophany counted by the letter); u-verekh oto (1288 tok61/137);
then the decree-then-formula verse [CROWN 1]. REGISTRY takes
yisrael; the census countersign at 35:21.
(9) 35:11-12 EL SHADDAI'S PACKAGE [card 8]: ani el shaday (7706
tok3/9) — gen_47's frozen horizon LANDS (28:3's ve-EL SHADAY
yevarekh otekha... — Isaac's send-off blessing wished ve-YAFREKHA
ve-YARBEKHA, jussives, li-qehal AMIM): God now speaks AS El
Shaddai and turns the wished jussives into commanded imperatives
— PERE u-REVE [VERIFIED: 6509 tok9 = 28:3's jussive → tok10 =
35:11's imperative; 7235 tok22 → tok24 — the wished verbs return
as commands from the wished God, consecutive-but-one career
tokens] — and qehal AMIM becomes u-qehal GOYIM (6951 tok2/34;
career → Exod 12:6, the qahal of Israel at the Passover);
u-melakhim ME-CHALATZEKHA yetzeu — the kings-promise requoted
from 17:6 (u-melakhim MIM-KHA yetzeu [VERIFIED: token scan])
with one delta: from-YOU → from-your-LOINS — and chalatzayim
(2504 tok1/1 HAPAX) exists in the Torah only inside this delta;
35:12 the land-grant triple: natati... etnena... eten (5414 toks
95-97 — gave, will-give-it, will-give: one verse conjugates the
grant past, singular-future, and future).
(10) 35:13 GOD GOES UP [CROWN 5]: va-yaal me-alav Elohim —
the demanded alah's only narrated in-span token: wrong performer,
opposite direction [cards 1-3]; ba-maqom asher diber ito — the
spoke-with-him refrain opens (1696 toks 45-47/415: 35:13,14,15 —
three verses running).
(11) 35:14-15 PILLAR AND NAME [CROWN 4; WRITE #4]: the libation
and oil on the matzevet aven; WRITE #4: bet-el over el-bet-el —
last-write-wins pair (a) [CROWN 3]; the verse has no etnachta —
the split rides its tifcha (prestage fallback).
(12) 35:16-17 THE HARD BIRTH [card 9]: kivrat ha-aretz la-vo
efrata [CROWN 6]; va-TEQASH be-lidtah (7185 tok1/9 DEBUT) — THE
HARDNESS-VERB IS BORN IN RACHEL'S LABOR: toks 2 = ve-haqshotah
(same verse-pair), tok3 = 49:7's curse on Simeon-Levi's anger
(qashata), then the career HARDENS: Pharaoh's heart (Exod 7:3
aqshe, 13:15 hiqsha), Sihon's spirit (Deut 2:30), Israel's neck
(Deut 10:16 taqshu) — born in birth-pang, spent on hearts and
necks; ha-meyaledet (3205 tok142/205) — THE MIDWIFE enters the
Torah at Rachel's death-bed; the office's next bearer is 38:28
(Tamar's midwife at the twins' birth, tok156), then Exod
1:15-21's midwives who refuse Pharaoh — the office debuts
losing a mother and ends saving the sons; al-TIRI ki gam ze lakh ben
[card 9] — and GAM ZE ("this one TOO") is the letter's receipt
of 30:24's yosef-etiology: Rachel's fenced wish "may YHWH ADD
me ANOTHER son" (gen_51's yosef-class, the fence's own
namesake) lands at her death — the other son arrives, the
midwife's gam-ze counts him, and the adding costs the asker her
life (landing-note; the gen_51 ledger is untouched).
(13) 35:18 THE TWO NAMES [CROWN 3(b); WRITES #5-6]: be-tzet
nafshah ki meta — as her soul went out; ben-oni (1126 tok1/1) /
vinyamin (1144 tok1/31 DEBUT) — the mother's write, the
father's overwrite.
(14) 35:19-20 THE GRAVE [CROWN 6]: va-tamat rachel (4191 tok43)
va-tiqaver be-derekh efrata hiv BET LACHEM; matzevet qevurat
rachel AD HA-YOM — the to-this-day monument (fact-class: no
al-ken, no practice — a standing-object report, not a PATTERN;
observation filed); qevura (6900 toks 1-2/4) — the burial-noun
debuts ×2 on Rachel's marked grave; its LAST token is Deut 34:6
— MOSES' grave, which "no man knows": the noun's career runs
from the grave marked to-this-day to the grave no one can find.
(15) 35:21-22a ISRAEL MOVES [CROWN 1's countersign]: va-yisa
YISRAEL (3478 tok7 — the narrator's first Israel) va-yet aholo
me-hala le-migdal eder (4029+/4029 both 1/1 HAPAX — the
tower-of-the-flock, once ever); bi-shekon yisrael ba-aretz
ha-hiv — Reuben and Bilhah (7901 shakhav tok16/62 — gen_57's
armed next-violation lands; 1090 bilha tok6/9; 6370 pilegesh
tok3/4); VA-YISHMA yisrael — Israel HEARD — and the verse says
nothing more of him: the hear-then-silence of 34:5 repeated
without even a silence-verb; the reckoning waits for 49:4 ("you
went UP your father's bed" — the ascend-verb again).
(16) 35:22b-26 THE TWELVE: va-yihyu vene yaaqov SHENEM ASAR —
the count-verse lands immediately after the violation; the
mother-census follows: Leah's six, Rachel's two, the maids'
four; bene rachel (35:24, zaqef-split, no etnachta) — Rachel's
sons listed two verses after Rachel's death; bekhor yaaqov
reuven (1060 tok6/69) — the letter still titles Reuben FIRSTBORN
one verse after his violation (the title's revocation is 49:3-4
and 1 Chr's, outside); asher yulad lo BE-FADAN ARAM — the
summary places all twelve births in Paddan-aram while this very
chapter narrated Binyamin's birth on the Efrat road [OPEN
OBSERVATIONS (a) — letter-tension filed, never adjudicated].
(17) 35:27-29 THE FATHER'S DEATH: va-yavo yaaqov el yitzchaq...
mamre QIRYAT HAARBA (7153+/7153 tok2/2 both — the name
Kiryat-Arba's only other appearance is 23:2: SARAH'S death-verse
— the four-fold city appears exactly twice, once per buried
matriarch-household death) hiv chevron (2275 tok4/9); asher GAR
sham avraham ve-yitzchaq (1481 tok8/37 — the sojourn-verb over
both fathers); meat shana u-shemonim shana — Isaac's 180: the
longest patriarch lifespan on the ledger (Abraham 175, 25:7;
Jacob 147, 47:28 — DB numbers); va-yigva yitzchaq va-yamat
va-yeasef el amav (1478 tok5/11 — the expire-verb: flood ×2,
Abraham, Ishmael, Isaac, then Jacob at 49:33: patriarch deaths
and the flood share one verb; 622 tok10/50 — ASAF: tok9 was
34:30's feared hostile gathering (ve-neesfu alay); tok10 is the
peaceful gathering-to-his-people — fear and homecoming,
consecutive career tokens); zaqen u-SEVA yamim (7649 tok2/3 —
the sated-word: tok1 = 25:8 Abraham ve-savea; tok3 = Deut 33:23
Naphtali seva ratzon — two sated patriarchs and one sated
tribe); va-yiqbru oto ESAV VE-YAAQOV banav (6912 tok14/35) —
THE BROTHER-PAIR BURIAL REPEATS WITH ITS ORDER FLIPPED: tok10 =
25:9, va-yiqbru oto YITZCHAQ VE-YISHMAEL banav — there the
chosen-younger stood first; here ESAV the elder precedes
yaaqov [VERIFIED: token order both verses] — the FIRST TWO patriarch
burials are matching plural bury-tokens, each performed by an
estranged brother-pair, and the letter swaps the precedence
(the third, 50:13's va-yiqbru of Jacob by his sons, has no
pair to order).

WATCHLIST ARMS (prospective, filed): 37:29-34 (Reuben at the pit;
simla torn — 8071 tok3; Jacob refuses comfort); 37:12-14 (Shechem
pasture — carried); 42:21 (tzara toks 2-3 — the brothers'
confession); 47:27 (va-yifru va-yirbu — the pere-u-reve card's
people-horizon, with the achaz card of gen_57 in the same verse);
48:3-4 (El Shaddai retell — luz tok3, qehal amim; the package's
third station); 48:7 (the Efrat retell — kivrat/efrata/bet-lachem
close their careers); 49:3-4 (Reuben's reckoning — alah on the
bed); 49:5-7 (Simeon-Levi — qashata tok3); 49:33 (gava tok6 —
Jacob); Exod 1:15-21 (the midwives); Exod 7:3/13:15 (qashah on
Pharaoh); Exod 12:6 (qehal); Exod 12:43 (ben-nekhar); Exod 29:40
(nesekh law opens); Exod 32:2-3 (the earrings → the calf); Lev
11:32+ (taher codebook); Lev 26:1 / Deut 16:22 (the pillar
banned); Deut 31:16 (elohe nekhar — the covenant-breach phrase);
Deut 34:6 (Moses' unfindable qevura vs Rachel's to-this-day
pillar).

OPEN OBSERVATIONS (filed, never push for rulings): (a) 35:26's
"born to him in PADDAN-ARAM" summary vs Binyamin's in-span
Efrat-road birth (35:16-18) — the two tokens stand eleven verses
apart; letter-tension filed, no adjudication. (b) 35:7's niglu —
plural verb (HVNp3cp) with ha-Elohim — morph fact, filed only
(20:13's hitu class). (c) 35:20's ad-ha-yom monument clause —
fact-class, not PATTERN (no al-ken, no practice; 26:33's
report-class neighborhood). (d) shakhan (35:22) vs the commanded
yashav (35:1) — near-synonym other-root pair, the compliance-class
poster child. (e) et-o mixed within span (853 oto at 35:9,29; 854
ito at 35:13,14,15) — left raw, subs.py NOTE (im-o/bi-y class).
(f) the chapter holds two tree-hapaxes (ela 35:4, alon 35:8) and
five 1/1 name-or-noun hapaxes at its graves and camps (devora,
alon bakhut ×2, migdal-eder ×2 class) — density note only.
"""

# ---------------------------------------------------------------------------

STEPS = [
 dict(ref=(35,1), op="THE_COMMAND_CHAIN",
  en="And God said to Jacob: Arise, go up to Bethel and dwell there; and make there an altar to the El who appeared to you when you fled from Esau your brother.",
  tl_en="God said to Jacob: arise, go up to Bethel and dwell there",
  tr_en="make there an altar to the El who appeared when you fled from Esau",
  ops=[
   dict(op="DECLARE",
    expr="DECLARE(Elohim, LET(qum_ale(yaaqov, bet_el)))",
    frag=("qum",4), prose="""
THE GO-UP THAT NEVER NARRATES [UNIT SHAPE (1)]. qum ale vet-el
(6965 tok39/145 HVqv2ms; 5927 tok17/201 HVqv2ms) [VERIFIED:
SNAPSHOT Gen.35.1 idx4-5 morphs] — God's arise-and-ascend on
Jacob: the arise-aux rides the travel-verb as one card (gen_47's
qum-chains; gen_56's nisa-ve-nelekha pair class). And the
ascend-verb alah will narrate exactly once in this span — at
35:13, with GOD as its subject, going up FROM Jacob: the
demanded verb's only narrated token is the wrong performer in
the opposite direction; Jacob himself COMES (bo, 35:6). Card
OPEN. PUSH LET(qum_ale(yaaqov, bet_el)). Depth 1."""),
   dict(op="DECLARE",
    expr="DECLARE(Elohim, LET(shev_sham(yaaqov, bet_el)))",
    frag=("ve-shev",2), prose="""
THE DWELL-CARD [UNIT SHAPE (1-3)]. ve-shev sham (3427 tok50/199,
HC/Vqv2ms) [VERIFIED: idx8 morph] — the dwell-obligation, its
own card (gen_57's settlement-triple class: distinct obligations
split). The dwell-verb yashav never returns in-span [VERIFIED:
3427 in-span census = this imperative only]; when the narrator
needs Jacob abiding he writes bi-SHEKON (35:22) — shakhan, the
near-synonym in the other root [OPEN OBSERVATIONS (d)]. Card
OPEN. PUSH LET(shev_sham(yaaqov, bet_el)). Depth 2."""),
   dict(op="DECLARE",
    expr="DECLARE(Elohim, LET(ase_sham_mizbeach(yaaqov, la_el_ha_nire)))",
    frag=("va-ase",4), prose="""
MAKE, ANSWERED BY BUILD [UNIT SHAPE (1-3)]. va-ase sham mizbecha
(6213 tok115/860, HC/Vqv2ms; 4196 tok11/198) [VERIFIED: idx10-12]
— the altar-task: at 35:7 the altar EXISTS — va-YIVEN sham
mizbecha — but the verb is bana ("build"), not the commanded asa
("make"): the thing made, the verb swapped — gen_45's other-root
law holds the card OPEN over a completed altar (the unit's
compliance-class thesis). la-el ha-nire elekha BE-VARCHAKHA
mi-pene esav (410 tok12/50; 1272 tok8/14) — GOD NAMES THE FLIGHT
[care 1]: gen_53's arm lands — the flee-verb Jacob never
performed in gen_47's span is the verb God uses for that journey
("when you FLED"), and the narrator will echo it at 35:7
(be-varcho, tok9/14). PUSH LET(ase_sham_mizbeach(yaaqov,
la_el_ha_nire)). Depth 3."""),
  ],
  comment="Three cards from one command; the flight gets its verb from God's mouth."),

 dict(ref=(35,2), op="THE_PURGE_TRIPLE",
  en="And Jacob said to his house and to all who were with him: Remove the foreign gods that are in your midst, and purify yourselves, and change your garments.",
  tl_en="Jacob said to his house and all with him",
  tr_en="remove the foreign gods; purify yourselves; change your garments",
  ops=[
   dict(op="DECLARE",
    expr="DECLARE(yaaqov, LET(hasiru(bet_yaaqov, et_elohe_ha_nekhar)))",
    frag=("hasiru",4), prose="""
THE REMOVE-DEMAND [UNIT SHAPE (4-6)]. hasiru et elohe ha-nekhar
(5493 tok6/55, HVhv2mp) [VERIFIED: SNAPSHOT Gen.35.2 idx8 morph]
— remove the foreign gods: at 35:4 the gods leave the household's
hands — by GIVING (va-yitnu) and HIDING (va-yitmon): two other
roots do the removing and sur never returns in-span. Card OPEN
over a completed purge [compliance class]. ha-nekhar (5236
tok3/8) — the foreign-noun's career: Exod 12:43 (the Passover's
ben-nekhar exclusion), Deut 31:16 (elohe nekhar, the
covenant-breach phrase) — the purge's object becomes apostasy
law's vocabulary. PUSH LET(hasiru(bet_yaaqov,
et_elohe_ha_nekhar)). Depth 4."""),
   dict(op="DECLARE",
    expr="DECLARE(yaaqov, LET(hitaharu(bet_yaaqov)))",
    frag=("ve-hitaharu",1), prose="""
THE PURIFY-VERB IS BORN [CROWN 2]. ve-hitaharu (2891 tok1/54
DEBUT, HC/Vtv2mp) [VERIFIED: SNAPSHOT Gen.35.2 idx14
ordinal=1/54] — taher, the purify-verb, enters the Torah in
Jacob's purge command — ONE CHAPTER after its opposite: tamei
("defile") debuted at 34:5, on Dinah. The codebook's axis-pair
is born back to back in these two family chapters; taher's toks
2+ are Lev 11:32 onward — the purification system entire. No
purification is ever narrated in-span: the debut-card stays
OPEN. PUSH LET(hitaharu(bet_yaaqov)). Depth 5."""),
   dict(op="DECLARE",
    expr="DECLARE(yaaqov, LET(hachalifu(bet_yaaqov, simlotekhem)))",
    frag=("ve-hachalifu",2), prose="""
THE GARMENT-CARD [UNIT SHAPE (4-6)]. ve-hachalifu simlotekhem
(2498 tok3/5, HC/Vhv2mp) [VERIFIED: idx15 morph] — the
change-verb is Laban's wage-switch verb (31:7,41 — the only
prior tokens), now aimed at garments; no change is narrated.
simla (8071 tok2/19) — the garment-noun's NEXT token is 37:34:
Jacob TEARING his garments over Joseph's tunic — ordered
changed here, torn there; career → the borrowed garments of
the Exodus (Exod 3:22, 12:34-35) and the garment-laws (Deut
22). Card OPEN. PUSH LET(hachalifu(bet_yaaqov, simlotekhem)).
Depth 6."""),
  ],
  comment="The purge-triple pushed; the purify-verb debuts against last chapter's defile."),

 dict(ref=(35,3), op="THE_COHORTATIVE_PAIR",
  en="And let us arise and go up to Bethel; and I will make there an altar to the El who answered me in the day of my distress, and was with me on the way that I walked.",
  tl_en="let us arise and go up to Bethel",
  tr_en="an altar to the El who answered me in my distress, with me on my way",
  ops=[
   dict(op="DECLARE",
    expr="DECLARE(yaaqov, CMD-US?(naquma_ve_naale(bet_yaaqov, bet_el)))",
    frag=("ve-naquma",4), prose="""
THE JOINT ASCENT [UNIT SHAPE (7)]. ve-naquma ve-naale bet-el
(6965 tok40/145 + 5927 tok18/201, both HC/Vqh1cp true 1cp
cohortatives) [VERIFIED: SNAPSHOT Gen.35.3 idx0-1 morphs] —
Jacob turns God's 2ms chain into a first-plural pair: one card
per gen_56's nisa-ve-nelekha travel-pair precedent, TIR-033's
?-guard while open. The group then JOURNEYS — va-yisu (35:5,
nasa) — and neither qum nor alah narrates for them: other root,
card OPEN [compliance class]. la-el ha-one oti be-yom TZARATI
(6030 tok14/48; 6869 tok1/5 DEBUT) [VERIFIED: idx11
ordinal=1/5] — the distress-noun born in Jacob's testimony;
toks 2-3 = 42:21, the brothers' Joseph-guilt confession ("we
saw the distress of his soul... therefore this distress") — the
word passes father to sons with the guilt attached. va-yehi
imadi ba-derekh (5978 tok12/19) — 28:20's vow-formula ("if God
will be WITH ME on this way") quoted back as history. PUSH
CMD-US?(naquma_ve_naale(bet_yaaqov, bet_el)). Depth 7."""),
  ],
  comment="The us-pair pushed guarded; the vow's with-me formula returns fulfilled."),

 dict(ref=(35,4), op="THE_HANDOVER",
  en="And they gave to Jacob all the foreign gods that were in their hand, and the rings that were in their ears; and Jacob hid them under the terebinth that is by Shechem.",
  tl_en="they gave Jacob the foreign gods and the rings in their ears",
  tr_en="Jacob hid them under the terebinth by Shechem",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yitnu_va_yitmon(elohe_ha_nekhar_ve_ha_nezamim, tachat_ha_ela), t7)",
    frag=("va-yitnu",3), prose="""
GIVEN AND HIDDEN, NOT REMOVED [UNIT SHAPE (4); care 4].
va-yitnu el yaaqov (5414 tok94/647) [VERIFIED: SNAPSHOT
Gen.35.4 idx0 ordinal=94/647] — the give-verb's first narrated
performance since gen_57's negotiation: eight tokens haggled
over a daughter and gave nothing; token 94 hands over gods.
ve-et ha-NEZAMIM asher be-aznehem (5141 tok4/7) [VERIFIED: idx10
ordinal=4/7] — THE EARRING'S LEDGER: toks 1-3 = the bride-ring
on Rebekah (24:22,30,47); tok4 = buried idol-freight; toks 5-6 =
Exod 32:2-3, THE CALF'S RINGS ("break off the rings in your
ears" — the same in-their-ears phrase); tok7 = Exod 35:22, the
Mishkan offering — bride-gift, buried, calf, sanctuary.
va-YITMON (2934 tok1/3 DEBUT) [VERIFIED: idx13 ordinal=1/3] —
the hide-verb's three tokens: Jacob hides gods, Moses hides the
Egyptian (Exod 2:12), Deut 33:19's hidden treasures. tachat
ha-ELA (424 tok1/1 HAPAX) — the terebinth appears once in the
Torah, here, holding the gods; the hasiru-card stays OPEN — the
purge is done in verbs the demand never used. Depth 7."""),
  ],
  comment="The purge performed in other verbs; the earrings begin their long ledger."),

 dict(ref=(35,5), op="THE_UN_PURSUIT",
  en="And they journeyed; and a terror of God was upon the cities that were around them, and they did not pursue after the sons of Jacob.",
  tl_en="and they journeyed",
  tr_en="a God-terror on the cities around; they did not pursue Jacob's sons",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(chitat_Elohim_ve_lo_radfu(he_arim), t7)",
    frag=("va-yisau",1), prose="""
THE TERROR AND THE NEGATED VERB [care 5]. va-yisau — and the
etnachta sits on the verse's FIRST TOKEN: 35:5 is one of the
Torah's TWELVE first-word splits [VERIFIED: corpus mark census,
gen_57 CROWN 2d] — and the previous unit closed on another
(34:31): two of the twelve in consecutive units, a question
hanging and a journey landing. chitat Elohim (2847 tok1/1
HAPAX) [VERIFIED: SNAPSHOT Gen.35.5 idx2 ordinal=1/1] — the
God-terror, said once in the Torah, answering 34:30's fear
("they will gather against me and strike me"); ve-lo RADFU
(7291 tok4/25) [VERIFIED: idx9 ordinal=4/25] — the pursue-verb:
tok3 was LABAN'S pursuit (31:23); tok4 is the pursuit that does
NOT happen; career → Pharaoh's sea-pursuit (Exod 14:4-23,
15:9) and Lev 26's seven pursue-tokens — Israel pursuing in
the blessing (26:7-8), pursued and phantom-pursued in the
curse (26:17,36-37) — with Deut 28's pursuing curses —
the feared verb is spent here on a negation. Depth 7."""),
  ],
  comment="A hapax terror; the pursuit refused by the letter; another first-word split."),

 dict(ref=(35,6), op="THE_ARRIVAL",
  en="And Jacob came to Luz, which is in the land of Canaan — it is Bethel — he and all the people who were with him.",
  tl_en="Jacob came to Luz in the land of Canaan — it is Bethel",
  tr_en="he and all the people who were with him",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yavo_luzah_hiv_bet_el(yaaqov_ve_ha_am), t7)",
    frag=("va-yavo",3), prose="""
HE COMES WHERE HE WAS TOLD TO GO UP [UNIT SHAPE (1)]. va-yavo
yaaqov luzah (935 tok123/619; 3870 tok2/3) [VERIFIED: SNAPSHOT
Gen.35.6 idx0-2] — the arrival lands in the COME-verb, not the
commanded ascend-verb: the qum_ale card holds OPEN over a
completed journey [compliance class]. luz — the pre-name from
28:19's etiology (tok1), re-glossed by the narrator (hiv
bet-el); tok3 = 48:3, Jacob's own deathbed retell ("El Shaddai
appeared to me at LUZ"). ve-khal ha-am asher im-o (5971
tok20/445) — the household that will hear the twelve-count.
Depth 7."""),
  ],
  comment="Arrival by the other verb; the old name surfaces under the new."),

 dict(ref=(35,7), op="THE_ALTAR_BUILT_AND_NAMED",
  en="And he built there an altar, and called the place El-Bethel; for there the Elohim were revealed to him when he fled from before his brother.",
  tl_en="he built an altar and called the place El-Bethel",
  tr_en="for there God was revealed to him when he fled from his brother",
  ops=[
   dict(op="REGISTRY_INSTALL",
    expr="WORLD += {ha_maqom}",
    frag=("va-yiven",3), prose="""
BUILD FOR MAKE [UNIT SHAPE (3)]. va-YIVEN sham mizbecha (1129
tok16/41) [VERIFIED: SNAPSHOT Gen.35.7 idx0 ordinal=16/41] —
the altar the command said MAKE (asa) is BUILT (bana): the
thing exists, the verb swapped, the ase-card OPEN — the unit's
compliance-thesis in one token. WORLD += ha_maqom."""),
   dict(op="NAME",
    expr="name(ha_maqom) := el_bet_el",
    frag=("va-yiqra",3), prose="""
WRITE #1 — EL RIDES THE NAME. va-yiqra la-maqom EL BET-EL (7121
tok83/193; 410 tok14/50) [VERIFIED: SNAPSHOT Gen.35.7 idx3-7] —
the naming formula (la-maqom class) writes a name with El
inside it — 33:20's el-elohe-yisrael altar-title class, now on
the place itself; 35:15 will overwrite it [CROWN 3(a)]. ki sham
NIGLU elav ha-Elohim (1540 tok2/33) [VERIFIED: idx10
ordinal=2/33] — the reveal-verb: tok1 = 9:21, Noah UNCOVERED
drunk in his tent; tok2 = the Elohim REVEALED at Bethel; career
→ Lev 18-20's uncover-nakedness cluster — shame, theophany,
prohibition share one root. The verb is PLURAL (niglu, HVNp3cp)
with ha-Elohim — morph fact, filed as observation [OPEN
OBSERVATIONS (b)]. be-varcho mi-pene achiv (1272 tok9/14) — the
narrator repeats God's flight-naming [care 1]. REGISTRY 1."""),
  ],
  comment="Built-not-made; the place takes El into its name; the reveal-verb debuts plural."),

 dict(ref=(35,8), op="THE_NURSE_NAMED_AT_DEATH",
  en="And Devorah, Rebekah's nurse, died, and she was buried below Bethel, under the oak; and he called its name Oak of Weeping.",
  tl_en="Devorah, Rebekah's nurse, died and was buried under the oak",
  tr_en="and he called its name Oak of Weeping",
  ops=[
   dict(op="REGISTRY_INSTALL",
    expr="WORLD += {ha_alon}",
    frag=("va-tamat",4), prose="""
DEATH #1 — THE ANONYMOUS NURSE GETS A NAME [care 7]. va-tamat
DEVORA meneqet rivqa (1683 tok1/1 HAPAX; 4191 tok41/303; 3243
tok4/11) [VERIFIED: SNAPSHOT Gen.35.8 idx0-3] — Rebekah's nurse
traveled nameless since 24:59 (meniqtah — "her nurse") and is
named in her death-verse: the Torah's only devora. And rivqa
(7259 tok29/30) — Rebekah's last living-narrative token: her
own death is never narrated; the nurse's death stands where the
mistress's never will (tok30 = 49:31's grave-list). WORLD +=
ha_alon."""),
   dict(op="NAME",
    expr="name(ha_alon) := alon_bakhut",
    frag=("va-yiqra",4), prose="""
WRITE #2 — A HAPAX NAME ON A HAPAX TREE. va-yiqra shemo ALON
BAKHUT (7121 tok84/193; 439+ tok1/1; 439 tok1/1; the tree:
437 tok1/1) [VERIFIED: SNAPSHOT Gen.35.8 idx9-13 — all three
ordinals 1/1] — the Oak of Weeping: a hapax person buried under
a hapax tree that takes a hapax name — with 35:4's terebinth
(424, also 1/1) the chapter holds two tree-hapaxes [OPEN
OBSERVATIONS (f)]. mi-tachat le-vet-el — below Bethel; the
weeping-name is the chapter's first grief-write; two more
deaths follow. REGISTRY 2."""),
  ],
  comment="The nurse named only in death; the weeping-oak written."),

 dict(ref=(35,9), op="THE_SECOND_APPEARANCE",
  en="And God appeared to Jacob again, in his coming from Paddan-aram; and He blessed him.",
  tl_en="God appeared to Jacob again, coming from Paddan-aram",
  tr_en="and He blessed him",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yera_Elohim_od_va_yevarekh(el_yaaqov), t7)",
    frag=("va-yera",5), prose="""
AGAIN, COUNTED [care 8]. va-yera Elohim el yaaqov OD (7200
tok89/396; 5750 tok29/95) [VERIFIED: SNAPSHOT Gen.35.9 idx0-4]
— the second Bethel theophany, marked by the letter's own
"again" (od); be-vo-o mi-padan aram (6307 tok8/11) — the
return-frame; va-yevarekh et-o (1288 tok61/137) — the
bless-verb's Jacob-walk (Laban's farewell 58 → demanded 59 →
granted 60 → God's own 61). The naming and the package follow.
Depth 7."""),
  ],
  comment="The second appearance, blessed; the verse before the write."),

 dict(ref=(35,10), op="THE_DECREE_AND_THE_FORMULA",
  en="And God said to him: Your name is Jacob; your name shall no more be called Jacob, but Israel shall be your name. And He called his name Israel.",
  tl_en="God said to him: your name is Jacob",
  tr_en="no more Jacob — Israel your name; and He called his name Israel",
  ops=[
   dict(op="REGISTRY_INSTALL",
    expr="WORLD += {yaaqov}",
    frag=("shim-kha",2), prose="""
THE STATEMENT [CROWN 1]. shimkha yaaqov — God begins from the
registry's standing value: "your name is Jacob" (8034 tok85/252)
[VERIFIED: SNAPSHOT Gen.35.10 idx3-4] — the label 25:26 wrote
and gen_55's decree left standing. WORLD += yaaqov (the bearer
enters this unit's world for the write)."""),
   dict(op="NAME",
    expr="name(yaaqov) := yisrael",
    frag=("va-yiqra",4), prose="""
WRITE #3 — THE DECREE AND THE FORMULA IN ONE VERSE [CROWN 1].
lo yiqare shimkha od yaaqov ki im yisrael yihye shemekha —
DECREE grammar (yiqare, HVNi3ms negated imperfect + nominal
clause) [VERIFIED: SNAPSHOT Gen.35.10 idx5-14 morphs]: the
exact class of 17:5, 17:15, and 32:29 — which WRITES NOTHING
(gen_33's frozen law; gen_55's care 13). Then, same verse:
VA-YIQRA et shemo YISRAEL (7121 tok86/193) — the narrative
formula, which WRITES. The registry takes name(yaaqov) :=
yisrael three chapters after the decree withheld it — decree
and formula stand side by side in one verse and only the
formula moves the machine. THE COUNTERSIGN: the narrator's
first Israel-for-the-man is 35:21 (3478 tok7/587 — AFTER the
write, never before [VERIFIED: toks 1-6 census]); and yaaqov
keeps appearing in-span after the write (3290 toks 132-139 —
the last in the burial-verse itself, 35:29) —
a write begins a usage; it erases nothing (the inverse of
17:5's avram-retirement letter-proof). REGISTRY 3."""),
  ],
  comment="The decree writes nothing; the formula writes Israel; the narrator obeys from 35:21."),

 dict(ref=(35,11), op="THE_SINGULAR_BLESSING_COMMAND",
  en="And God said to him: I am El Shaddai. Be fruitful and multiply — a nation and an assembly of nations shall be from you; and kings shall go out from your loins.",
  tl_en="I am El Shaddai: be fruitful and multiply — a nation, an assembly of nations",
  tr_en="and kings shall go out from your loins",
  ops=[
   dict(op="DECLARE",
    expr="DECLARE(el_shaday, LET(pere_u_reve(yisrael)))",
    frag=("pere",2), prose="""
THE ONLY SINGULAR BE-FRUITFUL-AND-MULTIPLY [UNIT SHAPE (8);
care 9]. ani el shaday (7706 tok3/9) — gen_47's frozen horizon
LANDS: Isaac's send-off wished "ve-EL SHADAY yevarekh otekha...
ve-YAFREKHA ve-YARBEKHA... li-qehal AMIM" (28:3, jussives)
[VERIFIED: token scan]; God now speaks AS El Shaddai and turns
the wished jussives into commanded imperatives: PERE u-REVE
(6509 tok10/19 HVqv2ms; 7235 tok24/66 HC/Vqv2ms) [VERIFIED:
morphs] — and these are the fruit-verb's and multiply-verb's
ONLY singular imperatives in the Torah [VERIFIED: full morph
census — every other imperative token is plural: 1:22, 1:28,
9:1, 9:7]: the creation-blessing spoken to seas, humanity, and
Noah as plural benediction arrives once as a command to one
man — the man just named Israel. One card (the fixed merism,
gen_56's pair class); horizon 47:27 (va-yifru va-yirbu — the
people, in Goshen). u-qehal GOYIM (6951 tok2/34 — 28:3's qehal
AMIM shifted; career → Exod 12:6's qahal of Israel); u-melakhim
ME-CHALATZEKHA yetzeu — 17:6's kings-promise ("u-melakhim
MIM-KHA yetzeu" [VERIFIED: token scan]) requoted with one
delta: from-YOU → from-your-LOINS, and chalatzayim (2504
tok1/1 HAPAX) exists only inside the delta. PUSH
LET(pere_u_reve(yisrael)). Depth 8."""),
  ],
  comment="The plural blessing becomes a singular command; the kings-promise gains loins."),

 dict(ref=(35,12), op="THE_LAND_GRANT_TRIPLE",
  en="And the land that I gave to Abraham and to Isaac — to you I will give it; and to your seed after you I will give the land.",
  tl_en="the land I gave to Abraham and Isaac — to you I give it",
  tr_en="and to your seed after you I will give the land",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(natati_etnena_eten(ha_aretz, le_yisrael_u_le_zaro), t8)",
    frag=("ve-et",4), prose="""
ONE VERSE, THREE TENSES OF GIVE [care 9]. natati... etnena...
eten (5414 toks 95-97/647) [VERIFIED: SNAPSHOT Gen.35.12
idx3,7,10] — the grant conjugated past (gave to Abraham and
Isaac), singular-future (to you I WILL GIVE IT), and future (to
your seed I WILL GIVE): the give-verb that performed at 35:4
now carries the whole land-promise in three forms — God's
self-commits, fenced by class (promise-content, no push).
u-le-zarakha acharekha (2233 tok48/112) — the seed-formula's
Jacob-station between 28:14 and 48:4. Depth 8."""),
  ],
  comment="The grant in three tenses; promise-content, no cards."),

 dict(ref=(35,13), op="GOD_GOES_UP",
  en="And God went up from him, in the place where He had spoken with him.",
  tl_en="God went up from him",
  tr_en="in the place where He had spoken with him",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yaal_me_alav_Elohim(ba_maqom), t8)",
    frag=("va-yaal",3), prose="""
THE ASCEND-VERB'S ONLY DEED — GOD'S [CROWN 5; UNIT SHAPE (1)].
va-yaal me-alav Elohim (5927 tok19/201) [VERIFIED: SNAPSHOT
Gen.35.13 idx0-2] — the verb God commanded Jacob (ale, 35:1)
performs its only in-span narration with GOD as subject,
ascending FROM Jacob: wrong performer, opposite direction; the
qum_ale card holds. And the God-ascends formula occurs exactly
TWICE in the Torah [VERIFIED: full 5927 census against adjacent
Elohim]: 17:22 (from ABRAHAM — closing the chapter whose
renames were DECREES that wrote nothing) and here (closing the
theophany whose formula WROTE): the two renaming theophanies,
and only they, end with God going up. ba-maqom asher diber
et-o — the spoke-with-him refrain opens its three-verse run
(1696 toks 45-47/415). Depth 8."""),
  ],
  comment="God performs the commanded verb, upward and away; the refrain begins."),

 dict(ref=(35,14), op="THE_PILLAR_AND_THE_LIBATION",
  en="And Jacob set up a pillar in the place where He had spoken with him, a pillar of stone; and he poured on it a libation, and poured on it oil.",
  tl_en="Jacob set a stone pillar where He had spoken with him",
  tr_en="he poured on it a libation, and poured on it oil",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yatzev_matzeva_va_yasekh_nesekh(yaaqov, shamen), t8)",
    frag=("va-yatzev",4), prose="""
THE CULT KIT SEEDED [CROWN 4]. va-yatzev yaaqov matzeva (5324
tok9/28; 4676 tok8/16) [VERIFIED: SNAPSHOT Gen.35.14 idx0-2] —
gen_54's arm lands (va-yatzev toks 9-10 = this pillar and
Rachel's, 35:20); the pillar-noun's career ends BANNED (Lev
26:1; Deut 16:22 — "a pillar, which YHWH your God hates"): the
stone Jacob raises becomes the stone the law forbids. matzevet
aven (4678 tok1/2 — the construct form's whole career is
in-span: this stone and the grave-stone). va-yasekh aleha
NESEKH (5258 tok1/5; 5262 tok1/41 DEBUT) [VERIFIED: idx9-11
ordinals] — THE LIBATION-NOUN IS BORN on Jacob's pillar; toks
2+ = Exod 29:40 onward, the tamid and festival libations
entire. va-yitzoq aleha SHAMEN (3332 tok2/19; 8081 tok2/106)
[VERIFIED: idx12-14] — the pour-verb and the oil-noun each
stand at tok2, and BOTH their tok1s are 28:18 — the same man,
the same pillar, twenty years apart: Jacob's two Bethel
anointings are the entire pre-history of the verbs that will
anoint Aaron (Exod 29:7; Lev 8:12) and fill its lamps (Exod 27:20).
Depth 8."""),
  ],
  comment="Libation and oil debut on the pillar the law will later ban."),

 dict(ref=(35,15), op="THE_NAME_REWRITTEN",
  en="And Jacob called the name of the place where God had spoken with him — Bethel.",
  tl_en="Jacob called the name of the place where God spoke with him",
  tr_en="Bethel",
  ops=[
   dict(op="NAME",
    expr="name(ha_maqom) := bet_el",
    frag=("va-yiqra",5), prose="""
WRITE #4 — LAST-WRITE-WINS, PAIR (a) [CROWN 3]. va-yiqra yaaqov
et shem ha-maqom... BET-EL (7121 tok87/193; 8034 tok89/252)
[VERIFIED: SNAPSHOT Gen.35.15] — the same namer writes the same
place-key a second time: 35:7's EL-BET-EL reduces to BET-EL;
h_name overwrites, the counter increments, the registry ends on
the plain name — the ledger keeps both acts and shows only the
last. The verse carries NO etnachta — the split rides its
tifcha (idx9, prestage fallback; the span's first of three
fallback verses). REGISTRY 4."""),
  ],
  comment="The El-name reduced to the plain name; the machine keeps the history."),

 dict(ref=(35,16), op="THE_HARD_BIRTH_BEGINS",
  en="And they journeyed from Bethel, and there was still a stretch of land to come to Efrat; and Rachel gave birth, and her birthing was hard.",
  tl_en="from Bethel, still a stretch of land to come to Efrat",
  tr_en="Rachel gave birth, and her birthing was hard",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_teqash_be_lidtah(rachel, kivrat_ha_aretz_efrata), t8)",
    frag=("va-teqash",2), prose="""
THE HARDNESS-VERB IS BORN [care 12; CROWN 6]. va-yisu mi-bet-el
va-yehi od KIVRAT HA-ARETZ la-vo EFRATA (3530 tok1/2; 672
tok1/4) [VERIFIED: SNAPSHOT Gen.35.16 idx5,8] — the death-
scene's rare words (the stretch-of-land measure, the
place-name) will recur ONLY in Jacob's deathbed retelling of
this death (48:7 — kivrat tok2/2, efrata toks 3-4/4): event and
memory, nothing between [CROWN 6]. va-TEQASH be-lidtah (7185
tok1/9 DEBUT) [VERIFIED: idx11 ordinal=1/9] — qashah, the
hardness-verb, enters the Torah in Rachel's labor; tok3 = 49:7
(the curse on Simeon-Levi's anger — qashata), then the career
hardens hearts and necks: Pharaoh (Exod 7:3, 13:15), Sihon
(Deut 2:30), Israel's neck (Deut 10:16), beside the law's two
hard-case tokens (Deut 1:17, 15:18) — born in birth-pang,
mostly spent on obstinacy. Depth 8."""),
  ],
  comment="The hard-verb debuts in labor; the scene's words wait for the deathbed."),

 dict(ref=(35,17), op="THE_MIDWIFE_AND_THE_FEAR_NOT",
  en="And it was, in her hard birthing, that the midwife said to her: Fear not, for this one too is a son for you.",
  tl_en="in her hard birthing",
  tr_en="the midwife said: fear not — this one too is a son for you",
  ops=[
   dict(op="DECLARE",
    expr="DECLARE(ha_meyaledet, LET-NOT(tiri(rachel)))",
    frag=("el",2), prose="""
THE FEAR-NOT AT THE DEATHBED [UNIT SHAPE (9); care 12].
al-TIRI (408 + 3372 tok13/81, HVqj2fs true jussive) [VERIFIED:
SNAPSHOT Gen.35.17 idx6-7 morphs] — the negative particle with
a true jussive: LET-NOT push (gen_54's yichar class; gen_35's
al-pair). The fear-verb never returns in-span; the next verse
is Rachel's death — the card stands OPEN over a comfort that
could not land. ha-MEYALEDET (3205 tok142/205) [VERIFIED:
idx5] — THE MIDWIFE enters the Torah at this deathbed; the
office's next bearer is 38:28 (Tamar's midwife at the twins'
birth, tok156), then Exod 1:15-21's midwives who defy Pharaoh
— the role debuts losing a mother and ends saving the sons. ki GAM ZE lakh ben — "this one TOO": the letter's
receipt of 30:24's yosef-etiology — Rachel's fenced wish "may
YHWH ADD me ANOTHER son" (gen_51's yosef-class, the fence's
namesake) lands at her death: the added son arrives and the
adding costs the asker her life (landing-note; gen_51's ledger
untouched). PUSH LET-NOT(tiri(rachel)). Depth 9."""),
  ],
  comment="Fear-not pushed at a deathbed; the midwife-office and the added son arrive together."),

 dict(ref=(35,18), op="THE_TWO_NAMES",
  en="And it was, as her soul went out — for she died — that she called his name Ben-oni [son of my sorrow]; and his father called him Binyamin [son of the right hand].",
  tl_en="as her soul went out — for she died — she named him Ben-oni",
  tr_en="and his father called him Binyamin",
  ops=[
   dict(op="REGISTRY_INSTALL",
    expr="WORLD += {ha_ben}",
    frag=("be-tzet",3), prose="""
DEATH #2 BEGINS [CROWN 3(b)]. va-yehi be-tzet nafshah ki meta
(3318 tok60/348; 5315 tok29/205; 4191 tok42/303) [VERIFIED:
SNAPSHOT Gen.35.18 idx0-4] — the exit-verb of gen_57's bracket
now carries a soul out. WORLD += ha_ben (the twelfth son
enters the world his mother is leaving)."""),
   dict(op="NAME",
    expr="name(ha_ben) := ben_oni",
    frag=("va-tiqra",4), prose="""
WRITE #5 — THE DYING MOTHER'S NAME. va-tiqra shemo BEN-ONI
(7121 tok88/193; 1126+/1126 tok1/1 each) [VERIFIED: SNAPSHOT
Gen.35.18 idx5-8 — both ordinals 1/1] — "son of my sorrow":
Rachel's naming formula (va-tiqra — the same form that named
most of the twelve in gen_51) writes her last word into the
registry; the name is a Torah hapax — the ledger holds it one
write deep and the text never says it again. REGISTRY 5."""),
   dict(op="NAME",
    expr="name(ha_ben) := vinyamin",
    frag=("ve-avi-v",4), prose="""
WRITE #6 — THE FATHER'S OVERWRITE [CROWN 3(b)]. ve-aviv qara
lo VINYAMIN (7121 tok89/193; 1144 tok1/31 DEBUT) [VERIFIED:
idx9-12] — the father's qara-lo write (gen_54's 31:47 class:
plain narrative naming writes) lands on the same key:
last-write-wins — the registry ends binyamin, and every later
token of the child is Binyamin (1144 toks 2-31): the machine's
overwrite law enacting the story's grief — the mother's name
exists only in the write-history. REGISTRY 6."""),
  ],
  comment="Two writes on one child in one verse; the ledger keeps her word, the text keeps his."),

 dict(ref=(35,19), op="RACHEL_DIES",
  en="And Rachel died; and she was buried on the way to Efrat — it is Bethlehem.",
  tl_en="and Rachel died",
  tr_en="buried on the way to Efrat — it is Bethlehem",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_tamat_va_tiqaver(rachel, be_derekh_efrata_bet_lachem), t9)",
    frag=("va-tamat",2), prose="""
BETHLEHEM EXISTS ONLY HERE [CROWN 6]. va-tamat rachel (4191
tok43/303; 7354 tok37/44) va-tiqaver be-derekh efrata (6912
tok13/35; 672 tok2/4) hiv BET LACHEM (1035+ tok1/2; 1035
tok1/2) [VERIFIED: SNAPSHOT Gen.35.19] — Bethlehem's only
other Torah appearance is 48:7, Jacob's deathbed retelling of
this very verse: in the Torah, Bethlehem is Rachel's grave and
its memory — nothing else. The mother of the just-counted
house dies on the road between the write and the list.
Depth 9."""),
  ],
  comment="Death #2; Bethlehem enters the Torah as a grave-gloss."),

 dict(ref=(35,20), op="THE_GRAVE_PILLAR",
  en="And Jacob set up a pillar upon her grave — it is the pillar of Rachel's grave to this day.",
  tl_en="Jacob set a pillar on her grave",
  tr_en="it is the pillar of Rachel's grave to this day",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(matzevet_qevurat_rachel(ad_ha_yom), t9)",
    frag=("va-yatzev",3), prose="""
THE MARKED GRAVE AND THE UNFINDABLE ONE [care 14]. va-yatzev
yaaqov matzeva al qevuratah (5324 tok10/28; 4676 tok9/16; 4678
tok2/2 — the construct pillar-form CLOSES its two-token career:
Bethel's stone and Rachel's) [VERIFIED: SNAPSHOT Gen.35.20] —
qevura (6900 toks 1-2/4) — the burial-noun debuts twice on this
marked grave; its LAST token is Deut 34:6: MOSES' burial-place,
which "no man knows to this day" — the noun runs from the grave
marked ad-ha-yom to the grave unfindable ad-ha-yom. hiv
matzevet qevurat rachel AD HA-YOM — a standing-object report:
fact-class, not PATTERN (no al-ken, no practice) [OPEN
OBSERVATIONS (c)]. Depth 9."""),
  ],
  comment="The pillar that stands to-this-day; the burial-noun's career ends where no one knows."),

 dict(ref=(35,21), op="ISRAEL_MOVES",
  en="And Israel journeyed, and pitched his tent beyond Migdal-eder.",
  tl_en="and Israel journeyed",
  tr_en="and pitched his tent beyond the Tower of the Flock",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yisa_yisrael(me_hala_le_migdal_eder), t9)",
    frag=("va-yisa",2), prose="""
THE COUNTERSIGN LANDS [CROWN 1]. va-yisa YISRAEL (3478
tok7/587; 5265 tok10/120) [VERIFIED: SNAPSHOT Gen.35.21
idx0-1] — the narrator's FIRST Israel-for-the-man, eleven
verses after the formula wrote it and never once before
[VERIFIED: toks 1-6 census — decree speech, people-law,
altar-title, jurisdiction, formula]: the write begins the
usage. va-yet aholo (5186 tok5/50; 168 tok24/215) me-hala
LE-MIGDAL EDER (4029+/4029 tok1/1 each — the Tower of the
Flock, once in the Torah) [VERIFIED: ordinals 1/1]. Depth 9."""),
  ],
  comment="The narrator says Israel for the first time; the tent passes the flock-tower."),

 dict(ref=(35,22), op="REUBEN_AND_THE_COUNT",
  en="And it was, while Israel dwelt in that land, that Reuben went and lay with Bilhah, his father's concubine; and Israel heard. And the sons of Jacob were twelve.",
  tl_en="while Israel dwelt there, Reuben lay with Bilhah, his father's concubine; and Israel heard",
  tr_en="and the sons of Jacob were twelve",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yishkav_reuven_va_yishma_yisrael(shenem_asar), t9)",
    frag=("va-yishkav",4), prose="""
HEARD, AND NOTHING MORE [care 15]. va-yehi bi-SHEKON yisrael
(7931 tok7/35 — shakhan: the abide-verb the narrator uses where
the shev-card's yashav never returns [OPEN OBSERVATIONS (d)]);
va-yelekh reuven va-YISHKAV et bilha pilegesh aviv (7901
tok16/62; 1090 tok6/9; 6370 tok3/4) [VERIFIED: SNAPSHOT
Gen.35.22] — gen_57's armed next-violation lands: the lie-verb's
next narrative token after Shechem is Reuben; its next after
this is Potiphar's wife's imperative (39:7). va-YISHMA yisrael
(8085 tok43/241) — Israel HEARD — and the verse turns to
arithmetic: the hear-then-silence of 34:5, this time without
even a silence-verb; the reckoning waits for 49:3-4 ("you went
UP your father's bed" — the ascend-verb again [watch]).
va-yihyu vene yaaqov SHENEM ASAR — the twelve-count lands
immediately after the violation: the house is whole on the
letter the moment it breaks in the story. Depth 9."""),
  ],
  comment="The violation, the hearing, and the count — in one verse."),

 dict(ref=(35,23), op="LEAH_S_SIX",
  en="The sons of Leah: Jacob's firstborn Reuben, and Simeon and Levi and Judah and Issachar and Zebulun.",
  tl_en="Leah's sons: Jacob's firstborn Reuben",
  tr_en="Simeon, Levi, Judah, Issachar, Zebulun",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(bene_lea_shisha(reuven_ad_zevulun), t9)",
    frag=("bene",3), prose="""
THE TITLE THE LETTER KEEPS [care 16]. bene lea BEKHOR yaaqov
reuven (3812 tok29/33; 1060 tok6/69) [VERIFIED: SNAPSHOT
Gen.35.23 idx0-4] — one verse after the violation the letter
still titles Reuben FIRSTBORN: the census keeps the rank the
story has just undermined; the reckoning is 49:3-4's, outside
the span. The six in birth order (gen_51's names, re-listed by
mother). Depth 9."""),
  ],
  comment="The census speaks in titles; Reuben is still the firstborn on the letter."),

 dict(ref=(35,24), op="RACHEL_S_TWO",
  en="The sons of Rachel: Joseph and Binyamin.",
  tl_en="the sons of Rachel",
  tr_en="Joseph and Binyamin",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(bene_rachel(yosef_u_vinyamin), t9)",
    frag=("bene",4), prose="""
THE DEAD MOTHER'S LINE [care 16]. bene RACHEL yosef u-vinyamin
(7354 tok39/44; 3130 tok5/175; 1144 tok2/31) [VERIFIED:
SNAPSHOT Gen.35.24] — Rachel's list, five verses after
Rachel's grave; Binyamin's second token ever is his census
entry, already under the father's name [CROWN 3(b)]. The verse
has no etnachta — the split rides its zaqef qatan (idx1,
prestage fallback). Depth 9."""),
  ],
  comment="Rachel's sons listed past her grave; the overwrite-name holds."),

 dict(ref=(35,25), op="BILHAH_S_TWO",
  en="And the sons of Bilhah, Rachel's maid: Dan and Naphtali.",
  tl_en="the sons of Bilhah, Rachel's maid",
  tr_en="Dan and Naphtali",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(bene_vilha(dan_ve_naftali), t9)",
    frag=("u-vene",4), prose="""
THE MAID STILL RACHEL'S [care 16]. u-vene vilha SHIFCHAT RACHEL
(1090 tok7/9; 8198 tok27/31) [VERIFIED: SNAPSHOT Gen.35.25] —
the census still writes Bilhah as Rachel's maid, three verses
after Rachel died and three after Reuben's violation named
Bilhah the father's concubine: the list keeps the older
grammar of the house. dan ve-naftali (1835 tok3/27; 5321
tok2/20). No etnachta — zaqef qatan split (idx3, fallback).
Depth 9."""),
  ],
  comment="The census's tags outlive the deaths and the violation they straddle."),

 dict(ref=(35,26), op="ZILPAH_S_TWO_AND_THE_SUMMARY",
  en="And the sons of Zilpah, Leah's maid: Gad and Asher. These are the sons of Jacob who were born to him in Paddan-aram.",
  tl_en="the sons of Zilpah, Leah's maid: Gad and Asher",
  tr_en="these are Jacob's sons, born to him in Paddan-aram",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(ele_vene_yaaqov(yulad_lo_be_fadan_aram), t9)",
    frag=("ele",5), prose="""
THE SUMMARY AND THE ROAD [OPEN OBSERVATIONS (a)]. u-vene zilpa
shifchat lea gad ve-asher (2153 tok5/7; 1410 tok2/28; 836
tok2/20); ele vene yaaqov asher YULAD lo BE-FADAN ARAM (3205
tok143/205; 6307 tok9/11) [VERIFIED: SNAPSHOT Gen.35.26] — the
summary places all twelve births in Paddan-aram, eleven verses
after this same chapter set Binyamin's birth on the Efrat road
(35:16-18): the two tokens stand as the letter gives them —
filed as an open observation, adjudicated by no one. Depth 9."""),
  ],
  comment="The list closes on a clause the chapter itself strains; filed, not judged."),

 dict(ref=(35,27), op="THE_RETURN_TO_THE_FATHER",
  en="And Jacob came to Isaac his father, to Mamre, Kiryat-Arba — it is Hebron — where Abraham and Isaac had sojourned.",
  tl_en="Jacob came to Isaac his father at Mamre, Kiryat-Arba",
  tr_en="it is Hebron, where Abraham and Isaac sojourned",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yavo_el_yitzchaq(mamre_qiryat_haarba_hiv_chevron), t9)",
    frag=("va-yavo",5), prose="""
THE FOUR-FOLD CITY, TWICE [care 17]. va-yavo yaaqov el yitzchaq
aviv (935 tok126/619; 3327 tok72/98) mamre QIRYAT HAARBA (4471
tok8/10; 7153+ tok2/2; 7153 tok2/2) [VERIFIED: SNAPSHOT
Gen.35.27 — both Kiryat-Arba ordinals 2/2] — the name
Kiryat-Arba appears exactly twice in the Torah: 23:2 (SARAH
dies at Kiryat-Arba) and here (Jacob reaches Isaac to bury
him): both tokens stand at a patriarchal household's
death-station. hiv chevron (2275 tok4/9); asher GAR sham
avraham ve-yitzchaq (1481 tok8/37) — the sojourn-verb over
both fathers, one clause. Depth 9."""),
  ],
  comment="Arrival at the fathers' city; its rare name has only death-stations."),

 dict(ref=(35,28), op="ISAAC_S_DAYS",
  en="And the days of Isaac were a hundred years and eighty years.",
  tl_en="and the days of Isaac were",
  tr_en="a hundred years and eighty years",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(yeme_yitzchaq(meat_u_shemonim_shana), t9)",
    frag=("va-yihyu",3), prose="""
THE LONGEST PATRIARCH SPAN [care 17]. va-yihyu yeme yitzchaq
meat shana u-shemonim shana (3117 tok112/668; 3967 tok59/194;
8084 tok5/9) [VERIFIED: SNAPSHOT Gen.35.28] — 180: longer than
Abraham's 175 (25:7) and Jacob's 147 (47:28) — the quietest
patriarch holds the longest ledger-line (DB arithmetic).
Depth 9."""),
  ],
  comment="One hundred and eighty; the middle patriarch's line is the longest."),

 dict(ref=(35,29), op="THE_BROTHERS_AT_THE_GRAVE",
  en="And Isaac expired and died, and was gathered to his people, old and full of days; and Esau and Jacob his sons buried him.",
  tl_en="Isaac expired, died, was gathered to his people, old and full of days",
  tr_en="and Esau and Jacob his sons buried him",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yigva_va_yeasef_va_yiqbru(yitzchaq, esav_ve_yaaqov), t9)",
    frag=("va-yigva",3), prose="""
DEATH #3, AND THE ORDER FLIPS [care 17]. va-yigva yitzchaq
va-yamat (1478 tok5/11 — the expire-verb belongs to the flood
×2 and the patriarchs: Abraham, Ishmael, Isaac, then Jacob at
49:33) va-YEASEF el amav (622 tok10/50) [VERIFIED: SNAPSHOT
Gen.35.29] — asaf: tok9 was 34:30's feared hostile gathering
(ve-neesfu alay, "they will gather against me"); tok10 is the
peaceful gathering-to-his-people — dread and homecoming on
consecutive career tokens. zaqen u-SEVA yamim (2205 tok5/54;
7649 tok2/3 — the sated-word: Abraham ve-savea 25:8, Isaac
here, Naphtali seva ratzon Deut 33:23 — two sated fathers, one
sated tribe). va-yiqbru oto ESAV VE-YAAQOV banav (6912
tok14/35) — the brother-pair burial repeats 25:9's (va-yiqbru
oto YITZCHAQ VE-YISHMAEL banav) with the order FLIPPED
[VERIFIED: token order both verses]: there the chosen younger
stood first; here the elder Esau precedes — the first two
patriarch burials are matching plural bury-tokens, each by an
estranged pair, and the letter swaps the precedence (the
third, 50:13's burial of Jacob by his sons, has no pair to
order). UNIT END:
SPECS depth 9 OPEN (qum_ale · shev_sham · ase_sham_mizbeach ·
hasiru · hitaharu · hachalifu · naquma_ve_naale? · pere_u_reve
· tiri-NOT) — NINE pushed, ZERO popped: the second nine-open
wall, back to back with gen_57's — refusal there, compliance
here, and the letter holds both open. REGISTRY 6 writes
(el_bet_el→bet_el; alon_bakhut; yisrael; ben_oni→vinyamin).
TESTS 0 [VERIFIED: zero tov-adjective (2896) tokens in
Gen 35]."""),
  ],
  comment="Isaac gathered; the estranged brothers bury him, elder first this time."),
]

# ---------------------------------------------------------------------------

def _s(id, ref, frag, title, given, expect, occ=1):
    d = dict(id=id, ref=ref, frag=frag, title=title, given=given, expect=expect)
    d["occ"] = occ
    return d

AL = "LET(qum_ale(yaaqov, bet_el)) pushed and OPEN;"
SB = "LET(shev_sham(yaaqov, bet_el)) pushed and OPEN;"
AS = "LET(ase_sham_mizbeach(yaaqov, la_el_ha_nire)) pushed and OPEN;"
HS = "LET(hasiru(bet_yaaqov, et_elohe_ha_nekhar)) pushed and OPEN;"
TH = "LET(hitaharu(bet_yaaqov)) pushed and OPEN;"
HH = "LET(hachalifu(bet_yaaqov, simlotekhem)) pushed and OPEN;"
NQ = "CMD-US?(naquma_ve_naale(bet_yaaqov, bet_el)) pushed and OPEN;"
PR = "LET(pere_u_reve(yisrael)) pushed and OPEN;"
TI = "LET-NOT(tiri(rachel)) pushed and OPEN;"
NTN = "no test, no name."
R1 = "REGISTRY 1 writes"
R2 = "REGISTRY 2 writes"
R3 = "REGISTRY 3 writes"
R4 = "REGISTRY 4 writes"
R6 = "REGISTRY 6 writes"

SCENS = [
 _s("S1", (35,1), ("qum",4),
    "after STEP_Gn_35_1 — the command-chain: three cards; depth 3",
    "Arise, go up to Bethel, dwell there, make there an altar.",
    [AL, SB, AS, NTN]),
 _s("S2", (35,2), ("hasiru",4),
    "after STEP_Gn_35_2 — the purge-triple; depth 6",
    "Remove the foreign gods, purify yourselves, change your garments.",
    [AL, SB, AS, HS, TH, HH, NTN]),
 _s("S3", (35,3), ("ve-naquma",4),
    "after STEP_Gn_35_3 — the cohortative pair pushed guarded; depth 7",
    "Let us arise and go up to Bethel.",
    [AL, SB, AS, HS, TH, HH, NQ, NTN]),
 _s("S4", (35,4), ("va-yitnu",3),
    "after STEP_Gn_35_4 — gods given and hidden, not removed; depth 7",
    "They gave the gods and rings; Jacob hid them under the terebinth.",
    [AL, SB, AS, HS, TH, HH, NQ, NTN]),
 _s("S5", (35,5), ("va-yisau",1),
    "after STEP_Gn_35_5 — the terror; no pursuit; depth 7",
    "A terror of God was on the cities; they did not pursue.",
    [AL, SB, AS, HS, TH, HH, NQ, NTN]),
 _s("S6", (35,6), ("va-yavo",3),
    "after STEP_Gn_35_6 — arrival by the come-verb; depth 7",
    "Jacob came to Luz — it is Bethel.",
    [AL, SB, AS, HS, TH, HH, NQ, NTN]),
 _s("S7", (35,7), ("va-yiqra",3),
    "after STEP_Gn_35_7 — altar built; El-Bethel written; REGISTRY 1",
    "He built an altar and called the place El-Bethel.",
    [AL, SB, AS, HS, TH, HH, NQ, "WORLD += ha_maqom;", R1]),
 _s("S8", (35,8), ("va-yiqra",4),
    "after STEP_Gn_35_8 — Devorah dead; the weeping-oak written; REGISTRY 2",
    "Devorah died; he called its name Oak of Weeping.",
    [AL, SB, AS, HS, TH, HH, NQ, "WORLD += ha_alon;", R2]),
 _s("S9", (35,9), ("va-yera",5),
    "after STEP_Gn_35_9 — the second appearance; depth 7",
    "God appeared to Jacob again and blessed him.",
    [AL, SB, AS, HS, TH, HH, NQ, R2]),
 _s("S10", (35,10), ("va-yiqra",4),
    "after STEP_Gn_35_10 — decree writes nothing; formula writes Israel; REGISTRY 3",
    "No more Jacob — Israel; and He called his name Israel.",
    [AL, SB, AS, HS, TH, HH, NQ, "WORLD += yaaqov;", R3]),
 _s("S11", (35,11), ("pere",2),
    "after STEP_Gn_35_11 — the singular be-fruitful-and-multiply; depth 8",
    "I am El Shaddai: be fruitful and multiply.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, R3]),
 _s("S12", (35,12), ("ve-et",4),
    "after STEP_Gn_35_12 — the land-grant in three tenses; depth 8",
    "The land I gave to Abraham and Isaac — to you I will give it.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, R3]),
 _s("S13", (35,13), ("va-yaal",3),
    "after STEP_Gn_35_13 — God performs the ascend-verb, away; depth 8",
    "God went up from him in the place where He spoke with him.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, R3]),
 _s("S14", (35,14), ("va-yatzev",4),
    "after STEP_Gn_35_14 — pillar, libation, oil; depth 8",
    "He poured on it a libation and poured on it oil.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, R3]),
 _s("S15", (35,15), ("va-yiqra",5),
    "after STEP_Gn_35_15 — Bethel over El-Bethel; REGISTRY 4",
    "Jacob called the name of the place Bethel.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, R4]),
 _s("S16", (35,16), ("va-teqash",2),
    "after STEP_Gn_35_16 — the hard birth begins; depth 8",
    "Rachel gave birth, and her birthing was hard.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, R4]),
 _s("S17", (35,17), ("el",2),
    "after STEP_Gn_35_17 — fear-not pushed at the deathbed; depth 9",
    "Fear not, for this one too is a son for you.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, TI, R4]),
 _s("S18", (35,18), ("va-tiqra",4),
    "after STEP_Gn_35_18 — Ben-oni written, Binyamin overwrites; REGISTRY 6",
    "She called him Ben-oni; his father called him Binyamin.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, TI, "WORLD += ha_ben;", R6]),
 _s("S19", (35,19), ("va-tamat",2),
    "after STEP_Gn_35_19 — Rachel dies; Bethlehem enters as a grave-gloss; depth 9",
    "Rachel died and was buried on the way to Efrat — it is Bethlehem.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, TI, R6]),
 _s("S20", (35,20), ("va-yatzev",3),
    "after STEP_Gn_35_20 — the grave-pillar to this day; depth 9",
    "It is the pillar of Rachel's grave to this day.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, TI, R6]),
 _s("S21", (35,21), ("va-yisa",2),
    "after STEP_Gn_35_21 — the narrator's first Israel; depth 9",
    "And Israel journeyed and pitched his tent beyond Migdal-eder.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, TI, R6]),
 _s("S22", (35,22), ("va-yishkav",4),
    "after STEP_Gn_35_22 — Reuben; Israel heard; the twelve counted; depth 9",
    "Reuben lay with Bilhah; Israel heard; the sons were twelve.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, TI, R6]),
 _s("S23", (35,23), ("bene",3),
    "after STEP_Gn_35_23 — Leah's six; the firstborn title kept; depth 9",
    "Leah's sons: Jacob's firstborn Reuben, and five brothers.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, TI, R6]),
 _s("S24", (35,24), ("bene",4),
    "after STEP_Gn_35_24 — Rachel's two, past her grave; depth 9",
    "The sons of Rachel: Joseph and Binyamin.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, TI, R6]),
 _s("S25", (35,25), ("u-vene",4),
    "after STEP_Gn_35_25 — Bilhah's two, still Rachel's maid; depth 9",
    "The sons of Bilhah, Rachel's maid: Dan and Naphtali.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, TI, R6]),
 _s("S26", (35,26), ("ele",5),
    "after STEP_Gn_35_26 — the Paddan-aram summary; observation filed; depth 9",
    "These are Jacob's sons, born to him in Paddan-aram.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, TI, R6]),
 _s("S27", (35,27), ("va-yavo",5),
    "after STEP_Gn_35_27 — to Isaac at Kiryat-Arba; depth 9",
    "Jacob came to Isaac his father — it is Hebron.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, TI, R6]),
 _s("S28", (35,28), ("va-yihyu",3),
    "after STEP_Gn_35_28 — one hundred and eighty; depth 9",
    "The days of Isaac were a hundred and eighty years.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, TI, R6]),
 _s("S29", (35,29), ("va-yigva",3),
    "after STEP_Gn_35_29 — Isaac gathered; the brothers bury; nine open at the wall",
    "Esau and Jacob his sons buried him.",
    [AL, SB, AS, HS, TH, HH, NQ, PR, TI, R6]),
]
