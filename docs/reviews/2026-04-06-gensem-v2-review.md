# Review Report v2 — ai4se6d_gensem

**Date**: 2026-04-06
**Module**: ai4se6d_gensem v2 (132 blocks)
**Reviewers**: SOTA coverage audit + quality review (72 new blocks) + v1/v2 integration review

---

## Executive Summary

**SOTA coverage**: Excellent — all major sections covered, no CRITICAL gaps.
**Code quality**: Good — consistent patterns, ruff passes, proper st_list/cite usage.
**Main issues**: (1) v1 blocks not updated with review fixes, (2) style duplication across ~40 blocks, (3) glossary too thin, (4) duplicate Fowler content, (5) 3 SOTA gaps worth addressing.

| Severity | Count |
|----------|-------|
| CRITICAL | 3 (all from unfixed v1 review) |
| MAJOR | 9 |
| MINOR | 10 |
| SUGGESTION | 7 |

---

## CRITICAL (must fix)

### CR1. v1 review fixes NOT applied — Forrester misrepresentation
**File**: `bck_gensem_roadmap.py` line 31
**Issue**: "50% of enterprises will attempt to replace developers" — source says "at least one org will try replacing 50% of devs." Materially different.
**Fix**: Correct text.

### CR2. v1 review fixes NOT applied — "90%+" unsourced claim
**File**: `bck_gensem_plugin_demo_compound.py` line 37
**Issue**: "AI generates correct code 90%+ on first attempt" — no citation or qualification.
**Fix**: Add "in our experience" or remove number.

### CR3. 15+ v1 blocks define factored styles locally
**Scope**: All v1 blocks (bck_gensem_sdlc_phases, ce_philosophy, ce_compound, calcapp_recap, method_overview, plugin_demo_brainstorm, roadmap, fw_se30, fw_vbounce, fw_agilegen, fw_multiagent, sdlc_evidence, sdlc_human, calcapp_v03_traceability, glossary, etc.)
**Issue**: Factored styles (heading, keyword, label, stat, source) now exist in custom/styles.py but v1 blocks still define them locally with slightly different compositions, creating visual inconsistency between v1 and v2 slides.
**Fix**: Update v1 blocks to use `s.project.titles.heading`, `.keyword`, `.label`, `.stat`, `.source`.

---

## MAJOR (should fix)

### MJ1. Duplicate Fowler content across 2 blocks
**Files**: `bck_gensem_human_fowler.py` (Part 1) + `bck_gensem_evidence_fowler.py` (Part 2)
**Issue**: Same quote, same talking points. Audience sees exact repetition.
**Fix**: Differentiate — Part 1 keeps Booch angle, Part 2 frames as evidence conclusion. Or remove one.

### MJ2. `closing` style duplicated in 15 new blocks
**Pattern**: `closing = s.project.titles.body + s.project.colors.highlight + s.bold`
**Fix**: Factor into custom/styles.py as `TextStylesCustom.closing`.

### MJ3. `card_title` style duplicated in 5 blocks
**Fix**: Factor into custom/styles.py.

### MJ4. `dont_callout`/`do_callout` styles with raw CSS in 2 blocks
**Files**: `ce_brainstorm_antipattern.py`, `ce_plan_antipattern.py`
**Fix**: Factor callout variants into ContainerStylesCustom.

### MJ5. `stat_hero` style duplicated in 3 blocks
**Fix**: Factor into custom/styles.py.

### MJ6. v1 framework blocks missing cite() calls
**Files**: `fw_se30.py`, `fw_vbounce.py`, `fw_agilegen.py`
**Issue**: Plain-text attributions ("Hassan et al.") instead of cite() calls.
**Fix**: Add proper cite() imports and calls.

### MJ7. v1 synthesis table symbols have no legend
**File**: `bck_gensem_fw_synthesis.py`
**Fix**: Replace symbols with descriptive labels or add legend.

### MJ8. Glossary too thin (9 terms vs 50+ in SOTA)
**Issue**: Missing essential terms: LLM, MCP, RAG, Context Engineering, Agent Mode, Hooks, SOP, CHOP, Hallucination, Automation Bias, AGENTS.md, etc.
**Fix**: Expand to ~25 terms. May need 2 glossary slides.

### MJ9. Cross-tool terminology dictionary missing
**SOTA gap**: Appendix B maps C1-C15 concepts to concrete names in Claude Code/Cursor/Copilot.
**Fix**: Add 1 block showing how key concepts (Project Rules, Agent Mode, Hooks, Memory, MCP, Skills) map across tools.

---

## MINOR (nice to fix)

| # | Issue | File(s) |
|---|-------|---------|
| m1 | METR estimate inconsistency: +20% vs +24% | evidence_perception vs evidence_metr |
| m2 | Missing Fowler/Karpathy/TOSEM bib entries + cite() | evidence_fowler, sdlc_codegen, human_creativity |
| m3 | `callout_body` useless alias in 9 blocks | 9 framework blocks |
| m4 | vbounce_diagram creates 3 redundant pt48 styles | fw_vbounce_diagram |
| m5 | `message` style duplicated in 6 blocks | fw_landscape, multiagent blocks, sdlc_spectrum |
| m6 | GenSE vs GenSEM terminology | calcapp_v03_traceability, calcapp_v03_prompts |
| m7 | v1 multiagent compact block redundant after v2 detail | bck_gensem_fw_multiagent in book.py |
| m8 | Junior/senior stats repeated on consecutive slides | sdlc_human → human_junior_senior |
| m9 | Ethics section thin — EU AI Act, responsibility gap, environmental cost missing | risks_overview |
| m10 | fw_landscape uses inline CSS margin | fw_landscape |

---

## SUGGESTIONS

| # | Suggestion |
|---|-----------|
| S1 | Split 15-task table into 2 slides (T1-T8, T9-T15) for projection readability |
| S2 | Split promptware crisis 8-step lifecycle into 2 columns or slides |
| S3 | Add "Study 1 of 3" progress indicators on RCT slides |
| S4 | Fix Part 4 block count comment in book.py (says 35, actual ~22) |
| S5 | Consider removing bck_gensem_fw_multiagent (v1 compact) — fully superseded by v2 detail blocks |
| S6 | Add Xiao longitudinal key finding to human factor section |
| S7 | Verify SWE-bench "March 2026" date accuracy |

---

## SOTA Coverage Summary

| SOTA Section | Coverage | Gaps |
|---|---|---|
| S2: GenAI Foundations | N/A (ai4se6d_genai_intro) | — |
| S3: GenAI in SE | Good | — |
| S4: SDLC Transformation | Excellent | — |
| S5: Frameworks | Excellent | MAISTRO mentioned but no dedicated slide (MINOR) |
| S6: Empirical Evidence | Excellent | Observational studies (Khojah, Ulfsnes) not individually covered (MINOR) |
| S7: Risks | Good | Ethics detail thin (m9) |
| S8: Human Factor | Excellent | — |
| S9: Tools & Concepts | Excellent | Cross-tool terminology missing (MJ9) |
| S10: Roadmaps | Good | Research gaps from synthesis not explicit (MINOR) |
| App A: CE | Excellent | — |
| App B: Terminology | Gap | Cross-tool dict missing (MJ9) |
| App C: Multi-Agent | Good | — |

---

## Prioritized Fix Plan

### Phase 1 — Critical + quick wins (automatable)
1. CR1: Fix Forrester text in roadmap block
2. CR2: Qualify "90%+" in plugin_demo_compound
3. MJ6: Add cite() to fw_se30, fw_vbounce, fw_agilegen
4. MJ7: Fix synthesis table with descriptive labels
5. m1: Fix METR +20% → +24% in evidence_perception
6. m6: Standardize GenSE → GenSEM terminology

### Phase 2 — Style factoring (systematic)
7. MJ2-MJ5: Factor closing, card_title, dont/do_callout, stat_hero into styles.py
8. CR3: Update all v1 blocks to use factored styles
9. m3-m5: Remove callout_body alias, fix vbounce_diagram, factor message style

### Phase 3 — Content additions (new blocks)
10. MJ8: Expand glossary to ~25 terms (split into 2 blocks)
11. MJ9: Add cross-tool terminology block
12. MJ1: Differentiate the 2 Fowler blocks
13. m7: Remove v1 multiagent compact from book.py
14. m9: Enrich risks_overview with ethics detail
