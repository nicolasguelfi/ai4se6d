# Review Report — ai4se6d_gensem

**Date**: 2026-04-06
**Module**: ai4se6d_gensem (Generative Software Engineering Methods)
**Reviewers**: 5 parallel agents (audience, pedagogy, visual, style, editorial)
**Scope**: 60 block files, book.py, custom/*, static/references.bib

---

## Executive Summary

**Overall quality**: 3.5/5 — Structurally sound, content-rich module with strong practical sections (CalcApp mapping, GenSEMOne method). Key issues: content density exceeds projection-safe limits, massive style duplication, missing citations, and pedagogical gaps in exercise coverage.

| Severity | Count | Automatable |
|----------|-------|-------------|
| CRITICAL | 5 | 3 |
| MAJOR | 11 | 7 |
| MINOR | 13 | 10 |
| SUGGESTION | 9 | — |

---

## CRITICAL Findings

### C1. Font sizes do not match projection spec
**Source**: Visual reviewer
**Blocks affected**: ALL 60
**Issue**: `styles.py` docstring claims body=48pt, caption=32pt but actual rendered sizes are body=32pt (`Large_size`), caption=24pt (`large_size`). At 20m projection distance, 32pt body and 24pt caption are borderline/illegible.
**Fix**: Override font sizes in `TextStylesCustom` with explicit pt values or CSS variable overrides.
**Automatable**: YES

### C2. Day 3 AM slide volume exceeds time budget
**Source**: Audience advocate (confirmed by pedagogy)
**Blocks affected**: Parts 1-2 (28 slides in 60 min = ~2 min/slide)
**Issue**: Part 1 surveys 6 frameworks individually before synthesis. Professional developers will disengage around framework 3-4.
**Fix**: Reduce framework survey to 3 representative examples + synthesis table. Move detailed framework slides to appendix.
**Automatable**: NO (content decision)

### C3. Forrester prediction factually misrepresented
**Source**: Content editor
**File**: `bck_gensem_roadmap.py`
**Issue**: Slide says "50% of enterprises will attempt to replace developers" but source says "at least one org will try replacing 50% of devs." Materially different claims.
**Fix**: Correct the text to match the source.
**Automatable**: YES

### C4. Unsourced "90%+" claim
**Source**: Content editor
**File**: `bck_gensem_plugin_demo_compound.py`
**Issue**: "AI generates correct code 90%+ on first attempt" — no citation, no qualification.
**Fix**: Add qualifier ("in our experience") or cite source or remove the number.
**Automatable**: YES

### C5. LO4 Bloom's level mismatch
**Source**: Pedagogy analyst
**Issue**: Objective says "Design a lightweight GenSEM" but content teaches GenSEMOne as a recipe to follow (Apply level, not Create). Learners never actually design anything.
**Fix**: Either downgrade verb to "Apply" or add a 20-min customization workshop.
**Automatable**: NO (pedagogical decision)

---

## MAJOR Findings

### M1. Massive style duplication across BlockStyles (52+ blocks)
**Source**: Style consistency checker
**Issue**: 7 identical style compositions copy-pasted into local BlockStyles instead of custom/styles.py. Violates project rule "Any style used in 2+ blocks must be in custom/styles.py."
**Patterns**: heading (52 blocks), body alias (46), keyword (38), label (14), callout_text (11), source (8), stat (5).
**Fix**: Factor into custom/styles.py, update all blocks.
**Automatable**: YES

### M2. Missing cite() calls in 4+ blocks
**Source**: Content editor
**Files**: `fw_se30`, `fw_vbounce`, `roadmap`, `fw_agilegen`
**Issue**: Plain-text attributions ("Hassan et al.") instead of cite() calls. Year discrepancies: slides say 2024, bib says 2025 for SE 3.0 and V-Bounce.
**Fix**: Add proper cite() imports and calls, fix year consistency.
**Automatable**: YES

### M3. Content density too high on 5 slides
**Source**: Visual reviewer
**Files**: `glossary` (9 terms), `fw_multiagent` (4×3 items), `sdlc_phases` (6×3 items), `method_vs_vibecoding` (7 rows), `plugin_cursor` (long bullets)
**Fix**: Split dense slides or reduce items per slide.
**Automatable**: PARTIAL (splitting requires content judgment)

### M4. Framework comparison table uses opaque symbols
**Source**: Audience advocate + pedagogy
**File**: `bck_gensem_fw_synthesis.py`
**Issue**: Checkmarks and stars without legend. Audience cannot distinguish single/double check/star.
**Fix**: Use descriptive labels (Low/Medium/High) or add legend.
**Automatable**: YES

### M5. CE Compound phase has no hands-on exercise
**Source**: Pedagogy analyst
**Issue**: LO3 says "Apply the CE 5-phase workflow" but Phase 5 (Compound) is only observed in Day 6 demo, never practiced. Only 4/5 phases covered.
**Fix**: Add 10-min debrief exercise on Day 3: "Write 3 rules for .cursor/rules based on today's learnings."
**Automatable**: NO (new block needed)

### M6. Day 3/5/6 articulation is implicit
**Source**: Pedagogy analyst + audience advocate
**Issue**: No session-bridge blocks for Day 5 and Day 6 re-entry. After 1-day gaps, participants need re-orientation.
**Fix**: Add session-opening blocks for Day 5 and Day 6 with "where we left off / what's ahead."
**Automatable**: NO (new blocks needed)

### M7. CalcApp CE mapping timing adds up beyond stated 15-min framing
**Source**: Audience advocate
**File**: `bck_gensem_calcapp_v03_ce_mapping.py`
**Issue**: Mapped activities total 255+ min but Part 4 is only a 15-min framing. Temporal references ("today") are ambiguous.
**Fix**: Clarify this is an overview of ALL Day 3 activities, not just this 15-min slot.
**Automatable**: YES

### M8. GenSEMOne timing inconsistency: 5 FRs in CalcApp vs 8 FRs in timeline
**Source**: Pedagogy analyst
**Files**: `calcapp_v03_overview.py` (5 FRs) vs `method_timeline.py` (8 FRs)
**Issue**: CalcApp has 5 FRs, GenSEMOne timeline says "8 FRs × 30 min". These are different contexts but the inconsistency confuses.
**Fix**: Clarify that 8 FRs is for the mini-project, not CalcApp.
**Automatable**: YES

### M9. 2 image+text grids use non-responsive cols="2fr 3fr"
**Source**: Style consistency checker
**Files**: `fw_vbounce.py`, `sdlc_human.py`
**Fix**: Change to `repeat(auto-fit, minmax(300px, 1fr))`.
**Automatable**: YES

### M10. GitLab bib key year mismatch
**Source**: Content editor
**File**: `references.bib`
**Issue**: Key `gitlab2024devsecops` contains "2024" but `year = {2025}`.
**Fix**: Rename key to `gitlab2025devsecops` or `gitlab-devsecops2025`.
**Automatable**: YES

### M11. Plugin Part 3 (11 blocks) is entirely passive
**Source**: Pedagogy analyst
**Issue**: 11 slides of exposition with no learner activity on Day 6.
**Fix**: Add at least one "try this command" micro-exercise.
**Automatable**: NO (new content)

---

## MINOR Findings

| # | Source | Issue | File(s) | Fix |
|---|--------|-------|---------|-----|
| m1 | Editor | Terminology inconsistency: GenSE vs GenSEM vs GenSEMOne | calcapp_v03_traceability, calcapp_v03_prompts | Standardize terminology |
| m2 | Editor | Duplicate bib entries: `soen101-2024` and `qian2024soen101` | references.bib | Remove duplicate |
| m3 | Style | Hardcoded color #E74C3C in block file | plugin_demo_review.py | Move to ColorsCustom |
| m4 | Style | Inconsistent l_style parameter (18 blocks omit it) | ~18 blocks | Standardize on explicit l_style |
| m5 | Style | 2 BlockStyles classes lack docstrings | frameworks_title, sdlc_title | Add docstrings |
| m6 | Visual | Table text (36pt) larger than body text (32pt) — hierarchy inversion | Table blocks | Resolves when C1 is fixed |
| m7 | Visual | ce_five_phases grid minmax(150px) too narrow for 5 cols | ce_five_phases.py | Change to minmax(200px) or 3+2 layout |
| m8 | Visual | Emoji in CalcApp recap may not render on projectors | calcapp_recap.py | Replace with text labels |
| m9 | Editor | "Compound interest" analogy — geometric not exponential | ce_compound.py | Change "exponential" to "compounding" |
| m10 | Editor | Missing `# REF:` comments for statistics | sdlc_evidence, sdlc_phases, roadmap | Add REF comments |
| m11 | Audience | VibeCoding comparison is strawman (Day 1 only, not Day 2 progress) | method_vs_vibecoding.py | Consider adding middle column |
| m12 | Editor | SDLC phases statistics heterogeneous and misleading without context | sdlc_phases.py | Normalize metrics or add explanatory note |
| m13 | Audience | 80/20 rule needs evidence/example to avoid "waterfall" skepticism | ce_philosophy.py | Add before/after example from Day 1-2 |

---

## SUGGESTIONS

| # | Source | Suggestion |
|---|--------|-----------|
| S1 | Pedagogy | Add "Session Map" block showing 3-day delivery plan |
| S2 | Pedagogy | Add mini-quiz after Part 1 SOTA (3 formative check questions) |
| S3 | Pedagogy | Move method_vs_vibecoding earlier in Part 5 as motivational hook |
| S4 | Pedagogy | Add reflective pair-discussion exercise linking Day 1 to GenSEMOne |
| S5 | Audience | Add discussion prompt after CE philosophy slide |
| S6 | Audience | Method step3 should be a printable reference card |
| S7 | Visual | Add more diagrams (Mermaid) to break text-heavy slides |
| S8 | Visual | Use section_title style (teal) for subsection openers to create visual rhythm |
| S9 | Style | Add convenience alias for s.project.containers.page_fill_top |

---

## Prioritized Action Plan

### Phase 1 — Critical fixes (immediate)
1. **C1**: Fix font sizes in custom/styles.py (body→48pt, caption→32pt)
2. **C3**: Fix Forrester misrepresentation in roadmap block
3. **C4**: Qualify or remove "90%+" claim in plugin_demo_compound
4. **M1**: Factor 7 duplicated styles into custom/styles.py, update all 52+ blocks

### Phase 2 — Major fixes (high impact)
5. **M2**: Add cite() calls and fix year discrepancies
6. **M4**: Fix framework synthesis table with descriptive labels
7. **M7**: Clarify temporal references in CalcApp CE mapping
8. **M8**: Clarify FR count context (CalcApp 5 vs mini-project 8)
9. **M9**: Make 2 image+text grids responsive
10. **M10**: Fix bib key naming

### Phase 3 — Content/pedagogical decisions (user input needed)
11. **C2**: Reduce Part 1 framework survey (cut to 3 + synthesis?)
12. **C5**: Resolve LO4 Bloom's mismatch (downgrade verb or add workshop?)
13. **M5**: Add Compound exercise block
14. **M6**: Add Day 5 and Day 6 session-bridge blocks
15. **M11**: Add micro-exercise to plugin demo section

### Phase 4 — Minor fixes
16. All MINOR items (m1-m13)
