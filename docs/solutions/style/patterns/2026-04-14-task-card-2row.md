---
title: "Pattern: task-card-2row — Task card with header and description"
category: style/patterns
scope: collection
origin: ai4se6d_gensem
tags: [pattern, grid, card, task, responsive, 2-row]
---

## Context

Presenting a list of tasks/features as responsive cards where each card needs a clear title and description, visually separated.

## Pattern: task-card-2row

A responsive grid of cards where each card has:
- **Row 1 (header)**: stronger background color + task ID + name
- **Row 2 (description)**: lighter background + description text

### Layout

```python
_cell = s.project.containers.cell_active_bg + s.center_txt  # outer card
_hdr = Style.create(
    s.project.containers.cell_active_bg + s.project.containers.cell_pad_sm
    + s.center_txt + Style("background-color: rgba(243,156,18,0.25);", "_hdr_bg"),
    "task_hdr",
)
_desc = s.project.containers.cell_pad_sm + s.center_txt

with st_grid(
    cols="repeat(auto-fit, minmax(350px, 1fr))",
    gap="16px",
    cell_styles=_cell,
) as g:
    for tid, name, desc in tasks:
        with g.cell():
            with st_block(_hdr):
                st_write(body, (label, f"{tid}  "), (body, name))
            with st_block(_desc):
                st_write(body, desc)
```

### Styles

- Outer cell: category-colored background (active/accent/primary) + center text
- Header block: same category color but 2-3x stronger opacity (0.25 vs 0.08)
- Description block: padding only, inherits outer cell background
- Font: `s.Large` for both rows
- Grid: `minmax(350px, 1fr)` ensures cards never get too narrow

### Variants

- **Color per category**: amber (active_bg) for NEW, teal (accent_bg) for ELEVATED, blue (primary_bg) for TRANSFORMED
- **Emoji prefix**: `🛡️` before task ID for GenAI-specific tasks

### Reference block

`ai4se6d_gensem/blocks/bck_gensem_sdlc_15tasks.py`
