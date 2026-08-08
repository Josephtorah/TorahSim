# -*- coding: utf-8 -*-
"""Authored content for lev_19 (19:1-37). DB evidence: lev19_prestage_full.txt
(regenerable: python3 logic/solo_tools/prestage.py Lev 19:1-19:37) + targeted
queries logged in the derivation session 2026-08-07 (probe wave, block 1)."""

UID = "lev_19_holiness_duty_ledger"
BOOK = "Lev"
SPAN = (19, 1, 19, 37)
EXTRA_SUBS = {
    # Object-marker vs with-preposition (853 vs 854), span-checked per token:
    # et-kha 19:13,33 and et-khem 19:34 are BOTH the with-preposition (854)
    # -> itkha/itkhem, overriding the global 853 reading "otkha"; et-o 19:33
    # and et-m 19:10,37 are the object-marker (853) -> oto/otam. 19:36's
    # et-khem is 853 ("brought YOU out") - but 854's itkhem at 19:34 and
    # 853's etkhem at 19:36 share one raw key, so et-khem stays RAW span-wide
    # (the gen_58 et-o mixed-lemma precedent). la-ה/le-haznota-ה are global.
    "et-kha": "itkha", "et-o": "oto", "et-m": "otam",
    # ve-avi-v: frozen gen_58 keeps the raw form (35:18 substring scan) —
    # global key withheld, polished here (the ahol-o carve-out class).
    "ve-avi-v": "ve-aviv",
}


META = [
    ("id", "lev_19_holiness_duty_ledger"),
    ("title_en", '"The holiness ledger: fifty-six statutes under one open card (19:1-37) - the apodictic probe"'),
    ("title_he", "קְדֹשִׁים תִּהְיוּ כִּי קָדוֹשׁ אֲנִי יְהוָה אֱלֹהֵיכֶם"),
    ("title_he_translit", "qedoshim tihyu ki qadosh ani YHWH elohekhem"),
    ("title_he_en", "\"'Holy shall you be, for holy am I, the LORD your God'\""),
    ("book_he", "וַיִּקְרָא"),
    ("book_he_translit", "Va-yiqra"),
    ("book_en", "Leviticus"),
    ("refs", "19:1-37"),
    ("unit_span_planned", "19:1-37"),
]

DRAFT_NOTE = """
DRAFT 2026-08-07 · SOLO ERA unit #14 · PROBE WAVE BLOCK 1 (owner order
2026-08-07: "probe wave lets do it" - jump ahead to Leviticus to
stress-test the encoding on the law genres before Gen 37-Exodus).
Span: 19:1-37, whole chapter: 37 verses · 440 tokens
(SNAPSHOT-verified). SNAPSHOT + debut_map. Conventions: step he: =
plain; tree halves = accents kept, slashes stripped; split at etnachta
- 36 of 37 verses carry one; the single verse without one is 19:1, THE
FRAME VERSE (tifcha idx1 fallback): the only narrative verse is the
only unbracketed verse, lev_13's exact signature re-run (there 13:1,
same shape). No ketiv in span. Onkelos BUFFER PENDING.

THE PROBE QUESTION AND ITS ANSWER. The narrative machine pushes
demands on true volitives (imperative / jussive / cohortative) and
lets decree grammar write nothing (gen_33) - so what does a chapter
do that commands ~fifty times with almost no volitives? The prestage
census: FIVE volitive tokens in 440 - ONE imperative (daber, 19:2,
YHWH to Moses: the relay), FOUR al-jussives (19:4 tifnu; 19:29
techalel; 19:31 tifnu, tevaqshu) - while the chapter's obligations
ride 42 lo-negated imperfects [VERIFIED: lemma 3808 in-span = 42],
bare imperfects, and weqatal duty-forms (gen_40's class). ANSWER
(the unit's thesis, the STATUTE operator): the LAW-RELAY FRAME
RE-TYPES. lev_13 established that ki ("when") re-types an imperfect
from demand to case-condition; this unit extends the same law to the
relay frame - a directive spoken THROUGH Moses TO a standing class
(kal adat bene yisrael, "the whole congregation") over open time is
not a scene-demand owed a narrated receipt; it is a STANDING STATUTE,
installed as a WORLD fact (the gen_48 vow-HANDLER / day-5
BLESS-mandate family). The letter's own witness sits in 19:4: EL
tifnu (negative particle + jussive - narrative's LET-NOT grammar,
gen_54's law) is coordinated in ONE prohibition list with LO taasu
(negated imperfect - narrative's writes-nothing grammar): inside the
law frame the two moods carry ONE register. So the four al-jussives
re-type to FORBID statutes exactly as the lo-imperfects do, and the
census closes 5 = 1 push + 4 re-typed [mood-law: gen_41's
retell-fence and lev_13's ki-retyping are the siblings; TIR-028/033
untouched - no LET? upgrades occur].

UNIT SHAPE - ONE CARD, FIFTY-SIX STATUTES: the queue takes exactly
ONE demand all span - 19:2's daber el kal adat bene yisrael, YHWH's
true imperative to Moses (Vpv2ms) - and it stays OPEN at the wall:
no verse of this chapter narrates Moses speaking to the congregation
(the span holds ONE wayyiqtol total, 19:1's va-yedaber, 1 narrative
verb in 440 tokens [VERIFIED: morph scan - the only V?w token]; the
compliance-class silence of gen_58, here on the relay itself). Under
that single open card the statute register fills: 56 statutes (39
FORBID + 17 BIND), 4 CASES, 8 HANDLERS - 68 standing facts, zero
executions. REGISTRY 0 [VERIFIED: zero qara-lemma (7121) tokens
in-span - fifty-six laws, not one name written]. TESTS 0 [VERIFIED:
zero tov-adjective (2896) tokens in-span]. Machine profile: the
narrative registers sleep while a register narrative never needed
does all the work - the probe's finding is that the law genre is
REAL and ADDITIVE: one new operator, no narrative semantics touched.

CROWN 1 - THE SEAL GRID (ani YHWH x16, 8+8): the chapter signs
itself sixteen times - ani YHWH elohekhem ("I am the LORD your
God") and bare ani YHWH ("I am the LORD") - and the census splits
EXACTLY EIGHT AND EIGHT [VERIFIED: adjacency scan - long at 19:2,
3, 4, 10, 25, 31, 34, 36; short at 19:12, 14, 16, 18, 28, 30, 32,
37]. The FIRST short seal is 19:12 - the false-oath verse: at the
exact line where swearing vi-shemi la-shaqer ("by My name falsely")
is banned, the seal drops elohekhem and becomes the bare Name. The
19:36 long seal alone extends into a clause - asher hotzeti etkhem
me-eretz mitzrayim ("who brought you out of the land of Egypt") -
the exodus signature on the verse of honest scales; and the chapter
closes 19:37 on a bare ani YHWH.

CROWN 2 - THE LOVE-COMMAND'S FOUR TOKENS: ve-ahavta ("and you shall
love", weqatal Vqq2ms of 157) occurs exactly FOUR times in the Torah
[VERIFIED: translit census]: Lev 19:18 (le-reakha kamokha, "your
neighbor as yourself"), Lev 19:34 (lo kamokha - the GER, "the
stranger as yourself"), Deut 6:5 and Deut 11:1 (et YHWH elohekha).
Both human-object love-commands stand in THIS chapter; both
God-object tokens are Deuteronomy's - two loves here, two there,
and kamokha ("as yourself") rides only the human pair.

CROWN 3 - THE VERBATIM TRIPLE: (a) 19:15 and 19:35 open with the
same four tokens letter-identical - lo taasu avel ba-mishpat ("you
shall do no wrong in judgment") [VERIFIED: he_plain identity] -
first over the courtroom (faces of poor and great), then over the
marketplace (measure, weight, liquid-measure): one clause, two
jurisdictions. (b) 19:30 recurs WHOLE-VERSE letter-identical at
26:2 - et shabtotay tishmoru u-miqdashi tirau ani YHWH [VERIFIED:
he_plain identity] - the sentence re-issued as the gate to the
blessings-and-curses chapter. (c) the harvest-edge block 19:9-10
re-issues at 23:22 inside the festival calendar - leqet
("gleaning", 3951) has exactly TWO Torah tokens, 19:9 and 23:22
[VERIFIED: 1-2/2], and the qatzir/peah/taazov chain re-runs there
token-class by token-class.

CROWN 4 - THE FEAR-KEEP CHIASM (19:3 <-> 19:30): 19:3 - ish imo
ve-aviv TIRAU ve-et shabtotay TISHMORU (fear mother-and-father,
keep My sabbaths); 19:30 - et shabtotay TISHMORU u-miqdashi TIRAU
(keep My sabbaths, fear My sanctuary): the same two verbs cross
over, parents traded for sanctuary. And 19:3 is MOTHER-FIRST
against both Decalogues' father-first (kabed et AVIKHA ve-et
IMEKHA, Exod 20:12 = Deut 5:16 [VERIFIED: token order all three]);
the fear-verb yare takes parents as object nowhere else. The
my-sabbaths noun-form shabtotay has 4 Torah tokens - Exod 31:13,
19:3, 19:30, 26:2 [VERIFIED] - three of its four in this chapter's
orbit.

CROWN 5 - THE HADAR REVERSAL: the honor-verb hadar has THREE Torah
tokens [VERIFIED: 1921 census]: Exod 23:3 (lo tehdar - do not favor
even the POOR man's case), 19:15 (lo tehdar pene gadol - do not
favor the GREAT in judgment), 19:32 (ve-hadarta pene zaqen - you
SHALL honor the face of the aged). The same verb, banned twice at
court and commanded once before grey hair - the career closes
in-span, FORBID and BIND on one root in one chapter.

CROWN 6 - SIXTEEN WHOLE-CAREER HAPAXES: sixteen lemmas live their
entire Torah life inside this chapter [VERIFIED: debut_map total=1,
in-span]: peret (fallen grapes), peulat (the wage), mikhshol (the
stumbling-block), rakhil (the talebearer), titor (the grudge-verb),
necherefet (the designated woman), chufsha (freedom), biqoret (the
inquest), chupasha (she-was-freed), va-araltem (the
treat-as-foreskin verb), hilulim (praise-fruit), taqifu (the
round-off verb), ketovet + qaaqa (the tattoo pair, one verse),
mesura (the liquid measure), mozne (the scales). FOUR of them stand
in 19:20 alone (necherefet, chufsha, biqoret, chupasha - the
inquest-not-death case speaks entirely in words used nowhere else;
corpus max is six, Gen 36:39, so a fact, not a record). No corpus
superlative claimed for the sixteen either: name-list chapters run
higher (Num 26 holds 63 hapax tokens) - the fact is that a LAW
chapter mints and retires sixteen legal instruments in one sitting.

CROWN 7 - GENESIS ARMS LAND (the frozen corpus reaches this span):
(a) nachash ("divine/read omens", 5172, 7 tokens) DEBUTED in
Laban's mouth at Gen 30:27 - gen_52's watchlist arm - and lands
here BANNED at 19:26 (tok 6/7; Joseph's cup holds 4; Deut 18:10
closes). (b) zanah ("play the harlot", 2181) tok1 is Gen 34:31 -
gen_57's closing question (ha-khe-zona) - and the root returns at
19:29 as the daughter-prostitution ban (toks 8-9/20; Deut 22:21's
li-zenot, gen_57's reunion verse, is tok18). (c) the reprove-verb
yakhach CLOSES its 8-token career at 19:17's hokheach tokhiach -
and tokens 5-6 are gen_54's tribunal pair (31:37 ve-yokhichu, 31:42
va-yokhach): Laban's court, God's night-verdict, then the standing
duty to reprove. (d) ganav ("steal"): tokens 1-12 of 21 are all
Genesis - Rachel's theft, the heart-thefts, the accusation storm
(gen_53/54 spans own six) - and 19:11's tignovu is the Torah's
ONLY 2mp token of the verb [VERIFIED: morph census]: the Decalogue
bans theft in the singular (Exod 20:15 / Deut 5:19 tignov, 2ms);
holiness bans it in the plural. (e) shaqar ("deal falsely", 8266,
2 tokens) closes here: Gen 21:23 - Avimelech exacting Abraham's
oath im-tishqor li - then 19:11's teshaqru: the patriarch's sworn
promise becomes the people's standing law. (f) gazal ("rob", 1497):
Gen 21:25 (the seized well) and 31:31 (Jacob's fear-word) precede
19:13's ban. (g) tame ("defile", 2930) tok1 = Gen 34:5 - Dinah,
gen_57's purity-debut - and 19:31's le-tama ("to be defiled by
them") extends the same root to mediums.

CROWN 8 - THE JUSSIVE PAIR AND THE TURN-VERB: the turn-verb pana
carries exactly TWO PLURAL (2mp) jussive tokens in the Torah
[VERIFIED: 6437 morphs - HVqj2mp x2; its two SINGULAR jussives are
Moses' al-tefen "do-not-turn" prayers, Num 16:15 and Deut 9:27],
and both are this chapter's: 19:4 el tifnu
el ha-elilim ("do not turn to the idols") and 19:31 el tifnu el
ha-ovot ("do not turn to the ghost-mediums") - the same three-word
opener re-issued, idols traded for mediums, decalogue-face traded
for necromancy. elilim ("worthless gods", 457) DEBUTS here (1/2;
26:1 closes); ovot and yidonim (178/3049) both debut here (1/4
each; both careers end in Deut 18:11's ban-list); masekha ("molten
image", 4541, tok 4/8) arrives carrying the CALF - its first three
tokens are Exod 32:4, 32:8 (the golden calf), 34:17 (the ban).

CROWN 9 - TZEDEQ'S FIVE-TOKEN OPENING: the righteousness-noun
tzedeq enters the Torah at 19:15 (be-tzedeq tishpot amitekha,
tok 1/12) and takes tokens 2-3-4-5 in ONE VERSE at 19:36 - mozne
TZEDEQ avne TZEDEQ efat TZEDEQ ve-hin TZEDEQ ("just scales, just
weights, a just efah, a just hin") [VERIFIED: 6664 ordinals 1-5
in-span]: the noun's first five tokens are this chapter's court
and market; Deut 16:20's tzedeq tzedeq tirdof doubling comes
eighth-ninth (tok7 = Deut 16:18). And amit ("fellow", 5997,
11 tokens) is a
LEVITICUS-ONLY noun [VERIFIED: book census] - three of its
eleven in-span (19:11, 15, 17).

CROWN 10 - THE ENFORCEMENT CLAUSE OF INVISIBLE WRONGS: ve-yareta
me-elohekha ("and you shall fear your God") occurs FIVE times in
the Torah, ALL in Leviticus [VERIFIED: translit census - 19:14,
19:32, 25:17, 25:36, 25:43]: first on the deaf-and-blind verse
(curse the deaf, stumble the blind - wrongs no victim can report),
then on rising before grey hair, then over Lev 25's hidden
oppressions. Where no court can see, the statute installs fear as
the enforcement. And 19:14's protected pair closes another career:
cheresh ("the deaf", 2795) has TWO Torah tokens - Exod 4:11 (mi
yasum... o cheresh - the Maker's own claim to have made the deaf)
and this verse's ban [VERIFIED: 2/2]; iver ("the blind") rides the
same two verses (2/6 here).

CROWN 11 - THE RELAY'S DISTRIBUTION LIST: 19:2's daber el KAL ADAT
bene yisrael is the Torah's ONLY daber-imperative ("speak")
addressed to the whole congregation of the sons of Israel - the
claim is VERB-SPECIFIC: Exod 16:9's emor ("say") addresses the
same four-token string [VERIFIED: all 18
kal-adat-bene-yisrael strings scanned - no other stands as the
addressee of a daber command; Exod 12:3's kin is plural daberu and
adat yisrael without bene]: the holiness code alone puts every
Israelite on the distribution list, and the relay card it opens
never pops.

STATUTE CENSUS (the wall, machine-checked per scenario): 39 FORBID
+ 17 BIND = 56 statutes; CASES 4 (19:5 shelamim-clock; 19:20
shifcha-inquest; 19:23 orlah-clock; 19:33 ger-protection);
HANDLERS 8 (19:6/7/8 the sacrifice window, pigul, karet; 19:21/22
the asham chain to forgiveness; 19:23b/24/25 the three-stage
orchard calendar). Negation census: lo x42 + al x4 = 46 negations
across 37 verses. SPECS depth 1 OPEN at the wall (the relay card).
"""

STEPS = [
 dict(ref=(19,1), op="THE_FRAME",
  en="And the LORD spoke to Moses, saying:",
  tl_en="the LORD spoke to Moses",
  tr_en="saying - the quote opener",
  ops=[
   dict(op="EVENT",
    expr="speak(e1) ∧ Agent(e1, YHWH)",
    frag=("va-yedaber",5), prose="""
THE SPAN'S ONLY NARRATIVE VERB. va-yedaber YHWH el moshe le-mor
("and the LORD spoke to Moses, saying") - Vpw3ms, the one
wayyiqtol ('and-then-he-did' form) in 440 tokens [VERIFIED: morph
scan, the only V?w token in-span]: after this verse the machine
never narrates again - lev_13's genre signature (1 narrative verb
vs 13 law verbs there) at chapter scale. And the accent layer
carries the same signature: 19:1 is the span's ONLY etnachta-less
verse [VERIFIED: mark census] - the one verse that tells instead
of binding is the one verse the cantillation leaves unbracketed
(13:1 behaved identically in the first law unit)."""),
   dict(op="NOTE_PRESUPPOSED",
    expr="moshe are READ without prior install (standalone machine; the Exodus narrative's person - cross-unit chaining is Stage E)",
    frag=("el",2), prose="""
Flag, not fix - the frame's addressee is an import (lev_13's
moshe/aharon precedent; here Moses alone: no Aaron on this
distribution list, contrast 13:1)."""),
  ],
  comment="One narrative verb, then the machine goes silent for thirty-six verses."),

 dict(ref=(19,2), op="THE_RELAY_AND_THE_THESIS",
  en="Speak to all the congregation of the sons of Israel and say to them: Holy shall you be, for holy am I, the LORD your God.",
  tl_en="speak to all the congregation of the sons of Israel and say to them",
  tr_en="holy shall you be, for holy am I, the LORD your God",
  ops=[
   dict(op="DECLARE",
    expr="DECLARE(YHWH, LET(daber_el_kal_adat(moshe)))",
    frag=("daber",6), prose="""
THE ONE CARD [UNIT SHAPE]. daber el kal adat bene yisrael
("speak to all the congregation of the sons of Israel") - the
span's single true imperative (Vpv2ms) [VERIFIED: volitive census
- 1 imperative + 4 al-jussives in 440 tokens], spoken in the
narrative present, YHWH to Moses: a real demand with a real
demandee, so it PUSHES (mood-law unchanged). ve-amarta alehem
("and you shall say to them", Vqq2ms weqatal) rides the same card
as duty-content (gen_47's aux-chain bundling). The addressee is
the Torah's ONLY whole-congregation daber-command [CROWN 11] -
and the relay is never narrated in-span: no verse says Moses
spoke these words (the one wayyiqtol is 19:1, YHWH's own). The
card stays OPEN across all fifty-six statutes it delivers. PUSH
LET(daber_el_kal_adat(moshe)). Depth 1."""),
   dict(op="STATUTE",
    expr="STATUTE BIND(qedoshim_tihyu)",
    frag=("qedoshim",7), prose="""
THE THESIS STATUTE - THE REGISTER OPENS. qedoshim tihyu ki
qadosh ani YHWH elohekhem ("holy shall you be, for holy am I,
the LORD your God") - imperfect 2mp inside the relay content:
not a scene-demand (no narrated receipt is possible for a
standing class over open time) but the LAW-FRAME RE-TYPING
[DRAFT_NOTE thesis]: the first STATUTE, and it is the chapter's
header - every FORBID and BIND below it is this one unpacked.
The motive clause is the imitatio ground: ki qadosh ANI - the
holiness-adjective pair qadosh/qedoshim rides toks 13-14/38 of
its career here [VERIFIED: 6918 ordinals], inside the family of
Lev 11:44-45 and 20:26. SEAL L1: ani YHWH elohekhem - the first
of the sixteen [CROWN 1]. STATUTES 1."""),
  ],
  comment="One push and one install in one verse: the queue and the statute register open together."),

 dict(ref=(19,3), op="MOTHER_FIRST",
  en="Each man shall fear his mother and his father, and My sabbaths you shall keep: I am the LORD your God.",
  tl_en="each man shall fear his mother and his father",
  tr_en="and My sabbaths you shall keep: I am the LORD your God",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE BIND(imo_ve_aviv_tirau)",
    frag=("ish",4), prose="""
FEAR YOUR MOTHER - MOTHER FIRST. ish imo ve-aviv tirau ("each
man - his MOTHER and his father you shall fear"): both
Decalogues honor FATHER first (kabed et avikha ve-et imekha,
Exod 20:12 = Deut 5:16 [VERIFIED: token order all three
verses]); the holiness code alone puts the mother before the
father - and swaps honor for FEAR: the fear-verb yare (3372)
takes parents as its object nowhere else in the Torah. Subject
ish ("each man", singular) with a PLURAL verb (tirau, 2mp) -
the law addresses every one and all at once in a single clause
[morph fact]. STATUTES 2."""),
   dict(op="STATUTE",
    expr="STATUTE BIND(shabtotay_tishmoru)",
    frag=("ve-et",6), prose="""
KEEP MY SABBATHS - THE CHIASM'S FIRST HALF. ve-et shabtotay
tishmoru ("and My sabbaths you shall keep") - the my-sabbaths
plural (7676, tok 17/47) whose noun-form has four Torah tokens:
Exod 31:13, here, 19:30, 26:2 [VERIFIED]. This verse pairs
FEAR(parents) + KEEP(sabbaths); 19:30 will re-issue the pair as
KEEP(sabbaths) + FEAR(sanctuary) - the two verbs cross over,
parents traded for sanctuary [CROWN 4]. SEAL L2: ani YHWH
elohekhem. STATUTES 3."""),
  ],
  comment="Fear-then-keep; the chapter will answer with keep-then-fear at 19:30."),

 dict(ref=(19,4), op="THE_RETYPING_WITNESS",
  en="Do not turn to the idols, and molten gods you shall not make for yourselves: I am the LORD your God.",
  tl_en="do not turn to the idols",
  tr_en="molten gods you shall not make for yourselves: I am the LORD your God",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(peno_el_ha_elilim)",
    frag=("el",4), prose="""
THE LETTER'S OWN WITNESS FOR THE RE-TYPING [DRAFT_NOTE thesis].
el tifnu el ha-elilim ("do NOT turn to the idols") - the
negative particle al + JUSSIVE (HVqj2mp): in narrative this
exact grammar is LET-NOT and pushes a card (gen_54's yichar,
gen_58's tiri); here it stands COORDINATED in one prohibition
list with the next clause's lo + imperfect - one register, two
moods: the law frame levels the distinction the narrative
maintains, so the jussive re-types to FORBID beside its
imperfect twin. The turn-verb pana carries exactly TWO PLURAL
(2mp) jussive tokens in the Torah and both are this chapter's
re-issued opener (19:4 idols / 19:31 mediums; its two 2ms
jussives are Moses' al-tefen prayers, Num 16:15 / Deut 9:27)
[VERIFIED: 6437 morphs; CROWN 8].
elilim ("worthless gods") DEBUTS - 1/2, its whole career ends
at 26:1 [VERIFIED: 457]. STATUTES 4."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(elohe_masekha)",
    frag=("ve-lohe",4), prose="""
THE MOLTEN GODS CARRY THE CALF. ve-lohe masekha lo taasu lakhem
("and molten gods you shall not make for yourselves") - masekha
("molten image", 4541) arrives at tok 4/8 with its first three
tokens being Exod 32:4 and 32:8 - THE GOLDEN CALF - and 34:17's
ban [VERIFIED: ordinals]: the noun's whole prior life is one
idol and its prohibition; the statute here re-signs that ban
into the holiness code. SEAL L3: ani YHWH elohekhem. STATUTES
5."""),
  ],
  comment="Jussive and imperfect side by side in one list: the probe's key verse."),

 dict(ref=(19,5), op="THE_SHELAMIM_CLOCK_OPENS",
  en="And when you sacrifice a sacrifice of well-being to the LORD, you shall sacrifice it for your acceptance.",
  tl_en="when you sacrifice a sacrifice of well-being to the LORD",
  tr_en="for your acceptance you shall sacrifice it",
  ops=[
   dict(op="CASE",
    expr="CASE(bene_yisrael, tizbchu_zevach_shelamim) ROUTE(li_retzonkhem_tizbachuhu)",
    frag=("ve-ki",7), prose="""
THE FIRST CASE - ki RE-TYPES (lev_13's law, second exercise).
ve-khi tizbchu zevach shelamim ("and WHEN you sacrifice a
sacrifice of well-being") - the ki-frame turns the imperfect
into a case-condition awaiting instances, exactly as 13:2's
adam ki-yihyeh did: no one is commanded to sacrifice; IF one
does, the clock below installs. Routing: li-retzonkhem
tizbachuhu ("for your ACCEPTANCE you shall sacrifice it") -
ratzon (7522, tok 4/11) is the acceptance-noun whose career is
almost wholly cultic law [VERIFIED: ordinals]; the shelamim
("well-being offering", 8002, tok 32/54) reaches back to Exod
24:5's covenant meal. CASES 1."""),
  ],
  comment="A case, not a command: the chapter's first ki-frame."),

 dict(ref=(19,6), op="THE_TWO_DAY_WINDOW",
  en="On the day of your sacrifice it shall be eaten, and on the morrow; and what is left until the third day shall be burned in fire.",
  tl_en="on the day of your sacrifice it shall be eaten, and on the morrow",
  tr_en="what remains to the third day is burned in fire",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(be_yom_zivchakhem_u_mi_machorat) THEN(yeakhel ∧ ha_notar_ba_esh_yisaref)",
    frag=("be-yom",10), prose="""
THE CONSUMPTION WINDOW. be-yom zivchakhem yeakhel u-mi-machorat
("on the day of your sacrifice it shall be eaten, and on the
morrow") - NIPHAL imperfect (yeakhel, "it SHALL BE eaten"):
passive time-law, no commanded agent (13:2's ve-huva class);
ve-ha-notar ad yom ha-shelishi ba-esh yisaref ("and what is
LEFT to the third day shall be BURNED in fire") - the
leftover-participle notar (3498, tok 26/33) is manna-law and
sacrifice-law vocabulary; the day-count rides ha-shelishi
(7992, toks 18-19/31 here and next verse). HANDLERS 1."""),
  ],
  comment="A clock on the altar: two days to eat, the third day burns."),

 dict(ref=(19,7), op="PIGUL",
  en="And if it is eaten at all on the third day, it is a foul thing; it shall not be accepted.",
  tl_en="if it is eaten at all on the third day",
  tr_en="it is pigul - a foul thing; it shall not be accepted",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(heakhol_yeakhel_ba_yom_ha_shelishi) THEN(pigul_hu_lo_yeratze)",
    frag=("ve-im",9), prose="""
THE VIOLATION BRANCH - WITH THE DOUBLED INFINITIVE. ve-im
heakhol yeakhel ("and if it IS EATEN at all" - VNa + VNi3ms,
the infinitive-absolute doubling on a PASSIVE: the mot-tamut
construction marking the branch that breaks the clock; 13:7's
pasoh tifseh class) ba-yom ha-shelishi - THEN pigul hu ("it is
a foul thing"): pigul (6292) has exactly TWO Torah tokens -
Lev 7:18 (the same third-day law in the priests' code) and
here [VERIFIED: 2/2 - the career CLOSES]: the rejection-noun
exists only for this one offense, twice stated, once for the
priests and once for the whole congregation. lo yeratze ("it
shall not be accepted") - the acceptance-verb ratzah negated
(7521, tok 4/14). HANDLERS 2."""),
  ],
  comment="The whole life of the word pigul: this law, told twice."),

 dict(ref=(19,8), op="KARET_ON_THE_EATER",
  en="And its eaters shall bear his iniquity, for the holy thing of the LORD he has profaned; and that soul shall be cut off from its people.",
  tl_en="its eaters bear his iniquity: the holy thing of the LORD profaned",
  tr_en="that soul is cut off from its people",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(akhal_pigul) THEN(avono_yisa ∧ nikhrta_ha_nefesh_me_ameha)",
    frag=("ve-okhlay-v",12), prose="""
THE SANCTION. ve-okhlav avono yisa ("and its EATERS shall bear
his iniquity" - plural participle Vqrmpc, the singular yisa
distributing over each eater) - the bear-iniquity idiom (avon 5771 tok 19/42 +
nasa 5375 tok 93/168); ki et qodesh YHWH chilel ("for the holy
thing of the LORD he has PROFANED") - the profane-verb chalal
(2490, tok 12/41) against the chapter's own thesis-adjective:
eat on the third day and you have profaned the qodesh of the
God who said BE HOLY; ve-nikhrta ha-nefesh ha-hiv me-ameha
("and that soul shall be cut off from its people") - the karet
formula (3772, tok 32/69), Gen 17:14's covenant-cut grammar as
the law's own sanction. HANDLERS 3. STATUTES still 5 - the
case-block installs procedure, not new statutes."""),
  ],
  comment="Profane the holy and be cut from the people: the thesis has teeth."),

 dict(ref=(19,9), op="THE_UNREAPED_CORNER",
  en="And when you reap the harvest of your land, you shall not finish the corner of your field in reaping, and the gleaning of your harvest you shall not gather.",
  tl_en="when you reap the harvest of your land: do not finish the corner",
  tr_en="the gleaning of your harvest you shall not gather",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(tekhale_peat_sadkha)",
    frag=("u-ve-qutzr-khem",9), prose="""
THE CORNER LEFT STANDING. u-ve-qutzrkhem et qetzir artzkhem
("and when YOU REAP the harvest of your land" - the temporal
infinitive frames without casing) lo tekhale peat sadkha
li-qtzor ("you shall not FINISH the corner of your field in
reaping") - the finish-verb kala (3615, tok 29/46) is Gen 2:2's
completion-verb: the God who FINISHED his work forbids the
farmer to finish his field. pea ("corner", 6285, tok 17/27):
its first FIFTEEN tokens are all the MISHKAN's sides [VERIFIED:
ordinals - Exod 25-38]; tok 16 is Lev 13:41's head-edge (the
baldness law) - the architecture-word walks sanctuary wall,
head, and now FIELD, and 19:27 will send it back to the head. STATUTES 6."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(leqet_qetzirkha)",
    frag=("ve-leqet",4), prose="""
THE GLEANING. ve-leqet qetzirkha lo telaqet ("and the gleaning
of your harvest you shall not gather") - leqet the
gleaning-noun (3951) DEBUTS: 1/2, and its ONLY other token is
23:22, where this whole two-verse block re-issues inside the
festival calendar [VERIFIED: 2/2; CROWN 3c]. The gather-verb
laqat (3950, tok 12/15) carries gen_54's find in its career:
tok1 is 31:46's liqtu avanim - the heap of witness - and toks
3-11 are the MANNA laws. STATUTES 7."""),
  ],
  comment="The harvest law: what you do not take is the poor man's title."),

 dict(ref=(19,10), op="VINEYARD_AND_THE_POOR",
  en="And your vineyard you shall not glean, and the fallen grapes of your vineyard you shall not gather; for the poor and for the stranger you shall leave them: I am the LORD your God.",
  tl_en="your vineyard you shall not glean; the fallen grapes you shall not gather",
  tr_en="for the poor and the stranger leave them: I am the LORD your God",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(teolel_karmkha)",
    frag=("ve-kharm-kha",3), prose="""
NO SECOND PASS. ve-kharmkha lo teolel ("and your vineyard you
shall not glean-over") - the glean-verb olel (5953, tok 2/4)
whose only other duty-token is Deut 24:21's same law. STATUTES
8."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(peret_karmkha)",
    frag=("u-feret",4), prose="""
THE FALLEN GRAPES - A HAPAX INSTRUMENT. u-feret karmkha lo
telaqet ("and the FALLEN GRAPES of your vineyard you shall not
gather") - peret lives its entire Torah life in this clause
[VERIFIED: 6528 1/1; CROWN 6]: a word minted for the single
purpose of being left on the ground. STATUTES 9."""),
   dict(op="STATUTE",
    expr="STATUTE BIND(le_ani_ve_la_ger_taazov)",
    frag=("le-ani",4), prose="""
LEAVE THEM - THE POSITIVE FACE. le-ani ve-la-ger taazov otam
("for the poor and for the stranger you shall LEAVE them") -
the leave-verb azav whose tok1 is Gen 2:24 (leave father and
mother) here binds the harvest's remainder to ani ("the poor",
6041 tok 2/7) and GER ("the stranger", 1616 tok 22/68) - the
stranger's first statute in the chapter that will command his
LOVE at 19:34. SEAL L4: ani YHWH elohekhem. STATUTES 10."""),
  ],
  comment="Two refusals and one bequest: the field's edges belong to the landless."),

 dict(ref=(19,11), op="THE_DECALOGUE_GOES_PLURAL",
  en="You shall not steal, and you shall not deny falsely, and you shall not lie each man to his fellow.",
  tl_en="you shall not steal",
  tr_en="you shall not deny, you shall not lie each man to his fellow",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(tignovu)",
    frag=("lo",2), prose="""
THE ONLY PLURAL THEFT-BAN. lo tignovu ("you shall not steal" -
2mp): the steal-verb ganav has 21 Torah tokens and this is its
ONLY 2mp form [VERIFIED: morph census] - the Decalogue bans
theft in the singular (lo tignov, Exod 20:15 / Deut 5:19);
holiness re-issues it to the plural congregation. And the
verb's tokens 1-12 are ALL Genesis - Rachel's terafim-theft,
Jacob's heart-theft, Laban's accusation storm, Joseph's
stolen-stolen doubling - eight of them inside our frozen gen_53/
gen_54 spans [CROWN 7d]: the narrative corpus's crime becomes
the law corpus's clause. STATUTES 11."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(tekhachashu)",
    frag=("ve-lo",2), prose="""
NO FALSE DENIAL. ve-lo tekhachashu ("and you shall not deny
falsely") - kachash (3584, tok 4/5): tok1 is Gen 18:15 - SARAH
DENIED, saying I laughed not - and toks 2-3 are Lev 5:21-22's
sacrilege case: the matriarch's frightened denial, the case
law, then the standing ban. STATUTES 12."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(teshaqru_ish_ba_amito)",
    frag=("ve-lo",4,2), prose="""
THE OATH OF AVIMELEKH BECOMES LAW. ve-lo teshaqru ish ba-amito
("and you shall not deal falsely each man with his fellow") -
shaqar the deal-falsely verb has exactly TWO Torah tokens
[VERIFIED: 8266 2/2 - career CLOSES]: Gen 21:23, Avimelekh
exacting Abraham's oath at Beersheba (im-tishqor li, "that you
will not deal falsely with me"), and this verse: what one king
once made one patriarch swear, the code binds on every
Israelite. amit ("fellow", 5997, tok 4/11) - the Leviticus-only
noun [CROWN 9]. STATUTES 13."""),
  ],
  comment="Steal, deny, lie: the property triad, plural for the first time."),

 dict(ref=(19,12), op="THE_NAME_SEALS_ITSELF",
  en="And you shall not swear by My name falsely, so that you profane the name of your God: I am the LORD.",
  tl_en="you shall not swear by My name falsely",
  tr_en="and profane the name of your God: I am the LORD",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(tishavu_vi_shemi_la_shaqer)",
    frag=("ve-lo",4), prose="""
THE FIRST BARE SEAL [CROWN 1]. ve-lo tishavu vi-shemi la-shaqer
("and you shall not SWEAR BY MY NAME falsely") - the oath-verb
shava (7650, tok 29/70) whose Genesis career is the corpus's
oath-ledger (Beersheba x3, Abraham's servant, the birthright);
ve-chilalta et shem elohekha ("so that you profane the NAME of
your God") - chalal again (tok 13/41, second time in-span:
first the holy THING at 19:8, now the NAME). And here the seal
grid turns: after four long seals, THIS verse - the
false-oath-by-the-Name verse - carries the chapter's FIRST
bare ani YHWH ("I am the LORD", no elohekhem): where the Name
is profaned, the Name alone signs [VERIFIED: seal census, short
seals begin 19:12]. SEAL S1. STATUTES 14."""),
  ],
  comment="Swear falsely by the Name, and the seal answers with the bare Name."),

 dict(ref=(19,13), op="THE_WAGE_MUST_NOT_SLEEP",
  en="You shall not oppress your neighbor and you shall not rob; the wage of a hired man shall not stay the night with you until morning.",
  tl_en="you shall not oppress your neighbor and you shall not rob",
  tr_en="the hired man's wage shall not sleep with you until morning",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(taashoq_et_reakha)",
    frag=("lo",4), prose="""
NO OPPRESSION. lo taashoq et reakha ("you shall not OPPRESS
your neighbor") - ashaq (6231, tok 3/6): toks 1-2 are Lev
5:21-23's sacrilege-case (the defrauded fellow), tok 4 is Deut
24:14's hired-man law - the verb's whole career is this verse's
two clauses unpacked. rea ("neighbor", 7453, tok 28/52) - first
of the chapter's three (19:13 oppressed, 19:16 bled, 19:18
loved). STATUTES 15."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(tigzol)",
    frag=("ve-lo",2), prose="""
NO ROBBERY. ve-lo tigzol ("and you shall not rob") - gazal
(1497, tok 4/6): tok1 is Gen 21:25, the WELL Avimelekh's
servants seized (the same Beersheba scene whose oath became
19:11's shaqar-ban); tok2 is Gen 31:31 - Jacob's fear-word to
Laban ("lest you TEAR your daughters from me"), inside frozen
gen_54's span [CROWN 7f]. STATUTES 16."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(talin_peulat_sakhir)",
    frag=("lo",7,2), prose="""
THE WAGE'S NIGHT. lo talin peulat sakhir itkha ad boqer ("the
WAGE of a hired man shall not stay-the-night with you until
morning") - the lodge-verb lin (3885, tok 18/31), Sodom's and
Jacob's night-verb, negated onto money; peulat ("wage") lives
its whole Torah life in this clause [VERIFIED: 6468 1/1;
CROWN 6]; sakhir ("hired man", 7916, tok 3/10) - Deut 24:14-15
will re-legislate the same night with the sun as the clock.
STATUTES 17."""),
  ],
  comment="The wage is minted its own noun and forbidden to sleep."),

 dict(ref=(19,14), op="THE_DEAF_AND_THE_BLIND",
  en="You shall not curse the deaf, and before the blind you shall not put a stumbling-block; and you shall fear your God: I am the LORD.",
  tl_en="do not curse the deaf; no stumbling-block before the blind",
  tr_en="and you shall fear your God: I am the LORD",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(teqalel_cheresh)",
    frag=("lo",3), prose="""
THE MAKER PROTECTS WHAT HE MADE. lo teqalel cheresh ("you shall
not curse the DEAF") - cheresh has exactly TWO Torah tokens
[VERIFIED: 2795 2/2 - career opens and closes on this pair]:
Exod 4:11 - mi yasum... o cheresh, God's own claim at the bush
to have MADE the deaf - and this ban: the man who cannot hear
the curse is cursed only before the God who made him deaf.
qalal (7043, tok 10/17): tok 4 is Gen 12:3's u-meqalelkha aor
- the curse-verb of the covenant's own warranty. STATUTES
18."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(mikhshol_li_fene_iver)",
    frag=("ve-li-fene",5), prose="""
THE STUMBLING-BLOCK. ve-li-fene iver lo titen mikhshol ("and
before the BLIND you shall not put a stumbling-block") -
mikhshol lives its entire Torah life in this clause [VERIFIED:
4383 1/1; CROWN 6]; iver ("the blind", 5787, tok 2/6) rides
the same Exod 4:11 verse as the deaf - the pair the law
protects is the pair the Maker claimed. STATUTES 19."""),
   dict(op="STATUTE",
    expr="STATUTE BIND(ve_yareta_me_elohekha)",
    frag=("ve-yareta",2), prose="""
FEAR AS ENFORCEMENT [CROWN 10]. ve-yareta me-elohekha ("and
you shall FEAR your God") - the clause occurs five times in
the Torah, all in Leviticus [VERIFIED: 19:14, 19:32, 25:17,
25:36, 25:43], and it attaches precisely to the wrongs no
victim can report: the deaf man never heard, the blind man
never saw who tripped him - where no court can see, the
statute installs fear. SEAL S2: ani YHWH. STATUTES 20."""),
  ],
  comment="Invisible wrongs get an invisible witness."),

 dict(ref=(19,15), op="NO_FACES_IN_COURT",
  en="You shall do no wrong in judgment; you shall not lift the face of the poor and you shall not favor the face of the great; in righteousness shall you judge your fellow.",
  tl_en="no wrong in judgment: lift no poor face, favor no great face",
  tr_en="in righteousness shall you judge your fellow",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(avel_ba_mishpat)",
    frag=("lo",4), prose="""
THE CLAUSE THAT WILL RETURN [CROWN 3a]. lo taasu avel
ba-mishpat ("you shall do no WRONG in JUDGMENT") - four tokens
that recur letter-identical at 19:35 over weights and measures
[VERIFIED: he_plain identity]: one formula, courtroom then
marketplace. avel ("wrong", 5766) DEBUTS - 1/4, both in-span
tokens are this formula's two firings. STATUTES 21."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(tisa_fene_dal)",
    frag=("lo",4,2), prose="""
NO LIFTED FACES - NOT EVEN THE POOR MAN'S. lo tisa fene dal
("you shall not LIFT the face of the POOR") - the court may
not tilt even toward mercy; dal ("the poor", 1800, tok 4/4 -
career CLOSES: Exod 23:3 lo tehdar be-rivo, Exod 30:15, Lev
14:21, here). STATUTES 22."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(tehdar_pene_gadol)",
    frag=("ve-lo",4), prose="""
THE HADAR BAN - FIRST HALF OF THE REVERSAL [CROWN 5]. ve-lo
tehdar pene gadol ("and you shall not FAVOR the face of the
GREAT") - the honor-verb hadar has three Torah tokens: Exod
23:3 (the poor man's case), here (the great man's face), and
19:32 - where the SAME verb will be COMMANDED before the face
of the aged: banned at court, bound before grey hair, the
whole career inside two chapters of law [VERIFIED: 1921
census]. STATUTES 23."""),
   dict(op="STATUTE",
    expr="STATUTE BIND(be_tzedeq_tishpot_amitekha)",
    frag=("be-tzedeq",3), prose="""
TZEDEQ DEBUTS [CROWN 9]. be-tzedeq tishpot amitekha ("in
RIGHTEOUSNESS shall you judge your fellow") - the
righteousness-noun tzedeq enters the Torah HERE (6664, 1/12)
and takes its next four tokens in 19:36's scales; the
judge-verb shafat (8199, tok 14/27) carries gen_32's and
gen_54's careers behind it (16:5 yishpot YHWH; 31:53 yishptu).
amit again - the Leviticus-only fellow. STATUTES 24."""),
  ],
  comment="Justice may not look at faces - either face."),

 dict(ref=(19,16), op="TALEBEARER_AND_BYSTANDER",
  en="You shall not go about as a talebearer among your people; you shall not stand upon the blood of your neighbor: I am the LORD.",
  tl_en="you shall not go talebearing among your people",
  tr_en="you shall not stand on your neighbor's blood: I am the LORD",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(telekh_rakhil_be_amekha)",
    frag=("lo",4), prose="""
THE TALEBEARER - A HAPAX OFFICE. lo telekh rakhil be-amekha
("you shall not GO ABOUT as a TALEBEARER among your people") -
rakhil lives its entire Torah life here [VERIFIED: 7400 1/1;
CROWN 6]: the gossip-trade is named once, banned once, and
never mentioned again. STATUTES 25."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(taamod_al_dam_reekha)",
    frag=("lo",5,2), prose="""
DO NOT STAND ON YOUR NEIGHBOR'S BLOOD. lo taamod al dam reekha
("you shall not STAND upon the BLOOD of your neighbor") - dam
(1818, tok 120/166): the blood-noun whose career opened with
Abel's crying bloods (Gen 4:10, deme achikha) here forbids the
BYSTANDER - the second rea-clause. SEAL S3: ani YHWH. STATUTES
26."""),
  ],
  comment="The tongue that walks and the feet that stand still: both banned."),

 dict(ref=(19,17), op="THE_REPROVE_DOUBLING",
  en="You shall not hate your brother in your heart; you shall surely reprove your fellow, and not bear sin upon him.",
  tl_en="you shall not hate your brother in your heart",
  tr_en="surely reprove your fellow, and bear no sin upon him",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(tisna_et_achikha_bi_levavekha)",
    frag=("lo",5), prose="""
HATRED MOVES INDOORS. lo tisna et achikha bi-levavekha ("you
shall not HATE your brother IN YOUR HEART") - the law reaches
where no court can: the heart (levav, 3824, tok 5/55) as the
crime scene; sane (8130, tok 12/34) - the hate-verb of Esau's
grudge (27:41's sitnah-family) and Joseph's brothers ahead.
STATUTES 27."""),
   dict(op="STATUTE",
    expr="STATUTE BIND(hokheach_tokhiach_et_amitekha)",
    frag=("hokhecha",4), prose="""
THE REPROVE-VERB'S LAST TOKENS [CROWN 7c]. hokheach tokhiach
et amitekha ("you shall SURELY REPROVE your fellow" - Vha +
Vhi2ms, the infinitive-absolute doubling: mot-tamut's emphatic
construction on the duty to speak): yakhach's 8-token career
CLOSES here [VERIFIED: 3198 toks 7-8/8], and its previous two
tokens are frozen gen_54's tribunal - 31:37's ve-yokhichu
(Jacob demanding the kinsmen JUDGE between the two of them)
and 31:42's va-yokhach (God REPROVING Laban in the night):
Laban's court, God's verdict, then the standing duty of every
fellow to every fellow. Third amit. STATUTES 28."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(tisa_alav_chet)",
    frag=("ve-lo",4), prose="""
AND CARRY NO SIN FOR HIM. ve-lo tisa alav chet ("and you shall
not BEAR SIN upon him") - silence before a wrong makes the
silent one a carrier: chet (2399, tok 2/17) with the
bear-verb nasa (tok 95/168, third in-span firing after 19:8's
iniquity and 19:15's faces). STATUTES 29."""),
  ],
  comment="Hate silently and the sin transfers; reprove aloud and it does not."),

 dict(ref=(19,18), op="THE_LOVE_COMMAND",
  en="You shall not avenge and you shall not keep a grudge against the sons of your people; and you shall love your neighbor as yourself: I am the LORD.",
  tl_en="no vengeance, no grudge against the sons of your people",
  tr_en="and you shall love your neighbor as yourself: I am the LORD",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(tiqom)",
    frag=("lo",2), prose="""
NO VENGEANCE. lo tiqom ("you shall not AVENGE") - naqam
(5358, tok 6/9): the venge-root's first tokens are Gen 4:15
and 4:24 - Cain's sevenfold and Lamekh's seventy-seven: the
escalation-arithmetic of Genesis is what the statute shuts
off. STATUTES 30."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(titor_et_bene_amekha)",
    frag=("ve-lo",5), prose="""
THE GRUDGE-VERB EXISTS FOR THIS BAN. ve-lo titor et bene
amekha ("and you shall not KEEP A GRUDGE against the sons of
your people") - natar lives its entire Torah life in this
clause [VERIFIED: 5201 1/1; CROWN 6]: the Torah names
grudge-keeping exactly once - to forbid it. STATUTES 31."""),
   dict(op="STATUTE",
    expr="STATUTE BIND(ve_ahavta_le_reakha_kamokha)",
    frag=("ve-ahavta",3), prose="""
THE FIRST OF THE FOUR [CROWN 2]. ve-ahavta le-reakha kamokha
("and you shall LOVE your NEIGHBOR as YOURSELF") - the
weqatal love-command has exactly FOUR Torah tokens [VERIFIED:
census]: this verse (the neighbor), 19:34 (the stranger),
Deut 6:5 and 11:1 (God). Both human-object loves are this
chapter's; ahav's prior career opened at Gen 22:2 (asher
ahavta - Isaac) and ran through the family's loves and
favoritisms - now it becomes a statute with kamokha ("as
yourself", 3644, tok 19/28) as its measure. The third
rea-clause: oppressed (13), bled (16), LOVED (18). SEAL S4:
ani YHWH - the bare Name signs the love command. STATUTES
32."""),
  ],
  comment="Vengeance and grudge cleared out; love installed in the space they leave."),

 dict(ref=(19,19), op="THE_MIXTURES",
  en="My statutes you shall keep: your beast you shall not mate in two kinds; your field you shall not sow in two kinds; and a garment of two kinds, shaatnez, shall not come upon you.",
  tl_en="My statutes you shall keep: no mixed mating of your beast",
  tr_en="no mixed sowing of your field; no shaatnez garment upon you",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE BIND(et_chuqotay_tishmoru)",
    frag=("et",3), prose="""
THE MID-CHAPTER HEADER. et chuqotay tishmoru ("MY STATUTES you
shall keep") - the code names its own genre mid-stream: chuqot
(2708, tok 21/56, and tok 22 is 19:37's closer) - the
statute-noun bracketing its own statutes; the keep-verb shamar
fires its second of four in-span tokens [VERIFIED: 8104 toks
46-49/148 = 19:3, 19, 30, 37]. STATUTES 33."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(tarbia_behemtekha_kilayim)",
    frag=("behemt-kha",3), prose="""
NO MIXED BREEDING. behemtekha lo tarbia kilayim ("your BEAST
you shall not mate in TWO-KINDS") - the mate-verb rava (7250,
tok 2/3; its other tokens are Lev 18:23 and 20:16's
bestiality laws); kilayim ("two-kinds") holds THREE of its
four Torah tokens in this one verse [VERIFIED: 3610 3/4; the
fourth is Deut 22:9]. STATUTES 34."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(tizra_sadkha_kilayim)",
    frag=("sad-kha",4), prose="""
NO MIXED SOWING. sadkha lo tizra kilayim ("your FIELD you
shall not sow in two-kinds") - zara (2232, tok 11/23): the
sow-verb of Gen 1:11-12's each-after-its-kind vegetation:
the creation taxonomy becomes agricultural law. STATUTES
35."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(beged_kilayim_shaatnez)",
    frag=("u-veged",6), prose="""
SHAATNEZ. u-veged kilayim shaatnez lo yaale alekha ("and a
garment of two-kinds, SHAATNEZ, shall not come upon you") -
shaatnez (8162) DEBUTS: 1/2, and its only other token, Deut
22:11, is the verse that DEFINES it (wool-and-linen together)
[VERIFIED: 2/2]: the code bans the word here and glosses it
one book later. The clause's verb is yaale ("shall not COME
UP upon you") - the ascend-verb as a garment's motion.
STATUTES 36."""),
  ],
  comment="Kinds keep their borders: beast, field, garment."),

 dict(ref=(19,20), op="THE_INQUEST_CASE",
  en="And a man who lies carnally with a woman who is a slave designated for a man, and she has not at all been redeemed nor freedom given her - there shall be an inquest; they shall not be put to death, for she was not freed.",
  tl_en="a man lies with a slave-woman designated for a man, unredeemed, unfreed",
  tr_en="an inquest there shall be; they shall not die, for she was not freed",
  ops=[
   dict(op="CASE",
    expr="CASE(ish_ve_shifcha_necherefet, yishkav_shikhvat_zera) ROUTE(biqoret_tihye)",
    frag=("ve-ish",11), prose="""
THE CASE THAT SPEAKS IN HAPAXES [CROWN 6]. ve-ish ki yishkav
("and a man WHEN he lies...") - the ki-case re-types again -
et isha ve-hiv shifcha NECHEREFET le-ish ("with a woman who is
a slave DESIGNATED for a man") ve-hafde lo nifdata o CHUFSHA
lo nitan lah ("and she has not at all been redeemed" - VHa +
VNp3fs, a third infinitive-absolute doubling, this one on the
redemption-verb - "nor FREEDOM given her"): the disposition -
BIQORET tihye ("an INQUEST there shall be"), lo yumtu ("they
shall NOT be put to death"), ki lo CHUPASHA ("for she was not
FREED"). FOUR words in this one verse live their whole Torah
life here: necherefet, chufsha, biqoret, chupasha [VERIFIED:
2778/2668/1244/2666 all 1/1; corpus max is six hapaxes in a
verse, Gen 36:39 - a fact, not a record]: the case where
status is ambiguous gets a vocabulary used for nothing else,
and the machine's routing is an INQUEST where every parallel
adultery case routes to death - the letter carves the
exception in words it never reuses. CASES 2. STATUTES still
36."""),
  ],
  comment="Ambiguous status, unique vocabulary, and death explicitly withheld."),

 dict(ref=(19,21), op="THE_ASHAM_ROUTE",
  en="And he shall bring his guilt-offering to the LORD to the entrance of the tent of meeting: a ram of guilt-offering.",
  tl_en="he brings his guilt-offering to the LORD",
  tr_en="to the tent of meeting's entrance: a ram of guilt",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(necherefet_case) THEN(ve_hevi_ashamo_el_petach_ohel_moed)",
    frag=("ve-hevi",8), prose="""
THE ONLY CULT GEOGRAPHY IN THE CHAPTER. ve-hevi et ashamo
la-YHWH el petach ohel moed ("and he shall BRING his
GUILT-OFFERING to the LORD, to the ENTRANCE of the TENT OF
MEETING") - the chapter's fifty-six statutes name no place at
all; only this case walks somewhere: asham (817, toks
26-27/33) - the guilt-offering of Lev 5's ladder - and the
petach ohel moed formula (6607/168/4150) whose tokens
cluster in Lev 17's centralization law. eil asham ("a RAM of
guilt") - the fixed tariff. HANDLERS 4."""),
  ],
  comment="The one road in the chapter leads to the tent's entrance."),

 dict(ref=(19,22), op="ATONED_AND_FORGIVEN",
  en="And the priest shall make atonement for him with the ram of the guilt-offering before the LORD for his sin which he has sinned; and he shall be forgiven of his sin which he has sinned.",
  tl_en="the priest atones for him with the guilt-ram before the LORD",
  tr_en="and he is forgiven of his sin which he sinned",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(el_ha_asham) THEN(ve_khiper_ha_kohen ∧ ve_nislach_lo)",
    frag=("ve-khiper",7), prose="""
THE FORGIVENESS CHAIN REACHES CHAPTER 19. ve-khiper alav
ha-kohen ("and the PRIEST shall make ATONEMENT for him") -
the priest's only appearance in-span (3548, tok 188/295); the
atone-verb kipper (3722, tok 59/79); ve-nislach lo ("and he
shall be FORGIVEN") - nislach (5545, tok 11/20): tokens 2-10
are Lev 4-5's ninefold refrain over the chatat and asham
ladders - the forgiveness-verb's machine, running once inside
the holiness code. chata doubled in the verse (me-chatato
asher chata, "of his sin which he sinned", x2 [VERIFIED:
token map]). HANDLERS 5."""),
  ],
  comment="The Lev 4-5 forgiveness engine fires once in the holiness code."),

 dict(ref=(19,23), op="THE_ORCHARD_CLOCK",
  en="And when you come into the land and plant any tree for food, you shall treat its fruit as its foreskin; three years it shall be to you as uncircumcised - it shall not be eaten.",
  tl_en="when you come into the land and plant any food tree",
  tr_en="its fruit is foreskin: three years uncircumcised, not eaten",
  ops=[
   dict(op="CASE",
    expr="CASE(bene_yisrael, tavou_el_ha_aretz_u_netatem_kal_etz) ROUTE(orlat_piryo)",
    frag=("ve-ki",8), prose="""
THE LAND-ENTRY CASE. ve-khi tavou el ha-aretz ("and WHEN you
COME into the land" - the code legislating for a land not yet
entered: the case-frame's horizon is the conquest)
u-netatem kal etz maakhal ("and plant any tree for FOOD") -
maakhal (3978, tok 5/7): the food-tree noun of Gen 2:9 and
3:6 (etz... le-maakhal - Eden's tree-grammar re-run as
orchard law). CASES 3."""),
   dict(op="HANDLER",
    expr="HANDLER IF(shalosh_shanim) THEN(arelim_lo_yeakhel)",
    frag=("va-araltem",4,1), prose="""
CIRCUMCISION GRAMMAR ON TREES. va-araltem arlato et piryo
("you shall treat-as-FORESKIN its foreskin - its fruit") -
the verb arel exists in the Torah only here [VERIFIED: 6188
1/1; CROWN 6], denominated on the spot from arlah
("foreskin", 6190, tok 9/10) - whose career is Gen 17's
covenant chapter (toks 1-5), Zipporah's flint (Exod 4:25),
and Deut 10:16's heart: the covenant-mark noun applied to
orchards, with a bounded clock: shalosh shanim yihye lakhem
arelim ("three years it shall be to you as uncircumcised")
lo yeakhel ("it shall not be eaten"). HANDLERS 6."""),
  ],
  comment="The tree is uncircumcised until year three: covenant grammar as horticulture."),

 dict(ref=(19,24), op="YEAR_FOUR_IS_PRAISE",
  en="And in the fourth year all its fruit shall be holy, praise-fruit to the LORD.",
  tl_en="in the fourth year all its fruit",
  tr_en="holy - praise-fruit to the LORD",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(ba_shana_ha_reviit) THEN(qodesh_hilulim_la_YHWH)",
    frag=("u-va-shana",8), prose="""
THE PRAISE-FRUIT. u-va-shana ha-reviit yihye kal piryo qodesh
HILULIM la-YHWH ("and in the FOURTH year all its fruit shall
be HOLY - praise-fruit to the LORD") - hilulim lives its
whole Torah life in this clause [VERIFIED: 1974 1/1; CROWN
6]: the fourth year's crop is named with a word the Torah
never needs again; qodesh - the thesis-root's noun on the
orchard (6944, tok 116/221). HANDLERS 7."""),
  ],
  comment="One year of the orchard is the LORD's, and it has its own noun."),

 dict(ref=(19,25), op="YEAR_FIVE_AND_THE_INCREASE",
  en="And in the fifth year you shall eat its fruit, to add its yield to you: I am the LORD your God.",
  tl_en="in the fifth year you shall eat its fruit",
  tr_en="to add its yield to you: I am the LORD your God",
  ops=[
   dict(op="HANDLER",
    expr="HANDLER IF(ba_shana_ha_chamishit) THEN(tokhlu_et_piryo ∧ le_hosif_tevuato)",
    frag=("u-va-shana",8), prose="""
THE CLOCK PAYS OUT. u-va-shana ha-chamishit tokhlu et piryo
("and in the FIFTH year you shall EAT its fruit") le-hosif
lakhem tevuato ("TO ADD its yield to you") - the only
yield-promise in the chapter: the add-verb yasaf (3254, tok
26/58) makes waiting itself the mechanism of increase;
tevua ("yield", 8393, tok 3/21 - the noun's career runs
into Lev 25's sabbath-year arithmetic, the probe's third
block). SEAL L5: ani YHWH elohekhem - the seal returns
after six statute-verses of bare-Name signing. HANDLERS 8.
CASES/HANDLERS complete: 3 cases so far + this chain."""),
  ],
  comment="Three years closed, one year holy, then the orchard opens with interest."),

 dict(ref=(19,26), op="BLOOD_AND_OMENS",
  en="You shall not eat upon the blood; you shall not read omens and you shall not tell fortunes.",
  tl_en="you shall not eat upon the blood",
  tr_en="no omen-reading, no fortune-telling",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(tokhlu_al_ha_dam)",
    frag=("lo",4), prose="""
NOT UPON THE BLOOD. lo tokhlu al ha-dam ("you shall not EAT
upon the BLOOD") - dam's second in-span token; the eat-verb's
seventh and last in-span firing (398 census) - the chapter's
eating-law cluster (pigul window, orlah clock, blood) closes
here. STATUTES 37."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(tenachashu)",
    frag=("lo",2,2), prose="""
LABAN'S VERB IS BANNED [CROWN 7a]. lo tenachashu ("you shall
not READ OMENS") - nachash the divination-verb (5172, tok
6/7) DEBUTED in Laban's mouth at Gen 30:27 (nichashti, "I
have DIVINED that the LORD blessed me for your sake" -
frozen gen_52's find, its watchlist arm landing here); toks
2-5 are Joseph's cup (44:5, 44:15 - each verse doubling the
verb); tok 7 is Deut 18:10's ban-list: the verb's whole
career is two diviners and two prohibitions. STATUTES 38."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(teonenu)",
    frag=("ve-lo",2), prose="""
NO FORTUNE-TELLING. ve-lo teonenu ("and you shall not TELL
FORTUNES") - anan (6049, tok 2/4): tok1 is Gen 9:14's cloud
homograph-root; the practice-tokens are here and Deut
18:10/14's list - the pair-ban (omens + fortunes) travels
to Deuteronomy intact. STATUTES 39."""),
  ],
  comment="The table and the future both closed to pagan technique."),

 dict(ref=(19,27), op="THE_CORNER_MOVES_TO_THE_HEAD",
  en="You shall not round off the corner of your head, and you shall not destroy the corner of your beard.",
  tl_en="do not round the corner of your head",
  tr_en="do not destroy the corner of your beard",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(taqifu_peat_roshkhem)",
    frag=("lo",4), prose="""
PEA AGAIN - FIELD TO HEAD. lo taqifu peat roshkhem ("you
shall not ROUND OFF the corner of your HEAD") - the
round-off verb naqaf lives its whole Torah life here
[VERIFIED: 5362 1/1; CROWN 6], and its object is PEA - the
same corner-noun the harvest law left standing at 19:9
(6285, toks 18-19/27 here): the chapter runs one noun from
sanctuary walls to field edges to the human head. STATUTES
40."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(tashchit_peat_zeqanekha)",
    frag=("ve-lo",5), prose="""
THE FLOOD-VERB ON A BEARD. ve-lo tashchit et peat zeqanekha
("and you shall not DESTROY the corner of your BEARD") -
shachat (7843, tok 22/34): the destroy-verb of Gen 6's
flood-decree (va-tishachet ha-aretz... hineni mashchitam)
scaled down to a razor; zaqan ("beard", 2206, tok 4/5 -
a Leviticus-only noun but for none: all five tokens are Lev
[VERIFIED: career list 13:29-21:5]). STATUTES 41."""),
  ],
  comment="The body gets field-law: corners left uncut."),

 dict(ref=(19,28), op="THE_TATTOO_PAIR",
  en="And a cut for the dead you shall not make in your flesh, and writing of tattoo you shall not put in you: I am the LORD.",
  tl_en="no cut for the dead in your flesh",
  tr_en="no tattoo-writing put in you: I am the LORD",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(seret_la_nefesh_bi_vesarkhem)",
    frag=("ve-seret",5), prose="""
NO CUT FOR THE DEAD. ve-seret la-nefesh lo titnu
bi-vesarkhem ("and a CUT for the DEAD you shall not make in
your FLESH") - seret (8296, 1/2; its only other token is
21:5's priest-law); la-nefesh - the soul-noun as "the dead"
(5315, tok 96/205); basar - Gen 2:21's flesh as the
forbidden writing surface. STATUTES 42."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(ketovet_qaaqa)",
    frag=("u-khetovet",5), prose="""
THE ONLY WRITING-NOUN THE TORAH BANS [CROWN 6]. u-khetovet
qaaqa lo titnu bakhem ("and WRITING of TATTOO you shall not
put in you") - BOTH nouns live their entire Torah life in
this clause [VERIFIED: 3793 1/1 + 7085 1/1]: ketovet is the
katav-root's only nominal token in the Torah - the corpus
that writes everything forbids exactly one kind of writing,
the kind cut into skin. SEAL S5: ani YHWH. STATUTES 43."""),
  ],
  comment="Grief may not carve, and skin is not a page."),

 dict(ref=(19,29), op="THE_DAUGHTER_AND_THE_LAND",
  en="Do not profane your daughter to make her a harlot, lest the land fall to harlotry and the land fill with depravity.",
  tl_en="do not profane your daughter to make her a harlot",
  tr_en="lest the land go harloting and fill with depravity",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(techalel_et_bitkha_le_haznotah)",
    frag=("el",5), prose="""
THE THIRD JUSSIVE - AND DINAH'S QUESTION ANSWERED IN LAW
[CROWN 7b]. el techalel et bitkha le-haznotah ("do NOT
profane your DAUGHTER to make her a harlot" - al + jussive
Vpj2ms, the third re-typed volitive): chalal's THIRD in-span
firing (thing 19:8, Name 19:12, daughter 19:29 - the
profane-verb's ascending ladder). zanah (2181, toks 8-9/20):
its tok1 is Gen 34:31 - frozen gen_57's closing question,
ha-khe-zona yaase et achotenu ("should he treat our sister
AS A HARLOT?") - the brothers' cry becomes the father's
statute; and tok18 is Deut 22:21's li-zenot, gen_57's
armed reunion verse: question, law, sanction - three units,
one root. Motive: ve-lo tizne ha-aretz u-mala ha-aretz zima
("lest the LAND go harloting and FILL with depravity") -
the land itself the subject of the harlot-verb; zima (2154,
tok 2/4; the depravity-noun's other tokens are Lev 18:17
and 20:14's incest laws). STATUTES 44."""),
  ],
  comment="Profane thing, Name, daughter: the verb climbs; the land answers."),

 dict(ref=(19,30), op="THE_CHIASM_CLOSES",
  en="My sabbaths you shall keep and My sanctuary you shall fear: I am the LORD.",
  tl_en="My sabbaths you shall keep",
  tr_en="My sanctuary you shall fear: I am the LORD",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE BIND(shabtotay_tishmoru_u_miqdashi_tirau)",
    frag=("et",5), prose="""
KEEP-THEN-FEAR [CROWN 4] - AND A VERSE THAT WILL RETURN
WHOLE [CROWN 3b]. et shabtotay tishmoru u-miqdashi tirau
("My SABBATHS you shall KEEP and My SANCTUARY you shall
FEAR") - 19:3's verb-pair crossed over: there FEAR(parents)
+ KEEP(sabbaths), here KEEP(sabbaths) + FEAR(sanctuary) -
the two duties trade verbs across the chapter, parents
traded for sanctuary (miqdash, 4720, tok 5/16). And this
verse recurs LETTER-IDENTICAL, all seven tokens including
the seal, at 26:2 [VERIFIED: he_plain identity] - the
holiness code's hinge re-used as the gate to the blessings
and curses. One compound statute (the verse is one breath).
SEAL S6: ani YHWH. STATUTES 45."""),
  ],
  comment="The 19:3 pair returns crossed, and the whole verse will be re-spoken at 26:2."),

 dict(ref=(19,31), op="THE_TURN_VERB_RETURNS",
  en="Do not turn to the ghost-mediums, and to the familiar spirits do not seek, to be defiled by them: I am the LORD your God.",
  tl_en="do not turn to the ghost-mediums",
  tr_en="do not seek the familiar spirits, to be defiled: I am the LORD your God",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(peno_el_ha_ovot)",
    frag=("el",6), prose="""
19:4'S OPENER RE-ISSUED [CROWN 8]. el tifnu el ha-ovot ("do
NOT turn to the GHOST-MEDIUMS") - the fourth re-typed
volitive: the turn-verb's second and last PLURAL jussive
token, the same three-word opener as 19:4 with mediums where
idols stood [VERIFIED: 6437 - the verb's only two 2mp jussives
are these two verses; its 2ms jussives are Moses' al-tefen
prayers, Num 16:15 / Deut 9:27]. ov (178) DEBUTS: 1/4; its career is 20:6,
20:27 (the medium put to death) and Deut 18:11's list.
STATUTES 46."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(baqesh_el_ha_yidonim)",
    frag=("el",4,3), prose="""
DO NOT SEEK THE KNOWERS. ve-el ha-yidonim el tevaqshu ("and
to the FAMILIAR SPIRITS do not SEEK" - the fifth volitive
token, jussive, re-typed) - yidoni (3049) DEBUTS 1/4, the
know-root's necromancy noun, always paired with ov in all
four tokens; le-tama va-hem ("to be DEFILED by them") - tame
(2930, tok 78/114): the defile-verb whose tok1 is Gen 34:5,
Dinah - frozen gen_57's purity-debut - here extended from
persons to seances. SEAL L6: ani YHWH elohekhem. STATUTES
47."""),
  ],
  comment="Idols at 19:4, ghosts at 19:31: one opener, both doors closed."),

 dict(ref=(19,32), op="RISE_BEFORE_GREY_HAIR",
  en="Before grey hair you shall rise, and you shall honor the face of the aged; and you shall fear your God: I am the LORD.",
  tl_en="before grey hair you shall rise",
  tr_en="honor the aged face, and fear your God: I am the LORD",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE BIND(mi_pene_seva_taqum)",
    frag=("mi-pene",3), prose="""
THE PATRIARCHS' WORD BECOMES A DUTY. mi-pene seva taqum
("before GREY HAIR you shall RISE") - seva (7872, tok 6/7):
its career is Abraham's promised good old age (15:15, 25:8)
and Jacob's grey hairs going down to Sheol (42:38, 44:29,
44:31 - the brothers' plea); the noun of the fathers' age
becomes the object of a standing duty: the body rises
(qum, 6965, tok 72/145). STATUTES 48."""),
   dict(op="STATUTE",
    expr="STATUTE BIND(ve_hadarta_pene_zaqen)",
    frag=("ve-hadarta",3), prose="""
THE HADAR REVERSAL COMPLETES [CROWN 5]. ve-hadarta pene
zaqen ("and you shall HONOR the face of the AGED") - the
same verb 19:15 banned toward the great-in-court is here
COMMANDED toward the old: hadar's three-token career (Exod
23:3, 19:15, 19:32) closes with FORBID twice and BIND once
- one root, both polarities, adjudicated by object.
STATUTES 49."""),
   dict(op="STATUTE",
    expr="STATUTE BIND(ve_yareta_me_elohekha)",
    frag=("ve-yareta",2), prose="""
THE ENFORCEMENT CLAUSE RE-SIGNS [CROWN 10]. ve-yareta
me-elohekha ("and you shall FEAR your God") - the second
in-span firing of the all-Leviticus clause (2 of 5;
25:17/36/43 ahead): who rises in an empty room, no court
sees - fear again posted where witnesses fail. The
register takes the same fact twice: the letter says it
twice, the machine writes it twice. SEAL S7: ani YHWH.
STATUTES 50."""),
  ],
  comment="Age gets the honor the court was denied."),

 dict(ref=(19,33), op="THE_GER_CASE",
  en="And when a stranger sojourns with you in your land, you shall not wrong him.",
  tl_en="when a stranger sojourns with you in your land",
  tr_en="you shall not wrong him",
  ops=[
   dict(op="CASE",
    expr="CASE(ger, yagur_itkha_be_artzkhem) ROUTE(mishpat_ha_ger)",
    frag=("ve-ki",5), prose="""
THE FOURTH CASE. ve-khi yagur itkha ger be-artzkhem ("and
WHEN a STRANGER sojourns WITH YOU in your land") - the
ki-frame on the sojourn-verb gur (1481, tok 20/37) whose
career is the patriarchs' own sojournings (Abram in Egypt,
Lot in Sodom, Gerar): the case-condition is Israel's
remembered condition. CASES 4."""),
   dict(op="STATUTE",
    expr="STATUTE FORBID(tonu_oto)",
    frag=("lo",3), prose="""
NO WRONGING. lo tonu oto ("you shall not WRONG him") -
yanah (3238, tok 2/5): tok1 is Exod 22:20 - ve-ger lo tone
("a stranger you shall not wrong, FOR YOU WERE STRANGERS in
the land of Egypt") - the same law with the same motive the
next verse will unpack; toks 3-4 are Lev 25:14/17 (wronging
in sale and in words). STATUTES 51."""),
  ],
  comment="The sojourner's case opens with Israel's own resume."),

 dict(ref=(19,34), op="THE_SECOND_LOVE",
  en="As a native among you shall the stranger who sojourns with you be to you, and you shall love him as yourself, for strangers you were in the land of Egypt: I am the LORD your God.",
  tl_en="as a native among you shall the sojourning stranger be",
  tr_en="love him as yourself, for you were strangers in Egypt: I am the LORD your God",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE BIND(ke_ezrach_mikem_yihye_lakhem)",
    frag=("ke-ezrach",7), prose="""
NATIVE-EQUAL. ke-ezrach mikem yihye lakhem ha-ger ha-gar
itkhem ("as a NATIVE among you shall the stranger who
sojourns with you be to you") - ezrach (249, tok 7/14): the
native-noun whose whole career is equal-law clauses (one
law for native and stranger: Exod 12:49, Lev 24:22, Num
15:29-30). STATUTES 52."""),
   dict(op="STATUTE",
    expr="STATUTE BIND(ve_ahavta_lo_kamokha)",
    frag=("ve-ahavta",3), prose="""
THE SECOND OF THE FOUR [CROWN 2]. ve-ahavta lo kamokha ("and
you shall LOVE him AS YOURSELF") - the love-command's second
Torah token, sixteen verses after the first: neighbor 19:18,
STRANGER here - the weqatal love-statute's only two
human-object tokens, both this chapter's, before Deuteronomy
turns the form on God (6:5, 11:1). Motive: ki gerim heyitem
be-eretz mitzrayim ("for STRANGERS you were in the land of
EGYPT") - Gen 15:13's prophecy-noun (ger yihye zarakha)
cited as the ground of empathy; mitzrayim tok 227/314. SEAL
L7: ani YHWH elohekhem. STATUTES 53."""),
  ],
  comment="The chapter's second love: the stranger, measured by the self."),

 dict(ref=(19,35), op="THE_FORMULA_RETURNS",
  en="You shall do no wrong in judgment - in measure, in weight, or in liquid-measure.",
  tl_en="you shall do no wrong in judgment",
  tr_en="in measure, in weight, in liquid-measure",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE FORBID(avel_ba_mishpat_ba_mida_ba_mishqal_u_va_mesura)",
    frag=("lo",7), prose="""
COURTROOM FORMULA, MARKETPLACE JURISDICTION [CROWN 3a]. lo
taasu avel ba-mishpat ("you shall do no WRONG in JUDGMENT")
- 19:15's four tokens LETTER-IDENTICAL [VERIFIED: he_plain]
- then the new docket: ba-mida ba-mishqal u-va-mesura ("in
MEASURE, in WEIGHT, in LIQUID-MEASURE") - mida (4060, tok
5/6: its first four tokens are the Mishkan's curtain
dimensions - sanctuary math becomes shop math); mesura
lives its whole Torah life here [VERIFIED: 4884 1/1; CROWN
6]; mishqal (4948, tok 4/17). The scales are a courtroom:
avel closes its in-span pair. STATUTES 54."""),
  ],
  comment="The same wrong, re-indicted at the counter."),

 dict(ref=(19,36), op="THE_JUST_KIT",
  en="Just scales, just weights, a just efah and a just hin shall you have: I am the LORD your God who brought you out of the land of Egypt.",
  tl_en="just scales, just weights, just efah, just hin",
  tr_en="I am the LORD your God who brought you out of Egypt",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE BIND(mozne_tzedeq_avne_tzedeq_efat_tzedeq_ve_hin_tzedeq)",
    frag=("mozne",10), prose="""
FOUR TZEDEQ IN ONE VERSE [CROWN 9]. mozne tzedeq avne tzedeq
efat tzedeq ve-hin tzedeq yihye lakhem ("JUST scales, JUST
weights, a JUST efah and a JUST hin shall you have") - the
righteousness-noun takes tokens 2-3-4-5 of its Torah career
in this single verse (after debuting at 19:15's court): the
noun's first five tokens are all this chapter's [VERIFIED:
6664 ordinals 1-5]. mozne ("scales") lives its whole Torah
life here [VERIFIED: 3976 1/1; CROWN 6]; even ("weight-
stone", 68, tok 54/88) - Bethel's pillow-stone lineage
weighed at the counter; efa and hin - the dry and liquid
standards. THE EXTENDED SEAL [CROWN 1]: ani YHWH elohekhem
ASHER HOTZETI etkhem me-eretz mitzrayim ("who BROUGHT YOU
OUT of the land of Egypt") - the only seal of the sixteen
that carries a clause: the exodus-verb (3318, tok 192/348)
signs the scales - the God of the going-out underwrites
honest weight. SEAL L8. STATUTES 55."""),
  ],
  comment="Sixteen seals, and only the scales get the exodus clause."),

 dict(ref=(19,37), op="THE_CLOSER",
  en="And you shall keep all My statutes and all My judgments, and do them: I am the LORD.",
  tl_en="keep all My statutes and all My judgments",
  tr_en="and do them: I am the LORD",
  ops=[
   dict(op="STATUTE",
    expr="STATUTE BIND(u_shemartem_kal_chuqotay_ve_kal_mishpatay_va_asitem)",
    frag=("u-shemartem",9), prose="""
THE WALL [UNIT SHAPE]. u-shemartem et kal chuqotay ve-et kal
mishpatay va-asitem otam ("and you shall KEEP ALL My
statutes and ALL My judgments, and DO them") - the closing
statute quantifies over the whole register: chuqot and
mishpat side by side (2708 tok 22/56; 4941 tok 22/84), the
keep-verb's fourth in-span firing, the do-verb's last. And
the final seal is BARE [CROWN 1]: ani YHWH - the chapter
that opened with elohekhem's full formula closes on the
two-word Name, the eighth short seal of the eight. UNIT
END: SPECS depth 1 OPEN (the relay card - Moses' speaking
never narrated); STATUTES 56 standing (39 FORBID + 17
BIND); CASES 4; HANDLERS 8; REGISTRY 0 [VERIFIED: zero
qara-lemma tokens]; TESTS 0 [VERIFIED: zero tov-adjective
tokens]. The narrative machine held one card while a new
register did all the work: the probe's answer. STATUTES
56."""),
  ],
  comment="All of them, kept and done: the ledger closes under one open card."),
]

# ---------------------------------------------------------------------------

def _s(id, ref, frag, title, given, expect, occ=1):
    d = dict(id=id, ref=ref, frag=frag, title=title, given=given, expect=expect)
    d["occ"] = occ
    return d

DB = "LET(daber_el_kal_adat(moshe)) pushed and OPEN;"
NTN = "no test, no name."

SCENS = [
 _s("S1", (19,1), ("va-yedaber",5),
    "after STEP_Lv_19_1 — the frame: one narrative verb, then silence",
    "The LORD spoke to Moses, saying.",
    ["SPECS empty;", NTN]),
 _s("S2", (19,2), ("qedoshim",7),
    "after STEP_Lv_19_2 — the relay card pushed; the thesis statute installs",
    "Speak to the whole congregation: holy shall you be.",
    [DB, "Facts statute-qedoshim HOLD;", "STATUTES 1 standing;", NTN]),
 _s("S3", (19,3), ("ish",4),
    "after STEP_Lv_19_3 — mother-first fear, sabbaths kept; statutes 3",
    "Each man shall fear his mother and father; keep My sabbaths.",
    [DB, "Facts statute-shabtotay HOLD;", "STATUTES 3 standing;", NTN]),
 _s("S4", (19,4), ("el",4),
    "after STEP_Lv_19_4 — the re-typing witness: jussive and imperfect one list; statutes 5",
    "Turn not to idols; molten gods make not.",
    [DB, "Facts statute-masekha HOLD;", "STATUTES 5 standing;", NTN]),
 _s("S5", (19,5), ("ve-ki",7),
    "after STEP_Lv_19_5 — the shelamim case opens; statutes hold at 5",
    "When you sacrifice a well-being offering, for your acceptance.",
    [DB, "Facts case-shelamim HOLD;", "STATUTES 5 standing;", NTN]),
 _s("S6", (19,6), ("be-yom",10),
    "after STEP_Lv_19_6 — the two-day window handler",
    "Eaten on the day and the morrow; the third day burns.",
    [DB, "Facts handler-yisaref HOLD;", "STATUTES 5 standing;", NTN]),
 _s("S7", (19,7), ("ve-im",9),
    "after STEP_Lv_19_7 — the pigul branch",
    "If eaten on the third day: foul, not accepted.",
    [DB, "Facts handler-pigul HOLD;", "STATUTES 5 standing;", NTN]),
 _s("S8", (19,8), ("ve-okhlay-v",12),
    "after STEP_Lv_19_8 — karet on the eater",
    "The eater bears iniquity; that soul is cut off.",
    [DB, "Facts handler-nikhrta HOLD;", "STATUTES 5 standing;", NTN]),
 _s("S9", (19,9), ("u-ve-qutzr-khem",9),
    "after STEP_Lv_19_9 — corner and gleaning left; statutes 7",
    "Finish not the corner; gather not the gleaning.",
    [DB, "Facts statute-peat HOLD;", "STATUTES 7 standing;", NTN]),
 _s("S10", (19,10), ("le-ani",4),
    "after STEP_Lv_19_10 — vineyard edges to the poor and the stranger; statutes 10",
    "Leave them for the poor and the stranger.",
    [DB, "Facts statute-taazov HOLD;", "STATUTES 10 standing;", NTN]),
 _s("S11", (19,11), ("lo",2),
    "after STEP_Lv_19_11 — steal, deny, lie: the plural triad; statutes 13",
    "You shall not steal, deny, or lie to your fellow.",
    [DB, "Facts statute-tignovu HOLD;", "STATUTES 13 standing;", NTN]),
 _s("S12", (19,12), ("ve-lo",4),
    "after STEP_Lv_19_12 — the false-oath ban; the first bare seal; statutes 14",
    "Swear not falsely by My name.",
    [DB, "Facts statute-tishavu HOLD;", "STATUTES 14 standing;", NTN]),
 _s("S13", (19,13), ("lo",7),
    "after STEP_Lv_19_13 — oppression, robbery, the sleeping wage; statutes 17",
    "The hired man's wage shall not sleep with you.",
    [DB, "Facts statute-talin HOLD;", "STATUTES 17 standing;", NTN], 2),
 _s("S14", (19,14), ("ve-li-fene",5),
    "after STEP_Lv_19_14 — deaf, blind, and the fear-clause; statutes 20",
    "Curse not the deaf; stumble not the blind; fear your God.",
    [DB, "Facts statute-mikhshol HOLD;", "STATUTES 20 standing;", NTN]),
 _s("S15", (19,15), ("be-tzedeq",3),
    "after STEP_Lv_19_15 — no faces in court; tzedeq debuts; statutes 24",
    "In righteousness shall you judge your fellow.",
    [DB, "Facts statute-tishpot HOLD;", "STATUTES 24 standing;", NTN]),
 _s("S16", (19,16), ("lo",4),
    "after STEP_Lv_19_16 — talebearer and bystander; statutes 26",
    "Go not talebearing; stand not on your neighbor's blood.",
    [DB, "Facts statute-rakhil HOLD;", "STATUTES 26 standing;", NTN]),
 _s("S17", (19,17), ("hokhecha",4),
    "after STEP_Lv_19_17 — heart-hatred banned, reproof bound; statutes 29",
    "Hate not in your heart; surely reprove your fellow.",
    [DB, "Facts statute-tokhiach HOLD;", "STATUTES 29 standing;", NTN]),
 _s("S18", (19,18), ("ve-ahavta",3),
    "after STEP_Lv_19_18 — the love command; statutes 32",
    "Love your neighbor as yourself.",
    [DB, "Facts statute-reakha HOLD;", "STATUTES 32 standing;", NTN]),
 _s("S19", (19,19), ("u-veged",6),
    "after STEP_Lv_19_19 — the mixtures: beast, field, garment; statutes 36",
    "My statutes keep: no two-kinds mating, sowing, or shaatnez.",
    [DB, "Facts statute-kilayim HOLD;", "STATUTES 36 standing;", NTN]),
 _s("S20", (19,20), ("biqoret",5),
    "after STEP_Lv_19_20 — the inquest case: four hapaxes, death withheld",
    "An inquest there shall be; they shall not die.",
    [DB, "Facts case-necherefet HOLD;", "STATUTES 36 standing;", NTN]),
 _s("S21", (19,21), ("ve-hevi",8),
    "after STEP_Lv_19_21 — the asham route to the tent",
    "He brings his guilt-offering to the tent of meeting.",
    [DB, "Facts handler-ashamo HOLD;", "STATUTES 36 standing;", NTN]),
 _s("S22", (19,22), ("ve-khiper",7),
    "after STEP_Lv_19_22 — atoned and forgiven",
    "The priest atones; he is forgiven.",
    [DB, "Facts handler-nislach HOLD;", "STATUTES 36 standing;", NTN]),
 _s("S23", (19,23), ("va-araltem",4),
    "after STEP_Lv_19_23 — the orchard case: three uncircumcised years",
    "When you enter the land and plant: its fruit is foreskin.",
    [DB, "Facts case-orlat HOLD;", "Facts handler-arelim HOLD;", "STATUTES 36 standing;", NTN]),
 _s("S24", (19,24), ("u-va-shana",8),
    "after STEP_Lv_19_24 — year four: praise-fruit",
    "In the fourth year, holy - praise-fruit to the LORD.",
    [DB, "Facts handler-hilulim HOLD;", "STATUTES 36 standing;", NTN]),
 _s("S25", (19,25), ("u-va-shana",8),
    "after STEP_Lv_19_25 — year five: eat, and the yield adds",
    "In the fifth year eat its fruit, to add its yield.",
    [DB, "Facts handler-tevuato HOLD;", "STATUTES 36 standing;", NTN]),
 _s("S26", (19,26), ("lo",4),
    "after STEP_Lv_19_26 — blood, omens, fortunes; statutes 39",
    "Eat not on the blood; no omens, no fortunes.",
    [DB, "Facts statute-tenachashu HOLD;", "STATUTES 39 standing;", NTN]),
 _s("S27", (19,27), ("lo",4),
    "after STEP_Lv_19_27 — head-corner and beard; statutes 41",
    "Round not the head's corner; destroy not the beard's.",
    [DB, "Facts statute-taqifu HOLD;", "STATUTES 41 standing;", NTN]),
 _s("S28", (19,28), ("u-khetovet",5),
    "after STEP_Lv_19_28 — the cut and the tattoo; statutes 43",
    "No cut for the dead; no tattoo-writing.",
    [DB, "Facts statute-qaaqa HOLD;", "STATUTES 43 standing;", NTN]),
 _s("S29", (19,29), ("el",5),
    "after STEP_Lv_19_29 — the daughter; the land's harlotry; statutes 44",
    "Profane not your daughter to make her a harlot.",
    [DB, "Facts statute-le_haznotah HOLD;", "STATUTES 44 standing;", NTN]),
 _s("S30", (19,30), ("et",5),
    "after STEP_Lv_19_30 — the chiasm closes; the 26:2 verse; statutes 45",
    "Keep My sabbaths, fear My sanctuary.",
    [DB, "Facts statute-miqdashi HOLD;", "STATUTES 45 standing;", NTN]),
 _s("S31", (19,31), ("el",6),
    "after STEP_Lv_19_31 — ghosts and familiar spirits; statutes 47",
    "Turn not to mediums; seek not the spirits.",
    [DB, "Facts statute-yidonim HOLD;", "STATUTES 47 standing;", NTN]),
 _s("S32", (19,32), ("mi-pene",3),
    "after STEP_Lv_19_32 — rise, honor, fear; statutes 50",
    "Before grey hair rise; honor the aged face.",
    [DB, "Facts statute-seva HOLD;", "STATUTES 50 standing;", NTN]),
 _s("S33", (19,33), ("ve-ki",5),
    "after STEP_Lv_19_33 — the stranger's case; statutes 51",
    "When a stranger sojourns with you, wrong him not.",
    [DB, "Facts case-yagur HOLD;", "Facts statute-tonu HOLD;", "STATUTES 51 standing;", NTN]),
 _s("S34", (19,34), ("ve-ahavta",3),
    "after STEP_Lv_19_34 — the second love: the stranger; statutes 53",
    "As a native shall he be; love him as yourself.",
    [DB, "Facts statute-ke_ezrach HOLD;", "STATUTES 53 standing;", NTN]),
 _s("S35", (19,35), ("lo",7),
    "after STEP_Lv_19_35 — the formula re-indicts the marketplace; statutes 54",
    "No wrong in judgment: measure, weight, liquid-measure.",
    [DB, "Facts statute-ba_mida HOLD;", "STATUTES 54 standing;", NTN]),
 _s("S36", (19,36), ("mozne",10),
    "after STEP_Lv_19_36 — the just kit; the exodus seal; statutes 55",
    "Just scales, weights, efah, hin: I brought you out of Egypt.",
    [DB, "Facts statute-mozne HOLD;", "STATUTES 55 standing;", NTN]),
 _s("S37", (19,37), ("u-shemartem",9),
    "after STEP_Lv_19_37 — the wall: 56 statutes under one open card",
    "Keep all My statutes and judgments, and do them.",
    [DB, "Facts statute-va_asitem HOLD;", "STATUTES 56 standing;", NTN]),
]
