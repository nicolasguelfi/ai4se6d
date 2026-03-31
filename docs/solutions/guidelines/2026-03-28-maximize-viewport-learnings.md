---
title: Maximize Viewport — Production Learnings
category: guidelines
scope: collection
origin: AI4SE-NG (migrated 2026-03-31)
date: 2026-03-28
tags: [maximize-viewport, centering, grids, images, slide-breaks, icons]
---

# Maximize Viewport — Production Learnings

Learnings from first production cycle applying the `maximize-viewport` guideline
to the AI4SE-NG presentation (16 slides, Block 1).

## Learnings Capitalized

### 1. Content centering requires container wrapper (P4)

**Problem**: `st_write(s.center_txt, "text")` and `st_image(s.center_txt, ...)` don't
center content because the style applies to the element, not its parent container.

**Solution**: Wrap ALL slide content in `st_block(s.center_txt)` inside the page-fill block.
This is now P4 in the guideline and the standard slide template.

### 2. Grid cell styling must use cell_styles + g.cell()

**Problem**: Using `st_block()` as cell wrapper inside grids breaks vertical centering
due to extra Streamlit DOM layers.

**Solution**: Always pass visual styling via `cell_styles=` parameter on `st_grid`,
use `g.cell()` context manager, include `vertical_center_layout + center_txt` in cell style.
Documented as Rule 12 in `slide-design-rules.md`.

### 3. Slide break spacing must be configured

**Problem**: Default `st_slide_break` space is `80vh` — way too much for paginated presentations.

**Solution**: Configure globally in `book.py`:
```python
set_slide_break_config(SlideBreakConfig(mode=SlideBreakMode.HIDDEN, space="5vh"))
```
Added to guideline "Recommended book.py Configuration".

### 4. Icons and logos use viewport-relative units

**Problem**: Pixel-sized icons (`width="75px"`) don't scale across different screen sizes.

**Solution**: Use `width="5vw"` for small icons, `width="10vw"` for medium logos.
Added to guideline "Icon and Logo Sizing" section.

### 5. AI image sizes must match model capabilities

**Problem**: `1792x1024` is a DALL-E 3 size rejected by `gpt-image-1`.

**Solution**: ModelCapabilities system added to lib — validates and auto-corrects sizes.
Valid for gpt-image-1: `1024x1024`, `1536x1024`, `1024x1536`, `auto`.

### 6. Image editor name bug

**Problem**: `_save_managed_image` used wrong operator precedence for `img_name`,
saving all images as `ai_image.png` instead of the block's `name`.

**Solution**: Fixed parenthesization: `name or (fallback if uri else "ai_image")`.

## Files Updated

- `maximize-viewport.md` — Added P4 (centering), slide template, icon sizing, anti-patterns
- `slide-design-rules.md` — Added Rule 7 image centering, Rule 12 grid checklist, Rule 13 column calibration
- `custom/design-guideline.md` — Added `table-roadmap` pattern
- `image_editor.py` — Fixed name bug, added Display tab
- `ai/capabilities.py` — New ModelCapabilities system
