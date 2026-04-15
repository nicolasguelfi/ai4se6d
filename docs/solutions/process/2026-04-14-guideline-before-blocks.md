---
title: Design guideline must be created before any block production
category: process
scope: collection
origin: ai4se6d_gensem
tags: [design-guideline, process, workflow, planning]
---

## Context

When creating a new StreamTeX module, the design guideline file (`custom/design-guideline.md`) governs all visual and structural decisions for every block.

## Problem

If blocks are produced before the guideline exists, each block makes ad-hoc design decisions (font sizes, grid types, spacing, tooltip behavior). This leads to inconsistent slides and multiple correction iterations.

In the `ai4se6d_gensem` module, the guideline was created after 3 iterations of block corrections — every issue (stat_hero abuse, non-responsive grids, tooltip clipping, missing image centering) would have been prevented by the guideline.

## Solution

The CE workflow for new modules must follow this order:

1. **Create `custom/design-guideline.md`** — choose base guideline(s), define module-specific rules
2. **Create infrastructure** — book.py, setup.py, custom/, blocks/__init__.py
3. **Produce blocks** — following the guideline rules

The guideline should specify at minimum:
- Base guideline (maximize-viewport, minimalist-visual, etc.)
- Font size table (what size for what usage, what is NEVER allowed)
- Grid rules (responsive minmax values)
- Image centering rule
- Tooltip defaults (position, width)
- Slide break pattern
- Branding assets

## Prevention

In `/stx-ce:produce`, verify that `custom/design-guideline.md` exists before creating any block. If it doesn't, create it first.

## References

- Created during: `ai4se6d_gensem` Sequence 1.1 production cycle
- Guideline file: `modules/ai4se6d_gensem/custom/design-guideline.md`
