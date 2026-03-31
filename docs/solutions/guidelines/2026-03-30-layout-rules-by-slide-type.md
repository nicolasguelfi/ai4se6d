---
title: Layout rules by slide type
category: guidelines
scope: collection
origin: AI4SE-NG (migrated 2026-03-31)
date: 2026-03-30
tags: [justify-content, billboard, balanced, image-orientation, portrait, landscape]
---

## Context

During production of AI4SE-NG (auditorium presentation, 16:9 dark theme), two layout rules emerged that were not in the initial maximize-viewport guideline.

## Problem

All slides initially used `justify-content: center`, which worked for billboard slides (single title/question) but pushed content slides down, wasting top space and making bullet lists harder to read at distance.

Similarly, all AI images used landscape `1536x1024` (16:9), but in balanced slides (40% image column), landscape images left large vertical gaps while the text column filled the height.

## Solution

### Rule 1: justify-content by slide type

- **Billboard / transition slides** (single large title or question, no other content): `justify-content: center`
- **All other slides** (content, balanced, lists, grids): `justify-content: flex-start`

### Rule 2: AI image orientation by slide type

- **Balanced slides** (image in 40% column): `ai_size="1024x1536"` portrait, `_SUFFIX` includes `"2:3 portrait aspect ratio"`
- **Image-dominant slides** (full-width image): `ai_size="1536x1024"` landscape, `_SUFFIX` includes `"16:9 aspect ratio"`

## Where documented

Both rules are in `custom/design-guideline.md` under `## Layout Rules`.

## Applicability

These rules apply to any StreamTeX presentation using the maximize-viewport guideline with a mix of billboard and content slides.
