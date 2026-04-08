---
title: Web-verified statistics workflow
category: content
scope: generic
origin: ai4se6d cross-module review (2026-04-08)
tags: [statistics, verification, bibliography, errata, web-sources]
---

## Context

During the cross-module review, the StackOverflow survey stats cited in the modules (76%/63%/82%) contradicted those in the KBSCI reference document (84%/51%). The trainer verified directly on the website and confirmed the module figures were correct — the KBSCI was wrong.

## Problem

- Reference documents (LaTeX SOTA, papers) may contain transcription errors for statistics
- Using unverified numbers from a reference document propagates errors into training materials
- Different survey editions (2024 vs 2025) were mixed, creating contradictions in the same training day

## Solution

### Before using any quantitative claim in slides:

1. **Go to the source website** and verify the exact number
2. **Record the URL and consultation date** in the `.bib` entry (`note` field)
3. **Use the consultation year** as the bibkey year convention (e.g., `stackoverflow-survey2026` for a page consulted in April 2026)

### When a reference document has wrong numbers:

1. **Create an errata file**: `docs/reviews/YYYY-MM-DD-<source>-errata.md`
2. **Log each discrepancy** with: section, claim in source, correct value, verification source, status
3. **Apply correct values** in the training modules immediately
4. **Schedule correction** of the reference document separately

### .bib entry template for web sources

```bibtex
@misc{stackoverflow-survey2026,
    title   = {Stack Overflow Developer Survey --- AI},
    author  = {{Stack Overflow}},
    year    = {2026},
    url     = {https://survey.stackoverflow.co/2024/ai},
    note    = {76\% use or plan to use AI tools. Consulted April 2026.},
}
```

## Applies when

Any training content citing quantitative statistics from web-accessible surveys or reports.
