# Review Report -- AI4SE-NG Session 1

## Metadata

| Field | Value |
|-------|-------|
| Project | ai4se6d_genai_intro (migrated from AI4SE-NG on 2026-03-31) |
| Date | 2026-03-30 |
| Plan ref | 2026-03-27-001-C-session1-plan.md |
| Assess ref | 2026-03-27-session1-assess-C.md |
| Guideline | maximize-viewport |
| Blocks reviewed | 24 files (17 wired in book.py) |
| Plan target | ~128 slides across ~85 block files |

---

## Executive Summary

The project is at **~13% production** (17 wired blocks out of ~128 planned slides). Part 1 (GenAI Fundamentals) exists in compressed form, but **Part 2 (VibeCoding/VibeEngineering) is entirely absent** (0 of 62 slides). All interactive elements (polls, exercises, discussions) are missing. The existing blocks are technically sound and follow StreamTeX conventions well, but have visual inconsistencies and editorial issues that need fixing.

**Overall quality score: 3/10** (production completeness is the primary blocker)

### Key Metrics

| Metric | Plan | Current | Gap |
|--------|------|---------|-----|
| Part 1 slides | 66 | ~20 (compressed) | ~46 |
| Part 2 slides | 62 | 0 | 62 |
| Interactive slides | 20 | 0 | 20 |
| Exercise slides | 8 | 0 | 8 |
| Learning objectives (O1-O8) | 8 | O1-O4 partial | O5-O8 zero |

---

## Consolidated Findings

### CRITICAL (5 findings)

| # | Finding | Perspectives | Blocks |
|---|---------|-------------|--------|
| C1 | **Part 2 (VibeCoding/VibeEngineering) entirely missing** -- 62 slides, objectives O5-O8, the actionable half of the training | Audience, Pedagogy | ~40 missing block files |
| C2 | **All interactive elements missing** -- 5 polls/questions (12 slides) + 3 hands-on exercises (8 slides, 23 min) | Audience, Pedagogy | 20 missing slides |
| C3 | **"Today's Objectives" slide missing** (`bck_intro_objective`) -- learners have no upfront framing | Audience, Pedagogy | `bck_intro_objective` (missing) |
| C4 | **Transition slides lost vertical centering** -- `bck_ai_definition`, `bck_llm_how_work` use `flex-start` but these single-question slides should be centered like billboards (violates P1: "NEVER leave bottom 30% empty") | Visual | `bck_ai_definition`, `bck_llm_how_work` |
| C5 | **Template blocks lack `_page_fill` container** -- `bck_conclusion`, `bck_title` use `st_space()` filler instead of flex containers | Visual | `bck_conclusion`, `bck_title` |

### MAJOR (13 findings)

| # | Finding | Perspectives | Blocks |
|---|---------|-------------|--------|
| M1 | **AI historical eras missing** (Symbolic/ML/DL/GenAI, slides 8-11) -- contextual scaffolding for why GenAI is different | Audience, Pedagogy | 4 missing blocks |
| M2 | **Discriminative vs Generative distinction missing** (slides 12-15) -- foundational concept | Audience, Pedagogy | 4 missing blocks |
| M3 | **LLM pipeline detail insufficient** -- 4 blocks cover 16 planned slides; missing embeddings, attention detail, RLHF, context windows | Audience, Pedagogy | 12 missing blocks |
| M4 | **Provider-specific slides missing** (OpenAI, Anthropic, Google, open-weight, slides 38-41) | Audience | 4 missing blocks |
| M5 | **Autonomy spectrum + agentic turn missing** (slides 44-46) | Audience | 3 missing blocks |
| M6 | **`bck_llm_comparison` font size 36pt** -- below 48pt auditorium minimum, unreadable at 10-20m | Visual | `bck_llm_comparison` |
| M7 | **Hardcoded `s.text.colors.white`** in 2 blocks + hardcoded CSS gradient in trainer photo circle | Visual | `bck_intro_title`, `bck_trainer_team` |
| M8 | **`bck_genai_revolution` caption style conflict** -- `s.project.titles.caption + s.huge` creates 80pt caption (should be subordinate) | Visual | `bck_genai_revolution` |
| M9 | **`bck_ai_ethics` gap=32px** exceeds guideline 24px max for balanced columns | Visual | `bck_ai_ethics` |
| M10 | **AI prompt strings duplicated** across 7+ files -- identical `_PREFIX`/`_SUFFIX` should be factored out | Style | 7 block files |
| M11 | **Non-responsive grid columns** -- `"2fr 3fr"` won't wrap on narrow viewports (coding standards require `auto-fit`) | Style | 5 balanced slides |
| M12 | **"Universite du Luxembourg" missing accent** + inconsistent with English form used elsewhere | Editorial | `bck_trainer_team` |
| M13 | **Bullet points too long** in `bck_same_tools` -- multi-sentence prose instead of max 7-word slide bullets | Editorial | `bck_same_tools` |

### MINOR (15 findings)

| # | Finding | Blocks |
|---|---------|--------|
| m1 | Invalid CSS `justify-content:top` in `bck_llm_capabilities` (should be `flex-start`) | `bck_llm_capabilities` |
| m2 | `bck_same_tools` missing `st_block(s.center_txt)` centering wrapper | `bck_same_tools` |
| m3 | `bck_same_tools` uses `min-height:82vh` instead of standard `85vh` | `bck_same_tools` |
| m4 | `bck_genai_takeaways` uses `st_space("h", "2rem")` -- likely should be `"v"` | `bck_genai_takeaways` |
| m5 | Keyword styles lack `Style.create()` with unique IDs in 4 blocks | `bck_llm_capabilities`, `bck_llm_limitations`, `bck_ai_ethics`, `bck_genai_takeaways` |
| m6 | `_page_fill` container style duplicated across 18 blocks -- should be shared base style | All presentation blocks |
| m7 | `st.html()` used in `book.py` instead of `stx.st_html()` | `book.py` |
| m8 | Template/demo blocks still in codebase (not wired) | `bck_title`, `bck_features`, `bck_grid_demo`, `bck_lists_demo`, `bck_conclusion` |
| m9 | "sensitive data in prompts leaks" -- grammar issue (should be "can leak") | `bck_ai_ethics` |
| m10 | "ROS" unexplained abbreviation on team slide | `bck_trainer_team` |
| m11 | Duplicate "Who?" TOC entries from both trainer profiles | `bck_trainer_ng`, `bck_trainer_ts` |
| m12 | Subtitle split mid-phrase "Software / Development" | `bck_intro_title` |
| m13 | Transition text "Next: VibeCoding" but no Part 2 content follows | `bck_genai_takeaways` |
| m14 | Inconsistent heading styles: `slide_title` (96pt) vs `section_title` (80pt) on similar slides | Mixed |
| m15 | `book.py` zoom=90 but guideline recommends zoom=80 | `book.py` |

### SUGGESTIONS (8 findings)

| # | Finding |
|---|---------|
| S1 | Add prerequisites slide ("laptop, Cursor, ChatGPT + Claude accounts") |
| S2 | Extract shared "balanced slide" helper (heading + 2-col grid + image + bullets) |
| S3 | Add `object-fit: cover` for AI-generated images (prevent letterboxing) |
| S4 | Standardize heading hierarchy: `slide_title` for chapter openers, `section_title` for content |
| S5 | Formally establish abbreviation: "Generative AI (GenAI)" on first use |
| S6 | Consider timing markers as comments in `book.py` for presenter pacing |
| S7 | Prioritize polls/exercises over content slides if time is limited (active > passive) |
| S8 | Factor `_page_fill` and `_PREFIX/_SUFFIX` into shared modules |

---

## Guideline Compliance

| Status | **PARTIAL** |
|--------|-------------|
| Guideline | maximize-viewport |

| Principle | Status | Notes |
|-----------|--------|-------|
| P1 -- Content fills viewport | PARTIAL | Most blocks use `_page_fill` 85vh. Transition slides violate (C4). |
| P2 -- One clear hierarchy | PARTIAL | Caption conflict in `bck_genai_revolution` (M8). |
| P3 -- Images fill zone | OK | Consistent `width="80%"`. |
| P4 -- All content centered | PARTIAL | `bck_same_tools` misses centering wrapper. |
| P5 -- Spacing serves rhythm | PARTIAL | Template blocks use `st_space()` as filler. |
| No font below 48pt body | FAIL | `bck_llm_comparison` uses 36pt (M6). |
| No hardcoded colors | PARTIAL | `s.text.colors.white` in 2 blocks (M7). |

### Violations

- C4: `bck_ai_definition`, `bck_llm_how_work` -- transition slides not centered
- M6: `bck_llm_comparison` -- 36pt font below 48pt minimum
- M7: `bck_intro_title`, `bck_trainer_team` -- hardcoded white
- M8: `bck_genai_revolution` -- caption hierarchy broken
- M9: `bck_ai_ethics` -- gap 32px exceeds 24px max

---

## Pattern Opportunities

Recurring visual components that could be extracted as named patterns in `custom/design-guideline.md`:

| Pattern | Description | Blocks using it |
|---------|-------------|-----------------|
| `balanced-image-text` | 2fr/3fr grid, image left (80%), bullet list right, centered cells | 5 balanced slides |
| `transition-question` | Single centered question, 80pt+, centered vertically, billboard style | `bck_ai_definition`, `bck_llm_how_work` |
| `trainer-profile` | Photo + name + role + multi-grid detail slides | `bck_trainer_ng`, `bck_trainer_ts` |
| `stat-hero` | Giant statistic number + supporting context below | (planned: `bck_genai_adoption`) |
| `topic-bullets` | Title + centered 4-5 item bullet list, keywords highlighted | `bck_llm_capabilities`, `bck_llm_limitations`, `bck_genai_takeaways` |

---

## Plan vs. Existing: Coverage Table

| Plan Section | Planned | Existing | Coverage |
|---|---|---|---|
| Seq 1: Opening | 4 slides | 3 blocks | 75% |
| Q1: AI Usage Poll | 2 slides | 0 | 0% |
| Seq 2: What is AI? | 10 slides | 2 blocks | ~20% |
| Q2: LLM Question | 2 slides | 0 | 0% |
| Seq 3: How LLMs Work | 16 slides | 4 blocks | ~25% |
| Ex1: Compare LLMs | 2 slides | 0 | 0% |
| Seq 4: Tool Landscape | 10 slides | 2 blocks | ~20% |
| Seq 5: Capabilities & Limits | 14 slides | 2 blocks | ~14% |
| Q3 + Ethics | 4 slides | 1 block | ~25% |
| Seq 6: Transition | 2 slides | 1 block | ~50% |
| **Part 1 Total** | **66** | **15** | **~23%** |
| Part 2: VibeCoding/VibeEng | 62 slides | 0 | **0%** |
| **Grand Total** | **128** | **17 wired** | **~13%** |

---

## Recommended Fix Priority

### Immediate (before next production cycle)

1. Fix C4: Restore `justify-content:center` on transition slides (`bck_ai_definition`, `bck_llm_how_work`)
2. Fix m1: Change `justify-content:top` to `justify-content:flex-start` in `bck_llm_capabilities`
3. Fix M6: Increase `bck_llm_comparison` font sizes from 36pt to 48pt
4. Fix M9: Change gap from 32px to 24px in `bck_ai_ethics`
5. Fix M8: Remove `s.huge` from caption style in `bck_genai_revolution`

### Before April 9 delivery

6. Create `bck_intro_objective` (C3)
7. Create all interactive/exercise blocks (C2)
8. Produce Part 2 VibeCoding/VibeEngineering blocks (C1)
9. Expand compressed Part 1 blocks to planned granularity (M1-M5)

### Quality polish

10. Factor out `_PREFIX/_SUFFIX` prompt strings (M10)
11. Fix editorial issues (M12, M13, m9-m13)
12. Remove template blocks (m8)
13. Extract named patterns (S2, S8)

---

## Next Steps

- Run `/stx-ce:fix` to auto-correct the immediate technical findings (C4, m1, M6, M8, M9)
- Run `/stx-ce:produce` to continue block production against the plan
- Re-run `/stx-ce:review` after fixes to validate corrections
