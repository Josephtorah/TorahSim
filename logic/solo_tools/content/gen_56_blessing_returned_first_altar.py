# -*- coding: utf-8 -*-
"""Authored content for gen_56 (33:1-20). DB evidence: gen56_prestage_full.txt
(regenerable: python3 logic/solo_tools/prestage.py Gen 33:1-33:20) + targeted
queries logged in the derivation session 2026-08-07."""

UID = "gen_56_blessing_returned_first_altar"
BOOK = "Gen"
SPAN = (33, 1, 33, 20)
EXTRA_SUBS = {"et-y": "iti", "ahol-o": "aholo"}


META = [
    ("id", "gen_56_blessing_returned_first_altar"),
    ("title_en", '"The blessing returned and the first altar (33:1-20)"'),
    ("title_he", "קַח־נָא אֶת־בִּרְכָתִי"),
    ("title_he_translit", "qach-na et-birkhati"),
    ("title_he_en", "\"'Take, please, my blessing'\""),
    ("book_he", "בְּרֵאשִׁית"),
    ("book_he_translit", "Be-reshit"),
    ("book_en", "Genesis"),
    ("refs", "33:1-20"),
    ("unit_span_planned", "33:1-20"),
]

DRAFT_NOTE = """
DRAFT 2026-08-07 · SOLO ERA unit #10 (Claude coordinator+deriver;
external fresh-context adversarial review before freeze per standing
law). Span: 33:1-20, from the lifted eyes to the named altar. 20
verses · 268 tokens (SNAPSHOT-verified). SNAPSHOT + debut_map. bar C.
Conventions: step he: = plain (no accents/meteg; maqqef ־ per
snapshot); tree halves = accents kept, slashes stripped; split at
etnachta — TWO verses carry NONE: 33:6 (5 tokens, split at the tifcha
idx3, rank 2) and 33:16 (6 tokens, split at the tifcha idx4, rank 2)
— gen_03 1:13 / gen_50 29:22 fallback law. Onkelos BUFFER PENDING.
Translit note: "ahol-o" (33:19) polishes to "aholo" via EXTRA_SUBS
only — frozen gen_54 keeps the raw form at 31:25 (subs.py NOTE).

UNIT SHAPE — FOUR pushes, ONE POP, THREE OPEN: after gen_54 and
gen_55 pushed fourteen cards and popped NONE, the run's first RESULT
fires — and the demand that clears is TAKE-BACK-THE-BLESSING.
(1) 33:9 LET(yehi(lekha_asher_lakh)) — Esau's keep-what-is-yours
jussive (HVqj3ms, mood law gen_32): pushed, then UNDONE BY ITS OWN
DEMANDER — at 33:11 Esau takes (va-yiqach) the very gift his jussive
told Jacob to keep: the demander performs his demand's own reversal
(no haya-root receipt ever fires; card OPEN with the self-reversal
filed — a new mismatch-family shape). (2) 33:11 THE POP:
LET(qach_na_et_birkhati(esav)) — qach (3947 tok102/393, HVqv2ms) →
va-yiftzar bo VA-YIQACH (tok103/393): the demand's own root returns
as a foreground deed by the demandee IN THE SAME VERSE — demand and
receipt are CONSECUTIVE career tokens (echo-receipt law, gen_25/
gen_35; latency zero verses — gen_51's bo pop had latency one).
(3) 33:12 CMD-US?(nisa_ve_nelekha(esav_ve_yaaqov)) — Esau's
joint-journey double cohortative (nisa HVqh1cp + ve-nelekha
HC/Vqh1cp, TIR-033): politely declined (33:13-14) and answered by
OPPOSITE VECTORS — 33:16 Esau returns to Seir, 33:17 Jacob journeys
to Sukkot; and the journey-verb's own career walks demand → solo
deed: nasa 5265 tok6 = the cohortative NISA itself, tok7 = 33:17
Jacob's SOLO nasa — the let-US-journey answered by a one-man journey
the other way, consecutive tokens: card OPEN. (4) 33:14
LET(yaavar_na(adoni, li_fene_avdo)) — Jacob's pass-before jussive
(HVqj3ms): Esau never passes-before — 33:16 gives him SHUV (returned
to his way), the other root (gen_45 Excerpt B): card OPEN. FENCED,
NO PUSH: 33:15's atziga (HVhh1cs — 1cs cohortative offer, gen_52's
30:31 ashuva self-commit class; declined by la-ma ze) and 33:15's
emtza (HVqh1cs inside a rhetorical question); 33:14's etnahala +
avo el adoni seira — self-commit content (and the stated Seir-visit
has NO arrival token in the corpus: Jacob's next narrated station is
Sukkot; filed as letter-note, no adjudication of intent). END:
SPECS depth 3 OPEN (yehi · nisa_ve_nelekha · yaavar_na — all three
are the brothers' courtesies; the one card that CLEARED in this
whole three-block run is the returned blessing). REGISTRY 1 write
(the altar). TESTS 0 (zero tov-adjective tokens in Gen 33 —
debut_map scan).

CROWN — THE RETURNED WORD (33:11): qach na et BIRKHATI — the
blessing-noun 1293 tok9/30, and its toks 3-7 are the Gen 27 wound:
27:35 "he took YOUR BLESSING" (birkhatekha), 27:36 Esau's own cry
"he took MY BLESSING" (birkhati), 27:36/38/41 the blessing fought
over. Now the taker says TAKE (laqach, the very verb of 27:35-36)
+ MY BLESSING (birkhati, Esau's own word from 27:36) — TO ESAU:
verb and noun of the theft-cry, speaker and addressee exchanged —
and Esau TAKES: the 27:36 sentence performed with the roles
reversed, and the machine pops its first card in three units on it.
THE SECOND CROWN (33:20): va-yatzev sham mizbecha — Jacob's FIRST
altar (mizbeach 4196 tok10/198; toks 1-9 = Noah ×2 at 8:20, Abram
×4 at 12:7/12:8/13:4/13:18, Moriah ×2 at 22:9, Isaac at 26:25 —
all his fathers') — and he
NAMES it (va-yiqra LO — full formula, the write fires): name :=
el_elohe_yisrael — "El, God of ISRAEL": yisrael tok3/587 sits
INSIDE the altar-name — the REGISTRY receives the name israel for
the first time not as the man's label (32:29's decree wrote
nothing; 35:10's formula-write is still ahead) but inside God's
title on an altar: the renamed man files his new name obliquely,
as a genitive of El. The set-up verb: va-yatzev 5324 tok8/28 —
toks 6-7 = 28:12-13, the ladder SET UP (mutzav) and YHWH STANDING
(nitzav) on it; toks 9-10 = 35:14 (Bethel's pillar re-set) and
35:20 (Rachel's grave-pillar): ladder, altar, pillar, grave.

CARE-POINTS (ordinals from debut_map via prestage unless tagged):
(1) 33:1-2 THE ORDER OF LOVE: maids+children first, Leah's group,
Rachel+Joseph LAST (acharonim 314 toks 1-2/11 DEBUT ×2 — the
last-word debuts double in the safest place); rishona 7223 tok7/55.
yosef 3130 toks 3-4/175 — Joseph's first NARRATIVE tokens (toks
1-2 were his naming, gen_51): the boy enters the story placed
hindmost, and bows (33:7). va-yachatz (2673 tok2/6) — gen_55's
divide-verb divides the CHILDREN one verse after dividing camps.
(2) 33:3 THE BOW INVERTED: ve-hu avar li-fenehem (5674 tok19/130 —
the cross-verb: Jacob crosses FIRST, ahead of the order he built);
va-yishtachu artza SHEVA peamim (7812 tok12/47) — THE BLESSING
PERFORMED BACKWARDS: hishtachavah's toks 9-11 are 27:29's own
decree — "peoples will bow to you, YOUR MOTHER'S SONS WILL BOW TO
YOU" (gen_46's blessing, incl. the ketiv token) — and the verb's
VERY NEXT token (12) is JACOB bowing, seven times, TO THE BROTHER:
the bow-verb goes from decree to inverse performance with nothing
between — wrong-direction landing on the stolen blessing's own
grammar. sheva peamim (7651 tok29/185; 6471 tok7/39 — the
seven-word of the served years now counts prostrations).
(3) 33:4 THE HAND BECOMES ARMS [gen_55 landing-note; frozen ledger
untouched]: va-yaratz esav liqrato (7323 tok9/12 — the RUN-verb:
toks 3-8 are the well-and-hearth hospitality runs of Gen 24/29 —
Laban ran to Jacob at 29:13 (tok8); Esau's run is tok9: the two
arrival-runs of the cycle) va-yechabqehu (2263 tok2/3 — the
EMBRACE-verb: tok1 = 29:13 LABAN embracing Jacob at the cycle's
door, tok2 = ESAU embracing at its exit, tok3 = 48:10 Jacob
embracing Joseph's sons — three embraces, all this family)
va-yipol al TZAVARAV (6677 tok3/9 — the NECK: tok1 = 27:16, the
kid-skins ON JACOB'S NECK — the deception's costume; tok2 = 27:40,
Esau's anti-blessing yoke ON YOUR NECK; tok3 = Esau falling ON
THE DECEIVER'S NECK in tears: the neck-word's first three tokens
are disguise, yoke, embrace) va-yishaqehu (5401 tok7/13 — the
kiss-walk's reconciliation token) va-yivku — AND THEY WEPT: bakha
1058 tok5/29, and toks 1-4 are ALL SINGULAR (Hagar 21:16, Abraham
23:2, ESAU ALONE at the blessing-theft 27:38, Jacob at the well
29:11) [VERIFIED: morphs 3fs/inf/3ms/3ms] — tok5 = va-yivku
HC/Vqw3mp, the verb's FIRST PLURAL token: the man who wept alone
at 27:38 now weeps WITH the man who caused it — the weep-verb
learns the plural at the reconciliation. The gen_55 hatzileni
card's feared HAND (mi-yad esav) arrives as arms around the neck
— no natzal-token fires; the fear dissolves without its demanded
verb (cross-unit landing-note).
(4) 33:5 THE GRACE-VERB IS BORN: mi ele lakh → ha-yeladim asher
CHANAN Elohim et avdekha (2603 tok1/10 DEBUT) — the grace-verb's
debut names the children God-graced; tok2 = 33:11 chanani (BOTH
in-span: born twice in one meeting); full career: 42:21 (Joseph's
pleading recalled by his brothers), 43:29 (Joseph to Benjamin,
"God be gracious to you" — the same blessing-shape over a younger
brother), Exod 33:19 ×2 ("I will be GRACIOUS to whom I will be
gracious" — the Attributes' own grammar), Num 6:25 (the PRIESTLY
BLESSING's vi-chuneka), Deut 3:23 (va-etchanan), then the two
grace-DENIALS that close it (Deut 7:2 lo techanem, 28:50 lo
yachon) — the verb that REACHES the priestly blessing begins in a
father's answer about children.
(5) 33:6-7 THE WAVES BOW (33:6 = etnachta-less, tifcha split):
va-tigashna / va-tigash / nigash (5066 toks 12-14/45 — the
APPROACH-verb: toks 8-9 = 27:26-27, gesha-na — the deception's
"come near and kiss me"; now the whole family approaches the
deceived party's son in waves); hishtachavah toks 13-15/47 — the
bowing multiplies (maids, Leah, Joseph-and-Rachel); hena 2007
tok3/17.
(6) 33:8-10 THE CAMP EXPLAINED AND THE FACE-CODA: mi lekha kal
ha-machane ha-ze asher PAGASHTI (6298 tok2/4 — gen_55's meet-verb
in ESAU'S mouth: the anticipated dangerous meeting, told by the
met one; machane 4264 tok7/104 — the camp-word's first
token in another speaker's mouth); li-metzo chen be-ene adoni (the grace-
formula, chen 2580 tok6/27; adoni ×5 in-span, 113 toks 35-39/91 —
Jacob keeps the servant-grammar even after the embrace);
33:10: im na matzati chen... ve-laqachta minchati mi-yadi (3947
tok101 — the take-verb warms up one verse before the pop; 4503
tok8/113 minchati — the offering-noun's Cain-and-Abel career in
its brother-reconciliation token) KI AL KEN RAITI FANEKHA KI-REOT
PENE ELOHIM (6440 toks 90-91/627; 7200 toks 84-85/396) — the
face-coda: one unit after panim-el-panim at Peniel, Jacob tells
Esau your face is like God's face — the face-walk of gen_55
closes on the brother's; VA-TIRTZENI (7521 tok1/14 DEBUT) — THE
ACCEPTANCE-VERB IS BORN: "and you have ACCEPTED me" — its career
is Leviticus's sacrificial acceptance formula (Lev 1:4 ve-nirtza
lo, 7:18/19:7/22:23-27 yeratze) and Lev 26's sabbath-repayment:
the verb by which the altar accepts debuts in a brother accepting
a brother — offering-noun and acceptance-verb meet in one
sentence a chapter before Jacob's first altar.
(7) 33:11 THE POP [CROWN]; plus: asher HUVAT lakh (935 tok114/619
hophal — "which was BROUGHT to you": the bring-verb gone passive
for the gift); ki chanani Elohim ve-khi yesh li KHOL ("I have
ALL" — 3605 tok239/1595: Esau said yesh li RAV, "I have MUCH"
(7227 tok10/66, 33:9); Jacob answers yesh li KHOL, "I have ALL" —
much against all, the two inventories one verse apart);
va-yiftzar bo (6484 tok3/3 CLOSES — the URGE-verb's whole career:
Lot urging the angels (19:3), the mob urging Lot (19:9), Jacob
urging Esau — two Sodom doors and a reconciliation, done).
(8) 33:12-14 THE DECLINED CONVOY: nisa ve-nelekha [UNIT SHAPE
(3)]; ve-elkha le-negdekha (5048 tok7/17 — neged: the CORRESPOND-
word of 2:18's ke-negdo — "I will go OPPOSITE you": the helper-
grammar offered brother-to-brother); adoni yodea ki ha-yeladim
RAKIM (7390 tok3/6 — tender: tok2 = 29:17 Leah's tender eyes —
the word's two Jacob-cycle tokens are eyes and children); alot
(5763 tok1/1 HAPAX — the nursing ones) alay; u-defaqum yom echad
(1849 tok1/1 HAPAX — the OVERDRIVE-verb, once ever) va-metu kal
ha-tzon; yaavar na adoni [UNIT SHAPE (4)]; va-ani ETNAHALA
LE-ITI (5095 tok1/3 DEBUT — the LEAD-GENTLY verb: tok2 = 47:17
Joseph leading Egypt through famine-bread, tok3 = Exod 15:13
NEHALTA — the Song of the Sea's "You led in Your strength to Your
holy habitation": the gentle-lead verb debuts in Jacob's
flock-pace and lands in the Exodus hymn; 328 le-iti tok1/1 HAPAX
— "at my slow pace", said once in the Torah) le-regel ha-melakha
(4399 tok4/65 — MELAKHA: toks 1-3 = GOD'S OWN WORK at 2:2-3, the
Sabbath's thrice-said melakha; tok4 = the drovers' work — the
labor-noun's first post-creation token; career → Exod 20:9-10's
Sabbath command cluster) u-le-regel ha-yeladim (7272 toks 8-9/60
— at the FOOT-pace of work and children) ad asher avo el adoni
SEIRA — the stated Seir-arrival has no narrated token anywhere in
the corpus (Jacob's next station is Sukkot, 33:17; letter-note
only, intent not adjudicated).
(9) 33:15 THE DECLINED GARRISON: atziga-na (3322 tok2/6 — the
STATION-verb: tok1 = 30:38 Jacob STATIONING the rods (gen_52's
device!); tok2 = Esau offering to station MEN; toks 3-4 = 43:9
Judah's ve-hitzagtiv (setting Benjamin before his father) and
47:2 (Joseph stationing five brothers before Pharaoh)) — 1cs
cohortative offer, gen_52's ashuva self-commit class, no push;
declined: la-ma ze emtza chen be-ene adoni (the grace-formula's
third in-span token closes the negotiation).
(10) 33:16-17 THE OPPOSITE VECTORS (33:16 = etnachta-less, tifcha
split): va-yashav esav le-darko SEIRA / ve-yaaqov nasa SUKOTA —
one verse-pair, two directions [UNIT SHAPE (3)]; va-yiven lo
BAYIT (1129 tok15/41 — the build-verb: Jacob's first BUILDING;
its Jacob-cycle neighbor is 30:3's ve-ibane, "that I may be
BUILT") u-le-miqnehu asa SUKOT — booths FOR THE CATTLE — and the
noun's career: sukka 5521 tok1/8 DEBUT, toks 2-5 = LEV 23:34-43
(the FESTIVAL OF SUKKOT law: ba-sukot teshvu, "in BOOTHS you
shall dwell"), toks 6-8 = Deut 16:13,16 + 31:10 — every later
token of the booth-noun is the festival's: the feast of Booths'
whole vocabulary springs from cattle-shelters at a road-fork;
AL KEN qara shem ha-maqom SUKOT — al-ken etiology = REPORT class
(gen_45's 26:33 law: no NAME write; the registry sleeps); the
PLACE sukot (5523 toks 1-2/6) career: tok3 = EXOD 12:37 — "the
children of Israel journeyed FROM RAMSES TO SUKKOT": the
Exodus's FIRST STATION bears this stop's name (+ 13:20, Num
33:5-6 the itinerary pair).
(11) 33:18-19 THE ARRIVAL AND THE SECOND PURCHASE: va-yavo yaaqov
SHALEM (8003 tok2/6 — the WHOLE-word: tok1 = 15:16, "the iniquity
of the Amorite is NOT YET WHOLE"; tok2 = Jacob arriving WHOLE to
Shechem's city — the word's two Genesis tokens weigh an unfilled
measure and a filled man) ir shekhem (7927 tok2/18 — Shechem's
second token; toks 4-18 = the Dinah story's cast, next unit's
span) be-eretz KENAAN be-voo mi-PADAN ARAM (3667 tok20/65; 6307
tok7/11) — the return-formula closes 28:2's departure arc: sent
to Paddan-Aram (toks 2-5, gen_47's span), back from Paddan-Aram;
va-YICHAN et pene ha-ir (2583 tok2/86 — the ENCAMP-verb: tok1 =
26:17 Isaac in Gerar's wadi; tok2 = Jacob before Shechem; toks
3+ = the wilderness itinerary's va-yachanu — the encamping of
Israel's journeys debuts its patriarch-leg here); va-YIQEN et
chelqat ha-sade (7069 tok5/25 — the BUY-verb: tok4 = 25:10 "the
field ABRAHAM BOUGHT" (Machpelah), tok5 = Jacob's plot — the
Torah's two patriarch land-purchases are adjacent career tokens;
toks 11-12 = 49:30/50:13, Machpelah retold at the burials);
CHELQAT (2513 tok2/3) — the SMOOTH/PORTION homograph: tok1 =
27:16, chelqat tzavarav — "the SMOOTH of his neck", the
deception's kid-skin site; tok2 = the PORTION of field — the
word that dressed the lie buys the first homestead (tok3 = Deut
33:21); mi-yad bene CHAMOR (2544 tok1/11 DEBUT — Hamor: all
eleven tokens are this purchase + the Dinah story) avi shekhem;
be-mea QESITA (7192 tok1/1 HAPAX — the coin-word, once ever in
the Torah); nata sham aholo (5186 tok4/50).
(12) 33:20 THE ALTAR AND THE OBLIQUE WRITE [CROWN 2]. Divine-name
walk: Elohim ×3 (33:5,10,11 — all in grace-speech) + el elohe
yisrael (33:20); YHWH ×0 in-span [debut_map 3068 — no token in
Gen 33]; the unit's God-talk is all chen/chanan grammar until
the altar speaks El.

WATCHLIST ARMS (prospective, filed): shekhem toks 4-18 + chamor
toks 2-11 + ir tokens = GEN 34 (the Dinah span, next block-run's
door); 35:1-7 (qum aleh bet-el: the altar God COMMANDS after the
altar Jacob volunteered; mizbeach toks 11-13); 35:10 (the Israel
formula-write); 35:14/20 (va-yatzev toks 9-10: pillar and
grave-pillar); 43:29 (chanan tok4 over Benjamin); 47:17 (nahal
tok2); Exod 12:37 (sukkot station); Exod 15:13 (nehalta); Lev 1:4
(the acceptance-formula; ratzah career); Lev 23:34-43 (the
Sukkot festival law); Num 6:25 (the priestly blessing's chanan);
Deut 3:23 (va-etchanan).
"""

# ---------------------------------------------------------------------------

STEPS = [
 dict(ref=(33,1), op="THE_LIFTED_EYES_AND_THE_SPLIT",
  en="And Jacob lifted his eyes and saw, and behold, Esau was coming, and with him four hundred men. And he divided the children unto Leah and unto Rachel and unto the two maids.",
  tl_en="Jacob saw Esau coming with four hundred men",
  tr_en="he divided the children among the mothers",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yar_esav_ba_va_yachatz(arba_meot_ish), t0)",
    frag=("va-yisa",7), prose="""
THE COLUMN FORMS [care 1]. va-yisa yaaqov enav va-yar (5375
tok24/168; 7200 tok82/396) [VERIFIED: SNAPSHOT Gen.33.1 idx0-3] —
the lifted eyes meet the feared sight: esav ba ve-imo arba meot
ish — the 32:7 army-count arrives in narrative present.
va-yachatz (2673 tok2/6) [VERIFIED: idx11 ordinal=2/6] — gen_55's
divide-verb, one career-token later, divides the CHILDREN as it
divided the camps: the split-strategy shrinks from camps to kids.
REGISTRY 0. TESTS 0. Onkelos BUFFER PENDING."""),
  ],
  comment="The four hundred arrive; the divide-verb moves from camps to children."),

 dict(ref=(33,2), op="THE_ORDER_OF_LOVE",
  en="And he put the maids and their children first, and Leah and her children behind, and Rachel and Joseph hindmost.",
  tl_en="the maids and their children first",
  tr_en="Leah behind, Rachel and Joseph hindmost",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(rishona_acharonim_acharonim(seder_ha_machane), t0)",
    frag=("va-yasem",6), prose="""
THE LAST-WORD DEBUTS DOUBLE [care 1]. va-yasem (7760 tok28/152 —
the set-verb of gen_54's saga now arranges the family);
acharonim ×2 (314 toks 1-2/11 DEBUT) [VERIFIED: SNAPSHOT Gen.33.2
idx9,14 ordinals=1-2/11] — the LAST-word enters the Torah twice
in one verse, both times marking the protected rear; rishona
(7223 tok7/55) [VERIFIED: idx5]. yosef (3130 tok3/175) [VERIFIED:
idx13 ordinal=3/175] — Joseph's first NARRATIVE token (toks 1-2 =
his naming, gen_51): the story meets the boy hindmost-placed,
the safest slot in a feared line."""),
  ],
  comment="Joseph enters the narrative in the safest place; the last-word is born."),

 dict(ref=(33,3), op="THE_BOW_INVERTED",
  en="And he himself crossed over before them and bowed to the ground seven times, until he came near to his brother.",
  tl_en="he himself crossed over before them",
  tr_en="bowed to the ground seven times, nearing his brother",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yishtachu_sheva_peamim(hipukh_ha_berakha), t0)",
    frag=("va-yishtachu",4), prose="""
THE BLESSING PERFORMED BACKWARDS [care 2]. ve-hu avar li-fenehem
(5674 tok19/130) [VERIFIED: SNAPSHOT Gen.33.3 idx1] — the
cross-verb: the man who ordered others before him (32:17) now
crosses FIRST. va-yishtachu artza sheva peamim (7812 tok12/47)
[VERIFIED: idx3 ordinal=12/47] — THE INVERSION: the bow-verb's
toks 9-11 are 27:29's own decree — "peoples will bow to you...
your mother's sons will bow to you" (gen_46's stolen blessing,
ketiv token included) — and its VERY NEXT token is JACOB bowing,
seven times, TO THE BROTHER: decree → inverse performance,
consecutive tokens, the stolen blessing's own grammar walking
backwards. sheva peamim (7651 tok29/185; 6471 tok7/39)
[VERIFIED: idx5-6] — the seven-word that counted served years
now counts prostrations. ad gishto ad achiv (5066 tok11/45) —
the approach-verb warms toward care 5's waves."""),
  ],
  comment="The bow-decree's next token bows the wrong way, seven times."),

 dict(ref=(33,4), op="THE_HAND_BECOMES_ARMS",
  en="And Esau ran to meet him and embraced him, and fell on his neck and kissed him; and they wept.",
  tl_en="Esau ran, embraced him, fell on his neck, kissed him",
  tr_en="and they wept",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yechabqehu_va_yivku(esav_ve_yaaqov), t0)",
    frag=("va-yaratz",4), prose="""
THE FIRST PLURAL WEEPING [care 3]. va-yaratz esav liqrato (7323
tok9/12; 7125 tok10/31) [VERIFIED: SNAPSHOT Gen.33.4 idx0-2] —
the run-verb's second cycle-arrival (Laban ran to Jacob, 29:13
tok8; Esau runs to him now). va-yechabqehu (2263 tok2/3)
[VERIFIED: idx3 ordinal=2/3] — the embrace-verb: Laban's
arrival-embrace (29:13), Esau's return-embrace, Jacob's
grandsons (48:10) — the career is three family embraces.
va-yipol al TZAVARAV (5307 tok11/58; 6677 tok3/9) [VERIFIED:
idx4-6; ordinal=3/9] — the NECK-word's first three tokens:
27:16 the kid-skins ON JACOB'S NECK (the costume), 27:40 the
yoke ON ESAU'S NECK (the anti-blessing), 33:4 Esau falling ON
THE DECEIVER'S NECK — disguise, yoke, embrace. va-yishaqehu
(5401 tok7/13) [VERIFIED: idx7] — the kiss-walk's
reconciliation token. VA-YIVKU (1058 tok5/29, HC/Vqw3mp)
[VERIFIED: idx8 morph=HC/Vqw3mp] — the weep-verb's toks 1-4 are
all SINGULAR (Hagar, Abraham, ESAU ALONE at 27:38, Jacob at
29:11) [VERIFIED: morph census toks 1-4] — tok5 is its FIRST
PLURAL: the man who wept alone at the theft weeps WITH the
thief. GEN_55 LANDING-NOTE (frozen ledger untouched): the
hatzileni-card's feared mi-yad esav (from Esau's HAND) arrives
as arms around the neck — no rescue-verb fires; the fear
dissolves without its demanded root."""),
  ],
  comment="The feared hand embraces; the weep-verb learns the plural."),

 dict(ref=(33,5), op="THE_GRACE_VERB_IS_BORN",
  en="And he lifted his eyes and saw the women and the children, and said: Who are these to you? And he said: The children with whom God has graced your servant.",
  tl_en="who are these to you?",
  tr_en="the children with whom God has graced your servant",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(ha_yeladim_asher_chanan_Elohim(maane_yaaqov), t0)",
    frag=("chanan",4), prose="""
CHANAN DEBUTS [care 4]. mi ele lakh (4310 tok13/55) — Esau's
question; ha-yeladim asher CHANAN Elohim et avdekha (2603
tok1/10 DEBUT) [VERIFIED: SNAPSHOT Gen.33.5 idx15 ordinal=1/10]
— the GRACE-verb enters the Torah counting children; tok2 =
33:11 chanani (both debut-tokens live in this one meeting);
full career: 42:21 (Joseph's pleading recalled), 43:29 (Joseph
graces Benjamin with this verse's own shape), Exod 33:19 ×2
("I will be gracious to whom I will be gracious" — the
Attributes' grammar), Num 6:25 (the priestly blessing's
vi-chuneka), Deut 3:23 (va-etchanan), and the closing
grace-denials (Deut 7:2 lo techanem, 28:50 lo yachon) — the
verb REACHES the priestly blessing from a father's answer about
children. avdekha (5650 tok43/180) — the
servant-grammar survives the embrace."""),
  ],
  comment="The grace-verb opens on children and reaches the priestly blessing."),

 dict(ref=(33,6), op="THE_FIRST_WAVE",
  en="And the maids came near, they and their children, and they bowed.",
  tl_en="the maids came near with their children",
  tr_en="and they bowed",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_tigashna_va_tishtachavena(ha_shefachot), t0)",
    frag=("va-tigashna",5), prose="""
THE WAVES BEGIN [care 5; etnachta-less verse #1 — five tokens,
no mid-verse rest: split at the tifcha idx3 (rank 2), the
gen_03 1:13 fallback]. va-tigashna (5066 tok12/45) [VERIFIED:
SNAPSHOT Gen.33.6 idx0 ordinal=12/45] — the approach-verb:
toks 8-9 were 27:26-27's gesha-na, the deception's
"come-near-and-kiss"; the family now approaches the deceived
line's son wave by wave. va-tishtachavena (7812 tok13/47) —
bow-wave one."""),
  ],
  comment="First bowing wave; the approach-verb's deception tokens behind it."),

 dict(ref=(33,7), op="THE_SECOND_AND_THIRD_WAVES",
  en="And Leah too came near, and her children, and they bowed; and after came Joseph near, and Rachel, and they bowed.",
  tl_en="Leah and her children came near and bowed",
  tr_en="after them Joseph and Rachel bowed",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yishtachavu_kulam(lea_yosef_ve_rachel), t0)",
    frag=("va-tigash",5), prose="""
THE ORDER HOLDS [care 5]. va-tigash gam lea... ve-achar NIGASH
YOSEF ve-rachel (5066 toks 13-14/45; 3130 tok4/175) [VERIFIED:
SNAPSHOT Gen.33.7 idx0,6-8] — the child placed last comes last,
and the letter puts JOSEPH BEFORE RACHEL in the approach (nigash
yosef ve-rachel — the boy steps ahead of his mother; his second
narrative token is already an act). hishtachavah toks 14-15/47 —
bow-waves two and three: the 27:29 decree's verb has now bowed
this household to Esau five times in five verses."""),
  ],
  comment="Joseph steps before Rachel; the bowing count reaches the whole house."),

 dict(ref=(33,8), op="THE_CAMP_EXPLAINED",
  en="And he said: What to you is all this camp which I met? And he said: To find grace in the eyes of my lord.",
  tl_en="what is all this camp which I met?",
  tr_en="to find grace in the eyes of my lord",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(mi_lekha_kal_ha_machane(pagashti), t0)",
    frag=("mi",6), prose="""
THE MET ONE SPEAKS [care 6]. mi lekha kal ha-machane ha-ze asher
PAGASHTI (4264 tok7/104; 6298 tok2/4) [VERIFIED: SNAPSHOT
Gen.33.8 idx1-7; pagashti ordinal=2/4] — gen_55's meet-verb
(born at 32:18 in Jacob's anticipation-script) returns in ESAU'S
mouth: the encounter scripted in fear is narrated by its object
as a puzzle; the camp-word's first token in ANOTHER SPEAKER'S
mouth (toks 1,3,4,5 are Jacob's speech; 2 and 6 the
narrator's). li-metzo chen be-ene adoni (2580 tok6/27; 113 tok35/91)
[VERIFIED: idx9-12] — the grace-formula, first of three in-span;
adoni — five my-lord tokens in this meeting (toks 35-39/91): the
blessing's "be lord to your brothers" stays reversed in Jacob's
grammar to the end."""),
  ],
  comment="The feared meeting retold as Esau's question; grace-formula one."),

 dict(ref=(33,9), op="THE_KEEP_IT_JUSSIVE",
  en="And Esau said: I have much, my brother; let what is yours be yours.",
  tl_en="and Esau said: I have much",
  tr_en="my brother — let what is yours be yours",
  ops=[
   dict(op="DECLARE",
    expr="DECLARE(esav, LET(yehi(lekha_asher_lakh)))",
    frag=("yesh",4), prose="""
THE KEEP-DEMAND [UNIT SHAPE (1)]. yesh li RAV achi (3426
tok8/30; 7227 tok10/66) [VERIFIED: SNAPSHOT Gen.33.9 idx2-5] —
"I have MUCH, my brother" — and ACHI: Esau's first direct
brother-address to Jacob in the corpus's narrative present
(27:41's brother-talk was inner speech; token-note). YEHI lekha
asher lakh (1961 tok207/1050, HVqj3ms TRUE JUSSIVE) [VERIFIED:
idx6 morph=HVqj3ms] — the mood law (gen_32: the letter's mood
decides) pushes the courtesy: let-what-is-yours-BE-yours, a
jussive of the be-verb aimed at Jacob's property. Its fate is
the unit's strangest: no haya-root receipt ever fires, and at
33:11 the DEMANDER HIMSELF takes the gift his jussive declined
— the demand undone by its own issuer (self-reversal, filed to
the mismatch family). PUSH LET(yehi(lekha_asher_lakh)).
Depth 1."""),
  ],
  comment="Esau's keep-it jussive pushes; its own speaker will reverse it."),

 dict(ref=(33,10), op="THE_FACE_CODA_AND_THE_ACCEPT_VERB",
  en="And Jacob said: No, please — if now I have found grace in your eyes, then take my offering from my hand; for therefore have I seen your face, as one sees the face of God, and you have accepted me.",
  tl_en="take my offering from my hand",
  tr_en="I saw your face as one sees God's face — you accepted me",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(ki_reot_pene_Elohim_va_tirtzeni(peniel_coda), t1)",
    frag=("ki",9), prose="""
THE ACCEPTANCE-VERB IS BORN [care 6]. al na... ve-laqachta
minchati mi-yadi (3947 tok101/393 weqatal — duty-content shape
warming the take-verb one verse before the pop; 4503 tok8/113 —
the offering-noun's brother-token, its Cain-and-Abel debut
inverted into appeasement accepted). ki al ken RAITI FANEKHA
KI-REOT PENE ELOHIM (7200 toks 84-85/396; 6440 toks 90-91/627)
[VERIFIED: SNAPSHOT Gen.33.10 idx15-18] — the face-coda: one
unit after panim-el-panim (32:31), Jacob names his brother's
face with God's — gen_55's ten-face walk closes on Esau's.
VA-TIRTZENI (7521 tok1/14 DEBUT, HC/Vqw2ms/Sp1cs) [VERIFIED: idx20
ordinal=1/14] — the ACCEPT-verb enters the Torah in a brother's
welcome; its career is the altar's acceptance-formula — Lev 1:4
ve-nirtza lo ("it shall be ACCEPTED for him"), Lev 7:18, 19:7,
22:23-27 yeratze — and Lev 26's sabbath-repayments: offering-
noun and acceptance-verb share this sentence a chapter before
Jacob's first altar. Depth 1."""),
  ],
  comment="Your face as God's face; the acceptance-verb debuts pre-altar."),

 dict(ref=(33,11), op="THE_POP_THE_BLESSING_RETURNED",
  en="Take, please, my blessing that was brought to you, for God has graced me, and because I have all. And he urged him, and he took.",
  tl_en="take, please, my blessing that was brought to you",
  tr_en="he urged him — and he took",
  ops=[
   dict(op="DECLARE",
    expr="DECLARE(yaaqov, LET(qach_na_et_birkhati(esav)))",
    frag=("qach",4), prose="""
THE RETURNED WORD [CROWN; UNIT SHAPE (2)]. qach na et BIRKHATI
(3947 tok102/393, HVqv2ms; 1293 tok9/30) [VERIFIED: SNAPSHOT
Gen.33.11 idx0-3 morph=HVqv2ms; ordinal=9/30] — the
blessing-noun's toks 3-7 are the Gen 27 wound (27:35 "he took
YOUR blessing", 27:36 Esau's cry "he took MY BLESSING —
birkhati", 27:38,41); now the taker says TAKE (the very laqach
of 27:35-36) + MY BLESSING (Esau's own word) — TO ESAU: the
theft-cry's verb and noun with speaker and addressee exchanged.
asher HUVAT lakh (935 tok114/619, hophal) — brought-to-you, the
gift gone passive. ki chanani Elohim (2603 tok2/10 — the
grace-verb's second debut-token) ve-khi yesh li KHOL (3605
tok239/1595) — Esau said RAV ("much"), Jacob answers KHOL
("all"): the two inventories one verse apart. PUSH
LET(qach_na_et_birkhati(esav)). Depth 2."""),
   dict(op="RESULT",
    expr="HOLDS(qach_na_et_birkhati(esav), t2)",
    frag=("va-yiftzar",3), prose="""
THE RUN'S FIRST POP. va-yiftzar bo VA-YIQACH (6484 tok3/3
CLOSES; 3947 tok103/393) [VERIFIED: SNAPSHOT Gen.33.11 idx14-16;
ordinals 3/3, 103/393] — the demand's own root returns as a
foreground deed by the demandee IN THE SAME VERSE: qach (tok102)
→ va-yiqach (tok103), demand and receipt CONSECUTIVE career
tokens, latency zero (the echo-receipt law, gen_25/gen_35;
gen_51's bo-pop ran latency one verse). After gen_54 and gen_55
pushed fourteen cards and popped none, the first RESULT of the
run fires on TAKE-BACK-THE-BLESSING — the Gen 27 debt is the
one demand the letter clears. AND THE SELF-REVERSAL [UNIT SHAPE
(1)]: the taking undoes 33:9's yehi — Esau performs the
opposite of his own keep-it jussive; that card stays OPEN (no
haya-receipt), its content reversed by its own demander.
va-yiftzar — the URGE-verb's whole career closes here: Lot
urging the angels (19:3), the mob urging Lot (19:9), Jacob
urging Esau — two Sodom doors and a reconciliation. Depth 1."""),
  ],
  comment="The stolen-blessing sentence performed in reverse; the run's first pop."),

 dict(ref=(33,12), op="THE_DECLINED_CONVOY",
  en="And he said: Let us journey and go, and I will go opposite you.",
  tl_en="let us journey and go",
  tr_en="I will go opposite you",
  ops=[
   dict(op="DECLARE",
    expr="DECLARE(esav, CMD-US?(nisa_ve_nelekha(esav_ve_yaaqov)))",
    frag=("nisa",4), prose="""
THE JOINT-JOURNEY CARD [UNIT SHAPE (3)]. nisa ve-nelekha (5265
tok6/120, HVqh1cp; 3212 tok66/229, HC/Vqh1cp — DOUBLE true
cohortative) [VERIFIED: SNAPSHOT Gen.33.12 idx1-2 morphs
HVqh1cp, HC/Vqh1cp] — TIR-033: cohortative → CMD-US, ?-guard
kept while the receipt path stays open (gen_45's law). ve-elkha
le-negdekha (5048 tok7/17) [VERIFIED: idx4 ordinal=7/17] — "I
will go OPPOSITE you": neged, the helper-word of 2:18's
ke-negdo, offered brother-to-brother. The card's fate is 33:16-17
[see step 33:17]. PUSH CMD-US?(nisa_ve_nelekha(...)). Depth 2."""),
  ],
  comment="Esau's double cohortative pushes guarded; the convoy is proposed."),

 dict(ref=(33,13), op="THE_TENDER_PACE",
  en="And he said to him: My lord knows that the children are tender, and the flock and herd giving suck are upon me; and were they overdriven one day, all the flock would die.",
  tl_en="my lord knows the children are tender",
  tr_en="overdriven one day, all the flock would die",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(ha_yeladim_rakim_ve_alot_alay(taanat_yaaqov), t2)",
    frag=("adoni",5), prose="""
TWO HAPAXES IN THE EXCUSE [care 8]. adoni yodea ki ha-yeladim
RAKIM (7390 tok3/6) [VERIFIED: SNAPSHOT Gen.33.13 idx6
ordinal=3/6] — TENDER: tok2 = 29:17, Leah's tender eyes — the
word's two Jacob-cycle tokens are eyes and children. ve-ha-tzon
ve-ha-baqar ALOT alay (5763 tok1/1 HAPAX) [VERIFIED: idx9
ordinal=1/1] — the nursing ones, named once in the Torah.
U-DEFAQUM yom echad (1849 tok1/1 HAPAX) [VERIFIED: idx11
ordinal=1/1] — the OVERDRIVE-verb, conjugated once ever, in a
shepherd's refusal; va-metu kal ha-tzon (4191 tok40/303) — the
diplomatic mortality forecast. Depth 2."""),
  ],
  comment="The pace-plea carries two of the Torah's one-time words."),

 dict(ref=(33,14), op="THE_PASS_BEFORE_JUSSIVE",
  en="Let my lord pass, please, before his servant, and I will lead on gently at my slow pace, at the foot of the work before me and at the foot of the children, until I come to my lord, to Seir.",
  tl_en="let my lord pass before his servant",
  tr_en="I will lead gently — until I come to my lord, to Seir",
  ops=[
   dict(op="DECLARE",
    expr="DECLARE(yaaqov, LET(yaavar_na(adoni, li_fene_avdo)))",
    frag=("yaavar",5), prose="""
THE PASS-CARD [UNIT SHAPE (4)]. yaavar na adoni li-fene avdo
(5674 tok20/130, HVqj3ms TRUE JUSSIVE) [VERIFIED: SNAPSHOT
Gen.33.14 idx0 morph=HVqj3ms ordinal=20/130] — the cross-verb
AGAIN as a demand (gen_55's ivru card was its imperative): mood
law pushes the courtesy-jussive. Esau never passes-before: 33:16
narrates SHUV (returned to his way) — the other root (gen_45
Excerpt B) — card OPEN. va-ani ETNAHALA (5095 tok1/3 DEBUT,
HVth1cs — self-commit content, no second push) [VERIFIED: idx6
ordinal=1/3] — the LEAD-GENTLY verb: tok2 = 47:17 (Joseph
leading Egypt through famine-bread), tok3 = Exod 15:13 NEHALTA
("You LED in Your strength to Your holy habitation") — from
flock-pace to the Song of the Sea. LE-ITI (328 tok1/1 HAPAX)
[VERIFIED: idx7 ordinal=1/1] — "at my slow pace", once ever.
le-regel ha-MELAKHA (4399 tok4/65) [VERIFIED: idx9 ordinal=4/65]
— the WORK-noun: toks 1-3 are God's own melakha at 2:2-3 (the
Sabbath's thrice-said word); tok4 is the drovers' — the
labor-noun's first post-creation token walks toward Exod 20:9's
Sabbath command. ad asher avo el adoni SEIRA — the stated
Seir-arrival has NO narrated token anywhere in the corpus
(Jacob's next station is 33:17's Sukkot; letter-note only,
intent not adjudicated). PUSH LET(yaavar_na(...)). Depth 3."""),
  ],
  comment="Pass-before pushed; the gentle-lead verb debuts toward the Sea-song."),

 dict(ref=(33,15), op="THE_DECLINED_GARRISON",
  en="And Esau said: Let me station with you, please, some of the people who are with me. And he said: Why so? Let me find grace in the eyes of my lord.",
  tl_en="let me station some of my people with you",
  tr_en="why so? let me find grace in my lord's eyes",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(atziga_na_declined(la_ma_ze), t3)",
    frag=("atziga",5), prose="""
THE OFFER DIES POLITELY [care 9]. atziga-na imkha (3322 tok2/6,
HVhh1cs) [VERIFIED: SNAPSHOT Gen.33.15 idx2 morph=HVhh1cs
ordinal=2/6] — a 1cs cohortative OFFER (gen_52's 30:31 ashuva
self-commit class; gen_47's no-addressee law: the speaker
volunteers his own act — no push): the STATION-verb's tok1 =
30:38, Jacob stationing the rods (gen_52's device); tok2 = Esau
offering to station MEN; toks 3-4 = 43:9 (Judah setting Benjamin
before his father), 47:2 (Joseph stationing brothers before
Pharaoh). Declined: la-ma ze EMTZA chen be-ene adoni (4672
tok34/122, HVqh1cs inside a rhetorical question — no push; 2580
tok8/27) — the grace-formula's third sounding closes the
negotiation: no convoy, no garrison, just grace. Depth 3."""),
  ],
  comment="The station-offer declined; three grace-formulas seal the parting."),

 dict(ref=(33,16), op="THE_FIRST_VECTOR",
  en="And Esau returned that day on his way to Seir.",
  tl_en="Esau returned that day",
  tr_en="on his way to Seir",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yashav_esav_seira(le_darko), t3)",
    frag=("va-yashav",6), prose="""
THE OTHER ROOT [UNIT SHAPE (4); etnachta-less verse #2 — six
tokens, split at the tifcha idx4 (rank 2), gen_03 1:13
fallback]. va-yashav ba-yom ha-hu esav le-darko SEIRA (7725
tok40/180; 1870 tok18/116; 8165 tok4/20) [VERIFIED: SNAPSHOT
Gen.33.16 idx0-5] — the yaavar-card asked PASSING-BEFORE; the
letter gives Esau RETURNING (shuv, the other root — gen_45
Excerpt B): the card holds OPEN, and the return-verb is the
very one YHWH's 31:3 command laid on JACOB — each brother now
carries a shuv: Jacob's commanded return (still OPEN in
gen_53's frozen ledger), Esau's narrated one. le-darko — the
derekh-noun's two went-his-way tokens are JACOB at 32:2
(leaving Laban) and ESAU here [VERIFIED: 1870 toks 17-18]:
each parting of this cycle closes on the same formula.
Depth 3."""),
  ],
  comment="Esau exits on the other root; the pass-before card stands."),

 dict(ref=(33,17), op="THE_SECOND_VECTOR_AND_THE_BOOTHS",
  en="And Jacob journeyed to Sukkot, and built himself a house, and for his cattle he made booths; therefore he called the name of the place Sukkot.",
  tl_en="Jacob journeyed to Sukkot, built a house",
  tr_en="booths for his cattle; so the place is called Sukkot",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(ve_yaaqov_nasa_sukota(bayit_u_sukot, report_only), t3)",
    frag=("ve-yaaqov",3), prose="""
THE SOLO JOURNEY [UNIT SHAPE (3); care 10]. ve-yaaqov NASA
sukota (5265 tok7/120) [VERIFIED: SNAPSHOT Gen.33.17 idx1
ordinal=7/120] — the journey-verb's tok6 was 33:12's NISA — the
let-US-journey cohortative itself; tok7 is Jacob journeying
ALONE, the other way: demand → solo deed, consecutive tokens —
the CMD-US? card's non-receipt written into the career (joint
demanded, single performed, opposite vector; card OPEN).
va-yiven lo BAYIT (1129 tok15/41; 1004 tok43/324) — Jacob's
first house-building (his cycle's earlier build-token is 30:3's
ve-ibane, "that I may be BUILT" — person then property);
u-le-miqnehu asa SUKOT (5521 tok1/8 DEBUT) [VERIFIED: idx8
ordinal=1/8] — THE BOOTH-NOUN IS BORN as cattle-shelter, and
every later token is the FESTIVAL'S: Lev 23:34-43 (chag
ha-SUKOT; ba-SUKOT teshvu — "in booths you shall dwell", toks
2-5), Deut 16:13,16, 31:10 (toks 6-8) — the feast of Booths'
entire vocabulary springs from livestock sheds at a road-fork
(init→law, the run's second specimen). AL KEN qara shem
ha-maqom sukot — al-ken etiology: REPORT class (gen_45's 26:33
law), NO write, the registry sleeps; the PLACE-name's career
(5523 toks 1-2/6): tok3 = EXOD 12:37 — "the children of Israel
journeyed from Ramses TO SUKKOT": the Exodus's FIRST STATION
bears this stop's name (13:20, Num 33:5-6 continue the
itinerary). Depth 3."""),
  ],
  comment="The us-journey performs solo; the festival's noun is born in a shed."),

 dict(ref=(33,18), op="THE_WHOLE_ARRIVAL",
  en="And Jacob came whole to the city of Shechem, which is in the land of Canaan, in his coming from Paddan-Aram; and he encamped before the city.",
  tl_en="Jacob came whole to the city of Shechem",
  tr_en="from Paddan-Aram; he encamped before the city",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yavo_shalem_mi_padan_aram(va_yichan), t3)",
    frag=("va-yavo",5), prose="""
SHALEM [care 11]. va-yavo yaaqov SHALEM ir shekhem (935
tok116/619; 8003 tok2/6; 7927 tok2/18) [VERIFIED: SNAPSHOT
Gen.33.18 idx0-4; shalem ordinal=2/6] — the WHOLE-word's two
Genesis tokens: 15:16 "the iniquity of the Amorite is NOT YET
WHOLE" and Jacob arriving WHOLE — an unfilled measure and a
filled man. be-eretz kenaan be-voo MI-PADAN ARAM (3667
tok20/65; 6307 tok7/11) [VERIFIED: idx6-10] — the return-
formula closes 28:2's arc: sent to Paddan-Aram (gen_47's
departure tokens), back from it — the Laban cycle's geographic
bracket shuts. va-YICHAN et pene ha-ir (2583 tok2/86)
[VERIFIED: idx11 ordinal=2/86] — the ENCAMP-verb: tok1 = 26:17
(Isaac in Gerar's wadi); tok2 = Jacob before Shechem; its
career becomes the wilderness itinerary's va-yachanu (Exod
13:20 onward) — Israel's encampments debut their patriarch-leg.
shekhem toks 2-3/18 + ha-ir — the Dinah story's stage assembles
(toks 4-18 = Gen 34; next block-run's door). Depth 3."""),
  ],
  comment="Whole to Shechem; the encamp-verb starts Israel's itinerary grammar."),

 dict(ref=(33,19), op="THE_SECOND_PURCHASE",
  en="And he bought the portion of the field where he had pitched his tent from the hand of the sons of Hamor, father of Shechem, for a hundred qesita.",
  tl_en="he bought the portion of the field",
  tr_en="from the sons of Hamor, for a hundred qesita",
  ops=[
   dict(op="PRECONDITION_STATE",
    expr="HOLDS(va_yiqen_chelqat_ha_sade(be_mea_qesita), t3)",
    frag=("va-yiqen",4), prose="""
THE SMOOTH WORD BUYS A FIELD [care 11]. va-YIQEN (7069 tok5/25)
[VERIFIED: SNAPSHOT Gen.33.19 idx0 ordinal=5/25] — the BUY-verb:
tok4 = 25:10, "the field ABRAHAM BOUGHT" (Machpelah); tok5 =
Jacob's plot — the Torah's two patriarch land-purchases sit on
adjacent career tokens (toks 11-12 = 49:30/50:13, Machpelah
retold at the burials). CHELQAT ha-sade (2513 tok2/3) [VERIFIED:
idx2 ordinal=2/3] — the SMOOTH/PORTION homograph: tok1 = 27:16,
chelqat tzavarav — "the SMOOTH of his neck", the kid-skin site
of the deception; tok2 = the PORTION of field: the word that
dressed the lie buys the first homestead (tok3 = Deut 33:21).
mi-yad bene CHAMOR (2544 tok1/11 DEBUT) [VERIFIED: idx10
ordinal=1/11] — Hamor: all eleven tokens are this purchase and
the Dinah story it stages. be-mea QESITA (7192 tok1/1 HAPAX)
[VERIFIED: idx14 ordinal=1/1] — the coin-word, once in the
Torah. nata sham aholo (5186 tok4/50) — tent pitched on owned
ground. Depth 3."""),
  ],
  comment="The deception's smooth-word buys the field; the coin is a hapax."),

 dict(ref=(33,20), op="THE_ALTAR_AND_THE_OBLIQUE_WRITE",
  en="And he set up there an altar, and called it El-Elohe-Israel [God, the God of Israel].",
  tl_en="he set up there an altar",
  tr_en="and called it El-Elohe-Israel",
  ops=[
   dict(op="REGISTRY_INSTALL",
    expr="WORLD += {ha_mizbeach}",
    frag=("va-yatzev",3), prose="""
THE FIRST ALTAR [CROWN 2; care 12]. va-YATZEV sham MIZBEACH
(5324 tok8/28; 4196 tok10/198) [VERIFIED: SNAPSHOT Gen.33.20
idx0-2; ordinals 8/28, 10/198] — Jacob's FIRST altar: the
altar-noun's toks 1-9 are his fathers' — Noah ×2 (8:20), Abram
×4 (12:7, 12:8, 13:4, 13:18), Moriah ×2 (22:9), Isaac (26:25)
[VERIFIED: debut_map 4196 toks 1-9]; tok10 is his. The set-up verb's career: toks 6-7 = 28:12-13 —
the ladder SET UP (mutzav) and YHWH STANDING (nitzav) upon it;
tok8 = this altar; toks 9-10 = 35:14 (Bethel's pillar) and
35:20 (Rachel's grave-pillar): ladder, altar, pillar, grave.
WORLD += ha_mizbeach."""),
   dict(op="NAME",
    expr="name(ha_mizbeach) := el_elohe_yisrael",
    frag=("va-yiqra",5), prose="""
WRITE #1 — ISRAEL ENTERS THE REGISTRY OBLIQUELY. va-yiqra LO
el elohe yisrael (7121 tok82/193; 410 tok11/50; 3478 tok3/587)
[VERIFIED: SNAPSHOT Gen.33.20 idx3-7] — full va-yiqra-lo
formula: the write FIRES (contrast 32:29's decree, which wrote
nothing — gen_33's class) — and the VALUE carries the decreed
name: el_elohe_yisrael, "El, God of ISRAEL" — yisrael's third
Torah token, and the registry's first: the renamed man's first
naming-act files his own new name inside God's title on an
altar — the ledger meets israel as a genitive of El before it
ever meets it as the man's label (35:10's formula-write is
still ahead; the gen_33 NAME-triage neighborhood stays OPEN,
no ruling sought). The el-word (410): gen_54's power-idiom
observation aside, this token is El the name proper, on
Jacob's lips over his first altar. UNIT END: SPECS depth 3
OPEN (yehi — self-reversed by its own demander ·
nisa_ve_nelekha — answered by a solo journey the other way ·
yaavar_na — answered in the other root); ONE POP (the
returned blessing — the run's only cleared card). REGISTRY 1
write. TESTS 0 [VERIFIED: zero tov-adjective tokens in Gen
33]. YHWH ×0 in-span; Elohim ×3 + el elohe yisrael — the
unit's God-grammar runs on grace until the altar speaks."""),
  ],
  comment="The first altar takes the wrestled name into the ledger, inside El's title."),
]

# ---------------------------------------------------------------------------

def _s(id, ref, frag, title, given, expect, occ=1):
    d = dict(id=id, ref=ref, frag=frag, title=title, given=given, expect=expect)
    d["occ"] = occ
    return d

YH = "LET(yehi(lekha_asher_lakh)) pushed and OPEN;"
QB = "LET(qach_na_et_birkhati(esav)) pushed and OPEN;"
NV = "CMD-US?(nisa_ve_nelekha(esav_ve_yaaqov)) pushed and OPEN;"
YA = "LET(yaavar_na(adoni, li_fene_avdo)) pushed and OPEN;"
NTN = "no test, no name."
R1 = "REGISTRY 1 writes"

SCENS = [
 _s("S1", (33,1), ("va-yisa",7),
    "after STEP_Gn_33_1 — the four hundred arrive; queue empty",
    "Esau was coming, and with him four hundred men.",
    ["SPECS empty;", NTN]),
 _s("S2", (33,2), ("va-yasem",6),
    "after STEP_Gn_33_2 — the order of love; queue empty",
    "Rachel and Joseph hindmost.",
    ["SPECS empty;", NTN]),
 _s("S3", (33,3), ("va-yishtachu",4),
    "after STEP_Gn_33_3 — seven bows the wrong way; queue empty",
    "He bowed to the ground seven times, nearing his brother.",
    ["SPECS empty;", NTN]),
 _s("S4", (33,4), ("va-yaratz",4),
    "after STEP_Gn_33_4 — the embrace and the first plural weeping",
    "He fell on his neck and kissed him; and they wept.",
    ["SPECS empty;", NTN]),
 _s("S5", (33,5), ("chanan",4),
    "after STEP_Gn_33_5 — the grace-verb born; queue empty",
    "The children with whom God has graced your servant.",
    ["SPECS empty;", NTN]),
 _s("S6", (33,6), ("va-tigashna",5),
    "after STEP_Gn_33_6 — the first wave bows; queue empty",
    "The maids came near with their children and bowed.",
    ["SPECS empty;", NTN]),
 _s("S7", (33,7), ("va-tigash",5),
    "after STEP_Gn_33_7 — all the waves have bowed; queue empty",
    "After came Joseph near, and Rachel, and they bowed.",
    ["SPECS empty;", NTN]),
 _s("S8", (33,8), ("mi",6),
    "after STEP_Gn_33_8 — the camp explained; queue empty",
    "What is all this camp which I met?",
    ["SPECS empty;", NTN]),
 _s("S9", (33,9), ("yesh",4),
    "after STEP_Gn_33_9 — the keep-it jussive pushed; depth 1",
    "I have much, my brother; let what is yours be yours.",
    [YH, NTN]),
 _s("S10", (33,10), ("ki",9),
    "after STEP_Gn_33_10 — the face-coda and the accept-verb; depth 1",
    "I saw your face as one sees the face of God.",
    [YH, NTN]),
 _s("S11", (33,11), ("va-yiftzar",3),
    "after STEP_Gn_33_11 — the blessing returned and TAKEN; depth 1",
    "Take, please, my blessing. And he urged him, and he took.",
    [YH, NTN]),
 _s("S12", (33,12), ("nisa",4),
    "after STEP_Gn_33_12 — the joint-journey pushed guarded; depth 2",
    "Let us journey and go, and I will go opposite you.",
    [YH, NV, NTN]),
 _s("S13", (33,13), ("adoni",5),
    "after STEP_Gn_33_13 — the tender-pace plea; depth 2",
    "The children are tender; overdriven one day, the flock dies.",
    [YH, NV, NTN]),
 _s("S14", (33,14), ("yaavar",5),
    "after STEP_Gn_33_14 — pass-before pushed; depth 3",
    "Let my lord pass before his servant; I will lead on gently.",
    [YH, NV, YA, NTN]),
 _s("S15", (33,15), ("atziga",5),
    "after STEP_Gn_33_15 — the garrison declined; depth 3",
    "Let me station some of my people — why so?",
    [YH, NV, YA, NTN]),
 _s("S16", (33,16), ("va-yashav",6),
    "after STEP_Gn_33_16 — Esau returns by the other root; depth 3",
    "Esau returned that day on his way to Seir.",
    [YH, NV, YA, NTN]),
 _s("S17", (33,17), ("ve-yaaqov",3),
    "after STEP_Gn_33_17 — the solo journey; the booths; depth 3",
    "Jacob journeyed to Sukkot and made booths for his cattle.",
    [YH, NV, YA, NTN]),
 _s("S18", (33,18), ("va-yavo",5),
    "after STEP_Gn_33_18 — whole to Shechem; depth 3",
    "Jacob came whole to the city of Shechem.",
    [YH, NV, YA, NTN]),
 _s("S19", (33,19), ("va-yiqen",4),
    "after STEP_Gn_33_19 — the field bought; depth 3",
    "He bought the portion of the field for a hundred qesita.",
    [YH, NV, YA, NTN]),
 _s("S20", (33,20), ("va-yatzev",3),
    "after STEP_Gn_33_20 — the first altar named; three open, one popped",
    "He set up an altar and called it El-Elohe-Israel.",
    [YH, NV, YA, "WORLD += ha_mizbeach;", R1]),
]
