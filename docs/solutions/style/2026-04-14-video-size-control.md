---
title: Video size control via grid wrapper
category: style
scope: collection
origin: ai4se6d_gensem
tags: [video, sizing, grid, layout, st_video]
---

## Context

`st_video()` wraps `st.video()` which does not accept a `width` parameter. The video takes the full container width by default.

## Problem

No direct way to reduce the video display size. `st_zoom()` scales visually but the container remains full-width.

## Solution

Wrap the video in a 3-column grid where the center column controls the width:

```python
# Video at 50% width, centered
with st_grid(cols="1fr 2fr 1fr", gap="0px") as g:
    with g.cell():
        pass
    with g.cell():
        st_video(path, autoplay=True, loop=True)
    with g.cell():
        pass
```

Adjust column ratios for different sizes:
- `"1fr 2fr 1fr"` → 50% width
- `"1fr 1fr 1fr"` → 33% width
- `"1fr 3fr 1fr"` → 60% width

## Prevention

Document this technique in design guideline when video is used.

## References

- Applied in: `ai4se6d_gensem/blocks/bck_gensem_sdlc_title.py`
