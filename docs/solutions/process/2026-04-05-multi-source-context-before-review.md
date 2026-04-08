---
title: Collect multi-source context before running a review
category: process
scope: collection
origin: ai4se6d_vibecoding review cycle (2026-04-04-05)
tags: [CE, review, context, sources, schedule, co-trainer, alignment]
---

## Context

The initial 5-perspective review of ai4se6d_vibecoding produced findings that were later reframed or dismissed after a source analysis (`/stx-ce:task`) revealed the broader training context: the schedule gave only 45 min (not 70), Tiago's slides duplicated Act IV content, and the PM FreeSelfApp workshop made Exercise 2 redundant.

## Problem

Without external context, the review:
- Flagged Act IV as "pedagogically disconnected" (MAJOR) — it was actually duplicating the co-trainer's deck (CRITICAL)
- Suggested expanding exercises — they were redundant with PM activities
- Missed the timing constraint (45 min vs 70 min actual)
- Suggested adding interaction points that already existed in the PM schedule

5 findings were reframed after context analysis. 2 were upgraded, 3 downgraded.

## Solution

**Before running `/stx-ce:review`, collect the training context with `/stx-ce:collect` or `/stx-ce:task` (source analysis):**

1. Official program (learning outcomes, session descriptions)
2. Schedule with precise timings per slot
3. Co-trainer materials (slides, exercises) — identify overlap zones
4. Case study structure (branches, iterations)
5. Previous module content (to check continuity)

Store in `docs/collect/` as a consolidated analysis document.

The review agents should receive this context to:
- Evaluate content against the allocated time (not just slide count)
- Identify duplication with co-trainer materials
- Assess exercises against the full-day schedule (not just this module)

## Update 2026-04-08: Cross-module 5-axis review methodology

The context analysis approach was extended into a full **5-axis cross-module review**:

1. **Inter-module coherence** — common terms defined consistently across modules (glossary, definitions)
2. **KBSCI alignment** — stats, definitions, bibkeys match the reference SOTA document
3. **Co-trainer alignment** — overlaps with practical slides identified and classified
4. **Temporal coherence** — content fits allocated time slots in the schedule
5. **Program completeness** — all program items covered by at least one module

### Method

- Launch parallel agents to inventory each module (blocks, terms, stats, exercises) and each source (KBSCI, co-trainer slides)
- Cross-reference definitions, stats, and bibkeys across all inventories
- Produce a unified review report with findings by axis, severity, and effort
- Create an errata registry for reference document errors (`docs/reviews/YYYY-MM-DD-kbsci-errata.md`)

### Reference

- `docs/reviews/2026-04-08-cross-module-review.md` (review report)
- `docs/reviews/2026-04-08-kbsci-errata.md` (errata registry)

## Applies when

Any module that is part of a multi-trainer, multi-day training program. Single-module standalone presentations can skip this.
