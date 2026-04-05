# Training Context Analysis — AI4SE6D

**Date**: 2026-04-04
**Task**: Consolidate all training sources into a unified reference for document production alignment.

---

## 1. Training Overview

| Field | Value |
|-------|-------|
| Title | VibeEngineering: The Future of Software Development with Generative AI |
| Duration | 6 days (42 hours), 9am–5pm |
| Dates | April 9-10, 16-17, 23-24, 2026 |
| Location | DLH Luxembourg |
| Audience | 5-20 professional software developers (intermediate level) |
| Prerequisites | Solid experience in TypeScript, Python, Git |
| Language | English (trainers speak French and English) |
| Trainers | Dr. Prof. Nicolas Guelfi (NG) — theory + methodology; Tiago Sousa (TS) — tools + practicals |
| Primary tool | Cursor (Days 1-5), Claude Code (Day 6 demo) |
| Case study | CalcApp (personal finance budgeting webapp) — 5 branches for progressive iterations |
| Mini-project | Day 5-6 — participants build their own professional project |

---

## 2. Session Map — Day-by-Day Structure

### Day 1 (April 9) — Introduction and Fundamentals

| Half | Step | Content | Duration | Trainer | Module |
|------|------|---------|----------|---------|--------|
| AM | 1 | Training Group Discovery | 45 min | NG | — |
| AM | 2 | Training Content overview | 15 min | NG | — |
| AM | 3 | Introduction to GenAI fundamentals | 45 min | NG | `ai4se6d_genai_intro` |
| AM | 4 | Break | 15 min | | |
| AM | 5 | Discovering VibeCoding / VibeEngineering | 45 min | NG | `ai4se6d_vibecoding` |
| AM | 6 | Tools ecosystem | 45 min | NG+TS | `ai4se6d_vibecoding` (Act IV) + TS `01_tools_ecosystem.pdf` |
| PM | 1 | Installation and configuration | 60 min | TS | `02_installation_and_configuration.pdf` |
| PM | 2 | Workshop "FreeSelfApp" — Naive prototype Part 1 | 60 min | TS | FreeSelfApp (naive VibeCoding) |
| PM | 3 | Break | 15 min | | |
| PM | 4 | Workshop "FreeSelfApp" Part 2 | 45 min | TS | FreeSelfApp continued |
| PM | 5 | Debrief & Discussion | 30 min | NG+TS | — |

**Key observations for ai4se6d_vibecoding:**
- The module has **45 min** in the schedule (step 5), but the current ~65 slides / ~70 min exceeds this
- The Tools ecosystem step (6) overlaps with Tiago's `01_tools_ecosystem.pdf` — need to coordinate who covers what
- The PM FreeSelfApp workshop (1h45) is the Day 1 practical — it aligns with Exercise 2 in the vibecoding module
- Exercise 2 in the module (10 min) appears redundant with the much longer FreeSelfApp workshop (1h45)

### Day 2 (April 10) — Mastering Cursor

| Half | Step | Content | Duration | Trainer |
|------|------|---------|----------|---------|
| AM | 1 | Advanced Cursor Guided Demos + Project structure | 90 min | TS |
| AM | 2 | Break | 15 min | |
| AM | 3 | Workshop: Technical Planning Presentation | 30 min | TS |
| AM | 4 | CalcApp v0.1 Project Part 1 | 45 min | TS |
| PM | 1 | CalcApp v0.2 Project Part 2 | 45 min | TS |
| PM | 2 | AI-assisted code review & Living documentation Intro | 45 min | TS |
| PM | 3 | Break | 15 min | |
| PM | 4 | AI-assisted code review practice | 60 min | TS |
| PM | 5 | Introduction to Git | 45 min | TS |

**Topics covered by TS (Day 2 deck: 234 pages):**
- AI-friendly project structure, system prompts (`.cursor/rules/*.mdc`)
- Context windows and @-mentions, `.cursorignore`
- Plan mode vs Act mode, todo system
- MCP (Model Context Protocol), Context7
- TDD in 5 minutes (Red-Green-Refactor), AI-TDD discipline
- CalcApp scaffolding: Vite + React + TypeScript + Vitest
- AI-assisted code review (1.7x more issues per PR), living documentation
- Git fundamentals + 3 AI-specific patterns

### Day 3 (April 16) — Methodology and Requirements

| Half | Step | Content | Duration | Trainer |
|------|------|---------|----------|---------|
| AM | 1 | SE Concepts — Defining your GenSEM | 60 min | NG |
| AM | 2 | Practice on CalcApp v0.3 — VibeTesting | 45 min | TS |
| AM | 3 | Break | 15 min | |
| AM | 4 | Requirements elicitation methods | 45 min | NG |
| AM | 5 | Workshop: Drafting Functional Requirements — CalcApp v0.3 | 45 min | TS |
| PM | 1 | Non-functional requirements (NFR) — Theory | 45 min | NG |
| PM | 2 | Practice on CalcApp — VibeNFRs v0.3 | 45 min | TS |
| PM | 3 | Break | 15 min | |
| PM | 4 | Verification and validation requirements | 30 min | NG |
| PM | 5 | Practice on CalcApp — V&V v0.3 | 45 min | TS |

### Day 4 (April 17) — Iterative and Incremental Improvement

| Half | Step | Content | Duration | Trainer |
|------|------|---------|----------|---------|
| AM | 1 | CalcApp Next Version Objectives | 30 min | NG+TS |
| AM | 2 | CalcApp v0.4 Iteration Part 1 | 60 min | TS |
| AM | 3 | Break | 15 min | |
| AM | 4 | CalcApp v0.4 Iteration continued | 90 min | TS |
| PM | 1 | CalcApp v0.5 Objectives | 30 min | NG+TS |
| PM | 2 | CalcApp v0.5 Iteration Part 1 | 60 min | TS |
| PM | 3 | Break | 15 min | |
| PM | 4 | CalcApp v0.5 Iteration continued | 90 min | TS |
| PM | 5 | Debrief | 15 min | NG+TS |

### Day 5 (April 23) — Professional Project and Synthesis

| Half | Step | Content | Duration | Trainer |
|------|------|---------|----------|---------|
| AM | 1-2 | Professional mini-project Presentation & start | 90 min | NG+TS |
| AM | 3 | Break | 15 min | |
| AM | 4 | Professional mini-project continued | 90 min | TS |
| PM | 1-2 | Professional mini-project continued | 90 min | TS |
| PM | 3 | Break | 15 min | |
| PM | 4 | Professional mini-project continued | 90 min | TS |

### Day 6 (April 24) — Project Closure, Ethics & Discussion

| Half | Step | Content | Duration | Trainer |
|------|------|---------|----------|---------|
| AM | 1-2 | Professional mini-project continued | 90 min | TS |
| AM | 3 | Break | 15 min | |
| AM | 4 | Professional mini-project continued | 90 min | TS |
| PM | 1-2 | Professional mini-project continued | 90 min | TS |
| PM | 3 | Break | 15 min | |
| PM | 4 | Demo of Advanced SE with Claude | 60 min | NG |
| PM | 5 | Training Closure | 30 min | NG+TS |

---

## 3. Source Document — LaTeX SOTA Structure

**Document**: `sota-ai-4-se-EN.tex` — "State of the Art: Methodological Approaches for Generative AI-Driven Software Engineering"
**Size**: 3,356 lines + 1,884 lines bibliography
**Date**: February 2026

### Section-to-Module Mapping

| SOTA Section | Lines | Feeds Into | Module |
|---|---|---|---|
| S1: Introduction | 170-237 | Day 1 opening | `ai4se6d_genai_intro` |
| S2: Foundations of GenAI | 239-410 | Day 1 AM | `ai4se6d_genai_intro` |
| S3: GenAI in SE Foundations | 412-488 | Day 1 AM | `ai4se6d_genai_intro` (coverage/capabilities/autonomy) |
| S4: SDLC Transformation | 490-597 | Day 1 AM + Day 3 | `ai4se6d_vibecoding` (VibeCoding/VibeEng) + Day 3 RE/Testing |
| S5: Methodological Frameworks | 599-761 | Day 3 | Future module (GenSEM, AgileGen, SE 3.0) |
| S6: Empirical Evidence | 764-828 | Day 1 (stats in vibecoding) | `ai4se6d_vibecoding` (danger stats, evidence) |
| S7: Risks | 831-889 | Day 1 (dangers) + Day 6 ethics | `ai4se6d_vibecoding` (Act II) + Day 6 closing |
| S8: Human Factor | 891-928 | Day 3 + Day 6 | Future modules |
| S9: Dev Environments | 931-1871 | Day 1 (tools overview) + Day 2 (deep Cursor) | `ai4se6d_vibecoding` (Act IV) + TS Day 2 |
| S10: Roadmaps | 1874-1905 | Day 6 closing | Future module |
| S11: Synthesis | 1908-1970 | Day 6 closing | Future module |
| App A: Compound Engineering | 1985-2791 | Day 6 demo | Advanced SE demo |
| App B: Terminology | 2794-3105 | All days | Glossaries |
| App C: Multi-Agent Landscape | 3108-3266 | Day 2 + Day 6 | Advanced topics |

### Key Statistics Registry

All statistics used across training modules should trace back to these sources:

| Stat | Value | Source | Bib key | Used in vibecoding? |
|------|-------|--------|---------|---------------------|
| Developer AI adoption | 84% | Stack Overflow 2025 | `stackoverflow-survey2025` | Yes (recap) — **missing cite** |
| Daily AI tool usage | 51% | Stack Overflow 2025 | `stackoverflow-survey2025` | No |
| Copilot productivity gain | +55.8% | Peng et al. 2023 | `peng-copilot2023` | No |
| Largest RCT gain | +26% | Cui et al. 2024 | `cui-fieldexperiments2024` | No |
| Counter-evidence | -19% slower | METR 2025 | `metr2025` | No |
| AI paradox lost time | 7h/week | GitLab 2025 | `gitlab-devsecops2025` | Yes — **cited in dedicated block** |
| Vulnerability rates | 12-65% | Basic & Giaretta SLR | `basic-codesecurity-slr2025` | Yes — **cited** |
| Package hallucinations | 5.2-21.7% | Spracklen et al. | `spracklen-packages2025` | Yes — **cited** |
| Structured SE improvement | 15% Pass@1 | FlowGen/SOEN101 | `soen101-2024` | Yes — **cited** |
| Work AI-integrable | 60% | Anthropic 2026 | `anthropic-agentic2026` | Yes (reality) |
| Fully delegable | 0-20% | Anthropic 2026 | `anthropic-agentic2026` | Yes (reality) |
| Cursor valuation | $29.3B | cursor-ainative2025 | `cursor-ainative2025` | Yes — **missing REF** |
| Cursor DAU | 1M+ | cursor-ainative2025 | `cursor-ainative2025` | Yes — **missing REF** |
| Windsurf devs | 800K+ | windsurf-cascade2025 | `windsurf-cascade2025` | Yes — **missing REF** |
| Copilot devs | 20M+ | copilot-plans2025 | `copilot-plans2025` | Yes — **missing REF** |
| MCP servers | 16,670+ | mcp-registry2025 | `mcp-registry2025` | Yes — **missing REF** |

---

## 4. Practicals Analysis — Tiago's Materials

### Available Slides

| Day | File | Pages | Content |
|-----|------|-------|---------|
| Day 1 | `01_tools_ecosystem.pdf` | 42 | Autonomy spectrum, tool comparison (Copilot, Cursor, Claude Code, Windsurf, Codex, Local LLMs) |
| Day 1 | `02_installation_and_configuration.pdf` | 21 | Cursor install, core loop, FreeSelfApp workshop |
| Day 2 | Full deck | 234 | Advanced Cursor, TDD, CalcApp v0.1-v0.2, code review, living docs, Git |
| Day 5 | Mini-project deck | 24 | VibeEngineering recap, mini-project launch (5 suggested domains) |
| Day 3-4 | **MISSING** | — | Likely RE + CalcApp v0.3/v0.4/v0.5 (inferred from schedule + branches) |

### CalcApp Branch Progression

| Branch | Session | Content | SE Concepts |
|--------|---------|---------|-------------|
| `v0-plans` | Day 2 start | Planning docs only, no code | "Plan before you code" |
| `v1-skeleton` | Day 2 | CRUD with TDD, routing, localStorage | TDD, scaffolding, AI-TDD |
| `v2-requirements` | Day 3 | Edit/delete, categories, search, sort, monthly summary | Functional requirements, acceptance criteria, V&V |
| `v3-architecture` | Day 4 Iter 2 | Feature-based folder layout, useReducer, StorageService interface | Architecture patterns, separation of concerns |
| `v4-features` | Day 4 Iter 3 | Theme toggle, multi-currency (API), budgets, charts, date filtering, recurring expenses | Advanced features, API integration |
| `v5-production` | Day 4 Iter 4 | ESLint+Prettier, accessibility tests, Playwright E2E, PWA, CSV export, CI pipeline | Production readiness, quality, deployment |

### NG ↔ TS Content Overlap Analysis

| Topic | NG Module | TS Slides | Overlap Risk |
|-------|-----------|-----------|-------------|
| Autonomy spectrum (5 levels) | `ai4se6d_vibecoding` Act IV | `01_tools_ecosystem.pdf` | **HIGH** — near-identical content |
| Cursor features | `ai4se6d_vibecoding` bck_ide_cursor | `01_tools_ecosystem.pdf` + Day 2 full deck | **HIGH** — NG gives overview, TS goes deep |
| Claude Code features | `ai4se6d_vibecoding` bck_ide_claude_code | `01_tools_ecosystem.pdf` | **MEDIUM** — NG has more detail |
| Tool comparison matrix | `ai4se6d_vibecoding` bck_ide_comparison | `01_tools_ecosystem.pdf` | **HIGH** — similar tables |
| MCP protocol | `ai4se6d_vibecoding` bck_ide_mcp | Day 2 deck (MCP section) | **MEDIUM** — NG introduces, TS demos |
| VibeCoding definition | `ai4se6d_vibecoding` Act I | Day 5 recap only | **LOW** — NG owns this topic |
| VibeCoding dangers | `ai4se6d_vibecoding` Act II | Not in TS slides | **NONE** — NG only |
| VibeEngineering principles | `ai4se6d_vibecoding` Act III | Day 5 recap | **LOW** — NG owns, TS references |
| TDD | `ai4se6d_vibecoding` bck_vibeeng_p_tdd (principle only) | Day 2 deck (60+ pages) | **LOW** — NG states principle, TS teaches practice |

---

## 5. Key Terminology — Master Glossary

| Term | LaTeX Definition | Module Coverage |
|------|-----------------|-----------------|
| **VibeCoding** | Developers describe tasks to LLMs, accept code without close review. Coined by Karpathy (Feb 2025). Collins Word of the Year 2025. | `ai4se6d_vibecoding` Act I |
| **VibeEngineering** | Evolution reintroducing systematic SE discipline: requirements, TDD, architecture, review. | `ai4se6d_vibecoding` Act III |
| **Context Engineering** | Systematically managing information fed to AI: project rules, memory, tools, relevant code. Replaces "prompt engineering." | `ai4se6d_vibecoding` P6 |
| **CHOP** | Chat-Oriented Programming — multi-turn conversational interaction with LLMs | Not explicitly in current modules |
| **SE 3.0** | Hassan et al.'s AI-native SE vision: intent-centric, conversation-oriented, adaptive partnership | Not in current modules (Day 3?) |
| **Promptware Engineering** | Chen et al.'s framework: SE principles applied to prompt lifecycle | Not in current modules |
| **Agentic DevOps** | Microsoft's vision: intelligent agents across every lifecycle stage | Not in current modules |
| **V-Bounce Model** | AI-native SDLC: humans validate, AI implements | Not in current modules |
| **ACI** | Agent-Computer Interface: AI agents interact through tool use | Not explicitly named |
| **MCP** | Model Context Protocol: open protocol connecting AI agents to external tools | `ai4se6d_vibecoding` bck_ide_mcp |
| **AGENTS.md** | Proposed standard for tool-agnostic project rules | Not in current modules |
| **GenSEM** | Generative Software Engineering Methods (NG's term for Day 3) | Future Day 3 module |
| **Package Hallucinations** | LLMs generating references to non-existent packages (supply-chain risk) | `ai4se6d_vibecoding` bck_vibecoding_danger_halluc |
| **AI Paradox** | Faster coding creates new bottlenecks; 7h/week lost | `ai4se6d_vibecoding` bck_vibecoding_danger_paradox |
| **Homogenization Effect** | AI-generated solutions converge toward similar patterns | Not in current modules |

---

## 6. Design Constraints for ai4se6d_vibecoding

Based on this consolidated context, the following constraints apply:

### Timing
- **Allocated slot**: 45 min (schedule step 5, 11:00-11:45)
- **Current module**: ~65 slides, ~70 min — **25 min over budget**
- **Implication**: Either negotiate more time, or cut ~15-20 slides

### Content Boundaries with Tiago
- **NG should NOT deep-dive into tools** — Tiago covers this thoroughly in the afternoon (Day 1) and all Day 2
- **NG should own**: VibeCoding concept, dangers, VibeEngineering principles, evidence
- **Shared zone**: Autonomy spectrum, tool overview — agree who does what
- **NG should NOT demo Cursor** — Tiago does this in PM with 60-min install + 1h45 FreeSelfApp

### Exercise Alignment
- **Exercise 2 (Pure VibeCoding)** in module vs **FreeSelfApp workshop** in PM:
  - If FreeSelfApp IS the VibeCoding exercise → Exercise 2 in module should be a brief intro/framing only, not a standalone 10-min exercise
  - If Exercise 2 is separate → it competes with FreeSelfApp time
- **Exercise 3 (VibeEngineering redo)** — there is NO equivalent in Tiago's Day 1 schedule. This exercise could work as the debrief framing (PM step 5, 30 min)

### Source Alignment
- All statistics MUST trace to the LaTeX SOTA bib entries
- The SOTA uses specific bib keys — modules should use the same keys for `cite()` calls
- Tool-specific claims (valuations, user counts) come from SOTA Section 9 — add `# REF:` with bib keys

---

## 7. Recommendations for Review Report Update

Based on this analysis, the following review findings should be **upgraded or reframed**:

| Finding | Original | Updated Assessment |
|---------|----------|-------------------|
| P6 (Act IV disconnected) | MAJOR | **CRITICAL** — Act IV (8 slides on tools) heavily overlaps with Tiago's `01_tools_ecosystem.pdf` (42 pages). Risk of boring repetition. |
| A3 (Cursor not introduced) | MAJOR | **Resolved by context** — Tiago introduces Cursor in the PM. But NG's module comes first, so a brief mention is still needed. |
| A4 (Exercise 3 too short) | MAJOR | **Reframe** — Exercise 3 may not belong in this module at all if the PM FreeSelfApp serves as the practical. Consider making Exercise 3 a framing for the debrief instead. |
| P1 (No learning objectives) | CRITICAL | **Confirmed CRITICAL** — The official program has explicit learning outcomes. The module should state them. |
| E5-E13 (Unsourced tool stats) | MAJOR | **Easy fix** — All stats come from SOTA S9. Bib keys identified: `cursor-ainative2025`, `windsurf-cascade2025`, `copilot-plans2025`, `mcp-registry2025` |
| A2 (Exercise 2 = no Exercise 1) | CRITICAL | **Reframe** — Exercise 1 is in `ai4se6d_genai_intro`. The numbering is correct across the training day, not just this module. Add a brief reference. |

### New Finding (from context analysis)

| # | Severity | Description | Impact |
|---|----------|-------------|--------|
| NEW-1 | **CRITICAL** | **Module duration (~70 min) exceeds allocated slot (45 min) by 25 min.** The schedule gives VibeCoding 45 min, Tools 45 min (shared with Tiago). Current 65 slides cannot fit. | Must cut or restructure |
| NEW-2 | **CRITICAL** | **Act IV (Tools) heavily duplicates Tiago's 42-page tool ecosystem deck.** Risk of boring the audience with near-identical autonomy spectrum, tool comparison, and Cursor details. | Reduce Act IV to 1-2 slides max |
| NEW-3 | **MAJOR** | **Exercise 2 (10 min VibeCoding) is redundant with FreeSelfApp (1h45).** Both are "naive VibeCoding" activities. | Convert Exercise 2 to a framing/teaser for the PM workshop |
