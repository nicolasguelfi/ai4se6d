---
title: AI prompt orientation convention
category: assets
scope: collection
origin: AI4SE-NG (migrated 2026-03-31)
date: 2026-03-30
tags: [ai-images, prompt, portrait, landscape, orientation, suffix]
---

## Context

During production of AI4SE-NG, AI-generated images in balanced slides (40% column) were initially landscape (16:9). They left vertical gaps and didn't fill the column well.

## Problem

The `_SUFFIX` of all image prompts contained `"16:9 aspect ratio"`, which instructed the AI model to generate landscape images regardless of the `ai_size` parameter. Even with `ai_size="1024x1536"` (portrait dimensions), the generated content was composed for landscape if the prompt said "16:9".

## Solution

The `_SUFFIX` must explicitly match the intended orientation:

### For balanced slides (portrait)

```python
_SUFFIX = "No text, no letters, no words, no labels, no watermarks. 2:3 portrait aspect ratio. Dark background #1A1A2E."
```

With `ai_size="1024x1536"`.

### For image-dominant slides (landscape)

```python
_SUFFIX = "No text, no letters, no words, no labels, no watermarks. 16:9 aspect ratio. Dark background #1A1A2E."
```

With `ai_size="1536x1024"`.

### Key insight

The `_PREFIX` (style, colors, aesthetic) stays identical for both. Only the `_SUFFIX` changes the orientation instruction. The `ai_size` parameter controls the output dimensions, but the prompt text controls the composition — both must agree.

## Anti-pattern

Generating with `ai_size="1024x1536"` but `_SUFFIX` saying `"16:9 aspect ratio"` produces an image with portrait dimensions but landscape composition (content squeezed horizontally, empty space vertically).

## Applicability

Any StreamTeX project using AI-generated images with the master prompt pattern (`_PREFIX` + specific + `_SUFFIX`).
