---
title: Anti-scroll pattern for multi-slide blocks
category: process
scope: collection
origin: ai4se6d_gensem
tags: [slide-break, scroll, navigation, multi-slide, pagination]
---

## Context

When a block contains multiple slides via `st_slide_break()`, navigating to that block from the sidebar or markers auto-scrolls to the 2nd slide instead of staying on the 1st.

## Problem

The paginated book needs an anchor point (TOC marker) at the very top of a block. Without it, the scroll target lands on the first `st_slide_break()` marker, which is between slide 1 and slide 2 — causing the view to show slide 2.

**Symptoms**: clicking a sidebar entry jumps to the wrong slide; the first slide of a multi-slide block is never visible when navigating via markers.

**Root cause**: no TOC marker declared before the first content in the block.

## Solution

Declare a marker BEFORE the first visible content using one of two equivalent patterns:

### Pattern A — Invisible marker via `st_slide_break`

```python
def build():
    st_slide_break(marker_label="Section Title")

    # First sub-slide
    with st_block(_page_fill):
        st_write(bs.heading, "Slide 1", tag=t.div, toc_lvl="+1")
        # ...

    st_slide_break()

    # Second sub-slide
    with st_block(_page_fill):
        st_write(bs.heading, "Slide 2", tag=t.div, toc_lvl="+1")
        # ...
```

### Pattern B — Visible marker via `st_write`

```python
def build():
    st_write(bs.heading, "Section Title", tag=t.div, toc_lvl="1", marker=True)

    # First sub-slide
    with st_block(_page_fill):
        st_write(bs.heading, "Slide 1", tag=t.div, toc_lvl="+1")
        # ...

    st_slide_break()
    # ...
```

**Pattern A** is preferred when the marker text would duplicate the first slide title.

### Key rules

- Sub-slides use `toc_lvl="+1"` (relative) for proper TOC hierarchy
- Do NOT use `st_space("v", "30vh")` before `st_slide_break()` — this was a wrong approach that does not reliably fix the issue
- Each sub-slide wraps its content in its own `with st_block(_page_fill):` context
- `st_slide_break()` is called OUTSIDE the `st_block` context, never inside

## Prevention

Every multi-slide block must start with either `st_slide_break(marker_label=...)` or `st_write(..., marker=True)` before the first visible content.

## References

- Working example: `ai4se6d_vibecoding/blocks/bck_intro_review_habits.py`
- Fixed blocks: `ai4se6d_gensem/blocks/bck_gensem_sdlc_15tasks.py`, `bck_gensem_sdlc_orchestrator.py`, `bck_gensem_sdlc_paradigms.py`
