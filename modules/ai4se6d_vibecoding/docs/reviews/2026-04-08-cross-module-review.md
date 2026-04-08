# Cross-Module Coherence Review — AI4SE6D Training

**Date**: 2026-04-08
**Scope**: `ai4se6d_genai_intro` (46 blocks) | `ai4se6d_vibecoding` (42 blocks) | `ai4se6d_collection` (1 block)
**Reference sources**: KBSCI (sota-ai-4-se-EN.tex), TIAGOSLIDES (practicals/), schedule, program
**Reviewer**: Claude CE Review Agent (5-axis cross-module analysis)

---

## Executive Summary

**Overall coherence score: 62/100 — PARTIAL**

The three modules form a coherent narrative arc (GenAI fundamentals -> VibeCoding/VibeEngineering -> future GenSEM). However, significant issues exist across all 5 review axes:

- **4 CRITICAL** findings — must fix before the training (April 9)
- **8 MAJOR** findings — should fix, significantly impact quality
- **6 MINOR** findings — nice to fix
- **4 SUGGESTIONS** — future improvements

---

## Axis 1: Inter-Module Coherence

### C1 — CRITICAL: VibeCoding definition inconsistent across modules

| Source | Definition |
|--------|-----------|
| `genai_intro` glossary | "Intent-driven development paradigm where AI acts as your **pair programmer**, generating code from natural language descriptions" |
| `vibecoding` glossary | "Development where developers describe intent to AI and accept generated code **without closely reviewing** it" |
| `vibecoding` definition slide | "A practice where developers describe tasks to LLMs, accept generated code **without closely reviewing** its internal structure, and rely on results and follow-up prompts to guide changes." |
| KBSCI | Karpathy quote + 4 characteristics (intent, trust, conversation, low barrier) — emphasis on **without reviewing** |

**Issue**: `genai_intro` uses a positive/aspirational framing ("pair programmer") that contradicts the KBSCI and vibecoding's critical framing ("without reviewing"). A participant seeing VibeCoding defined as "pair programmer" in Part 1 will be confused when Part 2 redefines it as "accepting code without review."

**Impact**: Fundamental conceptual confusion on Day 1's core concept.

**Fix**: Align `genai_intro` glossary to: "Development practice where developers describe intent to AI and accept generated code without closely reviewing it (Karpathy, 2025)."

---

### C2 — CRITICAL: Statistics cite different survey years, creating contradictions

| Module | Stat | Value | Source |
|--------|------|-------|--------|
| `genai_intro` bck_poll_ai_result | AI adoption | **76%** | StackOverflow **2024** (`stackoverflow2024survey`) |
| `vibecoding` bck_recap | AI adoption | **84%** | StackOverflow **2025** (`stackoverflow-survey2025`) |
| `genai_intro` bck_poll_ai_result | Daily AI use | **63%** | StackOverflow **2024** |
| KBSCI | Daily AI use | **51%** | StackOverflow **2025** |
| `genai_intro` bck_poll_ai_result | Regular AI coding | **82%** | StackOverflow **2024** |
| KBSCI | Regular AI coding | **85%** | JetBrains **2025** |

**Issue**: Participants see "76% adoption" at 10:30 AM and "84% adoption" at 11:45 AM on the same day. The numbers contradict because they come from different survey years. This undermines credibility.

**Impact**: Audience trust in presented data. A participant WILL notice.

**Fix**: Standardize on the 2025 survey data (aligned with KBSCI). Update `genai_intro` to use `stackoverflow-survey2025` with 84%/51% stats, or clearly label the year on each stat.

---

### M1 — MAJOR: VibeEngineering glossary definition is vague in genai_intro

| Module | Definition |
|--------|-----------|
| `genai_intro` | "**Broader** engineering discipline that integrates AI tools across the full software development lifecycle" |
| `vibecoding` | "Engineering discipline integrating AI across the full SDLC" |

**Issue**: The word "broader" in genai_intro implies a comparison, but VibeCoding hasn't been formally defined yet at that point. Also, both definitions miss the core insight from KBSCI: VibeEngineering **reintroduces systematic SE discipline** (requirements, TDD, architecture, review) to AI-assisted development.

**Fix**: Align both to: "Engineering discipline that reintroduces systematic SE practices (requirements, TDD, architecture, review) into AI-assisted development."

---

### M2 — MAJOR: No shared bibliography — bibkeys diverge between modules

| Concept | genai_intro bibkey | vibecoding bibkey | KBSCI bibkey |
|---------|-------------------|-------------------|--------------|
| StackOverflow survey | `stackoverflow2024survey` | `stackoverflow-survey2025` | `stackoverflow-survey2025` |
| Gartner prediction | `gartner2025aiassistants` | — | `gartner-se2025` |
| Karpathy VibeCoding | — | `karpathy2025vibecoding` | `karpathy-vibecoding2025` |

**Issue**: Each module maintains an independent `.bib` file with different naming conventions and sometimes different sources. No shared bibliography ensures consistency.

**Fix**: Create a shared `references.bib` in `shared-blocks/static/` and have both modules reference it. Use KBSCI bibkeys as the standard.

---

### M3 — MAJOR: genai_intro teases VibeCoding but doesn't bridge properly

`genai_intro` ends with "Next: VibeCoding — AI as your pair programmer" (`bck_genai_takeaways`). This framing:
1. Uses "pair programmer" which contradicts the vibecoding module's definition
2. Doesn't mention the 15-min break between modules
3. No transition mechanism between the two st_book instances

**Fix**: Change closing to "Next: VibeCoding — from intent to code, and why it matters" and add a brief context-setting line.

---

### m1 — MINOR: Glossary overlap — 10 terms duplicated

Both modules define: AI, GenAI, LLM, GPT, NLU, RLHF, HHH, DALL-E, RAG, Foundation model. The genai_intro versions have full explanations; vibecoding versions are abbreviated. Not a contradiction, but participants see two glossaries in 2 hours with different detail levels.

**Suggestion**: Vibecoding glossary could reference "See GenAI Introduction glossary" for shared terms and only define its own terms (VibeCoding, VibeEngineering, TDD, BDD, CI/CD, Context Engineering, NFR, V&V, MCP).

---

## Axis 2: Coherence with KBSCI

### C3 — CRITICAL: genai_intro uses outdated 2024 survey data vs. KBSCI's 2025

See C2 above. The `genai_intro` module cites the **2024** StackOverflow survey throughout, while KBSCI uses the **2025** edition. Since the training claims to present current state-of-the-art, using year-old data when newer is available is a credibility issue.

**All genai_intro stats to update:**
- 76% -> 84% (adoption)
- 63% -> 51% (daily use)
- 82% -> 85% (regular coding, switch to JetBrains source)
- 90% by 2028 -> OK (Gartner, unchanged)

---

### M4 — MAJOR: Key KBSCI concepts missing from Day 1 modules

| KBSCI Concept | Expected in | Status |
|---------------|-------------|--------|
| CHOP (Chat-Oriented Programming) | genai_intro or vibecoding | **Missing** — relevant to VibeCoding principles |
| METR paradox (-19% slower for experts) | vibecoding Act II | **Missing** — powerful counterpoint to productivity claims |
| Trust decline (40%->29%) | genai_intro | **Missing** — relevant after showing adoption stats |
| Copilot RCT (+55.8%) | genai_intro or vibecoding | **Missing** — key empirical evidence |
| Junior vs Senior productivity gap | vibecoding | **Missing** — 27-39% vs 8-13%, nuances the narrative |

**Impact**: The training presents a simplified view when KBSCI has rich nuances. Participants who later read the SOTA will see gaps.

**Fix**: Priority additions: METR paradox (fits `bck_vibecoding_danger_paradox`), Copilot RCT (fits `bck_vibeeng_evidence`).

---

### M5 — MAJOR: Bibkey naming convention doesn't match KBSCI

Vibecoding module uses close-but-not-identical keys:
- `tihanyi2024formai` vs KBSCI `tihanyi-secure2024`
- `spracklen2024packages` vs KBSCI `spracklen-packages2025`
- `gitlab2024devsecops` vs KBSCI `gitlab-devsecops2025`
- `anthropic2025impact` vs KBSCI `anthropic-agentic2026`
- `bain2025techreport` vs KBSCI `bain2025`

**Impact**: Makes cross-referencing between training modules and KBSCI document difficult. If KBSCI evolves, updating modules requires mapping different bibkeys.

**Fix**: Adopt KBSCI bibkey naming convention as standard across all modules.

---

### m2 — MINOR: VibeCoding origin date discrepancy

Vibecoding module `bck_vibecoding_origin` correctly cites Karpathy January 2023 ("English is the hottest programming language") and February 2025 ("vibe coding" term). KBSCI confirms February 2025. **Aligned.** However, the module doesn't mention Collins Dictionary Word of the Year 2025, which KBSCI does.

---

### m3 — MINOR: Autonomy spectrum aligned (5 levels) but level names differ slightly

| Level | KBSCI | vibecoding |
|-------|-------|------------|
| 1 | Passive assistance | Passive assistance |
| 2 | Proactive copiloting | Proactive copiloting |
| 3 | Task-level delegation | Task-level delegation |
| 4 | Autonomous agents | Autonomous agents |
| 5 | Multi-agent orchestration | Multi-agent orchestration |

**Aligned.** No issue.

---

### m4 — MINOR: 4-level VibeCoding-to-VibeEngineering spectrum aligned

Both KBSCI and vibecoding module use: Naive VibeCoding -> Guided VibeCoding -> Structured VibeCoding -> VibeEngineering. **Aligned.**

---

## Axis 3: Coherence with TIAGOSLIDES

### C4 — CRITICAL: Act IV (8 blocks, ~20 min) heavily duplicates Tiago's 42-page tool deck

| Topic | vibecoding blocks | Tiago `01_tools_ecosystem.pdf` | Overlap |
|-------|-------------------|-------------------------------|---------|
| Autonomy spectrum (5 levels) | `bck_ide_autonomy` | Pages 5-15 | **Near-identical** |
| Cursor features | `bck_ide_cursor` (2 sub-slides) | Pages 16-25 | **HIGH** |
| Claude Code | `bck_ide_claude_code` (2 sub-slides) | Pages 26-30 | **HIGH** |
| Windsurf + Copilot | `bck_ide_others` (2 sub-slides) | Pages 31-38 | **HIGH** |
| Comparison matrix | `bck_ide_comparison` | Pages 39-40 | **HIGH** |
| MCP | `bck_ide_mcp` | Day 2 deck, MCP section | **MEDIUM** |
| Cursor rationale | `bck_ide_cursor_choice` | Pages 41-42 | **MEDIUM** |

**Issue**: Participants will see the autonomy spectrum, Cursor features, and tool comparison twice in the same morning. This wastes 15-20 min of the already over-budget vibecoding module and bores the audience.

**Impact**: The schedule gives NG 45 min for VibeCoding/VibeEngineering and then **shares** the 45-min tools slot with Tiago. Having 8 dedicated blocks in NG's module for tools is excessive.

**Fix**: Reduce Act IV to 2-3 slides maximum:
1. One "Autonomy Spectrum" overview (keep `bck_ide_autonomy`)
2. One "Your Tool: Cursor" transition slide (merge `bck_ide_cursor_choice`)
3. Drop or move to appendix: `bck_ide_cursor`, `bck_ide_claude_code`, `bck_ide_others`, `bck_ide_comparison`, `bck_ide_mcp`

---

### M6 — MAJOR: Exercise 2 (10 min VibeCoding) is redundant with FreeSelfApp (1h45)

| Item | vibecoding Exercise 2 | Tiago's FreeSelfApp |
|------|----------------------|---------------------|
| Duration | 10 min | 1h45 |
| Tool | Cursor | Cursor |
| Goal | Pure VibeCoding — describe, accept, don't read | Naive prototype — VibeCoding approach |
| Timing | ~11:20 AM (during 45-min slot) | 2:30 PM (afternoon) |

**Issue**: Both exercises have the same pedagogical goal: "experience naive VibeCoding." The 10-min version is too short to be meaningful, and the 1h45 version is the real exercise. Having both wastes time and confuses the exercise numbering.

**Fix**: Convert Exercise 2 to a **framing teaser** for the afternoon workshop: "This afternoon, you'll experience pure VibeCoding in the FreeSelfApp workshop. Here's what to watch for..." (2 min, no timer).

---

### M7 — MAJOR: Exercise 3 has no equivalent in Tiago's Day 1 schedule

Exercise 3 ("Redo with Discipline", 8 min) asks participants to redo with TDD. But there is NO corresponding afternoon workshop for disciplined VibeCoding. The FreeSelfApp is purely naive. Exercise 3 only makes sense if:
1. It's done standalone (but 8 min is too short)
2. It frames the Day 2 CalcApp v0.1 (TDD-based)

**Fix**: Reframe Exercise 3 as a **preview/teaser** for Day 2: "Tomorrow, you'll apply these principles to CalcApp. Here's a taste of the difference..."

---

## Axis 4: Temporal Coherence

### M8 — MAJOR: vibecoding module exceeds time slot by 25+ minutes

| Metric | Value |
|--------|-------|
| Allocated time | 45 min (11:00-11:45) |
| Current blocks | 42 (with sub-slides: ~65 slides) |
| Estimated duration | 70+ min |
| **Overrun** | **25+ min** |

**Breakdown by Act:**
- Opening (3 blocks): ~5 min
- Act I — VibeCoding concept (8 blocks): ~15 min
- Exercise 2 (1 block): ~12 min (with debrief)
- Act II — Reality Check (8 blocks): ~15 min
- Act III — VibeEngineering (10 blocks): ~15 min
- Exercise 3 (1 block): ~10 min
- Act IV — Tools (8 blocks): ~15-20 min
- Closing (3 blocks): ~5 min

**Biggest time sinks to cut:**
1. Act IV (8 blocks, ~20 min) -> 2 blocks (~3 min) = **save 17 min**
2. Exercise 2 (10 min) -> teaser (2 min) = **save 8 min**
3. Total savings: **25 min** — fits the slot

---

### m5 — MINOR: genai_intro is tight but feasible

46 blocks for 45 min. Assuming ~1 min/block average (many are billboards and transitions), this is tight but feasible at ~45-50 min. The 11 LLM pipeline blocks may slow things down if not presented briskly.

---

### S1 — SUGGESTION: Tools ecosystem slot (11:45-12:30) coordination unclear

The schedule gives 45 min for "Tools ecosystem" shared between NG and TS. Currently, NG has 8 blocks on tools (in vibecoding Act IV) and TS has `01_tools_ecosystem.pdf` (42 pages). Who presents what during this slot needs explicit coordination.

---

## Axis 5: Completeness vs. Program

### Program Day 1 Coverage Checklist

| Program Item | Module | Status |
|--------------|--------|--------|
| Definition of AI and generative AI | `genai_intro` bck_ai_definition -> bck_ai_vs_genai | **Covered** |
| Overview of available generative AI tools | `genai_intro` bck_genai_landscape + `vibecoding` Act IV | **Covered** (but duplicated with Tiago) |
| How language models work | `genai_intro` 11 blocks (pipeline, attention, prediction) | **Thoroughly covered** |
| Limitations, capabilities, and ethics | `genai_intro` bck_llm_capabilities, bck_llm_limitations, bck_ai_ethics | **Covered** |
| VibeCoding concepts | `vibecoding` Act I (8 blocks) | **Covered** |
| VibeCoding philosophy | `vibecoding` Act I + Act II (dangers) | **Covered** |
| Tools ecosystem: Cursor | `vibecoding` bck_ide_cursor | **Covered** (overlaps with TS) |
| Tools ecosystem: Windsurf | `vibecoding` bck_ide_others | **Covered** (overlaps with TS) |
| Tools ecosystem: Claude Code | `vibecoding` bck_ide_claude_code | **Covered** (overlaps with TS) |
| Tools ecosystem: Co-Pilot | `vibecoding` bck_ide_others | **Covered** (overlaps with TS) |
| Tools ecosystem: OpenAI Codex | — | **NOT covered** |
| Using a local code generation model (LLM code) | — | **NOT covered** |
| Installation and configuration | TS `02_installation_and_configuration.pdf` | Tiago's responsibility |
| Workshop: FreeSelfApp | TS practicals | Tiago's responsibility |

---

### m6 — MINOR: OpenAI Codex not covered

The program explicitly lists "OpenAI Codex" as a tool to cover. Neither NG's modules nor the visible Tiago slides address it. Codex was superseded by ChatGPT/API, but the program lists it.

**Fix**: Add a brief mention in the tool comparison or in genai_intro's landscape slide.

---

### S2 — SUGGESTION: Local LLM code generation not covered

The program mentions "Using a local code generation model (LLM code)." This is not covered in NG's modules. Check if Tiago covers it in `01_tools_ecosystem.pdf` (possible, as it mentions "Local LLMs" in the content analysis).

---

### S3 — SUGGESTION: Collection module lists gensem but module doesn't exist yet

`collection.toml` declares `ai4se6d_gensem` (order 3) with URL `https://ai4se6d-gensem.streamtex.org`. This module doesn't exist yet. The collection landing page will show a broken link.

**Fix**: Either create a placeholder module or remove it from `collection.toml` until ready.

---

### S4 — SUGGESTION: Day 3-6 content modules not yet created

The training program covers 6 days. Currently only Day 1 modules exist (genai_intro + vibecoding). Days 3-6 need:
- `ai4se6d_gensem` (Day 3: SE concepts, GenSEM, requirements)
- Day 4 content is mostly TS practicals
- Day 5-6 content is mostly mini-project + closing

---

## Consolidated Findings — Priority Matrix

| # | Severity | Axis | Finding | Effort |
|---|----------|------|---------|--------|
| C1 | CRITICAL | Inter-module | VibeCoding definition inconsistent ("pair programmer" vs "without reviewing") | Low — text change |
| C2 | CRITICAL | Inter-module | Statistics contradict (76% vs 84% same day, different survey years) | Medium — update bib + stats |
| C3 | CRITICAL | KBSCI | genai_intro uses outdated 2024 survey vs KBSCI's 2025 | Medium — update all stats |
| C4 | CRITICAL | TIAGOSLIDES | Act IV (8 blocks) duplicates Tiago's 42-page tool deck | **SKIPPED** — pedagogical choice: repetition reinforces retention. Trainer will pass quickly in session. |
| M1 | MAJOR | Inter-module | VibeEngineering glossary definition vague, misses "reintroduces SE discipline" | Low — text change |
| M2 | MAJOR | Inter-module | No shared bibliography, divergent bibkeys | Medium — create shared .bib |
| M3 | MAJOR | Inter-module | genai_intro closing teases "pair programmer", contradicts vibecoding | Low — text change |
| M4 | MAJOR | KBSCI | Key concepts missing (METR paradox, Copilot RCT, trust decline) | Medium — add content |
| M5 | MAJOR | KBSCI | Bibkey naming doesn't match KBSCI convention | Medium — rename all keys |
| M6 | MAJOR | TIAGOSLIDES | Exercise 2 redundant with FreeSelfApp workshop | Low — reframe text |
| M7 | MAJOR | TIAGOSLIDES | Exercise 3 has no practical counterpart in Day 1 | Low — reframe text |
| M8 | MAJOR | Temporal | vibecoding module 25+ min over budget (70 min for 45 min slot) | Medium — cut Act IV + exercises |
| m1 | MINOR | Inter-module | 10 glossary terms duplicated across modules | Low |
| m2 | MINOR | KBSCI | Collins Dictionary Word of Year 2025 not mentioned | Low |
| m3 | MINOR | KBSCI | Autonomy spectrum aligned (no issue) | None |
| m4 | MINOR | KBSCI | 4-level spectrum aligned (no issue) | None |
| m5 | MINOR | Temporal | genai_intro tight but feasible | None |
| m6 | MINOR | Completeness | OpenAI Codex not covered per program | Low |
| S1 | SUGGESTION | Temporal | Tools ecosystem slot NG/TS coordination unclear | Process |
| S2 | SUGGESTION | Completeness | Local LLM not covered (may be in TS slides) | Check |
| S3 | SUGGESTION | Completeness | Collection links to non-existent gensem module | Low |
| S4 | SUGGESTION | Completeness | Days 3-6 modules not yet created | Future work |

---

## Quick Wins (high impact, low effort)

1. **Fix VibeCoding definition** in genai_intro glossary (C1) — 1 line change
2. **Fix genai_intro closing** "pair programmer" phrasing (M3) — 1 line change
3. **Reframe Exercise 2** as teaser for FreeSelfApp (M6) — text change in 1 block
4. **Reframe Exercise 3** as Day 2 preview (M7) — text change in 1 block
5. **Fix VibeEngineering definition** in both glossaries (M1) — 2 line changes

## Recommended Action Plan

1. **Immediate (before April 9)**: Fix C1, C2, C3, C4, M3, M6, M7, M8
2. **Short-term**: Fix M1, M2, M4, M5
3. **Medium-term**: Address S3, S4 (gensem module creation)

---

## Deferred Actions (to apply after all fixes)

| # | Action | Description |
|---|--------|-------------|
| DA1 | **Fusionner les 3 references.bib en un fichier central** | Creer `shared-blocks/static/references.bib` unique, deduplication des ~50 entrees, harmonisation des bibkeys. Mettre a jour les `bib_sources` dans les 3 `book.py` pour pointer vers le fichier central (la variable `_shared_static` existe deja). Supprimer les `.bib` locaux. |

## Next Steps

- `/stx-ce:fix` — Auto-fix CRITICAL and MAJOR findings
- `/stx-ce:fix --severity MAJOR` — Include all MAJOR findings
- Re-run `/stx-ce:review` after fixes to validate
