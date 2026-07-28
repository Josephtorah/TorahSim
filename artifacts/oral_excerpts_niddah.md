# Oral excerpts used in Lev 12 model (web recovery)

**Provenance:** Pasted from web Grok recovery batch. Representation / study notes only.

---

## Talmud Niddah 31a (excerpt cited for doubled periods)

**Hebrew (fuller line from final web recovery):**  
ומפני מה אמרה תורה זכר לשבעה ונקבה לארבעה עשר? זכר שהכל שמחים בו מתחרטת לשבעה נקבה שהכל עצבים בה מתחרטת לארבעה עשר.

**English (as provided in web recovery):**  
"Since everyone is excited about a male child, she has remorse in a week. But for the female, where everyone is upset, it takes fourteen days for her to have remorse."

**Longer Hebrew context:** see `talmud_niddah_doubled_period_he.md` (extracted from local `Data/bavli_niddah_he.json`).

**Use in model:** Explains *why* impurity is doubled for a female birth (Lev 12:5 vs 12:2) in the Talmud derivation layer (`talmud_derive` in `lev12_torah_model.py`).

**Note:** Full sugya context is larger; this is the snippet the web model used. Local full Hebrew is in `Data/bavli_niddah_he.json` (do not modify unless asked).

---

## Mishnah Niddah 3:7 (excerpt)

**English (as provided in web recovery):**  
"If a woman miscarries on day 40, she need not consider it a fetus; day 41 — she should treat it as both boy and girl and as niddah."

**Use in model:** Edge-case operationalization of gender-period logic without always quoting Lev 12.

**Hebrew source:** See `artifacts/mishnah_niddah_ch3.md` (extract from `Data/mishnah_niddah_he.json`).
