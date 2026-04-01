---
title: "Pattern: stat-hero — giant statistic with context"
category: guidelines
scope: collection
origin: ai4se6d (2026-04-01)
tags: [pattern, visual, statistics, keynote, hero]
---

## Pattern: stat-hero

A large statistic displayed prominently (96pt, highlight color) with supporting context below. Classic keynote/TED pattern for memorable data points.

## Layout

- Statistic: `s.Giant + s.bold + s.project.colors.highlight`, centered
- Context: `s.Large`, centered, below the stat
- Optional: source attribution in `s.project.titles.caption`

## Code

```python
class BlockStyles:
    stat = Style.create(s.Giant + s.bold + s.project.colors.highlight + s.center_txt, "my_stat")
    context = Style.create(s.Large + s.center_txt, "my_context")
    source = s.project.titles.caption + s.center_txt

def build():
    with st_block(_page_fill_center):
        st_write(bs.stat, "84%", tag=t.div)
        st_space("v", 1)
        st_write(bs.context, "of developers use or plan to use AI tools")
        st_write(bs.source, "Stack Overflow 2025")
```

## Reference blocks

- `ai4se6d_genai_intro/blocks/bck_poll_ai_result.py`
- `ai4se6d_vibecoding/blocks/bck_vibecoding_reality.py`

## Applicability

Any presentation with impactful statistics. Should be a standard blueprint.
