# -*- coding: utf-8 -*-
"""Authored content for gen_59 (36:1-43). DB evidence: gen59_prestage_full.txt
(regenerable: python3 logic/solo_tools/prestage.py Gen 36:1-36:43) + targeted
queries logged in the derivation session 2026-08-07."""

UID = "gen_59_esau_edom_kings_ledger"
BOOK = "Gen"
SPAN = (36, 1, 36, 43)
EXTRA_SUBS = {
    # "ir-o" appears raw inside frozen gen_54 (substring scan, gen_57's
    # carve-out) — module-local polish, kings' city-lines 36:32,35,39.
    "ir-o": "iro",
}


META = [
    ("id", "gen_59_esau_edom_kings_ledger"),
    ("title_en", '"Esau is Edom: the ledger of chiefs and kings (36:1-43)"'),
    ("title_he", "וְאֵלֶּה הַמְּלָכִים אֲשֶׁר מָלְכוּ בְּאֶרֶץ אֱדוֹם"),
    ("title_he_translit", "ve-ele ha-melakhim asher malkhu be-eretz edom"),
    ("title_he_en", "\"'And these are the kings who reigned in the land of Edom'\""),
    ("book_he", "בְּרֵאשִׁית"),
    ("book_he_translit", "Be-reshit"),
    ("book_en", "Genesis"),
    ("refs", "36:1-43"),
    ("unit_span_planned", "36:1-43"),
]

DRAFT_NOTE = """
DRAFT 2026-08-07 · SOLO ERA unit #13 (Claude coordinator+deriver;
external fresh-context adversarial review before freeze per standing
law). Span: 36:1-43, whole chapter: 43 verses · 489 tokens
(SNAPSHOT-verified). SNAPSHOT + debut_map. bar C. Conventions: step
he: = plain (no accents/meteg; maqqef ־ per snapshot); tree halves =
accents kept, slashes stripped; split at etnachta — 36 of 43 verses
carry one; the seven without (36:1, 3, 8, 19, 28, 41, 42) split at
the prestage fallback (tifcha ×6, zaqef qatan ×1 — the
strongest-disjunctive rule). KETIV pair in span: yysh(!) / yeush at
36:5 and 36:14 (the ketiv-then-qere adjacent-token convention, Deut
22:21's h-nr class) — rendered per snapshot. Onkelos BUFFER PENDING.

UNIT SHAPE — ZERO pushes, ZERO pops, SPECS EMPTY THROUGHOUT: the
prestage volitive census is NONE (no imperative, jussive, or
cohortative token in 43 verses) — after the corpus's two largest
all-open walls back to back (gen_57's refused nine, gen_58's obeyed
nine), the run closes on its quietest board: a pure ledger (the
gen_14 / gen_24 / gen_26 / gen_42 toledot-class). No naming formula
anywhere — the chapter that coins dozens of names WRITES none
(list-mentions, not va-yiqra acts): REGISTRY 0. TESTS 0 [VERIFIED:
zero tov-adjective (2896) tokens in Gen 36]. The machine-profile is
the point: Esau's line gets forty-three verses of pure state — no
demand, no test, no write — the ledger of a house the covenant
thread has left.

CROWN 1 — THE REIGN-VERB'S THIRTEEN TOKENS (36:31): ve-ele
ha-melakhim asher MALKHU be-eretz edom li-fene MELAKH-MELEKH
li-vene yisrael — "before a king REIGNED for the sons of Israel":
the verb malakh (4427) enters the Torah in this verse and has
exactly THIRTEEN verb-tokens in the whole corpus [VERIFIED: full
census]: toks 1-10 are THIS SPAN's — Edom's eight kings reigning
and dying (36:31-39); toks 11-12 are 37:8 — the brothers' mockery
of Joseph, ha-MALOKH TIMLOKH alenu ("will you REIGN, reign over
us?"), the very next tokens after the span; tok13 is Exod 15:18 —
YHWH YIMLOKH le-olam va-ed, the Song at the Sea's forever-reign:
ten Edomite reigns, two mocking doubts, one divine forever — the
verb's whole career. And the verse measures itself against the
promise ONE CHAPTER OLD: 35:11's u-melakhim me-chalatzekha yetzeu
("kings shall go out from your loins") — the letter counts Edom's
head start against Israel's not-yet kings (yisrael tok10/587, the
nation named in a ledger-clause before it exists as one).

CROWN 2 — THE CHIEF-TITLE'S ONE STEP OUT (441): aluf ("chief") has
a 44-token Torah career and FORTY-THREE of them stand in this
chapter [VERIFIED: debut_map — toks 1-43 in-span, 36:15-43]; the
single remaining token is Exod 15:15: az nivhalu ALUFE EDOM —
"then the chiefs of Edom were terrified", first in the Song's
panic-list at the Sea. The title is minted across one genealogy
and spent on one terror.

CROWN 3 — THE SEPARATION FORMULA REPEATS (36:6-7 ↔ 13:6): Esau
departs "from before Jacob his brother" in the exact sentence-shape
of Abram and Lot's parting: 13:6 ve-lo NASA otam ha-aretz LA-SHEVET
YACHDAV ki haya REKHUSHAM RAV [VERIFIED: token scan] → 36:7 ki haya
REKHUSHAM RAV mi-SHEVET YACHDAV ve-lo yakhla eretz megurehem LA-SET
otam — property-too-great, dwell-together, the land cannot
carry-them: the Torah separates its two brother-pairs with one
reusable sentence. And the FACE-PREPOSITION'S REVERSAL: mi-pene
(6440) walks toks 97-98 = 35:1,7 (Jacob FLED from-before Esau,
God's and the narrator's words) → tok99 = 36:6 (Esau now departs
from-before JACOB) [VERIFIED: consecutive ordinals]: the
from-before-the-face formula passes between the brothers — flight
answered by withdrawal. And the sojourn-noun seals it: eretz
MEGUREHEM (4033 tok3/7) — the land "of their sojournings" cannot
hold both; tok4 is 37:1, the span's very next verse: va-yeshev
yaaqov be-eretz MEGURE aviv — Esau leaves the sojourn-land, Jacob
settles it, consecutive career tokens across the chapter break
(the covenant word: 17:8 eretz megurekha to Abraham, 28:4 Isaac's
blessing, then Exod 6:4's covenant recall).

CROWN 4 — AMALEK IS BORN OF TIMNA (36:12): ve-TIMNA hayta filegesh
le-elifaz... va-teled le-elifaz et AMALEQ — Amalek (6002 tok1/14
DEBUT) enters the Torah as a concubine's son in Esau's list; the
career: Exod 17:8-16 (the war, ×7 — milchama la-YHWH ba-amaleq
mi-dor dor), Num 13:29, Num 24:20 ×2 (Balaam: "first of nations,
and his end — destruction"), Deut 25:17,19 (REMEMBER / BLOT OUT).
And timna (8555) has a THREE-token Torah career, ALL in this
chapter [VERIFIED: 3/3 in-span]: concubine (36:12), Lotan's sister
(36:22), and chief (36:40, aluf timna) — one name, three roles,
one chapter; the pilegesh-noun itself closes its 4-token career
here (6370 tok4/4 — Reuma, Keturah's line, Bilhah, Timna: every
Torah concubine-token is a genealogy's hinge).

CROWN 5 — THE DOUBLE TOLEDOT (36:1 + 36:9): ve-ele TOLDOT esav ×2
— Esau is the ONLY toledot-subject in the Torah whose header
appears TWICE [VERIFIED: full 8435 census — every other
generations-header (heavens 2:4, Adam 5:1, Noah 6:9, Noah's sons
10:1, Shem 11:10, Terach 11:27, Ishmael 25:12, Isaac 25:19, Jacob
37:2, Aaron-Moses Num 3:1) occurs once per subject; the suffixed
le-toldotam tokens are list-datives, not headers]: once as Canaan's
Esau (36:1-8, wives and departure) and once as Seir's (36:9-43,
chiefs and kings) — the letter itself splits him into
before-the-mountain and after. The identity-equation brackets the
chapter: hu edom (36:1) · esav hu edom (36:8) · hu edom (36:19) ·
hu esav avi edom (36:43, the chapter's last clause).

CARE-POINTS (ordinals from debut_map via prestage unless tagged):
(1) 36:2-3 THE WIFE-LIST TENSION [OPEN OBSERVATIONS (a)]: ada bat
elon ha-chiti · aholivama bat ana · basmat bat yishmael achot
nevayot — against 26:34's yehudit bat beeri + BASMAT BAT ELON and
28:9's MACHALAT bat yishmael achot nevayot: the three wife-lists
share fathers and vary names (Elon's daughter: Basmat there, Ada
here; Ishmael's daughter: Machalat there, Basmat here) — the
letter-tension is filed with both token-sets standing, adjudicated
by no one (35:26's Paddan-aram class, now three lists wide).
(2) 36:4-5 THE CANAAN-BORN: elifaz (tok1/11), reuel, yeush (KETIV
yysh — the span's ketiv pair opens), yalam, qorach — and QORACH
(7141 tok1/21): the name's first four Torah tokens are EDOMITE
(36:5,14,16,18); tokens 5+ are the Levite rebel's (Exod 6:21,24;
Num 16-17, 26-27) — one name, two houses, filed as
homograph-name note [OPEN OBSERVATIONS (b)].
(3) 36:6-7 THE WITHDRAWAL [CROWN 3]: the six-fold ve-et
possession-list (wives, sons, daughters, souls, livestock,
beasts, property) echoes 12:5's departure-list; rakhash (7408
tok4/5 — the acquire-verb's five tokens are all family
relocations); va-yelekh el-ERETZ ("to a land" — unnamed
in the verse; the narrator names Seir only at 36:8) — the
departure to an anonymous land, mi-pene yaaqov achiv.
(4) 36:8 SEIR SETTLED: va-yeshev esav be-har seir — the
dwell-verb (3427 tok52/199) Esau performs in one clause is the
verb gen_58's card still holds open for Jacob (the
brothers' inverse compliance — letter-note only).
(5) 36:11-14 THE GRANDSONS: teman (8487 tok1/3 — the name's
whole Torah career is this chapter's: 36:11, 36:15, 36:42; the
gentilic temani, 8489 1/1, supplies king Chusham at 36:34);
qenaz (7073 tok1/3 — likewise all in-span: 36:11, 36:15, 36:42;
15:19's Kenizzite is the separate gentilic lemma);
AMALEQ [CROWN 4]; the ketiv pair closes (36:14 yysh/yeush).
(6) 36:15-19 THE FIRST CHIEF-LIST [CROWN 2]: alufe vene esav —
eleven chiefs by Elifaz and Reuel and Aholivamah; ele vene esav
ve-ele alufehem HU EDOM (36:19) — equation #3.
(7) 36:20-30 THE HORITE LEDGER: bene SEIR ha-chori YOSHVE
HA-ARETZ ("the dwellers of the land" — the list absorbs the
natives into Esau's ledger: the only toledot-chapter that lists
the displaced people alongside the displacer); timna the sister
(36:22 [CROWN 4]); 36:24 THE YEMIM-FINDER: hu ana asher matza et
HA-YEMIM ba-midbar (3222 tok1/1 HAPAX — a word that occurs once
in the Torah and nowhere names its referent; left untranslated
on the letter) bi-reoto et HA-CHAMORIM le-tzivon aviv — found
while pasturing THE DONKEYS (2543 tok8/41 — the noun that
shadowed chamor-the-man in gen_57 returns in Edom's list); the
ledger's only narrative aside besides the king's war [care 9].
(8) 36:31 THE KINGS BEFORE THE KINGS [CROWN 1].
(9) 36:32-39 THE EIGHT: va-yamat X va-yimlokh tachtav Y — the
die-and-reign chain ×7 (muth toks 45-51/303 — seven king-deaths
in eight verses; no Edomite king succeeds his father: eight
kings, eight houses, seven place-notices — Baal-chanan alone
carries none — the letter's own contrast with the dynastic
promise of 35:11); HADAD BEN BEDAD ha-make et
MIDYAN bi-sede MOAV (36:35) — the king-list's only deed: Edom
strikes Midian in Moab's field — the three nations of the
Balaam cycle (Num 22-25, 31) pre-assembled in one clause
[watch]; shaul me-RECHOVOT ha-nahar (7344 tok3/3 — the
Rechovot-name's third and last token: Assyria's city 10:11,
Isaac's roomy well 26:22, an Edomite king's river-town);
MEHETAVEL bat matred bat ME ZAHAV (36:39) — the list's only
queen-line, ending in "waters of gold" — the king-list closes
on a woman's three-generation pedigree, as the chief-list
closed on Timna's three roles.
(10) 36:40-43 THE CLOSING LIST: alufe esav le-mishpechotam
li-meqomotam bi-shemotam — by families, places, names; ALUF
TIMNA (the name's third role [CROWN 4]); ALUF MAGDIEL ALUF IRAM
— and the ledger signs itself: ele alufe EDOM le-moshvotam
be-eretz ACHUZATAM (272 achuza tok5/39 — the HOLDING-noun: toks
1-4 are Abraham's — 17:8 achuzat olam, 23:4,9,20 the
grave-holding; tok5 is EDOM'S holding — Esau's line reaches the
covenant's land-word first; toks 6+ = 47:11 Goshen, 48:4, then
the Leviticus holding-law cluster) — HU ESAV AVI EDOM: the
chapter's last clause re-states its first (equation #4, the
bracket closed).

WATCHLIST ARMS (prospective, filed): 37:1 (megurim tok4 — Jacob
settles the sojourn-land Esau left: the consecutive-token landing);
37:2 (toledot tok13 — ele toldot YAAQOV: the next header, against
Esau's double); 37:8 (malakh toks 11-12 — the brothers' reign-mock,
the verb's first Israelite tokens); Exod 15:15 (aluf tok44 — the
chiefs' terror) + Exod 15:18 (malakh tok13 — the forever-reign);
Exod 17:8-16 (Amalek's war; zakhor Deut 25:17,19); Num 20:14-21
(Edom refuses Israel passage — the brother-nation meets the
brother-nation); Num 22-25 + 31 (Midian and Moab — Hadad's two
names pre-joined at 36:35); Num 24:18 (Balaam: "Edom shall be a
possession"); Num 24:20 (Amalek first-and-last); Deut 2:4-8 (the
bene esav of Seir — Israel commanded NOT to provoke them; achuza
and yerusha vocabulary); Deut 23:8 ("do not abhor an Edomite, for
he is your BROTHER" — the achikha of 36:6 legislated); Exod 6:21+
/ Num 16 (the Levite Korach — the name's second house).

OPEN OBSERVATIONS (filed, never push for rulings): (a) the
three-list wife-names tension (26:34 / 28:9 / 36:2-3) — shared
fathers, varying names; all token-sets stand; no adjudication
[care 1]. (b) qorach one-name-two-houses (Edom's chief toks 1-4;
Levi's rebel toks 5-21) [care 2]. (c) ha-yemim (36:24) — 1/1 hapax
with unglossed referent; left on the letter. (d) the aluf-count
symmetry: 43 in-span tokens across 43 verses — arithmetic note
only. (e) 36:31's melakh-melekh infinitive-plus-noun ("before the
REIGNING of a KING") — the verse holds the verb's infinitive and
the noun side by side; morph note. (f) esav hu edom equations ×4
(36:1,8,19,43) — the bracket-structure note.
"""

# ---------------------------------------------------------------------------

def _V(ref, op, en, tl, tr, expr, frag, prose, comment):
    return dict(ref=ref, op=op, en=en, tl_en=tl, tr_en=tr,
                ops=[dict(op="PRECONDITION_STATE", expr=expr, frag=frag, prose=prose)],
                comment=comment)

STEPS = [
 _V((36,1), "THE_FIRST_HEADER",
  "And these are the generations of Esau — he is Edom.",
  "and these are the generations of Esau",
  "he is Edom",
  "HOLDS(toldot_esav_hu_edom(kotev_rishon), t0)",
  ("ve-ele",3), """
THE DOUBLE HEADER OPENS [CROWN 5]. ve-ele TOLDOT esav (8435
tok11/29) [VERIFIED: SNAPSHOT Gen.36.1] — the generations-formula
takes Esau — and will take him AGAIN at 36:9: the only
toledot-subject in the Torah with two headers [VERIFIED: full 8435
census — every other header occurs once per subject]. hu EDOM —
equation #1 of four (36:1,8,19,43): the chapter opens and closes
identifying the man with the nation. No etnachta (tifcha split,
fallback #1 of seven). SPECS empty. REGISTRY 0. TESTS 0. Onkelos
BUFFER PENDING.""",
  "The first of two headers; the man equals the nation, said four times."),

 _V((36,2), "THE_WIVES_OF_CANAAN",
  "Esau took his wives from the daughters of Canaan: Ada, daughter of Elon the Hittite; and Aholivamah, daughter of Ana, daughter of Tzivon the Hivite;",
  "Esau took his wives from the daughters of Canaan",
  "Ada daughter of Elon; Aholivamah daughter of Ana daughter of Tzivon",
  "HOLDS(laqach_nashav_mi_benot_kenaan(esav, ada_ve_aholivama), t0)",
  ("esav",4), """
THE THIRD WIFE-LIST [OPEN OBSERVATIONS (a); care 1]. esav laqach
et nashav mi-benot kenaan (3947 tok113/393) [VERIFIED: SNAPSHOT
Gen.36.2] — ada bat ELON ha-chiti: at 26:34 Elon's daughter was
named BASMAT; here she is ADA — the wife-lists share fathers and
vary names (three lists: 26:34, 28:9, 36:2-3); the letter-tension
is filed with every token standing, adjudicated by no one
(35:26's class, now three lists wide). aholivama bat ana (173
tok1/7 DEBUT; 6034 tok1/9) — the third wife, absent from the
earlier lists altogether.""",
  "The wife-names shift between lists; filed, not judged."),

 _V((36,3), "THE_ISHMAEL_WIFE",
  "and Basmat, daughter of Ishmael, sister of Nevayot.",
  "and Basmat, daughter of Ishmael",
  "sister of Nevayot",
  "HOLDS(basmat_bat_yishmael(achot_nevayot), t0)",
  ("ve-et",3), """
THE RENAMED COUSIN [care 1]. ve-et basmat bat yishmael achot
nevayot (1315 tok2/6; 3458 tok17/17 CLOSES) [VERIFIED: SNAPSHOT
Gen.36.3] — ISHMAEL'S LAST TORAH TOKEN: the elder half-uncle's
name leaves the corpus inside Esau's wife-list — the two passed-
over elder lines join and exit together. At 28:9 Ishmael's
daughter, Nevayot's sister, was MACHALAT;
here she is BASMAT (the name 26:34 gave to Elon's daughter): the
second axis of the wife-list tension [OPEN OBSERVATIONS (a)]. No
etnachta (tifcha split, fallback #2).""",
  "Ishmael's daughter under her other name; the tension's second axis."),

 _V((36,4), "THE_FIRSTBORN_SONS",
  "And Ada bore to Esau Elifaz; and Basmat bore Reuel;",
  "Ada bore to Esau Elifaz",
  "and Basmat bore Reuel",
  "HOLDS(va_teled_ada_u_vasmat(elifaz_u_reuel), t0)",
  ("va-teled",4), """
THE LINE OPENS. va-teled ada le-esav et ELIFAZ (3205 tok144/205;
464 tok1/7 DEBUT) u-vasmat yalda et REUEL (7467 tok1/8 DEBUT)
[VERIFIED: SNAPSHOT Gen.36.4] — the bear-verb that filled
gen_51's twelve now counts Esau's five; Elifaz and Reuel head
the chief-lists to come (36:15-17) — and reuel's later tokens
leave Edom for MIDIAN: Exod 2:18's Reuel is Moses'
father-in-law, Num 2:14/10:29 his line — another name shared
across the Edom-Midian braid [care 9].""",
  "Two mothers, two heads of chief-lines."),

 _V((36,5), "THE_CANAAN_BORN_CLOSE",
  "and Aholivamah bore Yeush and Yalam and Korach. These are the sons of Esau who were born to him in the land of Canaan.",
  "Aholivamah bore Yeush, Yalam, and Korach",
  "these are Esau's sons, born to him in the land of Canaan",
  "HOLDS(ele_bene_esav(yuldu_lo_be_eretz_kenaan), t0)",
  ("ve-aholivama",2), """
THE KETIV PAIR OPENS; KORACH'S FIRST HOUSE [care 2]. ve-aholivama
yalda et yeush (KETIV yysh / qere yeush — the span's ketiv pair,
36:5 and 36:14, rendered per snapshot) ve-et yalam ve-et QORACH
(7141 tok1/21 DEBUT) [VERIFIED: SNAPSHOT Gen.36.5] — the name
Korach enters the Torah EDOMITE: its first four tokens are this
chapter's (36:5,14,16,18); tokens 5-21 belong to Levi's rebel
(Exod 6:21,24; Num 16-17, 26-27) — one name, two houses [OPEN
OBSERVATIONS (b)]. ele bene esav asher yuldu lo BE-ERETZ KENAAN —
the Canaan-frame that 36:6 will break.""",
  "Korach debuts in Edom; the ketiv pair opens."),

 _V((36,6), "THE_WITHDRAWAL",
  "And Esau took his wives and his sons and his daughters and all the souls of his house, and his livestock and all his beasts and all his property that he had acquired in the land of Canaan; and he went to a land, away from before Jacob his brother.",
  "Esau took wives, sons, daughters, all the souls of his house, livestock, beasts, and all he had acquired in Canaan",
  "and went to a land, away from before Jacob his brother",
  "HOLDS(va_yelekh_el_eretz(esav, mi_pene_yaaqov_achiv), t0)",
  ("va-yelekh",5), """
FROM BEFORE THE FACE, REVERSED [CROWN 3]. va-yiqach esav... ve-et
kal qinyano asher RAKHASH (7408 tok4/5 — the acquire-verb's
five tokens are all family relocations: Abram out of Haran
12:5, Jacob out of Paddan 31:18 ×2, Esau out of Canaan here,
Israel into Egypt 46:6) va-yelekh el-ERETZ — to a land the verse leaves
unnamed — MI-PENE YAAQOV ACHIV (6440 tok99/627) [VERIFIED:
SNAPSHOT Gen.36.6 idx24-29; ordinal census] — and the
face-preposition's walk tells the reversal: toks 97-98 = 35:1,7
(Jacob FLED from-before Esau — God's word and the narrator's);
tok99 = Esau departing from-before JACOB: flight answered by
withdrawal on consecutive career tokens. The six-fold ve-et
possession-list echoes 12:5's departure inventory — the
uncle-nephew parting re-run as the brothers'.""",
  "Esau withdraws from the face Jacob fled; the preposition keeps the score."),

 _V((36,7), "THE_LAND_THAT_COULD_NOT_BEAR",
  "For their property was too great for dwelling together; and the land of their sojournings could not bear them, because of their livestock.",
  "their property was too great for dwelling together",
  "the land of their sojournings could not bear them",
  "HOLDS(lo_yakhla_eretz_megurehem_la_set_otam(rekhusham_rav), t0)",
  ("ki",4), """
ONE SENTENCE, TWO PARTINGS [CROWN 3]. ki haya REKHUSHAM RAV
mi-SHEVET YACHDAV ve-lo yakhla eretz MEGUREHEM LA-SET otam
[VERIFIED: SNAPSHOT Gen.36.7 against 13:6's ve-lo NASA otam
ha-aretz LA-SHEVET YACHDAV ki haya REKHUSHAM RAV] — the
Abram-and-Lot separation sentence re-used for Esau and Jacob:
property-too-great, dwell-together, the-land-cannot-carry — the
Torah parts its brother-pairs with one reusable formula. eretz
MEGUREHEM (4033 tok3/7) — the sojourn-noun of the covenant (17:8
eretz megurekha; 28:4 Isaac's blessing): tok4 is 37:1, the very
next verse after this span — va-yeshev yaaqov be-eretz MEGURE
aviv: Esau leaves the sojourn-land, Jacob settles it,
consecutive career tokens across the chapter break [watch].""",
  "The separation formula returns; the sojourn-land changes hands next verse."),

 _V((36,8), "SEIR_SETTLED",
  "And Esau dwelt in the hill-country of Seir — Esau, he is Edom.",
  "Esau dwelt in the hill-country of Seir",
  "Esau — he is Edom",
  "HOLDS(va_yeshev_esav_be_har_seir(hu_edom), t0)",
  ("va-yeshev",4), """
THE OTHER BROTHER'S DWELL [care 4]. va-YESHEV esav be-har seir
(3427 tok52/199; 8165 tok5/20) [VERIFIED: SNAPSHOT Gen.36.8] —
Esau performs in one clause the dwell-verb that gen_58's
shev-card still holds open for Jacob (whose narrator got shakhan
instead): the brothers' inverse compliance, letter-note only.
esav HU EDOM — equation #2. No etnachta (the span's one
zaqef-qatan fallback).""",
  "Esau dwells where Jacob's dwell-card stays open; equation two."),

 _V((36,9), "THE_SECOND_HEADER",
  "And these are the generations of Esau, father of Edom, in the hill-country of Seir.",
  "and these are the generations of Esau, father of Edom",
  "in the hill-country of Seir",
  "HOLDS(toldot_esav_avi_edom(kotev_sheni, be_har_seir), t0)",
  ("ve-ele",4), """
THE ONLY DOUBLED TOLEDOT [CROWN 5]. ve-ele TOLDOT esav AVI edom
be-har seir (8435 tok12/29) [VERIFIED: SNAPSHOT Gen.36.9; full
census] — the generations-formula repeats for the same man: no
other subject in the Torah carries two headers — Canaan's Esau
(36:1-8) and Seir's (36:9-43), the letter splitting the life at
the mountain; and the epithet shifts with it: hu edom ("he IS
Edom") becomes avi edom ("FATHER of Edom") — man to nation
between the two headers.""",
  "The second header; is-Edom becomes father-of-Edom."),

 _V((36,10), "THE_SONS_NAMED",
  "These are the names of the sons of Esau: Elifaz son of Ada, Esau's wife; Reuel son of Basmat, Esau's wife.",
  "these are the names of Esau's sons",
  "Elifaz son of Ada; Reuel son of Basmat",
  "HOLDS(ele_shemot_bene_esav(elifaz_u_reuel), t0)",
  ("ele",4), """
THE NAME-LIST OPENS. ele SHEMOT bene esav (8034 tok91/252)
[VERIFIED: SNAPSHOT Gen.36.10] — the shem-noun heads a list that
WRITES nothing: dozens of names mentioned, no va-yiqra act
anywhere in the chapter — the registry sleeps through the
Torah's densest name-field [UNIT SHAPE]. Each son tagged by
mother: ben ada eshet esav, ben basmat eshet esav.""",
  "Names listed, none written; the registry sleeps."),

 _V((36,11), "ELIFAZ_S_FIVE",
  "And the sons of Elifaz were: Teman, Omar, Tzefo, and Gatam, and Kenaz.",
  "and the sons of Elifaz were",
  "Teman, Omar, Tzefo, Gatam, Kenaz",
  "HOLDS(bene_elifaz(teman_ad_qenaz), t0)",
  ("va-yihyu",3), """
THE SOUTH IS BORN [care 5]. va-yihyu bene elifaz TEMAN (8487
tok1/3 DEBUT) omar tzefo ve-gatam u-QENAZ (7073 tok1/3 DEBUT)
[VERIFIED: SNAPSHOT Gen.36.11] — Teman and Qenaz both open
whole-Torah careers that never leave this chapter (each 3/3:
born 36:11, titled 36:15, districted 36:42); Teman's gentilic
supplies king Chusham (36:34, me-eretz ha-temani, 8489 1/1);
the Kenizzite nation of 15:19 rides a separate gentilic
lemma.""",
  "Teman and Kenaz debut in Elifaz's five."),

 _V((36,12), "AMALEK_BORN",
  "And Timna was concubine to Elifaz, son of Esau, and she bore to Elifaz Amalek. These are the sons of Ada, Esau's wife.",
  "Timna, concubine to Elifaz, bore to Elifaz Amalek",
  "these are the sons of Ada, Esau's wife",
  "HOLDS(va_teled_timna_le_elifaz(et_amaleq), t0)",
  ("ve-timna",4), """
THE BLOTTED NAME'S BIRTH [CROWN 4]. ve-TIMNA hayta FILEGESH
le-elifaz (8555 tok1/3; 6370 tok4/4 — the concubine-noun CLOSES
its Torah career here: Reuma 22:24, Keturah's line 25:6, Bilhah
35:22, Timna — every token a genealogy's hinge) va-teled
le-elifaz et AMALEQ (6002 tok1/14 DEBUT) [VERIFIED: SNAPSHOT
Gen.36.12; ordinals] — Amalek enters the Torah as a concubine's
son in Esau's ledger; the career: Exod 17:8-16 (the war ×7 and
the oath — "war for YHWH against Amalek from generation to
generation"), Num 13:29, Num 24:20 ×2 (Balaam: "first of
nations, and his end — destruction"), Deut 25:17,19 (REMEMBER /
BLOT OUT): born in a list, sentenced in the law. And timna's
own three tokens all live in this chapter — concubine, sister
(36:22), chief (36:40) [CROWN 4].""",
  "Amalek born of Timna; the concubine-noun closes its four-hinge career."),

 _V((36,13), "REUEL_S_FOUR",
  "And these are the sons of Reuel: Nachat and Zerach, Shama and Miza. These were the sons of Basmat, Esau's wife.",
  "the sons of Reuel: Nachat, Zerach, Shama, Miza",
  "these were the sons of Basmat, Esau's wife",
  "HOLDS(bene_reuel(nachat_ad_miza), t0)",
  ("ve-ele",3), """
THE SECOND FOUR. ve-ele bene reuel nachat va-zerach shama u-miza
[VERIFIED: SNAPSHOT Gen.36.13] — Reuel's four seed the second
chief-list (36:17); zerach (2226 tok1/7) returns as king
Yovav's father (tok3, 36:33) — and then crosses houses: tok4
is 38:30, TAMAR'S Zerach of the scarlet thread, two chapters
on; tok5 = 46:12 (Judah's list), tok6 = Num 26:13 — SIMEON'S
Zerach clan, a third house — tok7 = Num 26:20 (Judah's
clan).""",
  "Reuel's four; a king's father among them."),

 _V((36,14), "AHOLIVAMAH_S_THREE",
  "And these were the sons of Aholivamah, daughter of Ana, daughter of Tzivon, Esau's wife: she bore to Esau Yeush and Yalam and Korach.",
  "the sons of Aholivamah daughter of Ana, Esau's wife",
  "she bore to Esau Yeush, Yalam, and Korach",
  "HOLDS(bene_aholivama(yeush_yalam_qorach), t0)",
  ("ve-ele",4), """
THE KETIV PAIR CLOSES [care 2]. va-teled le-esav et yeush (KETIV
yysh ×2 — 36:5 and here, the span's pair) ve-et yalam ve-et
qorach (7141 tok2/21) [VERIFIED: SNAPSHOT Gen.36.14] — the
third wife's three, repeated from 36:5 with the mother's full
pedigree; the qere-ketiv convention rendered per snapshot.""",
  "The third wife's sons again; the ketiv pair closes."),

 _V((36,15), "THE_CHIEF_TITLE_MINTED",
  "These are the chiefs of the sons of Esau. The sons of Elifaz, Esau's firstborn: chief Teman, chief Omar, chief Tzefo, chief Kenaz,",
  "these are the chiefs of Esau's sons",
  "of Elifaz the firstborn: chief Teman, chief Omar, chief Tzefo, chief Kenaz",
  "HOLDS(ele_alufe_vene_esav(alufe_elifaz), t0)",
  ("ele",3), """
ALUF ENTERS THE TORAH [CROWN 2]. ele ALUFE vene esav (441
tok1/44 DEBUT) [VERIFIED: SNAPSHOT Gen.36.15 idx1 ordinal=1/44]
— the chief-title is minted here and spent here: FORTY-THREE of
its forty-four Torah tokens stand in this chapter; the one
remaining token is Exod 15:15 — az nivhalu ALUFE EDOM, "then
the chiefs of Edom were TERRIFIED", first in the Song's
panic-list at the Sea [watch]. bekhor esav (1060 tok7/69) —
Esau keeps his firstborn-title in his own ledger as Reuben
kept his (35:23).""",
  "The chief-title minted; its one step out of this chapter is the Sea's panic."),

 _V((36,16), "ELIFAZ_S_CHIEFS_CLOSE",
  "chief Korach, chief Gatam, chief Amalek. These are the chiefs of Elifaz in the land of Edom; these are the sons of Ada.",
  "chief Korach, chief Gatam, chief Amalek",
  "the chiefs of Elifaz in Edom; the sons of Ada",
  "HOLDS(alufe_elifaz_be_eretz_edom(bene_ada), t0)",
  ("aluf",3), """
AMALEK WITH A TITLE [CROWN 4]. aluf qorach aluf gatam aluf
AMALEQ (6002 tok2/14) [VERIFIED: SNAPSHOT Gen.36.16] — Amalek's
second and last Genesis token wears the chief-title; his next
appearance is the war at Refidim (Exod 17:8). ele alufe elifaz
be-eretz edom.""",
  "Amalek titled chief; next stop Refidim."),

 _V((36,17), "REUEL_S_CHIEFS",
  "And these are the sons of Reuel, Esau's son: chief Nachat, chief Zerach, chief Shama, chief Miza. These are the chiefs of Reuel in the land of Edom; these are the sons of Basmat, Esau's wife.",
  "the sons of Reuel: chief Nachat, chief Zerach, chief Shama, chief Miza",
  "the chiefs of Reuel in Edom; the sons of Basmat, Esau's wife",
  "HOLDS(alufe_reuel_be_eretz_edom(bene_vasmat), t0)",
  ("ve-ele",6), """
THE SECOND FOUR TITLED. aluf nachat aluf zerach aluf shama aluf
miza — Reuel's four each take the title (441 toks 10-13/44)
[VERIFIED: SNAPSHOT Gen.36.17]; the mother-tag closes the list
as it closed 36:13.""",
  "Reuel's four titled; the mother-tags keep the ledger's order."),

 _V((36,18), "AHOLIVAMAH_S_CHIEFS",
  "And these are the sons of Aholivamah, Esau's wife: chief Yeush, chief Yalam, chief Korach. These are the chiefs of Aholivamah, daughter of Ana, Esau's wife.",
  "the sons of Aholivamah: chief Yeush, chief Yalam, chief Korach",
  "the chiefs of Aholivamah daughter of Ana, Esau's wife",
  "HOLDS(alufe_aholivama(yeush_yalam_qorach), t0)",
  ("ve-ele",5), """
KORACH TITLED [care 2]. aluf yeush aluf yalam aluf QORACH (7141
tok4/21) [VERIFIED: SNAPSHOT Gen.36.18] — the Edomite Korach's
last token wears the chief-title; the name's next bearer (tok5,
Exod 6:21) is born to Levi and dies in Num 16's earth.""",
  "The first Korach exits titled; the second waits in Levi."),

 _V((36,19), "THE_FIRST_LEDGER_SEALS",
  "These are the sons of Esau, and these their chiefs — he is Edom.",
  "these are Esau's sons and these their chiefs",
  "he is Edom",
  "HOLDS(ele_vene_esav_ve_alufehem(hu_edom), t0)",
  ("ele",2), """
EQUATION #3 [CROWN 5]. ele vene esav ve-ele ALUFEHEM hu EDOM
[VERIFIED: SNAPSHOT Gen.36.19] — the sons-and-chiefs ledger
seals with the identity-clause's third saying. No etnachta
(tifcha split, fallback #4).""",
  "The son-ledger seals on the equation."),

 _V((36,20), "THE_HORITES_ENTER",
  "These are the sons of Seir the Horite, the dwellers of the land: Lotan and Shoval and Tzivon and Ana,",
  "the sons of Seir the Horite, the dwellers of the land",
  "Lotan, Shoval, Tzivon, Ana",
  "HOLDS(bene_seir_ha_chori(yoshve_ha_aretz), t0)",
  ("ele",4), """
THE DISPLACED IN THE DISPLACER'S LEDGER [care 7]. ele vene SEIR
HA-CHORI yoshve ha-aretz (8165 tok7/20; 2752 tok2/6) [VERIFIED:
SNAPSHOT Gen.36.20] — the natives ("the dwellers of the land")
get their own generations inside Esau's chapter — the only
toledot-span that lists the displaced people alongside the
displacer (Deut 2:12,22 will narrate the displacement the
letter here only implies) [watch].""",
  "Seir's own line enters Esau's book."),

 _V((36,21), "THE_HORITE_SEVEN",
  "and Dishon and Etzer and Dishan. These are the chiefs of the Horites, the sons of Seir, in the land of Edom.",
  "and Dishon and Etzer and Dishan",
  "the Horite chiefs, sons of Seir, in the land of Edom",
  "HOLDS(alufe_ha_chori(bene_seir), t0)",
  ("ve-dishon",3), """
SEVEN NATIVE CHIEFS. ve-dishon ve-etzer ve-dishan — Seir's seven
sons (441 toks continue) [VERIFIED: SNAPSHOT Gen.36.21] — the
chief-title covers the natives too: Edom's ledger grants the
Horites the same rank-word it grants Esau's line.""",
  "The title crosses to the natives."),

 _V((36,22), "TIMNA_THE_SISTER",
  "And the sons of Lotan were Chori and Hemam; and Lotan's sister was Timna.",
  "the sons of Lotan were Chori and Hemam",
  "and Lotan's sister was Timna",
  "HOLDS(va_achot_lotan(timna), t0)",
  ("va-achot",3), """
THE NAME'S SECOND ROLE [CROWN 4]. va-achot lotan TIMNA (8555
tok2/3; 269 tok23/47) [VERIFIED: SNAPSHOT Gen.36.22] — the
sister-notice stitches the Horite list to 36:12's concubine:
Amalek's mother stands in the native line — the ledger's two
halves joined by one woman's name (role three, chief, waits at
36:40).""",
  "Timna again — the seam between the two ledgers."),

 _V((36,23), "SHOVAL_S_FIVE",
  "And these are the sons of Shoval: Alvan and Manachat and Eval, Shefo and Onam.",
  "the sons of Shoval: Alvan, Manachat, Eval",
  "Shefo and Onam",
  "HOLDS(bene_shoval(alvan_ad_onam), t0)",
  ("ve-ele",3), """
THE LIST RUNS. ve-ele bene shoval [VERIFIED: SNAPSHOT Gen.36.23]
— five Horite grandsons; the ledger's rhythm holds.""",
  "Five more entries."),

 _V((36,24), "THE_YEMIM_FINDER",
  "And these are the sons of Tzivon: Aya and Ana — he is the Ana who found the yemim in the wilderness, while pasturing the donkeys for Tzivon his father.",
  "the sons of Tzivon: Aya and Ana",
  "the Ana who found the yemim in the wilderness, pasturing his father's donkeys",
  "HOLDS(hu_ana_asher_matza_et_ha_yemim(ba_midbar), t0)",
  ("hu",4), """
THE UNGLOSSED FIND [OPEN OBSERVATIONS (c); care 7]. hu ana asher
MATZA et HA-YEMIM ba-midbar (3222 tok1/1 HAPAX; 4672 tok36/122;
4057 tok6/105) [VERIFIED: SNAPSHOT Gen.36.24 idx10 ordinal=1/1]
— the ledger's one aside: a word the Torah says once and never
glosses (left on the letter, untranslated); found bi-reoto et
HA-CHAMORIM (2543 tok8/41) — while pasturing THE DONKEYS: the
noun that shadowed chamor-the-man through gen_57 grazes on in
Edom's list, le-tzivon aviv.""",
  "A hapax found in the wilderness; the donkeys again."),

 _V((36,25), "ANA_S_TWO",
  "And these are the sons of Ana: Dishon; and Aholivamah, daughter of Ana.",
  "the sons of Ana: Dishon",
  "and Aholivamah, daughter of Ana",
  "HOLDS(bene_ana(dishon_ve_aholivama), t0)",
  ("ve-ele",3), """
THE WIFE'S PEDIGREE CONFIRMED. ve-ele vene ana dishon
ve-AHOLIVAMA bat ana (173 tok6/7) [VERIFIED: SNAPSHOT Gen.36.25]
— Esau's third wife stands in the Horite line: the marriage
crossed into the native list, as Timna's concubinage crossed
out of it — the two ledgers trade one woman each.""",
  "The wife from the native line; the ledgers trade women."),

 _V((36,26), "DISHAN_S_FOUR",
  "And these are the sons of Dishan: Chemdan and Eshban and Yitran and Cheran.",
  "and these are the sons of Dishan",
  "Chemdan, Eshban, Yitran, Cheran",
  "HOLDS(bene_dishan_rishon(chemdan_ad_kheran), t0)",
  ("ve-ele",3), """
THE LIST RUNS ON. ve-ele bene dishan [VERIFIED: SNAPSHOT
Gen.36.26] — four entries; the rhythm holds.""",
  "Four more entries."),

 _V((36,27), "ETZER_S_THREE",
  "These are the sons of Etzer: Bilhan and Zaavan and Akan.",
  "these are the sons of Etzer",
  "Bilhan, Zaavan, Akan",
  "HOLDS(bene_etzer(bilhan_zaavan_aqan), t0)",
  ("ele",3), """
THE SEVENTH HOUSE NEARS. ele bene etzer [VERIFIED: SNAPSHOT
Gen.36.27] — three entries; one Horite house remains.""",
  "Three entries; one house left."),

 _V((36,28), "DISHAN_S_TWO",
  "These are the sons of Dishan: Utz and Aran.",
  "these are the sons of Dishan",
  "Utz and Aran",
  "HOLDS(bene_dishan(utz_va_aran), t0)",
  ("ele",3), """
UTZ CLOSES. ele vene dishan UTZ va-aran (5780 tok3/3 CLOSES)
[VERIFIED: SNAPSHOT Gen.36.28] — the name's three Torah tokens
sit in three houses: Aram's son (10:23, Shem's line), Nachor's
firstborn (22:21, Abraham's kin), and the Horite here — one
name across three nations (the Korach pattern widened). No etnachta (tifcha split, fallback #5).""",
  "The last Horite house; a Shemite name inside it."),

 _V((36,29), "THE_HORITE_CHIEFS",
  "These are the chiefs of the Horites: chief Lotan, chief Shoval, chief Tzivon, chief Ana,",
  "these are the chiefs of the Horites",
  "chief Lotan, chief Shoval, chief Tzivon, chief Ana",
  "HOLDS(alufe_ha_chori_rishon(lotan_ad_ana), t0)",
  ("ele",3), """
THE NATIVE TITLES. ele alufe ha-chori [VERIFIED: SNAPSHOT
Gen.36.29] — the seven Horite heads take the aluf-title in
their own right (441 toks 21-25 in this verse; the seven
head-titles run toks 22-28 across 36:29-30).""",
  "The native chiefs listed."),

 _V((36,30), "THE_HORITE_LEDGER_SEALS",
  "chief Dishon, chief Etzer, chief Dishan. These are the chiefs of the Horites, by their chiefdoms, in the land of Seir.",
  "chief Dishon, chief Etzer, chief Dishan",
  "the Horite chiefs by their chiefdoms in the land of Seir",
  "HOLDS(alufe_ha_chori_le_alufehem(be_eretz_seir), t0)",
  ("aluf",2), """
BY THEIR CHIEFDOMS. ele alufe ha-chori LE-ALUFEHEM be-eretz
seir [VERIFIED: SNAPSHOT Gen.36.30] — the title doubled into a
collective ("by their chiefdoms") — the Horite ledger seals in
Seir's name as Esau's sealed in Edom's (36:19).""",
  "The native ledger seals in Seir's own name."),

 _V((36,31), "THE_KINGS_BEFORE_THE_KINGS",
  "And these are the kings who reigned in the land of Edom, before a king reigned for the sons of Israel.",
  "these are the kings who reigned in the land of Edom",
  "before a king reigned for the sons of Israel",
  "HOLDS(ha_melakhim_asher_malkhu_be_edom(li_fene_melakh_melekh_li_vene_yisrael), t0)",
  ("ve-ele",6), """
THE REIGN-VERB IS BORN COUNTING [CROWN 1]. ve-ele ha-melakhim
asher MALKHU be-eretz edom (4427 tok1/13 DEBUT; 4428 tok34/101)
li-fene MELAKH-MELEKH li-vene YISRAEL (4427 tok2/13, infinitive;
3478 tok10/587) [VERIFIED: SNAPSHOT Gen.36.31; full 4427
census] — the verb malakh enters the Torah here and has
thirteen tokens ever: toks 1-10 are this span's (Edom's eight
kings reigning and dying); toks 11-12 are 37:8 — the brothers'
mock of Joseph, ha-MALOKH TIMLOKH alenu ("will you REIGN,
reign over us?"), the very next tokens after the span; tok13
is Exod 15:18 — YHWH YIMLOKH le-olam va-ed, the Song's
forever-reign: ten Edomite reigns, two mocking doubts, one
divine forever. And the clause measures itself against a
promise one chapter old — 35:11's "kings shall go out from
your loins": the letter counts Edom's head start against
Israel's not-yet kings, naming the nation (li-vene yisrael,
tok10) before it exists as one. The infinitive-noun pair
melakh-melekh — "before the REIGNING of a KING" — puts the
verb's infinitive beside its noun [OPEN OBSERVATIONS (e)].""",
  "The reign-verb debuts against the loins-promise; Edom counts first."),

 _V((36,32), "THE_FIRST_KING",
  "And Bela son of Beor reigned in Edom; and the name of his city was Dinhava.",
  "Bela son of Beor reigned in Edom",
  "and the name of his city was Dinhava",
  "HOLDS(va_yimlokh_bela_ben_beor(ir_dinhava), t0)",
  ("va-yimlokh",4), """
BELA SON OF BEOR [care 9]. va-yimlokh be-edom BELA ben BEOR
(4427 tok3/13) [VERIFIED: SNAPSHOT Gen.36.32] — the first king;
his patronym returns on another famous son: bilam ben BEOR (Num
22:5) — of beor's six Torah tokens (1160), one is this king's
father and five are Balaam's patronym (Num 22:5; 24:3,15; 31:8;
Deut 23:5) — one name, two famous sons; ve-shem
IRO dinhava — the city-formula that will mark three of the
eight (Dinhava, Avit, Pau): eight kings, no dynasty, each from
his own town.""",
  "The first king; Beor's other son waits in Numbers."),

 _V((36,33), "THE_CHAIN_BEGINS",
  "And Bela died; and Yovav son of Zerach, from Botzra, reigned in his place.",
  "and Bela died",
  "Yovav son of Zerach from Botzra reigned in his place",
  "HOLDS(va_yamat_bela_va_yimlokh(yovav_mi_batzra), t0)",
  ("va-yamat",2), """
DIE-AND-REIGN [care 9]. va-yamat bala va-yimlokh tachtav (4191
tok45/303; 4427 tok4/13) [VERIFIED: SNAPSHOT Gen.36.33] — the
chain-formula opens: seven king-deaths in seven verses, and NO
king succeeds his father — eight kings, eight houses: the letter's own anti-dynasty, standing against the
loins-promise it was just measured by [CROWN 1] (seven of the
eight carry a place-notice; Baal-chanan alone, 36:38, has
none). yovav ben
zerach mi-BATZRA (1224 tok1/1 — Botzra, once in the Torah;
the prophets' Edom-oracles will wear it out of corpus).""",
  "The chain opens: no son ever succeeds."),

 _V((36,34), "THE_THIRD_KING",
  "And Yovav died; and Chusham, from the land of the Temanite, reigned in his place.",
  "and Yovav died",
  "Chusham from the land of the Temanite reigned in his place",
  "HOLDS(va_yamat_yovav_va_yimlokh(chusham_ha_temani), t0)",
  ("va-yamat",2), """
TEMAN SUPPLIES A KING [care 5]. va-yamat yovav va-yimlokh
tachtav CHUSHAM me-eretz HA-TEMANI (8489 tok1/1 — the
gentilic's only Torah token) [VERIFIED: SNAPSHOT Gen.36.34] — the grandson-name of 36:11 already a
land with a gentilic: the list's internal time runs fast —
Teman is born at 36:11 and territorial by 36:34.""",
  "Teman already a land; the ledger's clock runs fast."),

 _V((36,35), "THE_KING_WHO_STRUCK_MIDIAN",
  "And Chusham died; and Hadad son of Bedad — who struck Midian in the field of Moab — reigned in his place; and the name of his city was Avit.",
  "and Chusham died",
  "Hadad son of Bedad, who struck Midian in the field of Moab, reigned; his city was Avit",
  "HOLDS(va_yimlokh_hadad(ha_make_et_midyan_bi_sede_moav), t0)",
  ("ha-make",4), """
THE LIST'S ONE DEED [care 9]. hadad ben bedad HA-MAKE et MIDYAN
bi-sede MOAV (5221 tok11/99; 4080 tok3/18 — Midian born of
Keturah 25:2,4, struck by Edom here, then Moses' refuge
(Exod 2-4, 18) and Balaam's partner (Num 22-25) to the war
(Num 31); 4124 tok3/47 — Moab born at 19:37, and its very
NEXT token is Exod 15:15: the Song's trembling Moab, in the
same verse as the terrified chiefs of Edom [CROWN 2])
[VERIFIED: SNAPSHOT Gen.36.35] — the king-list's only narrated
event: Edom strikes Midian in Moab's field — the three nations
of the Balaam cycle (Num 22-25, the hire; Num 31, the war)
pre-assembled in one clause, generations early [watch]; the
strike-verb nakah is the one gen_55's ve-hikahu feared and
Num 31's va-yaku will discharge.""",
  "The only deed in the ledger: Edom, Midian, and Moab in one clause."),

 _V((36,36), "THE_FIFTH_KING",
  "And Hadad died; and Samla, from Masreka, reigned in his place.",
  "and Hadad died",
  "Samla from Masreka reigned in his place",
  "HOLDS(va_yamat_hadad_va_yimlokh(samla_mi_masreqa), t0)",
  ("va-yamat",2), """
THE CHAIN RUNS. va-yamat hadad va-yimlokh tachtav samla
mi-masreqa (4957 tok1/1 — Masreka, once) [VERIFIED: SNAPSHOT
Gen.36.36] — the fifth king, the fourth origin-town.""",
  "Fifth king, fourth town."),

 _V((36,37), "THE_KING_FROM_THE_WIDE_PLACES",
  "And Samla died; and Shaul, from Rechovot-of-the-river, reigned in his place.",
  "and Samla died",
  "Shaul from Rechovot-of-the-river reigned in his place",
  "HOLDS(va_yimlokh_shaul(me_rechovot_ha_nahar), t0)",
  ("va-yimlokh",4), """
RECHOVOT'S LAST TOKEN [care 9]. shaul me-RECHOVOT ha-nahar (7344
tok3/3 CLOSES; 5104 tok9/18) [VERIFIED: SNAPSHOT Gen.36.37] —
the Rechovot-name's three Torah stations complete: Assyria's
city (10:11), Isaac's roomy well (26:22 — "now YHWH has made
ROOM for us"), and an Edomite king's river-town — the
wide-place name spent on three nations. And SHAUL — the
name's five Torah tokens: this king ×2 (36:37,38), then
Simeon's son Shaul ben ha-kenaanit (46:10 = Exod 6:15's
list-double) and his clan (Num 26:13) — the name reigns in
Edom before it settles in Simeon.""",
  "Rechovot closes on a king; the name Shaul reigns first in Edom."),

 _V((36,38), "THE_SEVENTH_KING",
  "And Shaul died; and Baal-Chanan son of Akhbor reigned in his place.",
  "and Shaul died",
  "Baal-Chanan son of Akhbor reigned in his place",
  "HOLDS(va_yamat_shaul_va_yimlokh(baal_chanan_ben_akhbor), t0)",
  ("va-yamat",2), """
THE GRACE-NAME UNDER BAAL [care 9]. baal chanan ben akhbor
(1177 tok1/2) [VERIFIED: SNAPSHOT Gen.36.38] — the only Torah
name compounding baal with CHANAN, the grace-verb of gen_56's
chanani (2603's nominal cousin) — a lord-of-grace reigning in
Edom; akhbor ("mouse") his father.""",
  "Baal-of-grace, seventh on the list."),

 _V((36,39), "THE_LAST_KING_AND_THE_QUEEN_LINE",
  "And Baal-Chanan son of Akhbor died; and Hadar reigned in his place; and the name of his city was Pau; and his wife's name was Mehetavel, daughter of Matred, daughter of Me-zahav.",
  "Baal-Chanan died; Hadar reigned; his city was Pau",
  "his wife was Mehetavel, daughter of Matred, daughter of Me-zahav",
  "HOLDS(va_yimlokh_hadar(ishto_mehetavel_bat_me_zahav), t0)",
  ("ve-shem",8,2), """
THE LEDGER ENDS ON A WOMAN'S PEDIGREE [care 9]. va-yimlokh
tachtav HADAR (4427 tok10/13 — the reign-verb's last Edomite
token)... ve-shem ISHTO mehetavel bat matred bat ME ZAHAV
(4105 tok1/1 — Me-zahav, "waters of gold", once in the Torah)
[VERIFIED: SNAPSHOT Gen.36.39] — the king-list's only wife.
The Torah's THREE bat-X-bat-Y chains all stand in this chapter
(36:2 and 36:14's aholivama bat ana bat tzivon; and this) —
and this one alone has no verse construing its middle name as
male (36:24-25 make Ana Tzivon's son; Matred has no such
verse): filed on the letter, not adjudicated. The eight kings
close not on a successor — Hadar alone gets no death-notice
and no heir — but on a golden-water genealogy, as the
chief-lists closed on Timna's three roles [CROWN 4].""",
  "No eighth death; the list ends on the golden-water queen-line."),

 _V((36,40), "THE_CLOSING_LIST_OPENS",
  "And these are the names of the chiefs of Esau, by their families, by their places, by their names: chief Timna, chief Alva, chief Yetet,",
  "the names of Esau's chiefs by families, places, and names",
  "chief Timna, chief Alva, chief Yetet",
  "HOLDS(alufe_esav_le_mishpechotam(li_meqomotam_bi_shemotam), t0)",
  ("ve-ele",6), """
THE NAME'S THIRD ROLE [CROWN 4]. ve-ele shemot alufe esav
le-mishpechotam li-meqomotam BI-SHEMOTAM (8034 tok96/252)...
aluf TIMNA (8555 tok3/3 CLOSES) [VERIFIED: SNAPSHOT Gen.36.40]
— the closing list is keyed BY NAMES, and its first entry is
TIMNA: concubine (36:12), sister (36:22), now chief — the
name's whole Torah career, three roles, one chapter; Amalek's
mother-name ends the book of Edom ranked.""",
  "The by-names list opens on Timna's third role."),

 _V((36,41), "THE_LIST_RUNS",
  "chief Aholivamah, chief Ela, chief Pinon,",
  "chief Aholivamah, chief Ela",
  "chief Pinon",
  "HOLDS(aluf_aholivama_ela_pinon(reshima), t0)",
  ("aluf",4), """
A WIFE-NAME AMONG THE CHIEFS. aluf AHOLIVAMA (173 tok7/7
CLOSES) aluf ela aluf pinon [VERIFIED: SNAPSHOT Gen.36.41] —
the third wife's name closes its career as a CHIEF-name in
the place-list (as timna's did at 36:40): the closing ledger
reuses the chapter's women's names for its districts. No
etnachta (tifcha split, fallback #6).""",
  "Aholivamah's name closes as a chiefdom."),

 _V((36,42), "THE_LIST_NEARS_ITS_END",
  "chief Kenaz, chief Teman, chief Mivtzar,",
  "chief Kenaz, chief Teman",
  "chief Mivtzar",
  "HOLDS(aluf_qenaz_teman_mivtzar(reshima), t0)",
  ("aluf",4), """
THE SOUTH AGAIN. aluf qenaz aluf TEMAN (8487 tok3/3 CLOSES;
7073 tok3/3 CLOSES beside it) aluf
mivtzar (4014 tok1/1 — "fortress", once as a name) [VERIFIED:
SNAPSHOT Gen.36.42]. No etnachta (tifcha split, fallback #7 —
the span's last).""",
  "Kenaz and Teman ranked; a fortress-name once."),

 _V((36,43), "THE_BRACKET_CLOSES",
  "chief Magdiel, chief Iram. These are the chiefs of Edom, by their dwellings, in the land of their holding — he is Esau, father of Edom.",
  "chief Magdiel, chief Iram",
  "the chiefs of Edom by their dwellings in the land of their holding — he is Esau, father of Edom",
  "HOLDS(ele_alufe_edom_be_eretz_achuzatam(hu_esav_avi_edom), t0)",
  ("ele",6), """
THE HOLDING-WORD REACHES EDOM FIRST [CROWN 5; care 10]. aluf
magdiel aluf IRAM (441 tok42/44)... ele ALUFE edom (tok43/44 —
the chief-title's last in-span token; tok44 = Exod 15:15's
terrified chiefs [CROWN 2]) le-moshvotam be-eretz ACHUZATAM
(272 tok5/39) [VERIFIED: SNAPSHOT Gen.36.43] — achuza, the
HOLDING-noun: toks 1-4 are Abraham's (17:8's achuzat olam,
the everlasting-holding promise; 23:4,9,20 the grave-holding
at Machpelah); tok5 is EDOM'S — Esau's line reaches the
covenant's land-tenure word before Jacob's does (toks 6-9 =
47:11's Goshen grant, 48:4's retell, 49:30/50:13's Machpelah
burial-retells; then Lev 14:34's house-law and the Lev 25
jubilee cluster; 39 tokens in all). HU ESAV AVI EDOM — equation #4: the
chapter's last clause restates its first; the bracket closes
on the man who is the nation. UNIT END: SPECS EMPTY — ZERO
pushed, ZERO popped across 43 verses (the ledger class);
REGISTRY 0 writes; TESTS 0 [VERIFIED: zero tov-adjective
(2896) tokens in Gen 36].""",
  "The holding-word lands in Edom first; the bracket closes empty-handed and full-named."),
]

# ---------------------------------------------------------------------------

def _s(id, ref, frag, title, given, expect, occ=1):
    d = dict(id=id, ref=ref, frag=frag, title=title, given=given, expect=expect)
    d["occ"] = occ
    return d

SE = "SPECS empty;"
NTN = "no test, no name."

SCENS = [
 _s("S1", (36,1), ("ve-ele",3),
    "after STEP_Gn_36_1 — the first header; queue empty",
    "These are the generations of Esau — he is Edom.", [SE, NTN]),
 _s("S2", (36,2), ("esav",4),
    "after STEP_Gn_36_2 — the Canaan wives; queue empty",
    "Esau took his wives from the daughters of Canaan.", [SE, NTN]),
 _s("S3", (36,3), ("ve-et",3),
    "after STEP_Gn_36_3 — the Ishmael wife; queue empty",
    "Basmat, daughter of Ishmael, sister of Nevayot.", [SE, NTN]),
 _s("S4", (36,4), ("va-teled",4),
    "after STEP_Gn_36_4 — Elifaz and Reuel born; queue empty",
    "Ada bore Elifaz; Basmat bore Reuel.", [SE, NTN]),
 _s("S5", (36,5), ("ve-aholivama",2),
    "after STEP_Gn_36_5 — the Canaan-born close; queue empty",
    "These are Esau's sons born in the land of Canaan.", [SE, NTN]),
 _s("S6", (36,6), ("va-yelekh",5),
    "after STEP_Gn_36_6 — the withdrawal from before Jacob; queue empty",
    "He went to a land, away from before Jacob his brother.", [SE, NTN]),
 _s("S7", (36,7), ("ki",4),
    "after STEP_Gn_36_7 — the land could not bear them; queue empty",
    "The land of their sojournings could not bear them.", [SE, NTN]),
 _s("S8", (36,8), ("va-yeshev",4),
    "after STEP_Gn_36_8 — Seir settled; queue empty",
    "Esau dwelt in the hill-country of Seir — he is Edom.", [SE, NTN]),
 _s("S9", (36,9), ("ve-ele",4),
    "after STEP_Gn_36_9 — the second header; queue empty",
    "The generations of Esau, father of Edom, in Seir.", [SE, NTN]),
 _s("S10", (36,10), ("ele",4),
    "after STEP_Gn_36_10 — the sons named, none written; queue empty",
    "Elifaz son of Ada; Reuel son of Basmat.", [SE, NTN]),
 _s("S11", (36,11), ("va-yihyu",3),
    "after STEP_Gn_36_11 — Teman and Kenaz debut; queue empty",
    "Teman, Omar, Tzefo, Gatam, Kenaz.", [SE, NTN]),
 _s("S12", (36,12), ("ve-timna",4),
    "after STEP_Gn_36_12 — Amalek born of Timna; queue empty",
    "Timna bore to Elifaz Amalek.", [SE, NTN]),
 _s("S13", (36,13), ("ve-ele",3),
    "after STEP_Gn_36_13 — Reuel's four; queue empty",
    "Nachat, Zerach, Shama, Miza — Basmat's line.", [SE, NTN]),
 _s("S14", (36,14), ("ve-ele",4),
    "after STEP_Gn_36_14 — Aholivamah's three; queue empty",
    "She bore to Esau Yeush, Yalam, and Korach.", [SE, NTN]),
 _s("S15", (36,15), ("ele",3),
    "after STEP_Gn_36_15 — the chief-title minted; queue empty",
    "These are the chiefs of the sons of Esau.", [SE, NTN]),
 _s("S16", (36,16), ("aluf",3),
    "after STEP_Gn_36_16 — Amalek titled; queue empty",
    "Chief Korach, chief Gatam, chief Amalek.", [SE, NTN]),
 _s("S17", (36,17), ("ve-ele",6),
    "after STEP_Gn_36_17 — Reuel's chiefs; queue empty",
    "Chief Nachat, chief Zerach, chief Shama, chief Miza.", [SE, NTN]),
 _s("S18", (36,18), ("ve-ele",5),
    "after STEP_Gn_36_18 — Aholivamah's chiefs; queue empty",
    "Chief Yeush, chief Yalam, chief Korach.", [SE, NTN]),
 _s("S19", (36,19), ("ele",2),
    "after STEP_Gn_36_19 — the son-ledger seals; queue empty",
    "These are Esau's sons and their chiefs — he is Edom.", [SE, NTN]),
 _s("S20", (36,20), ("ele",4),
    "after STEP_Gn_36_20 — the Horites enter; queue empty",
    "The sons of Seir the Horite, the dwellers of the land.", [SE, NTN]),
 _s("S21", (36,21), ("ve-dishon",3),
    "after STEP_Gn_36_21 — the Horite seven; queue empty",
    "The Horite chiefs, sons of Seir, in the land of Edom.", [SE, NTN]),
 _s("S22", (36,22), ("va-achot",3),
    "after STEP_Gn_36_22 — Timna the sister; queue empty",
    "And Lotan's sister was Timna.", [SE, NTN]),
 _s("S23", (36,23), ("ve-ele",3),
    "after STEP_Gn_36_23 — Shoval's five; queue empty",
    "Alvan, Manachat, Eval, Shefo, Onam.", [SE, NTN]),
 _s("S24", (36,24), ("hu",4),
    "after STEP_Gn_36_24 — the yemim found; queue empty",
    "The Ana who found the yemim in the wilderness.", [SE, NTN]),
 _s("S25", (36,25), ("ve-ele",3),
    "after STEP_Gn_36_25 — Ana's two; queue empty",
    "Dishon; and Aholivamah, daughter of Ana.", [SE, NTN]),
 _s("S26", (36,26), ("ve-ele",3),
    "after STEP_Gn_36_26 — Dishan's four; queue empty",
    "Chemdan, Eshban, Yitran, Cheran.", [SE, NTN]),
 _s("S27", (36,27), ("ele",3),
    "after STEP_Gn_36_27 — Etzer's three; queue empty",
    "Bilhan, Zaavan, Akan.", [SE, NTN]),
 _s("S28", (36,28), ("ele",3),
    "after STEP_Gn_36_28 — Dishan's two; queue empty",
    "Utz and Aran.", [SE, NTN]),
 _s("S29", (36,29), ("ele",3),
    "after STEP_Gn_36_29 — the Horite chiefs; queue empty",
    "Chief Lotan, chief Shoval, chief Tzivon, chief Ana.", [SE, NTN]),
 _s("S30", (36,30), ("aluf",2),
    "after STEP_Gn_36_30 — the Horite ledger seals; queue empty",
    "The Horite chiefs by their chiefdoms in Seir.", [SE, NTN]),
 _s("S31", (36,31), ("ve-ele",6),
    "after STEP_Gn_36_31 — the kings before the kings; queue empty",
    "Before a king reigned for the sons of Israel.", [SE, NTN]),
 _s("S32", (36,32), ("va-yimlokh",4),
    "after STEP_Gn_36_32 — Bela son of Beor; queue empty",
    "Bela son of Beor reigned; his city was Dinhava.", [SE, NTN]),
 _s("S33", (36,33), ("va-yamat",2),
    "after STEP_Gn_36_33 — the die-and-reign chain opens; queue empty",
    "Bela died; Yovav from Botzra reigned in his place.", [SE, NTN]),
 _s("S34", (36,34), ("va-yamat",2),
    "after STEP_Gn_36_34 — Chusham the Temanite; queue empty",
    "Chusham from the land of the Temanite reigned.", [SE, NTN]),
 _s("S35", (36,35), ("ha-make",4),
    "after STEP_Gn_36_35 — Hadad who struck Midian; queue empty",
    "Hadad, who struck Midian in the field of Moab.", [SE, NTN]),
 _s("S36", (36,36), ("va-yamat",2),
    "after STEP_Gn_36_36 — Samla of Masreka; queue empty",
    "Samla from Masreka reigned in his place.", [SE, NTN]),
 _s("S37", (36,37), ("va-yimlokh",4),
    "after STEP_Gn_36_37 — Shaul of Rechovot; queue empty",
    "Shaul from Rechovot-of-the-river reigned.", [SE, NTN]),
 _s("S38", (36,38), ("va-yamat",2),
    "after STEP_Gn_36_38 — Baal-Chanan; queue empty",
    "Baal-Chanan son of Akhbor reigned in his place.", [SE, NTN]),
 _s("S39", (36,39), ("ve-shem",8,2),
    "after STEP_Gn_36_39 — Hadar and the queen-line; queue empty",
    "His wife was Mehetavel, daughter of Matred, daughter of Me-zahav.", [SE, NTN]),
 _s("S40", (36,40), ("ve-ele",6),
    "after STEP_Gn_36_40 — the by-names list opens on Timna; queue empty",
    "Chief Timna, chief Alva, chief Yetet.", [SE, NTN]),
 _s("S41", (36,41), ("aluf",4),
    "after STEP_Gn_36_41 — Aholivamah a chiefdom; queue empty",
    "Chief Aholivamah, chief Ela, chief Pinon.", [SE, NTN]),
 _s("S42", (36,42), ("aluf",4),
    "after STEP_Gn_36_42 — Kenaz, Teman, Mivtzar; queue empty",
    "Chief Kenaz, chief Teman, chief Mivtzar.", [SE, NTN]),
 _s("S43", (36,43), ("ele",6),
    "after STEP_Gn_36_43 — the bracket closes; the wall is empty",
    "These are the chiefs of Edom — he is Esau, father of Edom.", [SE, NTN]),
]
