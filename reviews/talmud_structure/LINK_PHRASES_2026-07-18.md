# Link-like words and phrases (Bavli) — indexed

**Machine index:** `operator_index_2026-07-18.json` (all lines) · `operator_index_compact_2026-07-18.json` (samples by operator) · `link_phrases_2026-07-18.json` (catalog + counts)

Built: 2026-07-18 · Source: `Data/bavli_*_he.json` · ~81,793 lines tagged

---

## What we built

Every Bavli line gets:

| Field | Meaning |
|-------|---------|
| `primary` | First matching operator (priority order) |
| `operators[]` | All matching link/move phrases on that line |
| `flags` | hakha, hatam, vegu, scripture_cite, … |
| `opener` | First 1–2 Hebrew words |

Plus reverse lookup: **operator → sample locations**.

---

## Categories of links

### A. Scripture address (out to Written Torah)

| Id | Hebrew | Role |
|----|--------|------|
| SHENEEMAR | שנאמר | “as it is said” |
| DIKHTIV | דכתיב | “as written” |
| KETIV | כתיב | “it is written” |
| TALMUD_LOMAR | תלמוד לומר / ת״ל | “verse comes to teach” |
| VEGU | וגו׳ | “and the rest of the verse” |
| VEKU | וכו׳ | “etc.” |

*(Parenthetical letter-cites like `(ויקרא א, ה)` are in **cite_index**, not this file.)*

### B. Case pointers

| Id | Hebrew | Role |
|----|--------|------|
| HAKHA | הכא | here |
| HATAM | התם | there |
| HAKHA_NAMI | הכא נמי | here too |
| HATAM_NAMI | התם נמי | there too |
| KI_HA | כי הא | like this case |

### C. Load Oral source

| Id | Hebrew | Role |
|----|--------|------|
| MATNI | מתני׳ | Mishnah lemma |
| GEMARA | גמ׳ | enter Gemara |
| TENAN / DETANAN | תנן / דתנן | we learned (Mishnah) |
| TANYA / DETANYA | תניא / דתניא | it was taught (baraita) |
| TANU_RABBANAN | תנו רבנן | our rabbis taught |
| GUFA | גופא | back to main thread |
| HADRAN | הדרן עלך | end of chapter |

### D. Fetch / open question

| Id | Hebrew | Role |
|----|--------|------|
| TA_SHEMA | תא שמע | come and hear |
| MEITIVEI | מיתיבי | they object from a text |
| AITEIVEIH | איתיביה | he objected to him |
| MENALAN | מנלן | from where do we know? |
| LEIMA | לימא | shall we say |
| IBAAYA_LEHU | איבעיא להו | they asked |

### E. Branch / control

| Id | Hebrew | Role |
|----|--------|------|
| MAI | מאי | what? |
| MAI_TAAMA | מאי טעמא | what is the reason? |
| ELLA | אלא | rather |
| I_HACHI | אי הכי | if so |
| IBAIT_EIMA | איבעית אימא | if you want say |
| BISHLAMA | בשלמא | granted (often with אלא) |
| KASHYA | קשיא | difficulty |
| PESHITA | פשיטא | obvious |
| SHEMA_MINEH | שמע מינה | infer from this |
| ALMA | אלמא | hence |
| TEIKU | תיקו | leave unsolved |
| TIYUVTA | תיובתא | refutation |

### F. Authority / dialogue

| Id | Hebrew | Role |
|----|--------|------|
| AMAR | אמר | said |
| AMAR_LEIH | אמר ליה | he said to him |
| IKA_DEAMREI | איכא דאמרי | some say |
| MATKIF | מתקיף | challenges |

---

## Hit counts (operator appears on line; line can have several)

See `link_phrases_2026-07-18.json` → `hit_counts` for full list. Top primaries:

| Primary | ~lines |
|---------|--------|
| NONE (no tagged op) | ~23.5k |
| AMAR | ~10.5k |
| ELLA | ~7.0k |
| MAI | ~3.3k |
| AMAR_LEIH | ~3.1k |
| SHENEEMAR | ~2.2k |
| MATNI | ~2.2k |
| GEMARA | ~2.1k |
| DIKHTIV | ~2.1k |
| HAKHA | ~1.9k |
| TALMUD_LOMAR | ~1.6k |
| TA_SHEMA | ~1.4k |

**Flags:**

| Flag | ~lines |
|------|--------|
| scripture_cite (paren book cite) | ~9.0k |
| scripture_trigger (שנאמר/דכתיב/כתיב) | ~6.9k |
| hakha | ~3.0k |
| hatam | ~2.3k |
| hakha_hatam_both | ~1.0k |
| vegu | ~1.4k |

---

## Query examples

```bash
# How many lines are "come and hear"?
python3 -c "
import json
c=json.load(open('reviews/talmud_structure/operator_index_compact_2026-07-18.json'))
print(c['by_operator']['TA_SHEMA']['count_total_hits'])
print(c['by_operator']['TA_SHEMA']['locations_sample'][:3])
"

# Full line list (large file)
python3 -c "
import json
idx=json.load(open('reviews/talmud_structure/operator_index_2026-07-18.json'))
# lines where both hakha and hatam
both=[L for L in idx['lines'] if 'hakha_hatam_both' in L['flags']]
print(len(both), both[0])
"
```

---

## How this pairs with cite_index

| Index | Answers |
|-------|---------|
| **cite_index** | Where does Bavli **point at verse X**? |
| **operator_index** | What **move/link type** is this **line** doing? |

Together: *“Show TA_SHEMA lines that also cite Lev.1.5”* (join on tractate + daf + line, or re-scan).
