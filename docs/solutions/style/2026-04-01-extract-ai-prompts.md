---
title: Extract AI image prompts to custom/prompts.py
category: style
scope: collection
origin: ai4se6d (2026-04-01)
tags: [ai-images, prompts, refactoring, duplication, graphic-line]
---

## Context

Projects using AI-generated images with a consistent graphic line (same palette, style, background) duplicate the master prompt prefix and suffix in every block file.

## Problem

The _PREFIX (5-line style description) and _SUFFIX (orientation instruction) are copy-pasted across 30+ blocks. If the palette or style changes, every file must be updated manually. Risk of divergence between blocks.

## Solution

Create `custom/prompts.py` with shared constants:

```python
AI_PREFIX = (
    "Minimalist digital illustration on a pure dark background (#1A1A2E). "
    "Flat vector style with soft gradients. ..."
)
AI_SUFFIX_PORTRAIT = "No text... 2:3 portrait aspect ratio. Dark background #1A1A2E."
AI_SUFFIX_LANDSCAPE = "No text... 16:9 aspect ratio. Dark background #1A1A2E."
```

In each block, replace local definitions with:
```python
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
```

Block-specific prompts (_PROMPT_*) remain local.

## When to apply

When a project has 5+ blocks with AI images sharing the same graphic line.

## Applicability

All StreamTeX projects using AI-generated images. Should be included in project templates.
