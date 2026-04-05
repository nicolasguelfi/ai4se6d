---
title: Intermediate font sizes are valid in maximize-viewport
category: guidelines
scope: collection
origin: ai4se6d_vibecoding review discussion (2026-04-05)
tags: [maximize-viewport, font-size, hierarchy, pt36, LARGE]
---

## Context

The maximize-viewport guideline declared a fixed font hierarchy (GIANT/Giant/Huge/huge/Large/large/big). A review finding flagged `pt36` and `s.LARGE` as violations because they weren't in the list.

## Problem

The hierarchy was interpreted as exclusive — only listed sizes are allowed. This is incorrect. StreamTeX provides a full range of sizes (`s.text.sizes.pt<N>`), and intermediate values serve legitimate purposes.

## Solution

The guideline was updated (`.claude/custom/references/design-guideline-maximize-viewport.md`) to include:

### Named sizes (primary)
GIANT (196pt), Giant (128pt), Huge (96pt), huge (80pt), Large (48pt), large (32pt), big (24pt)

### Intermediate sizes
When a named size doesn't fit, use any `s.text.sizes.pt<N>`. Common intermediates:
- `pt36` — dense table cells (between large 32pt and Large 48pt)
- `s.LARGE` (~64pt) — emphasized inline labels (between Large 48pt and huge 80pt)

Minimum projection-safe size remains 24pt (`s.big`).

## Applies when

Reviewing blocks for font size compliance. Do NOT flag intermediate sizes as violations if they serve the visual context.
