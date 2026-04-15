## Slide Break Navigation — Migration Guide

### What changed

The `SlideBreakConfig` now has a `marker_hidden` parameter that controls whether slide break markers appear in the floating marker popup. Previously, all slide break markers were always hidden (counter only).

Additionally, the sidebar "Style" selectbox now reflects the actual configured mode (including "Hidden" and "Marker only") and `auto_marker_on_toc` can be set to `0` to avoid duplicate navigation stops.

### New parameters

**In `SlideBreakConfig` (global, in `book.py`):**
```python
marker_hidden: bool = True   # default: backward-compatible (hidden)
```

**In `st_slide_break()` (per-call override):**
```python
marker_hidden: Optional[bool] = None  # None = use config default
```

Priority: `st_slide_break(marker_hidden=...)` > `SlideBreakConfig.marker_hidden` > default `True`.

### Migration for existing presentation projects

**Step 1 — `book.py` configuration:**

```python
set_slide_break_config(SlideBreakConfig(
    mode=SlideBreakMode.FULL,        # or any mode you need
    space="1vh",
    rule_margin_top="1vh",
    rule_margin_bottom="1vh",
    marker_hidden=False,             # markers visible in popup
))

marker_config = MarkerConfig(
    auto_marker_on_toc=0,            # disable TOC-based markers
    next_keys=["PageDown", "ArrowRight"],
    prev_keys=["PageUp", "ArrowLeft"],
)
```

**Step 2 — Label every `st_slide_break()` call:**

Every `st_slide_break()` must have a `marker_label`. The label is what appears in the marker popup.

```python
# BEFORE (unlabeled — creates a marker with no meaningful name)
st_slide_break()

# AFTER (labeled — appears as "Five Developer Surveys" in popup)
st_slide_break(marker_label="Five Developer Surveys")
```

**Step 3 — Add `st_marker()` to single-slide blocks:**

Blocks without any `st_slide_break()` need an explicit marker at the top of `build()`:

```python
def build():
    st_marker("The Productivity Paradox")   # visible by default
    with st_block(...):
        ...
```

**Step 4 — Clear the cache:**

```bash
rm -rf .streamlit/.stx_cache/
```

### Result

- **ArrowRight** = next slide (1 press = 1 slide, no duplicates)
- **Marker popup** = shows all slide labels (clickable navigation)
- **Sidebar TOC** = unchanged (`toc_lvl` still feeds the table of contents)
- **Sidebar Style** = reflects the actual mode, changeable at runtime

### Per-call override example

```python
# This specific break is a silent transition (not in popup)
st_slide_break(marker_label="transition", marker_hidden=True)
```
