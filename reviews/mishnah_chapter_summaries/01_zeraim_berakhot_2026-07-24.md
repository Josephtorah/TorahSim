# משנה ברכות / *Mishnah Berakhot* / “Blessings” — full tractate (9 chapters)

**Date:** 2026-07-24  
**Order:** Canonical Mishnah — **Seder Zeraim** tractate 1 (opens the entire Mishnah)  
**Corpus:** `Data/mishnah_berakhot_he.json` · **57** mishnayot  
**Lenses:** full-stack developer + Torah scholar  
**Limits:** ~100–180 words/chapter · dual-track Oral · not binding law  
**Hebrew first** + translit + English  

**Tractate job (one line):** Spec for daily **קְרִיאַת שְׁמַע / keri’at Shema / “recitation of the Shema”**, **תְּפִלָּה / tefillah / “prayer” (Amidah)**, and **בְּרָכוֹת / berakhot / “blessings”** over food, times, and world events.

---

### Chapter 1 · 5 mishnayot — Shema time windows & package

**Job:** When/how you run evening & morning Shema.

**Themes:** Start/end clocks (priests/terumah, color vision, sunrise, 3 hours); fence (**חֲצוֹת / ḥatzot / midnight** vs dawn); posture dispute Beit Shammai/Hillel; fixed berakhot counts; Exodus mention at night.

**Dev:** Feature `Shema.recite` — temporal gates, soft degrade (late = “like Torah”), immutable wrapper API, `kedei leharḥik` = UX deadline before hard deadline.

**Scholar:** Practice protocol around Deut 6/16; multi-opinion without yet merging Bavli; Gamliel story = case test.

**Standout:** **כְּדֵי לְהַרְחִיק אֶת הָאָדָם מִן הָעֲבֵרָה / kedei leharḥik et ha-adam min ha-averah / “to distance a person from sin”** (1:1).

---

### Chapter 2 · 8 mishnayot — Intention, interruptions, exemptions

**Job:** Valid performance: intent, breaks, volume, order; special persons.

**Themes:** **כִּוֵּן לִבּוֹ / kiven libo / “directed his heart”** (intent); break points between units; hear-to-ear / letter precision disputes; reverse order fails; craftsmen may read Shema up a tree (not Amidah); groom exempt first nights; Gamliel still reads (yoke of Heaven).

**Dev:** `intent` flag; interrupt policy by segment boundary; ordered pipeline of paragraphs; role-based `exempt` with override story.

**Scholar:** **עֹל מַלְכוּת שָׁמַיִם / ol malkhut shamayim / “yoke of the kingdom of Heaven”** before yoke of mitzvot (2:2) — theology inside sequencing.

**Standout:** **שֶׁיְּקַבֵּל עָלָיו עֹל מַלְכוּת שָׁמַיִם תְּחִלָּה / she-yekabel alav ol malkhut shamayim teḥillah / “so that he accept the yoke of Heaven first”** (2:2).

---

### Chapter 3 · 6 mishnayot — Death, purity, who is obligated

**Job:** Who is **פָּטוּר / patur / “exempt”** vs **חַיָּב / ḥayyav / “obligated”** under corpse-care and impurity.

**Themes:** Corpse before you → exempt Shema/tefillah/tefillin; bier carriers by need; women/slaves/minors matrix (exempt Shema/tefillin, obligated prayer/mezuzah/birkat hamazon); **בַּעַל קֶרִי / ba’al keri / “one with seminal emission”** — mental review vs full berakhot; immersion timing; zav/niddah edge cases.

**Dev:** Exemption matrix by role × state; funeral workflow suspends features; purity gate before blessing stack.

**Scholar:** Mourning and impurity as temporary deprioritization of speech-mitzvot; classic gender/obligation map (later law debates this surface).

**Standout:** **מִי שֶׁמֵּתוֹ מוּטָל לְפָנָיו, פָּטוּר… / mi she-meto mutal lefanav, patur… / “one whose dead lies before him is exempt…”** (3:1).

---

### Chapter 4 · 7 mishnayot — Amidah schedule & form

**Job:** **תְּפִלָּה / tefillah** daily slots and flexibility.

**Themes:** Morning until noon/4 hours; minchah until evening/plag; evening has no fixed time; musaf all day/7 hours; short prayer entering beit midrash; 18 blessings full vs “essence of 18”; don’t make prayer rote; danger short form; face **בֵּית קֹדֶשׁ הַקֳּדָשִׁים / beit kodesh ha-kodashim / “Holy of Holies”** when possible.

**Dev:** Cron windows per prayer type; degraded mode (short form); orientation = soft geolocation toward Temple; length policy vs fluency.

**Scholar:** Prayer as stand-in for service rhythm; orientation keeps destroyed Temple as spiritual endpoint.

**Standout:** **הָעוֹשֶׂה תְּפִלָּתוֹ קֶבַע, אֵין תְּפִלָּתוֹ תַּחֲנוּנִים / ha-oseh tefillato keva, ein tefillato taḥanunim / “one who makes his prayer fixed — his prayer is not supplication”** (4:4).

---

### Chapter 5 · 5 mishnayot — Prayer posture, inserts, errors

**Job:** How you stand in Amidah; seasonal inserts; bad formulas; shaliaḥ tzibbur.

**Themes:** **כֹּבֶד רֹאשׁ / koved rosh / “seriousness”** before prayer; even king/snake don’t interrupt; rain power in resurrection blessing; ask rain in years blessing; silence heretical/doubled formulas; replace mistaken prayer leader; Hanina b. Dosa — fluency as acceptance signal.

**Dev:** Precondition `seriousness`; seasonal feature flags in blessing slots; content filter on forbidden phrases; failover for failed celebrant; health-check “is prayer fluent?”

**Scholar:** Kavanah culture; boundary against theologically dangerous speech; wonder-worker as limit case of efficacy.

**Standout:** **אֲפִלּוּ נָחָשׁ כָּרוּךְ עַל עֲקֵבוֹ, לֹא יַפְסִיק / afilu naḥash karukh al akevo, lo yafsik / “even if a snake is wound around his heel, he does not interrupt”** (5:1).

---

### Chapter 6 · 8 mishnayot — Food blessings taxonomy

**Job:** Map food → correct **בְּרָכָה / berakhah** before (and some after).

**Themes:** Tree fruit / wine / earth produce / bread hierarchy; wrong berakhah sometimes still yotze; **שֶׁהַכֹּל / shehakol / “by whose word all exists”** fallback; primary vs secondary (**עִקָּר / ikkar** vs **טְפֵלָה / tefelah**); wine before meal covers after; shared vs individual when reclining.

**Dev:** Type hierarchy + fallback string; polymorphism (wrong parent type may still pass); coverage rules (bread covers sides); session “who blesses for the table.”

**Scholar:** Sanctifying ordinary eating; land/seven species gravity in after-blessings debate.

**Standout:** **כֹּל שֶׁהוּא עִקָּר וְעִמּוֹ טְפֵלָה, מְבָרֵךְ עַל הָעִקָּר וּפוֹטֵר אֶת הַטְּפֵלָה / kol shehu ikkar ve-imo tefelah… / “whatever is primary, and secondary with it — bless on the primary and exempt the secondary”** (6:7).

---

### Chapter 7 · 5 mishnayot — Zimun (invitation to grace)

**Job:** When a group must do communal after-blessing lead.

**Themes:** Three who ate together → **זִמּוּן / zimun**; who counts (demai yes, tevel no; cuthean yes, foreigner no); women/slaves/minors don’t form the quorum here; formula scales with 3 / 10 / 100 / 1000 / 10000; split rules; two groups if they can see each other; wine mixed with water dispute.

**Dev:** Quorum service; eligibility filters; string templates by N; merge/split group sessions by visibility.

**Scholar:** Table fellowship as mini-kehillah; language of blessing intensifies with public size (Ps 68 derashah).

**Standout:** **שְׁלשָׁה שֶׁאָכְלוּ כְאֶחָד, חַיָּבִין לְזַמֵּן / sheloshah she-akhlu ke-eḥad, ḥayyavin lezamen / “three who ate as one are obligated to invite [to grace]”** (7:1).

---

### Chapter 8 · 8 mishnayot — Meal order: Shammai vs Hillel

**Job:** Sequence bugs at the table (esp. Shabbat/havdalah edges).

**Themes:** Day vs wine first; netilat yadayim vs pouring cup; wipe hands where; sweep then wash vs reverse; havdalah order (lamp/spices/food); no berakhah on idolatrous/dead’s lamp; forgot birkat hamazon — return vs bless where you remember; amen after Israelite not Cuthean until full hearing.

**Dev:** Ordered pipeline disputes (A then B vs B then A); purity of inputs for berakhah; recovery path for forgotten after-blessing; trust filter on whose amen you answer.

**Scholar:** Classic House disputes as competing UX for holiness-in-meal; Hillel/Shammai as durable interface fork.

**Standout:** Chapter title theme — **אֵלּוּ דְּבָרִים שֶׁבֵּין בֵּית שַׁמַּאי וּבֵית הִלֵּל בַּסְּעֻדָּה / elu devarim she-bein Beit Shammai u-Veit Hillel ba-se’udah / “these are the matters between Beit Shammai and Beit Hillel at the meal”** (8:1).

---

### Chapter 9 · 5 mishnayot — Blessings on places, nature, news; love God

**Job:** Event-driven berakhot outside the meal/Shema stack; close with love-of-God totalism.

**Themes:** Miracle sites; uprooted idolatry; comets/quakes/lightning/thunder; mountains/seas as **מַעֲשֵׂה בְרֵאשִׁית / ma’aseh vereshit / “work of creation”**; good news vs bad news formulas; new house/vessels — **שֶׁהֶחֱיָנוּ / sheheḥeyanu**; vain prayer for past; enter/exit city prayers; bless on bad as on good (Deut 6:5); Temple mount decorum; seal change against minim (two worlds).

**Dev:** Event handlers for geo/nature/news; anti-pattern `vain_prayer` (past locked); symmetry API good/bad; sacred geofence rules on Har HaBayit.

**Scholar:** Whole-life berakhah piety; theodicy in one line (bless the bad); anti-heresy liturgy tweak; Shema’s “love” expanded to both inclinations and death.

**Standout:** **חַיָּב אָדָם לְבָרֵךְ עַל הָרָעָה כְּשֵׁם שֶׁהוּא מְבָרֵךְ עַל הַטּוֹבָה / ḥayyav adam levarekh al ha-ra’ah ke-shem shehu mevarekh al ha-tovah / “a person is obligated to bless on the bad just as he blesses on the good”** (9:5).

---

## Tractate rollup (dev + scholar)

| Lens | What Berakhot is |
|------|------------------|
| **Full-stack** | Scheduling (time windows), authz (exempt/obligated), content types (food→blessing), group quorum (zimun), ordered pipelines (meal/Shema), failover (error in prayer), event bus (nature/news) |
| **Torah scholar** | First tractate teaches: speech toward God structures day, meal, and crisis; Oral specifies **how** Written “hear / love / bless” becomes lived protocol; disputes preserved as live interface options |

**Next in canonical order:** **פֵּאָה / Peah / “Corner [of the field]”** (Zeraim 2).
