# Lev 1 first verses → Mesorat haShas references

**Method:** Filter local `Data/links*.csv` where `Conection Type` = `mesorat hashas`, via **Sifra Nedavah early units** that walk the **first verses of Leviticus** (not a home-grown parallel index — see README standing decision).

**Scope of “first few verses”:** Sifra `Vayikra Dibbura d'Nedavah` **Chapter 1–6** and **Section 2–4** (approx **Lev 1:1–9** opening / cattle olah setup). Direct Tanakh `Leviticus 1:x` almost never appears as an MH endpoint (MH is Oral↔Oral).

**Machine dump:** `lev1_opening_mesorat_2026-07-19.json`

### How MH reaches “first verses of Lev”

Mesorat haShas does **not** link `Leviticus 1:1` as a Tanakh node (0 hits).  
Path we use:

```text
Lev 1:1–9  →  Sifra Nedavah (early chapters/sections)  →  MH parallels  →  Talmud / Midrash / Mishnah / Tosefta
```

| Sifra unit | ≈ Written area |
|------------|----------------|
| Chapter 1 | Lev 1:1 (call / ויקרא) |
| Chapter 2 | Lev 1:1–2 (אליו) |
| Section 2 | Lev 1:2 (בני ישראל, leaning) |
| Section 3 | Lev 1:3–4 (עולה) |
| Chapter 4–6 | Lev 1:3–9 (north, lean, flay, arrange) |

### Snapshot (this filter)

| | Count |
|--|------:|
| **All MH pairs** (early Sifra ↔ anything) | **353** |
| → Midrash (other midrash / Sifra internal) | 252 |
| → **Talmud** | **81** |
| → Tanaitic (Tosefta etc.) | 11 |
| → Mishnah | 9 |
| Direct Tanakh Lev 1:1–9 on MH | **0** |

**Chapter 1 (closest to Lev 1:1):** 19 MH links, **all midrash** (e.g. Bamidbar Rabbah 14:21, Mekhilta Rashbi, Sifrei) — **no Talmud** edges on MH for that unit.

**Where Talmud starts showing up:** Section 2 (24 Talmud links), Chapter 4 (21), Section 3 (7), …

### Companion (not MH): Written cite inside Bavli

For “Bavli quotes `(ויקרא א, נ)`” use **`cite_index`**, not Mesorat haShas:

| Verse | Bavli paren-cite hits (cite_index) |
|-------|-----------------------------------:|
| Lev 1:1 | 1 |
| Lev 1:2 | 18 |
| Lev 1:3 | 11 |
| Lev 1:4 | 8 |
| Lev 1:5 | 19 |
| Lev 1:6–9 | 4–10 each |

---

## Totals (full filter)

| | Count |
|--|------:|
| Unique MH pairs (early Nedavah ↔ other) | **353** |
| Direct MH with Tanakh Lev 1:1–9 citation | 0 |
| Full Nedavah (any unit) MH edges (either side) | 993 |

## Other side by category

| Count | Category |
|------:|----------|
| 252 | Midrash |
| 81 | Talmud |
| 11 | Tanaitic |
| 9 | Mishnah |

## Other side by work (top)

| Count | Work |
|------:|------|
| 23 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 |
| 20 | Bamidbar Rabbah |
| 18 | Zevachim |
| 12 | Menachot |
| 12 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 2 |
| 10 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 3 |
| 10 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 5 |
| 8 | Sifra, Vayikra Dibbura d'Nedavah, Section 6 |
| 8 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 4 |
| 8 | Sifra, Vayikra Dibbura d'Nedavah, Section 2 |
| 7 | Sifrei Bamidbar |
| 7 | Mekhilta DeRabbi Shimon Bar Yochai, Additions |
| 7 | Mekhilta d'Rabbi Yishmael |
| 7 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 16 |
| 7 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 7 |
| 7 | Yoma |
| 6 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 10 |
| 5 | Chullin |
| 5 | Sifra, Tzav, Section 11 |
| 5 | Sifra, Shemini, Mechilta d'Miluim 2 |
| 5 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 18 |
| 5 | Temurah |
| 4 | Eruvin |
| 4 | Mekhilta DeRabbi Shimon Bar Yochai |
| 4 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 1 |

## By Sifra unit (≈ verse area)

### Chapter 1 — Lev 1:1 (call / ויקרא)

**19 links**

| Sifra | ↔ Parallel |
|-------|------------|
| Sifra Nedavah Chapter 1 12 | Bamidbar Rabbah 14:21 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 1 4 | Bamidbar Rabbah 14:21 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 1 3 | Bamidbar Rabbah 14:21 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 1 5 | Bamidbar Rabbah 14:21 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 1 1 | Bamidbar Rabbah 14:21 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 1 1 | Mekhilta DeRabbi Shimon Bar Yochai 12:1 `Mekhilta DeRabbi Shimon Bar Yochai` |
| Sifra Nedavah Chapter 1 1-2 | Mekhilta DeRabbi Shimon Bar Yochai, Additions 3:1 `Mekhilta DeRabbi Shimon Bar Yochai, Additions` |
| Sifra Nedavah Chapter 1 10-11 | Mekhilta DeRabbi Shimon Bar Yochai, Additions 3:1 `Mekhilta DeRabbi Shimon Bar Yochai, Additions` |
| Sifra Nedavah Chapter 1 11-12 | Mekhilta DeRabbi Shimon Bar Yochai, Additions 3:1 `Mekhilta DeRabbi Shimon Bar Yochai, Additions` |
| Sifra Nedavah Chapter 1 12 | Mekhilta DeRabbi Shimon Bar Yochai, Additions 3:1 `Mekhilta DeRabbi Shimon Bar Yochai, Additions` |
| Sifra Nedavah Chapter 1 2-3 | Mekhilta DeRabbi Shimon Bar Yochai, Additions 3:1 `Mekhilta DeRabbi Shimon Bar Yochai, Additions` |
| Sifra Nedavah Chapter 1 4 | Mekhilta DeRabbi Shimon Bar Yochai, Additions 3:1 `Mekhilta DeRabbi Shimon Bar Yochai, Additions` |
| Sifra Nedavah Chapter 1 5 | Mekhilta DeRabbi Shimon Bar Yochai, Additions 3:1 `Mekhilta DeRabbi Shimon Bar Yochai, Additions` |
| Sifra Nedavah Chapter 1 3 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 1 2 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 1` |
| Sifra Nedavah Chapter 1 2 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 1 3 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 1` |
| Sifra Nedavah Chapter 1 5 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 1 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 1` |
| Sifra Nedavah Chapter 1 4 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 1 5 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 1` |
| Sifra Nedavah Chapter 1 9 | Sifra, Vayikra Dibbura d'Nedavah, Section 5 1 `Sifra, Vayikra Dibbura d'Nedavah, Section 5` |
| Sifra Nedavah Chapter 1 1 | Sifrei Bamidbar 113:1 `Sifrei Bamidbar` |

### Chapter 2 — Lev 1:1–2 area (אליו / to him)

**44 links**

| Sifra | ↔ Parallel |
|-------|------------|
| Sifra Nedavah Chapter 2 1-2 | Bamidbar Rabbah 14:19 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 2 4 | Bamidbar Rabbah 14:19 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 2 3 | Bamidbar Rabbah 14:19 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 2 2 | Bamidbar Rabbah 14:19 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 2 8 | Bamidbar Rabbah 14:20-21 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 2 2 | Bamidbar Rabbah 14:20-21 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 2 7 | Bamidbar Rabbah 14:21 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 2 8 | Bamidbar Rabbah 14:21 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 2 10-11 | Bamidbar Rabbah 14:21 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 2 9 | Bamidbar Rabbah 14:21 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 2 10 | Bamidbar Rabbah 14:21 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 2 6 | Bamidbar Rabbah 14:21 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 2 11 | Bamidbar Rabbah 14:21 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 2 12 | Bamidbar Rabbah 14:22 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 2 2 | Bamidbar Rabbah 15:8 `Bamidbar Rabbah` |
| Sifra Nedavah Chapter 2 4 | Mekhilta d'Rabbi Yishmael 12:1:1 `Mekhilta d'Rabbi Yishmael` |
| Sifra Nedavah Chapter 2 12 | Mekhilta d'Rabbi Yishmael 12:1:5 `Mekhilta d'Rabbi Yishmael` |
| Sifra Nedavah Chapter 2 13 | Mekhilta d'Rabbi Yishmael 12:1:5 `Mekhilta d'Rabbi Yishmael` |
| Sifra Nedavah Chapter 2 13 | Mekhilta d'Rabbi Yishmael 20:1:2 `Mekhilta d'Rabbi Yishmael` |
| Sifra Nedavah Chapter 2 4 | Otzar Midrashim, Aharon, And These are the Generations of Aharon and Moshe 7 `Otzar Midrashim, Aharon, And These are the Generations of Aharon and Moshe` |
| Sifra Nedavah Chapter 2 2 | Otzar Midrashim, Baraita of Melechet HaMishkan 1:63 `Otzar Midrashim, Baraita of Melechet HaMishkan` |
| Sifra Nedavah Chapter 2 12 | Otzar Midrashim, The Garden of Eden; Gehinnom, Tractate 'The Beating in the Grave' 3 `Otzar Midrashim, The Garden of Eden; Gehinnom, Tractate 'The Beating in the Grave'` |
| Sifra Nedavah Chapter 2 2 | Sifra, Shemini, Section 1 4 `Sifra, Shemini, Section 1` |
| Sifra Nedavah Chapter 2 2 | Sifra, Tzav, Chapter 18 10 `Sifra, Tzav, Chapter 18` |
| Sifra Nedavah Chapter 2 4 | Sifra, Tzav, Chapter 18 10 `Sifra, Tzav, Chapter 18` |
| Sifra Nedavah Chapter 2 12 | Sifra, Tzav, Chapter 2 4 `Sifra, Tzav, Chapter 2` |
| Sifra Nedavah Chapter 2 4 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 2 2 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 2` |
| Sifra Nedavah Chapter 2 4 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 2 3 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 2` |
| Sifra Nedavah Chapter 2 2 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 2 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 2` |
| Sifra Nedavah Chapter 2 3 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 2 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 2` |
| Sifra Nedavah Chapter 2 6 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 2 5 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 2` |
| Sifra Nedavah Chapter 2 5 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 2 6 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 2` |
| Sifra Nedavah Chapter 2 8 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 2 6 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 2` |
| Sifra Nedavah Chapter 2 7 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 2 6 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 2` |
| Sifra Nedavah Chapter 2 6 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 2 7 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 2` |
| Sifra Nedavah Chapter 2 8 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 2 7 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 2` |
| Sifra Nedavah Chapter 2 6 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 2 8 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 2` |
| Sifra Nedavah Chapter 2 7 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 2 8 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 2` |
| Sifra Nedavah Chapter 2 2 | Sifrei Bamidbar 58:1 `Sifrei Bamidbar` |
| Sifra Nedavah Chapter 2 4 | Sifrei Bamidbar 58:1 `Sifrei Bamidbar` |
| Sifra Nedavah Chapter 2 10 | Vayikra Rabbah 1:11 `Vayikra Rabbah` |
| Sifra Nedavah Chapter 2 13 | Bava Batra 121b:1 `Bava Batra` |
| Sifra Nedavah Chapter 2 13 | Taanit 30b:12 `Taanit` |
| Sifra Nedavah Chapter 2 12 | Tractate Kallah Rabbati 3:1 `Tractate Kallah Rabbati` |

### Section 2 — Lev 1:2 area (בני ישראל, סמיכה)

**50 links**

| Sifra | ↔ Parallel |
|-------|------------|
| Sifra Nedavah Section 2 4 | Bereishit Rabbah 1:13 `Bereishit Rabbah` |
| Sifra Nedavah Section 2 9 | Mekhilta DeRabbi Shimon Bar Yochai 20:14 `Mekhilta DeRabbi Shimon Bar Yochai` |
| Sifra Nedavah Section 2 9 | Mekhilta d'Rabbi Yishmael 20:14:3 `Mekhilta d'Rabbi Yishmael` |
| Sifra Nedavah Section 2 11 | Sifra, Emor, Section 4 3 `Sifra, Emor, Section 4` |
| Sifra Nedavah Section 2 11 | Sifra, Emor, Section 6 1 `Sifra, Emor, Section 6` |
| Sifra Nedavah Section 2 11 | Sifra, Metzora Parashat Zavim, Chapter 3 7 `Sifra, Metzora Parashat Zavim, Chapter 3` |
| Sifra Nedavah Section 2 11 | Sifra, Metzora, Chapter 5 15 `Sifra, Metzora, Chapter 5` |
| Sifra Nedavah Section 2 1 | Sifra, Shemini, Section 7 7 `Sifra, Shemini, Section 7` |
| Sifra Nedavah Section 2 1 | Sifra, Shemini, Section 7 8 `Sifra, Shemini, Section 7` |
| Sifra Nedavah Section 2 1 | Sifra, Tzav, Section 11 1 `Sifra, Tzav, Section 11` |
| Sifra Nedavah Section 2 9 | Sifra, Tzav, Section 11 1 `Sifra, Tzav, Section 11` |
| Sifra Nedavah Section 2 1 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 4 1 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 4` |
| Sifra Nedavah Section 2 9 | Sifra, Vayikra Dibbura d'Nedavah, Section 2 1 `Sifra, Vayikra Dibbura d'Nedavah, Section 2` |
| Sifra Nedavah Section 2 7 | Sifra, Vayikra Dibbura d'Nedavah, Section 2 10 `Sifra, Vayikra Dibbura d'Nedavah, Section 2` |
| Sifra Nedavah Section 2 10 | Sifra, Vayikra Dibbura d'Nedavah, Section 2 7 `Sifra, Vayikra Dibbura d'Nedavah, Section 2` |
| Sifra Nedavah Section 2 8-9 | Sifra, Vayikra Dibbura d'Nedavah, Section 2 7 `Sifra, Vayikra Dibbura d'Nedavah, Section 2` |
| Sifra Nedavah Section 2 7 | Sifra, Vayikra Dibbura d'Nedavah, Section 2 8-9 `Sifra, Vayikra Dibbura d'Nedavah, Section 2` |
| Sifra Nedavah Section 2 1 | Sifra, Vayikra Dibbura d'Nedavah, Section 2 9 `Sifra, Vayikra Dibbura d'Nedavah, Section 2` |
| Sifra Nedavah Section 2 10 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 7-8 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 2 4 | Sifra, Vayikra Dibbura d'Nedavah, Section 8 3 `Sifra, Vayikra Dibbura d'Nedavah, Section 8` |
| Sifra Nedavah Section 2 9 | Mishnah Avodah Zarah 3:5 `Mishnah Avodah Zarah` |
| Sifra Nedavah Section 2 1 | Mishnah Bava Kamma 7:1 `Mishnah Bava Kamma` |
| Sifra Nedavah Section 2 1 | Mishnah Eruvin 1:7 `Mishnah Eruvin` |
| Sifra Nedavah Section 2 1 | Mishnah Menachot 9:9 `Mishnah Menachot` |
| Sifra Nedavah Section 2 8-9 | Bava Kamma 40b:16 `Bava Kamma` |
| Sifra Nedavah Section 2 10-11 | Bava Kamma 40b:16-19 `Bava Kamma` |
| Sifra Nedavah Section 2 1 | Bava Kamma 62b:7 `Bava Kamma` |
| Sifra Nedavah Section 2 11 | Bekhorot 41a:15 `Bekhorot` |
| Sifra Nedavah Section 2 1-2 | Chagigah 16b:15 `Chagigah` |
| Sifra Nedavah Section 2 2 | Chullin 85a:2-3 `Chullin` |
| Sifra Nedavah Section 2 1 | Eruvin 15a:20 `Eruvin` |
| Sifra Nedavah Section 2 9 | Eruvin 15b:3 `Eruvin` |
| Sifra Nedavah Section 2 1-2 | Eruvin 96b:7 `Eruvin` |
| Sifra Nedavah Section 2 9 | Gittin 21b:3 `Gittin` |
| Sifra Nedavah Section 2 1-2 | Kiddushin 36a:16 `Kiddushin` |
| Sifra Nedavah Section 2 8 | Kiddushin 66a:1 `Kiddushin` |
| Sifra Nedavah Section 2 10 | Menachot 5b:7 `Menachot` |
| Sifra Nedavah Section 2 1 | Menachot 94a:1 `Menachot` |
| Sifra Nedavah Section 2 4 | Nedarim 10a:14-10b:1 `Nedarim` |
| Sifra Nedavah Section 2 11 | Niddah 41a:8 `Niddah` |
| Sifra Nedavah Section 2 1-2 | Rosh Hashanah 33a:6 `Rosh Hashanah` |
| Sifra Nedavah Section 2 9 | Sukkah 24b:3 `Sukkah` |
| Sifra Nedavah Section 2 7 | Temurah 28a:14-15 `Temurah` |
| Sifra Nedavah Section 2 8 | Temurah 28a:17-18 `Temurah` |
| Sifra Nedavah Section 2 10-11 | Temurah 28b:11-12 `Temurah` |
| Sifra Nedavah Section 2 1 | Temurah 28b:6 `Temurah` |
| Sifra Nedavah Section 2 10 | Temurah 29a:11 `Temurah` |
| Sifra Nedavah Section 2 6 | Zevachim 34a:15 `Zevachim` |
| Sifra Nedavah Section 2 9 | Tosefta Gittin 2:6 `Tosefta Gittin` |
| Sifra Nedavah Section 2 1 | Tosefta Zavim 5:4 `Tosefta Zavim` |

### Chapter 3 — Lev 1:2 area (תקריבו)

**36 links**

| Sifra | ↔ Parallel |
|-------|------------|
| Sifra Nedavah Chapter 3 7 | Sifra, Emor, Section 8 2 `Sifra, Emor, Section 8` |
| Sifra Nedavah Chapter 3 7 | Sifra, Metzora Parashat Zavim, Chapter 5 3 `Sifra, Metzora Parashat Zavim, Chapter 5` |
| Sifra Nedavah Chapter 3 7 | Sifra, Metzora Parashat Zavim, Section 1 12 `Sifra, Metzora Parashat Zavim, Section 1` |
| Sifra Nedavah Chapter 3 7 | Sifra, Vayikra Dibbura d'Chovah, Section 8 2 `Sifra, Vayikra Dibbura d'Chovah, Section 8` |
| Sifra Nedavah Chapter 3 5 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 10 10 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 10` |
| Sifra Nedavah Chapter 3 10 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 10 11 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 10` |
| Sifra Nedavah Chapter 3 7 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 10 11 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 10` |
| Sifra Nedavah Chapter 3 1 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 10 9 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 10` |
| Sifra Nedavah Chapter 3 2 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 10 9 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 10` |
| Sifra Nedavah Chapter 3 4 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 10 9 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 10` |
| Sifra Nedavah Chapter 3 1 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 16 5 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 16` |
| Sifra Nedavah Chapter 3 4 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 16 5 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 16` |
| Sifra Nedavah Chapter 3 4 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 16 6 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 16` |
| Sifra Nedavah Chapter 3 4-6 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 16 6-7 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 16` |
| Sifra Nedavah Chapter 3 5-6 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 16 6-7 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 16` |
| Sifra Nedavah Chapter 3 6 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 16 7 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 16` |
| Sifra Nedavah Chapter 3 8 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 16 9 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 16` |
| Sifra Nedavah Chapter 3 4 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 3 1 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 3` |
| Sifra Nedavah Chapter 3 2 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 3 1 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 3` |
| Sifra Nedavah Chapter 3 7 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 3 10 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 3` |
| Sifra Nedavah Chapter 3 1 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 3 2 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 3` |
| Sifra Nedavah Chapter 3 4 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 3 2 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 3` |
| Sifra Nedavah Chapter 3 6 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 3 3 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 3` |
| Sifra Nedavah Chapter 3 1 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 3 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 3` |
| Sifra Nedavah Chapter 3 2 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 3 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 3` |
| Sifra Nedavah Chapter 3 3 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 3 6 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 3` |
| Sifra Nedavah Chapter 3 10 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 3 7 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 3` |
| Sifra Nedavah Chapter 3 1 | Sifra, Vayikra Dibbura d'Nedavah, Section 6 6 `Sifra, Vayikra Dibbura d'Nedavah, Section 6` |
| Sifra Nedavah Chapter 3 2 | Sifra, Vayikra Dibbura d'Nedavah, Section 6 6 `Sifra, Vayikra Dibbura d'Nedavah, Section 6` |
| Sifra Nedavah Chapter 3 4 | Sifra, Vayikra Dibbura d'Nedavah, Section 6 6 `Sifra, Vayikra Dibbura d'Nedavah, Section 6` |
| Sifra Nedavah Chapter 3 4-5 | Sifra, Vayikra Dibbura d'Nedavah, Section 6 7 `Sifra, Vayikra Dibbura d'Nedavah, Section 6` |
| Sifra Nedavah Chapter 3 5 | Sifra, Vayikra Dibbura d'Nedavah, Section 6 7 `Sifra, Vayikra Dibbura d'Nedavah, Section 6` |
| Sifra Nedavah Chapter 3 6 | Sifra, Vayikra Dibbura d'Nedavah, Section 6 7 `Sifra, Vayikra Dibbura d'Nedavah, Section 6` |
| Sifra Nedavah Chapter 3 8 | Sifra, Vayikra Dibbura d'Nedavah, Section 8 1 `Sifra, Vayikra Dibbura d'Nedavah, Section 8` |
| Sifra Nedavah Chapter 3 8 | Sifra, Vayikra Dibbura d'Nedavah, Section 8 2 `Sifra, Vayikra Dibbura d'Nedavah, Section 8` |
| Sifra Nedavah Chapter 3 3 | Sifra, Vayikra Dibbura d'Nedavah, Section 9 5 `Sifra, Vayikra Dibbura d'Nedavah, Section 9` |

### Section 3 — Lev 1:3–4 area (עולה)

**51 links**

| Sifra | ↔ Parallel |
|-------|------------|
| Sifra Nedavah Section 3 4 | Mekhilta DeRabbi Shimon Bar Yochai 13:11 `Mekhilta DeRabbi Shimon Bar Yochai` |
| Sifra Nedavah Section 3 4 | Sifra, Bechukotai, Chapter 9 14 `Sifra, Bechukotai, Chapter 9` |
| Sifra Nedavah Section 3 4 | Sifra, Bechukotai, Chapter 9 15 `Sifra, Bechukotai, Chapter 9` |
| Sifra Nedavah Section 3 13 | Sifra, Metzora Parashat Zavim, Chapter 9 4 `Sifra, Metzora Parashat Zavim, Chapter 9` |
| Sifra Nedavah Section 3 6 | Sifra, Shemini, Section 9 7 `Sifra, Shemini, Section 9` |
| Sifra Nedavah Section 3 8 | Sifra, Vayikra Dibbura d'Chovah, Section 2 6 `Sifra, Vayikra Dibbura d'Chovah, Section 2` |
| Sifra Nedavah Section 3 8 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 17 12 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 17` |
| Sifra Nedavah Section 3 6 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 18 2 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 18` |
| Sifra Nedavah Section 3 8 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 18 2 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 18` |
| Sifra Nedavah Section 3 9-10 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 18 2-3 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 18` |
| Sifra Nedavah Section 3 11 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 18 3 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 18` |
| Sifra Nedavah Section 3 8-9 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 18 3 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 18` |
| Sifra Nedavah Section 3 1 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 4 3 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 4` |
| Sifra Nedavah Section 3 2 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 4 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 4` |
| Sifra Nedavah Section 3 1 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 5 2 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 5` |
| Sifra Nedavah Section 3 13 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 6 6 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 6` |
| Sifra Nedavah Section 3 13 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 7 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 7` |
| Sifra Nedavah Section 3 7-8 | Sifra, Vayikra Dibbura d'Nedavah, Section 2 10 `Sifra, Vayikra Dibbura d'Nedavah, Section 2` |
| Sifra Nedavah Section 3 5 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 1 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 3-4 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 1-2 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 8-9 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 10-11 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 7 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 11 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 4 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 2 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 5 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 3 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 1-2 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 3-4 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 6 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 3-4 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 2 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 4 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 1 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 5 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 3 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 5 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 3-4 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 6 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 8 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 6 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 11 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 7 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 6 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 8 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 10-11 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 8-9 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 3 14 | Sifra, Vayikra Dibbura d'Nedavah, Section 4 7 `Sifra, Vayikra Dibbura d'Nedavah, Section 4` |
| Sifra Nedavah Section 3 13-14 | Sifra, Vayikra Dibbura d'Nedavah, Section 4 8 `Sifra, Vayikra Dibbura d'Nedavah, Section 4` |
| Sifra Nedavah Section 3 6 | Sifra, Vayikra Dibbura d'Nedavah, Section 5 3 `Sifra, Vayikra Dibbura d'Nedavah, Section 5` |
| Sifra Nedavah Section 3 8 | Sifra, Vayikra Dibbura d'Nedavah, Section 5 3 `Sifra, Vayikra Dibbura d'Nedavah, Section 5` |
| Sifra Nedavah Section 3 6 | Sifra, Vayikra Dibbura d'Nedavah, Section 6 1 `Sifra, Vayikra Dibbura d'Nedavah, Section 6` |
| Sifra Nedavah Section 3 8 | Sifra, Vayikra Dibbura d'Nedavah, Section 6 1 `Sifra, Vayikra Dibbura d'Nedavah, Section 6` |
| Sifra Nedavah Section 3 8 | Sifrei Bamidbar 107:2 `Sifrei Bamidbar` |
| Sifra Nedavah Section 3 6 | Sifrei Bamidbar 123:1 `Sifrei Bamidbar` |
| Sifra Nedavah Section 3 15 | Arakhin 21a:12 `Arakhin` |
| Sifra Nedavah Section 3 15 | Bava Batra 48a:1 `Bava Batra` |
| Sifra Nedavah Section 3 15 | Kiddushin 50a:1-2 `Kiddushin` |
| Sifra Nedavah Section 3 7-8 | Menachot 5b:7-8 `Menachot` |
| Sifra Nedavah Section 3 15 | Rosh Hashanah 6a:7 `Rosh Hashanah` |
| Sifra Nedavah Section 3 12 | Sukkah 42a:5 `Sukkah` |
| Sifra Nedavah Section 3 15 | Yevamot 106a:14 `Yevamot` |
| Sifra Nedavah Section 3 4 | Tosefta Ma'aser Sheni 2:19 `Tosefta Ma'aser Sheni` |
| Sifra Nedavah Section 3 12 | Tosefta Pesachim 5:5 `Tosefta Pesachim` |

### Chapter 4 — Lev 1:3–5 area (לפני ה׳, צפון, lean)

**70 links**

| Sifra | ↔ Parallel |
|-------|------------|
| Sifra Nedavah Chapter 4 10 | Mekhilta DeRabbi Shimon Bar Yochai 20:21 `Mekhilta DeRabbi Shimon Bar Yochai` |
| Sifra Nedavah Chapter 4 8 | Mekhilta d'Rabbi Yishmael 20:7:2 `Mekhilta d'Rabbi Yishmael` |
| Sifra Nedavah Chapter 4 10 | Mekhilta d'Rabbi Yishmael 21:31:2 `Mekhilta d'Rabbi Yishmael` |
| Sifra Nedavah Chapter 4 10 | Sifra, Acharei Mot, Chapter 10 4 `Sifra, Acharei Mot, Chapter 10` |
| Sifra Nedavah Chapter 4 1 | Sifra, Acharei Mot, Chapter 3 10 `Sifra, Acharei Mot, Chapter 3` |
| Sifra Nedavah Chapter 4 1 | Sifra, Acharei Mot, Chapter 4 8 `Sifra, Acharei Mot, Chapter 4` |
| Sifra Nedavah Chapter 4 1 | Sifra, Acharei Mot, Section 6 8 `Sifra, Acharei Mot, Section 6` |
| Sifra Nedavah Chapter 4 10 | Sifra, Emor, Section 3 4 `Sifra, Emor, Section 3` |
| Sifra Nedavah Chapter 4 1 | Sifra, Emor, Section 6 1 `Sifra, Emor, Section 6` |
| Sifra Nedavah Chapter 4 1 | Sifra, Metzora Parashat Zavim, Chapter 3 7 `Sifra, Metzora Parashat Zavim, Chapter 3` |
| Sifra Nedavah Chapter 4 1 | Sifra, Metzora, Chapter 2 4 `Sifra, Metzora, Chapter 2` |
| Sifra Nedavah Chapter 4 1 | Sifra, Metzora, Chapter 5 15 `Sifra, Metzora, Chapter 5` |
| Sifra Nedavah Chapter 4 1 | Sifra, Metzora, Chapter 5 3 `Sifra, Metzora, Chapter 5` |
| Sifra Nedavah Chapter 4 10 | Sifra, Metzora, Section 4 5 `Sifra, Metzora, Section 4` |
| Sifra Nedavah Chapter 4 2 | Sifra, Shemini, Mechilta d'Miluim 2 30 `Sifra, Shemini, Mechilta d'Miluim 2` |
| Sifra Nedavah Chapter 4 1 | Sifra, Shemini, Section 7 7 `Sifra, Shemini, Section 7` |
| Sifra Nedavah Chapter 4 1 | Sifra, Shemini, Section 7 8 `Sifra, Shemini, Section 7` |
| Sifra Nedavah Chapter 4 2 | Sifra, Tazria Parashat Nega'im, Chapter 2 4 `Sifra, Tazria Parashat Nega'im, Chapter 2` |
| Sifra Nedavah Chapter 4 2 | Sifra, Tazria Parashat Nega'im, Section 5 5 `Sifra, Tazria Parashat Nega'im, Section 5` |
| Sifra Nedavah Chapter 4 10 | Sifra, Tzav, Chapter 1 13 `Sifra, Tzav, Chapter 1` |
| Sifra Nedavah Chapter 4 10 | Sifra, Tzav, Chapter 13 5 `Sifra, Tzav, Chapter 13` |
| Sifra Nedavah Chapter 4 10 | Sifra, Tzav, Chapter 2 9 `Sifra, Tzav, Chapter 2` |
| Sifra Nedavah Chapter 4 1 | Sifra, Tzav, Section 11 1 `Sifra, Tzav, Section 11` |
| Sifra Nedavah Chapter 4 2 | Sifra, Tzav, Section 11 6 `Sifra, Tzav, Section 11` |
| Sifra Nedavah Chapter 4 2 | Sifra, Tzav, Section 11 8 `Sifra, Tzav, Section 11` |
| Sifra Nedavah Chapter 4 2 | Sifra, Vayikra Dibbura d'Chovah, Section 3 4 `Sifra, Vayikra Dibbura d'Chovah, Section 3` |
| Sifra Nedavah Chapter 4 2 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 13 1 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 13` |
| Sifra Nedavah Chapter 4 2 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 15 3 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 15` |
| Sifra Nedavah Chapter 4 2 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 15 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 15` |
| Sifra Nedavah Chapter 4 2 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 17 1 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 17` |
| Sifra Nedavah Chapter 4 2 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 17 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 17` |
| Sifra Nedavah Chapter 4 2 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 17 5 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 17` |
| Sifra Nedavah Chapter 4 6 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 20 3 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 20` |
| Sifra Nedavah Chapter 4 6 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 4 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 4` |
| Sifra Nedavah Chapter 4 4 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 4 6 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 4` |
| Sifra Nedavah Chapter 4 3 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 5 2 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 5` |
| Sifra Nedavah Chapter 4 5 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 5 3 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 5` |
| Sifra Nedavah Chapter 4 10 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 5 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 5` |
| Sifra Nedavah Chapter 4 2 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 9 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 9` |
| Sifra Nedavah Chapter 4 2 | Sifra, Vayikra Dibbura d'Nedavah, Section 10 4 `Sifra, Vayikra Dibbura d'Nedavah, Section 10` |
| Sifra Nedavah Chapter 4 3 | Sifra, Vayikra Dibbura d'Nedavah, Section 11 2 `Sifra, Vayikra Dibbura d'Nedavah, Section 11` |
| Sifra Nedavah Chapter 4 1 | Sifra, Vayikra Dibbura d'Nedavah, Section 12 5 `Sifra, Vayikra Dibbura d'Nedavah, Section 12` |
| Sifra Nedavah Chapter 4 1 | Sifra, Vayikra Dibbura d'Nedavah, Section 2 1 `Sifra, Vayikra Dibbura d'Nedavah, Section 2` |
| Sifra Nedavah Chapter 4 3 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 1 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Chapter 4 4 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 2 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Chapter 4 10 | Mishnah Meilah 2:9 `Mishnah Meilah` |
| Sifra Nedavah Chapter 4 10 | Mishnah Zevachim 13:4 `Mishnah Zevachim` |
| Sifra Nedavah Chapter 4 10 | Mishnah Zevachim 4:3 `Mishnah Zevachim` |
| Sifra Nedavah Chapter 4 9 | Keritot 22a:19 `Keritot` |
| Sifra Nedavah Chapter 4 1 | Megillah 3b:11 `Megillah` |
| Sifra Nedavah Chapter 4 10 | Meilah 10a:6 `Meilah` |
| Sifra Nedavah Chapter 4 10 | Menachot 12b:2 `Menachot` |
| Sifra Nedavah Chapter 4 10 | Menachot 21b:4 `Menachot` |
| Sifra Nedavah Chapter 4 9 | Menachot 25a:2 `Menachot` |
| Sifra Nedavah Chapter 4 10 | Menachot 26b:13 `Menachot` |
| Sifra Nedavah Chapter 4 2 | Menachot 60b:7 `Menachot` |
| Sifra Nedavah Chapter 4 2 | Menachot 62b:7 `Menachot` |
| Sifra Nedavah Chapter 4 2 | Menachot 93b:4 `Menachot` |
| Sifra Nedavah Chapter 4 10 | Menachot 93b:7 `Menachot` |
| Sifra Nedavah Chapter 4 9 | Pesachim 16b:7-8 `Pesachim` |
| Sifra Nedavah Chapter 4 10 | Shevuot 11a:5 `Shevuot` |
| Sifra Nedavah Chapter 4 10 | Yoma 5a:3 `Yoma` |
| Sifra Nedavah Chapter 4 9 | Yoma 7a:10 `Yoma` |
| Sifra Nedavah Chapter 4 10 | Zevachim 109a:4 `Zevachim` |
| Sifra Nedavah Chapter 4 9 | Zevachim 23a:11-23b:1 `Zevachim` |
| Sifra Nedavah Chapter 4 10 | Zevachim 42a:4 `Zevachim` |
| Sifra Nedavah Chapter 4 10 | Zevachim 43a:6 `Zevachim` |
| Sifra Nedavah Chapter 4 10 | Zevachim 44a:11 `Zevachim` |
| Sifra Nedavah Chapter 4 10 | Zevachim 6a:15 `Zevachim` |
| Sifra Nedavah Chapter 4 10 | Tosefta Menahot 4:1 `Tosefta Menahot` |

### Section 4 — Lev 1:4–5 area (וסמך…ושחט)

**39 links**

| Sifra | ↔ Parallel |
|-------|------------|
| Sifra Nedavah Section 4 10 | Sifra, Acharei Mot, Chapter 4 11 `Sifra, Acharei Mot, Chapter 4` |
| Sifra Nedavah Section 4 6 | Sifra, Emor, Section 1 1 `Sifra, Emor, Section 1` |
| Sifra Nedavah Section 4 10 | Sifra, Shemini, Mechilta d'Miluim 2 11 `Sifra, Shemini, Mechilta d'Miluim 2` |
| Sifra Nedavah Section 4 4 | Sifra, Shemini, Mechilta d'Miluim 2 11 `Sifra, Shemini, Mechilta d'Miluim 2` |
| Sifra Nedavah Section 4 10 | Sifra, Shemini, Mechilta d'Miluim 2 40 `Sifra, Shemini, Mechilta d'Miluim 2` |
| Sifra Nedavah Section 4 4 | Sifra, Shemini, Mechilta d'Miluim 2 40 `Sifra, Shemini, Mechilta d'Miluim 2` |
| Sifra Nedavah Section 4 6 | Sifra, Shemini, Section 1 3 `Sifra, Shemini, Section 1` |
| Sifra Nedavah Section 4 10 | Sifra, Tzav, Chapter 8 4 `Sifra, Tzav, Chapter 8` |
| Sifra Nedavah Section 4 4 | Sifra, Tzav, Chapter 8 4 `Sifra, Tzav, Chapter 8` |
| Sifra Nedavah Section 4 10 | Sifra, Tzav, Section 3 5 `Sifra, Tzav, Section 3` |
| Sifra Nedavah Section 4 4 | Sifra, Tzav, Section 3 5 `Sifra, Tzav, Section 3` |
| Sifra Nedavah Section 4 10 | Sifra, Vayikra Dibbura d'Chovah, Section 10 1 `Sifra, Vayikra Dibbura d'Chovah, Section 10` |
| Sifra Nedavah Section 4 4 | Sifra, Vayikra Dibbura d'Chovah, Section 10 1 `Sifra, Vayikra Dibbura d'Chovah, Section 10` |
| Sifra Nedavah Section 4 10 | Sifra, Vayikra Dibbura d'Chovah, Section 10 2 `Sifra, Vayikra Dibbura d'Chovah, Section 10` |
| Sifra Nedavah Section 4 4 | Sifra, Vayikra Dibbura d'Chovah, Section 10 2 `Sifra, Vayikra Dibbura d'Chovah, Section 10` |
| Sifra Nedavah Section 4 10 | Sifra, Vayikra Dibbura d'Chovah, Section 12 14 `Sifra, Vayikra Dibbura d'Chovah, Section 12` |
| Sifra Nedavah Section 4 4 | Sifra, Vayikra Dibbura d'Chovah, Section 12 14 `Sifra, Vayikra Dibbura d'Chovah, Section 12` |
| Sifra Nedavah Section 4 8 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 6 6 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 6` |
| Sifra Nedavah Section 4 8 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 7 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 7` |
| Sifra Nedavah Section 4 8 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 13-14 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 4 7 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 14 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Section 4 10 | Sifra, Vayikra Dibbura d'Nedavah, Section 9 12 `Sifra, Vayikra Dibbura d'Nedavah, Section 9` |
| Sifra Nedavah Section 4 4 | Sifrei Bamidbar 75:1 `Sifrei Bamidbar` |
| Sifra Nedavah Section 4 5 | Sifrei Bamidbar 75:1 `Sifrei Bamidbar` |
| Sifra Nedavah Section 4 2 | Mishnah Zevachim 3:1 `Mishnah Zevachim` |
| Sifra Nedavah Section 4 2 | Chullin 2b:12 `Chullin` |
| Sifra Nedavah Section 4 12 | Megillah 3b:11 `Megillah` |
| Sifra Nedavah Section 4 12 | Pesachim 77a:17 `Pesachim` |
| Sifra Nedavah Section 4 5 | Rosh Hashanah 25a:13 `Rosh Hashanah` |
| Sifra Nedavah Section 4 4 | Zevachim 13a:11-12 `Zevachim` |
| Sifra Nedavah Section 4 5 | Zevachim 13a:13 `Zevachim` |
| Sifra Nedavah Section 4 2 | Zevachim 31b:14 `Zevachim` |
| Sifra Nedavah Section 4 3 | Zevachim 32b:2 `Zevachim` |
| Sifra Nedavah Section 4 9-10 | Zevachim 53b:5-6 `Zevachim` |
| Sifra Nedavah Section 4 14 | Zevachim 59a:1 `Zevachim` |
| Sifra Nedavah Section 4 2 | Tosefta Chagigah 3:8 `Tosefta Chagigah` |
| Sifra Nedavah Section 4 4 | Tosefta Zevahim 1:6 `Tosefta Zevahim` |
| Sifra Nedavah Section 4 5 | Tosefta Zevahim 1:6 `Tosefta Zevahim` |
| Sifra Nedavah Section 4 12 | Tosefta Zevahim 4:1 `Tosefta Zevahim` |

### Chapter 5 — Lev 1:6 area (והפשיט ונתח)

**23 links**

| Sifra | ↔ Parallel |
|-------|------------|
| Sifra Nedavah Chapter 5 4 | Sifra, Shemini, Section 6 8 `Sifra, Shemini, Section 6` |
| Sifra Nedavah Chapter 5 4 | Sifra, Tzav, Section 10 4 `Sifra, Tzav, Section 10` |
| Sifra Nedavah Chapter 5 4 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 11 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 11` |
| Sifra Nedavah Chapter 5 4 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 4 10 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 4` |
| Sifra Nedavah Chapter 5 2 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 4 3 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 4` |
| Sifra Nedavah Chapter 5 3 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 4 5 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 4` |
| Sifra Nedavah Chapter 5 6-7 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 5 1 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 5` |
| Sifra Nedavah Chapter 5 3-4 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 5 2-3 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 5` |
| Sifra Nedavah Chapter 5 2-3 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 5 3-4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 5` |
| Sifra Nedavah Chapter 5 6 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 5 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 5` |
| Sifra Nedavah Chapter 5 4 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 5 6 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 5` |
| Sifra Nedavah Chapter 5 1 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 5 6-7 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 5` |
| Sifra Nedavah Chapter 5 4 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 7 6 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 7` |
| Sifra Nedavah Chapter 5 2 | Sifra, Vayikra Dibbura d'Nedavah, Section 11 2 `Sifra, Vayikra Dibbura d'Nedavah, Section 11` |
| Sifra Nedavah Chapter 5 2 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 1 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Chapter 5 8 | Sifra, Vayikra Dibbura d'Nedavah, Section 7 3 `Sifra, Vayikra Dibbura d'Nedavah, Section 7` |
| Sifra Nedavah Chapter 5 10 | Eruvin 63a:15 `Eruvin` |
| Sifra Nedavah Chapter 5 10 | Yoma 21b:5 `Yoma` |
| Sifra Nedavah Chapter 5 8 | Yoma 24b:9 `Yoma` |
| Sifra Nedavah Chapter 5 8 | Yoma 45a:12 `Yoma` |
| Sifra Nedavah Chapter 5 10 | Yoma 53a:20 `Yoma` |
| Sifra Nedavah Chapter 5 9 | Zevachim 18a:7 `Zevachim` |
| Sifra Nedavah Chapter 5 10 | Zevachim 61b:5 `Zevachim` |

### Chapter 6 — Lev 1:7–9 area (וערכו)

**21 links**

| Sifra | ↔ Parallel |
|-------|------------|
| Sifra Nedavah Chapter 6 7 | Sifra, Tzav, Chapter 7 3 `Sifra, Tzav, Chapter 7` |
| Sifra Nedavah Chapter 6 6-7 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 7 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 7` |
| Sifra Nedavah Chapter 6 7 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 7 4 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 7` |
| Sifra Nedavah Chapter 6 8 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 7 5 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 7` |
| Sifra Nedavah Chapter 6 10 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 7 8 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 7` |
| Sifra Nedavah Chapter 6 10 | Sifra, Vayikra Dibbura d'Nedavah, Chapter 9 7 `Sifra, Vayikra Dibbura d'Nedavah, Chapter 9` |
| Sifra Nedavah Chapter 6 6 | Sifra, Vayikra Dibbura d'Nedavah, Section 3 13 `Sifra, Vayikra Dibbura d'Nedavah, Section 3` |
| Sifra Nedavah Chapter 6 6 | Sifra, Vayikra Dibbura d'Nedavah, Section 4 8 `Sifra, Vayikra Dibbura d'Nedavah, Section 4` |
| Sifra Nedavah Chapter 6 4 | Vayikra Rabbah 7:1 `Vayikra Rabbah` |
| Sifra Nedavah Chapter 6 4 | Mishnah Tamid 2:3 `Mishnah Tamid` |
| Sifra Nedavah Chapter 6 3 | Chullin 27a:14-15 `Chullin` |
| Sifra Nedavah Chapter 6 2 | Chullin 27a:14-15 `Chullin` |
| Sifra Nedavah Chapter 6 2 | Chullin 27b:1 `Chullin` |
| Sifra Nedavah Chapter 6 5 | Menachot 22a:2-3 `Menachot` |
| Sifra Nedavah Chapter 6 4 | Tamid 29a:2 `Tamid` |
| Sifra Nedavah Chapter 6 4 | Tamid 29b:6 `Tamid` |
| Sifra Nedavah Chapter 6 2 | Yoma 25b:16 `Yoma` |
| Sifra Nedavah Chapter 6 5 | Zevachim 116b:6 `Zevachim` |
| Sifra Nedavah Chapter 6 5 | Zevachim 62b:3 `Zevachim` |
| Sifra Nedavah Chapter 6 9 | Zevachim 85b:17-86a:1 `Zevachim` |
| Sifra Nedavah Chapter 6 9 | Tosefta Zevahim 3:5 `Tosefta Zevahim` |

## Quick list — Talmud only (all early units)

```text
Zevachim (18):
  Zevachim 109a:4
  Zevachim 116b:6
  Zevachim 13a:11-12
  Zevachim 13a:13
  Zevachim 18a:7
  Zevachim 23a:11-23b:1
  Zevachim 31b:14
  Zevachim 32b:2
  Zevachim 34a:15
  Zevachim 42a:4
  Zevachim 43a:6
  Zevachim 44a:11
  Zevachim 53b:5-6
  Zevachim 59a:1
  Zevachim 61b:5
  Zevachim 62b:3
  Zevachim 6a:15
  Zevachim 85b:17-86a:1
Menachot (12):
  Menachot 12b:2
  Menachot 21b:4
  Menachot 22a:2-3
  Menachot 25a:2
  Menachot 26b:13
  Menachot 5b:7
  Menachot 5b:7-8
  Menachot 60b:7
  Menachot 62b:7
  Menachot 93b:4
  Menachot 93b:7
  Menachot 94a:1
Yoma (7):
  Yoma 21b:5
  Yoma 24b:9
  Yoma 25b:16
  Yoma 45a:12
  Yoma 53a:20
  Yoma 5a:3
  Yoma 7a:10
Chullin (5):
  Chullin 27a:14-15
  Chullin 27b:1
  Chullin 2b:12
  Chullin 85a:2-3
Temurah (5):
  Temurah 28a:14-15
  Temurah 28a:17-18
  Temurah 28b:11-12
  Temurah 28b:6
  Temurah 29a:11
Eruvin (4):
  Eruvin 15a:20
  Eruvin 15b:3
  Eruvin 63a:15
  Eruvin 96b:7
Bava Kamma (3):
  Bava Kamma 40b:16
  Bava Kamma 40b:16-19
  Bava Kamma 62b:7
Kiddushin (3):
  Kiddushin 36a:16
  Kiddushin 50a:1-2
  Kiddushin 66a:1
Rosh Hashanah (3):
  Rosh Hashanah 25a:13
  Rosh Hashanah 33a:6
  Rosh Hashanah 6a:7
Bava Batra (2):
  Bava Batra 121b:1
  Bava Batra 48a:1
Megillah (2):
  Megillah 3b:11
Pesachim (2):
  Pesachim 16b:7-8
  Pesachim 77a:17
Sukkah (2):
  Sukkah 24b:3
  Sukkah 42a:5
Tamid (2):
  Tamid 29a:2
  Tamid 29b:6
Arakhin (1):
  Arakhin 21a:12
Bekhorot (1):
  Bekhorot 41a:15
Chagigah (1):
  Chagigah 16b:15
Gittin (1):
  Gittin 21b:3
Keritot (1):
  Keritot 22a:19
Meilah (1):
  Meilah 10a:6
Nedarim (1):
  Nedarim 10a:14-10b:1
Niddah (1):
  Niddah 41a:8
Shevuot (1):
  Shevuot 11a:5
Taanit (1):
  Taanit 30b:12
Yevamot (1):
  Yevamot 106a:14
```

## Note

- For **Written verse addresses inside Bavli text** (not MH), use `cite_index` / `Lev.1.x`.
- MH answers: **which Oral places are traditionally parallel** to the Sifra on these verses.
