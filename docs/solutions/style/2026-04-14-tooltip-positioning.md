---
title: Tooltip positioning defaults to center
category: style
scope: collection
origin: ai4se6d_gensem
tags: [tooltip, positioning, hover, clipping]
---

## Context

`st_hover_tooltip()` has a `position` parameter that controls where the panel opens relative to the icon.

## Problem

Using `position="left"` when the icon is on the right side of the viewport causes the panel to be clipped (extends beyond viewport edge). Same issue with `position="right"` when icon is on the left.

**Symptom**: tooltip panel partially hidden, text cut off.

## Solution

- Default to `position="center"` — the panel centers under the icon, safe for any position
- Use `position="right"` ONLY when the icon is at the far left edge of the viewport
- Use `position="left"` ONLY when the icon is at the far right edge of the viewport
- Keep `width` at `50vw` maximum to avoid clipping on narrow viewports

```python
st_hover_tooltip(
    title="...",
    entries=[...],
    scale="2vw",
    width="50vw",       # never exceed 50vw
    position="center",  # safe default
)
```

## Prevention

Design guideline R8: `position="center"` by default, `width≤50vw`.

## References

- Applied across all `ai4se6d_gensem` blocks
