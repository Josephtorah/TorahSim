# The chain of transmission

TorahSim computes with the Written Torah as explained by the Oral Torah.
The oral explanation did not float free for three thousand years — it was
carried by an ordered, named, dated sequence of works, each building on the
ones before it. This document lists each work in the chain as it occurs,
what it is, and the role it plays in this project.

The tradition states the chain's opening links itself, in the Mishnah's
tractate Avot ("Fathers," 1:1): *Moses received the Torah from Sinai and
handed it on to Joshua, and Joshua to the elders, and the elders to the
prophets, and the prophets handed it on to the Men of the Great Assembly.*
Everything below is the continuation of that sentence into the written
record.

Dates given are the commonly used scholarly approximations; the tradition's
own datings sometimes differ. Nothing in this project's method depends on
resolving that — the *order* of the chain, which both agree on, is what the
code uses.

---

## 1. The Written Torah — the Five Books

**תורה** ("instruction, teaching") — Genesis, Exodus, Leviticus, Numbers,
Deuteronomy. Traditionally given through Moses at Sinai; the complete
manuscript this project's text derives from is the Leningrad Codex
(1008 CE), the oldest complete manuscript of the Hebrew Bible.

**Role here:** the source text of the law. Exodus 21 — the chapter taken to
full depth — is its first sustained block of civil and criminal law, given
immediately after the Ten Commandments.

## 2. The Prophets and the Writings — the rest of the 24 books

**נביאים** ("Prophets") — Joshua through the Twelve; **כתובים**
("Writings") — Psalms through Chronicles. Composed and gathered across the
biblical period; the traditional accounting closes the canon with the Men
of the Great Assembly (~5th century BCE). Together with the Five Books they
form the Tanakh, the 24-book Hebrew Bible.

**Role here:** the test corpus. The Tanakh run draws its 64 recorded cases
from these books and checks the machine's verdicts against the verdicts
their narratives record.

## 3. The Oral Torah in transmission (Sinai → ~200 CE)

**תורה שבעל פה** ("the Torah that is upon the mouth") — the explanation of
the written law, carried by memory and teaching through the chain named in
Avot: Moses, Joshua, the elders, the prophets, the Men of the Great
Assembly, then the paired teachers and the early sages down to the end of
the Second Temple period and beyond. During this whole span it is
deliberately *not* written.

**Role here:** the content that makes the written law executable — the
counting of the six years, the definition of the ransom, the measure of
the tariffs. Everything the machines encode is this explanation, cited from
the works below that finally wrote it down.

## 4. The Targumim — the early Aramaic translations (~1st–2nd century CE)

**תרגום** (targum, "translation") — Targum Onkelos on the Five Books and
Targum Jonathan on the Prophets: authorized Aramaic renderings from the
period when Aramaic was the spoken language.

**Role here:** early witnesses to how verses were *read* — a targum often
shows which oral interpretation of a legal phrase was standard, centuries
before the law codes spell it out.

## 5. The Mishnah (~200 CE)

**משנה** ("the repeated teaching") — the first great writing-down of the
oral law, arranged by Rabbi Judah the Prince into six orders and 63
tractates ("treatises"). The turning point of the whole chain: from memory
to text.

**Role here:** a primary witness for claims. The five heads of damages, the
worked injury cases, the rule that a standing verdict bans benefit from the
condemned animal — these enter the machines with Mishnah citations.

## 6. The Tosefta (~3rd century CE)

**תוספתא** ("the supplement") — a companion collection parallel to the
Mishnah, preserving the teachings the Mishnah's editor left out, often with
fuller detail.

**Role here:** supplementary witness — used when it preserves the worked
example or the measure the Mishnah states tersely.

## 7. The halakhic midrashim (~3rd–4th century CE)

Midrash ("exposition, inquiry") is the tradition's verse-by-verse mode:
law derived from and attached to the words of the written text. Halakha
("the law, the way to walk") names the legal content. The legal
expositions — the halakhic midrashim — are organized by book:

* **Mekhilta of Rabbi Ishmael** (mekhilta, "measure, rule") — on Exodus.
* **Sifra** ("the book") — on Leviticus.
* **Sifrei** ("the books") — on Numbers and Deuteronomy.

**Role here:** the single most-used shelf for Exodus 21. Because the
Mekhilta walks the chapter phrase by phrase, the full-inversion scan of
each block is, to a large degree, a complete read of the Mekhilta on it.

## 8. The Jerusalem Talmud (~400 CE)

**תלמוד ירושלמי** (Talmud Yerushalmi, "the learning of Jerusalem") — the
Land-of-Israel analysis of the Mishnah, recording the discussions of the
sages of the academies there.

**Role here:** consulted where its rulings or cases differ from the
Babylonian record — differences are exactly what a dispute-preserving
method wants on the page.

## 9. The Babylonian Talmud (~500–600 CE)

**תלמוד בבלי** (Talmud Bavli, "the learning of Babylonia") — the vast
analysis of the Mishnah from the Babylonian academies: 37 tractates of
argument, case law, derivation rules, and worked examples. The tradition's
central law library.

**Role here:** the main scanned shelf. The scan ledgers count their rows
against it; the assert battery draws most of its worked examples from it;
the recorded disputes the machines carry as data forks live here.

## 10. The Geonim (~600–1038 CE)

**גאונים** ("eminences") — the heads of the Babylonian academies after the
Talmud's close, answering legal questions across the diaspora and writing
the first summary codes.

**Role here:** the bridge that fixed how the Talmud is read; cited where a
reading choice matters to a coded rule.

## 11. The Rishonim (~1000–1500 CE)

**ראשונים** ("the early ones") — the medieval commentators and codifiers:

* **Rashi** (Rabbi Shlomo Yitzchaki, 1040–1105) — the base commentary on
  the Written Torah and nearly the whole Babylonian Talmud.
* **Rambam** (Rabbi Moses ben Maimon, Maimonides, 1138–1204) — the Mishneh
  Torah ("repetition of the Torah," ~1180), the first complete code of the
  entire law.
* **The Tosafists** (authors of Tosafot, "additions," 12th–13th century) —
  the dialectical glosses that cross-check the Talmud against itself.
* **Ramban** (Rabbi Moses ben Nachman, Nachmanides, 1194–1270) and the
  other great commentators of Spain and Provence.

**Role here:** the codification check. When a machine function is written,
the Rambam's codified form of the rule is the cleanest statement to test
its shape against; Rashi fixes what a Talmudic passage is actually saying.

## 12. The Shulchan Aruch (1565)

**שולחן ערוך** ("the set table") — Rabbi Joseph Karo's standard code of
practical law, with the glosses of Rabbi Moses Isserles (the Rema) carrying
the Ashkenazic rulings.

**Role here:** the settled-practice reference point; where the machines
carry a dispute forward as a fork, this is where one branch is often marked
as the practice.

## 13. The Acharonim (~1500 CE – present)

**אחרונים** ("the later ones") — the commentators after the Shulchan
Aruch. Two matter directly to this project:

* **The Vilna Gaon** (the GRA, Rabbi Elijah of Vilna, 1720–1797).
* **The Netziv** (Rabbi Naftali Zvi Yehuda Berlin, 1816–1893).

**Role here:** a live dispute between these two — whether the crown may
collect what sits on Heaven's docket, argued from Solomon's execution of
Joab at the altar — is carried in the machines as an open data fork. It
resurfaced, uninvited, in the very first simulation run. Disputes do not
die in this system; they ride along as state.

---

## How the code cites the chain

Every claim in the machines carries an identifier (like `L12-03`) that
resolves, through the claim manifests in `scans/manifests/`, to the work in
this chain that witnesses it — tractate, chapter, and section. The chain is
therefore not background reading: it is the citation graph of the code. A
constant without a chain citation cannot enter a machine; that is method
law number two (see `METHOD_LAWS.md`).
