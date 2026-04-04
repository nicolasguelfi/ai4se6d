# CE Review — ai4se6d_genai_intro (Session 1)

**Date**: 2026-04-03
**Guideline**: maximize-viewport
**Slides reviewed**: 45 wired blocks
**Perspectives**: 5/5 (audience, pedagogy, visual, style, editorial)

---

## Executive Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 3 |
| MAJOR | 13 |
| MINOR | 21 |
| SUGGESTION | 11 |
| **Total** | **48** |

The presentation is **well-structured and technically solid**, with strong StreamTeX conventions compliance (98/100 style score). The main concerns are **pedagogical scaffolding gaps** (no explicit learning objectives, long dense sequences without synthesis checkpoints) and **visual guideline partial compliance** (image aspect ratios, font hierarchy deviations). Content is accurate with minor editorial refinements needed. **Deliverable as-is**, but 4-5 targeted improvements would significantly increase audience retention.

---

## 1. Audience Advocate Review

### Findings

| ID | Severity | Block | Finding |
|----|----------|-------|---------|
| A01 | CRITICAL | bck_intro_objective | Missing duration/pacing info — schedule shows no time blocks or breaks |
| A02 | MAJOR | bck_ai_definition → bck_ai_era_genai | Conceptual jump: AI eras (slides 14-17) come AFTER discriminative/generative distinction (slides 12-13) that requires historical context |
| A03 | MAJOR | bck_llm_tokenization, bck_llm_vocabulary | Token examples lack cost/practical implications for developers |
| A04 | MAJOR | bck_llm_attention, bck_llm_attention_viz | Self-attention presented without prerequisite (why superior to RNNs) |
| A05 | MAJOR | bck_llm_how_work → bck_llm_alignment | Inference→training transition not clearly signposted |
| A06 | MAJOR | bck_llm_pretraining | "Emergent capabilities" used without definition |
| A07 | MAJOR | bck_llm_limitations | Hallucination severity understated for developer workflows |
| A08 | MINOR | bck_poll_ai_result | Statistics not attributed to individual sources |
| A09 | MINOR | bck_llm_context_window | Context window numbers lack real-world equivalents |
| A10 | MINOR | bck_genai_for_devs | "Architecture" capability vague for developers |
| A11 | MINOR | bck_ai_ethics | Privacy concern (data in prompts) underdeveloped |
| A12 | MINOR | bck_genai_landscape | Missing local/enterprise tools (Ollama, LM Studio, CodeWhisperer) |
| A13 | MINOR | bck_llm_transformer_demo | Interactive link has no usage guidance |
| A14 | SUGGESTION | bck_intro_roadmap | Days 2-6 lack brief descriptions |
| A15 | SUGGESTION | bck_ai_discriminative, bck_ai_generative | P(y|x)/P(x,y) notation too abstract — use developer examples |
| A16 | SUGGESTION | bck_llm_summary | Missing action-oriented developer takeaways |
| A17 | SUGGESTION | bck_llm_capabilities | "Reason & plan" overstated for current LLMs |

---

## 2. Pedagogy Analyst Review

### Findings

| ID | Severity | Block/Section | Finding |
|----|----------|---------------|---------|
| P01 | CRITICAL | Introduction (slides 1-8) | No explicit learning objectives — learners cannot calibrate expectations |
| P02 | CRITICAL | AI Fundamentals (slides 9-17) | 8 consecutive slides with identical structure, no cognitive breaks or synthesis |
| P03 | MAJOR | bck_poll_ai_experience/result | Poll not connected to instruction — results don't adjust pacing |
| P04 | MAJOR | LLM Inference (slides 26-35) | 10 dense technical slides without scaffolding checkpoints |
| P05 | MAJOR | bck_llm_teaser (slide 24) | "Next-token prediction" insight appears before prerequisite concepts are taught |
| P06 | MAJOR | LLM Engineering (slides 36-39) | Four critical phases compressed — no explicit comparison between them |
| P07 | MINOR | bck_ai_mccarthy | 1955 quote without bridge to modern GenAI relevance |
| P08 | MINOR | bck_genai_landscape | Tool categories not mapped to developer workflows |
| P09 | MINOR | bck_llm_capabilities/limitations | Limitations abstract — needs concrete failure examples |
| P10 | MINOR | bck_ai_ethics | Single slide for complex topic — no case studies or reflection |
| P11 | MINOR | Full presentation | Only 2 of 45 slides are interactive (poll + transformer demo link) |
| P12 | MINOR | bck_llm_tokenization → embeddings | 3 novel concepts in ~5 minutes, identical layout, no worked example |
| P13 | SUGGESTION | bck_trainer_ng/ts | Trainer profiles don't bridge to content relevance |
| P14 | SUGGESTION | bck_llm_summary | Synthesis slide appears too late (slide 40/45) — add intermediate summaries |

---

## 3. Visual Reviewer Report

### Findings

| ID | Severity | Block | Finding |
|----|----------|-------|---------|
| V01 | CRITICAL | All balanced image slides | Image cells lack explicit height constraint — portrait images (1024x1536) risk aspect ratio distortion on projection |
| V02 | MAJOR | bck_poll_ai_result | `stat_hero` hardcodes `font-size:96pt` via `ns()` instead of using project title hierarchy |
| V03 | MAJOR | Multiple balanced slides | Grid uses `2fr 3fr` (40/60) — inconsistent with guideline's balanced slide specification |
| V04 | MAJOR | bck_llm_attention_viz | `ai_size="1536x1024"` is 3:2, not 16:9 as prompt suffix claims |
| V05 | MAJOR | bck_features | `st_block(s.center_txt)` may override top-alignment for content slides |
| V06 | MINOR | bck_trainer_ng, bck_trainer_ts | Use `s.huge` instead of `s.project.titles.section_title` for name |
| V07 | MINOR | bck_intro_roadmap | Gap `0.8rem` while most blocks use `1.5rem` |
| V08 | MINOR | bck_poll_ai_result | `stat_hero` at 96pt used in content area, not as slide title |
| V09 | MINOR | bck_llm_how_built | Uses `s.Giant` — unclear if projection-safe (>= 96pt) |
| V10 | SUGGESTION | Multiple blocks | Cell padding inconsistency: `cell_pad_sm` vs `cell_pad_md` without clear rationale |
| V11 | SUGGESTION | Trainer profiles | Mix of `width="80%"` and `width="400px"` — prefer responsive units |

### Guideline Compliance

- **Status**: PARTIAL
- **Guideline**: maximize-viewport
- **Violations**:
  1. Image-to-text grid ratios not matching guideline specification
  2. Landscape image aspect ratio mismatch (3:2 vs claimed 16:9)
  3. Font sizes hardcoded outside hierarchy in 2 blocks
  4. Vertical spacing inconsistency across blocks
  5. No explicit dark theme contrast validation for 10-20m viewing

---

## 4. Style Consistency Checker Report

### Findings

| ID | Severity | Block/File | Finding |
|----|----------|-----------|---------|
| S01 | MINOR | bck_intro_round_table:52 | Missing `toc_lvl` in subtitle `st_write()` |
| S02 | MINOR | bck_llm_vocabulary:39-42 | Missing `toc_lvl` in secondary content lines |
| S03 | MINOR | bck_title:20 | Missing `toc_lvl` in subtitle vs. primary title |
| S04 | MINOR | bck_trainer_ng:134 | Missing `toc_lvl` in "More Information" heading |
| S05 | MINOR | bck_trainer_ts:111 | Missing `toc_lvl` in "More Information" heading |
| S06 | SUGGESTION | 26 blocks | Identical `body`/`keyword` style compositions — extract to `custom/styles.py` |
| S07 | SUGGESTION | 50 blocks | Identical `_page_fill` layout patterns — extract centered/top-aligned variants |

### Compliance Score: 98/100

- 100% BlockStyles + build() coverage
- 100% proper `from custom.styles import Styles as s` imports
- 100% Style composition operator usage
- 0 raw `st.write()` / `st.markdown()` / `st.html()` violations
- 0 hardcoded black/white colors
- 5 minor TOC navigation inconsistencies

---

## 5. Content Editor Review

### Findings

| ID | Severity | Block | Finding |
|----|----------|-------|---------|
| E01 | MAJOR | bck_ai_vs_genai | "GPT-3.5 sparked the revolution" — imprecise. GPT-3 (2020) vs ChatGPT (Nov 2022) distinction needed |
| E02 | MINOR | bck_llm_tokenization | Inconsistent dash characters (en dash – vs em dash —) |
| E03 | MINOR | bck_poll_ai_result | Source citations lack specific report names |
| E04 | MINOR | bck_intro_round_table | "VibeCoding" used without definition on first occurrence |
| E05 | MINOR | bck_llm_alignment | "HHH" acronym shown before expansion |
| E06 | MINOR | bck_features, bck_lists_demo, bck_grid_demo | Template/demo content — confirm exclusion from delivery |
| E07 | SUGGESTION | bck_poll_ai_result | "90% will use AI by 2028" — verify and cite specific Gartner report |
| E08 | SUGGESTION | bck_llm_pretraining | "Emergent" claim vague — needs specificity |
| E09 | SUGGESTION | bck_llm_tokens | Context window range "128K-1M" needs model attribution |

---

## Pattern Opportunities

| Pattern Name | Description | Blocks Affected |
|-------------|-------------|-----------------|
| `body-keyword-pair` | Generic `body` (Large + hyphens) + `keyword` (Large + bold + primary + hyphens) text styles | 26 blocks |
| `page-fill-centered` | Viewport-fill flex container with `justify-content: center` | 26 blocks |
| `page-fill-top` | Viewport-fill flex container with `justify-content: flex-start` | 24 blocks |
| `transition-question` | Giant + bold + center + highlight for billboard/transition slides | 4+ blocks |
| `image-size-presets` | Portrait `1024x1536` / Landscape `1536x1024` dimension aliases | 30+ blocks |

---

## Priority Actions

### Must fix before delivery (April 9)

1. **[P01] Add explicit learning objectives** to introduction section
2. **[A01] Add time blocks** to the schedule/objectives slide
3. **[A02/P02] Reorder AI eras** before discriminative/generative, add synthesis checkpoint
4. **[A05] Add clear section transition** between inference and training sequences
5. **[V04] Fix landscape aspect ratio** in bck_llm_attention_viz (3:2 → 16:9)

### Should fix (high impact)

6. **[A07/P09] Strengthen hallucination warning** with concrete developer examples
7. **[P04] Add 1-2 synthesis/reflection moments** in the 10-slide inference sequence
8. **[V02] Replace hardcoded font-size** in bck_poll_ai_result with style hierarchy
9. **[E01] Clarify GPT-3 vs ChatGPT timeline** in bck_ai_vs_genai
10. **[S06/S07] Extract shared patterns** to custom/styles.py (DRY improvement)

### Nice to have

11. Add intermediate summary slides after each major section
12. Increase interactive moments (polls, reflection prompts)
13. Standardize dash characters and source citations
14. Add concrete developer examples for tokenization costs and context windows

---

*Next step: `/stx-ce:fix` to address findings automatically*
