---
title: Standalone images must be wrapped in centered block
category: style
scope: collection
origin: ai4se6d_gensem
tags: [image, centering, layout, design-rule]
---

## Context

When a slide contains a single image as its main element, the image must be horizontally centered. This is a universal graphic design rule.

## Problem

`st_image(s.center_txt, ...)` does NOT center the image — `s.center_txt` applies `text-align: center` which only affects inline text content, not block-level image elements.

**Symptom**: image appears left-aligned despite having `s.center_txt` as style parameter.

## Solution

Wrap the image in a `st_block(s.center_txt)` container:

```python
# WRONG — image not centered
st_image(s.center_txt, width="60%", ...)

# CORRECT — image centered
with st_block(s.center_txt):
    st_image(s.none, width="60%", ...)
```

The `st_block(s.center_txt)` creates a div with `text-align: center` which centers the img element inside it.

## Prevention

Design guideline R7: when a slide contains a single image as main element, always wrap in `with st_block(s.center_txt):`.

## References

- Fixed in: `ai4se6d_gensem/blocks/bck_gensem_sdlc_orchestrator.py`
- All image-in-grid usages (`g.cell()`) center correctly because grid cells handle alignment
