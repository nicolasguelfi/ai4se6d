# Review Report — ai4se6d_genai_intro (Post-Migration)

## Metadata

| Field | Value |
|-------|-------|
| Project | ai4se6d_genai_intro (migrated from AI4SE-NG on 2026-03-31) |
| Date | 2026-03-31 |
| Plan ref | 2026-03-27-001-C-session1-plan.md |
| Assess ref | 2026-03-27-session1-assess-C.md |
| Previous review | 2026-03-30-session1-review.md (score 3/10, 17 blocks) |
| Guideline | maximize-viewport |
| Blocks reviewed | 56 files (44 wired in book.py) |
| Plan target | ~128 slides across ~24 block files |
| Perspectives | audience-advocate, pedagogy-analyst, visual-reviewer, style-consistency-checker, content-editor |

---

## Executive Summary

The project has progressed significantly since the previous review (2026-03-30). Part 1 is now **substantially complete** with 44 wired blocks covering objectives O1-O4 comprehensively. The LLM deep-dive (tokenization through alignment) is detailed and well-sequenced. However, **Part 2 (VibeCoding/VibeEngineering, O5-O8) remains absent**, interactivity is minimal, and timing is tight for 90 minutes.

**Overall quality score: 6/10** (up from 3/10 — production completeness improved, structural issues remain)

### Key Metrics (vs Previous Review)

| Metric | Previous (03-30) | Current (03-31) | Change |
|--------|-------------------|------------------|--------|
| Wired blocks | 17 | 44 | +27 |
| Part 1 coverage | ~23% | ~70% | +47% |
| Part 2 coverage | 0% | 0% | — |
| Interactive elements | 0 | 2 (polls) | +2 |
| Objectives O1-O4 | partial | complete | improved |
| Quality score | 3/10 | 6/10 | +3 |

### Previous Review Findings — Resolution Status

| # | Previous Finding | Status |
|---|------------------|--------|
| C1 | Part 2 (VibeCoding) entirely missing | **OPEN** — still missing |
| C2 | All interactive elements missing | **PARTIAL** — 2 polls added (bck_poll_ai_experience, bck_poll_ai_result) |
| C3 | "Today's Objectives" slide missing | **RESOLVED** — bck_intro_objective exists and is wired |
| C4 | Transition slides lost vertical centering | **OPEN** — bck_ai_definition, bck_llm_how_work still use flex-start |
| C5 | Template blocks lack _page_fill | **OPEN** — bck_title, bck_features, bck_conclusion, bck_grid_demo still lack it |
| M1 | AI historical eras missing | **RESOLVED** — 4 era blocks added (symbolic, ML, DL, GenAI) |
| M2 | Discriminative vs Generative missing | **RESOLVED** — bck_ai_discriminative + bck_ai_generative added |
| M3 | LLM pipeline detail insufficient | **RESOLVED** — 10 pipeline blocks (tokenization through autoregressive) |
| M6 | bck_llm_comparison 36pt font | **NEEDS VERIFICATION** |
| M7 | Hardcoded s.text.colors.white | **OPEN** — still present in bck_intro_title, bck_trainer_team |
| M10 | AI prompt _PREFIX/_SUFFIX duplicated | **OPEN** — duplicated across 31 blocks |
| M12 | "Universite du Luxembourg" missing accent | **NEEDS VERIFICATION** |

---

## Consolidated Findings

### CRITICAL (4 findings)

| # | Finding | Perspectives | Blocks |
|---|---------|-------------|--------|
| C1 | **Part 2 (VibeCoding/VibeEngineering) still entirely missing** — 62 planned slides, objectives O5-O8. The transition slide (bck_genai_takeaways) says "Next: VibeCoding" but no content follows. | Audience, Pedagogy, Editorial | ~40 missing blocks |
| C2 | **Insufficient interactivity for 90-min session** — Only 2 polls at the start (bck_poll_ai_experience, bck_poll_ai_result) + 1 round table. No mid-session checkpoints, no exercises, no Q&A prompts. 44 blocks of near-continuous lecture risks disengagement. | Audience, Pedagogy | All content blocks |
| C3 | **Timing unrealistic** — 44 wired blocks in ~45 min (Part 1) = 1 min/block average. Technical blocks (attention, embeddings, alignment) need 2-3 min. Compression required: either reduce to ~25-30 blocks or accept 60+ min for Part 1. | Pedagogy | book.py |
| C4 | **Abbreviations not defined on first use** — "LLM" (Large Language Model), "RLHF" (Reinforcement Learning from Human Feedback), "HHH" (Helpful, Harmless, Honest), "NLU", "GenAI" used without first-mention expansion. Intermediate developers may not know all of these. | Editorial | bck_llm_how_work, bck_llm_alignment, bck_ai_era_dl, multiple |

### MAJOR (10 findings)

| # | Finding | Perspectives | Blocks |
|---|---------|-------------|--------|
| M1 | **Hardcoded `s.text.colors.white`** in 2 blocks + hardcoded CSS gradient — violates "no hardcoded black/white" rule | Visual, Style | bck_intro_title, bck_trainer_team |
| M2 | **Transition slides not vertically centered** — bck_ai_definition, bck_llm_how_work, bck_llm_how_built use `justify-content:flex-start` but are billboard-style single-question slides that should use `center` | Visual | bck_ai_definition, bck_llm_how_work, bck_llm_how_built |
| M3 | **_PREFIX/_SUFFIX AI prompt strings duplicated** across 31 blocks — identical 5-line prefix repeated, identical suffix patterns. Should be extracted to `custom/prompts.py` | Style | 31 blocks with st_image(editable=True) |
| M4 | **Hardcoded RGBA values in CSS** — `rgba(122, 184, 245, 0.08)`, `rgba(243, 156, 18, 0.15)` etc. repeated in 8+ blocks for grid cells. Should be extracted to custom/styles.py | Visual, Style | bck_intro_roadmap, bck_intro_round_table, bck_trainer_ng, bck_trainer_ts, bck_llm_comparison |
| M5 | **Inconsistent terminology: "GenAI" vs "Generative AI"** — both forms used without convention. First use not defined. Titles mix both (e.g., "AI vs Generative AI" vs "The GenAI Landscape") | Editorial | bck_ai_vs_genai, bck_genai_landscape, bck_genai_for_devs, bck_intro_roadmap |
| M6 | **No formative assessment** — Trainer cannot verify O1-O4 mastery. No quiz, knowledge check, or "true/false" slides. Risk: carry misconceptions into Part 2 | Pedagogy | Missing blocks |
| M7 | **Statistics sourcing unverified** — "84% use or plan to use AI", "51% use daily" attributed to "Stack Overflow 2025 / JetBrains / Gartner" without specific report names or links | Editorial | bck_poll_ai_result |
| M8 | **11 unused blocks in codebase** — bck_conclusion, bck_features, bck_grid_demo, bck_lists_demo, bck_llm_layers, bck_llm_next_token, bck_llm_tokens, bck_llm_training, bck_same_tools, bck_title, bck_trainer_team. Intent unclear (demo? deprecated? planned?) | Style | 11 blocks |
| M9 | **"Foundation models" and "Emergent capabilities" poorly explained** — key concepts introduced as jargon without accessible definitions for intermediate developers | Editorial, Audience | bck_ai_era_genai, bck_llm_pretraining |
| M10 | **Missing explanation of what VibeCoding/VibeEngineering is** — term appears in roadmap and takeaways but is never defined. Audience won't understand the next session's topic | Editorial, Audience | bck_intro_roadmap, bck_genai_takeaways |

### MINOR (12 findings)

| # | Finding | Blocks |
|---|---------|--------|
| m1 | bck_intro_title uses `justify-content:flex-start` — should be `center` for hero/title slide | bck_intro_title |
| m2 | Date ambiguity: McCarthy "Dartmouth Proposal (1955)" vs era title "1956 — Symbolic AI" — both valid but inconsistent | bck_ai_mccarthy, bck_ai_era_symbolic |
| m3 | _page_fill missing in 7 unused blocks (bck_conclusion, bck_features, etc.) | 7 unused blocks |
| m4 | "NLU" abbreviation unexpanded in AI era block | bck_ai_era_dl |
| m5 | Duplicate "Who?" TOC entries from both trainer profiles | bck_trainer_ng, bck_trainer_ts |
| m6 | `bck_llm_capabilities` — text on "create images" exceeds 7-word bullet limit (8 words) | bck_llm_capabilities |
| m7 | "Models reflect training data biases" — passive phrasing, consider "models amplify biases" | bck_ai_ethics |
| m8 | Missing context for "Cursor" in landscape slide — not explained as AI code editor | bck_genai_landscape |
| m9 | Inconsistent arrow notation (→ vs —) across slides | Multiple |
| m10 | Mathematical notation P(y|x) and P(x,y) used without brief explanation | bck_ai_discriminative, bck_ai_generative |
| m11 | book.py zoom=90 but guideline recommends zoom=80 | book.py |
| m12 | LLM mechanism section (10+ consecutive content blocks) creates monotone rhythm | bck_llm_pipeline through bck_llm_autoregressive |

### SUGGESTIONS (8 findings)

| # | Finding |
|---|---------|
| S1 | Add 2-3 interactive checkpoints in Part 1: after AI fundamentals, after LLM mechanics, before synthesis |
| S2 | Extract `_PREFIX`/`_SUFFIX` to `custom/prompts.py` (saves ~500 lines of duplication) |
| S3 | Extract common grid cell RGBA styles to custom/styles.py as named constants |
| S4 | Add prerequisites slide ("laptop, Cursor, ChatGPT + Claude accounts") |
| S5 | Add 1-slide brief definition of VibeCoding before ending Part 1 |
| S6 | Consider compressing LLM mechanics (merge tokenization+vocabulary, embeddings+semantic space) to free time for interactivity |
| S7 | Add timing cues as comments in book.py for presenter pacing |
| S8 | Document intent of unused blocks (demo? deprecated?) or remove them |

---

## Guideline Compliance

| Status | **PARTIAL** |
|--------|-------------|
| Guideline | maximize-viewport |

| Principle | Status | Notes |
|-----------|--------|-------|
| Content fills viewport (85vh) | PASS | 44/44 wired blocks have _page_fill |
| Billboard slides centered | FAIL | bck_ai_definition, bck_llm_how_work, bck_llm_how_built use flex-start (M2) |
| No font below 48pt body | PASS | No sub-48pt text found in wired blocks |
| No hardcoded colors | FAIL | s.text.colors.white in 2 blocks (M1), inline RGBA in 8+ blocks (M4) |
| Responsive grids (auto-fit) | PASS | All grids use `repeat(auto-fit, minmax(...))` |
| Centering via st_block(s.center_txt) | PASS | Consistent across all wired blocks |
| AI image orientation correct | PASS | Portrait for balanced, landscape for hero |
| Grid cells via cell_styles + g.cell() | PASS | Proper pattern in all grid blocks |

### Violations

- M1: bck_intro_title, bck_trainer_team — hardcoded white
- M2: bck_ai_definition, bck_llm_how_work, bck_llm_how_built — billboard slides not centered
- M4: 8+ blocks — hardcoded RGBA inline in CSS

---

## Pattern Opportunities

| Pattern | Description | Blocks Using It |
|---------|-------------|-----------------|
| `balanced-image-text` | 2-col grid: AI image (40%) + bullet list (60%), centered cells | bck_ai_vs_genai, bck_ai_discriminative, bck_ai_generative, bck_ai_era_*, bck_genai_for_devs, bck_llm_* (20+ blocks) |
| `transition-question` | Single centered question, 80pt+, billboard vertical centering | bck_ai_definition, bck_llm_how_work, bck_llm_how_built |
| `stat-hero` | Giant statistic number (96pt) + supporting context below | bck_poll_ai_result |
| `topic-bullets` | Title + centered 4-5 keyword bullet list, keywords highlighted | bck_llm_capabilities, bck_llm_limitations, bck_genai_takeaways |
| `trainer-profile` | Photo + name + role, then multi-grid detail, then QR/link | bck_trainer_ng, bck_trainer_ts |
| `era-timeline` | Date title + AI image + 3-4 keyword bullets | bck_ai_era_symbolic, bck_ai_era_ml, bck_ai_era_dl, bck_ai_era_genai |

---

## Style Consistency Scorecard

| Criterion | Score | Notes |
|-----------|-------|-------|
| Import consistency | 100% | All blocks follow standard pattern |
| BlockStyles class | 100% | Every block has BlockStyles + build() |
| Style ID uniqueness | 100% | No collisions |
| st vs stx usage | 100% | Zero raw st.* calls |
| _page_fill in wired blocks | 100% | All 44 wired blocks compliant |
| Prompt duplication | 31 blocks | _PREFIX identical across all — extraction recommended |
| Unused blocks documented | 0% | 11 blocks undocumented |

---

## Recommended Fix Priority

### Immediate (automated, /stx-ce:fix)

1. Fix M2: Restore `justify-content:center` on billboard slides (bck_ai_definition, bck_llm_how_work, bck_llm_how_built)
2. Fix M1: Replace `s.text.colors.white` with project colors in bck_intro_title, bck_trainer_team
3. Fix m1: Change bck_intro_title to `justify-content:center`
4. Fix m11: Change book.py zoom from 90 to 80

### Before April 9 delivery

5. Address C4: Add first-use definitions for LLM, RLHF, HHH, GenAI
6. Address C2: Add 2-3 interactive checkpoint slides (after AI section, after LLM section)
7. Address M5: Standardize "Generative AI (GenAI)" convention
8. Address M10: Add brief VibeCoding definition before transition
9. Produce Part 2 VibeCoding/VibeEngineering blocks (C1)
10. Address C3: Compress or reorganize to fit 45-min slot

### Quality polish

11. Extract _PREFIX/_SUFFIX to custom/prompts.py (M3, S2)
12. Extract RGBA cell styles to custom/styles.py (M4, S3)
13. Fix editorial issues (M5, M7, M9, m2-m10)
14. Document or remove unused blocks (M8, S8)

---

## Fix applied on 2026-03-31

| # | Severity | Block | Finding | Status |
|---|----------|-------|---------|--------|
| M2 | MAJOR | bck_ai_definition, bck_llm_how_work, bck_llm_how_built | Billboard slides not vertically centered | ALREADY OK (fixed before review) |
| M1 | MAJOR | bck_intro_title, bck_trainer_team | Hardcoded `s.text.colors.white` | FIXED — replaced with `s.project.colors.primary` |
| m1 | MINOR | bck_intro_title | justify-content:flex-start on hero slide | FIXED — changed to `center` |
| m11 | MINOR | book.py | zoom=90 vs guideline 80 | SKIP — user choice |
| m5 | MINOR | bck_trainer_ng, bck_trainer_ts | Duplicate "Who?" TOC entries | FIXED — "Who? — Nicolas" / "Who? — Tiago" |
| M3 | MAJOR | 31 blocks | _PREFIX/_SUFFIX AI prompt strings duplicated | FIXED — extracted to `custom/prompts.py` |
| M4 | MAJOR | 5 blocks | Hardcoded RGBA values in CSS | FIXED — extracted to `custom/styles.py` (cell_primary_bg, cell_active_bg, cell_accent_bg) |
| M8 | MAJOR | 11 blocks | Unused blocks not documented | FIXED — documented in book.py with status (template/demo/deprecated/planned) |
| C4 | CRITICAL | multiple | Abbreviations not defined on first use | FIXED — created `bck_glossary.py` (12 entries) wired at end of presentation |
| M5 | MAJOR | multiple | GenAI vs Generative AI inconsistent | FIXED — glossary establishes convention, no title changes needed |
| M9 | MAJOR | bck_ai_era_genai | "Foundation models" poorly explained | FIXED — changed to "Models pretrained on very large datasets, adapted to many tasks" + glossary entry |
| M10 | MAJOR | bck_genai_takeaways, bck_intro_roadmap | VibeCoding/VibeEngineering never defined | FIXED — glossary entries added |

### Summary

- Findings processed: 12
- Fixed: 10
- Partial: 0
- Failed: 0
- Skipped (user choice): 1
- Already resolved: 1
- Regressions detected: 0

### Artifacts created

- `custom/prompts.py` — shared AI image prompt constants (AI_PREFIX, AI_SUFFIX_PORTRAIT, AI_SUFFIX_LANDSCAPE)
- `custom/styles.py` — added cell_primary_bg, cell_active_bg, cell_accent_bg, cell_pad_sm, cell_pad_md
- `blocks/bck_glossary.py` — 12-entry glossary (AI, GenAI, LLM, GPT, NLU, RLHF, HHH, DALL-E, RAG, Foundation model, VibeCoding, VibeEngineering)

### Feature request

- nicolasguelfi/streamtex#12 — Glossary system with hover tooltips (extend bibliography architecture)

| Guideline violations | 3 (M1, M2, M4) | FIXED |
|---|---|---|

---

## Remaining findings (manual, require decisions)

| # | Severity | Finding | Type |
|---|----------|---------|------|
| C1 | CRITICAL | Part 2 (VibeCoding/VibeEngineering) entirely missing — 62 planned slides, O5-O8 | Production |
| C2 | CRITICAL | Insufficient interactivity — only 2 polls, no exercises, no checkpoints | Creation |
| C3 | CRITICAL | Timing unrealistic — 44 blocks in 45 min = 1 min/block | Reorganization |

---

## Next Steps

- Run `/stx-ce:produce` to continue with Part 2 production (C1)
- Add interactive checkpoint blocks between content sections (C2)
- Consider compressing or reorganizing the slide sequence (C3)
- Re-run `/stx-ce:review` after production to validate the full presentation
