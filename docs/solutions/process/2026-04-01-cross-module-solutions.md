---
title: Cross-module solutions at collection level
category: process
scope: collection
origin: ai4se6d (2026-04-01)
tags: [collection, solutions, cross-module, knowledge-sharing]
---

## Context

When a collection has 2+ modules, learnings from production may apply to one module or to all modules.

## Problem

If each module stores solutions only in its own `docs/solutions/`, generic learnings are duplicated or lost. No shared knowledge base exists across modules.

## Solution

Two-level convention:
- **`<root>/docs/solutions/`** — cross-module learnings applicable to the entire collection
- **`modules/<name>/docs/solutions/`** — module-specific learnings

### When to promote

A learning should move from module-level to collection-level when:
- Its `scope` field is `generic` (not `specific`)
- It has been reused in 2+ modules
- It describes a pattern, convention, or anti-pattern applicable to all modules

### Template collection update

The `/stx-project:collection-new` template should create `docs/solutions/` at root level with subdirectories matching the 9 CE categories.

### CE compound awareness

`/stx-ce:compound` should check both levels when searching for duplicates and propose the right level when creating new solutions.

## Applicability

All StreamTeX collections with 2+ modules.
