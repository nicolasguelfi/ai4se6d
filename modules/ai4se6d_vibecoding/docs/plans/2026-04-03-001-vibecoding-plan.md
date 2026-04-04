# Production Plan — Module ai4se6d_vibecoding

## Metadata

| Field | Value |
|-------|-------|
| Project name | ai4se6d_vibecoding |
| Document type | presentation |
| Template | presentation |
| Previous plan ref | `docs/plans/2026-03-27-001-C-session1-plan.md` (Part 2 section) |
| Source document | `ul-ai-4-se/sota-ai-4-se-EN.tex` |
| Context | Day 1, Session 1 — Part 2 (45 min, after break following ai4se6d_genai_intro) |
| Training | "VibeEngineering: The Future of Software Development with Generative AI" |
| First delivery | April 9, 2026 — DLH Luxembourg |
| Date of this plan | 2026-04-03 |

---

## State of Affairs — Comparison with Original Plan

### Summary

The original plan (`2026-03-27-001-C-session1-plan.md`) covered **both** Part 1 (GenAI Intro) and Part 2 (VibeCoding/VibeEngineering) in a single document with ~128 slides across ~24 block files. The two parts have since been split into separate modules:

- **ai4se6d_genai_intro** — Part 1, 55 blocks (beta)
- **ai4se6d_vibecoding** — Part 2, 15 blocks (in progress)

### Consolidation Decisions

The original plan foresaw ~62 slides for Part 2 across ~30+ block files (slides 67-128). The implementation adopted a **denser, consolidated approach** — 15 blocks with ~26 slides. Major consolidations:

| Original Plan (block files) | Implementation | Slides (plan → actual) |
|-----|-----|-----|
| `bck_interact_review_question` + `bck_interact_review_spectrum` | **`bck_intro_review_habits`** | 2 → 4 (expanded to include AI usage spectrum) |
| `bck_vibecoding_origin` + `bck_vibecoding_definition` + `bck_vibecoding_paradigm` | **`bck_vibecoding_origin`** | 3 → 3 (merged definition + paradigm shift into origin) |
| `bck_vibecoding_intent` + `bck_vibecoding_trust` + `bck_vibecoding_conversation` + `bck_vibecoding_low_barrier` | **`bck_vibecoding_principles`** | 4 → 1 (4 principles as ordered list) |
| `bck_vibecoding_analogy` + `bck_vibecoding_compiler_trust` + `bck_vibecoding_llm_compiler` | **`bck_vibecoding_analogy`** | 3 → 2 (historical parallel + critical difference) |
| `bck_exercise_vibecoding_brief` + `_timer` + `_debrief` | **`bck_exercise_vibecoding`** | 3 → 3 (identical scope) |
| `bck_vibecoding_risk_overview` through `bck_vibecoding_risk_demo_prod` (5 slides) | **`bck_vibecoding_dangers`** | 5 → 1 (5 dangers as bullet list with stats) |
| `bck_vibecoding_stat_anthropic` + `bck_vibecoding_stat_bain` + `bck_vibecoding_naive_ok` + `bck_vibecoding_real_question` | **`bck_vibecoding_reality`** (NEW) | 4 → 2 (stats + bridge question) |
| `bck_interact_vibeeng_practices` + `bck_interact_vibeeng_transition` | **`bck_vibeeng_transition`** | 2 → 2 (identical scope) |
| `bck_vibeeng_rebranding` + 5 individual principle slides | **`bck_vibeeng_principles`** | 6 → 1 (6 principles as ordered list; added "Context Engineering" as 6th) |
| `bck_vibeeng_spectrum_overview` + 8 level slides + `bck_vibeeng_evidence` | **`bck_vibeeng_spectrum`** | 10 → 1 (4-level table with evidence) |
| `bck_exercise_vibeeng_brief` + `_timer` + `_debrief` | **`bck_exercise_vibeeng`** | 3 → 3 (identical scope) |
| `bck_ide_overview` through `bck_ide_why_cursor` (8 slides) | **`bck_ide_ecosystem`** | 8 → 5 (autonomy + 3 tool profiles + comparison) |
| `bck_recap_genai` through `bck_closing_questions` (6 slides) | **`bck_recap`** | 6 → 4 (GenAI recap + VC/VE recap + road ahead + key message) |
| *(not planned)* | **`bck_glossary`** (NEW) | 0 → 1 (19 key terms) |

### Dropped Content

The following planned slides were **dropped** (not present in any block):

| Planned Block | Reason |
|-------|--------|
| `bck_vibecoding_conductor` | "Conductor metaphor" — subsumed by role shift in `bck_vibecoding_origin` slide 3 |
| `bck_vibecoding_flow` | "Natural flow" — concept integrated into principles overview |
| `bck_vibecoding_risk_paradox` | Kept as bullet point in `bck_vibecoding_dangers` ("AI paradox: 7 hours/week") |
| Individual level "Appropriate For" slides (×4) | Merged into spectrum table's "Best For" column |

### Added Content (not in original plan)

| Block | Content |
|-------|---------|
| **`bck_glossary`** | 19-term glossary covering GenAI, LLM, VibeCoding, VibeEngineering, TDD, BDD, CI/CD, MCP, NFR, etc. |
| **`bck_vibecoding_origin` slide 1** | Added 2023 Karpathy quote ("English is the hottest new programming language") as historical precursor |
| **`bck_vibeeng_principles`** | Added **Principle 6: Context Engineering** (not in original plan which had 5 principles) |
| **`bck_intro_review_habits`** | Added AI usage percentage spectrum (0-100%) as first billboard before review habits |

---

## Current Implementation — Slide-by-Slide Reference

### Book Order (from `book.py`)

```
1.  bck_title                    (1 slide)
2.  bck_intro_review_habits      (4 slides)
3.  bck_vibecoding_origin        (3 slides)
4.  bck_vibecoding_principles    (1 slide)
5.  bck_vibecoding_analogy       (2 slides)
6.  bck_exercise_vibecoding      (3 slides)
7.  bck_vibecoding_dangers       (1 slide)
8.  bck_vibecoding_reality       (2 slides)
9.  bck_vibeeng_transition       (2 slides)
10. bck_vibeeng_principles       (1 slide)
11. bck_vibeeng_spectrum         (1 slide)
12. bck_exercise_vibeeng         (3 slides)
13. bck_ide_ecosystem            (5 slides)
14. bck_recap                    (4 slides)
15. bck_glossary                 (1 slide)
                         TOTAL: ~34 slides
```

### Narrative Arc

```
OPENING
  └── Title + Review Habits (ice-breaker, audience self-assessment)

VIBECODING — THE CONCEPT
  ├── Origin (Karpathy, definition, paradigm shift)
  ├── 4 Principles (intent, trust, conversation, low barrier)
  └── Historical Analogy (compiler parallel, critical difference)

EXERCISE 2 — PURE VIBECODING (10 min hands-on)

DANGERS OF NAIVE VIBECODING
  ├── 5 Key Risks (vulnerabilities, hallucinated deps, debt, paradox, demo vs prod)
  └── Reality Check (stats + bridge to VibeEngineering)

VIBEENGINEERING — THE DISCIPLINE
  ├── Transition (what practices remain essential?)
  ├── 6 Principles (requirements, TDD, architecture, iteration, review, context eng.)
  └── 4-Level Spectrum (naive → guided → structured → engineering)

EXERCISE 3 — REDO WITH DISCIPLINE (8 min hands-on)

IDE TOOL ECOSYSTEM
  ├── Autonomy Spectrum (5 levels)
  ├── Cursor (primary tool)
  ├── Claude Code
  ├── Windsurf + Copilot
  └── Comparison Matrix

CLOSING
  ├── GenAI Recap
  ├── VibeCoding → VibeEngineering Recap
  ├── Road Ahead (6-day preview)
  ├── Key Message: "Same Tools, Different Discipline"
  └── Glossary (19 terms)
```

---

## Block Status Assessment

| Block | Status | Quality Notes |
|-------|--------|---------------|
| `bck_title` | DONE | Hero image, proper config |
| `bck_intro_review_habits` | DONE | 4 billboards, interactive spectrum |
| `bck_vibecoding_origin` | IN PROGRESS | Has managed images (vc_origin.webp + multiple versions), Karpathy quotes + definition + paradigm shift |
| `bck_vibecoding_principles` | DONE | Clean ordered list, 4 principles |
| `bck_vibecoding_analogy` | DONE | 2 slides, compiler parallel + critical difference |
| `bck_exercise_vibecoding` | DONE | Instructions + timer + debrief |
| `bck_vibecoding_dangers` | DONE | 5 dangers with stats in grid layout |
| `bck_vibecoding_reality` | DONE | Statistics + bridge question |
| `bck_vibeeng_transition` | DONE | 2 billboards, rhetorical transition |
| `bck_vibeeng_principles` | DONE | 6 principles (added Context Engineering) |
| `bck_vibeeng_spectrum` | DONE | Table with 4 levels + FlowGen evidence |
| `bck_exercise_vibeeng` | DONE | Instructions + timer + comparison debrief |
| `bck_ide_ecosystem` | DONE | 5 slides, comprehensive ecosystem overview |
| `bck_recap` | DONE | 4-slide closing sequence |
| `bck_glossary` | DONE | 19 terms, continuous list |

---

## Remaining Work

### Priority 1 — Immediate (before April 9)

| Task | Block | Description |
|------|-------|-------------|
| P1.1 | `bck_vibecoding_origin` | Finalize managed image selection (multiple versions exist: v1-v8). Settle on final image and clean up unused versions. |
| P1.2 | All blocks | Full visual QA run-through in presentation mode (`stx run`). Check font sizes, image rendering, spacing on projector-like display. |
| P1.3 | All blocks | Verify all AI-generated images display correctly (3 images detected in `static/images/ai/`). |

### Priority 2 — Content Refinement

| Task | Block | Description |
|------|-------|-------------|
| P2.1 | `bck_vibecoding_dangers` | Consider expanding to 2 slides (currently dense with 5 stats in 1 slide). The original plan had 5 dedicated slides — 1 slide may be too compressed for auditorium delivery. |
| P2.2 | `bck_vibeeng_principles` | Consider expanding to 2 slides (6 principles in 1 slide is dense). At minimum, ensure each principle has enough visual space. |
| P2.3 | `bck_vibeeng_spectrum` | Consider expanding the table layout for auditorium readability. 4-level table may need larger fonts for projection. |
| P2.4 | `bck_vibecoding_origin` | Verify Collins English Dictionary "Word of the Year 2025" reference is accurate and up-to-date. |

### Priority 3 — Optional Enhancements

| Task | Block | Description |
|------|-------|-------------|
| P3.1 | `bck_ide_ecosystem` | Update tool stats (Cursor valuation, Copilot user count) from LaTeX source if newer data available. |
| P3.2 | `bck_recap` | Verify "Road Ahead" slide matches latest training program schedule (Days 1-6 content). |
| P3.3 | *(new block)* | Consider adding `bck_same_tools` — the "Same Tools, Different Discipline" concept (present in genai_intro) could be reinforced here. |

---

## Coordination with Source Document

The LaTeX source (`ul-ai-4-se/sota-ai-4-se-EN.tex`) is the master reference for all scientific and technical content. Key source line references used in this module:

| Content | Source Lines |
|---------|-------------|
| VibeCoding definition & origin | 524-525 |
| VibeCoding principles (4) | 528-533 |
| Historical analogy (compiler) | 540 |
| Danger: vulnerability rates | 542, 840 |
| Danger: hallucinated deps | 844 |
| Danger: tech debt | 852 |
| Danger: AI paradox | 619 |
| Anthropic finding (60%/0-20%) | 586 |
| Bain study (10% vs 25-30%) | 198, 1897 |
| VibeEngineering principles (5) | 553-557 |
| Spectrum levels | 566-580 |
| FlowGen evidence | 582 |
| Tool ecosystem | 1083-1870 |
| Autonomy spectrum | 455-461 |

**Action needed at each CE cycle**: Re-read these source lines for updates. The LaTeX source evolves and new data/references may have been added since the last production cycle.

---

## Design Configuration (inherited)

| Aspect | Choice |
|--------|--------|
| Theme | Dark (#1A1A2E) |
| Colors | #7AB8F5 / #2EC4B6 / #F39C12 / #FFFFFF |
| Image style | Flat vector, soft gradients, geometric, dark background |
| AI provider | OpenAI (gpt-image-1) |
| Default image size | 1536x1024 |
| Presentation | 16/9, paginated, hidden slide breaks |
| Typography | Projection-safe large fonts |

---

## Summary

| Metric | Original Plan (Part 2) | Current Implementation |
|--------|------------------------|----------------------|
| Block files | ~30+ | 15 |
| Total slides | ~62 | ~34 |
| Exercises | 2 (18 min) | 2 (18 min) |
| Audience questions | 2 | 2 |
| AI images | ~25 (planned) | 3+ managed images |
| Content coverage | 100% planned | ~95% (conductor metaphor + flow dropped) |
| Added content | — | Glossary, Context Engineering principle, AI usage spectrum |

The module is substantially complete. The consolidation from 62 to 34 slides reflects a design choice for **denser, faster-paced delivery** suited to 45-minute Part 2 timing. Primary remaining work is visual QA, image finalization, and considering selective expansion of the densest blocks for auditorium readability.

---

## Next Steps

1. Run `stx run` in module directory for visual QA
2. Finalize `bck_vibecoding_origin` managed image
3. Decide on P2.1-P2.3 (expand dense slides or keep compact)
4. Sync with LaTeX source for any late updates
5. Export HTML + PDF once validated
